#!/usr/bin/env python3
"""Materialize an actual q=1 G root as a V1 initializer-output state.

The materializer owns only deterministic state-wire construction.  It never
classifies the V1 owner and never grants persistent admission or queue rights.
Its local role grant is a shape capability only; it does not authenticate a
repository HEAD or create repository authority.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass, fields
from enum import Enum
from types import MappingProxyType
from typing import Any, ClassVar, Mapping

import t6_persistent_selector_state_v1 as state_contract
import t6_q_one_root_initializer_envelope_v2 as root_envelope
import t6_q_one_root_v1_terminal_adapter_v1 as terminal_adapter


ARTIFACT_ID = "q1_root_v1_base_materializer_v1"
ARTIFACT_PATH = "scripts/t6_q_one_root_v1_base_materializer_v1.py"
ARTIFACT_SYMBOLS = (
    "materialize_q_one_root_v1_base_state_v1",
    "base_materialization_receipt_to_mapping_v1",
)
ROLE = "Q1_ROOT_V1_BASE_MATERIALIZER"
GRANT_ID = "q1_root_v1_base_materializer_grant_v1"
CAPABILITIES = ("MATERIALIZE_Q1_G_V1_ROOT_INITIALIZER_OUTPUT",)
AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V5"

RECEIPT_TYPE = "Q1_ROOT_V1_BASE_MATERIALIZATION_RECEIPT_V1"
RECEIPT_ID_PREFIX = "q1-v1-root-materialization:"
STATUS = "V1_ROOT_INITIALIZER_OUTPUT_MATERIALIZED_NOT_ADMITTED"

PRODUCER_ID = "q1_root_v1_base_materializer_v1"
BRANCH_ID = "q1_g_registered_prefix_miss_base_v1"
TARGET_OWNER = "type_ii_relation_g_endpoint"
MARK_RECEIPT_ID_PREFIX = "q1-v1-root-sol-mark:"
SOURCE_RECEIPT_ID_PREFIX = "q1-v1-root-initializer:"

GRANT_FIELDS = {
    "grant_id",
    "role",
    "artifact_id",
    "artifact_path",
    "artifact_symbols",
    "capabilities",
    "authority_class",
    "artifact_semantic_sha256",
}


class BaseMaterializationRejectCode(str, Enum):
    INPUT_NOT_EXACT_MAPPING = "INPUT_NOT_EXACT_MAPPING"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    SOURCE_REPLAY_FAILED = "SOURCE_REPLAY_FAILED"
    TERMINAL_REPLAY_FAILED = "TERMINAL_REPLAY_FAILED"
    GRANT_MISMATCH = "GRANT_MISMATCH"
    STATE_WIRE_MISMATCH = "STATE_WIRE_MISMATCH"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    AUTHORITY_BOUNDARY_VIOLATION = "AUTHORITY_BOUNDARY_VIOLATION"


class BaseMaterializationError(ValueError):
    def __init__(self, code: BaseMaterializationRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: BaseMaterializationRejectCode, detail: str) -> None:
    raise BaseMaterializationError(code, detail)


def _json_copy(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(
                    BaseMaterializationRejectCode.MALFORMED_FIELD,
                    "canonical JSON keys must be exact strings",
                )
            result[key] = _json_copy(child)
        return result
    if type(value) is list or type(value) is tuple:
        return [_json_copy(child) for child in value]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(
        BaseMaterializationRejectCode.MALFORMED_FIELD,
        f"unsupported canonical JSON value {type(value).__name__}",
    )


def canonical_json_v1(value: Any) -> str:
    try:
        return json.dumps(
            _json_copy(value),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise BaseMaterializationError(
            BaseMaterializationRejectCode.MALFORMED_FIELD,
            f"value is not canonical JSON: {exc}",
        ) from exc


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


def _is_digest(value: Any) -> bool:
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _matches_root_potential(value: Any, p: int) -> bool:
    return (
        type(value) in {list, tuple}
        and len(value) == 7
        and all(type(item) is int for item in value)
        and tuple(value) == (p, 3, 0, 0, 0, 0, 0)
    )


def _exact_mapping(value: Any, name: str) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(
            BaseMaterializationRejectCode.INPUT_NOT_EXACT_MAPPING,
            f"{name} must be an exact dict",
        )
    return _json_copy(value)


def _grant(value: Any) -> tuple[dict[str, Any], str]:
    grant = _exact_mapping(value, "role_grant")
    if set(grant) != GRANT_FIELDS:
        _reject(
            BaseMaterializationRejectCode.GRANT_MISMATCH,
            "materializer grant has an inexact field set",
        )
    expected = {
        "grant_id": GRANT_ID,
        "role": ROLE,
        "artifact_id": ARTIFACT_ID,
        "artifact_path": ARTIFACT_PATH,
        "artifact_symbols": list(ARTIFACT_SYMBOLS),
        "capabilities": list(CAPABILITIES),
        "authority_class": AUTHORITY_CLASS,
    }
    if any(grant.get(name) != expected_value for name, expected_value in expected.items()):
        _reject(
            BaseMaterializationRejectCode.GRANT_MISMATCH,
            "materializer grant identity or capability changed",
        )
    if not _is_digest(grant.get("artifact_semantic_sha256")):
        _reject(
            BaseMaterializationRejectCode.GRANT_MISMATCH,
            "materializer semantic pin is malformed",
        )
    return grant, canonical_digest_v1(grant)


def _source_chain(
    *,
    raw_q_one_g: Any,
    source_body: Any,
    root_anchor: Any,
    source_state: Any,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    raw = _exact_mapping(raw_q_one_g, "raw_q_one_g")
    body_wire = _exact_mapping(source_body, "source_body")
    anchor_wire = _exact_mapping(root_anchor, "root_anchor")
    state_wire = _exact_mapping(source_state, "source_state")
    try:
        body = root_envelope.parse_canonical_q_one_g_source_body_v2(body_wire, raw)
        anchor = root_envelope.parse_root_initializer_anchor_v2(anchor_wire, body)
        state = root_envelope.parse_raw_root_source_state_v2(state_wire, body, anchor)
    except Exception as exc:
        raise BaseMaterializationError(
            BaseMaterializationRejectCode.SOURCE_REPLAY_FAILED,
            f"V2 root source chain did not replay: {exc}",
        ) from exc
    expected_body = root_envelope.artifact_to_mapping_v2(body)
    expected_anchor = root_envelope.artifact_to_mapping_v2(anchor)
    expected_state = root_envelope.artifact_to_mapping_v2(state)
    return raw, expected_body, expected_anchor, expected_state


def _selector_facts() -> dict[str, Any]:
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


def _producer_rule() -> dict[str, Any]:
    return {
        "producer_id": PRODUCER_ID,
        "queue_gate": state_contract.ROOT_INITIALIZER_OUTPUT,
        "branch_ids": [BRANCH_ID],
        "source_owners": [],
        "target_owners": [TARGET_OWNER],
    }


def _build_v1_state(
    *,
    source_state: Mapping[str, Any],
    root_actualness: Mapping[str, Any],
    terminal_receipt: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], str]:
    try:
        projection = terminal_adapter.project_q_one_v3_miss_to_v1_terminal_first_v1(
            source_state=_json_copy(source_state),
            root_actualness=_json_copy(root_actualness),
            terminal_receipt=_json_copy(terminal_receipt),
        )
    except terminal_adapter.TerminalProjectionError as exc:
        raise BaseMaterializationError(
            BaseMaterializationRejectCode.TERMINAL_REPLAY_FAILED,
            f"V3 MISS did not project to the fixed V1 terminal shape: {exc}",
        ) from exc
    projection_wire = terminal_adapter.terminal_projection_to_mapping_v1(projection)
    root_context = projection_wire["root_context"]
    if source_state.get("root_context") != root_context:
        _reject(
            BaseMaterializationRejectCode.SOURCE_REPLAY_FAILED,
            "V2 source and V3 terminal root contexts differ",
        )
    mark_binding = canonical_digest_v1(
        {
            "kind": state_contract.ROOT_SOL,
            "root_context": root_context,
            "equation_rank": root_context,
        }
    )
    mark = state_contract.seal_receipt_v1(
        {
            "schema_id": state_contract.MARK_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": MARK_RECEIPT_ID_PREFIX + mark_binding,
            "kind": state_contract.ROOT_SOL,
            "root_context": root_context,
            "equation_rank": root_context,
        }
    )
    terminal = _json_copy(projection_wire["v1_terminal_first"])
    selector_facts = _selector_facts()
    facts_digest = state_contract.canonical_digest_v1(selector_facts)
    semantic_origin = canonical_digest_v1(
        {
            "v2_source_state_id": source_state["state_id"],
            "v2_source_state_digest": source_state["digest"],
            "root_context": root_context,
            "producer_id": PRODUCER_ID,
            "branch_id": BRANCH_ID,
            "terminal_projection_binding_digest": projection_wire[
                "projection_binding_digest"
            ],
            "facts_digest": facts_digest,
        }
    )
    source_receipt = state_contract.seal_receipt_v1(
        {
            "schema_id": state_contract.INITIALIZER_RECEIPT_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": SOURCE_RECEIPT_ID_PREFIX + semantic_origin,
            "producer_id": PRODUCER_ID,
            "branch_id": BRANCH_ID,
            "root_context": root_context,
            "equation_rank": root_context,
            "target_facts_digest": facts_digest,
            "terminal_first_digest": terminal["digest"],
            "status": "NONTERMINAL_INITIALIZER_OUTPUT",
        }
    )
    state = {
        "schema_id": state_contract.STATE_SCHEMA_ID,
        "schema_version": state_contract.STATE_SCHEMA_VERSION,
        "state_id": "pending",
        "artifact_class": "persistent_state",
        "consumer": "t6_selector",
        "queue_gate": state_contract.ROOT_INITIALIZER_OUTPUT,
        "producer_id": PRODUCER_ID,
        "branch_id": BRANCH_ID,
        "parent_state_id": None,
        "root_context": root_context,
        "equation_rank": root_context,
        "mark": mark,
        "terminal_first": terminal,
        "source_receipt": source_receipt,
        "facts": selector_facts,
    }
    state["state_id"] = state_contract.build_state_id_v1(state)
    return state, projection_wire, semantic_origin


@dataclass(frozen=True, init=False, slots=True)
class QOneRootV1BaseMaterializationReceiptV1:
    ARTIFACT_TYPE: ClassVar[str] = RECEIPT_TYPE

    schema_version: int
    status: str
    role: str
    role_grant: Mapping[str, Any]
    role_grant_id: str
    role_grant_digest: str
    role_artifact_id: str
    role_artifact_semantic_sha256: str
    raw_q_one_g: Mapping[str, Any]
    raw_q_one_g_digest: str
    source_body: Mapping[str, Any]
    body_id: str
    body_digest: str
    root_anchor: Mapping[str, Any]
    anchor_id: str
    anchor_digest: str
    source_state: Mapping[str, Any]
    source_state_id: str
    source_state_digest: str
    root_actualness: Mapping[str, Any]
    root_actualness_id: str
    root_actualness_digest: str
    terminal_receipt: Mapping[str, Any]
    terminal_receipt_id: str
    terminal_receipt_digest: str
    terminal_projection: Mapping[str, Any]
    terminal_projection_id: str
    terminal_projection_digest: str
    producer_rule: Mapping[str, Any]
    producer_rule_digest: str
    semantic_origin_digest: str
    v1_state: Mapping[str, Any]
    v1_state_id: str
    v1_state_wire_digest: str
    canonical_root_potential_evidence: tuple[int, int, int, int, int, int, int]
    canonical_root_potential_evidence_digest: str
    local_grant_authenticates_head: bool
    repository_authority: bool
    root_base_materialization_authority: bool
    v1_base_owner_authority: bool
    root_base_admission_authority: bool
    persistent_admission: bool
    queue_authority: bool
    enqueue_authority: bool
    enqueue_performed: bool
    successor_admission: bool
    producer_authority: bool
    producer_continuation_allowed: bool
    e1_authority: bool
    e2_authority: bool
    e3_authority: bool
    e4_authority: bool
    e5_authority: bool
    t5_ticket_authority: bool
    t5_potential_authority: bool
    global_exhaustion: bool
    terminal_leaf_authority: bool
    receipt_id: str
    digest: str


_MAPPING_FIELDS = {
    "role_grant",
    "raw_q_one_g",
    "source_body",
    "root_anchor",
    "source_state",
    "root_actualness",
    "terminal_receipt",
    "terminal_projection",
    "producer_rule",
    "v1_state",
}


def _unsigned(values: Mapping[str, Any]) -> dict[str, Any]:
    result = {"receipt_type": RECEIPT_TYPE}
    for field in fields(QOneRootV1BaseMaterializationReceiptV1):
        if field.name not in {"receipt_id", "digest"}:
            result[field.name] = _json_copy(values[field.name])
    return result


def _construct(values: Mapping[str, Any]) -> QOneRootV1BaseMaterializationReceiptV1:
    result = object.__new__(QOneRootV1BaseMaterializationReceiptV1)
    for field in fields(QOneRootV1BaseMaterializationReceiptV1):
        value = values[field.name]
        if field.name in _MAPPING_FIELDS:
            value = MappingProxyType(_json_copy(value))
        object.__setattr__(result, field.name, value)
    return result


def _validate_receipt(receipt: QOneRootV1BaseMaterializationReceiptV1) -> None:
    if type(receipt) is not QOneRootV1BaseMaterializationReceiptV1:
        _reject(
            BaseMaterializationRejectCode.INPUT_NOT_EXACT_MAPPING,
            "materialization receipt has the wrong class",
        )
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    digest = canonical_digest_v1(_unsigned(values))
    if receipt.digest != digest or receipt.receipt_id != RECEIPT_ID_PREFIX + digest:
        _reject(
            BaseMaterializationRejectCode.DIGEST_MISMATCH,
            "materialization receipt seal does not replay",
        )
    grant, grant_digest = _grant(_json_copy(receipt.role_grant))
    if not (
        receipt.role_grant_id == grant["grant_id"]
        and receipt.role_grant_digest == grant_digest
        and receipt.role_artifact_id == grant["artifact_id"]
        and receipt.role_artifact_semantic_sha256
        == grant["artifact_semantic_sha256"]
    ):
        _reject(
            BaseMaterializationRejectCode.GRANT_MISMATCH,
            "materialization grant references changed",
        )
    raw, body, anchor, state = _source_chain(
        raw_q_one_g=_json_copy(receipt.raw_q_one_g),
        source_body=_json_copy(receipt.source_body),
        root_anchor=_json_copy(receipt.root_anchor),
        source_state=_json_copy(receipt.source_state),
    )
    expected_state, projection, semantic_origin = _build_v1_state(
        source_state=state,
        root_actualness=_json_copy(receipt.root_actualness),
        terminal_receipt=_json_copy(receipt.terminal_receipt),
    )
    if not (
        _json_copy(receipt.raw_q_one_g) == raw
        and receipt.raw_q_one_g_digest == canonical_digest_v1(raw)
        and _json_copy(receipt.source_body) == body
        and receipt.body_id == body["body_id"]
        and receipt.body_digest == body["digest"]
        and _json_copy(receipt.root_anchor) == anchor
        and receipt.anchor_id == anchor["anchor_id"]
        and receipt.anchor_digest == anchor["digest"]
        and _json_copy(receipt.source_state) == state
        and receipt.source_state_id == state["state_id"]
        and receipt.source_state_digest == state["digest"]
        and receipt.root_actualness_id
        == receipt.root_actualness.get("actualness_id")
        and receipt.root_actualness_digest == receipt.root_actualness.get("digest")
        and receipt.terminal_receipt_id == receipt.terminal_receipt.get("receipt_id")
        and receipt.terminal_receipt_digest == receipt.terminal_receipt.get("digest")
        and _json_copy(receipt.terminal_projection) == projection
        and receipt.terminal_projection_id == projection["receipt_id"]
        and receipt.terminal_projection_digest == projection["digest"]
        and _json_copy(receipt.producer_rule) == _producer_rule()
        and receipt.producer_rule_digest == canonical_digest_v1(_producer_rule())
        and receipt.semantic_origin_digest == semantic_origin
        and _json_copy(receipt.v1_state) == expected_state
        and receipt.v1_state_id == expected_state["state_id"]
        and receipt.v1_state_wire_digest == canonical_digest_v1(expected_state)
        and _matches_root_potential(
            receipt.canonical_root_potential_evidence,
            expected_state["equation_rank"],
        )
        and receipt.canonical_root_potential_evidence_digest
        == canonical_digest_v1(
            [expected_state["equation_rank"], 3, 0, 0, 0, 0, 0]
        )
        and receipt.local_grant_authenticates_head is False
        and receipt.repository_authority is False
    ):
        _reject(
            BaseMaterializationRejectCode.STATE_WIRE_MISMATCH,
            "materialized V1 state or an upstream binding changed",
        )
    if not (
        type(receipt.schema_version) is int
        and receipt.schema_version == 1
        and receipt.status == STATUS
        and receipt.role == ROLE
        and receipt.root_base_materialization_authority is True
    ):
        _reject(
            BaseMaterializationRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
            "materializer identity or sole positive capability changed",
        )
    for name in (
        "v1_base_owner_authority",
        "root_base_admission_authority",
        "persistent_admission",
        "queue_authority",
        "enqueue_authority",
        "enqueue_performed",
        "successor_admission",
        "producer_authority",
        "producer_continuation_allowed",
        "e1_authority",
        "e2_authority",
        "e3_authority",
        "e4_authority",
        "e5_authority",
        "t5_ticket_authority",
        "t5_potential_authority",
        "global_exhaustion",
        "terminal_leaf_authority",
    ):
        if getattr(receipt, name) is not False:
            _reject(
                BaseMaterializationRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
                f"materializer field {name} must be false",
            )


def materialize_q_one_root_v1_base_state_v1(
    *,
    raw_q_one_g: dict[str, Any],
    source_body: dict[str, Any],
    root_anchor: dict[str, Any],
    source_state: dict[str, Any],
    root_actualness: dict[str, Any],
    terminal_receipt: dict[str, Any],
    role_grant: dict[str, Any],
) -> QOneRootV1BaseMaterializationReceiptV1:
    """Materialize, but do not admit or enqueue, one q=1 G V1 base state."""

    raw, body, anchor, state = _source_chain(
        raw_q_one_g=raw_q_one_g,
        source_body=source_body,
        root_anchor=root_anchor,
        source_state=source_state,
    )
    actualness = _exact_mapping(root_actualness, "root_actualness")
    terminal = _exact_mapping(terminal_receipt, "terminal_receipt")
    grant, grant_digest = _grant(role_grant)
    v1_state, projection, semantic_origin = _build_v1_state(
        source_state=state,
        root_actualness=actualness,
        terminal_receipt=terminal,
    )
    values: dict[str, Any] = {
        "schema_version": 1,
        "status": STATUS,
        "role": ROLE,
        "role_grant": grant,
        "role_grant_id": grant["grant_id"],
        "role_grant_digest": grant_digest,
        "role_artifact_id": grant["artifact_id"],
        "role_artifact_semantic_sha256": grant["artifact_semantic_sha256"],
        "raw_q_one_g": raw,
        "raw_q_one_g_digest": canonical_digest_v1(raw),
        "source_body": body,
        "body_id": body["body_id"],
        "body_digest": body["digest"],
        "root_anchor": anchor,
        "anchor_id": anchor["anchor_id"],
        "anchor_digest": anchor["digest"],
        "source_state": state,
        "source_state_id": state["state_id"],
        "source_state_digest": state["digest"],
        "root_actualness": actualness,
        "root_actualness_id": actualness["actualness_id"],
        "root_actualness_digest": actualness["digest"],
        "terminal_receipt": terminal,
        "terminal_receipt_id": terminal["receipt_id"],
        "terminal_receipt_digest": terminal["digest"],
        "terminal_projection": projection,
        "terminal_projection_id": projection["receipt_id"],
        "terminal_projection_digest": projection["digest"],
        "producer_rule": _producer_rule(),
        "producer_rule_digest": canonical_digest_v1(_producer_rule()),
        "semantic_origin_digest": semantic_origin,
        "v1_state": v1_state,
        "v1_state_id": v1_state["state_id"],
        "v1_state_wire_digest": canonical_digest_v1(v1_state),
        "canonical_root_potential_evidence": (
            v1_state["equation_rank"],
            3,
            0,
            0,
            0,
            0,
            0,
        ),
        "canonical_root_potential_evidence_digest": canonical_digest_v1(
            [v1_state["equation_rank"], 3, 0, 0, 0, 0, 0]
        ),
        "local_grant_authenticates_head": False,
        "repository_authority": False,
        "root_base_materialization_authority": True,
        "v1_base_owner_authority": False,
        "root_base_admission_authority": False,
        "persistent_admission": False,
        "queue_authority": False,
        "enqueue_authority": False,
        "enqueue_performed": False,
        "successor_admission": False,
        "producer_authority": False,
        "producer_continuation_allowed": False,
        "e1_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "t5_ticket_authority": False,
        "t5_potential_authority": False,
        "global_exhaustion": False,
        "terminal_leaf_authority": False,
    }
    digest = canonical_digest_v1(_unsigned(values))
    values.update({"receipt_id": RECEIPT_ID_PREFIX + digest, "digest": digest})
    result = _construct(values)
    _validate_receipt(result)
    return result


def base_materialization_receipt_to_mapping_v1(
    receipt: QOneRootV1BaseMaterializationReceiptV1,
) -> dict[str, Any]:
    _validate_receipt(receipt)
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    result = _unsigned(values)
    result["receipt_id"] = receipt.receipt_id
    result["digest"] = receipt.digest
    return result


__all__ = [
    "ARTIFACT_ID",
    "ARTIFACT_PATH",
    "ARTIFACT_SYMBOLS",
    "AUTHORITY_CLASS",
    "BRANCH_ID",
    "BaseMaterializationError",
    "BaseMaterializationRejectCode",
    "CAPABILITIES",
    "GRANT_ID",
    "PRODUCER_ID",
    "QOneRootV1BaseMaterializationReceiptV1",
    "ROLE",
    "STATUS",
    "TARGET_OWNER",
    "base_materialization_receipt_to_mapping_v1",
    "canonical_digest_v1",
    "materialize_q_one_root_v1_base_state_v1",
]
