#!/usr/bin/env python3
"""Verify the top odd-primary kernel pair/overflow capacity dichotomy."""

from __future__ import annotations

import argparse
from itertools import combinations, product
from typing import Mapping, Sequence

Element = tuple[int, ...]
Exponent = tuple[int, ...]


def group_elements(moduli: Sequence[int]) -> tuple[Element, ...]:
    return tuple(product(*(range(modulus) for modulus in moduli)))


def add(left: Element, right: Element, moduli: Sequence[int]) -> Element:
    return tuple((a + b) % modulus for a, b, modulus in zip(left, right, moduli))


def scale(value: Element, multiplier: int, moduli: Sequence[int]) -> Element:
    return tuple((multiplier * coordinate) % modulus for coordinate, modulus in zip(value, moduli))


def negate_exponent(value: Exponent) -> Exponent:
    return tuple(-coordinate for coordinate in value)


def image(exponent: Exponent, generators: Sequence[Element], moduli: Sequence[int]) -> Element:
    result = tuple(0 for _ in moduli)
    for coefficient, generator in zip(exponent, generators):
        result = add(result, scale(generator, coefficient, moduli), moduli)
    return result


def box(bounds: Sequence[int]) -> tuple[Exponent, ...]:
    return tuple(product(*(range(-bound, bound + 1) for bound in bounds)))


def order(value: Element, moduli: Sequence[int]) -> int:
    identity = tuple(0 for _ in moduli)
    current = identity
    for exponent in range(1, 1 + max(moduli) * 12):
        current = add(current, value, moduli)
        if current == identity:
            return exponent
    raise AssertionError("element order exceeds control bound")


def top_kernel_pair_profile(
    *,
    moduli: Sequence[int],
    generators: Sequence[Element],
    bounds: Sequence[int],
    target: Element,
    kernel_generator: Element,
) -> dict[str, object]:
    moduli = tuple(moduli)
    bounds = tuple(bounds)
    if len(generators) != len(bounds) or len(target) != len(moduli):
        raise AssertionError("dimension mismatch")
    if order(kernel_generator, moduli) != 3:
        raise AssertionError("the focused top kernel must have odd prime order 3")
    if order(target, moduli) != 2:
        raise AssertionError("the target must be an involution")

    universe = set(group_elements(moduli))
    kernel = {scale(kernel_generator, coefficient, moduli) for coefficient in range(3)}
    target_coset = {add(target, element, moduli) for element in kernel}
    points = box(bounds)
    source_set = {image(exponent, generators, moduli) for exponent in points}
    if target in source_set:
        raise AssertionError("control must miss the exact target")
    if not source_set & target_coset:
        raise AssertionError("the lower quotient must hit the target coset")
    if add(target, kernel_generator, moduli) not in universe:
        raise AssertionError("invalid target coset")

    fiber = tuple(
        exponent for exponent in points if image(exponent, generators, moduli) in target_coset
    )
    if not fiber:
        raise AssertionError("target coset fiber is empty")
    if any(negate_exponent(exponent) not in fiber for exponent in fiber):
        raise AssertionError("symmetric source box did not give an antipodal fiber")
    if (0,) * len(bounds) in fiber:
        raise AssertionError("t not in K is required for a fixed-point-free fiber")

    fixed_fiber = {
        add(image(exponent, generators, moduli), scale(target, -1, moduli), moduli)
        for exponent in fiber
    }
    if not fixed_fiber <= kernel:
        raise AssertionError("fiber is not relative to target kernel")
    if tuple(0 for _ in moduli) in fixed_fiber:
        raise AssertionError("exact target unexpectedly appeared in source set")
    if any(scale(value, -1, moduli) not in fixed_fiber for value in fixed_fiber):
        raise AssertionError("kernel fiber is not antipodally symmetric")

    pairs: list[tuple[Exponent, Exponent]] = []
    unseen = set(fiber)
    while unseen:
        left = min(unseen)
        right = negate_exponent(left)
        if right == left or right not in unseen:
            raise AssertionError("antipodal pairing failed")
        pairs.append((left, right))
        unseen.remove(left)
        unseen.remove(right)

    pair_receipts: list[dict[str, object]] = []
    demand_units: list[tuple[int, int, int]] = []
    for pair_index, (left, right) in enumerate(pairs):
        oriented = max(left, right)
        delta = tuple(2 * coordinate for coordinate in oriented)
        relation = image(delta, generators, moduli)
        if relation not in kernel or relation == tuple(0 for _ in moduli):
            raise AssertionError("antipodal difference did not generate the odd kernel")
        overflow = tuple(
            max(abs(coordinate) - bound, 0)
            for coordinate, bound in zip(delta, bounds)
        )
        signed_overflow = tuple(
            (1 if coordinate >= 0 else -1) * amount
            for coordinate, amount in zip(delta, overflow)
        )
        near = not any(overflow)
        if near and any(abs(coordinate) > bound for coordinate, bound in zip(delta, bounds)):
            raise AssertionError("near relation exceeded its exponent box")
        if not near:
            for coordinate, amount in enumerate(overflow):
                for level in range(1, amount + 1):
                    demand_units.append((pair_index, coordinate, level))
        pair_receipts.append(
            {
                "pair_index": pair_index,
                "left": list(left),
                "right": list(right),
                "delta": list(delta),
                "kernel_relation": list(relation),
                "short_kernel_source_generator": near,
                "overflow": list(overflow),
                "signed_overflow": list(signed_overflow),
            }
        )

    return {
        "moduli": list(moduli),
        "kernel": [list(element) for element in sorted(kernel)],
        "kernel_fiber_size": len(fixed_fiber),
        "source_coset_fiber_size": len(fiber),
        "pair_count": len(pairs),
        "short_pair_count": sum(
            bool(receipt["short_kernel_source_generator"]) for receipt in pair_receipts
        ),
        "overflow_pair_count": sum(
            not bool(receipt["short_kernel_source_generator"]) for receipt in pair_receipts
        ),
        "overflow_unit_count": len(demand_units),
        "overflow_unit_lower_bound": sum(
            not bool(receipt["short_kernel_source_generator"]) for receipt in pair_receipts
        ),
        "pairs": pair_receipts,
        "certificate_type": (
            "SHORT_KERNEL_SOURCE_GENERATOR"
            if any(receipt["short_kernel_source_generator"] for receipt in pair_receipts)
            else "KERNEL_PAIR_OVERFLOW_DEMAND"
        ),
    }


def hall_capacity_certificate(
    demands: Sequence[tuple[int, int, int]],
    slot_capacities: Mapping[str, int],
    allowed_slots: Mapping[tuple[int, int, int], Sequence[str]],
) -> dict[str, object]:
    demand_ids = tuple(demands)
    for demand in demand_ids:
        if demand not in allowed_slots:
            raise AssertionError("every demand needs an explicit slot neighborhood")
    best: tuple[int, tuple[tuple[int, int, int], ...], int] | None = None
    for size in range(1, len(demand_ids) + 1):
        for subset in combinations(demand_ids, size):
            neighborhood = {
                slot for demand in subset for slot in allowed_slots[demand]
            }
            capacity = sum(slot_capacities.get(slot, 0) for slot in neighborhood)
            deficit = size - capacity
            if deficit > 0 and (best is None or deficit > best[0]):
                best = (deficit, tuple(subset), capacity)
    if best is None:
        return {
            "status": "FULL_SLOT_ASSIGNMENT_POSSIBLE",
            "demand_count": len(demand_ids),
            "total_capacity": sum(slot_capacities.values()),
        }
    deficit, subset, capacity = best
    return {
        "status": "HALL_Q_ADIC_CAPACITY_DEFICIT",
        "demand_count": len(demand_ids),
        "subset": [list(demand) for demand in subset],
        "neighborhood_capacity": capacity,
        "strict_deficit": deficit,
    }


def verify() -> None:
    common = {
        "moduli": (2, 3),
        "generators": ((1, 1),),
        "target": (1, 0),
        "kernel_generator": (0, 1),
    }
    overflow = top_kernel_pair_profile(bounds=(1,), **common)
    assert overflow["source_coset_fiber_size"] == 2
    assert overflow["pair_count"] == 1
    assert overflow["short_pair_count"] == 0
    assert overflow["overflow_unit_count"] == 1
    assert overflow["overflow_unit_lower_bound"] == 1
    pair = overflow["pairs"][0]
    assert pair["delta"] == [2]
    assert pair["kernel_relation"] == [0, 2]
    assert pair["signed_overflow"] == [1]
    assert overflow["certificate_type"] == "KERNEL_PAIR_OVERFLOW_DEMAND"

    short = top_kernel_pair_profile(bounds=(2,), **common)
    assert short["pair_count"] == 1
    assert short["short_pair_count"] == 1
    assert short["overflow_unit_count"] == 0
    assert short["certificate_type"] == "SHORT_KERNEL_SOURCE_GENERATOR"

    demand = [(0, 0, 1)]
    matched = hall_capacity_certificate(
        demand,
        {"q=3:layer=1": 1},
        {demand[0]: ("q=3:layer=1",)},
    )
    assert matched["status"] == "FULL_SLOT_ASSIGNMENT_POSSIBLE"
    deficit = hall_capacity_certificate(demand, {}, {demand[0]: ()})
    assert deficit["status"] == "HALL_Q_ADIC_CAPACITY_DEFICIT"
    assert deficit["strict_deficit"] == 1

    doubled = [(0, 0, 1), (1, 0, 1)]
    cross_state = hall_capacity_certificate(
        doubled,
        {"q=3:layer=1": 1},
        {demand: ("q=3:layer=1",) for demand in doubled},
    )
    assert cross_state["status"] == "HALL_Q_ADIC_CAPACITY_DEFICIT"
    assert cross_state["strict_deficit"] == 1
    assert cross_state["neighborhood_capacity"] == 1

    print("verified top odd-kernel pair/overflow capacity dichotomy")
    print(
        {
            "overflow": "one_signed_unit",
            "short_relation": "delta=2_maps_to_kernel_generator",
            "matched_slot": "capacity_one",
            "cross_state": "hall_deficit_one",
        }
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
