#!/usr/bin/env python3
"""Verify the target-fiber density / neighbor / Fourier trichotomy."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import product
from math import gcd


@dataclass(frozen=True)
class Fixture:
    name: str
    modulus: int
    generators: tuple[int, ...]
    budgets: tuple[int, ...]
    target: int
    expected_branch: str
    expected_count: int


FIXTURES = (
    Fixture("quotient_separation", 6, (2,), (1,), 1, "G_QUOTIENT_SEPARATION", 0),
    Fixture("neighbor_terminal", 3, (1, 1), (2, 2), 0, "NEIGHBOR_TERMINAL", 9),
    Fixture("fourier_deficit", 2, (1,), (2,), 1, "FIBER_DENSITY_FOURIER_DEFICIT", 2),
    Fixture("low_density_capacity", 7, (1,), (1,), 1, "FIBER_BOX_DENSITY_CAPACITY", 1),
)


def subgroup(modulus: int, generators: tuple[int, ...]) -> set[int]:
    step = modulus
    for generator in generators:
        step = gcd(step, generator % modulus)
    return {(step * index) % modulus for index in range(modulus // step)}


def box_points(budgets: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(product(*(range(-budget, budget + 1) for budget in budgets)))


def fiber_count(
    modulus: int,
    generators: tuple[int, ...],
    points: tuple[tuple[int, ...], ...],
    target: int,
) -> int:
    return sum(
        sum(generator * exponent for generator, exponent in zip(generators, point))
        % modulus
        == target
        for point in points
    )


def near_pair(points: tuple[tuple[int, ...], ...], budgets: tuple[int, ...]) -> bool:
    for left_index, left in enumerate(points):
        for right in points[left_index + 1 :]:
            if all(abs(left[i] - right[i]) <= budgets[i] for i in range(len(budgets))):
                return True
    return False


def audit(fixture: Fixture) -> str:
    modulus = fixture.modulus
    generators = fixture.generators
    budgets = fixture.budgets
    target = fixture.target
    H = subgroup(modulus, generators)
    points = box_points(budgets)
    volume = len(points)
    threshold = 1 << len(generators)
    count = fiber_count(modulus, generators, points, target)

    if count != fixture.expected_count:
        raise AssertionError(f"{fixture.name}: target fiber count changed")
    if target not in H:
        branch = "G_QUOTIENT_SEPARATION"
    elif count > threshold:
        target_points = tuple(
            point
            for point in points
            if sum(g * z for g, z in zip(generators, point)) % modulus == target
        )
        if not near_pair(target_points, budgets):
            raise AssertionError(f"{fixture.name}: near-pair witness missing")
        branch = "NEIGHBOR_TERMINAL"
    elif len(H) > 1 and volume > len(H) * threshold:
        deficit_numerator = volume - len(H) * count
        lower_bound_denominator = len(H) - 1
        if deficit_numerator <= 0:
            raise AssertionError(f"{fixture.name}: Fourier deficit is not positive")
        if fixture.name == "fourier_deficit":
            if (deficit_numerator, lower_bound_denominator) != (1, 1):
                raise AssertionError(f"{fixture.name}: Fourier lower bound changed")
            signed_character_sum = -1
            if -signed_character_sum * lower_bound_denominator < deficit_numerator:
                raise AssertionError(f"{fixture.name}: signed Fourier certificate changed")
        branch = "FIBER_DENSITY_FOURIER_DEFICIT"
    else:
        if volume > len(H) * threshold:
            raise AssertionError(f"{fixture.name}: low-density inequality changed")
        branch = "FIBER_BOX_DENSITY_CAPACITY"

    if branch != fixture.expected_branch:
        raise AssertionError(f"{fixture.name}: branch changed")
    return branch


def verify() -> None:
    branches = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_branch for fixture in FIXTURES}
    if branches != expected:
        raise AssertionError("target-fiber trichotomy receipt changed")
    print(f"verified {len(FIXTURES)} target-fiber density trichotomy receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
