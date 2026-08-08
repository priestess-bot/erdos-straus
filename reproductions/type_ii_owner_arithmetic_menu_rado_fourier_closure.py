#!/usr/bin/env python3
"""Verify arithmetic-filtered owner graph closure."""

from __future__ import annotations

import argparse
import cmath
from itertools import combinations


def subsets(requests: tuple[int, ...]) -> tuple[frozenset[int], ...]:
    """Return canonical nonempty request subsets."""
    return tuple(
        frozenset(combination)
        for size in range(1, len(requests) + 1)
        for combination in combinations(requests, size)
    )


def graph_closure(
    requests: tuple[int, ...],
    q_capacity: dict[frozenset[int], int],
    source_rank: dict[frozenset[int], int],
    arithmetic_neighbors: dict[frozenset[int], int],
    physical_flow: dict[frozenset[int], int],
    *,
    direct_certificate: bool,
    matched: bool,
    support: set[int] | None = None,
    target: int | None = None,
    modulus: int | None = None,
    source_compatible: bool = True,
) -> dict[str, object]:
    """Apply q, arithmetic-menu, physical-flow, rank, then Fourier priority."""
    ordered = sorted(subsets(requests), key=lambda subset: (len(subset), tuple(sorted(subset))))
    for subset in ordered:
        if q_capacity[subset] < len(subset):
            return {
                "status": "OWNER_GRAPH_Q_ADIC_CAPACITY_DEFICIT",
                "subset": tuple(sorted(subset)),
                "capacity": q_capacity[subset],
            }
    for subset in ordered:
        if arithmetic_neighbors[subset] < len(subset):
            return {
                "status": "OWNER_GRAPH_ARITHMETIC_HALL_DEFICIT",
                "subset": tuple(sorted(subset)),
                "neighbors": arithmetic_neighbors[subset],
            }
    for subset in ordered:
        if physical_flow[subset] < len(subset):
            return {
                "status": "OWNER_GRAPH_PHYSICAL_HALL_DEFICIT",
                "subset": tuple(sorted(subset)),
                "flow": physical_flow[subset],
            }
    for subset in ordered:
        if source_rank[subset] < len(subset):
            return {
                "status": "OWNER_GRAPH_SOURCE_RANK_DEFICIT",
                "subset": tuple(sorted(subset)),
                "rank": source_rank[subset],
            }
    if not matched:
        return {
            "status": "OWNER_GRAPH_RADO_MATCHING_OBSTRUCTED",
            "subset": requests,
        }
    if direct_certificate:
        return {"status": "OWNER_GRAPH_TYPE_II_SHORT_CERTIFICATE"}
    if support is None or target is None or modulus is None:
        raise ValueError("Fourier closure needs a finite support and target")
    if target % modulus in {point % modulus for point in support}:
        raise AssertionError("Fourier branch received a direct target")
    coefficients: list[tuple[float, int, complex]] = []
    for frequency in range(1, modulus):
        coefficient = sum(
            cmath.exp(-2j * cmath.pi * frequency * point / modulus)
            for point in support
        ) - cmath.exp(-2j * cmath.pi * frequency * target / modulus)
        coefficients.append((abs(coefficient), frequency, coefficient))
    coefficients.sort(key=lambda row: (-row[0], row[1]))
    amplitude, frequency, coefficient = coefficients[0]
    if amplitude <= 1e-9 or not source_compatible:
        return {
            "status": "OWNER_GRAPH_FOURIER_LIFT_OBSTRUCTED",
            "frequency": frequency,
            "amplitude": amplitude,
        }
    return {
        "status": "OWNER_GRAPH_SOURCE_RELATION_FOURIER",
        "frequency": frequency,
        "coefficient": coefficient,
    }


def one_request_maps(
    *,
    q_capacity: int,
    rank: int,
    arithmetic_neighbors: int,
) -> tuple[
    dict[frozenset[int], int],
    dict[frozenset[int], int],
    dict[frozenset[int], int],
    dict[frozenset[int], int],
]:
    subset = frozenset({0})
    return (
        {subset: q_capacity},
        {subset: rank},
        {subset: arithmetic_neighbors},
        {subset: min(q_capacity, arithmetic_neighbors)},
    )


def run_verification() -> dict[str, object]:
    # p=5113: one owner edge passes all gates and E4.
    q_map, rank_map, arith_map, flow_map = one_request_maps(
        q_capacity=1, rank=1, arithmetic_neighbors=1
    )
    direct = graph_closure(
        (0,),
        q_map,
        rank_map,
        arith_map,
        flow_map,
        direct_certificate=True,
        matched=True,
    )
    assert direct["status"] == "OWNER_GRAPH_TYPE_II_SHORT_CERTIFICATE"

    # p=433: q capacity is selected before rank or arithmetic diagnostics.
    requests = (0, 1)
    all_subsets = subsets(requests)
    q_capacity = {subset: (1 if len(subset) == 2 else 1) for subset in all_subsets}
    rank = {subset: len(subset) for subset in all_subsets}
    arithmetic = {subset: len(subset) for subset in all_subsets}
    flow = {subset: len(subset) for subset in all_subsets}
    q_deficit = graph_closure(
        requests,
        q_capacity,
        rank,
        arithmetic,
        flow,
        direct_certificate=False,
        matched=False,
    )
    assert q_deficit["status"] == "OWNER_GRAPH_Q_ADIC_CAPACITY_DEFICIT"
    assert q_deficit["subset"] == (0, 1)

    # Same graph with enough q slots but only one independent source column.
    q_capacity = {subset: len(subset) for subset in all_subsets}
    rank = {subset: (1 if len(subset) == 2 else 1) for subset in all_subsets}
    flow = {subset: len(subset) for subset in all_subsets}
    rank_deficit = graph_closure(
        requests,
        q_capacity,
        rank,
        arithmetic,
        flow,
        direct_certificate=False,
        matched=False,
    )
    assert rank_deficit["status"] == "OWNER_GRAPH_SOURCE_RANK_DEFICIT"

    # p=97: arithmetic filtering leaves no legal neighbor.
    rank = {subset: len(subset) for subset in all_subsets}
    arithmetic_empty = {subset: 0 for subset in all_subsets}
    flow = {subset: len(subset) for subset in all_subsets}
    arithmetic_deficit = graph_closure(
        requests,
        q_capacity,
        rank,
        arithmetic_empty,
        flow,
        direct_certificate=False,
        matched=False,
    )
    assert arithmetic_deficit["status"] == "OWNER_GRAPH_ARITHMETIC_HALL_DEFICIT"

    # Two owner tokens can still collide on one physical slot.
    physical_flow = {subset: (1 if len(subset) == 2 else 1) for subset in all_subsets}
    physical_deficit = graph_closure(
        requests,
        q_capacity,
        rank,
        arithmetic,
        physical_flow,
        direct_certificate=False,
        matched=False,
    )
    assert physical_deficit["status"] == "OWNER_GRAPH_PHYSICAL_HALL_DEFICIT"

    # Full necessary conditions but no E4 hit: finite support yields a Fourier role.
    q_map, rank_map, arith_map, flow_map = one_request_maps(
        q_capacity=1, rank=1, arithmetic_neighbors=1
    )
    fourier = graph_closure(
        (0,),
        q_map,
        rank_map,
        arith_map,
        flow_map,
        direct_certificate=False,
        matched=True,
        support={0, 4},
        target=1,
        modulus=8,
    )
    assert fourier["status"] == "OWNER_GRAPH_SOURCE_RELATION_FOURIER"
    assert abs(fourier["coefficient"]) > 1e-9

    obstructed = graph_closure(
        (0,),
        q_map,
        rank_map,
        arith_map,
        flow_map,
        direct_certificate=False,
        matched=True,
        support={0, 4},
        target=1,
        modulus=8,
        source_compatible=False,
    )
    assert obstructed["status"] == "OWNER_GRAPH_FOURIER_LIFT_OBSTRUCTED"

    return {
        "direct": direct,
        "q_deficit": q_deficit,
        "rank_deficit": rank_deficit,
        "arithmetic_deficit": arithmetic_deficit,
        "physical_deficit": physical_deficit,
        "fourier": fourier,
        "obstructed": obstructed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner arithmetic-menu Rado/Fourier closure")
    for key in (
        "direct",
        "q_deficit",
        "rank_deficit",
        "arithmetic_deficit",
        "physical_deficit",
        "fourier",
        "obstructed",
    ):
        print(key, result[key]["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
