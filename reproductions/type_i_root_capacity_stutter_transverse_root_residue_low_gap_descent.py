#!/usr/bin/env python3
"""Verify q-local root-residue factor gates, terminals, and strict two-tail lifts."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


LOW_GAPS = {3, 7, 11, 23}


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def verify_q_local_root_residue_low_gap(
    p: int, a: int, q: int, h: int, m: int
) -> None:
    """Check q-local stutter data, then reconstruct the marked two-tail lift."""
    if not (is_prime(p) and p % 24 == 1 and is_prime(q) and q % 2 == 1):
        raise AssertionError("control did not use a core prime and odd q")
    if not (a > 0 and a % 2 == 1 and (p + 3) % a == 0 and a % q):
        raise AssertionError("A must be an odd p-plus-three divisor prime to q")

    local_d = m * p + 1 - h
    if local_d % q or (p * h + 1) % q:
        raise AssertionError("q-local stutter congruences changed")
    if (h * h - 1) % q == 0:
        raise AssertionError("control did not use a transverse q residue")
    if (m + h * (h - 1)) % q:
        raise AssertionError("q-local finite-curve consequence changed")

    k = (a * h) % q
    if not (a < k < q and k % 2 == 0 and gcd(a, k) == 1):
        raise AssertionError("root residue did not enter the general-A positive chart")
    if (m * a * a + k * (k - a)) % q:
        raise AssertionError("root residue did not force the quadratic shift")
    if (k * p + a) % q:
        raise AssertionError("root residue did not force the positive linear branch")

    s, remainder = divmod(q + a, k)
    if remainder or s not in LOW_GAPS or s % (4 * a) != 3 % (4 * a):
        raise AssertionError("root residue did not enter the low-gap dispatch")
    if (p - 1) % (s + 1):
        raise AssertionError("core congruence did not provide the strict source denominator")

    c, remainder = divmod(p + s, 4 * a * q)
    if remainder or c <= 0:
        raise AssertionError("Type II terminal coordinates are not integral")
    n, remainder = divmod(p + s, s + 1)
    if remainder or not (0 < n < p):
        raise AssertionError("strict source denominator is invalid")

    x, d = a * q * c, a * a * c
    if x * x % d or d > x or (x + d) % s:
        raise AssertionError("Type II divisor certificate changed")
    target = (a * q * c, p * a * c * k, p * q * c * k)
    source = (a * q * c, a * c * k, q * c * k)
    if sum(Fraction(1, value) for value in target) != Fraction(4, p):
        raise AssertionError("target Type II terminal changed")
    if sum(Fraction(1, value) for value in source) != Fraction(4, n):
        raise AssertionError("source strict descent witness changed")
    if target != (source[0], p * source[1], p * source[2]):
        raise AssertionError("two-tail lift did not preserve the first denominator")


def verify_a_one_factor_gate(p: int, q: int, h: int, m: int, s: int) -> None:
    """Check the selection-free A=1 low-gap factor gate on q-local data."""
    if not (is_prime(p) and p % 24 == 1 and is_prime(q) and q % 2 == 1):
        raise AssertionError("control did not use a core prime and odd q")
    if s not in LOW_GAPS or q % (2 * s) != 2 * s - 1:
        raise AssertionError("q did not meet the low-gap factor residue")
    if (s * h - 1) % q:
        raise AssertionError("q did not divide the root factor sh-minus-one")

    local_d = m * p + 1 - h
    if local_d % q or (p * h + 1) % q:
        raise AssertionError("q-local stutter congruences changed")
    if (h * h - 1) % q == 0:
        raise AssertionError("control did not use a transverse q residue")
    if (m * s * s - s + 1) % q:
        raise AssertionError("root factor did not imply the m-polynomial filter")

    k, remainder = divmod(q + 1, s)
    if remainder or not (1 < k < q and k % 2 == 0 and h % q == k):
        raise AssertionError("factor gate did not recover the least even root residue")
    if (p + s) % q:
        raise AssertionError("root factor did not force q to divide p-plus-s")

    c, remainder = divmod(p + s, 4 * q)
    if remainder or c <= 0:
        raise AssertionError("factor gate did not recover integral terminal coordinates")
    n, remainder = divmod(p + s, s + 1)
    if remainder or not (0 < n < p):
        raise AssertionError("factor gate did not recover a strict source denominator")

    target = (q * c, p * c * k, p * q * c * k)
    source = (q * c, c * k, q * c * k)
    if sum(Fraction(1, value) for value in target) != Fraction(4, p):
        raise AssertionError("factor-gate target certificate changed")
    if sum(Fraction(1, value) for value in source) != Fraction(4, n):
        raise AssertionError("factor-gate source witness changed")
    if target != (source[0], p * source[1], p * source[2]):
        raise AssertionError("factor-gate two-tail lift changed")


def verify_m_polynomial_root_split(
    p: int, q: int, h: int, m: int, s: int, expect_positive: bool
) -> None:
    """Check the exact positive/negative root split of the m-side low-gap filter."""
    if not (is_prime(p) and p % 24 == 1 and is_prime(q) and q % 2 == 1):
        raise AssertionError("control did not use a core prime and odd q")
    if s not in LOW_GAPS or q % (2 * s) != 2 * s - 1:
        raise AssertionError("control did not meet the low-gap q residue")

    local_d = m * p + 1 - h
    if local_d % q or (p * h + 1) % q:
        raise AssertionError("q-local stutter congruences changed")
    if (h * h - 1) % q == 0:
        raise AssertionError("control did not use a transverse q residue")

    delta = m * s * s - s + 1
    positive_root = s * h - 1
    negative_root = s * (h - 1) + 1
    if delta + positive_root * negative_root != s * s * (m + h * (h - 1)):
        raise AssertionError("m-polynomial root identity changed")
    if delta % q:
        raise AssertionError("control did not enter the m-polynomial split")

    positive_hit = positive_root % q == 0
    negative_hit = negative_root % q == 0
    if positive_hit == negative_hit or positive_hit != expect_positive:
        raise AssertionError("m-polynomial root split did not select the expected branch")

    k, remainder = divmod(q + 1, s)
    if remainder or not (1 < k < q and k % 2 == 0):
        raise AssertionError("low-gap residue did not recover the even K")
    if (m + k * (k - 1)) % q:
        raise AssertionError("both roots must retain the quadratic shift")

    positive_factor = k * p + 1
    negative_factor = (k - 1) * p - 1
    if expect_positive:
        if h % q != k or positive_factor % q or negative_factor % q == 0:
            raise AssertionError("positive root did not select the known terminal branch")
    else:
        if (1 - h) % q != k or negative_factor % q or positive_factor % q == 0:
            raise AssertionError("negative root did not select the unresolved branch")


def verify() -> None:
    # These are q-local controls, not assertions of actual root receipts.
    verify_a_one_factor_gate(337, 17, 6, 4, 3)
    verify_a_one_factor_gate(97, 13, 15, 11, 7)
    verify_q_local_root_residue_low_gap(97, 1, 13, 15, 11)
    verify_q_local_root_residue_low_gap(1297, 5, 13, 9, 6)
    verify_m_polynomial_root_split(337, 17, 6, 4, 3, expect_positive=True)
    verify_m_polynomial_root_split(433, 11, 30, 10, 3, expect_positive=False)
    print("verified q-local root-residue gates, strict descents, and m-root split")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
