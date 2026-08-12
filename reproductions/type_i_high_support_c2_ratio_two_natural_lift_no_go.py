#!/usr/bin/env python3
"""Verify the parity-free C=2 ratio-two natural-lift no-go."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd

import sympy


def c2_chart(prime: int) -> dict[str, int]:
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise ValueError("expected a core prime")
    U = (prime - 1) // 4
    R = 8 * U - 1
    K = U * (8 * U + 1)
    L = 2 * K
    if not (R == 2 * prime - 3 and 4 * K == prime * R + 1):
        raise AssertionError("C=2 chart identity failed")
    return {"p": prime, "U": U, "R": R, "K": K, "L": L}


def marked_lift_data(R: int, K: int, E: int, p: int) -> dict[str, int]:
    if not (
        R > 1
        and 4 * K == p * R + 1
        and (4 * K * K) % E == 0
        and E % R == 1
        and 0 < E < 4 * K
    ):
        raise AssertionError("invalid parity-free marked-lift input")
    numerator = 4 * K - E
    n, remainder = divmod(numerator, R)
    if remainder or n <= 0:
        raise AssertionError("predecessor was not integral and positive")
    alpha, remainder = divmod(n * K, E)
    if remainder or alpha <= 0:
        raise AssertionError("natural marker was not integral")
    if not (
        gcd(E, R) == 1
        and (n * R * K) % E == 0
        and Fraction(4, n) - Fraction(1, alpha) == Fraction(R, K)
        and Fraction(4, p) - Fraction(1, p * K) == Fraction(R, K)
    ):
        raise AssertionError("parity-free marked-lift identities failed")
    return {"E": E, "n": n, "alpha": alpha}


def centered_divisors(U: int) -> tuple[int, ...]:
    R = 8 * U - 1
    K = U * (8 * U + 1)
    return tuple(
        divisor
        for divisor in sympy.divisors(K * K)
        if divisor < K and (divisor + K) % R == 0
    )


def ratio_two_data(chart: dict[str, int], a: int, b: int) -> dict[str, int]:
    R, K, L, p = chart["R"], chart["K"], chart["L"], chart["p"]
    if not (
        a > 0
        and b > 0
        and L % a == 0
        and L % b == 0
        and gcd(a, b) == 1
        and (a - 2 * b) % R == 0
        and a < 2 * b
    ):
        raise AssertionError("invalid ratio-two divisor pair")
    E, remainder = divmod(L * a, b)
    if remainder:
        raise AssertionError("ratio-two E was not integral")
    row = marked_lift_data(R, K, E, p)
    if not (E % R == 1 and E < 2 * L and row["n"] < p):
        raise AssertionError("ratio-two range or congruence failed")
    return {"a": a, "b": b, **row}


def verify() -> None:
    # These controls exercise the Vieta no-go independently of any finite box.
    for U in range(1, 65):
        if centered_divisors(U):
            raise AssertionError(f"U={U} acquired a centered divisor")

    p73 = c2_chart(73)
    even = ratio_two_data(p73, a=4, b=145)
    if even != {"a": 4, "b": 145, "E": 144, "n": 72, "alpha": 1305}:
        raise AssertionError("C=2 natural even predecessor changed")

    p12409 = c2_chart(12409)
    odd = ratio_two_data(p12409, a=1081, b=12948)
    if p12409 != {
        "p": 12409,
        "U": 3102,
        "R": 24815,
        "K": 76982334,
        "L": 153964668,
    } or odd != {
        "a": 1081,
        "b": 12948,
        "E": 12854171,
        "n": 11891,
        "alpha": 71214,
    }:
        raise AssertionError("strict odd C=2 ratio-two control changed")
    if not (
        odd["E"] % 2 == 1
        and odd["n"] % 2 == 1
        and not centered_divisors(p12409["U"])
    ):
        raise AssertionError("odd control no longer demonstrates the no-go")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused theorem controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()
    print("verified parity-free C=2 ratio-two natural-lift no-go")
    print("p=12409: E=12854171 n=11891 alpha=71214 marked_source=empty")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
