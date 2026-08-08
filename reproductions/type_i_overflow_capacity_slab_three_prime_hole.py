#!/usr/bin/env python3
"""Verify the three-prime dual bounded-divisor hole classification."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    d: int
    denominator: int
    carrier: int
    support: int
    cofactor: int
    residue: int
    terminal: tuple[int, int, int, int]


FIXTURES = (
    Fixture("p73", 73, 13, 1461, 2051, 293, 7, 7, (20, 219, 4380, 7)),
    Fixture("p673", 673, 647, 830_325, 215_923, 821, 263, 563,
            (170, 16_345, 374_006_290, 7)),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def divisors(value: int) -> tuple[int, ...]:
    factors: list[int] = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append(remaining)

    result = [1]
    for factor in factors:
        result.extend(item * factor for item in tuple(result))
    return tuple(sorted(set(result)))


def verify_terminal(prime: int, terminal: tuple[int, int, int, int]) -> None:
    x, y, z, gap = terminal
    if not (
        gap == 7
        and 4 * x == prime + gap
        and Fraction(4, prime) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
    ):
        raise AssertionError(f"{prime}: terminal certificate changed")


def audit(fixture: Fixture) -> None:
    p = fixture.prime
    d = fixture.d
    n = fixture.denominator
    M = fixture.carrier
    A = fixture.support
    b = fixture.cofactor
    r = fixture.residue
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4

    if not (is_prime(p) and p % 24 == 1 and p * n == 4 * M * d + 1):
        raise AssertionError(f"{fixture.name}: determinant gate changed")
    if not (B < M < 2 * B and c <= A <= B and M == A * b):
        raise AssertionError(f"{fixture.name}: capacity/support gate changed")
    if not (1 < b <= d and d * b >= p):
        raise AssertionError(f"{fixture.name}: residual gate changed")
    if not (
        is_prime(A)
        and is_prime(b)
        and is_prime(d)
        and len({A, b, d}) == 3
        and b <= A
        and d <= A
        and A * d > B
        and ((b * d <= A) or (b * d > B))
    ):
        raise AssertionError(f"{fixture.name}: three-prime fixed-n hypotheses changed")
    if not (
        r == M % p
        and is_prime(r)
        and is_prime(d)
        and r != d
        and r <= A
        and d <= A
        and ((r * d <= A) or (r * d > B))
        and (4 * r * d + 1) % p == 0
    ):
        raise AssertionError(f"{fixture.name}: fixed-s hypotheses changed")

    fixed_n = divisors(M * d)
    fixed_s = divisors(r * d)
    if any(A < divisor <= B for divisor in fixed_n):
        raise AssertionError(f"{fixture.name}: fixed-n hole closed unexpectedly")
    if any(A < divisor <= B for divisor in fixed_s):
        raise AssertionError(f"{fixture.name}: fixed-s hole closed unexpectedly")
    if any(A < divisor <= B and B // divisor < B // A for divisor in fixed_n):
        raise AssertionError(f"{fixture.name}: fixed-n rank filter changed")
    if any(
        A < divisor <= B and 4 * divisor > (4 * r * d + 1) // p
        and B // divisor < B // A
        for divisor in fixed_s
    ):
        raise AssertionError(f"{fixture.name}: fixed-s selector filter changed")

    verify_terminal(p, fixture.terminal)


def verify() -> None:
    for fixture in FIXTURES:
        audit(fixture)
    print(f"verified {len(FIXTURES)} three-prime dual bounded-divisor hole receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
