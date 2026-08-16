#!/usr/bin/env python3
"""Verify strict Q-carried quadratic external-source controls.

The receipt checks fixed controls only. It includes one q=3 strict-Q
lift and one valid non-strict square-factor boundary; it performs no scan.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


@dataclass(frozen=True)
class Fixture:
    prime: int
    k: int
    expected_strict: tuple[int, ...]
    non_strict_square: int | None = None


FIXTURES = (
    Fixture(prime=73, k=1, expected_strict=(5,)),
    Fixture(prime=97, k=1, expected_strict=()),
    Fixture(prime=97, k=2, expected_strict=()),
    Fixture(prime=1_873, k=3, expected_strict=()),
    Fixture(prime=409, k=6, expected_strict=(), non_strict_square=63),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def positive_divisors(value: int) -> tuple[int, ...]:
    divisors: set[int] = set()
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor == 0:
            divisors.add(divisor)
            divisors.add(value // divisor)
    return tuple(sorted(divisors))


def verify_lift_and_certificate(
    prime: int,
    source_denominator: int,
    q: int,
    retained: int,
    square: int,
) -> None:
    if (retained + square) % q != 0 or retained * retained % square != 0:
        raise AssertionError("quadratic external-source factor condition changed")
    u = (retained + square) // q
    if retained * u % square != 0 or u * u % square != 0:
        raise AssertionError("quadratic tail ceased to be integral")
    v = retained * u // square
    gap = (4 * square + 1) // q
    divisor = u * u // square
    if not (
        Fraction(4, source_denominator)
        == Fraction(1, retained) + Fraction(1, u) + Fraction(1, v)
        and Fraction(4, prime)
        == Fraction(1, retained * prime) + Fraction(1, u) + Fraction(1, v)
        and 3 <= gap <= prime - 2
        and (prime * u + divisor) % gap == 0
        and (prime * u + divisor) // gap == v
        and prime * (u + prime * (u * u // divisor)) % gap == 0
        and prime * (u + prime * (u * u // divisor)) // gap == retained * prime
    ):
        raise AssertionError("quadratic marked lift or Type I certificate changed")


def audit(fixture: Fixture) -> tuple[int, int, int, int, tuple[int, ...]]:
    prime, k = fixture.prime, fixture.k
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and ((prime - 1) // 4) % k == 0
    ):
        raise AssertionError("core-prime scale control changed")

    q = 4 * k - 1
    carrier = (prime - 3) // 2
    numerator = q * prime + 1
    if numerator % (q + 1) != 0:
        raise AssertionError("source denominator ceased to be integral")
    denominator = numerator // (q + 1)
    retained = k * denominator
    square_common = gcd(carrier, retained * retained)
    capacity_common = gcd(carrier, (3 * q + 1) ** 2)
    strict = tuple(
        divisor
        for divisor in positive_divisors(carrier)
        if divisor <= retained
        and retained * retained % divisor == 0
        and (retained + divisor) % q == 0
    )
    capacity_candidates = tuple(
        divisor
        for divisor in positive_divisors(capacity_common)
        if (4 * divisor + 1) % q == 0
    )

    if not (
        carrier % 2 == 1
        and carrier < retained
        and square_common == capacity_common
        and strict == capacity_candidates == fixture.expected_strict
    ):
        raise AssertionError("strict Q-carried square capacity changed")

    if k == 1:
        if not (
            q == 3
            and (strict == (5,)) == (prime % 120 == 73)
        ):
            raise AssertionError("q=3 strict-Q exception classification changed")
    elif not (q >= 7 and not strict):
        raise AssertionError("k>=2 strict-Q square no-go changed")

    for square in strict:
        verify_lift_and_certificate(prime, denominator, q, retained, square)

    if fixture.non_strict_square is not None:
        square = fixture.non_strict_square
        if not (
            carrier % square != 0
            and gcd(carrier, square) == 7
            and square <= retained
        ):
            raise AssertionError("non-strict square boundary changed")
        verify_lift_and_certificate(prime, denominator, q, retained, square)

    return prime, k, q, square_common, strict


def verify() -> None:
    receipts = tuple(audit(fixture) for fixture in FIXTURES)
    if receipts != (
        (73, 1, 3, 5, (5,)),
        (97, 1, 3, 1, ()),
        (97, 2, 7, 1, ()),
        (1_873, 3, 11, 17, ()),
        (409, 6, 23, 7, ()),
    ):
        raise AssertionError("fixed strict-Q quadratic controls changed")
    print("verified strict-Q square classification and non-strict boundary")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the fixed square-factor controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
