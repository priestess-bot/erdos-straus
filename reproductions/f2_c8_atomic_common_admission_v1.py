#!/usr/bin/env python3
"""Describe, but do not emulate, common admission for H4/c8 atomic targets.

The shared F1 producer registry is coordinator-owned. A track-local mapping or
caller-provided evidence cannot grant a queue right, so this module returns a
projection proposal only.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

from f2_c8_atomic_pending_target_v1 import (
    AtomicDisposition,
    AtomicPendingTargetV1,
    AtomicProtocolError,
    Disposition,
    canonical_charged_n7,
)


TARGET_OWNER = "type_i_a_gt_one_overflow_residual"
PRODUCER_BY_ARM = {
    "H4_A1": (
        "f2_h4_fused_atomic_final_target_v1",
        "h4_fused_atomic_final_target",
        "type_i_full_carrier_post_g",
    ),
    "C8_DOUBLE_LOW": (
        "f2_c8_double_low_final_target_v1",
        "c8_double_low_final_target",
        "c8_terminal_first_surviving_parent",
    ),
}


@dataclass(frozen=True)
class AtomicAdmissionProposal:
    status: str
    required_producer_id: str
    required_branch_id: str
    required_source_owner: str
    required_target_owner: str
    target_fiber: str
    target_n7: tuple[int, ...]
    required_evidence: tuple[str, ...]
    facts: dict[str, Any]


def required_producer(arm: str) -> tuple[str, str, str]:
    try:
        return PRODUCER_BY_ARM[arm]
    except KeyError as exc:
        raise AtomicProtocolError("UNSUPPORTED_ATOMIC_ARM", arm) from exc


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
            "final target must prove A>1 and R>p before projection",
        )
    return {
        "major_phase": "TYPEI",
        "type_i_protocol": "CHARGED",
        "t5_eta_p": 0,
        "pre_a": None,
        "absorb_m": None,
        "absorb_r_epsilon": 0,
        "reset_carrier": None,
        "endpoint_fiber": "NONE",
        "relation_q": None,
        "provenance_kind": "OVERFLOW",
        "full_carrier_scope": False,
        "atomic_arm": "NONE",
        "dispatch_status": "NONE",
        "proper_root_k": None,
        "proper_root_height_class": "NONE",
        "proper_root_height": None,
        "is_overflow": True,
        "support_A": chart.support,
        "carrier_M": None,
        "overflow_d": None,
        "chart_R": chart.residual,
        "chart_K": chart.carrier,
        "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }


def propose_final_target(
    pending: AtomicPendingTargetV1,
    disposition: AtomicDisposition,
    *,
    target_n7_potential: Sequence[int],
) -> AtomicAdmissionProposal:
    """Return requirements for a future shared admission, never an accept."""
    if disposition.disposition not in {
        Disposition.F_SUCCESSOR,
        Disposition.G_SUCCESSOR,
    }:
        raise AtomicProtocolError(
            "NOT_A_NONTERMINAL_DISPOSITION", disposition.disposition.value
        )
    target_rank = tuple(target_n7_potential)
    if target_rank != canonical_charged_n7(pending.chart):
        raise AtomicProtocolError(
            "N7_TARGET_MISMATCH", "target potential does not replay from its chart"
        )
    if target_rank >= pending.parent_n7_potential:
        raise AtomicProtocolError(
            "N7_NOT_STRICT", "parent-to-final target is not a strict N7 decrease"
        )
    producer_id, branch_id, source_owner = required_producer(
        pending.atomic_grammar_arm
    )
    return AtomicAdmissionProposal(
        status="PROPOSAL_NOT_ACTIVE_SHARED_ADMISSION_REQUIRED",
        required_producer_id=producer_id,
        required_branch_id=branch_id,
        required_source_owner=source_owner,
        required_target_owner=TARGET_OWNER,
        target_fiber=disposition.fiber_kind.value if disposition.fiber_kind else "UNKNOWN",
        target_n7=target_rank,
        required_evidence=(
            "admitted_parent_trace",
            "complete_terminal_first_miss_receipt",
            "source_specific_E1_E4_receipts",
            "shared_producer_registry_entry",
            "shared_common_gate_acceptance",
            "downstream_owner_totality",
        ),
        facts=_target_facts(pending),
    )


def admit_final_target(*_args: object, **_kwargs: object) -> None:
    """Fail closed until the coordinator installs a shared producer rule."""
    raise AtomicProtocolError(
        "SHARED_ADMISSION_NOT_INSTALLED",
        "a track-local proposal cannot invoke the common persistent queue gate",
    )


__all__ = [
    "AtomicAdmissionProposal",
    "PRODUCER_BY_ARM",
    "TARGET_OWNER",
    "admit_final_target",
    "n7_charged_potential",
    "propose_final_target",
    "required_producer",
]
