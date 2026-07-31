#!/usr/bin/env python3
"""Audit direct terminals and unlifted dyadic predecessors on all frozen Psi_0=1 F states."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import math
import multiprocessing
import os
from pathlib import Path
import sys
from typing import Iterable, Literal


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
OLD_PSI_ONE_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-psi-one-nearest-fiber-escape-boundary-results.json"
)
NEAR_SCRIPT = ROOT / "reproductions" / "type_i_f_psi_one_nearest_fiber_escape_boundary.py"
CLOSURE_SCRIPT = ROOT / "reproductions" / "type_i_f_psi_one_formal_transition_closure.py"
DYADIC_SCRIPT = ROOT / "reproductions" / "type_i_linear_target_fiber_dyadic_non_near_profile_600m.py"
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-psi-one-full-spectrum-terminal-descent-audit-results.json"
)

EXPECTED_INPUT_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_OLD_INPUT_SHA256 = "a7babc394423104647090a6bdae4255ff8cc73d2bb06dae6a0e3e1aefce4b2d2"
EXPECTED_SUMMARY = {
    "source_f_state_count": 2_752,
    "one_layer_face_point_count": 13_533_050,
    "psi_one_state_count": 483,
    "positive_witness_count": 1_615,
    "old_psi_one_subset_count": 55,
    "old_psi_one_positive_witness_count": 140,
    "legal_internal_gap_count": 11_406,
    "internal_hit_gap_count": 666,
    "internal_type_i_gap_count": 525,
    "internal_type_ii_gap_count": 141,
    "internal_hit_state_count": 328,
    "min_visited_hit_state_count": 430,
    "min_lookahead_hit_state_count": 392,
    "min_union_hit_state_count": 455,
    "max_visited_hit_state_count": 441,
    "max_lookahead_hit_state_count": 384,
    "max_union_hit_state_count": 459,
    "dual_rank_hit_state_count": 467,
    "internal_union_min_hit_state_count": 473,
    "internal_union_max_hit_state_count": 474,
    "internal_union_dual_hit_state_count": 475,
    "cross_chart_hit_state_count": 4,
    "state_local_direct_hit_state_count": 479,
    "state_local_direct_residual_count": 4,
    "external_gap_candidate_count": 29_058,
    "external_gap_hit_count": 5_166,
    "external_type_i_gap_count": 4_073,
    "external_type_ii_gap_count": 1_093,
    "unlifted_dyadic_state_count": 483,
    "unlifted_dyadic_candidate_count": 3_976,
    "unlifted_dyadic_distinct_n_count": 1_385,
    "unlifted_dyadic_maximum_j": 24,
    "unlifted_dyadic_maximum_state_candidate_count": 60,
    "dyadic_alpha_integral_candidate_count": 3_976,
    "dyadic_alpha_equals_n_over_2_count": 0,
    "dyadic_alpha_equals_n_count": 0,
    "global_gap_cap": 127,
    "global_fallback_hit_state_count": 4,
    "finite_final_verified_state_count": 483,
}
EXPECTED_RESIDUALS = [
    [37_793_809, 35],
    [78_268_369, 8_895],
    [174_600_409, 20_631],
    [278_505_049, 231],
]
EXPECTED_CROSS_KEYS = [
    [5_596_369, 35],
    [37_793_809, 623],
    [536_944_489, 7_367],
    [556_685_089, 199],
]
EXPECTED_CROSS_FIRST_HITS = [
    [5_596_369, 35, 11, 85, 31],
    [37_793_809, 623, 31, 8_300, 1_071],
    [536_944_489, 7_367, 19, 869, 183],
    [556_685_089, 199, 19, 71_466_329, 15_045_543],
]
EXPECTED_FALLBACKS = [
    [37_793_809, 35, 43, 9_448_463, 8_789_857],
    [78_268_369, 8_895, 19, 19_567_097, 1_361],
    [174_600_409, 20_631, 19, 43_650_107, 4_200_193],
    [278_505_049, 231, 15, 69_626_266, 2_066],
]

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


near = load_module("full_psi_one_near", NEAR_SCRIPT)
closure = load_module("full_psi_one_closure", CLOSURE_SCRIPT)
dyadic = load_module("full_psi_one_dyadic", DYADIC_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def key(record: dict[str, object]) -> tuple[int, int]:
    return int(record["prime"]), int(record["R"])


def first_certificate_for_gaps(
    prime: int, gaps: Iterable[int], origins: dict[int, dict[str, object]]
) -> tuple[int, dict[str, object] | None, Counter[str]]:
    hit_count = 0
    first: dict[str, object] | None = None
    types: Counter[str] = Counter()
    for gap in sorted(set(gaps)):
        certificate = closure.exact_gap_certificate(prime, gap)
        if certificate is None:
            continue
        hit_count += 1
        certificate_type = str(certificate["type"])
        types[certificate_type] += 1
        if first is None:
            first = {
                "external_gap": gap,
                "origin": origins[gap],
                **certificate,
            }
    return hit_count, first, types


def node_terminal_profile(nodes: set[Node], prime: int, K: int) -> dict[str, object]:
    gaps, origins = closure.external_gap_candidates(nodes, prime, K)
    hit_count, first, types = first_certificate_for_gaps(prime, gaps, origins)
    return {
        "node_count": len(nodes),
        "candidate_count": len(gaps),
        "hit_gap_count": hit_count,
        "type_i_gap_count": int(types["Type_I"]),
        "type_ii_gap_count": int(types["Type_II"]),
        "first_verified_certificate": first,
        "hit": first is not None,
        "_gaps": gaps,
    }


def ranked_profile(
    prime: int,
    R: int,
    K: int,
    K_bounds: dict[int, int],
    starts: list[Node],
    mode: RankMode,
) -> dict[str, object]:
    visited: set[Node] = set()
    accepted_edges: list[tuple[Node, dict[str, object]]] = []
    rejected_edges: list[tuple[Node, dict[str, object]]] = []
    frontier = list(starts)
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        for edge in closure.raw_transitions(node, R, K_bounds):
            destination = edge["destination"]
            if closure.rank(destination, mode) < closure.rank(node, mode):
                accepted_edges.append((node, edge))
                if destination not in visited:
                    frontier.append(destination)
            else:
                rejected_edges.append((node, edge))
        if len(visited) > 100_000:
            raise AssertionError("ranked closure exceeded its safety bound")

    rejected_successors = {
        edge["destination"] for _source, edge in rejected_edges
    } - visited
    visited_terminals = node_terminal_profile(visited, prime, K)
    lookahead_terminals = node_terminal_profile(rejected_successors, prime, K)
    union_terminals = node_terminal_profile(visited | rejected_successors, prime, K)
    return {
        "mode": mode,
        "visited_node_count": len(visited),
        "accepted_edge_count": len(accepted_edges),
        "rejected_edge_count": len(rejected_edges),
        "one_step_rejected_successor_count": len(rejected_successors),
        "visited_terminals": visited_terminals,
        "lookahead_terminals": lookahead_terminals,
        "union_terminals": union_terminals,
        "edge_semantics": "analysis_evidence_not_verified_edge",
    }


def internal_profile(prime: int, K: int) -> dict[str, object]:
    legal_gaps = [
        gap
        for gap in closure.divisors(K)
        if gap % 4 == 3 and 3 <= gap <= prime - 2
    ]
    hits = []
    types: Counter[str] = Counter()
    for gap in legal_gaps:
        certificate = closure.exact_gap_certificate(prime, gap)
        if certificate is None:
            continue
        hits.append({"internal_gap": gap, **certificate})
        types[str(certificate["type"])] += 1
    return {
        "legal_gap_count": len(legal_gaps),
        "hit_gap_count": len(hits),
        "type_i_gap_count": int(types["Type_I"]),
        "type_ii_gap_count": int(types["Type_II"]),
        "first_verified_certificate": hits[0] if hits else None,
        "hit": bool(hits),
        "_legal_gaps": legal_gaps,
    }


def dyadic_profile(R: int, K: int) -> dict[str, object]:
    terminals = dyadic.legal_terminals(R, K)
    alpha_integral_count = 0
    alpha_half_count = 0
    alpha_full_count = 0
    enriched = []
    for terminal in terminals:
        E = int(terminal["E"])
        n = int(terminal["n"])
        alpha, remainder = divmod(n * K, E)
        if remainder:
            raise AssertionError("dyadic marked denominator was not integral")
        if n * n % E:
            raise AssertionError("dyadic lift factor did not divide n^2")
        alpha_integral_count += 1
        alpha_half_count += int(alpha == n // 2)
        alpha_full_count += int(alpha == n)
        enriched.append({**terminal, "marked_denominator_alpha": alpha})
    return {
        "candidate_count": len(enriched),
        "distinct_n_count": len({int(item["n"]) for item in enriched}),
        "maximum_j": max((int(item["j"]) for item in enriched), default=0),
        "first_candidate": enriched[0] if enriched else None,
        "alpha_integral_count": alpha_integral_count,
        "alpha_equals_n_over_2_count": alpha_half_count,
        "alpha_equals_n_count": alpha_full_count,
        "status": "unlifted_generalized_dyadic_candidate" if enriched else "miss",
        "lift_boundary": (
            "The even base solution (n/2,n,n) does not contain alpha=nK/E. "
            "A marked source solution and an E4 lift are not supplied."
        ),
    }


def one_layer_face_size(bounds: list[int]) -> int:
    return sum(
        math.prod(2 * value + 1 for index, value in enumerate(bounds) if index != defect)
        for defect in range(len(bounds))
    )


def audit_source_record(raw: dict[str, object]) -> dict[str, object]:
    prime = int(raw["prime"])
    R = int(raw["R"])
    K = int(raw["K"])
    factors = [(int(q), int(exponent)) for q, exponent in raw["factorization"]]
    primes = [q for q, _exponent in factors]
    bounds = [exponent for _q, exponent in factors]
    face_size = one_layer_face_size(bounds)
    witnesses = near.positive_unit_witnesses(R, primes, bounds)
    if not witnesses:
        return {"psi_one": False, "one_layer_face_point_count": face_size}

    starts: list[Node] = []
    witness_rows = []
    for witness in witnesses:
        exponents = tuple(int(value) for value in witness["exponents"])
        left, right = near.ratio_from_exponents(primes, exponents)
        if (left + right) % R:
            raise AssertionError("one-layer witness left the target fiber")
        start = closure.canonical_node(left, right, (left + right) // R, R)
        starts.append(start)
        witness_rows.append(
            {
                "defect_prime": int(witness["defect_prime"]),
                "exponents": list(exponents),
                "start": list(start),
            }
        )

    K_bounds = {q: exponent for q, exponent in factors}
    internal = internal_profile(prime, K)
    minimum = ranked_profile(prime, R, K, K_bounds, starts, "min")
    maximum = ranked_profile(prime, R, K, K_bounds, starts, "max")
    all_external_gaps = sorted(
        set(minimum["union_terminals"]["_gaps"])
        | set(maximum["union_terminals"]["_gaps"])
    )
    origins = {gap: {"scope": "min_or_max_union"} for gap in all_external_gaps}
    external_hits, _first, external_types = first_certificate_for_gaps(
        prime, all_external_gaps, origins
    )
    return {
        "psi_one": True,
        "one_layer_face_point_count": face_size,
        "prime": prime,
        "R": R,
        "K": K,
        "factorization": [[q, exponent] for q, exponent in factors],
        "positive_witness_count": len(witness_rows),
        "positive_witnesses": witness_rows,
        "internal": internal,
        "min_rank": minimum,
        "max_rank": maximum,
        "external_gap_union": {
            "candidate_count": len(all_external_gaps),
            "hit_gap_count": external_hits,
            "type_i_gap_count": int(external_types["Type_I"]),
            "type_ii_gap_count": int(external_types["Type_II"]),
            "_gaps": all_external_gaps,
        },
        "dyadic": dyadic_profile(R, K),
    }


def cross_chart_profile(prime: int, candidate_moduli: list[int]) -> dict[str, object]:
    scans = []
    for modulus in candidate_moduli:
        K = (prime * modulus + 1) // 4
        if 4 * K != prime * modulus + 1:
            raise AssertionError("cross-chart candidate was not a legal modulus")
        search_space, hits = closure.centered_type_i_hits(prime, modulus, K)
        scans.append(
            {
                "new_modulus": modulus,
                "new_K": K,
                "centered_search_space": search_space,
                "hit_count": len(hits),
                "first_hit": hits[0] if hits else None,
            }
        )
    first_hit = next((scan for scan in scans if scan["hit_count"]), None)
    return {
        "candidate_moduli": candidate_moduli,
        "scans": scans,
        "first_hit": first_hit,
        "hit": first_hit is not None,
        "semantics": "direct Type I certificate for the original prime, not a recursive edge",
    }


def first_global_gap_certificate(prime: int, cap: int) -> dict[str, object] | None:
    for gap in range(3, cap + 1, 4):
        certificate = closure.exact_gap_certificate(prime, gap)
        if certificate is not None:
            return certificate
    return None


def strip_private_fields(value: object) -> object:
    if isinstance(value, dict):
        return {
            key_name: strip_private_fields(item)
            for key_name, item in value.items()
            if not key_name.startswith("_") and key_name != "psi_one"
        }
    if isinstance(value, list):
        return [strip_private_fields(item) for item in value]
    return value


def state_set(records: list[dict[str, object]], predicate) -> set[tuple[int, int]]:
    return {key(record) for record in records if predicate(record)}


def run(workers: int) -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen full-spectrum F input changed")
    if sha256(OLD_PSI_ONE_INPUT) != EXPECTED_OLD_INPUT_SHA256:
        raise AssertionError("the frozen 55-state Psi_0=1 input changed")
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    source_records = source["records"]
    if len(source_records) != EXPECTED_SUMMARY["source_f_state_count"]:
        raise AssertionError("the frozen full-spectrum state count changed")

    if workers == 1:
        raw_audit = [audit_source_record(record) for record in source_records]
    else:
        context = multiprocessing.get_context("fork")
        with context.Pool(processes=workers) as pool:
            raw_audit = pool.map(audit_source_record, source_records, chunksize=8)
    face_point_count = sum(int(record["one_layer_face_point_count"]) for record in raw_audit)
    records = [record for record in raw_audit if bool(record["psi_one"])]
    records.sort(key=key)

    old = json.loads(OLD_PSI_ONE_INPUT.read_text(encoding="utf-8"))
    old_keys = {(int(row["prime"]), int(row["R"])) for row in old["records"]}
    new_keys = {key(record) for record in records}
    if not old_keys <= new_keys:
        raise AssertionError("the old 55-state family ceased to be a subset")
    old_witness_count = sum(
        int(record["positive_witness_count"])
        for record in records
        if key(record) in old_keys
    )

    internal = state_set(records, lambda row: row["internal"]["hit"])
    min_visited = state_set(records, lambda row: row["min_rank"]["visited_terminals"]["hit"])
    min_lookahead = state_set(records, lambda row: row["min_rank"]["lookahead_terminals"]["hit"])
    min_union = state_set(records, lambda row: row["min_rank"]["union_terminals"]["hit"])
    max_visited = state_set(records, lambda row: row["max_rank"]["visited_terminals"]["hit"])
    max_lookahead = state_set(records, lambda row: row["max_rank"]["lookahead_terminals"]["hit"])
    max_union = state_set(records, lambda row: row["max_rank"]["union_terminals"]["hit"])
    dual = min_union | max_union
    before_cross = internal | dual

    cross_profiles = []
    cross_hits: set[tuple[int, int]] = set()
    for record in records:
        state_key = key(record)
        if state_key in before_cross:
            continue
        candidate_moduli = sorted(
            set(record["min_rank"]["union_terminals"]["_gaps"])
            | set(record["max_rank"]["union_terminals"]["_gaps"])
        )
        profile = cross_chart_profile(int(record["prime"]), candidate_moduli)
        cross_profiles.append(
            {"prime": state_key[0], "R": state_key[1], **profile}
        )
        if profile["hit"]:
            cross_hits.add(state_key)
    local_direct = before_cross | cross_hits
    residuals = sorted(new_keys - local_direct)

    fallback_records = []
    for prime, R in residuals:
        certificate = first_global_gap_certificate(
            prime, EXPECTED_SUMMARY["global_gap_cap"]
        )
        if certificate is None:
            raise AssertionError("a finite residual lost its global fallback")
        fallback_records.append({"prime": prime, "R": R, "certificate": certificate})

    cross_keys = sorted(cross_hits)
    if [list(item) for item in residuals] != EXPECTED_RESIDUALS:
        raise AssertionError(f"state-local residual set changed: {residuals}")
    if [list(item) for item in cross_keys] != EXPECTED_CROSS_KEYS:
        raise AssertionError(f"cross-chart exclusive set changed: {cross_keys}")
    cross_first_hits = [
        [
            int(profile["prime"]),
            int(profile["R"]),
            int(profile["first_hit"]["new_modulus"]),
            int(profile["first_hit"]["first_hit"]["centered_divisor"]),
            int(profile["first_hit"]["first_hit"]["gap"]),
        ]
        for profile in cross_profiles
        if profile["hit"]
    ]
    if cross_first_hits != EXPECTED_CROSS_FIRST_HITS:
        raise AssertionError(f"cross-chart first certificates changed: {cross_first_hits}")
    fallback_profiles = [
        [
            int(record["prime"]),
            int(record["R"]),
            int(record["certificate"]["gap"]),
            int(record["certificate"]["first_denominator"]),
            int(record["certificate"]["divisor"]),
        ]
        for record in fallback_records
    ]
    if fallback_profiles != EXPECTED_FALLBACKS:
        raise AssertionError(f"global fallback certificates changed: {fallback_profiles}")

    dyadic_records = [record["dyadic"] for record in records]
    summary = {
        "source_f_state_count": len(source_records),
        "one_layer_face_point_count": face_point_count,
        "psi_one_state_count": len(records),
        "positive_witness_count": sum(int(record["positive_witness_count"]) for record in records),
        "old_psi_one_subset_count": len(old_keys),
        "old_psi_one_positive_witness_count": old_witness_count,
        "legal_internal_gap_count": sum(int(record["internal"]["legal_gap_count"]) for record in records),
        "internal_hit_gap_count": sum(int(record["internal"]["hit_gap_count"]) for record in records),
        "internal_type_i_gap_count": sum(int(record["internal"]["type_i_gap_count"]) for record in records),
        "internal_type_ii_gap_count": sum(int(record["internal"]["type_ii_gap_count"]) for record in records),
        "internal_hit_state_count": len(internal),
        "min_visited_hit_state_count": len(min_visited),
        "min_lookahead_hit_state_count": len(min_lookahead),
        "min_union_hit_state_count": len(min_union),
        "max_visited_hit_state_count": len(max_visited),
        "max_lookahead_hit_state_count": len(max_lookahead),
        "max_union_hit_state_count": len(max_union),
        "dual_rank_hit_state_count": len(dual),
        "internal_union_min_hit_state_count": len(internal | min_union),
        "internal_union_max_hit_state_count": len(internal | max_union),
        "internal_union_dual_hit_state_count": len(before_cross),
        "cross_chart_hit_state_count": len(cross_hits),
        "state_local_direct_hit_state_count": len(local_direct),
        "state_local_direct_residual_count": len(residuals),
        "external_gap_candidate_count": sum(int(record["external_gap_union"]["candidate_count"]) for record in records),
        "external_gap_hit_count": sum(int(record["external_gap_union"]["hit_gap_count"]) for record in records),
        "external_type_i_gap_count": sum(int(record["external_gap_union"]["type_i_gap_count"]) for record in records),
        "external_type_ii_gap_count": sum(int(record["external_gap_union"]["type_ii_gap_count"]) for record in records),
        "unlifted_dyadic_state_count": sum(int(record["candidate_count"] > 0) for record in dyadic_records),
        "unlifted_dyadic_candidate_count": sum(int(record["candidate_count"]) for record in dyadic_records),
        "unlifted_dyadic_distinct_n_count": sum(int(record["distinct_n_count"]) for record in dyadic_records),
        "unlifted_dyadic_maximum_j": max(int(record["maximum_j"]) for record in dyadic_records),
        "unlifted_dyadic_maximum_state_candidate_count": max(int(record["candidate_count"]) for record in dyadic_records),
        "dyadic_alpha_integral_candidate_count": sum(int(record["alpha_integral_count"]) for record in dyadic_records),
        "dyadic_alpha_equals_n_over_2_count": sum(int(record["alpha_equals_n_over_2_count"]) for record in dyadic_records),
        "dyadic_alpha_equals_n_count": sum(int(record["alpha_equals_n_count"]) for record in dyadic_records),
        "global_gap_cap": EXPECTED_SUMMARY["global_gap_cap"],
        "global_fallback_hit_state_count": len(fallback_records),
        "finite_final_verified_state_count": len(local_direct) + len(fallback_records),
    }
    if summary != EXPECTED_SUMMARY:
        raise AssertionError(f"full Psi_0=1 audit changed: {summary}")

    priority_stages = {
        "internal": len(internal),
        "after_min_visited": len(internal | min_visited),
        "after_min_lookahead": len(internal | min_visited | min_lookahead),
        "after_max_visited": len(internal | min_visited | min_lookahead | max_visited),
        "after_max_lookahead": len(before_cross),
        "after_cross_chart": len(local_direct),
        "after_global_gap_cap_127": len(local_direct) + len(fallback_records),
    }
    expected_stages = {
        "internal": 328,
        "after_min_visited": 468,
        "after_min_lookahead": 473,
        "after_max_visited": 473,
        "after_max_lookahead": 475,
        "after_cross_chart": 479,
        "after_global_gap_cap_127": 483,
    }
    if priority_stages != expected_stages:
        raise AssertionError(f"selector priority stages changed: {priority_stages}")

    for record in records:
        state_key = key(record)
        if state_key in residuals:
            record["state_local_residual_external_gaps"] = record["external_gap_union"]["_gaps"]
            record["state_local_residual_internal_gaps"] = record["internal"]["_legal_gaps"]

    return {
        "schema_version": "psi-one-full-spectrum-terminal-descent-audit/v1",
        "arithmetic": (
            "Identify every Psi_0=1 state in the frozen 2,752-state finite-exponent F spectrum; "
            "run internal gaps, min/max ranked accepted closures, rejected one-step terminal "
            "lookahead, external-gap direct certificates, and centered cross-chart certificates; "
            "then enumerate every generalized dyadic predecessor and audit its natural marked lift."
        ),
        "scope_note": (
            "The 483 states come from 200 frozen pressure primes and are not all core primes. "
            "Formal transitions remain analysis evidence. Cross-chart hits and the final small-gap "
            "fallbacks are independently verified direct certificates. All generalized dyadic "
            "objects are recorded as unlifted predecessors: they do not satisfy E4 and are not "
            "counted in the 479 state-local direct hits or the final verified total."
        ),
        "inputs": {
            "full_spectrum": {"path": INPUT.name, "sha256": sha256(INPUT)},
            "old_psi_one_subset": {
                "path": OLD_PSI_ONE_INPUT.name,
                "sha256": sha256(OLD_PSI_ONE_INPUT),
            },
        },
        "script_sha256": sha256(Path(__file__)),
        "summary": summary,
        "priority_stage_counts": priority_stages,
        "set_intersections": {
            "internal_intersection_min": len(internal & min_union),
            "internal_intersection_max": len(internal & max_union),
            "internal_intersection_dual": len(internal & dual),
            "min_intersection_max": len(min_union & max_union),
            "min_visited_intersection_lookahead": len(min_visited & min_lookahead),
            "max_visited_intersection_lookahead": len(max_visited & max_lookahead),
        },
        "cross_chart_profiles": cross_profiles,
        "state_local_direct_residuals": [list(item) for item in residuals],
        "global_fallback_certificates": fallback_records,
        "natural_dyadic_lift_contract": {
            "marked_denominator": "alpha=n*K/E",
            "integrality_proof": "E|4K^2, nR=4K-E, and gcd(E,R)=1 imply E|nK",
            "marked_remainder": "4/n - 1/alpha = R/K = 4/p - 1/(pK)",
            "natural_lift": "(alpha,u,v) maps to (pK,u,v)",
            "nonempty_iff": "R/K is a sum of two positive unit fractions, equivalently the current chart has a centered Type I divisor",
            "F_state_consequence": "the natural marked source set is empty",
            "trivial_even_base_consequence": "alpha is neither n/2 nor n for these 483 states",
        },
        "records": [strip_private_fields(record) for record in records],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--workers", type=int, default=min(6, os.cpu_count() or 1))
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.workers < 1:
        raise ValueError("--workers must be positive")
    payload = run(args.workers)
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
