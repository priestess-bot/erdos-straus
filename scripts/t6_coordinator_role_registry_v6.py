#!/usr/bin/env python3
"""Exact-HEAD registry for a V6 q=1 source-input replay candidate.

The registry binds V3/V4/V5 records and the V6 rebind role to one selected Git
tree, but it authorizes no serializable source assertion.  Its outputs are
candidate data only; the independent replayer is the sole component that can
report a successful exact-HEAD verification at runtime.
"""

from __future__ import annotations

from contextlib import contextmanager
import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from types import ModuleType
from typing import Any, Mapping, NoReturn, Sequence

import jsonschema


REGISTRY_ID = "t6_coordinator_role_registry_v6"
REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v6.json"
SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v6.schema.json"
RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v6.py"
RESOLVED_SCHEMA_ID = "t6_coordinator_role_registry_resolved_v6"
STATUS = "HEAD_BOUND_Q1_EXACT_SOURCE_INPUT_CANDIDATE_REPLAY_ONLY"
ACTIVE = "ACTIVE"

V3_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v3.py"
V3_RESOLVER_SYMBOL = "resolve_registry_v3"
V4_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v4.py"
V4_RESOLVER_SYMBOL = "resolve_registry_v4"
V5_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v5.py"
V5_RESOLVER_SYMBOL = "resolve_registry_v5"

V3_STATUS = "HEAD_BOUND_Q1_ROOT_TERMINAL_DECISION_AUTHORITY_NO_RECURSION"
V4_STATUS = "HEAD_BOUND_Q1_ROOT_PREFIX_SCOPED_E1_AUTHORITY_NO_SUCCESSOR_OR_RECURSION"
V5_STATUS = "HEAD_BOUND_Q1_ROOT_V1_BASE_ADMISSION_AUTHORITY_NO_QUEUE_OR_SUCCESSOR"

BINDER_ID = "q1_exact_head_source_input_binder_v1"
BINDER_PATH = "scripts/t6_q_one_exact_head_source_input_v1.py"
BINDER_SYMBOLS = (
    "bind_exact_head_q_one_actual_source_input_v1",
    "exact_head_q_one_actual_source_input_to_mapping_v1",
)
BINDER_GRANT_ID = "q1_exact_head_q_one_source_input_binder_grant_v1"
BINDER_ROLE = "EXACT_HEAD_Q1_ACTUAL_SOURCE_INPUT_BINDER"
BINDER_CAPABILITIES = ("BUILD_EXACT_HEAD_Q1_SOURCE_INPUT_REPLAY_CANDIDATE",)
BINDER_AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V6_CANDIDATE_ONLY"

REBIND_ID = "q1_root_source_scoped_e1_rebind_v1"
REBIND_PATH = "scripts/t6_q_one_root_source_scoped_e1_rebind_v1.py"
REBIND_SYMBOLS = (
    "rebind_q_one_root_source_scoped_e1_v1",
    "root_source_scoped_e1_rebind_receipt_to_mapping_v1",
)
REBIND_GRANT_ID = "q1_root_source_scoped_e1_rebind_grant_v1"
REBIND_ROLE = "INDEPENDENT_Q1_ROOT_SOURCE_SCOPED_E1_REBINDER"
REBIND_CAPABILITIES = ("REBIND_ROOT_SOURCE_SCOPED_E1_TO_V1_BASE_SOURCE",)
REBIND_AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V6"

ORCHESTRATOR_ID = "q1_exact_head_source_input_orchestrator_v1"
ORCHESTRATOR_PATH = "scripts/t6_q_one_exact_head_source_input_orchestrator_v1.py"
ORCHESTRATOR_SYMBOLS = ("assemble_exact_head_q_one_actual_source_input_v1",)
REPLAYER_ID = "q1_exact_head_source_input_receipt_replayer_v1"
REPLAYER_PATH = "scripts/t6_q_one_exact_head_source_input_receipt_replayer_v1.py"
REPLAYER_SYMBOLS = ("verify_exact_head_q_one_actual_source_input_v1",)
PRESTATE_ID = "q1_phase_root_prestate_v2_projection_dependency"
PRESTATE_PATH = "scripts/t6_q_one_phase_root_prestate_v2.py"
PRESTATE_SYMBOLS = ("make_external_q_one_source_binding_v2", "artifact_to_mapping_v2")

IDENTITIES = (
    (BINDER_ID, "ROLE_ARTIFACT", BINDER_PATH, BINDER_SYMBOLS),
    (ORCHESTRATOR_ID, "CONTROLLED_LOADER_ORCHESTRATOR_ONLY", ORCHESTRATOR_PATH, ORCHESTRATOR_SYMBOLS),
    (PRESTATE_ID, "EXTERNAL_BINDING_PROJECTION_ONLY", PRESTATE_PATH, PRESTATE_SYMBOLS),
    (REBIND_ID, "ROLE_ARTIFACT", REBIND_PATH, REBIND_SYMBOLS),
    (REPLAYER_ID, "POST_ISSUANCE_REPLAY_DEPENDENCY_ONLY", REPLAYER_PATH, REPLAYER_SYMBOLS),
)
ROLE_BINDINGS = {
    BINDER_GRANT_ID: (BINDER_ROLE, BINDER_ID, BINDER_CAPABILITIES, BINDER_AUTHORITY_CLASS),
    REBIND_GRANT_ID: (REBIND_ROLE, REBIND_ID, REBIND_CAPABILITIES, REBIND_AUTHORITY_CLASS),
}

AUTHORITY_POLICY = {
    "source": "TRACKED_GIT_OBJECTS_AT_EXACT_REQUESTED_HEAD",
    "caller_override_authority": False,
    "worktree_authority": False,
    "external_review_condition": "REPOSITORY_SELECTED_EXACT_HEAD_REQUIRED",
    "candidate_scope": "EXACT_HEAD_Q1_ROOT_SOURCE_INPUT_REPLAY_CANDIDATE_NOT_E1",
    "new_roles": [BINDER_ROLE, REBIND_ROLE],
    "static_artifact_pin_policy": "EXACT_HEAD_GIT_OBJECT_AND_WORKTREE_BINDING_ONLY",
}
ORCHESTRATION_POLICY = {
    "caller_inputs": ["repository_locator", "requested_head", "raw_q_one_g", "production_miss_receipt"],
    "caller_supplied_grants": False,
    "caller_supplied_v4_v5_v6_receipts": False,
    "required_replay_order": ["V3", "V4", "V5", "V6", "SOURCE_INPUT_CANDIDATE", "EXTERNAL_BINDING_V2"],
}
POST_ISSUANCE_REPLAY_POLICY = {
    "orchestrator_import_allowed": False,
    "issuer_import_allowed": False,
    "independent_wire_reconstruction": True,
    "replay_order": ["V3", "V4", "V5", "V6", "SOURCE_INPUT_CANDIDATE", "EXTERNAL_BINDING_V2"],
}
AUTHORITY_DENIALS = {
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
    "global_exhaustion": False,
}
CROSS_REGISTRY_POLICY = {
    "v3": {"registry_id": "t6_coordinator_role_registry_v3", "status": V3_STATUS},
    "v4": {"registry_id": "t6_coordinator_role_registry_v4", "status": V4_STATUS},
    "v5": {"registry_id": "t6_coordinator_role_registry_v5", "status": V5_STATUS},
}

REGULAR_MODES = frozenset({"100644", "100755"})
OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")


class RegistryV6Error(ValueError):
    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


def _fail(code: str, detail: str) -> NoReturn:
    raise RegistryV6Error(code, detail)


def _copy_json(value: Any) -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _fail("NONCANONICAL_VALUE", "non-string key")
            result[key] = _copy_json(child)
        return result
    if type(value) is list:
        return [_copy_json(child) for child in value]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _fail("NONCANONICAL_VALUE", type(value).__name__)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(_copy_json(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode("ascii")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def _run_git(root: Path, args: Sequence[str]) -> bytes:
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(["git", *args], cwd=root, capture_output=True, check=False, env=env)
    if completed.returncode:
        _fail("GIT_ERROR", completed.stderr.decode(errors="replace").strip())
    return completed.stdout


@contextmanager
def _sanitized_git_environment() -> Any:
    inherited = {key: value for key, value in os.environ.items() if key.startswith("GIT_")}
    for key in inherited:
        os.environ.pop(key, None)
    os.environ["GIT_NO_REPLACE_OBJECTS"] = "1"
    try:
        yield
    finally:
        os.environ.pop("GIT_NO_REPLACE_OBJECTS", None)
        os.environ.update(inherited)


def _repository(locator: Path) -> Path:
    if type(locator) is not type(Path()):
        _fail("INVALID_ROOT", "exact platform Path required")
    try:
        return Path(_run_git(locator.resolve(), ("rev-parse", "--show-toplevel")).decode().strip()).resolve()
    except (OSError, UnicodeDecodeError) as exc:
        raise RegistryV6Error("INVALID_ROOT", str(exc)) from exc


def _exact_head(root: Path, requested_head: str) -> tuple[str, str]:
    fmt = _run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    size = 40 if fmt == "sha1" else 64 if fmt == "sha256" else 0
    if type(requested_head) is not str or len(requested_head) != size or OID_RE.fullmatch(requested_head) is None:
        _fail("INVALID_HEAD", "full lowercase commit ID required")
    if _run_git(root, ("cat-file", "-t", requested_head)).decode().strip() != "commit":
        _fail("INVALID_HEAD", "requested object is not a commit")
    if _run_git(root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}")).decode().strip() != requested_head:
        _fail("INVALID_HEAD", "commit resolution drift")
    return requested_head, _run_git(root, ("rev-parse", f"{requested_head}^{{tree}}")).decode().strip()


def _entries(root: Path, head: str) -> dict[str, tuple[str, str, str]]:
    result: dict[str, tuple[str, str, str]] = {}
    for record in _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head)).split(b"\0"):
        if not record:
            continue
        try:
            metadata, raw_path = record.split(b"\t", 1)
            mode, kind, object_id = metadata.decode("ascii").split(" ")
            path = raw_path.decode("utf-8")
        except (UnicodeDecodeError, ValueError) as exc:
            raise RegistryV6Error("GIT_TREE_INVALID", repr(record)) from exc
        pure = PurePosixPath(path)
        if not path or pure.is_absolute() or path != pure.as_posix() or "\\" in path or any(part in {"", ".", ".."} for part in pure.parts):
            _fail("GIT_TREE_INVALID", path)
        if path in result:
            _fail("GIT_TREE_INVALID", f"duplicate {path}")
        result[path] = (mode, kind, object_id)
    return result


def _blob(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str) -> bytes:
    pure = PurePosixPath(path) if type(path) is str else PurePosixPath(".")
    if type(path) is not str or PATH_RE.fullmatch(path) is None or pure.is_absolute() or path != pure.as_posix() or "\\" in path or any(part in {"", ".", ".."} for part in pure.parts):
        _fail("MISSING_ARTIFACT", str(path))
    entry = entries.get(path)
    if entry is None or entry[0] not in REGULAR_MODES or entry[1] != "blob":
        _fail("MISSING_ARTIFACT", path)
    content = _run_git(root, ("cat-file", "blob", entry[2]))
    local = root / path
    if local.is_symlink() or not local.is_file() or local.read_bytes() != content:
        _fail("WORKTREE_BINDING_MISMATCH", path)
    return content


def _strict_json(raw: bytes, name: str) -> dict[str, Any]:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                _fail("DUPLICATE_JSON_KEY", name)
            result[key] = value
        return result

    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_float=lambda _x: _fail("NONINTEGER_JSON", name))
    except RegistryV6Error:
        raise
    except Exception as exc:
        raise RegistryV6Error("INVALID_JSON", f"{name}: {exc}") from exc
    if type(value) is not dict:
        _fail("INVALID_JSON", name)
    return _copy_json(value)


def _fresh(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str, name: str) -> ModuleType:
    content = _blob(root, entries, path)
    module = ModuleType(name)
    module.__file__ = str((root / path).resolve())
    previous = sys.modules.get(name)
    sys.modules[name] = module
    try:
        exec(compile(content, module.__file__, "exec"), module.__dict__)
    except Exception as exc:
        raise RegistryV6Error("MODULE_BINDING_ERROR", f"{path}: {exc}") from exc
    finally:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous
    return module


def _call(module: ModuleType, symbol: str) -> Any:
    value = getattr(module, symbol, None)
    if not callable(value) or getattr(value, "__name__", None) != symbol or getattr(value, "__module__", None) != module.__name__:
        _fail("MODULE_BINDING_ERROR", f"missing exact callable {symbol}")
    return value


def _source_policy(source: Mapping[str, Any]) -> None:
    expected = {
        "schema_id", "schema_version", "registry_id", "status", "activation_status", "authority_policy",
        "orchestration_policy", "post_issuance_replay_policy", "cross_registry_policy", "authority_denials",
        "artifacts", "role_grants", "proof_boundary",
    }
    if set(source) != expected:
        _fail("FIXED_POLICY_MISMATCH", "source field set")
    if (
        source.get("schema_id") != REGISTRY_ID
        or source.get("schema_version") != 6
        or source.get("registry_id") != REGISTRY_ID
        or source.get("status") != STATUS
        or source.get("activation_status") != ACTIVE
        or source.get("authority_policy") != AUTHORITY_POLICY
        or source.get("orchestration_policy") != ORCHESTRATION_POLICY
        or source.get("post_issuance_replay_policy") != POST_ISSUANCE_REPLAY_POLICY
        or source.get("cross_registry_policy") != CROSS_REGISTRY_POLICY
        or source.get("authority_denials") != AUTHORITY_DENIALS
    ):
        _fail("FIXED_POLICY_MISMATCH", "identity/status/denial policy")
    if source.get("proof_boundary") != "REPLAY_CANDIDATE_ONLY_NO_SERIALIZED_SOURCE_AUTHORITY":
        _fail("FIXED_POLICY_MISMATCH", "proof boundary")


def _resolve_artifacts(root: Path, entries: Mapping[str, tuple[str, str, str]], source: Mapping[str, Any]) -> list[dict[str, Any]]:
    expected = {artifact_id: (artifact_class, path, symbols) for artifact_id, artifact_class, path, symbols in IDENTITIES}
    raw = source.get("artifacts")
    if type(raw) is not list or [item.get("artifact_id") if type(item) is dict else None for item in raw] != [item[0] for item in IDENTITIES]:
        _fail("FIXED_ARTIFACT_MISMATCH", "artifact order/set")
    resolved: list[dict[str, Any]] = []
    for item in raw:
        if type(item) is not dict:
            _fail("FIXED_ARTIFACT_MISMATCH", "artifact type")
        artifact_id = item.get("artifact_id")
        artifact_class, path, symbols = expected.get(artifact_id, (None, None, None))
        if (
            set(item) != {"artifact_id", "artifact_class", "path", "symbols", "pin_status"}
            or item.get("artifact_class") != artifact_class
            or item.get("path") != path
            or tuple(item.get("symbols", ())) != symbols
            or item.get("pin_status") != "EXACT_HEAD_RESOLVED"
        ):
            _fail("FIXED_ARTIFACT_MISMATCH", str(artifact_id))
        content = _blob(root, entries, path)
        mode, _kind, object_id = entries[path]
        resolved.append({
            **_copy_json(item),
            "git_mode": mode,
            "git_object_id": object_id,
            "blob_sha256": hashlib.sha256(content).hexdigest(),
            "semantic_sha256": hashlib.sha256(content).hexdigest(),
        })
    if len({item["path"] for item in resolved}) != len(resolved):
        _fail("ARTIFACT_PATH_COLLISION", "V6 artifact paths")
    return resolved


def _resolve_grants(source: Mapping[str, Any], artifacts: Mapping[str, Mapping[str, Any]]) -> list[dict[str, Any]]:
    raw = source.get("role_grants")
    if type(raw) is not list or [item.get("grant_id") if type(item) is dict else None for item in raw] != sorted(ROLE_BINDINGS):
        _fail("FIXED_GRANT_MISMATCH", "grant order/set")
    result: list[dict[str, Any]] = []
    for item in raw:
        if type(item) is not dict:
            _fail("FIXED_GRANT_MISMATCH", "grant type")
        grant_id = item.get("grant_id")
        role, artifact_id, capabilities, authority_class = ROLE_BINDINGS.get(grant_id, (None, None, None, None))
        artifact = artifacts.get(artifact_id)
        if (
            set(item) != {"grant_id", "role", "artifact_id", "capabilities", "authority_class"}
            or artifact is None
            or item.get("role") != role
            or item.get("artifact_id") != artifact_id
            or tuple(item.get("capabilities", ())) != capabilities
            or item.get("authority_class") != authority_class
        ):
            _fail("FIXED_GRANT_MISMATCH", str(grant_id))
        wire = {
            "grant_id": grant_id,
            "role": role,
            "artifact_id": artifact_id,
            "artifact_path": artifact["path"],
            "artifact_symbols": artifact["symbols"],
            "capabilities": item["capabilities"],
            "authority_class": authority_class,
            "artifact_semantic_sha256": artifact["semantic_sha256"],
        }
        result.append({**_copy_json(item), "grant_wire": wire, "role_grant_digest": digest(wire)})
    return result


def _cross_registry(root: Path, entries: Mapping[str, tuple[str, str, str]], head: str, tree: str, version: str, path: str, symbol: str) -> dict[str, Any]:
    module = _fresh(root, entries, path, f"_t6_v6_{version}_registry_{head}")
    try:
        with _sanitized_git_environment():
            resolved = _call(module, symbol)(root=root, requested_head=head)
    except Exception as exc:
        raise RegistryV6Error("CROSS_REGISTRY_RESOLUTION_FAILED", f"{version}: {exc}") from exc
    policy = CROSS_REGISTRY_POLICY[version]
    manifest = resolved.get("role_authority_manifest") if type(resolved) is dict else None
    if (
        type(resolved) is not dict
        or resolved.get("head_sha") != head
        or resolved.get("head_tree_sha") != tree
        or resolved.get("status") != policy["status"]
        or type(resolved.get("registry_digest")) is not str
        or type(manifest) is not dict
        or type(manifest.get("digest")) is not str
    ):
        _fail("CROSS_REGISTRY_MISMATCH", version)
    return {
        "registry_id": policy["registry_id"],
        "registry_digest": resolved["registry_digest"],
        "role_manifest_digest": manifest["digest"],
    }


def resolve_registry_v6(*, root: Path, requested_head: str) -> dict[str, Any]:
    """Resolve the V6 source-input policy and all V3--V5 exact-HEAD pins."""

    repo = _repository(root)
    head, tree = _exact_head(repo, requested_head)
    entries = _entries(repo, head)
    own = _blob(repo, entries, RESOLVER_PATH)
    local = Path(__file__)
    if local.is_symlink() or not local.is_file() or local.resolve() != (repo / RESOLVER_PATH).resolve() or local.read_bytes() != own:
        _fail("WORKTREE_BINDING_MISMATCH", RESOLVER_PATH)
    source = _strict_json(_blob(repo, entries, REGISTRY_PATH), REGISTRY_PATH)
    schema = _strict_json(_blob(repo, entries, SCHEMA_PATH), SCHEMA_PATH)
    jsonschema.Draft202012Validator.check_schema(schema)
    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(source))
    if errors:
        _fail("SOURCE_SCHEMA_INVALID", errors[0].message)
    _source_policy(source)
    artifacts_list = _resolve_artifacts(repo, entries, source)
    artifacts = {item["artifact_id"]: item for item in artifacts_list}
    grants = _resolve_grants(source, artifacts)
    crosses = {
        "v3": _cross_registry(repo, entries, head, tree, "v3", V3_RESOLVER_PATH, V3_RESOLVER_SYMBOL),
        "v4": _cross_registry(repo, entries, head, tree, "v4", V4_RESOLVER_PATH, V4_RESOLVER_SYMBOL),
        "v5": _cross_registry(repo, entries, head, tree, "v5", V5_RESOLVER_PATH, V5_RESOLVER_SYMBOL),
    }
    binding_files = []
    for path in (RESOLVER_PATH, REGISTRY_PATH, SCHEMA_PATH, *(item["path"] for item in artifacts_list), V3_RESOLVER_PATH, V4_RESOLVER_PATH, V5_RESOLVER_PATH):
        content = _blob(repo, entries, path)
        binding_files.append({"path": path, "git_object_id": entries[path][2], "sha256": hashlib.sha256(content).hexdigest()})
    binding = {"schema_id": "t6_v6_exact_source_input_toolchain", "head_sha": head, "files": binding_files}
    binding["digest"] = digest(binding)
    manifest = {
        "schema_id": "t6_q1_exact_head_source_input_candidate_manifest_v6",
        "head_sha": head,
        "status": STATUS,
        "grants": grants,
        "cross_registries": crosses,
        "authority_denials": AUTHORITY_DENIALS,
    }
    manifest["digest"] = digest(manifest)
    for path in (RESOLVER_PATH, REGISTRY_PATH, SCHEMA_PATH, *(item["path"] for item in artifacts_list), V3_RESOLVER_PATH, V4_RESOLVER_PATH, V5_RESOLVER_PATH):
        _blob(repo, entries, path)
    payload = {
        "schema_id": RESOLVED_SCHEMA_ID,
        "schema_version": 6,
        "head_sha": head,
        "head_tree_sha": tree,
        "execution_binding": binding,
        "resolved_artifacts": artifacts_list,
        "resolved_role_grants": grants,
        "cross_registries": crosses,
        "authority_policy": AUTHORITY_POLICY,
        "orchestration_policy": ORCHESTRATION_POLICY,
        "post_issuance_replay_policy": POST_ISSUANCE_REPLAY_POLICY,
        "authority_denials": AUTHORITY_DENIALS,
        "role_authority_manifest": manifest,
        "status": STATUS,
        "proof_boundary": source["proof_boundary"],
    }
    payload["registry_digest"] = digest(payload)
    return payload


__all__ = [
    "ACTIVE",
    "AUTHORITY_DENIALS",
    "BINDER_GRANT_ID",
    "BINDER_ID",
    "BINDER_ROLE",
    "ORCHESTRATOR_ID",
    "PRESTATE_ID",
    "REBIND_GRANT_ID",
    "REBIND_ID",
    "REBIND_ROLE",
    "REGISTRY_ID",
    "REGISTRY_PATH",
    "REPLAYER_ID",
    "RegistryV6Error",
    "RESOLVER_PATH",
    "STATUS",
    "canonical_bytes",
    "digest",
    "resolve_registry_v6",
]
