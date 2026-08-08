#!/usr/bin/env python3
"""Verify finite joint owner matching closure."""

from __future__ import annotations

import argparse
from itertools import combinations, permutations


Vector = tuple[int, int]
Edge = tuple[str, str, Vector]
REQUESTS = ("r1", "r2")
SLOTS = ("c1", "c2")
E1: Vector = (1, 0)
E2: Vector = (0, 1)


def rank_f2(vectors: list[Vector]) -> int:
    pivots: dict[int, int] = {}
    for vector in vectors:
        reduced = (vector[0] << 1) | vector[1]
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = reduced
                break
            reduced ^= pivots[pivot]
    return len(pivots)


def physical_matchings(
    edges: dict[str, dict[str, Edge]], slots: tuple[str, ...] = SLOTS
) -> list[tuple[Edge, ...]]:
    result = []
    for assignment in permutations(slots, len(REQUESTS)):
        selected: list[Edge] = []
        for request, slot in zip(REQUESTS, assignment):
            edge = edges[request].get(slot)
            if edge is None:
                break
            selected.append(edge)
        else:
            tokens = [edge[0] for edge in selected]
            if len(tokens) == len(set(tokens)):
                result.append(tuple(selected))
    return result


def minimal_circuit(matching: tuple[Edge, ...]) -> tuple[int, ...]:
    for size in range(2, len(matching) + 1):
        for subset in combinations(range(len(matching)), size):
            if rank_f2([matching[index][2] for index in subset]) < size:
                return subset
    raise AssertionError("matching is independent")


def joint_closure(edges: dict[str, dict[str, Edge]]) -> dict[str, object]:
    matchings = physical_matchings(edges)
    if not matchings:
        return {"status": "OWNER_JOINT_PHYSICAL_HALL_DEFICIT", "matchings": 0}
    independent = [
        matching
        for matching in matchings
        if rank_f2([edge[2] for edge in matching]) == len(REQUESTS)
    ]
    if independent:
        return {
            "status": "OWNER_JOINT_SOURCE_MATCH",
            "matching": independent[0],
        }
    circuits = [
        (matching, minimal_circuit(matching))
        for matching in matchings
    ]
    return {
        "status": "OWNER_JOINT_SOURCE_SLOT_OBSTRUCTION",
        "matching_count": len(matchings),
        "circuits": circuits,
    }


def run_verification() -> dict[str, object]:
    nonuniform = {
        "r1": {
            "c1": ("r1c1", "c1", E1),
            "c2": ("r1c2", "c2", E2),
        },
        "r2": {
            "c1": ("r2c1", "c1", E2),
            "c2": ("r2c2", "c2", E1),
        },
    }
    obstruction = joint_closure(nonuniform)
    assert obstruction["status"] == "OWNER_JOINT_SOURCE_SLOT_OBSTRUCTION"
    assert obstruction["matching_count"] == 2

    uniform = {
        "r1": {
            "c1": ("r1c1", "c1", E1),
            "c2": ("r1c2", "c2", E2),
        },
        "r2": {
            "c1": ("r2c1", "c1", E1),
            "c2": ("r2c2", "c2", E2),
        },
    }
    source_match = joint_closure(uniform)
    assert source_match["status"] == "OWNER_JOINT_SOURCE_MATCH"

    physical_empty = {
        "r1": {"c1": ("r1c1", "c1", E1)},
        "r2": {"c1": ("r2c1", "c1", E2)},
    }
    physical_deficit = joint_closure(physical_empty)
    assert physical_deficit["status"] == "OWNER_JOINT_PHYSICAL_HALL_DEFICIT"

    return {
        "nonuniform": obstruction,
        "uniform": source_match,
        "physical_empty": physical_deficit,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified finite joint owner matching closure")
    for key in ("nonuniform", "uniform", "physical_empty"):
        print(key, result[key]["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
