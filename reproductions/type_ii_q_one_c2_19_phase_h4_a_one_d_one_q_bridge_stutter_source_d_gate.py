#!/usr/bin/env python3
"""Verify focused controls for the d4=1 original q-bridge source-D closure."""

from __future__ import annotations

import argparse
from math import isqrt


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


def verify_two_candidate_gate() -> None:
    for p in (73, 97, 193):
        q = (p + 1) // 2
        dividend = 3 * q - 1
        candidates = (6, p + 6)

        if not (
            p % 24 == 1
            and 2 * q == p + 1
            and dividend == (3 * p + 1) // 2
            and 0 < dividend < 2 * p
            and dividend % 3 != 0
            and p + 6 < dividend < 2 * (p + 6)
            and all(dividend % candidate for candidate in candidates)
        ):
            raise AssertionError(f"p={p}: d4=1 source-D candidate gate changed")


def verify_p73_divisor_control() -> None:
    p = 73
    q = (p + 1) // 2
    dividend = 3 * q - 1
    matching = tuple(
        divisor for divisor in positive_divisors(dividend) if divisor % p == 6
    )

    if not (
        dividend == 110
        and positive_divisors(dividend) == (1, 2, 5, 10, 11, 22, 55, 110)
        and matching == ()
    ):
        raise AssertionError("p=73 d4=1 source-D divisor control changed")


def verify() -> None:
    verify_two_candidate_gate()
    verify_p73_divisor_control()
    print("verified d4=1 original q-bridge source-D stutter closure")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
