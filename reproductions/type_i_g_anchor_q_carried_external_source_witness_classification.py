#!/usr/bin/env python3
"""Verify the fixed controls for the G-anchor Q-carried witness classification.

The receipt checks one q=3 lift and three fixed empty-menu controls.
It does not scan prime ranges, denominators, or reachability histories.
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
    expected_common: int
    expected_witnesses: tuple[int, ...]


FIXTURES = (
    Fixture(prime=73, k=1, expected_common=5, expected_witnesses=(5,)),
    Fixture(prime=97, k=1, expected_common=1, expected_witnesses=()),
    Fixture(prime=97, k=2, expected_common=1, expected_witnesses=()),
    Fixture(prime=1_873, k=3, expected_common=17, expected_witnesses=()),
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


def audit(fixture: Fixture) -> tuple[int, int, int, int, tuple[int, ...]]:
    prime, k = fixture.prime, fixture.k
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and ((prime - 1) // 4) % k == 0
    ):
        raise AssertionError("core-prime external-source control changed")

    q = 4 * k - 1
    carrier = (prime - 3) // 2
    numerator = q * prime + 1
    if numerator % (q + 1) != 0:
        raise AssertionError("source denominator ceased to be integral")
    denominator = numerator // (q + 1)
    retained = k * denominator
    common = gcd(carrier, retained)
    witnesses = tuple(
        divisor
        for divisor in positive_divisors(common)
        if divisor > 1 and divisor % q == q - 1
    )

    if not (
        gcd(carrier, k) == gcd(carrier, q + 1) == 1
        and common == gcd(carrier, 3 * q + 1) == fixture.expected_common
        and witnesses == fixture.expected_witnesses
    ):
        raise AssertionError("Q-carried gcd classification changed")

    q_three_exception = k == 1 and prime % 120 == 73
    if k == 1:
        if not (
            q == 3
            and (witnesses == (5,)) == q_three_exception
            and (not witnesses or (5 <= denominator and denominator % 5 == 0))
        ):
            raise AssertionError("q=3 exception classification changed")
    elif not (q >= 7 and not witnesses):
        raise AssertionError("k>=2 Q-carried no-go changed")

    if witnesses:
        witness = witnesses[0]
        u_numerator = k * (denominator + witness)
        if u_numerator % q != 0:
            raise AssertionError("marked source tail ceased to be integral")
        u = u_numerator // q
        if denominator * u % witness != 0:
            raise AssertionError("marked source lift ceased to be integral")
        v = denominator * u // witness
        certificate_gap = (4 * k * witness + 1) // q
        certificate_divisor = u * u // (k * witness)
        if not (
            Fraction(4, denominator)
            == Fraction(1, retained) + Fraction(1, u) + Fraction(1, v)
            and Fraction(4, prime)
            == Fraction(1, retained * prime) + Fraction(1, u) + Fraction(1, v)
            and u * u % (k * witness) == 0
            and 3 <= certificate_gap <= prime - 2
            and (prime * u + certificate_divisor) % certificate_gap == 0
            and (prime * u + certificate_divisor) // certificate_gap == v
            and (u + prime * u * u // certificate_divisor) * prime
            == certificate_gap * retained * prime
        ):
            raise AssertionError("q=3 marked lift or Type I certificate changed")

    return prime, k, q, common, witnesses


def verify() -> None:
    receipts = tuple(audit(fixture) for fixture in FIXTURES)
    if receipts != (
        (73, 1, 3, 5, (5,)),
        (97, 1, 3, 1, ()),
        (97, 2, 7, 1, ()),
        (1_873, 3, 11, 17, ()),
    ):
        raise AssertionError("fixed Q-carried classification controls changed")
    print("verified q=3 exception, k>=2 no-go, and explicit marked lift")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the fixed classification controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
