#!/usr/bin/env python3
"""Audit a shared-gap Type II lift from the six lower-modulus F-box hits.

The lower hit supplies a finite K-supported representation a/b = -1 (mod t).
For every such representation we enumerate legal divisors m' of a+b and then
independently enumerate Type II divisors of x'=(p+m')/4. A shared divisor m'
is recorded only when both tests pass; no implication from the first test to
the second is assumed.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path
from fractions import Fraction


ROOT = Path(__file__).resolve().parents[1]
REPAIR_INPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
SOURCE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-lower-modulus-shared-gap-type-ii-results.json"

# These are the frozen inputs used for this audit. The support input is the
# factorization source; the repair output supplies the lower-box profiles.
EXPECTED_REPAIR_SHA256 = "c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f"
EXPECTED_SOURCE_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization(value: int) -> list[tuple[int, int]]:
    """Return a deterministic trial-division factorization for these inputs."""
    if value <= 0:
        raise ValueError("factorization requires a positive integer")
    factors: list[tuple[int, int]] = []
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    if exponent:
        factors.append((2, exponent))
    prime = 3
    while prime * prime <= value:
        if value % prime:
            prime += 2
            continue
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        factors.append((prime, exponent))
        prime += 2
    if value > 1:
        factors.append((value, 1))
    return factors


def divisors_from_factorization(
    factors: list[tuple[int, int]], *, square: bool = False
) -> list[int]:
    result = [1]
    for prime, exponent in factors:
        maximum = 2 * exponent if square else exponent
        result = [entry * prime**power for entry in result for power in range(maximum + 1)]
    return sorted(result)


def divisors(value: int) -> list[int]:
    return divisors_from_factorization(factorization(value))


def box_representations(
    factorization_data: list[tuple[int, int]], modulus: int
) -> list[dict[str, object]]:
    """Enumerate every exponent vector in the original K-box hitting -1 mod t."""
    records: list[dict[str, object]] = []
    ranges = [range(-exponent, exponent + 1) for _prime, exponent in factorization_data]
    for exponents in itertools.product(*ranges):
        numerator = 1
        denominator = 1
        for (prime, _exponent), signed_exponent in zip(factorization_data, exponents):
            if signed_exponent >= 0:
                numerator *= prime**signed_exponent
            else:
                denominator *= prime ** (-signed_exponent)
        if (numerator + denominator) % modulus:
            continue
        if math.gcd(numerator, denominator) != 1:
            raise AssertionError("signed exponent representation was not reduced")
        records.append(
            {
                "exponents": list(exponents),
                "a": numerator,
                "b": denominator,
                "sum": numerator + denominator,
            }
        )
    return records


def type_ii_certificates(p: int, gap: int) -> list[dict[str, int]]:
    """Enumerate all Type II normal-form divisors at one prescribed gap."""
    if p % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= p - 2:
        return []
    if (p + gap) % 4:
        raise AssertionError("prescribed Type II gap is not integral")
    x = (p + gap) // 4
    x_factors = factorization(x)
    certificates: list[dict[str, int]] = []
    for divisor in divisors_from_factorization(x_factors, square=True):
        if divisor > x or (x * x) % divisor or (x + divisor) % gap:
            continue
        common = math.gcd(divisor, x)
        a = divisor // common
        b = x // common
        if math.gcd(a, b) != 1 or common % a:
            raise AssertionError("Type II normalization lost coprimality")
        c = common // a
        if a > b or (a + b) % gap:
            raise AssertionError("Type II normalization lost its gap condition")
        if x != a * b * c or divisor != a * a * c:
            raise AssertionError("Type II normalization did not reconstruct")
        if (p * (x + divisor)) % gap:
            raise AssertionError("Type II first tail is not integral")
        if (p * (x + x * x // divisor)) % gap:
            raise AssertionError("Type II second tail is not integral")
        y = p * (x + divisor) // gap
        z = p * (x + x * x // divisor) // gap
        if Fraction(4, p) != Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
            raise AssertionError("Type II denominator identity did not verify")
        certificates.append(
            {
                "gap": gap,
                "x": x,
                "divisor": divisor,
                "A": a,
                "B": b,
                "C": c,
                "y": y,
                "z": z,
            }
        )
    return certificates


def run() -> dict[str, object]:
    repair_sha = sha256(REPAIR_INPUT)
    source_sha = sha256(SOURCE_INPUT)
    if repair_sha != EXPECTED_REPAIR_SHA256:
        raise AssertionError("the frozen repair input changed")
    if source_sha != EXPECTED_SOURCE_SHA256:
        raise AssertionError("the frozen factorization input changed")

    repair_payload = json.loads(REPAIR_INPUT.read_text(encoding="utf-8"))
    source_payload = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    source_rows = {
        (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"])): row
        for row in source_payload["records"]
        if row.get("within_radius_cap")
    }

    hit_rows: list[dict[str, object]] = []
    for row in repair_payload["records"]:
        for candidate in row["candidates"]:
            if candidate.get("lower_modulus_classification") != "F_box_hit":
                continue
            key = (int(row["prime"]), int(row["original_R"]), tuple(row["witness_exponents"]))
            if key not in source_rows:
                raise AssertionError("lower hit is missing its factorization source")
            hit_rows.append(
                {
                    "prime": int(row["prime"]),
                    "orientation": row["orientation"],
                    "original_R": int(row["original_R"]),
                    "repair_gap": int(candidate["gap"]),
                    "lower_modulus": int(candidate["balanced_t"]),
                    "reported_box_count": int(candidate["lower_modulus_target_count"]),
                    "factorization": source_rows[key]["factorization"],
                    "witness_exponents": row["witness_exponents"],
                }
            )
    if len(hit_rows) != 6:
        raise AssertionError(f"expected six lower F-box hits, found {len(hit_rows)}")

    records: list[dict[str, object]] = []
    for hit in sorted(hit_rows, key=lambda row: (int(row["prime"]), str(row["orientation"]))):
        factorization_data = [
            (int(prime), int(exponent)) for prime, exponent in hit["factorization"]
        ]
        lower_modulus = int(hit["lower_modulus"])
        representations = box_representations(factorization_data, lower_modulus)
        if len(representations) != int(hit["reported_box_count"]):
            raise AssertionError("reported lower-box multiplicity disagrees with enumeration")
        sums = sorted({int(entry["sum"]) for entry in representations})
        candidate_gaps = sorted(
            {
                divisor
                for total in sums
                for divisor in divisors(total)
                if divisor % 4 == 3 and 3 <= divisor <= int(hit["prime"]) - 2
            }
        )
        certificates: list[dict[str, object]] = []
        for gap in candidate_gaps:
            for certificate in type_ii_certificates(int(hit["prime"]), gap):
                matching_representations = [
                    {
                        "exponents": entry["exponents"],
                        "a": entry["a"],
                        "b": entry["b"],
                        "sum": entry["sum"],
                    }
                    for entry in representations
                    if int(entry["sum"]) % gap == 0
                ]
                certificates.append(
                    {
                        **certificate,
                        "matching_lower_representations": matching_representations,
                    }
                )
        records.append(
            {
                **hit,
                "factorization": [[prime, exponent] for prime, exponent in factorization_data],
                "representation_count": len(representations),
                "unique_sum_count": len(sums),
                "unique_sums": sums,
                "shared_gap_candidate_count": len(candidate_gaps),
                "shared_gap_candidates": candidate_gaps,
                "type_ii_certificate_count": len(certificates),
                "type_ii_certificates": certificates,
            }
        )

    certificate_count = sum(int(row["type_ii_certificate_count"]) for row in records)
    prime_hit_count = sum(int(row["type_ii_certificate_count"] > 0) for row in records)
    expected_certificate_gaps = {
        57399241: {311},
        242042089: {31},
        475619929: {295, 1703},
    }
    actual_certificate_gaps = {
        int(row["prime"]): {int(cert["gap"]) for cert in row["type_ii_certificates"]}
        for row in records
        if row["type_ii_certificate_count"]
    }
    if actual_certificate_gaps != expected_certificate_gaps:
        raise AssertionError("shared-gap Type II hit set changed")
    if certificate_count != 4 or prime_hit_count != 3:
        raise AssertionError("frozen shared-gap audit counts changed")

    return {
        "arithmetic": (
            "A lower F-box representation a/b=-1 (mod t) supplies a+b divisible by t. "
            "Every legal m' dividing a+b is only a shared-gap candidate; a Type II certificate "
            "still requires an independent x'=(p+m')/4 divisor d=A^2*C with A<=B and m'|A+B."
        ),
        "scope_note": (
            "Finite six-hit audit. A shared gap candidate does not automatically lift: the lower "
            "pair need not divide x', and the Type II divisor test is independent. The four hits "
            "below are valid certificates for three primes, not a universal lifting theorem."
        ),
        "repair_input": REPAIR_INPUT.name,
        "repair_input_sha256": repair_sha,
        "source_input": SOURCE_INPUT.name,
        "source_input_sha256": source_sha,
        "lower_hit_count": len(records),
        "representation_count": sum(int(row["representation_count"]) for row in records),
        "unique_sum_count": sum(int(row["unique_sum_count"]) for row in records),
        "shared_gap_candidate_count": sum(
            int(row["shared_gap_candidate_count"]) for row in records
        ),
        "type_ii_certificate_count": certificate_count,
        "prime_hit_count": prime_hit_count,
        "certificate_gap_histogram": dict(
            sorted(Counter(int(cert["gap"]) for row in records for cert in row["type_ii_certificates"]).items())
        ),
        "records": records,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "lower_hit_count",
                    "representation_count",
                    "unique_sum_count",
                    "shared_gap_candidate_count",
                    "type_ii_certificate_count",
                    "prime_hit_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
