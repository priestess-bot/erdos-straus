#!/usr/bin/env python3
"""Verify the focused source-supported D-only tail-ratio identities."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "two-denominator-lift-source-supported-tail-rigidity-results.json"
)

CASES = (
    {"prime": 73, "rank": 33, "D": 9, "expected_z": 11},
    {"prime": 73, "rank": 64, "D": 64, "expected_z": None},
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


def in_d_only_set(prime: int, rank: int, D: int) -> bool:
    r = prime - rank
    N = rank * prime
    C = 4 * r
    return (
        N * N % D == 0
        and 0 < D < rank * rank
        and (D - N) % C == 0
        and (N * N // D - N) % C == 0
    )


def analyze_case(case: dict[str, int | None]) -> dict[str, object]:
    prime = int(case["prime"])
    rank = int(case["rank"])
    D = int(case["D"])
    expected_z = case["expected_z"]
    r = prime - rank

    assert prime % 24 == 1
    assert 2 <= rank < prime
    assert in_d_only_set(prime, rank, D)
    assert rank * rank % D == 0

    h = rank * rank // D
    assert (h - 1) % r == 0
    k = (h - 1) // r
    assert (prime * k + 1) % 4 == 0
    lam = (prime * k + 1) // 4
    assert gcd(k, lam) == 1
    assert rank * lam % h == 0

    a = rank * lam // h
    a_prime = prime * lam
    M = 4 * a - rank
    S = rank * a
    g = gcd(M, S)
    assert M == D * k
    assert S == D * lam
    assert g == D
    assert Fraction(4, rank) - Fraction(1, a) == Fraction(k, lam)
    assert Fraction(4, prime) - Fraction(1, a_prime) == Fraction(k, lam)

    witnesses = [
        z for z in divisors(lam * lam) if (z + lam) % k == 0
    ]
    if expected_z is None:
        assert not witnesses
        tail = None
        canonical_center_divisor = None
    else:
        assert int(expected_z) in witnesses
        z = int(expected_z)
        b = (lam + z) // k
        c = (lam + lam * lam // z) // k
        assert Fraction(1, b) + Fraction(1, c) == Fraction(k, lam)
        assert Fraction(1, a) + Fraction(1, b) + Fraction(1, c) == Fraction(
            4, rank
        )
        assert Fraction(1, a_prime) + Fraction(1, b) + Fraction(
            1, c
        ) == Fraction(4, prime)
        tail = {"z": z, "b": b, "c": c}
        canonical_center_divisor = min(z, lam * lam // z)
        assert canonical_center_divisor < lam
        assert (canonical_center_divisor + lam) % k == 0

    return {
        "prime": prime,
        "rank": rank,
        "D": D,
        "r": r,
        "h": h,
        "k": k,
        "lambda": lam,
        "a": a,
        "a_prime": a_prime,
        "M": M,
        "S": S,
        "g": g,
        "tail_witness_count": len(witnesses),
        "tail": tail,
        "canonical_center_divisor": canonical_center_divisor,
    }


def run() -> dict[str, object]:
    records = [analyze_case(case) for case in CASES]
    observed = [
        (
            record["prime"],
            record["rank"],
            record["D"],
            record["h"],
            record["k"],
            record["lambda"],
            record["a"],
            record["a_prime"],
            record["tail_witness_count"],
        )
        for record in records
    ]
    expected = [
        (73, 33, 9, 121, 3, 55, 15, 4015, 4),
        (73, 64, 64, 64, 7, 128, 128, 9344, 0),
    ]
    if observed != expected:
        raise AssertionError(f"focused source-supported boundary changed: {observed}")

    false_converse = {
        "prime": 73,
        "rank": 36,
        "k": 35,
        "lambda": 639,
        "h": 1296,
    }
    assert 4 * false_converse["lambda"] == (
        false_converse["prime"] * false_converse["k"] + 1
    )
    assert false_converse["rank"] ** 2 % false_converse["h"] == 0
    assert (
        false_converse["rank"] * false_converse["lambda"]
    ) % false_converse["h"] != 0

    return {
        "schema_version": "two-denominator-source-supported-tail-rigidity/v1",
        "scope_note": (
            "Focused exact verification of one nonempty and one empty core-prime "
            "source-supported D-only state. It does not classify D not dividing n^2."
        ),
        "summary": {
            "case_count": len(records),
            "nonempty_tail_count": sum(
                record["tail_witness_count"] > 0 for record in records
            ),
            "empty_tail_count": sum(
                record["tail_witness_count"] == 0 for record in records
            ),
            "false_converse_without_h_divides_n_lambda": false_converse,
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
