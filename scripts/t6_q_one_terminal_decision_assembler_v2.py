#!/usr/bin/env python3
"""Exact-HEAD, non-authorizing q=1 root terminal-decision assembler V2.

The only assembly API accepts a repository locator, an exact commit ID, and one
raw ordinary q=1 G integer record.  It resolves the fixed coordinator registry,
fresh-loads every dependency implementation from regular blobs at that commit,
constructs the acyclic root source state, derives the scheduler domain from that
state, and runs the authorized scheduler followed by its independent coverage
verifier.

The result is one of two content-addressed evidence objects.  A hit records the
selected root certificate; a miss records that the registered gaps-3/7/11
priority prefix missed.  Both are explicitly non-authorizing.  This module has
no issuer, production receipt, caller-supplied callable/domain/authority table,
runtime, admission, producer-continuation, or queue API.

The executing assembler is the trusted current-process entry.  It verifies that
its backing file matches the requested-HEAD blob, but does not claim the
impossible circular result that already-running assembler code can independently
prove its own pre-import integrity.  All four dependency modules are instead
compiled and executed from exact-HEAD bytes in fresh private namespaces.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, fields
from enum import Enum
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from types import MappingProxyType
from types import ModuleType
from typing import Any, ClassVar, Mapping, NoReturn, Sequence, TypeVar


SCHEMA_VERSION = 2
ASSEMBLER_ID = "t6_q_one_terminal_decision_assembler_v2"
ASSEMBLER_PATH = "scripts/t6_q_one_terminal_decision_assembler_v2.py"
REGISTRY_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v2.py"
ROOT_ENVELOPE_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"
SCHEDULER_PATH = "scripts/t6_q_one_priority_prefix_scheduler_v1.py"
VERIFIER_PATH = "scripts/t6_q_one_priority_prefix_coverage_verifier_v1.py"

EXACT_HEAD_PATHS = (
    ASSEMBLER_PATH,
    REGISTRY_RESOLVER_PATH,
    ROOT_ENVELOPE_PATH,
    SCHEDULER_PATH,
    VERIFIER_PATH,
)
REGULAR_GIT_MODES = frozenset({"100644", "100755"})

EXPECTED_REGISTRY_STATUS = "HEAD_BOUND_PREFIX_SCHEDULE_AUTHORITY_NO_ISSUER"
EXPECTED_REGISTRY_ID = "t6_coordinator_role_registry_v2"
EXPECTED_RESOLVED_SCHEMA_ID = "t6_coordinator_role_registry_resolved_v2"
EXPECTED_EVIDENCE_CLASS = "EXACT_HEAD_NON_AUTHORIZING_TERMINAL_DECISION"
SUBJECT_KIND = "SOURCE_STATE"

SCHEDULE_ID = "q1_root_gap_3_7_11_registered_priority_prefix_v1"
SCHEDULER_ARTIFACT_ID = "q1_priority_prefix_scheduler_v1"
VERIFIER_ARTIFACT_ID = "q1_priority_prefix_coverage_verifier_v1"
SCHEDULER_GRANT_ID = "q1_prefix_terminal_scheduler_grant_v2"
VERIFIER_GRANT_ID = "q1_prefix_independent_coverage_verifier_grant_v2"
SCHEDULER_SYMBOL = "replay_q_one_priority_prefix_v1"
VERIFIER_SYMBOL = "verify_q_one_priority_prefix_coverage_v1"
SCHEDULER_CAPABILITIES = ("REGISTERED_PRIORITY_PREFIX_REPLAY",)
VERIFIER_CAPABILITIES = (
    "CERTIFICATE_VERIFIER",
    "DOMAIN_VERIFIER",
    "ROOT_TERMINAL_VERIFIER",
)
ROLE_AUTHORITY_CLASS = "HEAD_BOUND_EXECUTABLE_CAPABILITY_NO_ISSUER"
SEMANTIC_DIGEST_METHOD = (
    "PYTHON_AST_SYMBOL_BLOB_AND_LOCAL_IMPORT_CLOSURE_SHA256_V2"
)

SCHEDULER_DOMAIN_SCHEMA_ID = "q1_priority_prefix_domain_v1"
SCHEDULER_DOMAIN_SCHEMA_VERSION = 1
SCHEDULER_EVIDENCE_SCHEMA_ID = "t6_q_one_priority_prefix_evidence_v1"
CANDIDATE_ORDER = "gap_ascending_divisor_ascending_type_I_before_II"
COVERAGE_SCOPE = "REGISTERED_PRIORITY_PREFIX_GAPS_3_7_11"
ORDERED_GAPS = (3, 7, 11)
NEXT_UNCHECKED_GAP = 15
SCHEDULER_ROOT_TERMINAL_HIT = "ROOT_TERMINAL_HIT"
SCHEDULER_PREFIX_MISS = "PREFIX_MISS_EVIDENCE_ONLY"
SCHEDULER_BLOCKED = "BLOCKED"
COVERAGE_VERIFIED_STATUS = "PREFIX_COVERAGE_REPLAY_VERIFIED_EVIDENCE_ONLY"

BODY_ID_PREFIX = "q1-source-body:"
ANCHOR_ID_PREFIX = "root-init-anchor:"
STATE_ID_PREFIX = "state:"

ROOT_TERMINAL_HIT_EVIDENCE = "ROOT_TERMINAL_HIT_EVIDENCE"
PREFIX_MISS_EVIDENCE = "PREFIX_MISS_EVIDENCE"

HIT_DECISION_ID_PREFIX = "root-terminal-hit-evidence:"
MISS_DECISION_ID_PREFIX = "prefix-miss-evidence:"

_DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")
_GIT_OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
_MAPPING_PROXY_TYPE = type(MappingProxyType({}))


class TerminalDecisionAssemblerRejectCode(str, Enum):
    """Stable fail-closed categories for assembler failures."""

    HEAD_BINDING_ERROR = "HEAD_BINDING_ERROR"
    MODULE_BINDING_ERROR = "MODULE_BINDING_ERROR"
    WORKTREE_BINDING_ERROR = "WORKTREE_BINDING_ERROR"
    REGISTRY_ERROR = "REGISTRY_ERROR"
    GRANT_ERROR = "GRANT_ERROR"
    DOMAIN_ERROR = "DOMAIN_ERROR"
    EVIDENCE_ERROR = "EVIDENCE_ERROR"
    COVERAGE_ERROR = "COVERAGE_ERROR"
    OUTCOME_ERROR = "OUTCOME_ERROR"
    AUTHORITY_ERROR = "AUTHORITY_ERROR"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    ID_MISMATCH = "ID_MISMATCH"


class TerminalDecisionAssemblerError(ValueError):
    """Assembler rejection with a stable machine-readable code."""

    def __init__(self, code: TerminalDecisionAssemblerRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: TerminalDecisionAssemblerRejectCode, detail: str) -> NoReturn:
    raise TerminalDecisionAssemblerError(code, detail)


def _plain_int(value: Any) -> bool:
    return type(value) is int


def _require_text(value: Any, name: str) -> str:
    if type(value) is not str or not value or value.strip() != value:
        _reject(
            TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty trimmed exact string",
        )
    return value


def _require_digest(value: Any, name: str) -> str:
    if type(value) is not str or _DIGEST_RE.fullmatch(value) is None:
        _reject(
            TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
            f"{name} must be a lowercase SHA-256 digest",
        )
    return value


def _require_git_oid(value: Any, name: str) -> str:
    if type(value) is not str or _GIT_OID_RE.fullmatch(value) is None:
        _reject(
            TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
            f"{name} must be a full lowercase Git object ID",
        )
    return value


def _require_content_id(value: Any, name: str, prefix: str) -> str:
    text = _require_text(value, name)
    if not text.startswith(prefix) or _DIGEST_RE.fullmatch(text[len(prefix) :]) is None:
        _reject(
            TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
            f"{name} must be {prefix!r} followed by a SHA-256 digest",
        )
    return text


def _require_false(value: Any, name: str) -> None:
    if type(value) is not bool or value is not False:
        _reject(
            TerminalDecisionAssemblerRejectCode.AUTHORITY_ERROR,
            f"{name} must be exactly false",
        )


def _json_copy(value: Any, *, path: str = "$") -> Any:
    if type(value) in {dict, _MAPPING_PROXY_TYPE}:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                _reject(
                    TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
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
        TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
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


def canonical_json_v2(value: Any) -> str:
    return json.dumps(
        _json_copy(value),
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def canonical_digest_v2(value: Any) -> str:
    return hashlib.sha256(canonical_json_v2(value).encode("ascii")).hexdigest()


@dataclass(frozen=True, slots=True)
class _GitBlobV2:
    path: str
    git_mode: str
    git_object_id: str
    content: bytes

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.content).hexdigest()


@dataclass(frozen=True, slots=True)
class _FreshModulesV2:
    """Private exact-blob module namespaces used by one assembly call."""

    registry: ModuleType
    root_envelope: ModuleType
    scheduler: ModuleType
    coverage: ModuleType

    def by_path(self) -> Mapping[str, ModuleType]:
        return MappingProxyType(
            {
                REGISTRY_RESOLVER_PATH: self.registry,
                ROOT_ENVELOPE_PATH: self.root_envelope,
                SCHEDULER_PATH: self.scheduler,
                VERIFIER_PATH: self.coverage,
            }
        )


class _FactoryOnlyV2:
    __slots__ = ()

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} must be created by the assembler")


@dataclass(frozen=True, init=False, slots=True)
class QOneRootTerminalHitEvidenceV2(_FactoryOnlyV2):
    ARTIFACT_TYPE: ClassVar[str] = "QOneRootTerminalHitEvidenceV2"
    ID_FIELD: ClassVar[str] = "decision_id"
    ID_PREFIX: ClassVar[str] = HIT_DECISION_ID_PREFIX

    head_sha: str
    head_tree_sha: str
    registry_id: str
    registry_digest: str
    role_authority_manifest_digest: str
    schedule_id: str
    schedule_digest: str
    scheduler_grant_id: str
    scheduler_grant_digest: str
    scheduler_artifact_semantic_sha256: str
    coverage_verifier_grant_id: str
    coverage_verifier_grant_digest: str
    coverage_verifier_artifact_semantic_sha256: str
    module_binding_digest: str
    body_id: str
    body_digest: str
    anchor_id: str
    anchor_digest: str
    state_id: str
    state_digest: str
    subject_kind: str
    root_context: int
    scheduler_domain_digest: str
    scheduler_invocation_digest: str
    scheduler_evidence_digest: str
    coverage_replay_digest: str
    coverage_scope: str
    global_exhaustion: bool
    next_unchecked_gap: int
    scan_digests: tuple[str, str, str]
    selected_certificate: Mapping[str, Any]
    selected_certificate_digest: str
    outcome: str
    evidence_class: str
    source_actualness: bool
    initializer_authority: bool
    issuer_authority: bool
    terminal_authority: bool
    e1_authority: bool
    queue_authority: bool
    producer_continuation_allowed: bool
    decision_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class QOneRegisteredPrefixMissEvidenceV2(_FactoryOnlyV2):
    ARTIFACT_TYPE: ClassVar[str] = "QOneRegisteredPrefixMissEvidenceV2"
    ID_FIELD: ClassVar[str] = "decision_id"
    ID_PREFIX: ClassVar[str] = MISS_DECISION_ID_PREFIX

    head_sha: str
    head_tree_sha: str
    registry_id: str
    registry_digest: str
    role_authority_manifest_digest: str
    schedule_id: str
    schedule_digest: str
    scheduler_grant_id: str
    scheduler_grant_digest: str
    scheduler_artifact_semantic_sha256: str
    coverage_verifier_grant_id: str
    coverage_verifier_grant_digest: str
    coverage_verifier_artifact_semantic_sha256: str
    module_binding_digest: str
    body_id: str
    body_digest: str
    anchor_id: str
    anchor_digest: str
    state_id: str
    state_digest: str
    subject_kind: str
    root_context: int
    scheduler_domain_digest: str
    scheduler_invocation_digest: str
    scheduler_evidence_digest: str
    coverage_replay_digest: str
    coverage_scope: str
    global_exhaustion: bool
    next_unchecked_gap: int
    scan_digests: tuple[str, str, str]
    selected_certificate: None
    selected_certificate_digest: None
    outcome: str
    evidence_class: str
    source_actualness: bool
    initializer_authority: bool
    issuer_authority: bool
    terminal_authority: bool
    e1_authority: bool
    queue_authority: bool
    producer_continuation_allowed: bool
    decision_id: str
    digest: str


DecisionEvidenceV2 = QOneRootTerminalHitEvidenceV2 | QOneRegisteredPrefixMissEvidenceV2
DecisionT = TypeVar("DecisionT", bound=DecisionEvidenceV2)
_DECISION_CLASSES = frozenset(
    {QOneRootTerminalHitEvidenceV2, QOneRegisteredPrefixMissEvidenceV2}
)


def _run_git_v2(root: Path, args: Sequence[str]) -> bytes:
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
            TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
            f"git {' '.join(args)} failed: {detail}",
        )
    return completed.stdout


def _repository_root_v2(locator: Path) -> Path:
    if not isinstance(locator, Path):
        _reject(
            TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
            "root must be a pathlib.Path",
        )
    try:
        return Path(
            _run_git_v2(locator.resolve(), ("rev-parse", "--show-toplevel"))
            .decode("utf-8")
            .strip()
        ).resolve()
    except UnicodeDecodeError as exc:
        raise TerminalDecisionAssemblerError(
            TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
            "repository root is not UTF-8",
        ) from exc


def _exact_head_v2(root: Path, requested_head: str) -> tuple[str, str]:
    object_format = _run_git_v2(root, ("rev-parse", "--show-object-format")).decode(
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
            TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
            "requested_head must be one exact full lowercase commit ID",
        )
    object_type = _run_git_v2(root, ("cat-file", "-t", requested_head)).decode().strip()
    if object_type != "commit":
        _reject(
            TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
            "requested_head is not a commit",
        )
    resolved = _run_git_v2(
        root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}")
    ).decode("ascii").strip()
    if resolved != requested_head:
        _reject(
            TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
            "requested commit did not resolve exactly",
        )
    tree_sha = _run_git_v2(root, ("rev-parse", f"{requested_head}^{{tree}}"))
    tree_sha_text = tree_sha.decode("ascii").strip()
    if len(tree_sha_text) != oid_length:
        _reject(
            TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
            "requested commit tree ID is malformed",
        )
    return requested_head, tree_sha_text


def _tree_entries_v2(root: Path, head_sha: str) -> dict[str, tuple[str, str, str]]:
    raw = _run_git_v2(root, ("ls-tree", "-r", "-z", "--full-tree", head_sha))
    result: dict[str, tuple[str, str, str]] = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            metadata, path_bytes = record.split(b"\t", 1)
            mode, object_type, object_id = metadata.decode("ascii").split(" ")
            path = path_bytes.decode("utf-8")
        except (UnicodeDecodeError, ValueError) as exc:
            raise TerminalDecisionAssemblerError(
                TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
                f"malformed Git tree entry {record!r}",
            ) from exc
        pure = PurePosixPath(path)
        if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
            _reject(
                TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
                f"unsafe tracked path {path!r}",
            )
        if path in result:
            _reject(
                TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
                f"duplicate tracked path {path!r}",
            )
        result[path] = (mode, object_type, object_id)
    return result


def _exact_head_blob_v2(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    path: str,
) -> _GitBlobV2:
    entry = entries.get(path)
    if entry is None:
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            f"{path!r} is absent from requested HEAD",
        )
    mode, object_type, object_id = entry
    if mode not in REGULAR_GIT_MODES or object_type != "blob":
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            f"{path!r} is not a regular tracked blob",
        )
    content = _run_git_v2(root, ("cat-file", "blob", object_id))
    return _GitBlobV2(path, mode, object_id, content)


def _require_exact_worktree_blob_v2(
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    path: str,
) -> tuple[_GitBlobV2, Path]:
    blob = _exact_head_blob_v2(root, entries, path)
    worktree_path = root / path
    if worktree_path.is_symlink() or not worktree_path.is_file():
        _reject(
            TerminalDecisionAssemblerRejectCode.WORKTREE_BINDING_ERROR,
            f"{path} is not a regular worktree file",
        )
    if worktree_path.read_bytes() != blob.content:
        _reject(
            TerminalDecisionAssemblerRejectCode.WORKTREE_BINDING_ERROR,
            f"{path} differs from requested HEAD",
        )
    return blob, worktree_path


def _verify_assembler_self_v2(
    root: Path,
    head_sha: str,
    tree_sha: str,
    entries: Mapping[str, tuple[str, str, str]],
) -> dict[str, Any]:
    blob, worktree_path = _require_exact_worktree_blob_v2(
        root,
        entries,
        ASSEMBLER_PATH,
    )
    executing_path = Path(__file__)
    if (
        executing_path.is_symlink()
        or not executing_path.is_file()
        or executing_path.resolve() != worktree_path.resolve()
        or executing_path.read_bytes() != blob.content
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            "executing assembler is not backed by its requested-HEAD blob",
        )
    payload: dict[str, Any] = {
        "schema_id": "t6_q_one_terminal_decision_assembler_self_binding_v2",
        "head_sha": head_sha,
        "head_tree_sha": tree_sha,
        "path": ASSEMBLER_PATH,
        "module_name": __name__,
        "git_mode": blob.git_mode,
        "git_object_id": blob.git_object_id,
        "blob_sha256": blob.sha256,
        "execution_mode": "CURRENT_ASSEMBLER_MATCHES_EXACT_HEAD_BLOB",
    }
    payload["digest"] = canonical_digest_v2(payload)
    return payload


def _fresh_private_module_name_v2(role: str, head_sha: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9_]", "_", role)
    return f"_t6_exact_head_{normalized}_{head_sha}"


def _fresh_exec_module_v2(
    *,
    root: Path,
    entries: Mapping[str, tuple[str, str, str]],
    path: str,
    private_name: str,
) -> ModuleType:
    blob, worktree_path = _require_exact_worktree_blob_v2(root, entries, path)
    try:
        code = compile(
            blob.content,
            str(worktree_path.resolve()),
            "exec",
            dont_inherit=True,
            optimize=sys.flags.optimize,
        )
    except (SyntaxError, ValueError, TypeError) as exc:
        raise TerminalDecisionAssemblerError(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
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
        raise TerminalDecisionAssemblerError(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            f"exact-HEAD module {path} failed fresh execution: {exc}",
        ) from exc
    finally:
        if previous is None:
            sys.modules.pop(private_name, None)
        else:
            sys.modules[private_name] = previous
    if module.__file__ != str(worktree_path.resolve()):
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            f"fresh module {path} changed its __file__",
        )
    return module


def _load_fresh_modules_v2(
    *,
    root: Path,
    head_sha: str,
    entries: Mapping[str, tuple[str, str, str]],
) -> _FreshModulesV2:
    return _FreshModulesV2(
        registry=_fresh_exec_module_v2(
            root=root,
            entries=entries,
            path=REGISTRY_RESOLVER_PATH,
            private_name=_fresh_private_module_name_v2("registry", head_sha),
        ),
        root_envelope=_fresh_exec_module_v2(
            root=root,
            entries=entries,
            path=ROOT_ENVELOPE_PATH,
            private_name=_fresh_private_module_name_v2("root_envelope", head_sha),
        ),
        scheduler=_fresh_exec_module_v2(
            root=root,
            entries=entries,
            path=SCHEDULER_PATH,
            private_name=_fresh_private_module_name_v2("scheduler", head_sha),
        ),
        coverage=_fresh_exec_module_v2(
            root=root,
            entries=entries,
            path=VERIFIER_PATH,
            private_name=_fresh_private_module_name_v2("coverage", head_sha),
        ),
    )


def _require_callable_binding_v2(module: ModuleType, symbol: str) -> Any:
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
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            f"fresh callable {module.__name__}.{symbol} drifted",
        )
    return value


_CALLABLES_BY_PATH = MappingProxyType(
    {
        REGISTRY_RESOLVER_PATH: ("resolve_registry_v2",),
        ROOT_ENVELOPE_PATH: (
            "make_canonical_q_one_g_source_body_v2",
            "make_root_initializer_anchor_v2",
            "make_raw_root_source_state_v2",
            "artifact_to_mapping_v2",
        ),
        SCHEDULER_PATH: (SCHEDULER_SYMBOL, "evidence_to_mapping_v1"),
        VERIFIER_PATH: (VERIFIER_SYMBOL,),
    }
)


def _capture_fresh_module_binding_v2(
    root: Path,
    head_sha: str,
    tree_sha: str,
    entries: Mapping[str, tuple[str, str, str]],
    modules: _FreshModulesV2,
    assembler_binding: Mapping[str, Any],
) -> dict[str, Any]:
    files: list[dict[str, Any]] = [_json_copy(assembler_binding)]
    module_map = modules.by_path()
    if set(module_map) != set(EXACT_HEAD_PATHS) - {ASSEMBLER_PATH}:
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            "fresh module path set changed",
        )
    for path in EXACT_HEAD_PATHS[1:]:
        blob, worktree_path = _require_exact_worktree_blob_v2(root, entries, path)
        module = module_map[path]
        if type(module) is not ModuleType:
            _reject(
                TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
                f"{path} is not a fresh ModuleType namespace",
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
                TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
                f"fresh module backing file for {path} differs from exact HEAD",
            )
        callables: list[dict[str, Any]] = []
        for symbol in _CALLABLES_BY_PATH[path]:
            value = _require_callable_binding_v2(module, symbol)
            callables.append(
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
                "callable_identities": callables,
            }
        )
    payload: dict[str, Any] = {
        "schema_id": "t6_q_one_terminal_decision_module_binding_v2",
        "head_sha": head_sha,
        "head_tree_sha": tree_sha,
        "files": files,
        "status": "FRESH_PRIVATE_MODULES_FROM_REGULAR_EXACT_HEAD_BLOBS",
    }
    payload["digest"] = canonical_digest_v2(payload)
    return payload


def _verify_sealed_mapping_digest_v2(value: Any, name: str) -> str:
    if type(value) is not dict:
        _reject(
            TerminalDecisionAssemblerRejectCode.REGISTRY_ERROR,
            f"{name} must be an exact dict",
        )
    digest = value.get("digest")
    _require_digest(digest, f"{name}.digest")
    unsigned = _json_copy(value)
    unsigned.pop("digest")
    if canonical_digest_v2(unsigned) != digest:
        _reject(
            TerminalDecisionAssemblerRejectCode.DIGEST_MISMATCH,
            f"{name}.digest does not replay",
        )
    return digest


def _verify_registry_v2(
    resolved: Any,
    requested_head: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    if type(resolved) is not dict:
        _reject(
            TerminalDecisionAssemblerRejectCode.REGISTRY_ERROR,
            "resolved registry must be an exact dict",
        )
    registry_digest = resolved.get("registry_digest")
    _require_digest(registry_digest, "registry_digest")
    unsigned = _json_copy(resolved)
    unsigned.pop("registry_digest")
    if canonical_digest_v2(unsigned) != registry_digest:
        _reject(
            TerminalDecisionAssemblerRejectCode.REGISTRY_ERROR,
            "resolved registry digest does not replay",
        )
    if not (
        resolved.get("schema_id") == EXPECTED_RESOLVED_SCHEMA_ID
        and _plain_int(resolved.get("schema_version"))
        and resolved["schema_version"] == 2
        and resolved.get("head_sha") == requested_head
        and type(resolved.get("head_tree_sha")) is str
        and resolved.get("status") == EXPECTED_REGISTRY_STATUS
        and _plain_int(resolved.get("active_role_grant_count"))
        and resolved["active_role_grant_count"] == 2
        and _plain_int(resolved.get("terminal_prefix_authority_count"))
        and resolved["terminal_prefix_authority_count"] == 1
        and resolved.get("role_grant_counts")
        == {"INDEPENDENT_COVERAGE_VERIFIER": 1, "TERMINAL_SCHEDULER": 1}
        and resolved.get("authorized_branches") == []
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.REGISTRY_ERROR,
            "resolved registry identity, HEAD, cardinality, or branch boundary changed",
        )
    _require_git_oid(resolved["head_tree_sha"], "resolved head_tree_sha")
    denials = {
        "issuer_count": resolved.get("issuer_count"),
        "issuer_authority": resolved.get("issuer_authority"),
        "e1_authority": resolved.get("e1_authority"),
        "queue_authority": resolved.get("queue_authority"),
        "producer_authority": resolved.get("producer_authority"),
        "initializer_authority": resolved.get("initializer_authority"),
        "t5_authority": resolved.get("t5_authority"),
    }
    if not (_plain_int(denials["issuer_count"]) and denials["issuer_count"] == 0):
        _reject(
            TerminalDecisionAssemblerRejectCode.AUTHORITY_ERROR,
            "resolved issuer_count must be the plain integer zero",
        )
    for name, value in denials.items():
        if name != "issuer_count":
            _require_false(value, f"resolved.{name}")

    artifacts = resolved.get("resolved_artifacts")
    grants = resolved.get("resolved_role_grants")
    prefixes = resolved.get("authorized_terminal_prefixes")
    if (
        type(artifacts) is not list
        or len(artifacts) != 2
        or any(type(item) is not dict for item in artifacts)
        or type(grants) is not list
        or len(grants) != 2
        or any(type(item) is not dict for item in grants)
        or type(prefixes) is not list
        or len(prefixes) != 1
        or type(prefixes[0]) is not dict
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.REGISTRY_ERROR,
            "resolved artifact, grant, or prefix collections changed",
        )
    artifact_map = {item.get("artifact_id"): item for item in artifacts}
    grant_map = {item.get("grant_id"): item for item in grants}
    if set(artifact_map) != {
        SCHEDULER_ARTIFACT_ID,
        VERIFIER_ARTIFACT_ID,
    } or set(grant_map) != {SCHEDULER_GRANT_ID, VERIFIER_GRANT_ID}:
        _reject(
            TerminalDecisionAssemblerRejectCode.GRANT_ERROR,
            "resolved artifact or grant identity set changed",
        )
    scheduler_artifact = artifact_map[SCHEDULER_ARTIFACT_ID]
    verifier_artifact = artifact_map[VERIFIER_ARTIFACT_ID]
    scheduler_grant = grant_map[SCHEDULER_GRANT_ID]
    verifier_grant = grant_map[VERIFIER_GRANT_ID]
    expected_bindings = (
        (
            scheduler_artifact,
            SCHEDULER_PATH,
            SCHEDULER_SYMBOL,
            scheduler_grant,
            "TERMINAL_SCHEDULER",
            list(SCHEDULER_CAPABILITIES),
        ),
        (
            verifier_artifact,
            VERIFIER_PATH,
            VERIFIER_SYMBOL,
            verifier_grant,
            "INDEPENDENT_COVERAGE_VERIFIER",
            list(VERIFIER_CAPABILITIES),
        ),
    )
    for artifact, path, symbol, grant, role, capabilities in expected_bindings:
        for name in (
            "blob_sha256",
            "symbol_ast_sha256",
            "local_import_closure_digest",
            "semantic_sha256",
        ):
            _require_digest(artifact.get(name), f"artifact.{name}")
        if not (
            artifact.get("path") == path
            and artifact.get("symbol") == symbol
            and artifact.get("semantic_digest_method") == SEMANTIC_DIGEST_METHOD
            and artifact.get("expected_blob_sha256") == artifact.get("blob_sha256")
            and artifact.get("expected_symbol_ast_sha256")
            == artifact.get("symbol_ast_sha256")
            and artifact.get("expected_local_import_closure_digest")
            == artifact.get("local_import_closure_digest")
            and artifact.get("expected_semantic_sha256") == artifact.get("semantic_sha256")
            and grant.get("role") == role
            and grant.get("grant_id")
            in {SCHEDULER_GRANT_ID, VERIFIER_GRANT_ID}
            and grant.get("artifact_id") == artifact.get("artifact_id")
            and grant.get("schedule_id") == SCHEDULE_ID
            and grant.get("capabilities") == capabilities
            and grant.get("authority_class") == ROLE_AUTHORITY_CLASS
            and grant.get("expected_artifact_semantic_sha256")
            == artifact.get("semantic_sha256")
            and grant.get("artifact_semantic_sha256") == artifact.get("semantic_sha256")
            and grant.get("artifact_path") == path
            and grant.get("artifact_symbol") == symbol
            and grant.get("artifact_blob_sha256") == artifact.get("blob_sha256")
            and grant.get("artifact_closure_digest")
            == artifact.get("local_import_closure_digest")
        ):
            _reject(
                TerminalDecisionAssemblerRejectCode.GRANT_ERROR,
                f"resolved {role} artifact or grant binding changed",
            )

    prefix = prefixes[0]
    expected_prefix_values = {
        "schedule_id": SCHEDULE_ID,
        "scheduler_grant_id": SCHEDULER_GRANT_ID,
        "coverage_verifier_grant_id": VERIFIER_GRANT_ID,
        "domain_schema_id": SCHEDULER_DOMAIN_SCHEMA_ID,
        "evidence_schema_id": SCHEDULER_EVIDENCE_SCHEMA_ID,
        "ordered_gaps": [3, 7, 11],
        "next_unchecked_gap": 15,
        "candidate_order": CANDIDATE_ORDER,
        "coverage_scope": COVERAGE_SCOPE,
        "coverage_semantics": "REGISTERED_PRIORITY_ONLY",
        "global_exhaustion": False,
        "outcomes": [
            SCHEDULER_PREFIX_MISS,
            SCHEDULER_ROOT_TERMINAL_HIT,
        ],
        "terminal_hit_semantics": "ROOT_TERMINAL_EVIDENCE_ONLY_NO_ISSUER",
        "prefix_miss_semantics": "REGISTERED_PREFIX_MISS_EVIDENCE_ONLY_NO_E1",
        "issuer_authorized": False,
        "issuer_count": 0,
        "e1_authority": False,
        "queue_authority": False,
    }
    if not (
        _plain_int(prefix.get("issuer_count"))
        and prefix["issuer_count"] == 0
        and prefix.get("global_exhaustion") is False
        and prefix.get("issuer_authorized") is False
        and prefix.get("e1_authority") is False
        and prefix.get("queue_authority") is False
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.AUTHORITY_ERROR,
            "resolved prefix count or false authority fields changed type/value",
        )
    if any(prefix.get(key) != value for key, value in expected_prefix_values.items()):
        _reject(
            TerminalDecisionAssemblerRejectCode.REGISTRY_ERROR,
            "resolved terminal-prefix contract changed",
        )
    if not (
        prefix.get("scheduler_artifact_id") == SCHEDULER_ARTIFACT_ID
        and prefix.get("scheduler_artifact_semantic_sha256")
        == scheduler_artifact["semantic_sha256"]
        and prefix.get("scheduler_artifact_closure_digest")
        == scheduler_artifact["local_import_closure_digest"]
        and prefix.get("coverage_verifier_artifact_id")
        == VERIFIER_ARTIFACT_ID
        and prefix.get("coverage_verifier_artifact_semantic_sha256")
        == verifier_artifact["semantic_sha256"]
        and prefix.get("coverage_verifier_artifact_closure_digest")
        == verifier_artifact["local_import_closure_digest"]
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.GRANT_ERROR,
            "resolved prefix does not bind the exact scheduler and verifier",
        )

    role_manifest = resolved.get("role_authority_manifest")
    _verify_sealed_mapping_digest_v2(role_manifest, "role_authority_manifest")
    if not (
        role_manifest.get("head_sha") == requested_head
        and role_manifest.get("status") == EXPECTED_REGISTRY_STATUS
        and role_manifest.get("grants") == grants
        and role_manifest.get("terminal_prefix") == prefix
        and _plain_int(role_manifest.get("issuer_count"))
        and role_manifest["issuer_count"] == 0
        and role_manifest.get("e1_authority") is False
        and role_manifest.get("queue_authority") is False
        and role_manifest.get("producer_authority") is False
        and role_manifest.get("initializer_authority") is False
        and role_manifest.get("t5_authority") is False
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.AUTHORITY_ERROR,
            "role authority manifest changed or grants forbidden authority",
        )
    return resolved, prefix, scheduler_grant, verifier_grant


def _bind_fresh_roles_v2(
    module_binding: Mapping[str, Any],
    resolved: Mapping[str, Any],
) -> None:
    files = module_binding.get("files")
    if type(files) is not list:
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            "module binding files must be a list",
        )
    file_map = {item.get("path"): item for item in files if type(item) is dict}
    artifact_map = {
        item["artifact_id"]: item for item in resolved["resolved_artifacts"]
    }
    for artifact_id, path in (
        (SCHEDULER_ARTIFACT_ID, SCHEDULER_PATH),
        (VERIFIER_ARTIFACT_ID, VERIFIER_PATH),
    ):
        file_binding = file_map.get(path)
        artifact = artifact_map[artifact_id]
        if not (
            type(file_binding) is dict
            and file_binding.get("blob_sha256") == artifact.get("blob_sha256")
            and file_binding.get("git_object_id") == artifact.get("git_object_id")
            and file_binding.get("git_mode") == artifact.get("git_mode")
        ):
            _reject(
                TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
                f"loaded {artifact_id} does not match its resolved artifact pin",
            )


def _grant_digest_v2(grant: Mapping[str, Any]) -> str:
    return canonical_digest_v2(grant)


def _schedule_digest_v2(
    resolved: Mapping[str, Any],
    prefix: Mapping[str, Any],
    scheduler_grant_digest: str,
    verifier_grant_digest: str,
) -> str:
    return canonical_digest_v2(
        {
            "schema_id": "t6_q_one_registered_priority_prefix_schedule_binding_v2",
            "head_sha": resolved["head_sha"],
            "registry_digest": resolved["registry_digest"],
            "role_authority_manifest_digest": resolved["role_authority_manifest"][
                "digest"
            ],
            "terminal_prefix": prefix,
            "scheduler_grant_digest": scheduler_grant_digest,
            "coverage_verifier_grant_digest": verifier_grant_digest,
        }
    )


def _scheduler_domain_from_state_v2(
    state: Any,
    modules: _FreshModulesV2,
) -> dict[str, Any]:
    _require_callable_binding_v2(
        modules.root_envelope,
        "artifact_to_mapping_v2",
    )(state)
    return {
        "schema_id": SCHEDULER_DOMAIN_SCHEMA_ID,
        "schema_version": SCHEDULER_DOMAIN_SCHEMA_VERSION,
        "root_context": state.root_context,
        "equation_rank": state.equation_rank,
        "equation_numerator": state.equation_numerator,
        "equation_denominator": state.equation_denominator,
        "q": state.q,
        "gap_three_x": state.gap_three_x,
        "endpoint_fiber_code": state.endpoint_fiber_code,
        "major_phase_code": state.major_phase_code,
        "provenance_code": state.provenance_code,
        "mark_kind_code": state.mark_kind_code,
        "mark_root_context": state.mark_root_context,
        "mark_equation_rank": state.mark_equation_rank,
        "gap_three_factorization": [
            [prime, exponent] for prime, exponent in state.gap_three_factorization
        ],
    }


def _scheduler_invocation_digest_v2(
    *,
    resolved: Mapping[str, Any],
    prefix: Mapping[str, Any],
    schedule_digest: str,
    scheduler_grant_digest: str,
    verifier_grant_digest: str,
    module_binding_digest: str,
    body: Any,
    anchor: Any,
    state: Any,
    domain_digest: str,
) -> str:
    return canonical_digest_v2(
        {
            "schema_id": "t6_q_one_terminal_scheduler_invocation_v2",
            "head_sha": resolved["head_sha"],
            "head_tree_sha": resolved["head_tree_sha"],
            "registry_digest": resolved["registry_digest"],
            "role_authority_manifest_digest": resolved["role_authority_manifest"][
                "digest"
            ],
            "schedule_id": prefix["schedule_id"],
            "schedule_digest": schedule_digest,
            "scheduler_grant_digest": scheduler_grant_digest,
            "coverage_verifier_grant_digest": verifier_grant_digest,
            "module_binding_digest": module_binding_digest,
            "subject_kind": SUBJECT_KIND,
            "body_id": body.body_id,
            "body_digest": body.digest,
            "anchor_id": anchor.anchor_id,
            "anchor_digest": anchor.digest,
            "state_id": state.state_id,
            "state_digest": state.digest,
            "scheduler_domain_schema_id": SCHEDULER_DOMAIN_SCHEMA_ID,
            "scheduler_domain_digest": domain_digest,
        }
    )


def _coverage_replay_digest_v2(
    verification: Any,
    modules: _FreshModulesV2,
    *,
    domain_digest: str,
    evidence_digest: str,
    verifier_grant_digest: str,
    verifier_semantic_digest: str,
) -> str:
    verification_type = getattr(
        modules.coverage,
        "PrefixCoverageVerificationV1",
        None,
    )
    if type(verification_type) is not type or type(verification) is not verification_type:
        _reject(
            TerminalDecisionAssemblerRejectCode.COVERAGE_ERROR,
            "coverage verifier returned a non-canonical DTO",
        )
    if not (
        verification.status == COVERAGE_VERIFIED_STATUS
        and verification.evidence_digest == evidence_digest
        and verification.outcome
        in {SCHEDULER_ROOT_TERMINAL_HIT, SCHEDULER_PREFIX_MISS}
        and _plain_int(verification.root_context)
        and verification.global_exhaustion is False
        and verification.terminal_authority == SCHEDULER_BLOCKED
        and verification.role_authority == SCHEDULER_BLOCKED
        and verification.issuance_allowed is False
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.COVERAGE_ERROR,
            "coverage DTO changed its evidence-only invariant",
        )
    return canonical_digest_v2(
        {
            "schema_id": "t6_q_one_priority_prefix_coverage_replay_v2",
            "status": verification.status,
            "evidence_digest": verification.evidence_digest,
            "outcome": verification.outcome,
            "root_context": verification.root_context,
            "global_exhaustion": verification.global_exhaustion,
            "terminal_authority": verification.terminal_authority,
            "role_authority": verification.role_authority,
            "issuance_allowed": verification.issuance_allowed,
            "scheduler_domain_digest": domain_digest,
            "coverage_verifier_grant_digest": verifier_grant_digest,
            "coverage_verifier_artifact_semantic_sha256": verifier_semantic_digest,
        }
    )


_CERTIFICATE_FIELDS = frozenset(
    {"certificate_type", "gap", "x", "divisor", "y", "z", "candidate_index"}
)


def _validated_selected_certificate_v2(
    value: Any,
    *,
    root_context: int,
) -> Mapping[str, Any]:
    if type(value) is not dict or frozenset(value) != _CERTIFICATE_FIELDS:
        _reject(
            TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
            "selected terminal must be the exact scheduler certificate mapping",
        )
    if type(value["certificate_type"]) is not str or value["certificate_type"] not in {
        "TYPE_I",
        "TYPE_II",
    }:
        _reject(
            TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
            "selected certificate has an unknown type",
        )
    for name in _CERTIFICATE_FIELDS - {"certificate_type"}:
        if not _plain_int(value[name]):
            _reject(
                TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
                f"selected_certificate.{name} must be a plain integer",
            )
    gap = value["gap"]
    x, divisor, y, z = (value[name] for name in ("x", "divisor", "y", "z"))
    if not (
        gap in ORDERED_GAPS
        and x == (root_context + gap) // 4
        and divisor > 0
        and x * x % divisor == 0
        and y > 0
        and z > 0
        and value["candidate_index"] >= 0
        and 4 * x * y * z == root_context * (x * y + x * z + y * z)
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
            "selected terminal certificate does not replay the root equation",
        )
    quotient = x * x // divisor
    if value["certificate_type"] == "TYPE_I":
        if not (
            (root_context * x + divisor) % gap == 0
            and root_context * (x + root_context * quotient) % gap == 0
            and y == (root_context * x + divisor) // gap
            and z == root_context * (x + root_context * quotient) // gap
        ):
            _reject(
                TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
                "selected Type I certificate does not replay its divisor formulas",
            )
    elif not (
        divisor <= x
        and (x + divisor) % gap == 0
        and root_context * (x + quotient) % gap == 0
        and y == root_context * (x + divisor) // gap
        and z == root_context * (x + quotient) // gap
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
            "selected Type II certificate does not replay its divisor formulas",
        )
    return _freeze_json(value)


def _validate_decision_fields_v2(decision: DecisionEvidenceV2) -> None:
    cls = type(decision)
    if cls not in _DECISION_CLASSES:
        _reject(
            TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
            "decision must have an exact V2 terminal-decision class",
        )
    for field in fields(cls):
        try:
            getattr(decision, field.name)
        except AttributeError as exc:
            raise TerminalDecisionAssemblerError(
                TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
                f"{cls.ARTIFACT_TYPE}.{field.name} is missing",
            ) from exc
    _require_git_oid(decision.head_sha, "head_sha")
    _require_git_oid(decision.head_tree_sha, "head_tree_sha")
    if len(decision.head_sha) != len(decision.head_tree_sha):
        _reject(
            TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
            "head and tree use different Git object formats",
        )
    if decision.registry_id != EXPECTED_REGISTRY_ID:
        _reject(
            TerminalDecisionAssemblerRejectCode.REGISTRY_ERROR,
            "decision registry_id changed",
        )
    if decision.schedule_id != SCHEDULE_ID:
        _reject(
            TerminalDecisionAssemblerRejectCode.REGISTRY_ERROR,
            "decision schedule_id changed",
        )
    if (
        decision.scheduler_grant_id != SCHEDULER_GRANT_ID
        or decision.coverage_verifier_grant_id != VERIFIER_GRANT_ID
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.GRANT_ERROR,
            "decision grant IDs changed",
        )
    for name in (
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
        _require_digest(getattr(decision, name), name)
    _require_content_id(decision.body_id, "body_id", BODY_ID_PREFIX)
    _require_content_id(
        decision.anchor_id,
        "anchor_id",
        ANCHOR_ID_PREFIX,
    )
    _require_content_id(decision.state_id, "state_id", STATE_ID_PREFIX)
    if (
        decision.body_id != BODY_ID_PREFIX + decision.body_digest
        or decision.anchor_id != ANCHOR_ID_PREFIX + decision.anchor_digest
        or decision.state_id != STATE_ID_PREFIX + decision.state_digest
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.ID_MISMATCH,
            "decision body, anchor, or state ID disagrees with its digest",
        )
    if decision.subject_kind != SUBJECT_KIND:
        _reject(
            TerminalDecisionAssemblerRejectCode.DOMAIN_ERROR,
            "decision subject_kind must remain SOURCE_STATE",
        )
    if not _plain_int(decision.root_context) or decision.root_context < 2:
        _reject(
            TerminalDecisionAssemblerRejectCode.DOMAIN_ERROR,
            "decision root_context must be a plain positive integer",
        )
    if decision.coverage_scope != COVERAGE_SCOPE:
        _reject(
            TerminalDecisionAssemblerRejectCode.COVERAGE_ERROR,
            "decision coverage scope changed",
        )
    _require_false(decision.global_exhaustion, "global_exhaustion")
    if not _plain_int(decision.next_unchecked_gap) or decision.next_unchecked_gap != 15:
        _reject(
            TerminalDecisionAssemblerRejectCode.COVERAGE_ERROR,
            "next_unchecked_gap must remain the plain integer 15",
        )
    if (
        type(decision.scan_digests) is not tuple
        or len(decision.scan_digests) != 3
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.EVIDENCE_ERROR,
            "scan_digests must be an exact length-three tuple",
        )
    for index, digest in enumerate(decision.scan_digests):
        _require_digest(digest, f"scan_digests[{index}]")
    if decision.evidence_class != EXPECTED_EVIDENCE_CLASS:
        _reject(
            TerminalDecisionAssemblerRejectCode.AUTHORITY_ERROR,
            "decision evidence_class changed",
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
        _require_false(getattr(decision, name), name)

    if cls is QOneRootTerminalHitEvidenceV2:
        if decision.outcome != ROOT_TERMINAL_HIT_EVIDENCE:
            _reject(
                TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
                "hit decision outcome changed",
            )
        certificate = _validated_selected_certificate_v2(
            _json_copy(decision.selected_certificate),
            root_context=decision.root_context,
        )
        expected_certificate_digest = canonical_digest_v2(certificate)
        if decision.selected_certificate_digest != expected_certificate_digest:
            _reject(
                TerminalDecisionAssemblerRejectCode.DIGEST_MISMATCH,
                "selected certificate digest does not replay",
            )
    else:
        if (
            decision.outcome != PREFIX_MISS_EVIDENCE
            or decision.selected_certificate is not None
            or decision.selected_certificate_digest is not None
        ):
            _reject(
                TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
                "prefix-miss decision carries a terminal certificate or wrong outcome",
            )
    _require_content_id(decision.decision_id, "decision_id", cls.ID_PREFIX)
    _require_digest(decision.digest, "decision.digest")


def _decision_external_value_v2(value: Any) -> Any:
    return _json_copy(value)


def _unsigned_decision_mapping_v2(
    cls: type[DecisionT],
    values: Mapping[str, Any],
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "artifact_type": cls.ARTIFACT_TYPE,
        "schema_version": SCHEMA_VERSION,
    }
    for field in fields(cls):
        if field.name in {cls.ID_FIELD, "digest"}:
            continue
        payload[field.name] = _decision_external_value_v2(values[field.name])
    return payload


def _construct_decision_v2(
    cls: type[DecisionT],
    values: Mapping[str, Any],
) -> DecisionT:
    instance = object.__new__(cls)
    for field in fields(cls):
        object.__setattr__(instance, field.name, values[field.name])
    return instance


def _verify_decision_seal_v2(decision: DecisionEvidenceV2) -> None:
    _validate_decision_fields_v2(decision)
    cls = type(decision)
    values = {field.name: getattr(decision, field.name) for field in fields(cls)}
    expected_digest = canonical_digest_v2(_unsigned_decision_mapping_v2(cls, values))
    if decision.digest != expected_digest:
        _reject(
            TerminalDecisionAssemblerRejectCode.DIGEST_MISMATCH,
            "decision digest does not replay",
        )
    if decision.decision_id != cls.ID_PREFIX + expected_digest:
        _reject(
            TerminalDecisionAssemblerRejectCode.ID_MISMATCH,
            "decision ID does not replay",
        )


def _seal_decision_v2(
    cls: type[DecisionT],
    values: Mapping[str, Any],
) -> DecisionT:
    mutable = dict(values)
    digest = canonical_digest_v2(_unsigned_decision_mapping_v2(cls, mutable))
    mutable[cls.ID_FIELD] = cls.ID_PREFIX + digest
    mutable["digest"] = digest
    decision = _construct_decision_v2(cls, mutable)
    _verify_decision_seal_v2(decision)
    return decision


def terminal_decision_to_mapping_v2(
    decision: DecisionEvidenceV2,
) -> dict[str, Any]:
    """Serialize an exact decision after complete typed invariant replay."""

    if type(decision) not in _DECISION_CLASSES:
        _reject(
            TerminalDecisionAssemblerRejectCode.MALFORMED_FIELD,
            "serializer accepts only exact assembler decision classes",
        )
    _verify_decision_seal_v2(decision)
    cls = type(decision)
    values = {field.name: getattr(decision, field.name) for field in fields(cls)}
    result = _unsigned_decision_mapping_v2(cls, values)
    result[cls.ID_FIELD] = decision.decision_id
    result["digest"] = decision.digest
    return result


def _assemble_decision_values_v2(
    *,
    resolved: Mapping[str, Any],
    prefix: Mapping[str, Any],
    scheduler_grant: Mapping[str, Any],
    verifier_grant: Mapping[str, Any],
    scheduler_grant_digest: str,
    verifier_grant_digest: str,
    schedule_digest: str,
    module_binding_digest: str,
    body: Any,
    anchor: Any,
    state: Any,
    domain_digest: str,
    invocation_digest: str,
    evidence_mapping: Mapping[str, Any],
    coverage_replay_digest: str,
) -> tuple[type[DecisionEvidenceV2], dict[str, Any]]:
    scans = evidence_mapping.get("gap_scans")
    if type(scans) is not list or len(scans) != 3 or any(type(scan) is not dict for scan in scans):
        _reject(
            TerminalDecisionAssemblerRejectCode.EVIDENCE_ERROR,
            "scheduler evidence must contain exactly three scan mappings",
        )
    scan_digests = tuple(scan.get("scan_digest") for scan in scans)
    if any(type(digest) is not str or _DIGEST_RE.fullmatch(digest) is None for digest in scan_digests):
        _reject(
            TerminalDecisionAssemblerRejectCode.EVIDENCE_ERROR,
            "scheduler evidence scan digest is malformed",
        )
    selected = evidence_mapping.get("selected_terminal")
    status = evidence_mapping.get("status")
    common: dict[str, Any] = {
        "head_sha": resolved["head_sha"],
        "head_tree_sha": resolved["head_tree_sha"],
        "registry_id": EXPECTED_REGISTRY_ID,
        "registry_digest": resolved["registry_digest"],
        "role_authority_manifest_digest": resolved["role_authority_manifest"]["digest"],
        "schedule_id": prefix["schedule_id"],
        "schedule_digest": schedule_digest,
        "scheduler_grant_id": scheduler_grant["grant_id"],
        "scheduler_grant_digest": scheduler_grant_digest,
        "scheduler_artifact_semantic_sha256": scheduler_grant[
            "artifact_semantic_sha256"
        ],
        "coverage_verifier_grant_id": verifier_grant["grant_id"],
        "coverage_verifier_grant_digest": verifier_grant_digest,
        "coverage_verifier_artifact_semantic_sha256": verifier_grant[
            "artifact_semantic_sha256"
        ],
        "module_binding_digest": module_binding_digest,
        "body_id": body.body_id,
        "body_digest": body.digest,
        "anchor_id": anchor.anchor_id,
        "anchor_digest": anchor.digest,
        "state_id": state.state_id,
        "state_digest": state.digest,
        "subject_kind": SUBJECT_KIND,
        "root_context": state.root_context,
        "scheduler_domain_digest": domain_digest,
        "scheduler_invocation_digest": invocation_digest,
        "scheduler_evidence_digest": evidence_mapping["digest"],
        "coverage_replay_digest": coverage_replay_digest,
        "coverage_scope": prefix["coverage_scope"],
        "global_exhaustion": False,
        "next_unchecked_gap": prefix["next_unchecked_gap"],
        "scan_digests": scan_digests,
        "evidence_class": EXPECTED_EVIDENCE_CLASS,
        "source_actualness": False,
        "initializer_authority": False,
        "issuer_authority": False,
        "terminal_authority": False,
        "e1_authority": False,
        "queue_authority": False,
        "producer_continuation_allowed": False,
    }
    if status == SCHEDULER_ROOT_TERMINAL_HIT:
        certificate = _validated_selected_certificate_v2(
            selected,
            root_context=state.root_context,
        )
        common.update(
            {
                "selected_certificate": certificate,
                "selected_certificate_digest": canonical_digest_v2(certificate),
                "outcome": ROOT_TERMINAL_HIT_EVIDENCE,
            }
        )
        return QOneRootTerminalHitEvidenceV2, common
    if status == SCHEDULER_PREFIX_MISS:
        if selected is not None:
            _reject(
                TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
                "prefix miss unexpectedly carries a selected terminal",
            )
        common.update(
            {
                "selected_certificate": None,
                "selected_certificate_digest": None,
                "outcome": PREFIX_MISS_EVIDENCE,
            }
        )
        return QOneRegisteredPrefixMissEvidenceV2, common
    _reject(
        TerminalDecisionAssemblerRejectCode.OUTCOME_ERROR,
        f"scheduler returned unknown status {status!r}",
    )


def assemble_q_one_terminal_decision_v2(
    *,
    root: Path,
    requested_head: str,
    raw_q_one_g: dict[str, Any],
) -> DecisionEvidenceV2:
    """Assemble one exact-HEAD, non-authorizing q=1 terminal decision."""

    repository = _repository_root_v2(root)
    head_sha, tree_sha = _exact_head_v2(repository, requested_head)
    entries = _tree_entries_v2(repository, head_sha)
    assembler_binding = _verify_assembler_self_v2(
        repository,
        head_sha,
        tree_sha,
        entries,
    )
    modules = _load_fresh_modules_v2(
        root=repository,
        head_sha=head_sha,
        entries=entries,
    )
    initial_module_binding = _capture_fresh_module_binding_v2(
        repository,
        head_sha,
        tree_sha,
        entries,
        modules,
        assembler_binding,
    )

    registry_resolver = _require_callable_binding_v2(
        modules.registry,
        "resolve_registry_v2",
    )
    registry_error = getattr(modules.registry, "RegistryV2Error", None)
    if type(registry_error) is not type:
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            "fresh registry module has no exact RegistryV2Error type",
        )
    try:
        resolved = registry_resolver(
            root=repository,
            requested_head=requested_head,
        )
    except registry_error as exc:
        raise TerminalDecisionAssemblerError(
            TerminalDecisionAssemblerRejectCode.REGISTRY_ERROR,
            f"coordinator registry rejected: {exc}",
        ) from exc
    resolved, prefix, scheduler_grant, verifier_grant = _verify_registry_v2(
        resolved,
        requested_head,
    )

    if head_sha != resolved["head_sha"] or tree_sha != resolved["head_tree_sha"]:
        _reject(
            TerminalDecisionAssemblerRejectCode.HEAD_BINDING_ERROR,
            "independent exact-HEAD resolution differs from coordinator registry",
        )
    post_registry_module_binding = _capture_fresh_module_binding_v2(
        repository,
        head_sha,
        tree_sha,
        entries,
        modules,
        assembler_binding,
    )
    if post_registry_module_binding != initial_module_binding:
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            "loaded modules changed during registry resolution",
        )
    _bind_fresh_roles_v2(initial_module_binding, resolved)

    scheduler_grant_digest = _grant_digest_v2(scheduler_grant)
    verifier_grant_digest = _grant_digest_v2(verifier_grant)
    schedule_digest = _schedule_digest_v2(
        resolved,
        prefix,
        scheduler_grant_digest,
        verifier_grant_digest,
    )

    root_error = getattr(
        modules.root_envelope,
        "RootInitializerValidationError",
        None,
    )
    if type(root_error) is not type:
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            "fresh root-envelope module has no exact validation error type",
        )
    make_body = _require_callable_binding_v2(
        modules.root_envelope,
        "make_canonical_q_one_g_source_body_v2",
    )
    make_anchor = _require_callable_binding_v2(
        modules.root_envelope,
        "make_root_initializer_anchor_v2",
    )
    make_state = _require_callable_binding_v2(
        modules.root_envelope,
        "make_raw_root_source_state_v2",
    )
    serialize_state_artifact = _require_callable_binding_v2(
        modules.root_envelope,
        "artifact_to_mapping_v2",
    )
    try:
        body = make_body(raw_q_one_g)
        anchor = make_anchor(body)
        state = make_state(body, anchor)
        serialize_state_artifact(body)
        serialize_state_artifact(anchor)
        serialize_state_artifact(state)
    except root_error as exc:
        raise TerminalDecisionAssemblerError(
            TerminalDecisionAssemblerRejectCode.DOMAIN_ERROR,
            f"root source envelope rejected: {exc}",
        ) from exc

    scheduler_domain = _scheduler_domain_from_state_v2(state, modules)
    domain_digest = canonical_digest_v2(scheduler_domain)
    invocation_digest = _scheduler_invocation_digest_v2(
        resolved=resolved,
        prefix=prefix,
        schedule_digest=schedule_digest,
        scheduler_grant_digest=scheduler_grant_digest,
        verifier_grant_digest=verifier_grant_digest,
        module_binding_digest=initial_module_binding["digest"],
        body=body,
        anchor=anchor,
        state=state,
        domain_digest=domain_digest,
    )
    scheduler_error = getattr(modules.scheduler, "PriorityPrefixError", None)
    if type(scheduler_error) is not type:
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            "fresh scheduler module has no exact PriorityPrefixError type",
        )
    scheduler = _require_callable_binding_v2(modules.scheduler, SCHEDULER_SYMBOL)
    serialize_evidence = _require_callable_binding_v2(
        modules.scheduler,
        "evidence_to_mapping_v1",
    )
    try:
        scheduler_evidence = scheduler(scheduler_domain)
        evidence_mapping = serialize_evidence(scheduler_evidence)
    except scheduler_error as exc:
        raise TerminalDecisionAssemblerError(
            TerminalDecisionAssemblerRejectCode.EVIDENCE_ERROR,
            f"authorized scheduler rejected: {exc}",
        ) from exc
    if not (
        type(evidence_mapping) is dict
        and evidence_mapping.get("domain_input_digest") == domain_digest
        and evidence_mapping.get("schedule_id") == prefix["schedule_id"]
        and evidence_mapping.get("coverage_scope") == prefix["coverage_scope"]
        and evidence_mapping.get("ordered_gaps") == prefix["ordered_gaps"]
        and evidence_mapping.get("next_unchecked_gap") == prefix["next_unchecked_gap"]
        and evidence_mapping.get("candidate_order") == prefix["candidate_order"]
        and evidence_mapping.get("global_exhaustion") is False
        and evidence_mapping.get("terminal_authority") == SCHEDULER_BLOCKED
        and evidence_mapping.get("role_authority") == SCHEDULER_BLOCKED
        and evidence_mapping.get("issuance_allowed") is False
    ):
        _reject(
            TerminalDecisionAssemblerRejectCode.EVIDENCE_ERROR,
            "scheduler evidence is not bound to the derived state domain and prefix",
        )
    _require_digest(evidence_mapping.get("digest"), "scheduler evidence digest")

    coverage_error = getattr(
        modules.coverage,
        "PrefixCoverageVerificationError",
        None,
    )
    if type(coverage_error) is not type:
        _reject(
            TerminalDecisionAssemblerRejectCode.MODULE_BINDING_ERROR,
            "fresh coverage module has no exact verification error type",
        )
    coverage_verifier = _require_callable_binding_v2(
        modules.coverage,
        VERIFIER_SYMBOL,
    )
    try:
        verification = coverage_verifier(
            scheduler_domain,
            evidence_mapping,
        )
    except coverage_error as exc:
        raise TerminalDecisionAssemblerError(
            TerminalDecisionAssemblerRejectCode.COVERAGE_ERROR,
            f"independent coverage verifier rejected: {exc}",
        ) from exc
    coverage_replay_digest = _coverage_replay_digest_v2(
        verification,
        modules,
        domain_digest=domain_digest,
        evidence_digest=evidence_mapping["digest"],
        verifier_grant_digest=verifier_grant_digest,
        verifier_semantic_digest=verifier_grant["artifact_semantic_sha256"],
    )
    if verification.outcome != evidence_mapping["status"]:
        _reject(
            TerminalDecisionAssemblerRejectCode.COVERAGE_ERROR,
            "coverage verifier outcome differs from scheduler evidence",
        )

    final_module_binding = _capture_fresh_module_binding_v2(
        repository,
        head_sha,
        tree_sha,
        entries,
        modules,
        assembler_binding,
    )
    if final_module_binding != initial_module_binding:
        _reject(
            TerminalDecisionAssemblerRejectCode.WORKTREE_BINDING_ERROR,
            "loaded module backing files changed during assembly",
        )
    decision_cls, values = _assemble_decision_values_v2(
        resolved=resolved,
        prefix=prefix,
        scheduler_grant=scheduler_grant,
        verifier_grant=verifier_grant,
        scheduler_grant_digest=scheduler_grant_digest,
        verifier_grant_digest=verifier_grant_digest,
        schedule_digest=schedule_digest,
        module_binding_digest=initial_module_binding["digest"],
        body=body,
        anchor=anchor,
        state=state,
        domain_digest=domain_digest,
        invocation_digest=invocation_digest,
        evidence_mapping=evidence_mapping,
        coverage_replay_digest=coverage_replay_digest,
    )
    return _seal_decision_v2(decision_cls, values)


__all__ = [
    "ASSEMBLER_ID",
    "EXACT_HEAD_PATHS",
    "EXPECTED_EVIDENCE_CLASS",
    "PREFIX_MISS_EVIDENCE",
    "QOneRegisteredPrefixMissEvidenceV2",
    "QOneRootTerminalHitEvidenceV2",
    "ROOT_TERMINAL_HIT_EVIDENCE",
    "TerminalDecisionAssemblerError",
    "TerminalDecisionAssemblerRejectCode",
    "assemble_q_one_terminal_decision_v2",
    "canonical_digest_v2",
    "canonical_json_v2",
    "terminal_decision_to_mapping_v2",
]
