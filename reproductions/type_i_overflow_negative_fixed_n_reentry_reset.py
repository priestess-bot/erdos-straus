#!/usr/bin/env python3
"""Verify focused negative fixed-n reentry-reset receipts.

The first three fixtures are complete arithmetic edges.  The fourth is a
sharp d_T < p boundary and is deliberately analysis-only.
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
    d: int
    denominator: int
    support: int
    selected: int
    expected_route: str
    expected_target: tuple[int, int, int] | None = None


FIXTURES = (
    Fixture("general_product_divisor", 73, 666, 2, 73, 1, 12, "edge", (12, 38, 25)),
    Fixture("support_preserving_reentry", 73, 1332, 1, 73, 6, 18, "edge", (18, 1, 1)),
    Fixture("prime_large_reset_reentry", 73, 1501, 4, 329, 19, 79, "edge", (79, 3, 13)),
    Fixture("long_excess_boundary", 97, 4040, 5, 833, 40, 101, "boundary"),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def audit(fixture: Fixture) -> str:
    p = fixture.prime
    M = fixture.carrier
    d = fixture.d
    n = fixture.denominator
    A = fixture.support
    L = fixture.selected
    B = (p - 1) ** 2 // 4

    if not (is_prime(p) and p % 24 == 1 and p * n == 4 * M * d + 1):
        raise AssertionError(f"{fixture.name}: source determinant changed")
    if not (1 <= A <= B and M % A == 0 and M * d % L == 0 and A < L <= B):
        raise AssertionError(f"{fixture.name}: support or divisor gate changed")
    if not (B // L < B // A and 4 * M - n > p):
        raise AssertionError(f"{fixture.name}: source rank or overflow changed")

    D = M * d // L - p
    u = n - 4 * L
    if p * u != 4 * L * D + 1:
        raise AssertionError(f"{fixture.name}: negative reentry identity changed")

    if 1 <= D < p:
        R = 4 * L - u
        K = L * (p - D)
        if not (
            u > 0
            and p * u == 4 * L * D + 1
            and 0 < R < 4 * L
            and R % 4 == 3
            and K > 0
            and 4 * K == p * R + 1
            and K % L == 0
            and (B // L) < (B // A)
        ):
            raise AssertionError(f"{fixture.name}: reentry target chart changed")
        target = (L, D, u)
        if target != fixture.expected_target or fixture.expected_route != "edge":
            raise AssertionError(f"{fixture.name}: reentry target changed")
        return "edge"

    if not (D >= p and u > 0 and fixture.expected_route == "boundary" and fixture.expected_target is None):
        raise AssertionError(f"{fixture.name}: long-excess boundary changed")
    return "boundary"


def verify() -> None:
    routes = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_route for fixture in FIXTURES}
    if routes != expected:
        raise AssertionError("negative fixed-n reentry receipt changed")
    print(f"verified {len(FIXTURES)} focused negative fixed-n reentry receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
