#!/usr/bin/env python3
"""Resolve exact-HEAD q1 root V1 base-admission authority.

V5 turns one terminal-first q1 prefix-MISS root into a V1
ROOT_INITIALIZER_OUTPUT base admission only. It never queues the state or
authorizes a successor, producer, E1-E5, T5, global miss, or continuation.
"""

from __future__ import annotations

import argparse
import ast
from contextlib import contextmanager
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


SCHEMA_ID = "t6_coordinator_role_registry_v5"
SCHEMA_VERSION = 5
RESOLVED_SCHEMA_ID = "t6_coordinator_role_registry_resolved_v5"
REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v5.json"
RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v5.py"
SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v5.schema.json"
TOOLCHAIN_PATHS = (REGISTRY_PATH, RESOLVER_PATH, SCHEMA_PATH)
STATUS = "HEAD_BOUND_Q1_ROOT_V1_BASE_ADMISSION_AUTHORITY_NO_QUEUE_OR_SUCCESSOR"
PENDING = "PENDING_ARTIFACT_PINS"
ACTIVE = "ACTIVE_EXACT_HEAD_AUTHORITY"
METHOD = "PYTHON_STABLE_AST_SYMBOL_SET_BLOB_CLOSURE_DEPENDENCY_SHA256_V5"
ZERO = "0" * 64
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")
SYMBOL_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")
REGULAR_MODES = frozenset({"100644", "100755"})

V3_REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v3.json"
V3_SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v3.schema.json"
V3_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v3.py"
V3_PROD_PATH = "scripts/t6_q_one_terminal_receipt_verifier_v1.py"
V3_PROD_SYMBOL = "verify_q_one_production_terminal_receipt_v1"
V3_ROOT_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"
V3_ROOT_SYMBOLS = (
    "artifact_to_mapping_v2",
    "make_canonical_q_one_g_source_body_v2",
    "make_raw_root_source_state_v2",
    "make_root_initializer_anchor_v2",
)
V2_REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v2.json"
V2_SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v2.schema.json"
V2_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v2.py"
V2_RESOLVER_SYMBOL = "resolve_registry_v2"
V4_REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v4.json"
V4_SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v4.schema.json"
V4_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v4.py"
V4_OWNER_PATH = "scripts/t6_q_one_root_owner_classifier_v2.py"
V4_OWNER_SYMBOLS = (
    "classify_q_one_root_owner_v2",
    "root_owner_receipt_to_mapping_v2",
)
V4_SCOPE_PATH = "scripts/t6_q_one_scope_aware_e1_validator_v2.py"
V4_SCOPE_SYMBOLS = (
    "scope_validation_receipt_to_mapping_v2",
    "validate_q_one_registered_prefix_e1_scope_v2",
)
V1_STATE_PATH = "scripts/t6_persistent_selector_state_v1.py"
V1_STATE_SYMBOLS = (
    "classify_selector_owner_v1",
    "extract_verified_selector_header_v1",
    "reject_before_persistent_queue_v1",
)
ADAPTER_ID = "q1_root_v1_terminal_adapter_v1"
ADAPTER_PATH = "scripts/t6_q_one_root_v1_terminal_adapter_v1.py"
ADAPTER_SYMBOLS = (
    "project_q_one_v3_miss_to_v1_terminal_first_v1",
    "terminal_projection_to_mapping_v1",
)
MATERIALIZER_ID = "q1_root_v1_base_materializer_v1"
MATERIALIZER_PATH = "scripts/t6_q_one_root_v1_base_materializer_v1.py"
MATERIALIZER_SYMBOLS = (
    "materialize_q_one_root_v1_base_state_v1",
    "base_materialization_receipt_to_mapping_v1",
)
ADMISSION_ID = "q1_root_v1_base_admission_verifier_v1"
ADMISSION_PATH = "scripts/t6_q_one_root_v1_base_admission_verifier_v1.py"
ADMISSION_SYMBOLS = (
    "verify_and_admit_q_one_root_v1_base_v1",
    "base_admission_receipt_to_mapping_v1",
)
ORCHESTRATOR_ID = "q1_root_v1_base_admission_orchestrator_v1"
ORCHESTRATOR_PATH = "scripts/t6_q_one_root_v1_base_admission_orchestrator_v1.py"
ORCHESTRATOR_SYMBOL = "assemble_q_one_root_v1_base_admission_v1"
REPLAYER_ID = "q1_root_v1_base_admission_receipt_verifier_v1"
REPLAYER_PATH = "scripts/t6_q_one_root_v1_base_admission_receipt_verifier_v1.py"
REPLAYER_SYMBOL = "verify_q_one_root_v1_base_admission_receipt_v1"
V3_PROD_ID = "v3_production_receipt_verifier_dependency"
V3_ROOT_ID = "v3_root_initializer_dependency"
V2_RESOLVER_ID = "v2_registry_resolver_dependency"
V4_RESOLVER_ID = "v4_registry_resolver_dependency"
V4_OWNER_ID = "v4_owner_classifier_dependency"
V4_SCOPE_ID = "v4_scope_validator_dependency"
V1_STATE_ID = "v1_persistent_state_contract_dependency"
RECEIPT_SCHEMA_PATH = "schemas/t6-q-one-root-v1-base-admission-v1.schema.json"

ROLE_MATERIALIZER = "Q1_ROOT_V1_BASE_MATERIALIZER"
ROLE_ADMISSION = "INDEPENDENT_Q1_ROOT_V1_BASE_ADMISSION_VERIFIER"
MATERIALIZER_GRANT = "q1_root_v1_base_materializer_grant_v1"
ADMISSION_GRANT = "q1_root_v1_base_admission_verifier_grant_v1"
ROLES = (ROLE_ADMISSION, ROLE_MATERIALIZER)

IDENTITIES = (
    (ADAPTER_ID, "CANONICAL_PROJECTION_ONLY", ADAPTER_PATH, ADAPTER_SYMBOLS),
    (ADMISSION_ID, "ROLE_ARTIFACT", ADMISSION_PATH, ADMISSION_SYMBOLS),
    (MATERIALIZER_ID, "ROLE_ARTIFACT", MATERIALIZER_PATH, MATERIALIZER_SYMBOLS),
    (
        ORCHESTRATOR_ID,
        "CONTROLLED_LOADER_ORCHESTRATOR_ONLY",
        ORCHESTRATOR_PATH,
        (ORCHESTRATOR_SYMBOL,),
    ),
    (
        REPLAYER_ID,
        "POST_ISSUANCE_REPLAY_DEPENDENCY_ONLY",
        REPLAYER_PATH,
        (REPLAYER_SYMBOL,),
    ),
    (V1_STATE_ID, "V1_CONTRACT_DEPENDENCY_ONLY", V1_STATE_PATH, V1_STATE_SYMBOLS),
    (
        V2_RESOLVER_ID,
        "CROSS_REGISTRY_DEPENDENCY_ONLY",
        V2_RESOLVER_PATH,
        (V2_RESOLVER_SYMBOL,),
    ),
    (V3_PROD_ID, "CROSS_REGISTRY_DEPENDENCY_ONLY", V3_PROD_PATH, (V3_PROD_SYMBOL,)),
    (V3_ROOT_ID, "CROSS_REGISTRY_DEPENDENCY_ONLY", V3_ROOT_PATH, V3_ROOT_SYMBOLS),
    (V4_OWNER_ID, "CROSS_REGISTRY_DEPENDENCY_ONLY", V4_OWNER_PATH, V4_OWNER_SYMBOLS),
    (
        V4_RESOLVER_ID,
        "CROSS_REGISTRY_DEPENDENCY_ONLY",
        V4_RESOLVER_PATH,
        ("resolve_registry_v4",),
    ),
    (V4_SCOPE_ID, "CROSS_REGISTRY_DEPENDENCY_ONLY", V4_SCOPE_PATH, V4_SCOPE_SYMBOLS),
)

DEPS = {
    ADAPTER_ID: ((), (), ()),
    MATERIALIZER_ID: (
        (ADAPTER_ID, V1_STATE_ID, V3_ROOT_ID),
        (V3_PROD_ID,),
        (RECEIPT_SCHEMA_PATH,),
    ),
    ADMISSION_ID: (
        (V1_STATE_ID, V3_ROOT_ID),
        (MATERIALIZER_ID, ADAPTER_ID, V3_PROD_ID, V4_OWNER_ID, V4_SCOPE_ID),
        (RECEIPT_SCHEMA_PATH,),
    ),
    ORCHESTRATOR_ID: (
        (
            ADMISSION_ID,
            MATERIALIZER_ID,
            ADAPTER_ID,
            V1_STATE_ID,
            V3_PROD_ID,
            V3_ROOT_ID,
            V4_OWNER_ID,
            V4_RESOLVER_ID,
            V4_SCOPE_ID,
        ),
        (),
        (REGISTRY_PATH, SCHEMA_PATH, RECEIPT_SCHEMA_PATH, RESOLVER_PATH),
    ),
    REPLAYER_ID: (
        (
            ADMISSION_ID,
            MATERIALIZER_ID,
            ADAPTER_ID,
            V1_STATE_ID,
            V3_PROD_ID,
            V3_ROOT_ID,
            V4_OWNER_ID,
            V4_RESOLVER_ID,
            V4_SCOPE_ID,
        ),
        (ORCHESTRATOR_ID,),
        (RECEIPT_SCHEMA_PATH, RESOLVER_PATH),
    ),
    V1_STATE_ID: ((), (), ()),
    V2_RESOLVER_ID: ((), (), (V2_REGISTRY_PATH, V2_SCHEMA_PATH)),
    V3_PROD_ID: ((), (), (V3_REGISTRY_PATH, V3_SCHEMA_PATH, V3_RESOLVER_PATH)),
    V3_ROOT_ID: ((), (), (V3_REGISTRY_PATH, V3_SCHEMA_PATH)),
    V4_RESOLVER_ID: ((V2_RESOLVER_ID,), (), (V4_REGISTRY_PATH, V4_SCHEMA_PATH)),
    V4_OWNER_ID: ((), (), (V4_REGISTRY_PATH, V4_SCHEMA_PATH)),
    V4_SCOPE_ID: ((), (), (V4_REGISTRY_PATH, V4_SCHEMA_PATH)),
}

ROLE_BINDINGS = {
    ADMISSION_GRANT: (
        ROLE_ADMISSION,
        ADMISSION_ID,
        ("ISSUE_Q1_G_V1_BASE_ADMISSION_NO_QUEUE",),
    ),
    MATERIALIZER_GRANT: (
        ROLE_MATERIALIZER,
        MATERIALIZER_ID,
        ("MATERIALIZE_Q1_G_V1_ROOT_INITIALIZER_OUTPUT",),
    ),
}

AUTHORITY_POLICY = {
    "source": "TRACKED_GIT_OBJECTS_AT_EXACT_REQUESTED_HEAD",
    "caller_override_authority": False,
    "worktree_authority": False,
    "fixed_owner_domain": "ordinary_parentless_q1_g_root_v1",
    "inherited_v3_registry_id": "t6_coordinator_role_registry_v3",
    "inherited_v4_registry_id": "t6_coordinator_role_registry_v4",
    "new_roles": [ROLE_ADMISSION, ROLE_MATERIALIZER],
    "base_semantic_excludes_v4_e1_and_candidate": True,
}

BASE_ADMISSION_POLICY = {
    "source_owner": "type_ii_relation_g_endpoint",
    "v1_queue_gate": "ROOT_INITIALIZER_OUTPUT",
    "v3_terminal_type": "ProductionQOneRegisteredPrefixMissReceiptV1",
    "v3_terminal_outcome": "MISS_REGISTERED_PRIORITY_COMPLETE",
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

ORCHESTRATION_POLICY = {
    "artifact_id": ORCHESTRATOR_ID,
    "artifact_class": "CONTROLLED_LOADER_ORCHESTRATOR_ONLY",
    "public_symbol": ORCHESTRATOR_SYMBOL,
    "caller_inputs": [
        "production_miss_receipt",
        "raw_q_one_g",
        "repository_locator",
        "requested_head",
    ],
    "caller_supplied_grant_allowed": False,
    "caller_supplied_v4_receipt_allowed": False,
    "execution_toolchain_paths": [RESOLVER_PATH],
}

POST_ISSUANCE_REPLAY_POLICY = {
    "artifact_id": REPLAYER_ID,
    "artifact_class": "POST_ISSUANCE_REPLAY_DEPENDENCY_ONLY",
    "public_symbol": REPLAYER_SYMBOL,
    "orchestrator_import_allowed": False,
    "independent_wire_reconstruction": True,
}

V3_CROSS_REGISTRY_BINDING = {
    "registry_path": V3_REGISTRY_PATH,
    "schema_path": V3_SCHEMA_PATH,
    "resolver_path": V3_RESOLVER_PATH,
    "required_status": "HEAD_BOUND_Q1_ROOT_TERMINAL_DECISION_AUTHORITY_NO_RECURSION",
    "same_head_required": True,
}

V4_CROSS_REGISTRY_BINDING_BASE = {
    "registry_path": V4_REGISTRY_PATH,
    "schema_path": V4_SCHEMA_PATH,
    "resolver_path": V4_RESOLVER_PATH,
    "required_status": "HEAD_BOUND_Q1_ROOT_PREFIX_SCOPED_E1_AUTHORITY_NO_SUCCESSOR_OR_RECURSION",
    "same_head_required": True,
    "v4_e1_consumer_receipt_accepted_as_base_input": False,
}

AUTHORITY_DENIALS = {
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

# Both non-role modules use a deliberately narrow exact-blob loader.  These
# contracts bind their public caller, both compile/exec helpers, and every
# executable path constant to the fixed dependency graph.  They deliberately
# do not claim to recognize arbitrary malicious code after an explicit repin:
# a changed source policy is a new authority decision requiring fresh review.
CONTROLLED_LOADER_CONTRACTS = {
    ORCHESTRATOR_ID: {
        "caller_symbol": ORCHESTRATOR_SYMBOL,
        "caller_symbol_ast_sha256": "cc1334e83ad3f010bcc7749ea264023cdef7397da480d019439c29731db7b326",
        "loader_symbols": {
            "_fresh_module": "4a00516e1b2090f66ac01f95511c1a7c958d3c3ae00832b5c688adf93ae94739",
            "_fresh_v1_bundle": "978b7120575f683273804daf996b7fff6e7eed789b9fcec476373aa3038885fd",
        },
        "path_constants": {
            "ORCHESTRATOR_PATH": ORCHESTRATOR_PATH,
            "V5_RESOLVER_PATH": RESOLVER_PATH,
            "V4_RESOLVER_PATH": V4_RESOLVER_PATH,
            "V3_VERIFIER_PATH": V3_PROD_PATH,
            "ROOT_INITIALIZER_PATH": V3_ROOT_PATH,
            "V1_STATE_PATH": V1_STATE_PATH,
            "ADAPTER_PATH": ADAPTER_PATH,
            "MATERIALIZER_PATH": MATERIALIZER_PATH,
            "ADMISSION_PATH": ADMISSION_PATH,
            "OWNER_PATH": V4_OWNER_PATH,
            "SCOPE_PATH": V4_SCOPE_PATH,
        },
        "fresh_path_constants": {
            "V5_RESOLVER_PATH": None,
            "V4_RESOLVER_PATH": V4_RESOLVER_ID,
            "V3_VERIFIER_PATH": V3_PROD_ID,
            "OWNER_PATH": V4_OWNER_ID,
            "SCOPE_PATH": V4_SCOPE_ID,
        },
        "bundle_path_constants": {
            "V1_STATE_PATH": V1_STATE_ID,
            "ROOT_INITIALIZER_PATH": V3_ROOT_ID,
            "ADAPTER_PATH": ADAPTER_ID,
            "MATERIALIZER_PATH": MATERIALIZER_ID,
            "ADMISSION_PATH": ADMISSION_ID,
        },
    },
    REPLAYER_ID: {
        "caller_symbol": REPLAYER_SYMBOL,
        "caller_symbol_ast_sha256": "c210e05a173ef8829e676f3d167de444f7ae00c2b6ab284e335b64ee034139fa",
        "loader_symbols": {
            "_fresh": "a5862f8e27982b8e9d3506f043c503dda9e7dfd05c073b7d2c749ce850e7a562",
            "_fresh_v1_bundle": "807fd78aa7593835f17e3a214f93460b9cb9b6ecd8f3ae323257596f74abeaa4",
        },
        "path_constants": {
            "VERIFIER_PATH": REPLAYER_PATH,
            "ORCHESTRATOR_PATH": ORCHESTRATOR_PATH,
            "V5_RESOLVER_PATH": RESOLVER_PATH,
            "V4_RESOLVER_PATH": V4_RESOLVER_PATH,
            "V3_VERIFIER_PATH": V3_PROD_PATH,
            "ROOT_INITIALIZER_PATH": V3_ROOT_PATH,
            "V1_STATE_PATH": V1_STATE_PATH,
            "ADAPTER_PATH": ADAPTER_PATH,
            "MATERIALIZER_PATH": MATERIALIZER_PATH,
            "ADMISSION_PATH": ADMISSION_PATH,
            "OWNER_PATH": V4_OWNER_PATH,
            "SCOPE_PATH": V4_SCOPE_PATH,
        },
        "fresh_path_constants": {
            "V5_RESOLVER_PATH": None,
            "V4_RESOLVER_PATH": V4_RESOLVER_ID,
            "V3_VERIFIER_PATH": V3_PROD_ID,
            "OWNER_PATH": V4_OWNER_ID,
            "SCOPE_PATH": V4_SCOPE_ID,
        },
        "bundle_path_constants": {
            "V1_STATE_PATH": V1_STATE_ID,
            "ROOT_INITIALIZER_PATH": V3_ROOT_ID,
            "ADAPTER_PATH": ADAPTER_ID,
            "MATERIALIZER_PATH": MATERIALIZER_ID,
            "ADMISSION_PATH": ADMISSION_ID,
        },
        "binding_path_constants": {"ORCHESTRATOR_PATH": ORCHESTRATOR_ID},
    },
}


class RegistryV5Error(ValueError):
    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code


def fail(code: str, detail: str) -> NoReturn:
    raise RegistryV5Error(code, detail)


def copy_json(value: Any) -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                fail("NONCANONICAL_VALUE", "non-string mapping key")
            result[key] = copy_json(child)
        return result
    if type(value) is list:
        return [copy_json(child) for child in value]
    if value is None or type(value) in {str, bool, int}:
        return value
    fail("NONCANONICAL_VALUE", type(value).__name__)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        copy_json(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("ascii")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def run_git(root: Path, args: Sequence[str]) -> bytes:
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env["GIT_NO_REPLACE_OBJECTS"] = "1"
    result = subprocess.run(
        ["git", *args], cwd=root, capture_output=True, env=env, check=False
    )
    if result.returncode:
        fail("GIT_ERROR", result.stderr.decode("utf-8", errors="replace"))
    return result.stdout


@contextmanager
def sanitized_git_environment() -> Any:
    """Prevent recursively fresh-loaded V3/V4 code from inheriting Git routing."""

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


def repository(locator: Path) -> Path:
    if type(locator) is not type(Path()):
        fail("INVALID_ROOT", "exact platform Path required")
    return Path(
        run_git(locator.resolve(), ("rev-parse", "--show-toplevel")).decode().strip()
    ).resolve()


def exact_head(root: Path, requested_head: str) -> tuple[str, str]:
    object_format = run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    length = 40 if object_format == "sha1" else 64 if object_format == "sha256" else 0
    if (
        type(requested_head) is not str
        or len(requested_head) != length
        or any(character not in "0123456789abcdef" for character in requested_head)
    ):
        fail("INVALID_HEAD", "full lowercase commit ID required")
    if run_git(root, ("cat-file", "-t", requested_head)).decode().strip() != "commit":
        fail("INVALID_HEAD", "not a commit")
    if (
        run_git(root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}"))
        .decode()
        .strip()
        != requested_head
    ):
        fail("INVALID_HEAD", "resolution drift")
    return requested_head, run_git(
        root, ("rev-parse", f"{requested_head}^{{tree}}")
    ).decode().strip()


def tree_entries(root: Path, head: str) -> dict[str, tuple[str, str, str]]:
    result: dict[str, tuple[str, str, str]] = {}
    for record in run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head)).split(
        b"\0"
    ):
        if record:
            try:
                meta, raw_path = record.split(b"\t", 1)
                mode, kind, oid = meta.decode("ascii").split(" ")
                path = raw_path.decode("utf-8")
            except (UnicodeDecodeError, ValueError) as exc:
                raise RegistryV5Error("GIT_TREE_INVALID", repr(record)) from exc
            pure = PurePosixPath(path)
            if (
                not path
                or pure.is_absolute()
                or path != pure.as_posix()
                or "\\" in path
                or any(part in {"", ".", ".."} for part in pure.parts)
            ):
                fail("GIT_TREE_INVALID", repr(path))
            if path in result:
                fail("GIT_TREE_INVALID", f"duplicate {path}")
            result[path] = (mode, kind, oid)
    return result


def blob(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str) -> bytes:
    pure = PurePosixPath(path) if type(path) is str else PurePosixPath(".")
    if (
        type(path) is not str
        or PATH_RE.fullmatch(path) is None
        or pure.is_absolute()
        or path != pure.as_posix()
        or "\\" in path
        or any(part in {"", ".", ".."} for part in pure.parts)
        or path not in entries
    ):
        fail("MISSING_ARTIFACT", str(path))
    mode, kind, oid = entries[path]
    if mode not in REGULAR_MODES or kind != "blob":
        fail("INVALID_GIT_MODE", path)
    value = run_git(root, ("cat-file", "blob", oid))
    worktree = root / path
    if (
        worktree.is_symlink()
        or not worktree.is_file()
        or worktree.read_bytes() != value
    ):
        fail("WORKTREE_BINDING_MISMATCH", path)
    return value


def strict_json(raw: bytes, name: str) -> dict[str, Any]:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, value in items:
            if key in out:
                fail("DUPLICATE_JSON_KEY", name)
            out[key] = value
        return out

    try:
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=pairs,
            parse_float=lambda _v: fail("NONINTEGER_JSON", name),
        )
    except RegistryV5Error:
        raise
    except Exception as exc:
        raise RegistryV5Error("INVALID_JSON", str(exc)) from exc
    if type(value) is not dict:
        fail("INVALID_JSON", name)
    return copy_json(value)


def toolchain(
    root: Path, entries: Mapping[str, tuple[str, str, str]], head: str
) -> dict[str, Any]:
    files = []
    for path in TOOLCHAIN_PATHS:
        value = blob(root, entries, path)
        local = root / path
        if local.read_bytes() != value:
            fail("TOOLCHAIN_WORKTREE_MISMATCH", path)
        files.append(
            {
                "path": path,
                "sha256": hashlib.sha256(value).hexdigest(),
                "git_object_id": entries[path][2],
            }
        )
    if Path(__file__).resolve().read_bytes() != blob(root, entries, RESOLVER_PATH):
        fail("EXECUTING_RESOLVER_HEAD_MISMATCH", RESOLVER_PATH)
    data = {"schema_id": "t6_registry_v5_toolchain", "head_sha": head, "files": files}
    data["digest"] = digest(data)
    return data


def fresh(path: Path, content: bytes, name: str) -> ModuleType:
    module = ModuleType(name)
    module.__file__ = str(path.resolve())
    old = sys.modules.get(name)
    sys.modules[name] = module
    try:
        exec(compile(content, str(path), "exec"), module.__dict__)
    finally:
        if old is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = old
    return module


def stable_ast_value(value: Any) -> Any:
    """The V4-normalized AST form, implemented before any V4/V2 execution."""

    if isinstance(value, ast.AST):
        result: dict[str, Any] = {"_type": type(value).__name__}
        for name, child in ast.iter_fields(value):
            if name == "type_params" and child == []:
                continue
            result[name] = stable_ast_value(child)
        return result
    if type(value) is list:
        return [stable_ast_value(child) for child in value]
    if value is Ellipsis:
        return {"_literal": "ELLIPSIS"}
    if value is None or type(value) in {str, bool, int}:
        return value
    fail("PYTHON_AST_UNSUPPORTED", type(value).__name__)


def python_ast_contract_digest() -> str:
    return digest(
        {
            "schema_id": "t6_python_ast_normalization_v4",
            "stable_ast_fields": "ast.iter_fields",
            "omit_empty_type_params": True,
            "ellipsis_encoding": {"_literal": "ELLIPSIS"},
            "supported_scalar_types": ["None", "str", "bool", "int"],
        }
    )


def target_names(target: ast.AST) -> tuple[str, ...]:
    if isinstance(target, ast.Name):
        return (target.id,)
    if isinstance(target, ast.Starred):
        return target_names(target.value)
    if isinstance(target, (ast.Tuple, ast.List)):
        return tuple(name for child in target.elts for name in target_names(child))
    return ()


class NamedExpressionVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.bindings: list[tuple[str, ast.AST, str]] = []

    def visit_Lambda(self, node: ast.Lambda) -> None:
        del node

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.bindings.extend(
            (name, node, "NAMED_EXPR") for name in target_names(node.target)
        )
        self.visit(node.value)


def expression_bindings(value: ast.AST | None) -> list[tuple[str, ast.AST, str]]:
    if value is None:
        return []
    visitor = NamedExpressionVisitor()
    visitor.visit(value)
    return visitor.bindings


def pattern_names(pattern: ast.pattern) -> tuple[str, ...]:
    names: list[str] = []
    for node in ast.walk(pattern):
        if isinstance(node, ast.MatchAs) and node.name is not None:
            names.append(node.name)
        elif isinstance(node, ast.MatchStar) and node.name is not None:
            names.append(node.name)
        elif isinstance(node, ast.MatchMapping) and node.rest is not None:
            names.append(node.rest)
    return tuple(names)


def module_scope_bindings(
    statements: Sequence[ast.stmt], *, direct: bool = True
) -> list[tuple[str, ast.AST, str]]:
    """Fail-closed copy of the V2/V4 module binding audit."""

    result: list[tuple[str, ast.AST, str]] = []

    def bind_targets(target: ast.AST, node: ast.AST, kind: str) -> None:
        result.extend((name, node, kind) for name in target_names(target))

    def scan_expressions(*values: ast.AST | None) -> None:
        for value in values:
            result.extend(expression_bindings(value))

    for node in statements:
        if isinstance(node, ast.FunctionDef):
            result.append(
                (node.name, node, "DIRECT_FUNCTION" if direct else "CONDITIONAL_FUNCTION")
            )
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
                result.append(
                    (alias.asname or alias.name, node, "IMPORT_FROM")
                    if alias.name != "*"
                    else ("*", node, "STAR_IMPORT")
                )
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
            result.extend(module_scope_bindings(node.body, direct=False))
            result.extend(module_scope_bindings(node.orelse, direct=False))
        elif isinstance(node, (ast.With, ast.AsyncWith)):
            for item in node.items:
                scan_expressions(item.context_expr)
                if item.optional_vars is not None:
                    bind_targets(item.optional_vars, node, "WITH_TARGET")
            result.extend(module_scope_bindings(node.body, direct=False))
        elif isinstance(node, ast.If):
            scan_expressions(node.test)
            result.extend(module_scope_bindings(node.body, direct=False))
            result.extend(module_scope_bindings(node.orelse, direct=False))
        elif isinstance(node, ast.While):
            scan_expressions(node.test)
            result.extend(module_scope_bindings(node.body, direct=False))
            result.extend(module_scope_bindings(node.orelse, direct=False))
        elif isinstance(node, (ast.Try, ast.TryStar)):
            result.extend(module_scope_bindings(node.body, direct=False))
            result.extend(module_scope_bindings(node.orelse, direct=False))
            result.extend(module_scope_bindings(node.finalbody, direct=False))
            for handler in node.handlers:
                scan_expressions(handler.type)
                if handler.name is not None:
                    result.append((handler.name, handler, "EXCEPT_TARGET"))
                result.extend(module_scope_bindings(handler.body, direct=False))
        elif isinstance(node, ast.Match):
            scan_expressions(node.subject)
            for case in node.cases:
                result.extend(
                    (name, case.pattern, "MATCH_TARGET")
                    for name in pattern_names(case.pattern)
                )
                scan_expressions(case.guard)
                result.extend(module_scope_bindings(case.body, direct=False))
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


def symbol_receipt(path: str, symbol: str, content: bytes, blob_sha: str) -> str:
    if type(symbol) is not str or SYMBOL_RE.fullmatch(symbol) is None:
        fail("SYMBOL_INVALID", f"{path}:{symbol!r}")
    tree = parse_module(path, content)
    bindings = module_scope_bindings(tree.body)
    if any(name == "*" for name, _node, _kind in bindings):
        fail("STAR_IMPORT_FORBIDDEN", path)
    matches = [(node, kind) for name, node, kind in bindings if name == symbol]
    if len(matches) != 1:
        fail("SYMBOL_AMBIGUITY", f"{path}:{symbol}")
    node, kind = matches[0]
    if type(node) is not ast.FunctionDef or kind != "DIRECT_FUNCTION":
        fail("SYMBOL_NOT_FUNCTION", f"{path}:{symbol}")
    if node.decorator_list:
        fail("AUTHORIZED_SYMBOL_DECORATED", f"{path}:{symbol}")
    del blob_sha
    return digest(stable_ast_value(node))


def load_v4(root: Path, entries: Mapping[str, tuple[str, str, str]], head: str) -> ModuleType:
    """Called only after raw V4 and V2 artifacts have passed V5 pins."""

    return fresh(
        root / V4_RESOLVER_PATH,
        blob(root, entries, V4_RESOLVER_PATH),
        f"_v4_for_v5_{head}",
    )


def closure(
    root: Path, entries: Mapping[str, tuple[str, str, str]], path: str
) -> tuple[list[dict[str, Any]], str]:
    index: dict[str, str] = {}
    for item in entries:
        pure = PurePosixPath(item)
        if pure.parts and pure.parts[0] == "scripts" and pure.suffix == ".py":
            index[pure.stem] = item
    pending = [path]
    files: dict[str, dict[str, Any]] = {}
    while pending:
        current = pending.pop()
        if current in files:
            continue
        content = blob(root, entries, current)
        tree = ast.parse(content.decode(), filename=current)
        deps: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module]
            else:
                continue
            for name in names:
                first = name.split(".", 1)[0]
                if first in index:
                    deps.add(index[first])
        files[current] = {
            "path": current,
            "blob_sha256": hashlib.sha256(content).hexdigest(),
            "git_object_id": entries[current][2],
            "git_mode": entries[current][0],
        }
        pending.extend(sorted(deps, reverse=True))
    ordered = [files[item] for item in sorted(files)]
    return ordered, digest(
        {"schema_id": "t6_local_import_closure_v5", "files": ordered}
    )


def manifest_digest(value: Mapping[str, Any]) -> str:
    return digest(
        {"schema_id": "t6_artifact_dependency_manifest_v5", **copy_json(value)}
    )


def prevalidate_dependency_graph(sources: Sequence[Mapping[str, Any]]) -> None:
    """Reject any source graph outside the fixed V5 authority DAG."""

    identities = {item[0] for item in IDENTITIES}
    source_ids = [item.get("artifact_id") for item in sources]
    if source_ids != sorted(identities):
        fail("FIXED_ARTIFACT_MISMATCH", "artifact order or set")
    manifests: dict[str, Mapping[str, Any]] = {}
    for item in sources:
        artifact_id = item["artifact_id"]
        manifest = item["dependency_manifest"]
        expected = DEPS[artifact_id]
        if (
            tuple(manifest["execution_artifact_ids"]),
            tuple(manifest["binding_artifact_ids"]),
            tuple(manifest["binding_document_ids"]),
        ) != expected:
            fail("DEPENDENCY_POLICY_MISMATCH", artifact_id)
        required_ids = set(expected[0]) | set(expected[1])
        if set(manifest["artifact_semantic_pins"]) != required_ids:
            fail("DEPENDENCY_PIN_SET_MISMATCH", artifact_id)
        manifests[artifact_id] = manifest

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(artifact_id: str) -> None:
        if artifact_id in visiting:
            fail("DEPENDENCY_CYCLE", artifact_id)
        if artifact_id in visited:
            return
        visiting.add(artifact_id)
        manifest = manifests[artifact_id]
        for dependency_id in (
            list(manifest["execution_artifact_ids"])
            + list(manifest["binding_artifact_ids"])
        ):
            if dependency_id not in manifests:
                fail("UNKNOWN_DEPENDENCY", f"{artifact_id}:{dependency_id}")
            visit(dependency_id)
        visiting.remove(artifact_id)
        visited.add(artifact_id)

    for artifact_id in sorted(manifests):
        visit(artifact_id)


def activation_gate(source: Mapping[str, Any]) -> None:
    statuses = {item["pin_status"] for item in source["artifacts"]}
    statuses |= {item["pin_status"] for item in source["pinned_documents"]}
    has_placeholder = "PLACEHOLDER_UNRESOLVED" in statuses
    if source["activation_status"] == PENDING:
        if not has_placeholder:
            fail("ACTIVATION_STATUS_MISMATCH", "pending source has no placeholder")
        fail("REGISTRY_NOT_ACTIVE", "V5 artifact pins are pending")
    if source["activation_status"] != ACTIVE or has_placeholder:
        fail("ACTIVATION_STATUS_MISMATCH", "active source has incomplete pins")
    for artifact in source["artifacts"]:
        values = [
            artifact["expected_blob_sha256"],
            artifact["expected_symbol_set_digest"],
            artifact["expected_local_import_closure_digest"],
            artifact["expected_dependency_manifest_digest"],
            artifact["expected_semantic_sha256"],
            *artifact["expected_symbol_ast_sha256"].values(),
        ]
        if any(value == ZERO for value in values):
            fail("ZERO_AUTHORITY_PIN", artifact["artifact_id"])
    for document in source["pinned_documents"]:
        if (
            document["expected_blob_sha256"] == ZERO
            or document["expected_canonical_sha256"] == ZERO
        ):
            fail("ZERO_AUTHORITY_PIN", document["document_id"])


def parse_module(path: str, content: bytes) -> ast.Module:
    try:
        return ast.parse(content.decode("utf-8"), filename=path)
    except (UnicodeDecodeError, SyntaxError) as exc:
        raise RegistryV5Error("PYTHON_PARSE_ERROR", f"{path}: {exc}") from exc


def function_owners(tree: ast.Module) -> tuple[dict[int, str], dict[int, ast.AST]]:
    owners: dict[int, str] = {}
    parent: dict[int, ast.AST] = {}
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            parent[id(child)] = node
    for top in tree.body:
        if isinstance(top, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for child in ast.walk(top):
                owners[id(child)] = top.name
    return owners, parent


def constant_binding(
    *, path: str, tree: ast.Module, name: str, expected: str
) -> None:
    matches = [
        (node, kind)
        for bound, node, kind in module_scope_bindings(tree.body)
        if bound == name
    ]
    if len(matches) != 1:
        fail("CONTROLLED_PATH_BINDING_MISMATCH", f"{path}:{name}")
    node, kind = matches[0]
    if not (
        kind == "ASSIGN"
        and type(node) is ast.Assign
        and len(node.targets) == 1
        and type(node.targets[0]) is ast.Name
        and node.targets[0].id == name
        and type(node.value) is ast.Constant
        and type(node.value.value) is str
        and node.value.value == expected
    ):
        fail("CONTROLLED_PATH_BINDING_MISMATCH", f"{path}:{name}")


def bundle_path_names(tree: ast.Module, owner: str, path: str) -> list[str]:
    assignments = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "specs" for target in node.targets)
    ]
    owners, _parents = function_owners(tree)
    assignments = [node for node in assignments if owners.get(id(node)) == owner]
    if len(assignments) != 1 or not isinstance(assignments[0].value, (ast.Tuple, ast.List)):
        fail("CONTROLLED_BUNDLE_TABLE_MISMATCH", path)
    names: list[str] = []
    for row in assignments[0].value.elts:
        if not isinstance(row, ast.Tuple) or len(row.elts) != 3:
            fail("CONTROLLED_BUNDLE_TABLE_MISMATCH", path)
        item = row.elts[1]
        if not isinstance(item, ast.Name):
            fail("CONTROLLED_BUNDLE_TABLE_MISMATCH", path)
        names.append(item.id)
    return names


def audit_controlled_loader(
    *,
    artifact_id: str,
    path: str,
    tree: ast.Module,
    content: bytes,
    blob_sha256: str,
    manifest: Mapping[str, Any],
) -> dict[str, Any]:
    contract = CONTROLLED_LOADER_CONTRACTS[artifact_id]
    caller = contract["caller_symbol"]
    observed = {
        caller: symbol_receipt(path, caller, content, blob_sha256)
    }
    if observed[caller] != contract["caller_symbol_ast_sha256"]:
        fail("CONTROLLED_LOADER_AST_MISMATCH", f"{path}:{caller}")
    for symbol, expected in contract["loader_symbols"].items():
        observed[symbol] = symbol_receipt(path, symbol, content, blob_sha256)
        if observed[symbol] != expected:
            fail("CONTROLLED_LOADER_AST_MISMATCH", f"{path}:{symbol}")
    for name, expected in contract["path_constants"].items():
        constant_binding(path=path, tree=tree, name=name, expected=expected)

    executable_literals = {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and type(node.value) is str
        and node.value.startswith("scripts/")
        and node.value.endswith(".py")
    }
    if executable_literals != set(contract["path_constants"].values()):
        fail("CONTROLLED_EXECUTABLE_LITERAL_MISMATCH", path)

    expected_execution = {
        artifact_id
        for artifact_id in contract["fresh_path_constants"].values()
        if artifact_id is not None
    } | set(contract["bundle_path_constants"].values())
    if set(manifest["execution_artifact_ids"]) != expected_execution:
        fail("CONTROLLED_EXECUTION_MANIFEST_MISMATCH", artifact_id)
    if set(manifest["binding_artifact_ids"]) != set(
        contract.get("binding_path_constants", {}).values()
    ):
        fail("CONTROLLED_BINDING_MANIFEST_MISMATCH", artifact_id)

    owners, parent = function_owners(tree)
    loader_symbols = set(contract["loader_symbols"])
    helper_calls: dict[str, list[ast.Call]] = {name: [] for name in loader_symbols}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots = {alias.name.split(".", 1)[0] for alias in node.names}
            if roots & {"importlib", "runpy", "builtins"}:
                fail("CONTROLLED_LOADER_ESCAPE", f"{path}:dynamic import")
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".", 1)[0] in {"importlib", "runpy", "builtins"}:
                fail("CONTROLLED_LOADER_ESCAPE", f"{path}:dynamic import")
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.value.id == "sys" and node.attr == "modules":
                if owners.get(id(node)) not in loader_symbols:
                    fail("CONTROLLED_LOADER_ESCAPE", f"{path}:sys.modules")
            if node.value.id in {"importlib", "runpy", "builtins"}:
                fail("CONTROLLED_LOADER_ESCAPE", f"{path}:{node.value.id}")
        if isinstance(node, ast.Name):
            if node.id in {"__builtins__", "__import__", "eval", "globals", "locals", "vars", "open", "input"}:
                fail("CONTROLLED_LOADER_ESCAPE", f"{path}:{node.id}")
            if node.id in {"compile", "exec"} and owners.get(id(node)) not in loader_symbols:
                fail("CONTROLLED_LOADER_ESCAPE", f"{path}:{node.id}")
            if node.id in loader_symbols:
                call = parent.get(id(node))
                if not (
                    isinstance(call, ast.Call)
                    and call.func is node
                    and owners.get(id(call)) == caller
                ):
                    fail("CONTROLLED_LOADER_ESCAPE", f"{path}:{node.id}")
                helper_calls[node.id].append(call)

    fresh_names: list[str] = []
    fresh_loader = "_fresh_module" if "_fresh_module" in loader_symbols else "_fresh"
    for call in helper_calls[fresh_loader]:
        if len(call.args) <= 2 or not isinstance(call.args[2], ast.Name):
            fail("CONTROLLED_LOADER_CALL_SHAPE", f"{path}:{fresh_loader}")
        fresh_names.append(call.args[2].id)
    if sorted(fresh_names) != sorted(contract["fresh_path_constants"]):
        fail("CONTROLLED_LOADER_CALL_SET_MISMATCH", f"{path}:{fresh_loader}")
    bundle_loader = "_fresh_v1_bundle"
    if len(helper_calls[bundle_loader]) != 1:
        fail("CONTROLLED_LOADER_CALL_SET_MISMATCH", f"{path}:{bundle_loader}")
    if bundle_path_names(tree, bundle_loader, path) != list(contract["bundle_path_constants"]):
        fail("CONTROLLED_BUNDLE_TABLE_MISMATCH", path)
    return {
        "caller_symbol": caller,
        "caller_symbol_ast_sha256": observed[caller],
        "loader_symbol_ast_sha256": {
            key: observed[key] for key in sorted(contract["loader_symbols"])
        },
        "direct_execution_artifact_ids": sorted(expected_execution),
        "binding_artifact_ids": sorted(contract.get("binding_path_constants", {}).values()),
        "status": "FIXED_EXACT_BLOB_LOADER_TABLE_MATCHES_V5_DEPENDENCY_DAG",
    }


def resolve_registry_v5(*, root: Path, requested_head: str) -> dict[str, Any]:
    repo = repository(root)
    head, tree = exact_head(repo, requested_head)
    entries = tree_entries(repo, head)
    binding = toolchain(repo, entries, head)
    source = strict_json(blob(repo, entries, REGISTRY_PATH), REGISTRY_PATH)
    schema = strict_json(blob(repo, entries, SCHEMA_PATH), SCHEMA_PATH)
    jsonschema.Draft202012Validator.check_schema(schema)
    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(source))
    if errors:
        fail("SOURCE_SCHEMA_INVALID", errors[0].message)
    cross_v4 = copy_json(source["v4_cross_registry_binding"])
    expected_v4_semantics = cross_v4.pop("expected_v4_artifact_semantic_sha256", None)
    if (
        source["status"] != STATUS
        or source["authority_policy"] != AUTHORITY_POLICY
        or source["base_admission_policy"] != BASE_ADMISSION_POLICY
        or source["orchestration_policy"] != ORCHESTRATION_POLICY
        or source["post_issuance_replay_policy"] != POST_ISSUANCE_REPLAY_POLICY
        or source["v3_cross_registry_binding"] != V3_CROSS_REGISTRY_BINDING
        or cross_v4 != V4_CROSS_REGISTRY_BINDING_BASE
        or source["authorized_branches"] != []
        or source["authority_denials"] != AUTHORITY_DENIALS
    ):
        fail("FIXED_POLICY_MISMATCH", "V5 policy source changed")
    activation_gate(source)
    if type(expected_v4_semantics) is not dict or set(expected_v4_semantics) != {
        "q1_root_owner_classifier_v2",
        "q1_scope_aware_e1_validator_v2",
        "v3_production_receipt_verifier_dependency",
        "v3_root_initializer_dependency",
    } or any(type(value) is not str or value == ZERO for value in expected_v4_semantics.values()):
        fail("V4_CROSS_PIN_MISMATCH", "V4 semantic pin map")
    prevalidate_dependency_graph(source["artifacts"])
    identities = {item[0]: item for item in IDENTITIES}
    sources = {item["artifact_id"]: item for item in source["artifacts"]}
    resolved_artifacts = []
    sem: dict[str, str] = {}
    # Leaves and dependent nodes form the fixed acyclic graph. Compute semantic
    # values from source pin maps; validate cross maps after all nodes resolve.
    for artifact_id in sorted(sources):
        item = sources[artifact_id]
        expected = identities[artifact_id]
        if (
            item["artifact_class"],
            item["kind"],
            item["path"],
            tuple(item["symbols"]),
            item["pin_status"],
            item["semantic_digest_method"],
        ) != (
            expected[1],
            "PYTHON_SYMBOL_SET",
            expected[2],
            expected[3],
            "PINNED",
            METHOD,
        ):
            fail("FIXED_ARTIFACT_MISMATCH", artifact_id)
        dep = item["dependency_manifest"]
        exact = DEPS[artifact_id]
        if (
            tuple(dep["execution_artifact_ids"]),
            tuple(dep["binding_artifact_ids"]),
            tuple(dep["binding_document_ids"]),
        ) != exact:
            fail("DEPENDENCY_POLICY_MISMATCH", artifact_id)
        if set(dep["artifact_semantic_pins"]) != set(exact[0]) | set(exact[1]):
            fail("DEPENDENCY_PIN_SET_MISMATCH", artifact_id)
        content = blob(repo, entries, item["path"])
        bh = hashlib.sha256(content).hexdigest()
        module_tree = parse_module(item["path"], content)
        receipts = {
            s: {
                "symbol_ast_sha256": symbol_receipt(item["path"], s, content, bh)
            }
            for s in item["symbols"]
        }
        ss = digest({"schema_id": "t6_python_symbol_set_v5", "symbols": receipts})
        files, cl = closure(repo, entries, item["path"])
        local_imports = {record["path"] for record in files if record["path"] != item["path"]}
        allowed_imports = {identities[dep_id][2] for dep_id in exact[0]}
        if not local_imports <= allowed_imports:
            fail(
                "UNDECLARED_LOCAL_IMPORT",
                f"{artifact_id}:{sorted(local_imports - allowed_imports)}",
            )
        md = manifest_digest(dep)
        controlled_loader_receipt = None
        if artifact_id in CONTROLLED_LOADER_CONTRACTS:
            controlled_loader_receipt = audit_controlled_loader(
                artifact_id=artifact_id,
                path=item["path"],
                tree=module_tree,
                content=content,
                blob_sha256=bh,
                manifest=dep,
            )
        semantic = digest(
            {
                "method": METHOD,
                "path": item["path"],
                "blob_sha256": bh,
                "symbol_set_digest": ss,
                "local_import_closure_digest": cl,
                "dependency_manifest_digest": md,
                "python_ast_contract_digest": python_ast_contract_digest(),
            }
        )
        observed = {
            "expected_blob_sha256": bh,
            "expected_symbol_set_digest": ss,
            "expected_local_import_closure_digest": cl,
            "expected_dependency_manifest_digest": md,
            "expected_semantic_sha256": semantic,
        }
        if item["expected_symbol_ast_sha256"] != {
            k: v["symbol_ast_sha256"] for k, v in receipts.items()
        }:
            fail("ARTIFACT_PIN_MISMATCH", artifact_id + ":ast")
        if any(item[k] != v for k, v in observed.items()):
            fail("ARTIFACT_PIN_MISMATCH", artifact_id)
        sem[artifact_id] = semantic
        resolved_artifacts.append(
            {
                **copy_json(item),
                "git_mode": entries[item["path"]][0],
                "git_object_id": entries[item["path"]][2],
                "blob_sha256": bh,
                "semantic_sha256": semantic,
                "symbol_set_digest": ss,
                "local_import_closure_digest": cl,
                "local_import_closure_files": files,
                "dependency_manifest_digest": md,
                **(
                    {"controlled_loader_contract": controlled_loader_receipt}
                    if controlled_loader_receipt is not None
                    else {}
                ),
            }
        )
    for item in resolved_artifacts:
        for dep_id, expected_sem in item["dependency_manifest"][
            "artifact_semantic_pins"
        ].items():
            if sem[dep_id] != expected_sem:
                fail(
                    "DEPENDENCY_SEMANTIC_PIN_MISMATCH",
                    item["artifact_id"] + ":" + dep_id,
                )
    role_artifacts = [
        next(item for item in resolved_artifacts if item["artifact_id"] == binding[1])
        for binding in ROLE_BINDINGS.values()
    ]
    if len({item["path"] for item in role_artifacts}) != 2:
        fail("ROLE_PATH_COLLISION", "V5 role modules must differ")
    if len({item["blob_sha256"] for item in role_artifacts}) != 2:
        fail("ROLE_BLOB_COLLISION", "V5 role blobs must differ")
    if len({item["semantic_sha256"] for item in role_artifacts}) != 2:
        fail("ROLE_SEMANTIC_COLLISION", "V5 role semantics must differ")
    if set(CONTROLLED_LOADER_CONTRACTS) != {ORCHESTRATOR_ID, REPLAYER_ID}:
        fail("CONTROLLED_LOADER_CONTRACT_MISSING", "V5 non-role loader set")
    # The raw V4 and V2 resolver artifacts above have passed all V5 pins before
    # any requested-HEAD V4 code is allowed to execute.
    v4 = load_v4(repo, entries, head)
    # Exact V4 same-head resolver closes V3 transitively and ensures V4 E1 is
    # not accepted as a V5 base input.
    try:
        with sanitized_git_environment():
            v4_resolved = v4.resolve_registry_v4(root=repo, requested_head=head)
    except Exception as exc:
        raise RegistryV5Error("V4_CROSS_RESOLUTION_FAILED", str(exc)) from exc
    if (
        v4_resolved.get("head_sha") != head
        or v4_resolved.get("status")
        != "HEAD_BOUND_Q1_ROOT_PREFIX_SCOPED_E1_AUTHORITY_NO_SUCCESSOR_OR_RECURSION"
    ):
        fail("V4_CROSS_MISMATCH", "head/status")
    amap = {a["artifact_id"]: a for a in v4_resolved["resolved_artifacts"]}
    for own, foreign in (
        (V4_OWNER_ID, "q1_root_owner_classifier_v2"),
        (V4_SCOPE_ID, "q1_scope_aware_e1_validator_v2"),
        (V3_PROD_ID, "v3_production_receipt_verifier_dependency"),
        (V3_ROOT_ID, "v3_root_initializer_dependency"),
    ):
        if (
            resolved_artifacts[
                [a["artifact_id"] for a in resolved_artifacts].index(own)
            ]["blob_sha256"]
            != amap[foreign]["blob_sha256"]
        ):
            fail("V4_CROSS_ARTIFACT_MISMATCH", own)
        if amap[foreign]["semantic_sha256"] != expected_v4_semantics[foreign]:
            fail("V4_CROSS_SEMANTIC_PIN_MISMATCH", foreign)
    grants = []
    artmap = {a["artifact_id"]: a for a in resolved_artifacts}
    if [grant.get("grant_id") for grant in source["role_grants"]] != sorted(
        ROLE_BINDINGS
    ):
        fail("FIXED_GRANT_MISMATCH", "grant order or set")
    for grant in source["role_grants"]:
        grant_id = grant["grant_id"]
        if grant_id not in ROLE_BINDINGS:
            fail("FIXED_GRANT_MISMATCH", str(grant_id))
        role, aid, caps = ROLE_BINDINGS[grant_id]
        art = artmap[aid]
        if (
            grant["role"] != role
            or grant["artifact_id"] != aid
            or tuple(grant["capabilities"]) != caps
            or grant["authority_class"] != "HEAD_BOUND_EXECUTABLE_CAPABILITY_V5"
            or grant["expected_artifact_semantic_sha256"] != art["semantic_sha256"]
            or grant["expected_dependency_manifest_digest"]
            != art["dependency_manifest_digest"]
        ):
            fail("GRANT_PIN_MISMATCH", grant["grant_id"])
        wire = {
            "grant_id": grant["grant_id"],
            "role": role,
            "artifact_id": aid,
            "artifact_path": art["path"],
            "artifact_symbols": art["symbols"],
            "capabilities": grant["capabilities"],
            "authority_class": "HEAD_BOUND_EXECUTABLE_CAPABILITY_V5",
            "artifact_semantic_sha256": art["semantic_sha256"],
        }
        grants.append(
            {**copy_json(grant), "grant_wire": wire, "role_grant_digest": digest(wire)}
        )
    doc = source["pinned_documents"][0]
    if (
        doc["document_id"] != "q1_root_v1_base_admission_receipt_schema_v1"
        or doc["path"] != RECEIPT_SCHEMA_PATH
        or doc["schema_id"] != "q1_root_v1_base_admission_v1"
        or doc["schema_version"] != 1
    ):
        fail("DOCUMENT_POLICY_MISMATCH", "V1 base receipt schema")
    raw = blob(repo, entries, doc["path"])
    parsed = strict_json(raw, doc["path"])
    jsonschema.Draft202012Validator.check_schema(parsed)
    if (
        hashlib.sha256(raw).hexdigest() != doc["expected_blob_sha256"]
        or digest(parsed) != doc["expected_canonical_sha256"]
        or parsed.get("$id") != doc["expected_json_schema_id"]
    ):
        fail("DOCUMENT_PIN_MISMATCH", doc["document_id"])
    manifest = {
        "schema_id": "t6_q1_root_v1_base_admission_manifest_v5",
        "head_sha": head,
        "status": STATUS,
        "v4_registry_digest": v4_resolved["registry_digest"],
        "grants": grants,
        "authority_denials": AUTHORITY_DENIALS,
    }
    manifest["digest"] = digest(manifest)
    if toolchain(repo, entries, head) != binding:
        fail("TOOLCHAIN_CHANGED_DURING_RESOLUTION", RESOLVER_PATH)
    payload = {
        "schema_id": RESOLVED_SCHEMA_ID,
        "schema_version": 5,
        "head_sha": head,
        "head_tree_sha": tree,
        "execution_binding": binding,
        "resolved_artifacts": resolved_artifacts,
        "resolved_role_grants": grants,
        "v4_cross_registry_digest": v4_resolved["registry_digest"],
        "v4_role_manifest_digest": v4_resolved["role_authority_manifest"]["digest"],
        "base_admission_policy": copy_json(source["base_admission_policy"]),
        "authority_denials": AUTHORITY_DENIALS,
        "authorized_branches": [],
        "role_authority_manifest": manifest,
        "new_role_grant_count": 2,
        "inherited_v4_role_capability_count": 3,
        "effective_role_capability_count": 5,
        "queue_mutator_count": 0,
        "successor_producer_count": 0,
        "status": STATUS,
        "proof_boundary": source["proof_boundary"],
    }
    payload["registry_digest"] = digest(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--head", required=True)
    args = parser.parse_args(argv)
    try:
        print(
            canonical_bytes(
                resolve_registry_v5(root=args.root, requested_head=args.head)
            ).decode()
        )
    except RegistryV5Error as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
