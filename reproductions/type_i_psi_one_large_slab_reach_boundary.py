#!/usr/bin/env python3
"""Audit source-anchored formal-Reach slabs and natural-tail lift obstruction."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from typing import Literal


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-psi-one-full-spectrum-terminal-descent-audit-results.json"
)
CLOSURE_SCRIPT = (
    ROOT / "reproductions" / "type_i_f_psi_one_formal_transition_closure.py"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-psi-one-large-slab-reach-boundary-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "eb0ef6c4fe5103d907916ebb4d2fc0bc97913344d3cb143e1f17cb582fa0adc2"
)
EXPECTED_CLOSURE_SHA256 = (
    "cd76a4f2c0e602324f87d91ab4be86754feb2c256ab9553a6a05615f91286846"
)

EXPECTED_SUMMARY = {
    "source_state_count": 483,
    "positive_witness_count": 1_615,
    "complete_reach_node_count": 520_559,
    "complete_reach_edge_count": 1_874_407,
    "complete_reach_large_slab_count": 1_412,
    "complete_reach_large_slab_state_count": 282,
    "ranked_scope_large_slab_count": 638,
    "ranked_scope_large_slab_state_count": 256,
    "complete_reach_only_large_slab_count": 774,
    "complete_reach_only_large_slab_state_count": 26,
    "direct_collision_count": 2,
    "cross_chart_collision_count": 2,
    "collision_union_count": 4,
    "node_affine_hit_count": 86,
    "anchor_affine_hit_count": 397,
    "node_anchor_affine_overlap_count": 21,
    "pre_absorption_menu_miss_count": 948,
    "canonical_absorption_count": 581,
    "basic_local_good_count": 581,
    "basic_local_miss_count": 831,
    "local_miss_reaches_good_single_count": 761,
    "formal_descendant_residual_count": 70,
    "formal_descendant_residual_state_count": 45,
    "strong_miss_count": 566,
    "strong_miss_state_count": 198,
    "ranked_scope_strong_miss_count": 247,
    "ranked_scope_strong_miss_state_count": 150,
    "natural_endpoint_legal_gap_count": 14,
    "natural_endpoint_hit_count": 0,
    "ranked_scope_natural_endpoint_legal_gap_count": 11,
    "ranked_scope_natural_endpoint_hit_count": 0,
    "q_equals_2_count": 36,
    "exponent_one_count": 1_349,
    "higher_exponent_count": 63,
    "maximum_external_exponent": 13,
}

Node = tuple[int, int, int]
RankMode = Literal["min", "max"]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


closure = load_module("large_slab_reach_closure", CLOSURE_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def state_key(record: dict[str, object]) -> tuple[int, int]:
    return int(record["prime"]), int(record["R"])


def starts_and_bounds(
    record: dict[str, object],
) -> tuple[set[Node], dict[int, int]]:
    starts = {
        tuple(int(value) for value in witness["start"])
        for witness in record["positive_witnesses"]
    }
    bounds = {int(q): int(exponent) for q, exponent in record["factorization"]}
    return starts, bounds


def require_frozen_witness(
    record: dict[str, object],
    start: Node,
    exponents: list[int],
    *,
    unique_positive_witness: bool = False,
) -> None:
    matches = [
        witness
        for witness in record["positive_witnesses"]
        if tuple(int(value) for value in witness["start"]) == start
    ]
    if (
        len(matches) != 1
        or [int(value) for value in matches[0]["exponents"]] != exponents
    ):
        raise AssertionError(f"frozen source witness changed for start {start}")
    if unique_positive_witness and (
        int(record["positive_witness_count"]) != 1
        or len(record["positive_witnesses"]) != 1
    ):
        raise AssertionError("expected a unique positive source witness")


def complete_reach(
    starts: set[Node], R: int, bounds: dict[int, int]
) -> tuple[set[Node], int, dict[Node, set[Node]]]:
    maximum_start_layer = max(node[2] for node in starts)
    coarse_bound = R * maximum_start_layer * (maximum_start_layer + 1) // 4
    visited: set[Node] = set()
    reverse: dict[Node, set[Node]] = {}
    frontier = list(sorted(starts, reverse=True))
    edge_count = 0
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        edges = closure.raw_transitions(node, R, bounds)
        edge_count += len(edges)
        for edge in edges:
            destination = tuple(int(value) for value in edge["destination"])
            reverse.setdefault(destination, set()).add(node)
            if destination not in visited:
                frontier.append(destination)
        if len(visited) > coarse_bound:
            raise AssertionError("complete Reach exceeded its arithmetic bound")
    return visited, edge_count, reverse


def ranked_scope(
    starts: set[Node], R: int, bounds: dict[int, int], mode: RankMode
) -> tuple[set[Node], set[Node], set[Node]]:
    visited: set[Node] = set()
    rejected_successors: set[Node] = set()
    accepted_destinations: set[Node] = set()
    frontier = list(sorted(starts, reverse=True))
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        for edge in closure.raw_transitions(node, R, bounds):
            destination = tuple(int(value) for value in edge["destination"])
            if closure.rank(destination, mode) < closure.rank(node, mode):
                accepted_destinations.add(destination)
                if destination not in visited:
                    frontier.append(destination)
            else:
                rejected_successors.add(destination)
    return visited, rejected_successors - visited, accepted_destinations


def extract_single_slabs(
    nodes: set[Node], prime: int, R: int, K: int, bounds: dict[int, int]
) -> list[dict[str, object]]:
    records: dict[tuple[int, ...], dict[str, object]] = {}
    for A, B, layer in sorted(nodes):
        if layer != 1:
            continue
        for selected, other, side in ((A, B, "A"), (B, A, "B")):
            for q, exponent in closure.factorization(selected).items():
                if q in bounds:
                    continue
                Q = q**exponent
                alpha = selected // Q
                beta = other
                if K % (alpha * beta):
                    continue
                if q == prime:
                    raise AssertionError("m=1 linear Reach acquired q=p")
                slab_key = (A, B, layer, q, exponent, Q, alpha, beta)
                records[slab_key] = {
                    "prime": prime,
                    "R": R,
                    "K": K,
                    "node": [A, B, layer],
                    "selected_side": side,
                    "q": q,
                    "exponent": exponent,
                    "Q": Q,
                    "alpha": alpha,
                    "beta": beta,
                }
    return list(records.values())


def extract_large_slabs(
    nodes: set[Node], prime: int, R: int, K: int, bounds: dict[int, int]
) -> list[dict[str, object]]:
    records = [
        record
        for record in extract_single_slabs(nodes, prime, R, K, bounds)
        if 4 * int(record["Q"]) > R
    ]
    if any(int(record["alpha"]) not in (1, 2, 3) for record in records):
        raise AssertionError("large-slab compression invariant failed")
    return records


def basic_single_slab_good(record: dict[str, object]) -> bool:
    prime = int(record["prime"])
    R = int(record["R"])
    A, B, _layer = (int(value) for value in record["node"])
    Q = int(record["Q"])
    L = A * B
    collision = any(
        (prime + T) % (4 * L) == 0 or (prime * T + 1) % (4 * L) == 0
        for T in closure.divisors(R)
    )
    R_Q = (-pow(prime, -1, 4 * Q)) % (4 * Q)
    return collision or R_Q < R


def reverse_reachable(targets: set[Node], reverse: dict[Node, set[Node]]) -> set[Node]:
    reached = set(targets)
    frontier = list(targets)
    while frontier:
        node = frontier.pop()
        for predecessor in reverse.get(node, set()):
            if predecessor not in reached:
                reached.add(predecessor)
                frontier.append(predecessor)
    return reached


_AFFINE_CACHE: dict[tuple[int, int, int, Node], tuple[int, ...]] = {}


def affine_hit_gaps(node: Node, prime: int, R: int, K: int) -> tuple[int, ...]:
    cache_key = (prime, R, K, node)
    if cache_key not in _AFFINE_CACHE:
        gaps, _origins = closure.external_gap_candidates({node}, prime, K)
        _AFFINE_CACHE[cache_key] = tuple(
            gap for gap in gaps if closure.exact_gap_certificate(prime, gap) is not None
        )
    return _AFFINE_CACHE[cache_key]


def classify_slab(record: dict[str, object]) -> dict[str, object]:
    prime = int(record["prime"])
    R = int(record["R"])
    K = int(record["K"])
    A, B, layer = (int(value) for value in record["node"])
    q = int(record["q"])
    Q = int(record["Q"])
    alpha = int(record["alpha"])
    beta = int(record["beta"])
    L = A * B

    direct_T = [T for T in closure.divisors(R) if (prime + T) % (4 * L) == 0]
    cross_T = [T for T in closure.divisors(R) if (prime * T + 1) % (4 * L) == 0]
    node_hits = affine_hit_gaps((A, B, layer), prime, R, K)
    anchor = tuple(sorted((alpha, R - alpha))) + (1,)
    anchor_hits = affine_hit_gaps(anchor, prime, R, K)
    R_Q = (-pow(prime, -1, 4 * Q)) % (4 * Q)
    if not 1 <= R_Q < 4 * Q or R_Q == R:
        raise AssertionError("canonical Q-chart invariant failed")

    if math.gcd(Q, alpha * beta) != 1 or K % (alpha * beta):
        raise AssertionError("slab support separation failed")
    if (prime * Q * alpha + 1) % beta:
        raise AssertionError("beta source congruence failed")
    if (prime * beta + 1) % alpha:
        raise AssertionError("alpha source congruence failed")

    if q == 2:
        if K % 2 == 0 or R % 8 != 3 or alpha % 2 == 0 or beta % 2 == 0:
            raise AssertionError("dyadic slab parity invariant failed")
    else:
        if K % 2 or R % 8 != 7 or (alpha - beta) % 2 == 0:
            raise AssertionError("odd slab parity invariant failed")
    if alpha == 2 and (q == 2 or beta % 4 != 1):
        raise AssertionError("alpha=2 congruence invariant failed")
    if alpha == 3:
        if R % 3 != 2 or beta % 3 != 2:
            raise AssertionError("alpha=3 ternary invariant failed")
        if q == 2:
            if R % 24 != 11 or beta % 6 != 5:
                raise AssertionError("dyadic alpha=3 congruence failed")
        elif R % 24 != 23 or beta % 6 != 2:
            raise AssertionError("odd alpha=3 congruence failed")

    rho = (K * pow(prime, -1, Q)) % Q
    if not 1 <= rho < Q:
        raise AssertionError("canonical rho representative failed")
    expected_R_Q = R - 4 * rho if 4 * rho < R else R + 4 * (Q - rho)
    if R_Q != expected_R_Q or (R_Q < R) != (4 * rho < R):
        raise AssertionError("canonical capacity formula failed")

    c = K // (alpha * beta)
    if beta * (4 * alpha * c - prime) != alpha * prime * Q + 1:
        raise AssertionError("large-slab cofactor identity failed")
    good_tail = Fraction(K, beta)
    bad_tail = Fraction(K, Q * alpha)
    if good_tail.denominator != 1 or bad_tail.denominator == 1:
        raise AssertionError("natural slab-tail integrality split failed")
    if math.gcd(Q, beta * c) != 1:
        raise AssertionError("bad residual was not reduced")
    if Fraction(4, prime) != Fraction(1, prime * K) + Fraction(
        1, good_tail.numerator
    ) + Fraction(Q, beta * c):
        raise AssertionError("natural slab-tail identity failed")

    endpoint_gap = 4 * (K // beta) - prime
    endpoint_is_legal = 3 <= endpoint_gap <= prime - 2 and endpoint_gap % 4 == 3
    endpoint_hit = bool(
        endpoint_is_legal
        and closure.exact_gap_certificate(prime, endpoint_gap) is not None
    )

    pre_absorption_miss = not (direct_T or cross_T or node_hits or anchor_hits)
    canonical_absorption = R_Q < R
    strong_miss = pre_absorption_miss and not canonical_absorption
    return {
        **record,
        "direct_collision_T": direct_T,
        "cross_chart_collision_T": cross_T,
        "node_affine_hit_gaps": list(node_hits),
        "anchor": list(anchor),
        "anchor_affine_hit_gaps": list(anchor_hits),
        "R_Q": R_Q,
        "rho": rho,
        "canonical_absorption": canonical_absorption,
        "pre_absorption_menu_miss": pre_absorption_miss,
        "strong_miss": strong_miss,
        "natural_good_tail": good_tail.numerator,
        "natural_bad_tail": {
            "numerator": bad_tail.numerator,
            "denominator": bad_tail.denominator,
        },
        "natural_bad_residual": {"numerator": Q, "denominator": beta * c},
        "natural_endpoint_gap": endpoint_gap,
        "natural_endpoint_is_legal": endpoint_is_legal,
        "natural_endpoint_hit": endpoint_hit,
    }


def public_record(record: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in record.items() if not key.startswith("_")}


def transition_by_label(node: Node, R: int, bounds: dict[int, int], q: int) -> Node:
    destinations = [
        tuple(int(value) for value in edge["destination"])
        for edge in closure.raw_transitions(node, R, bounds)
        if int(edge["q"]) == q
    ]
    if len(destinations) != 1:
        raise AssertionError(f"expected one q={q} transition from {node}")
    return destinations[0]


def verify_alpha_three_source_path(
    record: dict[str, object], profile: dict[str, object]
) -> dict[str, object]:
    prime, R = state_key(record)
    K = int(record["K"])
    starts, bounds = starts_and_bounds(record)
    source_a = 2
    source_s = 494_137
    if prime != source_a + source_s + source_a * source_s * R:
        raise AssertionError("linear source identity failed")

    start = (1_585_081, 2_273_094, 17_945)
    if start not in starts:
        raise AssertionError("alpha=3 source start left the frozen witness set")
    require_frozen_witness(record, start, [-1, -2, -1, -1, 2])
    labels = (1_259, 983, 71, 53, 211, 107, 71)
    expected_nodes = [
        start,
        (1_259, 1_966, 15),
        (2, 213, 1),
        (3, 212, 1),
        (4, 211, 1),
        (1, 214, 1),
        (2, 213, 1),
        (3, 212, 1),
    ]
    nodes = [start]
    node = start
    for q in labels:
        node = transition_by_label(node, R, bounds, q)
        nodes.append(node)
    if nodes != expected_nodes:
        raise AssertionError(f"alpha=3 source path changed: {nodes}")

    target = (2, 213, 1)
    if tuple(int(value) for value in profile["node"]) != target:
        raise AssertionError("alpha=3 profile target changed")
    if not bool(profile["strong_miss"]):
        raise AssertionError("alpha=3 path target ceased to be a strong miss")
    certificate = closure.exact_gap_certificate(prime, 431)
    if certificate is None or certificate["type"] != "Type_I":
        raise AssertionError("independent internal terminal changed")

    cycle_slabs = []
    for slab in extract_single_slabs(set(nodes[2:7]), prime, R, K, bounds):
        Q = int(slab["Q"])
        cycle_slabs.append(
            {
                "node": slab["node"],
                "Q": Q,
                "alpha": int(slab["alpha"]),
                "beta": int(slab["beta"]),
                "R_Q": (-pow(prime, -1, 4 * Q)) % (4 * Q),
                "basic_good": basic_single_slab_good(slab),
            }
        )
    cycle_slabs.sort(key=lambda row: tuple(int(value) for value in row["node"]))
    expected_cycle_slabs = [
        {
            "node": [1, 214, 1],
            "Q": 107,
            "alpha": 2,
            "beta": 1,
            "R_Q": 55,
            "basic_good": True,
        },
        {
            "node": [2, 213, 1],
            "Q": 71,
            "alpha": 3,
            "beta": 2,
            "R_Q": 235,
            "basic_good": False,
        },
        {
            "node": [3, 212, 1],
            "Q": 53,
            "alpha": 4,
            "beta": 3,
            "R_Q": 171,
            "basic_good": True,
        },
        {
            "node": [4, 211, 1],
            "Q": 211,
            "alpha": 1,
            "beta": 4,
            "R_Q": 299,
            "basic_good": False,
        },
    ]
    if cycle_slabs != expected_cycle_slabs:
        raise AssertionError(f"alpha=3 cycle slab profile changed: {cycle_slabs}")

    cycle_labels = labels[2:6]
    cycle_nodes = nodes[2:7]
    for source, q, destination in zip(cycle_nodes, cycle_labels, cycle_nodes[1:]):
        edges = closure.raw_transitions(source, R, bounds)
        if (
            len(edges) != 1
            or int(edges[0]["q"]) != q
            or tuple(int(value) for value in edges[0]["destination"]) != destination
        ):
            raise AssertionError("bottom-layer formal cycle ceased to be deterministic")

    return {
        "prime": prime,
        "R": R,
        "K": K,
        "linear_source": {"a": source_a, "s": source_s},
        "source_witness_exponents": [-1, -2, -1, -1, 2],
        "labels": list(labels),
        "nodes": [list(item) for item in nodes],
        "large_slab": public_record(profile),
        "bottom_layer_formal_cycle": {
            "labels": list(cycle_labels),
            "nodes": [list(item) for item in cycle_nodes],
            "single_slabs": cycle_slabs,
        },
        "independent_original_state_terminal": {
            "gap": 431,
            "type": certificate["type"],
            "divisor": certificate["divisor"],
            "solution": certificate["solution"],
        },
        "edge_semantics": "analysis_evidence_not_verified_edge",
        "boundary": (
            "The source-witness-anchored formal path and its bottom-layer cycle "
            "refute automatic closure of the present slab/anchor menu; the "
            "independent gap 431 terminal means this is not an Erdos-Straus "
            "counterexample."
        ),
    }


def verify_residual_pressure_point(
    source_record: dict[str, object], profile: dict[str, object]
) -> dict[str, object]:
    prime, R = state_key(source_record)
    starts, bounds = starts_and_bounds(source_record)
    nodes, _edge_count, _reverse = complete_reach(starts, R, bounds)
    origin = (326, 1_787_569, 201)
    if origin not in nodes or abs(origin[0] - R) != 8_569 or 8_569 % 19:
        raise AssertionError("residual affine origin changed")
    require_frozen_witness(source_record, origin, [-1, 2, 0, -1, 2, 0])
    certificate = closure.exact_gap_certificate(prime, 19)
    if certificate is None or certificate["type"] != "Type_I":
        raise AssertionError("residual affine certificate changed")
    return {
        "large_slab": public_record(profile),
        "higher_layer_escape": {
            "origin_node": list(origin),
            "quantity": "abs_A_minus_R",
            "quantity_value": 8_569,
            "gap": 19,
            "type": certificate["type"],
            "divisor": certificate["divisor"],
            "solution": certificate["solution"],
        },
        "boundary": (
            "The m=1 slab and its anchor miss every audited local channel, while "
            "a higher-layer affine quantity supplies the direct terminal."
        ),
    }


def verify_formal_descendant_residual(
    source_record: dict[str, object], profile: dict[str, object]
) -> dict[str, object]:
    prime, R = state_key(source_record)
    K = int(source_record["K"])
    starts, bounds = starts_and_bounds(source_record)
    source_a, source_s = 331, 483
    if prime != source_a + source_s + source_a * source_s * R:
        raise AssertionError("minimum residual linear source identity failed")
    start = (107, 18_723, 538)
    if start not in starts:
        raise AssertionError("minimum residual start left the frozen witness set")
    require_frozen_witness(
        source_record,
        start,
        [1, 2, -1, 0],
        unique_positive_witness=True,
    )
    labels = (79, 2, 17, 11)
    expected_nodes = [
        start,
        (8, 237, 7),
        (1, 34, 1),
        (2, 33, 1),
        (3, 32, 1),
    ]
    path = []
    node = start
    nodes_on_path = [node]
    for q in labels:
        edges = [
            edge
            for edge in closure.raw_transitions(node, R, bounds)
            if int(edge["q"]) == q
        ]
        if len(edges) != 1:
            raise AssertionError(f"minimum residual lost q={q} path edge")
        edge = edges[0]
        destination = tuple(int(value) for value in edge["destination"])
        path.append(
            {
                "q": q,
                "shift": (-node[2]) % q,
                "gcd_reduction": int(edge["gcd_reduction"]),
                "source": list(node),
                "destination": list(destination),
            }
        )
        node = destination
        nodes_on_path.append(node)
    if nodes_on_path != expected_nodes:
        raise AssertionError(f"minimum residual path changed: {nodes_on_path}")
    if tuple(int(value) for value in profile["node"]) != expected_nodes[-1]:
        raise AssertionError("minimum residual slab profile changed")
    if bool(profile["reaches_good_single"]):
        raise AssertionError("minimum residual ceased to be descendant-free")

    descendant_nodes, edge_count, _reverse = complete_reach(
        {expected_nodes[-1]}, R, bounds
    )
    single_slabs = extract_single_slabs(descendant_nodes, prime, R, K, bounds)
    if len(descendant_nodes) != 12 or edge_count != 26 or len(single_slabs) != 1:
        raise AssertionError("minimum formal-descendant residual graph changed")
    if any(basic_single_slab_good(slab) for slab in single_slabs):
        raise AssertionError("formal-descendant residual acquired a good single slab")

    full_pure_label_product = math.prod(labels)
    full_normalized_word_product = math.prod(
        int(edge["q"]) * int(edge["gcd_reduction"]) for edge in path
    )
    if full_pure_label_product != 29_546 or full_normalized_word_product != 118_184:
        raise AssertionError("minimum residual path-word products changed")

    suffix_pure_label_product = math.prod(labels[1:])
    theta = math.prod(int(edge["q"]) * int(edge["gcd_reduction"]) for edge in path[1:])
    U_1, epsilon, u = 237, 1, 1_361
    X, Y = 32, 3
    if suffix_pure_label_product != 374 or theta != 1_496:
        raise AssertionError("source-word suffix products changed")
    if theta * X != epsilon * U_1 + R * u or theta * Y != (
        -epsilon * U_1 + R * (theta - u)
    ):
        raise AssertionError("source-word congruence identities failed")
    if (suffix_pure_label_product * X - epsilon * U_1) % R == 0:
        raise AssertionError(
            "label-only suffix unexpectedly retained the path congruence"
        )
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "linear_source": {"a": source_a, "s": source_s},
        "source_witness_exponents": [1, 2, -1, 0],
        "descendant_node_count": len(descendant_nodes),
        "descendant_edge_count": edge_count,
        "single_external_slab_count": len(single_slabs),
        "path": path,
        "large_slab": public_record(profile),
        "full_path_word": {
            "pure_label_product": full_pure_label_product,
            "normalized_product": full_normalized_word_product,
        },
        "post_first_edge_source_word": {
            "U_1": U_1,
            "X": X,
            "Y": Y,
            "epsilon": epsilon,
            "u": u,
            "pure_label_product": suffix_pure_label_product,
            "Theta": theta,
            "identities": [
                "Theta*X = epsilon*U_1 + R*u",
                "Theta*Y = -epsilon*U_1 + R*(Theta-u)",
            ],
        },
        "boundary": (
            "The complete formal descendant graph contains no good single slab. "
            "The q=2 step has gcd reduction 4, so a label-only path word is invalid."
        ),
        "edge_semantics": "analysis_evidence_not_verified_edge",
    }


def verify_alpha_three_descendant_residual(
    source_record: dict[str, object], profile: dict[str, object]
) -> dict[str, object]:
    prime, R = state_key(source_record)
    K = int(source_record["K"])
    starts, bounds = starts_and_bounds(source_record)
    source_a, source_s = 4, 13_585
    if prime != source_a + source_s + source_a * source_s * R:
        raise AssertionError("alpha=3 residual linear source identity failed")

    start = (107, 348, 1)
    if start not in starts:
        raise AssertionError("alpha=3 residual start left the frozen witness set")
    require_frozen_witness(source_record, start, [2, 1, 1, 0, -1, 0])
    labels = (2, 281, 227)
    expected_nodes = [start, (174, 281, 1), (1, 454, 1), (2, 453, 1)]
    nodes_on_path = [start]
    node = start
    for q in labels:
        node = transition_by_label(node, R, bounds, q)
        nodes_on_path.append(node)
    if nodes_on_path != expected_nodes:
        raise AssertionError(f"alpha=3 residual path changed: {nodes_on_path}")
    if tuple(int(value) for value in profile["node"]) != expected_nodes[-1]:
        raise AssertionError("alpha=3 residual slab profile changed")

    descendant_nodes, edge_count, _reverse = complete_reach(
        {expected_nodes[-1]}, R, bounds
    )
    slabs = extract_single_slabs(descendant_nodes, prime, R, K, bounds)
    slab_rows = []
    for slab in slabs:
        Q = int(slab["Q"])
        slab_rows.append(
            {
                "node": slab["node"],
                "Q": Q,
                "alpha": int(slab["alpha"]),
                "beta": int(slab["beta"]),
                "R_Q": (-pow(prime, -1, 4 * Q)) % (4 * Q),
                "basic_good": basic_single_slab_good(slab),
            }
        )
    slab_rows.sort(key=lambda row: tuple(int(value) for value in row["node"]))
    expected_slabs = [
        {
            "node": [1, 454, 1],
            "Q": 227,
            "alpha": 2,
            "beta": 1,
            "R_Q": 531,
            "basic_good": False,
        },
        {
            "node": [2, 453, 1],
            "Q": 151,
            "alpha": 3,
            "beta": 2,
            "R_Q": 523,
            "basic_good": False,
        },
        {
            "node": [6, 449, 1],
            "Q": 449,
            "alpha": 1,
            "beta": 6,
            "R_Q": 1_563,
            "basic_good": False,
        },
    ]
    if len(descendant_nodes) != 20 or edge_count != 43 or slab_rows != expected_slabs:
        raise AssertionError("alpha=3 formal-descendant residual graph changed")
    if bool(profile["reaches_good_single"]):
        raise AssertionError("alpha=3 residual acquired a good single slab")
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "linear_source": {"a": source_a, "s": source_s},
        "source_path_labels": list(labels),
        "source_path_nodes": [list(item) for item in nodes_on_path],
        "descendant_node_count": len(descendant_nodes),
        "descendant_edge_count": edge_count,
        "single_slabs": slab_rows,
        "large_slab": public_record(profile),
        "boundary": (
            "The sole alpha=3 formal-descendant residual reaches alpha=1 and "
            "alpha=2 large slabs, but every single slab in the descendant graph "
            "misses both collisions and canonical capacity descent."
        ),
        "edge_semantics": "analysis_evidence_not_verified_edge",
    }


def run() -> dict[str, object]:
    input_hash = sha256(INPUT)
    closure_hash = sha256(CLOSURE_SCRIPT)
    if input_hash != EXPECTED_INPUT_SHA256:
        raise AssertionError(f"frozen input hash changed: {input_hash}")
    if closure_hash != EXPECTED_CLOSURE_SHA256:
        raise AssertionError(f"formal closure script hash changed: {closure_hash}")

    source = json.loads(INPUT.read_text(encoding="utf-8"))
    records = source["records"]
    source_by_key = {state_key(record): record for record in records}
    profiles: list[dict[str, object]] = []
    complete_node_count = 0
    complete_edge_count = 0
    full_slab_states: set[tuple[int, int]] = set()
    ranked_slab_states: set[tuple[int, int]] = set()

    for source_record in records:
        prime, R = state_key(source_record)
        K = int(source_record["K"])
        starts, bounds = starts_and_bounds(source_record)
        full_nodes, edge_count, reverse = complete_reach(starts, R, bounds)
        min_visited, min_rejected, min_accepted = ranked_scope(starts, R, bounds, "min")
        max_visited, max_rejected, max_accepted = ranked_scope(starts, R, bounds, "max")
        ranked_nodes = min_visited | min_rejected | max_visited | max_rejected

        complete_node_count += len(full_nodes)
        complete_edge_count += edge_count
        full_slabs = extract_large_slabs(full_nodes, prime, R, K, bounds)
        single_slabs = extract_single_slabs(full_nodes, prime, R, K, bounds)
        good_single_nodes = {
            tuple(int(value) for value in slab["node"])
            for slab in single_slabs
            if basic_single_slab_good(slab)
        }
        can_reach_good_single = reverse_reachable(good_single_nodes, reverse)
        ranked_slab_keys = {
            tuple(int(value) for value in slab["node"])
            + (
                int(slab["q"]),
                int(slab["exponent"]),
                int(slab["Q"]),
                int(slab["alpha"]),
                int(slab["beta"]),
            )
            for slab in extract_large_slabs(ranked_nodes, prime, R, K, bounds)
        }
        if full_slabs:
            full_slab_states.add((prime, R))
        if ranked_slab_keys:
            ranked_slab_states.add((prime, R))

        for slab in full_slabs:
            slab_key = tuple(int(value) for value in slab["node"]) + (
                int(slab["q"]),
                int(slab["exponent"]),
                int(slab["Q"]),
                int(slab["alpha"]),
                int(slab["beta"]),
            )
            node = tuple(int(value) for value in slab["node"])
            slab["in_ranked_scope"] = slab_key in ranked_slab_keys
            slab["in_min_visited"] = node in min_visited
            slab["in_max_visited"] = node in max_visited
            slab["in_min_accepted_destination"] = node in min_accepted
            slab["in_max_accepted_destination"] = node in max_accepted
            slab["basic_local_good"] = node in good_single_nodes
            slab["reaches_good_single"] = node in can_reach_good_single
            slab["reaches_strict_descendant_good_single"] = (
                node not in good_single_nodes and node in can_reach_good_single
            )
            profiles.append(classify_slab(slab))

    strong = [profile for profile in profiles if bool(profile["strong_miss"])]
    ranked = [profile for profile in profiles if bool(profile["in_ranked_scope"])]
    ranked_strong = [profile for profile in strong if bool(profile["in_ranked_scope"])]
    basic_local_misses = [
        profile for profile in profiles if not bool(profile["basic_local_good"])
    ]
    descendant_releases = [
        profile
        for profile in basic_local_misses
        if bool(profile["reaches_strict_descendant_good_single"])
    ]
    formal_descendant_residuals = [
        profile
        for profile in basic_local_misses
        if not bool(profile["reaches_good_single"])
    ]
    collision_records = [
        profile
        for profile in profiles
        if profile["direct_collision_T"] or profile["cross_chart_collision_T"]
    ]

    summary = {
        "source_state_count": len(records),
        "positive_witness_count": sum(
            int(record["positive_witness_count"]) for record in records
        ),
        "complete_reach_node_count": complete_node_count,
        "complete_reach_edge_count": complete_edge_count,
        "complete_reach_large_slab_count": len(profiles),
        "complete_reach_large_slab_state_count": len(full_slab_states),
        "ranked_scope_large_slab_count": len(ranked),
        "ranked_scope_large_slab_state_count": len(ranked_slab_states),
        "complete_reach_only_large_slab_count": len(profiles) - len(ranked),
        "complete_reach_only_large_slab_state_count": len(
            full_slab_states - ranked_slab_states
        ),
        "direct_collision_count": sum(
            bool(profile["direct_collision_T"]) for profile in profiles
        ),
        "cross_chart_collision_count": sum(
            bool(profile["cross_chart_collision_T"]) for profile in profiles
        ),
        "collision_union_count": len(collision_records),
        "node_affine_hit_count": sum(
            bool(profile["node_affine_hit_gaps"]) for profile in profiles
        ),
        "anchor_affine_hit_count": sum(
            bool(profile["anchor_affine_hit_gaps"]) for profile in profiles
        ),
        "node_anchor_affine_overlap_count": sum(
            bool(profile["node_affine_hit_gaps"])
            and bool(profile["anchor_affine_hit_gaps"])
            for profile in profiles
        ),
        "pre_absorption_menu_miss_count": sum(
            bool(profile["pre_absorption_menu_miss"]) for profile in profiles
        ),
        "canonical_absorption_count": sum(
            bool(profile["canonical_absorption"]) for profile in profiles
        ),
        "basic_local_good_count": sum(
            bool(profile["basic_local_good"]) for profile in profiles
        ),
        "basic_local_miss_count": len(basic_local_misses),
        "local_miss_reaches_good_single_count": len(descendant_releases),
        "formal_descendant_residual_count": len(formal_descendant_residuals),
        "formal_descendant_residual_state_count": len(
            {
                (int(profile["prime"]), int(profile["R"]))
                for profile in formal_descendant_residuals
            }
        ),
        "strong_miss_count": len(strong),
        "strong_miss_state_count": len(
            {(int(profile["prime"]), int(profile["R"])) for profile in strong}
        ),
        "ranked_scope_strong_miss_count": len(ranked_strong),
        "ranked_scope_strong_miss_state_count": len(
            {(int(profile["prime"]), int(profile["R"])) for profile in ranked_strong}
        ),
        "natural_endpoint_legal_gap_count": sum(
            bool(profile["natural_endpoint_is_legal"]) for profile in profiles
        ),
        "natural_endpoint_hit_count": sum(
            bool(profile["natural_endpoint_hit"]) for profile in profiles
        ),
        "ranked_scope_natural_endpoint_legal_gap_count": sum(
            bool(profile["natural_endpoint_is_legal"]) for profile in ranked
        ),
        "ranked_scope_natural_endpoint_hit_count": sum(
            bool(profile["natural_endpoint_hit"]) for profile in ranked
        ),
        "q_equals_2_count": sum(int(profile["q"]) == 2 for profile in profiles),
        "exponent_one_count": sum(
            int(profile["exponent"]) == 1 for profile in profiles
        ),
        "higher_exponent_count": sum(
            int(profile["exponent"]) > 1 for profile in profiles
        ),
        "maximum_external_exponent": max(
            int(profile["exponent"]) for profile in profiles
        ),
    }
    if summary != EXPECTED_SUMMARY:
        raise AssertionError(f"large-slab Reach profile changed: {summary}")

    alpha_histogram = Counter(int(profile["alpha"]) for profile in profiles)
    ranked_alpha_histogram = Counter(int(profile["alpha"]) for profile in ranked)
    strong_alpha_histogram = Counter(int(profile["alpha"]) for profile in strong)
    ranked_strong_alpha_histogram = Counter(
        int(profile["alpha"]) for profile in ranked_strong
    )
    formal_descendant_residual_alpha_histogram = Counter(
        int(profile["alpha"]) for profile in formal_descendant_residuals
    )
    expected_histograms = {
        "complete_reach": {1: 899, 2: 368, 3: 145},
        "ranked_scope": {1: 378, 2: 202, 3: 58},
        "strong_miss": {1: 420, 2: 126, 3: 20},
        "ranked_scope_strong_miss": {1: 172, 2: 67, 3: 8},
        "formal_descendant_residual": {1: 53, 2: 16, 3: 1},
    }
    observed_histograms = {
        "complete_reach": dict(sorted(alpha_histogram.items())),
        "ranked_scope": dict(sorted(ranked_alpha_histogram.items())),
        "strong_miss": dict(sorted(strong_alpha_histogram.items())),
        "ranked_scope_strong_miss": dict(sorted(ranked_strong_alpha_histogram.items())),
        "formal_descendant_residual": dict(
            sorted(formal_descendant_residual_alpha_histogram.items())
        ),
    }
    if observed_histograms != expected_histograms:
        raise AssertionError(f"alpha histograms changed: {observed_histograms}")

    collision_keys = sorted(
        (
            int(profile["prime"]),
            int(profile["R"]),
            tuple(int(value) for value in profile["node"][:2]),
            tuple(int(value) for value in profile["direct_collision_T"]),
            tuple(int(value) for value in profile["cross_chart_collision_T"]),
        )
        for profile in collision_records
    )
    expected_collision_keys = [
        (178_790_089, 111, (10, 101), (111,), ()),
        (266_080_369, 63, (1, 62), (), (7,)),
        (452_110_129, 63, (1, 62), (), (7,)),
        (508_542_169, 103, (2, 101), (103,), ()),
    ]
    if collision_keys != expected_collision_keys:
        raise AssertionError(f"collision records changed: {collision_keys}")

    def sort_key(profile: dict[str, object]) -> tuple[object, ...]:
        return (
            int(profile["prime"]),
            int(profile["R"]),
            tuple(int(value) for value in profile["node"]),
            int(profile["Q"]),
        )

    minimum_strong = min(strong, key=sort_key)
    minimum_ranked_strong = min(ranked_strong, key=sort_key)
    minimum_both_rank_accepted = min(
        (
            profile
            for profile in strong
            if bool(profile["in_min_accepted_destination"])
            and bool(profile["in_max_accepted_destination"])
        ),
        key=sort_key,
    )
    minimum_ranked_alpha_three = min(
        (profile for profile in ranked_strong if int(profile["alpha"]) == 3),
        key=sort_key,
    )
    representative_keys = [
        (
            int(profile["prime"]),
            int(profile["R"]),
            tuple(int(value) for value in profile["node"][:2]),
            int(profile["Q"]),
            int(profile["alpha"]),
            int(profile["beta"]),
            int(profile["R_Q"]),
        )
        for profile in (
            minimum_strong,
            minimum_ranked_strong,
            minimum_both_rank_accepted,
            minimum_ranked_alpha_three,
        )
    ]
    expected_representatives = [
        (214_729, 391, (5, 386), 193, 2, 5, 731),
        (5_596_369, 35, (3, 32), 32, 1, 3, 79),
        (20_384_809, 719, (21, 698), 349, 2, 21, 1_319),
        (24_738_289, 455, (2, 453), 151, 3, 2, 523),
    ]
    if representative_keys != expected_representatives:
        raise AssertionError(
            f"representative strong misses changed: {representative_keys}"
        )

    alpha_three_profile = next(
        profile
        for profile in strong
        if (int(profile["prime"]), int(profile["R"])) == (212_973_049, 215)
        and tuple(int(value) for value in profile["node"]) == (2, 213, 1)
    )
    residual_profile = next(
        profile
        for profile in strong
        if (int(profile["prime"]), int(profile["R"])) == (78_268_369, 8_895)
        and tuple(int(value) for value in profile["node"]) == (652, 8_243, 1)
    )
    minimum_formal_descendant_residual = min(formal_descendant_residuals, key=sort_key)
    minimum_formal_descendant_key = (
        int(minimum_formal_descendant_residual["prime"]),
        int(minimum_formal_descendant_residual["R"]),
        tuple(int(value) for value in minimum_formal_descendant_residual["node"][:2]),
        int(minimum_formal_descendant_residual["Q"]),
        int(minimum_formal_descendant_residual["alpha"]),
        int(minimum_formal_descendant_residual["beta"]),
    )
    if minimum_formal_descendant_key != (
        5_596_369,
        35,
        (3, 32),
        32,
        1,
        3,
    ):
        raise AssertionError(
            "minimum formal-descendant residual changed: "
            f"{minimum_formal_descendant_key}"
        )

    return {
        "schema_version": "psi-one-large-slab-reach-boundary/v1",
        "arithmetic": (
            "For all 483 hash-frozen Psi_0=1 F states, rebuild the unpruned formal "
            "Reach and both ranked scopes; extract every m=1 single-external slab "
            "with Q>R/4; exhaust the two divisor collisions, filtered external-affine "
            "coordinate-divisor gaps at the node and anchor, and the canonical "
            "Q-capacity chart; then verify the natural-tail integrality identities "
            "and selected source paths exactly."
        ),
        "scope_note": (
            "This is exact finite evidence on a frozen 483-state family. Formal "
            "Reach edges are candidate-generation evidence and do not satisfy E4. "
            "A strong miss refutes only automatic closure of the audited local menu; "
            "it is not an Erdos-Straus counterexample or a universal impossibility result."
        ),
        "input": {"path": INPUT.name, "sha256": input_hash},
        "closure_script": {"path": CLOSURE_SCRIPT.name, "sha256": closure_hash},
        "script_sha256": sha256(Path(__file__)),
        "summary": summary,
        "counting_and_completeness": {
            "counting_unit": (
                "nodes and labeled transition occurrences are summed over the 483 "
                "per-state graphs; slab-menu counts are slab records"
            ),
            "closure": (
                "raw_transitions enumerates both coordinates and every prime whose "
                "coordinate valuation exceeds v_q(K), until the frontier is empty; "
                "m decreases above layer one and stays one at the bottom layer"
            ),
            "external_affine_filter": (
                "h divides a node coordinate, 3<=h<=p-2, h=3 mod 4, and "
                "h/gcd(h,K)>1; each retained gap is checked by exact square-divisor "
                "Type I/II enumeration"
            ),
            "pre_absorption_accounting": (
                "948 slab records miss both collisions and both external-affine "
                "menus; 382 of those have R_Q<R, leaving 566 strong misses"
            ),
        },
        "alpha_histograms": {
            family: {str(alpha): count for alpha, count in histogram.items()}
            for family, histogram in observed_histograms.items()
        },
        "stable_source_constraints": {
            "all_records_checked": len(profiles),
            "support": "gcd(Q,alpha*beta)=1 and alpha*beta divides K",
            "source_congruences": [
                "p*Q*alpha == -1 (mod beta)",
                "p*beta == -1 (mod alpha)",
            ],
            "capacity_test": "R_Q<R iff 4*rho<R, rho=K*p^{-1} mod Q",
            "alpha_three_odd_q": "R=23 (mod 24), beta=2 (mod 6)",
            "alpha_three_q_two": "R=11 (mod 24), beta=5 (mod 6)",
        },
        "collision_records": [public_record(profile) for profile in collision_records],
        "representative_strong_misses": {
            "minimum_complete_reach": public_record(minimum_strong),
            "minimum_ranked_scope": public_record(minimum_ranked_strong),
            "minimum_both_rank_accepted": public_record(minimum_both_rank_accepted),
            "minimum_ranked_alpha_three": public_record(minimum_ranked_alpha_three),
        },
        "source_anchored_alpha_three_formal_path": verify_alpha_three_source_path(
            source_by_key[(212_973_049, 215)], alpha_three_profile
        ),
        "minimum_formal_descendant_residual": verify_formal_descendant_residual(
            source_by_key[(5_596_369, 35)], minimum_formal_descendant_residual
        ),
        "alpha_three_formal_descendant_residual": (
            verify_alpha_three_descendant_residual(
                source_by_key[(24_738_289, 455)], minimum_ranked_alpha_three
            )
        ),
        "residual_pressure_point": verify_residual_pressure_point(
            source_by_key[(78_268_369, 8_895)], residual_profile
        ),
        "natural_tail_boundary": {
            "formal_node_identity": ("4/p = 1/(pK) + 1/(mK/B) + 1/(mK/A)"),
            "integrality_criterion": (
                "gcd(m,A)=gcd(m,B)=1, so both natural tails are integral iff A*B divides K"
            ),
            "slab_consequence": (
                "for A=Q*alpha, B=beta, K=alpha*beta*c, the good tail is "
                "m*alpha*c and the other residual is Q/(m*beta*c) in lowest terms"
            ),
            "ordinary_target_boundary": (
                "Q/(m*beta*c)=4/n only if Q divides 4; any resulting n is greater than p"
            ),
            "anchor_consequence": (
                "keeping pK and K/alpha forces K/(R-alpha), integral iff the anchor is already a sink"
            ),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
