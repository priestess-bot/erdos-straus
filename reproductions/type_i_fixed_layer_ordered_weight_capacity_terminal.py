#!/usr/bin/env python3
"""Verify ordered-weight capacity and the Davenport dilation boundary."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import prod


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
        residual_value(modulus, primes, vector)
        for vector in product(*(range(-budget, budget + 1) for budget in budgets))
    }


def stabilizer(modulus: int, group: set[int], layer: set[int]) -> set[int]:
    return {
        multiplier
        for multiplier in group
        if {multiplier * value % modulus for value in layer} == layer
    }


def residual_value(
    modulus: int, generators: tuple[int, ...], vector: tuple[int, ...]
) -> int:
    return prod(
        pow(generator, exponent, modulus)
        for generator, exponent in zip(generators, vector)
    ) % modulus


def sign_box(vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(0 if coordinate >= 0 else 1 for coordinate in vector)


def sign_box_sizes(budgets: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        prod(
            budget + 1 if sign == 0 else budget
            for budget, sign in zip(budgets, signs)
        )
        for signs in product((0, 1), repeat=len(budgets))
    )


def coset(modulus: int, value: int, period: set[int]) -> frozenset[int]:
    return frozenset(value * member % modulus for member in period)


def quotient_product(
    modulus: int,
    left: frozenset[int],
    right: frozenset[int],
    period: set[int],
) -> frozenset[int]:
    return coset(modulus, min(left) * min(right) % modulus, period)


def quotient_capacity(
    modulus: int,
    fixed_layer: set[int],
    period: set[int],
    kernel: set[int],
    residual_generators: tuple[int, ...],
    budgets: tuple[int, ...],
    target: int,
) -> dict[str, object]:
    residual_group = subgroup(modulus, residual_generators)
    quotient_group = {coset(modulus, value, period) for value in residual_group}
    quotient_fixed = {coset(modulus, value, period) for value in fixed_layer}
    quotient_kernel = {coset(modulus, value, period) for value in kernel}
    quotient_target = coset(modulus, target, period)
    target_kernel = {
        quotient_product(modulus, quotient_target, value, period)
        for value in quotient_kernel
    }

    weights = {
        value: sum(
            quotient_product(modulus, fixed, value, period) in target_kernel
            for fixed in quotient_fixed
        )
        for value in quotient_group
    }
    ordered_weights = sorted(weights.values(), reverse=True)
    box_sizes = sign_box_sizes(budgets)
    quotient_order = len(quotient_group)
    box_overflow = max(box_sizes) > quotient_order
    theta_ordered_capped = len(period) * sum(
        sum(ordered_weights[: min(size, quotient_order)]) for size in box_sizes
    )

    multiplicities: dict[tuple[int, ...], Counter[frozenset[int]]] = defaultdict(Counter)
    filtered = 0
    target_inverse = pow(target, -1, modulus)
    for vector in product(*(range(-budget, budget + 1) for budget in budgets)):
        value = residual_value(modulus, residual_generators, vector)
        quotient_value = coset(modulus, value, period)
        multiplicities[sign_box(vector)][quotient_value] += 1
        eligible_fixed = sum(
            fixed * value * target_inverse % modulus in kernel
            for fixed in fixed_layer
        )
        assert eligible_fixed == len(period) * weights[quotient_value]
        filtered += eligible_fixed

    theta_actual = len(period) * sum(
        weights[value]
        for counts in multiplicities.values()
        for value in counts
    )
    weighted_surplus = len(period) * sum(
        weights[value] * (multiplicity - 1)
        for counts in multiplicities.values()
        for value, multiplicity in counts.items()
    )
    assert filtered - theta_actual == weighted_surplus

    direct_collisions = [
        (signs, value, multiplicity)
        for signs, counts in multiplicities.items()
        for value, multiplicity in counts.items()
        if multiplicity > 1
    ]

    intersection_order = len(quotient_group & quotient_kernel)
    group_kernel = {
        quotient_product(modulus, group_value, kernel_value, period)
        for group_value in quotient_group
        for kernel_value in quotient_kernel
    }
    target_group_kernel = {
        quotient_product(modulus, quotient_target, value, period)
        for value in group_kernel
    }
    target_fixed_mass = len(quotient_fixed & target_group_kernel)
    total_weight = sum(weights.values())
    assert total_weight == intersection_order * target_fixed_mass
    coarse_capacity = (
        len(period)
        * (2 ** len(budgets))
        * intersection_order
        * target_fixed_mass
    )
    strong_threshold = (
        len(quotient_kernel)
        * len(fixed_layer)
        * (2 ** len(budgets))
    )
    assert theta_ordered_capped <= coarse_capacity <= strong_threshold

    return {
        "filtered": filtered,
        "weights": weights,
        "weight_spectrum": Counter(weights.values()),
        "box_sizes": box_sizes,
        "quotient_order": quotient_order,
        "box_overflow": box_overflow,
        "theta_ordered_capped": theta_ordered_capped,
        "theta_actual": theta_actual,
        "weighted_surplus": weighted_surplus,
        "direct_collisions": direct_collisions,
        "intersection_order": intersection_order,
        "target_fixed_mass": target_fixed_mass,
        "coarse_capacity": coarse_capacity,
        "strong_threshold": strong_threshold,
    }


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
        ratio *= Fraction(prime**max(exponent, 0), prime**max(-exponent, 0))
    if ratio >= 1:
        relation = tuple(-exponent for exponent in relation)
        ratio = 1 / ratio
    exponents = tuple(
        budget + exponent for budget, exponent in zip(budgets, relation)
    )
    assert ratio < 1 and all(
        0 <= exponent <= 2 * budget
        for exponent, budget in zip(exponents, budgets)
    )
    U = prod(prime**exponent for prime, exponent in zip(primes, exponents))
    E = 4 * U
    n = (4 * K - E) // R
    assert E % R == 1 and 4 * K - E == R * n
    assert 0 < n < p and n % 4 == 0
    return U, E, n


def is_prime_64(value: int) -> bool:
    if value < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if value % prime == 0:
            return value == prime
    odd_part = value - 1
    twos = 0
    while odd_part % 2 == 0:
        twos += 1
        odd_part //= 2
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        witness = pow(base, odd_part, value)
        if witness in (1, value - 1):
            continue
        for _ in range(twos - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def verify_zero_weight_collision() -> None:
    p, R, K = 2089, 7, 3656
    fixed_layer = {1}
    period = {1}
    kernel = {1}
    stats = quotient_capacity(
        R, fixed_layer, period, kernel, (2, 457), (3, 1), 2
    )

    assert is_prime_64(p) and p % 24 == 1 and 4 * K == p * R + 1
    unit_coset = coset(R, 1, period)
    assert stats["weights"][unit_coset] == 0
    assert any(
        signs == (0, 0) and value == unit_coset and multiplicity == 3
        for signs, value, multiplicity in stats["direct_collisions"]
    )
    assert terminal_data((2, 457), (3, 1), (3, 0), K, R, p) == (
        457,
        1828,
        1828,
    )


def verify_p97_boundary() -> None:
    _p, R, _K = 97, 67, 1625
    fixed_layer = centered_layer(R, (13,), (1,))
    group = subgroup(R, (13, 5))
    period = stabilizer(R, group, fixed_layer)
    kernel = {value * value % R for value in group}
    stats = quotient_capacity(R, fixed_layer, period, kernel, (5,), (3,), R - 1)

    assert fixed_layer == {1, 13, 31} and period == {1}
    assert stats["quotient_order"] == 22
    assert stats["weight_spectrum"] == Counter({2: 11, 1: 11})
    assert stats["box_sizes"] == (4, 3)
    assert stats["theta_ordered_capped"] == 14
    assert stats["filtered"] == 10
    assert stats["theta_actual"] == 10
    assert stats["weighted_surplus"] == 0
    assert not stats["direct_collisions"]
    assert stats["coarse_capacity"] == 66
    assert stats["strong_threshold"] == 198

    full_relations = [
        (fixed_exponent, residual_exponent)
        for fixed_exponent in range(-1, 2)
        for residual_exponent in range(-3, 4)
        if residual_value(
            R, (13, 5), (fixed_exponent, residual_exponent)
        ) == 1
    ]
    assert full_relations == [(0, 0)]


def verify_p433_terminal() -> None:
    p, R, K = 433, 15, 1624
    fixed_layer = centered_layer(R, (29,), (1,))
    group = subgroup(R, (29, 2, 7))
    period = stabilizer(R, group, fixed_layer)
    kernel = period
    stats = quotient_capacity(
        R, fixed_layer, period, kernel, (2, 7), (3, 1), R - 1
    )

    assert fixed_layer == period == {1, 14}
    assert stats["quotient_order"] == 4
    assert stats["box_sizes"] == (8, 4, 6, 3)
    assert stats["box_overflow"]
    assert stats["filtered"] == 10
    assert stats["theta_ordered_capped"] == 8
    assert stats["weighted_surplus"] == 2

    left, right = (1, 1), (0, 0)
    assert sign_box(left) == sign_box(right)
    quotient_left = coset(R, residual_value(R, (2, 7), left), period)
    quotient_right = coset(R, residual_value(R, (2, 7), right), period)
    assert quotient_left == quotient_right
    assert residual_value(R, (29, 2, 7), (-1, 1, 1)) == 1
    assert terminal_data((29, 2, 7), (1, 3, 1), (-1, 1, 1), K, R, p) == (
        784,
        3136,
        224,
    )


def verify_s3_sharp_boundary() -> None:
    s, R, q, budget = 3, 13, 3527, 5
    K = q**budget
    p = (4 * K - 1) // R
    group = subgroup(R, (q,))
    fixed_layer = {1}
    period = {1}
    kernel = subgroup(R, (q * q % R,))
    stats = quotient_capacity(
        R, fixed_layer, period, kernel, (q,), (budget,), R - 1
    )

    assert is_prime_64(q) and is_prime_64(p)
    assert K == 545792166732066407
    assert p == 167936051302174279 and p % 24 == 7
    assert 4 * K == p * R + 1
    assert len(group) == 2 * s and len(kernel) == s
    assert pow(q, s, R) == R - 1
    assert stats["box_sizes"] == (6, 5)
    assert stats["weight_spectrum"] == Counter({1: 3, 0: 3})
    assert stats["filtered"] == 2 * s
    assert stats["theta_ordered_capped"] == 2 * s
    assert stats["theta_actual"] == 2 * s
    assert stats["strong_threshold"] == 2 * s
    assert stats["weighted_surplus"] == 0
    assert not stats["direct_collisions"]

    exact = [
        exponent
        for exponent in range(-budget, budget + 1)
        if pow(q, exponent, R) == R - 1
    ]
    filtered = [
        exponent
        for exponent in range(-budget, budget + 1)
        if pow(q, exponent, R) * pow(R - 1, -1, R) % R in kernel
    ]
    bounded_kernel = [
        exponent
        for exponent in range(-budget, budget + 1)
        if pow(q, exponent, R) == 1
    ]
    assert exact == [-3, 3]
    assert filtered == [-5, -3, -1, 1, 3, 5]
    assert bounded_kernel == [0]

    buckets: dict[int, list[int]] = defaultdict(list)
    for exponent in filtered:
        buckets[0 if exponent >= 0 else 1].append(exponent)
    differences: list[int] = []
    for exponents in buckets.values():
        base = exponents[0]
        differences.extend(abs(exponent - base) for exponent in exponents[1:])
    assert differences == [2, 4, 2, 4]
    davenport_constant = s
    assert len(differences) >= davenport_constant
    zero_sums = [
        sum(differences[index] for index in indices)
        for size in range(1, davenport_constant + 1)
        for indices in combinations(range(len(differences)), size)
        if pow(q, sum(differences[index] for index in indices), R) in period
    ]
    assert min(zero_sums) == 2 * s > budget
    assert min(zero_sums) <= davenport_constant * budget


def verify() -> None:
    verify_zero_weight_collision()
    verify_p97_boundary()
    verify_p433_terminal()
    verify_s3_sharp_boundary()
    print("verified ordered-weight capacity and Davenport dilation boundary")
    print({
        "p2089": {"zero_weight_collision": True, "E": 1828, "n": 1828},
        "p97": {"C": 10, "theta_ordered": 14, "old_strong_threshold": 198},
        "p433": {"quotient_order": 4, "max_sign_box": 8, "E": 3136, "n": 224},
        "sharp_s3": {"C": 6, "strong_threshold": 6, "min_davenport_kernel": 6, "budget": 5},
    })


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
