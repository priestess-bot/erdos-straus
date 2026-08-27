#!/usr/bin/env python3
"""Factory-only, zero-authority branch-scoped E1 receipt foundation.

This module implements the wire and replay substrate requested by
``t6-branch-scoped-priority-clearance-soundness-v2``.  It deliberately does
not implement an issuer, coordinator runtime, producer, verifier grant,
transition admission, or queue mutation.

The three public receipt types are immutable, slotted, and cannot be directly
constructed.  Their factories revalidate every embedded upstream seal and all
cross-bindings.  Route-decision, producer, and branch identities occupy
separate slots.  A ``PASS`` in this module means only that the supplied JSON
evidence is structurally self-consistent.  The ``consumed_occurrence_*`` fields
are a structural source/path binding only; they are not independent evidence
that a producer consumed the value.  Evaluator IDs/digests and the external
authority-policy digest are inert caller evidence, not registered capability
pins.  Every authority bit remains false.  Public constructors are disabled,
and any externally obtained object must still pass the public parser.

V2 is intentionally wire-incompatible with ``E1OccurrenceReceiptV1``.  In
particular, this module never emits or accepts ``MISS_COMPLETE`` and never
claims a global terminal-universe miss.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, fields
from enum import Enum
import hashlib
import json
import re
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, NoReturn, Sequence, TypeVar


SCHEMA_VERSION = 2

CLEARANCE_OUTCOME = "MISS_HIGHER_PRIORITY_POLICY_COMPLETE"
COVERAGE_SEMANTICS = "REGISTERED_HIGHER_PRIORITY_ONLY"
COMPLETENESS_SCOPE = "BEFORE_SELECTED_BRANCH_ONLY"
TERMINAL_UNIVERSE_STATUS = "NOT_ASSERTED_NOT_REQUIRED"
E1_SCOPE_KIND = "BRANCH_SCOPED"
OCCURRENCE_NAMESPACE = "PERSISTENT_SOURCE_STATE_WIRE"
COMPATIBILITY_MODE = "V2_NOT_V1_NO_IMPLICIT_CAST"
ACTIVATION_STATUS = "FOUNDATION_ONLY_NOT_GOAL_GATE2_OR_GATE4_5"
CONSUMPTION_EVIDENCE_STATUS = (
    "STRUCTURAL_BINDING_ONLY_NO_INDEPENDENT_CONSUMPTION_EVIDENCE"
)

SELECTION_STATUS = "STRUCTURAL_BRANCH_SELECTION_REPLAY_PASS_NO_AUTHORITY"
E1_STATUS = "STRUCTURAL_OCCURRENCE_REPLAY_PASS_NO_E1_AUTHORITY"
INDEPENDENT_STATUS = "INDEPENDENT_REPLAY_PASS_EVIDENCE_ONLY_NO_AUTHORITY"

POLICY_TYPE = "BranchDecisionPolicyV2"
PRIOR_REPLAY_TYPE = "PriorDecisionReplayEvidenceV2"
GUARD_REPLAY_TYPE = "SelectedBranchGuardReplayEvidenceV2"
LINEAGE_REPLAY_TYPE = "SourceLineageReplayEvidenceV2"
INDEPENDENT_EVIDENCE_TYPE = "E1IndependentReplayEvidenceInputV2"

DECISION_KINDS = frozenset({"TERMINAL", "PRODUCER"})
PRIOR_OUTCOMES = frozenset({"TERMINAL_MISS", "GUARD_FALSE"})

_DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")
_GIT_OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
_MAPPING_PROXY_TYPE = type(MappingProxyType({}))


class BranchScopedE1RejectCode(str, Enum):
    """Stable fail-closed codes for the V2 foundation."""

    INPUT_NOT_EXACT_MAPPING = "INPUT_NOT_EXACT_MAPPING"
    UNKNOWN_RECEIPT_TYPE = "UNKNOWN_RECEIPT_TYPE"
    UNKNOWN_SCHEMA_VERSION = "UNKNOWN_SCHEMA_VERSION"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    ID_MISMATCH = "ID_MISMATCH"
    UPSTREAM_SEAL_MISMATCH = "UPSTREAM_SEAL_MISMATCH"
    SOURCE_BINDING_MISMATCH = "SOURCE_BINDING_MISMATCH"
    POLICY_BINDING_MISMATCH = "POLICY_BINDING_MISMATCH"
    PRIOR_DECISION_GAP = "PRIOR_DECISION_GAP"
    PRIOR_REPLAY_MISMATCH = "PRIOR_REPLAY_MISMATCH"
    BRANCH_GUARD_MISMATCH = "BRANCH_GUARD_MISMATCH"
    OCCURRENCE_REPLAY_FAILED = "OCCURRENCE_REPLAY_FAILED"
    CROSS_RECEIPT_MISMATCH = "CROSS_RECEIPT_MISMATCH"
    REPLAY_EVIDENCE_MISMATCH = "REPLAY_EVIDENCE_MISMATCH"
    AUTHORITY_BOUNDARY_VIOLATION = "AUTHORITY_BOUNDARY_VIOLATION"
    V1_INCOMPATIBLE = "V1_INCOMPATIBLE"


class BranchScopedE1ValidationError(ValueError):
    """Validation failure carrying a machine-readable reject code."""

    def __init__(self, code: BranchScopedE1RejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: BranchScopedE1RejectCode, detail: str) -> NoReturn:
    raise BranchScopedE1ValidationError(code, detail)


def _copy_json(value: Any, *, path: str = "$") -> Any:
    if type(value) is dict or type(value) is _MAPPING_PROXY_TYPE:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                _reject(
                    BranchScopedE1RejectCode.MALFORMED_FIELD,
                    f"{path} has a non-string or empty object key",
                )
            result[key] = _copy_json(child, path=f"{path}.{key}")
        return result
    if type(value) is list or type(value) is tuple:
        return [
            _copy_json(child, path=f"{path}[{index}]")
            for index, child in enumerate(value)
        ]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(
        BranchScopedE1RejectCode.MALFORMED_FIELD,
        f"{path} contains non-canonical JSON type {type(value).__name__}",
    )


def _freeze_json(value: Any) -> Any:
    copied = _copy_json(value)
    if type(copied) is dict:
        return MappingProxyType(
            {key: _freeze_json(child) for key, child in copied.items()}
        )
    if type(copied) is list:
        return tuple(_freeze_json(child) for child in copied)
    return copied


def canonical_json_v2(value: Any) -> str:
    """Return the canonical ASCII JSON encoding used by every V2 seal."""

    try:
        return json.dumps(
            _copy_json(value),
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise BranchScopedE1ValidationError(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            f"value is not canonical JSON: {exc}",
        ) from exc


def canonical_digest_v2(value: Any) -> str:
    return hashlib.sha256(canonical_json_v2(value).encode("ascii")).hexdigest()


def loads_strict_v2(encoded: str) -> Any:
    """Decode integer-only JSON and reject duplicate keys."""

    if type(encoded) is not str:
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            "encoded JSON must be an exact string",
        )

    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                _reject(
                    BranchScopedE1RejectCode.FIELD_SET_MISMATCH,
                    f"duplicate JSON key {key!r}",
                )
            result[key] = value
        return result

    def bad_number(value: str) -> NoReturn:
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            f"non-integer JSON number {value!r} is not supported",
        )

    try:
        decoded = json.loads(
            encoded,
            object_pairs_hook=object_pairs,
            parse_float=bad_number,
            parse_constant=bad_number,
        )
    except BranchScopedE1ValidationError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        raise BranchScopedE1ValidationError(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            f"invalid JSON: {exc}",
        ) from exc
    return _copy_json(decoded)


def _require_exact_dict(value: Any, name: str) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(
            BranchScopedE1RejectCode.INPUT_NOT_EXACT_MAPPING,
            f"{name} must be an exact JSON object",
        )
    return _copy_json(value, path=name)


def _require_exact_fields(
    value: Mapping[str, Any], expected: frozenset[str], name: str
) -> None:
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        _reject(
            BranchScopedE1RejectCode.FIELD_SET_MISMATCH,
            f"{name} fields differ; missing={missing}, extra={extra}",
        )


def _require_text(value: Any, name: str) -> str:
    if type(value) is not str or not value:
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty string",
        )
    return value


def _require_plain_int(value: Any, name: str, *, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            f"{name} must be a plain integer >= {minimum}",
        )
    return value


def _require_digest(value: Any, name: str) -> str:
    if type(value) is not str or _DIGEST_RE.fullmatch(value) is None:
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            f"{name} must be a lowercase SHA-256 digest",
        )
    return value


def _require_git_oid(value: Any, name: str) -> str:
    if type(value) is not str or _GIT_OID_RE.fullmatch(value) is None:
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            f"{name} must be a full lowercase Git object ID",
        )
    return value


def _require_fixed(value: Any, expected: Any, name: str) -> None:
    if type(value) is not type(expected) or value != expected:
        _reject(
            BranchScopedE1RejectCode.AUTHORITY_BOUNDARY_VIOLATION,
            f"{name} must remain fixed at {expected!r}",
        )


def _verify_upstream_seal(payload: Mapping[str, Any], name: str) -> str:
    digest = _require_digest(payload.get("digest"), f"{name}.digest")
    unsigned = dict(payload)
    unsigned.pop("digest")
    if canonical_digest_v2(unsigned) != digest:
        _reject(
            BranchScopedE1RejectCode.UPSTREAM_SEAL_MISMATCH,
            f"{name}.digest does not replay",
        )
    return digest


POLICY_FIELDS = frozenset(
    {
        "policy_type",
        "schema_version",
        "head_sha",
        "head_tree_sha",
        "source_state_id",
        "source_state_digest",
        "source_owner_id",
        "source_owner_digest",
        "owner_domain_id",
        "owner_domain_digest",
        "coordinator_route_registry_id",
        "coordinator_route_registry_version",
        "coordinator_route_registry_digest",
        "policy_id",
        "policy_version",
        "decisions",
        "global_exhaustion",
        "digest",
    }
)
DECISION_FIELDS = frozenset(
    {
        "decision_index",
        "decision_id",
        "decision_kind",
        "decision_contract_digest",
        "producer_id",
        "producer_digest",
        "branch_id",
        "branch_contract_digest",
        "expected_occurrence_path",
        "expected_occurrence_path_digest",
    }
)
PRIOR_REPLAY_FIELDS = frozenset(
    {
        "evidence_type",
        "schema_version",
        "source_state_id",
        "source_state_digest",
        "policy_id",
        "policy_version",
        "policy_digest",
        "decision_id",
        "decision_index",
        "decision_kind",
        "decision_contract_digest",
        "producer_id",
        "producer_digest",
        "branch_id",
        "branch_contract_digest",
        "expected_occurrence_path",
        "expected_occurrence_path_digest",
        "replay_outcome",
        "replay_result_digest",
        "replayer_id",
        "replayer_digest",
        "replay_complete",
        "authority",
        "digest",
    }
)
GUARD_REPLAY_FIELDS = frozenset(
    {
        "evidence_type",
        "schema_version",
        "source_state_id",
        "source_state_digest",
        "policy_id",
        "policy_version",
        "policy_digest",
        "selected_decision_id",
        "selected_decision_contract_digest",
        "producer_id",
        "producer_digest",
        "selected_branch_id",
        "selected_branch_index",
        "selected_branch_contract_digest",
        "expected_occurrence_path",
        "expected_occurrence_path_digest",
        "branch_guard_id",
        "branch_guard_digest",
        "branch_guard_result_digest",
        "branch_guard_result",
        "replayer_id",
        "replayer_digest",
        "replay_complete",
        "authority",
        "digest",
    }
)
LINEAGE_FIELDS = frozenset(
    {
        "evidence_type",
        "schema_version",
        "head_sha",
        "head_tree_sha",
        "signed_gate0_manifest_digest",
        "external_trust_anchor_digest",
        "authority_policy_digest",
        "policy_id",
        "policy_version",
        "policy_digest",
        "coordinator_registry_id",
        "coordinator_registry_version",
        "coordinator_registry_digest",
        "role_grant_id",
        "role_grant_digest",
        "issuer_id",
        "issuer_digest",
        "issuer_grant_id",
        "issuer_grant_digest",
        "independent_verifier_id",
        "independent_verifier_digest",
        "claim_id",
        "claim_version",
        "claim_digest",
        "reproduction_id",
        "reproduction_digest",
        "source_schema_id",
        "source_schema_version",
        "source_state_id",
        "source_state_wire_digest",
        "source_owner_id",
        "source_owner_digest",
        "source_base_admission_receipt_id",
        "source_base_admission_receipt_digest",
        "parent_kind",
        "parent_id",
        "parent_digest",
        "parent_replay_digest",
        "e1_scope_kind",
        "e1_scope_id",
        "e1_scope_digest",
        "route_decision_id",
        "route_decision_index",
        "route_decision_contract_digest",
        "expected_occurrence_path",
        "expected_occurrence_path_digest",
        "producer_id",
        "producer_digest",
        "branch_id",
        "branch_contract_digest",
        "source_domain_id",
        "source_domain_digest",
        "domain_membership_replay_digest",
        "branch_guard_id",
        "branch_guard_digest",
        "branch_guard_result_digest",
        "occurrence_namespace",
        "provenance_digest",
        "source_lineage_replayer_id",
        "source_lineage_replayer_digest",
        "source_lineage_replay_result_digest",
        "source_lineage_replay_result",
        "authority",
        "digest",
    }
)
INDEPENDENT_EVIDENCE_FIELDS = frozenset(
    {
        "evidence_type",
        "schema_version",
        "source_state_id",
        "source_state_digest",
        "selection_receipt_id",
        "selection_receipt_digest",
        "e1_occurrence_receipt_id",
        "e1_occurrence_receipt_digest",
        "replayer_id",
        "replayer_digest",
        "selection_replay_result",
        "occurrence_replay_result",
        "source_lineage_replay_result",
        "upstream_revalidation_complete",
        "evidence_only",
        "authority",
        "digest",
    }
)


def _normalize_occurrence_path(
    value: Any, name: str, *, allow_tuple: bool
) -> tuple[str | int, ...]:
    allowed_types = {list, tuple} if allow_tuple else {list}
    if type(value) not in allowed_types or not value:
        expected = "nonempty list or tuple" if allow_tuple else "nonempty JSON array"
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            f"{name} must be a {expected}",
        )
    result: list[str | int] = []
    for index, segment in enumerate(value):
        if type(segment) is str and segment:
            result.append(segment)
        elif type(segment) is int and segment >= 0:
            result.append(segment)
        else:
            _reject(
                BranchScopedE1RejectCode.MALFORMED_FIELD,
                f"{name}[{index}] must be a nonempty string or nonnegative plain int",
            )
    return tuple(result)


def _require_path_digest(value: Any, path: Sequence[str | int], name: str) -> str:
    digest = _require_digest(value, name)
    if digest != canonical_digest_v2(path):
        _reject(
            BranchScopedE1RejectCode.POLICY_BINDING_MISMATCH,
            f"{name} does not replay from its expected occurrence path",
        )
    return digest


def _validate_policy_payload(value: Any) -> Mapping[str, Any]:
    policy = _require_exact_dict(value, "policy_payload")
    _require_exact_fields(policy, POLICY_FIELDS, "policy_payload")
    _require_fixed(policy["policy_type"], POLICY_TYPE, "policy_type")
    _require_fixed(policy["schema_version"], SCHEMA_VERSION, "policy schema_version")
    _require_git_oid(policy["head_sha"], "policy.head_sha")
    _require_git_oid(policy["head_tree_sha"], "policy.head_tree_sha")
    if len(policy["head_sha"]) != len(policy["head_tree_sha"]):
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            "policy HEAD and tree object IDs use different hash formats",
        )
    _require_text(policy["source_state_id"], "policy.source_state_id")
    _require_digest(policy["source_state_digest"], "policy.source_state_digest")
    _require_text(policy["source_owner_id"], "policy.source_owner_id")
    _require_digest(policy["source_owner_digest"], "policy.source_owner_digest")
    _require_text(policy["owner_domain_id"], "policy.owner_domain_id")
    _require_digest(policy["owner_domain_digest"], "policy.owner_domain_digest")
    _require_text(
        policy["coordinator_route_registry_id"],
        "policy.coordinator_route_registry_id",
    )
    _require_plain_int(
        policy["coordinator_route_registry_version"],
        "policy.coordinator_route_registry_version",
        minimum=1,
    )
    _require_digest(
        policy["coordinator_route_registry_digest"],
        "policy.coordinator_route_registry_digest",
    )
    _require_text(policy["policy_id"], "policy.policy_id")
    _require_plain_int(policy["policy_version"], "policy.policy_version", minimum=1)
    _require_fixed(policy["global_exhaustion"], False, "policy.global_exhaustion")
    decisions = policy["decisions"]
    if type(decisions) is not list or not decisions:
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            "policy.decisions must be a nonempty exact JSON array",
        )
    for index, decision_value in enumerate(decisions):
        decision = _require_exact_dict(decision_value, f"policy.decisions[{index}]")
        _require_exact_fields(decision, DECISION_FIELDS, f"policy.decisions[{index}]")
        _require_plain_int(
            decision["decision_index"], f"decision[{index}].decision_index"
        )
        if decision["decision_index"] != index:
            _reject(
                BranchScopedE1RejectCode.PRIOR_DECISION_GAP,
                "policy decision indices must be the continuous range 0..n-1",
            )
        _require_text(decision["decision_id"], f"decision[{index}].decision_id")
        if decision["decision_kind"] not in DECISION_KINDS:
            _reject(
                BranchScopedE1RejectCode.MALFORMED_FIELD,
                f"decision[{index}].decision_kind is unsupported",
            )
        _require_digest(
            decision["decision_contract_digest"],
            f"decision[{index}].decision_contract_digest",
        )
        if decision["decision_kind"] == "TERMINAL":
            for field_name in (
                "producer_id",
                "producer_digest",
                "branch_id",
                "branch_contract_digest",
                "expected_occurrence_path",
                "expected_occurrence_path_digest",
            ):
                if decision[field_name] is not None:
                    _reject(
                        BranchScopedE1RejectCode.POLICY_BINDING_MISMATCH,
                        f"terminal decision[{index}] must have null {field_name}",
                    )
        else:
            _require_text(decision["producer_id"], f"decision[{index}].producer_id")
            _require_digest(
                decision["producer_digest"], f"decision[{index}].producer_digest"
            )
            _require_text(decision["branch_id"], f"decision[{index}].branch_id")
            _require_digest(
                decision["branch_contract_digest"],
                f"decision[{index}].branch_contract_digest",
            )
            expected_path = _normalize_occurrence_path(
                decision["expected_occurrence_path"],
                f"decision[{index}].expected_occurrence_path",
                allow_tuple=False,
            )
            _require_path_digest(
                decision["expected_occurrence_path_digest"],
                expected_path,
                f"decision[{index}].expected_occurrence_path_digest",
            )
    if len({item["decision_id"] for item in decisions}) != len(decisions):
        _reject(
            BranchScopedE1RejectCode.POLICY_BINDING_MISMATCH,
            "policy decision IDs must be unique",
        )
    producer_action_keys: set[tuple[str, str, str, str]] = set()
    for decision in decisions:
        if decision["decision_kind"] != "PRODUCER":
            continue
        action_key = (
            decision["producer_id"],
            decision["branch_id"],
            decision["branch_contract_digest"],
            decision["expected_occurrence_path_digest"],
        )
        if action_key in producer_action_keys:
            _reject(
                BranchScopedE1RejectCode.POLICY_BINDING_MISMATCH,
                "policy repeats the same producer/branch/contract/occurrence action",
            )
        producer_action_keys.add(action_key)
    _verify_upstream_seal(policy, "policy_payload")
    return _freeze_json(policy)


def _validate_prior_replay_payload(value: Any, index: int) -> Mapping[str, Any]:
    name = f"prior_decision_replays[{index}]"
    replay = _require_exact_dict(value, name)
    _require_exact_fields(replay, PRIOR_REPLAY_FIELDS, name)
    _require_fixed(replay["evidence_type"], PRIOR_REPLAY_TYPE, f"{name}.evidence_type")
    _require_fixed(replay["schema_version"], SCHEMA_VERSION, f"{name}.schema_version")
    for field_name in (
        "source_state_id",
        "policy_id",
        "decision_id",
        "replayer_id",
    ):
        _require_text(replay[field_name], f"{name}.{field_name}")
    for field_name in (
        "source_state_digest",
        "policy_digest",
        "decision_contract_digest",
        "replay_result_digest",
        "replayer_digest",
    ):
        _require_digest(replay[field_name], f"{name}.{field_name}")
    _require_plain_int(replay["policy_version"], f"{name}.policy_version", minimum=1)
    _require_plain_int(replay["decision_index"], f"{name}.decision_index")
    if replay["decision_kind"] not in DECISION_KINDS:
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            f"{name}.decision_kind is unsupported",
        )
    if replay["decision_kind"] == "TERMINAL":
        for field_name in (
            "producer_id",
            "producer_digest",
            "branch_id",
            "branch_contract_digest",
            "expected_occurrence_path",
            "expected_occurrence_path_digest",
        ):
            if replay[field_name] is not None:
                _reject(
                    BranchScopedE1RejectCode.PRIOR_REPLAY_MISMATCH,
                    f"{name}.{field_name} must be null for a terminal decision",
                )
    else:
        _require_text(replay["producer_id"], f"{name}.producer_id")
        _require_digest(replay["producer_digest"], f"{name}.producer_digest")
        _require_text(replay["branch_id"], f"{name}.branch_id")
        _require_digest(
            replay["branch_contract_digest"], f"{name}.branch_contract_digest"
        )
        expected_path = _normalize_occurrence_path(
            replay["expected_occurrence_path"],
            f"{name}.expected_occurrence_path",
            allow_tuple=False,
        )
        _require_path_digest(
            replay["expected_occurrence_path_digest"],
            expected_path,
            f"{name}.expected_occurrence_path_digest",
        )
    expected_outcome = (
        "TERMINAL_MISS" if replay["decision_kind"] == "TERMINAL" else "GUARD_FALSE"
    )
    if (
        replay["replay_outcome"] not in PRIOR_OUTCOMES
        or replay["replay_outcome"] != expected_outcome
    ):
        _reject(
            BranchScopedE1RejectCode.PRIOR_REPLAY_MISMATCH,
            f"{name}.replay_outcome must be {expected_outcome} for its decision kind",
        )
    _require_fixed(replay["replay_complete"], True, f"{name}.replay_complete")
    _require_fixed(replay["authority"], False, f"{name}.authority")
    _verify_upstream_seal(replay, name)
    return _freeze_json(replay)


def _validate_guard_replay_payload(value: Any) -> Mapping[str, Any]:
    guard = _require_exact_dict(value, "selected_branch_guard_replay")
    _require_exact_fields(guard, GUARD_REPLAY_FIELDS, "selected_branch_guard_replay")
    _require_fixed(guard["evidence_type"], GUARD_REPLAY_TYPE, "guard.evidence_type")
    _require_fixed(guard["schema_version"], SCHEMA_VERSION, "guard.schema_version")
    for field_name in (
        "source_state_id",
        "policy_id",
        "selected_decision_id",
        "producer_id",
        "selected_branch_id",
        "branch_guard_id",
        "replayer_id",
    ):
        _require_text(guard[field_name], f"guard.{field_name}")
    for field_name in (
        "source_state_digest",
        "policy_digest",
        "selected_decision_contract_digest",
        "producer_digest",
        "selected_branch_contract_digest",
        "expected_occurrence_path_digest",
        "branch_guard_digest",
        "branch_guard_result_digest",
        "replayer_digest",
    ):
        _require_digest(guard[field_name], f"guard.{field_name}")
    _require_plain_int(guard["policy_version"], "guard.policy_version", minimum=1)
    _require_plain_int(guard["selected_branch_index"], "guard.selected_branch_index")
    expected_path = _normalize_occurrence_path(
        guard["expected_occurrence_path"],
        "guard.expected_occurrence_path",
        allow_tuple=False,
    )
    _require_path_digest(
        guard["expected_occurrence_path_digest"],
        expected_path,
        "guard.expected_occurrence_path_digest",
    )
    _require_fixed(guard["branch_guard_result"], True, "guard.branch_guard_result")
    _require_fixed(guard["replay_complete"], True, "guard.replay_complete")
    _require_fixed(guard["authority"], False, "guard.authority")
    _verify_upstream_seal(guard, "selected_branch_guard_replay")
    return _freeze_json(guard)


def _validate_lineage_payload(value: Any) -> Mapping[str, Any]:
    lineage = _require_exact_dict(value, "source_lineage_payload")
    _require_exact_fields(lineage, LINEAGE_FIELDS, "source_lineage_payload")
    _require_fixed(
        lineage["evidence_type"], LINEAGE_REPLAY_TYPE, "lineage.evidence_type"
    )
    _require_fixed(lineage["schema_version"], SCHEMA_VERSION, "lineage.schema_version")
    _require_git_oid(lineage["head_sha"], "lineage.head_sha")
    _require_git_oid(lineage["head_tree_sha"], "lineage.head_tree_sha")
    if len(lineage["head_sha"]) != len(lineage["head_tree_sha"]):
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            "lineage HEAD and tree object IDs use different hash formats",
        )
    text_fields = (
        "coordinator_registry_id",
        "policy_id",
        "role_grant_id",
        "issuer_id",
        "issuer_grant_id",
        "independent_verifier_id",
        "claim_id",
        "reproduction_id",
        "source_schema_id",
        "source_state_id",
        "source_owner_id",
        "source_base_admission_receipt_id",
        "parent_kind",
        "parent_id",
        "e1_scope_id",
        "route_decision_id",
        "producer_id",
        "branch_id",
        "source_domain_id",
        "branch_guard_id",
        "source_lineage_replayer_id",
    )
    for field_name in text_fields:
        _require_text(lineage[field_name], f"lineage.{field_name}")
    _require_plain_int(
        lineage["coordinator_registry_version"],
        "lineage.coordinator_registry_version",
        minimum=1,
    )
    _require_plain_int(lineage["policy_version"], "lineage.policy_version", minimum=1)
    _require_plain_int(lineage["route_decision_index"], "lineage.route_decision_index")
    _require_plain_int(
        lineage["source_schema_version"],
        "lineage.source_schema_version",
        minimum=1,
    )
    digest_fields = (
        "signed_gate0_manifest_digest",
        "external_trust_anchor_digest",
        "authority_policy_digest",
        "policy_digest",
        "coordinator_registry_digest",
        "role_grant_digest",
        "issuer_digest",
        "issuer_grant_digest",
        "independent_verifier_digest",
        "claim_digest",
        "reproduction_digest",
        "source_state_wire_digest",
        "source_owner_digest",
        "source_base_admission_receipt_digest",
        "parent_digest",
        "parent_replay_digest",
        "e1_scope_digest",
        "route_decision_contract_digest",
        "expected_occurrence_path_digest",
        "producer_digest",
        "branch_contract_digest",
        "source_domain_digest",
        "domain_membership_replay_digest",
        "branch_guard_digest",
        "branch_guard_result_digest",
        "provenance_digest",
        "source_lineage_replayer_digest",
        "source_lineage_replay_result_digest",
    )
    for field_name in digest_fields:
        _require_digest(lineage[field_name], f"lineage.{field_name}")
    expected_path = _normalize_occurrence_path(
        lineage["expected_occurrence_path"],
        "lineage.expected_occurrence_path",
        allow_tuple=False,
    )
    _require_path_digest(
        lineage["expected_occurrence_path_digest"],
        expected_path,
        "lineage.expected_occurrence_path_digest",
    )
    _require_plain_int(lineage["claim_version"], "lineage.claim_version", minimum=1)
    if (
        len(
            {
                lineage["issuer_id"],
                lineage["source_lineage_replayer_id"],
                lineage["independent_verifier_id"],
            }
        )
        != 3
    ):
        _reject(
            BranchScopedE1RejectCode.SOURCE_BINDING_MISMATCH,
            "issuer, lineage replayer, and independent verifier IDs must be distinct",
        )
    _require_fixed(lineage["e1_scope_kind"], E1_SCOPE_KIND, "lineage.e1_scope_kind")
    _require_fixed(
        lineage["occurrence_namespace"],
        OCCURRENCE_NAMESPACE,
        "lineage.occurrence_namespace",
    )
    _require_fixed(
        lineage["source_lineage_replay_result"],
        "PASS",
        "lineage.source_lineage_replay_result",
    )
    _require_fixed(lineage["authority"], False, "lineage.authority")
    _verify_upstream_seal(lineage, "source_lineage_payload")
    return _freeze_json(lineage)


def _validate_independent_evidence_payload(value: Any) -> Mapping[str, Any]:
    evidence = _require_exact_dict(value, "replay_evidence")
    _require_exact_fields(evidence, INDEPENDENT_EVIDENCE_FIELDS, "replay_evidence")
    _require_fixed(
        evidence["evidence_type"],
        INDEPENDENT_EVIDENCE_TYPE,
        "replay_evidence.evidence_type",
    )
    _require_fixed(
        evidence["schema_version"],
        SCHEMA_VERSION,
        "replay_evidence.schema_version",
    )
    for field_name in (
        "source_state_id",
        "selection_receipt_id",
        "e1_occurrence_receipt_id",
        "replayer_id",
    ):
        _require_text(evidence[field_name], f"replay_evidence.{field_name}")
    for field_name in (
        "source_state_digest",
        "selection_receipt_digest",
        "e1_occurrence_receipt_digest",
        "replayer_digest",
    ):
        _require_digest(evidence[field_name], f"replay_evidence.{field_name}")
    for field_name in (
        "selection_replay_result",
        "occurrence_replay_result",
        "source_lineage_replay_result",
    ):
        _require_fixed(evidence[field_name], "PASS", f"replay_evidence.{field_name}")
    _require_fixed(
        evidence["upstream_revalidation_complete"],
        True,
        "replay_evidence.upstream_revalidation_complete",
    )
    _require_fixed(evidence["evidence_only"], True, "replay_evidence.evidence_only")
    _require_fixed(evidence["authority"], False, "replay_evidence.authority")
    _verify_upstream_seal(evidence, "replay_evidence")
    return _freeze_json(evidence)


class _FactoryOnlyV2:
    __slots__ = ()

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} must be created by its V2 factory")


@dataclass(frozen=True, init=False, slots=True)
class BranchSelectionReceiptV2(_FactoryOnlyV2):
    RECEIPT_TYPE: ClassVar[str] = "BranchSelectionReceiptV2"
    ID_PREFIX: ClassVar[str] = "branch-selection-v2:"

    status: str
    policy_payload: Mapping[str, Any]
    policy_digest: str
    head_sha: str
    head_tree_sha: str
    source_state_id: str
    source_state_digest: str
    source_owner_id: str
    source_owner_digest: str
    owner_domain_id: str
    owner_domain_digest: str
    coordinator_route_registry_id: str
    coordinator_route_registry_version: int
    coordinator_route_registry_digest: str
    policy_id: str
    policy_version: int
    selected_decision_id: str
    selected_decision_contract_digest: str
    selected_producer_id: str
    selected_producer_digest: str
    selected_branch_id: str
    selected_branch_index: int
    selected_branch_contract_digest: str
    expected_occurrence_path: tuple[str | int, ...]
    expected_occurrence_path_digest: str
    ordered_prior_decision_ids: tuple[str, ...]
    ordered_prior_decision_ids_digest: str
    prior_decision_replays: tuple[Mapping[str, Any], ...]
    prior_decision_replays_digest: str
    selected_branch_guard_replay: Mapping[str, Any]
    selected_branch_guard_replay_digest: str
    selection_replay_result: str
    higher_priority_policy_replay_complete: bool
    branch_guard_result: bool
    clearance_outcome: str
    coverage_semantics: str
    completeness_scope: str
    terminal_universe_status: str
    compatibility_mode: str
    activation_status: str
    branch_scoped_e1: bool
    evidence_only: bool
    foundation_only: bool
    v1_compatible: bool
    v1_downcast_authority: bool
    generic_e1: bool
    transferable: bool
    global_exhaustion: bool
    universe_miss_authority: bool
    authority: bool
    branch_selection_authority: bool
    e1_authority: bool
    producer_authority: bool
    admission_authority: bool
    persistent_admission: bool
    queue_authority: bool
    enqueue_authority: bool
    goal_gate2_e1_authority: bool
    complete_terminal_schedule_authority: bool
    goal_gate4_authority: bool
    goal_gate5_authority: bool
    receipt_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class E1OccurrenceReceiptV2(_FactoryOnlyV2):
    RECEIPT_TYPE: ClassVar[str] = "E1OccurrenceReceiptV2"
    ID_PREFIX: ClassVar[str] = "e1-occurrence-v2:"

    status: str
    selection_receipt: Mapping[str, Any]
    selection_receipt_id: str
    selection_receipt_digest: str
    source_lineage_payload: Mapping[str, Any]
    source_lineage_payload_digest: str
    source_state_payload: Mapping[str, Any]
    head_sha: str
    head_tree_sha: str
    signed_gate0_manifest_digest: str
    external_trust_anchor_digest: str
    authority_policy_digest: str
    policy_id: str
    policy_version: int
    policy_digest: str
    coordinator_registry_id: str
    coordinator_registry_version: int
    coordinator_registry_digest: str
    role_grant_id: str
    role_grant_digest: str
    issuer_id: str
    issuer_digest: str
    issuer_grant_id: str
    issuer_grant_digest: str
    independent_verifier_id: str
    independent_verifier_digest: str
    claim_id: str
    claim_version: int
    claim_digest: str
    reproduction_id: str
    reproduction_digest: str
    source_schema_id: str
    source_schema_version: int
    source_state_id: str
    source_state_wire_digest: str
    source_owner_id: str
    source_owner_digest: str
    source_base_admission_receipt_id: str
    source_base_admission_receipt_digest: str
    parent_kind: str
    parent_id: str
    parent_digest: str
    parent_replay_digest: str
    e1_scope_kind: str
    e1_scope_id: str
    e1_scope_digest: str
    route_decision_id: str
    route_decision_index: int
    route_decision_contract_digest: str
    expected_occurrence_path: tuple[str | int, ...]
    expected_occurrence_path_digest: str
    producer_id: str
    producer_digest: str
    branch_id: str
    branch_contract_digest: str
    source_domain_id: str
    source_domain_digest: str
    domain_membership_replay_digest: str
    branch_guard_id: str
    branch_guard_digest: str
    branch_guard_result_digest: str
    occurrence_namespace: str
    occurrence_path: tuple[str | int, ...]
    occurrence_value: Any
    occurrence_value_digest: str
    consumed_occurrence_path: tuple[str | int, ...]
    consumed_occurrence_value: int
    consumed_occurrence_value_digest: str
    consumption_evidence_status: str
    provenance_digest: str
    source_lineage_replayer_id: str
    source_lineage_replayer_digest: str
    source_lineage_replay_result_digest: str
    source_lineage_replay_result: str
    structural_occurrence_replay_result: str
    clearance_outcome: str
    coverage_semantics: str
    completeness_scope: str
    terminal_universe_status: str
    compatibility_mode: str
    activation_status: str
    branch_scoped_e1: bool
    evidence_only: bool
    foundation_only: bool
    source_authentication_authority: bool
    actual_occurrence_authority: bool
    v1_compatible: bool
    v1_downcast_authority: bool
    generic_e1: bool
    transferable: bool
    global_exhaustion: bool
    universe_miss_authority: bool
    authority: bool
    branch_selection_authority: bool
    e1_authority: bool
    producer_authority: bool
    admission_authority: bool
    persistent_admission: bool
    queue_authority: bool
    enqueue_authority: bool
    issuer_grant_authority: bool
    independent_verifier_grant_authority: bool
    independent_consumption_evidence_authority: bool
    goal_gate2_e1_authority: bool
    complete_terminal_schedule_authority: bool
    goal_gate4_authority: bool
    goal_gate5_authority: bool
    receipt_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class E1IndependentReplayReceiptV2(_FactoryOnlyV2):
    RECEIPT_TYPE: ClassVar[str] = "E1IndependentReplayReceiptV2"
    ID_PREFIX: ClassVar[str] = "e1-independent-replay-v2:"

    status: str
    selection_receipt: Mapping[str, Any]
    selection_receipt_id: str
    selection_receipt_digest: str
    e1_occurrence_receipt: Mapping[str, Any]
    e1_occurrence_receipt_id: str
    e1_occurrence_receipt_digest: str
    replay_evidence: Mapping[str, Any]
    replay_evidence_digest: str
    source_state_id: str
    source_state_digest: str
    head_sha: str
    head_tree_sha: str
    source_owner_id: str
    source_owner_digest: str
    owner_domain_id: str
    owner_domain_digest: str
    coordinator_route_registry_id: str
    coordinator_route_registry_version: int
    coordinator_route_registry_digest: str
    policy_id: str
    policy_version: int
    policy_digest: str
    selected_decision_id: str
    selected_decision_contract_digest: str
    selected_producer_id: str
    selected_producer_digest: str
    selected_branch_id: str
    selected_branch_index: int
    selected_branch_contract_digest: str
    occurrence_value_digest: str
    consumption_evidence_status: str
    replayer_id: str
    replayer_digest: str
    replay_result: str
    selection_replay_result: str
    occurrence_replay_result: str
    source_lineage_replay_result: str
    upstream_revalidation_complete: bool
    clearance_outcome: str
    coverage_semantics: str
    completeness_scope: str
    terminal_universe_status: str
    compatibility_mode: str
    activation_status: str
    branch_scoped_e1: bool
    evidence_only: bool
    foundation_only: bool
    independence_authority: bool
    replayer_grant_authority: bool
    source_authentication_authority: bool
    actual_occurrence_authority: bool
    v1_compatible: bool
    v1_downcast_authority: bool
    generic_e1: bool
    transferable: bool
    global_exhaustion: bool
    universe_miss_authority: bool
    authority: bool
    branch_selection_authority: bool
    independent_replay_authority: bool
    independent_consumption_evidence_authority: bool
    e1_authority: bool
    producer_authority: bool
    admission_authority: bool
    persistent_admission: bool
    queue_authority: bool
    enqueue_authority: bool
    issuer_grant_authority: bool
    independent_verifier_grant_authority: bool
    goal_gate2_e1_authority: bool
    complete_terminal_schedule_authority: bool
    goal_gate4_authority: bool
    goal_gate5_authority: bool
    receipt_id: str
    digest: str


ReceiptV2 = (
    BranchSelectionReceiptV2 | E1OccurrenceReceiptV2 | E1IndependentReplayReceiptV2
)
ReceiptT = TypeVar("ReceiptT", bound=ReceiptV2)
_RECEIPT_CLASSES = {
    BranchSelectionReceiptV2.RECEIPT_TYPE: BranchSelectionReceiptV2,
    E1OccurrenceReceiptV2.RECEIPT_TYPE: E1OccurrenceReceiptV2,
    E1IndependentReplayReceiptV2.RECEIPT_TYPE: E1IndependentReplayReceiptV2,
}


def _common_boundary_values() -> dict[str, Any]:
    return {
        "clearance_outcome": CLEARANCE_OUTCOME,
        "coverage_semantics": COVERAGE_SEMANTICS,
        "completeness_scope": COMPLETENESS_SCOPE,
        "terminal_universe_status": TERMINAL_UNIVERSE_STATUS,
        "compatibility_mode": COMPATIBILITY_MODE,
        "activation_status": ACTIVATION_STATUS,
        "branch_scoped_e1": True,
        "evidence_only": True,
        "foundation_only": True,
        "v1_compatible": False,
        "v1_downcast_authority": False,
        "generic_e1": False,
        "transferable": False,
        "global_exhaustion": False,
        "universe_miss_authority": False,
        "authority": False,
        "branch_selection_authority": False,
        "e1_authority": False,
        "producer_authority": False,
        "admission_authority": False,
        "persistent_admission": False,
        "queue_authority": False,
        "enqueue_authority": False,
        "goal_gate2_e1_authority": False,
        "complete_terminal_schedule_authority": False,
        "goal_gate4_authority": False,
        "goal_gate5_authority": False,
    }


def _construct(cls: type[ReceiptT], values: Mapping[str, Any]) -> ReceiptT:
    instance = object.__new__(cls)
    for field in fields(cls):
        object.__setattr__(instance, field.name, values[field.name])
    return instance


def _unsigned_mapping(cls: type[ReceiptT], values: Mapping[str, Any]) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "receipt_type": cls.RECEIPT_TYPE,
        "schema_version": SCHEMA_VERSION,
    }
    for field in fields(cls):
        if field.name not in {"receipt_id", "digest"}:
            payload[field.name] = _copy_json(values[field.name])
    return payload


def _seal(cls: type[ReceiptT], values: Mapping[str, Any]) -> ReceiptT:
    mutable = dict(values)
    digest = canonical_digest_v2(_unsigned_mapping(cls, mutable))
    mutable["receipt_id"] = cls.ID_PREFIX + digest
    mutable["digest"] = digest
    return _construct(cls, mutable)


def _mapping_unchecked(receipt: ReceiptV2) -> dict[str, Any]:
    cls = type(receipt)
    if cls not in _RECEIPT_CLASSES.values():
        _reject(
            BranchScopedE1RejectCode.UNKNOWN_RECEIPT_TYPE,
            "value is not an exact V2 receipt class",
        )
    values = {field.name: getattr(receipt, field.name) for field in fields(cls)}
    payload = _unsigned_mapping(cls, values)
    payload["receipt_id"] = receipt.receipt_id
    payload["digest"] = receipt.digest
    return payload


def _require_receipt_field_set(value: Mapping[str, Any], cls: type[ReceiptT]) -> None:
    expected = frozenset(
        {"receipt_type", "schema_version", *(field.name for field in fields(cls))}
    )
    _require_exact_fields(value, expected, cls.RECEIPT_TYPE)
    if value["receipt_type"] != cls.RECEIPT_TYPE:
        _reject(
            BranchScopedE1RejectCode.UNKNOWN_RECEIPT_TYPE,
            f"expected {cls.RECEIPT_TYPE}",
        )
    if value["schema_version"] != SCHEMA_VERSION:
        _reject(
            BranchScopedE1RejectCode.UNKNOWN_SCHEMA_VERSION,
            f"{cls.RECEIPT_TYPE} must use schema version 2",
        )
    _require_digest(value["digest"], f"{cls.RECEIPT_TYPE}.digest")
    _require_text(value["receipt_id"], f"{cls.RECEIPT_TYPE}.receipt_id")


def _resolve_occurrence_path(source: Any, path: Sequence[str | int]) -> Any:
    current = source
    for index, segment in enumerate(path):
        if type(segment) is str and segment:
            if type(current) is not dict or segment not in current:
                _reject(
                    BranchScopedE1RejectCode.OCCURRENCE_REPLAY_FAILED,
                    f"occurrence path segment {index} is absent or not an object key",
                )
            current = current[segment]
        elif type(segment) is int and segment >= 0:
            if type(current) is not list or segment >= len(current):
                _reject(
                    BranchScopedE1RejectCode.OCCURRENCE_REPLAY_FAILED,
                    f"occurrence path segment {index} is outside its array",
                )
            current = current[segment]
        else:
            _reject(
                BranchScopedE1RejectCode.MALFORMED_FIELD,
                f"occurrence path segment {index} must be nonempty string or nonnegative int",
            )
    return _freeze_json(current)


def _validate_source_state_payload(
    value: Any, expected_id: str, expected_digest: str
) -> Mapping[str, Any]:
    source = _require_exact_dict(value, "source_state_payload")
    if source.get("state_id") != expected_id:
        _reject(
            BranchScopedE1RejectCode.SOURCE_BINDING_MISMATCH,
            "source_state_payload.state_id does not match the lineage",
        )
    state_id = _require_text(source["state_id"], "source_state_payload.state_id")
    unsigned = dict(source)
    unsigned.pop("state_id")
    if state_id != "state:" + canonical_digest_v2(unsigned):
        _reject(
            BranchScopedE1RejectCode.SOURCE_BINDING_MISMATCH,
            "source state content ID does not replay",
        )
    if canonical_digest_v2(source) != expected_digest:
        _reject(
            BranchScopedE1RejectCode.SOURCE_BINDING_MISMATCH,
            "source state wire digest does not replay",
        )
    return _freeze_json(source)


def make_branch_selection_receipt_v2(
    policy_payload: Mapping[str, Any],
    prior_decision_replays: Sequence[Mapping[str, Any]],
    selected_branch_guard_replay: Mapping[str, Any],
) -> BranchSelectionReceiptV2:
    """Replay one complete policy prefix and seal zero-authority evidence."""

    policy = _validate_policy_payload(policy_payload)
    if type(prior_decision_replays) not in {list, tuple}:
        _reject(
            BranchScopedE1RejectCode.MALFORMED_FIELD,
            "prior_decision_replays must be an exact list or tuple",
        )
    replays = tuple(
        _validate_prior_replay_payload(value, index)
        for index, value in enumerate(prior_decision_replays)
    )
    guard = _validate_guard_replay_payload(selected_branch_guard_replay)
    policy_digest = policy["digest"]
    selected_index = guard["selected_branch_index"]
    decisions = policy["decisions"]
    if selected_index >= len(decisions):
        _reject(
            BranchScopedE1RejectCode.BRANCH_GUARD_MISMATCH,
            "selected branch index is outside the frozen policy",
        )
    selected = decisions[selected_index]
    if selected["decision_kind"] != "PRODUCER":
        _reject(
            BranchScopedE1RejectCode.BRANCH_GUARD_MISMATCH,
            "the selected decision is not a producer branch",
        )
    policy_binding = (
        guard["source_state_id"] == policy["source_state_id"]
        and guard["source_state_digest"] == policy["source_state_digest"]
        and guard["policy_id"] == policy["policy_id"]
        and guard["policy_version"] == policy["policy_version"]
        and guard["policy_digest"] == policy_digest
        and guard["selected_decision_id"] == selected["decision_id"]
        and guard["selected_decision_contract_digest"]
        == selected["decision_contract_digest"]
        and guard["producer_id"] == selected["producer_id"]
        and guard["producer_digest"] == selected["producer_digest"]
        and guard["selected_branch_id"] == selected["branch_id"]
        and guard["selected_branch_contract_digest"]
        == selected["branch_contract_digest"]
        and guard["expected_occurrence_path"] == selected["expected_occurrence_path"]
        and guard["expected_occurrence_path_digest"]
        == selected["expected_occurrence_path_digest"]
    )
    if not policy_binding:
        _reject(
            BranchScopedE1RejectCode.BRANCH_GUARD_MISMATCH,
            "selected guard replay does not bind the exact policy slot",
        )
    if len(replays) != selected_index:
        _reject(
            BranchScopedE1RejectCode.PRIOR_DECISION_GAP,
            "prior replay count must equal the selected branch index",
        )
    for index, replay in enumerate(replays):
        decision = decisions[index]
        if not (
            replay["decision_index"] == index
            and replay["source_state_id"] == policy["source_state_id"]
            and replay["source_state_digest"] == policy["source_state_digest"]
            and replay["policy_id"] == policy["policy_id"]
            and replay["policy_version"] == policy["policy_version"]
            and replay["policy_digest"] == policy_digest
            and replay["decision_id"] == decision["decision_id"]
            and replay["decision_kind"] == decision["decision_kind"]
            and replay["decision_contract_digest"]
            == decision["decision_contract_digest"]
            and replay["producer_id"] == decision["producer_id"]
            and replay["producer_digest"] == decision["producer_digest"]
            and replay["branch_id"] == decision["branch_id"]
            and replay["branch_contract_digest"] == decision["branch_contract_digest"]
            and replay["expected_occurrence_path"]
            == decision["expected_occurrence_path"]
            and replay["expected_occurrence_path_digest"]
            == decision["expected_occurrence_path_digest"]
        ):
            _reject(
                BranchScopedE1RejectCode.PRIOR_REPLAY_MISMATCH,
                f"prior replay {index} does not bind policy decision {index}",
            )
    prior_ids = tuple(
        decision["decision_id"] for decision in decisions[:selected_index]
    )
    values: dict[str, Any] = {
        "status": SELECTION_STATUS,
        "policy_payload": policy,
        "policy_digest": policy_digest,
        "head_sha": policy["head_sha"],
        "head_tree_sha": policy["head_tree_sha"],
        "source_state_id": policy["source_state_id"],
        "source_state_digest": policy["source_state_digest"],
        "source_owner_id": policy["source_owner_id"],
        "source_owner_digest": policy["source_owner_digest"],
        "owner_domain_id": policy["owner_domain_id"],
        "owner_domain_digest": policy["owner_domain_digest"],
        "coordinator_route_registry_id": policy["coordinator_route_registry_id"],
        "coordinator_route_registry_version": policy[
            "coordinator_route_registry_version"
        ],
        "coordinator_route_registry_digest": policy[
            "coordinator_route_registry_digest"
        ],
        "policy_id": policy["policy_id"],
        "policy_version": policy["policy_version"],
        "selected_decision_id": selected["decision_id"],
        "selected_decision_contract_digest": selected["decision_contract_digest"],
        "selected_producer_id": selected["producer_id"],
        "selected_producer_digest": selected["producer_digest"],
        "selected_branch_id": selected["branch_id"],
        "selected_branch_index": selected_index,
        "selected_branch_contract_digest": selected["branch_contract_digest"],
        "expected_occurrence_path": tuple(selected["expected_occurrence_path"]),
        "expected_occurrence_path_digest": selected["expected_occurrence_path_digest"],
        "ordered_prior_decision_ids": prior_ids,
        "ordered_prior_decision_ids_digest": canonical_digest_v2(prior_ids),
        "prior_decision_replays": replays,
        "prior_decision_replays_digest": canonical_digest_v2(replays),
        "selected_branch_guard_replay": guard,
        "selected_branch_guard_replay_digest": guard["digest"],
        "selection_replay_result": "PASS",
        "higher_priority_policy_replay_complete": True,
        "branch_guard_result": True,
        **_common_boundary_values(),
    }
    return _seal(BranchSelectionReceiptV2, values)


def _coerce_selection(value: Any) -> BranchSelectionReceiptV2:
    if type(value) is BranchSelectionReceiptV2:
        return parse_branch_selection_receipt_v2(_mapping_unchecked(value))
    return parse_branch_selection_receipt_v2(value)


def make_e1_occurrence_receipt_v2(
    source_state_payload: Mapping[str, Any],
    occurrence_path: Sequence[str | int],
    source_lineage_payload: Mapping[str, Any],
    selection_receipt: BranchSelectionReceiptV2 | Mapping[str, Any],
) -> E1OccurrenceReceiptV2:
    """Resolve an integer occurrence from the explicit source wire and selection."""

    selection = _coerce_selection(selection_receipt)
    selection_wire = _freeze_json(_mapping_unchecked(selection))
    lineage = _validate_lineage_payload(source_lineage_payload)
    source = _validate_source_state_payload(
        source_state_payload,
        lineage["source_state_id"],
        lineage["source_state_wire_digest"],
    )
    guard = selection.selected_branch_guard_replay
    if not (
        lineage["head_sha"] == selection.head_sha
        and lineage["head_tree_sha"] == selection.head_tree_sha
        and lineage["source_state_id"] == selection.source_state_id
        and lineage["source_state_wire_digest"] == selection.source_state_digest
        and lineage["source_owner_id"] == selection.source_owner_id
        and lineage["source_owner_digest"] == selection.source_owner_digest
        and lineage["policy_id"] == selection.policy_id
        and lineage["policy_version"] == selection.policy_version
        and lineage["policy_digest"] == selection.policy_digest
        and lineage["coordinator_registry_id"]
        == selection.coordinator_route_registry_id
        and lineage["coordinator_registry_version"]
        == selection.coordinator_route_registry_version
        and lineage["coordinator_registry_digest"]
        == selection.coordinator_route_registry_digest
        and lineage["route_decision_id"] == selection.selected_decision_id
        and lineage["route_decision_index"] == selection.selected_branch_index
        and lineage["route_decision_contract_digest"]
        == selection.selected_decision_contract_digest
        and tuple(lineage["expected_occurrence_path"])
        == selection.expected_occurrence_path
        and lineage["expected_occurrence_path_digest"]
        == selection.expected_occurrence_path_digest
        and lineage["producer_id"] == selection.selected_producer_id
        and lineage["producer_digest"] == selection.selected_producer_digest
        and lineage["branch_id"] == selection.selected_branch_id
        and lineage["branch_contract_digest"]
        == selection.selected_branch_contract_digest
        and lineage["source_domain_id"] == selection.owner_domain_id
        and lineage["source_domain_digest"] == selection.owner_domain_digest
        and lineage["branch_guard_id"] == guard["branch_guard_id"]
        and lineage["branch_guard_digest"] == guard["branch_guard_digest"]
        and lineage["branch_guard_result_digest"] == guard["branch_guard_result_digest"]
    ):
        _reject(
            BranchScopedE1RejectCode.CROSS_RECEIPT_MISMATCH,
            "source lineage does not bind the exact selection receipt",
        )
    path = _normalize_occurrence_path(
        occurrence_path, "occurrence_path", allow_tuple=True
    )
    if path != selection.expected_occurrence_path:
        _reject(
            BranchScopedE1RejectCode.OCCURRENCE_REPLAY_FAILED,
            "caller occurrence_path differs from the selected policy action",
        )
    occurrence = _resolve_occurrence_path(_copy_json(source), path)
    if type(occurrence) is not int:
        _reject(
            BranchScopedE1RejectCode.OCCURRENCE_REPLAY_FAILED,
            "E1 occurrence_value must be an actual integer (bool is not accepted)",
        )
    values: dict[str, Any] = {
        "status": E1_STATUS,
        "selection_receipt": selection_wire,
        "selection_receipt_id": selection.receipt_id,
        "selection_receipt_digest": selection.digest,
        "source_lineage_payload": lineage,
        "source_lineage_payload_digest": lineage["digest"],
        "source_state_payload": source,
        "head_sha": lineage["head_sha"],
        "head_tree_sha": lineage["head_tree_sha"],
        "signed_gate0_manifest_digest": lineage["signed_gate0_manifest_digest"],
        "external_trust_anchor_digest": lineage["external_trust_anchor_digest"],
        "authority_policy_digest": lineage["authority_policy_digest"],
        "policy_id": lineage["policy_id"],
        "policy_version": lineage["policy_version"],
        "policy_digest": lineage["policy_digest"],
        "coordinator_registry_id": lineage["coordinator_registry_id"],
        "coordinator_registry_version": lineage["coordinator_registry_version"],
        "coordinator_registry_digest": lineage["coordinator_registry_digest"],
        "role_grant_id": lineage["role_grant_id"],
        "role_grant_digest": lineage["role_grant_digest"],
        "issuer_id": lineage["issuer_id"],
        "issuer_digest": lineage["issuer_digest"],
        "issuer_grant_id": lineage["issuer_grant_id"],
        "issuer_grant_digest": lineage["issuer_grant_digest"],
        "independent_verifier_id": lineage["independent_verifier_id"],
        "independent_verifier_digest": lineage["independent_verifier_digest"],
        "claim_id": lineage["claim_id"],
        "claim_version": lineage["claim_version"],
        "claim_digest": lineage["claim_digest"],
        "reproduction_id": lineage["reproduction_id"],
        "reproduction_digest": lineage["reproduction_digest"],
        "source_schema_id": lineage["source_schema_id"],
        "source_schema_version": lineage["source_schema_version"],
        "source_state_id": lineage["source_state_id"],
        "source_state_wire_digest": lineage["source_state_wire_digest"],
        "source_owner_id": lineage["source_owner_id"],
        "source_owner_digest": lineage["source_owner_digest"],
        "source_base_admission_receipt_id": lineage["source_base_admission_receipt_id"],
        "source_base_admission_receipt_digest": lineage[
            "source_base_admission_receipt_digest"
        ],
        "parent_kind": lineage["parent_kind"],
        "parent_id": lineage["parent_id"],
        "parent_digest": lineage["parent_digest"],
        "parent_replay_digest": lineage["parent_replay_digest"],
        "e1_scope_kind": lineage["e1_scope_kind"],
        "e1_scope_id": lineage["e1_scope_id"],
        "e1_scope_digest": lineage["e1_scope_digest"],
        "route_decision_id": lineage["route_decision_id"],
        "route_decision_index": lineage["route_decision_index"],
        "route_decision_contract_digest": lineage["route_decision_contract_digest"],
        "expected_occurrence_path": tuple(lineage["expected_occurrence_path"]),
        "expected_occurrence_path_digest": lineage["expected_occurrence_path_digest"],
        "producer_id": lineage["producer_id"],
        "producer_digest": lineage["producer_digest"],
        "branch_id": lineage["branch_id"],
        "branch_contract_digest": lineage["branch_contract_digest"],
        "source_domain_id": lineage["source_domain_id"],
        "source_domain_digest": lineage["source_domain_digest"],
        "domain_membership_replay_digest": lineage["domain_membership_replay_digest"],
        "branch_guard_id": lineage["branch_guard_id"],
        "branch_guard_digest": lineage["branch_guard_digest"],
        "branch_guard_result_digest": lineage["branch_guard_result_digest"],
        "occurrence_namespace": lineage["occurrence_namespace"],
        "occurrence_path": path,
        "occurrence_value": occurrence,
        "occurrence_value_digest": canonical_digest_v2(occurrence),
        "consumed_occurrence_path": path,
        "consumed_occurrence_value": occurrence,
        "consumed_occurrence_value_digest": canonical_digest_v2(occurrence),
        "consumption_evidence_status": CONSUMPTION_EVIDENCE_STATUS,
        "provenance_digest": lineage["provenance_digest"],
        "source_lineage_replayer_id": lineage["source_lineage_replayer_id"],
        "source_lineage_replayer_digest": lineage["source_lineage_replayer_digest"],
        "source_lineage_replay_result_digest": lineage[
            "source_lineage_replay_result_digest"
        ],
        "source_lineage_replay_result": "PASS",
        "structural_occurrence_replay_result": "PASS",
        "source_authentication_authority": False,
        "actual_occurrence_authority": False,
        "issuer_grant_authority": False,
        "independent_verifier_grant_authority": False,
        "independent_consumption_evidence_authority": False,
        **_common_boundary_values(),
    }
    return _seal(E1OccurrenceReceiptV2, values)


def _coerce_e1(value: Any) -> E1OccurrenceReceiptV2:
    if type(value) is E1OccurrenceReceiptV2:
        return parse_e1_occurrence_receipt_v2(_mapping_unchecked(value))
    return parse_e1_occurrence_receipt_v2(value)


def make_e1_independent_replay_receipt_v2(
    selection_receipt: BranchSelectionReceiptV2 | Mapping[str, Any],
    e1_occurrence_receipt: E1OccurrenceReceiptV2 | Mapping[str, Any],
    replay_evidence: Mapping[str, Any],
) -> E1IndependentReplayReceiptV2:
    """Bind independently supplied PASS evidence without granting authority."""

    selection = _coerce_selection(selection_receipt)
    e1 = _coerce_e1(e1_occurrence_receipt)
    evidence = _validate_independent_evidence_payload(replay_evidence)
    if not (
        e1.selection_receipt_id == selection.receipt_id
        and e1.selection_receipt_digest == selection.digest
        and evidence["source_state_id"] == e1.source_state_id
        and evidence["source_state_digest"] == e1.source_state_wire_digest
        and evidence["selection_receipt_id"] == selection.receipt_id
        and evidence["selection_receipt_digest"] == selection.digest
        and evidence["e1_occurrence_receipt_id"] == e1.receipt_id
        and evidence["e1_occurrence_receipt_digest"] == e1.digest
    ):
        _reject(
            BranchScopedE1RejectCode.REPLAY_EVIDENCE_MISMATCH,
            "independent replay evidence does not bind both receipts",
        )
    if not (
        evidence["replayer_id"] == e1.independent_verifier_id
        and evidence["replayer_digest"] == e1.independent_verifier_digest
    ):
        _reject(
            BranchScopedE1RejectCode.REPLAY_EVIDENCE_MISMATCH,
            "replay evidence does not bind the E1 independent-verifier pin",
        )
    selection_replayer_ids = {
        replay["replayer_id"] for replay in selection.prior_decision_replays
    }
    selection_replayer_ids.add(selection.selected_branch_guard_replay["replayer_id"])
    selection_replayer_digests = {
        replay["replayer_digest"] for replay in selection.prior_decision_replays
    }
    selection_replayer_digests.add(
        selection.selected_branch_guard_replay["replayer_digest"]
    )
    if evidence["replayer_id"] in {
        e1.producer_id,
        e1.issuer_id,
        e1.source_lineage_replayer_id,
        *selection_replayer_ids,
    }:
        _reject(
            BranchScopedE1RejectCode.REPLAY_EVIDENCE_MISMATCH,
            "independent replay identity must differ from producer and every upstream replayer",
        )
    if evidence["replayer_digest"] in {
        e1.producer_digest,
        e1.issuer_digest,
        e1.source_lineage_replayer_digest,
        *selection_replayer_digests,
    }:
        _reject(
            BranchScopedE1RejectCode.REPLAY_EVIDENCE_MISMATCH,
            "independent replay digest must differ from producer and every upstream replayer",
        )
    values: dict[str, Any] = {
        "status": INDEPENDENT_STATUS,
        "selection_receipt": _freeze_json(_mapping_unchecked(selection)),
        "selection_receipt_id": selection.receipt_id,
        "selection_receipt_digest": selection.digest,
        "e1_occurrence_receipt": _freeze_json(_mapping_unchecked(e1)),
        "e1_occurrence_receipt_id": e1.receipt_id,
        "e1_occurrence_receipt_digest": e1.digest,
        "replay_evidence": evidence,
        "replay_evidence_digest": evidence["digest"],
        "source_state_id": e1.source_state_id,
        "source_state_digest": e1.source_state_wire_digest,
        "head_sha": selection.head_sha,
        "head_tree_sha": selection.head_tree_sha,
        "source_owner_id": selection.source_owner_id,
        "source_owner_digest": selection.source_owner_digest,
        "owner_domain_id": selection.owner_domain_id,
        "owner_domain_digest": selection.owner_domain_digest,
        "coordinator_route_registry_id": selection.coordinator_route_registry_id,
        "coordinator_route_registry_version": selection.coordinator_route_registry_version,
        "coordinator_route_registry_digest": selection.coordinator_route_registry_digest,
        "policy_id": selection.policy_id,
        "policy_version": selection.policy_version,
        "policy_digest": selection.policy_digest,
        "selected_decision_id": selection.selected_decision_id,
        "selected_decision_contract_digest": selection.selected_decision_contract_digest,
        "selected_producer_id": selection.selected_producer_id,
        "selected_producer_digest": selection.selected_producer_digest,
        "selected_branch_id": selection.selected_branch_id,
        "selected_branch_index": selection.selected_branch_index,
        "selected_branch_contract_digest": selection.selected_branch_contract_digest,
        "occurrence_value_digest": e1.occurrence_value_digest,
        "consumption_evidence_status": CONSUMPTION_EVIDENCE_STATUS,
        "replayer_id": evidence["replayer_id"],
        "replayer_digest": evidence["replayer_digest"],
        "replay_result": "PASS",
        "selection_replay_result": "PASS",
        "occurrence_replay_result": "PASS",
        "source_lineage_replay_result": "PASS",
        "upstream_revalidation_complete": True,
        "independence_authority": False,
        "replayer_grant_authority": False,
        "source_authentication_authority": False,
        "actual_occurrence_authority": False,
        "independent_replay_authority": False,
        "independent_consumption_evidence_authority": False,
        "issuer_grant_authority": False,
        "independent_verifier_grant_authority": False,
        **_common_boundary_values(),
    }
    return _seal(E1IndependentReplayReceiptV2, values)


def parse_branch_selection_receipt_v2(value: Any) -> BranchSelectionReceiptV2:
    if type(value) is BranchSelectionReceiptV2:
        mapping = _mapping_unchecked(value)
    else:
        mapping = _require_exact_dict(value, "BranchSelectionReceiptV2")
    _require_receipt_field_set(mapping, BranchSelectionReceiptV2)
    expected = make_branch_selection_receipt_v2(
        mapping["policy_payload"],
        mapping["prior_decision_replays"],
        mapping["selected_branch_guard_replay"],
    )
    if mapping != _mapping_unchecked(expected):
        _reject(
            BranchScopedE1RejectCode.DIGEST_MISMATCH,
            "BranchSelectionReceiptV2 fields, ID, or seal do not replay",
        )
    return expected


def parse_e1_occurrence_receipt_v2(value: Any) -> E1OccurrenceReceiptV2:
    if type(value) is E1OccurrenceReceiptV2:
        mapping = _mapping_unchecked(value)
    else:
        mapping = _require_exact_dict(value, "E1OccurrenceReceiptV2")
    _require_receipt_field_set(mapping, E1OccurrenceReceiptV2)
    expected = make_e1_occurrence_receipt_v2(
        mapping["source_state_payload"],
        mapping["occurrence_path"],
        mapping["source_lineage_payload"],
        mapping["selection_receipt"],
    )
    if mapping != _mapping_unchecked(expected):
        _reject(
            BranchScopedE1RejectCode.DIGEST_MISMATCH,
            "E1OccurrenceReceiptV2 fields, ID, or seal do not replay",
        )
    return expected


def parse_e1_independent_replay_receipt_v2(
    value: Any,
) -> E1IndependentReplayReceiptV2:
    if type(value) is E1IndependentReplayReceiptV2:
        mapping = _mapping_unchecked(value)
    else:
        mapping = _require_exact_dict(value, "E1IndependentReplayReceiptV2")
    _require_receipt_field_set(mapping, E1IndependentReplayReceiptV2)
    expected = make_e1_independent_replay_receipt_v2(
        mapping["selection_receipt"],
        mapping["e1_occurrence_receipt"],
        mapping["replay_evidence"],
    )
    if mapping != _mapping_unchecked(expected):
        _reject(
            BranchScopedE1RejectCode.DIGEST_MISMATCH,
            "E1IndependentReplayReceiptV2 fields, ID, or seal do not replay",
        )
    return expected


def parse_receipt_v2(value: Any) -> ReceiptV2:
    if type(value) in _RECEIPT_CLASSES.values():
        receipt_type = type(value).RECEIPT_TYPE
    elif type(value) is dict:
        receipt_type = value.get("receipt_type")
    else:
        _reject(
            BranchScopedE1RejectCode.INPUT_NOT_EXACT_MAPPING,
            "V2 receipt must be an exact receipt class or exact JSON object",
        )
    if receipt_type in {
        "E1OccurrenceReceiptV1",
        "BranchSelectionReceiptV1",
        "E1IndependentReplayReceiptV1",
    }:
        _reject(
            BranchScopedE1RejectCode.V1_INCOMPATIBLE,
            "V1 and branch-scoped V2 receipts are intentionally incompatible",
        )
    if receipt_type == BranchSelectionReceiptV2.RECEIPT_TYPE:
        return parse_branch_selection_receipt_v2(value)
    if receipt_type == E1OccurrenceReceiptV2.RECEIPT_TYPE:
        return parse_e1_occurrence_receipt_v2(value)
    if receipt_type == E1IndependentReplayReceiptV2.RECEIPT_TYPE:
        return parse_e1_independent_replay_receipt_v2(value)
    _reject(
        BranchScopedE1RejectCode.UNKNOWN_RECEIPT_TYPE,
        f"unsupported receipt_type {receipt_type!r}",
    )


def parse_receipt_json_v2(encoded: str) -> ReceiptV2:
    """Strictly decode and completely replay one V2 receipt."""

    return parse_receipt_v2(loads_strict_v2(encoded))


def receipt_to_mapping_v2(receipt: ReceiptV2) -> dict[str, Any]:
    """Serialize only after a complete reconstruction from embedded inputs."""

    parsed = parse_receipt_v2(receipt)
    return _mapping_unchecked(parsed)


def receipt_to_json_v2(receipt: ReceiptV2) -> str:
    return canonical_json_v2(receipt_to_mapping_v2(receipt))


__all__ = [
    "BranchScopedE1RejectCode",
    "BranchScopedE1ValidationError",
    "BranchSelectionReceiptV2",
    "E1OccurrenceReceiptV2",
    "E1IndependentReplayReceiptV2",
    "CLEARANCE_OUTCOME",
    "COVERAGE_SEMANTICS",
    "COMPLETENESS_SCOPE",
    "TERMINAL_UNIVERSE_STATUS",
    "canonical_json_v2",
    "canonical_digest_v2",
    "loads_strict_v2",
    "make_branch_selection_receipt_v2",
    "make_e1_occurrence_receipt_v2",
    "make_e1_independent_replay_receipt_v2",
    "parse_branch_selection_receipt_v2",
    "parse_e1_occurrence_receipt_v2",
    "parse_e1_independent_replay_receipt_v2",
    "parse_receipt_v2",
    "parse_receipt_json_v2",
    "receipt_to_mapping_v2",
    "receipt_to_json_v2",
]
