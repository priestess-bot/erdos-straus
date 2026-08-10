#!/usr/bin/env python3
"""Focused checks for primary-filter active-source saturation and zero capacity."""

from __future__ import annotations

import argparse
from itertools import product

Vector = tuple[int, ...]


def box_points(budgets: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(product(*(range(-budget, budget + 1) for budget in budgets)))


def cyclic_image(
    generators: tuple[int, ...], point: tuple[int, ...], modulus: int
) -> int:
    return sum(
        generator * exponent for generator, exponent in zip(generators, point)
    ) % modulus


def cyclic_subgroup(generators: tuple[int, ...], modulus: int) -> frozenset[int]:
    seen = {0}
    frontier = [0]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = (current + generator) % modulus
            if candidate not in seen:
                seen.add(candidate)
                frontier.append(candidate)
    return frozenset(seen)


def multiplicative_order(base: int, modulus: int) -> int:
    value = 1
    for order in range(1, modulus + 1):
        value = value * base % modulus
        if value == 1:
            return order
    raise AssertionError("base must be a unit modulo modulus")


def image_difference_subgroup(
    generators: tuple[int, ...], budgets: tuple[int, ...], modulus: int
) -> frozenset[int]:
    support = {
        cyclic_image(generators, point, modulus) for point in box_points(budgets)
    }
    differences = tuple(
        (left - right) % modulus for left in support for right in support
    )
    return cyclic_subgroup(differences, modulus)


def verify_active_difference_identity() -> dict[str, int]:
    fixtures = (
        ((2, 1), (4, 0), 4),
        ((15, 1), (1, 1), 18),
        ((1, 0, 1), (1, 0, 2), 6),
    )
    for generators, budgets, modulus in fixtures:
        active = tuple(
            generator
            for generator, budget in zip(generators, budgets)
            if budget > 0
        )
        assert image_difference_subgroup(generators, budgets, modulus) == (
            cyclic_subgroup(active, modulus)
        )

        points = box_points(budgets)
        for index, budget in enumerate(budgets):
            if budget == 0:
                assert all(point[index] == 0 for point in points)
            else:
                unit = tuple(
                    int(coordinate == index) for coordinate in range(len(budgets))
                )
                assert unit in points

    return {"focused_active_difference_controls": len(fixtures)}


def parity_fourier_receipt(
    generators: tuple[int, ...],
    budgets: tuple[int, ...],
    modulus: int,
    target: int,
) -> dict[str, int]:
    points = box_points(budgets)
    images = tuple(cyclic_image(generators, point, modulus) for point in points)
    exact_count = sum(value == target for value in images)
    target_parity = target % 2
    coset_count = sum(value % 2 == target_parity for value in images)
    box_sum = sum(1 if value % 2 == 0 else -1 for value in images)
    target_phase = 1 if target_parity == 0 else -1
    deficit_score = -target_phase * box_sum
    return {
        "volume": len(points),
        "threshold": 1 << len(budgets),
        "exact_count": exact_count,
        "coset_count": coset_count,
        "box_sum": box_sum,
        "deficit_score": deficit_score,
    }


def verify_frozen_quotient() -> dict[str, int]:
    generators = (2, 1)
    budgets = (4, 0)
    modulus = 4
    target = 1
    difference_group = image_difference_subgroup(generators, budgets, modulus)
    active_group = cyclic_subgroup((2,), modulus)
    assert difference_group == active_group == frozenset({0, 2})
    assert target not in difference_group
    assert all(value % 2 == 0 for value in difference_group)

    receipt = parity_fourier_receipt(generators, budgets, modulus, target)
    assert receipt == {
        "volume": 9,
        "threshold": 4,
        "exact_count": 0,
        "coset_count": 0,
        "box_sum": 9,
        "deficit_score": 9,
    }
    assert receipt["volume"] > 2 * receipt["threshold"]
    return {"difference_group_order": len(difference_group), **receipt}


def verify_ambient_extension_obstruction() -> dict[str, int]:
    # H=C4, D=<2>, ell(2)=1. Every H->F2 homomorphism kills 2.
    ambient = range(4)
    local_labels = {0: 0, 2: 1}
    q_h = {(2 * value) % 4 for value in ambient}
    intersection = set(local_labels) & q_h
    assert intersection == {0, 2}
    assert any(local_labels[value] for value in intersection)

    extensions = []
    for coefficient in range(2):
        labels = {value: coefficient * (value % 2) % 2 for value in ambient}
        if all(labels[value] == label for value, label in local_labels.items()):
            extensions.append(labels)
    assert not extensions
    return {
        "source_order": len(local_labels),
        "intersection_order": len(intersection),
        "ambient_extensions": len(extensions),
    }


def rank_mod(vectors: tuple[Vector, ...], prime: int) -> int:
    if not vectors:
        return 0
    matrix = [[entry % prime for entry in vector] for vector in vectors]
    row = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (index for index in range(row, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        inverse = pow(matrix[row][column], -1, prime)
        matrix[row] = [(entry * inverse) % prime for entry in matrix[row]]
        for index in range(len(matrix)):
            if index == row or matrix[index][column] == 0:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                (left - factor * right) % prime
                for left, right in zip(matrix[index], matrix[row])
            ]
        row += 1
        if row == len(matrix):
            break
    return row


def evaluation_columns(
    sources: tuple[Vector, ...], roles: tuple[Vector, ...], prime: int
) -> tuple[Vector, ...]:
    return tuple(
        tuple(
            sum(left * right for left, right in zip(role, source)) % prime
            for role in roles
        )
        for source in sources
    )


def verify_multirole_source_domination() -> dict[str, int]:
    sources = ((1, 0), (0, 1), (1, 1))
    roles = ((1, 0), (0, 1))
    columns = evaluation_columns(sources, roles, 2)
    assert columns == ((1, 0), (0, 1), (1, 1))
    source_rank = rank_mod(columns, 2)
    assert source_rank == len(roles) == 2
    role_capacity = len(roles) - source_rank
    assert role_capacity == 0
    return {
        "role_dimension": len(roles),
        "source_column_rank": source_rank,
        "role_capacity": role_capacity,
    }


def verify_p73_sharp_deficit_saturation() -> dict[str, int]:
    # U(27)=<2> has order 18; 17=2^15, 29=2, and -1=2^9.
    prime = 73
    chart_modulus = 27
    chart_k = (prime * chart_modulus + 1) // 4
    assert prime * chart_modulus + 1 == 4 * chart_k
    assert chart_k == 493 == 17 * 29
    assert multiplicative_order(2, chart_modulus) == 18
    assert pow(2, 15, chart_modulus) == 17
    assert pow(2, 1, chart_modulus) == 29 % chart_modulus
    assert pow(2, 9, chart_modulus) == -1 % chart_modulus

    generators = (15, 1)
    budgets = (1, 1)
    modulus = 18
    target = 9
    difference_group = image_difference_subgroup(generators, budgets, modulus)
    assert difference_group == frozenset(range(modulus))

    receipt = parity_fourier_receipt(generators, budgets, modulus, target)
    assert receipt == {
        "volume": 9,
        "threshold": 4,
        "exact_count": 0,
        "coset_count": 4,
        "box_sum": 1,
        "deficit_score": 1,
    }
    assert receipt["volume"] > 2 * receipt["threshold"]
    assert receipt["deficit_score"] == (
        receipt["volume"] - 2 * receipt["coset_count"]
    )

    source_columns = tuple((generator % 2,) for generator in generators)
    source_rank = rank_mod(source_columns, 2)
    assert source_columns == ((1,), (1,))
    assert source_rank == 1
    quotient_dimension = 1
    role_capacity = quotient_dimension - source_rank
    assert role_capacity == 0
    return {
        "difference_group_order": len(difference_group),
        "source_column_rank": source_rank,
        "role_capacity": role_capacity,
        **receipt,
    }


def verify() -> None:
    print("verified: active difference identity", verify_active_difference_identity())
    print("verified: frozen quotient separation", verify_frozen_quotient())
    print(
        "verified: ambient extension obstruction",
        verify_ambient_extension_obstruction(),
    )
    print("verified: multirole source domination", verify_multirole_source_domination())
    print(
        "verified: p=73 sharp deficit saturation",
        verify_p73_sharp_deficit_saturation(),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
