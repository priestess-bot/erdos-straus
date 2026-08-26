#!/usr/bin/env python3
"""Pure common-owner classifier for a parentless ordinary q=1 G root.

The module deliberately has no repository loader and imports no project module.
It consumes explicit JSON-like preimages, reconstructs the root initializer
chain and the production actualness sidecar, then evaluates the complete V1
persistent-family precedence.  No terminal result is an input: classification
is independent of a registered-prefix HIT or MISS.

The role grant is an explicit value supplied by an exact-HEAD coordinator.  Its
local shape and content digest are bound into the output, but this module cannot
authenticate HEAD provenance by itself.
"""

from __future__ import annotations

from dataclasses import dataclass, fields
from enum import Enum
import hashlib
import json
from math import isqrt
import re
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, NoReturn


SCHEMA_VERSION = 2
RECEIPT_TYPE = "COMMON_Q1_ROOT_OWNER_RECEIPT_V2"
STATUS = "COMMON_OWNER_CLASSIFIED"
ROLE = "COMMON_ROOT_OWNER_CLASSIFIER"
ARTIFACT_ID = "q1_root_owner_classifier_v2"
ARTIFACT_PATH = "scripts/t6_q_one_root_owner_classifier_v2.py"
ARTIFACT_SYMBOLS = (
    "classify_q_one_root_owner_v2",
    "root_owner_receipt_to_mapping_v2",
)
GRANT_ID = "q1_common_root_owner_classifier_grant_v4"
CAPABILITIES = ("CLASSIFY_COMMON_Q1_ROOT_OWNER",)
AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V4"

RAW_SCHEMA_ID = "q1_root_initializer_raw_v2"
RAW_SCHEMA_VERSION = 2
INITIALIZER_ID = "q_one_root_initializer_envelope_v2"
DOMAIN_REPLAY_ID = "q_one_g_raw_integer_replay_v2"
SOURCE_TREE_SCOPE = "type_ii_endpoint_only"
EVIDENCE_CLASS = "EVIDENCE_ONLY_ROOT_SOURCE"
ROOT_ORIGIN_KIND = "PARENTLESS_ROOT"
OWNER_DOMAIN_ID = "ordinary_parentless_q1_g_root_v1"
OWNER = "type_ii_relation_g_endpoint"
PERSISTENT_OWNER_CONTRACT_ID = "t6_persistent_selector_state_v1"
PERSISTENT_OWNER_SCHEMA_VERSION = 1

BODY_ID_PREFIX = "q1-source-body:"
ANCHOR_ID_PREFIX = "root-init-anchor:"
STATE_ID_PREFIX = "state:"
ACTUALNESS_ID_PREFIX = "q1-root-source-actualness:"
ROOT_PROBLEM_ID_PREFIX = "q1-root-problem:"
RECEIPT_ID_PREFIX = "q1-common-root-owner:"

FAMILY_PRECEDENCE = (
    "generic_nontrivial_marked_state",
    "type_ii_relation_f_endpoint",
    "type_ii_relation_g_endpoint",
    "h4_non_v1_branch_or_descendant",
    "c8_terminal_first_surviving_parent",
    "type_i_c2_19_macro_target",
    "proper_root_high_endpoint",
    "proper_root_stutter_k_one",
    "proper_root_stutter_k_gt_one",
    "type_i_absorb_marked_residual",
    "type_i_a_one_overflow",
    "type_i_high_support_sink",
    "type_i_low_support_persistent_overflow",
    "type_i_a_gt_one_overflow_residual",
    "type_i_full_carrier_post_g",
)

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

ACTUALNESS_DATA_FIELDS = (
    "head_sha",
    "head_tree_sha",
    "v3_registry_id",
    "v3_registry_digest",
    "v3_role_manifest_digest",
    "initializer_grant_id",
    "initializer_grant_digest",
    "initializer_artifact_id",
    "initializer_artifact_semantic_sha256",
    "issuer_grant_id",
    "issuer_grant_digest",
    "issuer_artifact_id",
    "issuer_artifact_semantic_sha256",
    "fresh_module_binding_digest",
    "root_problem",
    "root_problem_id",
    "root_problem_digest",
    "raw_q_one_g",
    "raw_q_one_g_digest",
    "deterministic_initial_branch_replay",
    "deterministic_initial_branch_replay_digest",
    "body_id",
    "body_digest",
    "anchor_id",
    "anchor_digest",
    "state_id",
    "state_digest",
    "initializer_id",
    "initializer_contract_digest",
    "domain_replay_id",
    "domain_replay_digest",
    "owner_domain_id",
    "occurrence_kind",
    "parent_kind",
    "actualness_scope",
    "initializer_output_self_authorizing",
    "actualness_attestor_role",
    "source_actualness",
    "root_initializer_authority",
    "terminal_issuer_attestation_authority",
    "persistent_admission",
    "common_owner_authority",
    "e1_authority",
    "queue_authority",
)
ACTUALNESS_FIELDS = frozenset(
    {"receipt_type", "schema_version", *ACTUALNESS_DATA_FIELDS, "actualness_id", "digest"}
)

_DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")
_GIT_OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
_MAPPING_PROXY_TYPE = type(MappingProxyType({}))


class RootOwnerRejectCode(str, Enum):
    INPUT_NOT_EXACT_MAPPING = "INPUT_NOT_EXACT_MAPPING"
    INPUT_NOT_EXACT_TYPE = "INPUT_NOT_EXACT_TYPE"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    SOURCE_REPLAY_FAILED = "SOURCE_REPLAY_FAILED"
    ACTUALNESS_REPLAY_FAILED = "ACTUALNESS_REPLAY_FAILED"
    GRANT_MISMATCH = "GRANT_MISMATCH"
    OWNER_MISMATCH = "OWNER_MISMATCH"
    AUTHORITY_BOUNDARY_VIOLATION = "AUTHORITY_BOUNDARY_VIOLATION"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    ID_MISMATCH = "ID_MISMATCH"


class RootOwnerClassificationError(ValueError):
    def __init__(self, code: RootOwnerRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: RootOwnerRejectCode, detail: str) -> NoReturn:
    raise RootOwnerClassificationError(code, detail)


def _json_copy(value: Any, *, path: str = "$") -> Any:
    if type(value) in {dict, _MAPPING_PROXY_TYPE}:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                _reject(RootOwnerRejectCode.MALFORMED_FIELD, f"{path} has a non-string key")
            result[key] = _json_copy(child, path=f"{path}.{key}")
        return result
    if type(value) in {list, tuple}:
        return [_json_copy(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return value
    _reject(
        RootOwnerRejectCode.MALFORMED_FIELD,
        f"{path} contains unsupported type {type(value).__name__}",
    )


def canonical_json_v2(value: Any) -> str:
    try:
        return json.dumps(
            _json_copy(value),
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise RootOwnerClassificationError(
            RootOwnerRejectCode.MALFORMED_FIELD,
            f"value is not canonical JSON: {exc}",
        ) from exc


def canonical_digest_v2(value: Any) -> str:
    return hashlib.sha256(canonical_json_v2(value).encode("ascii")).hexdigest()


def _exact_mapping(value: Any, expected: frozenset[str], name: str) -> dict[str, Any]:
    if type(value) not in {dict, _MAPPING_PROXY_TYPE}:
        _reject(RootOwnerRejectCode.INPUT_NOT_EXACT_MAPPING, f"{name} must be an exact dict")
    if any(type(key) is not str for key in value):
        _reject(RootOwnerRejectCode.MALFORMED_FIELD, f"{name} keys must be exact strings")
    observed = frozenset(value)
    if observed != expected:
        _reject(
            RootOwnerRejectCode.FIELD_SET_MISMATCH,
            f"{name} missing={sorted(expected - observed)} extra={sorted(observed - expected)}",
        )
    return dict(value)


def _plain_int(value: Any) -> bool:
    return type(value) is int


def _require_digest(value: Any, name: str) -> str:
    if type(value) is not str or _DIGEST_RE.fullmatch(value) is None:
        _reject(RootOwnerRejectCode.MALFORMED_FIELD, f"{name} must be lowercase sha256")
    return value


def _require_content_id(value: Any, name: str, prefix: str) -> str:
    if (
        type(value) is not str
        or not value.startswith(prefix)
        or _DIGEST_RE.fullmatch(value[len(prefix) :]) is None
    ):
        _reject(RootOwnerRejectCode.MALFORMED_FIELD, f"{name} has the wrong content-ID prefix")
    return value


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    if value % 3 == 0:
        return value == 3
    divisor = 5
    step = 2
    limit = isqrt(value)
    while divisor <= limit:
        if value % divisor == 0:
            return False
        divisor += step
        step = 6 - step
    return True


def _factor(value: int) -> list[list[int]]:
    remainder = value
    factors: list[list[int]] = []
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while remainder % divisor == 0:
            remainder //= divisor
            exponent += 1
        factors.append([divisor, exponent])
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        factors.append([remainder, 1])
    return factors


def _validate_raw(value: Any) -> dict[str, Any]:
    raw = _exact_mapping(value, RAW_FIELDS, "raw_q_one_g")
    if raw["schema_id"] != RAW_SCHEMA_ID or raw["schema_version"] != RAW_SCHEMA_VERSION:
        _reject(RootOwnerRejectCode.SOURCE_REPLAY_FAILED, "raw schema changed")
    for name in RAW_FIELDS - {"schema_id", "gap_three_factorization"}:
        if not _plain_int(raw[name]):
            _reject(RootOwnerRejectCode.MALFORMED_FIELD, f"raw.{name} must be a plain integer")
    p = raw["root_context"]
    x = (p + 3) // 4
    if not (
        _is_prime(p)
        and p % 24 == 1
        and raw["equation_rank"] == p
        and raw["equation_numerator"] == 4
        and raw["equation_denominator"] == p
        and raw["q"] == 1
        and raw["gap_three_x"] == x
        and raw["endpoint_fiber_code"] == 2
        and raw["major_phase_code"] == 3
        and raw["provenance_code"] == 1
        and raw["mark_kind_code"] == 1
        and raw["mark_root_context"] == p
        and raw["mark_equation_rank"] == p
        and type(raw["gap_three_factorization"]) is list
        and raw["gap_three_factorization"] == _factor(x)
        and all(factor % 3 == 1 for factor, _exponent in raw["gap_three_factorization"])
    ):
        _reject(
            RootOwnerRejectCode.SOURCE_REPLAY_FAILED,
            "raw integers do not establish the ordinary parentless q=1 G root domain",
        )
    return _json_copy(raw)


INITIALIZER_CONTRACT_DIGEST = canonical_digest_v2(
    {
        "contract_id": INITIALIZER_ID,
        "schema_version": 2,
        "raw_schema_id": RAW_SCHEMA_ID,
        "dependency_order": [
            "CanonicalQOneGSourceBodyV2",
            "RootInitializerAnchorV2",
            "RawRootSourceStateV2",
        ],
        "root_origin_kind": ROOT_ORIGIN_KIND,
        "domain_replay_id": DOMAIN_REPLAY_ID,
        "source_tree_scope": SOURCE_TREE_SCOPE,
        "evidence_class": EVIDENCE_CLASS,
        "initializer_authority": False,
        "admission_authority": False,
        "queue_authority": False,
    }
)


def _sealed_mapping(
    value: Any,
    expected_fields: frozenset[str],
    *,
    name: str,
    kind_field: str,
    kind: str,
    id_field: str,
    prefix: str,
) -> dict[str, Any]:
    item = _exact_mapping(value, expected_fields, name)
    if item[kind_field] != kind or item["schema_version"] != 2:
        _reject(RootOwnerRejectCode.SOURCE_REPLAY_FAILED, f"{name} type/schema changed")
    digest = _require_digest(item["digest"], f"{name}.digest")
    content_id = _require_content_id(item[id_field], f"{name}.{id_field}", prefix)
    unsigned = _json_copy(item)
    unsigned.pop(id_field)
    unsigned.pop("digest")
    if canonical_digest_v2(unsigned) != digest or content_id != prefix + digest:
        _reject(RootOwnerRejectCode.DIGEST_MISMATCH, f"{name} seal does not replay")
    return _json_copy(item)


def _validate_source_chain(
    raw_value: Any,
    body_value: Any,
    anchor_value: Any,
    state_value: Any,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    raw = _validate_raw(raw_value)
    body = _sealed_mapping(
        body_value,
        BODY_FIELDS,
        name="source_body",
        kind_field="artifact_type",
        kind="CanonicalQOneGSourceBodyV2",
        id_field="body_id",
        prefix=BODY_ID_PREFIX,
    )
    expected_body = {
        "artifact_type": "CanonicalQOneGSourceBodyV2",
        "schema_version": 2,
        **{name: raw[name] for name in SEMANTIC_FIELDS},
        "source_tree_scope": SOURCE_TREE_SCOPE,
        "evidence_class": EVIDENCE_CLASS,
        "initializer_authority": False,
        "admission_authority": False,
        "queue_authority": False,
    }
    body_digest = canonical_digest_v2(expected_body)
    if body != {**expected_body, "body_id": BODY_ID_PREFIX + body_digest, "digest": body_digest}:
        _reject(RootOwnerRejectCode.SOURCE_REPLAY_FAILED, "body differs from raw replay")

    anchor = _sealed_mapping(
        anchor_value,
        ANCHOR_FIELDS,
        name="root_anchor",
        kind_field="artifact_type",
        kind="RootInitializerAnchorV2",
        id_field="anchor_id",
        prefix=ANCHOR_ID_PREFIX,
    )
    domain_replay_digest = canonical_digest_v2(
        {
            "domain_replay_id": DOMAIN_REPLAY_ID,
            "source_body_id": body["body_id"],
            "source_body_digest": body["digest"],
            "result": "ORDINARY_Q_ONE_G_RAW_INTEGER_REPLAY",
            "initializer_authority": False,
            "admission_authority": False,
            "queue_authority": False,
        }
    )
    expected_anchor = {
        "artifact_type": "RootInitializerAnchorV2",
        "schema_version": 2,
        "body_id": body["body_id"],
        "body_digest": body["digest"],
        "initializer_id": INITIALIZER_ID,
        "contract_digest": INITIALIZER_CONTRACT_DIGEST,
        "root_origin_kind": ROOT_ORIGIN_KIND,
        "domain_replay_id": DOMAIN_REPLAY_ID,
        "domain_replay_digest": domain_replay_digest,
        "evidence_class": EVIDENCE_CLASS,
        "initializer_authority": False,
        "admission_authority": False,
        "queue_authority": False,
    }
    anchor_digest = canonical_digest_v2(expected_anchor)
    if anchor != {
        **expected_anchor,
        "anchor_id": ANCHOR_ID_PREFIX + anchor_digest,
        "digest": anchor_digest,
    }:
        _reject(RootOwnerRejectCode.SOURCE_REPLAY_FAILED, "anchor differs from body replay")

    state = _sealed_mapping(
        state_value,
        STATE_FIELDS,
        name="source_state",
        kind_field="artifact_type",
        kind="RawRootSourceStateV2",
        id_field="state_id",
        prefix=STATE_ID_PREFIX,
    )
    expected_state = {
        "artifact_type": "RawRootSourceStateV2",
        "schema_version": 2,
        "body_id": body["body_id"],
        "body_digest": body["digest"],
        **{name: raw[name] for name in SEMANTIC_FIELDS},
        "source_tree_scope": SOURCE_TREE_SCOPE,
        "root_origin": {
            "root_initializer_anchor_id": anchor["anchor_id"],
            "digest": anchor["digest"],
        },
        "evidence_class": EVIDENCE_CLASS,
        "initializer_authority": False,
        "admission_authority": False,
        "queue_authority": False,
    }
    state_digest = canonical_digest_v2(expected_state)
    if state != {**expected_state, "state_id": STATE_ID_PREFIX + state_digest, "digest": state_digest}:
        _reject(RootOwnerRejectCode.SOURCE_REPLAY_FAILED, "state differs from root chain replay")
    return raw, body, anchor, state


def _validate_actualness(
    value: Any,
    *,
    raw: Mapping[str, Any],
    body: Mapping[str, Any],
    anchor: Mapping[str, Any],
    state: Mapping[str, Any],
) -> dict[str, Any]:
    actual = _exact_mapping(value, ACTUALNESS_FIELDS, "root_actualness")
    if actual["receipt_type"] != "QOneRootSourceActualnessReceiptV1" or actual["schema_version"] != 1:
        _reject(RootOwnerRejectCode.ACTUALNESS_REPLAY_FAILED, "actualness type/schema changed")
    if (
        type(actual["head_sha"]) is not str
        or type(actual["head_tree_sha"]) is not str
        or _GIT_OID_RE.fullmatch(actual["head_sha"]) is None
        or _GIT_OID_RE.fullmatch(actual["head_tree_sha"]) is None
        or len(actual["head_sha"]) != len(actual["head_tree_sha"])
    ):
        _reject(RootOwnerRejectCode.ACTUALNESS_REPLAY_FAILED, "actualness HEAD binding is malformed")
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
        "digest",
    ):
        _require_digest(actual[name], f"actualness.{name}")
    unsigned = _json_copy(actual)
    actualness_id = unsigned.pop("actualness_id")
    digest = unsigned.pop("digest")
    if (
        canonical_digest_v2(unsigned) != digest
        or actualness_id != ACTUALNESS_ID_PREFIX + digest
    ):
        _reject(RootOwnerRejectCode.DIGEST_MISMATCH, "actualness seal does not replay")

    p = raw["root_context"]
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
    root_problem_digest = canonical_digest_v2(root_problem)
    raw_digest = canonical_digest_v2(raw)
    branch = {
        "schema_id": "q1_deterministic_initial_g_branch_replay_v1",
        "root_problem_id": ROOT_PROBLEM_ID_PREFIX + root_problem_digest,
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
        "state_id": state["state_id"],
        "state_digest": state["digest"],
        "state_authority": {
            "initializer_authority": False,
            "persistent_admission": False,
            "queue_authority": False,
        },
    }
    expected = {
        "v3_registry_id": "t6_coordinator_role_registry_v3",
        "initializer_grant_id": "q1_root_initializer_grant_v3",
        "initializer_artifact_id": "q1_root_initializer_envelope_v2",
        "issuer_grant_id": "q1_terminal_issuer_grant_v3",
        "issuer_artifact_id": "q1_terminal_issuer_v1",
        "root_problem": root_problem,
        "root_problem_id": ROOT_PROBLEM_ID_PREFIX + root_problem_digest,
        "root_problem_digest": root_problem_digest,
        "raw_q_one_g": raw,
        "raw_q_one_g_digest": raw_digest,
        "deterministic_initial_branch_replay": branch,
        "deterministic_initial_branch_replay_digest": canonical_digest_v2(branch),
        "body_id": body["body_id"],
        "body_digest": body["digest"],
        "anchor_id": anchor["anchor_id"],
        "anchor_digest": anchor["digest"],
        "state_id": state["state_id"],
        "state_digest": state["digest"],
        "initializer_id": INITIALIZER_ID,
        "initializer_contract_digest": anchor["contract_digest"],
        "domain_replay_id": DOMAIN_REPLAY_ID,
        "domain_replay_digest": anchor["domain_replay_digest"],
        "owner_domain_id": OWNER_DOMAIN_ID,
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
    for name, expected_value in expected.items():
        if _json_copy(actual[name]) != _json_copy(expected_value):
            _reject(
                RootOwnerRejectCode.ACTUALNESS_REPLAY_FAILED,
                f"actualness.{name} does not replay from the explicit root preimage",
            )
    return _json_copy(actual)


def _validate_grant(value: Any) -> tuple[dict[str, Any], str]:
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
    for name, expected_value in expected.items():
        if grant[name] != expected_value or type(grant[name]) is not type(expected_value):
            _reject(RootOwnerRejectCode.GRANT_MISMATCH, f"role_grant.{name} changed")
    _require_digest(grant["artifact_semantic_sha256"], "role_grant.artifact_semantic_sha256")
    plain = _json_copy(grant)
    return plain, canonical_digest_v2(plain)


def _normalized_header(state: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "state_id": state["state_id"],
        "state_digest": state["digest"],
        "root_context": state["root_context"],
        "equation_rank": state["equation_rank"],
        "mark_kind": "ROOT_SOL",
        "mark_root_context": state["mark_root_context"],
        "mark_equation_rank": state["mark_equation_rank"],
        "facts": {
            "major_phase": "TYPEII_G_HANDOFF",
            "type_i_protocol": None,
            "t5_eta_p": 0,
            "pre_a": None,
            "absorb_m": None,
            "absorb_r_epsilon": 0,
            "reset_carrier": None,
            "provenance_kind": "ORDINARY_ENDPOINT",
            "endpoint_fiber": "G",
            "relation_q": 1,
            "support_A": None,
            "proper_root_k": None,
            "proper_root_height_class": "NONE",
            "proper_root_height": None,
            "proper_root_r": None,
            "is_overflow": False,
            "overflow_d": None,
            "chart_R": None,
            "chart_K": None,
            "carrier_M": None,
            "sink_scc_receipt": False,
            "same_chart_promotion_receipt": False,
            "full_carrier_scope": False,
            "atomic_arm": "NONE",
            "dispatch_status": "NONE",
        },
    }


def _predicate_results(header: Mapping[str, Any]) -> dict[str, bool]:
    facts = header["facts"]
    ordinary = header["mark_kind"] == "ROOT_SOL"
    results = {
        "generic_nontrivial_marked_state": header["mark_kind"] == "NONTRIVIAL_MARK"
        and facts["major_phase"] == "GENERIC_MARKED"
        and facts["provenance_kind"] == "GENERIC_MARKED",
        "type_ii_relation_f_endpoint": ordinary
        and facts["major_phase"] == "TYPEII_REL"
        and facts["endpoint_fiber"] == "F",
        "type_ii_relation_g_endpoint": ordinary
        and facts["major_phase"] == "TYPEII_G_HANDOFF"
        and facts["endpoint_fiber"] == "G",
        "h4_non_v1_branch_or_descendant": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["provenance_kind"] == "H4_RESIDUAL",
        "c8_terminal_first_surviving_parent": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["provenance_kind"] == "C8_PARENT",
        "type_i_c2_19_macro_target": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["provenance_kind"] == "C2_19_MACRO",
        "proper_root_high_endpoint": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["provenance_kind"] == "PROPER_ROOT"
        and facts["proper_root_height_class"] == "HIGH",
        "proper_root_stutter_k_one": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["provenance_kind"] == "PROPER_ROOT"
        and facts["proper_root_height_class"] == "LOW"
        and facts["proper_root_k"] == 1,
        "proper_root_stutter_k_gt_one": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["provenance_kind"] == "PROPER_ROOT"
        and facts["proper_root_height_class"] == "LOW"
        and _plain_int(facts["proper_root_k"])
        and facts["proper_root_k"] > 1,
        "type_i_absorb_marked_residual": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "ABSORB"
        and facts["provenance_kind"] == "MARKED_ABSORB"
        and not facts["is_overflow"]
        and _plain_int(facts["chart_R"])
        and facts["chart_R"] < header["root_context"],
        "type_i_a_one_overflow": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["is_overflow"]
        and facts["support_A"] == 1
        and _plain_int(facts["overflow_d"])
        and 1 <= facts["overflow_d"] < header["root_context"],
        "type_i_high_support_sink": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["is_overflow"]
        and _plain_int(facts["support_A"])
        and facts["support_A"] > (header["root_context"] - 1) ** 2 // 4
        and facts["sink_scc_receipt"],
        "type_i_low_support_persistent_overflow": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["is_overflow"]
        and facts["same_chart_promotion_receipt"]
        and _plain_int(facts["support_A"])
        and _plain_int(facts["carrier_M"])
        and facts["carrier_M"] % facts["support_A"] == 0
        and facts["carrier_M"] // facts["support_A"] >= 2,
        "type_i_a_gt_one_overflow_residual": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["is_overflow"]
        and _plain_int(facts["support_A"])
        and facts["support_A"] > 1,
        "type_i_full_carrier_post_g": ordinary
        and facts["major_phase"] == "TYPEI"
        and facts["type_i_protocol"] == "CHARGED"
        and facts["provenance_kind"] == "FULL_CARRIER_POST_G"
        and facts["full_carrier_scope"],
    }
    if tuple(results) != FAMILY_PRECEDENCE or any(type(value) is not bool for value in results.values()):
        _reject(RootOwnerRejectCode.OWNER_MISMATCH, "family predicate registry changed")
    return results


class _FactoryOnlyV2:
    __slots__ = ()

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} must be created by classify_q_one_root_owner_v2")


@dataclass(frozen=True, init=False, slots=True)
class CommonQOneRootOwnerReceiptV2(_FactoryOnlyV2):
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
    root_context: int
    owner_scope: str
    normalized_header: Mapping[str, Any]
    normalized_header_digest: str
    facts_digest: str
    family_precedence: tuple[str, ...]
    family_precedence_digest: str
    predicate_results: Mapping[str, bool]
    predicate_results_digest: str
    matched_families: tuple[str, ...]
    owner: str
    precedence_index: int
    owner_contract_id: str
    owner_contract_schema_version: int
    owner_id: str
    owner_digest: str
    terminal_receipt_dependency: bool
    terminal_schedule_dependency: bool
    source_actualness: bool
    common_owner_authority: bool
    registered_prefix_miss_authority: bool
    scope_validation_authority: bool
    root_source_scoped_e1: bool
    scope_aware_consumer_authority: bool
    root_source_occurrence_authority: bool
    terminal_receipt_direct_continuation_authority: bool
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
    global_exhaustion: bool
    terminal_leaf_authority: bool
    root_proof_close_authority: bool
    receipt_id: str
    digest: str


def _external(value: Any) -> Any:
    return _json_copy(value)


def _unsigned_receipt(values: Mapping[str, Any]) -> dict[str, Any]:
    result = {"receipt_type": RECEIPT_TYPE}
    for field in fields(CommonQOneRootOwnerReceiptV2):
        if field.name in {"receipt_id", "digest"}:
            continue
        result[field.name] = _external(values[field.name])
    return result


def _construct(values: Mapping[str, Any]) -> CommonQOneRootOwnerReceiptV2:
    result = object.__new__(CommonQOneRootOwnerReceiptV2)
    for field in fields(CommonQOneRootOwnerReceiptV2):
        object.__setattr__(result, field.name, values[field.name])
    return result


def _validate_receipt(receipt: CommonQOneRootOwnerReceiptV2) -> None:
    if type(receipt) is not CommonQOneRootOwnerReceiptV2:
        _reject(RootOwnerRejectCode.INPUT_NOT_EXACT_TYPE, "receipt must have the exact V2 class")
    for field in fields(CommonQOneRootOwnerReceiptV2):
        try:
            getattr(receipt, field.name)
        except AttributeError as exc:
            raise RootOwnerClassificationError(
                RootOwnerRejectCode.MALFORMED_FIELD,
                f"receipt.{field.name} is missing",
            ) from exc
    if not (
        receipt.schema_version == SCHEMA_VERSION
        and type(receipt.schema_version) is int
        and receipt.status == STATUS
        and receipt.role == ROLE
        and receipt.role_grant_id == GRANT_ID
        and receipt.role_artifact_id == ARTIFACT_ID
        and _plain_int(receipt.root_context)
        and receipt.root_context >= 2
        and receipt.owner_scope == "ROOT_SOURCE_DISPATCH_ONLY"
        and receipt.family_precedence == FAMILY_PRECEDENCE
        and receipt.matched_families == (OWNER,)
        and receipt.owner == OWNER
        and receipt.precedence_index == FAMILY_PRECEDENCE.index(OWNER)
        and receipt.owner_contract_id == PERSISTENT_OWNER_CONTRACT_ID
        and receipt.owner_contract_schema_version == PERSISTENT_OWNER_SCHEMA_VERSION
    ):
        _reject(RootOwnerRejectCode.OWNER_MISMATCH, "owner receipt identity or classification changed")
    grant, grant_digest = _validate_grant(receipt.role_grant)
    if not (
        receipt.role_grant_id == grant["grant_id"]
        and receipt.role_grant_digest == grant_digest
        and receipt.role_artifact_id == grant["artifact_id"]
        and receipt.role_artifact_semantic_sha256 == grant["artifact_semantic_sha256"]
    ):
        _reject(RootOwnerRejectCode.GRANT_MISMATCH, "embedded role grant does not replay")
    raw, body, anchor, state = _validate_source_chain(
        receipt.raw_q_one_g,
        receipt.source_body,
        receipt.root_anchor,
        receipt.source_state,
    )
    actualness = _validate_actualness(
        receipt.root_actualness,
        raw=raw,
        body=body,
        anchor=anchor,
        state=state,
    )
    if not (
        receipt.raw_q_one_g_digest == canonical_digest_v2(raw)
        and receipt.body_id == body["body_id"]
        and receipt.body_digest == body["digest"]
        and receipt.anchor_id == anchor["anchor_id"]
        and receipt.anchor_digest == anchor["digest"]
        and receipt.state_id == state["state_id"]
        and receipt.state_digest == state["digest"]
        and receipt.root_actualness_id == actualness["actualness_id"]
        and receipt.root_actualness_digest == actualness["digest"]
        and receipt.root_context == raw["root_context"]
    ):
        _reject(RootOwnerRejectCode.SOURCE_REPLAY_FAILED, "receipt source references do not replay")
    header = _json_copy(receipt.normalized_header)
    expected_header = _normalized_header(state)
    if header != expected_header:
        _reject(
            RootOwnerRejectCode.OWNER_MISMATCH,
            "normalized header is not the canonical header of the explicit source state",
        )
    results = _predicate_results(header)
    if not (
        receipt.normalized_header_digest == canonical_digest_v2(header)
        and receipt.facts_digest == canonical_digest_v2(header["facts"])
        and receipt.family_precedence_digest
        == canonical_digest_v2({"family_precedence": list(FAMILY_PRECEDENCE)})
        and _json_copy(receipt.predicate_results) == results
        and receipt.predicate_results_digest == canonical_digest_v2(results)
        and tuple(name for name in FAMILY_PRECEDENCE if results[name]) == (OWNER,)
    ):
        _reject(RootOwnerRejectCode.OWNER_MISMATCH, "header or predicate replay changed")
    expected_owner_digest = canonical_digest_v2(
        {
            "contract_id": PERSISTENT_OWNER_CONTRACT_ID,
            "schema_version": PERSISTENT_OWNER_SCHEMA_VERSION,
            "state_id": receipt.state_id,
            "facts_digest": receipt.facts_digest,
            "matched_families": [OWNER],
            "owner": OWNER,
            "precedence_index": FAMILY_PRECEDENCE.index(OWNER),
        }
    )
    if (
        receipt.owner_digest != expected_owner_digest
        or receipt.owner_id != "owner:" + expected_owner_digest
    ):
        _reject(RootOwnerRejectCode.OWNER_MISMATCH, "V1-equivalent owner ID/digest does not replay")
    true_fields = ("source_actualness", "common_owner_authority")
    false_fields = (
        "terminal_receipt_dependency",
        "terminal_schedule_dependency",
        "registered_prefix_miss_authority",
        "scope_validation_authority",
        "root_source_scoped_e1",
        "scope_aware_consumer_authority",
        "root_source_occurrence_authority",
        "terminal_receipt_direct_continuation_authority",
        "e1_authority",
        "generic_e1",
        "successor_e1",
        "producer_authority",
        "producer_continuation_allowed",
        "persistent_admission",
        "queue_authority",
        "e2_authority",
        "e3_authority",
        "e4_authority",
        "e5_authority",
        "global_exhaustion",
        "terminal_leaf_authority",
        "root_proof_close_authority",
    )
    if any(type(getattr(receipt, name)) is not bool or not getattr(receipt, name) for name in true_fields):
        _reject(RootOwnerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, "required owner authority is absent")
    if any(type(getattr(receipt, name)) is not bool or getattr(receipt, name) for name in false_fields):
        _reject(RootOwnerRejectCode.AUTHORITY_BOUNDARY_VIOLATION, "forbidden authority became true")
    for name in (
        "role_grant_digest",
        "role_artifact_semantic_sha256",
        "raw_q_one_g_digest",
        "body_digest",
        "anchor_digest",
        "state_digest",
        "root_actualness_digest",
        "normalized_header_digest",
        "family_precedence_digest",
        "predicate_results_digest",
        "owner_digest",
        "digest",
    ):
        _require_digest(getattr(receipt, name), f"receipt.{name}")
    _require_content_id(receipt.body_id, "receipt.body_id", BODY_ID_PREFIX)
    _require_content_id(receipt.anchor_id, "receipt.anchor_id", ANCHOR_ID_PREFIX)
    _require_content_id(receipt.state_id, "receipt.state_id", STATE_ID_PREFIX)
    _require_content_id(receipt.root_actualness_id, "receipt.root_actualness_id", ACTUALNESS_ID_PREFIX)
    _require_content_id(receipt.owner_id, "receipt.owner_id", "owner:")
    _require_content_id(receipt.receipt_id, "receipt.receipt_id", RECEIPT_ID_PREFIX)
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    digest = canonical_digest_v2(_unsigned_receipt(values))
    if receipt.digest != digest or receipt.receipt_id != RECEIPT_ID_PREFIX + digest:
        _reject(RootOwnerRejectCode.DIGEST_MISMATCH, "owner receipt seal does not replay")


def classify_q_one_root_owner_v2(
    *,
    raw_q_one_g: dict[str, Any],
    source_body: dict[str, Any],
    root_anchor: dict[str, Any],
    source_state: dict[str, Any],
    root_actualness: dict[str, Any],
    role_grant: dict[str, Any],
) -> CommonQOneRootOwnerReceiptV2:
    """Classify the source with no terminal-result dependency."""

    raw, body, anchor, state = _validate_source_chain(
        raw_q_one_g, source_body, root_anchor, source_state
    )
    actualness = _validate_actualness(
        root_actualness,
        raw=raw,
        body=body,
        anchor=anchor,
        state=state,
    )
    grant, grant_digest = _validate_grant(role_grant)
    header = _normalized_header(state)
    results = _predicate_results(header)
    matches = tuple(name for name in FAMILY_PRECEDENCE if results[name])
    if matches != (OWNER,):
        _reject(RootOwnerRejectCode.OWNER_MISMATCH, f"expected unique G owner, got {matches!r}")
    header_digest = canonical_digest_v2(header)
    precedence_digest = canonical_digest_v2({"family_precedence": list(FAMILY_PRECEDENCE)})
    results_digest = canonical_digest_v2(results)
    owner_digest = canonical_digest_v2(
        {
            "contract_id": PERSISTENT_OWNER_CONTRACT_ID,
            "schema_version": PERSISTENT_OWNER_SCHEMA_VERSION,
            "state_id": state["state_id"],
            "facts_digest": canonical_digest_v2(header["facts"]),
            "matched_families": list(matches),
            "owner": OWNER,
            "precedence_index": FAMILY_PRECEDENCE.index(OWNER),
        }
    )
    values: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "status": STATUS,
        "role": ROLE,
        "role_grant": MappingProxyType(grant),
        "role_grant_id": grant["grant_id"],
        "role_grant_digest": grant_digest,
        "role_artifact_id": grant["artifact_id"],
        "role_artifact_semantic_sha256": grant["artifact_semantic_sha256"],
        "raw_q_one_g": MappingProxyType(raw),
        "raw_q_one_g_digest": canonical_digest_v2(raw),
        "source_body": MappingProxyType(body),
        "body_id": body["body_id"],
        "body_digest": body["digest"],
        "root_anchor": MappingProxyType(anchor),
        "anchor_id": anchor["anchor_id"],
        "anchor_digest": anchor["digest"],
        "source_state": MappingProxyType(state),
        "state_id": state["state_id"],
        "state_digest": state["digest"],
        "root_actualness": MappingProxyType(actualness),
        "root_actualness_id": actualness["actualness_id"],
        "root_actualness_digest": actualness["digest"],
        "root_context": raw["root_context"],
        "owner_scope": "ROOT_SOURCE_DISPATCH_ONLY",
        "normalized_header": MappingProxyType(header),
        "normalized_header_digest": header_digest,
        "facts_digest": canonical_digest_v2(header["facts"]),
        "family_precedence": FAMILY_PRECEDENCE,
        "family_precedence_digest": precedence_digest,
        "predicate_results": MappingProxyType(results),
        "predicate_results_digest": results_digest,
        "matched_families": matches,
        "owner": OWNER,
        "precedence_index": FAMILY_PRECEDENCE.index(OWNER),
        "owner_contract_id": PERSISTENT_OWNER_CONTRACT_ID,
        "owner_contract_schema_version": PERSISTENT_OWNER_SCHEMA_VERSION,
        "owner_id": "owner:" + owner_digest,
        "owner_digest": owner_digest,
        "terminal_receipt_dependency": False,
        "terminal_schedule_dependency": False,
        "source_actualness": True,
        "common_owner_authority": True,
        "registered_prefix_miss_authority": False,
        "scope_validation_authority": False,
        "root_source_scoped_e1": False,
        "scope_aware_consumer_authority": False,
        "root_source_occurrence_authority": False,
        "terminal_receipt_direct_continuation_authority": False,
        "e1_authority": False,
        "generic_e1": False,
        "successor_e1": False,
        "producer_authority": False,
        "producer_continuation_allowed": False,
        "persistent_admission": False,
        "queue_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "global_exhaustion": False,
        "terminal_leaf_authority": False,
        "root_proof_close_authority": False,
    }
    digest = canonical_digest_v2(_unsigned_receipt(values))
    values.update({"receipt_id": RECEIPT_ID_PREFIX + digest, "digest": digest})
    receipt = _construct(values)
    _validate_receipt(receipt)
    return receipt


def root_owner_receipt_to_mapping_v2(
    receipt: CommonQOneRootOwnerReceiptV2,
) -> dict[str, Any]:
    """Serialize only an exact locally replayed owner receipt."""

    _validate_receipt(receipt)
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    result = _unsigned_receipt(values)
    result["receipt_id"] = receipt.receipt_id
    result["digest"] = receipt.digest
    return result


__all__ = [
    "CommonQOneRootOwnerReceiptV2",
    "RootOwnerClassificationError",
    "RootOwnerRejectCode",
    "canonical_digest_v2",
    "classify_q_one_root_owner_v2",
    "root_owner_receipt_to_mapping_v2",
]
