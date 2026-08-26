#!/usr/bin/env python3
"""Resolve the narrow T6 q1 terminal-prefix authority at an exact Git HEAD.

The registry authorizes one scheduler capability and one independent coverage
verifier capability.  It imports or executes neither artifact and exposes no
issuer, E1, queue, producer, initializer, T5, or runtime-admission API.
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
from typing import Any, Iterable, Mapping, NoReturn, Sequence

import jsonschema


SCHEMA_ID = "t6_coordinator_role_registry_v2"
SCHEMA_VERSION = 2
RESOLVED_SCHEMA_ID = "t6_coordinator_role_registry_resolved_v2"
REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v2.json"
RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v2.py"
SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v2.schema.json"
TOOLCHAIN_PATHS = (REGISTRY_PATH, RESOLVER_PATH, SCHEMA_PATH)

STATUS = "HEAD_BOUND_PREFIX_SCHEDULE_AUTHORITY_NO_ISSUER"
AUTHORITY_SOURCE = "TRACKED_GIT_OBJECTS_AT_EXACT_REQUESTED_HEAD"
AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_NO_ISSUER"
DIGEST_METHOD = "PYTHON_AST_SYMBOL_BLOB_AND_LOCAL_IMPORT_CLOSURE_SHA256_V2"
AST_DUMP_CONTRACT_VERSION = (
    "PYTHON_AST_CANONICAL_JSON_OMIT_ATTRIBUTES_AND_EMPTY_TYPE_PARAMS_V2"
)

SCHEDULE_ID = "q1_root_gap_3_7_11_registered_priority_prefix_v1"
SCHEDULER_ARTIFACT_ID = "q1_priority_prefix_scheduler_v1"
SCHEDULER_PATH = "scripts/t6_q_one_priority_prefix_scheduler_v1.py"
SCHEDULER_SYMBOL = "replay_q_one_priority_prefix_v1"
VERIFIER_ARTIFACT_ID = "q1_priority_prefix_coverage_verifier_v1"
VERIFIER_PATH = "scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py"
VERIFIER_SYMBOL = "verify_q_one_priority_prefix_coverage_v1"
LEGACY_RUNTIME_PATH = "scripts/t6_persistent_selector_runtime_v1.py"

SCHEDULER_GRANT_ID = "q1_prefix_terminal_scheduler_grant_v2"
VERIFIER_GRANT_ID = "q1_prefix_independent_coverage_verifier_grant_v2"
ALLOWED_ROLES = ("INDEPENDENT_COVERAGE_VERIFIER", "TERMINAL_SCHEDULER")
SCHEDULER_CAPABILITIES = ("REGISTERED_PRIORITY_PREFIX_REPLAY",)
VERIFIER_CAPABILITIES = (
    "CERTIFICATE_VERIFIER",
    "DOMAIN_VERIFIER",
    "ROOT_TERMINAL_VERIFIER",
)

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
LOCAL_PYTHON_ROOTS = frozenset({"scripts", *FORBIDDEN_EXECUTABLE_ROOTS})
DYNAMIC_LOADING_MODULES = frozenset({"builtins", "importlib", "pkgutil", "runpy"})
REGULAR_MODES = frozenset({"100644", "100755"})
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")
SYMBOL_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")
IDENTIFIER_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]*\Z")

EXPECTED_SOURCE_KEYS = frozenset(
    {
        "schema_id",
        "schema_version",
        "registry_id",
        "status",
        "authority_policy",
        "artifacts",
        "role_grants",
        "terminal_prefix_authority",
        "branch_bindings",
        "authority_denials",
        "proof_boundary",
    }
)
ARTIFACT_IDENTITY_KEYS = (
    "artifact_id",
    "kind",
    "path",
    "symbol",
    "semantic_digest_method",
)
ARTIFACT_PIN_KEYS = (
    "expected_blob_sha256",
    "expected_symbol_ast_sha256",
    "expected_local_import_closure_digest",
    "expected_semantic_sha256",
)
GRANT_IDENTITY_KEYS = (
    "grant_id",
    "role",
    "artifact_id",
    "schedule_id",
    "capabilities",
    "authority_class",
)
GRANT_PIN_KEY = "expected_artifact_semantic_sha256"
EXPECTED_POLICY = {
    "source": AUTHORITY_SOURCE,
    "worktree_authority": False,
    "caller_override_authority": False,
    "allowed_executable_roots": list(ALLOWED_EXECUTABLE_ROOTS),
    "forbidden_executable_roots": list(FORBIDDEN_EXECUTABLE_ROOTS),
    "fixed_schedule_id": SCHEDULE_ID,
    "allowed_roles": list(ALLOWED_ROLES),
}
EXPECTED_ARTIFACT_IDENTITIES = [
    {
        "artifact_id": VERIFIER_ARTIFACT_ID,
        "kind": "PYTHON_SYMBOL",
        "path": VERIFIER_PATH,
        "symbol": VERIFIER_SYMBOL,
        "semantic_digest_method": DIGEST_METHOD,
    },
    {
        "artifact_id": SCHEDULER_ARTIFACT_ID,
        "kind": "PYTHON_SYMBOL",
        "path": SCHEDULER_PATH,
        "symbol": SCHEDULER_SYMBOL,
        "semantic_digest_method": DIGEST_METHOD,
    },
]
EXPECTED_GRANT_IDENTITIES = [
    {
        "grant_id": VERIFIER_GRANT_ID,
        "role": "INDEPENDENT_COVERAGE_VERIFIER",
        "artifact_id": VERIFIER_ARTIFACT_ID,
        "schedule_id": SCHEDULE_ID,
        "capabilities": list(VERIFIER_CAPABILITIES),
        "authority_class": AUTHORITY_CLASS,
    },
    {
        "grant_id": SCHEDULER_GRANT_ID,
        "role": "TERMINAL_SCHEDULER",
        "artifact_id": SCHEDULER_ARTIFACT_ID,
        "schedule_id": SCHEDULE_ID,
        "capabilities": list(SCHEDULER_CAPABILITIES),
        "authority_class": AUTHORITY_CLASS,
    },
]
EXPECTED_PREFIX = {
    "schedule_id": SCHEDULE_ID,
    "scheduler_grant_id": SCHEDULER_GRANT_ID,
    "coverage_verifier_grant_id": VERIFIER_GRANT_ID,
    "domain_schema_id": "q1_priority_prefix_domain_v1",
    "evidence_schema_id": "t6_q_one_priority_prefix_evidence_v1",
    "ordered_gaps": [3, 7, 11],
    "next_unchecked_gap": 15,
    "candidate_order": "gap_ascending_divisor_ascending_type_I_before_II",
    "coverage_scope": "REGISTERED_PRIORITY_PREFIX_GAPS_3_7_11",
    "coverage_semantics": "REGISTERED_PRIORITY_ONLY",
    "global_exhaustion": False,
    "outcomes": ["PREFIX_MISS_EVIDENCE_ONLY", "ROOT_TERMINAL_HIT"],
    "terminal_hit_semantics": "ROOT_TERMINAL_EVIDENCE_ONLY_NO_ISSUER",
    "prefix_miss_semantics": "REGISTERED_PREFIX_MISS_EVIDENCE_ONLY_NO_E1",
    "issuer_authorized": False,
}
EXPECTED_DENIALS = {
    "issuer_count": 0,
    "issuer_authority": False,
    "e1_authority": False,
    "queue_authority": False,
    "producer_authority": False,
    "initializer_authority": False,
    "t5_authority": False,
}


class RegistryV2Error(ValueError):
    """Fail-closed resolver error with a stable code."""

    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


@dataclass(frozen=True, slots=True)
class GitEntryV2:
    mode: str
    object_type: str
    object_id: str
    path: str


def _reject(code: str, detail: str) -> NoReturn:
    raise RegistryV2Error(code, detail)


def _strict_json_copy(value: Any, path: str = "$") -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject("NONCANONICAL_VALUE", f"{path} has a non-builtin string key")
            result[key] = _strict_json_copy(child, f"{path}.{key}")
        return result
    if type(value) is list:
        return [_strict_json_copy(child, f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return value
    _reject("NONCANONICAL_VALUE", f"{path} has unsupported {type(value).__name__}")


def canonical_json_bytes_v2(value: Any) -> bytes:
    normalized = _strict_json_copy(value)
    return json.dumps(
        normalized,
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("ascii")


def canonical_digest_v2(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes_v2(value)).hexdigest()


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _ast_authority_contract_digest_v2(contract_version: str) -> str:
    return canonical_digest_v2(
        {
            "schema_id": "t6_python_ast_authority_contract_v2",
            "ast_dump_contract_version": contract_version,
            "status": "HEAD_BOUND_SYMBOL_AND_IMPORT_CLOSURE_AUTHORITY",
        }
    )


def _python_ast_contract_diagnostic_v2(
    implementation: str, major_minor: str
) -> dict[str, Any]:
    return {
        **python_ast_contract_v2(),
        "python_implementation": implementation,
        "python_major_minor": major_minor,
    }


def python_ast_contract_v2() -> dict[str, Any]:
    semantic_payload: dict[str, Any] = {
        "schema_id": "t6_python_ast_authority_contract_v2",
        "ast_dump_contract_version": AST_DUMP_CONTRACT_VERSION,
        "status": "HEAD_BOUND_SYMBOL_AND_IMPORT_CLOSURE_AUTHORITY",
    }
    return {
        **semantic_payload,
        "digest": _ast_authority_contract_digest_v2(AST_DUMP_CONTRACT_VERSION),
    }


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
        _reject("GIT_ERROR", f"git {' '.join(args)} failed: {detail}")
    return completed.stdout


def _repository_root(locator: Path) -> Path:
    try:
        return Path(
            _run_git(locator.resolve(), ("rev-parse", "--show-toplevel"))
            .decode("utf-8")
            .strip()
        ).resolve()
    except UnicodeDecodeError as exc:
        raise RegistryV2Error("GIT_ERROR", "repository root is not UTF-8") from exc


def _object_format(root: Path) -> tuple[str, int]:
    value = _run_git(root, ("rev-parse", "--show-object-format")).decode("ascii").strip()
    if value == "sha1":
        return value, 40
    if value == "sha256":
        return value, 64
    _reject("GIT_ERROR", f"unsupported Git object format {value!r}")


def _exact_commit(root: Path, requested_head: str) -> tuple[str, str, str]:
    object_format, oid_length = _object_format(root)
    if (
        type(requested_head) is not str
        or len(requested_head) != oid_length
        or any(character not in "0123456789abcdef" for character in requested_head)
    ):
        _reject("INVALID_HEAD", "requested_head must be one exact full lowercase commit ID")
    object_type = _run_git(root, ("cat-file", "-t", requested_head)).decode().strip()
    if object_type != "commit":
        _reject("INVALID_HEAD", "requested object is not a commit")
    resolved = _run_git(root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}"))
    if resolved.decode("ascii").strip() != requested_head:
        _reject("INVALID_HEAD", "requested commit did not resolve exactly")
    tree_sha = _run_git(root, ("rev-parse", f"{requested_head}^{{tree}}"))
    tree_sha_text = tree_sha.decode("ascii").strip()
    if len(tree_sha_text) != oid_length:
        _reject("GIT_ERROR", "commit tree is not a full object ID")
    return requested_head, tree_sha_text, object_format


def _safe_path(value: Any, *, executable: bool = False) -> str:
    if type(value) is not str or not value or PATH_RE.fullmatch(value) is None:
        _reject("UNSAFE_PATH", f"invalid repository path {value!r}")
    pure = PurePosixPath(value)
    if (
        pure.is_absolute()
        or value != pure.as_posix()
        or any(part in {"", ".", ".."} for part in pure.parts)
        or "\\" in value
    ):
        _reject("UNSAFE_PATH", f"non-normal repository path {value!r}")
    if executable:
        root_name = pure.parts[0]
        if root_name not in ALLOWED_EXECUTABLE_ROOTS or root_name in FORBIDDEN_EXECUTABLE_ROOTS:
            _reject("FORBIDDEN_EXECUTABLE_ROOT", value)
        if pure.suffix != ".py":
            _reject("FORBIDDEN_EXECUTABLE_ROOT", "executable artifact must be Python")
    return value


def _tree_entries(root: Path, head_sha: str) -> dict[str, GitEntryV2]:
    raw = _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head_sha))
    result: dict[str, GitEntryV2] = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            metadata, path_bytes = record.split(b"\t", 1)
            mode, object_type, object_id = metadata.decode("ascii").split(" ")
            path = path_bytes.decode("utf-8")
        except (UnicodeDecodeError, ValueError) as exc:
            raise RegistryV2Error("GIT_TREE_INVALID", repr(record)) from exc
        pure = PurePosixPath(path)
        if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
            _reject("GIT_TREE_INVALID", f"unsafe tracked path {path!r}")
        if path in result:
            _reject("GIT_TREE_INVALID", f"duplicate tracked path {path!r}")
        result[path] = GitEntryV2(mode, object_type, object_id, path)
    return result


def _blob(root: Path, entry: GitEntryV2) -> bytes:
    if entry.object_type != "blob" or entry.mode not in REGULAR_MODES:
        _reject("INVALID_GIT_MODE", f"{entry.path!r} is not a regular tracked blob")
    return _run_git(root, ("cat-file", "blob", entry.object_id))


def _required_blob(
    root: Path,
    entries: Mapping[str, GitEntryV2],
    path: str,
    *,
    executable: bool = False,
) -> tuple[GitEntryV2, bytes]:
    safe = _safe_path(path, executable=executable)
    entry = entries.get(safe)
    if entry is None:
        _reject("MISSING_ARTIFACT", f"{safe!r} is absent from requested HEAD")
    return entry, _blob(root, entry)


def _capture_toolchain_binding(
    root: Path, entries: Mapping[str, GitEntryV2], head_sha: str
) -> dict[str, Any]:
    files: list[dict[str, Any]] = []
    head_blobs: dict[str, bytes] = {}
    for path in TOOLCHAIN_PATHS:
        entry, head_bytes = _required_blob(
            root, entries, path, executable=path == RESOLVER_PATH
        )
        worktree = root / path
        if worktree.is_symlink() or not worktree.is_file():
            _reject("DIRTY_TOOLCHAIN", f"{path} is not a regular worktree file")
        if worktree.read_bytes() != head_bytes:
            _reject("TOOLCHAIN_WORKTREE_MISMATCH", f"{path} differs from requested HEAD")
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
        _reject(
            "EXECUTING_RESOLVER_HEAD_MISMATCH",
            "executing resolver bytes differ from requested-HEAD resolver",
        )
    payload: dict[str, Any] = {
        "schema_id": "t6_coordinator_role_registry_toolchain_binding_v2",
        "head_sha": head_sha,
        "files": files,
        "status": "BOUND_SELF_SCHEMA_AND_REGISTRY_TO_CLEAN_REQUESTED_HEAD",
    }
    payload["digest"] = canonical_digest_v2(payload)
    return payload


def load_json_object_strict_v2(value: bytes, *, source: str) -> dict[str, Any]:
    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, child in pairs:
            if key in result:
                _reject("DUPLICATE_JSON_KEY", f"duplicate key {key!r} in {source}")
            result[key] = child
        return result

    def reject_number(number: str) -> NoReturn:
        _reject("NONINTEGER_JSON", f"noninteger/nonfinite number {number!r} in {source}")

    try:
        decoded = json.loads(
            value.decode("utf-8"),
            object_pairs_hook=object_pairs,
            parse_float=reject_number,
            parse_constant=reject_number,
        )
    except RegistryV2Error:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        raise RegistryV2Error("INVALID_JSON", f"invalid JSON in {source}: {exc}") from exc
    if type(decoded) is not dict:
        _reject("SOURCE_SCHEMA_INVALID", f"{source} is not an object")
    _strict_json_copy(decoded)
    return decoded


def _validate_with_head_schema(
    root: Path,
    entries: Mapping[str, GitEntryV2],
    head_sha: str,
    source: Mapping[str, Any],
) -> None:
    _, schema_bytes = _required_blob(root, entries, SCHEMA_PATH)
    schema = load_json_object_strict_v2(schema_bytes, source=f"{head_sha}:{SCHEMA_PATH}")
    try:
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(schema)
    except jsonschema.exceptions.SchemaError as exc:
        raise RegistryV2Error("HEAD_SCHEMA_INVALID", exc.message) from exc
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
        _reject("SOURCE_SCHEMA_INVALID", f"{location}: {error.message}")


def _validate_source(source: Mapping[str, Any]) -> None:
    if frozenset(source) != EXPECTED_SOURCE_KEYS:
        _reject("SOURCE_SCHEMA_INVALID", "source registry field set changed")
    if (
        source["schema_id"] != SCHEMA_ID
        or source["registry_id"] != SCHEMA_ID
        or type(source["schema_version"]) is not int
        or source["schema_version"] != SCHEMA_VERSION
        or source["status"] != STATUS
    ):
        _reject("FIXED_REGISTRY_MISMATCH", "registry identity or status changed")
    if source["authority_policy"] != EXPECTED_POLICY:
        _reject("CALLER_OVERRIDE_REJECTED", "authority policy changed")
    artifacts = source["artifacts"]
    if type(artifacts) is not list or len(artifacts) != len(
        EXPECTED_ARTIFACT_IDENTITIES
    ):
        _reject("FIXED_GRANT_MISMATCH", "artifact allowlist cardinality changed")
    for source_artifact, expected_identity in zip(
        artifacts, EXPECTED_ARTIFACT_IDENTITIES, strict=True
    ):
        if type(source_artifact) is not dict or any(
            source_artifact.get(key) != expected_identity[key]
            for key in ARTIFACT_IDENTITY_KEYS
        ):
            _reject("FIXED_GRANT_MISMATCH", "artifact identity allowlist changed")
        for key in ARTIFACT_PIN_KEYS:
            value = source_artifact.get(key)
            if (
                type(value) is not str
                or len(value) != 64
                or any(character not in "0123456789abcdef" for character in value)
            ):
                _reject("SOURCE_SCHEMA_INVALID", f"artifact pin {key} is malformed")
    grants = source["role_grants"]
    if type(grants) is not list or len(grants) != len(EXPECTED_GRANT_IDENTITIES):
        _reject("FIXED_GRANT_MISMATCH", "role grant cardinality changed")
    for source_grant, expected_identity in zip(
        grants, EXPECTED_GRANT_IDENTITIES, strict=True
    ):
        if type(source_grant) is not dict or any(
            source_grant.get(key) != expected_identity[key]
            for key in GRANT_IDENTITY_KEYS
        ):
            _reject("FIXED_GRANT_MISMATCH", "role grant allowlist changed")
        pin = source_grant.get(GRANT_PIN_KEY)
        if (
            type(pin) is not str
            or len(pin) != 64
            or any(character not in "0123456789abcdef" for character in pin)
        ):
            _reject("SOURCE_SCHEMA_INVALID", "grant semantic pin is malformed")
    if source["terminal_prefix_authority"] != EXPECTED_PREFIX:
        _reject("FIXED_SCHEDULE_MISMATCH", "terminal prefix contract changed")
    if source["branch_bindings"] != []:
        _reject("BRANCH_AUTHORITY_FORBIDDEN", "branch bindings are not authorized")
    if source["authority_denials"] != EXPECTED_DENIALS:
        _reject("FORBIDDEN_AUTHORITY", "issuer/E1/queue/producer denial changed")
    boundary = source["proof_boundary"]
    if type(boundary) is not str or STATUS not in boundary:
        _reject("SOURCE_SCHEMA_INVALID", "proof boundary does not preserve status")


def _parse_python(value: bytes, path: str) -> ast.Module:
    try:
        return ast.parse(value.decode("utf-8"), filename=path)
    except (UnicodeDecodeError, SyntaxError) as exc:
        raise RegistryV2Error("PYTHON_PARSE_ERROR", f"cannot parse {path}: {exc}") from exc


def _stable_ast_value(value: Any) -> Any:
    if isinstance(value, ast.AST):
        result: dict[str, Any] = {"_type": type(value).__name__}
        for name, child in ast.iter_fields(value):
            if name == "type_params" and child == []:
                continue
            result[name] = _stable_ast_value(child)
        return result
    if type(value) is list:
        return [_stable_ast_value(child) for child in value]
    if value is None or type(value) in {str, bool, int}:
        return value
    _reject("PYTHON_AST_UNSUPPORTED", f"unsupported AST field {type(value).__name__}")


def _target_names(target: ast.AST) -> tuple[str, ...]:
    if isinstance(target, ast.Name):
        return (target.id,)
    if isinstance(target, ast.Starred):
        return _target_names(target.value)
    if isinstance(target, (ast.Tuple, ast.List)):
        return tuple(name for child in target.elts for name in _target_names(child))
    return ()


class _NamedExpressionVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.bindings: list[tuple[str, ast.AST, str]] = []

    def visit_Lambda(self, node: ast.Lambda) -> None:
        del node

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.bindings.extend(
            (name, node, "NAMED_EXPR") for name in _target_names(node.target)
        )
        self.visit(node.value)


def _expression_bindings(value: ast.AST | None) -> list[tuple[str, ast.AST, str]]:
    if value is None:
        return []
    visitor = _NamedExpressionVisitor()
    visitor.visit(value)
    return visitor.bindings


def _pattern_names(pattern: ast.pattern) -> tuple[str, ...]:
    names: list[str] = []
    for node in ast.walk(pattern):
        if isinstance(node, ast.MatchAs) and node.name is not None:
            names.append(node.name)
        elif isinstance(node, ast.MatchStar) and node.name is not None:
            names.append(node.name)
        elif isinstance(node, ast.MatchMapping) and node.rest is not None:
            names.append(node.rest)
    return tuple(names)


def _module_scope_bindings(
    statements: Iterable[ast.stmt], *, direct: bool = True
) -> list[tuple[str, ast.AST, str]]:
    result: list[tuple[str, ast.AST, str]] = []

    def bind_targets(target: ast.AST, node: ast.AST, kind: str) -> None:
        result.extend((name, node, kind) for name in _target_names(target))

    def scan_expressions(*values: ast.AST | None) -> None:
        for value in values:
            result.extend(_expression_bindings(value))

    for node in statements:
        if isinstance(node, ast.FunctionDef):
            result.append((node.name, node, "DIRECT_FUNCTION" if direct else "CONDITIONAL_FUNCTION"))
            scan_expressions(
                *node.decorator_list,
                *node.args.defaults,
                *node.args.kw_defaults,
                node.returns,
            )
        elif isinstance(node, ast.AsyncFunctionDef):
            result.append((node.name, node, "ASYNC_FUNCTION"))
            scan_expressions(
                *node.decorator_list,
                *node.args.defaults,
                *node.args.kw_defaults,
                node.returns,
            )
        elif isinstance(node, ast.ClassDef):
            result.append((node.name, node, "CLASS"))
            scan_expressions(
                *node.decorator_list,
                *node.bases,
                *(keyword.value for keyword in node.keywords),
            )
        elif isinstance(node, ast.Import):
            for alias in node.names:
                result.append((alias.asname or alias.name.split(".")[0], node, "IMPORT"))
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.name == "*":
                    result.append(("*", node, "STAR_IMPORT"))
                else:
                    result.append((alias.asname or alias.name, node, "IMPORT_FROM"))
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                bind_targets(target, node, "ASSIGN")
            scan_expressions(node.value)
        elif isinstance(node, ast.AnnAssign):
            bind_targets(node.target, node, "ANN_ASSIGN")
            scan_expressions(node.annotation, node.value)
        elif isinstance(node, ast.AugAssign):
            bind_targets(node.target, node, "AUG_ASSIGN")
            scan_expressions(node.value)
        elif isinstance(node, (ast.For, ast.AsyncFor)):
            bind_targets(node.target, node, "FOR_TARGET")
            scan_expressions(node.iter)
            result.extend(_module_scope_bindings(node.body, direct=False))
            result.extend(_module_scope_bindings(node.orelse, direct=False))
        elif isinstance(node, (ast.With, ast.AsyncWith)):
            for item in node.items:
                scan_expressions(item.context_expr)
                if item.optional_vars is not None:
                    bind_targets(item.optional_vars, node, "WITH_TARGET")
            result.extend(_module_scope_bindings(node.body, direct=False))
        elif isinstance(node, ast.If):
            scan_expressions(node.test)
            result.extend(_module_scope_bindings(node.body, direct=False))
            result.extend(_module_scope_bindings(node.orelse, direct=False))
        elif isinstance(node, ast.While):
            scan_expressions(node.test)
            result.extend(_module_scope_bindings(node.body, direct=False))
            result.extend(_module_scope_bindings(node.orelse, direct=False))
        elif isinstance(node, (ast.Try, ast.TryStar)):
            result.extend(_module_scope_bindings(node.body, direct=False))
            result.extend(_module_scope_bindings(node.orelse, direct=False))
            result.extend(_module_scope_bindings(node.finalbody, direct=False))
            for handler in node.handlers:
                scan_expressions(handler.type)
                if handler.name is not None:
                    result.append((handler.name, handler, "EXCEPT_TARGET"))
                result.extend(_module_scope_bindings(handler.body, direct=False))
        elif isinstance(node, ast.Match):
            scan_expressions(node.subject)
            for case in node.cases:
                result.extend(
                    (name, case.pattern, "MATCH_TARGET")
                    for name in _pattern_names(case.pattern)
                )
                scan_expressions(case.guard)
                result.extend(_module_scope_bindings(case.body, direct=False))
        elif isinstance(node, ast.Delete):
            for target in node.targets:
                bind_targets(target, node, "DELETE")
        elif isinstance(node, ast.Expr):
            scan_expressions(node.value)
        elif isinstance(node, ast.Assert):
            scan_expressions(node.test, node.msg)
        elif isinstance(node, ast.Raise):
            scan_expressions(node.exc, node.cause)
        elif isinstance(node, ast.TypeAlias):
            bind_targets(node.name, node, "TYPE_ALIAS")
            scan_expressions(node.value)
    return result


def _symbol_receipt(path: str, symbol: str, value: bytes, blob_sha256: str) -> dict[str, str]:
    if type(symbol) is not str or SYMBOL_RE.fullmatch(symbol) is None:
        _reject("SYMBOL_INVALID", f"invalid symbol {symbol!r}")
    tree = _parse_python(value, path)
    bindings = _module_scope_bindings(tree.body)
    if any(name == "*" for name, _, _ in bindings):
        _reject("STAR_IMPORT_FORBIDDEN", f"{path} contains a module-scope star import")
    matches = [
        (node, kind) for name, node, kind in bindings if name == symbol
    ]
    if not matches:
        _reject("SYMBOL_MISSING", f"{path}:{symbol}")
    if len(matches) != 1:
        _reject("SYMBOL_AMBIGUITY", f"{path}:{symbol} has {len(matches)} bindings")
    node, kind = matches[0]
    if type(node) is not ast.FunctionDef or kind != "DIRECT_FUNCTION":
        _reject("SYMBOL_NOT_FUNCTION", f"{path}:{symbol}")
    if node.decorator_list:
        _reject("AUTHORIZED_SYMBOL_DECORATED", f"{path}:{symbol}")
    ast_sha = canonical_digest_v2(_stable_ast_value(node))
    return {"symbol_ast_sha256": ast_sha, "blob_sha256": blob_sha256}


def _module_aliases(path: str) -> tuple[str, ...]:
    pure = PurePosixPath(path)
    if len(pure.parts) < 2 or pure.parts[0] not in LOCAL_PYTHON_ROOTS:
        return ()
    if pure.suffix != ".py":
        return ()
    relative = PurePosixPath(*pure.parts[1:])
    if relative.name == "__init__.py":
        parts = relative.parent.parts
    else:
        parts = relative.with_suffix("").parts
    if not parts:
        return (pure.parts[0],)
    unqualified = ".".join(parts)
    qualified = ".".join((pure.parts[0], *parts))
    return tuple(sorted({unqualified, qualified}))


def _module_index(entries: Mapping[str, GitEntryV2]) -> dict[str, tuple[str, ...]]:
    values: dict[str, set[str]] = {}
    for path in entries:
        for alias in _module_aliases(path):
            values.setdefault(alias, set()).add(path)
    return {alias: tuple(sorted(paths)) for alias, paths in values.items()}


def _import_targets(tree: ast.AST, source_path: str) -> tuple[str, ...]:
    targets: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root_name = alias.name.split(".", 1)[0]
                if root_name in DYNAMIC_LOADING_MODULES:
                    _reject("DYNAMIC_IMPORT_FORBIDDEN", f"{source_path} imports {root_name}")
                if root_name in FORBIDDEN_EXECUTABLE_ROOTS:
                    _reject("FORBIDDEN_IMPORT_ROOT", f"{source_path} imports {alias.name}")
                targets.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                _reject("RELATIVE_IMPORT_FORBIDDEN", f"{source_path} uses a relative import")
            if node.module:
                root_name = node.module.split(".", 1)[0]
                if root_name in DYNAMIC_LOADING_MODULES:
                    _reject("DYNAMIC_IMPORT_FORBIDDEN", f"{source_path} imports {root_name}")
                if root_name in FORBIDDEN_EXECUTABLE_ROOTS:
                    _reject("FORBIDDEN_IMPORT_ROOT", f"{source_path} imports {node.module}")
                targets.add(node.module)
                targets.update(
                    f"{node.module}.{alias.name}"
                    for alias in node.names
                    if alias.name != "*"
                )
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in {
                "__import__",
                "compile",
                "delattr",
                "eval",
                "exec",
                "getattr",
                "globals",
                "locals",
                "setattr",
                "vars",
            }:
                _reject("DYNAMIC_IMPORT_FORBIDDEN", source_path)
        elif (
            isinstance(node, ast.Attribute)
            and isinstance(node.value, ast.Name)
            and node.value.id == "sys"
            and node.attr in {"meta_path", "modules", "path", "path_hooks"}
        ):
            _reject("DYNAMIC_IMPORT_FORBIDDEN", f"{source_path} mutates/reads sys.{node.attr}")
        elif isinstance(node, ast.Name) and node.id == "__builtins__":
            _reject("DYNAMIC_IMPORT_FORBIDDEN", f"{source_path} reads __builtins__")
    return tuple(sorted(targets))


def _resolve_import_target(
    target: str, module_index: Mapping[str, Sequence[str]], source_path: str
) -> tuple[str, ...]:
    parts = tuple(part for part in target.split(".") if part)
    resolved: set[str] = set()
    for length in range(1, len(parts) + 1):
        alias = ".".join(parts[:length])
        candidates = tuple(module_index.get(alias, ()))
        if len(candidates) > 1:
            _reject("AMBIGUOUS_LOCAL_IMPORT", f"{source_path} imports {alias}: {candidates}")
        if candidates:
            resolved.add(candidates[0])
    return tuple(sorted(resolved))


def _local_import_closure(
    root: Path,
    entries: Mapping[str, GitEntryV2],
    root_path: str,
) -> tuple[tuple[dict[str, Any], ...], tuple[str, ...], str]:
    index = _module_index(entries)
    pending = [root_path]
    closure: dict[str, dict[str, Any]] = {}
    direct_imports: tuple[str, ...] = ()
    while pending:
        path = pending.pop()
        if path in closure:
            continue
        entry, value = _required_blob(root, entries, path, executable=True)
        tree = _parse_python(value, path)
        dependencies: set[str] = set()
        for target in _import_targets(tree, path):
            dependencies.update(_resolve_import_target(target, index, path))
        if path == root_path:
            direct_imports = tuple(sorted(dependencies))
        for dependency in dependencies:
            dependency_root = PurePosixPath(dependency).parts[0]
            if dependency_root != "scripts":
                _reject("FORBIDDEN_IMPORT_ROOT", f"{root_path} reaches {dependency}")
        closure[path] = {
            "path": path,
            "git_mode": entry.mode,
            "git_object_id": entry.object_id,
            "blob_sha256": _sha256(value),
        }
        pending.extend(path for path in sorted(dependencies, reverse=True) if path not in closure)
    files = tuple(closure[path] for path in sorted(closure))
    digest = canonical_digest_v2(
        {"schema_id": "t6_local_python_import_closure_v2", "files": list(files)}
    )
    return files, direct_imports, digest


def _resolve_artifacts(
    root: Path,
    entries: Mapping[str, GitEntryV2],
    sources: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    raw: list[tuple[Mapping[str, Any], GitEntryV2, bytes, str]] = []
    for source in sources:
        path = _safe_path(source["path"], executable=True)
        entry, value = _required_blob(root, entries, path, executable=True)
        raw.append((source, entry, value, _sha256(value)))
    paths = [item[0]["path"] for item in raw]
    if len(paths) != len(set(paths)):
        _reject("ROLE_PATH_COLLISION", "scheduler and verifier share a module path")
    blobs = [item[3] for item in raw]
    if len(blobs) != len(set(blobs)):
        _reject("ROLE_BLOB_COLLISION", "scheduler and verifier module bytes are identical")

    resolved: list[dict[str, Any]] = []
    for source, entry, value, blob_sha in raw:
        path = source["path"]
        symbol = source["symbol"]
        symbol_receipt = _symbol_receipt(path, symbol, value, blob_sha)
        closure_files, direct_imports, closure_digest = _local_import_closure(
            root, entries, path
        )
        ast_contract = python_ast_contract_v2()
        semantic = canonical_digest_v2(
            {
                "method": DIGEST_METHOD,
                "path": path,
                "symbol": symbol,
                "blob_sha256": blob_sha,
                "symbol_ast_sha256": symbol_receipt["symbol_ast_sha256"],
                "local_import_closure_digest": closure_digest,
                "python_ast_contract_digest": ast_contract["digest"],
            }
        )
        resolved.append(
            {
                "artifact_id": source["artifact_id"],
                "kind": "PYTHON_SYMBOL",
                "path": path,
                "symbol": symbol,
                "semantic_digest_method": DIGEST_METHOD,
                "git_mode": entry.mode,
                "git_object_id": entry.object_id,
                "blob_sha256": blob_sha,
                "symbol_ast_sha256": symbol_receipt["symbol_ast_sha256"],
                "python_ast_contract_digest": ast_contract["digest"],
                "direct_local_import_paths": list(direct_imports),
                "local_import_closure_files": list(closure_files),
                "local_import_closure_digest": closure_digest,
                "semantic_sha256": semantic,
                **{key: source[key] for key in ARTIFACT_PIN_KEYS},
            }
        )
    by_id = {item["artifact_id"]: item for item in resolved}
    scheduler = by_id[SCHEDULER_ARTIFACT_ID]
    verifier = by_id[VERIFIER_ARTIFACT_ID]
    scheduler_closure = {item["path"] for item in scheduler["local_import_closure_files"]}
    verifier_closure = {item["path"] for item in verifier["local_import_closure_files"]}
    if VERIFIER_PATH in scheduler_closure:
        _reject("ROLE_IMPORT_CYCLE", "scheduler imports the independent verifier")
    if SCHEDULER_PATH in verifier_closure:
        _reject("VERIFIER_IMPORTS_SCHEDULER", "verifier imports the scheduler")
    for forbidden in (LEGACY_RUNTIME_PATH,):
        if forbidden in scheduler_closure or forbidden in verifier_closure:
            _reject("FORBIDDEN_AUTHORIZED_IMPORT", forbidden)
    if any(path.startswith("reproductions/") for path in verifier_closure):
        _reject("VERIFIER_IMPORTS_REPRODUCTION", repr(sorted(verifier_closure)))
    shared_dependencies = (scheduler_closure - {SCHEDULER_PATH}) & (
        verifier_closure - {VERIFIER_PATH}
    )
    if shared_dependencies:
        _reject(
            "SHARED_LOCAL_IMPORT_CLOSURE",
            f"scheduler and verifier share {sorted(shared_dependencies)}",
        )

    source_map = {source["artifact_id"]: source for source in sources}
    for artifact_id, artifact in by_id.items():
        expected = source_map[artifact_id]
        observed_pins = {
            "expected_blob_sha256": artifact["blob_sha256"],
            "expected_symbol_ast_sha256": artifact["symbol_ast_sha256"],
            "expected_local_import_closure_digest": artifact[
                "local_import_closure_digest"
            ],
            "expected_semantic_sha256": artifact["semantic_sha256"],
        }
        for key, observed in observed_pins.items():
            if expected[key] != observed:
                _reject(
                    "ARTIFACT_PIN_MISMATCH",
                    f"{artifact_id}.{key}: expected {expected[key]}, observed {observed}",
                )
    return sorted(resolved, key=lambda item: item["artifact_id"])


def _resolve_grants(
    sources: Sequence[Mapping[str, Any]], artifacts: Mapping[str, Mapping[str, Any]]
) -> list[dict[str, Any]]:
    resolved: list[dict[str, Any]] = []
    for source in sources:
        role = source["role"]
        if role not in ALLOWED_ROLES:
            _reject("UNKNOWN_ROLE", role)
        artifact = artifacts.get(source["artifact_id"])
        if artifact is None:
            _reject("UNKNOWN_ARTIFACT", source["artifact_id"])
        if source[GRANT_PIN_KEY] != artifact["semantic_sha256"]:
            _reject(
                "GRANT_PIN_MISMATCH",
                f"{source['grant_id']} does not pin its resolved artifact semantic digest",
            )
        resolved.append(
            {
                **dict(source),
                "artifact_path": artifact["path"],
                "artifact_symbol": artifact["symbol"],
                "artifact_blob_sha256": artifact["blob_sha256"],
                "artifact_closure_digest": artifact["local_import_closure_digest"],
                "artifact_semantic_sha256": artifact["semantic_sha256"],
            }
        )
    return sorted(resolved, key=lambda item: item["grant_id"])


def resolve_registry_v2(*, root: Path, requested_head: str) -> dict[str, Any]:
    """Resolve the fixed registry without accepting a source or callable override."""

    repository = _repository_root(root)
    head_sha, tree_sha, object_format = _exact_commit(repository, requested_head)
    entries = _tree_entries(repository, head_sha)
    initial_binding = _capture_toolchain_binding(repository, entries, head_sha)
    registry_entry, registry_bytes = _required_blob(repository, entries, REGISTRY_PATH)
    source = load_json_object_strict_v2(
        registry_bytes, source=f"{head_sha}:{REGISTRY_PATH}"
    )
    _validate_with_head_schema(repository, entries, head_sha, source)
    _validate_source(source)

    resolved_artifacts = _resolve_artifacts(repository, entries, source["artifacts"])
    artifact_map = {item["artifact_id"]: item for item in resolved_artifacts}
    if len(artifact_map) != 2:
        _reject("FIXED_GRANT_MISMATCH", "resolved artifact cardinality changed")
    resolved_grants = _resolve_grants(source["role_grants"], artifact_map)
    if len(resolved_grants) != 2:
        _reject("FIXED_GRANT_MISMATCH", "resolved grant cardinality changed")

    grant_map = {item["grant_id"]: item for item in resolved_grants}
    prefix = dict(source["terminal_prefix_authority"])
    scheduler_grant = grant_map[prefix["scheduler_grant_id"]]
    verifier_grant = grant_map[prefix["coverage_verifier_grant_id"]]
    if (
        scheduler_grant["role"] != "TERMINAL_SCHEDULER"
        or verifier_grant["role"] != "INDEPENDENT_COVERAGE_VERIFIER"
    ):
        _reject("FIXED_GRANT_MISMATCH", "schedule points to the wrong role")
    resolved_prefix = {
        **prefix,
        "scheduler_artifact_id": scheduler_grant["artifact_id"],
        "scheduler_artifact_semantic_sha256": scheduler_grant[
            "artifact_semantic_sha256"
        ],
        "scheduler_artifact_closure_digest": scheduler_grant[
            "artifact_closure_digest"
        ],
        "coverage_verifier_artifact_id": verifier_grant["artifact_id"],
        "coverage_verifier_artifact_semantic_sha256": verifier_grant[
            "artifact_semantic_sha256"
        ],
        "coverage_verifier_artifact_closure_digest": verifier_grant[
            "artifact_closure_digest"
        ],
        "issuer_count": 0,
        "e1_authority": False,
        "queue_authority": False,
    }

    role_subdigests = {
        "terminal_scheduler_registry": canonical_digest_v2(
            {
                "schema_id": "t6_role_subregistry_v2",
                "head_sha": head_sha,
                "role": "TERMINAL_SCHEDULER",
                "grants": [scheduler_grant],
            }
        ),
        "independent_coverage_verifier_registry": canonical_digest_v2(
            {
                "schema_id": "t6_role_subregistry_v2",
                "head_sha": head_sha,
                "role": "INDEPENDENT_COVERAGE_VERIFIER",
                "grants": [verifier_grant],
            }
        ),
        "terminal_prefix_registry": canonical_digest_v2(
            {
                "schema_id": "t6_terminal_prefix_subregistry_v2",
                "head_sha": head_sha,
                "prefix": resolved_prefix,
            }
        ),
    }
    role_manifest: dict[str, Any] = {
        "schema_id": "t6_head_bound_role_capability_manifest_v2",
        "head_sha": head_sha,
        "status": STATUS,
        "grants": resolved_grants,
        "terminal_prefix": resolved_prefix,
        "issuer_count": 0,
        "e1_authority": False,
        "queue_authority": False,
        "producer_authority": False,
        "initializer_authority": False,
        "t5_authority": False,
    }
    role_manifest["digest"] = canonical_digest_v2(role_manifest)

    final_binding = _capture_toolchain_binding(repository, entries, head_sha)
    if final_binding != initial_binding:
        _reject("TOOLCHAIN_CHANGED_DURING_RESOLUTION", "toolchain changed during replay")

    payload: dict[str, Any] = {
        "schema_id": RESOLVED_SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "artifact_policy": "EPHEMERAL_EXACT_HEAD_CAPABILITY_MANIFEST_NOT_TRACKED",
        "head_sha": head_sha,
        "head_tree_sha": tree_sha,
        "git_object_format": object_format,
        "registry_path": REGISTRY_PATH,
        "registry_git_mode": registry_entry.mode,
        "registry_git_object_id": registry_entry.object_id,
        "registry_source_sha256": _sha256(registry_bytes),
        "execution_binding": initial_binding,
        "python_ast_contract": python_ast_contract_v2(),
        "resolved_artifacts": resolved_artifacts,
        "resolved_role_grants": resolved_grants,
        "authorized_terminal_prefixes": [resolved_prefix],
        "authorized_branches": [],
        "role_authority_manifest": role_manifest,
        "role_subdigests": role_subdigests,
        "role_grant_counts": {
            "INDEPENDENT_COVERAGE_VERIFIER": 1,
            "TERMINAL_SCHEDULER": 1,
        },
        "active_role_grant_count": 2,
        "terminal_prefix_authority_count": 1,
        "issuer_count": 0,
        "issuer_authority": False,
        "e1_authority": False,
        "queue_authority": False,
        "producer_authority": False,
        "initializer_authority": False,
        "t5_authority": False,
        "status": STATUS,
        "proof_boundary": source["proof_boundary"],
    }
    payload["registry_digest"] = canonical_digest_v2(payload)
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
        payload = resolve_registry_v2(root=args.root, requested_head=args.head)
        encoded = canonical_json_bytes_v2(payload) + b"\n"
        if args.output is None:
            sys.stdout.buffer.write(encoded)
        else:
            args.output.write_bytes(encoded)
    except RegistryV2Error as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "ALLOWED_ROLES",
    "AUTHORITY_CLASS",
    "DIGEST_METHOD",
    "EXPECTED_ARTIFACT_IDENTITIES",
    "EXPECTED_DENIALS",
    "EXPECTED_GRANT_IDENTITIES",
    "EXPECTED_POLICY",
    "EXPECTED_PREFIX",
    "REGISTRY_PATH",
    "RESOLVER_PATH",
    "RegistryV2Error",
    "SCHEMA_PATH",
    "STATUS",
    "TOOLCHAIN_PATHS",
    "canonical_digest_v2",
    "canonical_json_bytes_v2",
    "resolve_registry_v2",
]
