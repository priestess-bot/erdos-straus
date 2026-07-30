#!/usr/bin/env python3
"""Audit smaller-R and Type II exits for proxy-overloaded private carriers.

The frozen square-terminal data contain one deterministic box-overflow witness
per state.  This script selects the states where one overflow coordinate is an
analytically private linear block and its excess exceeds that block's full
q-adic height.  It then asks two exact questions:

1. Does the complete frozen linear spectrum contain a Type I target hit at a
   strictly smaller source modulus R?
2. Does the prime have a direct Type II certificate with gap at most 51?

The first-witness excess is only a finite proxy.  The script does not claim an
overflow-to-carrier injection or a universal escape theorem.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import sympy


ROOT = Path(__file__).resolve().parents[1]
CAPACITY_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-all-assignment-height-upper-bound-results.json"
)
SOURCE_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-square-terminal-relation-certificate-results.json"
)
SPECTRUM_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-private-carrier-escape-profile-results.json"
)

EXPECTED_INPUT_SHA256 = {
    CAPACITY_INPUT.name: "62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5",
    SOURCE_INPUT.name: "53119e9aaeadac7080811782f3a3eb07f3cd6674dfb9a18776a3c5e68d108297",
    SPECTRUM_INPUT.name: "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f",
}
EXPECTED_PRIVATE_ROW_SHA256 = (
    "94595e1e49e0faf5046dd03ab94fd15cfe3703adec4718f0f47a978f4bfc05d0"
)
EXPECTED_PRIVATE_ROW_COUNT = 37
EXPECTED_PRIVATE_STATE_COUNT = 37
EXPECTED_PRIVATE_PRIME_COUNT = 31
EXPECTED_SMALLER_R_HIT_COUNT = 35
EXPECTED_NO_SMALLER_R_PRIMES = [168_434_809, 310_002_289]
EXPECTED_TYPE_II_GAP_HISTOGRAM = {15: 3, 19: 12, 27: 4, 31: 9, 39: 1, 47: 1, 51: 1}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_guarded(path: Path) -> dict[str, object]:
    expected = EXPECTED_INPUT_SHA256[path.name]
    actual = file_sha256(path)
    if actual != expected:
        raise AssertionError(f"authoritative input hash changed: {path.name}")
    return json.loads(path.read_text(encoding="utf-8"))


def q_valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factorization(value: int) -> list[tuple[int, int]]:
    factors = sorted(
        (int(prime), int(exponent))
        for prime, exponent in sympy.factorint(value).items()
    )
    if math.prod(prime**exponent for prime, exponent in factors) != value:
        raise AssertionError("factorization failed to reconstruct")
    if any(not sympy.isprime(prime) for prime, _ in factors):
        raise AssertionError("factorization contains a nonprime base")
    return factors


def divisors_from_factorization(
    factors: Iterable[tuple[int, int]], exponent_multiplier: int = 1
) -> list[int]:
    divisors = [1]
    for prime, exponent in factors:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent_multiplier * exponent + 1)
        ]
    return sorted(divisors)


def factorization_payload(factors: Iterable[tuple[int, int]]) -> list[dict[str, int]]:
    return [
        {"prime": int(prime), "exponent": int(exponent)}
        for prime, exponent in factors
    ]


def exact_identity(numerator: int, denominators: Iterable[int]) -> bool:
    return Fraction(4, numerator) == sum(
        (Fraction(1, denominator) for denominator in denominators), Fraction()
    )


def normalize_type_i_target(prime: int, R: int, K: int, divisor: int) -> dict[str, object]:
    common = math.gcd(divisor, K)
    B = divisor // common
    if common * common % divisor:
        raise AssertionError("target square divisor did not normalize")
    C = common * common // divisor
    H = K // common
    if H < B:
        B, H = H, B
    oriented_divisor = B * B * C
    A, A_remainder = divmod(B + H, R)
    gap, gap_remainder = divmod(4 * oriented_divisor + 1, R)
    x = A * B * C
    y = A * C * H
    target_solution = [x, y, prime * K]
    checks = {
        "square_divisor": K * K % oriented_divisor == 0,
        "target_residue": (oriented_divisor + K) % R == 0,
        "normal_coordinates": B * C * H == K and math.gcd(B, H) == 1,
        "A_integral": A_remainder == 0,
        "A_B_coprime": math.gcd(A, B) == 1,
        "gap_integral": gap_remainder == 0,
        "natural_gap": 3 <= gap <= prime - 2 and gap % 4 == 3,
        "prime_reconstruction": prime == 4 * A * B * C - gap,
        "target_identity": exact_identity(prime, target_solution),
    }
    if not all(checks.values()):
        raise AssertionError(
            "Type I target normalization failed: "
            + ", ".join(name for name, passed in checks.items() if not passed)
        )
    return {
        "divisor": oriented_divisor,
        "A": A,
        "B": B,
        "C": C,
        "H": H,
        "gap": gap,
        "target_solution": target_solution,
        "checks": checks,
    }


def target_hit(prime: int, R: int) -> tuple[int, int, list[tuple[int, int]]]:
    K = (prime * R + 1) // 4
    if R < 3 or R % 4 != 3 or 4 * K != prime * R + 1:
        raise AssertionError("invalid target modulus")
    factors = factorization(K)
    hits = [
        divisor
        for divisor in divisors_from_factorization(factors, 2)
        if divisor <= K and (divisor + K) % R == 0
    ]
    if not hits:
        raise AssertionError("frozen target hit could not be independently recovered")
    return K, min(hits), factors


def linear_sources_at_R(
    prime: int, R: int, factors_of_K: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    factors_of_4K = dict(factors_of_K)
    factors_of_4K[2] = factors_of_4K.get(2, 0) + 2
    sources: set[tuple[int, int]] = set()
    four_K = prime * R + 1
    for left_block in divisors_from_factorization(sorted(factors_of_4K.items())):
        right_block = four_K // left_block
        if left_block % R != 1 or right_block % R != 1:
            continue
        a = (left_block - 1) // R
        s = (right_block - 1) // R
        if (
            a >= 1
            and s >= 1
            and s % 2 == 1
            and prime == a + s + a * s * R
        ):
            sources.add((a, s))
    return sorted(sources)


def lift_witness(prime: int, R: int, K: int, target: dict[str, object], source: tuple[int, int]) -> dict[str, object]:
    a, s = source
    E = s * R + 1
    n = prime - s
    source_solution = [a * K, int(target["target_solution"][0]), int(target["target_solution"][1])]
    checks = {
        "linear_source": prime == a + s + a * s * R,
        "source_factorization": n == a * E,
        "strict_even_source": n % 2 == 0 and 2 <= n < prime,
        "K_factorization": 4 * K == (a * R + 1) * E,
        "shared_tail_identity": exact_identity(n, source_solution),
        "marked_first_term": n * K % E == 0 and n * K // E == a * K,
    }
    if not all(checks.values()):
        raise AssertionError("linear marked lift failed")
    return {
        "a": a,
        "s": s,
        "E": E,
        "source_denominator": n,
        "source_solution": source_solution,
        "checks": checks,
    }


def type_ii_certificate(prime: int, gap_cap: int = 51) -> dict[str, object] | None:
    for gap in range(3, min(gap_cap, prime - 2) + 1, 4):
        x = (prime + gap) // 4
        if 4 * x != prime + gap:
            continue
        factors = factorization(x)
        for divisor in divisors_from_factorization(factors, 2):
            if divisor > x:
                break
            if (x + divisor) % gap:
                continue
            y = prime * (x + divisor) // gap
            z = prime * (x + x * x // divisor) // gap
            if not exact_identity(prime, [x, y, z]):
                continue
            common = math.gcd(divisor, x)
            A = divisor // common
            B = x // common
            if common % A:
                raise AssertionError("Type II divisor did not normalize")
            C = common // A
            checks = {
                "normal_coordinates": x == A * B * C and divisor == A * A * C,
                "A_B_coprime": math.gcd(A, B) == 1,
                "orientation": A <= B,
                "gap_condition": (A + B) % gap == 0,
                "target_identity": exact_identity(prime, [x, y, z]),
            }
            if not all(checks.values()):
                raise AssertionError("Type II normalization failed")
            return {
                "gap": gap,
                "x": x,
                "divisor": divisor,
                "A": A,
                "B": B,
                "C": C,
                "y": y,
                "z": z,
                "checks": checks,
            }
    return None


def private_rows(
    capacity: dict[str, object],
    source_data: dict[str, object],
) -> list[dict[str, object]]:
    source_by_state = {
        (int(record["prime"]), int(record["R"])): record
        for record in source_data["records"]
    }
    rows: list[dict[str, object]] = []
    for capacity_record in capacity["records"]:
        if capacity_record["category"] != "no_assignment_can_carry_all_excess":
            continue
        prime = int(capacity_record["prime"])
        R = int(capacity_record["R"])
        source = source_by_state[(prime, R)]
        a = int(source["a"])
        s = int(source["s"])
        for q_text, excess_value in sorted(
            capacity_record["overflow_excess"].items(), key=lambda item: int(item[0])
        ):
            q = int(q_text)
            excess = int(excess_value)
            carriers = []
            for label, other in ((a, s), (s, a)):
                block = label * R + 1
                if block % q == 0:
                    carriers.append((label, other, block))
            if len(carriers) != 1:
                continue
            label, other, block = carriers[0]
            height = q_valuation(block, q)
            if excess <= height:
                continue
            d0 = block // q
            n0 = (prime - label) // q
            if not (
                sympy.isprime(q)
                and 0 < label < q
                and 0 < R < q
                and n0 == other * d0
                and d0 + R > n0 - 1
            ):
                continue
            eligible_divisors = [
                int(divisor)
                for divisor in sympy.divisors(n0)
                if divisor >= d0 and (divisor - d0) % label == 0
            ]
            if eligible_divisors != [d0]:
                continue
            rows.append(
                {
                    "prime": prime,
                    "R": R,
                    "q": q,
                    "overflow_excess": excess,
                    "block_height": height,
                    "label": label,
                    "other_coordinate": other,
                    "block": block,
                    "d0": d0,
                    "n0": n0,
                    "eligible_divisors": eligible_divisors,
                }
            )
    rows.sort(key=lambda row: (row["prime"], row["R"], row["q"]))
    return rows


def private_row_sha256(rows: list[dict[str, object]]) -> str:
    fields = (
        "prime",
        "R",
        "q",
        "overflow_excess",
        "block_height",
        "label",
        "other_coordinate",
        "d0",
        "n0",
    )
    payload = "".join(
        "\t".join(str(int(row[field])) for field in fields) + "\n" for row in rows
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def run_audit() -> dict[str, object]:
    capacity = load_guarded(CAPACITY_INPUT)
    source_data = load_guarded(SOURCE_INPUT)
    spectrum = load_guarded(SPECTRUM_INPUT)
    rows = private_rows(capacity, source_data)
    row_hash = private_row_sha256(rows)
    state_count = len({(row["prime"], row["R"]) for row in rows})
    primes = sorted({int(row["prime"]) for row in rows})
    if (
        len(rows) != EXPECTED_PRIVATE_ROW_COUNT
        or state_count != EXPECTED_PRIVATE_STATE_COUNT
        or len(primes) != EXPECTED_PRIVATE_PRIME_COUNT
        or row_hash != EXPECTED_PRIVATE_ROW_SHA256
    ):
        raise AssertionError("private proxy-overflow selection changed")

    profiles = {int(profile["prime"]): profile for profile in spectrum["profiles"]}
    type_ii_by_prime: dict[int, dict[str, object]] = {}
    for prime in primes:
        certificate = type_ii_certificate(prime)
        if certificate is None:
            raise AssertionError(f"no Type II certificate through gap 51 for {prime}")
        type_ii_by_prime[prime] = certificate

    gap_histogram = Counter(
        int(certificate["gap"]) for certificate in type_ii_by_prime.values()
    )
    if dict(sorted(gap_histogram.items())) != EXPECTED_TYPE_II_GAP_HISTOGRAM:
        raise AssertionError("Type II gap histogram changed")

    smaller_hit_count = 0
    no_smaller_rows: list[dict[str, object]] = []
    for row in rows:
        prime = int(row["prime"])
        R = int(row["R"])
        q = int(row["q"])
        profile_records = profiles[prime]["records"]
        if [int(record["R"]) for record in profile_records] != sorted(
            int(record["R"]) for record in profile_records
        ):
            raise AssertionError("complete linear spectrum is not R-sorted")
        current = next(record for record in profile_records if int(record["R"]) == R)
        if current["classification"] != "finite_exponent":
            raise AssertionError("selected private state is not the frozen F-box miss")
        smaller_hits = [
            record
            for record in profile_records
            if int(record["R"]) < R and record["classification"] == "hit"
        ]
        row["smaller_hit_Rs"] = [int(record["R"]) for record in smaller_hits]
        row["type_ii_gap"] = int(type_ii_by_prime[prime]["gap"])
        if smaller_hits:
            smaller_hit_count += 1
            selected = smaller_hits[0]
            selected_R = int(selected["R"])
            K, divisor, factors = target_hit(prime, selected_R)
            if K != int(selected["K"]) or q_valuation(K, q):
                raise AssertionError("smaller-R hit did not renew the private q support")
            sources = linear_sources_at_R(prime, selected_R, factors)
            if not sources or len(sources) != int(selected["source_state_count"]):
                raise AssertionError("smaller-R linear source reconstruction changed")
            target = normalize_type_i_target(prime, selected_R, K, divisor)
            lift = lift_witness(prime, selected_R, K, target, sources[0])
            row["selected_exit"] = "smaller_R_type_I_even_terminal"
            row["smaller_R_witness"] = {
                "R": selected_R,
                "K": K,
                "K_factorization": factorization_payload(factors),
                "q_absent_from_K": K % q != 0,
                "source_state_count": len(sources),
                "target": target,
                "lift": lift,
            }
        else:
            row["selected_exit"] = "direct_type_II"
            later_hit = next(
                (
                    record
                    for record in profile_records
                    if int(record["R"]) > R and record["classification"] == "hit"
                ),
                None,
            )
            if later_hit is None:
                raise AssertionError("counterexample state has no later target hit")
            later_R = int(later_hit["R"])
            later_K, later_divisor, later_factors = target_hit(prime, later_R)
            later_sources = linear_sources_at_R(prime, later_R, later_factors)
            later_target = normalize_type_i_target(
                prime, later_R, later_K, later_divisor
            )
            row["first_larger_R_hit"] = {
                "R": later_R,
                "K": later_K,
                "source_state_count": len(later_sources),
                "target": later_target,
            }
            no_smaller_rows.append(row)

    no_smaller_primes = sorted(int(row["prime"]) for row in no_smaller_rows)
    if (
        smaller_hit_count != EXPECTED_SMALLER_R_HIT_COUNT
        or no_smaller_primes != EXPECTED_NO_SMALLER_R_PRIMES
    ):
        raise AssertionError("smaller-R escape split changed")

    return {
        "arithmetic": (
            "select analytically private coordinates from the frozen deterministic "
            "overflow witness, compare their excess with the full current block height, "
            "look up the complete frozen linear target spectrum, independently rebuild "
            "one selected Type I hit and its even marked source, and scan exact Type II "
            "divisor certificates through gap 51"
        ),
        "scope_note": (
            "Finite proxy-overflow profile only. The selected excess comes from one "
            "deterministic radius-six witness and is not a target-fiber minimum or a "
            "proved overflow-to-carrier charge. The 35+2 split is not a universal escape theorem."
        ),
        "inputs": {
            path.name: {"sha256": EXPECTED_INPUT_SHA256[path.name]}
            for path in (CAPACITY_INPUT, SOURCE_INPUT, SPECTRUM_INPUT)
        },
        "private_row_count": len(rows),
        "private_state_count": state_count,
        "private_prime_count": len(primes),
        "private_row_tsv_sha256": row_hash,
        "smaller_R_type_I_even_terminal_count": smaller_hit_count,
        "no_smaller_R_hit_count": len(no_smaller_rows),
        "no_smaller_R_hit_primes": no_smaller_primes,
        "direct_type_II_prime_count": len(type_ii_by_prime),
        "direct_type_II_row_count": len(rows),
        "direct_type_II_gap_cap": 51,
        "direct_type_II_max_gap": max(gap_histogram),
        "direct_type_II_gap_histogram": {
            str(gap): count for gap, count in sorted(gap_histogram.items())
        },
        "selector_branch_counts": {
            "smaller_R_type_I_even_terminal": smaller_hit_count,
            "direct_type_II_after_no_smaller_R": len(no_smaller_rows),
        },
        "type_II_by_prime": [
            {"prime": prime, **type_ii_by_prime[prime]} for prime in primes
        ],
        "records": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit()
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    print(
        "private rows={private_row_count}, smaller-R exits="
        "{smaller_R_type_I_even_terminal_count}, no-smaller-R="
        "{no_smaller_R_hit_count}, Type-II max gap={direct_type_II_max_gap}".format(
            **result
        )
    )


if __name__ == "__main__":
    main()
