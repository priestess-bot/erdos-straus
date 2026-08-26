#!/usr/bin/env python3
"""Independent exact-HEAD wire replay for a V5 V1 base-admission receipt.

This module never imports or calls the V5 orchestrator.  It fresh-executes the
requested-HEAD V5/V4 resolvers, V3 production verifier, root initializer, V4
owner/scope roles, and V1 adapter/materializer/admission roles.  From raw
integers and one supplied V3 prefix-MISS receipt it rebuilds the only permitted
base-admission wire and compares canonical JSON exactly.

The replay verifies a narrow no-queue receipt.  It does not prove a successor,
producer action, E1--E5 transition, T5 descent, queue mutation, or a global
claim.
"""

from __future__ import annotations

import copy
from contextlib import contextmanager
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


VERIFIER_ID = "q1_root_v1_base_admission_receipt_verifier_v1"
VERIFIER_PATH = "scripts/t6_q_one_root_v1_base_admission_receipt_verifier_v1.py"
ORCHESTRATOR_ID = "q1_root_v1_base_admission_orchestrator_v1"
ORCHESTRATOR_PATH = "scripts/t6_q_one_root_v1_base_admission_orchestrator_v1.py"
V5_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v5.py"
V5_RESOLVER_SYMBOL = "resolve_registry_v5"
V4_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v4.py"
V4_RESOLVER_SYMBOL = "resolve_registry_v4"
V3_VERIFIER_PATH = "scripts/t6_q_one_terminal_receipt_verifier_v1.py"
V3_VERIFIER_SYMBOL = "verify_q_one_production_terminal_receipt_v1"
ROOT_INITIALIZER_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"
V1_STATE_PATH = "scripts/t6_persistent_selector_state_v1.py"
ADAPTER_PATH = "scripts/t6_q_one_root_v1_terminal_adapter_v1.py"
MATERIALIZER_PATH = "scripts/t6_q_one_root_v1_base_materializer_v1.py"
ADMISSION_PATH = "scripts/t6_q_one_root_v1_base_admission_verifier_v1.py"
OWNER_PATH = "scripts/t6_q_one_root_owner_classifier_v2.py"
OWNER_SYMBOL = "classify_q_one_root_owner_v2"
OWNER_SERIALIZER = "root_owner_receipt_to_mapping_v2"
SCOPE_PATH = "scripts/t6_q_one_scope_aware_e1_validator_v2.py"
SCOPE_SYMBOL = "validate_q_one_registered_prefix_e1_scope_v2"
SCOPE_SERIALIZER = "scope_validation_receipt_to_mapping_v2"
MATERIALIZER_SYMBOL = "materialize_q_one_root_v1_base_state_v1"
MATERIALIZER_SERIALIZER = "base_materialization_receipt_to_mapping_v1"
ADMISSION_SYMBOL = "verify_and_admit_q_one_root_v1_base_v1"
ADMISSION_SERIALIZER = "base_admission_receipt_to_mapping_v1"

V5_STATUS = "HEAD_BOUND_Q1_ROOT_V1_BASE_ADMISSION_AUTHORITY_NO_QUEUE_OR_SUCCESSOR"
V4_STATUS = "HEAD_BOUND_Q1_ROOT_PREFIX_SCOPED_E1_AUTHORITY_NO_SUCCESSOR_OR_RECURSION"
V3_MISS_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
V3_MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"

ROLE_MATERIALIZER = "Q1_ROOT_V1_BASE_MATERIALIZER"
ROLE_ADMISSION = "INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER"
MATERIALIZER_ID = "q1_root_v1_base_materializer_v1"
ADMISSION_ID = "q1_root_v1_base_admission_verifier_v1"
MATERIALIZER_GRANT_ID = "q1_root_v1_base_materializer_grant_v1"
ADMISSION_GRANT_ID = "q1_root_v1_base_admission_verifier_grant_v1"
OWNER_ROLE = "COMMON_ROOT_OWNER_CLASSIFIER"
SCOPE_ROLE = "INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR"
OWNER_ID = "q1_root_owner_classifier_v2"
SCOPE_ID = "q1_scope_aware_e1_validator_v2"
OWNER_GRANT_ID = "q1_common_root_owner_classifier_grant_v4"
SCOPE_GRANT_ID = "q1_scope_aware_e1_validator_grant_v4"

REGULAR_MODES = frozenset({"100644", "100755"})
OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")

V5_DENIALS = {
    "queue_authority": False,
    "enqueue_authority": False,
    "successor_authority": False,
    "producer_authority": False,
    "producer_continuation_authority": False,
    "e1_authority": False,
    "e2_authority": False,
    "e3_authority": False,
    "e4_authority": False,
    "e5_authority": False,
    "t5_ticket_authority": False,
    "t5_potential_authority": False,
    "global_exhaustion_authority": False,
    "terminal_leaf_authority": False,
    "generic_owner_authority": False,
    "branch_authority": False,
}
V5_BASE_POLICY = {
    "source_owner": "type_ii_relation_g_endpoint",
    "v1_queue_gate": "ROOT_INITIALIZER_OUTPUT",
    "v3_terminal_type": V3_MISS_TYPE,
    "v3_terminal_outcome": V3_MISS_OUTCOME,
    "coverage_semantics": "REGISTERED_PRIORITY_ONLY",
    "ordered_gaps": [3, 7, 11],
    "next_unchecked_gap": 15,
    "global_exhaustion": False,
    "requires_v4_owner_receipt": True,
    "requires_v4_scope_validation_receipt": True,
    "v1_state_semantic_forbidden_fields": [
        "v4_e1_receipt",
        "v4_e1_candidate",
        "v4_e1_candidate_digest",
        "v4_root_source_scoped_e1",
        "v4_consumer_receipt",
    ],
}


class ReceiptVerifierRejectCode(str, Enum):
    INVALID_ROOT = "INVALID_ROOT"
    INVALID_HEAD = "INVALID_HEAD"
    HEAD_BINDING_ERROR = "HEAD_BINDING_ERROR"
    WORKTREE_BINDING_ERROR = "WORKTREE_BINDING_ERROR"
    MODULE_BINDING_ERROR = "MODULE_BINDING_ERROR"
    REGISTRY_ERROR = "REGISTRY_ERROR"
    V3_RECEIPT_ERROR = "V3_RECEIPT_ERROR"
    TERMINAL_SOURCE_NOT_MISS = "TERMINAL_SOURCE_NOT_MISS"
    ROLE_GRANT_ERROR = "ROLE_GRANT_ERROR"
    SOURCE_MISMATCH = "SOURCE_MISMATCH"
    RECEIPT_TYPE_ERROR = "RECEIPT_TYPE_ERROR"
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
                _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, f"{path} key is not a string")
            result[key] = _json_copy(child, path=f"{path}.{key}")
        return result
    if type(value) is list:
        return [_json_copy(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, f"{path} contains {type(value).__name__}")


def _mapping(value: Any, name: str) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, f"{name} must be an exact dict")
    return _json_copy(value, path=name)


def _canonical(value: Any) -> bytes:
    try:
        return json.dumps(
            _json_copy(value),
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("ascii")
    except (TypeError, ValueError) as exc:
        raise ReceiptVerifierError(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, str(exc)) from exc


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _run_git(root: Path, args: Sequence[str]) -> bytes:
    environment = {
        key: value for key, value in os.environ.items() if not key.startswith("GIT_")
    }
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(
        ["git", *args], cwd=root, check=False, capture_output=True, env=environment
    )
    if completed.returncode:
        _reject(
            ReceiptVerifierRejectCode.HEAD_BINDING_ERROR,
            completed.stderr.decode(errors="replace").strip(),
        )
    return completed.stdout


@contextmanager
def _sanitized_git_environment() -> Any:
    """Keep fresh V3/V4 modules from inheriting caller-controlled Git routing."""

    inherited = {
        key: value for key, value in os.environ.items() if key.startswith("GIT_")
    }
    for key in inherited:
        os.environ.pop(key, None)
    os.environ["GIT_NO_REPLACE_OBJECTS"] = "1"
    try:
        yield
    finally:
        os.environ.pop("GIT_NO_REPLACE_OBJECTS", None)
        os.environ.update(inherited)


def _repository_root(locator: Path) -> Path:
    if type(locator) is not type(Path()):
        _reject(ReceiptVerifierRejectCode.INVALID_ROOT, "root must be the exact platform Path type")
    try:
        return Path(
            _run_git(locator.resolve(), ("rev-parse", "--show-toplevel")).decode().strip()
        ).resolve()
    except (OSError, UnicodeDecodeError) as exc:
        raise ReceiptVerifierError(ReceiptVerifierRejectCode.INVALID_ROOT, str(exc)) from exc


def _exact_head(root: Path, requested_head: str) -> tuple[str, str]:
    object_format = _run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    length = 40 if object_format == "sha1" else 64 if object_format == "sha256" else 0
    if (
        type(requested_head) is not str
        or len(requested_head) != length
        or OID_RE.fullmatch(requested_head) is None
    ):
        _reject(ReceiptVerifierRejectCode.INVALID_HEAD, "requested_head must be a full lowercase commit ID")
    if _run_git(root, ("cat-file", "-t", requested_head)).decode().strip() != "commit":
        _reject(ReceiptVerifierRejectCode.INVALID_HEAD, "requested object is not a commit")
    resolved = _run_git(root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}"))
    if resolved.decode().strip() != requested_head:
        _reject(ReceiptVerifierRejectCode.INVALID_HEAD, "commit resolution changed")
    return requested_head, _run_git(root, ("rev-parse", f"{requested_head}^{{tree}}")).decode().strip()


def _tree_entries(root: Path, head: str) -> dict[str, tuple[str, str, str]]:
    result: dict[str, tuple[str, str, str]] = {}
    raw = _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head))
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, encoded_path = record.split(b"\t", 1)
        mode, kind, object_id = metadata.decode("ascii").split(" ")
        path = encoded_path.decode("utf-8")
        pure = PurePosixPath(path)
        if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
            _reject(ReceiptVerifierRejectCode.HEAD_BINDING_ERROR, f"unsafe tree path {path!r}")
        if path in result:
            _reject(ReceiptVerifierRejectCode.HEAD_BINDING_ERROR, f"duplicate tree path {path!r}")
        result[path] = (mode, kind, object_id)
    return result


def _blob(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str) -> bytes:
    if type(path) is not str or PATH_RE.fullmatch(path) is None:
        _reject(ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, f"unsafe path {path!r}")
    entry = entries.get(path)
    if entry is None or entry[0] not in REGULAR_MODES or entry[1] != "blob":
        _reject(ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, f"missing regular blob {path}")
    content = _run_git(root, ("cat-file", "blob", entry[2]))
    worktree = root / path
    if worktree.is_symlink() or not worktree.is_file() or worktree.read_bytes() != content:
        _reject(ReceiptVerifierRejectCode.WORKTREE_BINDING_ERROR, path)
    return content


def _fresh(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    path: str,
    name: str,
) -> ModuleType:
    content = _blob(root, entries, path)
    module = ModuleType(name)
    module.__file__ = str((root / path).resolve())
    previous = sys.modules.get(name)
    sys.modules[name] = module
    try:
        exec(compile(content, module.__file__, "exec"), module.__dict__)
    except Exception as exc:
        raise ReceiptVerifierError(
            ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, f"fresh {path}: {exc}"
        ) from exc
    finally:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous
    return module


def _fresh_v1_bundle(
    root: Path, entries: Mapping[str, tuple[str, str, str]], head: str, label: str
) -> dict[str, ModuleType]:
    """Execute V1 local imports from exact blobs despite stale ``sys.modules`` slots."""

    specs = (
        ("t6_persistent_selector_state_v1", V1_STATE_PATH, "state"),
        ("t6_q_one_root_initializer_envelope_v2", ROOT_INITIALIZER_PATH, "initializer"),
        ("t6_q_one_root_v1_terminal_adapter_v1", ADAPTER_PATH, "adapter"),
        (f"_t6_v5_materializer_{label}_{head}", MATERIALIZER_PATH, "materializer"),
        (f"_t6_v5_admission_{label}_{head}", ADMISSION_PATH, "admission"),
    )
    sentinel = object()
    previous: dict[str, object] = {}
    result: dict[str, ModuleType] = {}
    try:
        for module_name, path, key in specs:
            previous[module_name] = sys.modules.get(module_name, sentinel)
            content = _blob(root, entries, path)
            module = ModuleType(module_name)
            module.__file__ = str((root / path).resolve())
            sys.modules[module_name] = module
            try:
                exec(compile(content, module.__file__, "exec"), module.__dict__)
            except Exception as exc:
                raise ReceiptVerifierError(
                    ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, f"fresh {path}: {exc}"
                ) from exc
            result[key] = module
    finally:
        for module_name, _path, _key in reversed(specs):
            prior = previous.get(module_name, sentinel)
            if prior is sentinel:
                sys.modules.pop(module_name, None)
            else:
                sys.modules[module_name] = prior
    return result


def _call(module: ModuleType, symbol: str) -> Any:
    value = getattr(module, symbol, None)
    if (
        not callable(value)
        or getattr(value, "__name__", None) != symbol
        or getattr(value, "__module__", None) != module.__name__
    ):
        _reject(ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, f"missing exact callable {symbol}")
    return value


def _artifact_map(resolved: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    artifacts = resolved.get("resolved_artifacts")
    if type(artifacts) is not list:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "resolved artifacts are missing")
    result: dict[str, dict[str, Any]] = {}
    for artifact in artifacts:
        if type(artifact) is not dict or type(artifact.get("artifact_id")) is not str:
            _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "malformed resolved artifact")
        artifact_id = artifact["artifact_id"]
        if artifact_id in result:
            _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, f"duplicate artifact {artifact_id}")
        result[artifact_id] = _json_copy(artifact)
    return result


def _check_artifact(
    artifacts: Mapping[str, Mapping[str, Any]],
    entries: Mapping[str, tuple[str, str, str]],
    root: Path,
    artifact_id: str,
    path: str,
) -> None:
    artifact = artifacts.get(artifact_id)
    entry = entries.get(path)
    content = _blob(root, entries, path)
    if artifact is None or entry is None:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, f"missing artifact pin {artifact_id}")
    if (
        artifact.get("path") != path
        or artifact.get("git_mode") != entry[0]
        or artifact.get("git_object_id") != entry[2]
        or artifact.get("blob_sha256") != hashlib.sha256(content).hexdigest()
        or artifact.get("semantic_sha256") != artifact.get("expected_semantic_sha256")
    ):
        _reject(ReceiptVerifierRejectCode.MODULE_BINDING_ERROR, f"artifact pin mismatch {artifact_id}")


def _v5_grants(resolved: Mapping[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    if type(resolved) is not dict:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V5 resolver output is not an exact dict")
    if (
        resolved.get("status") != V5_STATUS
        or resolved.get("authorized_branches") != []
        or resolved.get("authority_denials") != V5_DENIALS
        or resolved.get("base_admission_policy") != V5_BASE_POLICY
    ):
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V5 policy boundary changed")
    if (
        resolved.get("new_role_grant_count") != 2
        or resolved.get("inherited_v4_role_capability_count") != 3
        or resolved.get("effective_role_capability_count") != 5
        or resolved.get("queue_mutator_count") != 0
        or resolved.get("successor_producer_count") != 0
    ):
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V5 role or mutation counts changed")
    artifacts = _artifact_map(resolved)
    expected = {
        ROLE_MATERIALIZER: (
            MATERIALIZER_GRANT_ID,
            MATERIALIZER_ID,
            MATERIALIZER_PATH,
            [MATERIALIZER_SYMBOL, MATERIALIZER_SERIALIZER],
            ["MATERIALIZE_Q1_G_V1_ROOT_INITIALIZER_OUTPUT"],
        ),
        ROLE_ADMISSION: (
            ADMISSION_GRANT_ID,
            ADMISSION_ID,
            ADMISSION_PATH,
            [ADMISSION_SYMBOL, ADMISSION_SERIALIZER],
            ["ISSUE_Q1_G_V1_BASE_ADMISSION_NO_QUEUE"],
        ),
    }
    raw_grants = resolved.get("resolved_role_grants")
    if type(raw_grants) is not list or len(raw_grants) != len(expected):
        _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, "V5 grant cardinality changed")
    grants: dict[str, dict[str, Any]] = {}
    required = {
        "grant_id",
        "role",
        "artifact_id",
        "artifact_path",
        "artifact_symbols",
        "capabilities",
        "authority_class",
        "artifact_semantic_sha256",
    }
    for item in raw_grants:
        if type(item) is not dict or item.get("role") not in expected:
            _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, "V5 grant role changed")
        role = item["role"]
        if role in grants:
            _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, f"duplicate V5 role {role}")
        grant_id, artifact_id, path, symbols, capabilities = expected[role]
        wire = item.get("grant_wire")
        artifact = artifacts.get(artifact_id)
        if artifact is None or type(wire) is not dict:
            _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, f"missing V5 grant wire {role}")
        if (
            set(wire) != required
            or wire.get("grant_id") != grant_id
            or wire.get("role") != role
            or wire.get("artifact_id") != artifact_id
            or wire.get("artifact_path") != path
            or wire.get("artifact_symbols") != symbols
            or wire.get("capabilities") != capabilities
            or wire.get("authority_class") != "HEAD_BOUND_EXECUTABLE_CAPABILITY_V5"
            or wire.get("artifact_semantic_sha256") != artifact.get("semantic_sha256")
        ):
            _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, f"V5 grant wire changed {role}")
        grants[role] = _json_copy(wire)
    if set(grants) != set(expected):
        _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, "V5 grants incomplete")
    manifest = resolved.get("role_authority_manifest")
    if (
        type(manifest) is not dict
        or manifest.get("head_sha") != resolved.get("head_sha")
        or manifest.get("status") != V5_STATUS
        or manifest.get("v4_registry_digest") != resolved.get("v4_cross_registry_digest")
        or manifest.get("grants") != raw_grants
        or manifest.get("authority_denials") != V5_DENIALS
        or type(manifest.get("digest")) is not str
        or manifest.get("digest") != _digest({key: value for key, value in manifest.items() if key != "digest"})
    ):
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V5 role manifest changed")
    return artifacts, grants


def _v4_grants(resolved: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    if type(resolved) is not dict or resolved.get("status") != V4_STATUS:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 status changed")
    if resolved.get("authorized_branches") != [] or resolved.get("new_role_grant_count") != 3:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 role boundary changed")
    expected = {
        OWNER_ROLE: (
            OWNER_GRANT_ID,
            OWNER_ID,
            OWNER_PATH,
            [OWNER_SYMBOL, OWNER_SERIALIZER],
            ["CLASSIFY_COMMON_Q1_ROOT_OWNER"],
        ),
        SCOPE_ROLE: (
            SCOPE_GRANT_ID,
            SCOPE_ID,
            SCOPE_PATH,
            [SCOPE_SYMBOL, SCOPE_SERIALIZER],
            ["VALIDATE_REGISTERED_PREFIX_ROOT_SOURCE_E1_SCOPE"],
        ),
    }
    artifacts = _artifact_map(resolved)
    result: dict[str, dict[str, Any]] = {}
    required = {
        "grant_id",
        "role",
        "artifact_id",
        "artifact_path",
        "artifact_symbols",
        "capabilities",
        "authority_class",
        "artifact_semantic_sha256",
    }
    raw_grants = resolved.get("resolved_role_grants")
    if type(raw_grants) is not list:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 grants missing")
    for item in raw_grants:
        if type(item) is not dict or item.get("role") not in expected:
            continue
        role = item["role"]
        if role in result:
            _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, f"duplicate V4 role {role}")
        grant_id, artifact_id, path, symbols, capabilities = expected[role]
        wire = item.get("grant_wire")
        artifact = artifacts.get(artifact_id)
        if artifact is None or type(wire) is not dict:
            _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, f"missing V4 grant {role}")
        if (
            set(wire) != required
            or wire.get("grant_id") != grant_id
            or wire.get("role") != role
            or wire.get("artifact_id") != artifact_id
            or wire.get("artifact_path") != path
            or wire.get("artifact_symbols") != symbols
            or wire.get("capabilities") != capabilities
            or wire.get("authority_class") != "HEAD_BOUND_EXECUTABLE_CAPABILITY_V4"
            or wire.get("artifact_semantic_sha256") != artifact.get("semantic_sha256")
        ):
            _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, f"V4 grant wire changed {role}")
        result[role] = _json_copy(wire)
    if set(result) != set(expected):
        _reject(ReceiptVerifierRejectCode.ROLE_GRANT_ERROR, "V4 owner/scope grants incomplete")
    return result


def _verify_v3_result(result: Any, *, head: str, receipt: Mapping[str, Any]) -> None:
    if getattr(result, "status", None) != "PRODUCTION_Q1_TERMINAL_RECEIPT_VERIFIED":
        _reject(ReceiptVerifierRejectCode.V3_RECEIPT_ERROR, "V3 production receipt was not verified")
    if (
        getattr(result, "receipt_type", None) != V3_MISS_TYPE
        or getattr(result, "outcome", None) != V3_MISS_OUTCOME
    ):
        _reject(ReceiptVerifierRejectCode.TERMINAL_SOURCE_NOT_MISS, "only a V3 prefix MISS may enter V5")
    if (
        receipt.get("head_sha") != head
        or receipt.get("receipt_type") != V3_MISS_TYPE
        or receipt.get("outcome") != V3_MISS_OUTCOME
    ):
        _reject(ReceiptVerifierRejectCode.TERMINAL_SOURCE_NOT_MISS, "V3 MISS HEAD/outcome changed")


def _check_v4_evidence(owner: Mapping[str, Any], scope: Mapping[str, Any]) -> None:
    owner_expected = {
        "source_actualness": True,
        "common_owner_authority": True,
        "persistent_admission": False,
        "queue_authority": False,
        "e1_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "global_exhaustion": False,
    }
    scope_expected = {
        "source_actualness": True,
        "registered_prefix_miss_authority": True,
        "scope_validation_authority": True,
        "root_source_scoped_e1": False,
        "scope_aware_consumer_authority": False,
        "persistent_admission": False,
        "queue_authority": False,
        "e1_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "global_exhaustion": False,
    }
    for label, receipt, expected in (("owner", owner, owner_expected), ("scope", scope, scope_expected)):
        if type(receipt) is not dict:
            _reject(ReceiptVerifierRejectCode.SOURCE_MISMATCH, f"V4 {label} serializer returned non-dict")
        for field, wanted in expected.items():
            if type(receipt.get(field)) is not bool or receipt.get(field) is not wanted:
                _reject(ReceiptVerifierRejectCode.AUTHORITY_MISMATCH, f"V4 {label}.{field} changed")


def _contains_forbidden_key(value: Any, forbidden: set[str]) -> bool:
    if type(value) is dict:
        return any(key in forbidden or _contains_forbidden_key(child, forbidden) for key, child in value.items())
    if type(value) is list:
        return any(_contains_forbidden_key(child, forbidden) for child in value)
    return False


def _check_final_authority(receipt: Mapping[str, Any]) -> None:
    if type(receipt) is not dict:
        _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, "admission serializer returned non-dict")
    required = {
        "receipt_type": "Q1_ROOT_V1_BASE_ADMISSION_RECEIPT_V1",
        "status": "V1_ROOT_INITIALIZER_BASE_ADMISSION_ISSUED_NO_QUEUE",
        "role": ROLE_ADMISSION,
        "admission_decision": "ACCEPT",
        "admission_reason": "ACCEPT",
        "owner": "type_ii_relation_g_endpoint",
        "precedence_index": 2,
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
    for field, expected in required.items():
        value = receipt.get(field)
        if type(expected) is bool:
            if type(value) is not bool or value is not expected:
                _reject(ReceiptVerifierRejectCode.AUTHORITY_MISMATCH, f"receipt.{field} changed")
        elif value != expected:
            _reject(ReceiptVerifierRejectCode.AUTHORITY_MISMATCH, f"receipt.{field} changed")
    state = receipt.get("v1_state")
    if type(state) is not dict or state.get("queue_gate") != "ROOT_INITIALIZER_OUTPUT":
        _reject(ReceiptVerifierRejectCode.SOURCE_MISMATCH, "receipt no longer describes a V1 root initializer")
    forbidden = set(V5_BASE_POLICY["v1_state_semantic_forbidden_fields"])
    materialization = receipt.get("materialization_receipt")
    if (
        _contains_forbidden_key(state, forbidden)
        or type(materialization) is not dict
        or _contains_forbidden_key(materialization.get("v1_state"), forbidden)
    ):
        _reject(ReceiptVerifierRejectCode.AUTHORITY_MISMATCH, "V4 E1/candidate data entered V1 state semantics")


def _recheck_paths(root: Path, entries: Mapping[str, tuple[str, str, str]]) -> None:
    for path in (
        VERIFIER_PATH,
        ORCHESTRATOR_PATH,
        V5_RESOLVER_PATH,
        V4_RESOLVER_PATH,
        V3_VERIFIER_PATH,
        ROOT_INITIALIZER_PATH,
        V1_STATE_PATH,
        ADAPTER_PATH,
        MATERIALIZER_PATH,
        ADMISSION_PATH,
        OWNER_PATH,
        SCOPE_PATH,
        "data/t6-wave1/t6-coordinator-role-registry-v5.json",
        "schemas/t6-coordinator-role-registry-v5.schema.json",
        "schemas/t6-q-one-root-v1-base-admission-v1.schema.json",
    ):
        _blob(root, entries, path)


@dataclass(frozen=True, slots=True)
class QOneRootV1BaseAdmissionReplayResultV1:
    status: str
    receipt_type: str
    receipt_id: str
    receipt_digest: str
    v1_state_id: str
    root_context: int
    wire_match: bool
    authority_verified: bool

    @property
    def state_id(self) -> str:
        """Compatibility alias for replay callers that use the V4 result shape."""

        return self.v1_state_id


def verify_q_one_root_v1_base_admission_receipt_v1(
    *,
    root: Path,
    requested_head: str,
    raw_q_one_g: dict[str, Any],
    production_miss_receipt: dict[str, Any],
    receipt: dict[str, Any],
) -> QOneRootV1BaseAdmissionReplayResultV1:
    """Independently rebuild the V5 base receipt and compare its complete wire."""

    repository = _repository_root(root)
    head, tree = _exact_head(repository, requested_head)
    entries = _tree_entries(repository, head)
    own_blob = _blob(repository, entries, VERIFIER_PATH)
    executing = Path(__file__)
    expected_path = (repository / VERIFIER_PATH).resolve()
    if (
        executing.is_symlink()
        or not executing.is_file()
        or executing.resolve() != expected_path
        or executing.read_bytes() != own_blob
    ):
        _reject(ReceiptVerifierRejectCode.WORKTREE_BINDING_ERROR, "replayer is not backed by requested HEAD")
    raw = _mapping(raw_q_one_g, "raw_q_one_g")
    terminal = _mapping(production_miss_receipt, "production_miss_receipt")
    supplied = _mapping(receipt, "receipt")
    if supplied.get("receipt_type") != "Q1_ROOT_V1_BASE_ADMISSION_RECEIPT_V1":
        _reject(ReceiptVerifierRejectCode.RECEIPT_TYPE_ERROR, "wrong V5 receipt type")

    v5_module = _fresh(repository, entries, V5_RESOLVER_PATH, f"_t6_v5_replay_{head}")
    try:
        with _sanitized_git_environment():
            resolved_v5 = _call(v5_module, V5_RESOLVER_SYMBOL)(
                root=repository, requested_head=head
            )
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, f"V5 resolver rejected HEAD: {exc}")
    if resolved_v5.get("head_sha") != head or resolved_v5.get("head_tree_sha") != tree:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V5 resolver returned another HEAD")
    artifacts_v5, grants_v5 = _v5_grants(resolved_v5)
    _check_artifact(artifacts_v5, entries, repository, VERIFIER_ID, VERIFIER_PATH)
    # The orchestrator is a binding dependency only: inspect its exact pin but
    # never import or execute it from this independent replay path.
    _check_artifact(artifacts_v5, entries, repository, ORCHESTRATOR_ID, ORCHESTRATOR_PATH)
    for artifact_id, path in (
        (MATERIALIZER_ID, MATERIALIZER_PATH),
        (ADMISSION_ID, ADMISSION_PATH),
        ("q1_root_v1_terminal_adapter_v1", ADAPTER_PATH),
        ("v1_persistent_state_contract_dependency", V1_STATE_PATH),
        ("v3_production_receipt_verifier_dependency", V3_VERIFIER_PATH),
        ("v3_root_initializer_dependency", ROOT_INITIALIZER_PATH),
        ("v4_owner_classifier_dependency", OWNER_PATH),
        ("v4_registry_resolver_dependency", V4_RESOLVER_PATH),
        ("v4_scope_validator_dependency", SCOPE_PATH),
    ):
        _check_artifact(artifacts_v5, entries, repository, artifact_id, path)

    v4_module = _fresh(repository, entries, V4_RESOLVER_PATH, f"_t6_v4_for_v5_replay_{head}")
    try:
        with _sanitized_git_environment():
            resolved_v4 = _call(v4_module, V4_RESOLVER_SYMBOL)(
                root=repository, requested_head=head
            )
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, f"V4 resolver rejected HEAD: {exc}")
    if resolved_v4.get("head_sha") != head or resolved_v4.get("head_tree_sha") != tree:
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V4 resolver returned another HEAD")
    if (
        resolved_v5.get("v4_cross_registry_digest") != resolved_v4.get("registry_digest")
        or resolved_v5.get("v4_role_manifest_digest")
        != resolved_v4.get("role_authority_manifest", {}).get("digest")
    ):
        _reject(ReceiptVerifierRejectCode.REGISTRY_ERROR, "V5/V4 cross-registry binding changed")
    grants_v4 = _v4_grants(resolved_v4)

    v3_module = _fresh(repository, entries, V3_VERIFIER_PATH, f"_t6_v3_for_v5_replay_{head}")
    try:
        with _sanitized_git_environment():
            v3_result = _call(v3_module, V3_VERIFIER_SYMBOL)(
                root=repository,
                requested_head=head,
                raw_q_one_g=raw,
                receipt=terminal,
            )
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.V3_RECEIPT_ERROR, f"V3 production receipt rejected: {exc}")
    _verify_v3_result(v3_result, head=head, receipt=terminal)

    modules = _fresh_v1_bundle(repository, entries, head, "replay")
    initializer = modules["initializer"]
    try:
        serialize_initializer = _call(initializer, "artifact_to_mapping_v2")
        body_obj = _call(initializer, "make_canonical_q_one_g_source_body_v2")(raw)
        anchor_obj = _call(initializer, "make_root_initializer_anchor_v2")(body_obj)
        state_obj = _call(initializer, "make_raw_root_source_state_v2")(body_obj, anchor_obj)
        body = serialize_initializer(body_obj)
        anchor = serialize_initializer(anchor_obj)
        source_state = serialize_initializer(state_obj)
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.SOURCE_MISMATCH, f"root initializer rejected raw source: {exc}")
    actualness = terminal.get("root_actualness")
    if type(actualness) is not dict or actualness.get("head_sha") != head:
        _reject(ReceiptVerifierRejectCode.SOURCE_MISMATCH, "V3 receipt lacks same-HEAD actualness")
    actualness = _json_copy(actualness, path="production_miss_receipt.root_actualness")

    owner_module = _fresh(repository, entries, OWNER_PATH, f"_t6_v4_owner_for_v5_replay_{head}")
    scope_module = _fresh(repository, entries, SCOPE_PATH, f"_t6_v4_scope_for_v5_replay_{head}")
    try:
        owner_obj = _call(owner_module, OWNER_SYMBOL)(
            raw_q_one_g=raw,
            source_body=body,
            root_anchor=anchor,
            source_state=source_state,
            root_actualness=actualness,
            role_grant=grants_v4[OWNER_ROLE],
        )
        owner_wire = _call(owner_module, OWNER_SERIALIZER)(owner_obj)
        scope_obj = _call(scope_module, SCOPE_SYMBOL)(
            raw_q_one_g=raw,
            source_body=body,
            root_anchor=anchor,
            source_state=source_state,
            root_actualness=actualness,
            owner_receipt=owner_wire,
            terminal_receipt=terminal,
            role_grant=grants_v4[SCOPE_ROLE],
        )
        scope_wire = _call(scope_module, SCOPE_SERIALIZER)(scope_obj)
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.SOURCE_MISMATCH, f"V4 owner/scope evidence rejected source: {exc}")
    _check_v4_evidence(owner_wire, scope_wire)

    materializer = modules["materializer"]
    admission = modules["admission"]
    try:
        materialization_obj = _call(materializer, MATERIALIZER_SYMBOL)(
            raw_q_one_g=raw,
            source_body=body,
            root_anchor=anchor,
            source_state=source_state,
            root_actualness=actualness,
            terminal_receipt=terminal,
            role_grant=grants_v5[ROLE_MATERIALIZER],
        )
        materialization_wire = _call(materializer, MATERIALIZER_SERIALIZER)(materialization_obj)
        admission_obj = _call(admission, ADMISSION_SYMBOL)(
            raw_q_one_g=raw,
            source_body=body,
            root_anchor=anchor,
            source_state=source_state,
            root_actualness=actualness,
            terminal_receipt=terminal,
            materialization_receipt=materialization_wire,
            v4_owner_receipt=owner_wire,
            v4_scope_receipt=scope_wire,
            role_grant=grants_v5[ROLE_ADMISSION],
        )
        expected_wire = _call(admission, ADMISSION_SERIALIZER)(admission_obj)
    except Exception as exc:
        _reject(ReceiptVerifierRejectCode.SOURCE_MISMATCH, f"V5 base-admission chain rejected source: {exc}")
    _check_final_authority(expected_wire)
    _recheck_paths(repository, entries)
    if _canonical(supplied) != _canonical(expected_wire):
        _reject(ReceiptVerifierRejectCode.WIRE_MISMATCH, "supplied base-admission receipt differs from exact replay")
    _check_final_authority(supplied)
    return QOneRootV1BaseAdmissionReplayResultV1(
        status="Q1_ROOT_V1_BASE_ADMISSION_RECEIPT_REPLAY_VERIFIED",
        receipt_type=supplied["receipt_type"],
        receipt_id=supplied["receipt_id"],
        receipt_digest=supplied["digest"],
        v1_state_id=supplied["v1_state_id"],
        root_context=supplied["v1_state"]["root_context"],
        wire_match=True,
        authority_verified=True,
    )


__all__ = [
    "QOneRootV1BaseAdmissionReplayResultV1",
    "ReceiptVerifierError",
    "ReceiptVerifierRejectCode",
    "verify_q_one_root_v1_base_admission_receipt_v1",
]
