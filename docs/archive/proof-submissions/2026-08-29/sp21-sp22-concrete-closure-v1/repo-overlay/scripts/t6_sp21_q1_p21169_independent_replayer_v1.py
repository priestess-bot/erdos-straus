#!/usr/bin/env python3
"""Independent end-to-end verifier for the concrete SP-21/SP-22 slice.

This module deliberately imports no repository-local module and no symbol from
the selected producer.  It reconstructs source states, registered-prefix
results, the phase-root projection, target-bound terminal replay, E1--E5/R,
common admission, queue/re-entry facts, and the gap-31 negative control from
JSON plus integer arithmetic.  Its divisor enumeration is a complementary
scan, not the constructor's prime-exponent Cartesian product.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path
import sys
from typing import Any, Mapping, NoReturn, Sequence


MODULE_ID = "t6_sp21_q1_p21169_independent_replayer_v1"
BASE_HEAD_SHA = "e6e9e4a8c41b90a330b9ef333e542c18c2cb7be4"
TRUSTED_AUTHORITY_KEY_SHA256 = (
    "e03c0a9f1fd62668f5f89742aea49c16e68648e2e471480c3d9907d50346da65"
)
M23 = (3, 7, 11, 15, 19, 23)
REGRESSION_PS = (73, 193, 1201, 2521, 12721, 21169)
SELECTED_INDEX = 6
SHA256_DIGEST_INFO_PREFIX = bytes.fromhex(
    "3031300d060960864801650304020105000420"
)


class ReplayFailure(ValueError):
    pass


def fail(detail: str) -> NoReturn:
    raise ReplayFailure(detail)


def json_copy(value: Any, *, path: str = "$") -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                fail(f"{path}: invalid object key")
            result[key] = json_copy(child, path=f"{path}.{key}")
        return result
    if type(value) is list or type(value) is tuple:
        return [json_copy(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    fail(f"{path}: non-canonical type {type(value).__name__}")


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        json_copy(value),
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("ascii")


def digest_json(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {path}: {exc}")
    if type(value) is not dict:
        fail(f"{path}: top level is not object")
    return json_copy(value)


def seal(payload: Mapping[str, Any], id_field: str) -> dict[str, Any]:
    if id_field in payload:
        fail(f"duplicate seal field {id_field}")
    value = json_copy(dict(payload))
    value[id_field] = digest_json(value)
    return value


def verify_seal(value: Mapping[str, Any], id_field: str, *, where: str) -> None:
    if type(value) is not dict or type(value.get(id_field)) is not str:
        fail(f"{where}: missing {id_field}")
    payload = {key: json_copy(child) for key, child in value.items() if key != id_field}
    if digest_json(payload) != value[id_field]:
        fail(f"{where}: bad {id_field}")


def parse_payload_document(path: Path, schema_id: str) -> tuple[dict[str, Any], str]:
    document = load_json(path)
    if set(document) != {"schema_id", "schema_version", "payload", "payload_sha256"}:
        fail(f"{schema_id}: field set")
    if document["schema_id"] != schema_id or document["schema_version"] != 1:
        fail(f"{schema_id}: schema/version")
    if type(document["payload"]) is not dict:
        fail(f"{schema_id}: payload")
    actual = digest_json(document["payload"])
    if document["payload_sha256"] != actual:
        fail(f"{schema_id}: payload digest")
    return document["payload"], actual


def verify_rsa(n_hex: str, exponent: int, message: bytes, signature_hex: str) -> bool:
    try:
        n = int(n_hex, 16)
        signature = int(signature_hex, 16)
    except (TypeError, ValueError):
        return False
    if type(exponent) is not int or isinstance(exponent, bool):
        return False
    key_bytes = (n.bit_length() + 7) // 8
    if signature < 0 or signature >= n:
        return False
    encoded = pow(signature, exponent, n).to_bytes(key_bytes, "big")
    digest_info = SHA256_DIGEST_INFO_PREFIX + hashlib.sha256(message).digest()
    pad_len = key_bytes - len(digest_info) - 3
    if pad_len < 8:
        return False
    expected = b"\x00\x01" + b"\xff" * pad_len + b"\x00" + digest_info
    return encoded == expected


def verify_authority(
    path: Path, *, policy_digest: str, lock_digest: str
) -> tuple[dict[str, Any], str]:
    anchor = load_json(path)
    expected_fields = {
        "schema_id",
        "schema_version",
        "authority_id",
        "public_key",
        "statement",
        "statement_sha256",
        "signature_algorithm",
        "signature_hex",
    }
    if set(anchor) != expected_fields:
        fail("authority field set")
    if anchor["schema_id"] != "SP21ExternalAuthorityAnchorV1" or anchor["schema_version"] != 1:
        fail("authority schema")
    key = anchor["public_key"]
    if type(key) is not dict or set(key) != {"n_hex", "e"}:
        fail("authority key")
    if digest_json(key) != TRUSTED_AUTHORITY_KEY_SHA256:
        fail("authority key fingerprint")
    statement = anchor["statement"]
    statement_digest = digest_json(statement)
    if anchor["statement_sha256"] != statement_digest:
        fail("authority statement digest")
    expected_statement = {
        "authority_id": "sp21_external_coordinator_one_shot_v1",
        "authority_scope": "SP21_SP22_CONCRETE_POLICY_AND_ARTIFACT_LOCK_V1",
        "base_head_sha": BASE_HEAD_SHA,
        "policy_payload_sha256": policy_digest,
        "artifact_lock_payload_sha256": lock_digest,
        "producer_may_mutate_policy": False,
        "caller_authority_boolean_accepted": False,
        "status": "EXTERNAL_COORDINATOR_AUTHORIZED",
    }
    if statement != expected_statement:
        fail("authority statement scope")
    if anchor["authority_id"] != statement["authority_id"]:
        fail("authority ID binding")
    if anchor["signature_algorithm"] != "RSA_PKCS1_V1_5_SHA256":
        fail("authority signature algorithm")
    if not verify_rsa(
        key["n_hex"], key["e"], canonical_bytes(statement), anchor["signature_hex"]
    ):
        fail("authority signature")
    return anchor, statement_digest


def verify_lock(lock: Mapping[str, Any], lock_digest: str, repo_root: Path) -> dict[str, Any]:
    if lock.get("base_head_sha") != BASE_HEAD_SHA:
        fail("artifact lock base HEAD")
    rows = lock.get("artifacts")
    if type(rows) is not list or not rows:
        fail("artifact lock rows")
    seen: set[str] = set()
    verified: list[dict[str, str]] = []
    for row in rows:
        if type(row) is not dict or set(row) != {"path", "role", "sha256"}:
            fail("artifact lock row")
        rel = row["path"]
        if rel in seen or type(rel) is not str or rel.startswith("/") or ".." in Path(rel).parts:
            fail("artifact lock path")
        seen.add(rel)
        data = (repo_root / rel).read_bytes()
        actual = digest_bytes(data)
        if actual != row["sha256"]:
            fail(f"artifact digest: {rel}")
        verified.append({"path": rel, "sha256": actual})
    return seal(
        {
            "receipt_type": "ArtifactLockVerificationReceiptV1",
            "artifact_lock_payload_sha256": lock_digest,
            "base_head_sha": BASE_HEAD_SHA,
            "verified_artifacts": verified,
            "all_locked_artifacts_match": True,
        },
        "receipt_id",
    )


def independent_factorization(n: int) -> list[list[int]]:
    if type(n) is not int or isinstance(n, bool) or n < 1:
        fail("factorization input")
    result: list[list[int]] = []
    d = 2
    remaining = n
    while d * d <= remaining:
        exponent = 0
        while remaining % d == 0:
            remaining //= d
            exponent += 1
        if exponent:
            result.append([d, exponent])
        d += 1
    if remaining > 1:
        result.append([remaining, 1])
    return result


def independent_is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def complementary_divisors(n: int) -> list[int]:
    values: set[int] = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            values.add(d)
            values.add(n // d)
    return sorted(values)


def certificate_ok(p: int, triple: Sequence[int]) -> bool:
    if len(triple) != 3 or any(type(v) is not int or isinstance(v, bool) or v <= 0 for v in triple):
        return False
    x, y, z = triple
    return 4 * x * y * z == p * (x * y + x * z + y * z)


def independent_bradford_output(p: int, gap: int) -> dict[str, Any]:
    if gap <= 0 or gap % 4 != 3 or (p + gap) % 4:
        fail(f"invalid gap {gap}")
    x = (p + gap) // 4
    divisors = complementary_divisors(x * x)
    rows: list[dict[str, Any]] = []
    matches: list[dict[str, Any]] = []
    for d in divisors:
        type_i = (p * x + d) % gap == 0
        type_ii_eligible = d <= x
        type_ii = type_ii_eligible and (x + d) % gap == 0
        rows.append(
            {
                "d": d,
                "type_i_congruence": type_i,
                "type_ii_eligible": type_ii_eligible,
                "type_ii_congruence": type_ii,
            }
        )
        if type_i:
            y = (p * x + d) // gap
            numerator = p * x * y
            if numerator % d == 0:
                triple = [x, y, numerator // d]
                if certificate_ok(p, triple):
                    matches.append({"d": d, "family": "TYPE_I", "triple": triple})
        if type_ii:
            y_num = p * (x + d)
            if y_num % gap == 0:
                y = y_num // gap
                numerator = x * y
                if numerator % d == 0:
                    triple = [x, y, numerator // d]
                    if certificate_ok(p, triple):
                        matches.append({"d": d, "family": "TYPE_II", "triple": triple})
    matches.sort(key=lambda item: (item["d"], 0 if item["family"] == "TYPE_I" else 1, item["triple"]))
    return {
        "outcome": "HIT" if matches else "MISS",
        "gap": gap,
        "x": x,
        "x_prime_factorization": independent_factorization(x),
        "divisor_count": len(divisors),
        "divisors_sha256": digest_json(divisors),
        "transcript_sha256": digest_json(rows),
        "match_count": len(matches),
        "matches": matches,
        "selected_certificate": matches[0] if matches else None,
    }


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
    checks["p_is_prime"] = independent_is_prime(p)
    checks["p_equals_24t_plus_1"] = (p - 1) % 24 == 0
    if not checks["p_is_prime"] or not checks["p_equals_24t_plus_1"]:
        return False, checks
    t = (p - 1) // 24
    x_value = 6 * t + 1
    checks["X_equals_6t_plus_1"] = 4 * x_value == p + 3
    factors = independent_factorization(x_value)
    checks["every_prime_factor_of_X_is_1_mod_3"] = bool(factors) and all(
        prime % 3 == 1 for prime, _ in factors
    )
    return all(checks.values()), checks


def source_wire(policy: Mapping[str, Any], p: int) -> dict[str, Any]:
    in_domain, checks = source_domain_membership(p)
    if not in_domain:
        fail(f"source p={p} outside signed predicate domain")
    t = (p - 1) // 24
    x_value = 6 * t + 1
    factors = independent_factorization(x_value)
    domain = policy["source_domain"]
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
            "X_prime_factorization": factors,
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
            "checks": checks,
            "accepted": True,
        },
        "potential": [p, 3, 0, 0, 0, 0, 0],
    }

def expected_actual_source_receipt(
    policy: Mapping[str, Any],
    policy_digest: str,
    authority: Mapping[str, Any],
    statement_digest: str,
    p: int,
) -> dict[str, Any]:
    wire = source_wire(policy, p)
    state_id = digest_json(wire)
    domain = policy["source_domain"]
    return seal(
        {
            "receipt_type": "ActualSourceReceiptV1",
            "authority_id": authority["authority_id"],
            "authority_statement_sha256": statement_digest,
            "policy_payload_sha256": policy_digest,
            "initializer_id": domain["initializer_id"],
            "source_state_id": state_id,
            "source_state_wire": wire,
            "lineage_status": "PARENTLESS_ROOT_INITIALIZER_VERIFIED",
            "root_admission_contract_id": domain["root_admission_contract_id"],
            "root_admission_status": "EXTERNAL_COORDINATOR_ROOT_ADMISSION_VERIFIED",
            "source_admitted": True,
            "domain_membership_decider_id": domain["membership_decider_id"],
            "domain_membership_verified": True,
            "occurrence_namespace": "PERSISTENT_SOURCE_STATE_WIRE",
            "occurrence_path": ["arithmetic", "q"],
            "occurrence_value": 1,
            "owner_id": wire["owner"]["owner_id"],
            "domain_id": wire["owner"]["domain_id"],
            "source_actualness": True,
            "source_admission": True,
        },
        "receipt_id",
    )

def verify_policy_independently(policy: Mapping[str, Any]) -> dict[str, Any]:
    if policy["base_head_sha"] != BASE_HEAD_SHA:
        fail("policy base HEAD")
    actions = policy["source_policy"]["actions"]
    if len(actions) != 8 or [row["index"] for row in actions] != list(range(8)):
        fail("source policy order")
    if [row.get("gap") for row in actions[:6]] != list(M23):
        fail("M23 order")
    if any(row["kind"] != "TERMINAL" for row in actions[:6]):
        fail("M23 action kind")
    if actions[6]["kind"] != "PRODUCER" or actions[6]["action_id"] != "q1_phase_root_producer_v1":
        fail("selected producer")
    if actions[7]["kind"] != "TERMINAL" or actions[7]["gap"] != 31:
        fail("later gap 31")
    if any(row["kind"] == "REJECT" for row in actions):
        fail("reject in local-total policy")
    rows = policy["priority_overlap_proof"]["rows"]
    terminals = [row for row in actions if row["kind"] == "TERMINAL"]
    if len(rows) != len(terminals):
        fail("overlap cardinality")
    by_id = {row["terminal_action_id"]: row for row in rows}
    if set(by_id) != {row["action_id"] for row in terminals}:
        fail("overlap coverage")
    for action in terminals:
        row = by_id[action["action_id"]]
        if row["guard_overlap"] is not True:
            fail("guard overlap classification")
        relation = row["coordinator_relation"]
        if relation == "PRIOR" and not action["index"] < 6:
            fail("prior ordering")
        if relation == "LATER" and not action["index"] > 6:
            fail("later ordering")
        if relation not in {"PRIOR", "LATER"}:
            fail("unclassified overlap")
        if relation != action["priority_relation_to_selected"]:
            fail("priority relation disagreement")
    if policy["priority_overlap_proof"]["unclassified_registered_terminal_count"] != 0:
        fail("unclassified registered terminal")
    if policy["receipt_semantics"] != {
        "scope_clearance": "MISS_HIGHER_PRIORITY_POLICY_COMPLETE",
        "coverage": "REGISTERED_HIGHER_PRIORITY_ONLY",
        "global_exhaustion": False,
        "miss_complete_serialization_forbidden": True,
    }:
        fail("scope/global semantics")
    target_actions = policy["target_terminal_policy"]["actions"]
    if [row.get("gap") for row in target_actions[:6]] != list(M23):
        fail("target M23")
    if target_actions[6]["algorithm"] != "PHASE_ROOT_ANCHOR_SINK_V1":
        fail("target anchor")
    domain = policy["source_domain"]
    if set(domain) != {
        "domain_id",
        "owner_id",
        "initializer_id",
        "root_admission_contract_id",
        "membership_decider_id",
        "domain_predicate",
        "closed_world_kind",
    }:
        fail("source domain field set")
    if domain["closed_world_kind"] != "DECIDABLE_PREDICATE_CLOSED_WORLD":
        fail("source domain closed world")
    if domain["domain_predicate"] != {
        "p_is_prime": True,
        "p_equals_24t_plus_1": True,
        "q_equals_1": True,
        "X_equals_6t_plus_1": True,
        "every_prime_factor_of_X_is_1_mod_3": True,
    }:
        fail("source domain predicate")
    totality = policy["source_policy"]["local_totality_contract"]
    if totality != {
        "domain": "source_domain.domain_predicate",
        "allowed_results": ["TERMINAL", "VERIFIED_SUCCESSOR"],
        "reject_allowed_for_valid_domain_member": False,
        "fallthrough_allowed": False,
        "proof_method": "STRUCTURAL_FIRST_HIT_OR_TOTAL_PRODUCER_CASE_SPLIT",
        "producer_total_after_complete_prior_miss": True,
    }:
        fail("totality contract")
    return seal(
        {
            "receipt_type": "PolicyStaticVerificationReceiptV1",
            "registry_id": policy["registry_id"],
            "source_policy_id": policy["source_policy"]["policy_id"],
            "target_policy_id": policy["target_terminal_policy"]["policy_id"],
            "selected_action_id": actions[6]["action_id"],
            "selected_action_index": 6,
            "registered_source_action_count": 8,
            "registered_terminal_count": 7,
            "prior_terminal_indices": [0, 1, 2, 3, 4, 5],
            "later_terminal_indices": [7],
            "reject_action_count": 0,
            "overlap_partition_complete": True,
            "source_domain_closed_world_kind": domain["closed_world_kind"],
            "local_totality_proof_method": totality["proof_method"],
        },
        "receipt_id",
    )

def expected_terminal_record(
    *,
    p: int,
    action: Mapping[str, Any],
    subject_kind: str,
    subject_id: str,
    policy_id: str,
    policy_digest: str,
) -> dict[str, Any]:
    return seal(
        {
            "record_type": "PolicyActionReplayRecordV1",
            "subject_kind": subject_kind,
            "subject_id": subject_id,
            "policy_id": policy_id,
            "policy_payload_sha256": policy_digest,
            "action_index": action["index"],
            "action_id": action["action_id"],
            "action_contract_sha256": digest_json(action),
            "action_kind": "TERMINAL",
            "output": independent_bradford_output(p, action["gap"]),
        },
        "record_id",
    )


def expected_clearance(
    source_receipt: Mapping[str, Any], policy: Mapping[str, Any], policy_digest: str, records: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    return seal(
        {
            "receipt_type": "ScopeBoundPriorClearanceReceiptV1",
            "semantic": "MISS_HIGHER_PRIORITY_POLICY_COMPLETE",
            "coverage": "REGISTERED_HIGHER_PRIORITY_ONLY",
            "global_exhaustion": False,
            "source_state_id": source_receipt["source_state_id"],
            "actual_source_receipt_id": source_receipt["receipt_id"],
            "policy_id": policy["source_policy"]["policy_id"],
            "policy_payload_sha256": policy_digest,
            "selected_action_index": 6,
            "selected_action_id": policy["source_policy"]["actions"][6]["action_id"],
            "covered_action_indices": [0, 1, 2, 3, 4, 5],
            "prior_record_ids": [row["record_id"] for row in records],
            "prior_trace_sha256": digest_json(list(records)),
            "miss_complete_serialization_forbidden": True,
        },
        "receipt_id",
    )


def expected_guard(
    source_receipt: Mapping[str, Any], clearance: Mapping[str, Any], policy: Mapping[str, Any], policy_digest: str
) -> dict[str, Any]:
    action = policy["source_policy"]["actions"][6]
    source = source_receipt["source_state_wire"]
    checks = {
        "actual_source": source_receipt["source_actualness"] is True,
        "admitted_source": (
            source_receipt.get("source_admitted") is True
            and source_receipt.get("source_admission") is True
        ),
        "domain_membership": source_receipt.get("domain_membership_verified") is True,
        "source_policy_binding": clearance["source_state_id"] == source_receipt["source_state_id"],
        "policy_digest_binding": clearance["policy_payload_sha256"] == policy_digest,
        "complete_prior_indices": clearance["covered_action_indices"] == [0, 1, 2, 3, 4, 5],
        "scope_not_global": clearance["global_exhaustion"] is False,
        "q_occurrence": source["arithmetic"]["q"] == 1,
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
    return seal(
        {
            "record_type": "ProducerGuardReplayRecordV1",
            "subject_id": source_receipt["source_state_id"],
            "policy_id": policy["source_policy"]["policy_id"],
            "policy_payload_sha256": policy_digest,
            "action_index": 6,
            "action_id": action["action_id"],
            "action_contract_sha256": digest_json(action),
            "checks": checks,
            "outcome": "GUARD_TRUE" if all(checks.values()) else "GUARD_FALSE",
        },
        "record_id",
    )



def independent_source_prefix_decision(
    *,
    policy: Mapping[str, Any],
    policy_digest: str,
    authority: Mapping[str, Any],
    statement_digest: str,
    p: int,
) -> dict[str, Any]:
    """Replay only the frozen source prefix and selected-producer guard.

    This function deliberately does not call or import the selected producer or
    any constructor-side E1--E5/R verifier.  It is total on the signed source
    predicate domain: it returns the earliest terminal HIT or a complete
    scope-bound clearance followed by a true producer guard.
    """
    source_receipt = expected_actual_source_receipt(
        policy, policy_digest, authority, statement_digest, p
    )
    records: list[dict[str, Any]] = []
    for action in policy["source_policy"]["actions"][:SELECTED_INDEX]:
        record = expected_terminal_record(
            p=p,
            action=action,
            subject_kind="SOURCE_STATE",
            subject_id=source_receipt["source_state_id"],
            policy_id=policy["source_policy"]["policy_id"],
            policy_digest=policy_digest,
        )
        records.append(record)
        if record["output"]["outcome"] == "HIT":
            return seal(
                {
                    "receipt_type": "IndependentSourcePrefixDecisionV1",
                    "p": p,
                    "actual_source_receipt": source_receipt,
                    "selector_trace": records,
                    "result_kind": "TERMINAL",
                    "selected_action_index": action["index"],
                    "selected_action_id": action["action_id"],
                    "terminal_certificate": record["output"]["selected_certificate"],
                    "selected_producer_or_edge_code_called": False,
                },
                "receipt_id",
            )
    clearance = expected_clearance(source_receipt, policy, policy_digest, records)
    guard = expected_guard(source_receipt, clearance, policy, policy_digest)
    if guard["outcome"] != "GUARD_TRUE":
        fail(f"valid domain source p={p} reached false producer guard")
    return seal(
        {
            "receipt_type": "IndependentSourcePrefixDecisionV1",
            "p": p,
            "actual_source_receipt": source_receipt,
            "selector_trace": records + [guard],
            "result_kind": "SELECTED_PRODUCER_GUARD_TRUE",
            "selected_action_index": SELECTED_INDEX,
            "selected_action_id": policy["source_policy"]["actions"][SELECTED_INDEX]["action_id"],
            "clearance_receipt": clearance,
            "guard_record": guard,
            "selected_producer_or_edge_code_called": False,
        },
        "receipt_id",
    )

def expected_projection(source: Mapping[str, Any]) -> dict[str, Any]:
    p = source["arithmetic"]["p"]
    t = source["arithmetic"]["t"]
    x_value = source["arithmetic"]["X"]
    r_value = 16 * t + 3
    k_value = x_value * (16 * t + 1)
    if 4 * k_value != p * r_value + 1:
        fail("phase-root identity")
    return seal(
        {
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
        },
        "projection_id",
    )


def expected_preclassification(projection: Mapping[str, Any], policy: Mapping[str, Any]) -> dict[str, Any]:
    return seal(
        {
            "object_type": "TargetPredicatePreclassificationV1",
            "projection_id": projection["projection_id"],
            "checks": {
                "A_is_one": projection["A"] == 1,
                "four_k_identity": 4 * projection["K"] == projection["p"] * projection["R"] + 1,
                "X_divides_K": projection["K"] % projection["X"] == 0,
                "R_range": 3 <= projection["R"] <= projection["p"] - 2,
                "normal_form": True,
            },
            "unique_owner_id": policy["owner_registry"]["target_owner_id"],
            "owner_precedence_index": policy["owner_registry"]["target_owner_precedence_index"],
            "predicate_match_count": 1,
            "authority_status": "NON_AUTHORIZING_PRECLASSIFICATION",
        },
        "preclassification_id",
    )


def expected_anchor_record(
    projection: Mapping[str, Any], action: Mapping[str, Any], policy: Mapping[str, Any], policy_digest: str
) -> dict[str, Any]:
    divisor = projection["R"] - 1
    hit = divisor > 0 and projection["K"] % divisor == 0
    certificate = [projection["K"] // divisor, projection["K"], projection["p"] * projection["K"]] if hit else None
    if certificate is not None and not certificate_ok(projection["p"], certificate):
        fail("anchor certificate")
    return seal(
        {
            "record_type": "PolicyActionReplayRecordV1",
            "subject_kind": "TARGET_PROJECTION",
            "subject_id": projection["projection_id"],
            "policy_id": policy["target_terminal_policy"]["policy_id"],
            "policy_payload_sha256": policy_digest,
            "action_index": action["index"],
            "action_id": action["action_id"],
            "action_contract_sha256": digest_json(action),
            "action_kind": "TERMINAL",
            "output": {
                "outcome": "HIT" if hit else "MISS",
                "predicate": "R_MINUS_1_DIVIDES_K",
                "R_minus_1": divisor,
                "K": projection["K"],
                "gcd_R_minus_1_K": gcd(divisor, projection["K"]),
                "selected_certificate": certificate,
            },
        },
        "record_id",
    )


def expected_target_terminal(
    source_state_id: str, projection: Mapping[str, Any], policy: Mapping[str, Any], policy_digest: str
) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    target_policy = policy["target_terminal_policy"]
    for action in target_policy["actions"][:6]:
        records.append(
            expected_terminal_record(
                p=projection["p"],
                action=action,
                subject_kind="TARGET_PROJECTION",
                subject_id=projection["projection_id"],
                policy_id=target_policy["policy_id"],
                policy_digest=policy_digest,
            )
        )
    records.append(expected_anchor_record(projection, target_policy["actions"][6], policy, policy_digest))
    if any(row["output"]["outcome"] == "HIT" for row in records):
        fail("p=21169 target policy unexpectedly hits")
    return seal(
        {
            "receipt_type": "TargetTerminalDecisionReceiptV1",
            "source_state_id": source_state_id,
            "target_projection_id": projection["projection_id"],
            "target_policy_id": target_policy["policy_id"],
            "policy_payload_sha256": policy_digest,
            "outcome": "MISS_REGISTERED_TARGET_PRIORITY_COMPLETE",
            "coverage": "REGISTERED_TARGET_ACTIONS_ONLY",
            "global_exhaustion": False,
            "records": records,
            "terminal_certificate": None,
            "lift": None,
        },
        "receipt_id",
    )


def expected_potential(source: Mapping[str, Any], projection: Mapping[str, Any]) -> dict[str, Any]:
    p = source["arithmetic"]["p"]
    return seal(
        {
            "object_type": "T5PotentialDraftV1",
            "evaluator_id": "t5_frozen_n7_phase_drop_v1",
            "projection_id": projection["projection_id"],
            "source_potential": [p, 3, 0, 0, 0, 0, 0],
            "target_potential": [p, 2, 4, (p - 1) ** 2 // 4, projection["K"], 0, 0],
            "comparison": "LEX_STRICT_DECREASE",
            "ticket_kind": "PHASE_DROP",
        },
        "draft_id",
    )


def expected_edge_objects(
    *,
    source_receipt: Mapping[str, Any],
    clearance: Mapping[str, Any],
    guard: Mapping[str, Any],
    policy: Mapping[str, Any],
    policy_digest: str,
    authority: Mapping[str, Any],
    statement_digest: str,
) -> dict[str, Any]:
    source = source_receipt["source_state_wire"]
    projection = expected_projection(source)
    preclassification = expected_preclassification(projection, policy)
    target_terminal = expected_target_terminal(source_receipt["source_state_id"], projection, policy, policy_digest)
    potential = expected_potential(source, projection)
    anchor = seal(
        {
            "object_type": "SP22EdgeAnchorV1",
            "source_state_id": source_receipt["source_state_id"],
            "actual_source_receipt_id": source_receipt["receipt_id"],
            "clearance_receipt_id": clearance["receipt_id"],
            "policy_payload_sha256": policy_digest,
            "selected_action_index": 6,
            "selected_action_id": policy["source_policy"]["actions"][6]["action_id"],
            "projection_id": projection["projection_id"],
            "preclassification_id": preclassification["preclassification_id"],
            "target_terminal_receipt_id": target_terminal["receipt_id"],
            "potential_draft_id": potential["draft_id"],
        },
        "edge_anchor_id",
    )
    p = projection["p"]
    prestate = {
        "schema_id": "SP22PhaseRootSemanticPrestateV1",
        "schema_version": 1,
        "state_kind": "ROOT_SOL",
        "equation": {"numerator": 4, "denominator": p},
        "arithmetic": {"p": p, "R": projection["R"], "K": projection["K"], "A": 1},
        "normal_form": {
            "major_phase": "TYPEI",
            "protocol": "CHARGED",
            "carrier": "FULL_CARRIER_POST_G",
            "full_carrier_scope": True,
            "support_A": 1,
            "is_overflow": False,
        },
        "upstream_edge_anchor_id": anchor["edge_anchor_id"],
        "potential": [p, 2, 4, (p - 1) ** 2 // 4, projection["K"], 0, 0],
    }
    target_state_id = digest_json(prestate)
    registry = policy["owner_registry"]
    owner = seal(
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
    selected_action = policy["source_policy"]["actions"][6]
    e1 = seal(
        {
            "receipt_type": "E1ActualOccurrenceReceiptV1",
            "authority_id": authority["authority_id"],
            "authority_statement_sha256": statement_digest,
            "source_state_id": source_receipt["source_state_id"],
            "actual_source_receipt_id": source_receipt["receipt_id"],
            "lineage_status": source_receipt["lineage_status"],
            "occurrence_namespace": source_receipt["occurrence_namespace"],
            "occurrence_path": source_receipt["occurrence_path"],
            "occurrence_value": source_receipt["occurrence_value"],
            "policy_payload_sha256": policy_digest,
            "clearance_receipt_id": clearance["receipt_id"],
            "complete_prior_trace_sha256": clearance["prior_trace_sha256"],
            "selected_branch_index": 6,
            "selected_branch_id": selected_action["action_id"],
            "guard_record_id": guard["record_id"],
            "owner_id": source["owner"]["owner_id"],
            "domain_id": source["owner"]["domain_id"],
        },
        "receipt_id",
    )
    e2 = seal(
        {
            "receipt_type": "E2UniqueProjectionReceiptV1",
            "source_state_id": source_receipt["source_state_id"],
            "projection_id": projection["projection_id"],
            "target_state_id": target_state_id,
            "formula_id": projection["formula_id"],
            "inputs": {"p": p, "t": projection["t"], "X": projection["X"]},
            "outputs": {"R": projection["R"], "K": projection["K"], "A": 1},
            "identity_4K_equals_pR_plus_1": True,
            "caller_supplied_tie_break": False,
            "projection_unique": True,
        },
        "receipt_id",
    )
    e3 = seal(
        {
            "receipt_type": "E3CommonTargetAdmissionPredicateReceiptV1",
            "target_state_id": target_state_id,
            "target_schema_id": prestate["schema_id"],
            "preclassification_id": preclassification["preclassification_id"],
            "target_terminal_receipt_id": target_terminal["receipt_id"],
            "target_terminal_outcome": target_terminal["outcome"],
            "owner_receipt_id": owner["receipt_id"],
            "owner_id": owner["owner_id"],
            "domain_id": owner["domain_id"],
            "normal_form": prestate["normal_form"],
            "admission_gate_id": policy["admission_contract"]["admission_gate_id"],
            "schema_valid": True,
            "grammar_valid": True,
            "owner_recomputed": True,
            "registered_target_priority_clear": True,
        },
        "receipt_id",
    )
    e4 = seal(
        {
            "receipt_type": "E4UniversalIdentityLiftReceiptV1",
            "source_state_id": source_receipt["source_state_id"],
            "target_state_id": target_state_id,
            "source_equation": source["equation"],
            "target_equation": prestate["equation"],
            "lift_id": "IDENTITY_ON_POSITIVE_INTEGER_TRIPLES_V1",
            "definition": "Lambda(x,y,z)=(x,y,z)",
            "proof_rule": "DEFINITIONAL_EQUALITY_OF_SOLUTION_PREDICATES",
            "universal_quantifier": True,
        },
        "receipt_id",
    )
    e5 = seal(
        {
            "receipt_type": "E5FrozenPotentialReceiptV1",
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
        "receipt_id",
    )
    r_receipt = seal(
        {
            "receipt_type": "RRegisteredReentryReceiptV1",
            "target_state_id": target_state_id,
            "owner_receipt_id": owner["receipt_id"],
            "owner_id": owner["owner_id"],
            "route_id": registry["target_route_id"],
            "body_id": registry["target_body_id"],
            "selector_runtime_id": policy["admission_contract"]["selector_runtime_id"],
            "persistent_state_universe": "T6_PHASE_ROOT_PRESTATE_V1",
            "route_registered": True,
            "reentry_consumable": True,
            "self_edge_authorized": False,
        },
        "receipt_id",
    )
    bundle = seal(
        {
            "bundle_type": "SP22IndependentE1E5RBundleV1",
            "edge_anchor_id": anchor["edge_anchor_id"],
            "source_state_id": source_receipt["source_state_id"],
            "target_state_id": target_state_id,
            "policy_payload_sha256": policy_digest,
            "authority_statement_sha256": statement_digest,
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
    admission = policy["admission_contract"]
    token_preimage = {
        "source_state_id": bundle["source_state_id"],
        "target_state_id": target_state_id,
        "bundle_id": bundle["bundle_id"],
        "owner_receipt_id": owner["receipt_id"],
        "authority_statement_sha256": statement_digest,
        "admission_gate_id": admission["admission_gate_id"],
        "one_time_sequence": 0,
    }
    queue_token = digest_json(token_preimage)
    sidecar = seal(
        {
            "receipt_type": "CommonAdmissionSidecarV1",
            "admission_gate_id": admission["admission_gate_id"],
            "projector_id": admission["projector_id"],
            "classifier_id": admission["classifier_id"],
            "unique_queue_writer_id": admission["unique_queue_writer_id"],
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
    reentry = seal(
        {
            "receipt_type": "ActualReentryReceiptV1",
            "target_state_id": target_state_id,
            "admission_id": sidecar["admission_id"],
            "queue_token": queue_token,
            "selector_runtime_id": admission["selector_runtime_id"],
            "route_id": owner["route_id"],
            "body_id": owner["body_id"],
            "result": "ENTERED_TYPE_I_FULL_CARRIER_POST_G_BODY",
            "self_edge_emitted": False,
            "queue_write_during_reentry": False,
        },
        "receipt_id",
    )
    runtime_trace = [
        {
            "event": "QUEUE_INGRESS_WRITE",
            "writer_id": admission["unique_queue_writer_id"],
            "queue_token": queue_token,
            "target_state_id": target_state_id,
        },
        {
            "event": "QUEUE_CONSUME_AND_REENTRY",
            "route_id": owner["route_id"],
            "body_id": owner["body_id"],
            "target_state_id": target_state_id,
        },
    ]
    return {
        "projection": projection,
        "preclassification": preclassification,
        "target_terminal_receipt": target_terminal,
        "potential_draft": potential,
        "edge_anchor": anchor,
        "target_prestate": prestate,
        "target_state_id": target_state_id,
        "owner_receipt": owner,
        "edge_bundle": bundle,
        "admission_sidecar": sidecar,
        "reentry_receipt": reentry,
        "runtime_trace": runtime_trace,
        "queue_empty_after_reentry": True,
    }


def expected_queue_audit(selector_path: Path) -> dict[str, Any]:
    tree = ast.parse(selector_path.read_text(encoding="utf-8"))
    stack: list[str] = []
    stores: list[dict[str, Any]] = []
    ingress: list[str] = []

    class Visitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            stack.append(node.name)
            if node.name == "_unique_queue_write_v1":
                ingress.append(node.name)
            self.generic_visit(node)
            stack.pop()

        def visit_Assign(self, node: ast.Assign) -> None:
            for target in node.targets:
                if isinstance(target, ast.Attribute) and target.attr == "_queue":
                    stores.append({"function": stack[-1] if stack else "<module>", "line": node.lineno})
            self.generic_visit(node)

        def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
            if isinstance(node.target, ast.Attribute) and node.target.attr == "_queue":
                stores.append({"function": stack[-1] if stack else "<module>", "line": node.lineno})
            self.generic_visit(node)

    Visitor().visit(tree)
    if ingress != ["_unique_queue_write_v1"]:
        fail("unique queue writer AST")
    if not {row["function"] for row in stores}.issubset(
        {"__init__", "_unique_queue_write_v1", "consume_and_reenter_v1"}
    ):
        fail("unexpected queue store")
    return seal(
        {
            "receipt_type": "StaticQueueIngressAuditReceiptV1",
            "module_id": "t6_sp21_q1_p21169_concrete_selector_v1",
            "module_sha256": digest_bytes(selector_path.read_bytes()),
            "unique_ingress_writer": "_unique_queue_write_v1",
            "queue_store_sites": stores,
            "allowed_store_functions": ["__init__", "_unique_queue_write_v1", "consume_and_reenter_v1"],
            "public_enqueue_surface": False,
            "audit_pass": True,
        },
        "receipt_id",
    )


def expected_universal_totality(
    *, policy: Mapping[str, Any], policy_digest: str
) -> dict[str, Any]:
    actions = policy["source_policy"]["actions"]
    prior = actions[:6]
    selected = actions[6]
    checks = {
        "domain_is_decidable_predicate_closed_world": (
            policy["source_domain"]["closed_world_kind"]
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
        "no_fallthrough_after_prior_miss": selected["index"] == 6,
        "target_m23_transport_is_p_only": all(
            action["predicate"].get("kind") == "P_ONLY_FIXED_GAP_DIVISOR_SCREEN"
            for action in policy["target_terminal_policy"]["actions"][:6]
        ),
        "anchor_sink_uniform_miss_proof_registered": (
            policy["target_terminal_policy"]["actions"][6]["proof_id"]
            == "SP22_GCD_R_MINUS_1_K_EQUALS_1_V1"
        ),
    }
    if not all(checks.values()):
        fail("universal totality premise")
    return seal(
        {
            "receipt_type": "UniversalQ1GSourcePolicyTotalityTheoremReceiptV1",
            "domain_id": policy["source_domain"]["domain_id"],
            "domain_quantifier": "FOR_EVERY_P_SATISFYING_SIGNED_DOMAIN_PREDICATE",
            "policy_payload_sha256": policy_digest,
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


def expected_regression_witnesses(
    *,
    policy: Mapping[str, Any],
    policy_digest: str,
    authority: Mapping[str, Any],
    statement_digest: str,
    p21169_execution: Mapping[str, Any],
) -> dict[str, Any]:
    actions = policy["source_policy"]["actions"]
    summaries: list[dict[str, Any]] = []
    for p in REGRESSION_PS:
        source_receipt = expected_actual_source_receipt(
            policy, policy_digest, authority, statement_digest, p
        )
        first_hit = None
        for action in actions[:6]:
            output = independent_bradford_output(p, action["gap"])
            if output["outcome"] == "HIT":
                first_hit = (action, output["selected_certificate"])
                break
        if first_hit is not None:
            action, certificate = first_hit
            summaries.append(
                {
                    "p": p,
                    "source_state_id": source_receipt["source_state_id"],
                    "actual_source_receipt_id": source_receipt["receipt_id"],
                    "result_kind": "TERMINAL",
                    "selected_action_index": action["index"],
                    "selected_action_id": action["action_id"],
                    "terminal_certificate": certificate,
                }
            )
        else:
            if p != 21169:
                fail(f"unexpected nonterminal regression witness p={p}")
            summaries.append(
                {
                    "p": p,
                    "source_state_id": p21169_execution["actual_source_receipt"]["source_state_id"],
                    "actual_source_receipt_id": p21169_execution["actual_source_receipt"]["receipt_id"],
                    "result_kind": "VERIFIED_SUCCESSOR",
                    "selected_action_index": 6,
                    "selected_action_id": actions[6]["action_id"],
                    "clearance_receipt_id": p21169_execution["clearance_receipt"]["receipt_id"],
                    "target_state_id": p21169_execution["target_state_id"],
                    "edge_bundle_id": p21169_execution["edge_bundle"]["bundle_id"],
                    "admission_id": p21169_execution["admission_sidecar"]["admission_id"],
                    "reentry_receipt_id": p21169_execution["reentry_receipt"]["receipt_id"],
                }
            )
    return seal(
        {
            "receipt_type": "Q1GPolicyRegressionWitnessSuiteV1",
            "domain_id": policy["source_domain"]["domain_id"],
            "policy_payload_sha256": policy_digest,
            "witness_ps": list(REGRESSION_PS),
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


def expected_bounded_predicate_domain_audit(
    *, policy: Mapping[str, Any], policy_digest: str, upper_exclusive: int = 100_000
) -> dict[str, Any]:
    """Recompute the bounded census with the complementary divisor scan."""
    actions = policy["source_policy"]["actions"]
    counts = {str(index): 0 for index in range(SELECTED_INDEX + 1)}
    counts[str(SELECTED_INDEX)] = 0
    domain_ps: list[int] = []
    successor_ps: list[int] = []
    outcome_digest_rows: list[list[Any]] = []
    for p in range(2, upper_exclusive):
        accepted, _ = source_domain_membership(p)
        if not accepted:
            continue
        domain_ps.append(p)
        selected_index = SELECTED_INDEX
        selected_kind = "VERIFIED_SUCCESSOR"
        selected_certificate: dict[str, Any] | None = None
        for action in actions[:SELECTED_INDEX]:
            output = independent_bradford_output(p, action["gap"])
            if output["outcome"] == "HIT":
                selected_index = action["index"]
                selected_kind = "TERMINAL"
                selected_certificate = output["selected_certificate"]
                break
        if selected_kind == "VERIFIED_SUCCESSOR":
            successor_ps.append(p)
        counts[str(selected_index)] = counts.get(str(selected_index), 0) + 1
        outcome_digest_rows.append([p, selected_index, selected_kind, selected_certificate])
    if len(domain_ps) != sum(counts.values()):
        fail("bounded audit count partition")
    return seal(
        {
            "receipt_type": "BoundedQ1GPredicateDomainAuditV1",
            "domain_id": policy["source_domain"]["domain_id"],
            "policy_payload_sha256": policy_digest,
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

def verify_independence_of_this_module(path: Path) -> dict[str, Any]:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    local_imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith("t6_"):
                    local_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.startswith("t6_"):
                local_imports.append(node.module)
    if local_imports:
        fail("independent replayer imports a repository-local t6 module")
    return seal(
        {
            "receipt_type": "IndependentImplementationBoundaryReceiptV1",
            "replayer_module_id": MODULE_ID,
            "replayer_sha256": digest_bytes(path.read_bytes()),
            "repository_local_imports": local_imports,
            "selected_producer_imported": False,
            "divisor_algorithm": "COMPLEMENTARY_DIVISOR_SCAN",
            "constructor_divisor_algorithm": "PRIME_EXPONENT_CARTESIAN_PRODUCT",
            "independent_boundary_pass": True,
        },
        "receipt_id",
    )


def verify_evidence(
    *,
    repo_root: Path,
    policy_path: Path,
    lock_path: Path,
    authority_path: Path,
    evidence_path: Path,
) -> dict[str, Any]:
    policy, policy_digest = parse_payload_document(policy_path, "SP21ConcretePolicyRegistryV1")
    lock, lock_digest = parse_payload_document(lock_path, "SP21ArtifactLockV1")
    authority, statement_digest = verify_authority(
        authority_path, policy_digest=policy_digest, lock_digest=lock_digest
    )
    expected_lock_receipt = verify_lock(lock, lock_digest, repo_root)
    expected_policy_receipt = verify_policy_independently(policy)
    evidence = load_json(evidence_path)
    if evidence.get("evidence_id") != digest_json(
        {key: value for key, value in evidence.items() if key != "evidence_id"}
    ):
        fail("evidence seal")
    if evidence["artifact_lock_verification"] != expected_lock_receipt:
        fail("artifact lock receipt mismatch")
    if evidence["policy_static_verification"] != expected_policy_receipt:
        fail("policy static receipt mismatch")
    if evidence["base_head_sha"] != BASE_HEAD_SHA or evidence["policy_payload_sha256"] != policy_digest:
        fail("evidence base/policy binding")
    if evidence["artifact_lock_payload_sha256"] != lock_digest:
        fail("evidence lock binding")
    expected_authority_summary = {
        "authority_id": authority["authority_id"],
        "statement_sha256": statement_digest,
        "trusted_key_fingerprint": TRUSTED_AUTHORITY_KEY_SHA256,
        "producer_may_mutate_policy": False,
        "caller_authority_boolean_accepted": False,
    }
    if evidence["authority"] != expected_authority_summary:
        fail("evidence authority summary")

    execution = evidence["p21169_execution"]
    source_receipt = expected_actual_source_receipt(
        policy, policy_digest, authority, statement_digest, 21169
    )
    if execution["actual_source_receipt"] != source_receipt:
        fail("actual source receipt")
    source_actions = policy["source_policy"]["actions"]
    prior_records = [
        expected_terminal_record(
            p=21169,
            action=action,
            subject_kind="SOURCE_STATE",
            subject_id=source_receipt["source_state_id"],
            policy_id=policy["source_policy"]["policy_id"],
            policy_digest=policy_digest,
        )
        for action in source_actions[:6]
    ]
    if any(row["output"]["outcome"] != "MISS" for row in prior_records):
        fail("p=21169 M23 is not all MISS")
    clearance = expected_clearance(source_receipt, policy, policy_digest, prior_records)
    guard = expected_guard(source_receipt, clearance, policy, policy_digest)
    if guard["outcome"] != "GUARD_TRUE":
        fail("expected producer guard true")
    if execution["selector_trace"] != prior_records + [guard]:
        fail("source selector trace")
    if execution["clearance_receipt"] != clearance:
        fail("clearance receipt")
    expected_edge = expected_edge_objects(
        source_receipt=source_receipt,
        clearance=clearance,
        guard=guard,
        policy=policy,
        policy_digest=policy_digest,
        authority=authority,
        statement_digest=statement_digest,
    )
    for key, value in expected_edge.items():
        if execution.get(key) != value:
            fail(f"edge object mismatch: {key}")
    if execution["result_kind"] != "VERIFIED_SUCCESSOR" or execution["selected_action_index"] != 6:
        fail("p=21169 selector result")
    if execution["selected_action_id"] != source_actions[6]["action_id"]:
        fail("p=21169 selected action")
    if execution["p"] != 21169:
        fail("p=21169 execution p")

    expected_totality = expected_universal_totality(
        policy=policy,
        policy_digest=policy_digest,
    )
    if evidence["universal_local_totality"] != expected_totality:
        fail("universal local totality receipt")
    expected_witnesses = expected_regression_witnesses(
        policy=policy,
        policy_digest=policy_digest,
        authority=authority,
        statement_digest=statement_digest,
        p21169_execution=execution,
    )
    if evidence["regression_witnesses"] != expected_witnesses:
        fail("regression witness receipt")
    expected_bounded_audit = expected_bounded_predicate_domain_audit(
        policy=policy, policy_digest=policy_digest
    )
    if evidence["bounded_predicate_domain_audit"] != expected_bounded_audit:
        fail("bounded predicate-domain audit receipt")

    later_action = source_actions[7]
    later_record = expected_terminal_record(
        p=21169,
        action=later_action,
        subject_kind="SOURCE_STATE_ANALYSIS_ONLY_LATER_ACTION",
        subject_id=source_receipt["source_state_id"],
        policy_id=policy["source_policy"]["policy_id"],
        policy_digest=policy_digest,
    )
    expected_certificate = {
        "d": 1,
        "family": "TYPE_II",
        "triple": [5300, 3619899, 19185464700],
    }
    if later_record["output"]["selected_certificate"] != expected_certificate:
        fail("gap-31 certificate")
    expected_negative = seal(
        {
            "receipt_type": "Gap31LaterTerminalNegativeControlV1",
            "source_state_id": source_receipt["source_state_id"],
            "selected_producer_index": 6,
            "later_terminal_index": 7,
            "later_terminal_executed_by_selector": False,
            "analysis_only_replay_record": later_record,
            "gap31_certificate_exists": True,
            "scope_clearance_semantic": clearance["semantic"],
            "scope_clearance_global_exhaustion": False,
            "miss_complete_claim": False,
        },
        "receipt_id",
    )
    if evidence["gap31_negative_control"] != expected_negative:
        fail("gap-31 negative control receipt")

    selector_path = repo_root / "scripts/t6_sp21_q1_p21169_concrete_selector_v1.py"
    if evidence["queue_ingress_audit"] != expected_queue_audit(selector_path):
        fail("queue ingress audit")
    if evidence["status"] != {
        "SP21": "ESTABLISHED_SIGNED_Q1_G_POLICY_DOMAIN",
        "SP22": "ESTABLISHED_FOR_EVERY_SIGNED_Q1_G_ACTUAL_SOURCE",
        "F1": "UNCHANGED_OPEN",
        "F2": "UNCHANGED_OPEN",
        "F3": "UNCHANGED_OPEN",
        "T6": "UNCHANGED_OPEN",
        "erdos_straus_conjecture": "UNCHANGED_OPEN",
    }:
        fail("status/non-claims")

    independent_boundary = verify_independence_of_this_module(Path(__file__).resolve())
    return seal(
        {
            "receipt_type": "SP21SP22IndependentEndToEndReplayReceiptV1",
            "replayer_module_id": MODULE_ID,
            "base_head_sha": BASE_HEAD_SHA,
            "policy_payload_sha256": policy_digest,
            "artifact_lock_payload_sha256": lock_digest,
            "authority_statement_sha256": statement_digest,
            "evidence_id": evidence["evidence_id"],
            "source_domain": "ALL_P_SATISFYING_SIGNED_Q1_G_PREDICATE",
            "universal_local_totality_verified": True,
            "regression_witness_ps": list(REGRESSION_PS),
            "bounded_audit_upper_exclusive": 100000,
            "bounded_audit_domain_source_count": expected_bounded_audit["domain_source_count"],
            "bounded_audit_verified_successor_ps": expected_bounded_audit["verified_successor_ps"],
            "source_results": {
                "73": "TERMINAL_REGISTERED_PREFIX",
                "193": "TERMINAL_REGISTERED_PREFIX",
                "1201": "TERMINAL_GAP_23_TYPE_I_D_34",
                "2521": "TERMINAL_GAP_23_TYPE_II_D_8",
                "12721": "TERMINAL_GAP_19_TYPE_II_D_7",
                "21169": "VERIFIED_SUCCESSOR_PHASE_ROOT",
            },
            "p21169_target_state_id": execution["target_state_id"],
            "p21169_edge_bundle_id": execution["edge_bundle"]["bundle_id"],
            "gap31_later_certificate_verified": True,
            "global_exhaustion_asserted": False,
            "independent_boundary": independent_boundary,
            "all_checks_pass": True,
        },
        "receipt_id",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--policy", type=Path)
    parser.add_argument("--artifact-lock", type=Path)
    parser.add_argument("--authority", type=Path)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve()
    data = repo_root / "data/t6-sp21-q1-p21169"
    receipt = verify_evidence(
        repo_root=repo_root,
        policy_path=(args.policy or data / "sp21-policy-registry-v1.json").resolve(),
        lock_path=(args.artifact_lock or data / "sp21-artifact-lock-v1.json").resolve(),
        authority_path=(args.authority or data / "sp21-external-authority-anchor-v1.json").resolve(),
        evidence_path=args.evidence.resolve(),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(receipt["receipt_id"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
