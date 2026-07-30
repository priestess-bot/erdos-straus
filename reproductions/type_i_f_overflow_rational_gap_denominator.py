#!/usr/bin/env python3
"""Verify the exact rational-gap denominator carried by an overflow witness."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-rational-gap-denominator-results.json"
EXPECTED_INPUT_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    count = 0
    while value % prime == 0:
        value //= prime
        count += 1
    return count


def powers(factorization: list[tuple[int, int]], exponents: tuple[int, ...]) -> tuple[int, int]:
    numerator = 1
    denominator = 1
    for (prime, _bound), exponent in zip(factorization, exponents):
        if exponent >= 0:
            numerator *= prime**exponent
        else:
            denominator *= prime ** (-exponent)
    return numerator, denominator


def divisors(value: int) -> list[int]:
    """Return all positive divisors for the small repair moduli in the frozen audit."""
    result = [1]
    factor = 2
    remaining = value
    while factor * factor <= remaining:
        if remaining % factor:
            factor = 3 if factor == 2 else factor + 2
            continue
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        result = [entry * factor**power for entry in result for power in range(exponent + 1)]
        factor = 3 if factor == 2 else factor + 2
    if remaining > 1:
        result = [entry * remaining for entry in result]
    return sorted(result)


def admissible_repair_gaps(modulus: int | None, prime: int) -> list[int]:
    if modulus is None:
        return []
    return [
        value
        for value in divisors(modulus)
        if value % 4 == 3 and 3 <= value <= prime - 2
    ]


def audit_row(row: dict[str, object]) -> dict[str, object]:
    if not row.get("within_radius_cap"):
        raise AssertionError("the input contains a row without a frozen witness")
    prime = int(row["prime"])
    modulus = int(row["R"])
    K = (prime * modulus + 1) // 4
    factorization = [(int(q), int(nu)) for q, nu in row["factorization"]]
    witness = tuple(int(value) for value in row["witness_exponents"])
    if len(factorization) != len(witness):
        raise AssertionError("factorization and witness dimensions disagree")
    if 4 * K != prime * modulus + 1 or math.gcd(K, modulus) != 1:
        raise AssertionError("invalid Type-I state")
    if math.prod(q**nu for q, nu in factorization) != K:
        raise AssertionError("factorization does not reconstruct K")

    A, B = powers(factorization, witness)
    if math.gcd(A, B) != 1:
        raise AssertionError("positive and negative witness parts are not coprime")
    numerator = 4 * K * A + B
    if numerator % modulus:
        raise AssertionError("target congruence did not produce an integral numerator")
    gap_numerator = numerator // modulus
    if gap_numerator <= 0:
        raise AssertionError("formal gap numerator is not positive")
    if math.gcd(B, modulus) != 1:
        raise AssertionError("witness denominator is not coprime to R")

    actual_common = math.gcd(gap_numerator, B)
    predicted_common = math.gcd(4 * K, B)
    if actual_common != predicted_common:
        raise AssertionError("gcd reduction identity failed")
    reduced_denominator = B // actual_common

    m0_numerator = A + B
    if m0_numerator % modulus:
        raise AssertionError("the witness parts do not define an integral m0")
    m0 = m0_numerator // modulus
    if math.gcd(m0, B) != 1:
        raise AssertionError("m0 and witness denominator are not coprime")
    first_denominator = B // math.gcd(B, K)
    for (q, nu), exponent in zip(factorization, witness):
        expected = max(-exponent - nu, 0)
        actual = valuation(first_denominator, q)
        if actual != expected:
            raise AssertionError("formal first denominator does not equal box overflow")
    canonical_target_divisor = None
    canonical_target_divisor_divides_x_square = None
    canonical_repair_modulus = None
    canonical_repair_modulus_is_admissible = None
    canonical_repair_gaps: list[int] = []
    canonical_repair_square_hits: list[int] = []
    if first_denominator == 1:
        if K % B:
            raise AssertionError("integral first denominator did not imply B|K")
        H = K // B
        formal_gap = gap_numerator // B
        if gap_numerator % B:
            raise AssertionError("integral first denominator left a rational gap")
        x_z = H * m0
        canonical_target_divisor = H * A
        canonical_target_divisor_divides_x_square = x_z * x_z % canonical_target_divisor == 0
        if (4 * canonical_target_divisor + 1) % formal_gap:
            raise AssertionError("canonical target divisor lost the gap congruence")
        canonical_square_divisor = math.gcd(canonical_target_divisor, x_z * x_z)
        canonical_repair_modulus = math.gcd(formal_gap, 4 * canonical_square_divisor + 1)
        canonical_repair_modulus_is_admissible = (
            canonical_repair_modulus % 4 == 3
            and 3 <= canonical_repair_modulus <= prime - 2
        )
        canonical_repair_gaps = admissible_repair_gaps(canonical_repair_modulus, prime)
        for repair_gap in canonical_repair_gaps:
            repair_x_numerator = prime + repair_gap
            if repair_x_numerator % 4:
                continue
            repair_x = repair_x_numerator // 4
            if repair_x * repair_x % canonical_square_divisor == 0:
                canonical_repair_square_hits.append(repair_gap)

    predicted_denominator_excess: dict[str, int] = {}
    actual_denominator_excess: dict[str, int] = {}
    for (q, nu), exponent in zip(factorization, witness):
        four_k_height = nu + (2 if q == 2 else 0)
        predicted = max(-exponent - four_k_height, 0)
        actual = valuation(reduced_denominator, q)
        if actual != predicted:
            raise AssertionError("reduced denominator does not equal overflow excess")
        if predicted:
            predicted_denominator_excess[str(q)] = predicted
            actual_denominator_excess[str(q)] = actual

    reverse_A, reverse_B = powers(factorization, tuple(-value for value in witness))
    reverse_m0_numerator = reverse_A + reverse_B
    if reverse_m0_numerator % modulus:
        raise AssertionError("the reversed witness parts do not define an integral m0")
    reverse_m0 = reverse_m0_numerator // modulus
    if math.gcd(reverse_m0, reverse_B) != 1:
        raise AssertionError("the reversed m0 and witness denominator are not coprime")
    reverse_first_denominator = reverse_B // math.gcd(reverse_B, K)
    for (q, nu), exponent in zip(factorization, tuple(-value for value in witness)):
        expected = max(-exponent - nu, 0)
        actual = valuation(reverse_first_denominator, q)
        if actual != expected:
            raise AssertionError("reversed formal first denominator does not equal box overflow")
    reverse_numerator = 4 * K * reverse_A + reverse_B
    if reverse_numerator % modulus:
        raise AssertionError("the reversed target witness lost its congruence")
    reverse_gap_numerator = reverse_numerator // modulus
    reverse_denominator = reverse_B // math.gcd(reverse_gap_numerator, reverse_B)
    reverse_canonical_target_divisor = None
    reverse_canonical_target_divisor_divides_x_square = None
    reverse_canonical_repair_modulus = None
    reverse_canonical_repair_modulus_is_admissible = None
    reverse_canonical_repair_gaps: list[int] = []
    reverse_canonical_repair_square_hits: list[int] = []
    if reverse_first_denominator == 1:
        if K % reverse_B or reverse_gap_numerator % reverse_B:
            raise AssertionError("reversed integral first denominator left a rational gap")
        reverse_H = K // reverse_B
        reverse_formal_gap = reverse_gap_numerator // reverse_B
        reverse_x_z = reverse_H * reverse_m0
        reverse_canonical_target_divisor = reverse_H * reverse_A
        reverse_canonical_target_divisor_divides_x_square = (
            reverse_x_z * reverse_x_z % reverse_canonical_target_divisor == 0
        )
        if (4 * reverse_canonical_target_divisor + 1) % reverse_formal_gap:
            raise AssertionError("reversed canonical target divisor lost the gap congruence")
        reverse_canonical_square_divisor = math.gcd(
            reverse_canonical_target_divisor, reverse_x_z * reverse_x_z
        )
        reverse_canonical_repair_modulus = math.gcd(
            reverse_formal_gap, 4 * reverse_canonical_square_divisor + 1
        )
        reverse_canonical_repair_modulus_is_admissible = (
            reverse_canonical_repair_modulus % 4 == 3
            and 3 <= reverse_canonical_repair_modulus <= prime - 2
        )
        reverse_canonical_repair_gaps = admissible_repair_gaps(
            reverse_canonical_repair_modulus, prime
        )
        for repair_gap in reverse_canonical_repair_gaps:
            repair_x_numerator = prime + repair_gap
            if repair_x_numerator % 4:
                continue
            repair_x = repair_x_numerator // 4
            if repair_x * repair_x % reverse_canonical_square_divisor == 0:
                reverse_canonical_repair_square_hits.append(repair_gap)
    reverse_excess = sum(valuation(reverse_denominator, q) for q, _nu in factorization)
    forward_excess = sum(actual_denominator_excess.values())
    reverse_odd_excess = sum(
        valuation(reverse_denominator, q)
        for q, _nu in factorization
        if q != 2
    )

    return {
        "prime": prime,
        "R": modulus,
        "K": K,
        "witness_exponents": list(witness),
        "formal_A": A,
        "formal_B": B,
        "formal_gap_numerator": gap_numerator,
        "reduced_gap_denominator": reduced_denominator,
        "formal_m0": m0,
        "formal_first_denominator": first_denominator,
        "formal_first_denominator_is_integral": first_denominator == 1,
        "canonical_target_divisor": canonical_target_divisor,
        "canonical_target_divisor_divides_x_square": canonical_target_divisor_divides_x_square,
        "canonical_repair_modulus": canonical_repair_modulus,
        "canonical_repair_modulus_is_admissible": canonical_repair_modulus_is_admissible,
        "canonical_repair_gaps": canonical_repair_gaps,
        "canonical_repair_square_hits": canonical_repair_square_hits,
        "formal_reverse_m0": reverse_m0,
        "formal_reverse_first_denominator": reverse_first_denominator,
        "formal_reverse_first_denominator_is_integral": reverse_first_denominator == 1,
        "reverse_canonical_target_divisor": reverse_canonical_target_divisor,
        "reverse_canonical_target_divisor_divides_x_square": reverse_canonical_target_divisor_divides_x_square,
        "reverse_canonical_repair_modulus": reverse_canonical_repair_modulus,
        "reverse_canonical_repair_modulus_is_admissible": reverse_canonical_repair_modulus_is_admissible,
        "reverse_canonical_repair_gaps": reverse_canonical_repair_gaps,
        "reverse_canonical_repair_square_hits": reverse_canonical_repair_square_hits,
        "denominator_excess": actual_denominator_excess,
        "forward_denominator_excess_layers": forward_excess,
        "reverse_denominator_excess_layers": reverse_excess,
        "has_odd_overflow_denominator": any(
            q != 2 and amount
            for q, amount in ((int(q), amount) for q, amount in actual_denominator_excess.items())
        ),
        "has_odd_overflow_denominator_in_either_orientation": bool(
            any(
                q != 2 and amount
                for q, amount in ((int(q), amount) for q, amount in actual_denominator_excess.items())
            )
            or reverse_odd_excess
        ),
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen overflow input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    rows = [dict(row) for row in payload["records"] if row.get("within_radius_cap")]
    details = [audit_row(row) for row in rows]
    forward_layers = sum(int(row["forward_denominator_excess_layers"]) for row in details)
    reverse_layers = sum(int(row["reverse_denominator_excess_layers"]) for row in details)
    orientation_has_denominator = sum(
        int(
            int(row["forward_denominator_excess_layers"]) > 0
            or int(row["reverse_denominator_excess_layers"]) > 0
        )
        for row in details
    )
    odd_denominator_rows = sum(
        int(row["has_odd_overflow_denominator_in_either_orientation"]) for row in details
    )
    support = Counter(
        q
        for row in details
        for q in row["denominator_excess"]
    )
    return {
        "arithmetic": (
            "For a target affine witness z with product q_i^z=-1 mod R, write q^z=A/B. "
            "The formal gap (4K A/B+1)/R has reduced denominator exactly B/gcd(B,4K), "
            "whose q-adic exponents are the one-sided overflow beyond v_q(4K)."
        ),
        "scope_note": (
            "This is an exact arithmetic translation of a frozen affine-lattice witness. "
            "It does not make the rational gap a valid Type-I integer gap when the denominator "
            "is nontrivial, and it does not yet supply a cross-state capacity or lift map."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "record_count": len(details),
        "forward_denominator_excess_layers": forward_layers,
        "reverse_denominator_excess_layers": reverse_layers,
        "orientation_with_nontrivial_denominator_count": orientation_has_denominator,
        "odd_overflow_denominator_record_count": odd_denominator_rows,
        "formal_first_denominator_integral_record_count": sum(
            int(row["formal_first_denominator_is_integral"]) for row in details
        ),
        "formal_reverse_first_denominator_integral_record_count": sum(
            int(row["formal_reverse_first_denominator_is_integral"]) for row in details
        ),
        "formal_first_denominator_nontrivial_in_either_orientation_count": sum(
            int(
                not row["formal_first_denominator_is_integral"]
                or not row["formal_reverse_first_denominator_is_integral"]
            )
            for row in details
        ),
        "canonical_target_divisor_candidate_count": sum(
            int(row["canonical_target_divisor"] is not None) for row in details
        ),
        "canonical_target_divisor_square_divisibility_count": sum(
            int(row["canonical_target_divisor_divides_x_square"] is True) for row in details
        ),
        "canonical_repair_modulus_nontrivial_count": sum(
            int(row["canonical_repair_modulus"] not in (None, 1)) for row in details
        ),
        "canonical_repair_modulus_admissible_count": sum(
            int(row["canonical_repair_modulus_is_admissible"] is True) for row in details
        ),
        "canonical_repair_gap_candidate_count": sum(
            len(row["canonical_repair_gaps"]) for row in details
        ),
        "canonical_repair_square_hit_count": sum(
            len(row["canonical_repair_square_hits"]) for row in details
        ),
        "reverse_canonical_repair_modulus_nontrivial_count": sum(
            int(row["reverse_canonical_repair_modulus"] not in (None, 1))
            for row in details
        ),
        "reverse_canonical_repair_gap_candidate_count": sum(
            len(row["reverse_canonical_repair_gaps"]) for row in details
        ),
        "reverse_canonical_repair_square_hit_count": sum(
            len(row["reverse_canonical_repair_square_hits"]) for row in details
        ),
        "denominator_support_counts": {str(q): int(count) for q, count in sorted(support.items())},
        "records": details,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "record_count",
        "forward_denominator_excess_layers",
        "reverse_denominator_excess_layers",
        "orientation_with_nontrivial_denominator_count",
        "odd_overflow_denominator_record_count",
        "formal_first_denominator_integral_record_count",
        "formal_reverse_first_denominator_integral_record_count",
        "formal_first_denominator_nontrivial_in_either_orientation_count",
        "canonical_target_divisor_candidate_count",
        "canonical_target_divisor_square_divisibility_count",
        "canonical_repair_modulus_nontrivial_count",
        "canonical_repair_modulus_admissible_count",
        "canonical_repair_gap_candidate_count",
        "canonical_repair_square_hit_count",
        "reverse_canonical_repair_modulus_nontrivial_count",
        "reverse_canonical_repair_gap_candidate_count",
        "reverse_canonical_repair_square_hit_count",
        "denominator_support_counts",
    )}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
