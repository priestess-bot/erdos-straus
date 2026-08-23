#!/usr/bin/env python3
"""Project final H4/c8 atomic F/G targets through the common F1 gate.

The producer rules in this file are an interface proposal owned by this track;
they do not mutate the shared registry.  The arithmetic theorem proves that a
target support strictly above a high checkpoint produces an ordinary Type-I
overflow chart and therefore matches the existing
``type_i_a_gt_one_overflow_residual`` owner.  The shared gate remains the
authoritative schema/owner/admission implementation.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence

from f2_c8_atomic_pending_target_v1 import (
    AtomicDisposition,
    AtomicPendingTargetV1,
    AtomicProtocolError,
    Disposition,
    finalize_successor,
)

ROOT = Path(__file__).resolve().parents[1]


def _load_common():
    path = ROOT / "scripts" / "t6_persistent_selector_state_v1.py"
    name = "t6_persistent_selector_state_v1_atomic_reentry"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


common = _load_common()


TARGET_OWNER = "type_i_a_gt_one_overflow_residual"
PRODUCER_BY_ARM = {
    "H4_A1": (
        "f2_h4_atomic_final_target_v1",
        "h4_atomic_final_target",
        frozenset({"type_i_c2_19_macro_target"}),
    ),
    "C8_DOUBLE_LOW": (
        "f2_c8_double_low_final_target_v1",
        "c8_double_low_final_target",
        frozenset({"c8_terminal_first_surviving_parent"}),
    ),
}


@dataclass(frozen=True)
class CommonAdmissionReceipt:
    raw_state: Mapping[str, Any]
    decision: common.QueueAdmissionDecisionV1
    final_successor: Mapping[str, Any]


def producer_rule(arm: str) -> common.ProducerRuleV1:
    try:
        producer_id, branch_id, source_owners = PRODUCER_BY_ARM[arm]
    except KeyError as exc:
        raise AtomicProtocolError("UNSUPPORTED_ATOMIC_ARM", arm) from exc
    return common.ProducerRuleV1(
        producer_id=producer_id,
        queue_gate=common.ADMITTED_SUCCESSOR,
        branch_ids=frozenset({branch_id}),
        source_owners=source_owners,
        target_owners=frozenset({TARGET_OWNER}),
    )


def n7_charged_potential(
    *, prime: int, support: int, capacity: int, eta_p: int = 0
) -> tuple[int, ...]:
    if eta_p < 0:
        raise AtomicProtocolError("INVALID_N7_POTENTIAL", "eta_p is negative")
    boundary = (prime - 1) ** 2 // 4
    return (prime, 2, 4, boundary // support, capacity, eta_p, 0)


def _target_facts(pending: AtomicPendingTargetV1) -> dict[str, Any]:
    chart = pending.chart
    if not (
        chart.support > 1
        and chart.residual > chart.prime
        and chart.carrier == chart.support * chart.capacity
    ):
        raise AtomicProtocolError(
            "ATOMIC_TARGET_NOT_OVERFLOW",
            "final target must prove A>1 and R>p before common admission",
        )
    return {
        "major_phase": "TYPEI",
        "endpoint_fiber": "NONE",
        "relation_q": None,
        "provenance_kind": "OVERFLOW",
        "full_carrier_scope": False,
        "atomic_arm": "NONE",
        "dispatch_status": "NONE",
        "proper_root_k": None,
        "is_overflow": True,
        "support_A": chart.support,
        "carrier_M": None,
        "overflow_d": None,
        "chart_R": chart.residual,
        "chart_K": chart.carrier,
        "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }


def _sealed_mark(prime: int) -> dict[str, Any]:
    return common.seal_receipt_v1(
        {
            "schema_id": common.MARK_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": "mark:atomic-root-sol",
            "kind": common.ROOT_SOL,
            "root_context": prime,
            "equation_rank": prime,
        }
    )


def _sealed_terminal_miss(pending: AtomicPendingTargetV1) -> dict[str, Any]:
    return common.seal_receipt_v1(
        {
            "schema_id": common.TERMINAL_FIRST_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": f"terminal:{pending.content_digest}",
            "scope": "complete_atomic_target_terminal_and_centered_hit_screen",
            "outcome": "MISS",
        }
    )


def _require_evidence(evidence: Mapping[str, str]) -> None:
    required = {"E1", "E2", "E3", "E4"}
    if set(evidence) != required or any(
        not isinstance(evidence[name], str) or not evidence[name]
        for name in required
    ):
        raise AtomicProtocolError(
            "INCOMPLETE_E1_E4_EVIDENCE", "exactly four nonempty evidence digests required"
        )


def build_raw_final_target(
    pending: AtomicPendingTargetV1,
    disposition: AtomicDisposition,
    *,
    target_n7_potential: Sequence[int],
    evidence: Mapping[str, str],
) -> tuple[dict[str, Any], common.ProducerRuleV1]:
    """Build a final persistent candidate with no pending family/dispatch field."""
    if disposition.disposition not in {
        Disposition.F_SUCCESSOR,
        Disposition.G_SUCCESSOR,
    }:
        raise AtomicProtocolError(
            "NOT_A_NONTERMINAL_DISPOSITION", disposition.disposition.value
        )
    _require_evidence(evidence)
    target_rank = tuple(target_n7_potential)
    if len(target_rank) != 7 or target_rank >= pending.parent_n7_potential:
        raise AtomicProtocolError(
            "N7_NOT_STRICT", "parent-to-final target is not a strict N7 decrease"
        )
    rule = producer_rule(pending.atomic_grammar_arm)
    producer_id, branch_id, _ = PRODUCER_BY_ARM[pending.atomic_grammar_arm]
    facts = _target_facts(pending)
    terminal = _sealed_terminal_miss(pending)
    source = common.seal_receipt_v1(
        {
            "schema_id": common.SUCCESSOR_RECEIPT_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": f"edge:{pending.content_digest}",
            "producer_id": producer_id,
            "branch_id": branch_id,
            "root_context": pending.chart.prime,
            "equation_rank": pending.chart.prime,
            "target_facts_digest": common.canonical_digest_v1(facts),
            "terminal_first_digest": terminal["digest"],
            "status": "VERIFIED_EDGE",
            "parent_state_id": pending.source_parent_id,
            "E1": True,
            "E2": True,
            "E3": True,
            "E4": True,
            "E5": True,
            "T5_ticket": pending.t5_ticket_candidate,
        }
    )
    raw = {
        "schema_id": common.STATE_SCHEMA_ID,
        "schema_version": common.STATE_SCHEMA_VERSION,
        "state_id": "pending-content-address",
        "artifact_class": "persistent_state",
        "consumer": "t6_selector",
        "queue_gate": common.ADMITTED_SUCCESSOR,
        "producer_id": producer_id,
        "branch_id": branch_id,
        "parent_state_id": pending.source_parent_id,
        "root_context": pending.chart.prime,
        "equation_rank": pending.chart.prime,
        "mark": _sealed_mark(pending.chart.prime),
        "terminal_first": terminal,
        "source_receipt": source,
        "facts": facts,
    }
    raw["state_id"] = common.build_state_id_v1(raw)
    return raw, rule


def admit_final_target(
    pending: AtomicPendingTargetV1,
    disposition: AtomicDisposition,
    *,
    target_n7_potential: Sequence[int],
    evidence: Mapping[str, str],
) -> CommonAdmissionReceipt:
    """Run the real common gate, then seal a no-pending final successor receipt."""
    raw, rule = build_raw_final_target(
        pending,
        disposition,
        target_n7_potential=target_n7_potential,
        evidence=evidence,
    )
    decision = common.reject_before_persistent_queue_v1(
        raw, {rule.producer_id: rule}
    )
    if not decision.accepted or decision.owner != TARGET_OWNER:
        code = getattr(decision.reason_code, "value", str(decision.reason_code))
        raise AtomicProtocolError(
            "COMMON_ADMISSION_REJECTED", f"{code}: {decision.detail}"
        )
    final = finalize_successor(
        pending,
        disposition,
        target_state_id=str(decision.state_id),
        target_owner=str(decision.owner),
        target_n7_potential=target_n7_potential,
        e4_lift_digest=evidence["E4"],
        reentry_verified=True,
    )
    final = dict(final)
    final["common_owner_digest"] = decision.owner_digest
    return CommonAdmissionReceipt(raw, decision, final)


__all__ = [
    "CommonAdmissionReceipt",
    "PRODUCER_BY_ARM",
    "TARGET_OWNER",
    "admit_final_target",
    "build_raw_final_target",
    "n7_charged_potential",
    "producer_rule",
]
