#!/usr/bin/env python3
"""Bind one exact-HEAD q=1 source chain without creating an E1 transition.

The V3, V4, V5, and V6 records already describe a narrowly scoped source
occurrence.  This module packages those four independently replayable records
under one exact Git HEAD and deterministically projects the four values
consumed by ``ExternalQOneSourceBindingV2``.  It is deliberately a source-input
wrapper, not a structured E1 receipt or a successor constructor.

No local project module is imported here.  The controlled loader and the
post-issuance replayer separately instantiate the existing V2 object and
compare it with the projection calculated below.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, fields
from enum import Enum
import hashlib
import json
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, NoReturn


ARTIFACT_ID = "q1_exact_head_source_input_binder_v1"
ARTIFACT_PATH = "scripts/t6_q_one_exact_head_source_input_v1.py"
ARTIFACT_SYMBOLS = (
    "bind_exact_head_q_one_actual_source_input_v1",
    "exact_head_q_one_actual_source_input_to_mapping_v1",
)
ROLE = "EXACT_HEAD_Q1_ACTUAL_SOURCE_INPUT_BINDER"
GRANT_ID = "q1_exact_head_q_one_source_input_binder_grant_v1"
CAPABILITIES = ("BUILD_EXACT_HEAD_Q1_SOURCE_INPUT_REPLAY_CANDIDATE",)
AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V6_CANDIDATE_ONLY"

RECEIPT_TYPE = "EXACT_HEAD_Q_ONE_ACTUAL_SOURCE_INPUT_V1"
RECEIPT_ID_PREFIX = "exact-head-q1-source-input:"
STATUS = "EXACT_HEAD_Q1_SOURCE_INPUT_REPLAY_CANDIDATE_NONAUTHORITY"
BINDING_SCOPE = "EXACT_HEAD_Q1_ROOT_SOURCE_INPUT_REPLAY_CANDIDATE_NOT_E1"

V3_REGISTRY_ID = "t6_coordinator_role_registry_v3"
V4_REGISTRY_ID = "t6_coordinator_role_registry_v4"
V5_REGISTRY_ID = "t6_coordinator_role_registry_v5"
V6_REGISTRY_ID = "t6_coordinator_role_registry_v6"
V3_MISS_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
V3_MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"
V4_RECEIPT_TYPE = "Q1_REGISTERED_PREFIX_ROOT_SOURCE_E1_RECEIPT_V2"
V5_RECEIPT_TYPE = "Q1_ROOT_V1_BASE_ADMISSION_RECEIPT_V1"
V6_RECEIPT_TYPE = "Q1_ROOT_SOURCE_SCOPED_E1_REBIND_RECEIPT_V1"
V6_REBIND_STATUS = "ROOT_SOURCE_SCOPED_E1_REBOUND_TO_V1_BASE_NO_SUCCESSOR"

EXTERNAL_BINDING_TYPE = "ExternalQOneSourceBindingV2"
EXTERNAL_BINDING_ID_PREFIX = "external-q1-source-binding:"
EXTERNAL_BINDING_SCOPE = "EXTERNAL_Q1_SOURCE_PREIMAGE_NOT_E1"

SCOPE_ID = "q1_root_after_gap_3_7_11_registered_prefix_v1"
COVERAGE_SEMANTICS = "REGISTERED_PRIORITY_ONLY"
ORDERED_GAPS = (3, 7, 11)
NEXT_UNCHECKED_GAP = 15
OID_RE = __import__("re").compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
DIGEST_RE = __import__("re").compile(r"[0-9a-f]{64}\Z")


class SourceInputRejectCode(str, Enum):
    MALFORMED_INPUT = "MALFORMED_INPUT"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    GRANT_MISMATCH = "GRANT_MISMATCH"
    REGISTRY_MISMATCH = "REGISTRY_MISMATCH"
    HEAD_MISMATCH = "HEAD_MISMATCH"
    RECEIPT_MISMATCH = "RECEIPT_MISMATCH"
    SOURCE_MISMATCH = "SOURCE_MISMATCH"
    SCOPE_MISMATCH = "SCOPE_MISMATCH"
    AUTHORITY_MISMATCH = "AUTHORITY_MISMATCH"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"


class ExactHeadQOneSourceInputError(ValueError):
    def __init__(self, code: SourceInputRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: SourceInputRejectCode, detail: str) -> NoReturn:
    raise ExactHeadQOneSourceInputError(code, detail)


def _copy_json(value: Any, *, path: str = "$") -> Any:
    if type(value) is dict or type(value) is MappingProxyType:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                _reject(SourceInputRejectCode.MALFORMED_INPUT, f"{path} has a bad key")
            result[key] = _copy_json(child, path=f"{path}.{key}")
        return result
    if type(value) is list or type(value) is tuple:
        return [_copy_json(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(SourceInputRejectCode.MALFORMED_INPUT, f"{path} contains {type(value).__name__}")


def _freeze(value: Any) -> Any:
    copied = _copy_json(value)
    if type(copied) is dict:
        return MappingProxyType({key: _freeze(child) for key, child in copied.items()})
    if type(copied) is list:
        return tuple(_freeze(child) for child in copied)
    return copied


def canonical_json_v1(value: Any) -> str:
    return json.dumps(
        _copy_json(value), ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False
    )


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


def _mapping(value: Any, name: str) -> dict[str, Any]:
    if type(value) is not dict and type(value) is not MappingProxyType:
        _reject(SourceInputRejectCode.MALFORMED_INPUT, f"{name} must be an exact mapping")
    return _copy_json(value, path=name)


def _require_digest(value: Any, name: str) -> str:
    if type(value) is not str or DIGEST_RE.fullmatch(value) is None:
        _reject(SourceInputRejectCode.MALFORMED_INPUT, f"{name} is not a SHA-256 digest")
    return value


def _require_oid(value: Any, name: str) -> str:
    if type(value) is not str or OID_RE.fullmatch(value) is None:
        _reject(SourceInputRejectCode.MALFORMED_INPUT, f"{name} is not a full Git object ID")
    return value


def _require_content_id(value: Any, name: str, prefix: str) -> str:
    if type(value) is not str or not value.startswith(prefix):
        _reject(SourceInputRejectCode.MALFORMED_INPUT, f"{name} has the wrong prefix")
    suffix = value[len(prefix):]
    _require_digest(suffix, name)
    return value


def _require_bool(value: Any, expected: bool, name: str) -> None:
    if type(value) is not bool or value is not expected:
        _reject(SourceInputRejectCode.AUTHORITY_MISMATCH, f"{name} must be {expected!r}")


def _sealed_receipt(value: Any, *, receipt_type: str, prefix: str, name: str) -> dict[str, Any]:
    receipt = _mapping(value, name)
    if receipt.get("receipt_type") != receipt_type:
        _reject(SourceInputRejectCode.RECEIPT_MISMATCH, f"{name}.receipt_type")
    digest = _require_digest(receipt.get("digest"), f"{name}.digest")
    receipt_id = _require_content_id(receipt.get("receipt_id"), f"{name}.receipt_id", prefix)
    if receipt_id != prefix + digest:
        _reject(SourceInputRejectCode.DIGEST_MISMATCH, f"{name}.receipt_id")
    unsigned = dict(receipt)
    unsigned.pop("receipt_id", None)
    unsigned.pop("digest", None)
    if canonical_digest_v1(unsigned) != digest:
        _reject(SourceInputRejectCode.DIGEST_MISMATCH, f"{name}.digest")
    return receipt


def _grant(value: Any) -> tuple[dict[str, Any], str]:
    grant = _mapping(value, "role_grant")
    expected = {
        "grant_id": GRANT_ID,
        "role": ROLE,
        "artifact_id": ARTIFACT_ID,
        "artifact_path": ARTIFACT_PATH,
        "artifact_symbols": list(ARTIFACT_SYMBOLS),
        "capabilities": list(CAPABILITIES),
        "authority_class": AUTHORITY_CLASS,
    }
    if set(grant) != set(expected) | {"artifact_semantic_sha256"}:
        _reject(SourceInputRejectCode.FIELD_SET_MISMATCH, "role_grant")
    for key, wanted in expected.items():
        if grant.get(key) != wanted:
            _reject(SourceInputRejectCode.GRANT_MISMATCH, key)
    _require_digest(grant.get("artifact_semantic_sha256"), "role_grant.artifact_semantic_sha256")
    return grant, canonical_digest_v1(grant)


def _registry_context(value: Any) -> dict[str, Any]:
    context = _mapping(value, "registry_context")
    if set(context) != {"head_sha", "head_tree_sha", "registries"}:
        _reject(SourceInputRejectCode.FIELD_SET_MISMATCH, "registry_context")
    head = _require_oid(context["head_sha"], "registry_context.head_sha")
    tree = _require_oid(context["head_tree_sha"], "registry_context.head_tree_sha")
    if len(head) != len(tree):
        _reject(SourceInputRejectCode.HEAD_MISMATCH, "HEAD and tree formats differ")
    registries = _mapping(context["registries"], "registry_context.registries")
    expected_ids = {"v3": V3_REGISTRY_ID, "v4": V4_REGISTRY_ID, "v5": V5_REGISTRY_ID, "v6": V6_REGISTRY_ID}
    if set(registries) != set(expected_ids):
        _reject(SourceInputRejectCode.FIELD_SET_MISMATCH, "registry_context.registries")
    normalized: dict[str, Any] = {}
    for version, registry_id in expected_ids.items():
        row = _mapping(registries[version], f"registry_context.registries.{version}")
        if set(row) != {"registry_id", "registry_digest", "role_manifest_digest"}:
            _reject(SourceInputRejectCode.FIELD_SET_MISMATCH, f"registry_context.registries.{version}")
        if row["registry_id"] != registry_id:
            _reject(SourceInputRejectCode.REGISTRY_MISMATCH, version)
        normalized[version] = {
            "registry_id": registry_id,
            "registry_digest": _require_digest(row["registry_digest"], f"{version}.registry_digest"),
            "role_manifest_digest": _require_digest(row["role_manifest_digest"], f"{version}.role_manifest_digest"),
        }
    return {"head_sha": head, "head_tree_sha": tree, "registries": normalized}


def _scope(value: Mapping[str, Any], *, name: str, require_scope_id: bool = True) -> None:
    if (
        (require_scope_id and value.get("scope_id") != SCOPE_ID)
        or value.get("coverage_semantics") != COVERAGE_SEMANTICS
        or tuple(value.get("ordered_gaps", ())) != ORDERED_GAPS
        or value.get("next_unchecked_gap") != NEXT_UNCHECKED_GAP
        or value.get("global_exhaustion") is not False
    ):
        _reject(SourceInputRejectCode.SCOPE_MISMATCH, name)


def _validate_v3(value: Any, context: Mapping[str, Any]) -> dict[str, Any]:
    receipt = _sealed_receipt(
        value,
        receipt_type=V3_MISS_TYPE,
        prefix="production-q1-prefix-miss:",
        name="v3_prefix_miss_receipt",
    )
    row = context["registries"]["v3"]
    if (
        receipt.get("outcome") != V3_MISS_OUTCOME
        or receipt.get("head_sha") != context["head_sha"]
        or receipt.get("head_tree_sha") != context["head_tree_sha"]
        or receipt.get("v3_registry_id") != row["registry_id"]
        or receipt.get("v3_registry_digest") != row["registry_digest"]
        or receipt.get("v3_role_manifest_digest") != row["role_manifest_digest"]
    ):
        _reject(SourceInputRejectCode.RECEIPT_MISMATCH, "V3 exact-HEAD binding")
    _scope(receipt, name="V3 registered prefix", require_scope_id=False)
    for field, expected in {
        "source_actualness": True,
        "registered_prefix_miss_authority": True,
        "persistent_admission": False,
        "common_owner_authority": False,
        "e1_authority": False,
        "queue_authority": False,
        "producer_continuation_allowed": False,
        "terminal_leaf_authority": False,
        "global_exhaustion": False,
    }.items():
        _require_bool(receipt.get(field), expected, f"V3.{field}")
    return receipt


def _validate_v4(value: Any, v3: Mapping[str, Any], context: Mapping[str, Any]) -> dict[str, Any]:
    receipt = _sealed_receipt(
        value,
        receipt_type=V4_RECEIPT_TYPE,
        prefix="q1-root-source-scoped-e1:",
        name="v4_consumer_receipt",
    )
    actualness = _mapping(receipt.get("root_actualness"), "V4.root_actualness")
    if (
        receipt.get("terminal_receipt") != v3
        or receipt.get("terminal_receipt_id") != v3["receipt_id"]
        or receipt.get("terminal_receipt_digest") != v3["digest"]
        or actualness.get("head_sha") != context["head_sha"]
        or actualness.get("head_tree_sha") != context["head_tree_sha"]
    ):
        _reject(SourceInputRejectCode.SOURCE_MISMATCH, "V4/V3 source chain")
    _scope(receipt, name="V4 registered prefix")
    for field, expected in {
        "source_actualness": True,
        "common_owner_authority": True,
        "registered_prefix_miss_authority": True,
        "scope_validation_authority": True,
        "root_source_scoped_e1": True,
        "scope_aware_consumer_authority": True,
        "root_source_occurrence_authority": True,
        "e1_authority": False,
        "generic_e1": False,
        "successor_e1": False,
        "producer_authority": False,
        "persistent_admission": False,
        "queue_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "global_exhaustion": False,
    }.items():
        _require_bool(receipt.get(field), expected, f"V4.{field}")
    return receipt


def _validate_v5(value: Any, v4: Mapping[str, Any], v3: Mapping[str, Any], context: Mapping[str, Any]) -> dict[str, Any]:
    receipt = _sealed_receipt(
        value,
        receipt_type=V5_RECEIPT_TYPE,
        prefix="q1-v1-root-base-admission:",
        name="v5_base_admission_receipt",
    )
    materialization = _mapping(receipt.get("materialization_receipt"), "V5.materialization_receipt")
    actualness = _mapping(materialization.get("root_actualness"), "V5.materialization.root_actualness")
    if (
        materialization.get("terminal_receipt") != v3
        or receipt.get("v4_owner_receipt") != v4.get("owner_receipt")
        or receipt.get("v4_scope_receipt") != v4.get("scope_validation_receipt")
        or receipt.get("v4_owner_receipt_id") != v4.get("owner_receipt_id")
        or receipt.get("v4_owner_receipt_digest") != v4.get("owner_receipt_digest")
        or receipt.get("v4_scope_receipt_id") != v4.get("scope_validation_receipt_id")
        or receipt.get("v4_scope_receipt_digest") != v4.get("scope_validation_receipt_digest")
        or actualness.get("head_sha") != context["head_sha"]
        or actualness.get("head_tree_sha") != context["head_tree_sha"]
    ):
        _reject(SourceInputRejectCode.SOURCE_MISMATCH, "V5 source chain")
    for field, expected in {
        "root_base_materialization_authority": False,
        "v1_base_owner_authority": True,
        "root_base_admission_authority": True,
        "persistent_admission": True,
        "queue_authority": False,
        "enqueue_authority": False,
        "enqueue_performed": False,
        "successor_admission": False,
        "producer_authority": False,
        "e1_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "global_exhaustion": False,
    }.items():
        _require_bool(receipt.get(field), expected, f"V5.{field}")
    state_id = _require_content_id(receipt.get("v1_state_id"), "V5.v1_state_id", "state:")
    if receipt.get("v1_state", {}).get("state_id") != state_id:
        _reject(SourceInputRejectCode.SOURCE_MISMATCH, "V5 V1 state ID")
    _require_digest(receipt.get("v1_state_wire_digest"), "V5.v1_state_wire_digest")
    return receipt


def _validate_v6(value: Any, v4: Mapping[str, Any], v5: Mapping[str, Any], context: Mapping[str, Any]) -> dict[str, Any]:
    receipt = _sealed_receipt(
        value,
        receipt_type=V6_RECEIPT_TYPE,
        prefix="q1-root-source-scoped-e1-rebind:",
        name="v6_rebind_receipt",
    )
    if (
        receipt.get("status") != V6_REBIND_STATUS
        or receipt.get("head_sha") != context["head_sha"]
        or receipt.get("head_tree_sha") != context["head_tree_sha"]
        or receipt.get("v4_registry_id") != V4_REGISTRY_ID
        or receipt.get("v5_registry_id") != V5_REGISTRY_ID
        or receipt.get("v4_consumer_receipt") != v4
        or receipt.get("v5_admission_receipt") != v5
        or receipt.get("v4_receipt_id") != v4["receipt_id"]
        or receipt.get("v4_receipt_digest") != v4["digest"]
        or receipt.get("v5_admission_receipt_id") != v5["receipt_id"]
        or receipt.get("v5_admission_receipt_digest") != v5["digest"]
        or receipt.get("v1_source_state_id") != v5.get("v1_state_id")
        or receipt.get("v1_state_wire_digest") != v5.get("v1_state_wire_digest")
        or receipt.get("v1_owner_digest") != v5.get("v1_owner_digest")
    ):
        _reject(SourceInputRejectCode.SOURCE_MISMATCH, "V6 source rebind")
    _scope(receipt, name="V6 registered prefix")
    for field, expected in {
        "v4_root_source_scoped_e1": True,
        "root_source_scoped_e1_rebound": True,
        "source_rebind_authority": True,
        "not_transition": True,
        "generic_e1": False,
        "successor_e1": False,
        "e1_authority": False,
        "producer_authority": False,
        "admission_authority": False,
        "persistent_admission": False,
        "queue_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "t5_ticket_authority": False,
        "reentry_authority": False,
        "global_exhaustion": False,
    }.items():
        _require_bool(receipt.get(field), expected, f"V6.{field}")
    _require_content_id(receipt.get("v2_source_state_id"), "V6.v2_source_state_id", "state:")
    _require_content_id(receipt.get("v1_source_state_id"), "V6.v1_source_state_id", "state:")
    _require_digest(receipt.get("v1_source_state_digest"), "V6.v1_source_state_digest")
    _require_digest(receipt.get("v1_state_wire_digest"), "V6.v1_state_wire_digest")
    _require_content_id(receipt.get("v1_owner_digest"), "V6.v1_owner_digest", "owner:")
    _require_digest(receipt.get("source_facts_digest"), "V6.source_facts_digest")
    _require_digest(receipt.get("source_rebind_map_digest"), "V6.source_rebind_map_digest")
    _require_digest(receipt.get("semantic_origin_exclusion_digest"), "V6.semantic_origin_exclusion_digest")
    return receipt


def _source_preimage(
    *, context: Mapping[str, Any], v3: Mapping[str, Any], v4: Mapping[str, Any], v5: Mapping[str, Any], v6: Mapping[str, Any]
) -> str:
    return canonical_digest_v1(
        {
            "schema_id": "q1_exact_head_source_phase_root_preimage_v1",
            "head_sha": context["head_sha"],
            "head_tree_sha": context["head_tree_sha"],
            "v3_prefix_miss_receipt_id": v3["receipt_id"],
            "v3_prefix_miss_receipt_digest": v3["digest"],
            "v4_consumer_receipt_id": v4["receipt_id"],
            "v4_consumer_receipt_digest": v4["digest"],
            "v5_base_admission_receipt_id": v5["receipt_id"],
            "v5_base_admission_receipt_digest": v5["digest"],
            "v6_rebind_receipt_id": v6["receipt_id"],
            "v6_rebind_receipt_digest": v6["digest"],
            "v6_source_rebind_map_digest": v6["source_rebind_map_digest"],
            "v6_semantic_origin_exclusion_digest": v6["semantic_origin_exclusion_digest"],
            "v1_source_state_id": v6["v1_source_state_id"],
            "v1_state_wire_digest": v6["v1_state_wire_digest"],
        }
    )


def _external_binding_wire(
    *, v1_source_state_id: str, v1_source_wire_digest: str, source_prefix_receipt_digest: str, source_phase_root_preimage_digest: str
) -> dict[str, Any]:
    unsigned = {
        "artifact_type": EXTERNAL_BINDING_TYPE,
        "schema_version": 1,
        "binding_scope": EXTERNAL_BINDING_SCOPE,
        "v1_source_state_id": v1_source_state_id,
        "v1_source_wire_digest": v1_source_wire_digest,
        "source_prefix_receipt_digest": source_prefix_receipt_digest,
        "source_phase_root_preimage_digest": source_phase_root_preimage_digest,
    }
    digest = canonical_digest_v1(unsigned)
    return {**unsigned, "source_binding_id": EXTERNAL_BINDING_ID_PREFIX + digest, "digest": digest}


@dataclass(frozen=True, slots=True)
class ExactHeadQOneActualSourceInputV1:
    ARTIFACT_TYPE: ClassVar[str] = RECEIPT_TYPE
    schema_version: int
    status: str
    binding_scope: str
    role: str
    role_grant: Mapping[str, Any]
    role_grant_id: str
    role_grant_digest: str
    role_artifact_id: str
    role_artifact_semantic_sha256: str
    head_sha: str
    head_tree_sha: str
    v3_registry_id: str
    v3_registry_digest: str
    v3_role_manifest_digest: str
    v4_registry_id: str
    v4_registry_digest: str
    v4_role_manifest_digest: str
    v5_registry_id: str
    v5_registry_digest: str
    v5_role_manifest_digest: str
    v6_registry_id: str
    v6_registry_digest: str
    v6_role_manifest_digest: str
    v3_prefix_miss_receipt: Mapping[str, Any]
    v3_prefix_miss_receipt_id: str
    v3_prefix_miss_receipt_digest: str
    v4_consumer_receipt: Mapping[str, Any]
    v4_consumer_receipt_id: str
    v4_consumer_receipt_digest: str
    v4_owner_receipt_id: str
    v4_owner_receipt_digest: str
    v4_scope_receipt_id: str
    v4_scope_receipt_digest: str
    v5_base_admission_receipt: Mapping[str, Any]
    v5_base_admission_receipt_id: str
    v5_base_admission_receipt_digest: str
    v5_materialization_receipt_id: str
    v5_materialization_receipt_digest: str
    v6_rebind_receipt: Mapping[str, Any]
    v6_rebind_receipt_id: str
    v6_rebind_receipt_digest: str
    v2_source_state_id: str
    v2_source_state_digest: str
    v1_source_state_id: str
    v1_source_state_suffix_digest: str
    v1_source_wire_digest: str
    v1_owner_id: str
    v1_owner_digest: str
    source_facts_digest: str
    source_rebind_map_digest: str
    semantic_origin_exclusion_digest: str
    scope_id: str
    coverage_semantics: str
    ordered_gaps: tuple[int, int, int]
    next_unchecked_gap: int
    global_exhaustion: bool
    source_phase_root_preimage_digest: str
    external_binding_id: str
    external_binding_digest: str
    source_actualness_input: bool
    v1_base_admission_evidence: bool
    v6_rebind_evidence: bool
    generic_e1: bool
    successor_e1: bool
    e1_authority: bool
    producer_authority: bool
    branch_authority: bool
    admission_authority: bool
    queue_authority: bool
    enqueue_authority: bool
    e2_authority: bool
    e3_authority: bool
    e4_authority: bool
    e5_authority: bool
    t5_authority: bool
    reentry_authority: bool
    receipt_id: str
    digest: str


_MAPPING_FIELDS = {"role_grant", "v3_prefix_miss_receipt", "v4_consumer_receipt", "v5_base_admission_receipt", "v6_rebind_receipt"}


def _unsigned(values: Mapping[str, Any]) -> dict[str, Any]:
    result = {"receipt_type": RECEIPT_TYPE}
    for field in fields(ExactHeadQOneActualSourceInputV1):
        if field.name not in {"receipt_id", "digest"}:
            result[field.name] = _copy_json(values[field.name])
    return result


def _construct(values: Mapping[str, Any]) -> ExactHeadQOneActualSourceInputV1:
    normalized: dict[str, Any] = {}
    for field in fields(ExactHeadQOneActualSourceInputV1):
        value = values[field.name]
        if field.name in _MAPPING_FIELDS:
            value = _freeze(value)
        normalized[field.name] = value
    return ExactHeadQOneActualSourceInputV1(**normalized)


def _build_exact_head_q_one_source_input_replay_candidate_v1(
    *, registry_context: dict[str, Any], v3_prefix_miss_receipt: dict[str, Any], v4_consumer_receipt: dict[str, Any], v5_base_admission_receipt: dict[str, Any], v6_rebind_receipt: dict[str, Any], role_grant: dict[str, Any]
) -> ExactHeadQOneActualSourceInputV1:
    """Build a serializable non-authority candidate from a V3--V6 chain.

    The function never emits source authority, including for a caller that has
    independently rebuilt the chain.  Only the separate exact-HEAD replayer's
    runtime result can report that this candidate was verified.
    """

    context = _registry_context(registry_context)
    grant, grant_digest = _grant(role_grant)
    v3 = _validate_v3(v3_prefix_miss_receipt, context)
    v4 = _validate_v4(v4_consumer_receipt, v3, context)
    v5 = _validate_v5(v5_base_admission_receipt, v4, v3, context)
    v6 = _validate_v6(v6_rebind_receipt, v4, v5, context)
    preimage_digest = _source_preimage(context=context, v3=v3, v4=v4, v5=v5, v6=v6)
    external = _external_binding_wire(
        v1_source_state_id=v6["v1_source_state_id"],
        v1_source_wire_digest=v6["v1_state_wire_digest"],
        source_prefix_receipt_digest=v6["v3_terminal_receipt_digest"],
        source_phase_root_preimage_digest=preimage_digest,
    )
    values: dict[str, Any] = {
        "schema_version": 1,
        "status": STATUS,
        "binding_scope": BINDING_SCOPE,
        "role": ROLE,
        "role_grant": grant,
        "role_grant_id": grant["grant_id"],
        "role_grant_digest": grant_digest,
        "role_artifact_id": grant["artifact_id"],
        "role_artifact_semantic_sha256": grant["artifact_semantic_sha256"],
        "head_sha": context["head_sha"],
        "head_tree_sha": context["head_tree_sha"],
        "v3_registry_id": context["registries"]["v3"]["registry_id"],
        "v3_registry_digest": context["registries"]["v3"]["registry_digest"],
        "v3_role_manifest_digest": context["registries"]["v3"]["role_manifest_digest"],
        "v4_registry_id": context["registries"]["v4"]["registry_id"],
        "v4_registry_digest": context["registries"]["v4"]["registry_digest"],
        "v4_role_manifest_digest": context["registries"]["v4"]["role_manifest_digest"],
        "v5_registry_id": context["registries"]["v5"]["registry_id"],
        "v5_registry_digest": context["registries"]["v5"]["registry_digest"],
        "v5_role_manifest_digest": context["registries"]["v5"]["role_manifest_digest"],
        "v6_registry_id": context["registries"]["v6"]["registry_id"],
        "v6_registry_digest": context["registries"]["v6"]["registry_digest"],
        "v6_role_manifest_digest": context["registries"]["v6"]["role_manifest_digest"],
        "v3_prefix_miss_receipt": v3,
        "v3_prefix_miss_receipt_id": v3["receipt_id"],
        "v3_prefix_miss_receipt_digest": v3["digest"],
        "v4_consumer_receipt": v4,
        "v4_consumer_receipt_id": v4["receipt_id"],
        "v4_consumer_receipt_digest": v4["digest"],
        "v4_owner_receipt_id": v4["owner_receipt_id"],
        "v4_owner_receipt_digest": v4["owner_receipt_digest"],
        "v4_scope_receipt_id": v4["scope_validation_receipt_id"],
        "v4_scope_receipt_digest": v4["scope_validation_receipt_digest"],
        "v5_base_admission_receipt": v5,
        "v5_base_admission_receipt_id": v5["receipt_id"],
        "v5_base_admission_receipt_digest": v5["digest"],
        "v5_materialization_receipt_id": v5["materialization_receipt_id"],
        "v5_materialization_receipt_digest": v5["materialization_receipt_digest"],
        "v6_rebind_receipt": v6,
        "v6_rebind_receipt_id": v6["receipt_id"],
        "v6_rebind_receipt_digest": v6["digest"],
        "v2_source_state_id": v6["v2_source_state_id"],
        "v2_source_state_digest": v6["v2_source_state_digest"],
        "v1_source_state_id": v6["v1_source_state_id"],
        "v1_source_state_suffix_digest": v6["v1_source_state_digest"],
        "v1_source_wire_digest": v6["v1_state_wire_digest"],
        "v1_owner_id": v6["v1_owner_digest"],
        "v1_owner_digest": v6["source_owner_digest"],
        "source_facts_digest": v6["source_facts_digest"],
        "source_rebind_map_digest": v6["source_rebind_map_digest"],
        "semantic_origin_exclusion_digest": v6["semantic_origin_exclusion_digest"],
        "scope_id": SCOPE_ID,
        "coverage_semantics": COVERAGE_SEMANTICS,
        "ordered_gaps": ORDERED_GAPS,
        "next_unchecked_gap": NEXT_UNCHECKED_GAP,
        "global_exhaustion": False,
        "source_phase_root_preimage_digest": preimage_digest,
        "external_binding_id": external["source_binding_id"],
        "external_binding_digest": external["digest"],
        "source_actualness_input": False,
        "v1_base_admission_evidence": False,
        "v6_rebind_evidence": False,
        "generic_e1": False,
        "successor_e1": False,
        "e1_authority": False,
        "producer_authority": False,
        "branch_authority": False,
        "admission_authority": False,
        "queue_authority": False,
        "enqueue_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "t5_authority": False,
        "reentry_authority": False,
    }
    digest = canonical_digest_v1(_unsigned(values))
    values.update({"receipt_id": RECEIPT_ID_PREFIX + digest, "digest": digest})
    result = _construct(values)
    _validate_result(result)
    return result


def _validate_result(receipt: ExactHeadQOneActualSourceInputV1) -> None:
    if type(receipt) is not ExactHeadQOneActualSourceInputV1:
        _reject(SourceInputRejectCode.MALFORMED_INPUT, "wrong wrapper type")
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    digest = canonical_digest_v1(_unsigned(values))
    if receipt.digest != digest or receipt.receipt_id != RECEIPT_ID_PREFIX + digest:
        _reject(SourceInputRejectCode.DIGEST_MISMATCH, "wrapper seal")
    if (
        receipt.schema_version != 1
        or receipt.status != STATUS
        or receipt.binding_scope != BINDING_SCOPE
        or receipt.role != ROLE
        or receipt.scope_id != SCOPE_ID
        or receipt.coverage_semantics != COVERAGE_SEMANTICS
        or receipt.ordered_gaps != ORDERED_GAPS
        or receipt.next_unchecked_gap != NEXT_UNCHECKED_GAP
        or receipt.global_exhaustion is not False
    ):
        _reject(SourceInputRejectCode.RECEIPT_MISMATCH, "wrapper fixed boundary")
    for name, expected in {
        "source_actualness_input": False,
        "v1_base_admission_evidence": False,
        "v6_rebind_evidence": False,
        "generic_e1": False,
        "successor_e1": False,
        "e1_authority": False,
        "producer_authority": False,
        "branch_authority": False,
        "admission_authority": False,
        "queue_authority": False,
        "enqueue_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "t5_authority": False,
        "reentry_authority": False,
    }.items():
        _require_bool(getattr(receipt, name), expected, name)


def bind_exact_head_q_one_actual_source_input_v1(
    *, registry_context: dict[str, Any], v3_prefix_miss_receipt: dict[str, Any], v4_consumer_receipt: dict[str, Any], v5_base_admission_receipt: dict[str, Any], v6_rebind_receipt: dict[str, Any], role_grant: dict[str, Any]
) -> ExactHeadQOneActualSourceInputV1:
    """Build a self-contained non-authority replay candidate.

    The caller is responsible for treating the result as untrusted data.  A
    consumer that needs exact-HEAD authentication must invoke the independent
    replayer; no serializable candidate wire carries that conclusion.
    """

    return _build_exact_head_q_one_source_input_replay_candidate_v1(
        registry_context=registry_context,
        v3_prefix_miss_receipt=v3_prefix_miss_receipt,
        v4_consumer_receipt=v4_consumer_receipt,
        v5_base_admission_receipt=v5_base_admission_receipt,
        v6_rebind_receipt=v6_rebind_receipt,
        role_grant=role_grant,
    )


def exact_head_q_one_actual_source_input_to_mapping_v1(
    receipt: ExactHeadQOneActualSourceInputV1,
) -> dict[str, Any]:
    _validate_result(receipt)
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    result = _unsigned(values)
    result["receipt_id"] = receipt.receipt_id
    result["digest"] = receipt.digest
    return result


def parse_exact_head_q_one_actual_source_input_v1(value: Any) -> ExactHeadQOneActualSourceInputV1:
    del value
    _reject(
        SourceInputRejectCode.AUTHORITY_MISMATCH,
        "candidate wires require independent exact-HEAD replay, not public parsing",
    )


def _candidate_external_binding_wire_from_exact_head_source_input_v1(
    source_input: ExactHeadQOneActualSourceInputV1,
) -> dict[str, Any]:
    """Internal V2 projection for a candidate rebuilt in a replay process."""

    if type(source_input) is not ExactHeadQOneActualSourceInputV1:
        _reject(SourceInputRejectCode.MALFORMED_INPUT, "internal projection wrapper type")
    _validate_result(source_input)
    wire = _external_binding_wire(
        v1_source_state_id=source_input.v1_source_state_id,
        v1_source_wire_digest=source_input.v1_source_wire_digest,
        source_prefix_receipt_digest=source_input.v3_prefix_miss_receipt_digest,
        source_phase_root_preimage_digest=source_input.source_phase_root_preimage_digest,
    )
    if wire["source_binding_id"] != source_input.external_binding_id or wire["digest"] != source_input.external_binding_digest:
        _reject(SourceInputRejectCode.DIGEST_MISMATCH, "ExternalQOneSourceBindingV2 projection")
    return wire


def external_binding_wire_from_exact_head_source_input_v1(
    _source_input: ExactHeadQOneActualSourceInputV1 | Mapping[str, Any],
) -> dict[str, Any]:
    """Reject public projection of caller-supplied source evidence.

    The zero-authority V2 shell must receive its values only after the exact
    controlled orchestrator or independent replayer has rebuilt the complete
    source chain.  Keeping this former public convenience function as a hard
    rejection prevents a self-sealed chain from becoming a source-input path.
    """

    _reject(SourceInputRejectCode.AUTHORITY_MISMATCH, "public V2 projection is disabled")


__all__ = [
    "ARTIFACT_ID",
    "ARTIFACT_PATH",
    "ARTIFACT_SYMBOLS",
    "AUTHORITY_CLASS",
    "BINDING_SCOPE",
    "CAPABILITIES",
    "ExactHeadQOneSourceInputError",
    "ExactHeadQOneActualSourceInputV1",
    "GRANT_ID",
    "ROLE",
    "SourceInputRejectCode",
    "bind_exact_head_q_one_actual_source_input_v1",
    "canonical_digest_v1",
    "exact_head_q_one_actual_source_input_to_mapping_v1",
]
