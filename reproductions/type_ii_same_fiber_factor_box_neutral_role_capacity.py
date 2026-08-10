#!/usr/bin/env python3
"""Focused verifier for the same-fiber factor-box/neutral-role theorem."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
from math import gcd, prod


Record = tuple[int, ...]


def divisors_from_box(prime_powers: tuple[tuple[int, int], ...]) -> dict[Record, int]:
    bounds = [range(exponent + 1) for _, exponent in prime_powers]
    return {
        record: product_value
        for record in product(*bounds)
        for product_value in [
            prod(
                prime**power
                for (prime, _), power in zip(prime_powers, record)
            )
        ]
    }


def euler_phi(value: int) -> int:
    result = value
    prime = 2
    remainder = value
    while prime * prime <= remainder:
        if remainder % prime == 0:
            result -= result // prime
            while remainder % prime == 0:
                remainder //= prime
        prime += 1
    if remainder > 1:
        result -= result // remainder
    return result


def multiplicative_order(value: int, modulus: int) -> int:
    assert gcd(value, modulus) == 1
    current = 1
    for order in range(1, euler_phi(modulus) + 1):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("multiplicative order not found")


def chi_minus_eight(value: int) -> int:
    residue = value % 8
    assert residue in {1, 3, 5, 7}
    return 1 if residue in {1, 3} else -1


def downclosed(records: set[Record]) -> bool:
    return all(
        child in records
        for record in records
        for child in product(*(range(exponent + 1) for exponent in record))
    )


def verify_p557_factor_box() -> None:
    p = 557_281
    d_star = 182
    a_parameter = 1
    modulus = 4 * d_star
    numerator = p + 4 * a_parameter * d_star
    prime_powers = ((3, 4), (83, 2))

    assert (modulus, numerator) == (728, 558_009)
    assert numerator == 3**4 * 83**2
    assert gcd(numerator, modulus) == 1

    factor_box = divisors_from_box(prime_powers)
    divisors = set(factor_box.values())
    assert len(factor_box) == len(divisors) == 15
    assert all(numerator % divisor == 0 for divisor in divisors)

    residues = {record: divisor % modulus for record, divisor in factor_box.items()}
    assert len(set(residues.values())) == 15
    assert set(residues.values()) == {
        1,
        3,
        9,
        19,
        27,
        57,
        81,
        83,
        121,
        171,
        249,
        283,
        337,
        361,
        363,
    }
    assert modulus - 1 not in set(residues.values())

    b_three = {3**exponent for exponent in range(5)}
    b_83 = {83**exponent for exponent in range(3)}
    assert {left * right for left in b_three for right in b_83} == divisors
    assert max(exponent for exponent in range(8) if numerator % 3**exponent == 0) == 4
    assert max(exponent for exponent in range(6) if numerator % 83**exponent == 0) == 2

    def eta(value: int) -> int:
        return pow(value % 13, 4, 13)

    assert eta(3) == 3
    assert eta(83) == 1
    assert multiplicative_order(eta(3), 13) == 3
    assert multiplicative_order(eta(83), 13) == 1

    active_counts = Counter(eta(3**exponent) for exponent in range(5))
    full_counts = Counter(eta(divisor) for divisor in divisors)
    assert active_counts == Counter({1: 2, 3: 2, 9: 1})
    assert full_counts == Counter({1: 6, 3: 6, 9: 3})
    assert full_counts == Counter(
        {image: 3 * count for image, count in active_counts.items()}
    )
    assert min(4, multiplicative_order(eta(3), 13) - 1) == 2
    assert min(2, multiplicative_order(eta(83), 13) - 1) == 0

    kernel_records = {
        record for record, divisor in factor_box.items() if eta(divisor) == 1
    }
    assert kernel_records == {
        (0, 0),
        (0, 1),
        (0, 2),
        (3, 0),
        (3, 1),
        (3, 2),
    }

    assert all(chi_minus_eight(divisor) == 1 for divisor in divisors)
    assert chi_minus_eight(modulus - 1) == -1
    assert sum(chi_minus_eight(divisor) for divisor in divisors) == 15

    units = {value for value in range(1, modulus) if gcd(value, modulus) == 1}
    assert len(units) == euler_phi(modulus) == 288
    assert gcd(83, len(units)) == 1
    assert {pow(value, 83, modulus) for value in units} == units
    assert multiplicative_order(83, modulus) == 4


def verify_source_closure_independence() -> None:
    typed_prefix = {(exponent, 0) for exponent in range(3)}
    top_record = (3, 2)
    closed_model = set(typed_prefix)
    nonclosed_model = typed_prefix | {top_record}

    assert downclosed(closed_model)
    assert not downclosed(nonclosed_model)
    assert (3, 1) not in nonclosed_model
    assert all(left <= right for left, right in zip((3, 1), top_record))

    owner_map_one = {record: f"owner-{record}" for record in closed_model}
    owner_map_two = dict(owner_map_one)
    owner_map_two[(2, 0)] = owner_map_two[(1, 0)]
    assert set(owner_map_one) == set(owner_map_two) == closed_model
    assert owner_map_one != owner_map_two
    assert len(set(owner_map_one.values())) == 3
    assert len(set(owner_map_two.values())) == 2
    assert len(set(owner_map_one.values())) == len(owner_map_one)
    assert len(set(owner_map_two.values())) < len(owner_map_two)


def verify() -> None:
    verify_p557_factor_box()
    verify_source_closure_independence()
    print("PASS: TYPE_II_SAME_FIBER_FACTOR_BOX_NEUTRAL_ROLE_CAPACITY")
    print("p557_arithmetic_depth=(4,2) eta_capacity=(2,0)")
    print("p557_eta_neutral_multiplier_83=3 c83_role_rank=0")
    print("p557_same_fiber_type_ii_target_miss=True")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
