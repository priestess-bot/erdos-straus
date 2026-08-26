#!/usr/bin/env python3
"""Resolve the minimal q1 root terminal-decision authority at an exact HEAD.

V3 grants four roles: root initializer, terminal scheduler, independent coverage
verifier, and terminal issuer.  The decision assembler and production receipt
verifier are pinned dependencies, never roles.  No E1, queue, producer, T5, or
branch capability is exposed.
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
from types import ModuleType
from typing import Any, Mapping, NoReturn, Sequence

import jsonschema


SCHEMA_ID = "t6_coordinator_role_registry_v3"
SCHEMA_VERSION = 3
RESOLVED_SCHEMA_ID = "t6_coordinator_role_registry_resolved_v3"
REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v3.json"
RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v3.py"
SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v3.schema.json"
TOOLCHAIN_PATHS = (REGISTRY_PATH, RESOLVER_PATH, SCHEMA_PATH)

STATUS = "HEAD_BOUND_Q1_ROOT_TERMINAL_DECISION_AUTHORITY_NO_RECURSION"
AUTHORITY_SOURCE = "TRACKED_GIT_OBJECTS_AT_EXACT_REQUESTED_HEAD"
ROLE_AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V3"
SEMANTIC_DIGEST_METHOD = (
    "PYTHON_STABLE_AST_SYMBOL_SET_BLOB_CLOSURE_DEPENDENCY_SHA256_V3"
)

V2_REGISTRY_ID = "t6_coordinator_role_registry_v2"
V2_REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v2.json"
V2_SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v2.schema.json"
V2_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v2.py"
V2_RESOLVER_SYMBOL = "resolve_registry_v2"
V2_STATUS = "HEAD_BOUND_PREFIX_SCHEDULE_AUTHORITY_NO_ISSUER"

SCHEDULE_ID = "q1_root_gap_3_7_11_registered_priority_prefix_v1"
ORDERED_GAPS = (3, 7, 11)
NEXT_UNCHECKED_GAP = 15
COVERAGE_SEMANTICS = "REGISTERED_PRIORITY_ONLY"

COVERAGE_ARTIFACT_ID = "q1_priority_prefix_coverage_verifier_v1"
COVERAGE_PATH = "scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py"
COVERAGE_SYMBOL = "verify_q_one_priority_prefix_coverage_v1"
SCHEDULER_ARTIFACT_ID = "q1_priority_prefix_scheduler_v1"
SCHEDULER_PATH = "scripts/t6_q_one_priority_prefix_scheduler_v1.py"
SCHEDULER_SYMBOL = "replay_q_one_priority_prefix_v1"
INITIALIZER_ARTIFACT_ID = "q1_root_initializer_envelope_v2"
INITIALIZER_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"
INITIALIZER_SYMBOLS = (
    "artifact_to_mapping_v2",
    "make_canonical_q_one_g_source_body_v2",
    "make_raw_root_source_state_v2",
    "make_root_initializer_anchor_v2",
)
ASSEMBLER_ARTIFACT_ID = "q1_terminal_decision_assembler_v2"
ASSEMBLER_PATH = "scripts/t6_q_one_terminal_decision_assembler_v2.py"
ASSEMBLER_SYMBOL = "assemble_q_one_terminal_decision_v2"
ISSUER_ARTIFACT_ID = "q1_terminal_issuer_v1"
ISSUER_PATH = "scripts/t6_q_one_terminal_issuer_v1.py"
ISSUER_SYMBOL = "issue_q_one_terminal_decision_v1"
RECEIPT_VERIFIER_ARTIFACT_ID = "q1_production_terminal_receipt_verifier_v1"
RECEIPT_VERIFIER_PATH = "scripts/t6_q_one_terminal_receipt_verifier_v1.py"
RECEIPT_VERIFIER_SYMBOL = "verify_q_one_production_terminal_receipt_v1"
V2_RESOLVER_ARTIFACT_ID = "v2_registry_resolver_dependency"

PRODUCTION_RECEIPT_SCHEMA_ID = "t6_q_one_production_terminal_receipts_v1"
PRODUCTION_RECEIPT_SCHEMA_VERSION = 1
PRODUCTION_RECEIPT_SCHEMA_PATH = (
    "schemas/t6-q-one-production-terminal-receipts-v1.schema.json"
)
ROOT_ACTUALNESS_TYPE = "QOneRootSourceActualnessReceiptV1"
HIT_RECEIPT_TYPE = "ProductionQOneRootTerminalReceiptV1"
MISS_RECEIPT_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
HIT_OUTCOME = "ROOT_TERMINAL_HIT"
MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"

ROLE_INITIALIZER = "ROOT_INITIALIZER"
ROLE_ISSUER = "TERMINAL_ISSUER"
ROLE_SCHEDULER = "TERMINAL_SCHEDULER"
ROLE_COVERAGE = "INDEPENDENT_COVERAGE_VERIFIER"
ALLOWED_ROLES = (
    ROLE_COVERAGE,
    ROLE_INITIALIZER,
    ROLE_ISSUER,
    ROLE_SCHEDULER,
)
INITIALIZER_GRANT_ID = "q1_root_initializer_grant_v3"
ISSUER_GRANT_ID = "q1_terminal_issuer_grant_v3"
SCHEDULER_GRANT_ID = "q1_prefix_terminal_scheduler_grant_v3"
COVERAGE_GRANT_ID = "q1_prefix_independent_coverage_verifier_grant_v3"

ARTIFACT_CLASS_ROLE = "ROLE_ARTIFACT"
ARTIFACT_CLASS_ASSEMBLER = "ISSUER_DEPENDENCY_ONLY"
ARTIFACT_CLASS_REPLAYER = "POST_ISSUANCE_REPLAY_DEPENDENCY_ONLY"
ARTIFACT_CLASS_CROSS = "CROSS_REGISTRY_DEPENDENCY_ONLY"

REGULAR_MODES = frozenset({"100644", "100755"})
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
FORBIDDEN_EXECUTABLE_ROOTS = frozenset(
    {".github", "claims", "concepts", "data", "docs", "index", "reproductions", "schemas", "tests"}
)

ARTIFACT_IDENTITIES = (
    (COVERAGE_ARTIFACT_ID, ARTIFACT_CLASS_ROLE, COVERAGE_PATH, (COVERAGE_SYMBOL,)),
    (INITIALIZER_ARTIFACT_ID, ARTIFACT_CLASS_ROLE, INITIALIZER_PATH, INITIALIZER_SYMBOLS),
    (RECEIPT_VERIFIER_ARTIFACT_ID, ARTIFACT_CLASS_REPLAYER, RECEIPT_VERIFIER_PATH, (RECEIPT_VERIFIER_SYMBOL,)),
    (SCHEDULER_ARTIFACT_ID, ARTIFACT_CLASS_ROLE, SCHEDULER_PATH, (SCHEDULER_SYMBOL,)),
    (ASSEMBLER_ARTIFACT_ID, ARTIFACT_CLASS_ASSEMBLER, ASSEMBLER_PATH, (ASSEMBLER_SYMBOL,)),
    (ISSUER_ARTIFACT_ID, ARTIFACT_CLASS_ROLE, ISSUER_PATH, (ISSUER_SYMBOL,)),
    (V2_RESOLVER_ARTIFACT_ID, ARTIFACT_CLASS_CROSS, V2_RESOLVER_PATH, (V2_RESOLVER_SYMBOL,)),
)
ARTIFACT_PIN_FIELDS = (
    "expected_blob_sha256",
    "expected_symbol_set_digest",
    "expected_local_import_closure_digest",
    "expected_dependency_manifest_digest",
    "expected_semantic_sha256",
)

DEPENDENCIES = {
    COVERAGE_ARTIFACT_ID: ((), (), ()),
    INITIALIZER_ARTIFACT_ID: ((), (), ()),
    SCHEDULER_ARTIFACT_ID: ((), (), ()),
    V2_RESOLVER_ARTIFACT_ID: ((), (), (V2_REGISTRY_PATH, V2_SCHEMA_PATH)),
    ASSEMBLER_ARTIFACT_ID: (
        tuple(sorted((V2_RESOLVER_ARTIFACT_ID, INITIALIZER_ARTIFACT_ID, SCHEDULER_ARTIFACT_ID, COVERAGE_ARTIFACT_ID))),
        (),
        (),
    ),
    ISSUER_ARTIFACT_ID: (
        tuple(sorted((V2_RESOLVER_ARTIFACT_ID, INITIALIZER_ARTIFACT_ID, ASSEMBLER_ARTIFACT_ID))),
        (),
        (REGISTRY_PATH, RESOLVER_PATH, SCHEMA_PATH, PRODUCTION_RECEIPT_SCHEMA_PATH),
    ),
    RECEIPT_VERIFIER_ARTIFACT_ID: (
        tuple(sorted((V2_RESOLVER_ARTIFACT_ID, INITIALIZER_ARTIFACT_ID, ASSEMBLER_ARTIFACT_ID))),
        (ISSUER_ARTIFACT_ID,),
        (RESOLVER_PATH, PRODUCTION_RECEIPT_SCHEMA_PATH),
    ),
}

CONTROLLED_LOADER_CONTRACTS = {
    ASSEMBLER_ARTIFACT_ID: {
        "loader_symbol": "_fresh_exec_module_v2",
        "loader_symbol_ast_sha256": "b9e4bc61aa74be0bd1d6ba90796dd74309c77651b718370a44589c04730dd126",
        "caller_symbol": "_load_fresh_modules_v2",
        "caller_symbol_ast_sha256": "5b97960436aa645e73cf71bf0e2d4ccca096d0d509b6ad52da4a5ce9ee3e0e73",
        "path_constants": {
            "ASSEMBLER_PATH": ASSEMBLER_PATH,
            "REGISTRY_RESOLVER_PATH": V2_RESOLVER_PATH,
            "ROOT_ENVELOPE_PATH": INITIALIZER_PATH,
            "SCHEDULER_PATH": SCHEDULER_PATH,
            "VERIFIER_PATH": COVERAGE_PATH,
        },
        "execution_path_constants": (
            "REGISTRY_RESOLVER_PATH",
            "ROOT_ENVELOPE_PATH",
            "SCHEDULER_PATH",
            "VERIFIER_PATH",
        ),
        "execution_toolchain_paths": (),
        "path_keyword": "path",
    },
    ISSUER_ARTIFACT_ID: {
        "loader_symbol": "_fresh_exec_module_v1",
        "loader_symbol_ast_sha256": "63621dbed97bd656a3932594a12a71a257fb658704c86be68ef317c31d80528a",
        "caller_symbol": "_load_fresh_modules_v1",
        "caller_symbol_ast_sha256": "2fc461bb939d6f4db0c507fcbace2081a006eac9a7198faa01db32a7c353cad5",
        "path_constants": {
            "ISSUER_PATH": ISSUER_PATH,
            "V2_RESOLVER_PATH": V2_RESOLVER_PATH,
            "V3_RESOLVER_PATH": RESOLVER_PATH,
            "ROOT_ENVELOPE_PATH": INITIALIZER_PATH,
            "ASSEMBLER_PATH": ASSEMBLER_PATH,
        },
        "execution_path_constants": (
            "V2_RESOLVER_PATH",
            "V3_RESOLVER_PATH",
            "ROOT_ENVELOPE_PATH",
            "ASSEMBLER_PATH",
        ),
        "execution_toolchain_paths": (RESOLVER_PATH,),
        "path_keyword": "path",
    },
    RECEIPT_VERIFIER_ARTIFACT_ID: {
        "loader_symbol": "_fresh",
        "loader_symbol_ast_sha256": "9bc86f6c2a4dda63b23c7ceeb5cd9ad257cb8cffba7f1b067b0753d192242249",
        "caller_symbol": RECEIPT_VERIFIER_SYMBOL,
        "caller_symbol_ast_sha256": "aa10878db3ab64fabd3dea6b3bd6de09098d017cd18e77a12c2ffcd6335b6152",
        "path_constants": {
            "VERIFIER_PATH": RECEIPT_VERIFIER_PATH,
            "ISSUER_PATH": ISSUER_PATH,
            "V2_RESOLVER_PATH": V2_RESOLVER_PATH,
            "V3_RESOLVER_PATH": RESOLVER_PATH,
            "ROOT_ENVELOPE_PATH": INITIALIZER_PATH,
            "ASSEMBLER_PATH": ASSEMBLER_PATH,
        },
        "execution_path_constants": (
            "V2_RESOLVER_PATH",
            "V3_RESOLVER_PATH",
            "ROOT_ENVELOPE_PATH",
            "ASSEMBLER_PATH",
        ),
        "execution_toolchain_paths": (RESOLVER_PATH,),
        "path_position": 2,
    },
}

ROLE_BINDINGS = (
    (COVERAGE_GRANT_ID, ROLE_COVERAGE, COVERAGE_ARTIFACT_ID, ("CERTIFICATE_VERIFIER", "DOMAIN_VERIFIER", "ROOT_TERMINAL_VERIFIER")),
    (
        INITIALIZER_GRANT_ID,
        ROLE_INITIALIZER,
        INITIALIZER_ARTIFACT_ID,
        (
            "BUILD_PARENTLESS_Q1_G_ROOT_ENVELOPE",
            "ESTABLISH_AUTHORIZED_ROOT_INITIALIZER_OCCURRENCE",
        ),
    ),
    (ISSUER_GRANT_ID, ROLE_ISSUER, ISSUER_ARTIFACT_ID, ("ISSUE_REGISTERED_PREFIX_MISS", "ISSUE_ROOT_TERMINAL_HIT")),
    (SCHEDULER_GRANT_ID, ROLE_SCHEDULER, SCHEDULER_ARTIFACT_ID, ("REGISTERED_PRIORITY_PREFIX_REPLAY",)),
)

AUTHORITY_DENIALS = {
    "e1_authority": False,
    "queue_authority": False,
    "producer_authority": False,
    "t5_authority": False,
    "branch_authority": False,
}
AUTHORITY_POLICY = {
    "source": AUTHORITY_SOURCE,
    "caller_override_authority": False,
    "worktree_authority": False,
    "fixed_owner_domain": "ordinary_parentless_q1_g_root_v1",
    "allowed_roles": list(ALLOWED_ROLES),
}
ROOT_INITIALIZER_POLICY = {
    "grant_id": INITIALIZER_GRANT_ID,
    "initializer_id": "q_one_root_initializer_envelope_v2",
    "owner_domain_id": "ordinary_parentless_q1_g_root_v1",
    "factory_sequence": [
        "make_canonical_q_one_g_source_body_v2",
        "make_root_initializer_anchor_v2",
        "make_raw_root_source_state_v2",
    ],
    "occurrence_kind": "ROOT_INITIALIZER_OUTPUT",
    "parent_kind": "PARENTLESS_ROOT",
    "actualness_receipt_type": ROOT_ACTUALNESS_TYPE,
    "actualness_scope": "ROOT_OCCURRENCE_ONLY",
    "caller_supplied_state_allowed": False,
    "initializer_output_self_authorizing": False,
    "actualness_attestor_role": ROLE_ISSUER,
}
TERMINAL_PREFIX_POLICY = {
    "schedule_id": SCHEDULE_ID,
    "scheduler_grant_id": SCHEDULER_GRANT_ID,
    "coverage_verifier_grant_id": COVERAGE_GRANT_ID,
    "ordered_gaps": list(ORDERED_GAPS),
    "next_unchecked_gap": NEXT_UNCHECKED_GAP,
    "coverage_semantics": COVERAGE_SEMANTICS,
    "global_exhaustion": False,
    "outcomes": [MISS_OUTCOME, HIT_OUTCOME],
}
RECEIPT_AUTHORITY_MATRIX = {
    "common": {
        "source_actualness": True,
        "root_initializer_authority": True,
        "issuer_authority": True,
        "issued_under_terminal_issuer": True,
        "common_owner_authority": False,
        "global_exhaustion": False,
        "persistent_admission": False,
        "e1_authority": False,
        "queue_authority": False,
        "producer_continuation_allowed": False,
    },
    HIT_OUTCOME: {
        "terminal_leaf_authority": True,
        "registered_prefix_miss_authority": False,
        "root_proof_close_authority": True,
    },
    MISS_OUTCOME: {
        "terminal_leaf_authority": False,
        "registered_prefix_miss_authority": True,
        "root_proof_close_authority": False,
    },
}
TERMINAL_ISSUANCE_POLICY = {
    "issuer_grant_id": ISSUER_GRANT_ID,
    "receipt_schema_id": PRODUCTION_RECEIPT_SCHEMA_ID,
    "receipt_schema_version": PRODUCTION_RECEIPT_SCHEMA_VERSION,
    "root_actualness_type": ROOT_ACTUALNESS_TYPE,
    "hit_receipt_type": HIT_RECEIPT_TYPE,
    "miss_receipt_type": MISS_RECEIPT_TYPE,
    "hit_outcome": HIT_OUTCOME,
    "miss_outcome": MISS_OUTCOME,
    "unqualified_miss_complete_forbidden": True,
    "producer_continuation_allowed": False,
    "authority_matrix": RECEIPT_AUTHORITY_MATRIX,
}
ISSUER_DEPENDENCY_POLICY = {
    "issuer_artifact_id": ISSUER_ARTIFACT_ID,
    "assembler_artifact_id": ASSEMBLER_ARTIFACT_ID,
    "assembler_class": ARTIFACT_CLASS_ASSEMBLER,
    "allowed_execution_artifact_ids": list(DEPENDENCIES[ISSUER_ARTIFACT_ID][0]),
    "forbidden_direct_artifact_ids": [
        COVERAGE_ARTIFACT_ID,
        SCHEDULER_ARTIFACT_ID,
        RECEIPT_VERIFIER_ARTIFACT_ID,
    ],
    "caller_inputs": ["raw_q_one_g", "repository_locator", "requested_head"],
    "caller_supplied_state_or_decision_allowed": False,
}
POST_ISSUANCE_REPLAY_POLICY = {
    "artifact_id": RECEIPT_VERIFIER_ARTIFACT_ID,
    "artifact_class": ARTIFACT_CLASS_REPLAYER,
    "verifier_symbol": RECEIPT_VERIFIER_SYMBOL,
    "issuer_import_allowed": False,
    "verifier_imports_issuer": False,
    "independent_wire_reconstruction": True,
}


class RegistryV3Error(ValueError):
    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: str, detail: str) -> NoReturn:
    raise RegistryV3Error(code, detail)


@dataclass(frozen=True, slots=True)
class GitBlobV3:
    mode: str
    object_type: str
    object_id: str
    path: str
    content: bytes


def _json_copy(value: Any, path: str = "$") -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject("NONCANONICAL_VALUE", f"{path} has a non-string key")
            result[key] = _json_copy(child, f"{path}.{key}")
        return result
    if type(value) is list:
        return [_json_copy(child, f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return value
    _reject("NONCANONICAL_VALUE", f"{path} has unsupported {type(value).__name__}")


def canonical_json_bytes_v3(value: Any) -> bytes:
    return json.dumps(
        _json_copy(value), ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("ascii")


def canonical_digest_v3(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes_v3(value)).hexdigest()


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _run_git(root: Path, args: Sequence[str]) -> bytes:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(["git", *args], cwd=root, check=False, capture_output=True, env=environment)
    if completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        _reject("GIT_ERROR", f"git {' '.join(args)} failed: {detail}")
    return completed.stdout


def _repository_root(locator: Path) -> Path:
    return Path(_run_git(locator.resolve(), ("rev-parse", "--show-toplevel")).decode().strip()).resolve()


def _exact_head(root: Path, requested_head: str) -> tuple[str, str, str]:
    object_format = _run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    length = 40 if object_format == "sha1" else 64 if object_format == "sha256" else 0
    if (
        type(requested_head) is not str
        or len(requested_head) != length
        or any(character not in "0123456789abcdef" for character in requested_head)
    ):
        _reject("INVALID_HEAD", "requested_head must be one exact full lowercase commit ID")
    if _run_git(root, ("cat-file", "-t", requested_head)).decode().strip() != "commit":
        _reject("INVALID_HEAD", "requested object is not a commit")
    resolved = _run_git(root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}"))
    if resolved.decode().strip() != requested_head:
        _reject("INVALID_HEAD", "commit resolution changed")
    tree = _run_git(root, ("rev-parse", f"{requested_head}^{{tree}}" )).decode().strip()
    return requested_head, tree, object_format


def _tree_entries(root: Path, head_sha: str) -> dict[str, tuple[str, str, str]]:
    raw = _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head_sha))
    result: dict[str, tuple[str, str, str]] = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, path_bytes = record.split(b"\t", 1)
        mode, object_type, object_id = metadata.decode("ascii").split(" ")
        path = path_bytes.decode("utf-8")
        if path in result:
            _reject("GIT_TREE_INVALID", path)
        result[path] = (mode, object_type, object_id)
    return result


def _safe_path(value: Any, executable: bool = False) -> str:
    if type(value) is not str or PATH_RE.fullmatch(value) is None:
        _reject("UNSAFE_PATH", repr(value))
    pure = PurePosixPath(value)
    if pure.is_absolute() or value != pure.as_posix() or any(part in {"", ".", ".."} for part in pure.parts):
        _reject("UNSAFE_PATH", value)
    if executable and (pure.parts[0] != "scripts" or pure.suffix != ".py"):
        _reject("FORBIDDEN_EXECUTABLE_ROOT", value)
    return value


def _blob(
    root: Path, entries: Mapping[str, tuple[str, str, str]], path: str, *, executable: bool = False
) -> GitBlobV3:
    path = _safe_path(path, executable)
    entry = entries.get(path)
    if entry is None:
        _reject("MISSING_ARTIFACT", path)
    mode, object_type, object_id = entry
    if mode not in REGULAR_MODES or object_type != "blob":
        _reject("INVALID_GIT_MODE", path)
    return GitBlobV3(mode, object_type, object_id, path, _run_git(root, ("cat-file", "blob", object_id)))


def _strict_json(value: bytes, source: str) -> dict[str, Any]:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, child in items:
            if key in result:
                _reject("DUPLICATE_JSON_KEY", f"{source}:{key}")
            result[key] = child
        return result

    def number(text: str) -> NoReturn:
        _reject("NONINTEGER_JSON", f"{source}:{text}")

    try:
        decoded = json.loads(value.decode("utf-8"), object_pairs_hook=pairs, parse_float=number, parse_constant=number)
    except RegistryV3Error:
        raise
    except Exception as exc:
        raise RegistryV3Error("INVALID_JSON", f"{source}: {exc}") from exc
    if type(decoded) is not dict:
        _reject("INVALID_JSON", f"{source} is not an object")
    _json_copy(decoded)
    return decoded


def _toolchain_binding(
    root: Path, entries: Mapping[str, tuple[str, str, str]], head_sha: str
) -> dict[str, Any]:
    files: list[dict[str, Any]] = []
    head_values: dict[str, bytes] = {}
    for path in TOOLCHAIN_PATHS:
        blob = _blob(root, entries, path, executable=path == RESOLVER_PATH)
        worktree = root / path
        if worktree.is_symlink() or not worktree.is_file() or worktree.read_bytes() != blob.content:
            _reject("TOOLCHAIN_WORKTREE_MISMATCH", path)
        head_values[path] = blob.content
        files.append(
            {"path": path, "git_mode": blob.mode, "git_object_id": blob.object_id, "sha256": _sha256(blob.content)}
        )
    executing = Path(__file__)
    if executing.is_symlink() or executing.resolve().read_bytes() != head_values[RESOLVER_PATH]:
        _reject("EXECUTING_RESOLVER_HEAD_MISMATCH", RESOLVER_PATH)
    payload: dict[str, Any] = {
        "schema_id": "t6_coordinator_role_registry_toolchain_binding_v3",
        "head_sha": head_sha,
        "status": "BOUND_SELF_SCHEMA_AND_REGISTRY_TO_REQUESTED_HEAD",
        "files": files,
    }
    payload["digest"] = canonical_digest_v3(payload)
    return payload


def _fresh_module(path: Path, content: bytes, private_name: str) -> ModuleType:
    module = ModuleType(private_name)
    module.__file__ = str(path.resolve())
    previous = sys.modules.get(private_name)
    sys.modules[private_name] = module
    try:
        exec(compile(content, str(path), "exec"), module.__dict__)
    finally:
        if previous is None:
            sys.modules.pop(private_name, None)
        else:
            sys.modules[private_name] = previous
    return module


def _load_v2_resolver(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    source: Mapping[str, Any],
    head_sha: str,
) -> tuple[ModuleType, GitBlobV3]:
    cross = source["v2_cross_registry_binding"]
    for path, key in (
        (V2_REGISTRY_PATH, "expected_v2_registry_source_sha256"),
        (V2_SCHEMA_PATH, "expected_v2_schema_sha256"),
        (V2_RESOLVER_PATH, "expected_v2_resolver_blob_sha256"),
    ):
        blob = _blob(root, entries, path, executable=path == V2_RESOLVER_PATH)
        if _sha256(blob.content) != cross[key]:
            _reject("V2_CROSS_PIN_MISMATCH", path)
    resolver_blob = _blob(root, entries, V2_RESOLVER_PATH, executable=True)
    module = _fresh_module(
        root / V2_RESOLVER_PATH,
        resolver_blob.content,
        f"_t6_registry_v2_for_v3_{head_sha}",
    )
    return module, resolver_blob


def _static_import_names(tree: ast.AST) -> tuple[str, ...]:
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return tuple(sorted(names))


def _module_aliases(path: str) -> tuple[str, ...]:
    pure = PurePosixPath(path)
    if len(pure.parts) < 2 or pure.suffix != ".py":
        return ()
    relative = PurePosixPath(*pure.parts[1:]).with_suffix("")
    return tuple(sorted({".".join(relative.parts), ".".join(pure.with_suffix("").parts)}))


def _static_local_closure(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    root_path: str,
) -> tuple[list[dict[str, Any]], str]:
    index: dict[str, set[str]] = {}
    for path in entries:
        for alias in _module_aliases(path):
            index.setdefault(alias, set()).add(path)
    pending = [root_path]
    closure: dict[str, dict[str, Any]] = {}
    while pending:
        path = pending.pop()
        if path in closure:
            continue
        blob = _blob(root, entries, path, executable=True)
        tree = ast.parse(blob.content.decode("utf-8"), filename=path)
        dependencies: set[str] = set()
        for imported in _static_import_names(tree):
            root_name = imported.split(".", 1)[0]
            if root_name in FORBIDDEN_EXECUTABLE_ROOTS:
                _reject("FORBIDDEN_IMPORT_ROOT", f"{path}:{imported}")
            parts = imported.split(".")
            for length in range(1, len(parts) + 1):
                alias = ".".join(parts[:length])
                candidates = tuple(sorted(index.get(alias, ())))
                if len(candidates) > 1:
                    _reject("AMBIGUOUS_LOCAL_IMPORT", f"{path}:{alias}")
                if candidates:
                    dependencies.add(candidates[0])
        for dependency in dependencies:
            if not dependency.startswith("scripts/"):
                _reject("FORBIDDEN_IMPORT_ROOT", dependency)
        closure[path] = {
            "path": path,
            "git_mode": blob.mode,
            "git_object_id": blob.object_id,
            "blob_sha256": _sha256(blob.content),
        }
        pending.extend(sorted(dependencies, reverse=True))
    files = [closure[path] for path in sorted(closure)]
    digest = canonical_digest_v3({"schema_id": "t6_local_import_closure_v3", "files": files})
    return files, digest


def _dependency_manifest(source: Mapping[str, Any]) -> tuple[dict[str, Any], str]:
    manifest = _json_copy(source["dependency_manifest"])
    digest = canonical_digest_v3(
        {"schema_id": "t6_artifact_dependency_manifest_v3", **manifest}
    )
    if digest != source["expected_dependency_manifest_digest"]:
        _reject("DEPENDENCY_MANIFEST_PIN_MISMATCH", source["artifact_id"])
    return manifest, digest


def _audit_controlled_loader(
    tree: ast.AST, path: str, *, allow_pinned_compile_exec: bool
) -> None:
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots = {alias.name.split(".", 1)[0] for alias in node.names}
            if roots & {"builtins", "importlib", "pkgutil", "runpy"}:
                _reject("DYNAMIC_LOADER_FORBIDDEN", f"{path}:{sorted(roots)}")
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".", 1)[0] in {
                "builtins",
                "importlib",
                "pkgutil",
                "runpy",
            }:
                _reject("DYNAMIC_LOADER_FORBIDDEN", f"{path}:{node.module}")
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and (
                node.func.id in {"__import__", "eval"}
                or (
                    not allow_pinned_compile_exec
                    and node.func.id in {"compile", "exec"}
                )
            )
        ):
            _reject("DYNAMIC_LOADER_FORBIDDEN", f"{path}:{node.func.id}")


def _audit_controlled_loader_contract(
    *,
    artifact_id: str,
    path: str,
    tree: ast.Module,
    content: bytes,
    blob_sha256: str,
    manifest: Mapping[str, Any],
    identity_map: Mapping[str, tuple[str, str, str, tuple[str, ...]]],
    v2: ModuleType,
) -> dict[str, Any]:
    contract = CONTROLLED_LOADER_CONTRACTS[artifact_id]
    loader_symbol = contract["loader_symbol"]
    caller_symbol = contract["caller_symbol"]
    observed_ast: dict[str, str] = {}
    for symbol, expected in (
        (loader_symbol, contract["loader_symbol_ast_sha256"]),
        (caller_symbol, contract["caller_symbol_ast_sha256"]),
    ):
        try:
            digest = v2._symbol_receipt(
                path, symbol, content, blob_sha256
            )["symbol_ast_sha256"]
        except Exception as exc:
            code = getattr(exc, "code", "CONTROLLED_LOADER_SYMBOL_INVALID")
            raise RegistryV3Error(code, f"{path}:{symbol}: {exc}") from exc
        if digest != expected:
            _reject("CONTROLLED_LOADER_AST_MISMATCH", f"{path}:{symbol}")
        observed_ast[symbol] = digest

    bindings = v2._module_scope_bindings(tree.body)
    for name, expected_path in contract["path_constants"].items():
        matches = [
            (node, kind)
            for bound_name, node, kind in bindings
            if bound_name == name
        ]
        if len(matches) != 1:
            _reject("CONTROLLED_PATH_BINDING_MISMATCH", f"{path}:{name}")
        node, kind = matches[0]
        if not (
            kind == "ASSIGN"
            and type(node) is ast.Assign
            and len(node.targets) == 1
            and type(node.targets[0]) is ast.Name
            and node.targets[0].id == name
            and type(node.value) is ast.Constant
            and type(node.value.value) is str
            and node.value.value == expected_path
        ):
            _reject("CONTROLLED_PATH_BINDING_MISMATCH", f"{path}:{name}")

    executable_literals = {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and type(node.value) is str
        and node.value.startswith("scripts/")
        and node.value.endswith(".py")
    }
    if executable_literals != set(contract["path_constants"].values()):
        _reject(
            "CONTROLLED_EXECUTABLE_LITERAL_MISMATCH",
            f"{path}:{sorted(executable_literals)}",
        )

    declared_execution_paths = {
        identity_map[dependency_id][2]
        for dependency_id in manifest["execution_artifact_ids"]
    }
    contracted_execution_paths = {
        contract["path_constants"][name]
        for name in contract["execution_path_constants"]
    }
    if contracted_execution_paths != declared_execution_paths | set(
        contract["execution_toolchain_paths"]
    ):
        _reject("CONTROLLED_EXECUTION_MANIFEST_MISMATCH", artifact_id)

    parent: dict[int, ast.AST] = {}
    owners: dict[int, str] = {}
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            parent[id(child)] = node
    for top_level in tree.body:
        if isinstance(top_level, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for child in ast.walk(top_level):
                owners[id(child)] = top_level.name

    helper_calls: list[ast.Call] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Global) and set(node.names) & set(
            contract["path_constants"]
        ):
            _reject("CONTROLLED_PATH_REBINDING", f"{path}:{node.names}")
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.value.id == "sys" and node.attr == "modules":
                if owners.get(id(node)) != loader_symbol:
                    _reject("CONTROLLED_LOADER_ESCAPE", f"{path}:sys.modules")
        if isinstance(node, ast.Name) and node.id in {
            "__builtins__",
            "__import__",
            "eval",
            "globals",
            "locals",
            "vars",
        }:
            _reject("CONTROLLED_LOADER_ESCAPE", f"{path}:{node.id}")
        if isinstance(node, ast.Name) and node.id in {"compile", "exec"}:
            if owners.get(id(node)) != loader_symbol:
                _reject("CONTROLLED_LOADER_ESCAPE", f"{path}:{node.id}")
        if isinstance(node, ast.Name) and node.id == loader_symbol:
            call = parent.get(id(node))
            if not (
                isinstance(call, ast.Call)
                and call.func is node
                and owners.get(id(call)) == caller_symbol
            ):
                _reject("CONTROLLED_LOADER_ESCAPE", f"{path}:{loader_symbol}")
            helper_calls.append(call)

    observed_path_names: list[str] = []
    for call in helper_calls:
        if "path_keyword" in contract:
            candidates = [
                keyword.value
                for keyword in call.keywords
                if keyword.arg == contract["path_keyword"]
            ]
            if len(candidates) != 1:
                _reject("CONTROLLED_LOADER_CALL_SHAPE", f"{path}:{loader_symbol}")
            path_argument = candidates[0]
        else:
            position = contract["path_position"]
            if len(call.args) <= position:
                _reject("CONTROLLED_LOADER_CALL_SHAPE", f"{path}:{loader_symbol}")
            path_argument = call.args[position]
        if type(path_argument) is not ast.Name:
            _reject("CONTROLLED_LOADER_CALL_SHAPE", f"{path}:{loader_symbol}")
        observed_path_names.append(path_argument.id)
    if sorted(observed_path_names) != sorted(contract["execution_path_constants"]):
        _reject(
            "CONTROLLED_LOADER_CALL_SET_MISMATCH",
            f"{path}:{sorted(observed_path_names)}",
        )
    return {
        "loader_symbol": loader_symbol,
        "loader_symbol_ast_sha256": observed_ast[loader_symbol],
        "caller_symbol": caller_symbol,
        "caller_symbol_ast_sha256": observed_ast[caller_symbol],
        "execution_artifact_ids": list(manifest["execution_artifact_ids"]),
        "execution_toolchain_paths": list(contract["execution_toolchain_paths"]),
        "status": "FIXED_LOADER_AND_CALL_TABLE_MATCH_DEPENDENCY_MANIFEST",
    }


def _resolve_artifacts(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    sources: Sequence[Mapping[str, Any]],
    v2: ModuleType,
) -> list[dict[str, Any]]:
    identity_map = {item[0]: item for item in ARTIFACT_IDENTITIES}
    if [item["artifact_id"] for item in sources] != sorted(identity_map):
        _reject("FIXED_ARTIFACT_MISMATCH", "artifact ID set/order changed")
    resolved: list[dict[str, Any]] = []
    for source in sources:
        artifact_id = source["artifact_id"]
        expected_id, expected_class, expected_path, expected_symbols = identity_map[artifact_id]
        if (
            artifact_id != expected_id
            or source["artifact_class"] != expected_class
            or source["path"] != expected_path
            or tuple(source["symbols"]) != expected_symbols
            or source["semantic_digest_method"] != SEMANTIC_DIGEST_METHOD
        ):
            _reject("FIXED_ARTIFACT_MISMATCH", artifact_id)
        cross_pin_keys = {
            "expected_v2_semantic_sha256",
            "expected_v3_semantic_sha256",
        }
        present_cross_pins = cross_pin_keys & set(source)
        if artifact_id in {SCHEDULER_ARTIFACT_ID, COVERAGE_ARTIFACT_ID}:
            if present_cross_pins != cross_pin_keys:
                _reject("V2_V3_ROLE_PIN_MISSING", artifact_id)
        elif present_cross_pins:
            _reject("UNEXPECTED_CROSS_ROLE_PIN", artifact_id)
        blob = _blob(root, entries, expected_path, executable=True)
        blob_sha = _sha256(blob.content)
        tree = ast.parse(blob.content.decode("utf-8"), filename=expected_path)
        if artifact_id in {
            ISSUER_ARTIFACT_ID,
            ASSEMBLER_ARTIFACT_ID,
            RECEIPT_VERIFIER_ARTIFACT_ID,
        }:
            _audit_controlled_loader(
                tree, expected_path, allow_pinned_compile_exec=True
            )
        elif artifact_id == INITIALIZER_ARTIFACT_ID:
            _audit_controlled_loader(
                tree, expected_path, allow_pinned_compile_exec=False
            )
        else:
            try:
                v2._import_targets(tree, expected_path)
            except Exception as exc:
                code = getattr(exc, "code", "V2_ARTIFACT_AUDIT_FAILED")
                raise RegistryV3Error(code, f"{expected_path}: {exc}") from exc
        symbol_receipts: dict[str, dict[str, str]] = {}
        for symbol in expected_symbols:
            try:
                receipt = v2._symbol_receipt(
                    expected_path, symbol, blob.content, blob_sha
                )
            except Exception as exc:
                code = getattr(exc, "code", "V2_SYMBOL_AUDIT_FAILED")
                raise RegistryV3Error(
                    code, f"{expected_path}:{symbol}: {exc}"
                ) from exc
            symbol_receipts[symbol] = {
                "symbol_ast_sha256": receipt["symbol_ast_sha256"]
            }
        symbol_set_digest = canonical_digest_v3(
            {"schema_id": "t6_python_symbol_set_v3", "symbols": symbol_receipts}
        )
        closure_files, closure_digest = _static_local_closure(root, entries, expected_path)
        manifest, dependency_digest = _dependency_manifest(source)
        controlled_loader_receipt = None
        if artifact_id in CONTROLLED_LOADER_CONTRACTS:
            controlled_loader_receipt = _audit_controlled_loader_contract(
                artifact_id=artifact_id,
                path=expected_path,
                tree=tree,
                content=blob.content,
                blob_sha256=blob_sha,
                manifest=manifest,
                identity_map=identity_map,
                v2=v2,
            )
        actual_local_imports = {
            item["path"] for item in closure_files if item["path"] != expected_path
        }
        allowed_local_imports = {
            identity_map[dependency_id][2]
            for dependency_id in manifest["execution_artifact_ids"]
        }
        if not actual_local_imports <= allowed_local_imports:
            _reject(
                "UNDECLARED_LOCAL_IMPORT",
                f"{artifact_id}:{sorted(actual_local_imports - allowed_local_imports)}",
            )
        literal_strings = {
            node.value
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and type(node.value) is str
        }
        dependency_ids = tuple(manifest["execution_artifact_ids"])
        for dependency_id in dependency_ids:
            dependency_identity = identity_map.get(dependency_id)
            if dependency_identity is None or dependency_identity[2] not in literal_strings:
                _reject("DEPENDENCY_LITERAL_MISSING", f"{artifact_id}:{dependency_id}")
        for dependency_id in manifest["binding_artifact_ids"]:
            dependency_identity = identity_map.get(dependency_id)
            if dependency_identity is None or dependency_identity[2] not in literal_strings:
                _reject("DEPENDENCY_LITERAL_MISSING", f"{artifact_id}:{dependency_id}")
        for document_path in manifest["binding_document_ids"]:
            if document_path not in literal_strings:
                _reject(
                    "DEPENDENCY_LITERAL_MISSING",
                    f"{artifact_id}:{document_path}",
                )
        semantic = canonical_digest_v3(
            {
                "method": SEMANTIC_DIGEST_METHOD,
                "path": expected_path,
                "blob_sha256": blob_sha,
                "symbol_set_digest": symbol_set_digest,
                "local_import_closure_digest": closure_digest,
                "dependency_manifest_digest": dependency_digest,
                "python_ast_contract_digest": v2.python_ast_contract_v2()["digest"],
            }
        )
        observed = {
            "expected_blob_sha256": blob_sha,
            "expected_symbol_set_digest": symbol_set_digest,
            "expected_local_import_closure_digest": closure_digest,
            "expected_dependency_manifest_digest": dependency_digest,
            "expected_semantic_sha256": semantic,
        }
        if source["expected_symbol_ast_sha256"] != {
            key: value["symbol_ast_sha256"] for key, value in symbol_receipts.items()
        }:
            _reject("ARTIFACT_PIN_MISMATCH", f"{artifact_id}:symbol AST map")
        for key in ARTIFACT_PIN_FIELDS:
            if source[key] != observed[key]:
                _reject("ARTIFACT_PIN_MISMATCH", f"{artifact_id}:{key}")
        if (
            artifact_id in {SCHEDULER_ARTIFACT_ID, COVERAGE_ARTIFACT_ID}
            and source["expected_v3_semantic_sha256"] != semantic
        ):
            _reject("V2_V3_ROLE_PIN_MISMATCH", f"{artifact_id}:v3 semantic")
        resolved.append(
            {
                **{key: _json_copy(value) for key, value in source.items()},
                "git_mode": blob.mode,
                "git_object_id": blob.object_id,
                "blob_sha256": blob_sha,
                "symbol_ast_sha256": symbol_receipts,
                "symbol_set_digest": symbol_set_digest,
                "local_import_closure_files": closure_files,
                "local_import_closure_digest": closure_digest,
                "dependency_manifest_digest": dependency_digest,
                "semantic_sha256": semantic,
                **(
                    {"controlled_loader_contract": controlled_loader_receipt}
                    if controlled_loader_receipt is not None
                    else {}
                ),
            }
        )
    return resolved


def _validate_dependency_dag(artifacts: Mapping[str, Mapping[str, Any]]) -> None:
    expected_ids = set(artifacts)
    for artifact_id, artifact in artifacts.items():
        execution, binding, documents = DEPENDENCIES[artifact_id]
        manifest = artifact["dependency_manifest"]
        if (
            tuple(manifest["execution_artifact_ids"]) != execution
            or tuple(manifest["binding_artifact_ids"]) != binding
            or tuple(manifest["binding_document_ids"]) != documents
        ):
            _reject("DEPENDENCY_POLICY_MISMATCH", artifact_id)
        if not set(execution) <= expected_ids:
            _reject("UNKNOWN_DEPENDENCY", artifact_id)
        pinned_dependencies = manifest["artifact_semantic_pins"]
        dependency_ids = set(execution) | set(binding)
        if set(pinned_dependencies) != dependency_ids:
            _reject("DEPENDENCY_SEMANTIC_PIN_SET_MISMATCH", artifact_id)
        if not dependency_ids <= expected_ids:
            _reject("UNKNOWN_DEPENDENCY", artifact_id)
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(artifact_id: str) -> None:
        if artifact_id in visiting:
            _reject("DEPENDENCY_CYCLE", artifact_id)
        if artifact_id in visited:
            return
        visiting.add(artifact_id)
        manifest = artifacts[artifact_id]["dependency_manifest"]
        for child in (
            list(manifest["execution_artifact_ids"])
            + list(manifest["binding_artifact_ids"])
        ):
            visit(child)
        visiting.remove(artifact_id)
        visited.add(artifact_id)

    for artifact_id in sorted(artifacts):
        visit(artifact_id)
    for artifact_id, artifact in artifacts.items():
        for dependency_id, expected_semantic in artifact["dependency_manifest"][
            "artifact_semantic_pins"
        ].items():
            if artifacts[dependency_id]["semantic_sha256"] != expected_semantic:
                _reject(
                    "DEPENDENCY_SEMANTIC_PIN_MISMATCH",
                    f"{artifact_id}:{dependency_id}",
                )


def _prevalidate_source_dependency_graph(
    sources: Sequence[Mapping[str, Any]],
) -> None:
    expected_ids = {item[0] for item in ARTIFACT_IDENTITIES}
    source_ids = [item.get("artifact_id") for item in sources]
    if set(source_ids) != expected_ids or len(source_ids) != len(set(source_ids)):
        _reject("FIXED_ARTIFACT_MISMATCH", "artifact set changed")
    manifests = {
        item["artifact_id"]: item["dependency_manifest"] for item in sources
    }
    for artifact_id, manifest in manifests.items():
        dependency_ids = set(manifest["execution_artifact_ids"]) | set(
            manifest["binding_artifact_ids"]
        )
        if set(manifest["artifact_semantic_pins"]) != dependency_ids:
            _reject("DEPENDENCY_SEMANTIC_PIN_SET_MISMATCH", artifact_id)
        if not dependency_ids <= expected_ids:
            _reject("UNKNOWN_DEPENDENCY", artifact_id)
    issuer_execution = set(manifests[ISSUER_ARTIFACT_ID]["execution_artifact_ids"])
    if issuer_execution & {
        SCHEDULER_ARTIFACT_ID,
        COVERAGE_ARTIFACT_ID,
        RECEIPT_VERIFIER_ARTIFACT_ID,
    }:
        _reject("ISSUER_DIRECT_ROLE_BYPASS", repr(sorted(issuer_execution)))
    if ISSUER_ARTIFACT_ID in set(
        manifests[RECEIPT_VERIFIER_ARTIFACT_ID]["execution_artifact_ids"]
    ):
        _reject("RECEIPT_VERIFIER_IMPORTS_ISSUER", ISSUER_ARTIFACT_ID)
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(artifact_id: str) -> None:
        if artifact_id in visiting:
            _reject("DEPENDENCY_CYCLE", artifact_id)
        if artifact_id in visited:
            return
        visiting.add(artifact_id)
        manifest = manifests[artifact_id]
        for child in (
            list(manifest["execution_artifact_ids"])
            + list(manifest["binding_artifact_ids"])
        ):
            if child not in manifests:
                _reject("UNKNOWN_DEPENDENCY", child)
            visit(child)
        visiting.remove(artifact_id)
        visited.add(artifact_id)

    for artifact_id in sorted(manifests):
        visit(artifact_id)
    for artifact_id, manifest in manifests.items():
        execution, binding, documents = DEPENDENCIES[artifact_id]
        if (
            tuple(manifest["execution_artifact_ids"]) != execution
            or tuple(manifest["binding_artifact_ids"]) != binding
            or tuple(manifest["binding_document_ids"]) != documents
        ):
            _reject("DEPENDENCY_POLICY_MISMATCH", artifact_id)


def _resolve_grants(
    sources: Sequence[Mapping[str, Any]], artifacts: Mapping[str, Mapping[str, Any]]
) -> list[dict[str, Any]]:
    binding_map = {item[0]: item for item in ROLE_BINDINGS}
    source_ids = [item["grant_id"] for item in sources]
    if set(source_ids) != set(binding_map) or len(source_ids) != len(set(source_ids)):
        _reject("FIXED_GRANT_MISMATCH", "grant ID set/order changed")
    result: list[dict[str, Any]] = []
    for source in sources:
        grant_id = source["grant_id"]
        expected_grant, role, artifact_id, capabilities = binding_map[grant_id]
        artifact = artifacts.get(artifact_id)
        if (
            grant_id != expected_grant
            or source["role"] != role
            or source["artifact_id"] != artifact_id
            or tuple(source["capabilities"]) != capabilities
            or source["authority_class"] != ROLE_AUTHORITY_CLASS
            or artifact is None
        ):
            _reject("FIXED_GRANT_MISMATCH", grant_id)
        if (
            source["expected_artifact_semantic_sha256"] != artifact["semantic_sha256"]
            or source["expected_dependency_manifest_digest"]
            != artifact["dependency_manifest_digest"]
        ):
            _reject("GRANT_PIN_MISMATCH", grant_id)
        result.append(
            {
                **_json_copy(source),
                "artifact_path": artifact["path"],
                "artifact_symbols": artifact["symbols"],
                "artifact_blob_sha256": artifact["blob_sha256"],
                "artifact_semantic_sha256": artifact["semantic_sha256"],
                "artifact_dependency_manifest_digest": artifact[
                    "dependency_manifest_digest"
                ],
            }
        )
    return sorted(result, key=lambda item: item["grant_id"])


def _resolve_v2_cross(
    root: Path,
    head_sha: str,
    source: Mapping[str, Any],
    v2: ModuleType,
    artifacts: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    try:
        resolved = v2.resolve_registry_v2(root=root, requested_head=head_sha)
    except Exception as exc:
        raise RegistryV3Error("V2_CROSS_RESOLUTION_FAILED", str(exc)) from exc
    cross = source["v2_cross_registry_binding"]
    if resolved.get("status") != V2_STATUS:
        _reject("V2_CROSS_STATUS_MISMATCH", repr(resolved.get("status")))
    if (
        resolved.get("active_role_grant_count") != 2
        or resolved.get("issuer_count") != 0
        or resolved.get("e1_authority") is not False
        or resolved.get("queue_authority") is not False
        or resolved.get("producer_authority") is not False
        or resolved.get("initializer_authority") is not False
        or resolved.get("t5_authority") is not False
        or resolved.get("authorized_branches") != []
    ):
        _reject("V2_CROSS_AUTHORITY_MISMATCH", "v2 evidence-role boundary changed")
    resolved_artifacts = {
        item["artifact_id"]: item for item in resolved["resolved_artifacts"]
    }
    cross_expected = {
        SCHEDULER_ARTIFACT_ID: cross["expected_v2_scheduler_semantic_sha256"],
        COVERAGE_ARTIFACT_ID: cross[
            "expected_v2_coverage_verifier_semantic_sha256"
        ],
    }
    for artifact_id in (SCHEDULER_ARTIFACT_ID, COVERAGE_ARTIFACT_ID):
        if (
            resolved_artifacts[artifact_id]["semantic_sha256"]
            != artifacts[artifact_id]["expected_v2_semantic_sha256"]
            or artifacts[artifact_id]["expected_v2_semantic_sha256"]
            != cross_expected[artifact_id]
            or artifacts[artifact_id]["semantic_sha256"]
            != artifacts[artifact_id]["expected_v3_semantic_sha256"]
        ):
            _reject("V2_V3_ROLE_PIN_MISMATCH", artifact_id)
    required_keys = tuple(cross["required_v2_role_subdigest_keys"])
    if set(required_keys) - set(resolved["role_subdigests"]):
        _reject("V2_CROSS_ROLE_DIGEST_MISSING", repr(required_keys))
    return {
        "v2_registry_id": V2_REGISTRY_ID,
        "v2_head_sha": resolved["head_sha"],
        "v2_registry_digest": resolved["registry_digest"],
        "v2_role_manifest_digest": resolved["role_authority_manifest"]["digest"],
        "v2_role_subdigests": {
            key: resolved["role_subdigests"][key] for key in required_keys
        },
        "v2_scheduler_semantic_sha256": resolved_artifacts[
            SCHEDULER_ARTIFACT_ID
        ]["semantic_sha256"],
        "v2_coverage_verifier_semantic_sha256": resolved_artifacts[
            COVERAGE_ARTIFACT_ID
        ]["semantic_sha256"],
    }


def resolve_registry_v3(*, root: Path, requested_head: str) -> dict[str, Any]:
    repository = _repository_root(root)
    head_sha, tree_sha, object_format = _exact_head(repository, requested_head)
    entries = _tree_entries(repository, head_sha)
    initial_toolchain = _toolchain_binding(repository, entries, head_sha)
    registry_blob = _blob(repository, entries, REGISTRY_PATH)
    schema_blob = _blob(repository, entries, SCHEMA_PATH)
    source = _strict_json(registry_blob.content, f"{head_sha}:{REGISTRY_PATH}")
    schema = _strict_json(schema_blob.content, f"{head_sha}:{SCHEMA_PATH}")
    jsonschema.Draft202012Validator.check_schema(schema)
    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(source))
    if errors:
        _reject("SOURCE_SCHEMA_INVALID", errors[0].message)
    if (
        source["schema_id"] != SCHEMA_ID
        or source["registry_id"] != SCHEMA_ID
        or source["schema_version"] != SCHEMA_VERSION
        or source["status"] != STATUS
        or source["authority_policy"] != AUTHORITY_POLICY
        or source["root_initializer_authority"] != ROOT_INITIALIZER_POLICY
        or source["terminal_prefix_authority"] != TERMINAL_PREFIX_POLICY
        or source["terminal_issuance_policy"] != TERMINAL_ISSUANCE_POLICY
        or source["issuer_dependency_policy"] != ISSUER_DEPENDENCY_POLICY
        or source["post_issuance_replay_policy"]
        != POST_ISSUANCE_REPLAY_POLICY
        or source["authority_denials"] != AUTHORITY_DENIALS
        or source["branch_bindings"] != []
    ):
        _reject("FIXED_REGISTRY_MISMATCH", "identity/status/denials changed")
    v2, _ = _load_v2_resolver(repository, entries, source, head_sha)
    _prevalidate_source_dependency_graph(source["artifacts"])
    artifacts_list = _resolve_artifacts(repository, entries, source["artifacts"], v2)
    artifacts = {item["artifact_id"]: item for item in artifacts_list}
    _validate_dependency_dag(artifacts)
    if len({item["path"] for item in artifacts_list}) != len(artifacts_list):
        _reject("ARTIFACT_PATH_COLLISION", "all executable artifacts need distinct paths")
    if len({item["blob_sha256"] for item in artifacts_list}) != len(artifacts_list):
        _reject("ARTIFACT_BLOB_COLLISION", "all executable artifacts need distinct blobs")
    role_artifacts = [artifacts[item[2]] for item in ROLE_BINDINGS]
    if len({item["path"] for item in role_artifacts}) != 4:
        _reject("ROLE_PATH_COLLISION", "four roles need distinct modules")
    if len({item["blob_sha256"] for item in role_artifacts}) != 4:
        _reject("ROLE_BLOB_COLLISION", "four roles need distinct blobs")
    if len({item["semantic_sha256"] for item in role_artifacts}) != 4:
        _reject("ROLE_SEMANTIC_COLLISION", "four roles need distinct semantics")
    if artifacts[ISSUER_ARTIFACT_ID]["path"] in {
        artifacts[INITIALIZER_ARTIFACT_ID]["path"],
        artifacts[ASSEMBLER_ARTIFACT_ID]["path"],
    }:
        _reject("ISSUER_SEPARATION_FAILED", "issuer shares initializer/assembler")
    issuer_execution = set(
        artifacts[ISSUER_ARTIFACT_ID]["dependency_manifest"][
            "execution_artifact_ids"
        ]
    )
    if issuer_execution & {SCHEDULER_ARTIFACT_ID, COVERAGE_ARTIFACT_ID, RECEIPT_VERIFIER_ARTIFACT_ID}:
        _reject("ISSUER_DIRECT_ROLE_BYPASS", repr(sorted(issuer_execution)))
    verifier_execution = set(
        artifacts[RECEIPT_VERIFIER_ARTIFACT_ID]["dependency_manifest"][
            "execution_artifact_ids"
        ]
    )
    if ISSUER_ARTIFACT_ID in verifier_execution:
        _reject("RECEIPT_VERIFIER_IMPORTS_ISSUER", ISSUER_ARTIFACT_ID)
    grants = _resolve_grants(source["role_grants"], artifacts)
    grants_by_role = {item["role"]: item for item in grants}
    if set(grants_by_role) != set(ALLOWED_ROLES):
        _reject("FIXED_GRANT_MISMATCH", "role set changed")
    v2_cross = _resolve_v2_cross(repository, head_sha, source, v2, artifacts)
    prefix = _json_copy(source["terminal_prefix_authority"])
    initializer = _json_copy(source["root_initializer_authority"])
    issuance = _json_copy(source["terminal_issuance_policy"])
    issuer_dependencies = _json_copy(source["issuer_dependency_policy"])
    replay = _json_copy(source["post_issuance_replay_policy"])
    documents: list[dict[str, Any]] = []
    for document in source["pinned_documents"]:
        blob = _blob(repository, entries, document["path"])
        digest = _sha256(blob.content)
        parsed = _strict_json(blob.content, document["path"])
        try:
            jsonschema.Draft202012Validator.check_schema(parsed)
        except jsonschema.exceptions.SchemaError as exc:
            raise RegistryV3Error(
                "PINNED_DOCUMENT_SCHEMA_INVALID",
                f"{document['document_id']}: {exc.message}",
            ) from exc
        canonical_digest = canonical_digest_v3(parsed)
        if (
            digest != document["expected_blob_sha256"]
            or canonical_digest != document["expected_canonical_sha256"]
            or parsed.get("$id") != document["expected_json_schema_id"]
        ):
            _reject("DOCUMENT_PIN_MISMATCH", document["document_id"])
        documents.append(
            {
                **_json_copy(document),
                "git_mode": blob.mode,
                "git_object_id": blob.object_id,
                "blob_sha256": digest,
                "canonical_sha256": canonical_digest,
            }
        )
    role_subdigests = {
        role: canonical_digest_v3(
            {
                "schema_id": "t6_role_subregistry_v3",
                "head_sha": head_sha,
                "role": role,
                "grant": grants_by_role[role],
            }
        )
        for role in ALLOWED_ROLES
    }
    manifest: dict[str, Any] = {
        "schema_id": "t6_q1_root_terminal_role_manifest_v3",
        "head_sha": head_sha,
        "status": STATUS,
        "grants": grants,
        "root_initializer_authority": initializer,
        "terminal_prefix_authority": prefix,
        "terminal_issuance_policy": issuance,
        "authority_denials": AUTHORITY_DENIALS,
    }
    manifest["digest"] = canonical_digest_v3(manifest)
    if _toolchain_binding(repository, entries, head_sha) != initial_toolchain:
        _reject("TOOLCHAIN_CHANGED_DURING_RESOLUTION", RESOLVER_PATH)
    payload: dict[str, Any] = {
        "schema_id": RESOLVED_SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "artifact_policy": "EPHEMERAL_EXACT_HEAD_AUTHORITY_MANIFEST_NOT_TRACKED",
        "head_sha": head_sha,
        "head_tree_sha": tree_sha,
        "git_object_format": object_format,
        "registry_path": REGISTRY_PATH,
        "registry_source_sha256": _sha256(registry_blob.content),
        "execution_binding": initial_toolchain,
        "resolved_artifacts": artifacts_list,
        "resolved_role_grants": grants,
        "authorized_terminal_prefixes": [prefix],
        "root_initializer_authority": initializer,
        "terminal_issuance_policy": issuance,
        "issuer_dependency_policy": issuer_dependencies,
        "post_issuance_replay_policy": replay,
        "pinned_documents": documents,
        "v2_cross_registry_binding": v2_cross,
        "authorized_branches": [],
        "role_authority_manifest": manifest,
        "role_subdigests": role_subdigests,
        "role_grant_counts": {role: 1 for role in ALLOWED_ROLES},
        "active_role_grant_count": 4,
        "root_initializer_count": 1,
        "terminal_issuer_count": 1,
        "terminal_scheduler_count": 1,
        "independent_coverage_verifier_count": 1,
        "assembler_role_count": 0,
        "receipt_verifier_role_count": 0,
        "authority_denials": AUTHORITY_DENIALS,
        "status": STATUS,
        "proof_boundary": source["proof_boundary"],
    }
    payload["registry_digest"] = canonical_digest_v3(payload)
    return payload


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--head", required=True)
    parser.add_argument("--output", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        payload = resolve_registry_v3(root=args.root, requested_head=args.head)
        encoded = canonical_json_bytes_v3(payload) + b"\n"
        if args.output is None:
            sys.stdout.buffer.write(encoded)
        else:
            args.output.write_bytes(encoded)
    except RegistryV3Error as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "ALLOWED_ROLES",
    "ARTIFACT_IDENTITIES",
    "AUTHORITY_DENIALS",
    "PRODUCTION_RECEIPT_SCHEMA_PATH",
    "REGISTRY_PATH",
    "RESOLVER_PATH",
    "RegistryV3Error",
    "SCHEMA_PATH",
    "STATUS",
    "TOOLCHAIN_PATHS",
    "canonical_digest_v3",
    "resolve_registry_v3",
]
