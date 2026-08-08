#!/usr/bin/env python3
"""Verify the source-preserving owner canonicalization criterion."""

from __future__ import annotations

import argparse
from itertools import permutations


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


def flow_values(edges: dict[str, dict[str, Edge]]) -> tuple[int, int]:
    """Return token-aware and projected slot matching values."""
    token_flow = 0
    slot_flow = 0
    for assignment in permutations(SLOTS):
        selected = [
            edges[request].get(slot)
            for request, slot in zip(REQUESTS, assignment)
        ]
        if all(edge is not None for edge in selected):
            slot_flow = max(slot_flow, len(selected))
            tokens = [edge[0] for edge in selected if edge is not None]
            if len(tokens) == len(set(tokens)):
                token_flow = max(token_flow, len(tokens))
    return token_flow, slot_flow


def fiber_uniform(edges: dict[str, dict[str, Edge]]) -> bool:
    signatures: dict[str, set[tuple[str, Vector]]] = {slot: set() for slot in SLOTS}
    for request in REQUESTS:
        for slot, edge in edges[request].items():
            _, signature, vector = edge
            signatures[slot].add((signature, vector))
    return all(len(values) <= 1 for values in signatures.values())


def canonical_status(
    edges: dict[str, dict[str, Edge]], token_flow: int, slot_flow: int
) -> str:
    if token_flow < len(REQUESTS):
        return "OWNER_TOKEN_ASSIGNMENT_OBSTRUCTED"
    if slot_flow < len(REQUESTS):
        return "OWNER_GRAPH_PHYSICAL_HALL_DEFICIT"
    if not fiber_uniform(edges):
        return "OWNER_TOKEN_SOURCE_CANONICALIZATION_OBSTRUCTED"
    return "CANONICAL_RESOURCE_CERT"


def run_verification() -> dict[str, object]:
    uniform_edges: dict[str, dict[str, Edge]] = {
        "r1": {"c1": ("r1c1", "sigma1", E1), "c2": ("r1c2", "sigma2", E2)},
        "r2": {"c1": ("r2c1", "sigma1", E1), "c2": ("r2c2", "sigma2", E2)},
    }
    uniform_token_flow, uniform_slot_flow = flow_values(uniform_edges)
    assert (uniform_token_flow, uniform_slot_flow) == (2, 2)
    assert fiber_uniform(uniform_edges)
    assert canonical_status(
        uniform_edges, uniform_token_flow, uniform_slot_flow
    ) == "CANONICAL_RESOURCE_CERT"
    assert rank_f2([E1, E2]) == 2

    nonuniform_edges: dict[str, dict[str, Edge]] = {
        "r1": {"c1": ("r1c1", "sigma1", E1), "c2": ("r1c2", "sigma2", E2)},
        "r2": {"c1": ("r2c1", "sigma2", E2), "c2": ("r2c2", "sigma1", E1)},
    }
    nonuniform_token_flow, nonuniform_slot_flow = flow_values(nonuniform_edges)
    assert (nonuniform_token_flow, nonuniform_slot_flow) == (2, 2)
    assert not fiber_uniform(nonuniform_edges)
    assert canonical_status(
        nonuniform_edges, nonuniform_token_flow, nonuniform_slot_flow
    ) == "OWNER_TOKEN_SOURCE_CANONICALIZATION_OBSTRUCTED"

    token_collision = canonical_status(uniform_edges, 1, 2)
    assert token_collision == "OWNER_TOKEN_ASSIGNMENT_OBSTRUCTED"

    return {
        "uniform": canonical_status(
            uniform_edges, uniform_token_flow, uniform_slot_flow
        ),
        "nonuniform": canonical_status(
            nonuniform_edges, nonuniform_token_flow, nonuniform_slot_flow
        ),
        "token_collision": token_collision,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner source-preserving canonicalization criterion")
    for key, value in result.items():
        print(key, value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
