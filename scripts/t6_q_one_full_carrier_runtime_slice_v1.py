#!/usr/bin/env python3
"""Executable q=1 root-to-final runtime slice with explicit open boundary.

This module binds only the initial q=1 G endpoint, the established
full-carrier handoff, and the root-to-second-anchor checkpoint contraction.
It deliberately has no route for the final target, so it is evidence for a
real producer slice rather than a T6 totality implementation.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import sys
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / "reproductions", ROOT / "scripts"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import t6_persistent_selector_runtime_v1 as runtime  # noqa: E402
import type_ii_q_one_full_carrier_phase_root_entry as q_one  # noqa: E402
import type_ii_q_one_odd_low_final_third_anchor_contraction as third_anchor  # noqa: E402
import type_ii_q_one_full_carrier_root_second_anchor_contraction as contraction  # noqa: E402
import type_ii_q_one_type_i_carrier_rail_dispatch as rail  # noqa: E402


CONTRACT = runtime.state_contract

INITIALIZER_ID = "initial_q_one_root_runtime_v1"
INITIALIZER_BRANCH = "q_one_g_endpoint"
PHASE_ROOT_PRODUCER = "q_one_g_full_carrier_runtime_v1"
PHASE_ROOT_BRANCH = "q_one_g_to_full_carrier"
CONTRACTION_PRODUCER = "q_one_root_second_anchor_runtime_v1"
CONTRACTION_BRANCH = "q_one_root_to_second_anchor_final"

Q1_SOURCE_SCHEDULE = "q_one_gap_three_then_odd_low_gap_seven_v1"
ROOT_SINK_SCHEDULE = "q_one_full_carrier_anchor_sink_v1"
ROOT_TARGET_SCHEDULE = "q_one_full_carrier_target_sink_v1"
FINAL_TARGET_SCHEDULE = "q_one_second_anchor_final_sink_v1"
ANCHOR_TERMINAL_VERIFIER = "q_one_anchor_sink_terminal_v1"


def _facts_base() -> dict[str, Any]:
    return {
        "major_phase": "TYPEII_G_HANDOFF",
        "type_i_protocol": None,
        "t5_eta_p": 0,
        "pre_a": None,
        "absorb_m": None,
        "absorb_r_epsilon": 0,
        "reset_carrier": None,
        "endpoint_fiber": "G",
        "relation_q": 1,
        "provenance_kind": "ORDINARY_ENDPOINT",
        "full_carrier_scope": False,
        "atomic_arm": "NONE",
        "dispatch_status": "NONE",
        "proper_root_k": None,
        "proper_root_height_class": "NONE",
        "proper_root_height": None,
        "proper_root_r": None,
        "is_overflow": False,
        "support_A": None,
        "carrier_M": None,
        "overflow_d": None,
        "chart_R": None,
        "chart_K": None,
        "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }


def _mark_receipt(prime: int) -> dict[str, Any]:
    return CONTRACT.seal_receipt_v1(
        {
            "schema_id": CONTRACT.MARK_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": f"q1-root-sol:{prime}",
            "kind": CONTRACT.ROOT_SOL,
            "root_context": prime,
            "equation_rank": prime,
        }
    )


def _terminal_receipt(prime: int, scope: str) -> dict[str, Any]:
    return CONTRACT.seal_receipt_v1(
        {
            "schema_id": CONTRACT.TERMINAL_FIRST_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": f"{scope}:{prime}:miss",
            "scope": scope,
            "outcome": "MISS",
        }
    )


def _q_one_g_raw_state(prime: int) -> dict[str, Any]:
    """Build the nonterminal initializer output only after exact gap-3 miss."""
    endpoint = q_one.q_one_g_endpoint(prime)
    facts = _facts_base()
    terminal = _terminal_receipt(prime, Q1_SOURCE_SCHEDULE)
    source = CONTRACT.seal_receipt_v1(
        {
            "schema_id": CONTRACT.INITIALIZER_RECEIPT_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": f"q1-initializer:{prime}",
            "producer_id": INITIALIZER_ID,
            "branch_id": INITIALIZER_BRANCH,
            "root_context": prime,
            "equation_rank": prime,
            "target_facts_digest": CONTRACT.canonical_digest_v1(facts),
            "terminal_first_digest": terminal["digest"],
            "status": "NONTERMINAL_INITIALIZER_OUTPUT",
        }
    )
    raw = {
        "schema_id": CONTRACT.STATE_SCHEMA_ID,
        "schema_version": CONTRACT.STATE_SCHEMA_VERSION,
        "state_id": "pending",
        "artifact_class": "persistent_state",
        "consumer": "t6_selector",
        "queue_gate": CONTRACT.ROOT_INITIALIZER_OUTPUT,
        "producer_id": INITIALIZER_ID,
        "branch_id": INITIALIZER_BRANCH,
        "parent_state_id": None,
        "root_context": prime,
        "equation_rank": prime,
        "mark": _mark_receipt(prime),
        "terminal_first": terminal,
        "source_receipt": source,
        "facts": facts,
    }
    raw["state_id"] = CONTRACT.build_state_id_v1(raw)
    if endpoint["endpoint"]["q"] != 1:
        raise AssertionError("q=1 initializer endpoint changed")
    return raw


def initial_dispatch(prime: int) -> dict[str, Any]:
    """Return an initial terminal or the exact q=1 G initializer state."""
    if not (rail.is_prime(prime) and prime % 24 == 1):
        raise ValueError("initial dispatch requires a core prime")
    x = (prime + 3) // 4
    factors = rail.factorization(x)
    terminal_factors = sorted(q for q in factors if q % 3 == 2)
    if not terminal_factors:
        if prime % 336 == 265:
            gap = 7
            divisor = 2
            gap_x = (prime + gap) // 4
            y = prime * (gap_x + divisor) // gap
            z = prime * (gap_x + gap_x * gap_x // divisor) // gap
            if not (
                4 * gap_x == prime + gap
                and gap_x % 2 == 0
                and gap_x % gap == 5
                and (gap_x + divisor) % gap == 0
                and (gap_x + gap_x * gap_x // divisor) % gap == 0
                and sum((Fraction(1, value) for value in (gap_x, y, z)), Fraction())
                == Fraction(4, prime)
            ):
                raise AssertionError("odd-low gap-7 preemption changed")
            return {
                "kind": "terminal",
                "certificate": {
                    "type": "TYPEII_GAP_SEVEN_ODD_LOW_PREEMPTION",
                    "prime": prime,
                    "factor": divisor,
                    "denominators": (gap_x, y, z),
                },
            }
        return {"kind": "q_one_g", "raw_state": _q_one_g_raw_state(prime)}
    divisor = terminal_factors[0]
    y = prime * (x + divisor) // 3
    z = prime * (x + x * x // divisor) // 3
    if not (
        x % divisor == 0
        and (x + divisor) % 3 == 0
        and (x + x * x // divisor) % 3 == 0
        and sum((Fraction(1, value) for value in (x, y, z)), Fraction())
        == Fraction(4, prime)
    ):
        raise AssertionError("q=1 initial terminal reconstruction changed")
    return {
        "kind": "terminal",
        "certificate": {
            "type": "TYPEII_GAP_THREE",
            "prime": prime,
            "factor": divisor,
            "denominators": (x, y, z),
        },
    }


def _anchor_sink_draft(prime: int, chart_r: int, chart_k: int) -> runtime.TerminalDraftV1 | None:
    """Serialize the exact full-excess anchor terminal when it exists."""
    anchor = chart_r - 1
    if chart_k % anchor:
        return None
    denominators = tuple(sorted((chart_k // anchor, chart_k, prime * chart_k)))
    if sum((Fraction(1, value) for value in denominators), Fraction()) != Fraction(4, prime):
        raise AssertionError("anchor sink serializer changed")
    return runtime.TerminalDraftV1(
        verifier_id=ANCHOR_TERMINAL_VERIFIER,
        certificate_payload={
            "type": "TYPEI_ANCHOR_SINK",
            "prime": prime,
            "R": chart_r,
            "K": chart_k,
            "denominators": denominators,
        },
        lift_evidence_id="identity: Sol(p) -> Sol(p)",
    )


def _checkpoint_miss_record(
    prime: int, chart_r: int, chart_k: int, scope: str
) -> dict[str, str]:
    """Seal the macro-internal anchor check without making it a queue state."""
    if _anchor_sink_draft(prime, chart_r, chart_k) is not None:
        raise AssertionError("a checkpoint terminal must preempt the contraction")
    payload = {
        "schema_id": "q1_checkpoint_anchor_terminal_miss_v1",
        "schema_version": 1,
        "scope": scope,
        "prime": prime,
        "R": chart_r,
        "K": chart_k,
        "outcome": "MISS",
    }
    return {
        "scope": payload["scope"],
        "digest": runtime.canonical_digest_v1(payload),
    }


def _contraction_macro(prime: int) -> dict[str, Any]:
    """Return the final target after all nonpersistent q=1 checkpoints."""
    second = contraction.root_second_anchor_contraction(prime)
    second_final = second["final_target"]
    checkpoints: dict[str, Any] = {
        "first_child": second["checkpoints"]["first_child"],
        "second_anchor_high_determinant": second["checkpoints"][
            "second_anchor_high_determinant"
        ],
    }
    final = {
        "R": second_final["R"],
        "K": second_final["K"],
        "support": second_final["support"],
        "ticket": second_final["ticket"],
        "provenance_kind": second_final["facts"]["provenance_kind"],
    }
    mode = "second_anchor_final"
    if prime % 336 == 25:
        third = third_anchor.low_checkpoint_to_c9(prime)
        checkpoints["odd_low_final"] = {
            "R": second_final["R"],
            "K": second_final["K"],
            "support": second_final["support"],
        }
        checkpoints["third_anchor"] = third["low_checkpoint"]
        final = {
            "R": third["final_high"]["R"],
            "K": third["final_high"]["K"],
            "support": third["final_high"]["support"],
            "ticket": "LOCAL_DROP",
            "provenance_kind": "OVERFLOW",
        }
        mode = "second_anchor_then_c9"
    return {
        "prime": prime,
        "t": second["t"],
        "mode": mode,
        "checkpoints": checkpoints,
        "final_target": final,
    }


def _contraction_witness(prime: int, receipt: Mapping[str, Any]) -> dict[str, Any]:
    """Bind all nonpersistent checkpoint arithmetic into the runtime candidate."""
    child = receipt["checkpoints"]["first_child"]
    checkpoint_misses = [
        _checkpoint_miss_record(
            prime,
            int(child["R"]),
            int(child["K"]),
            "q1_first_child_anchor_sink",
        )["digest"]
    ]
    low_checkpoint = receipt["checkpoints"].get("odd_low_final")
    if isinstance(low_checkpoint, Mapping):
        checkpoint_misses.append(
            _checkpoint_miss_record(
                prime,
                int(low_checkpoint["R"]),
                int(low_checkpoint["K"]),
                "q1_odd_low_final_anchor_sink",
            )["digest"]
        )
    material = {
        "prime": prime,
        "t": receipt["t"],
        "mode": receipt["mode"],
        "checkpoints": receipt["checkpoints"],
        "final_target": receipt["final_target"],
    }
    return {
        "prime": prime,
        "macro": receipt["mode"],
        "t": receipt["t"],
        "checkpoint_terminal_misses": checkpoint_misses,
        "macro_replay_digest": runtime.canonical_digest_v1(material),
    }


def _miss(schedule_id: str, scope: str, evidence_id: str) -> runtime.TerminalMissV1:
    return runtime.TerminalMissV1(
        schedule_id=schedule_id,
        scope=scope,
        evidence_id=evidence_id,
    )


def _q_one_source_schedule(source: runtime.SourceExecutionContextV1) -> runtime.TargetTerminalOutputV1:
    prime = source.header.root_context
    facts = source.header.facts
    raw_terminal = source.raw_state["terminal_first"]
    endpoint = q_one.q_one_g_endpoint(prime)
    if not (
        source.owner == "type_ii_relation_g_endpoint"
        and facts["major_phase"] == "TYPEII_G_HANDOFF"
        and facts["relation_q"] == 1
        and facts["endpoint_fiber"] == "G"
        and raw_terminal["scope"] == Q1_SOURCE_SCHEDULE
        and raw_terminal["outcome"] == "MISS"
        and prime % 336 != 265
        and endpoint["endpoint"]["first_denominator"] == (prime + 3) // 4
    ):
        raise runtime.RuntimeContractError(
            runtime.RuntimeRejectCode.TERMINAL_RESULT_INVALID,
            "q=1 source does not replay the declared gap-3 miss",
        )
    return _miss(Q1_SOURCE_SCHEDULE, Q1_SOURCE_SCHEDULE, f"q1-gap3-miss:{prime}")


def _anchor_source_schedule(source: runtime.SourceExecutionContextV1) -> runtime.TargetTerminalOutputV1:
    facts = source.header.facts
    chart_r, chart_k = facts["chart_R"], facts["chart_K"]
    if not isinstance(chart_r, int) or not isinstance(chart_k, int):
        raise runtime.RuntimeContractError(
            runtime.RuntimeRejectCode.TERMINAL_RESULT_INVALID,
            "anchor scheduler needs a chart",
        )
    draft = _anchor_sink_draft(source.header.root_context, chart_r, chart_k)
    if draft is not None:
        return draft
    return _miss(ROOT_SINK_SCHEDULE, "full_carrier_anchor_sink", f"anchor-miss:{source.state_id}")


def _anchor_target_schedule(
    schedule_id: str, scope: str
) -> runtime.TargetTerminalSchedulerV1:
    def schedule(
        projection: runtime.TargetProjectionV1, witness: Mapping[str, Any]
    ) -> runtime.TargetTerminalOutputV1:
        del witness
        chart_r, chart_k = projection.facts["chart_R"], projection.facts["chart_K"]
        if not isinstance(chart_r, int) or not isinstance(chart_k, int):
            raise runtime.RuntimeContractError(
                runtime.RuntimeRejectCode.TERMINAL_RESULT_INVALID,
                "target anchor scheduler needs a chart",
            )
        draft = _anchor_sink_draft(projection.root_context, chart_r, chart_k)
        if draft is not None:
            return draft
        return _miss(schedule_id, scope, f"{scope}-miss:{projection.root_context}:{chart_r}")

    return schedule


def _root_facts(prime: int) -> dict[str, Any]:
    t = (prime - 1) // 24
    x = 6 * t + 1
    facts = _facts_base()
    facts.update(
        {
            "major_phase": "TYPEI",
            "type_i_protocol": "CHARGED",
            "endpoint_fiber": "NONE",
            "relation_q": None,
            "provenance_kind": "FULL_CARRIER_POST_G",
            "full_carrier_scope": True,
            "support_A": 1,
            "chart_R": 16 * t + 3,
            "chart_K": x * (16 * t + 1),
        }
    )
    return facts


def _final_facts(prime: int) -> tuple[dict[str, Any], runtime.T5StateDescriptorV1, str]:
    receipt = _contraction_macro(prime)
    final = receipt["final_target"]
    target_r, target_k, support = final["R"], final["K"], final["support"]
    if not all(isinstance(value, int) for value in (target_r, target_k, support)):
        raise AssertionError("contraction target lost integer chart fields")
    facts = _facts_base()
    facts.update(
        {
            "major_phase": "TYPEI",
            "endpoint_fiber": "NONE",
            "relation_q": None,
            "full_carrier_scope": True,
            "support_A": support,
            "chart_R": target_r,
            "chart_K": target_k,
        }
    )
    ticket = str(final["ticket"])
    if final["provenance_kind"] == "OVERFLOW":
        facts.update(
            {
                "type_i_protocol": "CHARGED",
                "provenance_kind": "OVERFLOW",
                "is_overflow": True,
                "carrier_M": support,
            }
        )
        descriptor = runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="CHARGED",
            eta_p=0,
        )
    else:
        facts.update(
            {
                "type_i_protocol": "ABSORB",
                "provenance_kind": "MARKED_ABSORB",
                "absorb_m": 1,
                "absorb_r_epsilon": 1,
            }
        )
        descriptor = runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="ABSORB",
            absorb_m=1,
            absorb_r_epsilon=1,
        )
    return facts, descriptor, ticket


def _phase_root_executor(
    source: runtime.SourceExecutionContextV1, branch_id: str
) -> runtime.ProducerOutputV1:
    if branch_id != PHASE_ROOT_BRANCH:
        return runtime.GuardMissV1("UNKNOWN_BRANCH", branch_id)
    prime = source.header.root_context
    return runtime.CandidateTransitionV1(
        producer_id=PHASE_ROOT_PRODUCER,
        branch_id=branch_id,
        witness_payload={"prime": prime, "q": 1, "root_formula": "full_carrier"},
        ticket_type="PHASE_DROP",
    )


def _contraction_executor(
    source: runtime.SourceExecutionContextV1, branch_id: str
) -> runtime.ProducerOutputV1:
    if branch_id != CONTRACTION_BRANCH:
        return runtime.GuardMissV1("UNKNOWN_BRANCH", branch_id)
    prime = source.header.root_context
    receipt = _contraction_macro(prime)
    final = receipt["final_target"]
    return runtime.CandidateTransitionV1(
        producer_id=CONTRACTION_PRODUCER,
        branch_id=branch_id,
        witness_payload=_contraction_witness(prime, receipt),
        ticket_type=str(final["ticket"]),
    )


def _phase_root_projector(
    source: runtime.SourceExecutionContextV1, candidate: runtime.CandidateTransitionV1
) -> runtime.TargetProjectionV1:
    prime = source.header.root_context
    if candidate.witness_payload != {"prime": prime, "q": 1, "root_formula": "full_carrier"}:
        raise runtime.RuntimeContractError(
            runtime.RuntimeRejectCode.PROJECTOR_OUTPUT_INVALID,
            "phase-root witness payload does not replay",
        )
    facts = _root_facts(prime)
    return runtime.TargetProjectionV1(
        root_context=prime,
        equation_rank=prime,
        facts=facts,
        t5=runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="CHARGED",
            eta_p=0,
        ),
        mark_behavior=runtime.IDENTITY_MARK,
    )


def _contraction_projector(
    source: runtime.SourceExecutionContextV1, candidate: runtime.CandidateTransitionV1
) -> runtime.TargetProjectionV1:
    prime = source.header.root_context
    receipt = _contraction_macro(prime)
    if candidate.witness_payload != _contraction_witness(prime, receipt):
        raise runtime.RuntimeContractError(
            runtime.RuntimeRejectCode.PROJECTOR_OUTPUT_INVALID,
            "contraction witness payload does not replay",
        )
    facts, descriptor, ticket = _final_facts(prime)
    if candidate.ticket_type != ticket:
        raise runtime.RuntimeContractError(
            runtime.RuntimeRejectCode.PROJECTOR_OUTPUT_INVALID,
            "contraction ticket does not replay",
        )
    return runtime.TargetProjectionV1(
        root_context=prime,
        equation_rank=prime,
        facts=facts,
        t5=descriptor,
        mark_behavior=runtime.IDENTITY_MARK,
    )


def _phase_root_validator(
    source: runtime.SourceExecutionContextV1,
    candidate: runtime.CandidateTransitionV1,
    projection: runtime.TargetProjectionV1,
) -> runtime.TransitionValidationV1:
    prime = source.header.root_context
    endpoint = q_one.q_one_g_endpoint(prime)
    facts = projection.facts
    t = (prime - 1) // 24
    e1 = bool(
        source.owner == "type_ii_relation_g_endpoint"
        and source.header.facts["relation_q"] == 1
        and endpoint["endpoint"]["first_denominator"] == 6 * t + 1
    )
    e2 = bool(facts["chart_R"] == 16 * t + 3 and facts["chart_K"] == (6 * t + 1) * (16 * t + 1))
    e3 = bool(
        facts["provenance_kind"] == "FULL_CARRIER_POST_G"
        and facts["full_carrier_scope"]
        and facts["support_A"] == 1
        and 4 * facts["chart_K"] == prime * facts["chart_R"] + 1
    )
    e4 = source.header.mark_kind == CONTRACT.ROOT_SOL
    return runtime.TransitionValidationV1(
        source_state_id=source.state_id,
        producer_id=candidate.producer_id,
        branch_id=candidate.branch_id,
        projection_digest=runtime.PersistentSelectorRuntimeV1._projection_digest_v1(projection),
        E1=e1,
        E2=e2,
        E3_pre_admission=e3,
        E4=e4,
        evidence_ids=(
            "claim:type-II-initial-q-one-root-terminal-or-full-carrier-dispatch",
            "claim:type-II-q-one-full-carrier-phase-root-entry",
        ),
    )


def _contraction_validator(
    source: runtime.SourceExecutionContextV1,
    candidate: runtime.CandidateTransitionV1,
    projection: runtime.TargetProjectionV1,
) -> runtime.TransitionValidationV1:
    prime = source.header.root_context
    receipt = _contraction_macro(prime)
    root_facts = source.header.facts
    final = receipt["final_target"]
    e1 = bool(
        source.owner == "type_i_full_carrier_post_g"
        and root_facts["chart_R"] == 16 * ((prime - 1) // 24) + 3
        and candidate.witness_payload == _contraction_witness(prime, receipt)
    )
    e2 = bool(
        projection.facts["chart_R"] == final["R"]
        and projection.facts["chart_K"] == final["K"]
        and projection.facts["support_A"] == final["support"]
    )
    e3 = bool(
        4 * projection.facts["chart_K"]
        == prime * projection.facts["chart_R"] + 1
        and projection.facts["chart_K"] % projection.facts["support_A"] == 0
        and projection.facts["provenance_kind"] == final["provenance_kind"]
    )
    e4 = source.header.mark_kind == CONTRACT.ROOT_SOL
    return runtime.TransitionValidationV1(
        source_state_id=source.state_id,
        producer_id=candidate.producer_id,
        branch_id=candidate.branch_id,
        projection_digest=runtime.PersistentSelectorRuntimeV1._projection_digest_v1(projection),
        E1=e1,
        E2=e2,
        E3_pre_admission=e3,
        E4=e4,
        evidence_ids=(
            "claim:type-II-q-one-full-carrier-root-second-anchor-contraction",
            "claim:type-II-q-one-odd-low-final-third-anchor-contraction",
        ),
    )


def _verify_anchor_terminal(
    source: runtime.SourceExecutionContextV1,
    payload: Mapping[str, Any],
    lift_evidence_id: str,
) -> bool:
    if lift_evidence_id != "identity: Sol(p) -> Sol(p)":
        return False
    try:
        prime = int(payload["prime"])
        chart_r = int(payload["R"])
        chart_k = int(payload["K"])
        denominators = tuple(int(value) for value in payload["denominators"])
    except (KeyError, TypeError, ValueError):
        return False
    return bool(
        payload.get("type") == "TYPEI_ANCHOR_SINK"
        and prime == source.header.root_context
        and len(denominators) == 3
        and all(value > 0 for value in denominators)
        and chart_k % (chart_r - 1) == 0
        and denominators == tuple(sorted((chart_k // (chart_r - 1), chart_k, prime * chart_k)))
        and sum((Fraction(1, value) for value in denominators), Fraction()) == Fraction(4, prime)
    )


def build_runtime() -> runtime.PersistentSelectorRuntimeV1:
    phase_root_branch = runtime.BranchRegistrationV1(
        branch_id=PHASE_ROOT_BRANCH,
        source_owners=frozenset({"type_ii_relation_g_endpoint"}),
        target_owners=frozenset({"type_i_full_carrier_post_g"}),
        evidence_refs=(
            "claim:type-II-initial-q-one-root-terminal-or-full-carrier-dispatch",
            "claim:type-II-q-one-full-carrier-phase-root-entry",
        ),
        allowed_tickets=frozenset({"PHASE_DROP"}),
        projector_id="q1.phase_root.projector",
        transition_validator_id="q1.phase_root.validator",
        source_terminal_schedule_id=Q1_SOURCE_SCHEDULE,
        target_terminal_schedule_id=ROOT_TARGET_SCHEDULE,
        terminal_verifier_ids=frozenset({ANCHOR_TERMINAL_VERIFIER}),
    )
    contraction_branch = runtime.BranchRegistrationV1(
        branch_id=CONTRACTION_BRANCH,
        source_owners=frozenset({"type_i_full_carrier_post_g"}),
        target_owners=frozenset(
            {"type_i_a_gt_one_overflow_residual", "type_i_absorb_marked_residual"}
        ),
        evidence_refs=(
            "claim:type-II-q-one-full-carrier-root-second-anchor-contraction",
            "claim:type-II-q-one-odd-low-final-third-anchor-contraction",
        ),
        allowed_tickets=frozenset({"LOCAL_DROP", "PHASE_DROP"}),
        projector_id="q1.contraction.projector",
        transition_validator_id="q1.contraction.validator",
        source_terminal_schedule_id=ROOT_SINK_SCHEDULE,
        target_terminal_schedule_id=FINAL_TARGET_SCHEDULE,
        terminal_verifier_ids=frozenset({ANCHOR_TERMINAL_VERIFIER}),
    )
    return runtime.PersistentSelectorRuntimeV1(
        initializer=runtime.InitializerRegistrationV1(
            producer_id=INITIALIZER_ID,
            branch_ids=frozenset({INITIALIZER_BRANCH}),
            target_owners=frozenset({"type_ii_relation_g_endpoint"}),
        ),
        producers=(
            runtime.ProducerRegistrationV1(
                producer_id=PHASE_ROOT_PRODUCER,
                implementation_ref=__name__ + ":_phase_root_executor",
                branches=(phase_root_branch,),
            ),
            runtime.ProducerRegistrationV1(
                producer_id=CONTRACTION_PRODUCER,
                implementation_ref=__name__ + ":_contraction_executor",
                branches=(contraction_branch,),
            ),
        ),
        executors={
            PHASE_ROOT_PRODUCER: _phase_root_executor,
            CONTRACTION_PRODUCER: _contraction_executor,
        },
        projectors={
            "q1.phase_root.projector": _phase_root_projector,
            "q1.contraction.projector": _contraction_projector,
        },
        transition_validators={
            "q1.phase_root.validator": _phase_root_validator,
            "q1.contraction.validator": _contraction_validator,
        },
        source_terminal_schedulers={
            Q1_SOURCE_SCHEDULE: _q_one_source_schedule,
            ROOT_SINK_SCHEDULE: _anchor_source_schedule,
        },
        target_terminal_schedulers={
            ROOT_TARGET_SCHEDULE: _anchor_target_schedule(
                ROOT_TARGET_SCHEDULE, "full_carrier_anchor_sink"
            ),
            FINAL_TARGET_SCHEDULE: _anchor_target_schedule(
                FINAL_TARGET_SCHEDULE, "second_anchor_final_sink"
            ),
        },
        terminal_verifiers={ANCHOR_TERMINAL_VERIFIER: _verify_anchor_terminal},
        dispatch_precedence={
            "type_ii_relation_g_endpoint": (
                runtime.DispatchEntryV1(PHASE_ROOT_PRODUCER, PHASE_ROOT_BRANCH),
            ),
            "type_i_full_carrier_post_g": (
                runtime.DispatchEntryV1(CONTRACTION_PRODUCER, CONTRACTION_BRANCH),
            ),
        },
    )


def run_q_one_runtime_slice(prime: int) -> dict[str, Any]:
    """Run the finite slice and expose the deliberately open final target."""
    initial = initial_dispatch(prime)
    if initial["kind"] == "terminal":
        return initial
    selector = build_runtime()
    endpoint = selector.bootstrap_nonterminal_v1(
        initial["raw_state"],
        runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEII_G_HANDOFF",
            type_i_protocol=None,
        ),
    )
    root_decision = selector.run_state_once_v1(endpoint)
    if root_decision.successor is None:
        raise AssertionError("q=1 runtime handoff did not enqueue the full-carrier root")
    root = next(
        item
        for item in selector.queue_snapshot_v1()
        if item.state_id == root_decision.successor.target_state_id
    )
    final_decision = selector.run_state_once_v1(root)
    if final_decision.successor is None:
        raise AssertionError("q=1 runtime contraction did not enqueue its final target")
    final = next(
        item
        for item in selector.queue_snapshot_v1()
        if item.state_id == final_decision.successor.target_state_id
    )
    dead_end = selector.run_state_once_v1(final)
    return {
        "kind": "runtime_slice",
        "prime": prime,
        "endpoint": endpoint,
        "root_decision": root_decision,
        "final_decision": final_decision,
        "final": final,
        "final_reentry": dead_end,
        "queue_size": len(selector.queue_snapshot_v1()),
    }


def verify() -> None:
    terminal = run_q_one_runtime_slice(97)
    if not (
        terminal["kind"] == "terminal"
        and terminal["certificate"]["denominators"] == (25, 970, 4850)
    ):
        raise AssertionError("initial q=1 terminal branch changed")
    preempted = run_q_one_runtime_slice(601)
    if not (
        preempted["kind"] == "terminal"
        and preempted["certificate"]["denominators"] == (152, 13_222, 1_004_872)
    ):
        raise AssertionError("p=601 odd-low gap-7 preemption changed")
    for prime, expected_owner, expected_ticket in (
        (73, "type_i_a_gt_one_overflow_residual", "LOCAL_DROP"),
        (1033, "type_i_a_gt_one_overflow_residual", "LOCAL_DROP"),
    ):
        result = run_q_one_runtime_slice(prime)
        final = result["final"]
        if not (
            result["kind"] == "runtime_slice"
            and result["root_decision"].successor is not None
            and result["final_decision"].successor is not None
            and final.owner == expected_owner
            and result["final_decision"].successor.t5_ticket_receipt["ticket_type"]
            == expected_ticket
            and result["queue_size"] == 3
            and not result["final_reentry"].accepted
            and result["final_reentry"].reason_code == runtime.RuntimeRejectCode.DEAD_END
        ):
            raise AssertionError(f"runtime slice changed for p={prime}")
    print("verified q=1 full-carrier runtime slice with explicit final reentry gap")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
