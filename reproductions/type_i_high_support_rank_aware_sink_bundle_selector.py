#!/usr/bin/env python3
"""Verify the rank-aware sink-bundle selector and its p=73 certificate."""

from __future__ import annotations

import argparse
import json
from collections import Counter, deque
from math import gcd, lcm, prod

import type_i_bottom_sink_scc_complete_excess_bundle as bottom


def rank(prime: int, K: int, support: int) -> tuple[int, int]:
    bound = (prime - 1) ** 2 // 4
    if K % support:
        raise AssertionError("charged support did not divide K")
    return bound // support, K // support


def centered_F_receipt(
    R: int,
    K: int,
    expected_factors: dict[int, int],
    witness: tuple[int, ...],
    expected_bounded_count: int,
) -> dict[str, object]:
    factors = bottom.factorization(K)
    if factors != expected_factors:
        raise AssertionError("centered-box factorization changed")
    primes = tuple(factors)
    if len(primes) != len(witness):
        raise AssertionError("F witness dimension changed")

    residues = {1}
    for q in primes:
        values = {
            pow(q, exponent, R)
            for exponent in range(-factors[q], factors[q] + 1)
        }
        residues = {left * right % R for left in residues for right in values}
    if len(residues) != expected_bounded_count or R - 1 in residues:
        raise AssertionError("bounded Type I box changed")

    residue = 1
    for q, exponent in zip(primes, witness, strict=True):
        if gcd(q, R) != 1:
            raise AssertionError("F witness used a nonunit")
        residue = residue * pow(q, exponent, R) % R
    if residue != R - 1 or not any(
        abs(exponent) > factors[q]
        for q, exponent in zip(primes, witness, strict=True)
    ):
        raise AssertionError("unbounded F witness changed")

    numerator = prod(
        q ** max(exponent, 0)
        for q, exponent in zip(primes, witness, strict=True)
    )
    denominator = prod(
        q ** max(-exponent, 0)
        for q, exponent in zip(primes, witness, strict=True)
    )
    quotient, remainder = divmod(numerator + denominator, R)
    if remainder:
        raise AssertionError("F witness did not lift to an integer source")
    return {
        "classification": "F",
        "factorization": factors,
        "bounded_residue_count": len(residues),
        "witness": list(witness),
        "numerator": numerator,
        "denominator": denominator,
        "source_layer": quotient,
    }


def source_path_to_anchor(
    R: int, K_factors: dict[int, int]
) -> tuple[tuple[int, int, int], list[dict[str, object]]]:
    fixtures = (
        ((4, 198375, 53), 2, 1, (2, 101059, 27)),
        ((2, 101059, 27), 7, 1, (535, 14437, 4)),
        ((535, 14437, 4), 14437, 14433, (1, 3742, 1)),
    )
    current = fixtures[0][0]
    rows = []
    for source, q, expected_shift, expected_destination in fixtures:
        if current != source:
            raise AssertionError("source path lost continuity")
        destination, shift, common = bottom.formal_transition(
            current, q, R, K_factors
        )
        if (
            destination != expected_destination
            or shift != expected_shift
            or common != 1
        ):
            raise AssertionError("source path changed")
        rows.append(
            {
                "source": list(source),
                "q": q,
                "shift": shift,
                "destination": list(destination),
            }
        )
        current = destination
    return current, rows


def sink_distances(
    adjacency: dict[bottom.Node, set[bottom.Node]],
    labels: dict[tuple[bottom.Node, bottom.Node], set[int]],
    component: set[bottom.Node],
    anchor: bottom.Node,
) -> tuple[
    dict[bottom.Node, int],
    dict[bottom.Node, bottom.Node | None],
    dict[bottom.Node, int],
]:
    distances = {anchor: 0}
    parents: dict[bottom.Node, bottom.Node | None] = {anchor: None}
    parent_labels: dict[bottom.Node, int] = {}
    queue = deque([anchor])
    while queue:
        source = queue.popleft()
        for destination in sorted(adjacency[source]):
            if destination not in component or destination in distances:
                continue
            distances[destination] = distances[source] + 1
            parents[destination] = source
            parent_labels[destination] = min(labels[(source, destination)])
            queue.append(destination)
    if set(distances) != component:
        raise AssertionError("sink SCC was not reachable from its anchor")
    return distances, parents, parent_labels


def bundle_candidates(
    prime: int,
    R: int,
    K: int,
    support: int,
    component: set[bottom.Node],
    distances: dict[bottom.Node, int],
) -> list[dict[str, object]]:
    K_factors = bottom.factorization(K)
    candidates = []
    for node in sorted(component):
        orientations = (
            (node[1], node[0], "larger"),
            (node[0], node[1], "smaller"),
        )
        for selected, other, orientation in orientations:
            Q = 1
            beta = 1
            blocks = []
            for q, exponent in bottom.factorization(selected).items():
                capacity = K_factors.get(q, 0)
                if exponent > capacity:
                    Q *= q**exponent
                    blocks.append((q, exponent, capacity))
                else:
                    beta *= q**exponent
            residual = other * beta
            if (
                Q <= 1
                or selected != Q * beta
                or gcd(Q, residual) != 1
                or K % residual
                or K % Q == 0
            ):
                continue
            combined_support = lcm(support, Q)
            if combined_support <= support or combined_support % prime == 0:
                continue
            target_R, target_K = bottom.canonical_chart(prime, combined_support)
            target_cofactor, remainder = divmod(target_K, combined_support)
            if remainder or target_cofactor != pow(4 * combined_support, -1, prime):
                raise AssertionError("canonical cofactor changed")
            candidates.append(
                {
                    "node": node,
                    "orientation": orientation,
                    "selected": selected,
                    "other": other,
                    "Q": Q,
                    "beta": beta,
                    "residual": residual,
                    "blocks": tuple(blocks),
                    "distance": distances[node],
                    "support": combined_support,
                    "target_R": target_R,
                    "target_K": target_K,
                    "target_cofactor": target_cofactor,
                }
            )
    return candidates


def recover_path(
    target: bottom.Node,
    parents: dict[bottom.Node, bottom.Node | None],
    parent_labels: dict[bottom.Node, int],
) -> list[tuple[bottom.Node, int, bottom.Node]]:
    reverse_path = []
    current = target
    while parents[current] is not None:
        source = parents[current]
        assert source is not None
        reverse_path.append((source, parent_labels[current], current))
        current = source
    return list(reversed(reverse_path))


def verify_rank_aware_selector() -> dict[str, object]:
    prime, R, K, support = 73, 3743, 68310, 1518
    terminal_denominators = (20, 219, 4380)
    x, y, z = terminal_denominators
    if 4 * x * y * z != prime * (x * y + x * z + y * z):
        raise AssertionError("p=73 terminal-first Type II control changed")
    bound = (prime - 1) ** 2 // 4
    source_cofactor = K // support
    if not (
        support > bound
        and source_cofactor == 45
        and rank(prime, K, support) == (0, 45)
        and 4 * K == prime * R + 1
    ):
        raise AssertionError("high-support source changed")

    source_F = centered_F_receipt(
        R,
        K,
        {2: 1, 3: 3, 5: 1, 11: 1, 23: 1},
        (2, -1, -3, 0, -2),
        551,
    )
    K_factors = bottom.factorization(K)
    bottom_anchor, source_path = source_path_to_anchor(R, K_factors)
    anchor = bottom_anchor[:2]

    adjacency, labels = bottom.bottom_graph(R, K_factors)
    sinks = bottom.sink_components(adjacency)
    matching = [component for component in sinks if anchor in component]
    if len(sinks) != 1 or len(matching) != 1 or len(matching[0]) != 324:
        raise AssertionError("focused sink SCC changed")
    component = matching[0]
    distances, parents, parent_labels = sink_distances(
        adjacency, labels, component, anchor
    )
    candidates = bundle_candidates(
        prime, R, K, support, component, distances
    )
    improving = [
        candidate
        for candidate in candidates
        if int(candidate["target_cofactor"]) < source_cofactor
    ]
    cofactor_multiset = sorted(
        int(candidate["target_cofactor"]) for candidate in candidates
    )
    expected_multiset = [
        6,
        8,
        9,
        11,
        14,
        15,
        15,
        18,
        18,
        18,
        20,
        23,
        26,
        30,
        32,
        34,
        35,
        39,
        39,
        41,
        44,
        44,
        47,
        48,
        49,
        50,
        55,
        59,
        60,
        60,
        61,
        68,
        71,
    ]
    if (
        len(candidates) != 33
        or len(improving) != 22
        or cofactor_multiset != expected_multiset
    ):
        raise AssertionError("rank-aware candidate universe changed")

    failed_anchor = [
        candidate
        for candidate in candidates
        if candidate["node"] == (1, 3742) and candidate["Q"] == 1871
    ]
    if len(failed_anchor) != 1 or failed_anchor[0]["target_cofactor"] != 47:
        raise AssertionError("minimum-node persistence boundary changed")

    selected = min(
        improving,
        key=lambda candidate: (
            candidate["distance"],
            candidate["target_cofactor"],
            candidate["node"],
            candidate["Q"],
        ),
    )
    shortest_distance = min(int(candidate["distance"]) for candidate in improving)
    shortest_improving = [
        candidate
        for candidate in improving
        if int(candidate["distance"]) == shortest_distance
    ]
    global_minimum = min(
        candidates,
        key=lambda candidate: (
            candidate["target_cofactor"],
            candidate["distance"],
            candidate["node"],
            candidate["Q"],
        ),
    )
    if not (
        len(shortest_improving) == 1
        and shortest_improving[0] is selected
        and selected["node"] == (2, 3741)
        and selected["distance"] == 1
        and selected["Q"] == 1247
        and selected["beta"] == 3
        and selected["residual"] == 6
        and selected["support"] == 1892946
        and selected["target_R"] == 4563815
        and selected["target_K"] == 83289624
        and selected["target_cofactor"] == 44
        and global_minimum["node"] == (297, 3446)
        and global_minimum["target_cofactor"] == 6
        and global_minimum["distance"] == 13
    ):
        raise AssertionError("rank-aware selection changed")

    selector_path = recover_path(selected["node"], parents, parent_labels)
    if selector_path != [((1, 3742), 1871, (2, 3741))]:
        raise AssertionError("shortest improving path changed")
    current = bottom_anchor
    path_rows = []
    for source, q, expected_destination in selector_path:
        if current[:2] != source:
            raise AssertionError("selector path lost provenance")
        destination, shift, common = bottom.formal_transition(
            current, q, R, K_factors
        )
        if destination[:2] != expected_destination or common != 1:
            raise AssertionError("selector raw edge changed")
        path_rows.append(
            {
                "source": list(current),
                "q": q,
                "shift": shift,
                "destination": list(destination),
            }
        )
        current = destination

    target_rank = rank(
        prime, int(selected["target_K"]), int(selected["support"])
    )
    if target_rank != (0, 44) or not target_rank < (0, 45):
        raise AssertionError("real parent-to-target rank did not decrease")
    target_F = centered_F_receipt(
        int(selected["target_R"]),
        int(selected["target_K"]),
        {2: 3, 3: 1, 11: 2, 23: 1, 29: 1, 43: 1},
        (-1, 6, 4, -7, -1, -8),
        2739,
    )

    return {
        "source": {
            "state": [R, K, support],
            "rank": [0, 45],
            "terminal_first_Type_II": list(terminal_denominators),
            "classification": source_F,
            "path_to_sink_anchor": source_path,
        },
        "sink_capacity_map": {
            "node_count": len(component),
            "candidate_count": len(candidates),
            "improving_count": len(improving),
            "cofactor_histogram": dict(
                sorted(Counter(cofactor_multiset).items())
            ),
            "failed_minimum_node_cofactor": 47,
            "global_minimum": {
                "node": list(global_minimum["node"]),
                "distance": global_minimum["distance"],
                "cofactor": global_minimum["target_cofactor"],
            },
        },
        "selected_edge": {
            "policy": "shortest_improving_then_minimum_cofactor",
            "raw_path": path_rows,
            "node": list(selected["node"]),
            "Q": selected["Q"],
            "beta": selected["beta"],
            "residual": selected["residual"],
            "target": [
                selected["target_R"],
                selected["target_K"],
                selected["support"],
            ],
            "source_rank": [0, 45],
            "target_rank": list(target_rank),
            "target_classification": target_F,
            "solution_lift": "identity_on_Sol(4,p)",
        },
        "theorem_status": "verified",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = verify_rank_aware_selector()
    if args.verify:
        print("verified high-support rank-aware sink-bundle selector")
    else:
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
