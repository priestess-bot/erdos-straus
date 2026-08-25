#!/usr/bin/env python3
"""Verify the R=3 G hard-core arithmetic partition and mixed-gap control."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor <= isqrt(value):
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def jacobi(a: int, modulus: int) -> int:
    """Return the Jacobi symbol for positive odd modulus."""
    if modulus <= 0 or modulus % 2 == 0:
        raise ValueError("Jacobi modulus must be positive and odd")
    a %= modulus
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if modulus % 8 in (3, 5):
                result = -result
        a, modulus = modulus, a
        if a % 4 == modulus % 4 == 3:
            result = -result
        a %= modulus
    return result if modulus == 1 else 0


def square_divisors(value: int) -> list[int]:
    divisors = [1]
    for prime, exponent in factorization(value).items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(2 * exponent + 1)
        ]
    return sorted(divisors)


def all_divisors(value: int) -> list[int]:
    divisors = [1]
    for prime, exponent in factorization(value).items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def mixed_gap_targets(prime: int, h: int) -> tuple[int, int, int, int]:
    """Return m, x, and the complete Type I/II residues for m=3h."""
    P = prime + 4
    if P % h or gcd(h, 3) != 1:
        raise AssertionError("h is not an admissible P divisor")
    m = 3 * h
    if m % 4 != 3 or not (3 <= m <= prime - 2):
        raise AssertionError("P-derived gap is not legal")
    x = (prime + m) // 4
    if 4 * x != prime + m:
        raise AssertionError("mixed gap first denominator changed")
    type_i = (-pow(4, -1, m)) % m
    type_ii = (-x) % m
    return m, x, type_i, type_ii


def parity_profiles(target: int, residues: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    profiles: set[tuple[int, int, int]] = set()
    for first in range(2):
        for second in range(2):
            for third in range(2):
                product = 1
                for residue, exponent in zip(residues, (first, second, third)):
                    if exponent:
                        product = (product * residue) % 24
                if product == target:
                    profiles.add((first, second, third))
    return profiles


def check_character_and_parity_partitions() -> None:
    minus = {2, 3, 4, 6, 9}
    plus = {1, 5, 8, 10}
    for residue in range(1, 11):
        if residue == 7:
            continue
        sign = jacobi(residue + 4, 11)
        if (residue in minus and sign != -1) or (residue in plus and sign != 1):
            raise AssertionError("11-character partition changed")
    if parity_profiles(5, (5, 13, 17)) != {(1, 0, 0), (0, 1, 1)}:
        raise AssertionError("P modulo-24 parity partition changed")
    expected_n = {
        1: {(0, 0, 0), (1, 1, 1)},
        19: {(0, 0, 1), (1, 1, 0)},
        13: {(0, 1, 0), (1, 0, 1)},
        7: {(1, 0, 0), (0, 1, 1)},
    }
    for target, profiles in expected_n.items():
        if parity_profiles(target, (7, 13, 19)) != profiles:
            raise AssertionError("N modulo-24 parity partition changed")


def check_hard_core_control_and_mixed_gap_misses() -> None:
    prime = 118_801
    P = prime + 4
    N = (3 * prime + 1) // 4
    X = (prime + 3) // 4
    if not (
        prime % 24 == 1
        and factorization(P) == {5: 1, 23_761: 1}
        and factorization(N) == {89_101: 1}
        and factorization(X) == {7: 1, 4_243: 1}
        and all(q % 4 == 1 for q in factorization(P))
        and all(q % 3 == 1 for q in factorization(N))
    ):
        raise AssertionError("hard-core control factorization changed")
    if not (
        3 * P - 4 * N == 11
        and gcd(P, N) == 1
        and prime % 11 != 7
        and jacobi(33, N) == jacobi(P, 11)
    ):
        raise AssertionError("hard-core 11 bridge changed")

    legal_h = [h for h in all_divisors(P) if 3 <= 3 * h <= prime - 2]
    if legal_h != [1, 5, 23_761]:
        raise AssertionError("P divisor menu changed")
    for h in legal_h:
        m, x, type_i, type_ii = mixed_gap_targets(prime, h)
        residues = {divisor % m for divisor in square_divisors(x)}
        bounded = {divisor % m for divisor in square_divisors(x) if divisor <= x}
        if type_i in residues or type_ii in bounded:
            raise AssertionError("P-derived control gap unexpectedly hits")
        if h > 1:
            expected_i_h = (-pow(4, -1, h)) % h
            if not (
                type_i % 3 == 2
                and type_i % h == expected_i_h
                and type_ii % 3 == 2
                and type_ii % h == 1
            ):
                raise AssertionError("mixed residue CRT split changed")


def verify() -> None:
    check_character_and_parity_partitions()
    check_hard_core_control_and_mixed_gap_misses()
    print("verified R=3 G hard-core character and P-min mixed-gap partition")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
