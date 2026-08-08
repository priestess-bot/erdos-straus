#!/usr/bin/env python3
"""Verify focused boundary receipts for the high-carrier d-height staircase.

This is deliberately a small exact arithmetic check.  It does not scan primes
or replay the historical selector corpus; the proof is in the accompanying
claim card.  The fixtures exercise the first-strip d=1 dichotomy and the first
few threshold layers where d can exceed one.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    carrier: int
    denominator: int
    d: int
    support: int


FIXTURES = (
    Fixture("p73_first_strip_fixed_s_descent", 73, 1332, 73, 1, 6),
    Fixture("p73_first_strip_fixed_s_saturation", 73, 1332, 73, 1, 18),
    Fixture("p97_first_strip_fixed_s_descent", 97, 2352, 97, 1, 12),
    Fixture("p73_d2_first_height", 73, 1323, 145, 2, 1),
    Fixture("p73_d3_first_height", 73, 1320, 217, 3, 1),
    Fixture("p73_d4_congruence_delayed", 73, 1355, 297, 4, 1),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def threshold(prime: int, layer: int) -> int:
    if not 1 <= layer <= prime - 2:
        raise ValueError("layer is outside the stated staircase range")
    return layer * (prime - 2) + 1 + layer % 4


def audit(fixture: Fixture) -> str:
    p = fixture.prime
    M = fixture.carrier
    n = fixture.denominator
    d = fixture.d
    A = fixture.support
    B = (p - 1) ** 2 // 4

    if not (is_prime(p) and p % 24 == 1):
        raise AssertionError(f"{fixture.name}: not a core prime")
    if not (1 <= d < p and 1 <= A <= B and M % A == 0):
        raise AssertionError(f"{fixture.name}: support or d precondition changed")
    if p * n != 4 * M * d + 1 or M <= B or n % 4 != 1:
        raise AssertionError(f"{fixture.name}: high-carrier determinant changed")

    if d > (n - 1) // (p - 2):
        raise AssertionError(f"{fixture.name}: coarse height bound failed")
    for layer in range(1, min(d, p - 2) + 1):
        lower = threshold(p, layer)
        if lower % 4 != 1 or lower - 4 > layer * (p - 2):
            raise AssertionError(f"{fixture.name}: modular staircase formula changed")
        if n < lower:
            raise AssertionError(f"{fixture.name}: violated layer {layer}")

    if n >= 2 * p - 1:
        return "higher_layer"

    c = (p - 1) // 4
    r = M % p
    s, remainder = divmod(4 * r * d + 1, p)
    if remainder or not (p <= n <= 2 * p - 5 and d == 1):
        raise AssertionError(f"{fixture.name}: first-strip d=1 collapse failed")
    if (r, s, r * d) != (c, 1, c):
        raise AssertionError(f"{fixture.name}: first-strip fixed-s coordinates changed")

    chart_R = p - 2
    chart_K = B
    if 4 * chart_K != p * chart_R + 1:
        raise AssertionError(f"{fixture.name}: p-2 G chart changed")

    if A < c:
        L = c
        if not (
            (r * d) % L == 0
            and A < L <= B
            and 4 * L > s
            and B // L < B // A
        ):
            raise AssertionError(f"{fixture.name}: fixed-s descent gate changed")
        return "first_strip_fixed_s_descent"

    if A < c or any(divisor > A for divisor in range(1, c + 1) if c % divisor == 0):
        raise AssertionError(f"{fixture.name}: fixed-s saturation boundary changed")
    return "first_strip_fixed_s_empty"


def verify() -> None:
    routes = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {
        "p73_first_strip_fixed_s_descent": "first_strip_fixed_s_descent",
        "p73_first_strip_fixed_s_saturation": "first_strip_fixed_s_empty",
        "p97_first_strip_fixed_s_descent": "first_strip_fixed_s_descent",
        "p73_d2_first_height": "higher_layer",
        "p73_d3_first_height": "higher_layer",
        "p73_d4_congruence_delayed": "higher_layer",
    }
    if routes != expected:
        raise AssertionError("focused route receipt changed")
    if [threshold(73, layer) for layer in range(1, 5)] != [73, 145, 217, 285]:
        raise AssertionError("p=73 threshold staircase changed")
    print(f"verified {len(FIXTURES)} focused high-carrier height-staircase receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
