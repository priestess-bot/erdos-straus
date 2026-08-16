#!/usr/bin/env python3
"""Verify the finite d=1 q0=1 x-side source-D gate elimination.

This verifier checks the bounded integer menu in the proof.  It does not
search primes, denominators, H4 predecessors, or complete-excess payloads.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def positive_divisors(value: int) -> tuple[int, ...]:
    divisors: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        divisors.append(divisor)
        paired = value // divisor
        if paired != divisor:
            divisors.append(paired)
    return tuple(sorted(divisors))


def verify_p73_control() -> None:
    p = 73
    q = (p + 1) // 2
    source_dividend = q * q - 4 * q + 1
    matching_divisors = tuple(
        divisor for divisor in positive_divisors(source_dividend) if divisor % p == 20
    )
    if not (
        p % 24 == 1
        and q == 37
        and 4 * source_dividend == p * p - 6 * p - 3
        and source_dividend % 4 == 2
        and positive_divisors(source_dividend) == (1, 2, 13, 26, 47, 94, 611, 1_222)
        and matching_divisors == ()
    ):
        raise AssertionError("p=73 source-D gate control changed")


def verify_core_residue_menu() -> None:
    candidate_pairs = [
        (k_value, v_value)
        for k_value in range(1, 20)
        for v_value in range(1, 20)
        if k_value * v_value < 20
        and (v_value * (k_value - 3) - 4 * (k_value - 1)) % 24 == 0
    ]
    eligible_k = [
        k_value
        for k_value in range(1, 20)
        if (4 * (k_value - 1)) % gcd(k_value - 3, 24) == 0
    ]
    k_value, v_value = candidate_pairs[0]
    numerator = 20 * k_value + 120 - 3 * v_value
    denominator = 20 - k_value * v_value

    if not (
        eligible_k == [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19]
        and candidate_pairs == [(1, 12)]
        and numerator == 104
        and denominator == 8
        and numerator % denominator == 0
        and numerator // denominator == 13
        and 13 % 24 != 1
    ):
        raise AssertionError("core residue-menu elimination changed")


def verify() -> None:
    verify_p73_control()
    verify_core_residue_menu()
    print("verified q0=1 d=1 x-side source-D gate elimination")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
