#!/usr/bin/env python3
"""Verify owner-flow-gated constructive primary/dyadic terminal dispatch."""

from __future__ import annotations

import argparse
from collections import Counter
from typing import Iterable

from type_ii_owner_saturation_quotient_kernel_dispatch import (
    owner_saturation_dispatch,
)


def exact_valuation(value: int, prime: int, exponent: int) -> int:
    """Return the exact prime layer of a nonzero residue in C_prime^exponent."""
    modulus = prime**exponent
    residue = value % modulus
    if residue == 0:
        raise ValueError("zero residue has no exact primary layer")
    level = 0
    while level + 1 < exponent and residue % (prime ** (level + 1)) == 0:
        level += 1
    return level


def flow_pass(slots: Iterable[str], budgets: dict[str, int]) -> bool:
    """Check only physical-slot capacity; owner labels are intentionally absent."""
    used = Counter(slots)
    return all(used[slot] <= budgets.get(slot, 0) for slot in used)


def reachable_with_masks(vectors: list[int], modulus: int) -> dict[int, tuple[int, ...]]:
    """Return one deterministic binary mask for every reachable residue."""
    states: dict[int, tuple[int, ...]] = {0: ()}
    for index, vector in enumerate(vectors):
        updates = dict(states)
        for residue, mask in states.items():
            candidate = (residue + vector) % modulus
            candidate_mask = mask + (index,)
            if candidate not in updates or candidate_mask < updates[candidate]:
                updates[candidate] = candidate_mask
        states = updates
    return states


def owner_primary_dispatch(
    vectors: list[int],
    target: int,
    prime: int,
    exponent: int,
    *,
    slots: tuple[str, ...],
    budgets: dict[str, int],
    compatible: bool = True,
) -> dict[str, object]:
    """Apply the owner gate, then the primary digit selector."""
    if not compatible:
        return {"status": "KERNEL_FOURIER_LIFT_OBSTRUCTED"}
    if len(vectors) != len(slots):
        raise ValueError("each primary block needs one flow edge")
    if not flow_pass(slots, budgets):
        return {"status": "OWNER_PROJECTION_CAPACITY_DEFICIT"}

    modulus = prime**exponent
    levels = [exact_valuation(vector, prime, exponent) for vector in vectors]
    counts = [levels.count(layer) for layer in range(exponent)]
    deficits = [layer for layer, count in enumerate(counts) if count < prime - 1]
    normalized_target = target % modulus

    if not deficits:
        reachable = reachable_with_masks(vectors, modulus)
        if normalized_target not in reachable:
            raise AssertionError("primary cover theorem was not realized")
        return {
            "status": "OWNER_PRIMARY_TYPE_II_SHORT_CERTIFICATE",
            "mask": reachable[normalized_target],
            "counts": counts,
        }

    highest = max(deficits)
    if highest == exponent - 1:
        return {
            "status": "TOP_PRIMARY_DIGIT_DEFICIT",
            "highest_layer": highest,
            "counts": counts,
        }

    quotient = prime ** (highest + 1)
    lower_vectors = [
        vector % quotient for vector, layer in zip(vectors, levels) if layer <= highest
    ]
    lower_reachable = reachable_with_masks(lower_vectors, quotient)
    projected_target = normalized_target % quotient
    if projected_target in lower_reachable:
        raise AssertionError("a missing target was reachable in the primary quotient")

    tail_vectors = [
        vector for vector, layer in zip(vectors, levels) if layer > highest
    ]
    tail_reachable = reachable_with_masks(tail_vectors, modulus)
    expected_tail = set(range(0, modulus, quotient))
    if set(tail_reachable) != expected_tail:
        raise AssertionError("saturated primary tail did not fill its subgroup")

    return {
        "status": "HIGHEST_PRIMARY_DEFICIT_QUOTIENT",
        "highest_layer": highest,
        "quotient": quotient,
        "projected_target": projected_target,
        "counts": counts,
        "tail_size": len(tail_reachable),
    }


def run_verification() -> dict[str, object]:
    # The preceding owner selector must route a height-one order-two block to a
    # kernel split before this primary terminal is entered.
    assert owner_saturation_dispatch(
        1, 2, direct_hit=False, quotient_hit=True
    ) == "SATURATED_OWNER_KERNEL_SPLIT"

    # C8: one physical block in each 2-adic layer gives a constructive hit.
    full = owner_primary_dispatch(
        [1, 2, 4],
        7,
        2,
        3,
        slots=("c0", "c1", "c2"),
        budgets={"c0": 1, "c1": 1, "c2": 1},
    )
    assert full["status"] == "OWNER_PRIMARY_TYPE_II_SHORT_CERTIFICATE"
    assert sum((1, 2, 4)[index] for index in full["mask"]) == 7

    # C16: the highest deficient layer is one, and the saturated tail is 4*C16.
    quotient = owner_primary_dispatch(
        [4, 8],
        1,
        2,
        4,
        slots=("c2", "c3"),
        budgets={"c2": 1, "c3": 1},
    )
    assert quotient["status"] == "HIGHEST_PRIMARY_DEFICIT_QUOTIENT"
    assert quotient["highest_layer"] == 1
    assert quotient["quotient"] == 4
    assert quotient["tail_size"] == 4

    # C8: a missing top 2-adic digit is a terminal, not a same-order quotient.
    top = owner_primary_dispatch(
        [1, 2],
        4,
        2,
        3,
        slots=("c0", "c1"),
        budgets={"c0": 1, "c1": 1},
    )
    assert top["status"] == "TOP_PRIMARY_DIGIT_DEFICIT"
    assert top["highest_layer"] == 2

    # C9: the same constructive rule works for an odd primary.
    odd = owner_primary_dispatch(
        [1, 1, 3, 3],
        8,
        3,
        2,
        slots=("d0", "d1", "d2", "d3"),
        budgets={"d0": 1, "d1": 1, "d2": 1, "d3": 1},
    )
    assert odd["status"] == "OWNER_PRIMARY_TYPE_II_SHORT_CERTIFICATE"

    # Two owner labels on one physical slot cannot pass to the digit selector.
    collision = owner_primary_dispatch(
        [1, 2],
        3,
        2,
        2,
        slots=("same-slot", "same-slot"),
        budgets={"same-slot": 1},
    )
    assert collision["status"] == "OWNER_PROJECTION_CAPACITY_DEFICIT"

    # An affine role that is not a genuine source-relation character stops first.
    obstructed = owner_primary_dispatch(
        [1],
        1,
        2,
        1,
        slots=("c0",),
        budgets={"c0": 1},
        compatible=False,
    )
    assert obstructed["status"] == "KERNEL_FOURIER_LIFT_OBSTRUCTED"

    return {
        "saturation_entry": "SATURATED_OWNER_KERNEL_SPLIT",
        "full": full,
        "quotient": quotient,
        "top": top,
        "odd_primary": odd,
        "collision": collision,
        "obstructed": obstructed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner kernel primary digit certificate")
    for key in ("full", "quotient", "top", "odd_primary", "collision", "obstructed"):
        value = result[key]
        print(key, value["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
