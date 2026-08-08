#!/usr/bin/env python3
"""Verify the owner circuit q-capacity flow bridge."""

from __future__ import annotations

import argparse


def max_flow(
    demands: dict[str, tuple[str, ...]], capacities: dict[str, int]
) -> int:
    """Solve the small bipartite capacity flow by recursive assignment."""
    names = tuple(demands)
    best = 0

    def visit(index: int, remaining: dict[str, int], value: int) -> None:
        nonlocal best
        best = max(best, value)
        if index == len(names):
            return
        name = names[index]
        visit(index + 1, remaining, value)
        for slot in demands[name]:
            if remaining.get(slot, 0) > 0:
                remaining[slot] -= 1
                visit(index + 1, remaining, value + 1)
                remaining[slot] += 1

    visit(0, capacities.copy(), 0)
    return best


def rank_f2(vectors: tuple[int, ...]) -> int:
    pivots: dict[int, int] = {}
    for value in vectors:
        reduced = value
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = reduced
                break
            reduced ^= pivots[pivot]
    return len(pivots)


def dispatch(
    demands: dict[str, tuple[str, ...]],
    capacities: dict[str, int],
    *,
    role_count: int,
    slot_vectors: dict[str, int],
    direct: bool = False,
) -> dict[str, object]:
    demand_count = len(demands)
    flow = max_flow(demands, capacities)
    if flow < demand_count:
        return {
            "status": "CIRCUIT_Q_CAPACITY_DEFICIT",
            "flow": flow,
            "demand": demand_count,
        }
    source_rank = rank_f2(tuple(slot_vectors[slot] for slot in capacities))
    if source_rank < role_count:
        return {
            "status": "CIRCUIT_SOURCE_RANK_DEFICIT",
            "rank": source_rank,
            "roles": role_count,
        }
    if direct:
        return {"status": "CIRCUIT_TYPE_II_SHORT_CERTIFICATE", "flow": flow}
    return {
        "status": "CIRCUIT_SOURCE_COMPLETE_CAPACITY_CERT",
        "flow": flow,
        "rank": source_rank,
    }


def run_verification() -> dict[str, object]:
    direct = dispatch(
        {"C17": ("q17",), "C7": ("q7",)},
        {"q17": 1, "q7": 1},
        role_count=2,
        slot_vectors={"q17": 2, "q7": 1},
        direct=True,
    )
    assert direct["status"] == "CIRCUIT_TYPE_II_SHORT_CERTIFICATE"

    collision = dispatch(
        {"C1": ("q5",), "C2": ("q5",)},
        {"q5": 1},
        role_count=2,
        slot_vectors={"q5": 1},
    )
    assert collision["status"] == "CIRCUIT_Q_CAPACITY_DEFICIT"
    assert collision["flow"] == 1

    rank_deficit = dispatch(
        {"C1": ("q3",), "C2": ("q7",)},
        {"q3": 1, "q7": 1},
        role_count=2,
        slot_vectors={"q3": 1, "q7": 1},
    )
    assert rank_deficit["status"] == "CIRCUIT_SOURCE_RANK_DEFICIT"

    ready = dispatch(
        {"C1": ("q3",), "C2": ("q7",)},
        {"q3": 1, "q7": 1},
        role_count=2,
        slot_vectors={"q3": 2, "q7": 1},
    )
    assert ready["status"] == "CIRCUIT_SOURCE_COMPLETE_CAPACITY_CERT"

    return {
        "direct": direct,
        "collision": collision,
        "rank_deficit": rank_deficit,
        "ready": ready,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner circuit q-capacity flow bridge")
    for key, value in result.items():
        print(key, value["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
