#!/usr/bin/env python3
"""Independently admit a materialized q=1 G root at the V1 base gate.

This verifier intentionally does not import or call the terminal adapter or the
base materializer.  It reconstructs their expected wire independently, invokes
the frozen V1 extractor/classifier/admission gate, and issues no queue right.
Its local grant is not exact-HEAD provenance; only a future registry/replayer
may authenticate repository authority.
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


ARTIFACT_ID = "q1_root_v1_base_admission_verifier_v1"
ARTIFACT_PATH = "scripts/t6_q_one_root_v1_base_admission_verifier_v1.py"
ARTIFACT_SYMBOLS = (
    "verify_and_admit_q_one_root_v1_base_v1",
    "base_admission_receipt_to_mapping_v1",
)
ROLE = "INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER"
GRANT_ID = "q1_root_v1_base_admission_verifier_grant_v1"
CAPABILITIES = ("ISSUE_Q1_G_V1_BASE_ADMISSION_NO_QUEUE",)
AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V5"

RECEIPT_TYPE = "Q1_ROOT_V1_BASE_ADMISSION_RECEIPT_V1"
RECEIPT_ID_PREFIX = "q1-v1-root-base-admission:"
STATUS = "V1_ROOT_INITIALIZER_BASE_ADMISSION_ISSUED_NO_QUEUE"

MATERIALIZATION_RECEIPT_TYPE = "Q1_ROOT_V1_BASE_MATERIALIZATION_RECEIPT_V1"
MATERIALIZATION_RECEIPT_ID_PREFIX = "q1-v1-root-materialization:"
MATERIALIZATION_STATUS = "V1_ROOT_INITIALIZER_OUTPUT_MATERIALIZED_NOT_ADMITTED"
MATERIALIZER_ROLE = "Q1_ROOT_V1_BASE_MATERIALIZER"
MATERIALIZER_ARTIFACT_ID = "q1_root_v1_base_materializer_v1"
MATERIALIZER_GRANT_ID = "q1_root_v1_base_materializer_grant_v1"

TERMINAL_PROJECTION_TYPE = "Q1_V3_MISS_TO_V1_TERMINAL_FIRST_PROJECTION_V1"
TERMINAL_PROJECTION_ID_PREFIX = "q1-v1-terminal-projection:"
V1_TERMINAL_RECEIPT_ID_PREFIX = "q1-v1-terminal-first:"
V3_MISS_RECEIPT_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
V3_MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"
V4_OWNER_RECEIPT_TYPE = "COMMON_Q1_ROOT_OWNER_RECEIPT_V2"
V4_OWNER_RECEIPT_ID_PREFIX = "q1-common-root-owner:"
V4_SCOPE_RECEIPT_TYPE = "Q1_REGISTERED_PREFIX_SCOPE_VALIDATION_RECEIPT_V2"
V4_SCOPE_RECEIPT_ID_PREFIX = "q1-prefix-scope-validation:"

PRODUCER_ID = "q1_root_v1_base_materializer_v1"
BRANCH_ID = "q1_g_registered_prefix_miss_base_v1"
TARGET_OWNER = "type_ii_relation_g_endpoint"
SCOPE_ID = "q1_root_after_gap_3_7_11_registered_prefix_v1"
COVERAGE_SEMANTICS = "REGISTERED_PRIORITY_ONLY"
ORDERED_GAPS = (3, 7, 11)
NEXT_UNCHECKED_GAP = 15
OUTSIDE_CONTROL_GAPS = (23,)
CANDIDATE_ORDER = "gap_ascending_divisor_ascending_type_I_before_II"
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

MATERIALIZATION_FIELDS = {
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
    "canonical_root_potential_evidence", "canonical_root_potential_evidence_digest",
    "local_grant_authenticates_head", "repository_authority",
    "root_base_materialization_authority", "v1_base_owner_authority",
    "root_base_admission_authority", "persistent_admission", "queue_authority",
    "enqueue_authority", "enqueue_performed", "successor_admission",
    "producer_authority", "producer_continuation_allowed", "e1_authority",
    "e2_authority", "e3_authority", "e4_authority", "e5_authority",
    "t5_ticket_authority", "t5_potential_authority", "global_exhaustion",
    "terminal_leaf_authority", "receipt_id", "digest"
}


class BaseAdmissionRejectCode(str, Enum):
    INPUT_NOT_EXACT_MAPPING = "INPUT_NOT_EXACT_MAPPING"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    GRANT_MISMATCH = "GRANT_MISMATCH"
    SOURCE_REPLAY_FAILED = "SOURCE_REPLAY_FAILED"
    TERMINAL_SOURCE_NOT_MISS = "TERMINAL_SOURCE_NOT_MISS"
    SCOPE_WIDENING = "SCOPE_WIDENING"
    MATERIALIZATION_MISMATCH = "MATERIALIZATION_MISMATCH"
    V4_OWNER_MISMATCH = "V4_OWNER_MISMATCH"
    V4_SCOPE_MISMATCH = "V4_SCOPE_MISMATCH"
    V1_GATE_REJECTED = "V1_GATE_REJECTED"
    OWNER_TRANSLATION_MISMATCH = "OWNER_TRANSLATION_MISMATCH"
    AUTHORITY_BOUNDARY_VIOLATION = "AUTHORITY_BOUNDARY_VIOLATION"


class BaseAdmissionError(ValueError):
    def __init__(self, code: BaseAdmissionRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: BaseAdmissionRejectCode, detail: str) -> None:
    raise BaseAdmissionError(code, detail)


def _json_copy(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(
                    BaseAdmissionRejectCode.MALFORMED_FIELD,
                    "canonical JSON keys must be exact strings",
                )
            result[key] = _json_copy(child)
        return result
    if type(value) is list or type(value) is tuple:
        return [_json_copy(child) for child in value]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(
        BaseAdmissionRejectCode.MALFORMED_FIELD,
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
        raise BaseAdmissionError(
            BaseAdmissionRejectCode.MALFORMED_FIELD,
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


def _is_nonzero_digest(value: Any) -> bool:
    return _is_digest(value) and value != "0" * 64


def _is_nonzero_git_oid(value: Any) -> bool:
    return (
        type(value) is str
        and len(value) in {40, 64}
        and value != "0" * len(value)
        and all(character in "0123456789abcdef" for character in value)
    )


def _root_potential_evidence(p: int) -> tuple[int, int, int, int, int, int, int]:
    if type(p) is not int or p < 2:
        _reject(BaseAdmissionRejectCode.MALFORMED_FIELD, "root potential p is malformed")
    return (p, 3, 0, 0, 0, 0, 0)


def _matches_root_potential(value: Any, p: int) -> bool:
    return (
        type(value) in {list, tuple}
        and len(value) == 7
        and all(type(item) is int for item in value)
        and tuple(value) == _root_potential_evidence(p)
    )


def _exact_mapping(value: Any, name: str) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(
            BaseAdmissionRejectCode.INPUT_NOT_EXACT_MAPPING,
            f"{name} must be an exact dict",
        )
    return _json_copy(value)


def _verify_content_seal(
    value: Mapping[str, Any], *, id_field: str, id_prefix: str, name: str
) -> None:
    digest = value.get("digest")
    artifact_id = value.get(id_field)
    if not _is_digest(digest) or artifact_id != id_prefix + digest:
        _reject(
            BaseAdmissionRejectCode.DIGEST_MISMATCH,
            f"{name} content ID or digest is malformed",
        )
    unsigned = _json_copy(value)
    unsigned.pop(id_field, None)
    unsigned.pop("digest", None)
    if canonical_digest_v1(unsigned) != digest:
        _reject(
            BaseAdmissionRejectCode.DIGEST_MISMATCH,
            f"{name} digest does not replay",
        )


def _grant(value: Any) -> tuple[dict[str, Any], str]:
    grant = _exact_mapping(value, "role_grant")
    if set(grant) != GRANT_FIELDS:
        _reject(
            BaseAdmissionRejectCode.GRANT_MISMATCH,
            "admission verifier grant has an inexact field set",
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
            BaseAdmissionRejectCode.GRANT_MISMATCH,
            "admission verifier grant identity or capability changed",
        )
    if not _is_digest(grant.get("artifact_semantic_sha256")):
        _reject(
            BaseAdmissionRejectCode.GRANT_MISMATCH,
            "admission verifier semantic pin is malformed",
        )
    return grant, canonical_digest_v1(grant)


def _source_chain(
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
        raise BaseAdmissionError(
            BaseAdmissionRejectCode.SOURCE_REPLAY_FAILED,
            f"V2 root source chain did not replay: {exc}",
        ) from exc
    return (
        raw,
        root_envelope.artifact_to_mapping_v2(body),
        root_envelope.artifact_to_mapping_v2(anchor),
        root_envelope.artifact_to_mapping_v2(state),
    )


def _validate_actualness_and_terminal(
    *,
    raw: Mapping[str, Any],
    body: Mapping[str, Any],
    anchor: Mapping[str, Any],
    source_state: Mapping[str, Any],
    root_actualness: Mapping[str, Any],
    terminal_receipt: Mapping[str, Any],
) -> int:
    state_id = source_state.get("state_id")
    state_digest = source_state.get("digest")
    _verify_content_seal(
        root_actualness,
        id_field="actualness_id",
        id_prefix="q1-root-source-actualness:",
        name="root actualness",
    )
    if not (
        root_actualness.get("receipt_type") == "QOneRootSourceActualnessReceiptV1"
        and root_actualness.get("schema_version") == 1
        and _is_nonzero_git_oid(root_actualness.get("head_sha"))
        and _is_nonzero_git_oid(root_actualness.get("head_tree_sha"))
        and len(root_actualness["head_sha"]) == len(root_actualness["head_tree_sha"])
    ):
        _reject(
            BaseAdmissionRejectCode.SOURCE_REPLAY_FAILED,
            "actualness identity or nonzero HEAD binding is malformed",
        )
    for name in (
        "v3_registry_digest",
        "v3_role_manifest_digest",
        "initializer_grant_digest",
        "initializer_artifact_semantic_sha256",
        "issuer_grant_digest",
        "issuer_artifact_semantic_sha256",
        "fresh_module_binding_digest",
        "root_problem_digest",
        "raw_q_one_g_digest",
        "deterministic_initial_branch_replay_digest",
        "body_digest",
        "anchor_digest",
        "state_digest",
        "initializer_contract_digest",
        "domain_replay_digest",
    ):
        if not _is_nonzero_digest(root_actualness.get(name)):
            _reject(
                BaseAdmissionRejectCode.SOURCE_REPLAY_FAILED,
                f"actualness {name} is not a nonzero semantic binding",
            )
    p = raw.get("root_context")
    if type(p) is not int or type(p) is bool:
        _reject(BaseAdmissionRejectCode.SOURCE_REPLAY_FAILED, "raw root context is malformed")
    root_problem = {
        "schema_id": "q1_canonical_root_problem_v1",
        "root_context": p,
        "equation_rank": p,
        "equation_numerator": 4,
        "equation_denominator": p,
        "mark_kind_code": 1,
        "mark_root_context": p,
        "mark_equation_rank": p,
    }
    root_problem_digest = canonical_digest_v1(root_problem)
    raw_digest = canonical_digest_v1(raw)
    branch = {
        "schema_id": "q1_deterministic_initial_g_branch_replay_v1",
        "root_problem_id": "q1-root-problem:" + root_problem_digest,
        "root_problem_digest": root_problem_digest,
        "raw_q_one_g_digest": raw_digest,
        "q": 1,
        "endpoint_fiber_code": 2,
        "major_phase_code": 3,
        "provenance_code": 1,
        "mark_kind_code": 1,
        "gap_three_x": raw["gap_three_x"],
        "gap_three_factorization": raw["gap_three_factorization"],
        "body_id": body["body_id"],
        "body_digest": body["digest"],
        "anchor_id": anchor["anchor_id"],
        "anchor_digest": anchor["digest"],
        "state_id": source_state["state_id"],
        "state_digest": source_state["digest"],
        "state_authority": {
            "initializer_authority": False,
            "persistent_admission": False,
            "queue_authority": False,
        },
    }
    expected_actualness = {
        "v3_registry_id": "t6_coordinator_role_registry_v3",
        "initializer_grant_id": "q1_root_initializer_grant_v3",
        "initializer_artifact_id": "q1_root_initializer_envelope_v2",
        "issuer_grant_id": "q1_terminal_issuer_grant_v3",
        "issuer_artifact_id": "q1_terminal_issuer_v1",
        "root_problem": root_problem,
        "root_problem_id": "q1-root-problem:" + root_problem_digest,
        "root_problem_digest": root_problem_digest,
        "raw_q_one_g": raw,
        "raw_q_one_g_digest": raw_digest,
        "deterministic_initial_branch_replay": branch,
        "deterministic_initial_branch_replay_digest": canonical_digest_v1(branch),
        "body_id": body["body_id"],
        "body_digest": body["digest"],
        "anchor_id": anchor["anchor_id"],
        "anchor_digest": anchor["digest"],
        "state_id": source_state["state_id"],
        "state_digest": source_state["digest"],
        "initializer_id": root_envelope.INITIALIZER_ID,
        "initializer_contract_digest": anchor["contract_digest"],
        "domain_replay_id": root_envelope.DOMAIN_REPLAY_ID,
        "domain_replay_digest": anchor["domain_replay_digest"],
        "owner_domain_id": "ordinary_parentless_q1_g_root_v1",
        "occurrence_kind": "ROOT_INITIALIZER_OUTPUT",
        "parent_kind": "PARENTLESS_ROOT",
        "actualness_scope": "ROOT_OCCURRENCE_ONLY",
        "initializer_output_self_authorizing": False,
        "actualness_attestor_role": "TERMINAL_ISSUER",
        "source_actualness": True,
        "root_initializer_authority": True,
        "terminal_issuer_attestation_authority": True,
        "persistent_admission": False,
        "common_owner_authority": False,
        "e1_authority": False,
        "queue_authority": False,
    }
    actualness_mismatches = [
        name
        for name, expected in expected_actualness.items()
        if _json_copy(root_actualness.get(name)) != _json_copy(expected)
    ]
    if actualness_mismatches:
        _reject(
            BaseAdmissionRejectCode.SOURCE_REPLAY_FAILED,
            "actualness semantic preimage does not replay from raw source: "
            + ",".join(actualness_mismatches),
        )
    if not (
        root_actualness.get("state_id") == state_id
        and root_actualness.get("state_digest") == state_digest
        and root_actualness.get("source_actualness") is True
        and root_actualness.get("root_initializer_authority") is True
        and root_actualness.get("persistent_admission") is False
        and root_actualness.get("queue_authority") is False
    ):
        _reject(
            BaseAdmissionRejectCode.SOURCE_REPLAY_FAILED,
            "actualness does not bind the V2 root source",
        )
    if terminal_receipt.get("receipt_type") != V3_MISS_RECEIPT_TYPE:
        _reject(
            BaseAdmissionRejectCode.TERMINAL_SOURCE_NOT_MISS,
            "only a V3 production prefix-MISS is admissible",
        )
    _verify_content_seal(
        terminal_receipt,
        id_field="receipt_id",
        id_prefix="production-q1-prefix-miss:",
        name="V3 terminal receipt",
    )
    nested_actualness = terminal_receipt.get("root_actualness")
    if not (
        type(nested_actualness) is dict
        and nested_actualness.get("actualness_id")
        == root_actualness.get("actualness_id")
        and nested_actualness.get("digest") == root_actualness.get("digest")
        and terminal_receipt.get("state_id") == state_id
        and terminal_receipt.get("state_digest") == state_digest
        and terminal_receipt.get("root_actualness_digest")
        == root_actualness.get("digest")
    ):
        _reject(
            BaseAdmissionRejectCode.SOURCE_REPLAY_FAILED,
            "V3 terminal receipt belongs to another actual root",
        )
    if not (
        _is_nonzero_git_oid(terminal_receipt.get("head_sha"))
        and _is_nonzero_git_oid(terminal_receipt.get("head_tree_sha"))
        and terminal_receipt.get("head_sha") == root_actualness.get("head_sha")
        and terminal_receipt.get("head_tree_sha") == root_actualness.get("head_tree_sha")
    ):
        _reject(
            BaseAdmissionRejectCode.SOURCE_REPLAY_FAILED,
            "terminal and actualness HEAD bindings disagree or are zero",
        )
    for name in (
        "initializer_artifact_semantic_sha256",
        "issuer_artifact_semantic_sha256",
        "scheduler_artifact_semantic_sha256",
        "coverage_verifier_artifact_semantic_sha256",
        "assembler_artifact_semantic_sha256",
        "fresh_module_binding_digest",
        "schedule_digest",
    ):
        if not _is_nonzero_digest(terminal_receipt.get(name)):
            _reject(
                BaseAdmissionRejectCode.TERMINAL_SOURCE_NOT_MISS,
                f"terminal {name} is not a nonzero semantic binding",
            )
    if not (
        terminal_receipt.get("outcome") == V3_MISS_OUTCOME
        and terminal_receipt.get("coverage_semantics") == COVERAGE_SEMANTICS
        and terminal_receipt.get("ordered_gaps") == list(ORDERED_GAPS)
        and terminal_receipt.get("next_unchecked_gap") == NEXT_UNCHECKED_GAP
        and type(terminal_receipt.get("next_unchecked_gap")) is int
        and terminal_receipt.get("global_exhaustion") is False
        and terminal_receipt.get("selected_certificate") is None
        and terminal_receipt.get("selected_certificate_digest") is None
        and terminal_receipt.get("registered_prefix_miss_authority") is True
        and terminal_receipt.get("terminal_leaf_authority") is False
        and terminal_receipt.get("root_proof_close_authority") is False
    ):
        _reject(
            BaseAdmissionRejectCode.SCOPE_WIDENING,
            "V3 registered-prefix MISS scope changed",
        )
    root_context = terminal_receipt.get("root_context")
    if type(root_context) is not int or type(root_context) is bool or root_context <= 1:
        _reject(
            BaseAdmissionRejectCode.MALFORMED_FIELD,
            "root_context is not a positive exact integer",
        )
    if root_context != p:
        _reject(
            BaseAdmissionRejectCode.SOURCE_REPLAY_FAILED,
            "terminal root context differs from the raw source",
        )
    registered_scans = tuple(_scan_registered_gap(p, gap) for gap in ORDERED_GAPS)
    if any(scan["matching_certificates"] for scan in registered_scans):
        _reject(
            BaseAdmissionRejectCode.TERMINAL_SOURCE_NOT_MISS,
            "raw registered prefix contains an independently reconstructed terminal",
        )
    return root_context


def _facts() -> dict[str, Any]:
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


def _producer_rule_mapping() -> dict[str, Any]:
    return {
        "producer_id": PRODUCER_ID,
        "queue_gate": state_contract.ROOT_INITIALIZER_OUTPUT,
        "branch_ids": [BRANCH_ID],
        "source_owners": [],
        "target_owners": [TARGET_OWNER],
    }


def _producer_rules() -> dict[str, state_contract.ProducerRuleV1]:
    return {
        PRODUCER_ID: state_contract.ProducerRuleV1(
            producer_id=PRODUCER_ID,
            queue_gate=state_contract.ROOT_INITIALIZER_OUTPUT,
            branch_ids=frozenset({BRANCH_ID}),
            source_owners=frozenset(),
            target_owners=frozenset({TARGET_OWNER}),
        )
    }


def _factor(value: int) -> list[list[int]]:
    """Exact trial-division factorization for the finite registered scan."""

    if type(value) is not int or value < 1:
        _reject(BaseAdmissionRejectCode.MALFORMED_FIELD, "scan input is not positive")
    remainder = value
    result: list[list[int]] = []
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while remainder % divisor == 0:
            remainder //= divisor
            exponent += 1
        result.append([divisor, exponent])
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        result.append([remainder, 1])
    return result


def _divisors(factors: list[list[int]]) -> list[int]:
    result = [1]
    for prime, exponent in factors:
        result = [
            base * prime**power
            for base in result
            for power in range(2 * exponent + 1)
        ]
    return sorted(set(result))


def _certificate(
    p: int, gap: int, x: int, divisor: int, index: int, kind: str
) -> dict[str, Any] | None:
    quotient = x * x // divisor
    if kind == "TYPE_I":
        if (p * x + divisor) % gap or p * (x + p * quotient) % gap:
            return None
        y, z, candidate_index = (
            (p * x + divisor) // gap,
            p * (x + p * quotient) // gap,
            2 * index,
        )
    else:
        if (
            divisor > x
            or (x + divisor) % gap
            or p * (x + divisor) % gap
            or p * (x + quotient) % gap
        ):
            return None
        y, z, candidate_index = (
            p * (x + divisor) // gap,
            p * (x + quotient) // gap,
            2 * index + 1,
        )
    if 4 * x * y * z != p * (x * y + x * z + y * z):
        return None
    return {
        "certificate_type": kind,
        "gap": gap,
        "x": x,
        "divisor": divisor,
        "y": y,
        "z": z,
        "candidate_index": candidate_index,
    }


def _scan_registered_gap(p: int, gap: int) -> dict[str, Any]:
    if p % 4 != 1 or gap % 4 != 3:
        _reject(BaseAdmissionRejectCode.MALFORMED_FIELD, "invalid registered-gap scan")
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
        "gap": gap,
        "x": x,
        "factorization": factors,
        "divisor_universe": divisors,
        "matching_certificates": matches,
        "scan_status": "GAP_HAS_TERMINAL" if matches else "GAP_PREFIX_MISS",
    }
    return {**unsigned, "scan_digest": canonical_digest_v1(unsigned)}


def _terminal_projection(
    *,
    source_state: Mapping[str, Any],
    root_actualness: Mapping[str, Any],
    terminal_receipt: Mapping[str, Any],
    root_context: int,
) -> dict[str, Any]:
    binding = canonical_digest_v1(
        {
            "source_state_id": source_state["state_id"],
            "source_state_digest": source_state["digest"],
            "root_actualness_id": root_actualness["actualness_id"],
            "root_actualness_digest": root_actualness["digest"],
            "v3_terminal_receipt_id": terminal_receipt["receipt_id"],
            "v3_terminal_receipt_digest": terminal_receipt["digest"],
            "root_context": root_context,
            "scope": SCOPE_ID,
            "coverage_semantics": COVERAGE_SEMANTICS,
            "ordered_gaps": list(ORDERED_GAPS),
            "next_unchecked_gap": NEXT_UNCHECKED_GAP,
            "global_exhaustion": False,
        }
    )
    terminal_unsigned = {
        "schema_id": state_contract.TERMINAL_FIRST_SCHEMA_ID,
        "schema_version": 1,
        "receipt_id": V1_TERMINAL_RECEIPT_ID_PREFIX + binding,
        "scope": SCOPE_ID,
        "outcome": "MISS",
    }
    terminal = {
        **terminal_unsigned,
        "digest": canonical_digest_v1(terminal_unsigned),
    }
    values = {
        "receipt_type": TERMINAL_PROJECTION_TYPE,
        "schema_version": 1,
        "status": "V1_TERMINAL_FIRST_PROJECTED_NO_AUTHORITY",
        "artifact_class": "CANONICAL_PROJECTION_ONLY",
        "source_state_id": source_state["state_id"],
        "source_state_digest": source_state["digest"],
        "root_actualness_id": root_actualness["actualness_id"],
        "root_actualness_digest": root_actualness["digest"],
        "v3_terminal_receipt_id": terminal_receipt["receipt_id"],
        "v3_terminal_receipt_digest": terminal_receipt["digest"],
        "root_context": root_context,
        "coverage_semantics": COVERAGE_SEMANTICS,
        "ordered_gaps": list(ORDERED_GAPS),
        "next_unchecked_gap": NEXT_UNCHECKED_GAP,
        "global_exhaustion": False,
        "v1_terminal_first": terminal,
        "v1_terminal_first_digest": terminal["digest"],
        "projection_binding_digest": binding,
        "terminal_projection_authority": False,
        "persistent_admission": False,
        "queue_authority": False,
        "successor_authority": False,
        "e1_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
    }
    digest = canonical_digest_v1(values)
    return {
        **values,
        "receipt_id": TERMINAL_PROJECTION_ID_PREFIX + digest,
        "digest": digest,
    }


def _expected_v1_state(
    *,
    source_state: Mapping[str, Any],
    root_actualness: Mapping[str, Any],
    terminal_receipt: Mapping[str, Any],
    root_context: int,
) -> tuple[dict[str, Any], dict[str, Any], str]:
    projection = _terminal_projection(
        source_state=source_state,
        root_actualness=root_actualness,
        terminal_receipt=terminal_receipt,
        root_context=root_context,
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
    selector_facts = _facts()
    facts_digest = state_contract.canonical_digest_v1(selector_facts)
    semantic_origin = canonical_digest_v1(
        {
            "v2_source_state_id": source_state["state_id"],
            "v2_source_state_digest": source_state["digest"],
            "root_context": root_context,
            "producer_id": PRODUCER_ID,
            "branch_id": BRANCH_ID,
            "terminal_projection_binding_digest": projection[
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
            "terminal_first_digest": projection["v1_terminal_first"]["digest"],
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
        "terminal_first": projection["v1_terminal_first"],
        "source_receipt": source_receipt,
        "facts": selector_facts,
    }
    state["state_id"] = state_contract.build_state_id_v1(state)
    return state, projection, semantic_origin


def _validate_materialization(
    materialization: Mapping[str, Any],
    *,
    raw: Mapping[str, Any],
    body: Mapping[str, Any],
    anchor: Mapping[str, Any],
    source_state: Mapping[str, Any],
    root_actualness: Mapping[str, Any],
    terminal_receipt: Mapping[str, Any],
    expected_state: Mapping[str, Any],
    expected_projection: Mapping[str, Any],
    semantic_origin: str,
) -> None:
    if set(materialization) != MATERIALIZATION_FIELDS:
        _reject(
            BaseAdmissionRejectCode.MATERIALIZATION_MISMATCH,
            "materialization receipt has missing or unknown fields",
        )
    if not (
        materialization.get("receipt_type") == MATERIALIZATION_RECEIPT_TYPE
        and type(materialization.get("schema_version")) is int
        and materialization.get("schema_version") == 1
    ):
        _reject(
            BaseAdmissionRejectCode.MATERIALIZATION_MISMATCH,
            "candidate is not the exact materialization receipt type",
        )
    _verify_content_seal(
        materialization,
        id_field="receipt_id",
        id_prefix=MATERIALIZATION_RECEIPT_ID_PREFIX,
        name="materialization receipt",
    )
    materializer_grant = materialization.get("role_grant")
    if not (
        type(materializer_grant) is dict
        and set(materializer_grant) == GRANT_FIELDS
        and materializer_grant.get("grant_id") == MATERIALIZER_GRANT_ID
        and materializer_grant.get("role") == MATERIALIZER_ROLE
        and materializer_grant.get("artifact_id") == MATERIALIZER_ARTIFACT_ID
        and materializer_grant.get("artifact_path")
        == "scripts/t6_q_one_root_v1_base_materializer_v1.py"
        and materializer_grant.get("artifact_symbols")
        == ["materialize_q_one_root_v1_base_state_v1", "base_materialization_receipt_to_mapping_v1"]
        and materializer_grant.get("capabilities")
        == ["MATERIALIZE_Q1_G_V1_ROOT_INITIALIZER_OUTPUT"]
        and materializer_grant.get("authority_class")
        == AUTHORITY_CLASS
        and _is_nonzero_digest(materializer_grant.get("artifact_semantic_sha256"))
        and materialization.get("role_grant_id") == MATERIALIZER_GRANT_ID
        and materialization.get("role_grant_digest")
        == canonical_digest_v1(materializer_grant)
        and materialization.get("role_artifact_id") == MATERIALIZER_ARTIFACT_ID
        and materialization.get("role_artifact_semantic_sha256")
        == materializer_grant.get("artifact_semantic_sha256")
        and _is_nonzero_digest(materialization.get("role_artifact_semantic_sha256"))
        and materialization.get("status") == MATERIALIZATION_STATUS
        and materialization.get("role") == MATERIALIZER_ROLE
        and materialization.get("role_artifact_id") == MATERIALIZER_ARTIFACT_ID
        and materialization.get("raw_q_one_g") == raw
        and materialization.get("source_body") == body
        and materialization.get("root_anchor") == anchor
        and materialization.get("source_state") == source_state
        and materialization.get("root_actualness") == root_actualness
        and materialization.get("terminal_receipt") == terminal_receipt
        and materialization.get("terminal_projection") == expected_projection
        and materialization.get("producer_rule") == _producer_rule_mapping()
        and materialization.get("producer_rule_digest")
        == canonical_digest_v1(_producer_rule_mapping())
        and materialization.get("semantic_origin_digest") == semantic_origin
        and materialization.get("v1_state") == expected_state
        and materialization.get("v1_state_id") == expected_state["state_id"]
        and materialization.get("v1_state_wire_digest")
        == canonical_digest_v1(expected_state)
        and _matches_root_potential(
            materialization.get("canonical_root_potential_evidence"),
            expected_state["equation_rank"],
        )
        and materialization.get("canonical_root_potential_evidence_digest")
        == canonical_digest_v1(
            [expected_state["equation_rank"], 3, 0, 0, 0, 0, 0]
        )
        and materialization.get("local_grant_authenticates_head") is False
        and materialization.get("repository_authority") is False
        and materialization.get("root_base_materialization_authority") is True
    ):
        _reject(
            BaseAdmissionRejectCode.MATERIALIZATION_MISMATCH,
            "materialization wire differs from the independent reconstruction",
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
        if materialization.get(name) is not False:
            _reject(
                BaseAdmissionRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
                f"materializer field {name} must remain false",
            )


def _validate_v4_owner(
    owner: Mapping[str, Any],
    *,
    raw: Mapping[str, Any],
    body: Mapping[str, Any],
    anchor: Mapping[str, Any],
    source_state: Mapping[str, Any],
    root_actualness: Mapping[str, Any],
    expected_facts: Mapping[str, Any],
) -> None:
    if owner.get("receipt_type") != V4_OWNER_RECEIPT_TYPE:
        _reject(BaseAdmissionRejectCode.V4_OWNER_MISMATCH, "V4 owner type changed")
    _verify_content_seal(
        owner,
        id_field="receipt_id",
        id_prefix=V4_OWNER_RECEIPT_ID_PREFIX,
        name="V4 owner receipt",
    )
    header = {
        "state_id": source_state["state_id"],
        "state_digest": source_state["digest"],
        "root_context": raw["root_context"],
        "equation_rank": raw["equation_rank"],
        "mark_kind": "ROOT_SOL",
        "mark_root_context": raw["mark_root_context"],
        "mark_equation_rank": raw["mark_equation_rank"],
        "facts": _json_copy(expected_facts),
    }
    validated_facts = state_contract._validate_facts(
        expected_facts, raw["root_context"], state_contract.ROOT_SOL
    )
    reference_header = state_contract.VerifiedSelectorHeaderV1(
        state_id=source_state["state_id"],
        queue_gate=state_contract.ROOT_INITIALIZER_OUTPUT,
        producer_id="v4_reference_equivalence_only",
        branch_id="q1_g_root",
        parent_state_id=None,
        root_context=raw["root_context"],
        equation_rank=raw["equation_rank"],
        mark_kind=state_contract.ROOT_SOL,
        mark_receipt_digest="0" * 64,
        terminal_first_digest="1" * 64,
        source_receipt_digest="2" * 64,
        facts_digest=state_contract.canonical_digest_v1(dict(validated_facts)),
        facts=validated_facts,
    )
    classification = state_contract.classify_selector_owner_v1(reference_header)
    expected_owner_id = state_contract.owner_digest_v1(
        reference_header,
        classification.owner,
        classification.matched_families,
        classification.precedence_index,
    )
    expected_predicates = {
        item.family_id: bool(item.predicate(reference_header))
        for item in state_contract.FAMILY_PREDICATES_V1
    }
    if not (
        _json_copy(owner.get("raw_q_one_g")) == _json_copy(raw)
        and _json_copy(owner.get("source_body")) == _json_copy(body)
        and _json_copy(owner.get("root_anchor")) == _json_copy(anchor)
        and _json_copy(owner.get("source_state")) == _json_copy(source_state)
        and _json_copy(owner.get("root_actualness")) == _json_copy(root_actualness)
        and owner.get("raw_q_one_g_digest") == canonical_digest_v1(raw)
        and owner.get("body_id") == body["body_id"]
        and owner.get("body_digest") == body["digest"]
        and owner.get("anchor_id") == anchor["anchor_id"]
        and owner.get("anchor_digest") == anchor["digest"]
        and owner.get("state_id") == source_state.get("state_id")
        and owner.get("state_digest") == source_state.get("digest")
        and owner.get("root_actualness_id") == root_actualness.get("actualness_id")
        and owner.get("root_actualness_digest") == root_actualness.get("digest")
        and _json_copy(owner.get("normalized_header")) == header
        and owner.get("normalized_header_digest") == canonical_digest_v1(header)
        and owner.get("facts_digest") == reference_header.facts_digest
        and _json_copy(owner.get("predicate_results")) == expected_predicates
        and owner.get("predicate_results_digest") == canonical_digest_v1(expected_predicates)
        and owner.get("family_precedence") == list(state_contract.FAMILY_PRECEDENCE_V1)
        and owner.get("family_precedence_digest")
        == canonical_digest_v1({"family_precedence": list(state_contract.FAMILY_PRECEDENCE_V1)})
        and owner.get("owner_contract_id") == state_contract.CONTRACT_ID
        and owner.get("owner_contract_schema_version") == 1
        and owner.get("owner") == classification.owner == TARGET_OWNER
        and owner.get("matched_families") == list(classification.matched_families)
        and owner.get("precedence_index") == classification.precedence_index == 2
        and owner.get("owner_id") == expected_owner_id
        and owner.get("owner_digest") == expected_owner_id.removeprefix("owner:")
        and owner.get("owner_scope") == "ROOT_SOURCE_DISPATCH_ONLY"
        and owner.get("common_owner_authority") is True
        and owner.get("persistent_admission") is False
        and owner.get("queue_authority") is False
        and owner.get("e1_authority") is False
    ):
        _reject(
            BaseAdmissionRejectCode.V4_OWNER_MISMATCH,
            "V4 owner does not describe the same non-admitted q=1 G root",
        )
    if not (
        _is_nonzero_digest(owner.get("owner_digest"))
        and _is_nonzero_digest(owner.get("role_artifact_semantic_sha256"))
        and type(owner.get("schema_version")) is int
        and owner.get("schema_version") == 2
        and owner.get("status") == "COMMON_OWNER_CLASSIFIED"
        and owner.get("role") == "COMMON_ROOT_OWNER_CLASSIFIER"
        and owner.get("role_grant_id") == "q1_common_root_owner_classifier_grant_v4"
    ):
        _reject(
            BaseAdmissionRejectCode.V4_OWNER_MISMATCH,
            "V4 owner ID/digest/version or local semantic pin is malformed",
        )


def _validate_v4_scope(
    scope: Mapping[str, Any],
    *,
    raw: Mapping[str, Any],
    body: Mapping[str, Any],
    anchor: Mapping[str, Any],
    source_state: Mapping[str, Any],
    root_actualness: Mapping[str, Any],
    owner: Mapping[str, Any],
    terminal_receipt: Mapping[str, Any],
) -> None:
    if scope.get("receipt_type") != V4_SCOPE_RECEIPT_TYPE:
        _reject(BaseAdmissionRejectCode.V4_SCOPE_MISMATCH, "V4 scope type changed")
    _verify_content_seal(
        scope,
        id_field="receipt_id",
        id_prefix=V4_SCOPE_RECEIPT_ID_PREFIX,
        name="V4 scope receipt",
    )
    p = raw["root_context"]
    registered = tuple(_scan_registered_gap(p, gap) for gap in ORDERED_GAPS)
    outside = tuple(_scan_registered_gap(p, gap) for gap in OUTSIDE_CONTROL_GAPS)
    registered_replay = canonical_digest_v1(
        {
            "scope_id": SCOPE_ID,
            "root_context": p,
            "ordered_gaps": list(ORDERED_GAPS),
            "scans": list(registered),
            "global_exhaustion": False,
            "next_unchecked_gap": NEXT_UNCHECKED_GAP,
        }
    )
    outside_replay = canonical_digest_v1(
        {
            "scope_id": SCOPE_ID,
            "root_context": p,
            "gaps": list(OUTSIDE_CONTROL_GAPS),
            "scans": list(outside),
            "outside_registered_scope": True,
        }
    )
    if any(scan["matching_certificates"] for scan in registered):
        _reject(
            BaseAdmissionRejectCode.V4_SCOPE_MISMATCH,
            "registered V4 scope contradicts an independently found terminal",
        )
    if not (
        type(scope.get("schema_version")) is int
        and scope.get("schema_version") == 2
        and scope.get("status") == "REGISTERED_PREFIX_SCOPE_VALIDATED_NO_E1"
        and scope.get("role") == "INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR"
        and scope.get("role_grant_id") == "q1_scope_aware_e1_validator_grant_v4"
        and _is_nonzero_digest(scope.get("role_artifact_semantic_sha256"))
        and _json_copy(scope.get("raw_q_one_g")) == _json_copy(raw)
        and _json_copy(scope.get("source_body")) == _json_copy(body)
        and _json_copy(scope.get("root_anchor")) == _json_copy(anchor)
        and _json_copy(scope.get("source_state")) == _json_copy(source_state)
        and _json_copy(scope.get("root_actualness")) == _json_copy(root_actualness)
        and scope.get("raw_q_one_g_digest") == canonical_digest_v1(raw)
        and scope.get("body_id") == body["body_id"]
        and scope.get("body_digest") == body["digest"]
        and scope.get("anchor_id") == anchor["anchor_id"]
        and scope.get("anchor_digest") == anchor["digest"]
        and scope.get("state_id") == source_state["state_id"]
        and scope.get("state_digest") == source_state["digest"]
        and scope.get("root_actualness_id") == root_actualness["actualness_id"]
        and scope.get("root_actualness_digest") == root_actualness["digest"]
        and _json_copy(scope.get("owner_receipt")) == _json_copy(owner)
        and _json_copy(scope.get("terminal_receipt")) == _json_copy(terminal_receipt)
        and scope.get("owner_receipt_id") == owner.get("receipt_id")
        and scope.get("owner_receipt_digest") == owner.get("digest")
        and scope.get("terminal_receipt_id") == terminal_receipt.get("receipt_id")
        and scope.get("terminal_receipt_digest") == terminal_receipt.get("digest")
        and scope.get("scope_id") == SCOPE_ID
        and scope.get("coverage_semantics") == COVERAGE_SEMANTICS
        and scope.get("ordered_gaps") == list(ORDERED_GAPS)
        and scope.get("next_unchecked_gap") == NEXT_UNCHECKED_GAP
        and scope.get("candidate_order") == CANDIDATE_ORDER
        and _json_copy(scope.get("registered_gap_scans")) == list(registered)
        and _json_copy(scope.get("outside_scope_gap_scans")) == list(outside)
        and scope.get("registered_prefix_replay_digest") == registered_replay
        and scope.get("outside_scope_control_digest") == outside_replay
        and scope.get("global_exhaustion") is False
        and scope.get("registered_prefix_miss_authority") is True
        and scope.get("scope_validation_authority") is True
        and scope.get("common_owner_authority") is False
        and scope.get("root_source_scoped_e1") is False
        and scope.get("e1_authority") is False
        and scope.get("persistent_admission") is False
        and scope.get("queue_authority") is False
    ):
        _reject(
            BaseAdmissionRejectCode.V4_SCOPE_MISMATCH,
            "V4 scope receipt was widened or rebound",
        )


def _header_mapping(header: state_contract.VerifiedSelectorHeaderV1) -> dict[str, Any]:
    return {
        "state_id": header.state_id,
        "queue_gate": header.queue_gate,
        "producer_id": header.producer_id,
        "branch_id": header.branch_id,
        "parent_state_id": header.parent_state_id,
        "root_context": header.root_context,
        "equation_rank": header.equation_rank,
        "mark_kind": header.mark_kind,
        "mark_receipt_digest": header.mark_receipt_digest,
        "terminal_first_digest": header.terminal_first_digest,
        "source_receipt_digest": header.source_receipt_digest,
        "facts_digest": header.facts_digest,
        "facts": dict(header.facts),
    }


@dataclass(frozen=True, init=False, slots=True)
class QOneRootV1BaseAdmissionReceiptV1:
    ARTIFACT_TYPE: ClassVar[str] = RECEIPT_TYPE

    schema_version: int
    status: str
    role: str
    role_grant: Mapping[str, Any]
    role_grant_id: str
    role_grant_digest: str
    role_artifact_id: str
    role_artifact_semantic_sha256: str
    materialization_receipt: Mapping[str, Any]
    materialization_receipt_id: str
    materialization_receipt_digest: str
    v4_owner_receipt: Mapping[str, Any]
    v4_owner_receipt_id: str
    v4_owner_receipt_digest: str
    v4_scope_receipt: Mapping[str, Any]
    v4_scope_receipt_id: str
    v4_scope_receipt_digest: str
    source_state_id: str
    source_state_digest: str
    v1_contract_id: str
    v1_state_schema_id: str
    v1_state_schema_version: int
    v1_state: Mapping[str, Any]
    v1_state_id: str
    v1_state_wire_digest: str
    canonical_root_potential_evidence: tuple[int, int, int, int, int, int, int]
    canonical_root_potential_evidence_digest: str
    local_grant_authenticates_head: bool
    repository_authority: bool
    producer_rule: Mapping[str, Any]
    producer_rule_digest: str
    verified_header: Mapping[str, Any]
    verified_header_digest: str
    family_precedence: tuple[str, ...]
    family_precedence_digest: str
    predicate_results: Mapping[str, bool]
    predicate_results_digest: str
    matched_families: tuple[str, ...]
    owner: str
    precedence_index: int
    v4_owner_id: str
    v4_owner_digest: str
    v1_owner_digest: str
    owner_translation_binding_digest: str
    admission_decision: str
    admission_reason: str
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
    generic_owner_authority: bool
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
    "materialization_receipt",
    "v4_owner_receipt",
    "v4_scope_receipt",
    "v1_state",
    "producer_rule",
    "verified_header",
    "predicate_results",
}


def _unsigned(values: Mapping[str, Any]) -> dict[str, Any]:
    result = {"receipt_type": RECEIPT_TYPE}
    for field in fields(QOneRootV1BaseAdmissionReceiptV1):
        if field.name not in {"receipt_id", "digest"}:
            result[field.name] = _json_copy(values[field.name])
    return result


def _construct(values: Mapping[str, Any]) -> QOneRootV1BaseAdmissionReceiptV1:
    result = object.__new__(QOneRootV1BaseAdmissionReceiptV1)
    for field in fields(QOneRootV1BaseAdmissionReceiptV1):
        value = values[field.name]
        if field.name in _MAPPING_FIELDS:
            value = MappingProxyType(_json_copy(value))
        object.__setattr__(result, field.name, value)
    return result


def _validate_admission_receipt(receipt: QOneRootV1BaseAdmissionReceiptV1) -> None:
    if type(receipt) is not QOneRootV1BaseAdmissionReceiptV1:
        _reject(
            BaseAdmissionRejectCode.INPUT_NOT_EXACT_MAPPING,
            "admission receipt has the wrong class",
        )
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    digest = canonical_digest_v1(_unsigned(values))
    if receipt.digest != digest or receipt.receipt_id != RECEIPT_ID_PREFIX + digest:
        _reject(
            BaseAdmissionRejectCode.DIGEST_MISMATCH,
            "admission receipt seal does not replay",
        )
    grant, grant_digest = _grant(_json_copy(receipt.role_grant))
    if not (
        receipt.role_grant_id == grant["grant_id"]
        and receipt.role_grant_digest == grant_digest
        and receipt.role_artifact_id == grant["artifact_id"]
        and receipt.role_artifact_semantic_sha256
        == grant["artifact_semantic_sha256"]
    ):
        _reject(BaseAdmissionRejectCode.GRANT_MISMATCH, "admission grant changed")
    materialization = _json_copy(receipt.materialization_receipt)
    raw, body, anchor, source_state = _source_chain(
        materialization.get("raw_q_one_g"),
        materialization.get("source_body"),
        materialization.get("root_anchor"),
        materialization.get("source_state"),
    )
    actualness = _exact_mapping(materialization.get("root_actualness"), "root_actualness")
    terminal = _exact_mapping(materialization.get("terminal_receipt"), "terminal_receipt")
    root_context = _validate_actualness_and_terminal(
        raw=raw,
        body=body,
        anchor=anchor,
        source_state=source_state,
        root_actualness=actualness,
        terminal_receipt=terminal,
    )
    expected_state, projection, semantic_origin = _expected_v1_state(
        source_state=source_state,
        root_actualness=actualness,
        terminal_receipt=terminal,
        root_context=root_context,
    )
    _validate_materialization(
        materialization,
        raw=raw,
        body=body,
        anchor=anchor,
        source_state=source_state,
        root_actualness=actualness,
        terminal_receipt=terminal,
        expected_state=expected_state,
        expected_projection=projection,
        semantic_origin=semantic_origin,
    )
    owner_receipt = _json_copy(receipt.v4_owner_receipt)
    scope_receipt = _json_copy(receipt.v4_scope_receipt)
    _validate_v4_owner(
        owner_receipt,
        raw=raw,
        body=body,
        anchor=anchor,
        source_state=source_state,
        root_actualness=actualness,
        expected_facts=_facts(),
    )
    _validate_v4_scope(
        scope_receipt,
        raw=raw,
        body=body,
        anchor=anchor,
        source_state=source_state,
        root_actualness=actualness,
        owner=owner_receipt,
        terminal_receipt=terminal,
    )
    rules = _producer_rules()
    decision = state_contract.reject_before_persistent_queue_v1(expected_state, rules)
    if not decision.accepted:
        _reject(
            BaseAdmissionRejectCode.V1_GATE_REJECTED,
            f"actual V1 gate rejected the root: {decision.reason_code.value}",
        )
    header = state_contract.extract_verified_selector_header_v1(expected_state, rules)
    classification = state_contract.classify_selector_owner_v1(header)
    predicate_results = {
        item.family_id: bool(item.predicate(header))
        for item in state_contract.FAMILY_PREDICATES_V1
    }
    header_wire = _header_mapping(header)
    translation = canonical_digest_v1(
        {
            "v2_state_id": source_state["state_id"],
            "v2_state_digest": source_state["digest"],
            "v4_owner_receipt_id": owner_receipt["receipt_id"],
            "v4_owner_receipt_digest": owner_receipt["digest"],
            "v4_owner_id": owner_receipt["owner_id"],
            "v4_owner_digest": owner_receipt["owner_digest"],
            "v1_state_id": expected_state["state_id"],
            "v1_state_wire_digest": canonical_digest_v1(expected_state),
            "v1_owner_digest": classification.owner_digest,
            "facts_digest": header.facts_digest,
            "owner": classification.owner,
            "matched_families": list(classification.matched_families),
            "precedence_index": classification.precedence_index,
        }
    )
    expected_checks = (
        type(receipt.schema_version) is int,
        receipt.schema_version == 1,
        receipt.status == STATUS,
        receipt.role == ROLE,
        receipt.materialization_receipt_id == materialization["receipt_id"],
        receipt.materialization_receipt_digest == materialization["digest"],
        receipt.v4_owner_receipt_id == owner_receipt["receipt_id"],
        receipt.v4_owner_receipt_digest == owner_receipt["digest"],
        receipt.v4_scope_receipt_id == scope_receipt["receipt_id"],
        receipt.v4_scope_receipt_digest == scope_receipt["digest"],
        receipt.source_state_id == source_state["state_id"],
        receipt.source_state_digest == source_state["digest"],
        receipt.v1_contract_id == state_contract.CONTRACT_ID,
        receipt.v1_state_schema_id == state_contract.STATE_SCHEMA_ID,
        receipt.v1_state_schema_version == state_contract.STATE_SCHEMA_VERSION,
        _json_copy(receipt.v1_state) == expected_state,
        receipt.v1_state_id == expected_state["state_id"],
        receipt.v1_state_wire_digest == canonical_digest_v1(expected_state),
        _matches_root_potential(
            receipt.canonical_root_potential_evidence,
            expected_state["equation_rank"],
        ),
        receipt.canonical_root_potential_evidence_digest
        == canonical_digest_v1(
            [expected_state["equation_rank"], 3, 0, 0, 0, 0, 0]
        ),
        receipt.local_grant_authenticates_head is False,
        receipt.repository_authority is False,
        _json_copy(receipt.producer_rule) == _producer_rule_mapping(),
        receipt.producer_rule_digest == canonical_digest_v1(_producer_rule_mapping()),
        _json_copy(receipt.verified_header) == header_wire,
        receipt.verified_header_digest == canonical_digest_v1(header_wire),
        receipt.family_precedence == tuple(state_contract.FAMILY_PRECEDENCE_V1),
        receipt.family_precedence_digest
        == canonical_digest_v1(list(state_contract.FAMILY_PRECEDENCE_V1)),
        _json_copy(receipt.predicate_results) == predicate_results,
        receipt.predicate_results_digest == canonical_digest_v1(predicate_results),
        receipt.matched_families == classification.matched_families,
        receipt.owner == classification.owner == TARGET_OWNER,
        receipt.precedence_index == classification.precedence_index == 2,
        receipt.v4_owner_id == owner_receipt["owner_id"],
        receipt.v4_owner_digest == owner_receipt["owner_digest"],
        receipt.v1_owner_digest == classification.owner_digest,
        receipt.owner_translation_binding_digest == translation,
        receipt.admission_decision == "ACCEPT",
        receipt.admission_reason == state_contract.RejectCode.ACCEPT.value,
        receipt.root_base_materialization_authority is False,
        receipt.v1_base_owner_authority is True,
        receipt.root_base_admission_authority is True,
        receipt.persistent_admission is True,
    )
    if not all(expected_checks):
        _reject(
            BaseAdmissionRejectCode.OWNER_TRANSLATION_MISMATCH,
            "admission, V1 owner, or V4-to-V1 translation changed",
        )
    for name in (
        "queue_authority",
        "enqueue_authority",
        "enqueue_performed",
        "successor_admission",
        "producer_authority",
        "producer_continuation_allowed",
        "generic_owner_authority",
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
                BaseAdmissionRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
                f"base admission field {name} must be false",
            )


def verify_and_admit_q_one_root_v1_base_v1(
    *,
    raw_q_one_g: dict[str, Any],
    source_body: dict[str, Any],
    root_anchor: dict[str, Any],
    source_state: dict[str, Any],
    root_actualness: dict[str, Any],
    terminal_receipt: dict[str, Any],
    materialization_receipt: dict[str, Any],
    v4_owner_receipt: dict[str, Any],
    v4_scope_receipt: dict[str, Any],
    role_grant: dict[str, Any],
) -> QOneRootV1BaseAdmissionReceiptV1:
    """Issue a V1 base-admission receipt without enqueueing any state."""

    raw, body, anchor, state = _source_chain(
        raw_q_one_g, source_body, root_anchor, source_state
    )
    actualness = _exact_mapping(root_actualness, "root_actualness")
    terminal = _exact_mapping(terminal_receipt, "terminal_receipt")
    materialization = _exact_mapping(materialization_receipt, "materialization_receipt")
    owner_receipt = _exact_mapping(v4_owner_receipt, "v4_owner_receipt")
    scope_receipt = _exact_mapping(v4_scope_receipt, "v4_scope_receipt")
    grant, grant_digest = _grant(role_grant)
    root_context = _validate_actualness_and_terminal(
        raw=raw,
        body=body,
        anchor=anchor,
        source_state=state,
        root_actualness=actualness,
        terminal_receipt=terminal,
    )
    expected_state, projection, semantic_origin = _expected_v1_state(
        source_state=state,
        root_actualness=actualness,
        terminal_receipt=terminal,
        root_context=root_context,
    )
    _validate_materialization(
        materialization,
        raw=raw,
        body=body,
        anchor=anchor,
        source_state=state,
        root_actualness=actualness,
        terminal_receipt=terminal,
        expected_state=expected_state,
        expected_projection=projection,
        semantic_origin=semantic_origin,
    )
    _validate_v4_owner(
        owner_receipt,
        raw=raw,
        body=body,
        anchor=anchor,
        source_state=state,
        root_actualness=actualness,
        expected_facts=_facts(),
    )
    _validate_v4_scope(
        scope_receipt,
        raw=raw,
        body=body,
        anchor=anchor,
        source_state=state,
        root_actualness=actualness,
        owner=owner_receipt,
        terminal_receipt=terminal,
    )
    rules = _producer_rules()
    decision = state_contract.reject_before_persistent_queue_v1(expected_state, rules)
    if not decision.accepted:
        _reject(
            BaseAdmissionRejectCode.V1_GATE_REJECTED,
            f"actual V1 gate rejected the root: {decision.reason_code.value}",
        )
    header = state_contract.extract_verified_selector_header_v1(expected_state, rules)
    classification = state_contract.classify_selector_owner_v1(header)
    if not (
        classification.owner == TARGET_OWNER
        and classification.matched_families == (TARGET_OWNER,)
        and classification.precedence_index == 2
        and decision.owner_digest == classification.owner_digest
    ):
        _reject(
            BaseAdmissionRejectCode.V1_GATE_REJECTED,
            "V1 base classification is not the unique q=1 G owner",
        )
    predicate_results = {
        item.family_id: bool(item.predicate(header))
        for item in state_contract.FAMILY_PREDICATES_V1
    }
    header_wire = _header_mapping(header)
    translation = canonical_digest_v1(
        {
            "v2_state_id": state["state_id"],
            "v2_state_digest": state["digest"],
            "v4_owner_receipt_id": owner_receipt["receipt_id"],
            "v4_owner_receipt_digest": owner_receipt["digest"],
            "v4_owner_id": owner_receipt["owner_id"],
            "v4_owner_digest": owner_receipt["owner_digest"],
            "v1_state_id": expected_state["state_id"],
            "v1_state_wire_digest": canonical_digest_v1(expected_state),
            "v1_owner_digest": classification.owner_digest,
            "facts_digest": header.facts_digest,
            "owner": classification.owner,
            "matched_families": list(classification.matched_families),
            "precedence_index": classification.precedence_index,
        }
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
        "materialization_receipt": materialization,
        "materialization_receipt_id": materialization["receipt_id"],
        "materialization_receipt_digest": materialization["digest"],
        "v4_owner_receipt": owner_receipt,
        "v4_owner_receipt_id": owner_receipt["receipt_id"],
        "v4_owner_receipt_digest": owner_receipt["digest"],
        "v4_scope_receipt": scope_receipt,
        "v4_scope_receipt_id": scope_receipt["receipt_id"],
        "v4_scope_receipt_digest": scope_receipt["digest"],
        "source_state_id": state["state_id"],
        "source_state_digest": state["digest"],
        "v1_contract_id": state_contract.CONTRACT_ID,
        "v1_state_schema_id": state_contract.STATE_SCHEMA_ID,
        "v1_state_schema_version": state_contract.STATE_SCHEMA_VERSION,
        "v1_state": expected_state,
        "v1_state_id": expected_state["state_id"],
        "v1_state_wire_digest": canonical_digest_v1(expected_state),
        "canonical_root_potential_evidence": (
            expected_state["equation_rank"],
            3,
            0,
            0,
            0,
            0,
            0,
        ),
        "canonical_root_potential_evidence_digest": canonical_digest_v1(
            [expected_state["equation_rank"], 3, 0, 0, 0, 0, 0]
        ),
        "local_grant_authenticates_head": False,
        "repository_authority": False,
        "producer_rule": _producer_rule_mapping(),
        "producer_rule_digest": canonical_digest_v1(_producer_rule_mapping()),
        "verified_header": header_wire,
        "verified_header_digest": canonical_digest_v1(header_wire),
        "family_precedence": tuple(state_contract.FAMILY_PRECEDENCE_V1),
        "family_precedence_digest": canonical_digest_v1(
            list(state_contract.FAMILY_PRECEDENCE_V1)
        ),
        "predicate_results": predicate_results,
        "predicate_results_digest": canonical_digest_v1(predicate_results),
        "matched_families": classification.matched_families,
        "owner": classification.owner,
        "precedence_index": classification.precedence_index,
        "v4_owner_id": owner_receipt["owner_id"],
        "v4_owner_digest": owner_receipt["owner_digest"],
        "v1_owner_digest": classification.owner_digest,
        "owner_translation_binding_digest": translation,
        "admission_decision": "ACCEPT",
        "admission_reason": state_contract.RejectCode.ACCEPT.value,
        "root_base_materialization_authority": False,
        "v1_base_owner_authority": True,
        "root_base_admission_authority": True,
        "persistent_admission": True,
        "queue_authority": False,
        "enqueue_authority": False,
        "enqueue_performed": False,
        "successor_admission": False,
        "producer_authority": False,
        "producer_continuation_allowed": False,
        "generic_owner_authority": False,
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
    _validate_admission_receipt(result)
    return result


def base_admission_receipt_to_mapping_v1(
    receipt: QOneRootV1BaseAdmissionReceiptV1,
) -> dict[str, Any]:
    _validate_admission_receipt(receipt)
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
    "BaseAdmissionError",
    "BaseAdmissionRejectCode",
    "CAPABILITIES",
    "GRANT_ID",
    "QOneRootV1BaseAdmissionReceiptV1",
    "ROLE",
    "STATUS",
    "base_admission_receipt_to_mapping_v1",
    "canonical_digest_v1",
    "verify_and_admit_q_one_root_v1_base_v1",
]
