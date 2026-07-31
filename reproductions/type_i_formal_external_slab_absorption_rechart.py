#!/usr/bin/env python3
"""Verify the two focused external-slab collision and absorption boundaries."""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-formal-external-slab-absorption-rechart-results.json"
)

CASES = (
    {"prime": 178_513, "R": 183, "Q": 13, "X": 13, "Y": 170},
    {"prime": 78_268_369, "R": 8_895, "Q": 8_243, "X": 8_243, "Y": 652},
)


def divisors(n: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d:
            continue
        low.append(d)
        if d * d != n:
            high.append(n // d)
    return low + high[::-1]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def canonical_chart(prime: int, modulus_capacity: int) -> tuple[int, int]:
    chart_modulus = (-pow(prime, -1, 4 * modulus_capacity)) % (
        4 * modulus_capacity
    )
    if not 1 <= chart_modulus < 4 * modulus_capacity:
        raise AssertionError("canonical representative is outside its range")
    chart_K = (prime * chart_modulus + 1) // 4
    if chart_modulus % 4 != 3 or chart_K % modulus_capacity:
        raise AssertionError("canonical chart failed its congruence contract")
    return chart_modulus, chart_K


def analyze_case(case: dict[str, int]) -> dict[str, object]:
    prime = case["prime"]
    R = case["R"]
    Q = case["Q"]
    X = case["X"]
    Y = case["Y"]
    K = (prime * R + 1) // 4
    S = X + Y
    L = X * Y

    assert is_prime(prime)
    assert prime % 24 == 1
    assert 4 * K == prime * R + 1
    assert S % R == 0
    assert gcd(X, Y) == 1
    assert X % Q == 0
    assert K % ((X // Q) * Y) == 0
    assert K % Q != 0

    divisor_collisions = []
    for T in divisors(S):
        type_ii = (prime + T) % (4 * L) == 0
        cross_chart_type_i = (prime * T + 1) % (4 * L) == 0
        if type_ii or cross_chart_type_i:
            divisor_collisions.append(
                {
                    "T": T,
                    "type_ii": type_ii,
                    "cross_chart_type_i": cross_chart_type_i,
                }
            )

    absorption = []
    for M in divisors(L):
        if M % Q:
            continue
        chart_R, chart_K = canonical_chart(prime, M)
        absorption.append(
            {
                "M": M,
                "R_M": chart_R,
                "K_M": chart_K,
                "decreases_R": chart_R < R,
            }
        )

    Q_chart = next(item for item in absorption if item["M"] == Q)
    full_chart = next(item for item in absorption if item["M"] == L)
    return {
        **case,
        "K": K,
        "S": S,
        "L": L,
        "divisors_of_S": divisors(S),
        "divisor_collisions": divisor_collisions,
        "absorption_candidate_count": len(absorption),
        "descending_absorption_candidates": [
            item for item in absorption if item["decreases_R"]
        ],
        "Q_chart": Q_chart,
        "full_slab_chart": full_chart,
    }


def run() -> dict[str, object]:
    records = [analyze_case(case) for case in CASES]
    observed = [
        (
            record["prime"],
            record["R"],
            [item["M"] for item in record["descending_absorption_candidates"]],
            record["Q_chart"]["R_M"],
            record["full_slab_chart"]["R_M"],
            len(record["divisor_collisions"]),
        )
        for record in records
    ]
    expected = [
        (178_513, 183, [13, 26], 35, 1_543, 0),
        (78_268_369, 8_895, [], 10_395, 11_319_791, 0),
    ]
    if observed != expected:
        raise AssertionError(f"focused external-slab boundary changed: {observed}")
    return {
        "schema_version": "formal-external-slab-absorption-rechart/v1",
        "scope_note": (
            "Focused exact verification of two boundary slabs. It does not establish "
            "a universal slab-existence or large-slab terminal theorem."
        ),
        "summary": {
            "case_count": len(records),
            "case_with_divisor_collision_count": sum(
                bool(record["divisor_collisions"]) for record in records
            ),
            "case_with_descending_absorption_count": sum(
                bool(record["descending_absorption_candidates"])
                for record in records
            ),
            "large_slab_local_miss_count": sum(
                not record["divisor_collisions"]
                and not record["descending_absorption_candidates"]
                for record in records
            ),
        },
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
