#!/usr/bin/env python3
"""Verify affine phase lifts after stabilizer-owner projection."""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


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


def owner_capacity(
    labels: tuple[int, ...],
    owners: dict[int, int],
    *,
    modulus: int,
    stabilizer: frozenset[int],
    capacities: dict[frozenset[int], int],
    requests: int,
) -> dict[str, object]:
    if any(label not in owners for label in labels):
        return {
            "status": "PHASE_OWNER_MAP_UNCLOSED",
            "labels": labels,
        }
    slots = {
        stabilizer_coset(owners[label], modulus, stabilizer)
        for label in labels
    }
    capacity = sum(capacities.get(slot, 0) for slot in slots)
    debt = len(labels) - len(slots)
    if requests > capacity:
        return {
            "status": "PHASE_OWNER_PROJECTION_HALL_DEFICIT",
            "requests": requests,
            "capacity": capacity,
            "deficit": requests - capacity,
            "collision_debt": debt,
            "slots": len(slots),
        }
    return {
        "status": "PHASE_OWNER_CAPACITY_PASS",
        "requests": requests,
        "capacity": capacity,
        "collision_debt": debt,
        "slots": len(slots),
    }


def dispatch(
    data: PhaseInput,
    owners: dict[int, int],
    *,
    modulus: int,
    stabilizer: frozenset[int],
    capacities: dict[frozenset[int], int],
    requests: int,
) -> dict[str, object]:
    branch, labels = phase_lifts(data)
    if branch != "PHASE_LIFTED":
        return {"status": branch, "labels": labels}
    result = owner_capacity(
        labels,
        owners,
        modulus=modulus,
        stabilizer=stabilizer,
        capacities=capacities,
        requests=requests,
    )
    result["labels"] = labels
    return result


def verify() -> None:
    lifted = PhaseInput(5, 2, 3, 10, 0, 40, 13)
    branch, labels = phase_lifts(lifted)
    assert (branch, labels) == ("PHASE_LIFTED", (13,))

    obstructed = PhaseInput(5, 2, 3, 10, 0, 40, 14)
    assert phase_lifts(obstructed) == ("PHASE_GCD_OBSTRUCTED", ())

    empty = PhaseInput(7, 2, 4, 14, 0, 10, 18)
    assert phase_lifts(empty) == ("PHASE_INTERVAL_EMPTY", ())

    # Two phase labels collapse to one P-coset, so two requests exceed one physical slot.
    multi = PhaseInput(5, 2, 3, 10, 0, 100, 13)
    assert phase_lifts(multi) == ("PHASE_LIFTED", (13, 63))
    modulus = 12
    stabilizer = frozenset({0, 4, 8})
    shared_slot = stabilizer_coset(0, modulus, stabilizer)
    collision = dispatch(
        multi,
        {13: 0, 63: 4},
        modulus=modulus,
        stabilizer=stabilizer,
        capacities={shared_slot: 1},
        requests=2,
    )
    assert collision["status"] == "PHASE_OWNER_PROJECTION_HALL_DEFICIT"
    assert collision["capacity"] == 1
    assert collision["collision_debt"] == 1

    # Distinct P-cosets restore the two-slot capacity without changing the phase lift.
    distinct = dispatch(
        multi,
        {13: 0, 63: 1},
        modulus=modulus,
        stabilizer=stabilizer,
        capacities={
            stabilizer_coset(0, modulus, stabilizer): 1,
            stabilizer_coset(1, modulus, stabilizer): 1,
        },
        requests=2,
    )
    assert distinct["status"] == "PHASE_OWNER_CAPACITY_PASS"
    assert distinct["capacity"] == 2
    assert distinct["collision_debt"] == 0

    unclosed = dispatch(
        multi,
        {13: 0},
        modulus=modulus,
        stabilizer=stabilizer,
        capacities={shared_slot: 1},
        requests=1,
    )
    assert unclosed["status"] == "PHASE_OWNER_MAP_UNCLOSED"

    print("verified stabilizer-aware affine phase/owner capacity controls")
    print({
        "gcd_obstructed": phase_lifts(obstructed)[0],
        "interval_empty": phase_lifts(empty)[0],
        "collision": collision,
        "distinct": distinct,
        "unclosed": unclosed["status"],
    })


if __name__ == "__main__":
    verify()
