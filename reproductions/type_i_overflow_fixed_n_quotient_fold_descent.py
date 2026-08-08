#!/usr/bin/env python3
"""Verify focused fixed-n quotient-fold descent receipts.

The fixtures cover both sides of S/L relative to p and a long quotient fold.
They are exact arithmetic receipts, not a scan.
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
    expected_target: tuple[int, int, int]


FIXTURES = (
    Fixture("ordinary_positive_fixed_n", 73, 1332, 1, 73, 6, 666, (666, 2, 73)),
    Fixture("product_divisor_single_fold", 73, 666, 2, 73, 1, 12, (12, 38, 25)),
    Fixture("support_preserving_single_fold", 73, 1332, 1, 73, 6, 18, (18, 1, 1)),
    Fixture("long_quotient_fold", 97, 4040, 5, 833, 40, 101, (101, 6, 25)),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def audit(fixture: Fixture) -> tuple[int, int, int]:
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
        raise AssertionError(f"{fixture.name}: support/divisor gate changed")
    if not (B // L < B // A and 4 * M - n > p):
        raise AssertionError(f"{fixture.name}: source rank or overflow changed")

    quotient = M * d // L
    h, delta = divmod(quotient, p)
    n_target = n - 4 * L * h
    if not (1 <= delta < p and n_target > 0):
        raise AssertionError(f"{fixture.name}: quotient normalization changed")

    R = 4 * L - n_target
    K = L * (p - delta)
    if not (
        p * n_target == 4 * L * delta + 1
        and 0 < R < 4 * L
        and R % 4 == 3
        and K > 0
        and 4 * K == p * R + 1
        and K % L == 0
        and (B // L) < (B // A)
    ):
        raise AssertionError(f"{fixture.name}: folded target chart changed")

    target = (L, delta, n_target)
    if target != fixture.expected_target:
        raise AssertionError(f"{fixture.name}: target coordinates changed")
    return target


def verify() -> None:
    targets = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_target for fixture in FIXTURES}
    if targets != expected:
        raise AssertionError("fixed-n quotient-fold receipt changed")
    print(f"verified {len(FIXTURES)} focused fixed-n quotient-fold descent receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
