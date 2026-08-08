#!/usr/bin/env python3
"""Verify the five exact routes closing the small-d capacity window.

This is a focused receipt for the complete case split, not a range scan.
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
    expected_route: str
    expected_target: tuple[int, int, int] | None = None


FIXTURES = (
    Fixture("composite_factor", 73, 2050, 3, 337, 41, "factor", (205, 30, 337)),
    Fixture("small_prime_factor", 73, 1396, 2, 153, 698, "factor", (698, 4, 153)),
    Fixture("small_prime_exchange", 73, 2491, 2, 273, 53, "exchange", (106, 47, 273)),
    Fixture("prime_large_ordinary", 73, 2573, 1, 141, 31, "fold", (83, 31, 141)),
    Fixture("prime_large_long_fold", 97, 4040, 5, 833, 40, "fold", (101, 6, 25)),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def divisors(value: int) -> tuple[int, ...]:
    result: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        result.append(divisor)
        if divisor * divisor != value:
            result.append(value // divisor)
    return tuple(sorted(result))


def movable_factors(cofactor: int, d: int, prime: int) -> tuple[int, ...]:
    return tuple(g for g in divisors(cofactor) if 1 < g and d * g < prime)


def chart(prime: int, carrier: int, d: int, denominator: int, support: int) -> tuple[int, int]:
    R = 4 * carrier - denominator
    K = carrier * (prime - d)
    if not (
        prime * denominator == 4 * carrier * d + 1
        and 0 < R < 4 * carrier
        and R % 4 == 3
        and K > 0
        and 4 * K == prime * R + 1
        and carrier % support == 0
        and K % support == 0
    ):
        raise AssertionError("target chart changed")
    return R, K


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
    if not (
        B < M < 2 * B
        and c <= A <= B
        and M % A == 0
        and 2 * d * d <= p - 1
        and 4 * M - n > p
    ):
        raise AssertionError(f"{fixture.name}: capacity or support gate changed")

    b = M // A
    if not (1 < b < 2 * (p - 1) and b != p):
        raise AssertionError(f"{fixture.name}: cofactor range changed")
    source_rank = (B // A, M)

    if not is_prime(b):
        choices = movable_factors(b, d, p)
        if not choices:
            raise AssertionError(f"{fixture.name}: composite lost movable factor")
        g = max(choices)
        target = (M // g, d * g, n)
        route = "factor"
    elif b < p and b <= d:
        target = (M // b, d * b, n)
        route = "factor"
    elif b < p:
        target = (A * d, b, n)
        route = "exchange"
    else:
        h, delta = divmod(M * d // b, p)
        target = (b, delta, n - 4 * b * h)
        route = "fold"
        if not (b > 2 * A and A < b <= B and B // b < B // A and 1 <= delta < p):
            raise AssertionError(f"{fixture.name}: prime-large fold gate changed")

    if target != fixture.expected_target or route != fixture.expected_route:
        raise AssertionError(f"{fixture.name}: route target changed")
    R_target, _ = chart(p, target[0], target[1], target[2], target[0] if route == "fold" else A)
    if route == "fold":
        if not (B // target[0] < B // A):
            raise AssertionError(f"{fixture.name}: fold outer rank changed")
    elif not (target[0] < M and (B // A, target[0]) < source_rank):
        raise AssertionError(f"{fixture.name}: retained-support descent changed")
    if R_target <= 0:
        raise AssertionError(f"{fixture.name}: target positivity changed")
    return route


def verify() -> None:
    routes = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_route for fixture in FIXTURES}
    if routes != expected:
        raise AssertionError("small-d capacity closure receipt changed")
    print(f"verified {len(FIXTURES)} focused small-d capacity closure receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
