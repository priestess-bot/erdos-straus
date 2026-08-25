#!/usr/bin/env python3
"""Resolve the T6 evidence-only role inventory from immutable Git objects.

No registered Python code is imported or executed.  The caller supplies only a
repository locator and an exact commit object ID; registry content, artifacts,
symbols and the governing schema are read from that commit's tree.  Slice 1
grants no executable or proof role.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from typing import Any, Iterable, Mapping, Sequence

import jsonschema


SCHEMA_ID = "t6_coordinator_role_registry_v1"
SCHEMA_VERSION = 1
RESOLVED_SCHEMA_ID = "t6_coordinator_role_registry_resolved_v1"
REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v1.json"
RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v1.py"
SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v1.schema.json"
TOOLCHAIN_PATHS = (RESOLVER_PATH, SCHEMA_PATH)
SOURCE_STATUS = "HEAD_BOUND_EVIDENCE_ONLY_NO_ROLE_AUTHORITY"
RESOLVED_STATUS = "HEAD_BOUND_EVIDENCE_ONLY_NO_ROLE_AUTHORITY"
AUTHORITY = "EVIDENCE_ONLY_NOT_AUTHORIZED"
AUTHORITY_SOURCE = "TRACKED_GIT_OBJECTS_AT_EXACT_REQUESTED_HEAD"
PYTHON_DIGEST_METHOD = "PYTHON_AST_SYMBOL_AND_GIT_BLOB_SHA256_V1"
JSON_DIGEST_METHOD = "CANONICAL_JSON_POINTER_AND_GIT_BLOB_SHA256_V1"
AST_DUMP_CONTRACT_VERSION = (
    "PYTHON_AST_DUMP_ANNOTATE_FIELDS_TRUE_INCLUDE_ATTRIBUTES_FALSE_V1"
)

ROLE_DIGEST_KEYS = {
    "PRODUCER": "producer_registry",
    "INDEPENDENT_VALIDATOR": "validator_registry",
    "PROJECTOR": "projector_registry",
    "TERMINAL_SCHEDULE": "terminal_schedule_registry",
    "T5_TICKET": "t5_ticket_registry",
}
ALLOWED_EXECUTABLE_ROOTS = ("scripts",)
FORBIDDEN_EXECUTABLE_ROOTS = (
    ".github",
    "claims",
    "concepts",
    "data",
    "docs",
    "index",
    "reproductions",
    "schemas",
    "tests",
)
EXPECTED_AUTHORITY_POLICY = {
    "scope": "EVIDENCE_INVENTORY_ONLY",
    "source": AUTHORITY_SOURCE,
    "worktree_authority": False,
    "caller_override_authority": False,
    "role_authority": False,
    "allowed_executable_roots": list(ALLOWED_EXECUTABLE_ROOTS),
    "forbidden_executable_roots": list(FORBIDDEN_EXECUTABLE_ROOTS),
}
SOURCE_KEYS = frozenset(
    {
        "schema_id",
        "schema_version",
        "registry_id",
        "status",
        "authority_policy",
        "artifacts",
        "role_grants",
        "branch_bindings",
        "complete_terminal_schedules",
        "blocked_candidates",
        "proof_boundary",
    }
)
PYTHON_ARTIFACT_KEYS = frozenset(
    {
        "artifact_id",
        "kind",
        "path",
        "symbol",
        "authority",
        "semantic_digest_method",
    }
)
JSON_ARTIFACT_KEYS = frozenset(
    {
        "artifact_id",
        "kind",
        "path",
        "json_pointer",
        "authority",
        "semantic_digest_method",
    }
)
BLOCKED_KEYS = frozenset(
    {
        "candidate_id",
        "status",
        "path",
        "producer_symbols",
        "projector_symbols",
        "validator_symbols",
        "terminal_schedule_symbols",
        "terminal_verifier_symbols",
        "reason_codes",
    }
)
BLOCKED_SYMBOL_KEYS = (
    "producer_symbols",
    "projector_symbols",
    "validator_symbols",
    "terminal_schedule_symbols",
    "terminal_verifier_symbols",
)
Q1_BLOCKED_ID = "q1_full_carrier_local_runtime_slice_v1"
Q1_BLOCK_REASONS = frozenset(
    {"SAME_MODULE_ROLE_COLLISION", "LOCAL_TERMINAL_SCOPE", "LEGACY_BOOL"}
)
OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
IDENTIFIER_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]*\Z")
SYMBOL_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")
REGULAR_MODES = frozenset({"100644", "100755"})


class RegistryError(ValueError):
    """Fail-closed registry resolution error with a stable code."""

    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


@dataclass(frozen=True)
class GitEntry:
    mode: str
    object_type: str
    object_id: str
    path: str


def canonical_json_bytes_v1(value: Any) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("ascii")
    except (TypeError, ValueError) as exc:
        raise RegistryError("NONCANONICAL_VALUE", str(exc)) from exc


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes_v1(value)).hexdigest()


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def python_ast_contract_v1() -> dict[str, Any]:
    payload: dict[str, Any] = {
        "schema_id": "t6_python_ast_evidence_contract_v1",
        "python_implementation": sys.implementation.name,
        "python_major_minor": f"{sys.version_info.major}.{sys.version_info.minor}",
        "ast_dump_contract_version": AST_DUMP_CONTRACT_VERSION,
        "status": "EVIDENCE_SERIALIZATION_CONTRACT_ONLY",
    }
    payload["digest"] = canonical_digest_v1(payload)
    return payload


def _run_git(root: Path, args: Sequence[str]) -> bytes:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        capture_output=True,
        env=environment,
    )
    if completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RegistryError("GIT_ERROR", f"git {' '.join(args)} failed: {detail}")
    return completed.stdout


def _repository_root(locator: Path) -> Path:
    root_bytes = _run_git(locator.resolve(), ("rev-parse", "--show-toplevel"))
    try:
        return Path(root_bytes.decode("utf-8").strip()).resolve()
    except UnicodeDecodeError as exc:
        raise RegistryError("GIT_ERROR", "repository root is not UTF-8") from exc


def _exact_commit(root: Path, requested_head: str) -> tuple[str, str]:
    if not isinstance(requested_head, str) or OID_RE.fullmatch(requested_head) is None:
        raise RegistryError(
            "INVALID_HEAD",
            "requested_head must be a lowercase full object ID, not a ref or prefix",
        )
    object_type = _run_git(root, ("cat-file", "-t", requested_head)).decode().strip()
    if object_type != "commit":
        raise RegistryError("INVALID_HEAD", "requested object is not a commit")
    resolved = _run_git(root, ("rev-parse", "--verify", requested_head)).decode().strip()
    if resolved != requested_head:
        raise RegistryError("INVALID_HEAD", "requested commit did not resolve exactly")
    tree = _run_git(root, ("rev-parse", f"{requested_head}^{{tree}}"))
    tree_id = tree.decode("ascii").strip()
    if OID_RE.fullmatch(tree_id) is None:
        raise RegistryError("GIT_ERROR", "commit tree is not a full object ID")
    return requested_head, tree_id


def _safe_path(value: Any, *, executable: bool = False) -> str:
    if not isinstance(value, str) or not value or PATH_RE.fullmatch(value) is None:
        raise RegistryError("UNSAFE_PATH", f"invalid repository path {value!r}")
    pure = PurePosixPath(value)
    if (
        pure.is_absolute()
        or value != pure.as_posix()
        or any(part in {"", ".", ".."} for part in pure.parts)
        or "\\" in value
    ):
        raise RegistryError("UNSAFE_PATH", f"non-normal repository path {value!r}")
    if executable:
        root = pure.parts[0]
        if root in FORBIDDEN_EXECUTABLE_ROOTS or root not in ALLOWED_EXECUTABLE_ROOTS:
            raise RegistryError(
                "FORBIDDEN_EXECUTABLE_ROOT",
                f"executable artifact {value!r} is outside scripts/",
            )
        if pure.suffix != ".py":
            raise RegistryError(
                "FORBIDDEN_EXECUTABLE_ROOT", "executable artifact must be Python"
            )
    return value


def _tree_entries(root: Path, head_sha: str) -> dict[str, GitEntry]:
    raw = _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head_sha))
    result: dict[str, GitEntry] = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            metadata, path_bytes = record.split(b"\t", 1)
            mode, object_type, object_id = metadata.decode("ascii").split(" ")
            path = path_bytes.decode("utf-8")
        except (UnicodeDecodeError, ValueError) as exc:
            raise RegistryError("GIT_TREE_INVALID", repr(record)) from exc
        pure = PurePosixPath(path)
        if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
            raise RegistryError("GIT_TREE_INVALID", f"unsafe tracked path {path!r}")
        if path in result:
            raise RegistryError("GIT_TREE_INVALID", f"duplicate tree path {path!r}")
        result[path] = GitEntry(mode, object_type, object_id, path)
    return result


def _blob(root: Path, entry: GitEntry) -> bytes:
    if entry.object_type != "blob" or entry.mode not in REGULAR_MODES:
        raise RegistryError(
            "INVALID_GIT_MODE", f"{entry.path!r} is not a regular tracked blob"
        )
    return _run_git(root, ("cat-file", "blob", entry.object_id))


def _required_blob(
    root: Path, entries: Mapping[str, GitEntry], path: str, *, executable: bool = False
) -> tuple[GitEntry, bytes]:
    safe = _safe_path(path, executable=executable)
    entry = entries.get(safe)
    if entry is None:
        raise RegistryError("MISSING_ARTIFACT", f"{safe!r} is absent from requested HEAD")
    return entry, _blob(root, entry)


def _capture_toolchain_binding(
    root: Path, entries: Mapping[str, GitEntry], head_sha: str
) -> dict[str, Any]:
    status = _run_git(
        root,
        (
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
            "--",
            *TOOLCHAIN_PATHS,
        ),
    ).decode("utf-8", errors="replace").strip()
    if status:
        raise RegistryError("DIRTY_TOOLCHAIN", status)

    files: list[dict[str, Any]] = []
    head_blobs: dict[str, bytes] = {}
    for path in TOOLCHAIN_PATHS:
        try:
            entry, head_bytes = _required_blob(root, entries, path, executable=path.endswith(".py"))
        except RegistryError as exc:
            if exc.code == "MISSING_ARTIFACT":
                raise RegistryError(
                    "TOOLCHAIN_MISSING_AT_HEAD", f"{path} is absent at {head_sha}"
                ) from exc
            raise
        worktree_path = root / path
        if worktree_path.is_symlink() or not worktree_path.is_file():
            raise RegistryError("DIRTY_TOOLCHAIN", f"{path} is not a regular worktree file")
        worktree_bytes = worktree_path.read_bytes()
        if worktree_bytes != head_bytes:
            raise RegistryError(
                "TOOLCHAIN_WORKTREE_MISMATCH", f"{path} differs from requested HEAD"
            )
        head_blobs[path] = head_bytes
        files.append(
            {
                "path": path,
                "git_mode": entry.mode,
                "git_object_id": entry.object_id,
                "sha256": _sha256(head_bytes),
            }
        )

    executing = Path(__file__)
    if executing.is_symlink() or executing.resolve().read_bytes() != head_blobs[RESOLVER_PATH]:
        raise RegistryError(
            "EXECUTING_RESOLVER_HEAD_MISMATCH",
            "executing resolver bytes differ from the requested-HEAD resolver blob",
        )
    payload: dict[str, Any] = {
        "schema_id": "t6_coordinator_inventory_toolchain_binding_v1",
        "head_sha": head_sha,
        "files": files,
        "status": "BOUND_TO_CLEAN_REQUESTED_HEAD",
    }
    payload["digest"] = canonical_digest_v1(payload)
    return payload


def load_json_object_strict_v1(value: bytes, *, source: str) -> dict[str, Any]:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, item in pairs:
            if key in result:
                raise RegistryError(
                    "DUPLICATE_JSON_KEY", f"duplicate key {key!r} in {source}"
                )
            result[key] = item
        return result

    def reject_constant(constant: str) -> None:
        raise RegistryError(
            "NONFINITE_JSON", f"non-finite value {constant!r} in {source}"
        )

    try:
        decoded = json.loads(
            value.decode("utf-8"),
            object_pairs_hook=reject_duplicates,
            parse_constant=reject_constant,
        )
    except RegistryError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RegistryError("INVALID_JSON", f"invalid JSON in {source}: {exc}") from exc
    if not isinstance(decoded, dict):
        raise RegistryError("SCHEMA_VIOLATION", f"{source} is not a JSON object")
    return decoded


def _validate_source_with_head_schema(
    root: Path,
    entries: Mapping[str, GitEntry],
    head_sha: str,
    source: Mapping[str, Any],
) -> None:
    _, schema_bytes = _required_blob(root, entries, SCHEMA_PATH)
    schema = load_json_object_strict_v1(
        schema_bytes, source=f"{head_sha}:{SCHEMA_PATH}"
    )
    try:
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(schema)
    except jsonschema.exceptions.SchemaError as exc:
        raise RegistryError(
            "HEAD_SCHEMA_INVALID", f"requested-HEAD schema is invalid: {exc.message}"
        ) from exc
    errors = sorted(
        validator.iter_errors(source),
        key=lambda error: (
            tuple(str(part) for part in error.absolute_path),
            error.message,
        ),
    )
    if errors:
        error = errors[0]
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        raise RegistryError(
            "SOURCE_SCHEMA_INVALID", f"{location}: {error.message}"
        )


def _exact_keys(value: Mapping[str, Any], expected: frozenset[str], name: str) -> None:
    observed = set(value)
    if observed != expected:
        raise RegistryError(
            "SCHEMA_VIOLATION",
            f"{name} fields differ; missing={sorted(expected - observed)}, "
            f"extra={sorted(observed - expected)}",
        )


def _identifier(value: Any, name: str) -> str:
    if not isinstance(value, str) or IDENTIFIER_RE.fullmatch(value) is None:
        raise RegistryError("SCHEMA_VIOLATION", f"invalid {name}: {value!r}")
    return value


def _symbol(value: Any, name: str) -> str:
    if not isinstance(value, str) or SYMBOL_RE.fullmatch(value) is None:
        raise RegistryError("SYMBOL_INVALID", f"invalid {name}: {value!r}")
    return value


def _sorted_unique_strings(value: Any, name: str, *, nonempty: bool = False) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise RegistryError("SCHEMA_VIOLATION", f"{name} must be a string array")
    if nonempty and not value:
        raise RegistryError("SCHEMA_VIOLATION", f"{name} must be nonempty")
    if value != sorted(value) or len(value) != len(set(value)):
        raise RegistryError("SCHEMA_VIOLATION", f"{name} must be sorted and unique")
    return value


def _module_scope_bindings(statements: Iterable[ast.stmt]) -> list[tuple[str, ast.AST]]:
    bindings: list[tuple[str, ast.AST]] = []

    def target_names(target: ast.AST) -> Iterable[str]:
        if isinstance(target, ast.Name):
            yield target.id
        elif isinstance(target, (ast.Tuple, ast.List)):
            for child in target.elts:
                yield from target_names(child)

    for node in statements:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            bindings.append((node.name, node))
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                bindings.extend((name, node) for name in target_names(target))
        elif isinstance(node, ast.AnnAssign):
            bindings.extend((name, node) for name in target_names(node.target))
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                name = alias.asname or alias.name.split(".")[0]
                bindings.append((name, node))
        elif isinstance(node, (ast.If, ast.For, ast.AsyncFor, ast.While)):
            bindings.extend(_module_scope_bindings(node.body))
            bindings.extend(_module_scope_bindings(node.orelse))
        elif isinstance(node, (ast.With, ast.AsyncWith)):
            bindings.extend(_module_scope_bindings(node.body))
        elif isinstance(node, ast.Try):
            bindings.extend(_module_scope_bindings(node.body))
            bindings.extend(_module_scope_bindings(node.orelse))
            bindings.extend(_module_scope_bindings(node.finalbody))
            for handler in node.handlers:
                bindings.extend(_module_scope_bindings(handler.body))
        elif isinstance(node, ast.Match):
            for case in node.cases:
                bindings.extend(_module_scope_bindings(case.body))
    return bindings


def _parse_python(value: bytes, path: str) -> ast.Module:
    try:
        source = value.decode("utf-8")
        return ast.parse(source, filename=path)
    except (UnicodeDecodeError, SyntaxError) as exc:
        raise RegistryError("PYTHON_PARSE_ERROR", f"cannot parse {path}: {exc}") from exc


def _resolve_symbol(
    *, path: str, symbol: str, value: bytes, blob_sha256: str
) -> dict[str, str]:
    symbol = _symbol(symbol, f"symbol in {path}")
    tree = _parse_python(value, path)
    matches = [node for name, node in _module_scope_bindings(tree.body) if name == symbol]
    if not matches:
        raise RegistryError("SYMBOL_MISSING", f"{path}:{symbol} is not defined")
    if len(matches) != 1:
        raise RegistryError(
            "SYMBOL_AMBIGUITY", f"{path}:{symbol} has {len(matches)} module bindings"
        )
    node = matches[0]
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        raise RegistryError(
            "SYMBOL_NOT_LOCAL", f"{path}:{symbol} is only an imported binding"
        )
    node_dump = ast.dump(node, annotate_fields=True, include_attributes=False)
    node_sha = _sha256(node_dump.encode("utf-8"))
    ast_contract = python_ast_contract_v1()
    semantic = canonical_digest_v1(
        {
            "method": PYTHON_DIGEST_METHOD,
            "path": path,
            "symbol": symbol,
            "blob_sha256": blob_sha256,
            "symbol_ast_sha256": node_sha,
            "python_ast_contract_digest": ast_contract["digest"],
        }
    )
    return {
        "symbol": symbol,
        "symbol_ast_sha256": node_sha,
        "python_ast_contract_digest": ast_contract["digest"],
        "semantic_sha256": semantic,
    }


def _json_pointer(document: Any, pointer: str, source: str) -> Any:
    if not isinstance(pointer, str):
        raise RegistryError("JSON_POINTER_INVALID", f"pointer in {source} is not text")
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise RegistryError("JSON_POINTER_INVALID", f"invalid pointer {pointer!r}")
    current = document
    for raw_part in pointer[1:].split("/"):
        if re.search(r"~(?:[^01]|$)", raw_part):
            raise RegistryError("JSON_POINTER_INVALID", f"invalid escape in {pointer!r}")
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if isinstance(current, Mapping):
            if part not in current:
                raise RegistryError("JSON_POINTER_MISSING", f"{pointer!r} misses {part!r}")
            current = current[part]
        elif isinstance(current, list):
            if not part.isdigit() or (len(part) > 1 and part.startswith("0")):
                raise RegistryError("JSON_POINTER_INVALID", f"invalid index {part!r}")
            index = int(part)
            if index >= len(current):
                raise RegistryError("JSON_POINTER_MISSING", f"index {index} is absent")
            current = current[index]
        else:
            raise RegistryError("JSON_POINTER_MISSING", f"cannot descend through {part!r}")
    return current


def _resolve_artifact(
    root: Path, entries: Mapping[str, GitEntry], source: Mapping[str, Any]
) -> dict[str, Any]:
    kind = source.get("kind")
    expected = PYTHON_ARTIFACT_KEYS if kind == "PYTHON_SYMBOL" else JSON_ARTIFACT_KEYS
    if kind not in {"PYTHON_SYMBOL", "JSON_POINTER"}:
        raise RegistryError("SCHEMA_VIOLATION", f"unknown artifact kind {kind!r}")
    _exact_keys(source, expected, f"artifact {source.get('artifact_id')!r}")
    artifact_id = _identifier(source["artifact_id"], "artifact_id")
    if source["authority"] != AUTHORITY:
        raise RegistryError("CALLER_AUTHORITY_REJECTED", artifact_id)
    executable = kind == "PYTHON_SYMBOL"
    path = _safe_path(source["path"], executable=executable)
    entry, value = _required_blob(root, entries, path, executable=executable)
    blob_sha = _sha256(value)
    base: dict[str, Any] = {
        "artifact_id": artifact_id,
        "kind": kind,
        "path": path,
        "authority": AUTHORITY,
        "git_mode": entry.mode,
        "git_object_id": entry.object_id,
        "blob_sha256": blob_sha,
    }
    if kind == "PYTHON_SYMBOL":
        if source["semantic_digest_method"] != PYTHON_DIGEST_METHOD:
            raise RegistryError("DIGEST_METHOD_INVALID", artifact_id)
        base.update(
            _resolve_symbol(
                path=path,
                symbol=source["symbol"],
                value=value,
                blob_sha256=blob_sha,
            )
        )
    else:
        if source["semantic_digest_method"] != JSON_DIGEST_METHOD:
            raise RegistryError("DIGEST_METHOD_INVALID", artifact_id)
        document = load_json_object_strict_v1(value, source=path)
        pointer = source["json_pointer"]
        selected = _json_pointer(document, pointer, path)
        selected_sha = canonical_digest_v1(selected)
        base.update(
            {
                "json_pointer": pointer,
                "json_value_sha256": selected_sha,
                "semantic_sha256": canonical_digest_v1(
                    {
                        "method": JSON_DIGEST_METHOD,
                        "path": path,
                        "json_pointer": pointer,
                        "blob_sha256": blob_sha,
                        "json_value_sha256": selected_sha,
                    }
                ),
            }
        )
    base["semantic_digest_method"] = source["semantic_digest_method"]
    return base


def _validate_source_header(source: Mapping[str, Any]) -> None:
    _exact_keys(source, SOURCE_KEYS, "registry")
    if source["schema_id"] != SCHEMA_ID or source["registry_id"] != SCHEMA_ID:
        raise RegistryError("SCHEMA_VIOLATION", "registry identity mismatch")
    if type(source["schema_version"]) is not int or source["schema_version"] != 1:
        raise RegistryError("SCHEMA_VIOLATION", "registry version must be integer 1")
    if source["status"] != SOURCE_STATUS:
        raise RegistryError("SCHEMA_VIOLATION", "source status mismatch")
    if source["authority_policy"] != EXPECTED_AUTHORITY_POLICY:
        raise RegistryError(
            "CALLER_AUTHORITY_REJECTED", "evidence-only authority policy changed"
        )
    if not isinstance(source["proof_boundary"], str) or not source["proof_boundary"]:
        raise RegistryError("SCHEMA_VIOLATION", "proof_boundary must be nonempty")
    if RESOLVED_STATUS not in source["proof_boundary"]:
        raise RegistryError(
            "SCHEMA_VIOLATION", "proof_boundary must state the evidence-only status"
        )
    for key in (
        "artifacts",
        "role_grants",
        "branch_bindings",
        "complete_terminal_schedules",
        "blocked_candidates",
    ):
        if not isinstance(source[key], list):
            raise RegistryError("SCHEMA_VIOLATION", f"{key} must be an array")
    if source["role_grants"]:
        raise RegistryError(
            "ROLE_AUTHORITY_FORBIDDEN", "Slice 1 role_grants must be empty"
        )


def _resolve_blocked_candidates(
    root: Path,
    entries: Mapping[str, GitEntry],
    source: Mapping[str, Any],
) -> list[dict[str, Any]]:
    blocked = source["blocked_candidates"]
    if any(not isinstance(item, Mapping) for item in blocked):
        raise RegistryError("SCHEMA_VIOLATION", "blocked candidate must be object")
    candidate_ids = [
        _identifier(item.get("candidate_id"), "candidate_id") for item in blocked
    ]
    if candidate_ids != sorted(candidate_ids) or len(candidate_ids) != len(
        set(candidate_ids)
    ):
        raise RegistryError("DUPLICATE_ID", "blocked candidates need sorted unique IDs")
    resolved: list[dict[str, Any]] = []
    for candidate in blocked:
        _exact_keys(
            candidate, BLOCKED_KEYS, f"blocked {candidate.get('candidate_id')!r}"
        )
        candidate_id = _identifier(candidate["candidate_id"], "candidate_id")
        if candidate["status"] != "BLOCKED_NOT_AUTHORIZED":
            raise RegistryError("SCHEMA_VIOLATION", f"{candidate_id} is not blocked")
        path = _safe_path(candidate["path"], executable=True)
        entry, value = _required_blob(root, entries, path, executable=True)
        blob_sha = _sha256(value)
        all_symbols: list[str] = []
        symbol_groups: dict[str, list[str]] = {}
        for key in BLOCKED_SYMBOL_KEYS:
            symbols = _sorted_unique_strings(candidate[key], f"{candidate_id}.{key}", nonempty=True)
            for symbol_value in symbols:
                _symbol(symbol_value, f"{candidate_id}.{key}")
            symbol_groups[key] = symbols
            all_symbols.extend(symbols)
        if len(all_symbols) != len(set(all_symbols)):
            raise RegistryError("SYMBOL_AMBIGUITY", f"{candidate_id} reuses role symbols")
        reasons = _sorted_unique_strings(
            candidate["reason_codes"], f"{candidate_id}.reason_codes", nonempty=True
        )
        semantic = {
            symbol_value: _resolve_symbol(
                path=path,
                symbol=symbol_value,
                value=value,
                blob_sha256=blob_sha,
            )["semantic_sha256"]
            for symbol_value in sorted(all_symbols)
        }
        resolved.append(
            {
                "candidate_id": candidate_id,
                "status": "BLOCKED_NOT_AUTHORIZED",
                "path": path,
                "git_mode": entry.mode,
                "git_object_id": entry.object_id,
                "blob_sha256": blob_sha,
                **symbol_groups,
                "symbol_semantic_sha256": semantic,
                "reason_codes": reasons,
            }
        )
    q1 = next((item for item in resolved if item["candidate_id"] == Q1_BLOCKED_ID), None)
    if q1 is None or set(q1["reason_codes"]) != Q1_BLOCK_REASONS:
        raise RegistryError(
            "Q1_BLOCK_BOUNDARY_MISSING", "q=1 local runtime must remain explicitly blocked"
        )
    return resolved


def resolve_registry_v1(*, root: Path, requested_head: str) -> dict[str, Any]:
    """Resolve the fixed coordinator registry at an exact commit.

    There is intentionally no registry mapping, path override, callable table or
    worktree-content parameter in this API.
    """

    repository = _repository_root(root)
    head_sha, tree_sha = _exact_commit(repository, requested_head)
    entries = _tree_entries(repository, head_sha)
    execution_binding = _capture_toolchain_binding(repository, entries, head_sha)
    registry_entry, registry_bytes = _required_blob(
        repository, entries, REGISTRY_PATH
    )
    source = load_json_object_strict_v1(
        registry_bytes, source=f"{head_sha}:{REGISTRY_PATH}"
    )
    _validate_source_with_head_schema(repository, entries, head_sha, source)
    _validate_source_header(source)

    artifact_sources = source["artifacts"]
    if any(not isinstance(item, Mapping) for item in artifact_sources):
        raise RegistryError("SCHEMA_VIOLATION", "artifact must be an object")
    artifact_ids = [
        _identifier(item.get("artifact_id"), "artifact_id")
        for item in artifact_sources
    ]
    if artifact_ids != sorted(artifact_ids) or len(artifact_ids) != len(
        set(artifact_ids)
    ):
        raise RegistryError("DUPLICATE_ID", "artifacts need sorted unique IDs")
    resolved_artifacts = [
        _resolve_artifact(repository, entries, item) for item in artifact_sources
    ]
    artifact_map = {item["artifact_id"]: item for item in resolved_artifacts}
    if len(artifact_map) != len(resolved_artifacts):
        raise RegistryError("DUPLICATE_ID", "duplicate artifact IDs")
    python_bindings = [
        (item["path"], item["symbol"])
        for item in resolved_artifacts
        if item["kind"] == "PYTHON_SYMBOL"
    ]
    if len(python_bindings) != len(set(python_bindings)):
        raise RegistryError("DUPLICATE_ID", "duplicate Python artifact binding")

    blocked = _resolve_blocked_candidates(repository, entries, source)
    if source["branch_bindings"]:
        raise RegistryError(
            "ACTIVE_BRANCHES_FORBIDDEN", "Slice 1 branch bindings must be empty"
        )
    if source["complete_terminal_schedules"]:
        raise RegistryError(
            "COMPLETE_SCHEDULES_FORBIDDEN",
            "Slice 1 complete terminal schedules must be empty",
        )

    digest_map = {
        artifact_id: artifact_map[artifact_id]["semantic_sha256"]
        for artifact_id in sorted(artifact_map)
    }
    artifact_inventory: dict[str, Any] = {
        "schema_id": "t6_evidence_artifact_digest_inventory_v1",
        "status": "EVIDENCE_ONLY_NOT_AUTHORIZED",
        "role_authority": False,
        "head_sha": head_sha,
        "digests": digest_map,
    }
    artifact_inventory["digest"] = canonical_digest_v1(artifact_inventory)

    role_subdigests: dict[str, str] = {}
    for role, key in ROLE_DIGEST_KEYS.items():
        role_subdigests[key] = canonical_digest_v1(
            {
                "schema_id": "t6_coordinator_role_subregistry_v1",
                "head_sha": head_sha,
                "role": role,
                "grants": [],
            }
        )

    final_binding = _capture_toolchain_binding(repository, entries, head_sha)
    if final_binding != execution_binding:
        raise RegistryError(
            "TOOLCHAIN_CHANGED_DURING_RESOLUTION",
            "resolver or schema binding changed during resolution",
        )

    payload: dict[str, Any] = {
        "schema_id": RESOLVED_SCHEMA_ID,
        "schema_version": 1,
        "artifact_policy": "EPHEMERAL_EXACT_HEAD_EVIDENCE_INVENTORY_NOT_TRACKED",
        "head_sha": head_sha,
        "head_tree_sha": tree_sha,
        "registry_path": REGISTRY_PATH,
        "registry_git_mode": registry_entry.mode,
        "registry_git_object_id": registry_entry.object_id,
        "registry_source_sha256": _sha256(registry_bytes),
        "execution_binding": execution_binding,
        "python_ast_contract": python_ast_contract_v1(),
        "resolved_artifacts": resolved_artifacts,
        "resolved_role_grants": [],
        "authorized_branches": [],
        "complete_terminal_schedules": [],
        "blocked_candidates": blocked,
        "artifact_evidence_inventory": artifact_inventory,
        "role_subdigests": role_subdigests,
        "role_grant_counts": {
            key: 0 for key in sorted(ROLE_DIGEST_KEYS.values())
        },
        "active_role_grant_count": 0,
        "active_producer_count": 0,
        "complete_terminal_schedule_count": 0,
        "status": RESOLVED_STATUS,
        "proof_boundary": source["proof_boundary"],
    }
    payload["registry_digest"] = canonical_digest_v1(payload)
    return payload


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--head", required=True, help="exact full commit object ID")
    parser.add_argument("--output", type=Path, help="ephemeral output; default stdout")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        payload = resolve_registry_v1(root=args.root, requested_head=args.head)
        encoded = canonical_json_bytes_v1(payload) + b"\n"
        if args.output is None:
            sys.stdout.buffer.write(encoded)
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(encoded)
    except RegistryError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
