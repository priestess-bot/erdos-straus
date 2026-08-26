#!/usr/bin/env python3
"""Rebind the narrow V4 q=1 root occurrence to a V5 V1 base source.

This is deliberately a source-side bridge, not a successor constructor.  V4
describes an actual ``RawRootSourceStateV2`` occurrence and V5 independently
admits a newly materialized ``ROOT_INITIALIZER_OUTPUT`` state.  Their content
addresses are necessarily different.  This module proves that the two receipts
describe the same root and emits a namespaced sidecar whose candidate is bound
to the V1 source ID.  It never changes the V1 state or its semantic origin.

The result is not a generic E1 receipt.  In particular V4 has only a
registered-prefix MISS, whereas the generic structured E1 contract requires
``MISS_COMPLETE``.  No producer, successor, target, T5 ticket, queue, or
re-entry authority is issued here.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass, fields
from enum import Enum
from math import gcd
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, NoReturn

import t6_persistent_selector_state_v1 as state_contract
import t6_q_one_root_initializer_envelope_v2 as root_envelope


ARTIFACT_ID = "q1_root_source_scoped_e1_rebind_v1"
ARTIFACT_PATH = "scripts/t6_q_one_root_source_scoped_e1_rebind_v1.py"
ARTIFACT_SYMBOLS = (
    "rebind_q_one_root_source_scoped_e1_v1",
    "root_source_scoped_e1_rebind_receipt_to_mapping_v1",
)
ROLE = "INDEPENDENT_Q1_ROOT_SOURCE_SCOPED_E1_REBINDER"
GRANT_ID = "q1_root_source_scoped_e1_rebind_grant_v1"
CAPABILITIES = ("REBIND_ROOT_SOURCE_SCOPED_E1_TO_V1_BASE_SOURCE",)
AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V6"

RECEIPT_TYPE = "Q1_ROOT_SOURCE_SCOPED_E1_REBIND_RECEIPT_V1"
RECEIPT_ID_PREFIX = "q1-root-source-scoped-e1-rebind:"
STATUS = "ROOT_SOURCE_SCOPED_E1_REBOUND_TO_V1_BASE_NO_SUCCESSOR"

V4_RECEIPT_TYPE = "Q1_REGISTERED_PREFIX_ROOT_SOURCE_E1_RECEIPT_V2"
V4_RECEIPT_ID_PREFIX = "q1-root-source-scoped-e1:"
V5_RECEIPT_TYPE = "Q1_ROOT_V1_BASE_ADMISSION_RECEIPT_V1"
V5_RECEIPT_ID_PREFIX = "q1-v1-root-base-admission:"
V5_MATERIALIZATION_TYPE = "Q1_ROOT_V1_BASE_MATERIALIZATION_RECEIPT_V1"
V5_MATERIALIZATION_ID_PREFIX = "q1-v1-root-materialization:"
V5_TERMINAL_PROJECTION_TYPE = "Q1_V3_MISS_TO_V1_TERMINAL_FIRST_PROJECTION_V1"
V5_TERMINAL_PROJECTION_ID_PREFIX = "q1-v1-terminal-projection:"

V3_MISS_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
V3_MISS_ID_PREFIX = "production-q1-prefix-miss:"
V4_OWNER_TYPE = "COMMON_Q1_ROOT_OWNER_RECEIPT_V2"
V4_OWNER_ID_PREFIX = "q1-common-root-owner:"
V4_SCOPE_TYPE = "Q1_REGISTERED_PREFIX_SCOPE_VALIDATION_RECEIPT_V2"
V4_SCOPE_ID_PREFIX = "q1-prefix-scope-validation:"

V4_REGISTRY_ID = "t6_coordinator_role_registry_v4"
V5_REGISTRY_ID = "t6_coordinator_role_registry_v5"
OWNER = "type_ii_relation_g_endpoint"
SCOPE_ID = "q1_root_after_gap_3_7_11_registered_prefix_v1"
COVERAGE_SEMANTICS = "REGISTERED_PRIORITY_ONLY"
ORDERED_GAPS = (3, 7, 11)
NEXT_UNCHECKED_GAP = 15
PHASE_ROOT_MATH_ID = "q1_full_carrier_phase_root_math_replay_v1"
REPRESENTATION_NAMESPACE = "Q1_ROOT_SOURCE_SCOPED_E1_REBIND_V1"
PATH_SEMANTICS = "DERIVED_WITNESS_NOT_V1_STATE_PATH"
DIGEST_DOMAIN_STATE_ID_SUFFIX = "STATE_ID_SUFFIX_SHA256_V1"
DIGEST_DOMAIN_STATE_WIRE = "FULL_V1_STATE_WIRE_SHA256_V1"
DIGEST_DOMAIN_V4_CANDIDATE = "V4_CANDIDATE_WITNESS_CANONICAL_JSON_V2"

V4_FIELDS = frozenset(
    {
        "receipt_type", "schema_version", "status", "role", "role_grant",
        "role_grant_id", "role_grant_digest", "role_artifact_id",
        "role_artifact_semantic_sha256", "raw_q_one_g", "raw_q_one_g_digest",
        "source_body", "body_id", "body_digest", "root_anchor", "anchor_id",
        "anchor_digest", "source_state", "state_id", "state_digest",
        "root_actualness", "root_actualness_id", "root_actualness_digest",
        "owner_receipt", "owner_receipt_id", "owner_receipt_digest",
        "terminal_receipt", "terminal_receipt_id", "terminal_receipt_digest",
        "scope_validation_receipt", "scope_validation_receipt_id",
        "scope_validation_receipt_digest", "scope_id", "coverage_semantics",
        "ordered_gaps", "next_unchecked_gap", "global_exhaustion",
        "terminal_receipt_direct_continuation_authority",
        "scope_aware_consumer_authority", "root_source_occurrence_authority",
        "candidate_witness", "candidate_witness_digest", "math_replay_id",
        "math_replay", "math_replay_digest", "parent_kind", "occurrence_path",
        "occurrence_value_digest", "source_actualness", "common_owner_authority",
        "registered_prefix_miss_authority", "scope_validation_authority",
        "root_source_scoped_e1", "e1_authority", "generic_e1",
        "successor_e1", "producer_authority", "producer_continuation_allowed",
        "persistent_admission", "queue_authority", "e2_authority",
        "e3_authority", "e4_authority", "e5_authority",
        "terminal_leaf_authority", "root_proof_close_authority", "receipt_id",
        "digest",
    }
)

V5_FIELDS = frozenset(
    {
        "receipt_type", "schema_version", "status", "role", "role_grant",
        "role_grant_id", "role_grant_digest", "role_artifact_id",
        "role_artifact_semantic_sha256", "materialization_receipt",
        "materialization_receipt_id", "materialization_receipt_digest",
        "v4_owner_receipt", "v4_owner_receipt_id", "v4_owner_receipt_digest",
        "v4_scope_receipt", "v4_scope_receipt_id", "v4_scope_receipt_digest",
        "source_state_id", "source_state_digest", "v1_contract_id",
        "v1_state_schema_id", "v1_state_schema_version", "v1_state",
        "v1_state_id", "v1_state_wire_digest",
        "canonical_root_potential_evidence",
        "canonical_root_potential_evidence_digest",
        "local_grant_authenticates_head", "repository_authority", "producer_rule",
        "producer_rule_digest", "verified_header", "verified_header_digest",
        "family_precedence", "family_precedence_digest", "predicate_results",
        "predicate_results_digest", "matched_families", "owner", "precedence_index",
        "v4_owner_id", "v4_owner_digest", "v1_owner_digest",
        "owner_translation_binding_digest", "admission_decision", "admission_reason",
        "root_base_materialization_authority", "v1_base_owner_authority",
        "root_base_admission_authority", "persistent_admission", "queue_authority",
        "enqueue_authority", "enqueue_performed", "successor_admission",
        "producer_authority", "producer_continuation_allowed",
        "generic_owner_authority", "e1_authority", "e2_authority",
        "e3_authority", "e4_authority", "e5_authority", "t5_ticket_authority",
        "t5_potential_authority", "global_exhaustion", "terminal_leaf_authority",
        "receipt_id", "digest",
    }
)

MATERIALIZATION_FIELDS = frozenset(
    {
        "receipt_type", "schema_version", "status", "role", "role_grant",
        "role_grant_id", "role_grant_digest", "role_artifact_id",
        "role_artifact_semantic_sha256", "raw_q_one_g", "raw_q_one_g_digest",
        "source_body", "body_id", "body_digest", "root_anchor", "anchor_id",
        "anchor_digest", "source_state", "source_state_id", "source_state_digest",
        "root_actualness", "root_actualness_id", "root_actualness_digest",
        "terminal_receipt", "terminal_receipt_id", "terminal_receipt_digest",
        "terminal_projection", "terminal_projection_id", "terminal_projection_digest",
        "producer_rule", "producer_rule_digest", "semantic_origin_digest",
        "v1_state", "v1_state_id", "v1_state_wire_digest",
        "canonical_root_potential_evidence",
        "canonical_root_potential_evidence_digest",
        "local_grant_authenticates_head", "repository_authority",
        "root_base_materialization_authority", "v1_base_owner_authority",
        "root_base_admission_authority", "persistent_admission", "queue_authority",
        "enqueue_authority", "enqueue_performed", "successor_admission",
        "producer_authority", "producer_continuation_allowed", "e1_authority",
        "e2_authority", "e3_authority", "e4_authority", "e5_authority",
        "t5_ticket_authority", "t5_potential_authority", "global_exhaustion",
        "terminal_leaf_authority", "receipt_id", "digest",
    }
)

CANDIDATE_FIELDS = frozenset(
    {
        "source_state_id", "source_state_digest", "parent_kind", "owner",
        "owner_id", "owner_digest", "scope_id", "coverage_semantics",
        "terminal_receipt_id", "terminal_receipt_digest", "math_replay_id",
        "math_replay_digest", "target_phase", "target_protocol",
        "target_provenance", "target_scope", "source", "target_anchor",
    }
)

MATH_FIELDS = frozenset(
    {
        "math_replay_id", "root_context", "t", "x", "chart_r", "chart_k",
        "support_a", "fresh_source", "target_anchor", "edge_prime",
        "edge_shift", "gcd_reduction", "source_phase", "target_phase",
        "target_protocol", "target_provenance", "mark_kind", "ticket",
        "admission_ticket_issued", "digest",
    }
)

GRANT_FIELDS = frozenset(
    {
        "grant_id", "role", "artifact_id", "artifact_path", "artifact_symbols",
        "capabilities", "authority_class", "artifact_semantic_sha256",
    }
)

# These are the reviewed V4/V5 registry grant wires.  A pure rebind role has
# no Git loader and therefore cannot discover a new authority manifest at
# runtime; changing any of these pins is a new V6 policy and must be reviewed.
EXPECTED_V4_GRANTS = {
    "COMMON_ROOT_OWNER_CLASSIFIER": {
        "grant_id": "q1_common_root_owner_classifier_grant_v4",
        "role": "COMMON_ROOT_OWNER_CLASSIFIER",
        "artifact_id": "q1_root_owner_classifier_v2",
        "artifact_path": "scripts/t6_q_one_root_owner_classifier_v2.py",
        "artifact_symbols": ["classify_q_one_root_owner_v2", "root_owner_receipt_to_mapping_v2"],
        "capabilities": ["CLASSIFY_COMMON_Q1_ROOT_OWNER"],
        "authority_class": "HEAD_BOUND_EXECUTABLE_CAPABILITY_V4",
        "artifact_semantic_sha256": "4d99732d962c35a7d0ef7ad994d2be27b33e9e7a80ee655805979c0392942c28",
    },
    "INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR": {
        "grant_id": "q1_scope_aware_e1_validator_grant_v4",
        "role": "INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR",
        "artifact_id": "q1_scope_aware_e1_validator_v2",
        "artifact_path": "scripts/t6_q_one_scope_aware_e1_validator_v2.py",
        "artifact_symbols": ["validate_q_one_registered_prefix_e1_scope_v2", "scope_validation_receipt_to_mapping_v2"],
        "capabilities": ["VALIDATE_REGISTERED_PREFIX_ROOT_SOURCE_E1_SCOPE"],
        "authority_class": "HEAD_BOUND_EXECUTABLE_CAPABILITY_V4",
        "artifact_semantic_sha256": "b692e6e5f3d12089f5abeedd024cba02d497a438ec31dba1e91865a6754dcc0f",
    },
    "REGISTERED_PREFIX_E1_CONSUMER": {
        "grant_id": "q1_registered_prefix_e1_consumer_grant_v4",
        "role": "REGISTERED_PREFIX_E1_CONSUMER",
        "artifact_id": "q1_registered_prefix_e1_consumer_v2",
        "artifact_path": "scripts/t6_q_one_registered_prefix_e1_consumer_v2.py",
        "artifact_symbols": ["consume_q_one_registered_prefix_miss_for_e1_v2", "root_source_scoped_e1_receipt_to_mapping_v2"],
        "capabilities": ["ISSUE_REGISTERED_PREFIX_ROOT_SOURCE_SCOPED_E1"],
        "authority_class": "HEAD_BOUND_EXECUTABLE_CAPABILITY_V4",
        "artifact_semantic_sha256": "0745b05f36cb9d62cd3835aa343dcf8eba926094f8cd98c351d30535111baecc",
    },
}
EXPECTED_V5_GRANTS = {
    "INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER": {
        "grant_id": "q1_root_v1_base_admission_verifier_grant_v1",
        "role": "INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER",
        "artifact_id": "q1_root_v1_base_admission_verifier_v1",
        "artifact_path": "scripts/t6_q_one_root_v1_base_admission_verifier_v1.py",
        "artifact_symbols": ["verify_and_admit_q_one_root_v1_base_v1", "base_admission_receipt_to_mapping_v1"],
        "capabilities": ["ISSUE_Q1_G_V1_BASE_ADMISSION_NO_QUEUE"],
        "authority_class": "HEAD_BOUND_EXECUTABLE_CAPABILITY_V5",
        "artifact_semantic_sha256": "4fda677482ad484324281e49b1954de1ecfe1b04171aa582b5be767efd19e386",
    },
    "Q1_ROOT_V1_BASE_MATERIALIZER": {
        "grant_id": "q1_root_v1_base_materializer_grant_v1",
        "role": "Q1_ROOT_V1_BASE_MATERIALIZER",
        "artifact_id": "q1_root_v1_base_materializer_v1",
        "artifact_path": "scripts/t6_q_one_root_v1_base_materializer_v1.py",
        "artifact_symbols": ["materialize_q_one_root_v1_base_state_v1", "base_materialization_receipt_to_mapping_v1"],
        "capabilities": ["MATERIALIZE_Q1_G_V1_ROOT_INITIALIZER_OUTPUT"],
        "authority_class": "HEAD_BOUND_EXECUTABLE_CAPABILITY_V5",
        "artifact_semantic_sha256": "6ea92f3962e4a25a58ed22cb32c54eadffbc7051f58fec69d361a71b072f92d9",
    },
}

FORBIDDEN_V1_CANDIDATE_KEYS = frozenset(
    {
        "v4_e1_receipt", "v4_e1_candidate", "v4_e1_candidate_digest",
        "v4_root_source_scoped_e1", "v4_consumer_receipt", "candidate_witness",
        "candidate_witness_digest", "math_replay", "math_replay_digest",
        "rebound_candidate_witness", "source_rebind_map",
    }
)


class RebindRejectCode(str, Enum):
    INPUT_NOT_EXACT_MAPPING = "INPUT_NOT_EXACT_MAPPING"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    HEAD_MISMATCH = "HEAD_MISMATCH"
    SOURCE_BINDING_MISMATCH = "SOURCE_BINDING_MISMATCH"
    V4_RECEIPT_MISMATCH = "V4_RECEIPT_MISMATCH"
    V5_RECEIPT_MISMATCH = "V5_RECEIPT_MISMATCH"
    TERMINAL_SOURCE_NOT_MISS = "TERMINAL_SOURCE_NOT_MISS"
    SCOPE_MISMATCH = "SCOPE_MISMATCH"
    OWNER_MISMATCH = "OWNER_MISMATCH"
    V1_STATE_MISMATCH = "V1_STATE_MISMATCH"
    CANDIDATE_MISMATCH = "CANDIDATE_MISMATCH"
    POTENTIAL_MISMATCH = "POTENTIAL_MISMATCH"
    SEMANTIC_ORIGIN_MISMATCH = "SEMANTIC_ORIGIN_MISMATCH"
    AUTHORITY_BOUNDARY_VIOLATION = "AUTHORITY_BOUNDARY_VIOLATION"


class RootSourceScopedE1RebindError(ValueError):
    def __init__(self, code: RebindRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: RebindRejectCode, detail: str) -> NoReturn:
    raise RootSourceScopedE1RebindError(code, detail)


def _json_copy(value: Any, *, path: str = "$") -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(RebindRejectCode.MALFORMED_FIELD, f"{path} has a non-string key")
            result[key] = _json_copy(child, path=f"{path}.{key}")
        return result
    if type(value) is list or type(value) is tuple:
        return [_json_copy(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(RebindRejectCode.MALFORMED_FIELD, f"{path} contains {type(value).__name__}")


def canonical_json_v1(value: Any) -> str:
    try:
        return json.dumps(
            _json_copy(value), ensure_ascii=True, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise RootSourceScopedE1RebindError(RebindRejectCode.MALFORMED_FIELD, str(exc)) from exc


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


def _is_digest(value: Any) -> bool:
    return type(value) is str and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def _is_nonzero_digest(value: Any) -> bool:
    return _is_digest(value) and value != "0" * 64


def _is_oid(value: Any) -> bool:
    return type(value) is str and len(value) in {40, 64} and all(c in "0123456789abcdef" for c in value) and value != "0" * len(value)


def _exact_mapping(value: Any, expected: frozenset[str], name: str) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(RebindRejectCode.INPUT_NOT_EXACT_MAPPING, f"{name} must be an exact dict")
    observed = frozenset(value)
    if observed != expected:
        _reject(
            RebindRejectCode.FIELD_SET_MISMATCH,
            f"{name} missing={sorted(expected-observed)} extra={sorted(observed-expected)}",
        )
    return _json_copy(value, path=name)


def _mapping(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        _reject(RebindRejectCode.INPUT_NOT_EXACT_MAPPING, f"{name} must be a mapping")
    return _json_copy(value, path=name)


def _verify_seal(value: Mapping[str, Any], *, id_field: str, prefix: str, name: str) -> None:
    digest = value.get("digest")
    if not _is_digest(digest) or value.get(id_field) != prefix + digest:
        _reject(RebindRejectCode.DIGEST_MISMATCH, f"{name} content ID/digest is malformed")
    unsigned = _json_copy(value, path=name)
    unsigned.pop(id_field, None)
    unsigned.pop("digest", None)
    if canonical_digest_v1(unsigned) != digest:
        _reject(RebindRejectCode.DIGEST_MISMATCH, f"{name} content seal does not replay")


def _grant(value: Any) -> tuple[dict[str, Any], str]:
    grant = _exact_mapping(value, GRANT_FIELDS, "role_grant")
    expected = {
        "grant_id": GRANT_ID,
        "role": ROLE,
        "artifact_id": ARTIFACT_ID,
        "artifact_path": ARTIFACT_PATH,
        "artifact_symbols": list(ARTIFACT_SYMBOLS),
        "capabilities": list(CAPABILITIES),
        "authority_class": AUTHORITY_CLASS,
    }
    if any(grant.get(key) != item for key, item in expected.items()) or not _is_nonzero_digest(grant.get("artifact_semantic_sha256")):
        _reject(RebindRejectCode.MALFORMED_FIELD, "rebind role grant changed")
    return grant, canonical_digest_v1(grant)


def _registry_grant(value: Any, *, role: str, version: int) -> dict[str, Any]:
    """Validate a nested V4/V5 grant against the reviewed registry wire."""

    grant = _mapping(value, f"{version}.{role}.role_grant")
    expected = (EXPECTED_V4_GRANTS if version == 4 else EXPECTED_V5_GRANTS).get(role)
    if expected is None or grant != expected:
        _reject(
            RebindRejectCode.V4_RECEIPT_MISMATCH if version == 4 else RebindRejectCode.V5_RECEIPT_MISMATCH,
            f"{version} role grant {role!r} is not the reviewed registry grant",
        )
    return grant


def _grant_parity(receipt: Mapping[str, Any], grant: Mapping[str, Any], name: str) -> None:
    expected_digest = canonical_digest_v1(grant)
    if not (
        receipt.get("role_grant_id") == grant.get("grant_id")
        and receipt.get("role_grant_digest") == expected_digest
        and receipt.get("role_artifact_id") == grant.get("artifact_id")
        and receipt.get("role_artifact_semantic_sha256") == grant.get("artifact_semantic_sha256")
    ):
        _reject(RebindRejectCode.V4_RECEIPT_MISMATCH if name.startswith("v4") else RebindRejectCode.V5_RECEIPT_MISMATCH, f"{name} role grant references changed")


def _source_chain(
    raw_value: Any, body_value: Any, anchor_value: Any, state_value: Any
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    raw = _mapping(raw_value, "raw_q_one_g")
    body_wire = _mapping(body_value, "source_body")
    anchor_wire = _mapping(anchor_value, "root_anchor")
    state_wire = _mapping(state_value, "source_state")
    try:
        body = root_envelope.parse_canonical_q_one_g_source_body_v2(body_wire, raw)
        anchor = root_envelope.parse_root_initializer_anchor_v2(anchor_wire, body)
        state = root_envelope.parse_raw_root_source_state_v2(state_wire, body, anchor)
    except Exception as exc:
        _reject(RebindRejectCode.SOURCE_BINDING_MISMATCH, f"V2 source chain did not replay: {exc}")
    return (
        raw,
        root_envelope.artifact_to_mapping_v2(body),
        root_envelope.artifact_to_mapping_v2(anchor),
        root_envelope.artifact_to_mapping_v2(state),
    )


def _factor(value: int) -> list[list[int]]:
    if type(value) is not int or value < 1:
        _reject(RebindRejectCode.MALFORMED_FIELD, "factorization input is invalid")
    result: list[list[int]] = []
    divisor, remaining = 2, value
    while divisor * divisor <= remaining:
        if remaining % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        result.append([divisor, exponent])
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        result.append([remaining, 1])
    return result


def _divisors(factors: list[list[int]]) -> list[int]:
    result = [1]
    for prime, exponent in factors:
        result = [base * prime**power for base in result for power in range(2 * exponent + 1)]
    return sorted(set(result))


def _certificate(p: int, gap: int, x: int, divisor: int, index: int, kind: str) -> dict[str, Any] | None:
    quotient = x * x // divisor
    if kind == "TYPE_I":
        if (p * x + divisor) % gap or p * (x + p * quotient) % gap:
            return None
        y, z, candidate_index = (p * x + divisor) // gap, p * (x + p * quotient) // gap, 2 * index
    else:
        if divisor > x or (x + divisor) % gap or p * (x + divisor) % gap or p * (x + quotient) % gap:
            return None
        y, z, candidate_index = p * (x + divisor) // gap, p * (x + quotient) // gap, 2 * index + 1
    if 4 * x * y * z != p * (x * y + x * z + y * z):
        return None
    return {
        "certificate_type": kind, "gap": gap, "x": x, "divisor": divisor,
        "y": y, "z": z, "candidate_index": candidate_index,
    }


def _scan_gap(p: int, gap: int) -> dict[str, Any]:
    x = (p + gap) // 4
    factors = _factor(x)
    divisors = _divisors(factors)
    matches: list[dict[str, Any]] = []
    for index, divisor in enumerate(divisors):
        for kind in ("TYPE_I", "TYPE_II"):
            certificate = _certificate(p, gap, x, divisor, index, kind)
            if certificate is not None:
                matches.append(certificate)
    unsigned = {
        "gap": gap, "x": x, "factorization": factors, "divisor_universe": divisors,
        "matching_certificates": matches,
        "scan_status": "GAP_HAS_TERMINAL" if matches else "GAP_PREFIX_MISS",
    }
    return {**unsigned, "scan_digest": canonical_digest_v1(unsigned)}


def _validate_actualness(actual: Mapping[str, Any], state: Mapping[str, Any], raw: Mapping[str, Any], body: Mapping[str, Any], anchor: Mapping[str, Any]) -> tuple[str, str]:
    actualness_id = actual.get("actualness_id")
    digest = actual.get("digest")
    if not _is_digest(digest) or actualness_id != "q1-root-source-actualness:" + digest:
        _reject(RebindRejectCode.DIGEST_MISMATCH, "root actualness seal is malformed")
    unsigned = _json_copy(actual, path="root_actualness")
    unsigned.pop("actualness_id", None)
    unsigned.pop("digest", None)
    if canonical_digest_v1(unsigned) != digest:
        _reject(RebindRejectCode.DIGEST_MISMATCH, "root actualness seal does not replay")
    if not (
        actual.get("state_id") == state["state_id"]
        and actual.get("state_digest") == state["digest"]
        and actual.get("body_id") == body["body_id"]
        and actual.get("body_digest") == body["digest"]
        and actual.get("anchor_id") == anchor["anchor_id"]
        and actual.get("anchor_digest") == anchor["digest"]
        and actual.get("raw_q_one_g") == raw
        and actual.get("raw_q_one_g_digest") == canonical_digest_v1(raw)
        and actual.get("source_actualness") is True
        and actual.get("root_initializer_authority") is True
        and actual.get("persistent_admission") is False
        and actual.get("queue_authority") is False
        and actual.get("e1_authority") is False
    ):
        _reject(RebindRejectCode.SOURCE_BINDING_MISMATCH, "actualness does not bind the V2 root")
    head, tree = actual.get("head_sha"), actual.get("head_tree_sha")
    if not (_is_oid(head) and _is_oid(tree) and len(head) == len(tree)):
        _reject(RebindRejectCode.HEAD_MISMATCH, "actualness HEAD binding is malformed")
    return head, tree


def _validate_terminal(terminal: Mapping[str, Any], actual: Mapping[str, Any], state: Mapping[str, Any], p: int) -> None:
    _verify_seal(terminal, id_field="receipt_id", prefix=V3_MISS_ID_PREFIX, name="V3 terminal")
    if not (
        terminal.get("receipt_type") == V3_MISS_TYPE
        and terminal.get("outcome") == "MISS_REGISTERED_PRIORITY_COMPLETE"
        and terminal.get("coverage_semantics") == COVERAGE_SEMANTICS
        and terminal.get("ordered_gaps") == list(ORDERED_GAPS)
        and terminal.get("next_unchecked_gap") == NEXT_UNCHECKED_GAP
        and terminal.get("global_exhaustion") is False
        and terminal.get("selected_certificate") is None
        and terminal.get("selected_certificate_digest") is None
        and terminal.get("registered_prefix_miss_authority") is True
        and terminal.get("terminal_leaf_authority") is False
        and terminal.get("root_proof_close_authority") is False
        and terminal.get("state_id") == state["state_id"]
        and terminal.get("state_digest") == state["digest"]
        and terminal.get("root_context") == p
        and terminal.get("root_actualness_digest") == actual["digest"]
        and terminal.get("root_actualness", {}).get("actualness_id") == actual["actualness_id"]
        and terminal.get("head_sha") == actual["head_sha"]
        and terminal.get("head_tree_sha") == actual["head_tree_sha"]
    ):
        _reject(RebindRejectCode.TERMINAL_SOURCE_NOT_MISS, "terminal is not the exact V3 registered-prefix MISS")


def _v4_header(state: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "state_id": state["state_id"], "state_digest": state["digest"],
        "root_context": state["root_context"], "equation_rank": state["equation_rank"],
        "mark_kind": "ROOT_SOL", "mark_root_context": state["mark_root_context"],
        "mark_equation_rank": state["mark_equation_rank"],
        "facts": {
            "major_phase": "TYPEII_G_HANDOFF", "type_i_protocol": None,
            "t5_eta_p": 0, "pre_a": None, "absorb_m": None,
            "absorb_r_epsilon": 0, "reset_carrier": None,
            "endpoint_fiber": "G", "relation_q": 1,
            "provenance_kind": "ORDINARY_ENDPOINT", "full_carrier_scope": False,
            "atomic_arm": "NONE", "dispatch_status": "NONE",
            "proper_root_k": None, "proper_root_height_class": "NONE",
            "proper_root_height": None, "proper_root_r": None,
            "is_overflow": False, "support_A": None, "carrier_M": None,
            "overflow_d": None, "chart_R": None, "chart_K": None,
            "sink_scc_receipt": False, "same_chart_promotion_receipt": False,
        },
    }


def _v4_owner_expected(state: Mapping[str, Any]) -> tuple[dict[str, Any], str, dict[str, bool]]:
    header = _v4_header(state)
    facts = state_contract._validate_facts(header["facts"], header["root_context"], state_contract.ROOT_SOL)
    reference = state_contract.VerifiedSelectorHeaderV1(
        state_id=state["state_id"], queue_gate=state_contract.ROOT_INITIALIZER_OUTPUT,
        producer_id="v4_reference_equivalence_only", branch_id="q1_g_root",
        parent_state_id=None, root_context=header["root_context"],
        equation_rank=header["equation_rank"], mark_kind=state_contract.ROOT_SOL,
        mark_receipt_digest="0" * 64, terminal_first_digest="1" * 64,
        source_receipt_digest="2" * 64,
        facts_digest=state_contract.canonical_digest_v1(dict(facts)), facts=facts,
    )
    classified = state_contract.classify_selector_owner_v1(reference)
    predicates = {item.family_id: bool(item.predicate(reference)) for item in state_contract.FAMILY_PREDICATES_V1}
    if classified.owner != OWNER or classified.precedence_index != 2:
        _reject(RebindRejectCode.OWNER_MISMATCH, "V4 source no longer has the unique G owner")
    return header, classified.owner_digest, predicates


def _validate_v4_owner(owner: Mapping[str, Any], *, raw: Mapping[str, Any], body: Mapping[str, Any], anchor: Mapping[str, Any], state: Mapping[str, Any], actual: Mapping[str, Any]) -> None:
    _verify_seal(owner, id_field="receipt_id", prefix=V4_OWNER_ID_PREFIX, name="V4 owner")
    header, owner_id, predicates = _v4_owner_expected(state)
    bare = owner_id.removeprefix("owner:")
    if not (
        owner.get("receipt_type") == V4_OWNER_TYPE
        and owner.get("schema_version") == 2
        and owner.get("status") == "COMMON_OWNER_CLASSIFIED"
        and owner.get("role") == "COMMON_ROOT_OWNER_CLASSIFIER"
        and owner.get("raw_q_one_g") == raw and owner.get("source_body") == body
        and owner.get("root_anchor") == anchor and owner.get("source_state") == state
        and owner.get("root_actualness") == actual
        and owner.get("normalized_header") == header
        and owner.get("normalized_header_digest") == canonical_digest_v1(header)
        and owner.get("facts_digest") == canonical_digest_v1(header["facts"])
        and owner.get("family_precedence") == list(state_contract.FAMILY_PRECEDENCE_V1)
        and owner.get("predicate_results") == predicates
        and owner.get("matched_families") == [OWNER]
        and owner.get("owner") == OWNER and owner.get("precedence_index") == 2
        and owner.get("owner_contract_id") == state_contract.CONTRACT_ID
        and owner.get("owner_contract_schema_version") == 1
        and owner.get("owner_id") == owner_id and owner.get("owner_digest") == bare
        and owner.get("owner_scope") == "ROOT_SOURCE_DISPATCH_ONLY"
        and owner.get("common_owner_authority") is True
        and owner.get("source_actualness") is True
        and owner.get("persistent_admission") is False
        and owner.get("queue_authority") is False and owner.get("e1_authority") is False
    ):
        _reject(RebindRejectCode.OWNER_MISMATCH, "V4 owner receipt does not replay")


def _validate_scope(scope: Mapping[str, Any], *, raw: Mapping[str, Any], body: Mapping[str, Any], anchor: Mapping[str, Any], state: Mapping[str, Any], actual: Mapping[str, Any], owner: Mapping[str, Any], terminal: Mapping[str, Any]) -> None:
    _verify_seal(scope, id_field="receipt_id", prefix=V4_SCOPE_ID_PREFIX, name="V4 scope")
    p = raw["root_context"]
    scans = [_scan_gap(p, gap) for gap in ORDERED_GAPS]
    outside = [_scan_gap(p, 23)]
    registered_digest = canonical_digest_v1({"scope_id": SCOPE_ID, "root_context": p, "ordered_gaps": list(ORDERED_GAPS), "scans": scans, "global_exhaustion": False, "next_unchecked_gap": NEXT_UNCHECKED_GAP})
    outside_digest = canonical_digest_v1({"scope_id": SCOPE_ID, "root_context": p, "gaps": [23], "scans": outside, "outside_registered_scope": True})
    if any(scan["matching_certificates"] for scan in scans):
        _reject(RebindRejectCode.TERMINAL_SOURCE_NOT_MISS, "registered prefix contains a terminal")
    if not (
        scope.get("receipt_type") == V4_SCOPE_TYPE and scope.get("schema_version") == 2
        and scope.get("status") == "REGISTERED_PREFIX_SCOPE_VALIDATED_NO_E1"
        and scope.get("role") == "INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR"
        and scope.get("raw_q_one_g") == raw and scope.get("source_body") == body
        and scope.get("root_anchor") == anchor and scope.get("source_state") == state
        and scope.get("root_actualness") == actual and scope.get("owner_receipt") == owner
        and scope.get("terminal_receipt") == terminal and scope.get("scope_id") == SCOPE_ID
        and scope.get("coverage_semantics") == COVERAGE_SEMANTICS
        and scope.get("ordered_gaps") == list(ORDERED_GAPS)
        and scope.get("next_unchecked_gap") == NEXT_UNCHECKED_GAP
        and scope.get("candidate_order") == "gap_ascending_divisor_ascending_type_I_before_II"
        and scope.get("registered_gap_scans") == scans and scope.get("outside_scope_gap_scans") == outside
        and scope.get("registered_prefix_replay_digest") == registered_digest
        and scope.get("outside_scope_control_digest") == outside_digest
        and scope.get("global_exhaustion") is False
        and scope.get("registered_prefix_miss_authority") is True
        and scope.get("scope_validation_authority") is True
        and scope.get("e1_authority") is False and scope.get("persistent_admission") is False
        and scope.get("queue_authority") is False
    ):
        _reject(RebindRejectCode.SCOPE_MISMATCH, "V4 scope receipt does not replay")


def _phase_math(p: int) -> dict[str, Any]:
    t = (p - 1) // 24
    x = (p + 3) // 4
    chart_r = 16 * t + 3
    chart_k = x * (16 * t + 1)
    source = [p, chart_r * (p - 1) - p, p - 1]
    target = [1, chart_r - 1, 1]
    if not (
        x == 6 * t + 1 and 4 * chart_k == p * chart_r + 1
        and gcd(x, chart_k) == x and 3 <= chart_r <= p - 2
        and source[0] + source[1] == chart_r * source[2]
        and gcd(source[0], source[1]) == 1 and chart_k % p != 0
        and source[0] % p == 0 and (source[1] + chart_r) % p == 0
        and (source[2] + 1) % p == 0
        and [source[0] // p, (source[1] + chart_r) // p, (source[2] + 1) // p] == target
    ):
        _reject(RebindRejectCode.CANDIDATE_MISMATCH, "full-carrier phase-root arithmetic failed")
    unsigned = {
        "math_replay_id": PHASE_ROOT_MATH_ID, "root_context": p, "t": t, "x": x,
        "chart_r": chart_r, "chart_k": chart_k, "support_a": 1,
        "fresh_source": source, "target_anchor": target, "edge_prime": p,
        "edge_shift": 1, "gcd_reduction": 1, "source_phase": "TYPEII_G_HANDOFF",
        "target_phase": "TYPEI", "target_protocol": "CHARGED",
        "target_provenance": "FULL_CARRIER_POST_G", "mark_kind": "ROOT_SOL",
        "ticket": "PHASE_DROP_EVIDENCE_ONLY", "admission_ticket_issued": False,
    }
    return {**unsigned, "digest": canonical_digest_v1(unsigned)}


def _validate_v4_receipt(v4: Mapping[str, Any], *, raw: Mapping[str, Any], body: Mapping[str, Any], anchor: Mapping[str, Any], state: Mapping[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str, str]:
    receipt = _exact_mapping(v4, V4_FIELDS, "v4_consumer_receipt")
    _verify_seal(receipt, id_field="receipt_id", prefix=V4_RECEIPT_ID_PREFIX, name="V4 consumer")
    consumer_grant = _registry_grant(receipt.get("role_grant"), role="REGISTERED_PREFIX_E1_CONSUMER", version=4)
    _grant_parity(receipt, consumer_grant, "v4 consumer")
    actual = _mapping(receipt["root_actualness"], "v4.root_actualness")
    head, tree = _validate_actualness(actual, state, raw, body, anchor)
    terminal = _mapping(receipt["terminal_receipt"], "v4.terminal_receipt")
    _validate_terminal(terminal, actual, state, raw["root_context"])
    owner = _mapping(receipt["owner_receipt"], "v4.owner_receipt")
    owner_grant = _registry_grant(owner.get("role_grant"), role="COMMON_ROOT_OWNER_CLASSIFIER", version=4)
    _grant_parity(owner, owner_grant, "v4 owner")
    _validate_v4_owner(owner, raw=raw, body=body, anchor=anchor, state=state, actual=actual)
    scope = _mapping(receipt["scope_validation_receipt"], "v4.scope_validation_receipt")
    scope_grant = _registry_grant(scope.get("role_grant"), role="INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR", version=4)
    _grant_parity(scope, scope_grant, "v4 scope")
    _validate_scope(scope, raw=raw, body=body, anchor=anchor, state=state, actual=actual, owner=owner, terminal=terminal)
    math = _exact_mapping(receipt["math_replay"], MATH_FIELDS, "v4.math_replay")
    expected_math = _phase_math(raw["root_context"])
    if math != expected_math or receipt.get("math_replay_id") != PHASE_ROOT_MATH_ID or receipt.get("math_replay_digest") != math["digest"]:
        _reject(RebindRejectCode.CANDIDATE_MISMATCH, "V4 math replay differs from the independent arithmetic")
    candidate = _exact_mapping(receipt["candidate_witness"], CANDIDATE_FIELDS, "v4.candidate_witness")
    expected_candidate = {
        "source_state_id": state["state_id"], "source_state_digest": state["digest"],
        "parent_kind": "ROOT_INITIALIZER_ACTUALNESS", "owner": OWNER,
        "owner_id": owner["owner_id"], "owner_digest": owner["owner_digest"],
        "scope_id": SCOPE_ID, "coverage_semantics": COVERAGE_SEMANTICS,
        "terminal_receipt_id": terminal["receipt_id"], "terminal_receipt_digest": terminal["digest"],
        "math_replay_id": PHASE_ROOT_MATH_ID, "math_replay_digest": math["digest"],
        "target_phase": "TYPEI", "target_protocol": "CHARGED",
        "target_provenance": "FULL_CARRIER_POST_G", "target_scope": "fresh_source_tree_only",
        "source": math["fresh_source"], "target_anchor": math["target_anchor"],
    }
    candidate_digest = canonical_digest_v1(expected_candidate)
    positives = {
        "source_actualness": True, "common_owner_authority": True,
        "registered_prefix_miss_authority": True, "scope_validation_authority": True,
        "root_source_scoped_e1": True, "scope_aware_consumer_authority": True,
        "root_source_occurrence_authority": True,
    }
    negatives = (
        "terminal_receipt_direct_continuation_authority", "e1_authority", "generic_e1",
        "successor_e1", "producer_authority", "producer_continuation_allowed",
        "persistent_admission", "queue_authority", "e2_authority", "e3_authority",
        "e4_authority", "e5_authority", "terminal_leaf_authority",
        "root_proof_close_authority", "global_exhaustion",
    )
    if not (
        receipt.get("receipt_type") == V4_RECEIPT_TYPE and receipt.get("schema_version") == 2
        and receipt.get("status") == "ROOT_SOURCE_SCOPED_E1_ISSUED"
        and receipt.get("role") == "REGISTERED_PREFIX_E1_CONSUMER"
        and receipt.get("raw_q_one_g") == raw and receipt.get("source_body") == body
        and receipt.get("root_anchor") == anchor and receipt.get("source_state") == state
        and receipt.get("root_actualness") == actual and receipt.get("owner_receipt") == owner
        and receipt.get("terminal_receipt") == terminal and receipt.get("scope_validation_receipt") == scope
        and receipt.get("state_id") == state["state_id"] and receipt.get("state_digest") == state["digest"]
        and receipt.get("root_actualness_id") == actual["actualness_id"]
        and receipt.get("root_actualness_digest") == actual["digest"]
        and receipt.get("raw_q_one_g_digest") == canonical_digest_v1(raw)
        and receipt.get("body_id") == body["body_id"]
        and receipt.get("body_digest") == body["digest"]
        and receipt.get("anchor_id") == anchor["anchor_id"]
        and receipt.get("anchor_digest") == anchor["digest"]
        and receipt.get("owner_receipt_id") == owner["receipt_id"]
        and receipt.get("owner_receipt_digest") == owner["digest"]
        and receipt.get("terminal_receipt_id") == terminal["receipt_id"]
        and receipt.get("terminal_receipt_digest") == terminal["digest"]
        and receipt.get("scope_validation_receipt_id") == scope["receipt_id"]
        and receipt.get("scope_validation_receipt_digest") == scope["digest"]
        and receipt.get("scope_id") == SCOPE_ID and receipt.get("coverage_semantics") == COVERAGE_SEMANTICS
        and receipt.get("ordered_gaps") == list(ORDERED_GAPS) and receipt.get("next_unchecked_gap") == NEXT_UNCHECKED_GAP
        and receipt.get("global_exhaustion") is False and receipt.get("parent_kind") == "ROOT_INITIALIZER_ACTUALNESS"
        and receipt.get("occurrence_path") == [] and candidate == expected_candidate
        and receipt.get("candidate_witness_digest") == candidate_digest
        and receipt.get("occurrence_value_digest") == candidate_digest
        and all(receipt.get(key) is value for key, value in positives.items())
        and all(receipt.get(key) is False for key in negatives)
    ):
        _reject(RebindRejectCode.V4_RECEIPT_MISMATCH, "V4 consumer receipt has another source, scope, candidate, or authority")
    return receipt, actual, terminal, head, tree


def _contains_forbidden(value: Any) -> bool:
    if type(value) is dict:
        return any(key in FORBIDDEN_V1_CANDIDATE_KEYS or _contains_forbidden(child) for key, child in value.items())
    if type(value) is list:
        return any(_contains_forbidden(child) for child in value)
    return False


def _header_mapping(header: state_contract.VerifiedSelectorHeaderV1) -> dict[str, Any]:
    return {
        "state_id": header.state_id, "queue_gate": header.queue_gate,
        "producer_id": header.producer_id, "branch_id": header.branch_id,
        "parent_state_id": header.parent_state_id, "root_context": header.root_context,
        "equation_rank": header.equation_rank, "mark_kind": header.mark_kind,
        "mark_receipt_digest": header.mark_receipt_digest,
        "terminal_first_digest": header.terminal_first_digest,
        "source_receipt_digest": header.source_receipt_digest,
        "facts_digest": header.facts_digest, "facts": dict(header.facts),
    }


def _validate_v1_state(v1_state: Mapping[str, Any], p: int) -> tuple[state_contract.VerifiedSelectorHeaderV1, state_contract.OwnerClassificationV1, dict[str, Any]]:
    rule = state_contract.ProducerRuleV1(
        producer_id="q1_root_v1_base_materializer_v1",
        queue_gate=state_contract.ROOT_INITIALIZER_OUTPUT,
        branch_ids=frozenset({"q1_g_registered_prefix_miss_base_v1"}),
        source_owners=frozenset(), target_owners=frozenset({OWNER}),
    )
    state = _mapping(v1_state, "v1_state")
    if _contains_forbidden(state):
        _reject(RebindRejectCode.SEMANTIC_ORIGIN_MISMATCH, "V4 candidate data entered the V1 state")
    try:
        header = state_contract.extract_verified_selector_header_v1(state, {rule.producer_id: rule})
        classification = state_contract.classify_selector_owner_v1(header)
    except Exception as exc:
        _reject(RebindRejectCode.V1_STATE_MISMATCH, f"V1 state did not replay: {exc}")
    if not (
        state_contract.build_state_id_v1(state) == state.get("state_id")
        and header.root_context == p and header.equation_rank == p
        and header.queue_gate == state_contract.ROOT_INITIALIZER_OUTPUT
        and header.parent_state_id is None and classification.owner == OWNER
        and classification.matched_families == (OWNER,) and classification.precedence_index == 2
    ):
        _reject(RebindRejectCode.V1_STATE_MISMATCH, "V1 root base state identity or owner changed")
    return header, classification, state


def _terminal_projection_binding(state: Mapping[str, Any], actual: Mapping[str, Any], terminal: Mapping[str, Any], p: int) -> tuple[dict[str, Any], str]:
    binding = canonical_digest_v1({
        "source_state_id": state["state_id"], "source_state_digest": state["digest"],
        "root_actualness_id": actual["actualness_id"], "root_actualness_digest": actual["digest"],
        "v3_terminal_receipt_id": terminal["receipt_id"], "v3_terminal_receipt_digest": terminal["digest"],
        "root_context": p, "scope": SCOPE_ID, "coverage_semantics": COVERAGE_SEMANTICS,
        "ordered_gaps": list(ORDERED_GAPS), "next_unchecked_gap": NEXT_UNCHECKED_GAP,
        "global_exhaustion": False,
    })
    terminal_first_unsigned = {
        "schema_id": state_contract.TERMINAL_FIRST_SCHEMA_ID, "schema_version": 1,
        "receipt_id": "q1-v1-terminal-first:" + binding, "scope": SCOPE_ID, "outcome": "MISS",
    }
    terminal_first = {**terminal_first_unsigned, "digest": canonical_digest_v1(terminal_first_unsigned)}
    values = {
        "receipt_type": V5_TERMINAL_PROJECTION_TYPE, "schema_version": 1,
        "status": "V1_TERMINAL_FIRST_PROJECTED_NO_AUTHORITY",
        "artifact_class": "CANONICAL_PROJECTION_ONLY", "source_state_id": state["state_id"],
        "source_state_digest": state["digest"], "root_actualness_id": actual["actualness_id"],
        "root_actualness_digest": actual["digest"], "v3_terminal_receipt_id": terminal["receipt_id"],
        "v3_terminal_receipt_digest": terminal["digest"], "root_context": p,
        "coverage_semantics": COVERAGE_SEMANTICS, "ordered_gaps": list(ORDERED_GAPS),
        "next_unchecked_gap": NEXT_UNCHECKED_GAP, "global_exhaustion": False,
        "v1_terminal_first": terminal_first, "v1_terminal_first_digest": terminal_first["digest"],
        "projection_binding_digest": binding, "terminal_projection_authority": False,
        "persistent_admission": False, "queue_authority": False, "successor_authority": False,
        "e1_authority": False, "e2_authority": False, "e3_authority": False,
        "e4_authority": False, "e5_authority": False,
    }
    digest = canonical_digest_v1(values)
    return {**values, "receipt_id": V5_TERMINAL_PROJECTION_ID_PREFIX + digest, "digest": digest}, binding


def _validate_v5_receipt(v5: Mapping[str, Any], *, v4: Mapping[str, Any], raw: Mapping[str, Any], body: Mapping[str, Any], anchor: Mapping[str, Any], state: Mapping[str, Any], actual: Mapping[str, Any], terminal: Mapping[str, Any], p: int, explicit_v1_state: Mapping[str, Any]) -> tuple[dict[str, Any], state_contract.VerifiedSelectorHeaderV1, state_contract.OwnerClassificationV1, dict[str, Any], dict[str, Any]]:
    receipt = _exact_mapping(v5, V5_FIELDS, "v5_admission_receipt")
    _verify_seal(receipt, id_field="receipt_id", prefix=V5_RECEIPT_ID_PREFIX, name="V5 admission")
    admission_grant = _registry_grant(receipt.get("role_grant"), role="INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER", version=5)
    _grant_parity(receipt, admission_grant, "v5 admission")
    materialization = _exact_mapping(receipt["materialization_receipt"], MATERIALIZATION_FIELDS, "v5.materialization")
    _verify_seal(materialization, id_field="receipt_id", prefix=V5_MATERIALIZATION_ID_PREFIX, name="V5 materialization")
    materializer_grant = _registry_grant(materialization.get("role_grant"), role="Q1_ROOT_V1_BASE_MATERIALIZER", version=5)
    _grant_parity(materialization, materializer_grant, "v5 materialization")
    expected_projection, projection_binding = _terminal_projection_binding(state, actual, terminal, p)
    projection = _mapping(materialization["terminal_projection"], "v5.terminal_projection")
    _verify_seal(projection, id_field="receipt_id", prefix=V5_TERMINAL_PROJECTION_ID_PREFIX, name="V5 terminal projection")
    header, classification, v1_state = _validate_v1_state(explicit_v1_state, p)
    if v1_state != receipt.get("v1_state") or v1_state != materialization.get("v1_state"):
        _reject(RebindRejectCode.V1_STATE_MISMATCH, "explicit V1 source differs from V5 state")
    v1_wire_digest = canonical_digest_v1(v1_state)
    v1_state_digest = v1_state["state_id"].removeprefix("state:")
    facts_digest = state_contract.canonical_digest_v1(dict(header.facts))
    semantic_origin = canonical_digest_v1({
        "v2_source_state_id": state["state_id"], "v2_source_state_digest": state["digest"],
        "root_context": p, "producer_id": "q1_root_v1_base_materializer_v1",
        "branch_id": "q1_g_registered_prefix_miss_base_v1",
        "terminal_projection_binding_digest": projection_binding, "facts_digest": facts_digest,
    })
    predicates = {item.family_id: bool(item.predicate(header)) for item in state_contract.FAMILY_PREDICATES_V1}
    header_wire = _header_mapping(header)
    translation = canonical_digest_v1({
        "v2_state_id": state["state_id"], "v2_state_digest": state["digest"],
        "v4_owner_receipt_id": v4["owner_receipt"]["receipt_id"],
        "v4_owner_receipt_digest": v4["owner_receipt"]["digest"],
        "v4_owner_id": v4["owner_receipt"]["owner_id"],
        "v4_owner_digest": v4["owner_receipt"]["owner_digest"],
        "v1_state_id": v1_state["state_id"], "v1_state_wire_digest": v1_wire_digest,
        "v1_owner_digest": classification.owner_digest, "facts_digest": header.facts_digest,
        "owner": OWNER, "matched_families": [OWNER], "precedence_index": 2,
    })
    expected_producer_rule = {
        "producer_id": "q1_root_v1_base_materializer_v1", "queue_gate": "ROOT_INITIALIZER_OUTPUT",
        "branch_ids": ["q1_g_registered_prefix_miss_base_v1"], "source_owners": [],
        "target_owners": [OWNER],
    }
    v5_positive = {"v1_base_owner_authority": True, "root_base_admission_authority": True, "persistent_admission": True}
    v5_negative = (
        "root_base_materialization_authority", "queue_authority", "enqueue_authority",
        "enqueue_performed", "successor_admission", "producer_authority",
        "producer_continuation_allowed", "generic_owner_authority", "e1_authority",
        "e2_authority", "e3_authority", "e4_authority", "e5_authority",
        "t5_ticket_authority", "t5_potential_authority", "global_exhaustion",
        "terminal_leaf_authority", "local_grant_authenticates_head", "repository_authority",
    )
    materialization_negative = (
        "v1_base_owner_authority", "root_base_admission_authority", "persistent_admission",
        "queue_authority", "enqueue_authority", "enqueue_performed", "successor_admission",
        "producer_authority", "producer_continuation_allowed", "e1_authority", "e2_authority",
        "e3_authority", "e4_authority", "e5_authority", "t5_ticket_authority",
        "t5_potential_authority", "global_exhaustion", "terminal_leaf_authority",
        "local_grant_authenticates_head", "repository_authority",
    )
    if not (
        receipt.get("receipt_type") == V5_RECEIPT_TYPE and receipt.get("schema_version") == 1
        and receipt.get("status") == "V1_ROOT_INITIALIZER_BASE_ADMISSION_ISSUED_NO_QUEUE"
        and receipt.get("role") == "INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER"
        and receipt.get("source_state_id") == state["state_id"] and receipt.get("source_state_digest") == state["digest"]
        and receipt.get("role_grant_id") == admission_grant["grant_id"]
        and receipt.get("role_grant_digest") == canonical_digest_v1(admission_grant)
        and receipt.get("role_artifact_id") == admission_grant["artifact_id"]
        and receipt.get("role_artifact_semantic_sha256") == admission_grant["artifact_semantic_sha256"]
        and receipt.get("materialization_receipt_id") == materialization["receipt_id"]
        and receipt.get("materialization_receipt_digest") == materialization["digest"]
        and receipt.get("v4_owner_receipt") == v4["owner_receipt"]
        and receipt.get("v4_scope_receipt") == v4["scope_validation_receipt"]
        and receipt.get("v4_owner_receipt_id") == v4["owner_receipt"]["receipt_id"]
        and receipt.get("v4_owner_receipt_digest") == v4["owner_receipt"]["digest"]
        and receipt.get("v4_scope_receipt_id") == v4["scope_validation_receipt"]["receipt_id"]
        and receipt.get("v4_scope_receipt_digest") == v4["scope_validation_receipt"]["digest"]
        and receipt.get("v4_owner_id") == v4["owner_receipt"]["owner_id"]
        and receipt.get("v4_owner_digest") == v4["owner_receipt"]["owner_digest"]
        and receipt.get("v1_contract_id") == state_contract.CONTRACT_ID
        and receipt.get("v1_state_schema_id") == state_contract.STATE_SCHEMA_ID
        and receipt.get("v1_state_schema_version") == state_contract.STATE_SCHEMA_VERSION
        and receipt.get("v1_state_id") == v1_state["state_id"]
        and receipt.get("v1_state_wire_digest") == v1_wire_digest
        and receipt.get("v1_owner_digest") == classification.owner_digest
        and receipt.get("verified_header") == header_wire
        and receipt.get("verified_header_digest") == canonical_digest_v1(header_wire)
        and receipt.get("predicate_results") == predicates
        and receipt.get("predicate_results_digest") == canonical_digest_v1(predicates)
        and receipt.get("family_precedence") == list(state_contract.FAMILY_PRECEDENCE_V1)
        and receipt.get("matched_families") == [OWNER] and receipt.get("owner") == OWNER
        and receipt.get("precedence_index") == 2
        and receipt.get("owner_translation_binding_digest") == translation
        and receipt.get("admission_decision") == "ACCEPT" and receipt.get("admission_reason") == "ACCEPT"
        and receipt.get("producer_rule") == expected_producer_rule
        and receipt.get("producer_rule_digest") == canonical_digest_v1(expected_producer_rule)
        and receipt.get("canonical_root_potential_evidence") == [p, 3, 0, 0, 0, 0, 0]
        and receipt.get("canonical_root_potential_evidence_digest") == canonical_digest_v1([p, 3, 0, 0, 0, 0, 0])
        and all(receipt.get(key) is value for key, value in v5_positive.items())
        and all(receipt.get(key) is False for key in v5_negative)
    ):
        _reject(RebindRejectCode.V5_RECEIPT_MISMATCH, "V5 base admission did not replay")
    if not (
        materialization.get("receipt_type") == V5_MATERIALIZATION_TYPE and materialization.get("schema_version") == 1
        and materialization.get("status") == "V1_ROOT_INITIALIZER_OUTPUT_MATERIALIZED_NOT_ADMITTED"
        and materialization.get("role") == "Q1_ROOT_V1_BASE_MATERIALIZER"
        and materialization.get("role_grant_id") == materializer_grant["grant_id"]
        and materialization.get("role_grant_digest") == canonical_digest_v1(materializer_grant)
        and materialization.get("role_artifact_id") == materializer_grant["artifact_id"]
        and materialization.get("role_artifact_semantic_sha256") == materializer_grant["artifact_semantic_sha256"]
        and materialization.get("raw_q_one_g") == raw and materialization.get("source_body") == body
        and materialization.get("raw_q_one_g_digest") == canonical_digest_v1(raw)
        and materialization.get("body_id") == body["body_id"]
        and materialization.get("body_digest") == body["digest"]
        and materialization.get("root_anchor") == anchor and materialization.get("source_state") == state
        and materialization.get("anchor_id") == anchor["anchor_id"]
        and materialization.get("anchor_digest") == anchor["digest"]
        and materialization.get("source_state_id") == state["state_id"]
        and materialization.get("source_state_digest") == state["digest"]
        and materialization.get("root_actualness") == actual and materialization.get("terminal_receipt") == terminal
        and materialization.get("root_actualness_id") == actual["actualness_id"]
        and materialization.get("root_actualness_digest") == actual["digest"]
        and materialization.get("terminal_receipt_id") == terminal["receipt_id"]
        and materialization.get("terminal_receipt_digest") == terminal["digest"]
        and projection == expected_projection and materialization.get("terminal_projection_id") == projection["receipt_id"]
        and materialization.get("terminal_projection_digest") == projection["digest"]
        and materialization.get("semantic_origin_digest") == semantic_origin
        and materialization.get("v1_state_id") == v1_state["state_id"]
        and materialization.get("v1_state_wire_digest") == v1_wire_digest
        and materialization.get("producer_rule") == expected_producer_rule
        and materialization.get("canonical_root_potential_evidence") == [p, 3, 0, 0, 0, 0, 0]
        and materialization.get("root_base_materialization_authority") is True
        and all(materialization.get(key) is False for key in materialization_negative)
    ):
        _reject(RebindRejectCode.V5_RECEIPT_MISMATCH, "V5 materialization did not replay")
    if v1_state["state_id"] == state["state_id"] or v1_state_digest == state["digest"]:
        _reject(RebindRejectCode.V1_STATE_MISMATCH, "V1 state must be newly content-addressed")
    return receipt, header, classification, materialization, projection


def _source_potential(state_id: str, p: int) -> dict[str, Any]:
    unsigned = {
        "schema_id": "t5_n7_potential_receipt_v1", "schema_version": 1,
        "state_id": state_id, "coordinates": [p, 3, 0, 0, 0, 0, 0],
    }
    return {**unsigned, "digest": canonical_digest_v1(unsigned)}


@dataclass(frozen=True, slots=True)
class QOneRootSourceScopedE1RebindReceiptV1:
    ARTIFACT_TYPE: ClassVar[str] = RECEIPT_TYPE
    schema_version: int
    status: str
    role: str
    role_grant: Mapping[str, Any]
    role_grant_id: str
    role_grant_digest: str
    role_artifact_id: str
    role_artifact_semantic_sha256: str
    head_sha: str
    head_tree_sha: str
    v4_registry_id: str
    v5_registry_id: str
    v4_consumer_receipt: Mapping[str, Any]
    v5_admission_receipt: Mapping[str, Any]
    v4_receipt_id: str
    v4_receipt_digest: str
    v5_admission_receipt_id: str
    v5_admission_receipt_digest: str
    v2_source_state_id: str
    v2_source_state_digest: str
    v1_source_state_id: str
    v1_source_state_digest: str
    v1_state_wire_digest: str
    v1_state: Mapping[str, Any]
    representation_namespace: str
    path_semantics: str
    not_transition: bool
    v1_source_state_digest_domain: str
    v1_state_wire_digest_domain: str
    v4_candidate_digest_domain: str
    source_owner: str
    source_owner_id: str
    source_owner_digest: str
    source_facts_digest: str
    owner_contract_id: str
    owner_contract_schema_version: int
    owner_precedence_index: int
    v4_owner_receipt_id: str
    v4_owner_receipt_digest: str
    v1_owner_digest: str
    v3_terminal_receipt_id: str
    v3_terminal_receipt_digest: str
    v1_terminal_projection_id: str
    v1_terminal_projection_digest: str
    scope_id: str
    coverage_semantics: str
    ordered_gaps: tuple[int, int, int]
    next_unchecked_gap: int
    global_exhaustion: bool
    v4_candidate_witness_digest: str
    v4_math_replay_id: str
    v4_math_replay_digest: str
    rebound_candidate_witness: Mapping[str, Any]
    rebound_candidate_witness_digest: str
    source_potential_receipt: Mapping[str, Any]
    source_potential_receipt_digest: str
    source_potential_coordinates: tuple[int, int, int, int, int, int, int]
    source_rebind_map: Mapping[str, Any]
    source_rebind_map_digest: str
    semantic_origin_exclusion_digest: str
    v4_root_source_scoped_e1: bool
    root_source_scoped_e1_rebound: bool
    source_rebind_authority: bool
    local_grant_authenticates_head: bool
    repository_authority: bool
    common_owner_authority: bool
    registered_prefix_miss_authority: bool
    scope_validation_authority: bool
    root_source_occurrence_authority: bool
    terminal_receipt_direct_continuation_authority: bool
    e1_authority: bool
    generic_e1: bool
    successor_e1: bool
    producer_authority: bool
    producer_continuation_allowed: bool
    admission_authority: bool
    persistent_admission: bool
    queue_authority: bool
    enqueue_authority: bool
    e2_authority: bool
    e3_authority: bool
    e4_authority: bool
    e5_authority: bool
    t5_ticket_authority: bool
    t5_potential_authority: bool
    reentry_authority: bool
    terminal_leaf_authority: bool
    receipt_id: str
    digest: str


_MAPPING_FIELDS = {
    "role_grant", "v4_consumer_receipt", "v5_admission_receipt", "v1_state",
    "rebound_candidate_witness", "source_potential_receipt", "source_rebind_map",
}


def _unsigned(values: Mapping[str, Any]) -> dict[str, Any]:
    result = {"receipt_type": RECEIPT_TYPE}
    for field in fields(QOneRootSourceScopedE1RebindReceiptV1):
        if field.name not in {"receipt_id", "digest"}:
            result[field.name] = _json_copy(values[field.name])
    return result


def _construct(values: Mapping[str, Any]) -> QOneRootSourceScopedE1RebindReceiptV1:
    normalized: dict[str, Any] = {}
    for field in fields(QOneRootSourceScopedE1RebindReceiptV1):
        value = values[field.name]
        if field.name in _MAPPING_FIELDS:
            value = MappingProxyType(_json_copy(value))
        normalized[field.name] = value
    return QOneRootSourceScopedE1RebindReceiptV1(**normalized)


def _validate_result(receipt: QOneRootSourceScopedE1RebindReceiptV1) -> None:
    if type(receipt) is not QOneRootSourceScopedE1RebindReceiptV1:
        _reject(RebindRejectCode.INPUT_NOT_EXACT_MAPPING, "rebind receipt class changed")
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    digest = canonical_digest_v1(_unsigned(values))
    if receipt.digest != digest or receipt.receipt_id != RECEIPT_ID_PREFIX + digest:
        _reject(RebindRejectCode.DIGEST_MISMATCH, "rebind receipt seal does not replay")
    _grant(_json_copy(receipt.role_grant))
    if not (
        receipt.schema_version == 1 and receipt.status == STATUS and receipt.role == ROLE
        and receipt.v4_registry_id == V4_REGISTRY_ID and receipt.v5_registry_id == V5_REGISTRY_ID
        and receipt.scope_id == SCOPE_ID and receipt.coverage_semantics == COVERAGE_SEMANTICS
        and receipt.ordered_gaps == ORDERED_GAPS and receipt.next_unchecked_gap == NEXT_UNCHECKED_GAP
        and receipt.global_exhaustion is False and _is_oid(receipt.head_sha)
        and _is_oid(receipt.head_tree_sha) and len(receipt.head_sha) == len(receipt.head_tree_sha)
        and receipt.v4_root_source_scoped_e1 is True
        and receipt.root_source_scoped_e1_rebound is True
        and receipt.source_rebind_authority is True
        and receipt.representation_namespace == REPRESENTATION_NAMESPACE
        and receipt.path_semantics == PATH_SEMANTICS
        and receipt.not_transition is True
        and receipt.v1_source_state_digest_domain == DIGEST_DOMAIN_STATE_ID_SUFFIX
        and receipt.v1_state_wire_digest_domain == DIGEST_DOMAIN_STATE_WIRE
        and receipt.v4_candidate_digest_domain == DIGEST_DOMAIN_V4_CANDIDATE
    ):
        _reject(RebindRejectCode.MALFORMED_FIELD, "rebind identity/scope changed")
    v1_state_preview = _mapping(receipt.v1_state, "receipt.v1_state")
    if not (
        receipt.v1_source_state_id.startswith("state:")
        and receipt.v1_source_state_id == "state:" + receipt.v1_source_state_digest
        and receipt.v2_source_state_id == "state:" + receipt.v2_source_state_digest
        and receipt.v1_source_state_id != receipt.v2_source_state_id
        and _is_nonzero_digest(receipt.v1_state_wire_digest)
        and _is_nonzero_digest(receipt.source_owner_digest)
        and receipt.source_owner == OWNER and receipt.source_owner_id == "owner:" + receipt.source_owner_digest
        and receipt.v1_owner_digest == receipt.source_owner_id
        and receipt.owner_contract_id == state_contract.CONTRACT_ID
        and receipt.owner_contract_schema_version == 1 and receipt.owner_precedence_index == 2
        and type(v1_state_preview.get("root_context")) is int
        and tuple(receipt.source_potential_coordinates) == (v1_state_preview.get("root_context"), 3, 0, 0, 0, 0, 0)
        and isinstance(receipt.source_potential_receipt, Mapping)
        and receipt.source_potential_receipt_digest == receipt.source_potential_receipt.get("digest")
        and receipt.rebound_candidate_witness_digest == canonical_digest_v1(receipt.rebound_candidate_witness)
        and receipt.source_rebind_map_digest == canonical_digest_v1(receipt.source_rebind_map)
    ):
        _reject(RebindRejectCode.MALFORMED_FIELD, "rebind source references do not replay")
    # A serialized receipt is independently replayable.  Keep the complete V4
    # and V5 evidence in the sidecar and rebuild all derived fields here; this
    # prevents a coherent attacker reseal from changing only an ID/digest/map.
    v4 = _mapping(receipt.v4_consumer_receipt, "receipt.v4_consumer_receipt")
    raw, body, anchor, state = _source_chain(
        v4.get("raw_q_one_g"), v4.get("source_body"), v4.get("root_anchor"), v4.get("source_state")
    )
    checked_v4, actual, terminal, head, tree = _validate_v4_receipt(
        v4, raw=raw, body=body, anchor=anchor, state=state
    )
    v5 = _mapping(receipt.v5_admission_receipt, "receipt.v5_admission_receipt")
    checked_v5, header, classification, materialization, projection = _validate_v5_receipt(
        v5, v4=checked_v4, raw=raw, body=body, anchor=anchor, state=state,
        actual=actual, terminal=terminal, p=raw["root_context"], explicit_v1_state=_json_copy(receipt.v1_state)
    )
    if not (
        checked_v4["receipt_id"] == receipt.v4_receipt_id
        and checked_v4["digest"] == receipt.v4_receipt_digest
        and checked_v5["receipt_id"] == receipt.v5_admission_receipt_id
        and checked_v5["digest"] == receipt.v5_admission_receipt_digest
        and head == receipt.head_sha and tree == receipt.head_tree_sha
        and state["state_id"] == receipt.v2_source_state_id
        and state["digest"] == receipt.v2_source_state_digest
        and checked_v5["v1_state_id"] == receipt.v1_source_state_id
        and checked_v5["v1_state_wire_digest"] == receipt.v1_state_wire_digest
        and checked_v5["v1_owner_digest"] == receipt.v1_owner_digest
        and checked_v5["v4_owner_receipt_id"] == receipt.v4_owner_receipt_id
        and checked_v5["v4_owner_receipt_digest"] == receipt.v4_owner_receipt_digest
        and terminal["receipt_id"] == receipt.v3_terminal_receipt_id
        and terminal["digest"] == receipt.v3_terminal_receipt_digest
        and projection["receipt_id"] == receipt.v1_terminal_projection_id
        and projection["digest"] == receipt.v1_terminal_projection_digest
        and checked_v4["candidate_witness_digest"] == receipt.v4_candidate_witness_digest
        and checked_v4["math_replay_id"] == receipt.v4_math_replay_id
        and checked_v4["math_replay_digest"] == receipt.v4_math_replay_digest
    ):
        _reject(RebindRejectCode.SOURCE_BINDING_MISMATCH, "receipt evidence IDs do not rebind to the same source")
    p = raw["root_context"]
    potential = _source_potential(checked_v5["v1_state_id"], p)
    old_candidate = checked_v4["candidate_witness"]
    rebound_candidate = {
        "source_state_id": checked_v5["v1_state_id"],
        "source_state_digest": checked_v5["v1_state_id"].removeprefix("state:"),
        "source_state_digest_domain": DIGEST_DOMAIN_STATE_ID_SUFFIX,
        "source_state_wire_digest": checked_v5["v1_state_wire_digest"],
        "source_state_wire_digest_domain": DIGEST_DOMAIN_STATE_WIRE,
        "representation_namespace": REPRESENTATION_NAMESPACE,
        "path_semantics": PATH_SEMANTICS,
        "not_transition": True,
        "parent_kind": "ROOT_INITIALIZER_OUTPUT_BASE_ADMITTED", "owner": OWNER,
        "owner_namespace": "V1_SOURCE_OWNER",
        "owner_id": classification.owner_digest,
        "owner_digest": classification.owner_digest.removeprefix("owner:"),
        "scope_id": SCOPE_ID, "coverage_semantics": COVERAGE_SEMANTICS,
        "terminal_receipt_id": terminal["receipt_id"], "terminal_receipt_digest": terminal["digest"],
        "math_replay_id": PHASE_ROOT_MATH_ID, "math_replay_digest": checked_v4["math_replay_digest"],
        "target_phase": old_candidate["target_phase"], "target_protocol": old_candidate["target_protocol"],
        "target_provenance": old_candidate["target_provenance"], "target_scope": old_candidate["target_scope"],
        "source": old_candidate["source"], "target_anchor": old_candidate["target_anchor"],
    }
    expected_map = {
        "map_type": "V4_V2_ROOT_TO_V5_V1_BASE_SOURCE",
        "representation_namespace": REPRESENTATION_NAMESPACE,
        "path_semantics": PATH_SEMANTICS,
        "not_transition": True,
        "old_source_state_id": state["state_id"], "old_source_state_digest": state["digest"],
        "new_source_state_id": checked_v5["v1_state_id"],
        "new_source_state_digest": checked_v5["v1_state_id"].removeprefix("state:"),
        "new_source_state_wire_digest": checked_v5["v1_state_wire_digest"],
        "old_owner_id": old_candidate["owner_id"], "old_owner_digest": old_candidate["owner_digest"],
        "new_owner_id": classification.owner_digest,
        "new_owner_digest": classification.owner_digest.removeprefix("owner:"),
        "occurrence_kind": "ROOT_INITIALIZER_OUTPUT", "parent_state_id": None,
        "target_state_id": None, "producer_id": None, "branch_id": None,
    }
    expected_exclusion = canonical_digest_v1({
        "v5_semantic_origin_digest": materialization["semantic_origin_digest"],
        "v1_state_id": checked_v5["v1_state_id"],
        "v1_state_wire_digest": checked_v5["v1_state_wire_digest"],
        "forbidden_v4_candidate_keys": sorted(FORBIDDEN_V1_CANDIDATE_KEYS),
        "candidate_in_v1_state": False, "candidate_in_semantic_origin": False,
    })
    if not (
        _json_copy(receipt.v1_state) == checked_v5["v1_state"]
        and receipt.source_owner == classification.owner
        and receipt.source_owner_id == classification.owner_digest
        and receipt.source_owner_digest == classification.owner_digest.removeprefix("owner:")
        and receipt.source_facts_digest == header.facts_digest
        and receipt.owner_contract_id == state_contract.CONTRACT_ID
        and receipt.owner_contract_schema_version == 1
        and receipt.owner_precedence_index == classification.precedence_index == 2
        and receipt.scope_id == SCOPE_ID
        and receipt.coverage_semantics == COVERAGE_SEMANTICS
        and receipt.ordered_gaps == ORDERED_GAPS
        and receipt.next_unchecked_gap == NEXT_UNCHECKED_GAP
        and receipt.global_exhaustion is False
        and _json_copy(receipt.source_potential_receipt) == potential
        and tuple(receipt.source_potential_coordinates) == tuple(potential["coordinates"])
        and receipt.source_potential_receipt_digest == potential["digest"]
        and _json_copy(receipt.rebound_candidate_witness) == rebound_candidate
        and receipt.rebound_candidate_witness_digest == canonical_digest_v1(rebound_candidate)
        and _json_copy(receipt.source_rebind_map) == expected_map
        and receipt.source_rebind_map_digest == canonical_digest_v1(expected_map)
        and receipt.semantic_origin_exclusion_digest == expected_exclusion
    ):
        _reject(RebindRejectCode.CANDIDATE_MISMATCH, "rebind candidate/map/potential does not replay")
    false_fields = (
        "local_grant_authenticates_head", "repository_authority", "common_owner_authority",
        "registered_prefix_miss_authority", "scope_validation_authority",
        "root_source_occurrence_authority", "terminal_receipt_direct_continuation_authority",
        "e1_authority", "generic_e1", "successor_e1", "producer_authority",
        "producer_continuation_allowed", "admission_authority", "persistent_admission",
        "queue_authority", "enqueue_authority", "e2_authority", "e3_authority",
        "e4_authority", "e5_authority", "t5_ticket_authority", "t5_potential_authority",
        "reentry_authority", "terminal_leaf_authority",
    )
    if any(getattr(receipt, field) is not False for field in false_fields):
        _reject(RebindRejectCode.AUTHORITY_BOUNDARY_VIOLATION, "rebind granted recursive authority")
    if _contains_forbidden(_json_copy(receipt.v1_state)):
        _reject(RebindRejectCode.SEMANTIC_ORIGIN_MISMATCH, "candidate entered output V1 state")


def rebind_q_one_root_source_scoped_e1_v1(
    *,
    v4_consumer_receipt: dict[str, Any],
    v5_admission_receipt: dict[str, Any],
    raw_q_one_g: dict[str, Any],
    source_body: dict[str, Any],
    root_anchor: dict[str, Any],
    source_state: dict[str, Any],
    v1_state: dict[str, Any],
    role_grant: dict[str, Any],
) -> QOneRootSourceScopedE1RebindReceiptV1:
    """Bind one valid V4 root occurrence to one V5 V1 base state.

    All source objects are explicit so an opaque V4/V5 ID alone cannot be
    rebound.  The local grant is only a typed capability preimage; exact-HEAD
    provenance remains inherited from the independently replayed V4/V5 inputs.
    """

    raw, body, anchor, state = _source_chain(raw_q_one_g, source_body, root_anchor, source_state)
    grant, grant_digest = _grant(role_grant)
    v4, actual, terminal, head, tree = _validate_v4_receipt(
        v4_consumer_receipt, raw=raw, body=body, anchor=anchor, state=state
    )
    v5, header, classification, materialization, projection = _validate_v5_receipt(
        v5_admission_receipt, v4=v4, raw=raw, body=body, anchor=anchor, state=state,
        actual=actual, terminal=terminal, p=raw["root_context"], explicit_v1_state=v1_state,
    )
    if materialization["root_actualness"] != actual or materialization["terminal_receipt"] != terminal:
        _reject(RebindRejectCode.SOURCE_BINDING_MISMATCH, "V5 materialization uses another V3/V2 chain")
    if actual.get("head_sha") != head or actual.get("head_tree_sha") != tree:
        _reject(RebindRejectCode.HEAD_MISMATCH, "V4 actualness HEAD changed during rebind")
    p = raw["root_context"]
    v1_state_wire = _mapping(v1_state, "v1_state")
    v1_state_id = v1_state_wire["state_id"]
    v1_state_digest = v1_state_id.removeprefix("state:")
    potential = _source_potential(v1_state_id, p)
    if tuple(v5["canonical_root_potential_evidence"]) != tuple(potential["coordinates"]):
        _reject(RebindRejectCode.POTENTIAL_MISMATCH, "V5 root potential evidence differs from V1 replay")
    old_candidate = _mapping(v4["candidate_witness"], "v4.candidate_witness")
    rebound_candidate = {
        "source_state_id": v1_state_id,
        "source_state_digest": v1_state_digest,
        "source_state_digest_domain": DIGEST_DOMAIN_STATE_ID_SUFFIX,
        "source_state_wire_digest": v5["v1_state_wire_digest"],
        "source_state_wire_digest_domain": DIGEST_DOMAIN_STATE_WIRE,
        "parent_kind": "ROOT_INITIALIZER_OUTPUT_BASE_ADMITTED",
        "representation_namespace": REPRESENTATION_NAMESPACE,
        "path_semantics": PATH_SEMANTICS,
        "not_transition": True,
        "owner": OWNER,
        "owner_namespace": "V1_SOURCE_OWNER",
        "owner_id": classification.owner_digest,
        "owner_digest": classification.owner_digest.removeprefix("owner:"),
        "scope_id": SCOPE_ID,
        "coverage_semantics": COVERAGE_SEMANTICS,
        "terminal_receipt_id": terminal["receipt_id"],
        "terminal_receipt_digest": terminal["digest"],
        "math_replay_id": PHASE_ROOT_MATH_ID,
        "math_replay_digest": v4["math_replay_digest"],
        "target_phase": old_candidate["target_phase"],
        "target_protocol": old_candidate["target_protocol"],
        "target_provenance": old_candidate["target_provenance"],
        "target_scope": old_candidate["target_scope"],
        "source": old_candidate["source"],
        "target_anchor": old_candidate["target_anchor"],
    }
    rebind_map = {
        "map_type": "V4_V2_ROOT_TO_V5_V1_BASE_SOURCE",
        "representation_namespace": REPRESENTATION_NAMESPACE,
        "path_semantics": PATH_SEMANTICS,
        "not_transition": True,
        "old_source_state_id": state["state_id"], "old_source_state_digest": state["digest"],
        "new_source_state_id": v1_state_id, "new_source_state_digest": v1_state_digest,
        "new_source_state_wire_digest": v5["v1_state_wire_digest"],
        "old_owner_id": old_candidate["owner_id"], "old_owner_digest": old_candidate["owner_digest"],
        "new_owner_id": classification.owner_digest,
        "new_owner_digest": classification.owner_digest.removeprefix("owner:"),
        "occurrence_kind": "ROOT_INITIALIZER_OUTPUT", "parent_state_id": None,
        "target_state_id": None, "producer_id": None, "branch_id": None,
    }
    semantic_exclusion = canonical_digest_v1({
        "v5_semantic_origin_digest": materialization["semantic_origin_digest"],
        "v1_state_id": v1_state_id, "v1_state_wire_digest": v5["v1_state_wire_digest"],
        "forbidden_v4_candidate_keys": sorted(FORBIDDEN_V1_CANDIDATE_KEYS),
        "candidate_in_v1_state": False, "candidate_in_semantic_origin": False,
    })
    values: dict[str, Any] = {
        "schema_version": 1, "status": STATUS, "role": ROLE,
        "role_grant": grant, "role_grant_id": grant["grant_id"],
        "role_grant_digest": grant_digest, "role_artifact_id": grant["artifact_id"],
        "role_artifact_semantic_sha256": grant["artifact_semantic_sha256"],
        "head_sha": head, "head_tree_sha": tree, "v4_registry_id": V4_REGISTRY_ID,
        "v5_registry_id": V5_REGISTRY_ID, "v4_consumer_receipt": v4,
        "v5_admission_receipt": v5, "v4_receipt_id": v4["receipt_id"],
        "v4_receipt_digest": v4["digest"], "v5_admission_receipt_id": v5["receipt_id"],
        "v5_admission_receipt_digest": v5["digest"], "v2_source_state_id": state["state_id"],
        "v2_source_state_digest": state["digest"], "v1_source_state_id": v1_state_id,
        "v1_source_state_digest": v1_state_digest, "v1_state_wire_digest": v5["v1_state_wire_digest"],
        "v1_state": v1_state_wire, "source_owner": OWNER,
        "representation_namespace": REPRESENTATION_NAMESPACE,
        "path_semantics": PATH_SEMANTICS,
        "not_transition": True,
        "v1_source_state_digest_domain": DIGEST_DOMAIN_STATE_ID_SUFFIX,
        "v1_state_wire_digest_domain": DIGEST_DOMAIN_STATE_WIRE,
        "v4_candidate_digest_domain": DIGEST_DOMAIN_V4_CANDIDATE,
        "source_owner_id": classification.owner_digest,
        "source_owner_digest": classification.owner_digest.removeprefix("owner:"),
        "source_facts_digest": header.facts_digest, "owner_contract_id": state_contract.CONTRACT_ID,
        "owner_contract_schema_version": 1, "owner_precedence_index": 2,
        "v4_owner_receipt_id": v4["owner_receipt_id"],
        "v4_owner_receipt_digest": v4["owner_receipt_digest"],
        "v1_owner_digest": classification.owner_digest, "v3_terminal_receipt_id": terminal["receipt_id"],
        "v3_terminal_receipt_digest": terminal["digest"],
        "v1_terminal_projection_id": projection["receipt_id"],
        "v1_terminal_projection_digest": projection["digest"], "scope_id": SCOPE_ID,
        "coverage_semantics": COVERAGE_SEMANTICS, "ordered_gaps": ORDERED_GAPS,
        "next_unchecked_gap": NEXT_UNCHECKED_GAP, "global_exhaustion": False,
        "v4_candidate_witness_digest": v4["candidate_witness_digest"],
        "v4_math_replay_id": PHASE_ROOT_MATH_ID, "v4_math_replay_digest": v4["math_replay_digest"],
        "rebound_candidate_witness": rebound_candidate,
        "rebound_candidate_witness_digest": canonical_digest_v1(rebound_candidate),
        "source_potential_receipt": potential, "source_potential_receipt_digest": potential["digest"],
        "source_potential_coordinates": tuple(potential["coordinates"]), "source_rebind_map": rebind_map,
        "source_rebind_map_digest": canonical_digest_v1(rebind_map),
        "semantic_origin_exclusion_digest": semantic_exclusion,
        "v4_root_source_scoped_e1": True, "root_source_scoped_e1_rebound": True,
        "source_rebind_authority": True, "local_grant_authenticates_head": False,
        "repository_authority": False, "common_owner_authority": False,
        "registered_prefix_miss_authority": False, "scope_validation_authority": False,
        "root_source_occurrence_authority": False,
        "terminal_receipt_direct_continuation_authority": False, "e1_authority": False,
        "generic_e1": False, "successor_e1": False, "producer_authority": False,
        "producer_continuation_allowed": False, "admission_authority": False,
        "persistent_admission": False, "queue_authority": False, "enqueue_authority": False,
        "e2_authority": False, "e3_authority": False, "e4_authority": False,
        "e5_authority": False, "t5_ticket_authority": False,
        "t5_potential_authority": False, "reentry_authority": False,
        "terminal_leaf_authority": False,
    }
    digest = canonical_digest_v1(_unsigned(values))
    values.update({"receipt_id": RECEIPT_ID_PREFIX + digest, "digest": digest})
    result = _construct(values)
    _validate_result(result)
    return result


def root_source_scoped_e1_rebind_receipt_to_mapping_v1(
    receipt: QOneRootSourceScopedE1RebindReceiptV1,
) -> dict[str, Any]:
    """Serialize a locally replayed rebind receipt without adding authority."""

    _validate_result(receipt)
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    result = _unsigned(values)
    result["receipt_id"] = receipt.receipt_id
    result["digest"] = receipt.digest
    return result


__all__ = [
    "ARTIFACT_ID", "ARTIFACT_PATH", "ARTIFACT_SYMBOLS", "AUTHORITY_CLASS",
    "CAPABILITIES", "GRANT_ID", "QOneRootSourceScopedE1RebindReceiptV1",
    "ROLE", "RebindRejectCode", "RootSourceScopedE1RebindError", "STATUS",
    "canonical_digest_v1", "rebind_q_one_root_source_scoped_e1_v1",
    "root_source_scoped_e1_rebind_receipt_to_mapping_v1",
]
