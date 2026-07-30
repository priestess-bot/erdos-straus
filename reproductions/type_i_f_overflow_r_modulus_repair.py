#!/usr/bin/env python3
"""Audit the R-factor repair branch induced by a rational overflow witness."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-rational-gap-denominator-results.json"
SOURCE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
EXPECTED_INPUT_SHA256 = "60cbb80428d6e2fbb1295138fe265893d7bfecbd23a92ed863edf10e0361b768"
EXPECTED_SOURCE_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def divisors(value: int) -> list[int]:
    if value <= 0:
        raise ValueError("divisors requires a positive integer")
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


def valuation(value: int, prime: int) -> int:
    count = 0
    while value % prime == 0:
        value //= prime
        count += 1
    return count


def admissible_gaps(modulus: int, prime: int) -> list[int]:
    return [
        value
        for value in divisors(modulus)
        if value % 4 == 3 and 3 <= value <= prime - 2
    ]


def audit_orientation(
    row: dict[str, object], source_row: dict[str, object], orientation: str
) -> dict[str, object]:
    if orientation not in {"forward", "reverse"}:
        raise ValueError("unknown orientation")
    prime = int(row["prime"])
    original_R = int(row["R"])
    K = int(row["K"])
    if orientation == "forward":
        A = int(row["formal_A"])
        B = int(row["formal_B"])
    else:
        A = int(row["formal_B"])
        B = int(row["formal_A"])
    factorization = [(int(q), int(nu)) for q, nu in source_row["factorization"]]
    witness = tuple(int(value) for value in source_row["witness_exponents"])
    if orientation == "reverse":
        witness = tuple(-value for value in witness)

    repair_gcd = math.gcd(original_R, B - 1)
    target_divisor = K * A
    candidates: list[dict[str, object]] = []
    for gap in divisors(repair_gcd):
        if gap < 3 or gap > prime - 2 or gap % 4 != 3:
            continue
        if (4 * target_divisor + 1) % gap:
            raise AssertionError("R-factor repair lost the target congruence")
        first_numerator = prime + gap
        if first_numerator % 4:
            raise AssertionError("candidate gap is not integral")
        first_denominator = first_numerator // 4
        repaired_R = (4 * target_divisor + 1) // gap
        repaired_K = first_denominator * repaired_R - target_divisor
        if repaired_K <= 0 or 4 * repaired_K != prime * repaired_R + 1:
            raise AssertionError("candidate did not reconstruct a valid K state")
        if repaired_R % 4 != 3 or math.gcd(repaired_K, repaired_R) != 1:
            raise AssertionError("candidate did not reconstruct an admissible modulus state")
        square_hit = first_denominator * first_denominator % target_divisor == 0
        identity_numerator = 4 * K + gap * gap * (original_R // gap) - 1
        square_deficits: dict[str, int] = {}
        for (q, nu), exponent in zip(factorization, witness):
            first_valuation = valuation(first_denominator, q)
            identity_valuation = valuation(identity_numerator, q) - (2 if q == 2 else 0)
            if identity_valuation != first_valuation:
                raise AssertionError("R-factor q-adic identity did not recover x_m")
            target_exponent = nu + max(exponent, 0)
            deficit = max(target_exponent - 2 * first_valuation, 0)
            if deficit:
                square_deficits[str(q)] = deficit
        if square_hit != (not square_deficits):
            raise AssertionError("square-divisibility and q-adic deficit disagree")
        repair_divisor = math.gcd(target_divisor, first_denominator * first_denominator)
        second_repair_modulus = math.gcd(gap, 4 * repair_divisor + 1)
        second_repair_gaps = admissible_gaps(second_repair_modulus, prime)
        second_repair_square_hits: list[int] = []
        for second_gap in second_repair_gaps:
            second_x = (prime + second_gap) // 4
            if second_x * second_x % repair_divisor == 0:
                second_repair_square_hits.append(second_gap)
        candidates.append(
            {
                "gap": gap,
                "target_divisor": target_divisor,
                "first_denominator": first_denominator,
                "target_divisor_divides_first_square": square_hit,
                "square_deficits": square_deficits,
                "square_deficit_layers": sum(square_deficits.values()),
                "deficient_q_coordinate_count": len(square_deficits),
                "repair_divisor": repair_divisor,
                "second_repair_modulus": second_repair_modulus,
                "second_repair_gaps": second_repair_gaps,
                "second_repair_square_hits": second_repair_square_hits,
                "repaired_R": repaired_R,
                "repaired_K": repaired_K,
            }
        )

    return {
        "orientation": orientation,
        "original_R": original_R,
        "formal_A": A,
        "formal_B": B,
        "repair_gcd": repair_gcd,
        "repair_gcd_is_nontrivial": repair_gcd > 1,
        "candidate_count": len(candidates),
        "square_hit_count": sum(
            int(candidate["target_divisor_divides_first_square"]) for candidate in candidates
        ),
        "square_deficit_layers": sum(
            int(candidate["square_deficit_layers"]) for candidate in candidates
        ),
        "deficient_q_coordinate_count": sum(
            int(candidate["deficient_q_coordinate_count"]) for candidate in candidates
        ),
        "second_repair_modulus_nontrivial_count": sum(
            int(candidate["second_repair_modulus"] > 1) for candidate in candidates
        ),
        "second_repair_gap_candidate_count": sum(
            len(candidate["second_repair_gaps"]) for candidate in candidates
        ),
        "second_repair_square_hit_count": sum(
            len(candidate["second_repair_square_hits"]) for candidate in candidates
        ),
        "candidates": candidates,
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the rational-gap input changed")
    if sha256(SOURCE_INPUT) != EXPECTED_SOURCE_SHA256:
        raise AssertionError("the frozen factorization input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    source_payload = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    source_rows = {
        (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"])): dict(row)
        for row in source_payload["records"]
        if row.get("within_radius_cap")
    }
    records: list[dict[str, object]] = []
    for row in payload["records"]:
        row = dict(row)
        key = (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"]))
        if key not in source_rows:
            raise AssertionError("rational-gap row is missing its frozen factorization")
        source_row = source_rows[key]
        for orientation in ("forward", "reverse"):
            detail = audit_orientation(row, source_row, orientation)
            records.append(
                {
                    "prime": int(row["prime"]),
                    "R": int(row["R"]),
                    "witness_exponents": row["witness_exponents"],
                    **detail,
                }
            )

    by_orientation = {
        orientation: [row for row in records if row["orientation"] == orientation]
        for orientation in ("forward", "reverse")
    }
    return {
        "arithmetic": (
            "For a rational overflow witness q^z=A/B, every m dividing gcd(R,B-1) "
            "with m=3 mod 4 gives an integer target divisor e=K*A satisfying "
            "4e+1=0 mod m. It therefore defines a new admissible state "
            "R'=(4e+1)/m, K'=(p+m)R'/4-e; a direct Type-I certificate exists "
            "exactly when e divides ((p+m)/4)^2. The square failure has the exact "
            "q-adic deficit e_q-2*v_q((p+m)/4), recoverable from "
            "v_q(4K+m^2(R/m)-1)."
        ),
        "scope_note": (
            "This is an unconditional repair branch and a finite frozen audit. "
            "A candidate gap reconstructs a valid algebraic state, but failure of "
            "the square-divisibility test is not an arithmetic descent. The branch "
            "must be combined with a further repair modulus, cross-state capacity, "
            "or another liftable state transition."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "factorization_input": SOURCE_INPUT.name,
        "factorization_input_sha256": sha256(SOURCE_INPUT),
        "input_record_count": len(payload["records"]),
        "orientation_record_count": len(records),
        "nontrivial_repair_modulus_count": sum(
            int(row["repair_gcd_is_nontrivial"]) for row in records
        ),
        "candidate_orientation_count": sum(int(row["candidate_count"] > 0) for row in records),
        "candidate_gap_count": sum(int(row["candidate_count"]) for row in records),
        "direct_square_hit_count": sum(int(row["square_hit_count"]) for row in records),
        "square_deficit_layers": sum(int(row["square_deficit_layers"]) for row in records),
        "deficient_q_coordinate_count": sum(
            int(row["deficient_q_coordinate_count"]) for row in records
        ),
        "maximum_square_deficit": max(
            (
                int(candidate["square_deficit_layers"])
                for row in records
                for candidate in row["candidates"]
            ),
            default=0,
        ),
        "second_repair_modulus_nontrivial_count": sum(
            int(candidate["second_repair_modulus"] > 1)
            for row in records
            for candidate in row["candidates"]
        ),
        "second_repair_gap_candidate_count": sum(
            len(candidate["second_repair_gaps"])
            for row in records
            for candidate in row["candidates"]
        ),
        "second_repair_square_hit_count": sum(
            len(candidate["second_repair_square_hits"])
            for row in records
            for candidate in row["candidates"]
        ),
        "by_orientation": {
            orientation: {
                "record_count": len(rows),
                "nontrivial_repair_modulus_count": sum(
                    int(row["repair_gcd_is_nontrivial"]) for row in rows
                ),
                "candidate_orientation_count": sum(
                    int(row["candidate_count"] > 0) for row in rows
                ),
                "candidate_gap_count": sum(int(row["candidate_count"]) for row in rows),
                "direct_square_hit_count": sum(int(row["square_hit_count"]) for row in rows),
                "square_deficit_layers": sum(int(row["square_deficit_layers"]) for row in rows),
                "deficient_q_coordinate_count": sum(
                    int(row["deficient_q_coordinate_count"]) for row in rows
                ),
                "second_repair_modulus_nontrivial_count": sum(
                    int(candidate["second_repair_modulus"] > 1)
                    for row in rows
                    for candidate in row["candidates"]
                ),
                "second_repair_gap_candidate_count": sum(
                    len(candidate["second_repair_gaps"])
                    for row in rows
                    for candidate in row["candidates"]
                ),
                "second_repair_square_hit_count": sum(
                    len(candidate["second_repair_square_hits"])
                    for row in rows
                    for candidate in row["candidates"]
                ),
            }
            for orientation, rows in by_orientation.items()
        },
        "repair_gcd_histogram": {
            str(value): count
            for value, count in sorted(
                Counter(int(row["repair_gcd"]) for row in records).items()
            )
        },
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
                    "input_record_count",
                    "orientation_record_count",
                    "nontrivial_repair_modulus_count",
                    "candidate_orientation_count",
                    "candidate_gap_count",
                    "direct_square_hit_count",
                    "square_deficit_layers",
                    "deficient_q_coordinate_count",
                    "maximum_square_deficit",
                    "second_repair_modulus_nontrivial_count",
                    "second_repair_gap_candidate_count",
                    "second_repair_square_hit_count",
                    "by_orientation",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
