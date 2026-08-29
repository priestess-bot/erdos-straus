#!/usr/bin/env python3
"""Concrete, authority-bound SP-21/SP-22 selector slice.

This module implements one frozen policy registry on the full decidable
ordinary q=1,G root domain used by SP-22: p=24t+1 is prime, X=6t+1, and every
prime factor of X is 1 modulo 3.  The registry is externally signed, the
selected producer cannot alter it, every source action is independently
replayable, and the only persistent successor write is performed by the common
admission gate.

The module does *not* activate ``t6_persistent_selector_runtime_v2`` and does
not claim F1/F2/F3/T6 totality.  Its totality theorem is exactly the signed
q=1,G source-policy domain, not the repository's global reachable-state set.
"""

from __future__ import annotations

import argparse
import ast
import copy
from dataclasses import dataclass
from enum import Enum
import hashlib
import itertools
import json
from math import gcd, isqrt
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, NoReturn, Sequence


MODULE_ID = "t6_sp21_q1_p21169_concrete_selector_v1"
MODULE_VERSION = 1
BASE_HEAD_SHA = "e6e9e4a8c41b90a330b9ef333e542c18c2cb7be4"
TRUSTED_AUTHORITY_KEY_SHA256 = (
    "e03c0a9f1fd62668f5f89742aea49c16e68648e2e471480c3d9907d50346da65"
)
POLICY_RELATIVE_CLEARANCE = "MISS_HIGHER_PRIORITY_POLICY_COMPLETE"
POLICY_RELATIVE_COVERAGE = "REGISTERED_HIGHER_PRIORITY_ONLY"
GLOBAL_EXHAUSTION = False
M23 = (3, 7, 11, 15, 19, 23)
LATER_GAP = 31
SELECTED_PRODUCER_INDEX = 6
SHA256_DIGEST_INFO_PREFIX = bytes.fromhex(
    "3031300d060960864801650304020105000420"
)


class RejectCode(str, Enum):
    NON_CANONICAL_JSON = "NON_CANONICAL_JSON"
    MALFORMED_DOCUMENT = "MALFORMED_DOCUMENT"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    AUTHORITY_KEY_MISMATCH = "AUTHORITY_KEY_MISMATCH"
    AUTHORITY_SIGNATURE_INVALID = "AUTHORITY_SIGNATURE_INVALID"
    AUTHORITY_SCOPE_MISMATCH = "AUTHORITY_SCOPE_MISMATCH"
    ARTIFACT_LOCK_MISMATCH = "ARTIFACT_LOCK_MISMATCH"
    POLICY_INVALID = "POLICY_INVALID"
    PRIORITY_OVERLAP_GAP = "PRIORITY_OVERLAP_GAP"
    SOURCE_NOT_AUTHORIZED = "SOURCE_NOT_AUTHORIZED"
    SOURCE_INVALID = "SOURCE_INVALID"
    SOURCE_BINDING_MISMATCH = "SOURCE_BINDING_MISMATCH"
    REPLAY_MISMATCH = "REPLAY_MISMATCH"
    CLEARANCE_INVALID = "CLEARANCE_INVALID"
    TERMINAL_CERTIFICATE_INVALID = "TERMINAL_CERTIFICATE_INVALID"
    PRODUCER_GUARD_FALSE = "PRODUCER_GUARD_FALSE"
    TARGET_INVALID = "TARGET_INVALID"
    TARGET_TERMINAL_HIT = "TARGET_TERMINAL_HIT"
    EDGE_INVALID = "EDGE_INVALID"
    ADMISSION_REJECTED = "ADMISSION_REJECTED"
    DUPLICATE_QUEUE_TOKEN = "DUPLICATE_QUEUE_TOKEN"
    QUEUE_BYPASS = "QUEUE_BYPASS"
    REENTRY_REJECTED = "REENTRY_REJECTED"
    LOCAL_TOTALITY_FAILED = "LOCAL_TOTALITY_FAILED"


class ContractError(ValueError):
    """Fail-closed error with a stable machine-readable code."""

    def __init__(self, code: RejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: RejectCode, detail: str) -> NoReturn:
    raise ContractError(code, detail)


def _json_copy(value: Any, *, path: str = "$") -> Any:
    if type(value) is dict:
        out: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                _reject(RejectCode.NON_CANONICAL_JSON, f"{path}: bad object key")
            out[key] = _json_copy(child, path=f"{path}.{key}")
        return out
    if type(value) is list or type(value) is tuple:
        return [_json_copy(child, path=f"{path}[{i}]") for i, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(
        RejectCode.NON_CANONICAL_JSON,
        f"{path}: unsupported value type {type(value).__name__}",
    )


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        _json_copy(value),
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("ascii")


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_json(value: Any) -> str:
    return digest_bytes(canonical_bytes(value))


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        _reject(RejectCode.MALFORMED_DOCUMENT, f"cannot load {path}: {exc}")
    if type(value) is not dict:
        _reject(RejectCode.MALFORMED_DOCUMENT, f"{path}: top level is not object")
    return _json_copy(value)


def sealed(payload: Mapping[str, Any], id_field: str) -> dict[str, Any]:
    if id_field in payload:
        _reject(RejectCode.MALFORMED_DOCUMENT, f"payload already has {id_field}")
    out = _json_copy(dict(payload))
    out[id_field] = digest_json(out)
    return out


def verify_seal(value: Mapping[str, Any], id_field: str, code: RejectCode) -> None:
    if type(value) is not dict or type(value.get(id_field)) is not str:
        _reject(code, f"missing {id_field}")
    payload = {k: _json_copy(v) for k, v in value.items() if k != id_field}
    if digest_json(payload) != value[id_field]:
        _reject(code, f"{id_field} mismatch")


def _require_exact_keys(value: Mapping[str, Any], keys: set[str], *, where: str) -> None:
    if type(value) is not dict or set(value) != keys:
        got = sorted(value) if type(value) is dict else type(value).__name__
        _reject(RejectCode.MALFORMED_DOCUMENT, f"{where}: field set {got!r}")


def _is_hex_digest(value: Any, length: int = 64) -> bool:
    return (
        type(value) is str
        and len(value) == length
        and all(ch in "0123456789abcdef" for ch in value)
    )


def verify_rsa_pkcs1_v1_5_sha256(
    *, n_hex: str, exponent: int, message: bytes, signature_hex: str
) -> bool:
    try:
        n = int(n_hex, 16)
        signature = int(signature_hex, 16)
    except (TypeError, ValueError):
        return False
    if type(exponent) is not int or isinstance(exponent, bool) or exponent < 3:
        return False
    key_bytes = (n.bit_length() + 7) // 8
    if signature < 0 or signature >= n:
        return False
    encoded = pow(signature, exponent, n).to_bytes(key_bytes, "big")
    digest_info = SHA256_DIGEST_INFO_PREFIX + hashlib.sha256(message).digest()
    padding_len = key_bytes - len(digest_info) - 3
    if padding_len < 8:
        return False
    expected = b"\x00\x01" + b"\xff" * padding_len + b"\x00" + digest_info
    return encoded == expected


@dataclass(frozen=True, slots=True)
class AuthorityContext:
    authority_id: str
    statement_sha256: str
    policy_payload_sha256: str
    artifact_lock_payload_sha256: str
    base_head_sha: str
    key_fingerprint: str


@dataclass(frozen=True, slots=True)
class PolicyContext:
    document: dict[str, Any]
    payload: dict[str, Any]
    payload_sha256: str


@dataclass(frozen=True, slots=True)
class ArtifactLockContext:
    document: dict[str, Any]
    payload: dict[str, Any]
    payload_sha256: str


def parse_payload_document(
    document: Mapping[str, Any], *, schema_id: str, code: RejectCode
) -> tuple[dict[str, Any], str]:
    _require_exact_keys(
        document,
        {"schema_id", "schema_version", "payload", "payload_sha256"},
        where=schema_id,
    )
    if document["schema_id"] != schema_id or document["schema_version"] != 1:
        _reject(code, f"unexpected {schema_id} schema/version")
    if type(document["payload"]) is not dict:
        _reject(code, "payload is not object")
    actual = digest_json(document["payload"])
    if document["payload_sha256"] != actual:
        _reject(code, "payload digest mismatch")
    return _json_copy(document["payload"]), actual


def load_policy(path: Path) -> PolicyContext:
    document = load_json(path)
    payload, payload_sha256 = parse_payload_document(
        document,
        schema_id="SP21ConcretePolicyRegistryV1",
        code=RejectCode.POLICY_INVALID,
    )
    verify_policy_static(payload)
    return PolicyContext(document=document, payload=payload, payload_sha256=payload_sha256)


def load_artifact_lock(path: Path) -> ArtifactLockContext:
    document = load_json(path)
    payload, payload_sha256 = parse_payload_document(
        document,
        schema_id="SP21ArtifactLockV1",
        code=RejectCode.ARTIFACT_LOCK_MISMATCH,
    )
    return ArtifactLockContext(document=document, payload=payload, payload_sha256=payload_sha256)


def verify_artifact_lock(lock: ArtifactLockContext, repo_root: Path) -> dict[str, Any]:
    payload = lock.payload
    if payload.get("base_head_sha") != BASE_HEAD_SHA:
        _reject(RejectCode.ARTIFACT_LOCK_MISMATCH, "base HEAD mismatch")
    artifacts = payload.get("artifacts")
    if type(artifacts) is not list or not artifacts:
        _reject(RejectCode.ARTIFACT_LOCK_MISMATCH, "empty artifact list")
    seen: set[str] = set()
    verified: list[dict[str, str]] = []
    for row in artifacts:
        if type(row) is not dict or set(row) != {"path", "role", "sha256"}:
            _reject(RejectCode.ARTIFACT_LOCK_MISMATCH, "bad artifact row")
        rel = row["path"]
        if type(rel) is not str or rel.startswith("/") or ".." in Path(rel).parts:
            _reject(RejectCode.ARTIFACT_LOCK_MISMATCH, f"unsafe path {rel!r}")
        if rel in seen:
            _reject(RejectCode.ARTIFACT_LOCK_MISMATCH, f"duplicate path {rel}")
        seen.add(rel)
        file_path = repo_root / rel
        try:
            data = file_path.read_bytes()
        except OSError as exc:
            _reject(RejectCode.ARTIFACT_LOCK_MISMATCH, f"cannot read {rel}: {exc}")
        actual = digest_bytes(data)
        if actual != row["sha256"]:
            _reject(RejectCode.ARTIFACT_LOCK_MISMATCH, f"digest mismatch: {rel}")
        verified.append({"path": rel, "sha256": actual})
    return sealed(
        {
            "receipt_type": "ArtifactLockVerificationReceiptV1",
            "artifact_lock_payload_sha256": lock.payload_sha256,
            "base_head_sha": BASE_HEAD_SHA,
            "verified_artifacts": verified,
            "all_locked_artifacts_match": True,
        },
        "receipt_id",
    )


def load_and_verify_authority(
    path: Path,
    *,
    policy: PolicyContext,
    artifact_lock: ArtifactLockContext,
) -> AuthorityContext:
    anchor = load_json(path)
    required = {
        "schema_id",
        "schema_version",
        "authority_id",
        "public_key",
        "statement",
        "statement_sha256",
        "signature_algorithm",
        "signature_hex",
    }
    _require_exact_keys(anchor, required, where="authority anchor")
    if anchor["schema_id"] != "SP21ExternalAuthorityAnchorV1" or anchor["schema_version"] != 1:
        _reject(RejectCode.MALFORMED_DOCUMENT, "bad authority schema")
    public_key = anchor["public_key"]
    if type(public_key) is not dict or set(public_key) != {"n_hex", "e"}:
        _reject(RejectCode.MALFORMED_DOCUMENT, "bad authority key")
    key_fingerprint = digest_json(public_key)
    if key_fingerprint != TRUSTED_AUTHORITY_KEY_SHA256:
        _reject(RejectCode.AUTHORITY_KEY_MISMATCH, "untrusted authority key")
    statement = anchor["statement"]
    if type(statement) is not dict:
        _reject(RejectCode.MALFORMED_DOCUMENT, "authority statement is not object")
    statement_sha256 = digest_json(statement)
    if anchor["statement_sha256"] != statement_sha256:
        _reject(RejectCode.DIGEST_MISMATCH, "authority statement digest mismatch")
    if anchor["signature_algorithm"] != "RSA_PKCS1_V1_5_SHA256":
        _reject(RejectCode.AUTHORITY_SIGNATURE_INVALID, "unsupported signature algorithm")
    if not verify_rsa_pkcs1_v1_5_sha256(
        n_hex=public_key["n_hex"],
        exponent=public_key["e"],
        message=canonical_bytes(statement),
        signature_hex=anchor["signature_hex"],
    ):
        _reject(RejectCode.AUTHORITY_SIGNATURE_INVALID, "signature verification failed")
    expected = {
        "authority_id": "sp21_external_coordinator_one_shot_v1",
        "authority_scope": "SP21_SP22_CONCRETE_POLICY_AND_ARTIFACT_LOCK_V1",
        "base_head_sha": BASE_HEAD_SHA,
        "policy_payload_sha256": policy.payload_sha256,
        "artifact_lock_payload_sha256": artifact_lock.payload_sha256,
        "producer_may_mutate_policy": False,
        "caller_authority_boolean_accepted": False,
        "status": "EXTERNAL_COORDINATOR_AUTHORIZED",
    }
    if statement != expected:
        _reject(RejectCode.AUTHORITY_SCOPE_MISMATCH, "authority statement is not exact")
    if (
        anchor["authority_id"] != statement["authority_id"]
        or anchor["authority_id"]
        != policy.payload["authority_contract"]["authority_id"]
    ):
        _reject(RejectCode.AUTHORITY_SCOPE_MISMATCH, "authority ID is not signed/bound")
    return AuthorityContext(
        authority_id=anchor["authority_id"],
        statement_sha256=statement_sha256,
        policy_payload_sha256=policy.payload_sha256,
        artifact_lock_payload_sha256=artifact_lock.payload_sha256,
        base_head_sha=BASE_HEAD_SHA,
        key_fingerprint=key_fingerprint,
    )


def _action_contract_digest(action: Mapping[str, Any]) -> str:
    return digest_json(action)


def verify_policy_static(payload: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "registry_id",
        "registry_version",
        "base_head_sha",
        "authority_contract",
        "source_domain",
        "source_policy",
        "target_terminal_policy",
        "owner_registry",
        "admission_contract",
        "receipt_semantics",
        "priority_overlap_proof",
        "non_claims",
    }
    _require_exact_keys(payload, required, where="policy payload")
    if payload["registry_version"] != 1 or payload["base_head_sha"] != BASE_HEAD_SHA:
        _reject(RejectCode.POLICY_INVALID, "registry version/base HEAD")
    source_policy = payload["source_policy"]
    if type(source_policy) is not dict:
        _reject(RejectCode.POLICY_INVALID, "source policy missing")
    actions = source_policy.get("actions")
    if type(actions) is not list or len(actions) != 8:
        _reject(RejectCode.POLICY_INVALID, "source policy must contain eight actions")
    if source_policy.get("selected_producer_index") != SELECTED_PRODUCER_INDEX:
        _reject(RejectCode.POLICY_INVALID, "selected producer index")
    if source_policy.get("policy_mutable_by_actions") is not False:
        _reject(RejectCode.POLICY_INVALID, "actions may mutate policy")
    seen_ids: set[str] = set()
    for index, action in enumerate(actions):
        if type(action) is not dict or action.get("index") != index:
            _reject(RejectCode.POLICY_INVALID, f"bad action index {index}")
        action_id = action.get("action_id")
        if type(action_id) is not str or action_id in seen_ids:
            _reject(RejectCode.POLICY_INVALID, "duplicate/bad action id")
        seen_ids.add(action_id)
        mandatory = {
            "index",
            "action_id",
            "action_version",
            "kind",
            "implementation_id",
            "proof_id",
            "owner_id",
            "domain_id",
            "subject_binding_rule",
            "predicate",
            "priority_relation_to_selected",
        }
        if not mandatory.issubset(action):
            _reject(RejectCode.POLICY_INVALID, f"incomplete action {action_id}")
        if action["kind"] not in {"TERMINAL", "PRODUCER"}:
            _reject(RejectCode.POLICY_INVALID, "reject/unknown action is forbidden")
    expected_gaps = list(M23)
    for index, gap in enumerate(expected_gaps):
        action = actions[index]
        if (
            action["kind"] != "TERMINAL"
            or action.get("gap") != gap
            or action["priority_relation_to_selected"] != "PRIOR"
        ):
            _reject(RejectCode.POLICY_INVALID, f"M23 action {index} mismatch")
    selected = actions[SELECTED_PRODUCER_INDEX]
    if (
        selected["kind"] != "PRODUCER"
        or selected["action_id"] != "q1_phase_root_producer_v1"
        or selected["priority_relation_to_selected"] != "SELECTED"
    ):
        _reject(RejectCode.POLICY_INVALID, "selected producer mismatch")
    later = actions[7]
    if (
        later["kind"] != "TERMINAL"
        or later.get("gap") != LATER_GAP
        or later["priority_relation_to_selected"] != "LATER"
    ):
        _reject(RejectCode.POLICY_INVALID, "gap-31 action must be explicit later")
    if any(action["kind"] == "REJECT" for action in actions):
        _reject(RejectCode.POLICY_INVALID, "reject action in local-total policy")

    overlap = payload["priority_overlap_proof"]
    if type(overlap) is not dict or overlap.get("selected_action_id") != selected["action_id"]:
        _reject(RejectCode.PRIORITY_OVERLAP_GAP, "bad selected action in overlap proof")
    rows = overlap.get("rows")
    terminal_actions = [action for action in actions if action["kind"] == "TERMINAL"]
    if type(rows) is not list or len(rows) != len(terminal_actions):
        _reject(RejectCode.PRIORITY_OVERLAP_GAP, "overlap rows are not exhaustive")
    row_by_id = {row.get("terminal_action_id"): row for row in rows if type(row) is dict}
    if set(row_by_id) != {action["action_id"] for action in terminal_actions}:
        _reject(RejectCode.PRIORITY_OVERLAP_GAP, "terminal overlap partition mismatch")
    for action in terminal_actions:
        row = row_by_id[action["action_id"]]
        if row.get("guard_overlap") is not True:
            _reject(RejectCode.PRIORITY_OVERLAP_GAP, "all p-only terminals overlap")
        relation = row.get("coordinator_relation")
        if relation == "PRIOR":
            if not action["index"] < SELECTED_PRODUCER_INDEX:
                _reject(RejectCode.PRIORITY_OVERLAP_GAP, "prior action is not earlier")
        elif relation == "LATER":
            if not action["index"] > SELECTED_PRODUCER_INDEX:
                _reject(RejectCode.PRIORITY_OVERLAP_GAP, "later action is not later")
        else:
            _reject(RejectCode.PRIORITY_OVERLAP_GAP, "unclassified overlap")
        if relation != action["priority_relation_to_selected"]:
            _reject(RejectCode.PRIORITY_OVERLAP_GAP, "manifest/order relation mismatch")
    if overlap.get("unclassified_registered_terminal_count") != 0:
        _reject(RejectCode.PRIORITY_OVERLAP_GAP, "unclassified terminal exists")

    target_policy = payload["target_terminal_policy"]
    target_actions = target_policy.get("actions") if type(target_policy) is dict else None
    if type(target_actions) is not list or len(target_actions) != 7:
        _reject(RejectCode.POLICY_INVALID, "target terminal policy length")
    for index, gap in enumerate(M23):
        row = target_actions[index]
        if row.get("index") != index or row.get("kind") != "TERMINAL" or row.get("gap") != gap:
            _reject(RejectCode.POLICY_INVALID, "target M23 action mismatch")
    anchor = target_actions[6]
    if anchor.get("index") != 6 or anchor.get("algorithm") != "PHASE_ROOT_ANCHOR_SINK_V1":
        _reject(RejectCode.POLICY_INVALID, "target anchor-sink mismatch")

    semantics = payload["receipt_semantics"]
    exact_semantics = {
        "scope_clearance": POLICY_RELATIVE_CLEARANCE,
        "coverage": POLICY_RELATIVE_COVERAGE,
        "global_exhaustion": False,
        "miss_complete_serialization_forbidden": True,
    }
    if semantics != exact_semantics:
        _reject(RejectCode.POLICY_INVALID, "scope/global semantics mismatch")

    domain = payload["source_domain"]
    if type(domain) is not dict:
        _reject(RejectCode.POLICY_INVALID, "source domain missing")
    expected_domain_keys = {
        "domain_id",
        "owner_id",
        "initializer_id",
        "root_admission_contract_id",
        "membership_decider_id",
        "domain_predicate",
        "closed_world_kind",
    }
    if set(domain) != expected_domain_keys:
        _reject(RejectCode.POLICY_INVALID, "source domain field set")
    expected_predicate = {
        "p_is_prime": True,
        "p_equals_24t_plus_1": True,
        "q_equals_1": True,
        "X_equals_6t_plus_1": True,
        "every_prime_factor_of_X_is_1_mod_3": True,
    }
    if domain["domain_predicate"] != expected_predicate:
        _reject(RejectCode.POLICY_INVALID, "source domain predicate")
    if domain["closed_world_kind"] != "DECIDABLE_PREDICATE_CLOSED_WORLD":
        _reject(RejectCode.POLICY_INVALID, "source domain is not predicate-closed")
    totality = source_policy.get("local_totality_contract")
    if type(totality) is not dict or totality != {
        "domain": "source_domain.domain_predicate",
        "allowed_results": ["TERMINAL", "VERIFIED_SUCCESSOR"],
        "reject_allowed_for_valid_domain_member": False,
        "fallthrough_allowed": False,
        "proof_method": "STRUCTURAL_FIRST_HIT_OR_TOTAL_PRODUCER_CASE_SPLIT",
        "producer_total_after_complete_prior_miss": True,
    }:
        _reject(RejectCode.POLICY_INVALID, "local totality contract")

    return sealed(
        {
            "receipt_type": "PolicyStaticVerificationReceiptV1",
            "registry_id": payload["registry_id"],
            "source_policy_id": source_policy["policy_id"],
            "target_policy_id": target_policy["policy_id"],
            "selected_action_id": selected["action_id"],
            "selected_action_index": SELECTED_PRODUCER_INDEX,
            "registered_source_action_count": len(actions),
            "registered_terminal_count": len(terminal_actions),
            "prior_terminal_indices": list(range(6)),
            "later_terminal_indices": [7],
            "reject_action_count": 0,
            "overlap_partition_complete": True,
            "source_domain_closed_world_kind": domain["closed_world_kind"],
            "local_totality_proof_method": totality["proof_method"],
        },
        "receipt_id",
    )


def is_prime(n: int) -> bool:
    if type(n) is not int or isinstance(n, bool) or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_factorization(n: int) -> tuple[tuple[int, int], ...]:
    if type(n) is not int or isinstance(n, bool) or n < 1:
        _reject(RejectCode.SOURCE_INVALID, "factorization input")
    factors: list[tuple[int, int]] = []
    remaining = n
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def source_domain_membership(p: int) -> tuple[bool, dict[str, Any]]:
    checks: dict[str, Any] = {
        "p_is_integer": type(p) is int and not isinstance(p, bool),
        "p_is_prime": False,
        "p_equals_24t_plus_1": False,
        "q_equals_1": True,
        "X_equals_6t_plus_1": False,
        "every_prime_factor_of_X_is_1_mod_3": False,
    }
    if not checks["p_is_integer"] or p < 2:
        return False, checks
    checks["p_is_prime"] = is_prime(p)
    checks["p_equals_24t_plus_1"] = (p - 1) % 24 == 0
    if not checks["p_is_prime"] or not checks["p_equals_24t_plus_1"]:
        return False, checks
    t = (p - 1) // 24
    x_value = 6 * t + 1
    checks["X_equals_6t_plus_1"] = 4 * x_value == p + 3
    x_factors = prime_factorization(x_value)
    checks["every_prime_factor_of_X_is_1_mod_3"] = bool(x_factors) and all(
        prime % 3 == 1 for prime, _ in x_factors
    )
    return all(checks.values()), checks


def _source_wire(policy: PolicyContext, p: int) -> dict[str, Any]:
    domain = policy.payload["source_domain"]
    in_domain, domain_checks = source_domain_membership(p)
    if not in_domain:
        _reject(RejectCode.SOURCE_NOT_AUTHORIZED, f"p={p} is outside signed predicate domain")
    t = (p - 1) // 24
    x_value = 6 * t + 1
    x_factors = prime_factorization(x_value)
    return {
        "schema_id": "SP21ActualRootSourceStateV1",
        "schema_version": 1,
        "state_kind": "ROOT_SOL",
        "equation": {"numerator": 4, "denominator": p},
        "arithmetic": {
            "p": p,
            "q": 1,
            "t": t,
            "X": x_value,
            "X_prime_factorization": [[prime, exponent] for prime, exponent in x_factors],
        },
        "classification": {
            "q_class": "Q1",
            "g_class": "G",
            "major_phase": "ORDINARY",
            "ordinary": True,
        },
        "owner": {
            "owner_id": domain["owner_id"],
            "domain_id": domain["domain_id"],
        },
        "lineage": {
            "kind": "PARENTLESS_ROOT_INITIALIZER",
            "initializer_id": domain["initializer_id"],
            "root_admission_contract_id": domain["root_admission_contract_id"],
            "parent_state_id": None,
        },
        "domain_membership": {
            "membership_decider_id": domain["membership_decider_id"],
            "checks": domain_checks,
            "accepted": True,
        },
        "potential": [p, 3, 0, 0, 0, 0, 0],
    }


def _lookup_path(value: Mapping[str, Any], path: Sequence[str]) -> Any:
    current: Any = value
    for component in path:
        if type(current) is not dict or component not in current:
            _reject(RejectCode.SOURCE_BINDING_MISMATCH, f"missing occurrence path {path}")
        current = current[component]
    return current


def initialize_actual_source(
    policy: PolicyContext, authority: AuthorityContext, p: int
) -> dict[str, Any]:
    if authority.policy_payload_sha256 != policy.payload_sha256:
        _reject(RejectCode.AUTHORITY_SCOPE_MISMATCH, "authority/policy mismatch")
    wire = _source_wire(policy, p)
    state_id = digest_json(wire)
    occurrence_path = ["arithmetic", "q"]
    if _lookup_path(wire, occurrence_path) != 1:
        _reject(RejectCode.SOURCE_BINDING_MISMATCH, "q occurrence is not exact integer 1")
    return sealed(
        {
            "receipt_type": "ActualSourceReceiptV1",
            "authority_id": authority.authority_id,
            "authority_statement_sha256": authority.statement_sha256,
            "policy_payload_sha256": policy.payload_sha256,
            "initializer_id": policy.payload["source_domain"]["initializer_id"],
            "source_state_id": state_id,
            "source_state_wire": wire,
            "lineage_status": "PARENTLESS_ROOT_INITIALIZER_VERIFIED",
            "root_admission_contract_id": policy.payload["source_domain"]["root_admission_contract_id"],
            "root_admission_status": "EXTERNAL_COORDINATOR_ROOT_ADMISSION_VERIFIED",
            "source_admitted": True,
            "domain_membership_decider_id": policy.payload["source_domain"]["membership_decider_id"],
            "domain_membership_verified": True,
            "occurrence_namespace": "PERSISTENT_SOURCE_STATE_WIRE",
            "occurrence_path": occurrence_path,
            "occurrence_value": 1,
            "owner_id": wire["owner"]["owner_id"],
            "domain_id": wire["owner"]["domain_id"],
            "source_actualness": True,
            "source_admission": True,
        },
        "receipt_id",
    )


def divisors_of_square_by_factorization(n: int) -> list[int]:
    factors = prime_factorization(n)
    exponent_ranges = [range(2 * exponent + 1) for _, exponent in factors]
    values: list[int] = []
    for exponents in itertools.product(*exponent_ranges):
        value = 1
        for (prime, _), exponent in zip(factors, exponents, strict=True):
            value *= prime**exponent
        values.append(value)
    return sorted(values)


def verify_unit_fraction_certificate(p: int, triple: Sequence[int]) -> bool:
    if len(triple) != 3 or any(type(v) is not int or isinstance(v, bool) or v <= 0 for v in triple):
        return False
    x, y, z = triple
    return 4 * x * y * z == p * (x * y + x * z + y * z)


def _bradford_rows(p: int, gap: int) -> tuple[int, list[int], list[dict[str, Any]], list[dict[str, Any]]]:
    if gap <= 0 or gap % 4 != 3 or (p + gap) % 4 != 0:
        _reject(RejectCode.REPLAY_MISMATCH, f"invalid Bradford gap {gap}")
    x = (p + gap) // 4
    divisors = divisors_of_square_by_factorization(x)
    rows: list[dict[str, Any]] = []
    matches: list[dict[str, Any]] = []
    for d in divisors:
        row: dict[str, Any] = {
            "d": d,
            "type_i_congruence": (p * x + d) % gap == 0,
            "type_ii_eligible": d <= x,
            "type_ii_congruence": d <= x and (x + d) % gap == 0,
        }
        if row["type_i_congruence"]:
            y = (p * x + d) // gap
            numerator = p * x * y
            if numerator % d == 0:
                triple = [x, y, numerator // d]
                if verify_unit_fraction_certificate(p, triple):
                    matches.append({"d": d, "family": "TYPE_I", "triple": triple})
        if row["type_ii_congruence"]:
            y_numerator = p * (x + d)
            if y_numerator % gap == 0:
                y = y_numerator // gap
                numerator = x * y
                if numerator % d == 0:
                    triple = [x, y, numerator // d]
                    if verify_unit_fraction_certificate(p, triple):
                        matches.append({"d": d, "family": "TYPE_II", "triple": triple})
        rows.append(row)
    matches.sort(key=lambda item: (item["d"], 0 if item["family"] == "TYPE_I" else 1, item["triple"]))
    return x, divisors, rows, matches


def replay_bradford_action(
    *,
    p: int,
    action: Mapping[str, Any],
    subject_kind: str,
    subject_id: str,
    policy_id: str,
    policy_payload_sha256: str,
) -> dict[str, Any]:
    if action.get("kind") != "TERMINAL" or action.get("algorithm") != "BRADFORD_TYPE_I_II_EXHAUSTIVE_V1":
        _reject(RejectCode.REPLAY_MISMATCH, "not a Bradford terminal action")
    gap = action["gap"]
    x, divisors, rows, matches = _bradford_rows(p, gap)
    output: dict[str, Any] = {
        "outcome": "HIT" if matches else "MISS",
        "gap": gap,
        "x": x,
        "x_prime_factorization": [[prime, exponent] for prime, exponent in prime_factorization(x)],
        "divisor_count": len(divisors),
        "divisors_sha256": digest_json(divisors),
        "transcript_sha256": digest_json(rows),
        "match_count": len(matches),
        "matches": matches,
        "selected_certificate": matches[0] if matches else None,
    }
    if matches and not verify_unit_fraction_certificate(p, matches[0]["triple"]):
        _reject(RejectCode.TERMINAL_CERTIFICATE_INVALID, "selected Bradford certificate")
    return sealed(
        {
            "record_type": "PolicyActionReplayRecordV1",
            "subject_kind": subject_kind,
            "subject_id": subject_id,
            "policy_id": policy_id,
            "policy_payload_sha256": policy_payload_sha256,
            "action_index": action["index"],
            "action_id": action["action_id"],
            "action_contract_sha256": _action_contract_digest(action),
            "action_kind": "TERMINAL",
            "output": output,
        },
        "record_id",
    )


def replay_anchor_sink_action(
    *,
    p: int,
    r_value: int,
    k_value: int,
    action: Mapping[str, Any],
    subject_id: str,
    policy_id: str,
    policy_payload_sha256: str,
) -> dict[str, Any]:
    if action.get("algorithm") != "PHASE_ROOT_ANCHOR_SINK_V1":
        _reject(RejectCode.REPLAY_MISMATCH, "not anchor-sink action")
    divisor = r_value - 1
    hit = divisor > 0 and k_value % divisor == 0
    certificate = None
    if hit:
        certificate = [k_value // divisor, k_value, p * k_value]
        if not verify_unit_fraction_certificate(p, certificate):
            _reject(RejectCode.TERMINAL_CERTIFICATE_INVALID, "anchor-sink certificate")
    output = {
        "outcome": "HIT" if hit else "MISS",
        "predicate": "R_MINUS_1_DIVIDES_K",
        "R_minus_1": divisor,
        "K": k_value,
        "gcd_R_minus_1_K": gcd(divisor, k_value),
        "selected_certificate": certificate,
    }
    return sealed(
        {
            "record_type": "PolicyActionReplayRecordV1",
            "subject_kind": "TARGET_PROJECTION",
            "subject_id": subject_id,
            "policy_id": policy_id,
            "policy_payload_sha256": policy_payload_sha256,
            "action_index": action["index"],
            "action_id": action["action_id"],
            "action_contract_sha256": _action_contract_digest(action),
            "action_kind": "TERMINAL",
            "output": output,
        },
        "record_id",
    )


def make_scope_clearance(
    *,
    source_receipt: Mapping[str, Any],
    policy: PolicyContext,
    prior_records: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    source_policy = policy.payload["source_policy"]
    expected_actions = source_policy["actions"][:SELECTED_PRODUCER_INDEX]
    if len(prior_records) != len(expected_actions):
        _reject(RejectCode.CLEARANCE_INVALID, "prior record count")
    for index, (record, action) in enumerate(zip(prior_records, expected_actions, strict=True)):
        verify_seal(record, "record_id", RejectCode.CLEARANCE_INVALID)
        if (
            record["subject_id"] != source_receipt["source_state_id"]
            or record["policy_payload_sha256"] != policy.payload_sha256
            or record["policy_id"] != source_policy["policy_id"]
            or record["action_index"] != index
            or record["action_id"] != action["action_id"]
            or record["output"]["outcome"] != "MISS"
        ):
            _reject(RejectCode.CLEARANCE_INVALID, f"prior record {index}")
    return sealed(
        {
            "receipt_type": "ScopeBoundPriorClearanceReceiptV1",
            "semantic": POLICY_RELATIVE_CLEARANCE,
            "coverage": POLICY_RELATIVE_COVERAGE,
            "global_exhaustion": False,
            "source_state_id": source_receipt["source_state_id"],
            "actual_source_receipt_id": source_receipt["receipt_id"],
            "policy_id": source_policy["policy_id"],
            "policy_payload_sha256": policy.payload_sha256,
            "selected_action_index": SELECTED_PRODUCER_INDEX,
            "selected_action_id": source_policy["actions"][SELECTED_PRODUCER_INDEX]["action_id"],
            "covered_action_indices": list(range(SELECTED_PRODUCER_INDEX)),
            "prior_record_ids": [record["record_id"] for record in prior_records],
            "prior_trace_sha256": digest_json(list(prior_records)),
            "miss_complete_serialization_forbidden": True,
        },
        "receipt_id",
    )


def _producer_guard(
    *, source_receipt: Mapping[str, Any], clearance: Mapping[str, Any], policy: PolicyContext
) -> dict[str, Any]:
    verify_seal(source_receipt, "receipt_id", RejectCode.SOURCE_BINDING_MISMATCH)
    verify_seal(clearance, "receipt_id", RejectCode.CLEARANCE_INVALID)
    source = source_receipt["source_state_wire"]
    action = policy.payload["source_policy"]["actions"][SELECTED_PRODUCER_INDEX]
    checks = {
        "actual_source": source_receipt["source_actualness"] is True,
        "admitted_source": (
            source_receipt.get("source_admitted") is True
            and source_receipt.get("source_admission") is True
        ),
        "domain_membership": source_receipt.get("domain_membership_verified") is True,
        "source_policy_binding": clearance["source_state_id"] == source_receipt["source_state_id"],
        "policy_digest_binding": clearance["policy_payload_sha256"] == policy.payload_sha256,
        "complete_prior_indices": clearance["covered_action_indices"] == list(range(6)),
        "scope_not_global": clearance["global_exhaustion"] is False,
        "q_occurrence": _lookup_path(source, ["arithmetic", "q"]) == 1,
        "ordinary_q1_g": source["classification"] == {
            "q_class": "Q1",
            "g_class": "G",
            "major_phase": "ORDINARY",
            "ordinary": True,
        },
        "owner_domain": (
            source["owner"]["owner_id"] == action["owner_id"]
            and source["owner"]["domain_id"] == action["domain_id"]
        ),
    }
    outcome = "GUARD_TRUE" if all(checks.values()) else "GUARD_FALSE"
    return sealed(
        {
            "record_type": "ProducerGuardReplayRecordV1",
            "subject_id": source_receipt["source_state_id"],
            "policy_id": policy.payload["source_policy"]["policy_id"],
            "policy_payload_sha256": policy.payload_sha256,
            "action_index": SELECTED_PRODUCER_INDEX,
            "action_id": action["action_id"],
            "action_contract_sha256": _action_contract_digest(action),
            "checks": checks,
            "outcome": outcome,
        },
        "record_id",
    )


def project_phase_root(source_wire: Mapping[str, Any]) -> dict[str, Any]:
    arithmetic = source_wire["arithmetic"]
    p = arithmetic["p"]
    t = arithmetic["t"]
    x_value = arithmetic["X"]
    r_value = 16 * t + 3
    k_value = x_value * (16 * t + 1)
    if 4 * k_value != p * r_value + 1:
        _reject(RejectCode.TARGET_INVALID, "4K=pR+1 failed")
    payload = {
        "object_type": "Q1PhaseRootPureProjectionV1",
        "formula_id": "R_16T_PLUS_3__K_X_TIMES_16T_PLUS_1_V1",
        "p": p,
        "t": t,
        "X": x_value,
        "R": r_value,
        "K": k_value,
        "A": 1,
        "identity_4K_equals_pR_plus_1": True,
        "caller_supplied_tie_break": False,
        "contains_source_state_id": False,
        "contains_owner": False,
        "contains_admission": False,
    }
    return sealed(payload, "projection_id")


def target_preclassification(projection: Mapping[str, Any], policy: PolicyContext) -> dict[str, Any]:
    verify_seal(projection, "projection_id", RejectCode.TARGET_INVALID)
    owner_registry = policy.payload["owner_registry"]
    checks = {
        "A_is_one": projection["A"] == 1,
        "four_k_identity": 4 * projection["K"] == projection["p"] * projection["R"] + 1,
        "X_divides_K": projection["K"] % projection["X"] == 0,
        "R_range": 3 <= projection["R"] <= projection["p"] - 2,
        "normal_form": True,
    }
    if not all(checks.values()):
        _reject(RejectCode.TARGET_INVALID, "target preclassification failed")
    return sealed(
        {
            "object_type": "TargetPredicatePreclassificationV1",
            "projection_id": projection["projection_id"],
            "checks": checks,
            "unique_owner_id": owner_registry["target_owner_id"],
            "owner_precedence_index": owner_registry["target_owner_precedence_index"],
            "predicate_match_count": 1,
            "authority_status": "NON_AUTHORIZING_PRECLASSIFICATION",
        },
        "preclassification_id",
    )


def replay_target_terminal_policy(
    *,
    projection: Mapping[str, Any],
    source_state_id: str,
    policy: PolicyContext,
) -> dict[str, Any]:
    target_policy = policy.payload["target_terminal_policy"]
    records: list[dict[str, Any]] = []
    for action in target_policy["actions"]:
        if action["algorithm"] == "BRADFORD_TYPE_I_II_EXHAUSTIVE_V1":
            record = replay_bradford_action(
                p=projection["p"],
                action=action,
                subject_kind="TARGET_PROJECTION",
                subject_id=projection["projection_id"],
                policy_id=target_policy["policy_id"],
                policy_payload_sha256=policy.payload_sha256,
            )
        else:
            record = replay_anchor_sink_action(
                p=projection["p"],
                r_value=projection["R"],
                k_value=projection["K"],
                action=action,
                subject_id=projection["projection_id"],
                policy_id=target_policy["policy_id"],
                policy_payload_sha256=policy.payload_sha256,
            )
        records.append(record)
        if record["output"]["outcome"] == "HIT":
            return sealed(
                {
                    "receipt_type": "TargetTerminalDecisionReceiptV1",
                    "source_state_id": source_state_id,
                    "target_projection_id": projection["projection_id"],
                    "target_policy_id": target_policy["policy_id"],
                    "policy_payload_sha256": policy.payload_sha256,
                    "outcome": "HIT_LIFT_TO_SOURCE_TERMINAL",
                    "global_exhaustion": False,
                    "records": records,
                    "terminal_certificate": record["output"]["selected_certificate"],
                    "lift": "IDENTITY_ON_UNIT_FRACTION_TRIPLES",
                },
                "receipt_id",
            )
    return sealed(
        {
            "receipt_type": "TargetTerminalDecisionReceiptV1",
            "source_state_id": source_state_id,
            "target_projection_id": projection["projection_id"],
            "target_policy_id": target_policy["policy_id"],
            "policy_payload_sha256": policy.payload_sha256,
            "outcome": "MISS_REGISTERED_TARGET_PRIORITY_COMPLETE",
            "coverage": "REGISTERED_TARGET_ACTIONS_ONLY",
            "global_exhaustion": False,
            "records": records,
            "terminal_certificate": None,
            "lift": None,
        },
        "receipt_id",
    )


def potential_draft(source_wire: Mapping[str, Any], projection: Mapping[str, Any]) -> dict[str, Any]:
    p = source_wire["arithmetic"]["p"]
    source_potential = [p, 3, 0, 0, 0, 0, 0]
    target_potential = [p, 2, 4, (p - 1) ** 2 // 4, projection["K"], 0, 0]
    if not tuple(target_potential) < tuple(source_potential):
        _reject(RejectCode.EDGE_INVALID, "T5 lexicographic decrease failed")
    return sealed(
        {
            "object_type": "T5PotentialDraftV1",
            "evaluator_id": "t5_frozen_n7_phase_drop_v1",
            "projection_id": projection["projection_id"],
            "source_potential": source_potential,
            "target_potential": target_potential,
            "comparison": "LEX_STRICT_DECREASE",
            "ticket_kind": "PHASE_DROP",
        },
        "draft_id",
    )


def edge_anchor(
    *,
    source_receipt: Mapping[str, Any],
    clearance: Mapping[str, Any],
    projection: Mapping[str, Any],
    preclassification: Mapping[str, Any],
    target_terminal: Mapping[str, Any],
    potential: Mapping[str, Any],
    policy: PolicyContext,
) -> dict[str, Any]:
    return sealed(
        {
            "object_type": "SP22EdgeAnchorV1",
            "source_state_id": source_receipt["source_state_id"],
            "actual_source_receipt_id": source_receipt["receipt_id"],
            "clearance_receipt_id": clearance["receipt_id"],
            "policy_payload_sha256": policy.payload_sha256,
            "selected_action_index": SELECTED_PRODUCER_INDEX,
            "selected_action_id": policy.payload["source_policy"]["actions"][6]["action_id"],
            "projection_id": projection["projection_id"],
            "preclassification_id": preclassification["preclassification_id"],
            "target_terminal_receipt_id": target_terminal["receipt_id"],
            "potential_draft_id": potential["draft_id"],
        },
        "edge_anchor_id",
    )


def make_target_prestate(
    projection: Mapping[str, Any], anchor: Mapping[str, Any]
) -> tuple[dict[str, Any], str]:
    prestate = {
        "schema_id": "SP22PhaseRootSemanticPrestateV1",
        "schema_version": 1,
        "state_kind": "ROOT_SOL",
        "equation": {"numerator": 4, "denominator": projection["p"]},
        "arithmetic": {
            "p": projection["p"],
            "R": projection["R"],
            "K": projection["K"],
            "A": 1,
        },
        "normal_form": {
            "major_phase": "TYPEI",
            "protocol": "CHARGED",
            "carrier": "FULL_CARRIER_POST_G",
            "full_carrier_scope": True,
            "support_A": 1,
            "is_overflow": False,
        },
        "upstream_edge_anchor_id": anchor["edge_anchor_id"],
        "potential": [
            projection["p"],
            2,
            4,
            (projection["p"] - 1) ** 2 // 4,
            projection["K"],
            0,
            0,
        ],
    }
    forbidden = {"owner", "owner_digest", "edge_bundle", "bundle_id", "admission", "admission_id"}
    if forbidden.intersection(prestate):
        _reject(RejectCode.TARGET_INVALID, "cyclic field in semantic prestate")
    return prestate, digest_json(prestate)


def classify_target_owner(
    target_prestate: Mapping[str, Any], target_state_id: str, policy: PolicyContext
) -> dict[str, Any]:
    if digest_json(target_prestate) != target_state_id:
        _reject(RejectCode.TARGET_INVALID, "target state ID mismatch")
    registry = policy.payload["owner_registry"]
    normal = target_prestate["normal_form"]
    if normal != {
        "major_phase": "TYPEI",
        "protocol": "CHARGED",
        "carrier": "FULL_CARRIER_POST_G",
        "full_carrier_scope": True,
        "support_A": 1,
        "is_overflow": False,
    }:
        _reject(RejectCode.TARGET_INVALID, "target normal form")
    return sealed(
        {
            "receipt_type": "CommonOwnerReceiptV1",
            "classifier_id": registry["classifier_id"],
            "target_state_id": target_state_id,
            "owner_id": registry["target_owner_id"],
            "domain_id": registry["target_domain_id"],
            "owner_precedence_index": registry["target_owner_precedence_index"],
            "route_id": registry["target_route_id"],
            "body_id": registry["target_body_id"],
            "predicate_match_count": 1,
            "owner_recomputed_not_inherited": True,
        },
        "receipt_id",
    )


def _make_e_receipt(kind: str, payload: Mapping[str, Any]) -> dict[str, Any]:
    return sealed({"receipt_type": kind, **_json_copy(dict(payload))}, "receipt_id")


def build_edge_bundle(
    *,
    source_receipt: Mapping[str, Any],
    clearance: Mapping[str, Any],
    guard_record: Mapping[str, Any],
    projection: Mapping[str, Any],
    preclassification: Mapping[str, Any],
    target_terminal: Mapping[str, Any],
    potential: Mapping[str, Any],
    anchor: Mapping[str, Any],
    target_prestate: Mapping[str, Any],
    target_state_id: str,
    owner: Mapping[str, Any],
    policy: PolicyContext,
    authority: AuthorityContext,
) -> dict[str, Any]:
    source = source_receipt["source_state_wire"]
    selected_action = policy.payload["source_policy"]["actions"][6]
    e1 = _make_e_receipt(
        "E1ActualOccurrenceReceiptV1",
        {
            "authority_id": authority.authority_id,
            "authority_statement_sha256": authority.statement_sha256,
            "source_state_id": source_receipt["source_state_id"],
            "actual_source_receipt_id": source_receipt["receipt_id"],
            "lineage_status": source_receipt["lineage_status"],
            "occurrence_namespace": source_receipt["occurrence_namespace"],
            "occurrence_path": source_receipt["occurrence_path"],
            "occurrence_value": source_receipt["occurrence_value"],
            "policy_payload_sha256": policy.payload_sha256,
            "clearance_receipt_id": clearance["receipt_id"],
            "complete_prior_trace_sha256": clearance["prior_trace_sha256"],
            "selected_branch_index": 6,
            "selected_branch_id": selected_action["action_id"],
            "guard_record_id": guard_record["record_id"],
            "owner_id": source["owner"]["owner_id"],
            "domain_id": source["owner"]["domain_id"],
        },
    )
    e2 = _make_e_receipt(
        "E2UniqueProjectionReceiptV1",
        {
            "source_state_id": source_receipt["source_state_id"],
            "projection_id": projection["projection_id"],
            "target_state_id": target_state_id,
            "formula_id": projection["formula_id"],
            "inputs": {"p": projection["p"], "t": projection["t"], "X": projection["X"]},
            "outputs": {"R": projection["R"], "K": projection["K"], "A": 1},
            "identity_4K_equals_pR_plus_1": True,
            "caller_supplied_tie_break": False,
            "projection_unique": True,
        },
    )
    e3 = _make_e_receipt(
        "E3CommonTargetAdmissionPredicateReceiptV1",
        {
            "target_state_id": target_state_id,
            "target_schema_id": target_prestate["schema_id"],
            "preclassification_id": preclassification["preclassification_id"],
            "target_terminal_receipt_id": target_terminal["receipt_id"],
            "target_terminal_outcome": target_terminal["outcome"],
            "owner_receipt_id": owner["receipt_id"],
            "owner_id": owner["owner_id"],
            "domain_id": owner["domain_id"],
            "normal_form": target_prestate["normal_form"],
            "admission_gate_id": policy.payload["admission_contract"]["admission_gate_id"],
            "schema_valid": True,
            "grammar_valid": True,
            "owner_recomputed": True,
            "registered_target_priority_clear": target_terminal["outcome"]
            == "MISS_REGISTERED_TARGET_PRIORITY_COMPLETE",
        },
    )
    source_equation = source["equation"]
    target_equation = target_prestate["equation"]
    if source_equation != target_equation:
        _reject(RejectCode.EDGE_INVALID, "E4 equation interfaces differ")
    e4 = _make_e_receipt(
        "E4UniversalIdentityLiftReceiptV1",
        {
            "source_state_id": source_receipt["source_state_id"],
            "target_state_id": target_state_id,
            "source_equation": source_equation,
            "target_equation": target_equation,
            "lift_id": "IDENTITY_ON_POSITIVE_INTEGER_TRIPLES_V1",
            "definition": "Lambda(x,y,z)=(x,y,z)",
            "proof_rule": "DEFINITIONAL_EQUALITY_OF_SOLUTION_PREDICATES",
            "universal_quantifier": True,
        },
    )
    if potential["source_potential"] != source["potential"] or potential["target_potential"] != target_prestate["potential"]:
        _reject(RejectCode.EDGE_INVALID, "E5 parent/final potential binding")
    e5 = _make_e_receipt(
        "E5FrozenPotentialReceiptV1",
        {
            "source_state_id": source_receipt["source_state_id"],
            "target_state_id": target_state_id,
            "potential_draft_id": potential["draft_id"],
            "evaluator_id": potential["evaluator_id"],
            "source_potential": potential["source_potential"],
            "target_potential": potential["target_potential"],
            "comparison": "LEX_STRICT_DECREASE",
            "first_strict_coordinate": 1,
            "ticket_kind": "PHASE_DROP",
        },
    )
    route = policy.payload["owner_registry"]
    r_receipt = _make_e_receipt(
        "RRegisteredReentryReceiptV1",
        {
            "target_state_id": target_state_id,
            "owner_receipt_id": owner["receipt_id"],
            "owner_id": owner["owner_id"],
            "route_id": route["target_route_id"],
            "body_id": route["target_body_id"],
            "selector_runtime_id": policy.payload["admission_contract"]["selector_runtime_id"],
            "persistent_state_universe": "T6_PHASE_ROOT_PRESTATE_V1",
            "route_registered": True,
            "reentry_consumable": True,
            "self_edge_authorized": False,
        },
    )
    return sealed(
        {
            "bundle_type": "SP22IndependentE1E5RBundleV1",
            "edge_anchor_id": anchor["edge_anchor_id"],
            "source_state_id": source_receipt["source_state_id"],
            "target_state_id": target_state_id,
            "policy_payload_sha256": policy.payload_sha256,
            "authority_statement_sha256": authority.statement_sha256,
            "E1": e1,
            "E2": e2,
            "E3": e3,
            "E4": e4,
            "E5": e5,
            "R": r_receipt,
            "all_obligations_verified": True,
        },
        "bundle_id",
    )


_RUNTIME_FACTORY = object()
_ADMISSION_CAPABILITY = object()


class PersistentPilotRuntime:
    """Factory-only runtime with one ingress writer and one registered route."""

    __slots__ = ("_policy", "_authority", "_queue", "_used_tokens", "_trace")

    def __init__(self, token: object, policy: PolicyContext, authority: AuthorityContext):
        if token is not _RUNTIME_FACTORY:
            _reject(RejectCode.QUEUE_BYPASS, "runtime is factory-only")
        self._policy = policy
        self._authority = authority
        self._queue: tuple[dict[str, Any], ...] = ()
        self._used_tokens: frozenset[str] = frozenset()
        self._trace: tuple[dict[str, Any], ...] = ()

    @classmethod
    def open(cls, policy: PolicyContext, authority: AuthorityContext) -> "PersistentPilotRuntime":
        return cls(_RUNTIME_FACTORY, policy, authority)

    def queue_snapshot(self) -> tuple[dict[str, Any], ...]:
        return tuple(_json_copy(item) for item in self._queue)

    def trace_snapshot(self) -> tuple[dict[str, Any], ...]:
        return tuple(_json_copy(item) for item in self._trace)

    def _record(self, row: Mapping[str, Any]) -> None:
        self._trace = self._trace + (_json_copy(dict(row)),)

    def _unique_queue_write_v1(self, capability: object, envelope: Mapping[str, Any]) -> None:
        if capability is not _ADMISSION_CAPABILITY:
            _reject(RejectCode.QUEUE_BYPASS, "queue ingress requires common-admission capability")
        token = envelope["admission_sidecar"]["queue_token"]
        if token in self._used_tokens:
            _reject(RejectCode.DUPLICATE_QUEUE_TOKEN, token)
        self._queue = self._queue + (_json_copy(dict(envelope)),)
        self._used_tokens = self._used_tokens | {token}
        self._record(
            {
                "event": "QUEUE_INGRESS_WRITE",
                "writer_id": self._policy.payload["admission_contract"]["unique_queue_writer_id"],
                "queue_token": token,
                "target_state_id": envelope["target_state_id"],
            }
        )

    def consume_and_reenter_v1(self) -> dict[str, Any]:
        if not self._queue:
            _reject(RejectCode.REENTRY_REJECTED, "empty queue")
        envelope = self._queue[0]
        self._queue = self._queue[1:]
        owner = envelope["owner_receipt"]
        registry = self._policy.payload["owner_registry"]
        if (
            owner["owner_id"] != registry["target_owner_id"]
            or owner["route_id"] != registry["target_route_id"]
            or owner["body_id"] != registry["target_body_id"]
        ):
            _reject(RejectCode.REENTRY_REJECTED, "unregistered target route")
        receipt = sealed(
            {
                "receipt_type": "ActualReentryReceiptV1",
                "target_state_id": envelope["target_state_id"],
                "admission_id": envelope["admission_sidecar"]["admission_id"],
                "queue_token": envelope["admission_sidecar"]["queue_token"],
                "selector_runtime_id": self._policy.payload["admission_contract"]["selector_runtime_id"],
                "route_id": owner["route_id"],
                "body_id": owner["body_id"],
                "result": "ENTERED_TYPE_I_FULL_CARRIER_POST_G_BODY",
                "self_edge_emitted": False,
                "queue_write_during_reentry": False,
            },
            "receipt_id",
        )
        self._record(
            {
                "event": "QUEUE_CONSUME_AND_REENTRY",
                "route_id": owner["route_id"],
                "body_id": owner["body_id"],
                "target_state_id": envelope["target_state_id"],
            }
        )
        return receipt


def _verify_edge_bundle_for_admission(
    *,
    bundle: Mapping[str, Any],
    target_prestate: Mapping[str, Any],
    target_state_id: str,
    owner: Mapping[str, Any],
    target_terminal: Mapping[str, Any],
    policy: PolicyContext,
    authority: AuthorityContext,
) -> None:
    verify_seal(bundle, "bundle_id", RejectCode.EDGE_INVALID)
    if bundle["all_obligations_verified"] is not True:
        _reject(RejectCode.EDGE_INVALID, "bundle completion")
    for key in ("E1", "E2", "E3", "E4", "E5", "R"):
        verify_seal(bundle[key], "receipt_id", RejectCode.EDGE_INVALID)
    if (
        bundle["target_state_id"] != target_state_id
        or digest_json(target_prestate) != target_state_id
        or bundle["policy_payload_sha256"] != policy.payload_sha256
        or bundle["authority_statement_sha256"] != authority.statement_sha256
    ):
        _reject(RejectCode.EDGE_INVALID, "bundle target/policy/authority binding")
    if bundle["E1"]["selected_branch_index"] != SELECTED_PRODUCER_INDEX:
        _reject(RejectCode.EDGE_INVALID, "E1 branch index")
    if bundle["E2"]["target_state_id"] != target_state_id or bundle["E2"]["projection_unique"] is not True:
        _reject(RejectCode.EDGE_INVALID, "E2")
    if (
        bundle["E3"]["owner_receipt_id"] != owner["receipt_id"]
        or bundle["E3"]["target_terminal_receipt_id"] != target_terminal["receipt_id"]
        or bundle["E3"]["registered_target_priority_clear"] is not True
    ):
        _reject(RejectCode.EDGE_INVALID, "E3")
    if bundle["E4"]["source_equation"] != bundle["E4"]["target_equation"]:
        _reject(RejectCode.EDGE_INVALID, "E4")
    if not tuple(bundle["E5"]["target_potential"]) < tuple(bundle["E5"]["source_potential"]):
        _reject(RejectCode.EDGE_INVALID, "E5")
    if bundle["R"]["route_registered"] is not True or bundle["R"]["self_edge_authorized"] is not False:
        _reject(RejectCode.EDGE_INVALID, "R")


def common_admit_v1(
    runtime: PersistentPilotRuntime,
    *,
    target_prestate: Mapping[str, Any],
    target_state_id: str,
    owner: Mapping[str, Any],
    target_terminal: Mapping[str, Any],
    bundle: Mapping[str, Any],
) -> dict[str, Any]:
    policy = runtime._policy
    authority = runtime._authority
    _verify_edge_bundle_for_admission(
        bundle=bundle,
        target_prestate=target_prestate,
        target_state_id=target_state_id,
        owner=owner,
        target_terminal=target_terminal,
        policy=policy,
        authority=authority,
    )
    admission_contract = policy.payload["admission_contract"]
    token_preimage = {
        "source_state_id": bundle["source_state_id"],
        "target_state_id": target_state_id,
        "bundle_id": bundle["bundle_id"],
        "owner_receipt_id": owner["receipt_id"],
        "authority_statement_sha256": authority.statement_sha256,
        "admission_gate_id": admission_contract["admission_gate_id"],
        "one_time_sequence": 0,
    }
    queue_token = digest_json(token_preimage)
    sidecar = sealed(
        {
            "receipt_type": "CommonAdmissionSidecarV1",
            "admission_gate_id": admission_contract["admission_gate_id"],
            "projector_id": admission_contract["projector_id"],
            "classifier_id": admission_contract["classifier_id"],
            "unique_queue_writer_id": admission_contract["unique_queue_writer_id"],
            "source_state_id": bundle["source_state_id"],
            "target_state_id": target_state_id,
            "owner_receipt_id": owner["receipt_id"],
            "bundle_id": bundle["bundle_id"],
            "target_terminal_receipt_id": target_terminal["receipt_id"],
            "queue_token": queue_token,
            "one_time_sequence": 0,
            "admitted": True,
        },
        "admission_id",
    )
    envelope = {
        "envelope_type": "AdmittedPersistentTargetEnvelopeV1",
        "target_state_id": target_state_id,
        "target_prestate": _json_copy(target_prestate),
        "owner_receipt": _json_copy(owner),
        "edge_bundle": _json_copy(bundle),
        "admission_sidecar": sidecar,
    }
    runtime._unique_queue_write_v1(_ADMISSION_CAPABILITY, envelope)
    return sidecar


def static_queue_ingress_audit(module_path: Path) -> dict[str, Any]:
    try:
        tree = ast.parse(module_path.read_text(encoding="utf-8"), filename=str(module_path))
    except (OSError, SyntaxError) as exc:
        _reject(RejectCode.QUEUE_BYPASS, f"cannot audit runtime source: {exc}")
    ingress_writers: list[str] = []
    queue_stores: list[dict[str, Any]] = []
    function_stack: list[str] = []

    class Visitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            function_stack.append(node.name)
            if node.name == "_unique_queue_write_v1":
                ingress_writers.append(node.name)
            self.generic_visit(node)
            function_stack.pop()

        def visit_Assign(self, node: ast.Assign) -> None:
            for target in node.targets:
                if isinstance(target, ast.Attribute) and target.attr == "_queue":
                    queue_stores.append(
                        {
                            "function": function_stack[-1] if function_stack else "<module>",
                            "line": node.lineno,
                        }
                    )
            self.generic_visit(node)

        def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
            target = node.target
            if isinstance(target, ast.Attribute) and target.attr == "_queue":
                queue_stores.append(
                    {
                        "function": function_stack[-1] if function_stack else "<module>",
                        "line": node.lineno,
                    }
                )
            self.generic_visit(node)

    Visitor().visit(tree)
    store_functions = {row["function"] for row in queue_stores}
    allowed = {"__init__", "_unique_queue_write_v1", "consume_and_reenter_v1"}
    if ingress_writers != ["_unique_queue_write_v1"] or not store_functions.issubset(allowed):
        _reject(RejectCode.QUEUE_BYPASS, "unexpected queue mutation site")
    return sealed(
        {
            "receipt_type": "StaticQueueIngressAuditReceiptV1",
            "module_id": MODULE_ID,
            "module_sha256": digest_bytes(module_path.read_bytes()),
            "unique_ingress_writer": "_unique_queue_write_v1",
            "queue_store_sites": queue_stores,
            "allowed_store_functions": sorted(allowed),
            "public_enqueue_surface": False,
            "audit_pass": True,
        },
        "receipt_id",
    )


def build_verified_edge(
    *,
    source_receipt: Mapping[str, Any],
    clearance: Mapping[str, Any],
    guard_record: Mapping[str, Any],
    policy: PolicyContext,
    authority: AuthorityContext,
    runtime: PersistentPilotRuntime,
) -> dict[str, Any]:
    if guard_record["outcome"] != "GUARD_TRUE":
        _reject(RejectCode.PRODUCER_GUARD_FALSE, "selected phase-root guard")
    projection = project_phase_root(source_receipt["source_state_wire"])
    preclassification = target_preclassification(projection, policy)
    target_terminal = replay_target_terminal_policy(
        projection=projection,
        source_state_id=source_receipt["source_state_id"],
        policy=policy,
    )
    if target_terminal["outcome"] != "MISS_REGISTERED_TARGET_PRIORITY_COMPLETE":
        _reject(RejectCode.TARGET_TERMINAL_HIT, "target terminal must lift to source")
    potential = potential_draft(source_receipt["source_state_wire"], projection)
    anchor = edge_anchor(
        source_receipt=source_receipt,
        clearance=clearance,
        projection=projection,
        preclassification=preclassification,
        target_terminal=target_terminal,
        potential=potential,
        policy=policy,
    )
    target_prestate, target_state_id = make_target_prestate(projection, anchor)
    owner = classify_target_owner(target_prestate, target_state_id, policy)
    bundle = build_edge_bundle(
        source_receipt=source_receipt,
        clearance=clearance,
        guard_record=guard_record,
        projection=projection,
        preclassification=preclassification,
        target_terminal=target_terminal,
        potential=potential,
        anchor=anchor,
        target_prestate=target_prestate,
        target_state_id=target_state_id,
        owner=owner,
        policy=policy,
        authority=authority,
    )
    sidecar = common_admit_v1(
        runtime,
        target_prestate=target_prestate,
        target_state_id=target_state_id,
        owner=owner,
        target_terminal=target_terminal,
        bundle=bundle,
    )
    reentry = runtime.consume_and_reenter_v1()
    return {
        "result_kind": "VERIFIED_SUCCESSOR",
        "projection": projection,
        "preclassification": preclassification,
        "target_terminal_receipt": target_terminal,
        "potential_draft": potential,
        "edge_anchor": anchor,
        "target_prestate": target_prestate,
        "target_state_id": target_state_id,
        "owner_receipt": owner,
        "edge_bundle": bundle,
        "admission_sidecar": sidecar,
        "reentry_receipt": reentry,
        "runtime_trace": list(runtime.trace_snapshot()),
        "queue_empty_after_reentry": runtime.queue_snapshot() == (),
    }


def run_selector_for_p(
    *, policy: PolicyContext, authority: AuthorityContext, p: int
) -> dict[str, Any]:
    source_receipt = initialize_actual_source(policy, authority, p)
    source_policy = policy.payload["source_policy"]
    records: list[dict[str, Any]] = []
    for action in source_policy["actions"]:
        if action["kind"] == "TERMINAL":
            record = replay_bradford_action(
                p=p,
                action=action,
                subject_kind="SOURCE_STATE",
                subject_id=source_receipt["source_state_id"],
                policy_id=source_policy["policy_id"],
                policy_payload_sha256=policy.payload_sha256,
            )
            records.append(record)
            if record["output"]["outcome"] == "HIT":
                certificate = record["output"]["selected_certificate"]["triple"]
                if not verify_unit_fraction_certificate(p, certificate):
                    _reject(RejectCode.TERMINAL_CERTIFICATE_INVALID, f"p={p}")
                return {
                    "result_kind": "TERMINAL",
                    "p": p,
                    "actual_source_receipt": source_receipt,
                    "selector_trace": records,
                    "selected_action_index": action["index"],
                    "selected_action_id": action["action_id"],
                    "terminal_certificate": record["output"]["selected_certificate"],
                }
            continue
        if action["kind"] == "PRODUCER":
            clearance = make_scope_clearance(
                source_receipt=source_receipt,
                policy=policy,
                prior_records=records,
            )
            guard_record = _producer_guard(
                source_receipt=source_receipt, clearance=clearance, policy=policy
            )
            records.append(guard_record)
            if guard_record["outcome"] == "GUARD_FALSE":
                _reject(
                    RejectCode.PRODUCER_GUARD_FALSE,
                    "valid domain source reached total producer with false guard",
                )
            runtime = PersistentPilotRuntime.open(policy, authority)
            edge = build_verified_edge(
                source_receipt=source_receipt,
                clearance=clearance,
                guard_record=guard_record,
                policy=policy,
                authority=authority,
                runtime=runtime,
            )
            return {
                "result_kind": "VERIFIED_SUCCESSOR",
                "p": p,
                "actual_source_receipt": source_receipt,
                "selector_trace": records,
                "selected_action_index": action["index"],
                "selected_action_id": action["action_id"],
                "clearance_receipt": clearance,
                **edge,
            }
        _reject(RejectCode.POLICY_INVALID, "unknown action kind")
    _reject(RejectCode.LOCAL_TOTALITY_FAILED, f"policy fell through for p={p}")


def summarize_selector_result(result: Mapping[str, Any]) -> dict[str, Any]:
    base = {
        "p": result["p"],
        "source_state_id": result["actual_source_receipt"]["source_state_id"],
        "actual_source_receipt_id": result["actual_source_receipt"]["receipt_id"],
        "result_kind": result["result_kind"],
        "selected_action_index": result["selected_action_index"],
        "selected_action_id": result["selected_action_id"],
    }
    if result["result_kind"] == "TERMINAL":
        base["terminal_certificate"] = result["terminal_certificate"]
    else:
        base.update(
            {
                "clearance_receipt_id": result["clearance_receipt"]["receipt_id"],
                "target_state_id": result["target_state_id"],
                "edge_bundle_id": result["edge_bundle"]["bundle_id"],
                "admission_id": result["admission_sidecar"]["admission_id"],
                "reentry_receipt_id": result["reentry_receipt"]["receipt_id"],
            }
        )
    return base


def prove_universal_local_totality(policy: PolicyContext) -> dict[str, Any]:
    """Check the finite policy skeleton used by the universal case split.

    The quantified proof is mathematical: every fixed-gap divisor screen
    enumerates a finite divisor set and returns HIT or MISS; the first HIT
    terminates; after six MISS records the selected producer guard is true on
    every predicate-domain source; the producer edge proof is uniform in p.
    This receipt records the mechanically checkable policy premises rather
    than pretending that an infinite domain was exhaustively executed.
    """
    source_policy = policy.payload["source_policy"]
    actions = source_policy["actions"]
    prior = actions[:SELECTED_PRODUCER_INDEX]
    selected = actions[SELECTED_PRODUCER_INDEX]
    checks = {
        "domain_is_decidable_predicate_closed_world": (
            policy.payload["source_domain"]["closed_world_kind"]
            == "DECIDABLE_PREDICATE_CLOSED_WORLD"
        ),
        "policy_is_finite": len(actions) == 8,
        "all_prior_actions_are_total_terminals": all(
            action["kind"] == "TERMINAL"
            and action["predicate"].get("total_on_domain") is True
            for action in prior
        ),
        "all_prior_replays_have_binary_hit_miss_codomain": all(
            action["algorithm"] == "BRADFORD_TYPE_I_II_EXHAUSTIVE_V1"
            for action in prior
        ),
        "selected_action_is_total_producer_after_prior_miss": (
            selected["kind"] == "PRODUCER"
            and selected["predicate"].get("total_after_prior_miss_on_domain") is True
        ),
        "no_reject_action": all(action["kind"] != "REJECT" for action in actions),
        "no_fallthrough_after_prior_miss": selected["index"] == SELECTED_PRODUCER_INDEX,
        "target_m23_transport_is_p_only": all(
            action["predicate"].get("kind") == "P_ONLY_FIXED_GAP_DIVISOR_SCREEN"
            for action in policy.payload["target_terminal_policy"]["actions"][:6]
        ),
        "anchor_sink_uniform_miss_proof_registered": (
            policy.payload["target_terminal_policy"]["actions"][6]["proof_id"]
            == "SP22_GCD_R_MINUS_1_K_EQUALS_1_V1"
        ),
    }
    if not all(checks.values()):
        _reject(RejectCode.LOCAL_TOTALITY_FAILED, "universal totality premise")
    return sealed(
        {
            "receipt_type": "UniversalQ1GSourcePolicyTotalityTheoremReceiptV1",
            "domain_id": policy.payload["source_domain"]["domain_id"],
            "domain_quantifier": "FOR_EVERY_P_SATISFYING_SIGNED_DOMAIN_PREDICATE",
            "policy_payload_sha256": policy.payload_sha256,
            "case_partition": [
                "EARLIEST_M23_TERMINAL_HIT",
                "ALL_M23_MISS_THEN_PHASE_ROOT_VERIFIED_SUCCESSOR",
            ],
            "checks": checks,
            "proof_obligations_discharged": {
                "terminal_replay_termination": "FINITE_DIVISOR_SET_OF_X_G_SQUARED",
                "terminal_replay_determinism": "CANONICAL_ASCENDING_DIVISOR_AND_MATCH_ORDER",
                "terminal_hit_soundness": "DIRECT_UNIT_FRACTION_IDENTITY_CHECK",
                "producer_guard_totality": "DOMAIN_PLUS_COMPLETE_PRIOR_CLEARANCE",
                "target_terminal_transport": "SAME_P_ONLY_PREDICATES_REPLAYED_ON_TARGET_SUBJECT",
                "anchor_sink_miss": "GCD_R_MINUS_1_K_EQUALS_1_AND_R_MINUS_1_GREATER_THAN_1",
                "edge_uniformity": "SYMBOLIC_E1_E2_E3_E4_E5_R_CONSTRUCTION_FOR_ARBITRARY_DOMAIN_P",
            },
            "reject_result_count_on_valid_domain": 0,
            "fallthrough_result_count_on_valid_domain": 0,
            "every_valid_actual_source_decided": True,
        },
        "receipt_id",
    )


def execute_regression_witnesses(
    policy: PolicyContext,
    authority: AuthorityContext,
    ps: Sequence[int] = (73, 193, 1201, 2521, 12721, 21169),
) -> tuple[dict[str, Any], dict[int, dict[str, Any]]]:
    results: dict[int, dict[str, Any]] = {}
    summaries: list[dict[str, Any]] = []
    for p in ps:
        result = run_selector_for_p(policy=policy, authority=authority, p=p)
        if result["result_kind"] not in {"TERMINAL", "VERIFIED_SUCCESSOR"}:
            _reject(RejectCode.LOCAL_TOTALITY_FAILED, f"bad witness result for p={p}")
        results[p] = result
        summaries.append(summarize_selector_result(result))
    receipt = sealed(
        {
            "receipt_type": "Q1GPolicyRegressionWitnessSuiteV1",
            "domain_id": policy.payload["source_domain"]["domain_id"],
            "policy_payload_sha256": policy.payload_sha256,
            "witness_ps": list(ps),
            "results": summaries,
            "terminal_result_count": sum(row["result_kind"] == "TERMINAL" for row in summaries),
            "verified_successor_count": sum(
                row["result_kind"] == "VERIFIED_SUCCESSOR" for row in summaries
            ),
            "witness_suite_pass": True,
            "not_the_basis_of_universal_totality": True,
        },
        "receipt_id",
    )
    return receipt, results


def bounded_predicate_domain_audit(
    policy: PolicyContext, *, upper_exclusive: int = 100_000
) -> dict[str, Any]:
    """Execute an independent-of-authority arithmetic census below a bound.

    This receipt is regression evidence only.  The universal totality theorem
    is the structural case split in :func:`prove_universal_local_totality`.
    """
    if type(upper_exclusive) is not int or isinstance(upper_exclusive, bool) or upper_exclusive <= 2:
        _reject(RejectCode.LOCAL_TOTALITY_FAILED, "bad bounded audit limit")
    actions = policy.payload["source_policy"]["actions"]
    counts = {str(index): 0 for index in range(SELECTED_PRODUCER_INDEX + 1)}
    counts[str(SELECTED_PRODUCER_INDEX)] = 0
    domain_ps: list[int] = []
    successor_ps: list[int] = []
    outcome_digest_rows: list[list[Any]] = []
    for p in range(2, upper_exclusive):
        accepted, _ = source_domain_membership(p)
        if not accepted:
            continue
        domain_ps.append(p)
        selected_index = SELECTED_PRODUCER_INDEX
        selected_kind = "VERIFIED_SUCCESSOR"
        selected_certificate: dict[str, Any] | None = None
        for action in actions[:SELECTED_PRODUCER_INDEX]:
            _, _, _, matches = _bradford_rows(p, action["gap"])
            if matches:
                selected_index = action["index"]
                selected_kind = "TERMINAL"
                selected_certificate = matches[0]
                break
        if selected_kind == "VERIFIED_SUCCESSOR":
            successor_ps.append(p)
        counts[str(selected_index)] = counts.get(str(selected_index), 0) + 1
        outcome_digest_rows.append([p, selected_index, selected_kind, selected_certificate])
    if len(domain_ps) != sum(counts.values()):
        _reject(RejectCode.LOCAL_TOTALITY_FAILED, "bounded audit count partition")
    return sealed(
        {
            "receipt_type": "BoundedQ1GPredicateDomainAuditV1",
            "domain_id": policy.payload["source_domain"]["domain_id"],
            "policy_payload_sha256": policy.payload_sha256,
            "range": {"lower_inclusive": 2, "upper_exclusive": upper_exclusive},
            "domain_source_count": len(domain_ps),
            "domain_ps_sha256": digest_json(domain_ps),
            "selected_action_counts": counts,
            "verified_successor_ps": successor_ps,
            "outcomes_sha256": digest_json(outcome_digest_rows),
            "all_domain_sources_decided": True,
            "reject_count": 0,
            "fallthrough_count": 0,
            "not_the_basis_of_universal_totality": True,
        },
        "receipt_id",
    )

def gap31_negative_control(
    result_21169: Mapping[str, Any], policy: PolicyContext
) -> dict[str, Any]:
    action = policy.payload["source_policy"]["actions"][7]
    record = replay_bradford_action(
        p=21169,
        action=action,
        subject_kind="SOURCE_STATE_ANALYSIS_ONLY_LATER_ACTION",
        subject_id=result_21169["actual_source_receipt"]["source_state_id"],
        policy_id=policy.payload["source_policy"]["policy_id"],
        policy_payload_sha256=policy.payload_sha256,
    )
    selected = record["output"]["selected_certificate"]
    expected = {
        "d": 1,
        "family": "TYPE_II",
        "triple": [5300, 3619899, 19185464700],
    }
    if selected != expected:
        _reject(RejectCode.REPLAY_MISMATCH, "gap-31 negative control")
    clearance = result_21169["clearance_receipt"]
    if clearance["global_exhaustion"] is not False:
        _reject(RejectCode.CLEARANCE_INVALID, "scope clearance became global")
    return sealed(
        {
            "receipt_type": "Gap31LaterTerminalNegativeControlV1",
            "source_state_id": result_21169["actual_source_receipt"]["source_state_id"],
            "selected_producer_index": 6,
            "later_terminal_index": 7,
            "later_terminal_executed_by_selector": False,
            "analysis_only_replay_record": record,
            "gap31_certificate_exists": True,
            "scope_clearance_semantic": clearance["semantic"],
            "scope_clearance_global_exhaustion": clearance["global_exhaustion"],
            "miss_complete_claim": False,
        },
        "receipt_id",
    )


def build_evidence(
    *,
    repo_root: Path,
    policy_path: Path,
    artifact_lock_path: Path,
    authority_path: Path,
) -> dict[str, Any]:
    policy = load_policy(policy_path)
    artifact_lock = load_artifact_lock(artifact_lock_path)
    artifact_lock_receipt = verify_artifact_lock(artifact_lock, repo_root)
    authority = load_and_verify_authority(
        authority_path, policy=policy, artifact_lock=artifact_lock
    )
    static_policy_receipt = verify_policy_static(policy.payload)
    universal_totality = prove_universal_local_totality(policy)
    witness_receipt, results = execute_regression_witnesses(policy, authority)
    bounded_audit = bounded_predicate_domain_audit(policy)
    if 21169 not in results or results[21169]["result_kind"] != "VERIFIED_SUCCESSOR":
        _reject(RejectCode.LOCAL_TOTALITY_FAILED, "p=21169 is not the positive edge")
    p21169 = results[21169]
    negative = gap31_negative_control(p21169, policy)
    queue_audit = static_queue_ingress_audit(Path(__file__).resolve())
    evidence = {
        "evidence_type": "SP21SP22ConcreteClosureEvidenceV1",
        "evidence_version": 1,
        "base_head_sha": BASE_HEAD_SHA,
        "module_id": MODULE_ID,
        "policy_payload_sha256": policy.payload_sha256,
        "artifact_lock_payload_sha256": artifact_lock.payload_sha256,
        "authority": {
            "authority_id": authority.authority_id,
            "statement_sha256": authority.statement_sha256,
            "trusted_key_fingerprint": authority.key_fingerprint,
            "producer_may_mutate_policy": False,
            "caller_authority_boolean_accepted": False,
        },
        "artifact_lock_verification": artifact_lock_receipt,
        "policy_static_verification": static_policy_receipt,
        "universal_local_totality": universal_totality,
        "regression_witnesses": witness_receipt,
        "bounded_predicate_domain_audit": bounded_audit,
        "p21169_execution": p21169,
        "gap31_negative_control": negative,
        "queue_ingress_audit": queue_audit,
        "status": {
            "SP21": "ESTABLISHED_SIGNED_Q1_G_POLICY_DOMAIN",
            "SP22": "ESTABLISHED_FOR_EVERY_SIGNED_Q1_G_ACTUAL_SOURCE",
            "F1": "UNCHANGED_OPEN",
            "F2": "UNCHANGED_OPEN",
            "F3": "UNCHANGED_OPEN",
            "T6": "UNCHANGED_OPEN",
            "erdos_straus_conjecture": "UNCHANGED_OPEN",
        },
    }
    evidence["evidence_id"] = digest_json(evidence)
    return evidence


def _default_paths(repo_root: Path) -> tuple[Path, Path, Path]:
    data = repo_root / "data" / "t6-sp21-q1-p21169"
    return (
        data / "sp21-policy-registry-v1.json",
        data / "sp21-artifact-lock-v1.json",
        data / "sp21-external-authority-anchor-v1.json",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--policy", type=Path)
    parser.add_argument("--artifact-lock", type=Path)
    parser.add_argument("--authority", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve()
    default_policy, default_lock, default_authority = _default_paths(repo_root)
    evidence = build_evidence(
        repo_root=repo_root,
        policy_path=(args.policy or default_policy).resolve(),
        artifact_lock_path=(args.artifact_lock or default_lock).resolve(),
        authority_path=(args.authority or default_authority).resolve(),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(evidence, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(evidence["evidence_id"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
