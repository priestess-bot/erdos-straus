#!/usr/bin/env python3
"""Verify the capacity-slab factor-threshold dichotomy on four exact rows."""

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
    expected_route: str


FIXTURES = (
    Fixture("large_cofactor_fold", 97, 4040, 5, 833, 40, "fold"),
    Fixture("small_cofactor_exchange", 73, 2491, 2, 273, 53, "exchange"),
    Fixture("below_factor_threshold", 73, 1396, 2, 153, 698, "factor"),
    Fixture("factor_threshold_residual", 73, 1309, 11, 789, 187, "residual"),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def smallest_prime_factor(value: int) -> int:
    if value % 2 == 0:
        return 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return divisor
    return value


def audit(fixture: Fixture) -> str:
    p = fixture.prime
    M = fixture.carrier
    d = fixture.d
    n = fixture.denominator
    A = fixture.support
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4

    if not (is_prime(p) and p % 24 == 1 and p * n == 4 * M * d + 1):
        raise AssertionError(f"{fixture.name}: source determinant changed")
    if not (B < M < 2 * B and c <= A <= B and M % A == 0 and 4 * M - n > p):
        raise AssertionError(f"{fixture.name}: capacity/support gate changed")

    b = M // A
    q = smallest_prime_factor(b)
    if not (1 < b < 2 * (p - 1) and b != p):
        raise AssertionError(f"{fixture.name}: cofactor range changed")

    if b > p:
        h, delta = divmod(M * d // b, p)
        n_target = n - 4 * b * h
        if not (b > 2 * A and A < b <= B and B // b < B // A and 1 <= delta < p and n_target > 0):
            raise AssertionError(f"{fixture.name}: quotient-fold gate changed")
        route = "fold"
    elif b > d:
        if not (b < p and A * d < M):
            raise AssertionError(f"{fixture.name}: exchange gate changed")
        route = "exchange"
    elif d * q < p:
        if not (q > 1 and b % q == 0):
            raise AssertionError(f"{fixture.name}: factor gate changed")
        route = "factor"
    else:
        if not (1 < b <= d and d * q >= p):
            raise AssertionError(f"{fixture.name}: residual gate changed")
        route = "residual"

    if route != fixture.expected_route:
        raise AssertionError(f"{fixture.name}: route changed")
    return route


def verify() -> None:
    routes = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_route for fixture in FIXTURES}
    if routes != expected:
        raise AssertionError("capacity-slab factor-threshold receipt changed")
    print(f"verified {len(FIXTURES)} focused capacity-slab factor-threshold receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
