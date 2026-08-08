#!/usr/bin/env python3
"""Verify the q-primary filtered target-fiber density relay."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Fixture:
    name: str
    modulus: int
    generators: tuple[int, ...]
    budgets: tuple[int, ...]
    target: int
    quotient_order: int
    expected_branch: str
    expected_exact_count: int
    expected_coset_count: int


FIXTURES = (
    Fixture(
        "q_primary_deficit",
        6,
        (1,),
        (2,),
        1,
        2,
        "Q_PRIMARY_FILTERED_FOURIER_DEFICIT",
        1,
        2,
    ),
    Fixture(
        "quotient_saturation",
        6,
        (1,),
        (3,),
        1,
        2,
        "PRIMARY_QUOTIENT_BOX_SATURATED",
        1,
        4,
    ),
    Fixture(
        "q_primary_capacity",
        6,
        (1,),
        (1,),
        1,
        2,
        "Q_PRIMARY_FILTERED_BOX_CAPACITY",
        1,
        2,
    ),
    Fixture(
        "exact_neighbor_priority",
        3,
        (1, 1),
        (2, 2),
        0,
        3,
        "NEIGHBOR_TERMINAL",
        9,
        9,
    ),
)


def box_points(budgets: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(product(*(range(-budget, budget + 1) for budget in budgets)))


def image_value(
    generators: tuple[int, ...],
    point: tuple[int, ...],
    modulus: int,
) -> int:
    return sum(generator * exponent for generator, exponent in zip(generators, point)) % modulus


def counts(fixture: Fixture) -> tuple[int, int, int]:
    points = box_points(fixture.budgets)
    exact = sum(
        image_value(fixture.generators, point, fixture.modulus) == fixture.target
        for point in points
    )
    coset = sum(
        image_value(fixture.generators, point, fixture.quotient_order)
        == fixture.target % fixture.quotient_order
        for point in points
    )
    return len(points), exact, coset


def parity_signed_target_sum(fixture: Fixture) -> int:
    points = box_points(fixture.budgets)
    box_sum = sum(
        1
        if image_value(fixture.generators, point, 2) == 0
        else -1
        for point in points
    )
    target_phase = 1 if fixture.target % 2 == 0 else -1
    return target_phase * box_sum


def near_pair(
    points: tuple[tuple[int, ...], ...],
    budgets: tuple[int, ...],
) -> bool:
    for left_index, left in enumerate(points):
        for right in points[left_index + 1 :]:
            if all(
                abs(left[index] - right[index]) <= budgets[index]
                for index in range(len(budgets))
            ):
                return True
    return False


def audit(fixture: Fixture) -> str:
    volume, exact, coset = counts(fixture)
    expected_counts = (fixture.expected_exact_count, fixture.expected_coset_count)
    if (exact, coset) != expected_counts:
        raise AssertionError(f"{fixture.name}: target or coset count changed")

    threshold = 1 << len(fixture.generators)
    if exact > threshold:
        target_points = tuple(
            point
            for point in box_points(fixture.budgets)
            if image_value(fixture.generators, point, fixture.modulus)
            == fixture.target
        )
        if not near_pair(target_points, fixture.budgets):
            raise AssertionError(f"{fixture.name}: near-pair witness missing")
        branch = "NEIGHBOR_TERMINAL"
    elif coset > threshold:
        branch = "PRIMARY_QUOTIENT_BOX_SATURATED"
    elif volume > fixture.quotient_order * threshold:
        deficit = volume - fixture.quotient_order * coset
        if deficit <= 0:
            raise AssertionError(f"{fixture.name}: filtered Fourier deficit is not positive")
        if fixture.name == "q_primary_deficit":
            if deficit != 1:
                raise AssertionError(f"{fixture.name}: Fourier lower bound changed")
            signed_character_sum = parity_signed_target_sum(fixture)
            if signed_character_sum != -deficit:
                raise AssertionError(f"{fixture.name}: signed Fourier sum changed")
            if -signed_character_sum < deficit:
                raise AssertionError(f"{fixture.name}: signed Fourier certificate changed")
        branch = "Q_PRIMARY_FILTERED_FOURIER_DEFICIT"
    else:
        if volume > fixture.quotient_order * threshold:
            raise AssertionError(f"{fixture.name}: filtered capacity inequality changed")
        branch = "Q_PRIMARY_FILTERED_BOX_CAPACITY"

    if branch != fixture.expected_branch:
        raise AssertionError(f"{fixture.name}: branch changed")
    return branch


def verify() -> None:
    branches = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_branch for fixture in FIXTURES}
    if branches != expected:
        raise AssertionError("q-primary filtered relay receipt changed")
    print(f"verified {len(FIXTURES)} q-primary filtered relay receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
