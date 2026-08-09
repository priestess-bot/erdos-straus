#!/usr/bin/env python3
"""Verify focused strict and stuttering cofactor mod-p folds."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    denominator: int
    carrier: int
    d: int
    support: int
    cofactor: int
    expected: tuple[int, int, int, int, int]
    high_capacity: bool
    strict: bool


FIXTURES = (
    Fixture(
        "prethreshold_residual",
        73,
        645,
        11771,
        1,
        149,
        79,
        (149, 6, 49, 547, 9983),
        True,
        True,
    ),
    Fixture(
        "prime_supercapacity_residual",
        73,
        1585,
        28926,
        1,
        18,
        1607,
        (18, 1, 1, 71, 1296),
        True,
        True,
    ),
    Fixture(
        "composite_exact_shell_gap",
        73,
        37617,
        686510,
        1,
        110,
        6241,
        (110, 36, 217, 223, 4070),
        True,
        True,
    ),
    Fixture(
        "dilated_total_cofactor",
        73,
        7553,
        68921,
        2,
        41,
        1681,
        (41, 4, 9, 155, 2829),
        True,
        True,
    ),
    Fixture(
        "proper_cofactor_strict",
        73,
        7553,
        68921,
        2,
        41,
        41,
        (1681, 9, 829, 5895, 107584),
        False,
        True,
    ),
    Fixture(
        "canonical_stutter_boundary",
        73,
        16057,
        4070,
        72,
        74,
        55,
        (74, 18, 73, 223, 4070),
        False,
        False,
    ),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def fold(fixture: Fixture) -> tuple[int, int, int, int, int]:
    p = fixture.prime
    n = fixture.denominator
    M = fixture.carrier
    d = fixture.d
    A = fixture.support
    g = fixture.cofactor
    B = (p - 1) ** 2 // 4

    assert is_prime(p) and p % 24 == 1
    assert p * n == 4 * M * d + 1
    assert 1 <= d < p and 1 <= A <= B and M % A == 0
    b = M // A
    assert b > 1 and g > 1 and b % g == 0
    assert (M * d) % p != 0

    h, delta = divmod(d * g, p)
    assert 1 <= delta < p
    target_M = M // g
    target_n = n - 4 * target_M * h
    target_R = 4 * target_M - target_n
    target_K = target_M * (p - delta)
    source_R = 4 * M - n
    source_K = M * (p - d)

    assert target_M % A == 0
    assert p * target_n == 4 * target_M * delta + 1
    assert 0 < target_n < 4 * target_M
    assert target_R > 0 and target_R % 4 == 3
    assert target_K > 0 and target_K % A == 0
    assert p * target_R + 1 == 4 * target_K
    assert p * source_R + 1 == 4 * source_K

    strict_gate = g * (p - d) > p
    assert (target_R < source_R) == strict_gate
    assert (target_R == source_R and target_K == source_K) == (not strict_gate)
    assert strict_gate == fixture.strict

    if fixture.high_capacity:
        assert M >= 2 * B and d * d < p and b >= 2 and g == b
        assert d * 2 < p and strict_gate

    target = (target_M, delta, target_n, target_R, target_K)
    assert target == fixture.expected
    return target


def verify() -> None:
    targets = {fixture.name: fold(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected for fixture in FIXTURES}
    assert targets == expected
    print(f"verified {len(FIXTURES)} focused cofactor mod-p fold receipts")
    print("strict_high_capacity", sum(item.high_capacity for item in FIXTURES))
    print("stutter_boundaries", sum(not item.strict for item in FIXTURES))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run exact focused checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
