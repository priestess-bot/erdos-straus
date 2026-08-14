#!/usr/bin/env python3
"""Verify q-local general-A quadratic shifts and Type II terminals."""

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
        divisor += 1
    return True


def verify_q_local_general_shift(
    p: int, a: int, k: int, q: int, m: int, h: int
) -> None:
    """Check q-local stutter consequences, then reconstruct a Type II certificate."""
    if not (is_prime(p) and p % 24 == 1 and is_prime(q) and q % 2 == 1):
        raise AssertionError("control did not use a core prime and odd prime factor")
    if not (a > 0 and a % 2 == 1 and (p + 3) % a == 0):
        raise AssertionError("A must be an odd divisor of p+3")
    if not (k > a and k % 2 == 0 and gcd(a, k) == 1):
        raise AssertionError("general fan requires coprime odd A and even K>A")

    local_d = m * p + 1 - h
    if local_d % q or (p * h + 1) % q:
        raise AssertionError("q-local stutter congruences changed")
    if (m * a * a + k * (k - a)) % q:
        raise AssertionError("general quadratic shift control changed")

    minus_factor = (k - a) * p - a
    plus_factor = k * p + a
    if (
        k * (k - a) * p * p - a * a * p - a * a
        != minus_factor * plus_factor
    ):
        raise AssertionError("general quadratic shift factorization changed")
    if plus_factor % q or minus_factor % q == 0:
        raise AssertionError("control did not select the positive linear branch")
    if (a * h - k) % q:
        raise AssertionError("positive branch height residue changed")
    if (h * h - 1) % q == 0:
        raise AssertionError("positive branch must be transverse to h-squared-minus-one")

    if q % (4 * a * k) != (3 * k - a) % (4 * a * k):
        raise AssertionError("control did not meet the general Type II residue class")
    s, s_remainder = divmod(q + a, k)
    c, c_remainder = divmod(p + s, 4 * a * q)
    if s_remainder or c_remainder:
        raise AssertionError("Type II terminal parameters are not integral")
    if not (3 <= s <= p - 2 and s % 4 == 3 and c > 0 and a <= q):
        raise AssertionError("Type II terminal left the natural gap range")

    raw_generator, raw_remainder = divmod(k * p + a, q)
    if raw_remainder or raw_generator != 4 * a * c * k - 1:
        raise AssertionError("raw-ray generator identity changed")

    x, d = a * q * c, a * a * c
    if x * x % d or d > x or (x + d) % s:
        raise AssertionError("Type II divisor conditions failed")
    y = p * (x + d) // s
    z = p * (x + x * x // d) // s
    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p):
        raise AssertionError("Type II denominators changed")
    if (x, y, z) != (a * q * c, p * a * c * k, p * q * c * k):
        raise AssertionError("closed-form Type II denominators changed")


def verify() -> None:
    # The first control recovers the A=1, K=6 row; the second is genuinely A>1.
    verify_q_local_general_shift(337, 1, 6, 17, 4, 6)
    verify_q_local_general_shift(1297, 5, 6, 13, 6, 9)
    print("verified general-A quadratic-shift Type II terminal fan")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
