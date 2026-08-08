#!/usr/bin/env python3
"""Verify the owner-flow/Rado separation counterexample."""

from __future__ import annotations

import argparse
from itertools import permutations


Vector = tuple[int, int]
REQUESTS = ("r1", "r2")
SLOTS = ("c1", "c2")
E1: Vector = (1, 0)
E2: Vector = (0, 1)
EDGES: dict[str, dict[str, Vector]] = {
    "r1": {"c1": E1, "c2": E2},
    "r2": {"c1": E2, "c2": E1},
}


def rank_f2(vectors: list[Vector]) -> int:
    """Compute the rank of two-coordinate vectors over F_2."""
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


def physical_flow() -> int:
    """The ordinary request-to-slot matching value."""
    value = 0
    for assignment in permutations(SLOTS):
        if len(set(assignment)) == len(assignment):
            value = max(value, len(assignment))
    return value


def independent_perfect_assignments() -> list[tuple[tuple[str, str, Vector], ...]]:
    """Enumerate all physical perfect matchings and retain independent ones."""
    result = []
    for assignment in permutations(SLOTS):
        selected = tuple(
            (request, slot, EDGES[request][slot])
            for request, slot in zip(REQUESTS, assignment)
        )
        if rank_f2([edge[2] for edge in selected]) == len(REQUESTS):
            result.append(selected)
    return result


def run_verification() -> dict[str, object]:
    union_rank = rank_f2(
        [EDGES[request][slot] for request in REQUESTS for slot in SLOTS]
    )
    assert union_rank == 2
    assert physical_flow() == 2
    assert len(independent_perfect_assignments()) == 0

    single_flow = physical_flow()
    assert single_flow >= 1
    return {
        "q_capacity": 2,
        "candidate_neighbors": 2,
        "physical_flow": physical_flow(),
        "union_source_rank": union_rank,
        "independent_perfect_matchings": independent_perfect_assignments(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner-flow/Rado separation counterexample")
    for key, value in result.items():
        print(key, value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
