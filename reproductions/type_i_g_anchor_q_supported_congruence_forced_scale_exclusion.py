#!/usr/bin/env python3
"""Verify a fixed exclusion control for the congruence-forced scale bundle."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


PRIME = 14_281
MODULUS = 14_280
SCALES = (1, 2, 3, 6)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def scale_record(k: int) -> tuple[int, int, int, int, int]:
    q = 4 * k - 1
    source = (q * PRIME + 1) // (q + 1)
    retained = k * source
    carrier = (PRIME - 3) // 2
    return k, q, source, retained, gcd(carrier, retained)


def verify() -> None:
    records = tuple(scale_record(k) for k in SCALES)
    k2_residues = {pow(11, exponent, 7) for exponent in range(3)}
    if not (
        is_prime(PRIME)
        and PRIME % MODULUS == 1
        and PRIME % 24 == 1
        and all(((PRIME - 1) // 4) % k == 0 for k in SCALES)
        and PRIME % 5 == PRIME % 7 == PRIME % 17 == 1
        and records
        == (
            (1, 3, 10_711, 10_711, 1),
            (2, 7, 12_496, 24_992, 11),
            (3, 11, 13_091, 39_273, 1),
            (6, 23, 13_686, 82_116, 1),
        )
        and k2_residues == {1, 2, 4}
        and (-2) % 7 not in k2_residues
        and all((-k) % (4 * k - 1) != 1 for k in SCALES)
    ):
        raise AssertionError("congruence-forced Q-supported scale exclusion changed")
    print("verified the p=14281 four-scale Q-supported exclusion control")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the fixed exclusion control")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
