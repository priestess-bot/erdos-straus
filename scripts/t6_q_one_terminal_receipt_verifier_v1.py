#!/usr/bin/env python3
"""Independent exact-HEAD replay for production q=1 terminal receipts.

This module deliberately does not import or execute the terminal issuer,
scheduler, or coverage verifier.  It fresh-executes the exact-HEAD V2/V3
registry resolvers, root envelope, and terminal-decision assembler; rebuilds
the actual root source and assembler decision from raw integers; reconstructs
the issuer's expected actualness and production receipt wire; and requires a
caller-supplied plain JSON receipt to be byte-identical canonical JSON.
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

import jsonschema


SCHEMA_VERSION = 1
VERIFIER_PATH = "scripts/t6_q_one_terminal_receipt_verifier_v1.py"
ISSUER_PATH = "scripts/t6_q_one_terminal_issuer_v1.py"
V2_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v2.py"
V3_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v3.py"
V3_REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v3.json"
V3_SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v3.schema.json"
ROOT_ENVELOPE_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"
ASSEMBLER_PATH = "scripts/t6_q_one_terminal_decision_assembler_v2.py"
SCHEMA_PATH = "schemas/t6-q-one-production-terminal-receipts-v1.schema.json"

V2_ID = "t6_coordinator_role_registry_v2"
V3_ID = "t6_coordinator_role_registry_v3"
V2_STATUS = "HEAD_BOUND_PREFIX_SCHEDULE_AUTHORITY_NO_ISSUER"
V3_STATUS = "HEAD_BOUND_Q1_ROOT_TERMINAL_DECISION_AUTHORITY_NO_RECURSION"
SCHEDULE_ID = "q1_root_gap_3_7_11_registered_priority_prefix_v1"
INITIALIZER_ID = "q1_root_initializer_envelope_v2"
ASSEMBLER_ID = "q1_terminal_decision_assembler_v2"
ISSUER_ID = "q1_terminal_issuer_v1"
SCHEDULER_ID = "q1_priority_prefix_scheduler_v1"
COVERAGE_ID = "q1_priority_prefix_coverage_verifier_v1"
V2_RESOLVER_ID = "v2_registry_resolver_dependency"
RECEIPT_VERIFIER_ID = "q1_production_terminal_receipt_verifier_v1"

INITIALIZER_GRANT = "q1_root_initializer_grant_v3"
ISSUER_GRANT = "q1_terminal_issuer_grant_v3"
SCHEDULER_GRANT = "q1_prefix_terminal_scheduler_grant_v3"
COVERAGE_GRANT = "q1_prefix_independent_coverage_verifier_grant_v3"

ACTUALNESS_TYPE = "QOneRootSourceActualnessReceiptV1"
HIT_TYPE = "ProductionQOneRootTerminalReceiptV1"
MISS_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
HIT_OUTCOME = "ROOT_TERMINAL_HIT"
MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"
ASSEMBLER_HIT = "ROOT_TERMINAL_HIT_EVIDENCE"
ASSEMBLER_MISS = "PREFIX_MISS_EVIDENCE"
ROOT_OUTCOME = "ROOT_CERTIFICATE_LEFT_INJECTION"

BODY_PREFIX = "q1-source-body:"
ANCHOR_PREFIX = "root-init-anchor:"
STATE_PREFIX = "state:"
ROOT_PROBLEM_PREFIX = "q1-root-problem:"
ACTUALNESS_PREFIX = "q1-root-source-actualness:"
HIT_RECEIPT_PREFIX = "production-q1-root-terminal:"
MISS_RECEIPT_PREFIX = "production-q1-prefix-miss:"

REGULAR_MODES = frozenset({"100644", "100755"})
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
_OID = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")


class ProductionReceiptReplayRejectCode(str, Enum):
    HEAD_ERROR = "HEAD_ERROR"
    WORKTREE_ERROR = "WORKTREE_ERROR"
    MODULE_ERROR = "MODULE_ERROR"
    REGISTRY_ERROR = "REGISTRY_ERROR"
    SCHEMA_ERROR = "SCHEMA_ERROR"
    RECEIPT_TYPE_ERROR = "RECEIPT_TYPE_ERROR"
    RECEIPT_SEAL_ERROR = "RECEIPT_SEAL_ERROR"
    SOURCE_MISMATCH = "SOURCE_MISMATCH"
    DECISION_MISMATCH = "DECISION_MISMATCH"
    AUTHORITY_MISMATCH = "AUTHORITY_MISMATCH"
    WIRE_MISMATCH = "WIRE_MISMATCH"


class ProductionReceiptReplayError(ValueError):
    def __init__(self, code: ProductionReceiptReplayRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: ProductionReceiptReplayRejectCode, detail: str) -> NoReturn:
    raise ProductionReceiptReplayError(code, detail)


def _json_copy(value: Any, path: str = "$") -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(ProductionReceiptReplayRejectCode.RECEIPT_TYPE_ERROR, f"{path} key")
            result[key] = _json_copy(child, f"{path}.{key}")
        return result
    if type(value) is list:
        return [_json_copy(child, f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(
        ProductionReceiptReplayRejectCode.RECEIPT_TYPE_ERROR,
        f"{path} contains {type(value).__name__}",
    )


def canonical_json_v1(value: Any) -> str:
    return json.dumps(
        _json_copy(value), ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False
    )


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


def _run_git(root: Path, args: Sequence[str]) -> bytes:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(["git", *args], cwd=root, capture_output=True, check=False, env=environment)
    if completed.returncode:
        _reject(ProductionReceiptReplayRejectCode.HEAD_ERROR, completed.stderr.decode(errors="replace"))
    return completed.stdout


def _repo(locator: Path) -> Path:
    if type(locator) is not type(Path()):
        _reject(
            ProductionReceiptReplayRejectCode.HEAD_ERROR,
            "root must be the exact platform Path type",
        )
    return Path(_run_git(locator.resolve(), ("rev-parse", "--show-toplevel")).decode().strip()).resolve()


def _head(root: Path, requested: str) -> tuple[str, str]:
    fmt = _run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    length = 40 if fmt == "sha1" else 64 if fmt == "sha256" else 0
    if type(requested) is not str or len(requested) != length or not _OID.fullmatch(requested):
        _reject(ProductionReceiptReplayRejectCode.HEAD_ERROR, "head must be exact full lowercase OID")
    if _run_git(root, ("cat-file", "-t", requested)).decode().strip() != "commit":
        _reject(ProductionReceiptReplayRejectCode.HEAD_ERROR, "head is not commit")
    tree = _run_git(root, ("rev-parse", f"{requested}^{{tree}}")).decode().strip()
    return requested, tree


def _entries(root: Path, head: str) -> dict[str, tuple[str, str, str]]:
    raw = _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head))
    result: dict[str, tuple[str, str, str]] = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, encoded = record.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split(" ")
        path = encoded.decode()
        pure = PurePosixPath(path)
        if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
            _reject(ProductionReceiptReplayRejectCode.HEAD_ERROR, path)
        result[path] = (mode, kind, oid)
    return result


def _blob(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str) -> tuple[bytes, str, str]:
    item = entries.get(path)
    if item is None or item[0] not in REGULAR_MODES or item[1] != "blob":
        _reject(ProductionReceiptReplayRejectCode.MODULE_ERROR, f"missing regular {path}")
    content = _run_git(root, ("cat-file", "blob", item[2]))
    worktree = root / path
    if worktree.is_symlink() or not worktree.is_file() or worktree.read_bytes() != content:
        _reject(ProductionReceiptReplayRejectCode.WORKTREE_ERROR, path)
    return content, item[0], item[2]


def _fresh(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str, name: str) -> ModuleType:
    content, _mode, _oid = _blob(root, entries, path)
    module = ModuleType(name)
    module.__file__ = str((root / path).resolve())
    previous = sys.modules.get(name)
    sys.modules[name] = module
    try:
        exec(compile(content, module.__file__, "exec"), module.__dict__)
    finally:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous
    return module


def _verifier_self_binding(
    root: Path,
    head: str,
    tree: str,
    entries: Mapping[str, tuple[str, str, str]],
) -> dict[str, Any]:
    content, mode, oid = _blob(root, entries, VERIFIER_PATH)
    executing = Path(__file__)
    expected_path = (root / VERIFIER_PATH).resolve()
    if (
        executing.is_symlink()
        or not executing.is_file()
        or executing.resolve() != expected_path
        or executing.read_bytes() != content
    ):
        _reject(
            ProductionReceiptReplayRejectCode.MODULE_ERROR,
            "executing receipt verifier is not backed by requested HEAD",
        )
    payload = {
        "schema_id": "t6_q_one_terminal_receipt_verifier_self_binding_v1",
        "head_sha": head,
        "head_tree_sha": tree,
        "path": VERIFIER_PATH,
        "module_name": RECEIPT_VERIFIER_ID,
        "git_mode": mode,
        "git_object_id": oid,
        "blob_sha256": hashlib.sha256(content).hexdigest(),
        "status": "CURRENT_RECEIPT_VERIFIER_MATCHES_EXACT_HEAD_BLOB",
    }
    payload["digest"] = canonical_digest_v1(payload)
    return payload


def _call(module: ModuleType, symbol: str) -> Any:
    value = getattr(module, symbol, None)
    if not callable(value) or value.__name__ != symbol or value.__module__ != module.__name__:
        _reject(ProductionReceiptReplayRejectCode.MODULE_ERROR, f"{module.__name__}.{symbol}")
    return value


def _sealed(mapping: Mapping[str, Any], id_field: str, prefix: str) -> None:
    if type(mapping) is not dict or type(mapping.get("digest")) is not str:
        _reject(ProductionReceiptReplayRejectCode.RECEIPT_SEAL_ERROR, "mapping/digest")
    digest = mapping["digest"]
    if not _DIGEST.fullmatch(digest) or mapping.get(id_field) != prefix + digest:
        _reject(ProductionReceiptReplayRejectCode.RECEIPT_SEAL_ERROR, id_field)
    unsigned = dict(mapping)
    unsigned.pop(id_field)
    unsigned.pop("digest")
    if canonical_digest_v1(unsigned) != digest:
        _reject(ProductionReceiptReplayRejectCode.RECEIPT_SEAL_ERROR, "digest")


def _grant_digest(grant: Mapping[str, Any]) -> str:
    return canonical_digest_v1(grant)


def _issuer_binding_digest(
    root: Path,
    head: str,
    tree: str,
    entries: Mapping[str, tuple[str, str, str]],
    modules: Mapping[str, ModuleType],
) -> str:
    paths = (ISSUER_PATH, V2_RESOLVER_PATH, V3_RESOLVER_PATH, ROOT_ENVELOPE_PATH, ASSEMBLER_PATH)
    symbols = {
        V2_RESOLVER_PATH: ("resolve_registry_v2",),
        V3_RESOLVER_PATH: ("resolve_registry_v3",),
        ROOT_ENVELOPE_PATH: (
            "artifact_to_mapping_v2", "make_canonical_q_one_g_source_body_v2",
            "make_raw_root_source_state_v2", "make_root_initializer_anchor_v2",
        ),
        ASSEMBLER_PATH: ("assemble_q_one_terminal_decision_v2", "terminal_decision_to_mapping_v2"),
    }
    files: list[dict[str, Any]] = []
    for path in paths:
        content, mode, oid = _blob(root, entries, path)
        if path == ISSUER_PATH:
            entry = {
                "schema_id": "t6_q_one_terminal_issuer_self_binding_v1",
                "head_sha": head,
                "head_tree_sha": tree,
                "path": path,
                "module_name": ISSUER_ID,
                "git_mode": mode,
                "git_object_id": oid,
                "blob_sha256": hashlib.sha256(content).hexdigest(),
                "status": "CURRENT_ISSUER_MATCHES_EXACT_HEAD_BLOB",
            }
            entry["digest"] = canonical_digest_v1(entry)
            files.append(entry)
            continue
        module = modules[path]
        callable_ids = []
        for symbol in symbols[path]:
            value = _call(module, symbol)
            callable_ids.append(
                {
                    "symbol": symbol,
                    "callable_name": value.__name__,
                    "callable_module": value.__module__,
                    "callable_qualname": getattr(value, "__qualname__", value.__name__),
                }
            )
        files.append(
            {
                "path": path,
                "module_name": module.__name__,
                "git_mode": mode,
                "git_object_id": oid,
                "blob_sha256": hashlib.sha256(content).hexdigest(),
                "execution_mode": "FRESH_COMPILE_EXEC_FROM_EXACT_HEAD_BLOB",
                "callable_identities": callable_ids,
            }
        )
    payload = {
        "schema_id": "t6_q_one_terminal_issuer_module_binding_v1",
        "head_sha": head,
        "head_tree_sha": tree,
        "files": files,
        "forbidden_direct_modules": ["coverage verifier", "post-issuance receipt verifier", "terminal scheduler"],
        "status": "ONLY_V2_V3_INITIALIZER_ASSEMBLER_FRESH_EXECUTED",
    }
    payload["digest"] = canonical_digest_v1(payload)
    return payload["digest"]


def _root_material(raw: dict[str, Any], root_module: ModuleType) -> tuple[dict, dict, dict]:
    body_obj = _call(root_module, "make_canonical_q_one_g_source_body_v2")(raw)
    anchor_obj = _call(root_module, "make_root_initializer_anchor_v2")(body_obj)
    state_obj = _call(root_module, "make_raw_root_source_state_v2")(body_obj, anchor_obj)
    serializer = _call(root_module, "artifact_to_mapping_v2")
    return serializer(body_obj), serializer(anchor_obj), serializer(state_obj)


def _root_problem(raw: Mapping[str, Any]) -> tuple[dict, str, str]:
    p = raw["root_context"]
    payload = {
        "schema_id": "q1_canonical_root_problem_v1", "root_context": p,
        "equation_rank": raw["equation_rank"], "equation_numerator": raw["equation_numerator"],
        "equation_denominator": raw["equation_denominator"], "mark_kind_code": raw["mark_kind_code"],
        "mark_root_context": raw["mark_root_context"], "mark_equation_rank": raw["mark_equation_rank"],
    }
    digest = canonical_digest_v1(payload)
    return payload, ROOT_PROBLEM_PREFIX + digest, digest


def _branch(raw: Mapping[str, Any], raw_digest: str, problem_id: str, problem_digest: str,
            body: Mapping[str, Any], anchor: Mapping[str, Any], state: Mapping[str, Any]) -> tuple[dict, str]:
    payload = {
        "schema_id": "q1_deterministic_initial_g_branch_replay_v1",
        "root_problem_id": problem_id, "root_problem_digest": problem_digest,
        "raw_q_one_g_digest": raw_digest, "q": 1, "endpoint_fiber_code": 2,
        "major_phase_code": 3, "provenance_code": 1, "mark_kind_code": 1,
        "gap_three_x": raw["gap_three_x"], "gap_three_factorization": raw["gap_three_factorization"],
        "body_id": body["body_id"], "body_digest": body["digest"],
        "anchor_id": anchor["anchor_id"], "anchor_digest": anchor["digest"],
        "state_id": state["state_id"], "state_digest": state["digest"],
        "state_authority": {"initializer_authority": False, "persistent_admission": False, "queue_authority": False},
    }
    return payload, canonical_digest_v1(payload)


def _cross(v2: Mapping[str, Any], v3: Mapping[str, Any], v2a: Mapping[str, Any], v3a: Mapping[str, Any]) -> str:
    cross = v3["v2_cross_registry_binding"]
    payload = {
        "schema_id": "t6_v2_v3_q1_terminal_authority_equivalence_v1",
        "head_sha": v3["head_sha"], "v2_registry_digest": v2["registry_digest"],
        "v2_role_manifest_digest": v2["role_authority_manifest"]["digest"],
        "v3_registry_digest": v3["registry_digest"],
        "v3_role_manifest_digest": v3["role_authority_manifest"]["digest"],
        "resolved_v2_cross_binding": cross,
    }
    for artifact_id in (SCHEDULER_ID, COVERAGE_ID):
        if not (
            cross[f"v2_{'scheduler' if artifact_id == SCHEDULER_ID else 'coverage_verifier'}_semantic_sha256"]
            == v2a[artifact_id]["semantic_sha256"]
            == v3a[artifact_id]["expected_v2_semantic_sha256"]
            and v3a[artifact_id]["semantic_sha256"] == v3a[artifact_id]["expected_v3_semantic_sha256"]
            and v2a[artifact_id]["path"] == v3a[artifact_id]["path"]
            and v2a[artifact_id]["blob_sha256"] == v3a[artifact_id]["blob_sha256"]
        ):
            _reject(ProductionReceiptReplayRejectCode.REGISTRY_ERROR, f"cross {artifact_id}")
    return canonical_digest_v1(payload)


@dataclass(frozen=True, slots=True)
class VerifiedProductionReceiptV1:
    status: str
    receipt_type: str
    receipt_id: str
    receipt_digest: str
    state_id: str
    outcome: str


def verify_q_one_production_terminal_receipt_v1(
    *, root: Path, requested_head: str, raw_q_one_g: dict[str, Any], receipt: object
) -> VerifiedProductionReceiptV1:
    """Rebuild and compare one production receipt without importing its issuer."""

    if type(receipt) is not dict:
        _reject(ProductionReceiptReplayRejectCode.RECEIPT_TYPE_ERROR, "receipt must be exact dict")
    supplied = _json_copy(receipt)
    repository = _repo(root)
    head, tree = _head(repository, requested_head)
    entries = _entries(repository, head)
    initial_self_binding = _verifier_self_binding(repository, head, tree, entries)
    schema_bytes, _mode, _oid = _blob(repository, entries, SCHEMA_PATH)
    schema = json.loads(schema_bytes)
    jsonschema.Draft202012Validator.check_schema(schema)
    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(supplied))
    if errors:
        _reject(ProductionReceiptReplayRejectCode.SCHEMA_ERROR, errors[0].message)
    receipt_type = supplied["receipt_type"]
    prefix = HIT_RECEIPT_PREFIX if receipt_type == HIT_TYPE else MISS_RECEIPT_PREFIX
    if receipt_type not in {HIT_TYPE, MISS_TYPE}:
        _reject(ProductionReceiptReplayRejectCode.RECEIPT_TYPE_ERROR, receipt_type)
    _sealed(supplied["root_actualness"], "actualness_id", ACTUALNESS_PREFIX)
    _sealed(supplied, "receipt_id", prefix)

    modules = {
        V2_RESOLVER_PATH: _fresh(repository, entries, V2_RESOLVER_PATH, f"_t6_issuer_exact_head_v2_registry_{head}"),
        V3_RESOLVER_PATH: _fresh(repository, entries, V3_RESOLVER_PATH, f"_t6_issuer_exact_head_v3_registry_{head}"),
        ROOT_ENVELOPE_PATH: _fresh(repository, entries, ROOT_ENVELOPE_PATH, f"_t6_issuer_exact_head_root_envelope_{head}"),
        ASSEMBLER_PATH: _fresh(repository, entries, ASSEMBLER_PATH, f"_t6_issuer_exact_head_assembler_{head}"),
    }
    v2 = _call(modules[V2_RESOLVER_PATH], "resolve_registry_v2")(root=repository, requested_head=head)
    v3 = _call(modules[V3_RESOLVER_PATH], "resolve_registry_v3")(root=repository, requested_head=head)
    if v2.get("status") != V2_STATUS or v3.get("status") != V3_STATUS:
        _reject(ProductionReceiptReplayRejectCode.REGISTRY_ERROR, "status")
    v2a = {item["artifact_id"]: item for item in v2["resolved_artifacts"]}
    v3a = {item["artifact_id"]: item for item in v3["resolved_artifacts"]}
    verifier_artifact = v3a.get(RECEIPT_VERIFIER_ID)
    if not (
        type(verifier_artifact) is dict
        and verifier_artifact.get("path") == VERIFIER_PATH
        and verifier_artifact.get("artifact_class")
        == "POST_ISSUANCE_REPLAY_DEPENDENCY_ONLY"
        and verifier_artifact.get("blob_sha256")
        == initial_self_binding["blob_sha256"]
        and verifier_artifact.get("git_mode") == initial_self_binding["git_mode"]
        and verifier_artifact.get("git_object_id")
        == initial_self_binding["git_object_id"]
        and verifier_artifact.get("expected_blob_sha256")
        == verifier_artifact.get("blob_sha256")
        and verifier_artifact.get("expected_semantic_sha256")
        == verifier_artifact.get("semantic_sha256")
    ):
        _reject(
            ProductionReceiptReplayRejectCode.REGISTRY_ERROR,
            "receipt verifier does not match its V3 post-issuance pin",
        )
    grants = {item["role"]: item for item in v3["resolved_role_grants"]}
    body, anchor, state = _root_material(raw_q_one_g, modules[ROOT_ENVELOPE_PATH])
    decision_obj = _call(modules[ASSEMBLER_PATH], "assemble_q_one_terminal_decision_v2")(
        root=repository, requested_head=head, raw_q_one_g=raw_q_one_g
    )
    decision = _call(modules[ASSEMBLER_PATH], "terminal_decision_to_mapping_v2")(decision_obj)
    expected_type = HIT_TYPE if decision["outcome"] == "ROOT_TERMINAL_HIT_EVIDENCE" else MISS_TYPE
    if receipt_type != expected_type:
        _reject(ProductionReceiptReplayRejectCode.DECISION_MISMATCH, "HIT/MISS swap")

    raw = _json_copy(raw_q_one_g)
    raw_digest = canonical_digest_v1(raw)
    problem, problem_id, problem_digest = _root_problem(raw)
    branch, branch_digest = _branch(raw, raw_digest, problem_id, problem_digest, body, anchor, state)
    binding_digest = _issuer_binding_digest(repository, head, tree, entries, modules)
    v3_artifacts = v3a
    initializer = grants["ROOT_INITIALIZER"]
    issuer = grants["TERMINAL_ISSUER"]
    expected_actual_unsigned = {
        "receipt_type": ACTUALNESS_TYPE, "schema_version": 1,
        "head_sha": head, "head_tree_sha": tree, "v3_registry_id": V3_ID,
        "v3_registry_digest": v3["registry_digest"],
        "v3_role_manifest_digest": v3["role_authority_manifest"]["digest"],
        "initializer_grant_id": INITIALIZER_GRANT, "initializer_grant_digest": _grant_digest(initializer),
        "initializer_artifact_id": INITIALIZER_ID,
        "initializer_artifact_semantic_sha256": v3_artifacts[INITIALIZER_ID]["semantic_sha256"],
        "issuer_grant_id": ISSUER_GRANT, "issuer_grant_digest": _grant_digest(issuer),
        "issuer_artifact_id": ISSUER_ID, "issuer_artifact_semantic_sha256": v3_artifacts[ISSUER_ID]["semantic_sha256"],
        "fresh_module_binding_digest": binding_digest, "root_problem": problem,
        "root_problem_id": problem_id, "root_problem_digest": problem_digest,
        "raw_q_one_g": raw, "raw_q_one_g_digest": raw_digest,
        "deterministic_initial_branch_replay": branch,
        "deterministic_initial_branch_replay_digest": branch_digest,
        "body_id": body["body_id"], "body_digest": body["digest"],
        "anchor_id": anchor["anchor_id"], "anchor_digest": anchor["digest"],
        "state_id": state["state_id"], "state_digest": state["digest"],
        "initializer_id": anchor["initializer_id"], "initializer_contract_digest": anchor["contract_digest"],
        "domain_replay_id": anchor["domain_replay_id"], "domain_replay_digest": anchor["domain_replay_digest"],
        "owner_domain_id": "ordinary_parentless_q1_g_root_v1", "occurrence_kind": "ROOT_INITIALIZER_OUTPUT",
        "parent_kind": "PARENTLESS_ROOT", "actualness_scope": "ROOT_OCCURRENCE_ONLY",
        "initializer_output_self_authorizing": False, "actualness_attestor_role": "TERMINAL_ISSUER",
        "source_actualness": True, "root_initializer_authority": True,
        "terminal_issuer_attestation_authority": True, "persistent_admission": False,
        "common_owner_authority": False, "e1_authority": False, "queue_authority": False,
    }
    actual_digest = canonical_digest_v1(expected_actual_unsigned)
    expected_actual = {
        **expected_actual_unsigned,
        "actualness_id": ACTUALNESS_PREFIX + actual_digest,
        "digest": actual_digest,
    }
    if supplied["root_actualness"] != expected_actual:
        differing = sorted(
            key
            for key in set(supplied["root_actualness"]) | set(expected_actual)
            if supplied["root_actualness"].get(key) != expected_actual.get(key)
        )
        _reject(
            ProductionReceiptReplayRejectCode.SOURCE_MISMATCH,
            f"actualness preimage differs at {differing}",
        )

    cross_digest = _cross(v2, v3, v2a, v3a)
    common = {
        "head_sha": head, "head_tree_sha": tree,
        "v2_registry_id": V2_ID, "v2_registry_digest": v2["registry_digest"],
        "v2_role_manifest_digest": v2["role_authority_manifest"]["digest"],
        "v3_registry_id": V3_ID, "v3_registry_digest": v3["registry_digest"],
        "v3_role_manifest_digest": v3["role_authority_manifest"]["digest"],
        "cross_registry_equivalence_digest": cross_digest,
        "initializer_grant_id": INITIALIZER_GRANT, "initializer_grant_digest": _grant_digest(initializer),
        "initializer_artifact_semantic_sha256": v3a[INITIALIZER_ID]["semantic_sha256"],
        "issuer_grant_id": ISSUER_GRANT, "issuer_grant_digest": _grant_digest(issuer),
        "issuer_artifact_semantic_sha256": v3a[ISSUER_ID]["semantic_sha256"],
        "scheduler_grant_id": SCHEDULER_GRANT, "scheduler_grant_digest": _grant_digest(grants["TERMINAL_SCHEDULER"]),
        "scheduler_artifact_semantic_sha256": v3a[SCHEDULER_ID]["semantic_sha256"],
        "coverage_verifier_grant_id": COVERAGE_GRANT,
        "coverage_verifier_grant_digest": _grant_digest(grants["INDEPENDENT_COVERAGE_VERIFIER"]),
        "coverage_verifier_artifact_semantic_sha256": v3a[COVERAGE_ID]["semantic_sha256"],
        "fresh_module_binding_digest": binding_digest, "root_actualness": expected_actual,
        "root_actualness_digest": actual_digest, "root_problem_id": problem_id,
        "root_problem_digest": problem_digest, "raw_q_one_g_digest": raw_digest,
        "deterministic_initial_branch_replay_digest": branch_digest,
        "body_id": body["body_id"], "body_digest": body["digest"],
        "anchor_id": anchor["anchor_id"], "anchor_digest": anchor["digest"],
        "state_id": state["state_id"], "state_digest": state["digest"], "subject_kind": "SOURCE_STATE",
        "root_context": decision["root_context"], "assembler_artifact_id": ASSEMBLER_ID,
        "assembler_artifact_semantic_sha256": v3a[ASSEMBLER_ID]["semantic_sha256"],
        "assembler_module_binding_digest": decision["module_binding_digest"],
        "assembler_decision_id": decision["decision_id"], "assembler_decision_digest": decision["digest"],
        "assembler_evidence_digest": decision["scheduler_evidence_digest"],
        "assembler_coverage_replay_digest": decision["coverage_replay_digest"],
        "schedule_id": decision["schedule_id"], "schedule_digest": decision["schedule_digest"],
        "source_actualness": True, "root_initializer_authority": True, "issuer_authority": True,
        "issued_under_terminal_issuer": True, "persistent_admission": False,
        "common_owner_authority": False, "e1_authority": False, "queue_authority": False,
        "producer_continuation_allowed": False,
    }
    if receipt_type == HIT_TYPE:
        cert = _json_copy(decision["selected_certificate"])
        equation = {
            "root_context": decision["root_context"], "equation_numerator": 4,
            "equation_denominator": decision["root_context"],
            "x": cert["x"], "y": cert["y"], "z": cert["z"],
        }
        branch_fields = {
            "outcome": HIT_OUTCOME, "root_outcome_kind": "ROOT_CERTIFICATE_LEFT_INJECTION",
            "selected_certificate": cert, "selected_certificate_digest": canonical_digest_v1(cert),
            "root_equation": equation, "root_equation_digest": canonical_digest_v1(equation),
            "global_exhaustion": False, "terminal_leaf_authority": True,
            "registered_prefix_miss_authority": False, "root_proof_close_authority": True,
        }
    else:
        branch_fields = {
            "outcome": MISS_OUTCOME, "coverage_semantics": "REGISTERED_PRIORITY_ONLY",
            "ordered_gaps": [3, 7, 11], "next_unchecked_gap": 15,
            "global_exhaustion": False, "selected_certificate": None,
            "selected_certificate_digest": None, "terminal_leaf_authority": False,
            "registered_prefix_miss_authority": True, "root_proof_close_authority": False,
        }
    unsigned = {"receipt_type": receipt_type, "schema_version": 1, **common, **branch_fields}
    digest = canonical_digest_v1(unsigned)
    expected = {
        **unsigned,
        "receipt_id": (HIT_RECEIPT_PREFIX if receipt_type == HIT_TYPE else MISS_RECEIPT_PREFIX) + digest,
        "digest": digest,
    }
    if canonical_json_v1(supplied) != canonical_json_v1(expected):
        _reject(ProductionReceiptReplayRejectCode.WIRE_MISMATCH, "receipt differs from fresh expected wire")
    if _verifier_self_binding(repository, head, tree, entries) != initial_self_binding:
        _reject(
            ProductionReceiptReplayRejectCode.WORKTREE_ERROR,
            "receipt verifier backing changed during replay",
        )
    return VerifiedProductionReceiptV1(
        status="PRODUCTION_Q1_TERMINAL_RECEIPT_VERIFIED",
        receipt_type=receipt_type,
        receipt_id=expected["receipt_id"],
        receipt_digest=digest,
        state_id=state["state_id"],
        outcome=expected["outcome"],
    )


__all__ = [
    "ProductionReceiptReplayError",
    "ProductionReceiptReplayRejectCode",
    "VerifiedProductionReceiptV1",
    "canonical_digest_v1",
    "canonical_json_v1",
    "verify_q_one_production_terminal_receipt_v1",
]
