#!/usr/bin/env python3
"""Verify fixed p+1 and 2p+1 terminal branches of the transverse residual dispatch."""

from __future__ import annotations

import argparse
from fractions import Fraction


def verify_p_plus_one_type_i(p: int, q: int) -> None:
    x, remainder = divmod(p + q, 4)
    if remainder or (p + 1) % q:
        raise AssertionError("p+1 control did not define its Type I certificate")
    if not (q % 4 == 3 and 3 <= q <= p - 2 and x > 0):
        raise AssertionError("p+1 control left the natural certificate range")
    d = x
    if x * x % d or (p * x + d) % q:
        raise AssertionError("p+1 Type I divisor conditions failed")
    y = x * (p + 1) // q
    z = p * x * (p + 1) // q
    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p):
        raise AssertionError("p+1 Type I denominators changed")


def verify_two_p_plus_one_type_ii(p: int, q: int) -> None:
    s, s_remainder = divmod(q + 1, 2)
    x, x_remainder = divmod(p + s, 4)
    c, c_remainder = divmod(x, q)
    if any((s_remainder, x_remainder, c_remainder)) or (2 * p + 1) % q:
        raise AssertionError("2p+1 control did not define its Type II certificate")
    if not (q % 8 == 5 and 3 <= s <= p - 2 and c > 0):
        raise AssertionError("2p+1 control left the natural certificate range")
    d = c
    if x * x % d or d > x or (x + d) % s:
        raise AssertionError("2p+1 Type II divisor conditions failed")
    y = p * (x + d) // s
    z = p * (x + x * x // d) // s
    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p):
        raise AssertionError("2p+1 Type II denominators changed")
    if (x, y, z) != (q * c, 2 * p * c, 2 * p * q * c):
        raise AssertionError("2p+1 closed-form denominators changed")


def verify() -> None:
    # Fixed prime controls for the two independently derived direct terminals.
    verify_p_plus_one_type_i(433, 7)
    verify_two_p_plus_one_type_ii(97, 5)
    verify_two_p_plus_one_type_ii(409, 13)
    print("verified transverse residual local Type I/II terminal dispatch")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
