#!/usr/bin/env python3
"""Verify the complete Q-supported external-source exclusion at p=14281."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from math import gcd, isqrt


PRIME = 14_281
HALF_QUARTER = (PRIME - 1) // 4
CARRIER = (PRIME - 3) // 2
SUPPORT_PRIMES = (11, 59)


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


def valuation(value: int, prime: int) -> int:
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def scale_record(k: int) -> tuple[int, int, int, int, tuple[int, int], tuple[int, ...]]:
    q = 4 * k - 1
    a = HALF_QUARTER // k
    source = q * a + 1
    retained = k * source
    exponents = tuple(valuation(retained, prime) for prime in SUPPORT_PRIMES)
    residues = {
        pow(11, alpha, q) * pow(59, beta, q) % q
        for alpha, beta in product(
            range(2 * exponents[0] + 1),
            range(2 * exponents[1] + 1),
        )
    }
    return k, q, source, retained, exponents, tuple(sorted(residues))


def verify() -> None:
    scale_divisors = divisors(HALF_QUARTER)
    records = tuple(scale_record(k) for k in scale_divisors)
    relevant = tuple(record for record in records if gcd(CARRIER, record[3]) > 1)
    support_scales = {
        prime: tuple(k for k in scale_divisors if (6 * k - 1) % prime == 0)
        for prime in SUPPORT_PRIMES
    }
    expected_relevant = (
        (2, 7, 12_496, 24_992, (1, 0), (1, 2, 4)),
        (10, 39, 13_924, 139_240, (0, 2), (1, 5, 10, 20, 22)),
        (35, 139, 14_179, 496_265, (1, 0), (1, 11, 121)),
        (255, 1_019, 14_267, 3_638_085, (1, 0), (1, 11, 121)),
        (
            1_190,
            4_759,
            14_278,
            16_990_820,
            (2, 1),
            (
                1,
                11,
                59,
                121,
                219,
                364,
                649,
                1_190,
                1_331,
                2_380,
                2_385,
                2_409,
                2_440,
                2_704,
                3_481,
            ),
        ),
    )
    targets = tuple((-record[0]) % record[1] for record in relevant)
    gap = 7
    first = (PRIME + gap) // 4
    divisor = 19
    source_denominator = (PRIME + gap) // (gap + 1)
    source_tail_one = (first + divisor) // gap
    source_tail_two = (first + first * first // divisor) // gap
    target_tail_one = PRIME * source_tail_one
    target_tail_two = PRIME * source_tail_two

    if not (
        is_prime(PRIME)
        and PRIME % 24 == 1
        and HALF_QUARTER == 3_570
        and CARRIER == 11**2 * 59
        and len(scale_divisors) == 32
        and support_scales == {11: (2, 35, 255, 1_190), 59: (10, 1_190)}
        and relevant == expected_relevant
        and targets == (5, 29, 104, 764, 3_569)
        and all(target not in record[-1] for target, record in zip(targets, relevant))
        and all(1 != (-k) % (4 * k - 1) for k in scale_divisors)
        and 3 <= gap <= PRIME - 2
        and first == 3_572
        and divisor <= first
        and first * first % divisor == 0
        and (first + divisor) % gap == 0
        and (gap + 1) * source_denominator == PRIME + gap
        and source_denominator == 1_786
        and source_denominator < PRIME
        and source_tail_one == 513
        and source_tail_two == 96_444
        and target_tail_one == 7_326_153
        and target_tail_two == 1_377_316_764
        and Fraction(4, source_denominator)
        == Fraction(1, first) + Fraction(1, source_tail_one) + Fraction(1, source_tail_two)
        and Fraction(4, PRIME)
        == Fraction(1, first) + Fraction(1, target_tail_one) + Fraction(1, target_tail_two)
    ):
        raise AssertionError("p=14281 full-scale Q-supported exclusion changed")
    print("verified the complete p=14281 Q-supported scale exclusion")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the complete finite control")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
