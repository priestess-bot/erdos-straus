#!/usr/bin/env python3
"""Resolve the q1 root prefix-scoped source-E1 authority at one exact HEAD.

V4 inherits the frozen V3 terminal-issuance authority and adds exactly three
loader-free roles.  It grants no generic/successor E1, producer, branch,
admission, T5, re-entry, or queue capability.  A tracked placeholder keeps the
registry inactive until every executable and normative document is pinned.
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


SCHEMA_ID = "t6_coordinator_role_registry_v4"
SCHEMA_VERSION = 4
RESOLVED_SCHEMA_ID = "t6_coordinator_role_registry_resolved_v4"
REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v4.json"
RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v4.py"
SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v4.schema.json"
TOOLCHAIN_PATHS = (REGISTRY_PATH, RESOLVER_PATH, SCHEMA_PATH)

STATUS = (
    "HEAD_BOUND_Q1_ROOT_PREFIX_SCOPED_E1_AUTHORITY_"
    "NO_SUCCESSOR_OR_RECURSION"
)
PENDING = "PENDING_ARTIFACT_PINS"
ACTIVE = "ACTIVE_EXACT_HEAD_AUTHORITY"
AUTHORITY_SOURCE = "TRACKED_GIT_OBJECTS_AT_EXACT_REQUESTED_HEAD"
ROLE_AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V4"
SEMANTIC_DIGEST_METHOD = (
    "PYTHON_STABLE_AST_SYMBOL_SET_BLOB_CLOSURE_DEPENDENCY_SHA256_V4"
)
AST_CONTRACT_ID = "t6_python_ast_normalization_v4"

V3_REGISTRY_ID = "t6_coordinator_role_registry_v3"
V3_REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v3.json"
V3_SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v3.schema.json"
V3_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v3.py"
V3_RESOLVER_SYMBOL = "resolve_registry_v3"
V3_STATUS = "HEAD_BOUND_Q1_ROOT_TERMINAL_DECISION_AUTHORITY_NO_RECURSION"
V3_PRODUCTION_VERIFIER_PATH = (
    "scripts/t6_q_one_terminal_receipt_verifier_v1.py"
)
V3_PRODUCTION_VERIFIER_SYMBOL = "verify_q_one_production_terminal_receipt_v1"
V3_PRODUCTION_SCHEMA_PATH = (
    "schemas/t6-q-one-production-terminal-receipts-v1.schema.json"
)

OWNER_REFERENCE_ID = "persistent_owner_contract_reference_v1"
OWNER_REFERENCE_PATH = "scripts/t6_persistent_selector_state_v1.py"
OWNER_REFERENCE_SYMBOLS = (
    "_family_predicates_v1",
    "classify_selector_owner_v1",
    "owner_digest_v1",
)
OWNER_ARTIFACT_ID = "q1_root_owner_classifier_v2"
OWNER_PATH = "scripts/t6_q_one_root_owner_classifier_v2.py"
OWNER_SYMBOLS = (
    "classify_q_one_root_owner_v2",
    "root_owner_receipt_to_mapping_v2",
)
VALIDATOR_ARTIFACT_ID = "q1_scope_aware_e1_validator_v2"
VALIDATOR_PATH = "scripts/t6_q_one_scope_aware_e1_validator_v2.py"
VALIDATOR_SYMBOLS = (
    "validate_q_one_registered_prefix_e1_scope_v2",
    "scope_validation_receipt_to_mapping_v2",
)
CONSUMER_ARTIFACT_ID = "q1_registered_prefix_e1_consumer_v2"
CONSUMER_PATH = "scripts/t6_q_one_registered_prefix_e1_consumer_v2.py"
CONSUMER_SYMBOLS = (
    "consume_q_one_registered_prefix_miss_for_e1_v2",
    "root_source_scoped_e1_receipt_to_mapping_v2",
)
ORCHESTRATOR_ARTIFACT_ID = "q1_root_prefix_scoped_e1_orchestrator_v2"
ORCHESTRATOR_PATH = "scripts/t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py"
ORCHESTRATOR_SYMBOL = "assemble_q_one_root_prefix_scoped_e1_v2"
REPLAYER_ARTIFACT_ID = "q1_root_prefix_scoped_e1_receipt_verifier_v2"
REPLAYER_PATH = "scripts/t6_q_one_root_prefix_scoped_e1_receipt_verifier_v2.py"
REPLAYER_SYMBOL = "verify_q_one_root_prefix_scoped_e1_receipt_v2"
V3_RESOLVER_ARTIFACT_ID = "v3_registry_resolver_dependency"
V3_PRODUCTION_VERIFIER_ARTIFACT_ID = (
    "v3_production_receipt_verifier_dependency"
)
V3_ROOT_INITIALIZER_ARTIFACT_ID = "v3_root_initializer_dependency"

RECEIPT_SCHEMA_ID = "t6-q-one-root-prefix-scoped-e1-v2"
RECEIPT_SCHEMA_VERSION = 2
RECEIPT_SCHEMA_PATH = "schemas/t6-q-one-root-prefix-scoped-e1-v2.schema.json"
RECEIPT_JSON_SCHEMA_ID = (
    "https://priestess-bot.github.io/erdos-straus/schemas/"
    "t6-q-one-root-prefix-scoped-e1-v2.schema.json"
)

ROLE_OWNER = "COMMON_ROOT_OWNER_CLASSIFIER"
ROLE_VALIDATOR = "INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR"
ROLE_CONSUMER = "REGISTERED_PREFIX_E1_CONSUMER"
ALLOWED_ROLES = (ROLE_OWNER, ROLE_VALIDATOR, ROLE_CONSUMER)
OWNER_GRANT_ID = "q1_common_root_owner_classifier_grant_v4"
VALIDATOR_GRANT_ID = "q1_scope_aware_e1_validator_grant_v4"
CONSUMER_GRANT_ID = "q1_registered_prefix_e1_consumer_grant_v4"

REGULAR_MODES = frozenset({"100644", "100755"})
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
ZERO_SHA256 = "0" * 64
PATH_TYPE = type(Path())
FORBIDDEN_EXECUTABLE_ROOTS = frozenset(
    {
        ".github",
        "claims",
        "concepts",
        "data",
        "docs",
        "index",
        "reproductions",
        "schemas",
        "tests",
    }
)
PURE_ROLE_FORBIDDEN_IMPORTS = frozenset(
    {
        "builtins",
        "importlib",
        "os",
        "pathlib",
        "pkgutil",
        "runpy",
        "subprocess",
        "sys",
    }
)
PURE_ROLE_ALLOWED_IMPORT_ROOTS = frozenset(
    {
        "__future__",
        "collections",
        "dataclasses",
        "enum",
        "functools",
        "hashlib",
        "itertools",
        "json",
        "math",
        "re",
        "types",
        "typing",
    }
)

ARTIFACT_CLASS_ROLE = "ROLE_ARTIFACT"
ARTIFACT_CLASS_REFERENCE = "REFERENCE_ONLY"
ARTIFACT_CLASS_ORCHESTRATOR = "CONTROLLED_LOADER_ORCHESTRATOR_ONLY"
ARTIFACT_CLASS_REPLAYER = "POST_ISSUANCE_REPLAY_DEPENDENCY_ONLY"
ARTIFACT_CLASS_V3 = "V3_CROSS_REGISTRY_DEPENDENCY_ONLY"

ARTIFACT_IDENTITIES = (
    (
        OWNER_REFERENCE_ID,
        ARTIFACT_CLASS_REFERENCE,
        "PYTHON_REFERENCE_SYMBOL_SET",
        OWNER_REFERENCE_PATH,
        OWNER_REFERENCE_SYMBOLS,
    ),
    (
        CONSUMER_ARTIFACT_ID,
        ARTIFACT_CLASS_ROLE,
        "PYTHON_SYMBOL_SET",
        CONSUMER_PATH,
        CONSUMER_SYMBOLS,
    ),
    (
        OWNER_ARTIFACT_ID,
        ARTIFACT_CLASS_ROLE,
        "PYTHON_SYMBOL_SET",
        OWNER_PATH,
        OWNER_SYMBOLS,
    ),
    (
        ORCHESTRATOR_ARTIFACT_ID,
        ARTIFACT_CLASS_ORCHESTRATOR,
        "PYTHON_SYMBOL_SET",
        ORCHESTRATOR_PATH,
        (ORCHESTRATOR_SYMBOL,),
    ),
    (
        REPLAYER_ARTIFACT_ID,
        ARTIFACT_CLASS_REPLAYER,
        "PYTHON_SYMBOL_SET",
        REPLAYER_PATH,
        (REPLAYER_SYMBOL,),
    ),
    (
        VALIDATOR_ARTIFACT_ID,
        ARTIFACT_CLASS_ROLE,
        "PYTHON_SYMBOL_SET",
        VALIDATOR_PATH,
        VALIDATOR_SYMBOLS,
    ),
    (
        V3_PRODUCTION_VERIFIER_ARTIFACT_ID,
        ARTIFACT_CLASS_V3,
        "PYTHON_SYMBOL_SET",
        V3_PRODUCTION_VERIFIER_PATH,
        (V3_PRODUCTION_VERIFIER_SYMBOL,),
    ),
    (
        V3_RESOLVER_ARTIFACT_ID,
        ARTIFACT_CLASS_V3,
        "PYTHON_SYMBOL_SET",
        V3_RESOLVER_PATH,
        (V3_RESOLVER_SYMBOL,),
    ),
    (
        V3_ROOT_INITIALIZER_ARTIFACT_ID,
        ARTIFACT_CLASS_V3,
        "PYTHON_SYMBOL_SET",
        "scripts/t6_q_one_root_initializer_envelope_v2.py",
        (
            "artifact_to_mapping_v2",
            "make_canonical_q_one_g_source_body_v2",
            "make_raw_root_source_state_v2",
            "make_root_initializer_anchor_v2",
        ),
    ),
)

DEPENDENCIES = {
    OWNER_REFERENCE_ID: ((), (), ()),
    OWNER_ARTIFACT_ID: (
        (),
        tuple(sorted((OWNER_REFERENCE_ID, V3_ROOT_INITIALIZER_ARTIFACT_ID))),
        (RECEIPT_SCHEMA_PATH,),
    ),
    VALIDATOR_ARTIFACT_ID: (
        (),
        tuple(
            sorted(
                (
                    OWNER_ARTIFACT_ID,
                    V3_PRODUCTION_VERIFIER_ARTIFACT_ID,
                    V3_ROOT_INITIALIZER_ARTIFACT_ID,
                )
            )
        ),
        (RECEIPT_SCHEMA_PATH,),
    ),
    CONSUMER_ARTIFACT_ID: (
        (),
        tuple(
            sorted(
                (
                    OWNER_ARTIFACT_ID,
                    VALIDATOR_ARTIFACT_ID,
                    V3_PRODUCTION_VERIFIER_ARTIFACT_ID,
                    V3_ROOT_INITIALIZER_ARTIFACT_ID,
                )
            )
        ),
        (RECEIPT_SCHEMA_PATH,),
    ),
    ORCHESTRATOR_ARTIFACT_ID: (
        tuple(
            sorted(
                (
                    CONSUMER_ARTIFACT_ID,
                    OWNER_ARTIFACT_ID,
                    VALIDATOR_ARTIFACT_ID,
                    V3_PRODUCTION_VERIFIER_ARTIFACT_ID,
                    V3_RESOLVER_ARTIFACT_ID,
                    V3_ROOT_INITIALIZER_ARTIFACT_ID,
                )
            )
        ),
        (),
        (REGISTRY_PATH, SCHEMA_PATH, RECEIPT_SCHEMA_PATH, RESOLVER_PATH),
    ),
    REPLAYER_ARTIFACT_ID: (
        tuple(
            sorted(
                (
                    CONSUMER_ARTIFACT_ID,
                    OWNER_ARTIFACT_ID,
                    VALIDATOR_ARTIFACT_ID,
                    V3_PRODUCTION_VERIFIER_ARTIFACT_ID,
                    V3_RESOLVER_ARTIFACT_ID,
                    V3_ROOT_INITIALIZER_ARTIFACT_ID,
                )
            )
        ),
        tuple(
            sorted(
                (
                    ORCHESTRATOR_ARTIFACT_ID,
                )
            )
        ),
        (RECEIPT_SCHEMA_PATH, RESOLVER_PATH),
    ),
    V3_PRODUCTION_VERIFIER_ARTIFACT_ID: (
        (),
        (),
        (
            V3_REGISTRY_PATH,
            V3_SCHEMA_PATH,
            V3_PRODUCTION_SCHEMA_PATH,
            V3_RESOLVER_PATH,
        ),
    ),
    V3_RESOLVER_ARTIFACT_ID: ((), (), (V3_REGISTRY_PATH, V3_SCHEMA_PATH)),
    V3_ROOT_INITIALIZER_ARTIFACT_ID: (
        (),
        (),
        (V3_REGISTRY_PATH, V3_SCHEMA_PATH),
    ),
}

CONTROLLED_LOADER_CONTRACTS = {
    ORCHESTRATOR_ARTIFACT_ID: {
        "loader_symbol": "_fresh_module",
        "loader_symbol_ast_sha256": "4a00516e1b2090f66ac01f95511c1a7c958d3c3ae00832b5c688adf93ae94739",
        "caller_symbol": ORCHESTRATOR_SYMBOL,
        "caller_symbol_ast_sha256": "7a9df28e6b71c0787486df37ee9a2c7994d3f40e9070241719f93cc27f4037a2",
        "path_constants": {
            "ORCHESTRATOR_PATH": ORCHESTRATOR_PATH,
            "V4_RESOLVER_PATH": RESOLVER_PATH,
            "V3_VERIFIER_PATH": V3_PRODUCTION_VERIFIER_PATH,
            "V3_RESOLVER_PATH": V3_RESOLVER_PATH,
            "ROOT_INITIALIZER_PATH": "scripts/t6_q_one_root_initializer_envelope_v2.py",
            "OWNER_PATH": OWNER_PATH,
            "VALIDATOR_PATH": VALIDATOR_PATH,
            "CONSUMER_PATH": CONSUMER_PATH,
        },
        "direct_loader_artifacts": {
            "V3_VERIFIER_PATH": V3_PRODUCTION_VERIFIER_ARTIFACT_ID,
            "ROOT_INITIALIZER_PATH": V3_ROOT_INITIALIZER_ARTIFACT_ID,
            "OWNER_PATH": OWNER_ARTIFACT_ID,
            "VALIDATOR_PATH": VALIDATOR_ARTIFACT_ID,
            "CONSUMER_PATH": CONSUMER_ARTIFACT_ID,
        },
        "direct_loader_toolchain_paths": {
            "V4_RESOLVER_PATH": RESOLVER_PATH,
        },
        "transitive_execution_artifact_ids": (V3_RESOLVER_ARTIFACT_ID,),
        "path_position": 2,
    },
    REPLAYER_ARTIFACT_ID: {
        "loader_symbol": "_fresh",
        "loader_symbol_ast_sha256": "a5862f8e27982b8e9d3506f043c503dda9e7dfd05c073b7d2c749ce850e7a562",
        "caller_symbol": REPLAYER_SYMBOL,
        "caller_symbol_ast_sha256": "9be5c9d6aad998b47b1b9abb66385d59663f88eb349d83245d361cca59b02806",
        "path_constants": {
            "VERIFIER_PATH": REPLAYER_PATH,
            "ORCHESTRATOR_PATH": ORCHESTRATOR_PATH,
            "V4_RESOLVER_PATH": RESOLVER_PATH,
            "V3_VERIFIER_PATH": V3_PRODUCTION_VERIFIER_PATH,
            "ROOT_INITIALIZER_PATH": "scripts/t6_q_one_root_initializer_envelope_v2.py",
            "OWNER_PATH": OWNER_PATH,
            "VALIDATOR_PATH": VALIDATOR_PATH,
            "CONSUMER_PATH": CONSUMER_PATH,
        },
        "direct_loader_artifacts": {
            "V3_VERIFIER_PATH": V3_PRODUCTION_VERIFIER_ARTIFACT_ID,
            "ROOT_INITIALIZER_PATH": V3_ROOT_INITIALIZER_ARTIFACT_ID,
            "OWNER_PATH": OWNER_ARTIFACT_ID,
            "VALIDATOR_PATH": VALIDATOR_ARTIFACT_ID,
            "CONSUMER_PATH": CONSUMER_ARTIFACT_ID,
        },
        "direct_loader_toolchain_paths": {
            "V4_RESOLVER_PATH": RESOLVER_PATH,
        },
        "transitive_execution_artifact_ids": (V3_RESOLVER_ARTIFACT_ID,),
        "path_position": 2,
    },
}

ROLE_BINDINGS = (
    (
        OWNER_GRANT_ID,
        ROLE_OWNER,
        OWNER_ARTIFACT_ID,
        ("CLASSIFY_COMMON_Q1_ROOT_OWNER",),
    ),
    (
        CONSUMER_GRANT_ID,
        ROLE_CONSUMER,
        CONSUMER_ARTIFACT_ID,
        ("ISSUE_REGISTERED_PREFIX_ROOT_SOURCE_SCOPED_E1",),
    ),
    (
        VALIDATOR_GRANT_ID,
        ROLE_VALIDATOR,
        VALIDATOR_ARTIFACT_ID,
        ("VALIDATE_REGISTERED_PREFIX_ROOT_SOURCE_E1_SCOPE",),
    ),
)

AUTHORITY_POLICY = {
    "source": AUTHORITY_SOURCE,
    "caller_override_authority": False,
    "worktree_authority": False,
    "fixed_owner_domain": "ordinary_parentless_q1_g_root_v1",
    "inherited_registry_id": V3_REGISTRY_ID,
    "new_roles": list(ALLOWED_ROLES),
    "role_modules_must_be_loader_free": True,
}
CONSUMER_SCOPE = {
    "scope_id": "q1_root_after_gap_3_7_11_registered_prefix_v1",
    "owner_domain_id": "ordinary_parentless_q1_g_root_v1",
    "owner": "type_ii_relation_g_endpoint",
    "owner_scope": "ROOT_SOURCE_DISPATCH_ONLY",
    "source_terminal_outcome": "MISS_REGISTERED_PRIORITY_COMPLETE",
    "coverage_semantics": "REGISTERED_PRIORITY_ONLY",
    "ordered_gaps": [3, 7, 11],
    "next_unchecked_gap": 15,
    "global_exhaustion": False,
    "remaining_domain_unchecked": True,
    "same_head_consumption_required": True,
}
RECEIPT_AUTHORITY_MATRIX = {
    "COMMON_Q1_ROOT_OWNER_RECEIPT_V2": {
        "source_actualness": True,
        "common_owner_authority": True,
        "registered_prefix_miss_authority": False,
        "scope_validation_authority": False,
        "root_source_scoped_e1": False,
        "scope_aware_consumer_authority": False,
        "root_source_occurrence_authority": False,
        "terminal_receipt_direct_continuation_authority": False,
        "e1_authority": False,
        "generic_e1": False,
        "successor_e1": False,
        "producer_authority": False,
        "producer_continuation_allowed": False,
        "persistent_admission": False,
        "queue_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "global_exhaustion": False,
        "terminal_leaf_authority": False,
        "root_proof_close_authority": False,
    },
    "Q1_REGISTERED_PREFIX_SCOPE_VALIDATION_RECEIPT_V2": {
        "source_actualness": True,
        "common_owner_authority": False,
        "registered_prefix_miss_authority": True,
        "scope_validation_authority": True,
        "root_source_scoped_e1": False,
        "scope_aware_consumer_authority": False,
        "root_source_occurrence_authority": False,
        "terminal_receipt_direct_continuation_authority": False,
        "e1_authority": False,
        "generic_e1": False,
        "successor_e1": False,
        "producer_authority": False,
        "producer_continuation_allowed": False,
        "persistent_admission": False,
        "queue_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "global_exhaustion": False,
        "terminal_leaf_authority": False,
        "root_proof_close_authority": False,
    },
    "Q1_REGISTERED_PREFIX_ROOT_SOURCE_E1_RECEIPT_V2": {
        "source_actualness": True,
        "common_owner_authority": True,
        "registered_prefix_miss_authority": True,
        "scope_validation_authority": True,
        "root_source_scoped_e1": True,
        "scope_aware_consumer_authority": True,
        "root_source_occurrence_authority": True,
        "terminal_receipt_direct_continuation_authority": False,
        "e1_authority": False,
        "generic_e1": False,
        "successor_e1": False,
        "producer_authority": False,
        "producer_continuation_allowed": False,
        "persistent_admission": False,
        "queue_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
        "global_exhaustion": False,
        "terminal_leaf_authority": False,
        "root_proof_close_authority": False,
    },
}
ORCHESTRATION_POLICY = {
    "artifact_id": ORCHESTRATOR_ARTIFACT_ID,
    "artifact_class": ARTIFACT_CLASS_ORCHESTRATOR,
    "public_symbol": ORCHESTRATOR_SYMBOL,
    "allowed_execution_artifact_ids": list(
        DEPENDENCIES[ORCHESTRATOR_ARTIFACT_ID][0]
    ),
    "execution_toolchain_paths": [RESOLVER_PATH],
    "forbidden_execution_roots": ["reproductions", "tests"],
    "caller_inputs": [
        "production_miss_receipt",
        "raw_q_one_g",
        "repository_locator",
        "requested_head",
    ],
    "caller_supplied_owner_or_validation_allowed": False,
}
POST_REPLAY_POLICY = {
    "artifact_id": REPLAYER_ARTIFACT_ID,
    "artifact_class": ARTIFACT_CLASS_REPLAYER,
    "public_symbol": REPLAYER_SYMBOL,
    "consumer_import_allowed": False,
    "orchestrator_import_allowed": False,
    "independent_wire_reconstruction": True,
}
AUTHORITY_DENIALS = {
    "global_miss_authority": False,
    "global_exhaustion_authority": False,
    "terminal_leaf_authority": False,
    "root_proof_close_authority": False,
    "generic_e1_authority": False,
    "successor_e1_authority": False,
    "legacy_e1_boolean_authority": False,
    "producer_authority": False,
    "branch_authority": False,
    "candidate_authority": False,
    "e2_authority": False,
    "e3_authority": False,
    "e4_authority": False,
    "e5_authority": False,
    "t5_authority": False,
    "persistent_admission_authority": False,
    "reentry_authority": False,
    "queue_authority": False,
    "enqueue_authority": False,
}

class RegistryV4Error(ValueError):
    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: str, detail: str) -> NoReturn:
    raise RegistryV4Error(code, detail)


@dataclass(frozen=True, slots=True)
class GitBlobV4:
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
                _reject("NONCANONICAL_VALUE", f"{path} has non-string key")
            result[key] = _json_copy(child, f"{path}.{key}")
        return result
    if type(value) is list:
        return [_json_copy(child, f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return value
    _reject("NONCANONICAL_VALUE", f"{path} has unsupported {type(value).__name__}")


def canonical_json_bytes_v4(value: Any) -> bytes:
    return json.dumps(
        _json_copy(value),
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("ascii")


def canonical_digest_v4(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes_v4(value)).hexdigest()


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _stable_ast_value_v4(value: Any) -> Any:
    """Normalize Python AST while explicitly representing ``Ellipsis``."""

    if isinstance(value, ast.AST):
        result: dict[str, Any] = {"_type": type(value).__name__}
        for name, child in ast.iter_fields(value):
            if name == "type_params" and child == []:
                continue
            result[name] = _stable_ast_value_v4(child)
        return result
    if type(value) is list:
        return [_stable_ast_value_v4(child) for child in value]
    if value is Ellipsis:
        return {"_literal": "ELLIPSIS"}
    if value is None or type(value) in {str, bool, int}:
        return value
    _reject("PYTHON_AST_UNSUPPORTED", f"unsupported AST field {type(value).__name__}")


def _python_ast_contract_digest_v4() -> str:
    return canonical_digest_v4(
        {
            "schema_id": AST_CONTRACT_ID,
            "stable_ast_fields": "ast.iter_fields",
            "omit_empty_type_params": True,
            "ellipsis_encoding": {"_literal": "ELLIPSIS"},
            "supported_scalar_types": ["None", "str", "bool", "int"],
        }
    )


def _symbol_receipt_v4(
    path: str, symbol: str, content: bytes, blob_sha256: str, v2: ModuleType
) -> dict[str, str]:
    if type(symbol) is not str or v2.SYMBOL_RE.fullmatch(symbol) is None:
        _reject("SYMBOL_INVALID", f"invalid symbol {symbol!r}")
    try:
        tree = ast.parse(content.decode("utf-8"), filename=path)
    except (UnicodeDecodeError, SyntaxError) as exc:
        raise RegistryV4Error("PYTHON_PARSE_ERROR", f"{path}: {exc}") from exc
    bindings = v2._module_scope_bindings(tree.body)
    matches = [(node, kind) for name, node, kind in bindings if name == symbol]
    if not matches:
        _reject("SYMBOL_MISSING", f"{path}:{symbol}")
    if len(matches) != 1:
        _reject("SYMBOL_AMBIGUITY", f"{path}:{symbol} has {len(matches)} bindings")
    node, kind = matches[0]
    if type(node) is not ast.FunctionDef or kind != "DIRECT_FUNCTION":
        _reject("SYMBOL_NOT_FUNCTION", f"{path}:{symbol}")
    if node.decorator_list:
        _reject("AUTHORIZED_SYMBOL_DECORATED", f"{path}:{symbol}")
    return {
        "symbol_ast_sha256": canonical_digest_v4(_stable_ast_value_v4(node)),
        "blob_sha256": blob_sha256,
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
    if type(locator) is not PATH_TYPE:
        _reject("INVALID_ROOT", "root must be a pathlib.Path")
    return Path(
        _run_git(locator.resolve(), ("rev-parse", "--show-toplevel"))
        .decode()
        .strip()
    ).resolve()


def _exact_head(root: Path, requested_head: str) -> tuple[str, str, str]:
    object_format = _run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    length = 40 if object_format == "sha1" else 64 if object_format == "sha256" else 0
    if (
        type(requested_head) is not str
        or len(requested_head) != length
        or any(character not in "0123456789abcdef" for character in requested_head)
    ):
        _reject("INVALID_HEAD", "requested_head must be one full lowercase commit ID")
    if _run_git(root, ("cat-file", "-t", requested_head)).decode().strip() != "commit":
        _reject("INVALID_HEAD", "requested object is not a commit")
    resolved = _run_git(root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}"))
    if resolved.decode().strip() != requested_head:
        _reject("INVALID_HEAD", "commit resolution changed")
    tree = _run_git(root, ("rev-parse", f"{requested_head}^{{tree}}")).decode().strip()
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


def _safe_path(value: Any, *, executable: bool = False) -> str:
    if type(value) is not str or PATH_RE.fullmatch(value) is None:
        _reject("UNSAFE_PATH", repr(value))
    pure = PurePosixPath(value)
    if pure.is_absolute() or value != pure.as_posix() or any(
        part in {"", ".", ".."} for part in pure.parts
    ):
        _reject("UNSAFE_PATH", value)
    if executable and (pure.parts[0] != "scripts" or pure.suffix != ".py"):
        _reject("FORBIDDEN_EXECUTABLE_ROOT", value)
    return value


def _blob(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    path: str,
    *,
    executable: bool = False,
) -> GitBlobV4:
    path = _safe_path(path, executable=executable)
    entry = entries.get(path)
    if entry is None:
        _reject("MISSING_ARTIFACT", path)
    mode, object_type, object_id = entry
    if mode not in REGULAR_MODES or object_type != "blob":
        _reject("INVALID_GIT_MODE", path)
    content = _run_git(root, ("cat-file", "blob", object_id))
    return GitBlobV4(mode, object_type, object_id, path, content)


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
        decoded = json.loads(
            value.decode("utf-8"),
            object_pairs_hook=pairs,
            parse_float=number,
            parse_constant=number,
        )
    except RegistryV4Error:
        raise
    except Exception as exc:
        raise RegistryV4Error("INVALID_JSON", f"{source}: {exc}") from exc
    if type(decoded) is not dict:
        _reject("INVALID_JSON", f"{source} is not an object")
    _json_copy(decoded)
    return decoded


def _toolchain_binding(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    head_sha: str,
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
            {
                "path": path,
                "git_mode": blob.mode,
                "git_object_id": blob.object_id,
                "sha256": _sha256(blob.content),
            }
        )
    executing = Path(__file__)
    if executing.is_symlink() or executing.resolve().read_bytes() != head_values[RESOLVER_PATH]:
        _reject("EXECUTING_RESOLVER_HEAD_MISMATCH", RESOLVER_PATH)
    payload: dict[str, Any] = {
        "schema_id": "t6_coordinator_role_registry_toolchain_binding_v4",
        "head_sha": head_sha,
        "status": "BOUND_SELF_SCHEMA_AND_REGISTRY_TO_REQUESTED_HEAD",
        "files": files,
    }
    payload["digest"] = canonical_digest_v4(payload)
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


def _load_v3(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    source: Mapping[str, Any],
    head_sha: str,
) -> tuple[ModuleType, ModuleType, Mapping[str, Any]]:
    cross = source["v3_cross_registry_binding"]
    checks = (
        (V3_REGISTRY_PATH, "expected_v3_registry_source_sha256"),
        (V3_SCHEMA_PATH, "expected_v3_schema_sha256"),
        (V3_RESOLVER_PATH, "expected_v3_resolver_blob_sha256"),
    )
    for path, key in checks:
        blob = _blob(root, entries, path, executable=path == V3_RESOLVER_PATH)
        if _sha256(blob.content) != cross[key]:
            _reject("V3_STATIC_PIN_MISMATCH", path)
    v3_source = _strict_json(
        _blob(root, entries, V3_REGISTRY_PATH).content,
        f"{head_sha}:{V3_REGISTRY_PATH}",
    )
    resolver_blob = _blob(root, entries, V3_RESOLVER_PATH, executable=True)
    v3 = _fresh_module(
        root / V3_RESOLVER_PATH,
        resolver_blob.content,
        f"_t6_registry_v3_for_v4_{head_sha}",
    )
    try:
        v2, _ = v3._load_v2_resolver(root, entries, v3_source, head_sha)
    except Exception as exc:
        raise RegistryV4Error("V3_TOOLCHAIN_LOAD_FAILED", str(exc)) from exc
    return v3, v2, v3_source


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
    digest = canonical_digest_v4(
        {"schema_id": "t6_local_import_closure_v4", "files": files}
    )
    return files, digest


def _audit_pure_role(tree: ast.Module, path: str) -> None:
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots = {alias.name.split(".", 1)[0] for alias in node.names}
            forbidden = roots & PURE_ROLE_FORBIDDEN_IMPORTS
            if forbidden:
                _reject("PURE_ROLE_FORBIDDEN_IMPORT", f"{path}:{sorted(forbidden)}")
            unknown = roots - PURE_ROLE_ALLOWED_IMPORT_ROOTS
            if unknown:
                _reject("PURE_ROLE_FORBIDDEN_IMPORT", f"{path}:{sorted(unknown)}")
        elif isinstance(node, ast.ImportFrom) and node.module:
            root = node.module.split(".", 1)[0]
            if root in PURE_ROLE_FORBIDDEN_IMPORTS:
                _reject("PURE_ROLE_FORBIDDEN_IMPORT", f"{path}:{root}")
            if root not in PURE_ROLE_ALLOWED_IMPORT_ROOTS:
                _reject("PURE_ROLE_FORBIDDEN_IMPORT", f"{path}:{root}")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in {
                "__import__",
                "compile",
                "eval",
                "exec",
                "globals",
                "locals",
                "open",
                "vars",
            }:
                _reject("PURE_ROLE_DYNAMIC_EXECUTION", f"{path}:{node.func.id}")
        elif isinstance(node, ast.Name) and node.id == "__builtins__":
            _reject("PURE_ROLE_DYNAMIC_EXECUTION", f"{path}:__builtins__")


def _audit_controlled_loader_contract(
    *,
    artifact_id: str,
    path: str,
    tree: ast.Module,
    content: bytes,
    blob_sha256: str,
    manifest: Mapping[str, Any],
    identities: Mapping[str, tuple[str, str, str, str, tuple[str, ...]]],
    v2: ModuleType,
) -> dict[str, Any]:
    contract = CONTROLLED_LOADER_CONTRACTS[artifact_id]
    loader_symbol = contract["loader_symbol"]
    caller_symbol = contract["caller_symbol"]
    observed_ast: dict[str, str] = {}
    for symbol, expected_digest in (
        (loader_symbol, contract["loader_symbol_ast_sha256"]),
        (caller_symbol, contract["caller_symbol_ast_sha256"]),
    ):
        digest = _symbol_receipt_v4(
            path, symbol, content, blob_sha256, v2
        )["symbol_ast_sha256"]
        if digest != expected_digest:
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

    declared_execution = set(manifest["execution_artifact_ids"])
    direct_artifact_ids = set(contract["direct_loader_artifacts"].values())
    transitive_ids = set(contract["transitive_execution_artifact_ids"])
    if declared_execution != direct_artifact_ids | transitive_ids:
        _reject("CONTROLLED_EXECUTION_MANIFEST_MISMATCH", artifact_id)
    for name, dependency_id in contract["direct_loader_artifacts"].items():
        if contract["path_constants"][name] != identities[dependency_id][3]:
            _reject("CONTROLLED_EXECUTION_MANIFEST_MISMATCH", f"{artifact_id}:{name}")
    if set(contract["direct_loader_toolchain_paths"].values()) != {RESOLVER_PATH}:
        _reject("CONTROLLED_EXECUTION_TOOLCHAIN_MISMATCH", artifact_id)

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
        if (
            isinstance(node, ast.Attribute)
            and isinstance(node.value, ast.Name)
            and node.value.id == "sys"
            and node.attr == "modules"
            and owners.get(id(node)) != loader_symbol
        ):
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
    position = contract["path_position"]
    for call in helper_calls:
        if len(call.args) <= position or type(call.args[position]) is not ast.Name:
            _reject("CONTROLLED_LOADER_CALL_SHAPE", f"{path}:{loader_symbol}")
        observed_path_names.append(call.args[position].id)
    expected_direct_names = sorted(
        set(contract["direct_loader_artifacts"])
        | set(contract["direct_loader_toolchain_paths"])
    )
    if sorted(observed_path_names) != expected_direct_names:
        _reject(
            "CONTROLLED_LOADER_CALL_SET_MISMATCH",
            f"{path}:{sorted(observed_path_names)}",
        )
    return {
        "loader_symbol": loader_symbol,
        "loader_symbol_ast_sha256": observed_ast[loader_symbol],
        "caller_symbol": caller_symbol,
        "caller_symbol_ast_sha256": observed_ast[caller_symbol],
        "direct_loader_path_constants": expected_direct_names,
        "transitive_execution_artifact_ids": list(
            contract["transitive_execution_artifact_ids"]
        ),
        "status": "FIXED_LOADER_CALL_TABLE_MATCHES_V4_DEPENDENCY_DAG",
    }


def _dependency_manifest(source: Mapping[str, Any]) -> tuple[dict[str, Any], str]:
    manifest = _json_copy(source["dependency_manifest"])
    digest = canonical_digest_v4(
        {"schema_id": "t6_artifact_dependency_manifest_v4", **manifest}
    )
    if digest != source["expected_dependency_manifest_digest"]:
        _reject("DEPENDENCY_MANIFEST_PIN_MISMATCH", source["artifact_id"])
    return manifest, digest


def _prevalidate_dependency_graph(sources: Sequence[Mapping[str, Any]]) -> None:
    identities = {item[0] for item in ARTIFACT_IDENTITIES}
    source_ids = [item["artifact_id"] for item in sources]
    if set(source_ids) != identities or len(source_ids) != len(set(source_ids)):
        _reject("FIXED_ARTIFACT_MISMATCH", "artifact set changed")
    manifests = {item["artifact_id"]: item["dependency_manifest"] for item in sources}
    for artifact_id, manifest in manifests.items():
        expected = DEPENDENCIES[artifact_id]
        if (
            tuple(manifest["execution_artifact_ids"]) != expected[0]
            or tuple(manifest["binding_artifact_ids"]) != expected[1]
            or tuple(manifest["binding_document_ids"]) != expected[2]
        ):
            _reject("DEPENDENCY_POLICY_MISMATCH", artifact_id)
        dependency_ids = set(expected[0]) | set(expected[1])
        if set(manifest["artifact_semantic_pins"]) != dependency_ids:
            _reject("DEPENDENCY_SEMANTIC_PIN_SET_MISMATCH", artifact_id)
        if not dependency_ids <= identities:
            _reject("UNKNOWN_DEPENDENCY", artifact_id)

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
            visit(child)
        visiting.remove(artifact_id)
        visited.add(artifact_id)

    for artifact_id in sorted(manifests):
        visit(artifact_id)


def _activation_gate(source: Mapping[str, Any]) -> None:
    artifact_statuses = {item["pin_status"] for item in source["artifacts"]}
    document_statuses = {item["pin_status"] for item in source["pinned_documents"]}
    has_placeholder = "PLACEHOLDER_UNRESOLVED" in artifact_statuses | document_statuses
    if source["activation_status"] == PENDING:
        if not has_placeholder:
            _reject("ACTIVATION_STATUS_MISMATCH", "pending registry has no placeholder")
        _reject("REGISTRY_NOT_ACTIVE", "tracked V4 artifact pins are still placeholders")
    if source["activation_status"] != ACTIVE or has_placeholder:
        _reject("ACTIVATION_STATUS_MISMATCH", "active registry contains placeholders")
    if any(
        item[key] == ZERO_SHA256
        for item in source["artifacts"]
        for key in (
            "expected_blob_sha256",
            "expected_symbol_set_digest",
            "expected_local_import_closure_digest",
            "expected_dependency_manifest_digest",
            "expected_semantic_sha256",
        )
    ):
        _reject("ZERO_AUTHORITY_PIN", "active artifact has a zero pin")


def _resolve_artifacts(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    sources: Sequence[Mapping[str, Any]],
    v2: ModuleType,
) -> list[dict[str, Any]]:
    identities = {item[0]: item for item in ARTIFACT_IDENTITIES}
    if [item["artifact_id"] for item in sources] != sorted(identities):
        _reject("FIXED_ARTIFACT_MISMATCH", "artifact order changed")
    resolved: list[dict[str, Any]] = []
    for source in sources:
        artifact_id = source["artifact_id"]
        expected = identities[artifact_id]
        if (
            source["artifact_class"] != expected[1]
            or source["kind"] != expected[2]
            or source["path"] != expected[3]
            or tuple(source["symbols"]) != expected[4]
            or source["pin_status"] != "PINNED"
            or source["semantic_digest_method"] != SEMANTIC_DIGEST_METHOD
        ):
            _reject("FIXED_ARTIFACT_MISMATCH", artifact_id)
        path = expected[3]
        blob = _blob(root, entries, path, executable=True)
        blob_sha256 = _sha256(blob.content)
        try:
            tree = ast.parse(blob.content.decode("utf-8"), filename=path)
        except (UnicodeDecodeError, SyntaxError) as exc:
            raise RegistryV4Error("PYTHON_PARSE_ERROR", f"{path}: {exc}") from exc
        if artifact_id in {OWNER_ARTIFACT_ID, VALIDATOR_ARTIFACT_ID, CONSUMER_ARTIFACT_ID}:
            _audit_pure_role(tree, path)
        symbol_receipts: dict[str, dict[str, str]] = {}
        for symbol in expected[4]:
            try:
                receipt = _symbol_receipt_v4(
                    path, symbol, blob.content, blob_sha256, v2
                )
            except Exception as exc:
                code = getattr(exc, "code", "SYMBOL_AUDIT_FAILED")
                raise RegistryV4Error(code, f"{path}:{symbol}: {exc}") from exc
            symbol_receipts[symbol] = {
                "symbol_ast_sha256": receipt["symbol_ast_sha256"]
            }
        symbol_set_digest = canonical_digest_v4(
            {"schema_id": "t6_python_symbol_set_v4", "symbols": symbol_receipts}
        )
        closure_files, closure_digest = _static_local_closure(root, entries, path)
        manifest, dependency_digest = _dependency_manifest(source)
        controlled_loader_receipt = None
        if artifact_id in CONTROLLED_LOADER_CONTRACTS:
            controlled_loader_receipt = _audit_controlled_loader_contract(
                artifact_id=artifact_id,
                path=path,
                tree=tree,
                content=blob.content,
                blob_sha256=blob_sha256,
                manifest=manifest,
                identities=identities,
                v2=v2,
            )
        local_imports = {
            item["path"] for item in closure_files if item["path"] != path
        }
        allowed_imports = {
            identities[dependency_id][3]
            for dependency_id in manifest["execution_artifact_ids"]
        }
        if not local_imports <= allowed_imports:
            _reject(
                "UNDECLARED_LOCAL_IMPORT",
                f"{artifact_id}:{sorted(local_imports - allowed_imports)}",
            )
        if artifact_id in {OWNER_ARTIFACT_ID, VALIDATOR_ARTIFACT_ID, CONSUMER_ARTIFACT_ID} and local_imports:
            _reject("PURE_ROLE_LOCAL_IMPORT", f"{artifact_id}:{sorted(local_imports)}")
        semantic = canonical_digest_v4(
            {
                "method": SEMANTIC_DIGEST_METHOD,
                "path": path,
                "blob_sha256": blob_sha256,
                "symbol_set_digest": symbol_set_digest,
                "local_import_closure_digest": closure_digest,
                "dependency_manifest_digest": dependency_digest,
                "python_ast_contract_digest": _python_ast_contract_digest_v4(),
            }
        )
        observed_pins = {
            "expected_blob_sha256": blob_sha256,
            "expected_symbol_set_digest": symbol_set_digest,
            "expected_local_import_closure_digest": closure_digest,
            "expected_dependency_manifest_digest": dependency_digest,
            "expected_semantic_sha256": semantic,
        }
        if source["expected_symbol_ast_sha256"] != {
            name: value["symbol_ast_sha256"]
            for name, value in symbol_receipts.items()
        }:
            _reject("ARTIFACT_PIN_MISMATCH", f"{artifact_id}:symbol AST")
        for key, observed in observed_pins.items():
            if source[key] != observed:
                _reject("ARTIFACT_PIN_MISMATCH", f"{artifact_id}:{key}")
        resolved.append(
            {
                **_json_copy(source),
                "git_mode": blob.mode,
                "git_object_id": blob.object_id,
                "blob_sha256": blob_sha256,
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
    artifacts = {item["artifact_id"]: item for item in resolved}
    for artifact_id, artifact in artifacts.items():
        for dependency_id, expected_semantic in artifact["dependency_manifest"][
            "artifact_semantic_pins"
        ].items():
            if artifacts[dependency_id]["semantic_sha256"] != expected_semantic:
                _reject(
                    "DEPENDENCY_SEMANTIC_PIN_MISMATCH",
                    f"{artifact_id}:{dependency_id}",
                )
    role_artifacts = [artifacts[item[2]] for item in ROLE_BINDINGS]
    if len({item["path"] for item in role_artifacts}) != 3:
        _reject("ROLE_PATH_COLLISION", "three roles need distinct modules")
    if len({item["blob_sha256"] for item in role_artifacts}) != 3:
        _reject("ROLE_BLOB_COLLISION", "three roles need distinct blobs")
    if len({item["semantic_sha256"] for item in role_artifacts}) != 3:
        _reject("ROLE_SEMANTIC_COLLISION", "three roles need distinct semantics")
    if set(CONTROLLED_LOADER_CONTRACTS) != {
        ORCHESTRATOR_ARTIFACT_ID,
        REPLAYER_ARTIFACT_ID,
    }:
        _reject("CONTROLLED_LOADER_CONTRACT_MISSING", "V4 non-role loaders")
    return resolved


def _resolve_grants(
    sources: Sequence[Mapping[str, Any]],
    artifacts: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    bindings = {item[0]: item for item in ROLE_BINDINGS}
    source_ids = [item["grant_id"] for item in sources]
    if set(source_ids) != set(bindings) or len(source_ids) != len(set(source_ids)):
        _reject("FIXED_GRANT_MISMATCH", "grant set changed")
    resolved: list[dict[str, Any]] = []
    for source in sources:
        grant_id = source["grant_id"]
        expected = bindings[grant_id]
        artifact = artifacts.get(expected[2])
        if (
            source["role"] != expected[1]
            or source["artifact_id"] != expected[2]
            or tuple(source["capabilities"]) != expected[3]
            or source["authority_class"] != ROLE_AUTHORITY_CLASS
            or artifact is None
        ):
            _reject("FIXED_GRANT_MISMATCH", grant_id)
        if (
            source["expected_artifact_semantic_sha256"]
            != artifact["semantic_sha256"]
            or source["expected_dependency_manifest_digest"]
            != artifact["dependency_manifest_digest"]
        ):
            _reject("GRANT_PIN_MISMATCH", grant_id)
        wire = {
            "grant_id": grant_id,
            "role": expected[1],
            "artifact_id": expected[2],
            "artifact_path": artifact["path"],
            "artifact_symbols": artifact["symbols"],
            "capabilities": source["capabilities"],
            "authority_class": ROLE_AUTHORITY_CLASS,
            "artifact_semantic_sha256": artifact["semantic_sha256"],
        }
        resolved.append(
            {
                **_json_copy(source),
                "grant_wire": wire,
                "role_grant_digest": canonical_digest_v4(wire),
                "artifact_dependency_manifest_digest": artifact[
                    "dependency_manifest_digest"
                ],
            }
        )
    return sorted(resolved, key=lambda item: item["grant_id"])


def _resolve_v3_cross(
    root: Path,
    head_sha: str,
    source: Mapping[str, Any],
    v3: ModuleType,
    artifacts: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    try:
        resolved = v3.resolve_registry_v3(root=root, requested_head=head_sha)
    except Exception as exc:
        raise RegistryV4Error("V3_CROSS_RESOLUTION_FAILED", str(exc)) from exc
    cross = source["v3_cross_registry_binding"]
    if resolved.get("status") != V3_STATUS or resolved.get("head_sha") != head_sha:
        _reject("V3_CROSS_STATUS_MISMATCH", repr(resolved.get("status")))
    if (
        resolved.get("active_role_grant_count") != 4
        or resolved.get("authorized_branches") != []
        or resolved.get("authority_denials")
        != {
            "e1_authority": False,
            "queue_authority": False,
            "producer_authority": False,
            "t5_authority": False,
            "branch_authority": False,
        }
    ):
        _reject("V3_CROSS_AUTHORITY_MISMATCH", "V3 frozen boundary changed")
    grants = {item["role"]: item for item in resolved["resolved_role_grants"]}
    if set(grants) != set(cross["required_v3_roles"]):
        _reject("V3_CROSS_ROLE_MISMATCH", repr(sorted(grants)))
    v3_artifacts = {
        item["artifact_id"]: item for item in resolved["resolved_artifacts"]
    }
    if (
        v3_artifacts["q1_terminal_issuer_v1"]["semantic_sha256"]
        != cross["expected_v3_terminal_issuer_semantic_sha256"]
        or v3_artifacts["q1_production_terminal_receipt_verifier_v1"][
            "semantic_sha256"
        ]
        != cross["expected_v3_production_verifier_semantic_sha256"]
        or artifacts[V3_PRODUCTION_VERIFIER_ARTIFACT_ID]["blob_sha256"]
        != v3_artifacts["q1_production_terminal_receipt_verifier_v1"][
            "blob_sha256"
        ]
        or artifacts[V3_PRODUCTION_VERIFIER_ARTIFACT_ID].get(
            "expected_v3_semantic_sha256"
        )
        != cross["expected_v3_production_verifier_semantic_sha256"]
        or artifacts[V3_RESOLVER_ARTIFACT_ID]["blob_sha256"]
        != cross["expected_v3_resolver_blob_sha256"]
        or artifacts[V3_ROOT_INITIALIZER_ARTIFACT_ID]["blob_sha256"]
        != v3_artifacts["q1_root_initializer_envelope_v2"]["blob_sha256"]
        or artifacts[V3_ROOT_INITIALIZER_ARTIFACT_ID].get(
            "expected_v3_semantic_sha256"
        )
        != cross["expected_v3_initializer_semantic_sha256"]
        or cross["expected_v3_initializer_semantic_sha256"]
        != v3_artifacts["q1_root_initializer_envelope_v2"]["semantic_sha256"]
    ):
        _reject("V3_CROSS_ARTIFACT_MISMATCH", "issuer/verifier pin changed")
    return {
        "v3_registry_id": V3_REGISTRY_ID,
        "v3_head_sha": resolved["head_sha"],
        "v3_registry_digest": resolved["registry_digest"],
        "v3_role_manifest_digest": resolved["role_authority_manifest"]["digest"],
        "v3_role_subdigests": {
            role: resolved["role_subdigests"][role]
            for role in cross["required_v3_roles"]
        },
        "v3_terminal_issuer_semantic_sha256": v3_artifacts[
            "q1_terminal_issuer_v1"
        ]["semantic_sha256"],
        "v3_production_verifier_semantic_sha256": v3_artifacts[
            "q1_production_terminal_receipt_verifier_v1"
        ]["semantic_sha256"],
        "v3_initializer_semantic_sha256": v3_artifacts[
            "q1_root_initializer_envelope_v2"
        ]["semantic_sha256"],
        "same_head_required": True,
        "cross_head_receipts_allowed": False,
    }


def resolve_registry_v4(*, root: Path, requested_head: str) -> dict[str, Any]:
    repository = _repository_root(root)
    head_sha, tree_sha, object_format = _exact_head(repository, requested_head)
    entries = _tree_entries(repository, head_sha)
    initial_toolchain = _toolchain_binding(repository, entries, head_sha)
    registry_blob = _blob(repository, entries, REGISTRY_PATH)
    schema_blob = _blob(repository, entries, SCHEMA_PATH)
    source = _strict_json(registry_blob.content, f"{head_sha}:{REGISTRY_PATH}")
    schema = _strict_json(schema_blob.content, f"{head_sha}:{SCHEMA_PATH}")
    try:
        jsonschema.Draft202012Validator.check_schema(schema)
    except jsonschema.exceptions.SchemaError as exc:
        raise RegistryV4Error("REGISTRY_SCHEMA_INVALID", exc.message) from exc
    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(source))
    if errors:
        _reject("SOURCE_SCHEMA_INVALID", errors[0].message)
    if (
        source["schema_id"] != SCHEMA_ID
        or source["registry_id"] != SCHEMA_ID
        or source["schema_version"] != SCHEMA_VERSION
        or source["status"] != STATUS
        or source["authority_policy"] != AUTHORITY_POLICY
        or source["authorized_consumer_scopes"] != [CONSUMER_SCOPE]
        or source["receipt_authority_matrix"] != RECEIPT_AUTHORITY_MATRIX
        or source["orchestration_policy"] != ORCHESTRATION_POLICY
        or source["post_issuance_replay_policy"] != POST_REPLAY_POLICY
        or source["authority_denials"] != AUTHORITY_DENIALS
        or source["authorized_branches"] != []
    ):
        _reject("FIXED_REGISTRY_MISMATCH", "identity or authority policy changed")
    _prevalidate_dependency_graph(source["artifacts"])
    v3, v2, _ = _load_v3(repository, entries, source, head_sha)
    _activation_gate(source)
    artifacts_list = _resolve_artifacts(
        repository, entries, source["artifacts"], v2
    )
    artifacts = {item["artifact_id"]: item for item in artifacts_list}
    grants = _resolve_grants(source["role_grants"], artifacts)
    v3_cross = _resolve_v3_cross(
        repository, head_sha, source, v3, artifacts
    )
    documents: list[dict[str, Any]] = []
    for document in source["pinned_documents"]:
        if document["pin_status"] != "PINNED":
            _reject("DOCUMENT_NOT_PINNED", document["document_id"])
        blob = _blob(repository, entries, document["path"])
        parsed = _strict_json(blob.content, document["path"])
        try:
            jsonschema.Draft202012Validator.check_schema(parsed)
        except jsonschema.exceptions.SchemaError as exc:
            raise RegistryV4Error("PINNED_DOCUMENT_SCHEMA_INVALID", exc.message) from exc
        canonical = canonical_digest_v4(parsed)
        if (
            _sha256(blob.content) != document["expected_blob_sha256"]
            or canonical != document["expected_canonical_sha256"]
            or parsed.get("$id") != document["expected_json_schema_id"]
        ):
            _reject("DOCUMENT_PIN_MISMATCH", document["document_id"])
        documents.append(
            {
                **_json_copy(document),
                "git_mode": blob.mode,
                "git_object_id": blob.object_id,
                "blob_sha256": _sha256(blob.content),
                "canonical_sha256": canonical,
            }
        )
    grants_by_role = {item["role"]: item for item in grants}
    role_subdigests = {
        role: canonical_digest_v4(
            {
                "schema_id": "t6_role_subregistry_v4",
                "head_sha": head_sha,
                "role": role,
                "grant": grants_by_role[role],
            }
        )
        for role in ALLOWED_ROLES
    }
    manifest: dict[str, Any] = {
        "schema_id": "t6_q1_root_prefix_scoped_e1_role_manifest_v4",
        "head_sha": head_sha,
        "status": STATUS,
        "inherited_v3_role_manifest_digest": v3_cross[
            "v3_role_manifest_digest"
        ],
        "new_grants": grants,
        "authorized_consumer_scopes": [CONSUMER_SCOPE],
        "receipt_authority_matrix": RECEIPT_AUTHORITY_MATRIX,
        "authority_denials": AUTHORITY_DENIALS,
    }
    manifest["digest"] = canonical_digest_v4(manifest)
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
        "authorized_consumer_scopes": [CONSUMER_SCOPE],
        "receipt_authority_matrix": RECEIPT_AUTHORITY_MATRIX,
        "orchestration_policy": ORCHESTRATION_POLICY,
        "post_issuance_replay_policy": POST_REPLAY_POLICY,
        "pinned_documents": documents,
        "v3_cross_registry_binding": v3_cross,
        "authorized_branches": [],
        "role_authority_manifest": manifest,
        "role_subdigests": role_subdigests,
        "new_role_grant_counts": {role: 1 for role in ALLOWED_ROLES},
        "new_role_grant_count": 3,
        "inherited_v3_role_grant_count": 4,
        "effective_role_capability_count": 7,
        "common_root_owner_classifier_count": 1,
        "scope_aware_e1_validator_count": 1,
        "registered_prefix_e1_consumer_count": 1,
        "new_terminal_issuer_count": 0,
        "producer_count": 0,
        "queue_mutator_count": 0,
        "authority_denials": AUTHORITY_DENIALS,
        "status": STATUS,
        "proof_boundary": source["proof_boundary"],
    }
    payload["registry_digest"] = canonical_digest_v4(payload)
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
        payload = resolve_registry_v4(root=args.root, requested_head=args.head)
        encoded = canonical_json_bytes_v4(payload) + b"\n"
        if args.output is None:
            sys.stdout.buffer.write(encoded)
        else:
            args.output.write_bytes(encoded)
    except RegistryV4Error as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
