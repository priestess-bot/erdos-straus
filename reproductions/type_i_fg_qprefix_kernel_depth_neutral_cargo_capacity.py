#!/usr/bin/env python3
"""Focused verifier for labelled kernel depth and neutral cargo capacity."""

from __future__ import annotations

import argparse
from itertools import product


Record = tuple[int, ...]


def exponent_box(bounds: tuple[int, ...]) -> set[Record]:
    return set(product(*(range(bound + 1) for bound in bounds)))


def kernel_records(
    bounds: tuple[int, ...], weights: tuple[int, ...], modulus: int
) -> set[Record]:
    assert len(bounds) == len(weights)
    return {
        record
        for record in exponent_box(bounds)
        if sum(value * weight for value, weight in zip(record, weights)) % modulus
        == 0
    }


def prefix_box(depth: tuple[int, ...]) -> set[Record]:
    return exponent_box(depth)


def kernel_depth(kernel: set[Record]) -> tuple[int, ...]:
    assert kernel
    dimension = len(next(iter(kernel)))
    return tuple(max(record[index] for record in kernel) for index in range(dimension))


def maximal_records(records: set[Record]) -> set[Record]:
    return {
        record
        for record in records
        if not any(
            record != other
            and all(left <= right for left, right in zip(record, other))
            for other in records
        )
    }


def downclosure(records: set[Record]) -> set[Record]:
    return {
        child
        for record in records
        for child in product(*(range(value + 1) for value in record))
    }


def layer_ideal(record: Record) -> set[tuple[int, int]]:
    return {
        (index, layer)
        for index, exponent in enumerate(record)
        for layer in range(1, exponent + 1)
    }


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("zero has infinite valuation in this verifier")
    exponent = 0
    value = abs(value)
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def cyclic_log(value: int, generator: int, modulus: int, order: int) -> int:
    for exponent in range(order):
        if pow(generator, exponent, modulus) == value:
            return exponent
    raise AssertionError("value is outside the declared cyclic subgroup")


def verify_generic_depth_theorem() -> None:
    controls = [
        ((2, 2), (1, 1), 3),
        ((4, 2), (1, 0), 3),
        ((3, 2, 1), (1, 2, 0), 4),
    ]
    for bounds, weights, modulus in controls:
        kernel = kernel_records(bounds, weights, modulus)
        kappa = kernel_depth(kernel)

        for index, bound in enumerate(bounds):
            other_indices = [j for j in range(len(bounds)) if j != index]
            other_sums = {
                sum(record[j] * weights[j] for j in other_indices) % modulus
                for record in exponent_box(bounds)
            }
            projected = {record[index] for record in kernel}
            predicted = {
                value
                for value in range(bound + 1)
                if (-value * weights[index]) % modulus in other_sums
            }
            assert projected == predicted
            assert kappa[index] == max(predicted)

        for depth in exponent_box(bounds):
            covered = kernel <= prefix_box(depth)
            assert covered == all(
                value >= required for value, required in zip(depth, kappa)
            )

        required_layers = set().union(*(layer_ideal(record) for record in kernel))
        assert required_layers == layer_ideal(kappa)


def verify_product_synthesis_boundary() -> None:
    kernel = kernel_records((1, 1), (1, 1), 2)
    assert kernel == {(0, 0), (1, 1)}
    assert kernel_depth(kernel) == (1, 1)
    physical_records = {(0, 0), (1, 0), (0, 1)}
    present_layers = set().union(
        *(layer_ideal(record) for record in physical_records)
    )
    assert present_layers == layer_ideal((1, 1))
    assert (1, 1) not in physical_records


def verify_downset_boundary() -> None:
    kernel = kernel_records((2, 2), (1, 1), 3)
    assert kernel == {(0, 0), (1, 2), (2, 1)}
    maximal = maximal_records(kernel)
    kappa = kernel_depth(kernel)
    assert maximal == {(1, 2), (2, 1)}
    assert kappa == (2, 2)
    assert kappa not in kernel
    assert downclosure(maximal) == exponent_box(kappa) - {(2, 2)}

    larger_kernel = kernel_records((3, 3), (1, 1), 3)
    assert maximal_records(larger_kernel) == {(3, 3)}
    non_downset_source = {(0, 0), (3, 3)}
    assert maximal_records(larger_kernel) <= non_downset_source
    assert (1, 2) in larger_kernel - non_downset_source


def verify_collision_boundary() -> None:
    kernel = exponent_box((4, 1))

    def beta(record: Record) -> tuple[int, int]:
        return record[0] % 2, record[1]

    full_image = {beta(record) for record in kernel}
    prefix_records = kernel & prefix_box((4, 0))
    prefix_image = {beta(record) for record in prefix_records}
    rho = len(prefix_image)
    collision_loss = len(prefix_records) - rho
    uncovered = len(full_image) - rho

    assert len(prefix_records) == 5 > len(full_image) == 4
    assert prefix_image == {(0, 0), (1, 0)}
    assert (rho, collision_loss, uncovered) == (2, 3, 2)
    assert uncovered == len(full_image) - len(prefix_records) + collision_loss


def verify_p557_capacity_map() -> None:
    p = 557_281
    d_star = 182
    modulus = 4 * d_star
    numerator = p + 4 * d_star
    assert (modulus, numerator) == (728, 3**4 * 83**2)

    eta_three = pow(3 % 13, 4, 13)
    eta_83 = pow(83 % 13, 4, 13)
    assert eta_three == 3
    assert eta_83 == 1
    assert pow(eta_three, 3, 13) == 1
    assert all(pow(eta_three, exponent, 13) != 1 for exponent in (1, 2))

    bounds = (4, 2)
    weights = (
        cyclic_log(eta_three, eta_three, 13, 3),
        cyclic_log(eta_83, eta_three, 13, 3),
    )
    assert weights == (1, 0)
    kernel = kernel_records(bounds, weights, 3)
    expected_kernel = {
        (0, 0),
        (0, 1),
        (0, 2),
        (3, 0),
        (3, 1),
        (3, 2),
    }
    assert kernel == expected_kernel
    assert kernel_depth(kernel) == (3, 2)
    assert maximal_records(kernel) == {(3, 2)}
    assert downclosure(kernel) == prefix_box((3, 2))

    legacy_depth = (2, 0)
    kappa = kernel_depth(kernel)
    defect = tuple(
        max(0, required - current)
        for required, current in zip(kappa, legacy_depth)
    )
    assert defect == (1, 2)
    assert layer_ideal(kappa) - layer_ideal(legacy_depth) == {
        (0, 3),
        (1, 1),
        (1, 2),
    }

    def residue(record: Record) -> int:
        exponent_three, exponent_83 = record
        return (
            pow(3, exponent_three, modulus)
            * pow(83, exponent_83, modulus)
            % modulus
        )

    ambient = exponent_box(bounds)
    ambient_images = {residue(record) for record in ambient}
    assert len(ambient_images) == len(ambient) == 15

    completed_prefix = prefix_box(kappa)
    completed_images = {residue(record) for record in completed_prefix}
    assert completed_images == {
        1,
        3,
        9,
        19,
        27,
        57,
        83,
        121,
        249,
        283,
        337,
        363,
    }
    assert ambient_images - completed_images == {81, 171, 361}

    missing_map = {
        record: residue(record)
        for record in completed_prefix - prefix_box(legacy_depth)
    }
    assert missing_map == {
        (0, 1): 83,
        (0, 2): 337,
        (1, 1): 249,
        (1, 2): 283,
        (2, 1): 19,
        (2, 2): 121,
        (3, 0): 27,
        (3, 1): 57,
        (3, 2): 363,
    }
    assert 3**3 * 83**2 == 186_003 == numerator // 3

    x = d_star
    s_zero = 19_838
    j_base = 1
    valuation_profile = (
        valuation(p + 4 * s_zero, 3),
        valuation(x - s_zero, 3),
        valuation(p + 4 * x, 3),
    )
    assert valuation_profile == (3, 3, 4)
    assert min(valuation_profile) - j_base == 2

    print("PASS: FG_QPREFIX_KERNEL_DEPTH_NEUTRAL_CARGO_CAPACITY")
    print(f"kernel={sorted(kernel)}")
    print(f"kappa={kappa} legacy_depth={legacy_depth} legacy_defect={defect}")
    print(f"completed_prefix_images={sorted(completed_images)}")
    print(f"missing_records={sorted(missing_map.items())}")
    print("q3_fixed_lineage_depth_max=2 ambient_neutral_83_depth_requirement=2")


def verify() -> None:
    verify_generic_depth_theorem()
    verify_product_synthesis_boundary()
    verify_downset_boundary()
    verify_collision_boundary()
    verify_p557_capacity_map()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
