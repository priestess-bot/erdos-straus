#!/usr/bin/env python3
"""Pure, scope-aware consumer for a q=1 registered-prefix MISS.

The consumer is intentionally a small mathematical boundary, not a scheduler
or a transition producer.  It accepts explicit serialized source artifacts and
receipts, independently replays the ordinary q=1 G source, verifies the
registered-prefix scans (gaps 3, 7, 11), and rejects a terminal HIT.  Only the
deterministic root-source phase-root occurrence is issued.  No generic or
successor E1, producer continuation, admission, queue, or E2--E5 authority is
created.

No repository/runtime module is imported.  A caller-supplied grant is merely a
typed capability preimage; exact-HEAD authentication belongs to the V4
orchestrator and post-issuance replayer.
"""

from __future__ import annotations

from dataclasses import dataclass, fields
from enum import Enum
import hashlib
import json
from math import gcd, isqrt
import re
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, NoReturn


SCHEMA_VERSION = 2
RECEIPT_TYPE = "Q1_REGISTERED_PREFIX_ROOT_SOURCE_E1_RECEIPT_V2"
STATUS = "ROOT_SOURCE_SCOPED_E1_ISSUED"
ROLE = "REGISTERED_PREFIX_E1_CONSUMER"
ARTIFACT_ID = "q1_registered_prefix_e1_consumer_v2"
ARTIFACT_PATH = "scripts/t6_q_one_registered_prefix_e1_consumer_v2.py"
ARTIFACT_SYMBOLS = (
    "consume_q_one_registered_prefix_miss_for_e1_v2",
    "root_source_scoped_e1_receipt_to_mapping_v2",
)
GRANT_ID = "q1_registered_prefix_e1_consumer_grant_v4"
CAPABILITIES = ("ISSUE_REGISTERED_PREFIX_ROOT_SOURCE_SCOPED_E1",)
AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V4"

OWNER_RECEIPT_TYPE = "COMMON_Q1_ROOT_OWNER_RECEIPT_V2"
OWNER = "type_ii_relation_g_endpoint"
OWNER_DOMAIN_ID = "ordinary_parentless_q1_g_root_v1"
VALIDATION_RECEIPT_TYPE = "Q1_REGISTERED_PREFIX_SCOPE_VALIDATION_RECEIPT_V2"
VALIDATION_STATUS = "REGISTERED_PREFIX_SCOPE_VALIDATED_NO_E1"
PRODUCTION_MISS_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"
SCOPE_ID = "q1_root_after_gap_3_7_11_registered_prefix_v1"
COVERAGE_SEMANTICS = "REGISTERED_PRIORITY_ONLY"
ORDERED_GAPS = (3, 7, 11)
NEXT_UNCHECKED_GAP = 15
OUTSIDE_CONTROL_GAPS = (23,)
CANDIDATE_ORDER = "gap_ascending_divisor_ascending_type_I_before_II"

RAW_SCHEMA_ID = "q1_root_initializer_raw_v2"
RAW_SCHEMA_VERSION = 2
INITIALIZER_ID = "q_one_root_initializer_envelope_v2"
DOMAIN_REPLAY_ID = "q_one_g_raw_integer_replay_v2"
SOURCE_TREE_SCOPE = "type_ii_endpoint_only"
EVIDENCE_CLASS = "EVIDENCE_ONLY_ROOT_SOURCE"
ROOT_ORIGIN_KIND = "PARENTLESS_ROOT"
BODY_ID_PREFIX = "q1-source-body:"
ANCHOR_ID_PREFIX = "root-init-anchor:"
STATE_ID_PREFIX = "state:"
ACTUALNESS_ID_PREFIX = "q1-root-source-actualness:"
ROOT_PROBLEM_ID_PREFIX = "q1-root-problem:"
OWNER_RECEIPT_ID_PREFIX = "q1-common-root-owner:"
VALIDATION_ID_PREFIX = "q1-prefix-scope-validation:"
RECEIPT_ID_PREFIX = "q1-root-source-scoped-e1:"
MATH_REPLAY_ID = "q1_full_carrier_phase_root_math_replay_v1"

RAW_FIELDS = frozenset(
    {
        "schema_id",
        "schema_version",
        "root_context",
        "equation_rank",
        "equation_numerator",
        "equation_denominator",
        "q",
        "gap_three_x",
        "endpoint_fiber_code",
        "major_phase_code",
        "provenance_code",
        "mark_kind_code",
        "mark_root_context",
        "mark_equation_rank",
        "gap_three_factorization",
    }
)
SEMANTIC_FIELDS = (
    "root_context",
    "equation_rank",
    "equation_numerator",
    "equation_denominator",
    "q",
    "gap_three_x",
    "endpoint_fiber_code",
    "major_phase_code",
    "provenance_code",
    "mark_kind_code",
    "mark_root_context",
    "mark_equation_rank",
    "gap_three_factorization",
)
BODY_FIELDS = frozenset(
    {
        "artifact_type",
        "schema_version",
        *SEMANTIC_FIELDS,
        "source_tree_scope",
        "evidence_class",
        "initializer_authority",
        "admission_authority",
        "queue_authority",
        "body_id",
        "digest",
    }
)
ANCHOR_FIELDS = frozenset(
    {
        "artifact_type",
        "schema_version",
        "body_id",
        "body_digest",
        "initializer_id",
        "contract_digest",
        "root_origin_kind",
        "domain_replay_id",
        "domain_replay_digest",
        "evidence_class",
        "initializer_authority",
        "admission_authority",
        "queue_authority",
        "anchor_id",
        "digest",
    }
)
STATE_FIELDS = frozenset(
    {
        "artifact_type",
        "schema_version",
        "body_id",
        "body_digest",
        *SEMANTIC_FIELDS,
        "source_tree_scope",
        "root_origin",
        "evidence_class",
        "initializer_authority",
        "admission_authority",
        "queue_authority",
        "state_id",
        "digest",
    }
)
GRANT_FIELDS = frozenset(
    {
        "grant_id",
        "role",
        "artifact_id",
        "artifact_path",
        "artifact_symbols",
        "capabilities",
        "authority_class",
        "artifact_semantic_sha256",
    }
)

_DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")
_GIT_OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
_MAPPING_PROXY_TYPE = type(MappingProxyType({}))


class ConsumerRejectCode(str, Enum):
    INPUT_NOT_EXACT_MAPPING = "INPUT_NOT_EXACT_MAPPING"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    SOURCE_REPLAY_FAILED = "SOURCE_REPLAY_FAILED"
    ACTUALNESS_REPLAY_FAILED = "ACTUALNESS_REPLAY_FAILED"
    OWNER_REPLAY_FAILED = "OWNER_REPLAY_FAILED"
    TERMINAL_REPLAY_FAILED = "TERMINAL_REPLAY_FAILED"
    VALIDATION_REPLAY_FAILED = "VALIDATION_REPLAY_FAILED"
    PREFIX_REPLAY_FAILED = "PREFIX_REPLAY_FAILED"
    GRANT_MISMATCH = "GRANT_MISMATCH"
    AUTHORITY_BOUNDARY_VIOLATION = "AUTHORITY_BOUNDARY_VIOLATION"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    ID_MISMATCH = "ID_MISMATCH"
    TERMINAL_SOURCE_NOT_MISS = "TERMINAL_SOURCE_NOT_MISS"
    MATH_REPLAY_FAILED = "MATH_REPLAY_FAILED"


class ConsumerError(ValueError):
    def __init__(self, code: ConsumerRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: ConsumerRejectCode, detail: str) -> NoReturn:
    raise ConsumerError(code, detail)


def _json_copy(value: Any, *, path: str = "$") -> Any:
    if type(value) in {dict, _MAPPING_PROXY_TYPE}:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                _reject(ConsumerRejectCode.MALFORMED_FIELD, f"{path} has an invalid key")
            result[key] = _json_copy(child, path=f"{path}.{key}")
        return result
    if type(value) in {list, tuple}:
        return [_json_copy(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return value
    _reject(ConsumerRejectCode.MALFORMED_FIELD, f"{path} has an unsupported type")


def canonical_json_v2(value: Any) -> str:
    try:
        return json.dumps(
            _json_copy(value), ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False
        )
    except (TypeError, ValueError) as exc:
        raise ConsumerError(ConsumerRejectCode.MALFORMED_FIELD, str(exc)) from exc


def canonical_digest_v2(value: Any) -> str:
    return hashlib.sha256(canonical_json_v2(value).encode("ascii")).hexdigest()


def _exact_mapping(value: Any, expected: frozenset[str], name: str) -> dict[str, Any]:
    if type(value) not in {dict, _MAPPING_PROXY_TYPE}:
        _reject(ConsumerRejectCode.INPUT_NOT_EXACT_MAPPING, f"{name} must be an exact mapping")
    observed = frozenset(value)
    if observed != expected:
        _reject(
            ConsumerRejectCode.FIELD_SET_MISMATCH,
            f"{name} missing={sorted(expected-observed)} extra={sorted(observed-expected)}",
        )
    if any(type(key) is not str for key in value):
        _reject(ConsumerRejectCode.MALFORMED_FIELD, f"{name} keys must be strings")
    return dict(value)


def _plain_int(value: Any) -> bool:
    return type(value) is int


def _digest(value: Any, name: str) -> str:
    if type(value) is not str or _DIGEST_RE.fullmatch(value) is None:
        _reject(ConsumerRejectCode.MALFORMED_FIELD, f"{name} must be lowercase SHA-256")
    return value


def _content_id(value: Any, name: str, prefix: str) -> str:
    if type(value) is not str or not value.startswith(prefix) or _DIGEST_RE.fullmatch(value[len(prefix):]) is None:
        _reject(ConsumerRejectCode.MALFORMED_FIELD, f"{name} has invalid content-ID")
    return value


def _prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    if value % 3 == 0:
        return value == 3
    divisor, step = 5, 2
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += step
        step = 6 - step
    return True


def _factor(value: int) -> list[list[int]]:
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


def _raw(value: Any) -> dict[str, Any]:
    raw = _exact_mapping(value, RAW_FIELDS, "raw_q_one_g")
    if raw["schema_id"] != RAW_SCHEMA_ID or raw["schema_version"] != RAW_SCHEMA_VERSION:
        _reject(ConsumerRejectCode.SOURCE_REPLAY_FAILED, "raw schema mismatch")
    for name in RAW_FIELDS - {"schema_id", "gap_three_factorization"}:
        if not _plain_int(raw[name]):
            _reject(ConsumerRejectCode.MALFORMED_FIELD, f"raw.{name} must be a plain integer")
    p = raw["root_context"]
    x = (p + 3) // 4
    if not (
        _prime(p) and p % 24 == 1 and raw["equation_rank"] == p and raw["equation_numerator"] == 4
        and raw["equation_denominator"] == p and raw["q"] == 1 and raw["gap_three_x"] == x
        and raw["endpoint_fiber_code"] == 2 and raw["major_phase_code"] == 3 and raw["provenance_code"] == 1
        and raw["mark_kind_code"] == 1 and raw["mark_root_context"] == p and raw["mark_equation_rank"] == p
        and type(raw["gap_three_factorization"]) is list and raw["gap_three_factorization"] == _factor(x)
        and all(prime % 3 == 1 for prime, _exponent in raw["gap_three_factorization"])
    ):
        _reject(ConsumerRejectCode.SOURCE_REPLAY_FAILED, "raw is not ordinary q=1 G")
    return _json_copy(raw)


def _sealed(value: Any, expected: frozenset[str], name: str, kind: str, id_field: str, prefix: str) -> dict[str, Any]:
    item = _exact_mapping(value, expected, name)
    if item["artifact_type"] != kind or item["schema_version"] != 2:
        _reject(ConsumerRejectCode.SOURCE_REPLAY_FAILED, f"{name} type/schema mismatch")
    digest = _digest(item["digest"], f"{name}.digest")
    content_id = _content_id(item[id_field], f"{name}.{id_field}", prefix)
    unsigned = _json_copy(item)
    unsigned.pop(id_field)
    unsigned.pop("digest")
    if canonical_digest_v2(unsigned) != digest or content_id != prefix + digest:
        _reject(ConsumerRejectCode.DIGEST_MISMATCH, f"{name} seal mismatch")
    return _json_copy(item)


def _source_chain(raw_value: Any, body_value: Any, anchor_value: Any, state_value: Any) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    raw = _raw(raw_value)
    body = _sealed(body_value, BODY_FIELDS, "source_body", "CanonicalQOneGSourceBodyV2", "body_id", BODY_ID_PREFIX)
    expected_body = {
        "artifact_type": "CanonicalQOneGSourceBodyV2", "schema_version": 2,
        **{name: raw[name] for name in SEMANTIC_FIELDS}, "source_tree_scope": SOURCE_TREE_SCOPE,
        "evidence_class": EVIDENCE_CLASS, "initializer_authority": False,
        "admission_authority": False, "queue_authority": False,
    }
    body_digest = canonical_digest_v2(expected_body)
    expected_body.update({"body_id": BODY_ID_PREFIX + body_digest, "digest": body_digest})
    if body != expected_body:
        _reject(ConsumerRejectCode.SOURCE_REPLAY_FAILED, "body does not replay")
    anchor = _sealed(anchor_value, ANCHOR_FIELDS, "root_anchor", "RootInitializerAnchorV2", "anchor_id", ANCHOR_ID_PREFIX)
    domain_digest = canonical_digest_v2({
        "domain_replay_id": DOMAIN_REPLAY_ID, "source_body_id": body["body_id"], "source_body_digest": body["digest"],
        "result": "ORDINARY_Q_ONE_G_RAW_INTEGER_REPLAY", "initializer_authority": False,
        "admission_authority": False, "queue_authority": False,
    })
    contract_digest = canonical_digest_v2({
        "contract_id": INITIALIZER_ID, "schema_version": 2, "raw_schema_id": RAW_SCHEMA_ID,
        "dependency_order": ["CanonicalQOneGSourceBodyV2", "RootInitializerAnchorV2", "RawRootSourceStateV2"],
        "root_origin_kind": ROOT_ORIGIN_KIND, "domain_replay_id": DOMAIN_REPLAY_ID,
        "source_tree_scope": SOURCE_TREE_SCOPE, "evidence_class": EVIDENCE_CLASS,
        "initializer_authority": False, "admission_authority": False, "queue_authority": False,
    })
    expected_anchor = {
        "artifact_type": "RootInitializerAnchorV2", "schema_version": 2, "body_id": body["body_id"],
        "body_digest": body["digest"], "initializer_id": INITIALIZER_ID, "contract_digest": contract_digest,
        "root_origin_kind": ROOT_ORIGIN_KIND, "domain_replay_id": DOMAIN_REPLAY_ID,
        "domain_replay_digest": domain_digest, "evidence_class": EVIDENCE_CLASS,
        "initializer_authority": False, "admission_authority": False, "queue_authority": False,
    }
    anchor_digest = canonical_digest_v2(expected_anchor)
    expected_anchor.update({"anchor_id": ANCHOR_ID_PREFIX + anchor_digest, "digest": anchor_digest})
    if anchor != expected_anchor:
        _reject(ConsumerRejectCode.SOURCE_REPLAY_FAILED, "anchor does not replay")
    state = _sealed(state_value, STATE_FIELDS, "source_state", "RawRootSourceStateV2", "state_id", STATE_ID_PREFIX)
    expected_state = {
        "artifact_type": "RawRootSourceStateV2", "schema_version": 2, "body_id": body["body_id"],
        "body_digest": body["digest"], **{name: raw[name] for name in SEMANTIC_FIELDS},
        "source_tree_scope": SOURCE_TREE_SCOPE, "root_origin": {"root_initializer_anchor_id": anchor["anchor_id"], "digest": anchor["digest"]},
        "evidence_class": EVIDENCE_CLASS, "initializer_authority": False,
        "admission_authority": False, "queue_authority": False,
    }
    state_digest = canonical_digest_v2(expected_state)
    expected_state.update({"state_id": STATE_ID_PREFIX + state_digest, "digest": state_digest})
    if state != expected_state:
        _reject(ConsumerRejectCode.SOURCE_REPLAY_FAILED, "state does not replay")
    return raw, body, anchor, state


def _actualness(value: Any, *, raw: Mapping[str, Any], body: Mapping[str, Any], anchor: Mapping[str, Any], state: Mapping[str, Any]) -> dict[str, Any]:
    expected_fields = frozenset({
        "receipt_type", "schema_version", "head_sha", "head_tree_sha", "v3_registry_id", "v3_registry_digest", "v3_role_manifest_digest",
        "initializer_grant_id", "initializer_grant_digest", "initializer_artifact_id", "initializer_artifact_semantic_sha256", "issuer_grant_id",
        "issuer_grant_digest", "issuer_artifact_id", "issuer_artifact_semantic_sha256", "fresh_module_binding_digest", "root_problem", "root_problem_id",
        "root_problem_digest", "raw_q_one_g", "raw_q_one_g_digest", "deterministic_initial_branch_replay", "deterministic_initial_branch_replay_digest",
        "body_id", "body_digest", "anchor_id", "anchor_digest", "state_id", "state_digest", "initializer_id", "initializer_contract_digest",
        "domain_replay_id", "domain_replay_digest", "owner_domain_id", "occurrence_kind", "parent_kind", "actualness_scope",
        "initializer_output_self_authorizing", "actualness_attestor_role", "source_actualness", "root_initializer_authority",
        "terminal_issuer_attestation_authority", "persistent_admission", "common_owner_authority", "e1_authority", "queue_authority", "actualness_id", "digest",
    })
    actual = _exact_mapping(value, expected_fields, "root_actualness")
    if actual["receipt_type"] != "QOneRootSourceActualnessReceiptV1" or actual["schema_version"] != 1:
        _reject(ConsumerRejectCode.ACTUALNESS_REPLAY_FAILED, "actualness type/schema mismatch")
    if any(type(actual[name]) is not str or _GIT_OID_RE.fullmatch(actual[name]) is None for name in ("head_sha", "head_tree_sha")):
        _reject(ConsumerRejectCode.ACTUALNESS_REPLAY_FAILED, "actualness HEAD malformed")
    for name in (
        "v3_registry_digest", "v3_role_manifest_digest", "initializer_grant_digest", "initializer_artifact_semantic_sha256", "issuer_grant_digest",
        "issuer_artifact_semantic_sha256", "fresh_module_binding_digest", "root_problem_digest", "raw_q_one_g_digest", "deterministic_initial_branch_replay_digest",
        "body_digest", "anchor_digest", "state_digest", "initializer_contract_digest", "domain_replay_digest", "digest",
    ):
        _digest(actual[name], f"actualness.{name}")
    unsigned = _json_copy(actual)
    actualness_id = unsigned.pop("actualness_id")
    digest = unsigned.pop("digest")
    if canonical_digest_v2(unsigned) != digest or actualness_id != ACTUALNESS_ID_PREFIX + digest:
        _reject(ConsumerRejectCode.DIGEST_MISMATCH, "actualness seal mismatch")
    p = raw["root_context"]
    root_problem = {"schema_id": "q1_canonical_root_problem_v1", "root_context": p, "equation_rank": p, "equation_numerator": 4, "equation_denominator": p, "mark_kind_code": 1, "mark_root_context": p, "mark_equation_rank": p}
    root_digest = canonical_digest_v2(root_problem)
    raw_digest = canonical_digest_v2(raw)
    branch = {
        "schema_id": "q1_deterministic_initial_g_branch_replay_v1", "root_problem_id": ROOT_PROBLEM_ID_PREFIX + root_digest,
        "root_problem_digest": root_digest, "raw_q_one_g_digest": raw_digest, "q": 1, "endpoint_fiber_code": 2,
        "major_phase_code": 3, "provenance_code": 1, "mark_kind_code": 1, "gap_three_x": raw["gap_three_x"],
        "gap_three_factorization": raw["gap_three_factorization"], "body_id": body["body_id"], "body_digest": body["digest"],
        "anchor_id": anchor["anchor_id"], "anchor_digest": anchor["digest"], "state_id": state["state_id"], "state_digest": state["digest"],
        "state_authority": {"initializer_authority": False, "persistent_admission": False, "queue_authority": False},
    }
    expected = {
        "v3_registry_id": "t6_coordinator_role_registry_v3", "initializer_grant_id": "q1_root_initializer_grant_v3", "initializer_artifact_id": "q1_root_initializer_envelope_v2",
        "issuer_grant_id": "q1_terminal_issuer_grant_v3", "issuer_artifact_id": "q1_terminal_issuer_v1", "root_problem": root_problem,
        "root_problem_id": ROOT_PROBLEM_ID_PREFIX + root_digest, "root_problem_digest": root_digest, "raw_q_one_g": raw, "raw_q_one_g_digest": raw_digest,
        "deterministic_initial_branch_replay": branch, "deterministic_initial_branch_replay_digest": canonical_digest_v2(branch), "body_id": body["body_id"],
        "body_digest": body["digest"], "anchor_id": anchor["anchor_id"], "anchor_digest": anchor["digest"], "state_id": state["state_id"], "state_digest": state["digest"],
        "initializer_id": INITIALIZER_ID, "initializer_contract_digest": anchor["contract_digest"], "domain_replay_id": DOMAIN_REPLAY_ID, "domain_replay_digest": anchor["domain_replay_digest"],
        "owner_domain_id": OWNER_DOMAIN_ID, "occurrence_kind": "ROOT_INITIALIZER_OUTPUT", "parent_kind": "PARENTLESS_ROOT", "actualness_scope": "ROOT_OCCURRENCE_ONLY",
        "initializer_output_self_authorizing": False, "actualness_attestor_role": "TERMINAL_ISSUER", "source_actualness": True, "root_initializer_authority": True,
        "terminal_issuer_attestation_authority": True, "persistent_admission": False, "common_owner_authority": False, "e1_authority": False, "queue_authority": False,
    }
    for name, expected_value in expected.items():
        if _json_copy(actual[name]) != _json_copy(expected_value):
            _reject(ConsumerRejectCode.ACTUALNESS_REPLAY_FAILED, f"actualness.{name} does not replay")
    return actual


def _grant(value: Any) -> tuple[dict[str, Any], str]:
    grant = _exact_mapping(value, GRANT_FIELDS, "role_grant")
    expected = {"grant_id": GRANT_ID, "role": ROLE, "artifact_id": ARTIFACT_ID, "artifact_path": ARTIFACT_PATH, "artifact_symbols": list(ARTIFACT_SYMBOLS), "capabilities": list(CAPABILITIES), "authority_class": AUTHORITY_CLASS}
    for name, expected_value in expected.items():
        if grant[name] != expected_value or type(grant[name]) is not type(expected_value):
            _reject(ConsumerRejectCode.GRANT_MISMATCH, f"role_grant.{name} mismatch")
    _digest(grant["artifact_semantic_sha256"], "role_grant.artifact_semantic_sha256")
    plain = _json_copy(grant)
    return plain, canonical_digest_v2(plain)


def _header(state: Mapping[str, Any]) -> dict[str, Any]:
    return {"state_id": state["state_id"], "state_digest": state["digest"], "root_context": state["root_context"], "equation_rank": state["equation_rank"], "mark_kind": "ROOT_SOL", "mark_root_context": state["mark_root_context"], "mark_equation_rank": state["mark_equation_rank"], "facts": {"major_phase": "TYPEII_G_HANDOFF", "type_i_protocol": None, "t5_eta_p": 0, "pre_a": None, "absorb_m": None, "absorb_r_epsilon": 0, "reset_carrier": None, "provenance_kind": "ORDINARY_ENDPOINT", "endpoint_fiber": "G", "relation_q": 1, "support_A": None, "proper_root_k": None, "proper_root_height_class": "NONE", "proper_root_height": None, "proper_root_r": None, "is_overflow": False, "overflow_d": None, "chart_R": None, "chart_K": None, "carrier_M": None, "sink_scc_receipt": False, "same_chart_promotion_receipt": False, "full_carrier_scope": False, "atomic_arm": "NONE", "dispatch_status": "NONE"}}


def _predicates(header: Mapping[str, Any]) -> dict[str, bool]:
    f = header["facts"]
    ordinary = header["mark_kind"] == "ROOT_SOL"
    p = header["root_context"]
    results = {
        "generic_nontrivial_marked_state": header["mark_kind"] == "NONTRIVIAL_MARK" and f["major_phase"] == "GENERIC_MARKED" and f["provenance_kind"] == "GENERIC_MARKED",
        "type_ii_relation_f_endpoint": ordinary and f["major_phase"] == "TYPEII_REL" and f["endpoint_fiber"] == "F",
        "type_ii_relation_g_endpoint": ordinary and f["major_phase"] == "TYPEII_G_HANDOFF" and f["endpoint_fiber"] == "G",
        "h4_non_v1_branch_or_descendant": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["provenance_kind"] == "H4_RESIDUAL",
        "c8_terminal_first_surviving_parent": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["provenance_kind"] == "C8_PARENT",
        "type_i_c2_19_macro_target": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["provenance_kind"] == "C2_19_MACRO",
        "proper_root_high_endpoint": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["provenance_kind"] == "PROPER_ROOT" and f["proper_root_height_class"] == "HIGH",
        "proper_root_stutter_k_one": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["provenance_kind"] == "PROPER_ROOT" and f["proper_root_height_class"] == "LOW" and f["proper_root_k"] == 1,
        "proper_root_stutter_k_gt_one": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["provenance_kind"] == "PROPER_ROOT" and f["proper_root_height_class"] == "LOW" and _plain_int(f["proper_root_k"]) and f["proper_root_k"] > 1,
        "type_i_absorb_marked_residual": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "ABSORB" and f["provenance_kind"] == "MARKED_ABSORB" and not f["is_overflow"] and _plain_int(f["chart_R"]) and f["chart_R"] < p,
        "type_i_a_one_overflow": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["is_overflow"] and f["support_A"] == 1 and _plain_int(f["overflow_d"]) and 1 <= f["overflow_d"] < p,
        "type_i_high_support_sink": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["is_overflow"] and _plain_int(f["support_A"]) and f["support_A"] > (p - 1) ** 2 // 4 and f["sink_scc_receipt"],
        "type_i_low_support_persistent_overflow": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["is_overflow"] and f["same_chart_promotion_receipt"] and _plain_int(f["support_A"]) and _plain_int(f["carrier_M"]) and f["carrier_M"] % f["support_A"] == 0 and f["carrier_M"] // f["support_A"] >= 2,
        "type_i_a_gt_one_overflow_residual": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["is_overflow"] and _plain_int(f["support_A"]) and f["support_A"] > 1,
        "type_i_full_carrier_post_g": ordinary and f["major_phase"] == "TYPEI" and f["type_i_protocol"] == "CHARGED" and f["provenance_kind"] == "FULL_CARRIER_POST_G" and f["full_carrier_scope"],
    }
    if tuple(results) != FAMILY_PRECEDENCE:
        _reject(ConsumerRejectCode.OWNER_REPLAY_FAILED, "family precedence changed")
    return results


FAMILY_PRECEDENCE = (
    "generic_nontrivial_marked_state", "type_ii_relation_f_endpoint", "type_ii_relation_g_endpoint", "h4_non_v1_branch_or_descendant", "c8_terminal_first_surviving_parent", "type_i_c2_19_macro_target", "proper_root_high_endpoint", "proper_root_stutter_k_one", "proper_root_stutter_k_gt_one", "type_i_absorb_marked_residual", "type_i_a_one_overflow", "type_i_high_support_sink", "type_i_low_support_persistent_overflow", "type_i_a_gt_one_overflow_residual", "type_i_full_carrier_post_g"
)


def _owner(value: Any, *, raw: Mapping[str, Any], body: Mapping[str, Any], anchor: Mapping[str, Any], state: Mapping[str, Any], actual: Mapping[str, Any]) -> dict[str, Any]:
    owner = _exact_mapping(value, OWNER_FIELDS, "owner_receipt")
    if owner["receipt_type"] != OWNER_RECEIPT_TYPE or owner["schema_version"] != 2 or owner["status"] != "COMMON_OWNER_CLASSIFIED":
        _reject(ConsumerRejectCode.OWNER_REPLAY_FAILED, "owner receipt identity changed")
    unsigned = _json_copy(owner)
    rid = unsigned.pop("receipt_id")
    digest = unsigned.pop("digest")
    _digest(digest, "owner_receipt.digest")
    if rid != OWNER_RECEIPT_ID_PREFIX + digest or canonical_digest_v2(unsigned) != digest:
        _reject(ConsumerRejectCode.DIGEST_MISMATCH, "owner receipt seal mismatch")
    if owner["role"] != "COMMON_ROOT_OWNER_CLASSIFIER" or owner["role_grant_id"] != "q1_common_root_owner_classifier_grant_v4" or owner["owner_scope"] != "ROOT_SOURCE_DISPATCH_ONLY":
        _reject(ConsumerRejectCode.OWNER_REPLAY_FAILED, "owner role/scope changed")
    if (_json_copy(owner["raw_q_one_g"]) != _json_copy(raw) or _json_copy(owner["source_body"]) != _json_copy(body) or _json_copy(owner["root_anchor"]) != _json_copy(anchor) or _json_copy(owner["source_state"]) != _json_copy(state) or _json_copy(owner["root_actualness"]) != _json_copy(actual)):
        _reject(ConsumerRejectCode.OWNER_REPLAY_FAILED, "owner source chain differs")
    header = _header(state)
    results = _predicates(header)
    if (_json_copy(owner["normalized_header"]) != header or _json_copy(owner["predicate_results"]) != results or tuple(owner["family_precedence"]) != FAMILY_PRECEDENCE or tuple(owner["matched_families"]) != (OWNER,) or owner["owner"] != OWNER or owner["precedence_index"] != 2):
        _reject(ConsumerRejectCode.OWNER_REPLAY_FAILED, "owner predicates do not replay")
    if owner["normalized_header_digest"] != canonical_digest_v2(header) or owner["facts_digest"] != canonical_digest_v2(header["facts"]) or owner["predicate_results_digest"] != canonical_digest_v2(results):
        _reject(ConsumerRejectCode.OWNER_REPLAY_FAILED, "owner predicate digests do not replay")
    expected_owner_digest = canonical_digest_v2({"contract_id": "t6_persistent_selector_state_v1", "schema_version": 1, "state_id": state["state_id"], "facts_digest": canonical_digest_v2(header["facts"]), "owner": OWNER, "matched_families": [OWNER], "precedence_index": 2})
    if owner["owner_contract_id"] != "t6_persistent_selector_state_v1" or owner["owner_contract_schema_version"] != 1 or owner["owner_id"] != "owner:" + expected_owner_digest or owner["owner_digest"] != expected_owner_digest:
        _reject(ConsumerRejectCode.OWNER_REPLAY_FAILED, "owner digest does not replay")
    for name in ("source_actualness", "common_owner_authority"):
        if owner[name] is not True or type(owner[name]) is not bool:
            _reject(ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, f"owner.{name} must be true")
    for name in ("terminal_receipt_dependency", "terminal_schedule_dependency", "registered_prefix_miss_authority", "scope_validation_authority", "root_source_scoped_e1", "scope_aware_consumer_authority", "root_source_occurrence_authority", "terminal_receipt_direct_continuation_authority", "e1_authority", "generic_e1", "successor_e1", "producer_authority", "producer_continuation_allowed", "persistent_admission", "queue_authority", "e2_authority", "e3_authority", "e4_authority", "e5_authority", "global_exhaustion", "terminal_leaf_authority", "root_proof_close_authority"):
        if owner[name] is not False or type(owner[name]) is not bool:
            _reject(ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, f"owner.{name} must be false")
    return owner


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
        y, z, rank = (p * x + divisor) // gap, p * (x + p * quotient) // gap, 2 * index
    else:
        if divisor > x or (x + divisor) % gap or p * (x + divisor) % gap or p * (x + quotient) % gap:
            return None
        y, z, rank = p * (x + divisor) // gap, p * (x + quotient) // gap, 2 * index + 1
    if 4 * x * y * z != p * (x * y + x * z + y * z):
        return None
    return {"certificate_type": kind, "gap": gap, "x": x, "divisor": divisor, "y": y, "z": z, "candidate_index": rank}


def _scan(p: int, gap: int) -> dict[str, Any]:
    x = (p + gap) // 4
    factors = _factor(x)
    divisors = _divisors(factors)
    matches: list[dict[str, Any]] = []
    for index, divisor in enumerate(divisors):
        for kind in ("TYPE_I", "TYPE_II"):
            certificate = _certificate(p, gap, x, divisor, index, kind)
            if certificate is not None:
                matches.append(certificate)
    unsigned = {"gap": gap, "x": x, "factorization": factors, "divisor_universe": divisors, "matching_certificates": matches, "scan_status": "GAP_HAS_TERMINAL" if matches else "GAP_PREFIX_MISS"}
    return {**unsigned, "scan_digest": canonical_digest_v2(unsigned)}


def _production(value: Any, *, raw: Mapping[str, Any], body: Mapping[str, Any], anchor: Mapping[str, Any], state: Mapping[str, Any], actual: Mapping[str, Any]) -> dict[str, Any]:
    if type(value) not in {dict, _MAPPING_PROXY_TYPE}:
        _reject(ConsumerRejectCode.INPUT_NOT_EXACT_MAPPING, "production receipt must be a mapping")
    if value.get("receipt_type") != PRODUCTION_MISS_TYPE:
        _reject(ConsumerRejectCode.TERMINAL_SOURCE_NOT_MISS, "only a registered-prefix MISS can feed this consumer")
    fields_expected = frozenset({
        "receipt_type", "schema_version", "head_sha", "head_tree_sha", "v2_registry_id", "v2_registry_digest", "v2_role_manifest_digest", "v3_registry_id", "v3_registry_digest", "v3_role_manifest_digest", "cross_registry_equivalence_digest", "initializer_grant_id", "initializer_grant_digest", "initializer_artifact_semantic_sha256", "issuer_grant_id", "issuer_grant_digest", "issuer_artifact_semantic_sha256", "scheduler_grant_id", "scheduler_grant_digest", "scheduler_artifact_semantic_sha256", "coverage_verifier_grant_id", "coverage_verifier_grant_digest", "coverage_verifier_artifact_semantic_sha256", "fresh_module_binding_digest", "root_actualness", "root_actualness_digest", "root_problem_id", "root_problem_digest", "raw_q_one_g_digest", "deterministic_initial_branch_replay_digest", "body_id", "body_digest", "anchor_id", "anchor_digest", "state_id", "state_digest", "subject_kind", "root_context", "assembler_artifact_id", "assembler_artifact_semantic_sha256", "assembler_module_binding_digest", "assembler_decision_id", "assembler_decision_digest", "assembler_evidence_digest", "assembler_coverage_replay_digest", "schedule_id", "schedule_digest", "source_actualness", "root_initializer_authority", "issuer_authority", "issued_under_terminal_issuer", "persistent_admission", "common_owner_authority", "e1_authority", "queue_authority", "producer_continuation_allowed", "receipt_id", "digest", "outcome", "coverage_semantics", "ordered_gaps", "next_unchecked_gap", "global_exhaustion", "selected_certificate", "selected_certificate_digest", "terminal_leaf_authority", "registered_prefix_miss_authority", "root_proof_close_authority",
    })
    receipt = _exact_mapping(value, fields_expected, "production_receipt")
    unsigned = _json_copy(receipt)
    rid = unsigned.pop("receipt_id")
    digest = unsigned.pop("digest")
    _digest(digest, "production_receipt.digest")
    if rid != "production-q1-prefix-miss:" + digest or canonical_digest_v2(unsigned) != digest:
        _reject(ConsumerRejectCode.DIGEST_MISMATCH, "production receipt seal mismatch")
    for name in ("head_sha", "head_tree_sha"):
        if type(receipt[name]) is not str or _GIT_OID_RE.fullmatch(receipt[name]) is None:
            _reject(ConsumerRejectCode.TERMINAL_REPLAY_FAILED, f"production.{name} malformed")
    for name in ("v2_registry_digest", "v2_role_manifest_digest", "v3_registry_digest", "v3_role_manifest_digest", "cross_registry_equivalence_digest", "initializer_grant_digest", "initializer_artifact_semantic_sha256", "issuer_grant_digest", "issuer_artifact_semantic_sha256", "scheduler_grant_digest", "scheduler_artifact_semantic_sha256", "coverage_verifier_grant_digest", "coverage_verifier_artifact_semantic_sha256", "fresh_module_binding_digest", "root_actualness_digest", "root_problem_digest", "raw_q_one_g_digest", "deterministic_initial_branch_replay_digest", "body_digest", "anchor_digest", "state_digest", "assembler_artifact_semantic_sha256", "assembler_module_binding_digest", "assembler_decision_digest", "assembler_evidence_digest", "assembler_coverage_replay_digest", "schedule_digest"):
        _digest(receipt[name], f"production.{name}")
    if not (receipt["v3_registry_id"] == "t6_coordinator_role_registry_v3" and receipt["subject_kind"] == "SOURCE_STATE" and receipt["root_context"] == raw["root_context"] and receipt["root_problem_id"] == actual["root_problem_id"] and receipt["root_problem_digest"] == actual["root_problem_digest"] and receipt["root_actualness_digest"] == actual["digest"] and _json_copy(receipt["root_actualness"]) == _json_copy(actual) and receipt["raw_q_one_g_digest"] == canonical_digest_v2(raw) and receipt["body_id"] == body["body_id"] and receipt["body_digest"] == body["digest"] and receipt["anchor_id"] == anchor["anchor_id"] and receipt["anchor_digest"] == anchor["digest"] and receipt["state_id"] == state["state_id"] and receipt["state_digest"] == state["digest"]):
        _reject(ConsumerRejectCode.TERMINAL_REPLAY_FAILED, "production source chain differs")
    for name in ("source_actualness", "root_initializer_authority", "issuer_authority", "issued_under_terminal_issuer"):
        if receipt[name] is not True or type(receipt[name]) is not bool:
            _reject(ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, f"production.{name} must be true")
    for name in ("persistent_admission", "common_owner_authority", "e1_authority", "queue_authority", "producer_continuation_allowed"):
        if receipt[name] is not False or type(receipt[name]) is not bool:
            _reject(ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, f"production.{name} must be false")
    if not (receipt["outcome"] == MISS_OUTCOME and receipt["coverage_semantics"] == COVERAGE_SEMANTICS and receipt["ordered_gaps"] == list(ORDERED_GAPS) and receipt["next_unchecked_gap"] == NEXT_UNCHECKED_GAP and receipt["global_exhaustion"] is False and receipt["selected_certificate"] is None and receipt["selected_certificate_digest"] is None and receipt["terminal_leaf_authority"] is False and receipt["registered_prefix_miss_authority"] is True and receipt["root_proof_close_authority"] is False):
        _reject(ConsumerRejectCode.TERMINAL_REPLAY_FAILED, "production MISS scope changed")
    return receipt


def _validation(value: Any, *, raw: Mapping[str, Any], body: Mapping[str, Any], anchor: Mapping[str, Any], state: Mapping[str, Any], actual: Mapping[str, Any], owner: Mapping[str, Any], terminal: Mapping[str, Any]) -> dict[str, Any]:
    # The validator receipt is self-contained; its seal and the mathematical
    # scans are replayed here rather than trusted as a caller assertion.
    expected = frozenset({
        "receipt_type", "schema_version", "status", "role", "role_grant", "role_grant_id", "role_grant_digest", "role_artifact_id", "role_artifact_semantic_sha256", "raw_q_one_g", "raw_q_one_g_digest", "source_body", "body_id", "body_digest", "root_anchor", "anchor_id", "anchor_digest", "source_state", "state_id", "state_digest", "root_actualness", "root_actualness_id", "root_actualness_digest", "owner_receipt", "owner_receipt_id", "owner_receipt_digest", "terminal_receipt", "terminal_receipt_id", "terminal_receipt_digest", "scope_id", "coverage_semantics", "ordered_gaps", "next_unchecked_gap", "candidate_order", "registered_gap_scans", "outside_scope_gap_scans", "registered_prefix_replay_digest", "outside_scope_control_digest", "global_exhaustion", "source_actualness", "common_owner_authority", "registered_prefix_miss_authority", "scope_validation_authority", "root_source_scoped_e1", "scope_aware_consumer_authority", "root_source_occurrence_authority", "terminal_receipt_direct_continuation_authority", "e1_authority", "generic_e1", "successor_e1", "producer_authority", "producer_continuation_allowed", "persistent_admission", "queue_authority", "e2_authority", "e3_authority", "e4_authority", "e5_authority", "terminal_leaf_authority", "root_proof_close_authority", "receipt_id", "digest",
    })
    validation = _exact_mapping(value, expected, "scope_validation_receipt")
    unsigned = _json_copy(validation)
    rid = unsigned.pop("receipt_id")
    digest = unsigned.pop("digest")
    _digest(digest, "scope_validation_receipt.digest")
    if rid != VALIDATION_ID_PREFIX + digest or canonical_digest_v2(unsigned) != digest:
        _reject(ConsumerRejectCode.DIGEST_MISMATCH, "scope validation seal mismatch")
    if not (validation["receipt_type"] == VALIDATION_RECEIPT_TYPE and validation["schema_version"] == 2 and validation["status"] == VALIDATION_STATUS and validation["scope_id"] == SCOPE_ID and validation["coverage_semantics"] == COVERAGE_SEMANTICS and validation["ordered_gaps"] == list(ORDERED_GAPS) and validation["next_unchecked_gap"] == NEXT_UNCHECKED_GAP and validation["candidate_order"] == CANDIDATE_ORDER and validation["global_exhaustion"] is False):
        _reject(ConsumerRejectCode.VALIDATION_REPLAY_FAILED, "scope validation identity changed")
    if (_json_copy(validation["raw_q_one_g"]) != _json_copy(raw) or _json_copy(validation["source_body"]) != _json_copy(body) or _json_copy(validation["root_anchor"]) != _json_copy(anchor) or _json_copy(validation["source_state"]) != _json_copy(state) or _json_copy(validation["root_actualness"]) != _json_copy(actual) or _json_copy(validation["owner_receipt"]) != _json_copy(owner) or _json_copy(validation["terminal_receipt"]) != _json_copy(terminal)):
        _reject(ConsumerRejectCode.VALIDATION_REPLAY_FAILED, "scope validation source references differ")
    expected_registered = tuple(_scan(raw["root_context"], gap) for gap in ORDERED_GAPS)
    expected_outside = tuple(_scan(raw["root_context"], gap) for gap in OUTSIDE_CONTROL_GAPS)
    if tuple(_json_copy(scan) for scan in validation["registered_gap_scans"]) != expected_registered or tuple(_json_copy(scan) for scan in validation["outside_scope_gap_scans"]) != expected_outside or any(scan["matching_certificates"] for scan in expected_registered):
        _reject(ConsumerRejectCode.PREFIX_REPLAY_FAILED, "scope validation scans do not replay")
    registered_unsigned = {"scope_id": SCOPE_ID, "root_context": raw["root_context"], "ordered_gaps": list(ORDERED_GAPS), "scans": list(expected_registered), "global_exhaustion": False, "next_unchecked_gap": NEXT_UNCHECKED_GAP}
    outside_unsigned = {"scope_id": SCOPE_ID, "root_context": raw["root_context"], "gaps": list(OUTSIDE_CONTROL_GAPS), "scans": list(expected_outside), "outside_registered_scope": True}
    if validation["registered_prefix_replay_digest"] != canonical_digest_v2(registered_unsigned) or validation["outside_scope_control_digest"] != canonical_digest_v2(outside_unsigned):
        _reject(ConsumerRejectCode.PREFIX_REPLAY_FAILED, "scope validation scan digests do not replay")
    if validation["owner_receipt_id"] != owner["receipt_id"] or validation["owner_receipt_digest"] != owner["digest"] or validation["terminal_receipt_id"] != terminal["receipt_id"] or validation["terminal_receipt_digest"] != terminal["digest"]:
        _reject(ConsumerRejectCode.VALIDATION_REPLAY_FAILED, "scope validation receipt bindings differ")
    for name in ("source_actualness", "registered_prefix_miss_authority", "scope_validation_authority"):
        if validation[name] is not True or type(validation[name]) is not bool:
            _reject(ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, f"validation.{name} must be true")
    for name in ("common_owner_authority", "root_source_scoped_e1", "scope_aware_consumer_authority", "root_source_occurrence_authority", "terminal_receipt_direct_continuation_authority", "e1_authority", "generic_e1", "successor_e1", "producer_authority", "producer_continuation_allowed", "persistent_admission", "queue_authority", "e2_authority", "e3_authority", "e4_authority", "e5_authority", "terminal_leaf_authority", "root_proof_close_authority"):
        if validation[name] is not False or type(validation[name]) is not bool:
            _reject(ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, f"validation.{name} must be false")
    return validation


def _phase_root_math(p: int) -> dict[str, Any]:
    t = (p - 1) // 24
    x = (p + 3) // 4
    r = 16 * t + 3
    k = x * (16 * t + 1)
    source = (p, r * (p - 1) - p, p - 1)
    target = (1, r - 1, 1)
    if not (x == 6 * t + 1 and 4 * k == p * r + 1 and gcd(x, k) == x and 3 <= r <= p - 2):
        _reject(ConsumerRejectCode.MATH_REPLAY_FAILED, "full-carrier chart identity failed")
    if not (source[0] > 0 and source[1] > 0 and source[2] > 0 and source[0] + source[1] == r * source[2] and gcd(source[0], source[1]) == 1 and k % p != 0 and source[0] % p == 0 and (source[1] + r) % p == 0 and (source[2] + 1) % p == 0 and (source[0] // p, (source[1] + r) // p, (source[2] + 1) // p) == target):
        _reject(ConsumerRejectCode.MATH_REPLAY_FAILED, "fresh p-source identity failed")
    if not (target[0] + target[1] == r * target[2] and gcd(target[0], target[1]) == 1):
        _reject(ConsumerRejectCode.MATH_REPLAY_FAILED, "target chart identity failed")
    payload = {"math_replay_id": MATH_REPLAY_ID, "root_context": p, "t": t, "x": x, "chart_r": r, "chart_k": k, "support_a": 1, "fresh_source": list(source), "target_anchor": list(target), "edge_prime": p, "edge_shift": 1, "gcd_reduction": 1, "source_phase": "TYPEII_G_HANDOFF", "target_phase": "TYPEI", "target_protocol": "CHARGED", "target_provenance": "FULL_CARRIER_POST_G", "mark_kind": "ROOT_SOL", "ticket": "PHASE_DROP_EVIDENCE_ONLY", "admission_ticket_issued": False}
    return {**payload, "digest": canonical_digest_v2(payload)}


@dataclass(frozen=True, init=False, slots=True)
class QOneRegisteredPrefixE1ReceiptV2:
    ARTIFACT_TYPE: ClassVar[str] = RECEIPT_TYPE
    ID_PREFIX: ClassVar[str] = RECEIPT_ID_PREFIX
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
    state_id: str
    state_digest: str
    root_actualness: Mapping[str, Any]
    root_actualness_id: str
    root_actualness_digest: str
    owner_receipt: Mapping[str, Any]
    owner_receipt_id: str
    owner_receipt_digest: str
    terminal_receipt: Mapping[str, Any]
    terminal_receipt_id: str
    terminal_receipt_digest: str
    scope_validation_receipt: Mapping[str, Any]
    scope_validation_receipt_id: str
    scope_validation_receipt_digest: str
    scope_id: str
    coverage_semantics: str
    ordered_gaps: tuple[int, int, int]
    next_unchecked_gap: int
    global_exhaustion: bool
    terminal_receipt_direct_continuation_authority: bool
    scope_aware_consumer_authority: bool
    root_source_occurrence_authority: bool
    candidate_witness: Mapping[str, Any]
    candidate_witness_digest: str
    math_replay_id: str
    math_replay: Mapping[str, Any]
    math_replay_digest: str
    parent_kind: str
    occurrence_path: tuple[Any, ...]
    occurrence_value_digest: str
    source_actualness: bool
    common_owner_authority: bool
    registered_prefix_miss_authority: bool
    scope_validation_authority: bool
    root_source_scoped_e1: bool
    e1_authority: bool
    generic_e1: bool
    successor_e1: bool
    producer_authority: bool
    producer_continuation_allowed: bool
    persistent_admission: bool
    queue_authority: bool
    e2_authority: bool
    e3_authority: bool
    e4_authority: bool
    e5_authority: bool
    terminal_leaf_authority: bool
    root_proof_close_authority: bool
    receipt_id: str
    digest: str


def _unsigned(values: Mapping[str, Any]) -> dict[str, Any]:
    result = {"receipt_type": RECEIPT_TYPE}
    for field in fields(QOneRegisteredPrefixE1ReceiptV2):
        if field.name not in {"receipt_id", "digest"}:
            result[field.name] = _json_copy(values[field.name])
    return result


def _construct(values: Mapping[str, Any]) -> QOneRegisteredPrefixE1ReceiptV2:
    result = object.__new__(QOneRegisteredPrefixE1ReceiptV2)
    for field in fields(QOneRegisteredPrefixE1ReceiptV2):
        object.__setattr__(result, field.name, values[field.name])
    return result


def _validate_receipt(receipt: QOneRegisteredPrefixE1ReceiptV2) -> None:
    if type(receipt) is not QOneRegisteredPrefixE1ReceiptV2:
        _reject(ConsumerRejectCode.INPUT_NOT_EXACT_MAPPING, "receipt class mismatch")
    for field in fields(QOneRegisteredPrefixE1ReceiptV2):
        if not hasattr(receipt, field.name):
            _reject(ConsumerRejectCode.MALFORMED_FIELD, f"receipt.{field.name} missing")
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    digest = canonical_digest_v2(_unsigned(values))
    if receipt.digest != digest or receipt.receipt_id != RECEIPT_ID_PREFIX + digest:
        _reject(ConsumerRejectCode.DIGEST_MISMATCH, "consumer receipt seal mismatch")
    if not (receipt.schema_version == 2 and type(receipt.schema_version) is int and receipt.status == STATUS and receipt.role == ROLE and receipt.scope_id == SCOPE_ID and receipt.coverage_semantics == COVERAGE_SEMANTICS and receipt.ordered_gaps == ORDERED_GAPS and receipt.next_unchecked_gap == NEXT_UNCHECKED_GAP and receipt.global_exhaustion is False and receipt.parent_kind == "ROOT_INITIALIZER_ACTUALNESS" and receipt.math_replay_id == MATH_REPLAY_ID):
        _reject(ConsumerRejectCode.MALFORMED_FIELD, "consumer receipt identity/scope changed")
    _grant(receipt.role_grant)
    if receipt.role_grant_id != GRANT_ID or receipt.role_grant_digest != canonical_digest_v2(_json_copy(receipt.role_grant)):
        _reject(ConsumerRejectCode.GRANT_MISMATCH, "consumer grant does not replay")
    raw, body, anchor, state = _source_chain(
        receipt.raw_q_one_g,
        receipt.source_body,
        receipt.root_anchor,
        receipt.source_state,
    )
    actual = _actualness(
        receipt.root_actualness,
        raw=raw,
        body=body,
        anchor=anchor,
        state=state,
    )
    owner = _owner(
        receipt.owner_receipt,
        raw=raw,
        body=body,
        anchor=anchor,
        state=state,
        actual=actual,
    )
    terminal = _production(
        receipt.terminal_receipt,
        raw=raw,
        body=body,
        anchor=anchor,
        state=state,
        actual=actual,
    )
    validation = _validation(
        receipt.scope_validation_receipt,
        raw=raw,
        body=body,
        anchor=anchor,
        state=state,
        actual=actual,
        owner=owner,
        terminal=terminal,
    )
    if not (
        receipt.raw_q_one_g_digest == canonical_digest_v2(raw)
        and receipt.body_id == body["body_id"]
        and receipt.body_digest == body["digest"]
        and receipt.anchor_id == anchor["anchor_id"]
        and receipt.anchor_digest == anchor["digest"]
        and receipt.state_id == state["state_id"]
        and receipt.state_digest == state["digest"]
        and receipt.root_actualness_id == actual["actualness_id"]
        and receipt.root_actualness_digest == actual["digest"]
        and receipt.owner_receipt_id == owner["receipt_id"]
        and receipt.owner_receipt_digest == owner["digest"]
        and receipt.terminal_receipt_id == terminal["receipt_id"]
        and receipt.terminal_receipt_digest == terminal["digest"]
        and receipt.scope_validation_receipt_id == validation["receipt_id"]
        and receipt.scope_validation_receipt_digest == validation["digest"]
    ):
        _reject(ConsumerRejectCode.SOURCE_REPLAY_FAILED, "consumer source references do not replay")
    math_replay = _phase_root_math(raw["root_context"])
    candidate = {
        "source_state_id": state["state_id"],
        "source_state_digest": state["digest"],
        "parent_kind": "ROOT_INITIALIZER_ACTUALNESS",
        "owner": OWNER,
        "owner_id": owner["owner_id"],
        "owner_digest": owner["owner_digest"],
        "scope_id": SCOPE_ID,
        "coverage_semantics": COVERAGE_SEMANTICS,
        "terminal_receipt_id": terminal["receipt_id"],
        "terminal_receipt_digest": terminal["digest"],
        "math_replay_id": MATH_REPLAY_ID,
        "math_replay_digest": math_replay["digest"],
        "target_phase": "TYPEI",
        "target_protocol": "CHARGED",
        "target_provenance": "FULL_CARRIER_POST_G",
        "target_scope": "fresh_source_tree_only",
        "source": math_replay["fresh_source"],
        "target_anchor": math_replay["target_anchor"],
    }
    candidate_digest = canonical_digest_v2(candidate)
    if (
        _json_copy(receipt.math_replay) != math_replay
        or receipt.math_replay_digest != math_replay["digest"]
        or _json_copy(receipt.candidate_witness) != candidate
        or receipt.candidate_witness_digest != candidate_digest
        or receipt.occurrence_value_digest != candidate_digest
        or receipt.occurrence_path != ()
    ):
        _reject(ConsumerRejectCode.MATH_REPLAY_FAILED, "consumer candidate witness does not replay")
    for name in ("terminal_receipt_direct_continuation_authority",):
        if getattr(receipt, name) is not False or type(getattr(receipt, name)) is not bool:
            _reject(ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, f"{name} must be false")
    for name in ("scope_aware_consumer_authority", "root_source_occurrence_authority", "source_actualness", "common_owner_authority", "registered_prefix_miss_authority", "scope_validation_authority", "root_source_scoped_e1"):
        if getattr(receipt, name) is not True or type(getattr(receipt, name)) is not bool:
            _reject(ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, f"{name} must be true")
    for name in ("e1_authority", "generic_e1", "successor_e1", "producer_authority", "producer_continuation_allowed", "persistent_admission", "queue_authority", "e2_authority", "e3_authority", "e4_authority", "e5_authority", "terminal_leaf_authority", "root_proof_close_authority"):
        if getattr(receipt, name) is not False or type(getattr(receipt, name)) is not bool:
            _reject(ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, f"{name} must be false")


def consume_q_one_registered_prefix_miss_for_e1_v2(
    *, raw_q_one_g: dict[str, Any], source_body: dict[str, Any], root_anchor: dict[str, Any], source_state: dict[str, Any], root_actualness: dict[str, Any], owner_receipt: dict[str, Any], terminal_receipt: dict[str, Any], scope_validation_receipt: dict[str, Any], role_grant: dict[str, Any]
) -> QOneRegisteredPrefixE1ReceiptV2:
    """Consume a verified prefix MISS and issue only root-source-scoped E1."""
    raw, body, anchor, state = _source_chain(raw_q_one_g, source_body, root_anchor, source_state)
    actual = _actualness(root_actualness, raw=raw, body=body, anchor=anchor, state=state)
    owner = _owner(owner_receipt, raw=raw, body=body, anchor=anchor, state=state, actual=actual)
    terminal = _production(terminal_receipt, raw=raw, body=body, anchor=anchor, state=state, actual=actual)
    validation = _validation(scope_validation_receipt, raw=raw, body=body, anchor=anchor, state=state, actual=actual, owner=owner, terminal=terminal)
    grant, grant_digest = _grant(role_grant)
    math_replay = _phase_root_math(raw["root_context"])
    candidate = {
        "source_state_id": state["state_id"], "source_state_digest": state["digest"], "parent_kind": "ROOT_INITIALIZER_ACTUALNESS", "owner": OWNER,
        "owner_id": owner["owner_id"], "owner_digest": owner["owner_digest"], "scope_id": SCOPE_ID, "coverage_semantics": COVERAGE_SEMANTICS,
        "terminal_receipt_id": terminal["receipt_id"], "terminal_receipt_digest": terminal["digest"], "math_replay_id": MATH_REPLAY_ID,
        "math_replay_digest": math_replay["digest"], "target_phase": "TYPEI", "target_protocol": "CHARGED", "target_provenance": "FULL_CARRIER_POST_G",
        "target_scope": "fresh_source_tree_only", "source": math_replay["fresh_source"], "target_anchor": math_replay["target_anchor"],
    }
    candidate_digest = canonical_digest_v2(candidate)
    values: dict[str, Any] = {
        "schema_version": 2, "status": STATUS, "role": ROLE, "role_grant": MappingProxyType(grant), "role_grant_id": grant["grant_id"], "role_grant_digest": grant_digest,
        "role_artifact_id": grant["artifact_id"], "role_artifact_semantic_sha256": grant["artifact_semantic_sha256"], "raw_q_one_g": MappingProxyType(raw), "raw_q_one_g_digest": canonical_digest_v2(raw),
        "source_body": MappingProxyType(body), "body_id": body["body_id"], "body_digest": body["digest"], "root_anchor": MappingProxyType(anchor), "anchor_id": anchor["anchor_id"], "anchor_digest": anchor["digest"],
        "source_state": MappingProxyType(state), "state_id": state["state_id"], "state_digest": state["digest"], "root_actualness": MappingProxyType(actual), "root_actualness_id": actual["actualness_id"], "root_actualness_digest": actual["digest"],
        "owner_receipt": MappingProxyType(owner), "owner_receipt_id": owner["receipt_id"], "owner_receipt_digest": owner["digest"], "terminal_receipt": MappingProxyType(terminal), "terminal_receipt_id": terminal["receipt_id"], "terminal_receipt_digest": terminal["digest"],
        "scope_validation_receipt": MappingProxyType(validation), "scope_validation_receipt_id": validation["receipt_id"], "scope_validation_receipt_digest": validation["digest"], "scope_id": SCOPE_ID, "coverage_semantics": COVERAGE_SEMANTICS, "ordered_gaps": ORDERED_GAPS, "next_unchecked_gap": NEXT_UNCHECKED_GAP, "global_exhaustion": False,
        "terminal_receipt_direct_continuation_authority": False, "scope_aware_consumer_authority": True, "root_source_occurrence_authority": True, "candidate_witness": MappingProxyType(candidate), "candidate_witness_digest": candidate_digest, "math_replay_id": MATH_REPLAY_ID, "math_replay": MappingProxyType(math_replay), "math_replay_digest": math_replay["digest"], "parent_kind": "ROOT_INITIALIZER_ACTUALNESS", "occurrence_path": (), "occurrence_value_digest": candidate_digest,
        "source_actualness": True, "common_owner_authority": True, "registered_prefix_miss_authority": True, "scope_validation_authority": True, "root_source_scoped_e1": True, "e1_authority": False, "generic_e1": False, "successor_e1": False, "producer_authority": False, "producer_continuation_allowed": False, "persistent_admission": False, "queue_authority": False, "e2_authority": False, "e3_authority": False, "e4_authority": False, "e5_authority": False, "terminal_leaf_authority": False, "root_proof_close_authority": False,
    }
    digest = canonical_digest_v2(_unsigned(values))
    values.update({"receipt_id": RECEIPT_ID_PREFIX + digest, "digest": digest})
    receipt = _construct(values)
    _validate_receipt(receipt)
    return receipt


def root_source_scoped_e1_receipt_to_mapping_v2(receipt: QOneRegisteredPrefixE1ReceiptV2) -> dict[str, Any]:
    """Serialize an exact consumer receipt after its local seal/authority checks."""
    _validate_receipt(receipt)
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    result = _unsigned(values)
    result["receipt_id"] = receipt.receipt_id
    result["digest"] = receipt.digest
    return result


# The following field set is intentionally kept local: the consumer cannot
# import the classifier/validator role merely to parse their receipts.
OWNER_FIELDS = frozenset({
    "receipt_type", "schema_version", "status", "role", "role_grant", "role_grant_id", "role_grant_digest", "role_artifact_id", "role_artifact_semantic_sha256", "raw_q_one_g", "raw_q_one_g_digest", "source_body", "body_id", "body_digest", "root_anchor", "anchor_id", "anchor_digest", "source_state", "state_id", "state_digest", "root_actualness", "root_actualness_id", "root_actualness_digest", "root_context", "owner_scope", "normalized_header", "normalized_header_digest", "facts_digest", "family_precedence", "family_precedence_digest", "predicate_results", "predicate_results_digest", "matched_families", "owner", "precedence_index", "owner_contract_id", "owner_contract_schema_version", "owner_id", "owner_digest", "terminal_receipt_dependency", "terminal_schedule_dependency", "source_actualness", "common_owner_authority", "registered_prefix_miss_authority", "scope_validation_authority", "root_source_scoped_e1", "scope_aware_consumer_authority", "root_source_occurrence_authority", "terminal_receipt_direct_continuation_authority", "e1_authority", "generic_e1", "successor_e1", "producer_authority", "producer_continuation_allowed", "persistent_admission", "queue_authority", "e2_authority", "e3_authority", "e4_authority", "e5_authority", "global_exhaustion", "terminal_leaf_authority", "root_proof_close_authority", "receipt_id", "digest",
})


__all__ = [
    "ConsumerError", "ConsumerRejectCode", "QOneRegisteredPrefixE1ReceiptV2", "canonical_digest_v2", "consume_q_one_registered_prefix_miss_for_e1_v2", "root_source_scoped_e1_receipt_to_mapping_v2",
]
