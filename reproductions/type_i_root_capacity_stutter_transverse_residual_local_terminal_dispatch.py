#!/usr/bin/env python3
"""Verify transverse residual terminals and a q=7 mod 8 K=2 retraction."""

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


def verify_p_plus_one_type_i(p: int, q: int) -> None:
    if not (is_prime(p) and p % 24 == 1 and is_prime(q)):
        raise AssertionError("p+1 control did not use a core prime and prime factor")
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
    if not (is_prime(p) and p % 24 == 1 and is_prime(q)):
        raise AssertionError("2p+1 control did not use a core prime and prime factor")
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


def verify_two_p_plus_one_seven_mod_eight_retracts_to_k2(p: int, q: int) -> None:
    if not (is_prime(p) and p % 24 == 1 and is_prime(q)):
        raise AssertionError("q=7 control did not use a core prime and prime factor")
    lambda_value, lambda_remainder = divmod(q + 1, 2)
    gap, gap_remainder = divmod(3 * q + 1, 2)
    x, x_remainder = divmod(p + gap, 4)
    c, c_remainder = divmod(x, q)
    if any((lambda_remainder, gap_remainder, x_remainder, c_remainder)):
        raise AssertionError("q=7 control did not define its candidate quantities")
    if (2 * p + 1) % q or q % 8 != 7 or c % lambda_value:
        raise AssertionError("q=7 control did not satisfy its transverse hypotheses")
    if not (3 <= gap <= p - 2 and c > 0):
        raise AssertionError("q=7 control left the natural certificate range")

    # This candidate does give a Type II identity, but is subsumed by K=2.
    d = lambda_value * c
    if x * x % d or d > x or (x + d) % gap:
        raise AssertionError("q=7 candidate Type II divisor conditions failed")
    y = p * (x + d) // gap
    z = p * (x + x * x // d) // gap
    if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p):
        raise AssertionError("q=7 candidate Type II denominators changed")
    if (x, y, z) != (q * c, p * c, p * q * c // lambda_value):
        raise AssertionError("q=7 candidate closed-form denominators changed")

    bridge_modulus = 2 * gap - 1
    bridge_c, bridge_remainder = divmod(x, bridge_modulus)
    if bridge_modulus != 3 * q or bridge_remainder or c % 3:
        raise AssertionError("q=7 candidate did not force the K=2 bridge")
    bridge_d = bridge_c
    if x * x % bridge_d or bridge_d > x or (x + bridge_d) % gap:
        raise AssertionError("K=2 bridge Type II divisor conditions failed")
    bridge_y = p * (x + bridge_d) // gap
    bridge_z = p * (x + x * x // bridge_d) // gap
    if (
        Fraction(1, x) + Fraction(1, bridge_y) + Fraction(1, bridge_z)
        != Fraction(4, p)
    ):
        raise AssertionError("K=2 bridge Type II denominators changed")
    if (x, bridge_y, bridge_z) != (
        bridge_modulus * bridge_c,
        2 * p * bridge_c,
        2 * p * bridge_modulus * bridge_c,
    ):
        raise AssertionError("K=2 bridge closed-form denominators changed")


def verify() -> None:
    # Fixed core controls for two direct terminals and one K=2 retraction.
    verify_p_plus_one_type_i(433, 7)
    verify_two_p_plus_one_type_ii(97, 5)
    verify_two_p_plus_one_type_ii(409, 13)
    verify_two_p_plus_one_seven_mod_eight_retracts_to_k2(4441, 47)
    print("verified transverse residual terminal dispatch and q=7 K=2 retraction")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
