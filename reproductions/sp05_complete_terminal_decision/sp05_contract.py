#!/usr/bin/env python3
"""Repository-compatible contract primitives for the SP-05 proof package.

This module mirrors the public PersistentSelectorStateV1 field set, owner rule,
state-ID convention and frozen T5 coordinates used by the repository at the
pinned HEAD.  It is a standalone reproducer; it does not claim repository
issuer or queue authority.
"""
from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

PINNED_HEAD_SHA = "7dff8a9e7338814e83ab839c33b8b58c28f4ea0d"

STATE_SCHEMA_ID = "persistent_selector_state_v1"
STATE_SCHEMA_VERSION = 1
MARK_SCHEMA_ID = "selector_mark_receipt_v1"
TERMINAL_FIRST_SCHEMA_ID = "terminal_first_receipt_v1"
INITIALIZER_RECEIPT_SCHEMA_ID = "t6_initializer_nonterminal_receipt_v1"
SUCCESSOR_RECEIPT_SCHEMA_ID = "t6_admitted_successor_receipt_v1"
ROOT_INITIALIZER_OUTPUT = "ROOT_INITIALIZER_OUTPUT"
ADMITTED_SUCCESSOR = "ADMITTED_SUCCESSOR"
ROOT_SOL = "ROOT_SOL"
SOURCE_OWNER = "type_ii_relation_g_endpoint"
TARGET_OWNER = "type_i_full_carrier_post_g"
PHASE_DROP = "PHASE_DROP"

ROOT_PRODUCER_ID = "q1_root_v1_base_materializer_v1"
ROOT_BRANCH_ID = "q1_g_registered_prefix_miss_base_v1"
EDGE_PRODUCER_ID = "q1_phase_root_complete_producer_v1"
EDGE_BRANCH_ID = "q1_g_complete_miss_phase_root_v1"
REENTRY_ROUTE_ID = "q1_phase_root_body_entry_v1"

FACT_FIELDS = frozenset(
    {
        "major_phase",
        "type_i_protocol",
        "t5_eta_p",
        "pre_a",
        "absorb_m",
        "absorb_r_epsilon",
        "reset_carrier",
        "endpoint_fiber",
        "relation_q",
        "provenance_kind",
        "full_carrier_scope",
        "atomic_arm",
        "dispatch_status",
        "proper_root_k",
        "proper_root_height_class",
        "proper_root_height",
        "proper_root_r",
        "is_overflow",
        "support_A",
        "carrier_M",
        "overflow_d",
        "chart_R",
        "chart_K",
        "sink_scc_receipt",
        "same_chart_promotion_receipt",
    }
)

TOP_LEVEL_FIELDS = frozenset(
    {
        "schema_id",
        "schema_version",
        "state_id",
        "artifact_class",
        "consumer",
        "queue_gate",
        "producer_id",
        "branch_id",
        "parent_state_id",
        "root_context",
        "equation_rank",
        "mark",
        "terminal_first",
        "source_receipt",
        "facts",
    }
)


class ContractError(ValueError):
    """Fail-closed standalone contract error."""


@dataclass(frozen=True)
class PhaseProjection:
    p: int
    t: int
    X: int
    R: int
    K: int
    facts: Mapping[str, Any]
    projection_id: str
    digest: str


def canonical_json(value: Any) -> str:
    """Canonical ASCII JSON used by repository v1 receipts."""
    try:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise ContractError(f"not canonical JSON: {exc}") from exc


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("ascii")).hexdigest()


def seal(payload: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(payload))
    result.pop("digest", None)
    result["digest"] = canonical_digest(result)
    return result


def verify_seal(value: Mapping[str, Any]) -> None:
    if not isinstance(value, Mapping):
        raise ContractError("sealed value is not a mapping")
    digest = value.get("digest")
    if not isinstance(digest, str) or len(digest) != 64:
        raise ContractError("sealed value has malformed digest")
    payload = dict(value)
    payload.pop("digest", None)
    if canonical_digest(payload) != digest:
        raise ContractError("sealed value digest does not replay")


def state_wire_digest(raw_state: Mapping[str, Any]) -> str:
    return canonical_digest(raw_state)


def build_state_id(raw_state: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(raw_state))
    payload.pop("state_id", None)
    return "state:" + canonical_digest(payload)


def exact_value_equal(value: Any, expected: Any) -> bool:
    """Compare decoded JSON values without accepting bool/float int aliases."""
    if type(expected) in {type(None), bool, int, str}:
        return type(value) is type(expected) and value == expected
    if isinstance(expected, Mapping):
        return (
            isinstance(value, Mapping)
            and set(value) == set(expected)
            and all(exact_value_equal(value[key], expected[key]) for key in expected)
        )
    if isinstance(expected, (list, tuple)):
        return (
            isinstance(value, (list, tuple))
            and len(value) == len(expected)
            and all(exact_value_equal(item, want) for item, want in zip(value, expected))
        )
    return type(value) is type(expected) and value == expected


def root_parameters(p: int) -> tuple[int, int]:
    if type(p) is not int or p < 25 or (p - 1) % 24:
        raise ContractError("p must have the form 24t+1 with t>=1")
    t = (p - 1) // 24
    return t, 6 * t + 1


def source_facts() -> dict[str, Any]:
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


def target_facts(p: int) -> dict[str, Any]:
    t, X = root_parameters(p)
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
        "provenance_kind": "FULL_CARRIER_POST_G",
        "full_carrier_scope": True,
        "atomic_arm": "NONE",
        "dispatch_status": "NONE",
        "proper_root_k": None,
        "proper_root_height_class": "NONE",
        "proper_root_height": None,
        "proper_root_r": None,
        "is_overflow": False,
        "support_A": 1,
        "carrier_M": None,
        "overflow_d": None,
        "chart_R": 16 * t + 3,
        "chart_K": X * (16 * t + 1),
        "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }


def phase_projection(p: int) -> PhaseProjection:
    t, X = root_parameters(p)
    R = 16 * t + 3
    K = X * (16 * t + 1)
    if 4 * K != p * R + 1:
        raise ContractError("phase projection lost 4K=pR+1")
    facts = target_facts(p)
    payload = {
        "artifact_type": "CanonicalPhaseRootProjectionV2",
        "schema_version": 1,
        "transition_kind": "Q1_G_FULL_CARRIER_PHASE_ROOT",
        "root_context": p,
        "equation_rank": p,
        "t": t,
        "x": X,
        "mark_kind": ROOT_SOL,
        "facts": facts,
        "tie_break_rule_id": "q1_phase_root_closed_form_no_caller_tie_break_v1",
    }
    digest = canonical_digest(payload)
    return PhaseProjection(
        p=p,
        t=t,
        X=X,
        R=R,
        K=K,
        facts=facts,
        projection_id="phase-root-projection:" + digest,
        digest=digest,
    )


def source_potential(p: int) -> tuple[int, int, int, int, int, int, int]:
    return (p, 3, 0, 0, 0, 0, 0)


def target_potential(p: int) -> tuple[int, int, int, int, int, int, int]:
    projection = phase_projection(p)
    Bp = (p - 1) ** 2 // 4
    return (p, 2, 4, Bp, projection.K, 0, 0)


def verify_phase_drop(p: int, source: Sequence[int], target: Sequence[int]) -> None:
    if tuple(source) != source_potential(p):
        raise ContractError("source T5 vector is not the frozen root vector")
    if tuple(target) != target_potential(p):
        raise ContractError("target T5 vector is not the frozen phase-root vector")
    if not tuple(target) < tuple(source):
        raise ContractError("target T5 vector is not lexicographically smaller")
    if not (target[0] == source[0] and target[1] < source[1]):
        raise ContractError("PHASE_DROP must be paid at the phase coordinate")


def make_mark_receipt(p: int, receipt_id: str) -> dict[str, Any]:
    return seal(
        {
            "schema_id": MARK_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": receipt_id,
            "kind": ROOT_SOL,
            "root_context": p,
            "equation_rank": p,
        }
    )


def make_terminal_first_receipt(
    *, receipt_id: str, scope: str, outcome: str = "MISS"
) -> dict[str, Any]:
    if outcome != "MISS":
        raise ContractError("persistent state terminal_first outcome must be MISS")
    return seal(
        {
            "schema_id": TERMINAL_FIRST_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": receipt_id,
            "scope": scope,
            "outcome": outcome,
        }
    )


def make_reference_root_state(p: int) -> dict[str, Any]:
    """Create an exact-shaped V1 root fixture, not an authority receipt.

    A repository proof must replace this fixture by the actual V5-admitted wire
    and its exact-HEAD provenance.  The field shape and state-ID computation are
    identical to the public v1 state contract.
    """
    facts = source_facts()
    mark = make_mark_receipt(p, "sp05-reference-root-mark:" + canonical_digest({"p": p}))
    terminal = make_terminal_first_receipt(
        receipt_id="sp05-reference-registered-prefix-miss:" + canonical_digest({"p": p}),
        scope="REGISTERED_PREFIX_M23_REFERENCE_FIXTURE",
    )
    source_receipt = seal(
        {
            "schema_id": INITIALIZER_RECEIPT_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": "sp05-reference-root-initializer:" + canonical_digest({"p": p}),
            "producer_id": ROOT_PRODUCER_ID,
            "branch_id": ROOT_BRANCH_ID,
            "root_context": p,
            "equation_rank": p,
            "target_facts_digest": canonical_digest(facts),
            "terminal_first_digest": terminal["digest"],
            "status": "NONTERMINAL_INITIALIZER_OUTPUT",
        }
    )
    state = {
        "schema_id": STATE_SCHEMA_ID,
        "schema_version": STATE_SCHEMA_VERSION,
        "state_id": "pending",
        "artifact_class": "persistent_state",
        "consumer": "t6_selector",
        "queue_gate": ROOT_INITIALIZER_OUTPUT,
        "producer_id": ROOT_PRODUCER_ID,
        "branch_id": ROOT_BRANCH_ID,
        "parent_state_id": None,
        "root_context": p,
        "equation_rank": p,
        "mark": mark,
        "terminal_first": terminal,
        "source_receipt": source_receipt,
        "facts": facts,
    }
    state["state_id"] = build_state_id(state)
    return state


def make_successor_state(
    *,
    source_state: Mapping[str, Any],
    complete_source_miss_digest: str,
    complete_target_miss_digest: str,
) -> dict[str, Any]:
    """Construct the raw V1 successor wire after both complete MISS decisions.

    The legacy E1--E5 booleans are claims inside the current v1 wire.  A caller
    must additionally verify a structured bundle after the state ID is fixed.
    """
    validate_root_state_shape(source_state)
    p = int(source_state["root_context"])
    facts = target_facts(p)
    mark = make_mark_receipt(p, "sp05-phase-root-mark:" + canonical_digest({"p": p}))
    terminal = make_terminal_first_receipt(
        receipt_id="sp05-target-complete-miss:"
        + canonical_digest(
            {
                "source_state_id": source_state["state_id"],
                "source_miss": complete_source_miss_digest,
                "target_miss": complete_target_miss_digest,
            }
        ),
        scope="COMPLETE_TERMINAL_UNIVERSE_PLUS_PHASE_ROOT_ANCHOR",
    )
    source_receipt = seal(
        {
            "schema_id": SUCCESSOR_RECEIPT_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": "sp05-phase-root-edge:"
            + canonical_digest(
                {
                    "source_state_id": source_state["state_id"],
                    "source_miss": complete_source_miss_digest,
                    "target_miss": complete_target_miss_digest,
                }
            ),
            "producer_id": EDGE_PRODUCER_ID,
            "branch_id": EDGE_BRANCH_ID,
            "root_context": p,
            "equation_rank": p,
            "target_facts_digest": canonical_digest(facts),
            "terminal_first_digest": terminal["digest"],
            "status": "VERIFIED_EDGE",
            "parent_state_id": source_state["state_id"],
            "E1": True,
            "E2": True,
            "E3": True,
            "E4": True,
            "E5": True,
            "T5_ticket": PHASE_DROP,
        }
    )
    state = {
        "schema_id": STATE_SCHEMA_ID,
        "schema_version": STATE_SCHEMA_VERSION,
        "state_id": "pending",
        "artifact_class": "persistent_state",
        "consumer": "t6_selector",
        "queue_gate": ADMITTED_SUCCESSOR,
        "producer_id": EDGE_PRODUCER_ID,
        "branch_id": EDGE_BRANCH_ID,
        "parent_state_id": source_state["state_id"],
        "root_context": p,
        "equation_rank": p,
        "mark": mark,
        "terminal_first": terminal,
        "source_receipt": source_receipt,
        "facts": facts,
    }
    state["state_id"] = build_state_id(state)
    return state


def _validate_receipt_seal(value: Any, schema_id: str) -> None:
    if not isinstance(value, Mapping):
        raise ContractError(f"{schema_id} receipt is not a mapping")
    verify_seal(value)
    if (
        value.get("schema_id") != schema_id
        or type(value.get("schema_version")) is not int
        or value.get("schema_version") != 1
    ):
        raise ContractError(f"wrong receipt schema for {schema_id}")


def _validate_exact_facts(facts: Any) -> Mapping[str, Any]:
    if not isinstance(facts, Mapping) or set(facts) != FACT_FIELDS:
        raise ContractError("facts do not have the exact V1 field set")
    return facts


def validate_root_state_shape(raw: Mapping[str, Any]) -> None:
    if not isinstance(raw, Mapping) or set(raw) != TOP_LEVEL_FIELDS:
        raise ContractError("root state does not have exact V1 top-level fields")
    if (
        raw.get("schema_id") != STATE_SCHEMA_ID
        or type(raw.get("schema_version")) is not int
        or raw.get("schema_version") != 1
    ):
        raise ContractError("root state schema mismatch")
    if raw.get("queue_gate") != ROOT_INITIALIZER_OUTPUT:
        raise ContractError("source is not a root initializer output")
    if raw.get("parent_state_id") is not None:
        raise ContractError("root state has a parent")
    p = raw.get("root_context")
    if (
        type(p) is not int
        or type(raw.get("equation_rank")) is not int
        or raw.get("equation_rank") != p
    ):
        raise ContractError("root/equation rank mismatch")
    if raw.get("state_id") != build_state_id(raw):
        raise ContractError("root state ID does not replay")
    _validate_receipt_seal(raw["mark"], MARK_SCHEMA_ID)
    _validate_receipt_seal(raw["terminal_first"], TERMINAL_FIRST_SCHEMA_ID)
    _validate_receipt_seal(raw["source_receipt"], INITIALIZER_RECEIPT_SCHEMA_ID)
    facts = _validate_exact_facts(raw["facts"])
    if not exact_value_equal(facts, source_facts()):
        raise ContractError("root facts are not the q=1 G handoff shape")
    if raw["producer_id"] != ROOT_PRODUCER_ID or raw["branch_id"] != ROOT_BRANCH_ID:
        raise ContractError("root producer/branch mismatch")
    if raw["source_receipt"].get("target_facts_digest") != canonical_digest(facts):
        raise ContractError("root source receipt does not bind facts")
    if raw["source_receipt"].get("terminal_first_digest") != raw["terminal_first"].get("digest"):
        raise ContractError("root source receipt does not bind terminal receipt")


def classify_owner(raw: Mapping[str, Any]) -> str:
    facts = _validate_exact_facts(raw.get("facts"))
    p = raw.get("root_context")
    if (
        type(p) is not int
        or type(raw.get("equation_rank")) is not int
        or raw.get("equation_rank") != p
    ):
        raise ContractError("owner classification root/equation mismatch")
    if exact_value_equal(facts, source_facts()):
        return SOURCE_OWNER
    if exact_value_equal(facts, target_facts(p)):
        return TARGET_OWNER
    raise ContractError("state matches neither SP-05 source nor target owner")


def owner_digest(raw: Mapping[str, Any], owner: str) -> str:
    precedence_index = 2 if owner == SOURCE_OWNER else 14
    payload = {
        "contract_id": "t6_persistent_selector_state_v1",
        "schema_version": 1,
        "state_id": raw["state_id"],
        "facts_digest": canonical_digest(raw["facts"]),
        "owner": owner,
        "matched_families": [owner],
        "precedence_index": precedence_index,
    }
    return "owner:" + canonical_digest(payload)


def validate_successor_state_shape(
    raw: Mapping[str, Any], source_state: Mapping[str, Any]
) -> tuple[str, str]:
    validate_root_state_shape(source_state)
    if not isinstance(raw, Mapping) or set(raw) != TOP_LEVEL_FIELDS:
        raise ContractError("target state does not have exact V1 top-level fields")
    if (
        raw.get("schema_id") != STATE_SCHEMA_ID
        or type(raw.get("schema_version")) is not int
        or raw.get("schema_version") != 1
    ):
        raise ContractError("target state schema mismatch")
    if raw.get("queue_gate") != ADMITTED_SUCCESSOR:
        raise ContractError("target is not an ADMITTED_SUCCESSOR wire")
    if raw.get("producer_id") != EDGE_PRODUCER_ID or raw.get("branch_id") != EDGE_BRANCH_ID:
        raise ContractError("target producer/branch mismatch")
    if raw.get("parent_state_id") != source_state.get("state_id"):
        raise ContractError("target parent is not the actual source ID")
    p = source_state["root_context"]
    if (
        type(raw.get("root_context")) is not int
        or type(raw.get("equation_rank")) is not int
        or raw.get("root_context") != p
        or raw.get("equation_rank") != p
    ):
        raise ContractError("target equation interface changed")
    if raw.get("state_id") != build_state_id(raw):
        raise ContractError("target state ID does not replay")
    _validate_receipt_seal(raw["mark"], MARK_SCHEMA_ID)
    _validate_receipt_seal(raw["terminal_first"], TERMINAL_FIRST_SCHEMA_ID)
    _validate_receipt_seal(raw["source_receipt"], SUCCESSOR_RECEIPT_SCHEMA_ID)
    facts = _validate_exact_facts(raw["facts"])
    if not exact_value_equal(facts, target_facts(p)):
        raise ContractError("target facts are not canonical phase-root facts")
    receipt = raw["source_receipt"]
    if receipt.get("parent_state_id") != source_state["state_id"]:
        raise ContractError("target source receipt parent mismatch")
    if not all(receipt.get(name) is True for name in ("E1", "E2", "E3", "E4", "E5")):
        raise ContractError("legacy target receipt does not carry E1--E5 claims")
    if receipt.get("T5_ticket") != PHASE_DROP:
        raise ContractError("target does not carry PHASE_DROP")
    if receipt.get("target_facts_digest") != canonical_digest(facts):
        raise ContractError("target receipt facts digest mismatch")
    if receipt.get("terminal_first_digest") != raw["terminal_first"].get("digest"):
        raise ContractError("target receipt terminal digest mismatch")
    owner = classify_owner(raw)
    if owner != TARGET_OWNER:
        raise ContractError("target common owner is not type_i_full_carrier_post_g")
    digest = owner_digest(raw, owner)
    return owner, digest


def make_reentry_registration() -> dict[str, Any]:
    return seal(
        {
            "schema_id": "sp05_phase_root_reentry_registration_v1",
            "schema_version": 1,
            "route_id": REENTRY_ROUTE_ID,
            "source_owners": [TARGET_OWNER],
            "consumer": "t6_selector",
            "handler_semantics": "VERIFY_TARGET_COMPLETE_TERMINAL_AND_ANCHOR_THEN_ENTER_TYPEI_FULL_CARRIER_BODY",
            "creates_self_edge": False,
            "requires_admitted_state": True,
        }
    )


def verify_reentry(
    target_state: Mapping[str, Any], registration: Mapping[str, Any]
) -> dict[str, Any]:
    verify_seal(registration)
    if registration.get("schema_id") != "sp05_phase_root_reentry_registration_v1":
        raise ContractError("wrong re-entry registration schema")
    if registration.get("route_id") != REENTRY_ROUTE_ID:
        raise ContractError("wrong re-entry route")
    owner = classify_owner(target_state)
    if owner not in registration.get("source_owners", []):
        raise ContractError("target owner is not registered for re-entry")
    if registration.get("consumer") != "t6_selector":
        raise ContractError("re-entry uses a different selector")
    if registration.get("creates_self_edge") is not False:
        raise ContractError("re-entry must not create a fake self-edge")
    return seal(
        {
            "receipt_type": "SP05ReentryReceiptV1",
            "schema_version": 1,
            "target_state_id": target_state["state_id"],
            "target_owner": owner,
            "route_id": REENTRY_ROUTE_ID,
            "consumer": "t6_selector",
            "outcome": "PHASE_BODY_ENTERED",
        }
    )
