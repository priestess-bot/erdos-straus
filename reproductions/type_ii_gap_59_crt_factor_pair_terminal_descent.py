#!/usr/bin/env python3
"""Verify the gap-59 CRT factor-pair terminal and marked-descent ray."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def ray_data(h: int) -> tuple[int, int, int, int, int]:
    assert h > 0
    assert h % 5 == 0 and h % 7 == 1 and h % 59 == 53
    p = 24 * h + 1
    x = (p + 59) // 4
    d = 21
    assert x == 6 * h + 15 and x % d == 0 and d <= x
    assert (x + d) % 59 == 0 and (p - 1) % 60 == 0
    B = x // d
    K = (B + 1) // 59
    n = (p + 59) // 60
    assert (B + 1) % 59 == 0 and n == 2 * h // 5 + 1 and n < p
    return p, x, B, K, n


def verify() -> None:
    # h=820 is the unique least positive simultaneous residue.
    assert all(
        (h % 5, h % 7, h % 59) != (0, 1, 53)
        for h in range(1, 820)
    )
    for index in range(3):
        h = 820 + 2065 * index
        assert (h % 5, h % 7, h % 59) == (0, 1, 53)

    assert 24 * 820 + 1 == 19681
    assert 24 * 2065 == 49560
    assert gcd(19681, 49560) == 1

    h = 4950
    p, x, B, K, n = ray_data(h)
    assert p == 118801 and is_prime(p)
    assert (x, B, K, n) == (29715, 1415, 24, 1981)

    A, C = 1, 21
    assert x == A * B * C and A + B == 59 * K
    source = (x, A * C * K, B * C * K)
    target = (source[0], p * source[1], p * source[2])
    assert source == (29715, 504, 713160)
    assert target == (29715, 59875704, 84724121160)
    assert Fraction(4, n) == sum((Fraction(1, value) for value in source), Fraction())
    assert Fraction(4, p) == sum((Fraction(1, value) for value in target), Fraction())

    print("verified gap-59 CRT factor-pair terminal and marked-descent ray")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if args.verify:
        verify()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
