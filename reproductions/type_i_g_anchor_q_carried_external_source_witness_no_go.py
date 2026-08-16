#!/usr/bin/env python3
"""Verify that a G-anchor Q-carried factor cannot be an external witness.

The controls are fixed core primes. They do not scan prime ranges,
denominators, or reachability histories.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class Fixture:
    prime: int
    k: int
    q: int
    expected_common: int


FIXTURES = (
    Fixture(prime=73, k=2, q=7, expected_common=1),
    Fixture(prime=1_873, k=3, q=11, expected_common=17),
)


def jacobi(numerator: int, denominator: int) -> int:
    if denominator <= 0 or denominator % 2 == 0 or gcd(numerator, denominator) != 1:
        raise ValueError("Jacobi symbol requires coprime odd positive inputs")
    numerator %= denominator
    result = 1
    while numerator:
        while numerator % 2 == 0:
            numerator //= 2
            if denominator % 8 in (3, 5):
                result = -result
        numerator, denominator = denominator, numerator
        if numerator % 4 == denominator % 4 == 3:
            result = -result
        numerator %= denominator
    return result if denominator == 1 else 0


def positive_divisors(value: int) -> tuple[int, ...]:
    divisors: set[int] = set()
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor == 0:
            divisors.add(divisor)
            divisors.add(value // divisor)
    return tuple(sorted(divisors))


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def audit(fixture: Fixture) -> tuple[int, int, int, tuple[int, ...]]:
    prime, k, q = fixture.prime, fixture.k, fixture.q
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and q == 4 * k - 1
        and ((prime - 1) // 4) % k == 0
        and (q * prime + 1) % (q + 1) == 0
    ):
        raise AssertionError("external-source parameter control changed")

    radius = prime - 2
    carrier = (prime - 3) // 2
    denominator = (q * prime + 1) // (q + 1)
    retained = k * denominator
    common = gcd(carrier, retained)

    if not (
        carrier % q == 0
        and q >= 7
        and 0 < denominator < prime
        and radius % q == 1
        and radius % 4 == q % 4 == 3
        and jacobi(q, radius) == -1
        and gcd(carrier, k) == gcd(carrier, q + 1) == 1
        and common == gcd(carrier, 3 * q + 1) == fixture.expected_common
    ):
        raise AssertionError("G-anchor/external-source gcd identity changed")

    witnesses = positive_divisors(common)
    if any(witness % q == q - 1 for witness in witnesses):
        raise AssertionError("a Q-carried external-source witness appeared")
    return prime, q, common, witnesses


def verify() -> None:
    receipts = tuple(audit(fixture) for fixture in FIXTURES)
    if receipts != (
        (73, 7, 1, (1,)),
        (1_873, 11, 17, (1, 17)),
    ):
        raise AssertionError("G-anchor external-source witness controls changed")
    print("verified 2 G-anchor Q/external-source intersections and no Q-carried witness")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the fixed G-anchor controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
