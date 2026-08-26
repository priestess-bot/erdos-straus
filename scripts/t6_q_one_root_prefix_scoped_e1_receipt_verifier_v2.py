#!/usr/bin/env python3
"""Post-issuance exact-HEAD replay for the V4 root-scoped E1 receipt.

The verifier is intentionally separate from the orchestrator and the three
roles.  It never directly imports or calls the orchestrator, issuer, scheduler,
or coverage runtime.  The V3 production verifier may transitively execute its
pinned legacy verification path; that is a provenance check, not an independent
third mathematical proof.  Instead this module loads the requested-HEAD V4 resolver, V3
production verifier, root initializer, and role blobs into fresh namespaces,
rebuilds the expected role chain from raw integers and the supplied production
MISS, and compares the supplied consumer wire byte-for-byte (canonical JSON).

This is an issuer-independent *wire* replay.  It is not a third mathematical
proof of the phase-root identities, and it does not grant any authority.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from types import ModuleType
from typing import Any, Mapping, NoReturn, Sequence


VERIFIER_ID = "q1_root_prefix_scoped_e1_receipt_verifier_v2"
VERIFIER_PATH = "scripts/t6_q_one_root_prefix_scoped_e1_receipt_verifier_v2.py"
ORCHESTRATOR_PATH = "scripts/t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py"
V4_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v4.py"
V4_RESOLVER_SYMBOL = "resolve_registry_v4"
V3_VERIFIER_PATH = "scripts/t6_q_one_terminal_receipt_verifier_v1.py"
V3_VERIFIER_SYMBOL = "verify_q_one_production_terminal_receipt_v1"
ROOT_INITIALIZER_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"
OWNER_PATH = "scripts/t6_q_one_root_owner_classifier_v2.py"
OWNER_SYMBOL = "classify_q_one_root_owner_v2"
OWNER_SERIALIZER = "root_owner_receipt_to_mapping_v2"
VALIDATOR_PATH = "scripts/t6_q_one_scope_aware_e1_validator_v2.py"
VALIDATOR_SYMBOL = "validate_q_one_registered_prefix_e1_scope_v2"
VALIDATOR_SERIALIZER = "scope_validation_receipt_to_mapping_v2"
CONSUMER_PATH = "scripts/t6_q_one_registered_prefix_e1_consumer_v2.py"
CONSUMER_SYMBOL = "consume_q_one_registered_prefix_miss_for_e1_v2"
CONSUMER_SERIALIZER = "root_source_scoped_e1_receipt_to_mapping_v2"

ROLE_OWNER = "COMMON_ROOT_OWNER_CLASSIFIER"
ROLE_VALIDATOR = "INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR"
ROLE_CONSUMER = "REGISTERED_PREFIX_E1_CONSUMER"
OWNER_ARTIFACT_ID = "q1_root_owner_classifier_v2"
VALIDATOR_ARTIFACT_ID = "q1_scope_aware_e1_validator_v2"
CONSUMER_ARTIFACT_ID = "q1_registered_prefix_e1_consumer_v2"
OWNER_GRANT_ID = "q1_common_root_owner_classifier_grant_v4"
VALIDATOR_GRANT_ID = "q1_scope_aware_e1_validator_grant_v4"
CONSUMER_GRANT_ID = "q1_registered_prefix_e1_consumer_grant_v4"
V4_STATUS = "HEAD_BOUND_Q1_ROOT_PREFIX_SCOPED_E1_AUTHORITY_NO_SUCCESSOR_OR_RECURSION"
V3_MISS_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
V3_MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"
V4_SCOPE_ID = "q1_root_after_gap_3_7_11_registered_prefix_v1"
V4_SCOPE_GAPS = (3, 7, 11)
V4_SCOPE_NEXT = 15
REGULAR_MODES = frozenset({"100644", "100755"})
OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")


class ReceiptVerifierRejectCode(str, Enum):
    INVALID_ROOT = "INVALID_ROOT"
    INVALID_HEAD = "INVALID_HEAD"
    HEAD_BINDING_ERROR = "HEAD_BINDING_ERROR"
    WORKTREE_BINDING_ERROR = "WORKTREE_BINDING_ERROR"
    MODULE_BINDING_ERROR = "MODULE_BINDING_ERROR"
    REGISTRY_ERROR = "REGISTRY_ERROR"
    V3_RECEIPT_ERROR = "V3_RECEIPT_ERROR"
    RECEIPT_TYPE_ERROR = "RECEIPT_TYPE_ERROR"
    RECEIPT_SEAL_ERROR = "RECEIPT_SEAL_ERROR"
    SOURCE_MISMATCH = "SOURCE_MISMATCH"
    WIRE_MISMATCH = "WIRE_MISMATCH"
    AUTHORITY_MISMATCH = "AUTHORITY_MISMATCH"


class ReceiptVerifierError(ValueError):
    def __init__(self, code: ReceiptVerifierRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: ReceiptVerifierRejectCode, detail: str) -> NoReturn:
    raise ReceiptVerifierError(code, detail)


def _json_copy(value: Any, *, path: str = "$") -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, f"{path} key")
            result[key] = _json_copy(child, path=f"{path}.{key}")
        return result
    if type(value) is list:
        return [_json_copy(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, f"{path} contains {type(value).__name__}")


def _canonical(value: Any) -> bytes:
    try:
        return json.dumps(_json_copy(value), ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("ascii")
    except (TypeError, ValueError) as exc:
        raise ReceiptVerifierError(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, str(exc)) from exc


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _run_git(root: Path, args: Sequence[str]) -> bytes:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    result = subprocess.run(["git", *args], cwd=root, check=False, capture_output=True, env=environment)
    if result.returncode:
        _reject(ReceiptVerifierRejectCode.HEAD_BINDING_ERROR, result.stderr.decode(errors="replace").strip())
    return result.stdout


def _repo(locator: Path) -> Path:
    if type(locator) is not type(Path()):
        _reject(ReceiptVerifierRejectCode.INVALID_ROOT, "root must be the exact platform Path type")
    return Path(_run_git(locator.resolve(), ("rev-parse", "--show-toplevel")).decode().strip()).resolve()


def _head(root: Path, requested: str) -> tuple[str, str]:
    fmt = _run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    length = 40 if fmt == "sha1" else 64 if fmt == "sha256" else 0
    if type(requested) is not str or len(requested) != length or not OID_RE.fullmatch(requested):
        _reject(ReceiptVerifierRejectCode.INVALID_HEAD, "requested head is not a full lowercase object ID")
    if _run_git(root, ("cat-file", "-t", requested)).decode().strip() != "commit":
        _reject(ReceiptVerifierRejectCode.INVALID_HEAD, "requested object is not a commit")
    resolved = _run_git(root, ("rev-parse", "--verify", f"{requested}^{{commit}}"))
    if resolved.decode().strip() != requested:
        _reject(ReceiptVerifierRejectCode.INVALID_HEAD, "commit resolution changed")
    return requested, _run_git(root, ("rev-parse", f"{requested}^{{tree}}")).decode().strip()


def _entries(root: Path, head: str) -> dict[str, tuple[str, str, str]]:
    result: dict[str, tuple[str, str, str]] = {}
    for record in _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head)).split(b"\0"):
        if not record:
            continue
        metadata, encoded = record.split(b"\t", 1)
        mode, kind, object_id = metadata.decode("ascii").split(" ")
        path = encoded.decode("utf-8")
        pure = PurePosixPath(path)
        if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
            _reject(ReceiptVerifierRejectCode.HEAD_BINDING_ERROR, path)
        result[path] = (mode, kind, object_id)
    return result


def _blob(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str) -> bytes:
    if type(path) is not str or PATH_RE.fullmatch(path) is None:
        _reject(ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, path)
    item = entries.get(path)
    if item is None or item[0] not in REGULAR_MODES or item[1] != "blob":
        _reject(ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, f"missing regular {path}")
    content = _run_git(root, ("cat-file", "blob", item[2]))
    worktree = root / path
    if worktree.is_symlink() or not worktree.is_file() or worktree.read_bytes() != content:
        _reject(ReceiptVerifierRejectCode.WORKTREE_BINDING_ERROR, path)
    return content


def _fresh(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str, name: str) -> ModuleType:
    content = _blob(root, entries, path)
    module = ModuleType(name)
    module.__file__ = str((root / path).resolve())
    previous = sys.modules.get(name)
    sys.modules[name] = module
    try:
        exec(compile(content, module.__file__, "exec"), module.__dict__)
    except Exception as exc:
        raise ReceiptVerifierError(ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, f"fresh {path}: {exc}") from exc
    finally:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous
    return module


def _call(module: ModuleType, symbol: str) -> Any:
    value = getattr(module, symbol, None)
    if not callable(value) or getattr(value, "__name__", None) != symbol or getattr(value, "__module__", None) != module.__name__:
        _reject(ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, f"missing exact callable {symbol}")
    return value


def _grants(resolved: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    if type(resolved) is not dict or resolved.get("status") != V4_STATUS or resolved.get("authorized_branches") != []:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 resolved status/branches changed")
    if resolved.get("new_role_grant_count") != 3:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 role count changed")
    expected = {
        ROLE_OWNER: (
            OWNER_GRANT_ID,
            OWNER_ARTIFACT_ID,
            OWNER_PATH,
            [OWNER_SYMBOL, OWNER_SERIALIZER],
            ["CLASSIFY_COMMON_Q1_ROOT_OWNER"],
        ),
        ROLE_VALIDATOR: (
            VALIDATOR_GRANT_ID,
            VALIDATOR_ARTIFACT_ID,
            VALIDATOR_PATH,
            [VALIDATOR_SYMBOL, VALIDATOR_SERIALIZER],
            ["VALIDATE_REGISTERED_PREFIX_ROOT_SOURCE_E1_SCOPE"],
        ),
        ROLE_CONSUMER: (
            CONSUMER_GRANT_ID,
            CONSUMER_ARTIFACT_ID,
            CONSUMER_PATH,
            [CONSUMER_SYMBOL, CONSUMER_SERIALIZER],
            ["ISSUE_REGISTERED_PREFIX_ROOT_SOURCE_SCOPED_E1"],
        ),
    }
    artifacts = resolved.get("resolved_artifacts")
    if type(artifacts) is not list:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 resolved artifacts are missing")
    artifact_map = {item.get("artifact_id"): item for item in artifacts if type(item) is dict}
    result: dict[str, dict[str, Any]] = {}
    for item in resolved.get("resolved_role_grants", []):
        if type(item) is not dict or item.get("role") not in expected:
            _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 grant role changed")
        role = item["role"]
        if role in result:
            _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "duplicate V4 role")
        grant_id, artifact_id, expected_path, expected_symbols, expected_capabilities = expected[role]
        wire = item.get("grant_wire")
        required = {"grant_id", "role", "artifact_id", "artifact_path", "artifact_symbols", "capabilities", "authority_class", "artifact_semantic_sha256"}
        artifact = artifact_map.get(artifact_id)
        if artifact is None:
            _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, f"artifact {artifact_id} is missing")
        if type(wire) is not dict or set(wire) != required or wire.get("grant_id") != grant_id or wire.get("artifact_id") != artifact_id or wire.get("role") != role or wire.get("authority_class") != "HEAD_BOUND_EXECUTABLE_CAPABILITY_V4" or wire.get("artifact_path") != expected_path or wire.get("artifact_symbols") != expected_symbols or wire.get("capabilities") != expected_capabilities or wire.get("artifact_semantic_sha256") != artifact.get("semantic_sha256"):
            _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, f"V4 grant wire changed for {role}")
        result[role] = _json_copy(wire)
    if set(result) != set(expected):
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 grants incomplete")
    scope = resolved.get("authorized_consumer_scopes")
    expected_scope = {"scope_id": V4_SCOPE_ID, "owner_domain_id": "ordinary_parentless_q1_g_root_v1", "owner": "type_ii_relation_g_endpoint", "owner_scope": "ROOT_SOURCE_DISPATCH_ONLY", "source_terminal_outcome": V3_MISS_OUTCOME, "coverage_semantics": "REGISTERED_PRIORITY_ONLY", "ordered_gaps": list(V4_SCOPE_GAPS), "next_unchecked_gap": V4_SCOPE_NEXT, "global_exhaustion": False, "remaining_domain_unchecked": True, "same_head_consumption_required": True}
    if scope != [expected_scope]:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 scope changed")
    return result


def _verify_v3(result: Any, *, head: str, receipt: Mapping[str, Any]) -> None:
    if getattr(result, "status", None) != "PRODUCTION_Q1_TERMINAL_RECEIPT_VERIFIED":
        _reject(ReceiptVerifierRejectCode.V3_RECEIPT_ERROR, "V3 receipt status is not verified")
    if getattr(result, "receipt_type", None) != V3_MISS_TYPE or getattr(result, "outcome", None) != V3_MISS_OUTCOME:
        _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, "V3 receipt is not a registered-prefix MISS")
    if receipt.get("head_sha") != head or receipt.get("receipt_type") != V3_MISS_TYPE or receipt.get("outcome") != V3_MISS_OUTCOME:
        _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, "production MISS HEAD/outcome changed")


@dataclass(frozen=True, slots=True)
class RootPrefixScopedE1ReplayResultV2:
    status: str
    receipt_type: str
    receipt_id: str
    receipt_digest: str
    state_id: str
    root_context: int
    wire_match: bool
    authority_verified: bool


def verify_q_one_root_prefix_scoped_e1_receipt_v2(
    *, root: Path, requested_head: str, raw_q_one_g: dict[str, Any], production_miss_receipt: dict[str, Any], receipt: dict[str, Any]
) -> RootPrefixScopedE1ReplayResultV2:
    """Rebuild expected V4 consumer wire and compare the supplied receipt."""
    repository = _repo(root)
    head, tree = _head(repository, requested_head)
    entries = _entries(repository, head)
    verifier_blob = _blob(repository, entries, VERIFIER_PATH)
    executing = Path(__file__)
    expected_verifier_path = (repository / VERIFIER_PATH).resolve()
    if (
        executing.is_symlink()
        or not executing.is_file()
        or executing.resolve() != expected_verifier_path
        or executing.read_bytes() != verifier_blob
    ):
        _reject(ReceiptVerifierRejectCode.WORKTREE_BINDING_ERROR, "replayer is not backed by requested HEAD")
    if type(receipt) is not dict:
        _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, "receipt must be an exact dict")

    v4 = _fresh(repository, entries, V4_RESOLVER_PATH, f"_t6_v4_replay_{head}")
    try:
        resolved = _call(v4, V4_RESOLVER_SYMBOL)(root=repository, requested_head=head)
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, str(exc))
    if resolved.get("head_sha") != head or resolved.get("head_tree_sha") != tree:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 resolver returned another HEAD")
    grants = _grants(resolved)
    artifacts = resolved.get("resolved_artifacts")
    replayer_artifact = (
        next(
            (
                item
                for item in artifacts
                if type(item) is dict
                and item.get("artifact_id") == "q1_root_prefix_scoped_e1_receipt_verifier_v2"
            ),
            None,
        )
        if type(artifacts) is list
        else None
    )
    entry = entries.get(VERIFIER_PATH)
    if replayer_artifact is None or entry is None:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 replayer artifact pin is missing")
    if (
        replayer_artifact.get("path") != VERIFIER_PATH
        or replayer_artifact.get("git_mode") != entry[0]
        or replayer_artifact.get("git_object_id") != entry[2]
        or replayer_artifact.get("blob_sha256") != hashlib.sha256(verifier_blob).hexdigest()
        or replayer_artifact.get("semantic_sha256") != replayer_artifact.get("expected_semantic_sha256")
    ):
        _reject(ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, "running replayer does not match V4 artifact pin")
    v3 = _fresh(repository, entries, V3_VERIFIER_PATH, f"_t6_v3_replay_{head}")
    try:
        v3_result = _call(v3, V3_VERIFIER_SYMBOL)(root=repository, requested_head=head, raw_q_one_g=raw_q_one_g, receipt=production_miss_receipt)
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.V3_RECEIPT_ERROR, str(exc))
    _verify_v3(v3_result, head=head, receipt=production_miss_receipt)
    initializer = _fresh(repository, entries, ROOT_INITIALIZER_PATH, f"_t6_initializer_replay_{head}")
    try:
        body_obj = _call(initializer, "make_canonical_q_one_g_source_body_v2")(raw_q_one_g)
        anchor_obj = _call(initializer, "make_root_initializer_anchor_v2")(body_obj)
        state_obj = _call(initializer, "make_raw_root_source_state_v2")(body_obj, anchor_obj)
        serialize = _call(initializer, "artifact_to_mapping_v2")
        body, anchor, state = serialize(body_obj), serialize(anchor_obj), serialize(state_obj)
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.SOURCE_MISMATCH, str(exc))
    actualness = production_miss_receipt.get("root_actualness")
    if type(actualness) is not dict:
        _reject(ReceiptVerifierRejectCode.SOURCE_MISMATCH, "production receipt lacks actualness mapping")
    owner_module = _fresh(repository, entries, OWNER_PATH, f"_t6_owner_replay_{head}")
    validator_module = _fresh(repository, entries, VALIDATOR_PATH, f"_t6_validator_replay_{head}")
    consumer_module = _fresh(repository, entries, CONSUMER_PATH, f"_t6_consumer_replay_{head}")
    try:
        owner_obj = _call(owner_module, OWNER_SYMBOL)(raw_q_one_g=raw_q_one_g, source_body=body, root_anchor=anchor, source_state=state, root_actualness=actualness, role_grant=grants[ROLE_OWNER])
        owner_wire = _call(owner_module, OWNER_SERIALIZER)(owner_obj)
        validation_obj = _call(validator_module, VALIDATOR_SYMBOL)(raw_q_one_g=raw_q_one_g, source_body=body, root_anchor=anchor, source_state=state, root_actualness=actualness, owner_receipt=owner_wire, terminal_receipt=production_miss_receipt, role_grant=grants[ROLE_VALIDATOR])
        validation_wire = _call(validator_module, VALIDATOR_SERIALIZER)(validation_obj)
        consumer_obj = _call(consumer_module, CONSUMER_SYMBOL)(raw_q_one_g=raw_q_one_g, source_body=body, root_anchor=anchor, source_state=state, root_actualness=actualness, owner_receipt=owner_wire, terminal_receipt=production_miss_receipt, scope_validation_receipt=validation_wire, role_grant=grants[ROLE_CONSUMER])
        expected_wire = _call(consumer_module, CONSUMER_SERIALIZER)(consumer_obj)
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.SOURCE_MISMATCH, str(exc))
    # Recheck the self and role blobs after all fresh executions.  A worktree
    # replacement between the two reads must not turn into a valid receipt.
    for path in (
        VERIFIER_PATH,
        V4_RESOLVER_PATH,
        V3_VERIFIER_PATH,
        ROOT_INITIALIZER_PATH,
        OWNER_PATH,
        VALIDATOR_PATH,
        CONSUMER_PATH,
    ):
        _blob(repository, entries, path)
    if _canonical(receipt) != _canonical(expected_wire):
        _reject(ReceiptVerifierRejectCode.WIRE_MISMATCH, "supplied consumer receipt differs from exact replay")
    for name, expected in {"source_actualness": True, "common_owner_authority": True, "registered_prefix_miss_authority": True, "scope_validation_authority": True, "root_source_scoped_e1": True, "scope_aware_consumer_authority": True, "root_source_occurrence_authority": True, "e1_authority": False, "generic_e1": False, "successor_e1": False, "producer_authority": False, "producer_continuation_allowed": False, "persistent_admission": False, "queue_authority": False, "e2_authority": False, "e3_authority": False, "e4_authority": False, "e5_authority": False, "global_exhaustion": False, "terminal_receipt_direct_continuation_authority": False, "terminal_leaf_authority": False, "root_proof_close_authority": False}.items():
        if type(receipt.get(name)) is not bool or receipt.get(name) is not expected:
            _reject(ReceiptVerifierRejectCode.AUTHORITY_MISMATCH, f"receipt.{name}")
    return RootPrefixScopedE1ReplayResultV2(
        status="Q1_ROOT_PREFIX_SCOPED_E1_RECEIPT_REPLAY_VERIFIED",
        receipt_type=receipt["receipt_type"],
        receipt_id=receipt["receipt_id"],
        receipt_digest=receipt["digest"],
        state_id=receipt["state_id"],
        root_context=receipt["source_state"]["root_context"],
        wire_match=True,
        authority_verified=True,
    )


__all__ = ["ReceiptVerifierError", "ReceiptVerifierRejectCode", "RootPrefixScopedE1ReplayResultV2", "verify_q_one_root_prefix_scoped_e1_receipt_v2"]
