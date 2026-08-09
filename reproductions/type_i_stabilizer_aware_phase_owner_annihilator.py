#!/usr/bin/env python3
"""Verify the phase-owner capacity to annihilator dispatch."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import product
from math import gcd


Vector = tuple[int, ...]


@dataclass(frozen=True)
class PhaseInput:
    q: int
    exponent: int
    offset: int
    step: int
    lower: int
    upper: int
    phase: int


def ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def phase_lifts(data: PhaseInput) -> tuple[str, tuple[int, ...]]:
    modulus = data.q ** data.exponent
    delta = (data.phase - data.offset) % modulus
    divisor = gcd(data.step, modulus)
    if delta % divisor:
        return "PHASE_GCD_OBSTRUCTED", ()

    reduced_step = data.step // divisor
    reduced_modulus = modulus // divisor
    residue = 0 if reduced_modulus == 1 else (
        (delta // divisor) * pow(reduced_step, -1, reduced_modulus)
    ) % reduced_modulus
    minimum = ceil_div(data.lower - data.offset, data.step)
    maximum = (data.upper - data.offset) // data.step
    k_min = ceil_div(minimum - residue, reduced_modulus)
    k_max = (maximum - residue) // reduced_modulus
    if k_min > k_max:
        return "PHASE_INTERVAL_EMPTY", ()
    return "PHASE_LIFTED", tuple(
        data.offset + data.step * (residue + reduced_modulus * k)
        for k in range(k_min, k_max + 1)
    )


def stabilizer_coset(owner: int, modulus: int, stabilizer: frozenset[int]) -> frozenset[int]:
    return frozenset((owner + shift) % modulus for shift in stabilizer)


def add(left: Vector, right: Vector, field: int) -> Vector:
    return tuple((a + b) % field for a, b in zip(left, right))


def scale(value: int, vector: Vector, field: int) -> Vector:
    return tuple((value * coordinate) % field for coordinate in vector)


def span(vectors: tuple[Vector, ...], field: int, dimension: int) -> set[Vector]:
    result = {(0,) * dimension}
    for vector in vectors:
        result = {
            add(base, scale(coefficient, vector, field), field)
            for base in result
            for coefficient in range(field)
        }
    return result


def dot(left: Vector, right: Vector, field: int) -> int:
    return sum(a * b for a, b in zip(left, right)) % field


def separating_functional(
    source_space: set[Vector],
    demand_space: set[Vector],
    field: int,
    dimension: int,
) -> Vector | None:
    """Find lambda with lambda(source_space)=0 and lambda(demand_space) nonzero."""
    for coefficients in product(range(field), repeat=dimension):
        if not any(coefficients):
            continue
        if all(dot(coefficients, vector, field) == 0 for vector in source_space):
            if any(dot(coefficients, vector, field) != 0 for vector in demand_space):
                return coefficients
    return None


def span_rank(space: set[Vector], field: int) -> int:
    size = len(space)
    rank = 0
    cardinality = 1
    while cardinality < size:
        cardinality *= field
        rank += 1
    assert cardinality == size
    return rank


def owner_slots(
    labels: tuple[int, ...],
    owners: dict[int, int],
    *,
    modulus: int,
    stabilizer: frozenset[int],
) -> tuple[str, set[frozenset[int]]]:
    missing = tuple(label for label in labels if label not in owners)
    if missing:
        return "PHASE_OWNER_SOURCE_UNCLOSED", set()
    return "PHASE_OWNER_CLOSED", {
        stabilizer_coset(owners[label], modulus, stabilizer) for label in labels
    }


def dispatch(
    data: PhaseInput,
    owners: dict[int, int],
    *,
    modulus: int,
    stabilizer: frozenset[int],
    capacities: dict[frozenset[int], int],
    demands: tuple[Vector, ...],
    source_columns: dict[frozenset[int], Vector],
    source_generators: tuple[Vector, ...],
    source_set: tuple[Vector, ...],
    target: Vector,
    field: int,
    dimension: int,
) -> dict[str, object]:
    phase_status, labels = phase_lifts(data)
    if phase_status != "PHASE_LIFTED":
        return {"status": phase_status, "labels": labels}

    owner_status, slots = owner_slots(
        labels, owners, modulus=modulus, stabilizer=stabilizer
    )
    if owner_status != "PHASE_OWNER_CLOSED":
        return {"status": owner_status, "labels": labels}
    if any(slot not in source_columns for slot in slots):
        return {
            "status": "PHASE_OWNER_SOURCE_UNCLOSED",
            "labels": labels,
            "slots": len(slots),
        }

    capacity = sum(capacities.get(slot, 0) for slot in slots)
    demand_space = span(demands, field, dimension)
    source_space = span(tuple(source_columns[slot] for slot in slots), field, dimension)
    deficit = len(demands) - capacity
    result: dict[str, object] = {
        "labels": labels,
        "slots": len(slots),
        "capacity": capacity,
        "requests": len(demands),
        "deficit": max(0, deficit),
        "demand_rank": span_rank(demand_space, field),
        "source_rank": span_rank(source_space, field),
    }

    separating = separating_functional(
        source_space, demand_space, field, dimension
    )
    if deficit <= 0:
        if separating is None:
            result["status"] = "PHASE_OWNER_RANK_PASS"
        else:
            result["status"] = "PHASE_OWNER_RANK_GAP"
            result["lambda"] = separating
        return result

    result["status"] = "PHASE_OWNER_PROJECTION_HALL_DEFICIT"
    if separating is None:
        result["status"] = "PHASE_OWNER_COLLISION_ONLY"
        return result

    result["lambda"] = separating
    if not all(vector in source_space for vector in source_generators):
        result["status"] = "PHASE_OWNER_SOURCE_COLUMN_ESCAPE"
        return result

    target_value = dot(separating, target, field)
    kernel_size = field ** (dimension - 1)
    result["target_lambda"] = target_value
    result["kernel_size"] = kernel_size
    if target_value:
        result["status"] = (
            "PHASE_OWNER_TOP_PRIMARY_TERMINAL"
            if kernel_size == 1
            else "PHASE_OWNER_QUOTIENT_RELAY"
        )
    elif target not in source_set:
        result["status"] = "PHASE_OWNER_SUBGROUP_RELAY"
    else:
        result["status"] = "PHASE_OWNER_RELATION_ONLY"
    return result


def verify() -> None:
    lifted = PhaseInput(5, 2, 3, 10, 0, 40, 13)
    assert phase_lifts(lifted) == ("PHASE_LIFTED", (13,))
    assert phase_lifts(PhaseInput(5, 2, 3, 10, 0, 40, 14))[0] == "PHASE_GCD_OBSTRUCTED"
    assert phase_lifts(PhaseInput(7, 2, 4, 14, 0, 10, 18))[0] == "PHASE_INTERVAL_EMPTY"

    multi = PhaseInput(5, 2, 3, 10, 0, 100, 13)
    modulus = 12
    stabilizer = frozenset({0, 4, 8})
    shared_slot = stabilizer_coset(0, modulus, stabilizer)
    distinct_slot = stabilizer_coset(1, modulus, stabilizer)

    common = {
        "modulus": modulus,
        "stabilizer": stabilizer,
        "demands": ((1, 0), (0, 1)),
        "source_columns": {shared_slot: (1, 0)},
        "source_generators": ((1, 0),),
        "source_set": ((0, 0), (1, 0)),
        "target": (0, 1),
        "field": 3,
        "dimension": 2,
    }
    quotient = dispatch(
        multi,
        {13: 0, 63: 4},
        capacities={shared_slot: 1},
        **common,
    )
    assert quotient["status"] == "PHASE_OWNER_QUOTIENT_RELAY"
    assert quotient["lambda"] == (0, 1)
    assert quotient["target_lambda"] == 1

    subgroup = dispatch(
        multi,
        {13: 0, 63: 4},
        capacities={shared_slot: 1},
        **{**common, "target": (2, 0)},
    )
    assert subgroup["status"] == "PHASE_OWNER_SUBGROUP_RELAY"

    collision = dispatch(
        multi,
        {13: 0, 63: 4},
        capacities={shared_slot: 1},
        **{
            **common,
            "demands": ((1, 0), (2, 0)),
        },
    )
    assert collision["status"] == "PHASE_OWNER_COLLISION_ONLY"

    escape = dispatch(
        multi,
        {13: 0, 63: 4},
        capacities={shared_slot: 1},
        **{
            **common,
            "source_generators": ((1, 0), (0, 1)),
        },
    )
    assert escape["status"] == "PHASE_OWNER_SOURCE_COLUMN_ESCAPE"

    distinct = dispatch(
        multi,
        {13: 0, 63: 1},
        capacities={shared_slot: 1, distinct_slot: 1},
        **{
            **common,
            "source_columns": {shared_slot: (1, 0), distinct_slot: (0, 1)},
            "source_generators": ((1, 0), (0, 1)),
        },
    )
    assert distinct["status"] == "PHASE_OWNER_RANK_PASS"

    unclosed = dispatch(
        multi,
        {13: 0},
        capacities={shared_slot: 1},
        **common,
    )
    assert unclosed["status"] == "PHASE_OWNER_SOURCE_UNCLOSED"

    top = dispatch(
        PhaseInput(5, 2, 3, 10, 0, 40, 13),
        {13: 0},
        capacities={frozenset({0}): 0},
        modulus=1,
        stabilizer=frozenset({0}),
        demands=((1,),),
        source_columns={frozenset({0}): (0,)},
        source_generators=((0,),),
        source_set=((0,),),
        target=(1,),
        field=3,
        dimension=1,
    )
    assert top["status"] == "PHASE_OWNER_TOP_PRIMARY_TERMINAL"

    print("verified phase-owner annihilator/collision dispatch controls")
    print({
        "quotient": quotient,
        "subgroup": subgroup,
        "collision": collision,
        "escape": escape,
        "rank_pass": distinct,
        "unclosed": unclosed["status"],
        "top": top,
    })


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true", help="run finite-field controls")
    parser.parse_args()
    verify()


if __name__ == "__main__":
    main()
