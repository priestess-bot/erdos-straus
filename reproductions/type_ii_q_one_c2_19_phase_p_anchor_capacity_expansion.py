#!/usr/bin/env python3
"""Verify the p-anchor complete-excess capacity map of the q=1 high C=2 phase.

The checks use two fixed prime controls and exact polynomial identities.  They
do not scan a parameter interval or enumerate Egyptian-fraction solutions.
"""

from __future__ import annotations

import argparse
from math import gcd


def valuation_two(value: int) -> int:
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def phase_data(prime: int) -> dict[str, int]:
    if not (is_prime(prime) and prime % 24 == 1 and prime % 912 == 769):
        raise AssertionError("control is not a q=1 high C=2 core prime")

    f = 2 * prime * prime - 3 * prime - 1
    support = (prime - 1) * (2 * prime + 1) * f // 8
    capacity = 2
    k = capacity * support
    r = 4 * prime**3 - 8 * prime**2 - prime + 4
    q = (r - 1) // 2
    next_support = support * q
    next_capacity = (2 * prime + 4) // 3
    next_k = next_support * next_capacity
    next_r = (4 * next_k - 1) // prime

    if not (
        8 * support == (prime - 1) * (2 * prime + 1) * f
        and prime * r + 1 == 4 * k
        and r % prime == 4
        and r % 4 == 3
        and valuation_two(r - 1) == 1
        and valuation_two(k) >= 2
        and gcd(r - 1, k) == 2
        and q % 2 == 1
        and gcd(q, k) == 1
        and gcd(q, support) == 1
        and q % prime != 0
        and (2 * prime + 4) % 3 == 0
        and 2 < next_capacity < prime
        and (2 * pow(q, -1, prime)) % prime == next_capacity
        and prime * next_r + 1 == 4 * next_k
        and next_k // next_support == next_capacity
    ):
        raise AssertionError(f"p={prime}: high C=2 p-anchor capacity map changed")

    # Exact divisibility identities used to rule out odd common factors.
    if not (
        (r - 1 + 2) % (prime - 1) == 0
        and (r - 2) % (2 * prime + 1) == 0
        and r - 1 == (2 * prime - 1) * f - 2 * (prime - 1)
        and f % (prime - 1) == (prime - 3) % (prime - 1)
    ):
        raise AssertionError(f"p={prime}: gcd proof identities changed")

    return {
        "prime": prime,
        "support": support,
        "R": r,
        "K": k,
        "Q": q,
        "next_capacity": next_capacity,
        "next_support": next_support,
        "next_R": next_r,
    }


def verify() -> None:
    first = phase_data(769)
    second = phase_data(2593)
    if not (
        first["Q"] == 907_147_391
        and first["next_capacity"] == 514
        and second["next_capacity"] == 1_730
        and first["next_capacity"] > 2
        and second["next_capacity"] > 2
    ):
        raise AssertionError("the fixed high C=2 phase controls changed")
    print(
        "verified q=1 high C=2 p-anchor map: Q=(R-1)/2 and "
        "capacity 2 -> (2p+4)/3"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run exact phase controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
