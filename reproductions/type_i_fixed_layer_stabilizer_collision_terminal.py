#!/usr/bin/env python3
"""Verify focused stabilizer-collision and q-primary terminal receipts."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from math import gcd, prod


def units(modulus: int) -> set[int]:
    return {value for value in range(1, modulus) if gcd(value, modulus) == 1}


def subgroup(modulus: int, generators: tuple[int, ...]) -> set[int]:
    values = {1}
    while True:
        expanded = values | {
            value * generator % modulus
            for value in values
            for generator in generators
        }
        if expanded == values:
            return values
        values = expanded


def centered_layer(
    modulus: int, primes: tuple[int, ...], budgets: tuple[int, ...]
) -> set[int]:
    return {
        prod(pow(prime, exponent, modulus) for prime, exponent in zip(primes, vector))
        % modulus
        for vector in product(*(range(-budget, budget + 1) for budget in budgets))
    }


def stabilizer(modulus: int, group: set[int], layer: set[int]) -> set[int]:
    return {
        multiplier
        for multiplier in group
        if {multiplier * value % modulus for value in layer} == layer
    }


def coset(modulus: int, value: int, subgroup_values: set[int]) -> frozenset[int]:
    return frozenset(value * member % modulus for member in subgroup_values)


def residual_value(modulus: int, primes: tuple[int, ...], vector: tuple[int, ...]) -> int:
    return prod(pow(prime, exponent, modulus) for prime, exponent in zip(primes, vector)) % modulus


def sign_box(vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(0 if coordinate >= 0 else 1 for coordinate in vector)


def terminal_data(
    primes: tuple[int, ...],
    budgets: tuple[int, ...],
    relation: tuple[int, ...],
    K: int,
    R: int,
    p: int,
) -> tuple[int, int, int]:
    ratio = Fraction(1, 1)
    for prime, exponent in zip(primes, relation):
        if exponent >= 0:
            ratio *= prime**exponent
        else:
            ratio /= prime ** (-exponent)
    if ratio >= 1:
        relation = tuple(-exponent for exponent in relation)
        ratio = 1 / ratio
    assert ratio < 1
    exponents = tuple(budget + exponent for budget, exponent in zip(budgets, relation))
    assert all(0 <= exponent <= 2 * budget for exponent, budget in zip(exponents, budgets))
    U = prod(prime**exponent for prime, exponent in zip(primes, exponents))
    E = 4 * U
    n = (4 * K - E) // R
    assert E % R == 1 and E > 0 and E <= 4 * K - 4 * R
    assert 4 * K - E == R * n and 0 < n < p and n % 4 == 0
    return U, E, n


def verify_direct_quotient_collision() -> None:
    p, R, K = 73, 23, 420
    fixed_primes, fixed_budgets = (2, 3), (2, 1)
    residual_primes, residual_budgets = (5, 7), (1, 1)
    H = subgroup(R, fixed_primes + residual_primes)
    J = centered_layer(R, fixed_primes, fixed_budgets)
    P = stabilizer(R, H, J)
    assert H == units(R) and J == P and len(H) == 22 and len(P) == 11

    z, w = (1, 0), (0, 1)
    phi_z = residual_value(R, residual_primes, z)
    phi_w = residual_value(R, residual_primes, w)
    assert sign_box(z) == sign_box(w)
    assert coset(R, phi_z, P) == coset(R, phi_w, P)
    assert residual_value(R, residual_primes, (1, -1)) == 4

    image_cosets = {
        coset(R, residual_value(R, residual_primes, vector), P)
        for vector in product(*(range(-budget, budget + 1) for budget in residual_budgets))
    }
    assert 9 > 2 ** len(residual_primes) * len(image_cosets) == 8

    relation = (1, 1, 1, -1)
    assert residual_value(R, (2, 3, 5, 7), relation) == 1
    assert terminal_data((2, 3, 5, 7), (2, 1, 1, 1), relation, K, R, p) == (
        98,
        392,
        56,
    )


def verify_qprimary_terminal_upgrade() -> None:
    p, R, K = 433, 15, 1624
    fixed_primes, fixed_budgets = (29,), (1,)
    residual_primes, residual_budgets = (2, 7), (3, 1)
    H = subgroup(R, fixed_primes + residual_primes)
    J = centered_layer(R, fixed_primes, fixed_budgets)
    P = stabilizer(R, H, J)
    y = R - 1
    assert H == units(R) and J == P == {1, 14}
    assert len(H) // len(P) == 4

    records = [
        (fixed, vector, fixed * residual_value(R, residual_primes, vector) % R)
        for fixed in J
        for vector in product(*(range(-budget, budget + 1) for budget in residual_budgets))
    ]
    exact = [(fixed, vector) for fixed, vector, value in records if value == y]
    filtered = [
        (fixed, vector)
        for fixed, vector, value in records
        if value * pow(y, -1, R) % R in P
    ]
    threshold = len(J) * 2 ** len(residual_primes)
    quotient_threshold = len(J) // len(P) * 2 ** len(residual_primes)
    assert len(exact) == 5 and len(filtered) == 10
    assert len(exact) <= threshold < len(filtered)
    assert len(exact) > quotient_threshold == 4

    left, right = (1, (1, 1)), (14, (0, 0))
    assert (
        left[0] * residual_value(R, residual_primes, left[1]) % R
        == right[0] * residual_value(R, residual_primes, right[1]) % R
        == y
    )
    assert coset(R, left[0], P) == coset(R, right[0], P)
    assert sign_box(left[1]) == sign_box(right[1])
    assert residual_value(R, residual_primes, (1, 1)) == 14

    relation = (-1, 1, 1)
    assert residual_value(R, (29, 2, 7), relation) == 1
    assert terminal_data((29, 2, 7), (1, 3, 1), relation, K, R, p) == (
        784,
        3136,
        224,
    )


def verify_weak_saturation_boundary() -> None:
    _p, R, _K = 97, 67, 1625
    fixed_primes, fixed_budgets = (13,), (1,)
    residual_primes, residual_budgets = (5,), (3,)
    H = subgroup(R, fixed_primes + residual_primes)
    J = centered_layer(R, fixed_primes, fixed_budgets)
    P = stabilizer(R, H, J)
    K_X = {value * value % R for value in H}
    y = R - 1
    assert H == units(R) and J == {1, 13, 31} and P == {1}
    assert len(K_X) == 33 and len(H) // len(K_X) == 2

    records = [
        (fixed, vector, fixed * residual_value(R, residual_primes, vector) % R)
        for fixed in J
        for vector in product(*(range(-budget, budget + 1) for budget in residual_budgets))
    ]
    exact = sum(value == y for _, _, value in records)
    filtered = sum(value * pow(y, -1, R) % R in K_X for _, _, value in records)
    threshold = len(J) * 2 ** len(residual_primes)
    assert exact == 0 and filtered == 10 > threshold == 6
    assert filtered <= len(K_X) * threshold

    full_relations = [
        (fixed_exponent, residual_exponent)
        for fixed_exponent in range(-1, 2)
        for residual_exponent in range(-3, 4)
        if residual_value(R, (13, 5), (fixed_exponent, residual_exponent)) == 1
    ]
    assert full_relations == [(0, 0)]


def verify() -> None:
    verify_direct_quotient_collision()
    verify_qprimary_terminal_upgrade()
    verify_weak_saturation_boundary()
    print("verified stabilizer quotient collision and q-primary terminal receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run exact focused checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
