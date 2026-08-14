#!/usr/bin/env python3
"""Verify fixed root-shape controls for the D-star native Type II raw-ray menu."""

from __future__ import annotations

import argparse
from fractions import Fraction


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def verify_menu_control(p: int, h: int, q: int, expect_prime: bool) -> None:
    """Check a root-shape q|ph+1 control, not an actual receipt assertion."""
    if not (is_prime(p) and p % 24 == 1 and 3 <= h < p):
        raise AssertionError("control did not use a core prime and proper root shape")
    if (p * p + p + 1) % h:
        raise AssertionError("control root did not divide the cyclotomic layer")
    if is_prime(q) != expect_prime:
        raise AssertionError("prime/composite menu-control label changed")
    if q <= 1 or q % (4 * h) != 4 * h - 1:
        raise AssertionError("raw-ray generator residue changed")
    if (p * h + 1) % q:
        raise AssertionError("menu modulus did not divide ph+1")

    c, c_remainder = divmod(q + 1, 4 * h)
    b, b_remainder = divmod(p * h + 1, q)
    m, m_remainder = divmod(b + 1, h)
    if any((c_remainder, b_remainder, m_remainder)):
        raise AssertionError("raw-ray coordinates are not integral")
    if not (c > 0 and b >= 1 and 3 <= m <= p - 2 and m % 4 == 3):
        raise AssertionError("raw-ray left the Type II natural range")
    if q != 4 * c * h - 1:
        raise AssertionError("raw-ray generator identity changed")

    x, d = b * c, c
    if x * x % d or d > x or (x + d) % m:
        raise AssertionError("Type II divisor conditions failed")
    y = p * (x + d) // m
    z = p * (x + x * x // d) // m
    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p):
        raise AssertionError("Type II denominators changed")
    if (x, y, z) != (b * c, p * h * c, p * h * b * c):
        raise AssertionError("closed-form raw-ray denominators changed")


def verify() -> None:
    # The second control makes the menu's composite-divisor support explicit.
    verify_menu_control(4657, 39, 311, expect_prime=True)
    verify_menu_control(10369, 21, 335, expect_prime=False)
    print("verified D-star native Type II raw-ray terminal menu controls")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
