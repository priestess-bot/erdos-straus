#!/usr/bin/env python3
"""Audit the frozen pre-T6 kernel and the explicit T6 proof frontier.

This verifier is deliberately structural.  It proves that the repository's
*claims about its proof boundary* are internally consistent; it does not prove
reachable-state exhaustion, construct a total selector, or prove the
Erdos--Straus conjecture.

The script uses only the Python standard library so it can run in the existing
knowledge-base CI without adding a dependency.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

BASELINE_COMMIT = "ef95ac0f2c3b687bb67d33dc490b248ccd8cfcb0"

KERNEL_THEOREM_STATUSES = {
    "T1v1": "CLOSED_RELATIVE",
    "T2v1": "CLOSED_PHASE_LOCAL",
    "T3v1": "CLOSED_CURRENT_GRAPH",
    "T4v1": "CLOSED_RELATIVE",
    "T5v1": "CLOSED_CONTRACT_LEVEL",
}

LEGACY_STRONG_IDS = {"T1-star", "T2-star", "T3-star"}
MECHANICAL_CLOSURE_IDS = {
    "registered_surface_inventory",
    "current_graph_mark_invariant",
    "constructor_admission_firewall",
    "pre_t6_scope_separation",
    "q1_package_provenance_boundary",
}

EXPECTED_FAMILY_IDS = {
    "initial_core_root",
    "type_ii_relation_f_endpoint",
    "type_ii_relation_g_endpoint",
    "type_i_full_carrier_post_g",
    "type_i_low_support_persistent_overflow",
    "type_i_a_one_overflow",
    "type_i_a_gt_one_overflow_residual",
    "type_i_high_support_sink",
    "proper_root_stutter_k_one",
    "proper_root_stutter_k_gt_one",
    "c8_terminal_first_surviving_parent",
    "h4_non_v1_branch_or_descendant",
    "type_i_c2_19_macro_target",
    "t2_v1_atomic_pending_target",
    "generic_nontrivial_marked_state",
    "direct_terminal_leaf",
}

EXPECTED_EDGE_IDS = {
    "type_ii_proper_endpoint_descent",
    "type_ii_gcd_shadow_endpoint_descent",
    "q_one_g_full_carrier_phase_root",
    "positive_q_g_full_carrier_phase_root",
    "q_one_g_c3_source_lineage_relay",
    "q_one_full_carrier_second_anchor_fixed_n_macro",
    "same_chart_support_promotion",
    "joined_support_outer_reset",
    "a_one_dual_outer_reset",
    "high_carrier_fixed_n_descent",
    "high_support_rank_aware_sink_bundle",
    "q_one_d_one_p_free_relay",
    "high_c_two_three_anchor_macro",
    "h4_a_one_atomic_macro",
    "c8_double_low_atomic_macro",
}

EXPECTED_FAMILY_STATUSES = {
    "initial_core_root": "CLOSED_BY_UNIVERSAL_SUCCESSOR",
    "type_ii_relation_f_endpoint": "CLOSED_BY_UNIVERSAL_SUCCESSOR",
    "type_ii_relation_g_endpoint": "RELATIVE_EDGE_ONLY",
    "type_i_full_carrier_post_g": "OPEN",
    "type_i_low_support_persistent_overflow": "CLOSED_BY_UNIVERSAL_SUCCESSOR",
    "type_i_a_one_overflow": "CLOSED_BY_UNIVERSAL_SUCCESSOR",
    "type_i_a_gt_one_overflow_residual": "OPEN",
    "type_i_high_support_sink": "LOCAL_EDGE_ONLY",
    "proper_root_stutter_k_one": "CLOSED_BY_EMPTY_PROOF",
    "proper_root_stutter_k_gt_one": "OPEN",
    "c8_terminal_first_surviving_parent": "OPEN",
    "h4_non_v1_branch_or_descendant": "OPEN",
    "type_i_c2_19_macro_target": "OPEN",
    "t2_v1_atomic_pending_target": "OPEN",
    "generic_nontrivial_marked_state": "UNREACHABLE_IN_FROZEN_GRAPH",
    "direct_terminal_leaf": "TERMINAL",
}

EXPECTED_V1_FAMILY_STATUSES = {
    **{
        family_id: status
        for family_id, status in EXPECTED_FAMILY_STATUSES.items()
        if family_id != "generic_nontrivial_marked_state"
    },
    "generic_nontrivial_marked_state": "UNREACHABLE_IN_CURRENT_NAMED_GRAPH",
}

EXPECTED_V1_GATE_STATUSES = {
    "initial_state_serializer": "ESTABLISHED",
    "reachable_state_exhaustion": "OPEN",
    "all_nonterminal_leaves_closed": "OPEN",
    "proper_root_qc1_or_tr1": "OPEN",
    "c8_outgoing_totality": "OPEN",
    "post_g_type_i_totality": "OPEN",
    "new_atomic_or_marked_t2_t3": "OPEN",
    "deterministic_computable_selector": "OPEN",
    "edge_e1_to_e5_coverage": "PARTIAL",
    "t5_strong_induction_termination": "PARTIAL",
    "terminal_certificate_lifts": "PARTIAL",
    "no_open_or_finite_only_in_closure": "OPEN",
    "repository_artifact_consistency": "PARTIAL",
    "independent_closure_audit": "OPEN",
}

EXPECTED_EDGE_SURFACE = {
    "type_ii_proper_endpoint_descent": (
        ("type_ii_relation_f_endpoint",),
        (
            "type_ii_relation_f_endpoint",
            "type_ii_relation_g_endpoint",
            "direct_terminal_leaf",
        ),
        "conditional_adapter_control",
    ),
    "type_ii_gcd_shadow_endpoint_descent": (
        ("type_ii_relation_f_endpoint",),
        (
            "type_ii_relation_f_endpoint",
            "type_ii_relation_g_endpoint",
            "direct_terminal_leaf",
        ),
        "actual",
    ),
    "q_one_g_full_carrier_phase_root": (
        ("type_ii_relation_g_endpoint",),
        ("type_i_full_carrier_post_g",),
        "actual",
    ),
    "positive_q_g_full_carrier_phase_root": (
        ("type_ii_relation_g_endpoint",),
        ("type_i_full_carrier_post_g",),
        "conditional_adapter_control",
    ),
    "q_one_g_c3_source_lineage_relay": (
        ("type_ii_relation_g_endpoint",),
        ("type_i_full_carrier_post_g",),
        "conditional_adapter_control",
    ),
    "q_one_full_carrier_second_anchor_fixed_n_macro": (
        ("type_i_full_carrier_post_g",),
        ("type_i_full_carrier_post_g",),
        "actual",
    ),
    "same_chart_support_promotion": (
        ("type_i_low_support_persistent_overflow",),
        ("type_i_low_support_persistent_overflow",),
        "actual",
    ),
    "joined_support_outer_reset": (
        ("type_i_a_gt_one_overflow_residual",),
        (
            "type_i_low_support_persistent_overflow",
            "type_i_a_gt_one_overflow_residual",
        ),
        "conditional_adapter_control",
    ),
    "a_one_dual_outer_reset": (
        ("type_i_a_one_overflow",),
        ("type_i_low_support_persistent_overflow",),
        "actual",
    ),
    "high_carrier_fixed_n_descent": (
        ("type_i_a_gt_one_overflow_residual",),
        ("type_i_low_support_persistent_overflow",),
        "conditional_adapter_control",
    ),
    "high_support_rank_aware_sink_bundle": (
        ("type_i_high_support_sink",),
        (
            "type_i_high_support_sink",
            "type_i_low_support_persistent_overflow",
        ),
        "conditional_adapter_control",
    ),
    "q_one_d_one_p_free_relay": (
        ("type_i_full_carrier_post_g",),
        (
            "type_i_c2_19_macro_target",
            "type_i_high_support_sink",
            "direct_terminal_leaf",
        ),
        "actual",
    ),
    "high_c_two_three_anchor_macro": (
        ("type_i_c2_19_macro_target",),
        ("type_i_c2_19_macro_target", "direct_terminal_leaf"),
        "conditional_adapter_control",
    ),
    "h4_a_one_atomic_macro": (
        ("type_i_c2_19_macro_target",),
        ("t2_v1_atomic_pending_target", "direct_terminal_leaf"),
        "conditional_adapter_control",
    ),
    "c8_double_low_atomic_macro": (
        ("c8_terminal_first_surviving_parent",),
        ("t2_v1_atomic_pending_target", "direct_terminal_leaf"),
        "conditional_adapter_control",
    ),
}

EXPECTED_IMMEDIATE_IDS = {
    "T6-M0-INITIAL-SERIALIZER",
    "T6-M1-NAMED-SURFACE-INVENTORY",
    "T6-M2-CURRENT-MARK-UNREACHABILITY",
    "T6-M3-CONSTRUCTOR-ADMISSION-FIREWALL",
    "T6-M4-M3-Q5-PFREE-RAW-POLICY",
    "T6-M5-PBLOCK-POLICY-ELIMINATION",
    "T6-M6-CANONICAL-CHANNEL-PARTITION",
    "T6-M7-P2-RESIDUAL-ISOLATION",
}

EXPECTED_FRONTIER_IDS = {
    "T6-F1-REACHABLE-STATE-EXHAUSTION",
    "T6-F2-NONPROPER-DISPATCH-TOTALITY",
    "T6-F3-PROPER-ROOT-PHYSICALIZATION",
    "T6-F4-SELECTOR-ASSEMBLY-AND-LIFTS",
    "T6-F5-INDEPENDENT-CLOSURE-AUDIT",
}

EXPECTED_ACTIVE_LEGACY_GAPS = {
    "GAP-O1-GLOBAL-EXHAUSTION",
    "GAP-O1-H4-OTHER-BRANCHES",
    "GAP-O1-POST-G-TYPE-I",
    "GAP-O1-A-GT-ONE-OVERFLOW",
    "GAP-O1-HIGH-SUPPORT-ROOT-CAPACITY",
    "GAP-O1-ATOMIC-TARGET-CLOSURE",
    "GAP-O2-PROPER-ROOT-K-GT-ONE",
    "GAP-O3-C8-OUTGOING",
}

EXPECTED_GATE_STATUSES = {
    "pre_t6_contract_kernel": "ESTABLISHED",
    "initial_state_serializer": "ESTABLISHED",
    "named_surface_inventory": "ESTABLISHED",
    "current_graph_mark_invariant": "ESTABLISHED",
    "constructor_admission_firewall": "ESTABLISHED",
    "m3_q5_arithmetic_dispatch": "ESTABLISHED_ARITHMETIC_ONLY",
    "reachable_state_exhaustion": "OPEN",
    "all_nonterminal_leaves_closed": "OPEN",
    "proper_root_physicalization": "OPEN",
    "deterministic_computable_selector": "OPEN",
    "edge_e1_to_e5_coverage": "PARTIAL",
    "terminal_certificate_lifts": "PARTIAL",
    "t5_strong_induction_termination": "PARTIAL",
    "no_open_or_finite_only_in_closure": "OPEN",
    "repository_artifact_consistency": "PARTIAL_UNTIL_FULL_CHECKOUT_CI",
    "independent_closure_audit": "OPEN",
}

REQUIRED_FORBIDDEN_CONCLUSIONS = {
    "T6_GLOBAL_SELECTOR_TOTALITY=CLOSED",
    "F0=CLOSED",
    "ERDOS_STRAUS_CONJECTURE=CLOSED",
    "arithmetic_candidate_implies_verified_edge",
    "registered_taxonomy_implies_semantic_reachability_exhaustion",
}

ALLOWED_GUARD_CLASSES = {"actual", "conditional_adapter_control"}


@dataclass(frozen=True)
class AuditResult:
    errors: tuple[str, ...]
    warnings: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing JSON file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"top-level JSON value must be an object: {path}")
    return value


def _ids(items: Sequence[Mapping[str, Any]], label: str, errors: list[str]) -> list[str]:
    result: list[str] = []
    for index, item in enumerate(items):
        identifier = item.get("id")
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"{label}[{index}] has no nonempty string id")
            continue
        result.append(identifier)
    duplicates = sorted({identifier for identifier in result if result.count(identifier) > 1})
    if duplicates:
        errors.append(f"{label} contains duplicate ids: {duplicates}")
    return result


def _expect_equal(errors: list[str], label: str, actual: Any, expected: Any) -> None:
    if actual != expected:
        errors.append(f"{label}: expected {expected!r}, got {actual!r}")


def _expect_nonempty_string(errors: list[str], label: str, value: Any) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a nonempty string")


def _expect_nonempty_string_list(errors: list[str], label: str, value: Any) -> None:
    if (
        not isinstance(value, list)
        or not value
        or any(not isinstance(item, str) or not item.strip() for item in value)
    ):
        errors.append(f"{label} must be a nonempty list of nonempty strings")


def _audit_baseline(kernel: Mapping[str, Any], frontier: Mapping[str, Any], errors: list[str]) -> None:
    kernel_sha = kernel.get("baseline_commit")
    frontier_sha = frontier.get("baseline_commit")
    _expect_equal(errors, "kernel baseline_commit", kernel_sha, BASELINE_COMMIT)
    _expect_equal(errors, "frontier baseline_commit", frontier_sha, BASELINE_COMMIT)
    if isinstance(kernel_sha, str) and not re.fullmatch(r"[0-9a-f]{40}", kernel_sha):
        errors.append("kernel baseline_commit is not a lowercase 40-hex commit SHA")
    if kernel_sha != frontier_sha:
        errors.append("kernel and frontier are not pinned to the same commit")


def _audit_kernel(kernel: Mapping[str, Any], errors: list[str]) -> None:
    _expect_equal(errors, "kernel manifest_id", kernel.get("manifest_id"), "pre_t6_contract_kernel_v1")
    _expect_equal(errors, "kernel manifest_version", kernel.get("manifest_version"), 1)
    _expect_equal(errors, "kernel date", kernel.get("date"), "2026-08-20")
    _expect_equal(errors, "kernel status", kernel.get("status"), "CLOSED_WITH_EXPLICIT_SCOPE")

    scope = kernel.get("scope")
    if not isinstance(scope, dict):
        errors.append("kernel scope must be an object")
        scope = {}
    _expect_equal(errors, "kernel scope.closed_world", scope.get("closed_world"), True)
    _expect_equal(
        errors,
        "kernel scope.semantic_reachable_state_exhaustion",
        scope.get("semantic_reachable_state_exhaustion"),
        False,
    )
    _expect_equal(errors, "kernel scope.registered_family_count", scope.get("registered_family_count"), 16)
    _expect_equal(errors, "kernel scope.registered_edge_count", scope.get("registered_edge_count"), 15)
    _expect_equal(
        errors,
        "kernel scope.future_constructor_policy",
        scope.get("future_constructor_policy"),
        "REJECT_UNTIL_REGISTERED_WITH_T2_T3_AND_T6_OBLIGATIONS",
    )

    theorems = kernel.get("kernel_theorems")
    if not isinstance(theorems, list):
        errors.append("kernel_theorems must be a list")
        theorems = []
    theorem_ids = _ids(theorems, "kernel_theorems", errors)
    _expect_equal(errors, "kernel theorem id set", set(theorem_ids), set(KERNEL_THEOREM_STATUSES))
    by_id = {item.get("id"): item for item in theorems if isinstance(item, dict)}
    for theorem_id, expected_status in KERNEL_THEOREM_STATUSES.items():
        theorem = by_id.get(theorem_id, {})
        _expect_equal(errors, f"{theorem_id}.status", theorem.get("status"), expected_status)
        _expect_nonempty_string(errors, f"{theorem_id}.statement", theorem.get("statement"))
        _expect_nonempty_string(errors, f"{theorem_id}.closure_class", theorem.get("closure_class"))
        _expect_nonempty_string_list(errors, f"{theorem_id}.does_not_claim", theorem.get("does_not_claim"))
        _expect_nonempty_string_list(errors, f"{theorem_id}.evidence", theorem.get("evidence"))
        if theorem.get("status") == "CLOSED":
            errors.append(f"{theorem_id} uses an unscoped CLOSED status")

    strong = kernel.get("legacy_strong_formulations")
    if not isinstance(strong, list):
        errors.append("legacy_strong_formulations must be a list")
        strong = []
    strong_ids = _ids(strong, "legacy_strong_formulations", errors)
    _expect_equal(errors, "legacy strong id set", set(strong_ids), LEGACY_STRONG_IDS)
    for item in strong:
        _expect_equal(
            errors,
            f"legacy {item.get('id')}.status",
            item.get("status"),
            "RESEARCH_EXTENSION_NOT_KERNEL_PREREQUISITE",
        )
        _expect_nonempty_string(errors, f"legacy {item.get('id')}.owner", item.get("owner"))

    mechanical = kernel.get("mechanical_closures")
    if not isinstance(mechanical, list):
        errors.append("mechanical_closures must be a list")
        mechanical = []
    mechanical_ids = _ids(mechanical, "mechanical_closures", errors)
    _expect_equal(errors, "mechanical closure id set", set(mechanical_ids), MECHANICAL_CLOSURE_IDS)
    for item in mechanical:
        _expect_equal(errors, f"mechanical {item.get('id')}.status", item.get("status"), "ESTABLISHED")
        _expect_nonempty_string(errors, f"mechanical {item.get('id')}.proof", item.get("proof"))

    global_status = kernel.get("global_status")
    if not isinstance(global_status, dict):
        errors.append("global_status must be an object")
        global_status = {}
    _expect_equal(
        errors,
        "global_status",
        global_status,
        {
            "T6_GLOBAL_SELECTOR_TOTALITY": "OPEN",
            "F0": "OPEN",
            "ERDOS_STRAUS_CONJECTURE": "OPEN",
        },
    )


def _audit_frontier(frontier: Mapping[str, Any], errors: list[str]) -> None:
    _expect_equal(errors, "frontier_id", frontier.get("frontier_id"), "t6_proof_frontier_v2")
    _expect_equal(errors, "frontier_version", frontier.get("frontier_version"), 2)
    _expect_equal(errors, "frontier date", frontier.get("date"), "2026-08-20")
    _expect_equal(errors, "frontier current_status", frontier.get("current_status"), "OPEN")
    _expect_nonempty_string(errors, "frontier statement_boundary", frontier.get("statement_boundary"))

    families = frontier.get("state_families")
    if not isinstance(families, list):
        errors.append("state_families must be a list")
        families = []
    family_ids = _ids(families, "state_families", errors)
    _expect_equal(errors, "state family id set", set(family_ids), EXPECTED_FAMILY_IDS)
    family_status = {
        item.get("id"): item.get("status")
        for item in families
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    _expect_equal(errors, "state family statuses", family_status, EXPECTED_FAMILY_STATUSES)

    initializer = frontier.get("initializer")
    if not isinstance(initializer, dict):
        errors.append("initializer must be an object")
        initializer = {}
    _expect_equal(errors, "initializer.status", initializer.get("status"), "ESTABLISHED")
    _expect_equal(errors, "initializer.source", initializer.get("source"), "initial_core_root")
    _expect_equal(
        errors,
        "initializer.targets",
        initializer.get("targets"),
        ["type_ii_relation_g_endpoint", "direct_terminal_leaf"],
    )
    if initializer.get("source") not in EXPECTED_FAMILY_IDS:
        errors.append(f"initializer has unknown source family: {initializer.get('source')!r}")
    initializer_targets = initializer.get("targets")
    _expect_nonempty_string_list(errors, "initializer.targets", initializer_targets)
    if isinstance(initializer_targets, list):
        unknown = sorted(set(initializer_targets) - EXPECTED_FAMILY_IDS)
        if unknown:
            errors.append(f"initializer has unknown targets: {unknown}")
        if "generic_nontrivial_marked_state" in initializer_targets:
            errors.append("initializer creates a nontrivial marked state")

    edges = frontier.get("registered_edges")
    if not isinstance(edges, list):
        errors.append("registered_edges must be a list")
        edges = []
    edge_ids = _ids(edges, "registered_edges", errors)
    _expect_equal(errors, "registered edge id set", set(edge_ids), EXPECTED_EDGE_IDS)
    for edge in edges:
        edge_id = edge.get("id")
        sources = edge.get("source_family_ids")
        targets = edge.get("target_family_ids")
        _expect_nonempty_string_list(errors, f"edge {edge_id}.source_family_ids", sources)
        _expect_nonempty_string_list(errors, f"edge {edge_id}.target_family_ids", targets)
        if isinstance(sources, list):
            unknown_sources = sorted(set(sources) - EXPECTED_FAMILY_IDS)
            if unknown_sources:
                errors.append(f"edge {edge_id} has unknown sources: {unknown_sources}")
        if isinstance(targets, list):
            unknown_targets = sorted(set(targets) - EXPECTED_FAMILY_IDS)
            if unknown_targets:
                errors.append(f"edge {edge_id} has unknown targets: {unknown_targets}")
            if "generic_nontrivial_marked_state" in targets:
                errors.append(f"edge {edge_id} creates a nontrivial marked state")
        guard_class = edge.get("guard_class")
        if guard_class not in ALLOWED_GUARD_CLASSES:
            errors.append(f"edge {edge_id} has unsupported guard_class: {guard_class!r}")
        expected_surface = EXPECTED_EDGE_SURFACE.get(edge_id)
        if expected_surface is not None:
            expected_sources, expected_targets, expected_guard = expected_surface
            _expect_equal(
                errors,
                f"edge {edge_id}.source_family_ids",
                sources,
                list(expected_sources),
            )
            _expect_equal(
                errors,
                f"edge {edge_id}.target_family_ids",
                targets,
                list(expected_targets),
            )
            _expect_equal(
                errors,
                f"edge {edge_id}.guard_class",
                guard_class,
                expected_guard,
            )

    immediate = frontier.get("closed_immediate_items")
    if not isinstance(immediate, list):
        errors.append("closed_immediate_items must be a list")
        immediate = []
    immediate_ids = _ids(immediate, "closed_immediate_items", errors)
    _expect_equal(errors, "closed immediate id set", set(immediate_ids), EXPECTED_IMMEDIATE_IDS)
    immediate_by_id = {item.get("id"): item for item in immediate if isinstance(item, dict)}
    _expect_equal(
        errors,
        "T6-M0 status",
        immediate_by_id.get("T6-M0-INITIAL-SERIALIZER", {}).get("status"),
        "ESTABLISHED",
    )
    _expect_equal(
        errors,
        "T6-M0 edge completeness",
        immediate_by_id.get("T6-M0-INITIAL-SERIALIZER", {}).get("edge_complete"),
        True,
    )
    for item_id in {
        "T6-M1-NAMED-SURFACE-INVENTORY",
        "T6-M2-CURRENT-MARK-UNREACHABILITY",
        "T6-M3-CONSTRUCTOR-ADMISSION-FIREWALL",
    }:
        item = immediate_by_id.get(item_id, {})
        _expect_equal(errors, f"{item_id}.status", item.get("status"), "ESTABLISHED")
        _expect_equal(errors, f"{item_id}.edge_complete", item.get("edge_complete"), False)
    for item_id in {
        "T6-M4-M3-Q5-PFREE-RAW-POLICY",
        "T6-M5-PBLOCK-POLICY-ELIMINATION",
        "T6-M6-CANONICAL-CHANNEL-PARTITION",
        "T6-M7-P2-RESIDUAL-ISOLATION",
    }:
        item = immediate_by_id.get(item_id, {})
        _expect_equal(errors, f"{item_id}.status", item.get("status"), "ESTABLISHED_ARITHMETIC_ONLY")
        _expect_equal(errors, f"{item_id}.edge_complete", item.get("edge_complete"), False)
        _expect_nonempty_string(errors, f"{item_id}.boundary", item.get("boundary"))

    theorems = frontier.get("frontier_theorems")
    if not isinstance(theorems, list):
        errors.append("frontier_theorems must be a list")
        theorems = []
    theorem_ids = _ids(theorems, "frontier_theorems", errors)
    _expect_equal(errors, "frontier theorem id set", set(theorem_ids), EXPECTED_FRONTIER_IDS)
    mapped_gap_ids: list[str] = []
    for theorem in theorems:
        theorem_id = theorem.get("id")
        _expect_equal(errors, f"frontier {theorem_id}.status", theorem.get("status"), "OPEN")
        _expect_nonempty_string(errors, f"frontier {theorem_id}.quantifier", theorem.get("quantifier"))
        _expect_nonempty_string_list(errors, f"frontier {theorem_id}.subgaps", theorem.get("subgaps"))
        closes = theorem.get("closes_legacy_gap_ids")
        if not isinstance(closes, list) or any(not isinstance(item, str) for item in closes):
            errors.append(f"frontier {theorem_id}.closes_legacy_gap_ids must be a string list")
        else:
            mapped_gap_ids.extend(closes)

    registry = frontier.get("legacy_gap_registry")
    if not isinstance(registry, list):
        errors.append("legacy_gap_registry must be a list")
        registry = []
    registry_ids = _ids(registry, "legacy_gap_registry", errors)
    _expect_equal(errors, "active legacy gap id set", set(registry_ids), EXPECTED_ACTIVE_LEGACY_GAPS)
    if len(mapped_gap_ids) != len(set(mapped_gap_ids)):
        errors.append("a legacy gap is assigned to more than one frontier theorem")
    _expect_equal(errors, "frontier legacy gap ownership union", set(mapped_gap_ids), EXPECTED_ACTIVE_LEGACY_GAPS)
    theorem_id_set = set(theorem_ids)
    for item in registry:
        if item.get("owner") not in theorem_id_set:
            errors.append(f"legacy gap {item.get('id')} has unknown owner {item.get('owner')!r}")
        theorem = next((candidate for candidate in theorems if candidate.get("id") == item.get("owner")), None)
        if theorem is not None and item.get("id") not in theorem.get("closes_legacy_gap_ids", []):
            errors.append(f"legacy gap {item.get('id')} registry owner disagrees with frontier theorem")

    ownership = frontier.get("family_frontier_ownership")
    if not isinstance(ownership, dict):
        errors.append("family_frontier_ownership must be an object")
        ownership = {}
    _expect_equal(errors, "family ownership key set", set(ownership), EXPECTED_FAMILY_IDS)
    valid_owners = EXPECTED_FRONTIER_IDS | EXPECTED_IMMEDIATE_IDS | {"constructor_admission_firewall", "TERMINAL"}
    for family_id, owner in ownership.items():
        if owner not in valid_owners:
            errors.append(f"family {family_id} has unknown frontier owner {owner!r}")
    for family_id, status in family_status.items():
        owner = ownership.get(family_id)
        if status == "OPEN" and owner not in EXPECTED_FRONTIER_IDS:
            errors.append(f"open family {family_id} is not owned by an open frontier theorem")
        if status == "TERMINAL" and owner != "TERMINAL":
            errors.append(f"terminal family {family_id} must be owned by TERMINAL")
        if status == "UNREACHABLE_IN_FROZEN_GRAPH" and owner != "constructor_admission_firewall":
            errors.append(f"marked family {family_id} must be owned by constructor_admission_firewall")

    process_gap = frontier.get("superseded_process_gap")
    if not isinstance(process_gap, dict):
        errors.append("superseded_process_gap must be an object")
        process_gap = {}
    _expect_equal(errors, "superseded process gap id", process_gap.get("id"), "GAP-O4-NEW-ATOMIC-OR-MARKED-FAMILY")
    _expect_equal(
        errors,
        "superseded process gap status",
        process_gap.get("status"),
        "CLOSED_FOR_FROZEN_V1_BY_ADMISSION_FIREWALL",
    )
    _expect_nonempty_string(errors, "superseded process gap reopen_trigger", process_gap.get("reopen_trigger"))
    _expect_nonempty_string_list(
        errors,
        "superseded process gap required_before_admission",
        process_gap.get("required_before_admission"),
    )

    gates = frontier.get("acceptance_gates")
    if not isinstance(gates, list):
        errors.append("acceptance_gates must be a list")
        gates = []
    gate_ids = _ids(gates, "acceptance_gates", errors)
    _expect_equal(errors, "acceptance gate id set", set(gate_ids), set(EXPECTED_GATE_STATUSES))
    gate_by_id = {item.get("id"): item.get("status") for item in gates if isinstance(item, dict)}
    _expect_equal(errors, "acceptance gate statuses", gate_by_id, EXPECTED_GATE_STATUSES)

    forbidden = frontier.get("forbidden_conclusions")
    if not isinstance(forbidden, list) or any(not isinstance(item, str) for item in forbidden):
        errors.append("forbidden_conclusions must be a string list")
    else:
        _expect_equal(errors, "forbidden conclusion set", set(forbidden), REQUIRED_FORBIDDEN_CONCLUSIONS)


def _audit_cross_manifest(kernel: Mapping[str, Any], frontier: Mapping[str, Any], errors: list[str]) -> None:
    scope = kernel.get("scope", {})
    edges = frontier.get("registered_edges", [])
    families = frontier.get("state_families", [])
    if isinstance(scope, dict) and isinstance(families, list):
        _expect_equal(
            errors,
            "kernel/frontier registered family count",
            scope.get("registered_family_count"),
            len(families),
        )
    if isinstance(scope, dict) and isinstance(edges, list):
        _expect_equal(errors, "kernel/frontier registered edge count", scope.get("registered_edge_count"), len(edges))

    kernel_global = kernel.get("global_status", {})
    if isinstance(kernel_global, dict):
        if kernel_global.get("T6_GLOBAL_SELECTOR_TOTALITY") != frontier.get("current_status"):
            errors.append("kernel and frontier disagree on T6 status")

    theorem_owners = {
        item.get("id")
        for item in frontier.get("frontier_theorems", [])
        if isinstance(item, dict)
    }
    for item in kernel.get("legacy_strong_formulations", []):
        if not isinstance(item, dict):
            continue
        owner = item.get("owner")
        if owner not in theorem_owners and owner != "constructor_admission_firewall":
            errors.append(f"legacy strong formulation {item.get('id')} has unresolved owner {owner!r}")


def _audit_original_v1_ledger(root: Path, frontier: Mapping[str, Any], errors: list[str], warnings: list[str]) -> None:
    ledger_path = root / "data" / "t6-selector-obligation-ledger-v1.json"
    if not ledger_path.exists():
        warnings.append("original v1 T6 ledger not present; skipped cross-ledger comparison")
        return
    try:
        ledger = _load_json(ledger_path)
    except ValueError as exc:
        errors.append(str(exc))
        return

    status = ledger.get("current_status")
    if not isinstance(status, dict) or status.get("t6_global_selector_totality") != "OPEN":
        errors.append("original v1 ledger no longer says T6 totality is OPEN")

    v1_families = ledger.get("state_families")
    if not isinstance(v1_families, list):
        errors.append("original v1 ledger has no state_families list")
        v1_families = []
    v1_family_ids = {
        item.get("id") for item in v1_families if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    _expect_equal(errors, "v1/v2 state-family set", v1_family_ids, EXPECTED_FAMILY_IDS)
    v1_family_statuses = {
        item.get("id"): item.get("coverage_status")
        for item in v1_families
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    _expect_equal(errors, "historical v1 family statuses", v1_family_statuses, EXPECTED_V1_FAMILY_STATUSES)

    v1_edges = ledger.get("concrete_edge_families")
    if not isinstance(v1_edges, list):
        errors.append("original v1 ledger has no concrete_edge_families list")
        v1_edges = []
    v1_edge_ids = {
        item.get("id") for item in v1_edges if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    _expect_equal(errors, "v1/v2 registered-edge set", v1_edge_ids, EXPECTED_EDGE_IDS)

    for edge in v1_edges:
        if not isinstance(edge, dict):
            continue
        counterpart = next(
            (item for item in frontier.get("registered_edges", []) if item.get("id") == edge.get("id")),
            None,
        )
        if counterpart is None:
            continue
        for field in ("source_family_ids", "target_family_ids", "guard_class"):
            _expect_equal(errors, f"v1/v2 edge {edge.get('id')}.{field}", counterpart.get(field), edge.get(field))

    v1_gap_items = ledger.get("minimal_selector_gaps", [])
    if not isinstance(v1_gap_items, list):
        errors.append("original v1 ledger has no minimal_selector_gaps list")
        v1_gap_items = []
    active_v1_gaps = {
        item.get("id")
        for item in v1_gap_items
        if isinstance(item, dict)
        and item.get("status") == "OPEN"
        and item.get("id") != "GAP-O4-NEW-ATOMIC-OR-MARKED-FAMILY"
    }
    _expect_equal(errors, "v1/v2 active mathematical gap set", active_v1_gaps, EXPECTED_ACTIVE_LEGACY_GAPS)
    o4 = next(
        (
            item
            for item in v1_gap_items
            if isinstance(item, dict)
            and item.get("id") == "GAP-O4-NEW-ATOMIC-OR-MARKED-FAMILY"
        ),
        None,
    )
    if o4 is None or o4.get("status") != "OPEN":
        errors.append("historical v1 O4 process gap is missing or no longer OPEN")

    v1_gates = ledger.get("acceptance_gates")
    if not isinstance(v1_gates, list):
        errors.append("original v1 ledger has no acceptance_gates list")
        v1_gates = []
    v1_gate_statuses = {
        item.get("id"): item.get("status")
        for item in v1_gates
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    _expect_equal(errors, "historical v1 acceptance gates", v1_gate_statuses, EXPECTED_V1_GATE_STATUSES)


def _audit_repository_anchors(root: Path, errors: list[str], warnings: list[str], require_full_tree: bool) -> None:
    required_files = {
        "README.md": ["T6 Global-Selector", "T6 仍为 `OPEN`"],
        "concepts/flagship-proof-program-2026-08-16.md": ["T1", "T5", "T6"],
        "concepts/denominator-escape-state-contract.md": [
            "E1",
            "E5",
            "constructor admission firewall",
        ],
        "docs/T2-T5-full-integration-review-2026-08-17.md": [
            "T1V1_TO_T5V1_PRE_T6_KERNEL",
            "T6_GLOBAL_SELECTOR_TOTALITY",
        ],
        "docs/T6-current-progress-2026-08-17.md": ["T6-F1", "p^2", "E1--E5"],
        "docs/T6-selector-obligation-ledger-2026-08-18.md": ["OPEN", "proper-root"],
        "docs/q1-fresh-handoff-proof-package-audit-2026-08-17.md": ["manifest", "q=1"],
        "docs/pre-T6-contract-kernel-closure-2026-08-20.md": ["T1v1", "T5v1", "T6"],
        "docs/T6-proof-boundary-2026-08-20.md": ["T6-F1", "T6-F5", "L_\\omega"],
    }
    for relative, snippets in required_files.items():
        path = root / relative
        if not path.exists():
            errors.append(f"missing repository anchor: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for snippet in snippets:
            if snippet not in text:
                errors.append(f"repository anchor {relative} lacks required text: {snippet!r}")

    if require_full_tree:
        full_tree_sentinels = [
            "scripts/kb.py",
            "data/t6-selector-obligation-ledger-v1.json",
            "claims/type-I-t5-full-contract-level-global-well-foundedness.md",
            "claims/type-II-q-one-full-carrier-phase-root-entry.md",
            "claims/type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction.md",
            "reproductions/type_ii_initial_q_one_root_dispatch.py",
        ]
        missing = [relative for relative in full_tree_sentinels if not (root / relative).exists()]
        if missing:
            errors.append(f"--require-full-tree was set but the checkout is incomplete: {missing}")
    elif not (root / "scripts" / "kb.py").exists():
        warnings.append("sparse checkout detected; repository-wide kb.py validation is outside this audit run")


def audit(
    kernel: Mapping[str, Any],
    frontier: Mapping[str, Any],
    *,
    root: Path | None = None,
    require_full_tree: bool = False,
) -> AuditResult:
    """Return all manifest and optional repository-boundary audit findings."""

    errors: list[str] = []
    warnings: list[str] = []
    _audit_baseline(kernel, frontier, errors)
    _audit_kernel(kernel, errors)
    _audit_frontier(frontier, errors)
    _audit_cross_manifest(kernel, frontier, errors)
    if root is not None:
        _audit_repository_anchors(root, errors, warnings, require_full_tree)
        _audit_original_v1_ledger(root, frontier, errors, warnings)
    return AuditResult(tuple(errors), tuple(warnings))


def classify_family(frontier: Mapping[str, Any], family_id: str) -> dict[str, str]:
    """Classify one named family without asserting semantic exhaustiveness."""

    family = next(
        (
            item
            for item in frontier.get("state_families", [])
            if isinstance(item, dict) and item.get("id") == family_id
        ),
        None,
    )
    if family is None:
        return {
            "family_id": family_id,
            "classification": "UNREGISTERED_REJECTED",
            "owner": "constructor_admission_firewall",
        }

    status = str(family.get("status"))
    owner = str(frontier.get("family_frontier_ownership", {}).get(family_id, "UNASSIGNED"))
    if status == "TERMINAL":
        classification = "TERMINAL"
    elif status.startswith("CLOSED_BY_") or status == "UNREACHABLE_IN_FROZEN_GRAPH":
        classification = "CLOSED_LOCAL"
    elif status in {"RELATIVE_EDGE_ONLY", "LOCAL_EDGE_ONLY", "OPEN"}:
        classification = "T6_FRONTIER"
    else:
        classification = "INVALID_STATUS"
    return {"family_id": family_id, "classification": classification, "owner": owner}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=_default_root(), help="repository root")
    parser.add_argument(
        "--kernel",
        type=Path,
        default=None,
        help="pre-T6 kernel manifest (default: ROOT/data/pre-t6-contract-kernel-v1.json)",
    )
    parser.add_argument(
        "--frontier",
        type=Path,
        default=None,
        help="T6 frontier manifest (default: ROOT/data/t6-proof-frontier-v2.json)",
    )
    parser.add_argument(
        "--require-full-tree",
        action="store_true",
        help="fail unless a complete repository checkout is available",
    )
    parser.add_argument("--family", help="print the frozen-graph classification of one family")
    parser.add_argument("--json", action="store_true", help="emit the audit result as JSON")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    root = args.root.resolve()
    kernel_path = (args.kernel or root / "data" / "pre-t6-contract-kernel-v1.json").resolve()
    frontier_path = (args.frontier or root / "data" / "t6-proof-frontier-v2.json").resolve()

    try:
        kernel = _load_json(kernel_path)
        frontier = _load_json(frontier_path)
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2

    if args.family:
        print(json.dumps(classify_family(frontier, args.family), ensure_ascii=False, indent=2))
        return 0

    result = audit(kernel, frontier, root=root, require_full_tree=args.require_full_tree)
    payload = {
        "ok": result.ok,
        "baseline_commit": BASELINE_COMMIT,
        "kernel_sha256": _sha256(kernel_path),
        "frontier_sha256": _sha256(frontier_path),
        "registered_family_count": len(frontier.get("state_families", [])),
        "registered_edge_count": len(frontier.get("registered_edges", [])),
        "closed_immediate_count": len(frontier.get("closed_immediate_items", [])),
        "active_legacy_mathematical_gap_count": len(frontier.get("legacy_gap_registry", [])),
        "open_frontier_theorem_count": len(frontier.get("frontier_theorems", [])),
        "errors": list(result.errors),
        "warnings": list(result.warnings),
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if result.ok:
            print(
                "PASS: frozen pre-T6 kernel and T6 proof boundary are structurally consistent "
                f"({payload['registered_family_count']} families, "
                f"{payload['registered_edge_count']} edges, "
                f"{payload['closed_immediate_count']} immediate items, "
                f"{payload['active_legacy_mathematical_gap_count']} active mathematical gaps, "
                f"{payload['open_frontier_theorem_count']} open frontier theorems)."
            )
            print(f"baseline: {BASELINE_COMMIT}")
            print(f"kernel sha256:   {payload['kernel_sha256']}")
            print(f"frontier sha256: {payload['frontier_sha256']}")
        else:
            print("FAIL: pre-T6/T6 boundary audit found inconsistencies", file=sys.stderr)
            for error in result.errors:
                print(f"  - {error}", file=sys.stderr)
        for warning in result.warnings:
            print(f"WARNING: {warning}", file=sys.stderr)
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
