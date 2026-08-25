#!/usr/bin/env python3
"""Verify proper-endpoint descent from source-reachable bottom relation nodes.

This verifier is deliberately local.  It checks the new conditional E1--E5
adapter and its two ordering boundaries; it does not run a historical prime
range scan.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
from itertools import product
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from reproductions.short_certificate import (  # noqa: E402
    certificate_at_gap,
    smallest_prime_factors,
    type_ii_residue_certificate,
    verify_certificate,
)
from reproductions.type_ii_odd_kernel_overflow_natural_tail_relation_graph import (  # noqa: E402
    bottom_graph,
    factorization,
    positive_divisors,
    reachable_nodes,
    relation_receipt,
    strongly_connected_components,
    transition,
)


def endpoint_bound(rank: int) -> int:
    k0 = (rank + 5) // 4
    denominator = 4 * k0 - rank - 1
    if denominator <= 0:
        raise AssertionError("endpoint denominator is not positive")
    return k0 * (k0 + 1) // denominator


def endpoint_state(prime: int, cofactor: int) -> dict[str, object]:
    if factorization(prime) != {prime: 1} or prime % 24 != 1:
        raise AssertionError("prime is not in the core class")
    U = (prime - 1) // 4
    if U % cofactor:
        raise AssertionError("endpoint cofactor does not divide U")
    rank = U // cofactor
    if cofactor > endpoint_bound(rank):
        raise AssertionError("endpoint is outside the allowed downset")
    gap = 4 * cofactor - 1
    x = U + cofactor
    if 4 * x != prime + gap or gcd(x, gap) != 1:
        raise AssertionError("endpoint normal form failed")
    return {
        "prime": prime,
        "U": U,
        "cofactor": cofactor,
        "rank": rank,
        "endpoint_bound": endpoint_bound(rank),
        "gap": gap,
        "x": x,
        "factors": factorization(x),
    }


def signed_box_profile(prime: int, cofactor: int) -> dict[str, object]:
    state = endpoint_state(prime, cofactor)
    gap = int(state["gap"])
    factors = dict(state["factors"])
    primes = tuple(factors)
    hits: list[tuple[int, ...]] = []
    subgroup = {1}

    for vector in product(
        *(range(-exponent, exponent + 1) for exponent in factors.values())
    ):
        residue = 1
        for carrier, exponent in zip(primes, vector, strict=True):
            residue = residue * pow(carrier, exponent, gap) % gap
        if residue == gap - 1:
            hits.append(vector)

    frontier = [1]
    while frontier:
        residue = frontier.pop()
        for carrier in primes:
            target = residue * carrier % gap
            if target not in subgroup:
                subgroup.add(target)
                frontier.append(target)

    if hits:
        classification = "hit"
    elif gap - 1 in subgroup:
        classification = "F"
    else:
        classification = "G"
    return {
        **state,
        "classification": classification,
        "signed_box_hits": hits,
        "source_subgroup_size": len(subgroup),
        "target_in_source_subgroup": gap - 1 in subgroup,
    }


def terminal_first_relation_reach(
    prime: int, cofactor: int, initial_pair: tuple[int, int]
) -> dict[str, object]:
    state = endpoint_state(prime, cofactor)
    gap = int(state["gap"])
    x = int(state["x"])
    capacity_factors = factorization(prime * x)
    spf = smallest_prime_factors(prime // 2 + 2)
    stack = [tuple(sorted(initial_pair))]
    seen: set[tuple[int, int]] = set()
    bottom_entries: set[tuple[int, int]] = set()

    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        first, second = node
        receipt = relation_receipt(prime, gap, first, second)
        kappa = int(receipt["kappa"])
        if receipt["integral"]:
            return {
                "status": "preempted",
                "terminal_kind": "natural_tail",
                "terminal_node": node,
                "reachable_relation_nodes": len(seen),
            }

        for quotient_gap in positive_divisors(kappa):
            if quotient_gap % 4 != 3 or not 3 <= quotient_gap <= prime - 2:
                continue
            certificate = certificate_at_gap(prime, quotient_gap, spf)
            if certificate is not None:
                if not verify_certificate(certificate):
                    raise AssertionError("quotient terminal failed verification")
                return {
                    "status": "preempted",
                    "terminal_kind": "fresh_quotient",
                    "terminal_gap": quotient_gap,
                    "terminal_certificate": asdict(certificate),
                    "terminal_node": node,
                    "reachable_relation_nodes": len(seen),
                }

        if kappa == 1:
            bottom_entries.add(node)
        carriers: list[int] = []
        for carrier, exponent in factorization(first * second).items():
            if exponent <= capacity_factors.get(carrier, 0):
                continue
            if carrier % 4 == 3 and carrier <= prime - 2:
                certificate = certificate_at_gap(prime, carrier, spf)
                if certificate is not None:
                    if not verify_certificate(certificate):
                        raise AssertionError("edge-label terminal failed verification")
                    return {
                        "status": "preempted",
                        "terminal_kind": "edge_label",
                        "terminal_gap": carrier,
                        "terminal_certificate": asdict(certificate),
                        "terminal_node": node,
                        "reachable_relation_nodes": len(seen),
                    }
            carriers.append(carrier)

        if not carriers:
            raise AssertionError("nonintegral relation has no over-capacity carrier")
        for carrier in carriers:
            target, next_kappa, _ = transition(
                prime, gap, first, second, carrier
            )
            stack.append(target)
            if next_kappa == 1:
                bottom_entries.add(target)

    graph = bottom_graph(prime, gap, x)
    bottom_reach: set[tuple[int, int]] = set()
    for entry in bottom_entries:
        bottom_reach.update(reachable_nodes(graph, entry))
    components = strongly_connected_components(graph, bottom_reach)
    sink_components = [
        component
        for component in components
        if not any(
            target not in component
            for node in component
            for _, target in graph[node]
        )
    ]
    if not sink_components:
        raise AssertionError("terminal-free finite reach has no sink SCC")
    sink_minima = [
        min(component, key=lambda node: (node[0], node[1]))
        for component in sink_components
    ]
    return {
        "status": "terminal_free",
        "reachable_relation_nodes": len(seen),
        "bottom_entries": sorted(bottom_entries),
        "bottom_nodes": sorted(bottom_reach),
        "bottom_reachable_nodes": len(bottom_reach),
        "sink_scc_sizes": sorted(len(component) for component in sink_components),
        "sink_minima": sorted(sink_minima),
    }


def proper_endpoint_dispatch(
    prime: int, cofactor: int, initial_pair: tuple[int, int]
) -> dict[str, object]:
    source = endpoint_state(prime, cofactor)
    reach = terminal_first_relation_reach(prime, cofactor, initial_pair)
    if reach["status"] != "terminal_free":
        return {"selector_status": "preempted", "relation_reach": reach}

    candidates = []
    used_cofactors: set[int] = set()
    for node in reach["bottom_nodes"]:
        smaller = int(node[0])
        if not (smaller < cofactor and cofactor % smaller == 0):
            continue
        if smaller in used_cofactors:
            continue
        used_cofactors.add(smaller)
        target = signed_box_profile(prime, smaller)
        if int(target["cofactor"]) > int(target["endpoint_bound"]):
            raise AssertionError("downset successor is not endpoint-allowed")
        spf = smallest_prime_factors(prime // 2 + 2)
        certificate = certificate_at_gap(prime, int(target["gap"]), spf)
        type_ii = type_ii_residue_certificate(prime, int(target["gap"]), spf)
        if target["classification"] == "hit" and type_ii is None:
            raise AssertionError("nonempty signed box did not reconstruct Type II")
        if type_ii is not None and not verify_certificate(type_ii):
            raise AssertionError("endpoint Type II terminal failed verification")
        candidates.append(
            {
                "source_bottom_node": node,
                "target": target,
                "short_certificate": None if certificate is None else asdict(certificate),
                "type_ii_certificate": None if type_ii is None else asdict(type_ii),
                "E1_premises": (
                    smaller < cofactor
                    and cofactor % smaller == 0
                    and int(source["U"]) % cofactor == 0
                ),
                "E2_construction": (
                    int(target["gap"]) == 4 * smaller - 1
                    and int(target["x"]) == int(source["U"]) + smaller
                ),
                "E3_normal_form": (
                    4 * int(target["x"]) == prime + int(target["gap"])
                    and int(source["U"]) % smaller == 0
                ),
                "E4_solution_lift": "identity_on_Sol(p)",
                "E5_rank": [cofactor, smaller],
                "E5_strict": smaller < cofactor,
            }
        )

    if not candidates:
        return {
            "selector_status": "KAPPA_ONE_RELATION_REACH_NO_PROPER_ENDPOINT",
            "relation_reach": reach,
        }

    terminal_candidates = [
        candidate
        for candidate in candidates
        if candidate["short_certificate"] is not None
        or candidate["type_ii_certificate"] is not None
    ]
    selected = min(
        terminal_candidates or candidates,
        key=lambda candidate: int(candidate["target"]["cofactor"]),
    )
    if not all(
        selected[key]
        for key in (
            "E1_premises",
            "E2_construction",
            "E3_normal_form",
            "E5_strict",
        )
    ):
        raise AssertionError("proper-endpoint E1--E5 receipt is incomplete")
    selected["selector_status"] = (
        "terminal_leaf" if terminal_candidates else "verified_edge"
    )
    selected["recursive_edge_eligible"] = not terminal_candidates
    selected["relation_reach"] = reach
    return selected


def verify() -> dict[str, object]:
    edge_1201 = proper_endpoint_dispatch(1_201, 3, (9, 101))
    if (
        edge_1201["selector_status"],
        edge_1201["recursive_edge_eligible"],
        edge_1201["target"]["cofactor"],
        edge_1201["target"]["classification"],
        edge_1201["E5_rank"],
    ) != ("verified_edge", True, 1, "G", [3, 1]):
        raise AssertionError("p=1201 proper-endpoint descent changed")

    edge_31249 = proper_endpoint_dispatch(31_249, 42, (14, 153))
    if (
        edge_31249["selector_status"],
        edge_31249["target"]["cofactor"],
        edge_31249["target"]["classification"],
        edge_31249["E5_rank"],
    ) != ("verified_edge", 1, "G", [42, 1]):
        raise AssertionError("p=31249 proper-endpoint descent changed")

    terminal_3433 = proper_endpoint_dispatch(3_433, 22, (32, 55))
    if (
        terminal_3433["selector_status"],
        terminal_3433["target"]["cofactor"],
        terminal_3433["target"]["classification"],
        terminal_3433["type_ii_certificate"]["gap"],
    ) != ("terminal_leaf", 2, "hit", 7):
        raise AssertionError("p=3433 endpoint terminal changed")

    terminal_9601 = proper_endpoint_dispatch(9_601, 40, (488, 625))
    if (
        terminal_9601["selector_status"],
        terminal_9601["target"]["cofactor"],
        terminal_9601["target"]["classification"],
        terminal_9601["type_ii_certificate"]["gap"],
    ) != ("terminal_leaf", 5, "hit", 19):
        raise AssertionError("p=9601 terminal-first endpoint choice changed")

    preempted = proper_endpoint_dispatch(20_857, 66, (81, 1_760))
    if (
        preempted["selector_status"],
        preempted["relation_reach"]["terminal_kind"],
        preempted["relation_reach"]["terminal_gap"],
    ) != ("preempted", "edge_label", 3):
        raise AssertionError("edge-label ordering boundary changed")

    source_reach = terminal_first_relation_reach(6_529, 48, (16, 175))
    if source_reach["status"] != "terminal_free" or source_reach["sink_minima"] != [(1, 190)]:
        raise AssertionError("source-reachable sink boundary changed")
    full_graph = bottom_graph(6_529, 191, 1_680)
    full_components = strongly_connected_components(full_graph, set(full_graph))
    full_sink_minima = sorted(
        min(component, key=lambda node: (node[0], node[1]))
        for component in full_components
        if not any(
            target not in component
            for node in component
            for _, target in full_graph[node]
        )
    )
    if full_sink_minima != [(1, 190), (5, 186)]:
        raise AssertionError("full bottom-graph boundary changed")

    return {
        "status": "verified",
        "verified_edges": [edge_1201, edge_31249],
        "endpoint_terminals": [terminal_3433, terminal_9601],
        "ordering_boundary": preempted,
        "source_reach_boundary": {
            "prime": 6_529,
            "cofactor": 48,
            "source_reachable_sink_minima": source_reach["sink_minima"],
            "full_bottom_graph_sink_minima": full_sink_minima,
            "unreachable_nondivisor_sink": (5, 186),
        },
        "scope": "proper-endpoint relation-reach adapter only; no historical range scan",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = verify()
    if args.verify:
        print(result)


if __name__ == "__main__":
    main()
