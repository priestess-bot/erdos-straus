#!/usr/bin/env python3
"""Verify q-local quadratic-shift factorization and even-K Type II terminals."""

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


def verify_q_local_shift_and_terminal(p: int, k: int, q: int, m: int) -> None:
    """Check only q-local stutter consequences, then reconstruct the certificate."""
    if not (is_prime(p) and p % 24 == 1 and is_prime(q) and q % 2 == 1):
        raise AssertionError("control did not use a core prime and odd prime factor")
    if k < 2 or k % 2:
        raise AssertionError("terminal fan requires an even K")

    # These are the q-level consequences of q|D, D=mp+1-h, and q|ph+1.
    h = k
    local_d = m * p + 1 - h
    if local_d % q or (p * h + 1) % q:
        raise AssertionError("q-local stutter congruences changed")
    if (m + k * (k - 1)) % q:
        raise AssertionError("quadratic shift control changed")

    minus_factor = (k - 1) * p - 1
    plus_factor = k * p + 1
    if (k * (k - 1) * p * p - p - 1) != minus_factor * plus_factor:
        raise AssertionError("quadratic shift factorization changed")
    if plus_factor % q or minus_factor % q == 0:
        raise AssertionError("control did not select the positive linear branch")
    if h % q != k % q:
        raise AssertionError("positive branch height residue changed")

    if q % (4 * k) != (3 * k - 1) % (4 * k):
        raise AssertionError("control did not meet the Type II residue class")
    s, s_remainder = divmod(q + 1, k)
    x, x_remainder = divmod(p + s, 4)
    c, c_remainder = divmod(x, q)
    if any((s_remainder, x_remainder, c_remainder)):
        raise AssertionError("Type II terminal parameters are not integral")
    if not (3 <= s <= p - 2 and s % 4 == 3 and c > 0):
        raise AssertionError("Type II terminal left the natural gap range")

    d = c
    if x * x % d or d > x or (x + d) % s:
        raise AssertionError("Type II divisor conditions failed")
    y = p * (x + d) // s
    z = p * (x + x * x // d) // s
    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p):
        raise AssertionError("Type II denominators changed")
    if (x, y, z) != (q * c, k * p * c, k * p * q * c):
        raise AssertionError("closed-form Type II denominators changed")


def verify() -> None:
    # K=2 is the established m+2/2p+1 branch; K=4 and K=6 check new fan rows.
    verify_q_local_shift_and_terminal(97, 2, 5, 3)
    verify_q_local_shift_and_terminal(1009, 4, 11, 10)
    verify_q_local_shift_and_terminal(337, 6, 17, 4)
    print("verified quadratic-shift even-K Type II terminal fan")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
