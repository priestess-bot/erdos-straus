#!/usr/bin/env python3
"""Verify the owner-token projection flow gate and collision deficit."""

from __future__ import annotations

import argparse
from collections import deque

from type_ii_target_fiber_owner_weighted_fourier_capacity_bridge import (
    owner_weighted_spectrum,
)


Token = tuple[int, int, int]
Physical = str


def max_flow(
    requests: tuple[int, ...],
    neighborhoods: dict[int, tuple[Token, ...]],
    projection: dict[Token, Physical],
    capacities: dict[Physical, int],
) -> int:
    """Compute the integral flow in the request-token-physical network."""
    source = ("source",)
    sink = ("sink",)
    residual: dict[object, dict[object, int]] = {}

    def add_edge(left: object, right: object, capacity: int) -> None:
        residual.setdefault(left, {})
        residual.setdefault(right, {})
        residual[left][right] = residual[left].get(right, 0) + capacity
        residual[right].setdefault(left, 0)

    for request in requests:
        request_node = ("request", request)
        add_edge(source, request_node, 1)
        for token in neighborhoods[request]:
            token_node = ("token", token)
            physical_node = ("physical", projection[token])
            add_edge(request_node, token_node, 1)
            add_edge(token_node, physical_node, 1)
    for physical, capacity in capacities.items():
        add_edge(("physical", physical), sink, capacity)

    flow = 0
    while True:
        parent: dict[object, object | None] = {source: None}
        queue: deque[object] = deque([source])
        while queue and sink not in parent:
            node = queue.popleft()
            for neighbor, capacity in residual[node].items():
                if capacity > 0 and neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)
        if sink not in parent:
            return flow
        increment = None
        node = sink
        while parent[node] is not None:
            previous = parent[node]
            edge_capacity = residual[previous][node]
            increment = edge_capacity if increment is None else min(increment, edge_capacity)
            node = previous
        assert increment is not None
        node = sink
        while parent[node] is not None:
            previous = parent[node]
            residual[previous][node] -= increment
            residual[node][previous] += increment
            node = previous
        flow += increment


def flow_gate(
    requests: tuple[int, ...],
    neighborhoods: dict[int, tuple[Token, ...]],
    projection: dict[Token, Physical],
    capacities: dict[Physical, int],
) -> dict[str, object]:
    token_set = {
        token for request in requests for token in neighborhoods[request]
    }
    physical_set = {projection[token] for token in token_set}
    physical_capacity = sum(capacities[physical] for physical in physical_set)
    value = max_flow(requests, neighborhoods, projection, capacities)
    if physical_capacity < len(requests):
        status = "OWNER_PROJECTION_CAPACITY_DEFICIT"
    elif value < len(requests):
        status = "OWNER_TOKEN_ASSIGNMENT_OBSTRUCTED"
    else:
        status = "OWNER_FLOW_PASS"
    return {
        "status": status,
        "token_mass": len(token_set),
        "physical_capacity": physical_capacity,
        "flow": value,
        "request_count": len(requests),
    }


def gf2_basis(vectors: tuple[int, ...]) -> tuple[int, ...]:
    """Return a compact Gaussian basis for bit-vector coordinates over F_2."""
    pivots: dict[int, int] = {}
    for value in vectors:
        reduced = value
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = reduced
                break
            reduced ^= pivots[pivot]
    return tuple(pivots.values())


def gf2_contains(value: int, basis: tuple[int, ...]) -> bool:
    """Test membership in a bit-vector span."""
    pivots = {vector.bit_length() - 1: vector for vector in basis}
    reduced = value
    while reduced:
        pivot = reduced.bit_length() - 1
        if pivot not in pivots:
            return False
        reduced ^= pivots[pivot]
    return True


def linear_deficit_status(
    demands: tuple[int, ...], token_columns: tuple[int, ...]
) -> dict[str, object]:
    """Separate a physical collision from a source-column annihilator."""
    demand_basis = gf2_basis(demands)
    token_basis = gf2_basis(token_columns)
    outside = tuple(
        vector for vector in demand_basis if not gf2_contains(vector, token_basis)
    )
    status = (
        "OWNER_PROJECTION_RANK_ANNIHILATOR"
        if outside
        else "OWNER_COLLISION_ONLY"
    )
    return {
        "status": status,
        "demand_rank": len(demand_basis),
        "token_rank": len(token_basis),
        "outside_demand": outside,
    }


def run_verification() -> dict[str, object]:
    # Real owner collision: two source rows expose one physical q factor.
    p_collision = 57_399_241
    collision_sources = {
        1: p_collision + 4 * 41,
        41: p_collision + 4 * 41 * 41,
    }
    collision_target = p_collision + 4
    collision_profile = owner_weighted_spectrum(
        collision_sources, collision_target, 4
    )
    assert collision_profile["heights"] == {5: 1}
    owners = collision_profile["owner_counts"][5][1]
    assert owners == (1, 41)
    assert collision_profile["weights"] == {1: 3}
    collision_tokens = tuple((5, 1, owner) for owner in owners)
    collision_neighborhoods = {0: collision_tokens, 1: collision_tokens}
    collision_projection = {token: "q5" for token in collision_tokens}
    collision = flow_gate(
        (0, 1),
        collision_neighborhoods,
        collision_projection,
        {"q5": 1},
    )
    assert collision == {
        "status": "OWNER_PROJECTION_CAPACITY_DEFICIT",
        "token_mass": 2,
        "physical_capacity": 1,
        "flow": 1,
        "request_count": 2,
    }

    # Real no-collision control: distinct q factors provide distinct physical slots.
    p_safe = 409
    safe_sources = {
        4: p_safe + 4 * 8 * 4,
        8: p_safe + 4 * 8 * 8,
    }
    safe_target = p_safe + 4 * 2 * 4
    safe_profile = owner_weighted_spectrum(safe_sources, safe_target, 16)
    assert safe_profile["owner_counts"] == {3: {1: (4,)}, 7: {1: (8,)}}
    safe_tokens = ((3, 1, 4), (7, 1, 8))
    safe = flow_gate(
        (0, 1),
        {0: (safe_tokens[0],), 1: (safe_tokens[1],)},
        {safe_tokens[0]: "q3", safe_tokens[1]: "q7"},
        {"q3": 1, "q7": 1},
    )
    assert safe == {
        "status": "OWNER_FLOW_PASS",
        "token_mass": 2,
        "physical_capacity": 2,
        "flow": 2,
        "request_count": 2,
    }

    # The collision becomes legal only after an explicit repeat budget is declared.
    repeated = flow_gate(
        (0, 1),
        collision_neighborhoods,
        collision_projection,
        {"q5": 2},
    )
    assert repeated == {
        "status": "OWNER_FLOW_PASS",
        "token_mass": 2,
        "physical_capacity": 2,
        "flow": 2,
        "request_count": 2,
    }

    # The same physical collision can be pure collision or carry a linear annihilator.
    collision_only_linear = linear_deficit_status((1, 2), (1, 2))
    assert collision_only_linear == {
        "status": "OWNER_COLLISION_ONLY",
        "demand_rank": 2,
        "token_rank": 2,
        "outside_demand": (),
    }
    annihilator_linear = linear_deficit_status((1, 2), (1, 1))
    assert annihilator_linear == {
        "status": "OWNER_PROJECTION_RANK_ANNIHILATOR",
        "demand_rank": 2,
        "token_rank": 1,
        "outside_demand": (2,),
    }

    return {
        "real_collision": collision,
        "real_safe": safe,
        "declared_repeat_budget": repeated,
        "collision_only_linear": collision_only_linear,
        "annihilator_linear": annihilator_linear,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner-token projection physical-capacity flow gate")
    for branch in (
        "real_collision",
        "real_safe",
        "declared_repeat_budget",
        "collision_only_linear",
        "annihilator_linear",
    ):
        print(branch, result[branch]["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
