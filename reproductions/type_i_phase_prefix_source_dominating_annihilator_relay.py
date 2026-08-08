#!/usr/bin/env python3
"""Verify phase-prefix source-dominating annihilator dispatch."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import product


Vector = tuple[int, ...]


@dataclass(frozen=True)
class Fixture:
    name: str
    source_columns: tuple[Vector, ...]
    slot_vectors: tuple[Vector, ...]
    demand_vectors: tuple[Vector, ...]
    target: Vector
    expected_branch: str


FIXTURES = (
    Fixture(
        "quotient_relay",
        ((1, 0),),
        ((1, 0),),
        ((1, 0), (0, 1)),
        (0, 1),
        "GLOBAL_PHASE_PREFIX_ANNIHILATOR_QUOTIENT_RELAY",
    ),
    Fixture(
        "subgroup_relay",
        ((1, 0, 0),),
        ((1, 0, 0),),
        ((1, 0, 0), (0, 0, 1)),
        (0, 1, 0),
        "GLOBAL_PHASE_PREFIX_ANNIHILATOR_SUBGROUP_RELAY",
    ),
    Fixture(
        "source_escape",
        ((1, 0), (0, 1)),
        ((1, 0),),
        ((1, 0), (0, 1)),
        (0, 1),
        "PHASE_PREFIX_SOURCE_COLUMN_ESCAPE",
    ),
    Fixture(
        "top_primary",
        (),
        (),
        ((1,),),
        (1,),
        "TOP_PRIMARY_ANNIHILATOR",
    ),
)


def dot(left: Vector, right: Vector) -> int:
    return sum(a * b for a, b in zip(left, right)) % 2


def span(vectors: tuple[Vector, ...], dimension: int) -> set[Vector]:
    result = {(0,) * dimension}
    for vector in vectors:
        result = result | {
            tuple((left[index] + vector[index]) % 2 for index in range(dimension))
            for left in tuple(result)
        }
    return result


def find_annihilator(
    slot_vectors: tuple[Vector, ...],
    demand_vectors: tuple[Vector, ...],
    dimension: int,
) -> Vector | None:
    for candidate in product((0, 1), repeat=dimension):
        if candidate == (0,) * dimension:
            continue
        if all(dot(candidate, vector) == 0 for vector in slot_vectors):
            if any(dot(candidate, vector) != 0 for vector in demand_vectors):
                return tuple(candidate)
    return None


def dispatch(fixture: Fixture) -> str:
    dimension = len(fixture.target)
    if len(fixture.slot_vectors) >= len(fixture.demand_vectors):
        raise AssertionError(f"{fixture.name}: capacity deficit missing")
    dominated = all(column in fixture.slot_vectors for column in fixture.source_columns)
    if not dominated:
        return "PHASE_PREFIX_SOURCE_COLUMN_ESCAPE"

    lam = find_annihilator(
        fixture.slot_vectors,
        fixture.demand_vectors,
        dimension,
    )
    if lam is None:
        raise AssertionError(f"{fixture.name}: annihilator missing")
    source_span = span(fixture.source_columns, dimension)
    if any(dot(lam, column) != 0 for column in fixture.source_columns):
        raise AssertionError(f"{fixture.name}: source column not annihilated")
    target_in_kernel = dot(lam, fixture.target) == 0
    target_in_source = fixture.target in source_span
    kernel_size = 2 ** (dimension - 1)
    if not target_in_kernel:
        branch = (
            "TOP_PRIMARY_ANNIHILATOR"
            if kernel_size == 1
            else "GLOBAL_PHASE_PREFIX_ANNIHILATOR_QUOTIENT_RELAY"
        )
    elif not target_in_source:
        branch = "GLOBAL_PHASE_PREFIX_ANNIHILATOR_SUBGROUP_RELAY"
    else:
        raise AssertionError(f"{fixture.name}: target is not a missing target")
    return branch


def verify() -> None:
    for fixture in FIXTURES:
        branch = dispatch(fixture)
        if branch != fixture.expected_branch:
            raise AssertionError(f"{fixture.name}: branch changed")
    print(f"verified {len(FIXTURES)} phase-prefix annihilator controls")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
