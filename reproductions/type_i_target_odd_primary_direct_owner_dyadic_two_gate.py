#!/usr/bin/env python3
"""Verify the target-odd direct-owner and natural-dyadic two-gate lemma."""

from __future__ import annotations

import argparse
import math


def square_divisors(factors: tuple[tuple[int, int], ...]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors:
        divisors = [d * prime**j for d in divisors for j in range(2 * exponent + 1)]
    return divisors


def verify() -> None:
    # Odd-q direct-owner conflict from the genuine p=73, R=27 F control.
    p, R, K = 73, 27, 493
    assert 4 * K == p * R + 1
    q, e = 3, 2
    gamma = (2 * 9) % (q**e)
    beta = (-p * pow(4, -1, q**e)) % (q**e)
    assert gamma == 0
    assert beta == 2
    assert gamma != beta

    # The q=2 prefix has no positive layer for any integer owner.
    for owner in range(-5, 6):
        assert (p + 4 * owner) % 2 == 1
    assert math.gcd(4, 2) != 1

    # A real F-state generalized-dyadic candidate: its natural marker is integral,
    # while the complete centered Type-I divisor class is empty.
    p, R, K = 67369, 27, 454741
    E, n = 28, 67368
    assert 4 * K == p * R + 1
    assert E % R == 1
    assert (4 * K - E) % R == 0
    assert n == (4 * K - E) // R
    assert (4 * K * K) % E == 0
    assert (n * K) % E == 0
    alpha = n * K // E
    assert alpha == 1094106846
    assert alpha not in {n // 2, n}

    centered = [
        d
        for d in square_divisors(((7, 1), (167, 1), (389, 1)))
        if d < K and (d + K) % R == 0
    ]
    assert centered == []

    print("verified target-odd primary two-gate no-local-lift dispatch")
    print(
        {
            "direct_owner": {
                "p": 73,
                "R": 27,
                "K": 493,
                "odd_q": 3,
                "e": 2,
                "gamma": gamma,
                "beta": beta,
                "branch": "TARGET_ODD_QPREFIX_DIRECT_OWNER_CONFLICT",
            },
            "q2": {"branch": "QPREFIX_CAPACITY_ZERO_BY_PARITY"},
            "dyadic": {
                "p": p,
                "R": R,
                "K": K,
                "E": E,
                "n": n,
                "alpha": alpha,
                "centered_divisor_count": len(centered),
                "branch": "DYADIC_NATURAL_LIFT_EMPTY",
            },
            "dispatch": "TARGET_ODD_PRIMARY_TWO_GATE_NO_LOCAL_LIFT",
        }
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
