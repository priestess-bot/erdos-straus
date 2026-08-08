#!/usr/bin/env python3
"""Verify support-annihilator versus source-q-demand dispatch."""

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
    expected_branch: str
    expected_score: int


FIXTURES = (
    Fixture(
        "support_annihilator",
        4,
        (2, 1),
        (4, 0),
        1,
        "SUPPORT_ANNIHILATOR_SEPARATION",
        -9,
    ),
    Fixture(
        "source_difference_q_demand",
        6,
        (1,),
        (2,),
        1,
        "SOURCE_DIFFERENCE_Q_DEMAND",
        -1,
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
        image_value(fixture.generators, point, 2) == fixture.target % 2
        for point in points
    )
    return len(points), exact, coset


def signed_parity_score(fixture: Fixture) -> int:
    points = box_points(fixture.budgets)
    box_sum = sum(
        1 if image_value(fixture.generators, point, 2) == 0 else -1
        for point in points
    )
    target_phase = 1 if fixture.target % 2 == 0 else -1
    return target_phase * box_sum


def audit(fixture: Fixture) -> str:
    volume, exact, coset = counts(fixture)
    threshold = 1 << len(fixture.generators)
    m = 2
    if exact > threshold or coset > threshold or volume <= m * threshold:
        raise AssertionError(f"{fixture.name}: not a filtered Fourier deficit control")

    deficit = volume - m * coset
    score = signed_parity_score(fixture)
    if score != fixture.expected_score or score > -deficit:
        raise AssertionError(f"{fixture.name}: Fourier score changed")

    support_parities = {
        image_value(fixture.generators, point, 2)
        for point in box_points(fixture.budgets)
    }
    if len(support_parities) == 1:
        branch = "SUPPORT_ANNIHILATOR_SEPARATION"
        if score >= 0:
            raise AssertionError(f"{fixture.name}: support separation score is not negative")
    else:
        branch = "SOURCE_DIFFERENCE_Q_DEMAND"
        if support_parities != {0, 1}:
            raise AssertionError(f"{fixture.name}: q=2 source difference changed")

    if branch != fixture.expected_branch:
        raise AssertionError(f"{fixture.name}: dispatch changed")
    return branch


def verify() -> None:
    branches = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_branch for fixture in FIXTURES}
    if branches != expected:
        raise AssertionError("support/source dichotomy receipt changed")
    print(f"verified {len(FIXTURES)} support/source dichotomy receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
