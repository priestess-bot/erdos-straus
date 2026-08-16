#!/usr/bin/env python3
"""Verify fixed controls for the Q-supported power external-source ray.

This receipt checks two prime points of p = 3913 + 15000*t. It does not
search for primes, denominators, or raw-path histories.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt


K = 6
Q_MODULUS = 23
POWER_PRIME = 5
POWER_EXPONENT = 7
POWER_FACTOR = POWER_PRIME**POWER_EXPONENT
SOURCE_POWER_LEVEL = POWER_PRIME**4
RAY_BASE = 3_913
RAY_STEP = 15_000
FIXTURE_T = (1, 4)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def reciprocal_sum(*denominators: int) -> Fraction:
    return sum((Fraction(1, value) for value in denominators), Fraction())


def ray_record(t: int) -> tuple[int, ...]:
    if t < 1:
        raise ValueError("the strict natural-gap control starts at t=1")

    a = 163 + 625 * t
    prime = RAY_BASE + RAY_STEP * t
    source = 625 * (23 * t + 6)
    retained = K * source
    carrier = (prime - 3) // 2
    u = 625 * (6 * t + 7)
    v = 30 * (23 * t + 6) * (6 * t + 7)
    gap = 13_587
    divisor = 5 * (6 * t + 7) ** 2

    if not (
        is_prime(prime)
        and gcd(RAY_BASE, RAY_STEP) == 1
        and (6 * K - 1) % POWER_PRIME == 0
        and pow(POWER_PRIME, POWER_EXPONENT, Q_MODULUS) == (-K) % Q_MODULUS
        and (Q_MODULUS * 163 + 1) % SOURCE_POWER_LEVEL == 0
        and prime == 4 * K * a + 1
        and prime % 24 == 1
        and ((prime - 1) // 4) % K == 0
        and source == (Q_MODULUS * prime + 1) // (Q_MODULUS + 1)
        and (Q_MODULUS + 1) * source == Q_MODULUS * prime + 1
        and carrier == 5 * (1_500 * t + 391)
        and carrier % POWER_PRIME == 0
        and (carrier // POWER_PRIME) % POWER_PRIME != 0
        and carrier % POWER_FACTOR != 0
        and POWER_FACTOR <= retained
        and retained * retained % POWER_FACTOR == 0
        and (retained + POWER_FACTOR) % Q_MODULUS == 0
        and POWER_FACTOR % Q_MODULUS == (-K) % Q_MODULUS
        and gap == (4 * POWER_FACTOR + 1) // Q_MODULUS
        and 4 * u - prime == gap
        and 3 <= gap <= prime - 2
        and u * u % POWER_FACTOR == 0
        and divisor == u * u // POWER_FACTOR
        and (prime * u + divisor) % gap == 0
        and (prime * u + divisor) // gap == v
        and prime * (u + prime * (u * u // divisor)) % gap == 0
        and prime * (u + prime * (u * u // divisor)) // gap == prime * retained
        and reciprocal_sum(retained, u, v) == Fraction(4, source)
        and reciprocal_sum(prime * retained, u, v) == Fraction(4, prime)
    ):
        raise AssertionError("Q-supported power witness or certificate changed")

    return (
        t,
        prime,
        source,
        retained,
        carrier,
        POWER_FACTOR,
        u,
        v,
        gap,
        divisor,
    )


def composite_record() -> tuple[int, ...]:
    """Replay the two-prime Q-supported control at k=6, q=23."""
    t = 16
    lattice = POWER_PRIME**2 * 7**3
    factor = POWER_PRIME**3 * 7**6
    a0 = 6_338
    a = a0 + lattice * t
    prime = 4 * K * a + 1
    source = Q_MODULUS * a + 1
    retained = K * source
    carrier = (prime - 3) // 2
    u = (retained + factor) // Q_MODULUS
    v = retained * u // factor
    gap = (4 * factor + 1) // Q_MODULUS
    divisor = u * u // factor

    if not (
        is_prime(prime)
        and gcd(152_113, 205_800) == 1
        and (6 * K - 1) % POWER_PRIME == 0
        and (6 * K - 1) % 7 == 0
        and factor % Q_MODULUS == (-K) % Q_MODULUS
        and (Q_MODULUS * a0 + 1) % lattice == 0
        and prime == 152_113 + 205_800 * t
        and prime % 24 == 1
        and source == lattice * (23 * t + 17)
        and (Q_MODULUS + 1) * source == Q_MODULUS * prime + 1
        and carrier == 35 * (2_173 + 2_940 * t)
        and carrier % 35 == 0
        and (carrier // 35) % POWER_PRIME != 0
        and (carrier // 35) % 7 != 0
        and carrier % factor != 0
        and factor <= retained
        and retained * retained % factor == 0
        and (retained + factor) % Q_MODULUS == 0
        and gap == 2_557_587
        and 4 * u - prime == gap
        and 3 <= gap <= prime - 2
        and u * u % factor == 0
        and (prime * u + divisor) % gap == 0
        and (prime * u + divisor) // gap == v
        and prime * (u + prime * (u * u // divisor)) % gap == 0
        and prime * (u + prime * (u * u // divisor)) // gap == prime * retained
        and reciprocal_sum(retained, u, v) == Fraction(4, source)
        and reciprocal_sum(prime * retained, u, v) == Fraction(4, prime)
    ):
        raise AssertionError("composite Q-supported witness or certificate changed")

    return (
        t,
        prime,
        source,
        retained,
        carrier,
        factor,
        u,
        v,
        gap,
        divisor,
    )


def verify() -> None:
    receipts = tuple(ray_record(t) for t in FIXTURE_T)
    if receipts != (
        (1, 18_913, 18_125, 108_750, 9_455, 78_125, 8_125, 11_310, 13_587, 845),
        (4, 63_913, 61_250, 367_500, 31_955, 78_125, 19_375, 91_140, 13_587, 4_805),
    ):
        raise AssertionError("fixed Q-supported power-ray controls changed")
    if composite_record() != (
        16,
        3_444_913,
        3_301_375,
        19_808_250,
        1_722_455,
        14_706_125,
        1_500_625,
        2_021_250,
        2_557_587,
        153_125,
    ):
        raise AssertionError("fixed composite Q-supported control changed")
    print("verified Q-supported prime-power and composite external-source controls")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run fixed ray controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
