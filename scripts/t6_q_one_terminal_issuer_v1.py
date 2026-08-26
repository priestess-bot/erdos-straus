#!/usr/bin/env python3
"""Production q=1 root terminal issuer with no recursive authority.

The issuer is intentionally a narrow post-assembly attestor.  It accepts only a
repository locator, an exact commit ID, and raw q=1 G integers.  It imports no
T6 module at module load time.  During issuance it executes exact-HEAD blobs for
the V2 and V3 registry resolvers, root-envelope module, and terminal-decision
assembler in fresh private ``ModuleType`` namespaces.  It never imports or calls
the terminal scheduler, coverage verifier, or post-issuance receipt verifier
directly.

V3 authorizes the root-initializer capability and the terminal-issuer role as
separate artifacts.  Consequently the root state remains evidence-only and
self-non-authorizing.  Only after both grants resolve does this module attach a
separate actualness receipt and wrap the assembler evidence as either a root
terminal receipt or a scope-bounded registered-prefix miss receipt.

Neither production receipt grants persistent admission, a common owner, E1,
queue mutation, or producer continuation.  This module exposes no runtime,
admission, E1, enqueue, or post-issuance verifier API.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, fields
from enum import Enum
import hashlib
import json
from math import isqrt
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from types import MappingProxyType, ModuleType
from typing import Any, ClassVar, Mapping, NoReturn, Sequence, TypeVar


SCHEMA_VERSION = 1
ISSUER_ID = "q1_terminal_issuer_v1"
ISSUER_PATH = "scripts/t6_q_one_terminal_issuer_v1.py"
ISSUER_SYMBOL = "issue_q_one_terminal_decision_v1"

V2_REGISTRY_ID = "t6_coordinator_role_registry_v2"
V2_REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v2.json"
V2_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v2.py"
V2_RESOLVER_SYMBOL = "resolve_registry_v2"
V2_STATUS = "HEAD_BOUND_PREFIX_SCHEDULE_AUTHORITY_NO_ISSUER"

V3_REGISTRY_ID = "t6_coordinator_role_registry_v3"
V3_REGISTRY_PATH = "data/t6-wave1/t6-coordinator-role-registry-v3.json"
V3_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v3.py"
V3_SCHEMA_PATH = "schemas/t6-coordinator-role-registry-v3.schema.json"
V3_RESOLVER_SYMBOL = "resolve_registry_v3"
V3_STATUS = "HEAD_BOUND_Q1_ROOT_TERMINAL_DECISION_AUTHORITY_NO_RECURSION"

ROOT_ENVELOPE_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"
ASSEMBLER_PATH = "scripts/t6_q_one_terminal_decision_assembler_v2.py"
ASSEMBLER_SYMBOL = "assemble_q_one_terminal_decision_v2"
ASSEMBLER_SERIALIZER_SYMBOL = "terminal_decision_to_mapping_v2"

EXACT_EXECUTION_PATHS = (
    ISSUER_PATH,
    V2_RESOLVER_PATH,
    V3_RESOLVER_PATH,
    ROOT_ENVELOPE_PATH,
    ASSEMBLER_PATH,
)
REGULAR_GIT_MODES = frozenset({"100644", "100755"})

SCHEDULE_ID = "q1_root_gap_3_7_11_registered_priority_prefix_v1"
ORDERED_GAPS = (3, 7, 11)
NEXT_UNCHECKED_GAP = 15
COVERAGE_SEMANTICS = "REGISTERED_PRIORITY_ONLY"
SUBJECT_KIND = "SOURCE_STATE"

INITIALIZER_ARTIFACT_ID = "q1_root_initializer_envelope_v2"
ASSEMBLER_ARTIFACT_ID = "q1_terminal_decision_assembler_v2"
ISSUER_ARTIFACT_ID = "q1_terminal_issuer_v1"
SCHEDULER_ARTIFACT_ID = "q1_priority_prefix_scheduler_v1"
COVERAGE_ARTIFACT_ID = "q1_priority_prefix_coverage_verifier_v1"
V2_RESOLVER_ARTIFACT_ID = "v2_registry_resolver_dependency"

INITIALIZER_GRANT_ID = "q1_root_initializer_grant_v3"
ISSUER_GRANT_ID = "q1_terminal_issuer_grant_v3"
SCHEDULER_GRANT_ID = "q1_prefix_terminal_scheduler_grant_v3"
COVERAGE_GRANT_ID = "q1_prefix_independent_coverage_verifier_grant_v3"

ROLE_INITIALIZER = "ROOT_INITIALIZER"
ROLE_ISSUER = "TERMINAL_ISSUER"
ROLE_SCHEDULER = "TERMINAL_SCHEDULER"
ROLE_COVERAGE = "INDEPENDENT_COVERAGE_VERIFIER"
ROLE_AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_V3"

PRODUCTION_RECEIPT_SCHEMA_ID = "t6_q_one_production_terminal_receipts_v1"
PRODUCTION_RECEIPT_SCHEMA_PATH = (
    "schemas/t6-q-one-production-terminal-receipts-v1.schema.json"
)
ACTUALNESS_SCOPE = "ROOT_OCCURRENCE_ONLY"
OWNER_DOMAIN_ID = "ordinary_parentless_q1_g_root_v1"
OCCURRENCE_KIND = "ROOT_INITIALIZER_OUTPUT"
PARENT_KIND = "PARENTLESS_ROOT"
ACTUALNESS_ATTESTOR_ROLE = ROLE_ISSUER

ASSEMBLER_HIT_OUTCOME = "ROOT_TERMINAL_HIT_EVIDENCE"
ASSEMBLER_MISS_OUTCOME = "PREFIX_MISS_EVIDENCE"
HIT_OUTCOME = "ROOT_TERMINAL_HIT"
MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"
ROOT_OUTCOME_KIND = "ROOT_CERTIFICATE_LEFT_INJECTION"

AUTHORITY_MATRIX = {
    "common": {
        "source_actualness": True,
        "root_initializer_authority": True,
        "issuer_authority": True,
        "issued_under_terminal_issuer": True,
        "persistent_admission": False,
        "common_owner_authority": False,
        "global_exhaustion": False,
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

BODY_ID_PREFIX = "q1-source-body:"
ANCHOR_ID_PREFIX = "root-init-anchor:"
STATE_ID_PREFIX = "state:"
ACTUALNESS_ID_PREFIX = "q1-root-source-actualness:"
ROOT_PROBLEM_ID_PREFIX = "q1-root-problem:"
HIT_RECEIPT_ID_PREFIX = "production-q1-root-terminal:"
MISS_RECEIPT_ID_PREFIX = "production-q1-prefix-miss:"

_DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")
_GIT_OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
_MAPPING_PROXY_TYPE = type(MappingProxyType({}))


class QOneTerminalIssuerRejectCode(str, Enum):
    HEAD_BINDING_ERROR = "HEAD_BINDING_ERROR"
    MODULE_BINDING_ERROR = "MODULE_BINDING_ERROR"
    WORKTREE_BINDING_ERROR = "WORKTREE_BINDING_ERROR"
    V2_REGISTRY_ERROR = "V2_REGISTRY_ERROR"
    V3_REGISTRY_ERROR = "V3_REGISTRY_ERROR"
    CROSS_REGISTRY_ERROR = "CROSS_REGISTRY_ERROR"
    GRANT_ERROR = "GRANT_ERROR"
    DEPENDENCY_POLICY_ERROR = "DEPENDENCY_POLICY_ERROR"
    ROOT_INITIALIZER_ERROR = "ROOT_INITIALIZER_ERROR"
    ASSEMBLER_ERROR = "ASSEMBLER_ERROR"
    DECISION_BINDING_ERROR = "DECISION_BINDING_ERROR"
    OUTCOME_ERROR = "OUTCOME_ERROR"
    AUTHORITY_ERROR = "AUTHORITY_ERROR"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    ID_MISMATCH = "ID_MISMATCH"


class QOneTerminalIssuerError(ValueError):
    def __init__(self, code: QOneTerminalIssuerRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: QOneTerminalIssuerRejectCode, detail: str) -> NoReturn:
    raise QOneTerminalIssuerError(code, detail)


def _plain_int(value: Any) -> bool:
    return type(value) is int


def _require_text(value: Any, name: str) -> str:
    if type(value) is not str or not value or value.strip() != value:
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty trimmed exact string",
        )
    return value


def _require_digest(value: Any, name: str) -> str:
    if type(value) is not str or _DIGEST_RE.fullmatch(value) is None:
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            f"{name} must be a lowercase SHA-256 digest",
        )
    return value


def _require_git_oid(value: Any, name: str) -> str:
    if type(value) is not str or _GIT_OID_RE.fullmatch(value) is None:
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            f"{name} must be a full lowercase Git object ID",
        )
    return value


def _require_content_id(value: Any, name: str, prefix: str) -> str:
    text = _require_text(value, name)
    if not text.startswith(prefix) or _DIGEST_RE.fullmatch(text[len(prefix) :]) is None:
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            f"{name} must be {prefix!r} followed by a SHA-256 digest",
        )
    return text


def _require_exact_bool(value: Any, expected: bool, name: str) -> None:
    if type(value) is not bool or value is not expected:
        _reject(
            QOneTerminalIssuerRejectCode.AUTHORITY_ERROR,
            f"{name} must be exactly {expected!r}",
        )


def _json_copy(value: Any, *, path: str = "$") -> Any:
    if type(value) in {dict, _MAPPING_PROXY_TYPE}:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                _reject(
                    QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
                    f"{path} keys must be nonempty exact strings",
                )
            result[key] = _json_copy(child, path=f"{path}.{key}")
        return result
    if type(value) in {list, tuple}:
        return [
            _json_copy(child, path=f"{path}[{index}]")
            for index, child in enumerate(value)
        ]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(
        QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
        f"{path} contains unsupported type {type(value).__name__}",
    )


def _freeze_json(value: Any) -> Any:
    normalized = _json_copy(value)
    if type(normalized) is dict:
        return MappingProxyType(
            {key: _freeze_json(child) for key, child in normalized.items()}
        )
    if type(normalized) is list:
        return tuple(_freeze_json(child) for child in normalized)
    return normalized


def canonical_json_v1(value: Any) -> str:
    return json.dumps(
        _json_copy(value),
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


class _FactoryOnlyV1:
    __slots__ = ()

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} must be created by the production issuer")


@dataclass(frozen=True, init=False, slots=True)
class QOneRootSourceActualnessReceiptV1(_FactoryOnlyV1):
    ARTIFACT_TYPE: ClassVar[str] = "QOneRootSourceActualnessReceiptV1"
    ID_FIELD: ClassVar[str] = "actualness_id"
    ID_PREFIX: ClassVar[str] = ACTUALNESS_ID_PREFIX

    head_sha: str
    head_tree_sha: str
    v3_registry_id: str
    v3_registry_digest: str
    v3_role_manifest_digest: str
    initializer_grant_id: str
    initializer_grant_digest: str
    initializer_artifact_id: str
    initializer_artifact_semantic_sha256: str
    issuer_grant_id: str
    issuer_grant_digest: str
    issuer_artifact_id: str
    issuer_artifact_semantic_sha256: str
    fresh_module_binding_digest: str
    root_problem: Mapping[str, Any]
    root_problem_id: str
    root_problem_digest: str
    raw_q_one_g: Mapping[str, Any]
    raw_q_one_g_digest: str
    deterministic_initial_branch_replay: Mapping[str, Any]
    deterministic_initial_branch_replay_digest: str
    body_id: str
    body_digest: str
    anchor_id: str
    anchor_digest: str
    state_id: str
    state_digest: str
    initializer_id: str
    initializer_contract_digest: str
    domain_replay_id: str
    domain_replay_digest: str
    owner_domain_id: str
    occurrence_kind: str
    parent_kind: str
    actualness_scope: str
    initializer_output_self_authorizing: bool
    actualness_attestor_role: str
    source_actualness: bool
    root_initializer_authority: bool
    terminal_issuer_attestation_authority: bool
    persistent_admission: bool
    common_owner_authority: bool
    e1_authority: bool
    queue_authority: bool
    actualness_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class _ProductionReceiptBaseV1(_FactoryOnlyV1):
    head_sha: str
    head_tree_sha: str
    v2_registry_id: str
    v2_registry_digest: str
    v2_role_manifest_digest: str
    v3_registry_id: str
    v3_registry_digest: str
    v3_role_manifest_digest: str
    cross_registry_equivalence_digest: str
    initializer_grant_id: str
    initializer_grant_digest: str
    initializer_artifact_semantic_sha256: str
    issuer_grant_id: str
    issuer_grant_digest: str
    issuer_artifact_semantic_sha256: str
    scheduler_grant_id: str
    scheduler_grant_digest: str
    scheduler_artifact_semantic_sha256: str
    coverage_verifier_grant_id: str
    coverage_verifier_grant_digest: str
    coverage_verifier_artifact_semantic_sha256: str
    fresh_module_binding_digest: str
    root_actualness: QOneRootSourceActualnessReceiptV1
    root_actualness_digest: str
    root_problem_id: str
    root_problem_digest: str
    raw_q_one_g_digest: str
    deterministic_initial_branch_replay_digest: str
    body_id: str
    body_digest: str
    anchor_id: str
    anchor_digest: str
    state_id: str
    state_digest: str
    subject_kind: str
    root_context: int
    assembler_artifact_id: str
    assembler_artifact_semantic_sha256: str
    assembler_module_binding_digest: str
    assembler_decision_id: str
    assembler_decision_digest: str
    assembler_evidence_digest: str
    assembler_coverage_replay_digest: str
    schedule_id: str
    schedule_digest: str
    source_actualness: bool
    root_initializer_authority: bool
    issuer_authority: bool
    issued_under_terminal_issuer: bool
    persistent_admission: bool
    common_owner_authority: bool
    e1_authority: bool
    queue_authority: bool
    producer_continuation_allowed: bool
    receipt_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class ProductionQOneRootTerminalReceiptV1(_ProductionReceiptBaseV1):
    ARTIFACT_TYPE: ClassVar[str] = "ProductionQOneRootTerminalReceiptV1"
    ID_FIELD: ClassVar[str] = "receipt_id"
    ID_PREFIX: ClassVar[str] = HIT_RECEIPT_ID_PREFIX

    outcome: str
    root_outcome_kind: str
    selected_certificate: Mapping[str, Any]
    selected_certificate_digest: str
    root_equation: Mapping[str, Any]
    root_equation_digest: str
    global_exhaustion: bool
    terminal_leaf_authority: bool
    registered_prefix_miss_authority: bool
    root_proof_close_authority: bool


@dataclass(frozen=True, init=False, slots=True)
class ProductionQOneRegisteredPrefixMissReceiptV1(_ProductionReceiptBaseV1):
    ARTIFACT_TYPE: ClassVar[str] = "ProductionQOneRegisteredPrefixMissReceiptV1"
    ID_FIELD: ClassVar[str] = "receipt_id"
    ID_PREFIX: ClassVar[str] = MISS_RECEIPT_ID_PREFIX

    outcome: str
    coverage_semantics: str
    ordered_gaps: tuple[int, int, int]
    next_unchecked_gap: int
    global_exhaustion: bool
    selected_certificate: None
    selected_certificate_digest: None
    terminal_leaf_authority: bool
    registered_prefix_miss_authority: bool
    root_proof_close_authority: bool


ProductionReceiptV1 = (
    ProductionQOneRootTerminalReceiptV1
    | ProductionQOneRegisteredPrefixMissReceiptV1
)
ReceiptT = TypeVar("ReceiptT", bound=ProductionReceiptV1)


@dataclass(frozen=True, slots=True)
class _GitBlobV1:
    path: str
    git_mode: str
    git_object_id: str
    content: bytes

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.content).hexdigest()


@dataclass(frozen=True, slots=True)
class _FreshModulesV1:
    v2_registry: ModuleType
    v3_registry: ModuleType
    root_envelope: ModuleType
    assembler: ModuleType

    def by_path(self) -> Mapping[str, ModuleType]:
        return MappingProxyType(
            {
                V2_RESOLVER_PATH: self.v2_registry,
                V3_RESOLVER_PATH: self.v3_registry,
                ROOT_ENVELOPE_PATH: self.root_envelope,
                ASSEMBLER_PATH: self.assembler,
            }
        )


def _run_git_v1(root: Path, args: Sequence[str]) -> bytes:
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
        _reject(
            QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
            f"git {' '.join(args)} failed: {detail}",
        )
    return completed.stdout


def _repository_root_v1(locator: Path) -> Path:
    if not isinstance(locator, Path):
        _reject(
            QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
            "root must be a pathlib.Path",
        )
    try:
        return Path(
            _run_git_v1(locator.resolve(), ("rev-parse", "--show-toplevel"))
            .decode("utf-8")
            .strip()
        ).resolve()
    except UnicodeDecodeError as exc:
        raise QOneTerminalIssuerError(
            QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
            "repository root is not UTF-8",
        ) from exc


def _exact_head_v1(root: Path, requested_head: str) -> tuple[str, str]:
    object_format = _run_git_v1(root, ("rev-parse", "--show-object-format")).decode(
        "ascii"
    ).strip()
    oid_length = 40 if object_format == "sha1" else 64 if object_format == "sha256" else 0
    if (
        oid_length == 0
        or type(requested_head) is not str
        or len(requested_head) != oid_length
        or any(character not in "0123456789abcdef" for character in requested_head)
    ):
        _reject(
            QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
            "requested_head must be one exact full lowercase commit ID",
        )
    object_type = _run_git_v1(root, ("cat-file", "-t", requested_head)).decode().strip()
    if object_type != "commit":
        _reject(
            QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
            "requested_head is not a commit",
        )
    resolved = _run_git_v1(
        root,
        ("rev-parse", "--verify", f"{requested_head}^{{commit}}"),
    ).decode("ascii").strip()
    if resolved != requested_head:
        _reject(
            QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
            "requested commit did not resolve exactly",
        )
    tree_sha = _run_git_v1(root, ("rev-parse", f"{requested_head}^{{tree}}"))
    tree_sha_text = tree_sha.decode("ascii").strip()
    if len(tree_sha_text) != oid_length:
        _reject(
            QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
            "requested commit tree ID is malformed",
        )
    return requested_head, tree_sha_text


def _tree_entries_v1(root: Path, head_sha: str) -> dict[str, tuple[str, str, str]]:
    raw = _run_git_v1(root, ("ls-tree", "-r", "-z", "--full-tree", head_sha))
    result: dict[str, tuple[str, str, str]] = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            metadata, path_bytes = record.split(b"\t", 1)
            mode, object_type, object_id = metadata.decode("ascii").split(" ")
            path = path_bytes.decode("utf-8")
        except (UnicodeDecodeError, ValueError) as exc:
            raise QOneTerminalIssuerError(
                QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
                f"malformed Git tree entry {record!r}",
            ) from exc
        pure = PurePosixPath(path)
        if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
            _reject(
                QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
                f"unsafe tracked path {path!r}",
            )
        if path in result:
            _reject(
                QOneTerminalIssuerRejectCode.HEAD_BINDING_ERROR,
                f"duplicate tracked path {path!r}",
            )
        result[path] = (mode, object_type, object_id)
    return result


def _exact_head_blob_v1(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    path: str,
) -> _GitBlobV1:
    entry = entries.get(path)
    if entry is None:
        _reject(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            f"{path!r} is absent from requested HEAD",
        )
    mode, object_type, object_id = entry
    if mode not in REGULAR_GIT_MODES or object_type != "blob":
        _reject(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            f"{path!r} is not a regular tracked blob",
        )
    return _GitBlobV1(
        path,
        mode,
        object_id,
        _run_git_v1(root, ("cat-file", "blob", object_id)),
    )


def _require_exact_worktree_blob_v1(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    path: str,
) -> tuple[_GitBlobV1, Path]:
    blob = _exact_head_blob_v1(root, entries, path)
    worktree_path = root / path
    if worktree_path.is_symlink() or not worktree_path.is_file():
        _reject(
            QOneTerminalIssuerRejectCode.WORKTREE_BINDING_ERROR,
            f"{path} is not a regular worktree file",
        )
    if worktree_path.read_bytes() != blob.content:
        _reject(
            QOneTerminalIssuerRejectCode.WORKTREE_BINDING_ERROR,
            f"{path} differs from requested HEAD",
        )
    return blob, worktree_path


def _verify_issuer_self_v1(
    root: Path,
    head_sha: str,
    tree_sha: str,
    entries: Mapping[str, tuple[str, str, str]],
) -> dict[str, Any]:
    blob, worktree_path = _require_exact_worktree_blob_v1(root, entries, ISSUER_PATH)
    executing = Path(__file__)
    if (
        executing.is_symlink()
        or not executing.is_file()
        or executing.resolve() != worktree_path.resolve()
        or executing.read_bytes() != blob.content
    ):
        _reject(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            "executing issuer is not backed by its requested-HEAD blob",
        )
    payload: dict[str, Any] = {
        "schema_id": "t6_q_one_terminal_issuer_self_binding_v1",
        "head_sha": head_sha,
        "head_tree_sha": tree_sha,
        "path": ISSUER_PATH,
        "module_name": ISSUER_ID,
        "git_mode": blob.git_mode,
        "git_object_id": blob.git_object_id,
        "blob_sha256": blob.sha256,
        "status": "CURRENT_ISSUER_MATCHES_EXACT_HEAD_BLOB",
    }
    payload["digest"] = canonical_digest_v1(payload)
    return payload


def _fresh_private_name_v1(role: str, head_sha: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9_]", "_", role)
    return f"_t6_issuer_exact_head_{normalized}_{head_sha}"


def _fresh_exec_module_v1(
    *,
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    path: str,
    private_name: str,
) -> ModuleType:
    blob, worktree_path = _require_exact_worktree_blob_v1(root, entries, path)
    try:
        code = compile(
            blob.content,
            str(worktree_path.resolve()),
            "exec",
            dont_inherit=True,
            optimize=sys.flags.optimize,
        )
    except (SyntaxError, ValueError, TypeError) as exc:
        raise QOneTerminalIssuerError(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            f"cannot compile exact-HEAD module {path}: {exc}",
        ) from exc
    module = ModuleType(private_name)
    module.__file__ = str(worktree_path.resolve())
    module.__package__ = ""
    previous = sys.modules.get(private_name)
    sys.modules[private_name] = module
    try:
        exec(code, module.__dict__)
    except Exception as exc:
        raise QOneTerminalIssuerError(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            f"exact-HEAD module {path} failed fresh execution: {exc}",
        ) from exc
    finally:
        if previous is None:
            sys.modules.pop(private_name, None)
        else:
            sys.modules[private_name] = previous
    return module


def _load_fresh_modules_v1(
    *,
    root: Path,
    head_sha: str,
    entries: Mapping[str, tuple[str, str, str]],
) -> _FreshModulesV1:
    return _FreshModulesV1(
        v2_registry=_fresh_exec_module_v1(
            root=root,
            entries=entries,
            path=V2_RESOLVER_PATH,
            private_name=_fresh_private_name_v1("v2_registry", head_sha),
        ),
        v3_registry=_fresh_exec_module_v1(
            root=root,
            entries=entries,
            path=V3_RESOLVER_PATH,
            private_name=_fresh_private_name_v1("v3_registry", head_sha),
        ),
        root_envelope=_fresh_exec_module_v1(
            root=root,
            entries=entries,
            path=ROOT_ENVELOPE_PATH,
            private_name=_fresh_private_name_v1("root_envelope", head_sha),
        ),
        assembler=_fresh_exec_module_v1(
            root=root,
            entries=entries,
            path=ASSEMBLER_PATH,
            private_name=_fresh_private_name_v1("assembler", head_sha),
        ),
    )


def _require_callable_v1(module: ModuleType, symbol: str) -> Any:
    value = getattr(module, symbol, None)
    if (
        not callable(value)
        or type(getattr(value, "__name__", None)) is not str
        or value.__name__ != symbol
        or type(getattr(value, "__module__", None)) is not str
        or value.__module__ != module.__name__
        or getattr(module, symbol) is not value
    ):
        _reject(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            f"fresh callable {module.__name__}.{symbol} drifted",
        )
    return value


_CALLABLES_BY_PATH = MappingProxyType(
    {
        V2_RESOLVER_PATH: (V2_RESOLVER_SYMBOL,),
        V3_RESOLVER_PATH: (V3_RESOLVER_SYMBOL,),
        ROOT_ENVELOPE_PATH: (
            "artifact_to_mapping_v2",
            "make_canonical_q_one_g_source_body_v2",
            "make_raw_root_source_state_v2",
            "make_root_initializer_anchor_v2",
        ),
        ASSEMBLER_PATH: (ASSEMBLER_SYMBOL, ASSEMBLER_SERIALIZER_SYMBOL),
    }
)


def _capture_fresh_module_binding_v1(
    root: Path,
    head_sha: str,
    tree_sha: str,
    entries: Mapping[str, tuple[str, str, str]],
    modules: _FreshModulesV1,
    issuer_self: Mapping[str, Any],
) -> dict[str, Any]:
    files: list[dict[str, Any]] = [_json_copy(issuer_self)]
    module_map = modules.by_path()
    for path in EXACT_EXECUTION_PATHS[1:]:
        blob, worktree_path = _require_exact_worktree_blob_v1(root, entries, path)
        module = module_map.get(path)
        if type(module) is not ModuleType:
            _reject(
                QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
                f"{path} is not a fresh private ModuleType",
            )
        module_file = getattr(module, "__file__", None)
        if (
            type(module_file) is not str
            or Path(module_file).is_symlink()
            or not Path(module_file).is_file()
            or Path(module_file).resolve() != worktree_path.resolve()
            or Path(module_file).read_bytes() != blob.content
        ):
            _reject(
                QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
                f"fresh module backing for {path} differs from exact HEAD",
            )
        callable_identities = []
        for symbol in _CALLABLES_BY_PATH[path]:
            value = _require_callable_v1(module, symbol)
            callable_identities.append(
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
                "git_mode": blob.git_mode,
                "git_object_id": blob.git_object_id,
                "blob_sha256": blob.sha256,
                "execution_mode": "FRESH_COMPILE_EXEC_FROM_EXACT_HEAD_BLOB",
                "callable_identities": callable_identities,
            }
        )
    payload: dict[str, Any] = {
        "schema_id": "t6_q_one_terminal_issuer_module_binding_v1",
        "head_sha": head_sha,
        "head_tree_sha": tree_sha,
        "files": files,
        "forbidden_direct_modules": [
            "coverage verifier",
            "post-issuance receipt verifier",
            "terminal scheduler",
        ],
        "status": "ONLY_V2_V3_INITIALIZER_ASSEMBLER_FRESH_EXECUTED",
    }
    payload["digest"] = canonical_digest_v1(payload)
    return payload


def _verify_mapping_seal_v1(
    value: Any,
    *,
    name: str,
    digest_field: str = "digest",
) -> str:
    if type(value) is not dict:
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            f"{name} must be an exact dict",
        )
    digest = value.get(digest_field)
    _require_digest(digest, f"{name}.{digest_field}")
    unsigned = _json_copy(value)
    unsigned.pop(digest_field)
    if canonical_digest_v1(unsigned) != digest:
        _reject(
            QOneTerminalIssuerRejectCode.DIGEST_MISMATCH,
            f"{name}.{digest_field} does not replay",
        )
    return digest


def _verify_v2_registry_v1(
    resolved: Any,
    *,
    head_sha: str,
    tree_sha: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    if type(resolved) is not dict:
        _reject(
            QOneTerminalIssuerRejectCode.V2_REGISTRY_ERROR,
            "resolved V2 registry must be an exact dict",
        )
    digest = resolved.get("registry_digest")
    _require_digest(digest, "v2.registry_digest")
    unsigned = _json_copy(resolved)
    unsigned.pop("registry_digest")
    if canonical_digest_v1(unsigned) != digest:
        _reject(
            QOneTerminalIssuerRejectCode.V2_REGISTRY_ERROR,
            "resolved V2 registry digest does not replay",
        )
    if not (
        resolved.get("schema_id") == "t6_coordinator_role_registry_resolved_v2"
        and _plain_int(resolved.get("schema_version"))
        and resolved["schema_version"] == 2
        and resolved.get("head_sha") == head_sha
        and resolved.get("head_tree_sha") == tree_sha
        and resolved.get("status") == V2_STATUS
        and _plain_int(resolved.get("active_role_grant_count"))
        and resolved["active_role_grant_count"] == 2
        and resolved.get("authorized_branches") == []
        and _plain_int(resolved.get("issuer_count"))
        and resolved["issuer_count"] == 0
    ):
        _reject(
            QOneTerminalIssuerRejectCode.V2_REGISTRY_ERROR,
            "resolved V2 identity, HEAD, roles, branch, or issuer boundary changed",
        )
    for name in (
        "issuer_authority",
        "e1_authority",
        "queue_authority",
        "producer_authority",
        "initializer_authority",
        "t5_authority",
    ):
        _require_exact_bool(resolved.get(name), False, f"v2.{name}")
    artifacts = resolved.get("resolved_artifacts")
    grants = resolved.get("resolved_role_grants")
    if (
        type(artifacts) is not list
        or len(artifacts) != 2
        or any(type(item) is not dict for item in artifacts)
        or type(grants) is not list
        or len(grants) != 2
        or any(type(item) is not dict for item in grants)
    ):
        _reject(
            QOneTerminalIssuerRejectCode.V2_REGISTRY_ERROR,
            "resolved V2 artifact/grant collections changed",
        )
    artifact_map = {item.get("artifact_id"): item for item in artifacts}
    grant_map = {item.get("role"): item for item in grants}
    if set(artifact_map) != {SCHEDULER_ARTIFACT_ID, COVERAGE_ARTIFACT_ID} or set(
        grant_map
    ) != {ROLE_SCHEDULER, ROLE_COVERAGE}:
        _reject(
            QOneTerminalIssuerRejectCode.V2_REGISTRY_ERROR,
            "resolved V2 role identities changed",
        )
    prefixes = resolved.get("authorized_terminal_prefixes")
    if (
        type(prefixes) is not list
        or len(prefixes) != 1
        or type(prefixes[0]) is not dict
        or prefixes[0].get("schedule_id") != SCHEDULE_ID
        or prefixes[0].get("ordered_gaps") != list(ORDERED_GAPS)
        or prefixes[0].get("next_unchecked_gap") != NEXT_UNCHECKED_GAP
        or prefixes[0].get("global_exhaustion") is not False
    ):
        _reject(
            QOneTerminalIssuerRejectCode.V2_REGISTRY_ERROR,
            "resolved V2 terminal-prefix contract changed",
        )
    manifest = resolved.get("role_authority_manifest")
    _verify_mapping_seal_v1(value=manifest, name="v2 role manifest")
    if not (
        manifest.get("head_sha") == head_sha
        and manifest.get("status") == V2_STATUS
        and manifest.get("issuer_count") == 0
        and manifest.get("e1_authority") is False
        and manifest.get("queue_authority") is False
        and manifest.get("producer_authority") is False
        and manifest.get("initializer_authority") is False
        and manifest.get("t5_authority") is False
    ):
        _reject(
            QOneTerminalIssuerRejectCode.V2_REGISTRY_ERROR,
            "V2 role manifest grants forbidden authority",
        )
    return resolved, artifact_map, grant_map


def _exact_v3_grant_expectations_v1() -> Mapping[str, tuple[str, str, tuple[str, ...]]]:
    return MappingProxyType(
        {
            ROLE_COVERAGE: (
                COVERAGE_GRANT_ID,
                COVERAGE_ARTIFACT_ID,
                ("CERTIFICATE_VERIFIER", "DOMAIN_VERIFIER", "ROOT_TERMINAL_VERIFIER"),
            ),
            ROLE_INITIALIZER: (
                INITIALIZER_GRANT_ID,
                INITIALIZER_ARTIFACT_ID,
                (
                    "BUILD_PARENTLESS_Q1_G_ROOT_ENVELOPE",
                    "ESTABLISH_AUTHORIZED_ROOT_INITIALIZER_OCCURRENCE",
                ),
            ),
            ROLE_ISSUER: (
                ISSUER_GRANT_ID,
                ISSUER_ARTIFACT_ID,
                ("ISSUE_REGISTERED_PREFIX_MISS", "ISSUE_ROOT_TERMINAL_HIT"),
            ),
            ROLE_SCHEDULER: (
                SCHEDULER_GRANT_ID,
                SCHEDULER_ARTIFACT_ID,
                ("REGISTERED_PRIORITY_PREFIX_REPLAY",),
            ),
        }
    )


def _verify_v3_registry_v1(
    resolved: Any,
    *,
    head_sha: str,
    tree_sha: str,
) -> tuple[
    dict[str, Any],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
]:
    if type(resolved) is not dict:
        _reject(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            "resolved V3 registry must be an exact dict",
        )
    digest = resolved.get("registry_digest")
    _require_digest(digest, "v3.registry_digest")
    unsigned = _json_copy(resolved)
    unsigned.pop("registry_digest")
    if canonical_digest_v1(unsigned) != digest:
        _reject(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            "resolved V3 registry digest does not replay",
        )
    count_fields = (
        "active_role_grant_count",
        "root_initializer_count",
        "terminal_issuer_count",
        "terminal_scheduler_count",
        "independent_coverage_verifier_count",
    )
    if not (
        resolved.get("schema_id") == "t6_coordinator_role_registry_resolved_v3"
        and _plain_int(resolved.get("schema_version"))
        and resolved["schema_version"] == 3
        and resolved.get("head_sha") == head_sha
        and resolved.get("head_tree_sha") == tree_sha
        and resolved.get("status") == V3_STATUS
        and resolved.get("authorized_branches") == []
        and all(_plain_int(resolved.get(name)) for name in count_fields)
        and resolved["active_role_grant_count"] == 4
        and all(resolved[name] == 1 for name in count_fields[1:])
        and _plain_int(resolved.get("assembler_role_count"))
        and resolved["assembler_role_count"] == 0
        and _plain_int(resolved.get("receipt_verifier_role_count"))
        and resolved["receipt_verifier_role_count"] == 0
    ):
        _reject(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            "resolved V3 identity, HEAD, role counts, or branch boundary changed",
        )
    denials = resolved.get("authority_denials")
    expected_denials = {
        "e1_authority": False,
        "queue_authority": False,
        "producer_authority": False,
        "t5_authority": False,
        "branch_authority": False,
    }
    if type(denials) is not dict or set(denials) != set(expected_denials):
        _reject(
            QOneTerminalIssuerRejectCode.AUTHORITY_ERROR,
            "V3 authority denial field set changed",
        )
    for name in expected_denials:
        _require_exact_bool(denials[name], False, f"v3.{name}")

    artifacts = resolved.get("resolved_artifacts")
    grants = resolved.get("resolved_role_grants")
    if (
        type(artifacts) is not list
        or len(artifacts) != 7
        or any(type(item) is not dict for item in artifacts)
        or type(grants) is not list
        or len(grants) != 4
        or any(type(item) is not dict for item in grants)
    ):
        _reject(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            "V3 artifact or grant collections changed",
        )
    artifact_map = {item.get("artifact_id"): item for item in artifacts}
    required_artifacts = {
        COVERAGE_ARTIFACT_ID,
        INITIALIZER_ARTIFACT_ID,
        SCHEDULER_ARTIFACT_ID,
        ASSEMBLER_ARTIFACT_ID,
        ISSUER_ARTIFACT_ID,
        V2_RESOLVER_ARTIFACT_ID,
        "q1_production_terminal_receipt_verifier_v1",
    }
    if set(artifact_map) != required_artifacts:
        _reject(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            "V3 artifact identity set changed",
        )
    grant_map = {item.get("role"): item for item in grants}
    expectations = _exact_v3_grant_expectations_v1()
    if set(grant_map) != set(expectations):
        _reject(
            QOneTerminalIssuerRejectCode.GRANT_ERROR,
            "V3 role grant set changed",
        )
    for role, (grant_id, artifact_id, capabilities) in expectations.items():
        grant = grant_map[role]
        artifact = artifact_map[artifact_id]
        if not (
            grant.get("grant_id") == grant_id
            and grant.get("artifact_id") == artifact_id
            and grant.get("capabilities") == list(capabilities)
            and grant.get("authority_class") == ROLE_AUTHORITY_CLASS
            and grant.get("expected_artifact_semantic_sha256")
            == artifact.get("semantic_sha256")
            and grant.get("artifact_semantic_sha256") == artifact.get("semantic_sha256")
            and grant.get("expected_dependency_manifest_digest")
            == artifact.get("dependency_manifest_digest")
            and grant.get("artifact_dependency_manifest_digest")
            == artifact.get("dependency_manifest_digest")
        ):
            _reject(
                QOneTerminalIssuerRejectCode.GRANT_ERROR,
                f"V3 grant/pin mismatch for {role}",
            )
        for name in (
            "blob_sha256",
            "symbol_set_digest",
            "local_import_closure_digest",
            "dependency_manifest_digest",
            "semantic_sha256",
        ):
            _require_digest(artifact.get(name), f"v3 artifact {artifact_id}.{name}")

    expected_initializer = {
        "grant_id": INITIALIZER_GRANT_ID,
        "initializer_id": "q_one_root_initializer_envelope_v2",
        "owner_domain_id": OWNER_DOMAIN_ID,
        "factory_sequence": [
            "make_canonical_q_one_g_source_body_v2",
            "make_root_initializer_anchor_v2",
            "make_raw_root_source_state_v2",
        ],
        "occurrence_kind": OCCURRENCE_KIND,
        "parent_kind": PARENT_KIND,
        "actualness_receipt_type": "QOneRootSourceActualnessReceiptV1",
        "actualness_scope": ACTUALNESS_SCOPE,
        "caller_supplied_state_allowed": False,
        "initializer_output_self_authorizing": False,
        "actualness_attestor_role": ACTUALNESS_ATTESTOR_ROLE,
    }
    initializer_policy = resolved.get("root_initializer_authority")
    if initializer_policy != expected_initializer:
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "V3 root initializer authority policy changed",
        )
    prefix_values = resolved.get("authorized_terminal_prefixes")
    if type(prefix_values) is not list or len(prefix_values) != 1:
        _reject(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            "V3 must authorize exactly one terminal prefix",
        )
    prefix = prefix_values[0]
    if prefix != {
        "schedule_id": SCHEDULE_ID,
        "scheduler_grant_id": SCHEDULER_GRANT_ID,
        "coverage_verifier_grant_id": COVERAGE_GRANT_ID,
        "ordered_gaps": list(ORDERED_GAPS),
        "next_unchecked_gap": NEXT_UNCHECKED_GAP,
        "coverage_semantics": COVERAGE_SEMANTICS,
        "global_exhaustion": False,
        "outcomes": [MISS_OUTCOME, HIT_OUTCOME],
    }:
        _reject(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            "V3 terminal-prefix authority changed",
        )
    issuance = resolved.get("terminal_issuance_policy")
    if not (
        type(issuance) is dict
        and issuance.get("issuer_grant_id") == ISSUER_GRANT_ID
        and issuance.get("receipt_schema_id") == PRODUCTION_RECEIPT_SCHEMA_ID
        and _plain_int(issuance.get("receipt_schema_version"))
        and issuance["receipt_schema_version"] == 1
        and issuance.get("root_actualness_type")
        == "QOneRootSourceActualnessReceiptV1"
        and issuance.get("hit_receipt_type")
        == "ProductionQOneRootTerminalReceiptV1"
        and issuance.get("miss_receipt_type")
        == "ProductionQOneRegisteredPrefixMissReceiptV1"
        and issuance.get("hit_outcome") == HIT_OUTCOME
        and issuance.get("miss_outcome") == MISS_OUTCOME
        and issuance.get("unqualified_miss_complete_forbidden") is True
        and issuance.get("producer_continuation_allowed") is False
        and issuance.get("authority_matrix") == AUTHORITY_MATRIX
    ):
        _reject(
            QOneTerminalIssuerRejectCode.AUTHORITY_ERROR,
            "V3 terminal issuance policy changed",
        )
    dependency_policy = resolved.get("issuer_dependency_policy")
    expected_dependency_policy = {
        "issuer_artifact_id": ISSUER_ARTIFACT_ID,
        "assembler_artifact_id": ASSEMBLER_ARTIFACT_ID,
        "assembler_class": "ISSUER_DEPENDENCY_ONLY",
        "allowed_execution_artifact_ids": [
            INITIALIZER_ARTIFACT_ID,
            ASSEMBLER_ARTIFACT_ID,
            V2_RESOLVER_ARTIFACT_ID,
        ],
        "forbidden_direct_artifact_ids": [
            COVERAGE_ARTIFACT_ID,
            SCHEDULER_ARTIFACT_ID,
            "q1_production_terminal_receipt_verifier_v1",
        ],
        "caller_inputs": ["raw_q_one_g", "repository_locator", "requested_head"],
        "caller_supplied_state_or_decision_allowed": False,
    }
    if dependency_policy != expected_dependency_policy:
        _reject(
            QOneTerminalIssuerRejectCode.DEPENDENCY_POLICY_ERROR,
            "V3 issuer dependency policy changed",
        )
    manifest = resolved.get("role_authority_manifest")
    _verify_mapping_seal_v1(value=manifest, name="v3 role manifest")
    if not (
        manifest.get("head_sha") == head_sha
        and manifest.get("status") == V3_STATUS
        and manifest.get("grants") == grants
        and manifest.get("root_initializer_authority") == initializer_policy
        and manifest.get("terminal_prefix_authority") == prefix
        and manifest.get("terminal_issuance_policy") == issuance
        and manifest.get("authority_denials") == expected_denials
    ):
        _reject(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            "V3 role authority manifest changed",
        )
    return resolved, artifact_map, grant_map


def _cross_registry_equivalence_digest_v1(
    v2: Mapping[str, Any],
    v3: Mapping[str, Any],
    v2_artifacts: Mapping[str, Mapping[str, Any]],
    v3_artifacts: Mapping[str, Mapping[str, Any]],
) -> str:
    cross = v3.get("v2_cross_registry_binding")
    if type(cross) is not dict:
        _reject(
            QOneTerminalIssuerRejectCode.CROSS_REGISTRY_ERROR,
            "V3 has no resolved V2 cross-registry binding",
        )
    if not (
        cross.get("v2_registry_id") == V2_REGISTRY_ID
        and cross.get("v2_head_sha") == v2.get("head_sha") == v3.get("head_sha")
        and cross.get("v2_registry_digest") == v2.get("registry_digest")
        and cross.get("v2_role_manifest_digest")
        == v2.get("role_authority_manifest", {}).get("digest")
        and cross.get("v2_scheduler_semantic_sha256")
        == v2_artifacts[SCHEDULER_ARTIFACT_ID].get("semantic_sha256")
        == v3_artifacts[SCHEDULER_ARTIFACT_ID].get("expected_v2_semantic_sha256")
        and cross.get("v2_coverage_verifier_semantic_sha256")
        == v2_artifacts[COVERAGE_ARTIFACT_ID].get("semantic_sha256")
        == v3_artifacts[COVERAGE_ARTIFACT_ID].get("expected_v2_semantic_sha256")
        and v3_artifacts[SCHEDULER_ARTIFACT_ID].get("semantic_sha256")
        == v3_artifacts[SCHEDULER_ARTIFACT_ID].get("expected_v3_semantic_sha256")
        and v3_artifacts[COVERAGE_ARTIFACT_ID].get("semantic_sha256")
        == v3_artifacts[COVERAGE_ARTIFACT_ID].get("expected_v3_semantic_sha256")
        and v2_artifacts[SCHEDULER_ARTIFACT_ID].get("path")
        == v3_artifacts[SCHEDULER_ARTIFACT_ID].get("path")
        and v2_artifacts[COVERAGE_ARTIFACT_ID].get("path")
        == v3_artifacts[COVERAGE_ARTIFACT_ID].get("path")
        and v2_artifacts[SCHEDULER_ARTIFACT_ID].get("blob_sha256")
        == v3_artifacts[SCHEDULER_ARTIFACT_ID].get("blob_sha256")
        and v2_artifacts[COVERAGE_ARTIFACT_ID].get("blob_sha256")
        == v3_artifacts[COVERAGE_ARTIFACT_ID].get("blob_sha256")
        and [v2_artifacts[SCHEDULER_ARTIFACT_ID].get("symbol")]
        == v3_artifacts[SCHEDULER_ARTIFACT_ID].get("symbols")
        and [v2_artifacts[COVERAGE_ARTIFACT_ID].get("symbol")]
        == v3_artifacts[COVERAGE_ARTIFACT_ID].get("symbols")
        and v2.get("authorized_terminal_prefixes", [{}])[0].get("schedule_id")
        == v3.get("authorized_terminal_prefixes", [{}])[0].get("schedule_id")
        == SCHEDULE_ID
    ):
        _reject(
            QOneTerminalIssuerRejectCode.CROSS_REGISTRY_ERROR,
            "V2/V3 registry, role manifest, scheduler, or coverage pins diverged",
        )
    return canonical_digest_v1(
        {
            "schema_id": "t6_v2_v3_q1_terminal_authority_equivalence_v1",
            "head_sha": v3["head_sha"],
            "v2_registry_digest": v2["registry_digest"],
            "v2_role_manifest_digest": v2["role_authority_manifest"]["digest"],
            "v3_registry_digest": v3["registry_digest"],
            "v3_role_manifest_digest": v3["role_authority_manifest"]["digest"],
            "resolved_v2_cross_binding": cross,
        }
    )


def _grant_digest_v1(grant: Mapping[str, Any]) -> str:
    return canonical_digest_v1(grant)


_RAW_Q_ONE_G_FIELDS = frozenset(
    {
        "schema_id",
        "schema_version",
        "root_context",
        "equation_rank",
        "equation_numerator",
        "equation_denominator",
        "q",
        "gap_three_x",
        "endpoint_fiber_code",
        "major_phase_code",
        "provenance_code",
        "mark_kind_code",
        "mark_root_context",
        "mark_equation_rank",
        "gap_three_factorization",
    }
)


def _is_prime_trial_v1(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    if value % 3 == 0:
        return value == 3
    divisor = 5
    step = 2
    limit = isqrt(value)
    while divisor <= limit:
        if value % divisor == 0:
            return False
        divisor += step
        step = 6 - step
    return True


def _factor_trial_v1(value: int) -> list[list[int]]:
    remainder = value
    factors: list[list[int]] = []
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while remainder % divisor == 0:
            remainder //= divisor
            exponent += 1
        factors.append([divisor, exponent])
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        factors.append([remainder, 1])
    return factors


def _validate_raw_q_one_g_v1(value: Any) -> dict[str, Any]:
    if type(value) not in {dict, _MAPPING_PROXY_TYPE}:
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "raw q1G preimage must be an exact frozen/object mapping",
        )
    raw = _json_copy(value)
    if frozenset(raw) != _RAW_Q_ONE_G_FIELDS:
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "raw q1G preimage field set changed",
        )
    if raw["schema_id"] != "q1_root_initializer_raw_v2" or not (
        _plain_int(raw["schema_version"]) and raw["schema_version"] == 2
    ):
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "raw q1G schema changed",
        )
    for name in _RAW_Q_ONE_G_FIELDS - {"schema_id", "gap_three_factorization"}:
        if not _plain_int(raw[name]):
            _reject(
                QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
                f"raw q1G {name} must be a plain integer",
            )
    p = raw["root_context"]
    x = (p + 3) // 4
    if not (
        _is_prime_trial_v1(p)
        and p % 24 == 1
        and raw["equation_rank"] == p
        and raw["equation_numerator"] == 4
        and raw["equation_denominator"] == p
        and raw["q"] == 1
        and raw["gap_three_x"] == x
        and raw["endpoint_fiber_code"] == 2
        and raw["major_phase_code"] == 3
        and raw["provenance_code"] == 1
        and raw["mark_kind_code"] == 1
        and raw["mark_root_context"] == p
        and raw["mark_equation_rank"] == p
    ):
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "raw preimage is not the canonical ordinary q=1 G root domain",
        )
    factors = raw["gap_three_factorization"]
    if (
        type(factors) is not list
        or not factors
        or any(
            type(pair) is not list
            or len(pair) != 2
            or not _plain_int(pair[0])
            or not _plain_int(pair[1])
            for pair in factors
        )
        or factors != _factor_trial_v1(x)
        or any(prime % 3 != 1 for prime, _exponent in factors)
    ):
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "raw q1G factorization is not the complete all-1-mod-3 factorization of X",
        )
    return raw


def _root_problem_v1(raw: Mapping[str, Any]) -> tuple[Mapping[str, Any], str, str]:
    p = raw["root_context"]
    payload = {
        "schema_id": "q1_canonical_root_problem_v1",
        "root_context": p,
        "equation_rank": raw["equation_rank"],
        "equation_numerator": raw["equation_numerator"],
        "equation_denominator": raw["equation_denominator"],
        "mark_kind_code": raw["mark_kind_code"],
        "mark_root_context": raw["mark_root_context"],
        "mark_equation_rank": raw["mark_equation_rank"],
    }
    if not (
        _plain_int(p)
        and raw["equation_rank"] == p
        and raw["equation_numerator"] == 4
        and raw["equation_denominator"] == p
        and raw["mark_kind_code"] == 1
        and raw["mark_root_context"] == p
        and raw["mark_equation_rank"] == p
    ):
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "raw input does not define the canonical marked 4/p root problem",
        )
    digest = canonical_digest_v1(payload)
    return _freeze_json(payload), ROOT_PROBLEM_ID_PREFIX + digest, digest


def _deterministic_initial_branch_replay_digest_v1(
    *,
    raw: Mapping[str, Any],
    raw_digest: str,
    root_problem_id: str,
    root_problem_digest: str,
    body_mapping: Mapping[str, Any],
    anchor_mapping: Mapping[str, Any],
    state_mapping: Mapping[str, Any],
) -> tuple[Mapping[str, Any], str]:
    if not (
        raw["q"] == 1
        and raw["endpoint_fiber_code"] == 2
        and raw["major_phase_code"] == 3
        and raw["provenance_code"] == 1
        and raw["gap_three_x"] == (raw["root_context"] + 3) // 4
        and body_mapping.get("root_context") == raw["root_context"]
        and body_mapping.get("q") == 1
        and body_mapping.get("endpoint_fiber_code") == 2
        and body_mapping.get("major_phase_code") == 3
        and body_mapping.get("provenance_code") == 1
        and body_mapping.get("mark_kind_code") == 1
        and body_mapping.get("gap_three_factorization")
        == raw["gap_three_factorization"]
        and anchor_mapping.get("body_id") == body_mapping.get("body_id")
        and anchor_mapping.get("body_digest") == body_mapping.get("digest")
        and state_mapping.get("body_id") == body_mapping.get("body_id")
        and state_mapping.get("body_digest") == body_mapping.get("digest")
        and state_mapping.get("root_context") == raw["root_context"]
        and state_mapping.get("q") == 1
        and state_mapping.get("endpoint_fiber_code") == 2
        and state_mapping.get("major_phase_code") == 3
        and state_mapping.get("provenance_code") == 1
        and state_mapping.get("mark_kind_code") == 1
        and state_mapping.get("initializer_authority") is False
        and state_mapping.get("admission_authority") is False
        and state_mapping.get("queue_authority") is False
    ):
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "fresh root artifacts do not replay the deterministic initial q=1 G branch",
        )
    payload = {
            "schema_id": "q1_deterministic_initial_g_branch_replay_v1",
            "root_problem_id": root_problem_id,
            "root_problem_digest": root_problem_digest,
            "raw_q_one_g_digest": raw_digest,
            "q": 1,
            "endpoint_fiber_code": 2,
            "major_phase_code": 3,
            "provenance_code": 1,
            "mark_kind_code": 1,
            "gap_three_x": raw["gap_three_x"],
            "gap_three_factorization": raw["gap_three_factorization"],
            "body_id": body_mapping["body_id"],
            "body_digest": body_mapping["digest"],
            "anchor_id": anchor_mapping["anchor_id"],
            "anchor_digest": anchor_mapping["digest"],
            "state_id": state_mapping["state_id"],
            "state_digest": state_mapping["digest"],
            "state_authority": {
                "initializer_authority": False,
                "persistent_admission": False,
                "queue_authority": False,
            },
        }
    return _freeze_json(payload), canonical_digest_v1(payload)


_ACTUALNESS_CLASSES = frozenset({QOneRootSourceActualnessReceiptV1})
_TOP_RECEIPT_CLASSES = frozenset(
    {
        ProductionQOneRootTerminalReceiptV1,
        ProductionQOneRegisteredPrefixMissReceiptV1,
    }
)


def _external_value_v1(value: Any) -> Any:
    if type(value) is QOneRootSourceActualnessReceiptV1:
        return actualness_receipt_to_mapping_v1(value)
    return _json_copy(value)


def _unsigned_artifact_mapping_v1(
    cls: type[Any],
    values: Mapping[str, Any],
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "receipt_type": cls.ARTIFACT_TYPE,
        "schema_version": SCHEMA_VERSION,
    }
    for field in fields(cls):
        if field.name in {cls.ID_FIELD, "digest"}:
            continue
        payload[field.name] = _external_value_v1(values[field.name])
    return payload


def _construct_artifact_v1(cls: type[Any], values: Mapping[str, Any]) -> Any:
    instance = object.__new__(cls)
    for field in fields(cls):
        object.__setattr__(instance, field.name, values[field.name])
    return instance


def _seal_artifact_v1(cls: type[Any], values: Mapping[str, Any]) -> Any:
    mutable = dict(values)
    digest = canonical_digest_v1(_unsigned_artifact_mapping_v1(cls, mutable))
    mutable[cls.ID_FIELD] = cls.ID_PREFIX + digest
    mutable["digest"] = digest
    artifact = _construct_artifact_v1(cls, mutable)
    _verify_artifact_seal_v1(artifact)
    return artifact


def _validate_actualness_v1(receipt: QOneRootSourceActualnessReceiptV1) -> None:
    if type(receipt) is not QOneRootSourceActualnessReceiptV1:
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            "actualness must have the exact issuer receipt class",
        )
    for field in fields(QOneRootSourceActualnessReceiptV1):
        try:
            getattr(receipt, field.name)
        except AttributeError as exc:
            raise QOneTerminalIssuerError(
                QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
                f"actualness.{field.name} is missing",
            ) from exc
    _require_git_oid(receipt.head_sha, "actualness.head_sha")
    _require_git_oid(receipt.head_tree_sha, "actualness.head_tree_sha")
    if len(receipt.head_sha) != len(receipt.head_tree_sha):
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            "actualness HEAD and tree object formats differ",
        )
    if receipt.v3_registry_id != V3_REGISTRY_ID:
        _reject(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            "actualness V3 registry ID changed",
        )
    if (
        receipt.initializer_grant_id != INITIALIZER_GRANT_ID
        or receipt.initializer_artifact_id != INITIALIZER_ARTIFACT_ID
        or receipt.issuer_grant_id != ISSUER_GRANT_ID
        or receipt.issuer_artifact_id != ISSUER_ARTIFACT_ID
    ):
        _reject(
            QOneTerminalIssuerRejectCode.GRANT_ERROR,
            "actualness initializer or issuer grant binding changed",
        )
    for name in (
        "v3_registry_digest",
        "v3_role_manifest_digest",
        "initializer_grant_digest",
        "initializer_artifact_semantic_sha256",
        "issuer_grant_digest",
        "issuer_artifact_semantic_sha256",
        "fresh_module_binding_digest",
        "root_problem_digest",
        "raw_q_one_g_digest",
        "deterministic_initial_branch_replay_digest",
        "body_digest",
        "anchor_digest",
        "state_digest",
        "initializer_contract_digest",
        "domain_replay_digest",
    ):
        _require_digest(getattr(receipt, name), f"actualness.{name}")
    raw = _validate_raw_q_one_g_v1(receipt.raw_q_one_g)
    expected_root_problem, expected_root_id, expected_root_digest = _root_problem_v1(raw)
    if not (
        _json_copy(receipt.root_problem) == _json_copy(expected_root_problem)
        and receipt.root_problem_id == expected_root_id
        and receipt.root_problem_digest == expected_root_digest
        and receipt.raw_q_one_g_digest == canonical_digest_v1(raw)
    ):
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "actualness root problem or raw q1G preimage does not replay",
        )
    expected_branch = {
        "schema_id": "q1_deterministic_initial_g_branch_replay_v1",
        "root_problem_id": receipt.root_problem_id,
        "root_problem_digest": receipt.root_problem_digest,
        "raw_q_one_g_digest": receipt.raw_q_one_g_digest,
        "q": 1,
        "endpoint_fiber_code": 2,
        "major_phase_code": 3,
        "provenance_code": 1,
        "mark_kind_code": 1,
        "gap_three_x": raw["gap_three_x"],
        "gap_three_factorization": raw["gap_three_factorization"],
        "body_id": receipt.body_id,
        "body_digest": receipt.body_digest,
        "anchor_id": receipt.anchor_id,
        "anchor_digest": receipt.anchor_digest,
        "state_id": receipt.state_id,
        "state_digest": receipt.state_digest,
        "state_authority": {
            "initializer_authority": False,
            "persistent_admission": False,
            "queue_authority": False,
        },
    }
    if not (
        _json_copy(receipt.deterministic_initial_branch_replay) == expected_branch
        and receipt.deterministic_initial_branch_replay_digest
        == canonical_digest_v1(expected_branch)
    ):
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "actualness deterministic initial branch preimage does not replay",
        )
    _require_content_id(
        receipt.root_problem_id,
        "actualness.root_problem_id",
        ROOT_PROBLEM_ID_PREFIX,
    )
    _require_content_id(receipt.body_id, "actualness.body_id", BODY_ID_PREFIX)
    _require_content_id(receipt.anchor_id, "actualness.anchor_id", ANCHOR_ID_PREFIX)
    _require_content_id(receipt.state_id, "actualness.state_id", STATE_ID_PREFIX)
    if not (
        receipt.root_problem_id == ROOT_PROBLEM_ID_PREFIX + receipt.root_problem_digest
        and receipt.body_id == BODY_ID_PREFIX + receipt.body_digest
        and receipt.anchor_id == ANCHOR_ID_PREFIX + receipt.anchor_digest
        and receipt.state_id == STATE_ID_PREFIX + receipt.state_digest
    ):
        _reject(
            QOneTerminalIssuerRejectCode.ID_MISMATCH,
            "actualness content IDs disagree with their digests",
        )
    if not (
        receipt.initializer_id == "q_one_root_initializer_envelope_v2"
        and receipt.owner_domain_id == OWNER_DOMAIN_ID
        and receipt.occurrence_kind == OCCURRENCE_KIND
        and receipt.parent_kind == PARENT_KIND
        and receipt.actualness_scope == ACTUALNESS_SCOPE
        and receipt.actualness_attestor_role == ACTUALNESS_ATTESTOR_ROLE
    ):
        _reject(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            "actualness root initializer semantics changed",
        )
    _require_exact_bool(
        receipt.initializer_output_self_authorizing,
        False,
        "actualness.initializer_output_self_authorizing",
    )
    _require_exact_bool(receipt.source_actualness, True, "actualness.source_actualness")
    _require_exact_bool(
        receipt.root_initializer_authority,
        True,
        "actualness.root_initializer_authority",
    )
    _require_exact_bool(
        receipt.terminal_issuer_attestation_authority,
        True,
        "actualness.terminal_issuer_attestation_authority",
    )
    for name in (
        "persistent_admission",
        "common_owner_authority",
        "e1_authority",
        "queue_authority",
    ):
        _require_exact_bool(getattr(receipt, name), False, f"actualness.{name}")
    _require_content_id(
        receipt.actualness_id,
        "actualness.actualness_id",
        ACTUALNESS_ID_PREFIX,
    )
    _require_digest(receipt.digest, "actualness.digest")


def _certificate_mapping_v1(value: Any, root_context: int) -> Mapping[str, Any]:
    fields_expected = frozenset(
        {"certificate_type", "gap", "x", "divisor", "y", "z", "candidate_index"}
    )
    if type(value) not in {dict, _MAPPING_PROXY_TYPE} or frozenset(value) != fields_expected:
        _reject(
            QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
            "selected certificate has the wrong exact field set",
        )
    plain = _json_copy(value)
    if plain["certificate_type"] not in {"TYPE_I", "TYPE_II"} or type(
        plain["certificate_type"]
    ) is not str:
        _reject(
            QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
            "selected certificate type changed",
        )
    for name in fields_expected - {"certificate_type"}:
        if not _plain_int(plain[name]):
            _reject(
                QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
                f"selected certificate {name} must be a plain integer",
            )
    x, y, z = plain["x"], plain["y"], plain["z"]
    divisor = plain["divisor"]
    gap = plain["gap"]
    if not (
        gap in ORDERED_GAPS
        and x == (root_context + gap) // 4
        and divisor > 0
        and y > 0
        and z > 0
    ):
        _reject(
            QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
            "selected certificate has invalid gap, denominator, or positivity",
        )
    square_divisors = [1]
    for prime, exponent in _factor_trial_v1(x):
        square_divisors = [
            base * prime**power
            for base in square_divisors
            for power in range(2 * exponent + 1)
        ]
    square_divisors = sorted(set(square_divisors))
    if divisor not in square_divisors:
        _reject(
            QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
            "selected certificate divisor does not divide x^2",
        )
    divisor_index = square_divisors.index(divisor)
    if plain["certificate_type"] == "TYPE_I":
        numerator_y = root_context * x + divisor
        numerator_z = root_context * (x + root_context * x * x // divisor)
        expected_index = 2 * divisor_index
        valid_formula = (
            x * x % divisor == 0
            and numerator_y % gap == 0
            and numerator_z % gap == 0
            and y == numerator_y // gap
            and z == numerator_z // gap
        )
    else:
        numerator_y = root_context * (x + divisor)
        numerator_z = root_context * (x + x * x // divisor)
        expected_index = 2 * divisor_index + 1
        valid_formula = (
            x * x % divisor == 0
            and divisor <= x
            and (x + divisor) % gap == 0
            and numerator_y % gap == 0
            and numerator_z % gap == 0
            and y == numerator_y // gap
            and z == numerator_z // gap
        )
    if not (
        plain["candidate_index"] == expected_index
        and valid_formula
        and 4 * x * y * z == root_context * (x * y + x * z + y * z)
    ):
        _reject(
            QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
            "selected certificate does not verify the root equation",
        )
    return _freeze_json(plain)


def _validate_receipt_common_v1(receipt: ProductionReceiptV1) -> None:
    cls = type(receipt)
    if cls not in _TOP_RECEIPT_CLASSES:
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            "production receipt must have one exact issuer class",
        )
    for field in fields(cls):
        try:
            getattr(receipt, field.name)
        except AttributeError as exc:
            raise QOneTerminalIssuerError(
                QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
                f"{cls.ARTIFACT_TYPE}.{field.name} is missing",
            ) from exc
    _require_git_oid(receipt.head_sha, "receipt.head_sha")
    _require_git_oid(receipt.head_tree_sha, "receipt.head_tree_sha")
    if len(receipt.head_sha) != len(receipt.head_tree_sha):
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            "receipt HEAD and tree object formats differ",
        )
    if receipt.v2_registry_id != V2_REGISTRY_ID or receipt.v3_registry_id != V3_REGISTRY_ID:
        _reject(
            QOneTerminalIssuerRejectCode.CROSS_REGISTRY_ERROR,
            "receipt registry IDs changed",
        )
    expected_grant_ids = {
        "initializer_grant_id": INITIALIZER_GRANT_ID,
        "issuer_grant_id": ISSUER_GRANT_ID,
        "scheduler_grant_id": SCHEDULER_GRANT_ID,
        "coverage_verifier_grant_id": COVERAGE_GRANT_ID,
    }
    for name, expected in expected_grant_ids.items():
        if getattr(receipt, name) != expected:
            _reject(
                QOneTerminalIssuerRejectCode.GRANT_ERROR,
                f"receipt {name} changed",
            )
    for name in (
        "v2_registry_digest",
        "v2_role_manifest_digest",
        "v3_registry_digest",
        "v3_role_manifest_digest",
        "cross_registry_equivalence_digest",
        "initializer_grant_digest",
        "initializer_artifact_semantic_sha256",
        "issuer_grant_digest",
        "issuer_artifact_semantic_sha256",
        "scheduler_grant_digest",
        "scheduler_artifact_semantic_sha256",
        "coverage_verifier_grant_digest",
        "coverage_verifier_artifact_semantic_sha256",
        "fresh_module_binding_digest",
        "root_actualness_digest",
        "root_problem_digest",
        "raw_q_one_g_digest",
        "deterministic_initial_branch_replay_digest",
        "body_digest",
        "anchor_digest",
        "state_digest",
        "assembler_artifact_semantic_sha256",
        "assembler_module_binding_digest",
        "assembler_decision_digest",
        "assembler_evidence_digest",
        "assembler_coverage_replay_digest",
        "schedule_digest",
    ):
        _require_digest(getattr(receipt, name), f"receipt.{name}")
    _verify_artifact_seal_v1(receipt.root_actualness)
    if not (
        receipt.root_actualness_digest == receipt.root_actualness.digest
        and receipt.root_actualness.head_sha == receipt.head_sha
        and receipt.root_actualness.head_tree_sha == receipt.head_tree_sha
        and receipt.root_actualness.v3_registry_digest == receipt.v3_registry_digest
        and receipt.root_actualness.v3_role_manifest_digest
        == receipt.v3_role_manifest_digest
        and receipt.root_actualness.initializer_grant_id
        == receipt.initializer_grant_id
        and receipt.root_actualness.initializer_grant_digest
        == receipt.initializer_grant_digest
        and receipt.root_actualness.initializer_artifact_semantic_sha256
        == receipt.initializer_artifact_semantic_sha256
        and receipt.root_actualness.issuer_grant_id == receipt.issuer_grant_id
        and receipt.root_actualness.issuer_grant_digest
        == receipt.issuer_grant_digest
        and receipt.root_actualness.issuer_artifact_semantic_sha256
        == receipt.issuer_artifact_semantic_sha256
        and receipt.root_actualness.fresh_module_binding_digest
        == receipt.fresh_module_binding_digest
        and receipt.root_actualness.root_problem_id == receipt.root_problem_id
        and receipt.root_actualness.root_problem_digest == receipt.root_problem_digest
        and receipt.root_actualness.raw_q_one_g_digest == receipt.raw_q_one_g_digest
        and receipt.root_actualness.deterministic_initial_branch_replay_digest
        == receipt.deterministic_initial_branch_replay_digest
        and receipt.root_actualness.body_id == receipt.body_id
        and receipt.root_actualness.body_digest == receipt.body_digest
        and receipt.root_actualness.anchor_id == receipt.anchor_id
        and receipt.root_actualness.anchor_digest == receipt.anchor_digest
        and receipt.root_actualness.state_id == receipt.state_id
        and receipt.root_actualness.state_digest == receipt.state_digest
    ):
        _reject(
            QOneTerminalIssuerRejectCode.DECISION_BINDING_ERROR,
            "top receipt and nested actualness differ",
        )
    assembler_id_prefix = (
        "root-terminal-hit-evidence:"
        if type(receipt) is ProductionQOneRootTerminalReceiptV1
        else "prefix-miss-evidence:"
    )
    _require_content_id(
        receipt.assembler_decision_id,
        "receipt.assembler_decision_id",
        assembler_id_prefix,
    )
    if receipt.assembler_decision_id != assembler_id_prefix + receipt.assembler_decision_digest:
        _reject(
            QOneTerminalIssuerRejectCode.ID_MISMATCH,
            "assembler decision ID differs from its bound digest",
        )
    _require_content_id(receipt.root_problem_id, "receipt.root_problem_id", ROOT_PROBLEM_ID_PREFIX)
    _require_content_id(receipt.body_id, "receipt.body_id", BODY_ID_PREFIX)
    _require_content_id(receipt.anchor_id, "receipt.anchor_id", ANCHOR_ID_PREFIX)
    _require_content_id(receipt.state_id, "receipt.state_id", STATE_ID_PREFIX)
    if not (
        receipt.root_problem_id == ROOT_PROBLEM_ID_PREFIX + receipt.root_problem_digest
        and receipt.body_id == BODY_ID_PREFIX + receipt.body_digest
        and receipt.anchor_id == ANCHOR_ID_PREFIX + receipt.anchor_digest
        and receipt.state_id == STATE_ID_PREFIX + receipt.state_digest
        and receipt.subject_kind == SUBJECT_KIND
        and _plain_int(receipt.root_context)
        and receipt.root_context >= 2
        and receipt.assembler_artifact_id == ASSEMBLER_ARTIFACT_ID
        and receipt.schedule_id == SCHEDULE_ID
    ):
        _reject(
            QOneTerminalIssuerRejectCode.DECISION_BINDING_ERROR,
            "receipt source, assembler, or schedule binding changed",
        )
    for name in (
        "source_actualness",
        "root_initializer_authority",
        "issuer_authority",
        "issued_under_terminal_issuer",
    ):
        _require_exact_bool(getattr(receipt, name), True, f"receipt.{name}")
    for name in (
        "persistent_admission",
        "common_owner_authority",
        "e1_authority",
        "queue_authority",
        "producer_continuation_allowed",
    ):
        _require_exact_bool(getattr(receipt, name), False, f"receipt.{name}")
    _require_content_id(receipt.receipt_id, "receipt.receipt_id", cls.ID_PREFIX)
    _require_digest(receipt.digest, "receipt.digest")


def _validate_top_receipt_v1(receipt: ProductionReceiptV1) -> None:
    _validate_receipt_common_v1(receipt)
    if type(receipt) is ProductionQOneRootTerminalReceiptV1:
        if not (
            receipt.outcome == HIT_OUTCOME
            and receipt.root_outcome_kind == ROOT_OUTCOME_KIND
        ):
            _reject(
                QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
                "root terminal outcome changed",
            )
        certificate = _certificate_mapping_v1(
            receipt.selected_certificate,
            receipt.root_context,
        )
        if receipt.selected_certificate_digest != canonical_digest_v1(certificate):
            _reject(
                QOneTerminalIssuerRejectCode.DIGEST_MISMATCH,
                "root terminal certificate digest does not replay",
            )
        equation = _json_copy(receipt.root_equation)
        expected_equation = {
            "root_context": receipt.root_context,
            "equation_numerator": 4,
            "equation_denominator": receipt.root_context,
            "x": certificate["x"],
            "y": certificate["y"],
            "z": certificate["z"],
        }
        if equation != expected_equation or receipt.root_equation_digest != canonical_digest_v1(
            expected_equation
        ):
            _reject(
                QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
                "root equation receipt differs from the selected certificate",
            )
        _require_exact_bool(
            receipt.terminal_leaf_authority,
            True,
            "receipt.terminal_leaf_authority",
        )
        _require_exact_bool(
            receipt.registered_prefix_miss_authority,
            False,
            "receipt.registered_prefix_miss_authority",
        )
        _require_exact_bool(
            receipt.root_proof_close_authority,
            True,
            "receipt.root_proof_close_authority",
        )
        _require_exact_bool(
            receipt.global_exhaustion,
            False,
            "receipt.global_exhaustion",
        )
    else:
        if not (
            receipt.outcome == MISS_OUTCOME
            and receipt.coverage_semantics == COVERAGE_SEMANTICS
            and type(receipt.ordered_gaps) is tuple
            and receipt.ordered_gaps == ORDERED_GAPS
            and _plain_int(receipt.next_unchecked_gap)
            and receipt.next_unchecked_gap == NEXT_UNCHECKED_GAP
            and receipt.global_exhaustion is False
            and receipt.selected_certificate is None
            and receipt.selected_certificate_digest is None
        ):
            _reject(
                QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
                "registered-prefix miss scope or selected terminal changed",
            )
        _require_exact_bool(
            receipt.terminal_leaf_authority,
            False,
            "receipt.terminal_leaf_authority",
        )
        _require_exact_bool(
            receipt.registered_prefix_miss_authority,
            True,
            "receipt.registered_prefix_miss_authority",
        )
        _require_exact_bool(
            receipt.root_proof_close_authority,
            False,
            "receipt.root_proof_close_authority",
        )


def _verify_artifact_seal_v1(value: Any) -> None:
    if type(value) is QOneRootSourceActualnessReceiptV1:
        _validate_actualness_v1(value)
    elif type(value) in _TOP_RECEIPT_CLASSES:
        _validate_top_receipt_v1(value)
    else:
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            "value is not an exact issuer artifact class",
        )
    cls = type(value)
    values = {field.name: getattr(value, field.name) for field in fields(cls)}
    expected_digest = canonical_digest_v1(_unsigned_artifact_mapping_v1(cls, values))
    if value.digest != expected_digest:
        _reject(
            QOneTerminalIssuerRejectCode.DIGEST_MISMATCH,
            f"{cls.ARTIFACT_TYPE}.digest does not replay",
        )
    if getattr(value, cls.ID_FIELD) != cls.ID_PREFIX + expected_digest:
        _reject(
            QOneTerminalIssuerRejectCode.ID_MISMATCH,
            f"{cls.ARTIFACT_TYPE}.{cls.ID_FIELD} does not replay",
        )


def actualness_receipt_to_mapping_v1(
    receipt: QOneRootSourceActualnessReceiptV1,
) -> dict[str, Any]:
    _verify_artifact_seal_v1(receipt)
    cls = type(receipt)
    values = {field.name: getattr(receipt, field.name) for field in fields(cls)}
    result = _unsigned_artifact_mapping_v1(cls, values)
    result[cls.ID_FIELD] = receipt.actualness_id
    result["digest"] = receipt.digest
    return result


def production_terminal_receipt_to_mapping_v1(
    receipt: ProductionReceiptV1,
) -> dict[str, Any]:
    if type(receipt) not in _TOP_RECEIPT_CLASSES:
        _reject(
            QOneTerminalIssuerRejectCode.MALFORMED_FIELD,
            "serializer accepts only exact production receipt classes",
        )
    _verify_artifact_seal_v1(receipt)
    cls = type(receipt)
    values = {field.name: getattr(receipt, field.name) for field in fields(cls)}
    result = _unsigned_artifact_mapping_v1(cls, values)
    result[cls.ID_FIELD] = receipt.receipt_id
    result["digest"] = receipt.digest
    return result


def _bind_fresh_modules_to_v3_v1(
    module_binding: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any]],
) -> None:
    files = module_binding.get("files")
    if type(files) is not list:
        _reject(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            "fresh module binding files must be a list",
        )
    file_map = {item.get("path"): item for item in files if type(item) is dict}
    expected = (
        (ISSUER_ARTIFACT_ID, ISSUER_PATH),
        (V2_RESOLVER_ARTIFACT_ID, V2_RESOLVER_PATH),
        (INITIALIZER_ARTIFACT_ID, ROOT_ENVELOPE_PATH),
        (ASSEMBLER_ARTIFACT_ID, ASSEMBLER_PATH),
    )
    for artifact_id, path in expected:
        artifact = artifacts[artifact_id]
        file_binding = file_map.get(path)
        if not (
            artifact.get("path") == path
            and type(file_binding) is dict
            and file_binding.get("blob_sha256") == artifact.get("blob_sha256")
            and file_binding.get("git_object_id") == artifact.get("git_object_id")
            and file_binding.get("git_mode") == artifact.get("git_mode")
        ):
            _reject(
                QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
                f"fresh {artifact_id} module does not match its V3 artifact pin",
            )


def _build_actualness_values_v1(
    *,
    v3: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any]],
    grants: Mapping[str, Mapping[str, Any]],
    module_binding_digest: str,
    root_problem: Mapping[str, Any],
    root_problem_id: str,
    root_problem_digest: str,
    raw_q_one_g: Mapping[str, Any],
    raw_digest: str,
    branch_replay: Mapping[str, Any],
    branch_replay_digest: str,
    body: Mapping[str, Any],
    anchor: Mapping[str, Any],
    state: Mapping[str, Any],
) -> dict[str, Any]:
    initializer_grant = grants[ROLE_INITIALIZER]
    issuer_grant = grants[ROLE_ISSUER]
    return {
        "head_sha": v3["head_sha"],
        "head_tree_sha": v3["head_tree_sha"],
        "v3_registry_id": V3_REGISTRY_ID,
        "v3_registry_digest": v3["registry_digest"],
        "v3_role_manifest_digest": v3["role_authority_manifest"]["digest"],
        "initializer_grant_id": INITIALIZER_GRANT_ID,
        "initializer_grant_digest": _grant_digest_v1(initializer_grant),
        "initializer_artifact_id": INITIALIZER_ARTIFACT_ID,
        "initializer_artifact_semantic_sha256": artifacts[INITIALIZER_ARTIFACT_ID][
            "semantic_sha256"
        ],
        "issuer_grant_id": ISSUER_GRANT_ID,
        "issuer_grant_digest": _grant_digest_v1(issuer_grant),
        "issuer_artifact_id": ISSUER_ARTIFACT_ID,
        "issuer_artifact_semantic_sha256": artifacts[ISSUER_ARTIFACT_ID][
            "semantic_sha256"
        ],
        "fresh_module_binding_digest": module_binding_digest,
        "root_problem": _freeze_json(root_problem),
        "root_problem_id": root_problem_id,
        "root_problem_digest": root_problem_digest,
        "raw_q_one_g": _freeze_json(raw_q_one_g),
        "raw_q_one_g_digest": raw_digest,
        "deterministic_initial_branch_replay": _freeze_json(branch_replay),
        "deterministic_initial_branch_replay_digest": branch_replay_digest,
        "body_id": body["body_id"],
        "body_digest": body["digest"],
        "anchor_id": anchor["anchor_id"],
        "anchor_digest": anchor["digest"],
        "state_id": state["state_id"],
        "state_digest": state["digest"],
        "initializer_id": anchor["initializer_id"],
        "initializer_contract_digest": anchor["contract_digest"],
        "domain_replay_id": anchor["domain_replay_id"],
        "domain_replay_digest": anchor["domain_replay_digest"],
        "owner_domain_id": OWNER_DOMAIN_ID,
        "occurrence_kind": OCCURRENCE_KIND,
        "parent_kind": PARENT_KIND,
        "actualness_scope": ACTUALNESS_SCOPE,
        "initializer_output_self_authorizing": False,
        "actualness_attestor_role": ACTUALNESS_ATTESTOR_ROLE,
        "source_actualness": True,
        "root_initializer_authority": True,
        "terminal_issuer_attestation_authority": True,
        "persistent_admission": False,
        "common_owner_authority": False,
        "e1_authority": False,
        "queue_authority": False,
    }


def _common_top_values_v1(
    *,
    v2: Mapping[str, Any],
    v3: Mapping[str, Any],
    cross_digest: str,
    artifacts: Mapping[str, Mapping[str, Any]],
    grants: Mapping[str, Mapping[str, Any]],
    module_binding_digest: str,
    actualness: QOneRootSourceActualnessReceiptV1,
    decision: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "head_sha": v3["head_sha"],
        "head_tree_sha": v3["head_tree_sha"],
        "v2_registry_id": V2_REGISTRY_ID,
        "v2_registry_digest": v2["registry_digest"],
        "v2_role_manifest_digest": v2["role_authority_manifest"]["digest"],
        "v3_registry_id": V3_REGISTRY_ID,
        "v3_registry_digest": v3["registry_digest"],
        "v3_role_manifest_digest": v3["role_authority_manifest"]["digest"],
        "cross_registry_equivalence_digest": cross_digest,
        "initializer_grant_id": INITIALIZER_GRANT_ID,
        "initializer_grant_digest": _grant_digest_v1(grants[ROLE_INITIALIZER]),
        "initializer_artifact_semantic_sha256": artifacts[INITIALIZER_ARTIFACT_ID][
            "semantic_sha256"
        ],
        "issuer_grant_id": ISSUER_GRANT_ID,
        "issuer_grant_digest": _grant_digest_v1(grants[ROLE_ISSUER]),
        "issuer_artifact_semantic_sha256": artifacts[ISSUER_ARTIFACT_ID][
            "semantic_sha256"
        ],
        "scheduler_grant_id": SCHEDULER_GRANT_ID,
        "scheduler_grant_digest": _grant_digest_v1(grants[ROLE_SCHEDULER]),
        "scheduler_artifact_semantic_sha256": artifacts[SCHEDULER_ARTIFACT_ID][
            "semantic_sha256"
        ],
        "coverage_verifier_grant_id": COVERAGE_GRANT_ID,
        "coverage_verifier_grant_digest": _grant_digest_v1(grants[ROLE_COVERAGE]),
        "coverage_verifier_artifact_semantic_sha256": artifacts[
            COVERAGE_ARTIFACT_ID
        ]["semantic_sha256"],
        "fresh_module_binding_digest": module_binding_digest,
        "root_actualness": actualness,
        "root_actualness_digest": actualness.digest,
        "root_problem_id": actualness.root_problem_id,
        "root_problem_digest": actualness.root_problem_digest,
        "raw_q_one_g_digest": actualness.raw_q_one_g_digest,
        "deterministic_initial_branch_replay_digest": actualness.deterministic_initial_branch_replay_digest,
        "body_id": actualness.body_id,
        "body_digest": actualness.body_digest,
        "anchor_id": actualness.anchor_id,
        "anchor_digest": actualness.anchor_digest,
        "state_id": actualness.state_id,
        "state_digest": actualness.state_digest,
        "subject_kind": SUBJECT_KIND,
        "root_context": decision["root_context"],
        "assembler_artifact_id": ASSEMBLER_ARTIFACT_ID,
        "assembler_artifact_semantic_sha256": artifacts[ASSEMBLER_ARTIFACT_ID][
            "semantic_sha256"
        ],
        "assembler_module_binding_digest": decision["module_binding_digest"],
        "assembler_decision_id": decision["decision_id"],
        "assembler_decision_digest": decision["digest"],
        "assembler_evidence_digest": decision["scheduler_evidence_digest"],
        "assembler_coverage_replay_digest": decision["coverage_replay_digest"],
        "schedule_id": decision["schedule_id"],
        "schedule_digest": decision["schedule_digest"],
        "source_actualness": True,
        "root_initializer_authority": True,
        "issuer_authority": True,
        "issued_under_terminal_issuer": True,
        "persistent_admission": False,
        "common_owner_authority": False,
        "e1_authority": False,
        "queue_authority": False,
        "producer_continuation_allowed": False,
    }


def _issue_from_assembler_decision_v1(
    *,
    common: Mapping[str, Any],
    decision: Mapping[str, Any],
) -> ProductionReceiptV1:
    if decision["outcome"] == ASSEMBLER_HIT_OUTCOME:
        certificate = _certificate_mapping_v1(
            decision["selected_certificate"],
            decision["root_context"],
        )
        if decision["selected_certificate_digest"] != canonical_digest_v1(certificate):
            _reject(
                QOneTerminalIssuerRejectCode.DECISION_BINDING_ERROR,
                "assembler selected-certificate digest does not replay",
            )
        root_equation = _freeze_json(
            {
                "root_context": decision["root_context"],
                "equation_numerator": 4,
                "equation_denominator": decision["root_context"],
                "x": certificate["x"],
                "y": certificate["y"],
                "z": certificate["z"],
            }
        )
        return _seal_artifact_v1(
            ProductionQOneRootTerminalReceiptV1,
            {
                **dict(common),
                "outcome": HIT_OUTCOME,
                "root_outcome_kind": ROOT_OUTCOME_KIND,
                "selected_certificate": certificate,
                "selected_certificate_digest": canonical_digest_v1(certificate),
                "root_equation": root_equation,
                "root_equation_digest": canonical_digest_v1(root_equation),
                "global_exhaustion": False,
                "terminal_leaf_authority": True,
                "registered_prefix_miss_authority": False,
                "root_proof_close_authority": True,
            },
        )
    if decision["outcome"] == ASSEMBLER_MISS_OUTCOME:
        if decision.get("selected_certificate") is not None or decision.get(
            "selected_certificate_digest"
        ) is not None:
            _reject(
                QOneTerminalIssuerRejectCode.DECISION_BINDING_ERROR,
                "assembler prefix miss carries a selected certificate",
            )
        return _seal_artifact_v1(
            ProductionQOneRegisteredPrefixMissReceiptV1,
            {
                **dict(common),
                "outcome": MISS_OUTCOME,
                "coverage_semantics": COVERAGE_SEMANTICS,
                "ordered_gaps": ORDERED_GAPS,
                "next_unchecked_gap": NEXT_UNCHECKED_GAP,
                "global_exhaustion": False,
                "selected_certificate": None,
                "selected_certificate_digest": None,
                "terminal_leaf_authority": False,
                "registered_prefix_miss_authority": True,
                "root_proof_close_authority": False,
            },
        )
    _reject(
        QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
        f"assembler returned unknown outcome {decision.get('outcome')!r}",
    )


def _verify_assembler_decision_v1(
    decision: Any,
    *,
    head_sha: str,
    tree_sha: str,
    v2: Mapping[str, Any],
    v2_artifacts: Mapping[str, Mapping[str, Any]],
    body: Mapping[str, Any],
    anchor: Mapping[str, Any],
    state: Mapping[str, Any],
) -> dict[str, Any]:
    if type(decision) is not dict:
        _reject(
            QOneTerminalIssuerRejectCode.DECISION_BINDING_ERROR,
            "assembler serializer must return an exact dict",
        )
    for name in (
        "digest",
        "registry_digest",
        "role_authority_manifest_digest",
        "schedule_digest",
        "scheduler_grant_digest",
        "scheduler_artifact_semantic_sha256",
        "coverage_verifier_grant_digest",
        "coverage_verifier_artifact_semantic_sha256",
        "module_binding_digest",
        "body_digest",
        "anchor_digest",
        "state_digest",
        "scheduler_domain_digest",
        "scheduler_invocation_digest",
        "scheduler_evidence_digest",
        "coverage_replay_digest",
    ):
        _require_digest(decision.get(name), f"assembler decision.{name}")
    unsigned = _json_copy(decision)
    decision_id = unsigned.pop("decision_id", None)
    digest = unsigned.pop("digest")
    if canonical_digest_v1(unsigned) != digest:
        _reject(
            QOneTerminalIssuerRejectCode.DECISION_BINDING_ERROR,
            "assembler decision digest does not replay",
        )
    artifact_type = decision.get("artifact_type")
    prefix = (
        "root-terminal-hit-evidence:"
        if artifact_type == "QOneRootTerminalHitEvidenceV2"
        else "prefix-miss-evidence:"
        if artifact_type == "QOneRegisteredPrefixMissEvidenceV2"
        else None
    )
    if prefix is None or decision_id != prefix + digest:
        _reject(
            QOneTerminalIssuerRejectCode.DECISION_BINDING_ERROR,
            "assembler decision ID/type does not replay",
        )
    if not (
        decision.get("head_sha") == head_sha
        and decision.get("head_tree_sha") == tree_sha
        and decision.get("registry_id") == V2_REGISTRY_ID
        and decision.get("registry_digest") == v2.get("registry_digest")
        and decision.get("role_authority_manifest_digest")
        == v2.get("role_authority_manifest", {}).get("digest")
        and decision.get("schedule_id") == SCHEDULE_ID
        and decision.get("subject_kind") == SUBJECT_KIND
        and decision.get("body_id") == body.get("body_id")
        and decision.get("body_digest") == body.get("digest")
        and decision.get("anchor_id") == anchor.get("anchor_id")
        and decision.get("anchor_digest") == anchor.get("digest")
        and decision.get("state_id") == state.get("state_id")
        and decision.get("state_digest") == state.get("digest")
        and decision.get("root_context") == state.get("root_context")
        and decision.get("scheduler_artifact_semantic_sha256")
        == v2_artifacts[SCHEDULER_ARTIFACT_ID].get("semantic_sha256")
        and decision.get("coverage_verifier_artifact_semantic_sha256")
        == v2_artifacts[COVERAGE_ARTIFACT_ID].get("semantic_sha256")
        and decision.get("coverage_scope")
        == "REGISTERED_PRIORITY_PREFIX_GAPS_3_7_11"
        and decision.get("global_exhaustion") is False
        and decision.get("next_unchecked_gap") == NEXT_UNCHECKED_GAP
    ):
        _reject(
            QOneTerminalIssuerRejectCode.DECISION_BINDING_ERROR,
            "assembler decision differs from V2 registry or fresh root artifacts",
        )
    for name in (
        "source_actualness",
        "initializer_authority",
        "issuer_authority",
        "terminal_authority",
        "e1_authority",
        "queue_authority",
        "producer_continuation_allowed",
    ):
        _require_exact_bool(decision.get(name), False, f"assembler decision.{name}")
    if decision.get("outcome") == ASSEMBLER_HIT_OUTCOME:
        _certificate_mapping_v1(decision.get("selected_certificate"), state["root_context"])
    elif not (
        decision.get("outcome") == ASSEMBLER_MISS_OUTCOME
        and decision.get("selected_certificate") is None
        and decision.get("selected_certificate_digest") is None
    ):
        _reject(
            QOneTerminalIssuerRejectCode.OUTCOME_ERROR,
            "assembler decision outcome/certificate pairing changed",
        )
    return decision


def issue_q_one_terminal_decision_v1(
    *,
    root: Path,
    requested_head: str,
    raw_q_one_g: dict[str, Any],
) -> ProductionReceiptV1:
    """Issue one exact-HEAD q=1 root terminal or registered-prefix miss receipt."""

    repository = _repository_root_v1(root)
    head_sha, tree_sha = _exact_head_v1(repository, requested_head)
    entries = _tree_entries_v1(repository, head_sha)
    issuer_self = _verify_issuer_self_v1(
        repository,
        head_sha,
        tree_sha,
        entries,
    )
    modules = _load_fresh_modules_v1(
        root=repository,
        head_sha=head_sha,
        entries=entries,
    )
    initial_module_binding = _capture_fresh_module_binding_v1(
        repository,
        head_sha,
        tree_sha,
        entries,
        modules,
        issuer_self,
    )

    resolve_v2 = _require_callable_v1(modules.v2_registry, V2_RESOLVER_SYMBOL)
    resolve_v3 = _require_callable_v1(modules.v3_registry, V3_RESOLVER_SYMBOL)
    v2_error = getattr(modules.v2_registry, "RegistryV2Error", None)
    v3_error = getattr(modules.v3_registry, "RegistryV3Error", None)
    if type(v2_error) is not type or type(v3_error) is not type:
        _reject(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            "fresh registry resolver error types are missing",
        )
    try:
        v2_raw = resolve_v2(root=repository, requested_head=head_sha)
    except v2_error as exc:
        raise QOneTerminalIssuerError(
            QOneTerminalIssuerRejectCode.V2_REGISTRY_ERROR,
            f"V2 registry rejected: {exc}",
        ) from exc
    try:
        v3_raw = resolve_v3(root=repository, requested_head=head_sha)
    except v3_error as exc:
        raise QOneTerminalIssuerError(
            QOneTerminalIssuerRejectCode.V3_REGISTRY_ERROR,
            f"V3 registry rejected: {exc}",
        ) from exc
    v2, v2_artifacts, _v2_grants = _verify_v2_registry_v1(
        v2_raw,
        head_sha=head_sha,
        tree_sha=tree_sha,
    )
    v3, v3_artifacts, v3_grants = _verify_v3_registry_v1(
        v3_raw,
        head_sha=head_sha,
        tree_sha=tree_sha,
    )
    cross_digest = _cross_registry_equivalence_digest_v1(
        v2,
        v3,
        v2_artifacts,
        v3_artifacts,
    )
    _bind_fresh_modules_to_v3_v1(
        initial_module_binding,
        v3_artifacts,
    )

    root_error = getattr(
        modules.root_envelope,
        "RootInitializerValidationError",
        None,
    )
    if type(root_error) is not type:
        _reject(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            "fresh root-envelope error type is missing",
        )
    make_body = _require_callable_v1(
        modules.root_envelope,
        "make_canonical_q_one_g_source_body_v2",
    )
    make_anchor = _require_callable_v1(
        modules.root_envelope,
        "make_root_initializer_anchor_v2",
    )
    make_state = _require_callable_v1(
        modules.root_envelope,
        "make_raw_root_source_state_v2",
    )
    serialize_root = _require_callable_v1(
        modules.root_envelope,
        "artifact_to_mapping_v2",
    )
    try:
        body_object = make_body(raw_q_one_g)
        anchor_object = make_anchor(body_object)
        state_object = make_state(body_object, anchor_object)
        body = serialize_root(body_object)
        anchor = serialize_root(anchor_object)
        state = serialize_root(state_object)
    except root_error as exc:
        raise QOneTerminalIssuerError(
            QOneTerminalIssuerRejectCode.ROOT_INITIALIZER_ERROR,
            f"fresh root initializer rejected: {exc}",
        ) from exc

    raw_canonical = _validate_raw_q_one_g_v1(raw_q_one_g)
    raw_digest = canonical_digest_v1(raw_canonical)
    root_problem, root_problem_id, root_problem_digest = _root_problem_v1(
        raw_canonical
    )
    branch_replay, branch_replay_digest = _deterministic_initial_branch_replay_digest_v1(
        raw=raw_canonical,
        raw_digest=raw_digest,
        root_problem_id=root_problem_id,
        root_problem_digest=root_problem_digest,
        body_mapping=body,
        anchor_mapping=anchor,
        state_mapping=state,
    )

    assemble = _require_callable_v1(modules.assembler, ASSEMBLER_SYMBOL)
    serialize_decision = _require_callable_v1(
        modules.assembler,
        ASSEMBLER_SERIALIZER_SYMBOL,
    )
    assembler_error = getattr(modules.assembler, "TerminalDecisionAssemblerError", None)
    if type(assembler_error) is not type:
        _reject(
            QOneTerminalIssuerRejectCode.MODULE_BINDING_ERROR,
            "fresh assembler error type is missing",
        )
    try:
        decision_object = assemble(
            root=repository,
            requested_head=head_sha,
            raw_q_one_g=raw_canonical,
        )
        decision_raw = serialize_decision(decision_object)
    except assembler_error as exc:
        raise QOneTerminalIssuerError(
            QOneTerminalIssuerRejectCode.ASSEMBLER_ERROR,
            f"fresh assembler rejected: {exc}",
        ) from exc
    decision = _verify_assembler_decision_v1(
        decision_raw,
        head_sha=head_sha,
        tree_sha=tree_sha,
        v2=v2,
        v2_artifacts=v2_artifacts,
        body=body,
        anchor=anchor,
        state=state,
    )

    actualness = _seal_artifact_v1(
        QOneRootSourceActualnessReceiptV1,
        _build_actualness_values_v1(
            v3=v3,
            artifacts=v3_artifacts,
            grants=v3_grants,
            module_binding_digest=initial_module_binding["digest"],
            root_problem=root_problem,
            root_problem_id=root_problem_id,
            root_problem_digest=root_problem_digest,
            raw_q_one_g=raw_canonical,
            raw_digest=raw_digest,
            branch_replay=branch_replay,
            branch_replay_digest=branch_replay_digest,
            body=body,
            anchor=anchor,
            state=state,
        ),
    )
    common = _common_top_values_v1(
        v2=v2,
        v3=v3,
        cross_digest=cross_digest,
        artifacts=v3_artifacts,
        grants=v3_grants,
        module_binding_digest=initial_module_binding["digest"],
        actualness=actualness,
        decision=decision,
    )
    receipt = _issue_from_assembler_decision_v1(
        common=common,
        decision=decision,
    )

    final_module_binding = _capture_fresh_module_binding_v1(
        repository,
        head_sha,
        tree_sha,
        entries,
        modules,
        issuer_self,
    )
    if final_module_binding != initial_module_binding:
        _reject(
            QOneTerminalIssuerRejectCode.WORKTREE_BINDING_ERROR,
            "fresh dependency backing files changed during issuance",
        )
    _verify_artifact_seal_v1(receipt)
    return receipt


__all__ = [
    "HIT_OUTCOME",
    "MISS_OUTCOME",
    "PRODUCTION_RECEIPT_SCHEMA_ID",
    "ProductionQOneRegisteredPrefixMissReceiptV1",
    "ProductionQOneRootTerminalReceiptV1",
    "QOneRootSourceActualnessReceiptV1",
    "QOneTerminalIssuerError",
    "QOneTerminalIssuerRejectCode",
    "actualness_receipt_to_mapping_v1",
    "canonical_digest_v1",
    "canonical_json_v1",
    "issue_q_one_terminal_decision_v1",
    "production_terminal_receipt_to_mapping_v1",
]
