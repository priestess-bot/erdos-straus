#!/usr/bin/env python3
"""Verify the exact-flow negative-certificate relay dispatch."""

from __future__ import annotations

import argparse
from itertools import combinations


def dot_f2(left: int, right: int) -> int:
    return (left & right).bit_count() & 1


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


def independent(vectors: tuple[int, ...]) -> bool:
    return rank_f2(vectors) == len(vectors)


def slot_copies(capacities: dict[str, int]) -> dict[str, tuple[str, ...]]:
    return {
        slot: tuple(f"{slot}#{index}" for index in range(capacity))
        for slot, capacity in capacities.items()
    }


def active_neighbors(
    demands: dict[str, tuple[str, ...]], capacities: dict[str, int]
) -> dict[str, tuple[str, ...]]:
    copies = slot_copies(capacities)
    return {
        token: tuple(
            copy
            for slot in neighbors
            for copy in copies.get(slot, ())
        )
        for token, neighbors in demands.items()
    }


def max_matching(neighbors: dict[str, tuple[str, ...]]) -> int:
    tokens = tuple(neighbors)
    best = 0

    def visit(index: int, used: set[str], value: int) -> None:
        nonlocal best
        best = max(best, value)
        if index == len(tokens):
            return
        token = tokens[index]
        visit(index + 1, used, value)
        for copy in neighbors[token]:
            if copy not in used:
                used.add(copy)
                visit(index + 1, used, value + 1)
                used.remove(copy)

    visit(0, set(), 0)
    return best


def hall_witness(
    neighbors: dict[str, tuple[str, ...]],
) -> tuple[tuple[str, ...], tuple[str, ...]] | None:
    tokens = tuple(neighbors)
    for size in range(1, len(tokens) + 1):
        for selected in combinations(tokens, size):
            adjacent = tuple(
                sorted({copy for token in selected for copy in neighbors[token]})
            )
            if len(adjacent) < size:
                return selected, adjacent
    return None


def dual_separator(
    neighbor_vectors: tuple[int, ...], request_vectors: tuple[int, ...]
) -> int | None:
    dimension = max(
        1,
        *(value.bit_length() for value in neighbor_vectors + request_vectors),
    )
    for functional in range(1, 1 << dimension):
        if any(dot_f2(functional, vector) for vector in neighbor_vectors):
            continue
        if any(dot_f2(functional, vector) for vector in request_vectors):
            return functional
    return None


def canonicalization_status(
    signatures: dict[str, tuple[tuple[object, ...], ...]] | None,
) -> str | None:
    if signatures is None:
        return None
    for values in signatures.values():
        if values and any(value != values[0] for value in values[1:]):
            return "OWNER_TOKEN_SOURCE_CANONICALIZATION_OBSTRUCTED"
    return None


def lambda_dispatch(
    functional: int,
    global_vectors: tuple[int, ...],
    *,
    target_phase: bool,
    kernel_nontriv: bool,
    escape_action: str,
) -> dict[str, object]:
    if any(dot_f2(functional, vector) for vector in global_vectors):
        return {"status": escape_action, "lambda": functional}
    if target_phase:
        if kernel_nontriv:
            return {
                "status": "GLOBAL_ANNIHILATOR_LOWER_RELAY",
                "lambda": functional,
            }
        return {"status": "TOP_PRIMARY_ANNIHILATOR", "lambda": functional}
    return {"status": "ANNIHILATOR_SUBGROUP_LOWER_RELAY", "lambda": functional}


def dispatch(
    demands: dict[str, tuple[str, ...]],
    capacities: dict[str, int],
    *,
    request_vectors: dict[str, int],
    slot_vectors: dict[str, int],
    global_vectors: tuple[int, ...],
    target_phase: bool,
    kernel_nontriv: bool,
    rank_mode: bool = False,
    signatures: dict[str, tuple[tuple[object, ...], ...]] | None = None,
    escape_action: str = "SOURCE_COLUMN_EDGE_OBSTRUCTED",
) -> dict[str, object]:
    blocked = canonicalization_status(signatures)
    if blocked is not None:
        return {"status": blocked}

    neighbors = active_neighbors(demands, capacities)
    tokens = tuple(demands)
    flow = max_matching(neighbors)
    if flow < len(tokens):
        witness = hall_witness(neighbors)
        assert witness is not None
        selected, adjacent = witness
        selected_vectors = tuple(request_vectors[token] for token in selected)
        if not independent(selected_vectors):
            return {
                "status": "DEPENDENT_SOURCE_ESCAPE_RELATION",
                "flow": flow,
                "witness": selected,
            }
        copies = tuple(
            slot
            for copy in adjacent
            for slot in slot_vectors
            if copy.startswith(f"{slot}#")
        )
        neighbor_vectors = tuple(slot_vectors[slot] for slot in copies)
        functional = dual_separator(neighbor_vectors, selected_vectors)
        assert functional is not None
        result = lambda_dispatch(
            functional,
            global_vectors,
            target_phase=target_phase,
            kernel_nontriv=kernel_nontriv,
            escape_action=escape_action,
        )
        result.update({"flow": flow, "witness": selected})
        return result

    if rank_mode:
        active_vectors = tuple(
            slot_vectors[slot]
            for slot, capacity in capacities.items()
            if capacity > 0
        )
        role_count = len(tokens)
        source_rank = rank_f2(active_vectors)
        if source_rank < role_count:
            selected_vectors = tuple(request_vectors[token] for token in tokens)
            functional = dual_separator(active_vectors, selected_vectors)
            assert functional is not None
            result = lambda_dispatch(
                functional,
                global_vectors,
                target_phase=target_phase,
                kernel_nontriv=kernel_nontriv,
                escape_action=escape_action,
            )
            result.update({"flow": flow, "rank": source_rank})
            return result

    return {
        "status": "SOURCE_COMPLETE_CAPACITY_CERT",
        "flow": flow,
    }


def run_verification() -> dict[str, object]:
    deficit_closed = dispatch(
        {"x1": ("q5",), "x2": ("q5",)},
        {"q5": 1},
        request_vectors={"x1": 1, "x2": 2},
        slot_vectors={"q5": 0},
        global_vectors=(0,),
        target_phase=True,
        kernel_nontriv=True,
    )
    assert deficit_closed["status"] == "GLOBAL_ANNIHILATOR_LOWER_RELAY"

    escape_release = dispatch(
        {"x1": ("q5",), "x2": ("q5",)},
        {"q5": 1},
        request_vectors={"x1": 1, "x2": 2},
        slot_vectors={"q5": 0},
        global_vectors=(1,),
        target_phase=True,
        kernel_nontriv=True,
        escape_action="Q_ADIC_ESCAPE_EXPANSION_RELEASE",
    )
    assert escape_release["status"] == "Q_ADIC_ESCAPE_EXPANSION_RELEASE"

    dependent = dispatch(
        {"x1": ("q5",), "x2": ("q5",)},
        {"q5": 1},
        request_vectors={"x1": 1, "x2": 1},
        slot_vectors={"q5": 0},
        global_vectors=(0,),
        target_phase=True,
        kernel_nontriv=True,
    )
    assert dependent["status"] == "DEPENDENT_SOURCE_ESCAPE_RELATION"

    rank_closed = dispatch(
        {"x1": ("q3",), "x2": ("q7",)},
        {"q3": 1, "q7": 1},
        request_vectors={"x1": 1, "x2": 2},
        slot_vectors={"q3": 1, "q7": 1},
        global_vectors=(0,),
        target_phase=False,
        kernel_nontriv=True,
        rank_mode=True,
    )
    assert rank_closed["status"] == "ANNIHILATOR_SUBGROUP_LOWER_RELAY"

    top_primary = dispatch(
        {"x1": ("q5",)},
        {"q5": 0},
        request_vectors={"x1": 1},
        slot_vectors={"q5": 0},
        global_vectors=(0,),
        target_phase=True,
        kernel_nontriv=False,
    )
    assert top_primary["status"] == "TOP_PRIMARY_ANNIHILATOR"

    nonuniform = dispatch(
        {"x1": ("q5",)},
        {"q5": 1},
        request_vectors={"x1": 1},
        slot_vectors={"q5": 1},
        global_vectors=(0,),
        target_phase=True,
        kernel_nontriv=True,
        signatures={
            "q5": (("q5", "owner-a", 1), ("q5", "owner-b", 2)),
        },
    )
    assert nonuniform["status"] == "OWNER_TOKEN_SOURCE_CANONICALIZATION_OBSTRUCTED"

    return {
        "deficit_closed": deficit_closed,
        "escape_release": escape_release,
        "dependent": dependent,
        "rank_closed": rank_closed,
        "top_primary": top_primary,
        "nonuniform": nonuniform,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified exact-flow negative-certificate relay")
    for key, value in result.items():
        print(key, value["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
