#!/usr/bin/env python3
"""Exact-HEAD, zero-authority persistent-selector runtime cut for T6 V2.

This module is deliberately non-activating.  It resolves the fixed coordinator
role registry at one exact Git commit, parses the complete-terminal registry
from that same commit, and opens a runtime only when both registries prove the
current zero-authority state.  The resulting runtime has no routes, no
initializer and an immutable empty queue.

There is no caller-supplied producer, projector, validator, scheduler, evidence
manifest or legacy V1 receipt surface.  A well-formed acyclic V2 successor
request is shape-checked and then rejected because no successor role is
authorized.  This is a fail-closed migration cut, not Gate 2 or T6 closure.
"""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass, fields
from enum import Enum
from pathlib import Path
import subprocess
import sys
from types import MappingProxyType
from typing import Any, Mapping, NoReturn, Sequence


SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import t6_acyclic_transition_bundle_v2 as acyclic_v2  # noqa: E402
import t6_complete_terminal_receipts_v1 as terminal_contract  # noqa: E402
import t6_coordinator_role_registry_v1 as role_registry  # noqa: E402


RUNTIME_ID = "t6_persistent_selector_runtime_v2"
RUNTIME_VERSION = 2
RUNTIME_STATUS = "ZERO_AUTHORITY_FAIL_CLOSED"
PROOF_BOUNDARY = "NOT_GATE2_NOT_T6_CLOSURE"

TERMINAL_REGISTRY_PATH = (
    "data/t6-wave1/t6-complete-terminal-schedule-registry-v1.json"
)
RUNTIME_PATH = "scripts/t6_persistent_selector_runtime_v2.py"
HEAD_BOUND_DEPENDENCIES = (
    RUNTIME_PATH,
    "scripts/t6_acyclic_transition_bundle_v2.py",
    "scripts/t6_complete_terminal_receipts_v1.py",
)
LOADED_DEPENDENCY_MODULES = MappingProxyType(
    {
        RUNTIME_PATH: sys.modules[__name__],
        "scripts/t6_acyclic_transition_bundle_v2.py": acyclic_v2,
        "scripts/t6_complete_terminal_receipts_v1.py": terminal_contract,
    }
)
REGULAR_GIT_MODES = frozenset({"100644", "100755"})


class RuntimeRejectCodeV2(str, Enum):
    AUTHORITY_RESOLUTION_FAILED = "AUTHORITY_RESOLUTION_FAILED"
    AUTHORITY_STATE_INVALID = "AUTHORITY_STATE_INVALID"
    EXACT_HEAD_DEPENDENCY_MISMATCH = "EXACT_HEAD_DEPENDENCY_MISMATCH"
    CALLER_BOOTSTRAP_PAYLOAD_FORBIDDEN = "CALLER_BOOTSTRAP_PAYLOAD_FORBIDDEN"
    BOOTSTRAP_AUTHORITY_UNAVAILABLE = "BOOTSTRAP_AUTHORITY_UNAVAILABLE"
    CALLER_OR_LEGACY_SUCCESSOR_FORBIDDEN = (
        "CALLER_OR_LEGACY_SUCCESSOR_FORBIDDEN"
    )
    V2_BUNDLE_INVALID = "V2_BUNDLE_INVALID"
    SUCCESSOR_AUTHORITY_UNAVAILABLE = "SUCCESSOR_AUTHORITY_UNAVAILABLE"


class RuntimeContractErrorV2(ValueError):
    """Stable fail-closed rejection from the V2 runtime boundary."""

    def __init__(self, code: RuntimeRejectCodeV2, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


@dataclass(frozen=True, slots=True)
class _ExactHeadBlobV2:
    path: str
    git_mode: str
    git_object_id: str
    content: bytes

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.content).hexdigest()


@dataclass(frozen=True, slots=True)
class ZeroAuthoritySnapshotV2:
    """Sealed facts used to construct the non-activating runtime."""

    schema_id: str
    schema_version: int
    runtime_id: str
    head_sha: str
    head_tree_sha: str
    coordinator_registry_digest: str
    terminal_registry_id: str
    terminal_registry_digest: str
    terminal_registry_git_object_id: str
    terminal_registry_blob_sha256: str
    active_role_grant_count: int
    authorized_route_count: int
    initializer_count: int
    complete_terminal_schedule_count: int
    status: str
    proof_boundary: str
    digest: str


class _FactoryOnlyV2:
    __slots__ = ()

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} must be created by its V2 factory")


@dataclass(frozen=True, init=False, slots=True)
class SuccessorAdmissionRequestV2(_FactoryOnlyV2):
    """Non-authorizing wrapper around the existing acyclic V2 end products."""

    target: acyclic_v2.RawTargetStateV2
    transition_bundle: acyclic_v2.FinalTransitionReceiptBundleV2
    admission_sidecar: acyclic_v2.StateAdmissionSidecarV2


@dataclass(frozen=True, init=False, slots=True)
class PersistentSelectorRuntimeV2(_FactoryOnlyV2):
    """A frozen runtime with zero routes, zero initializers and an empty queue."""

    _authority: ZeroAuthoritySnapshotV2
    _queue: tuple[acyclic_v2.StateAdmissionSidecarV2, ...]

    def authority_snapshot_v2(self) -> ZeroAuthoritySnapshotV2:
        return self._authority

    def authority_mapping_v2(self) -> dict[str, Any]:
        return snapshot_to_mapping_v2(self._authority)

    def route_ids_v2(self) -> tuple[str, ...]:
        return ()

    def initializer_ids_v2(self) -> tuple[str, ...]:
        return ()

    def queue_snapshot_v2(
        self,
    ) -> tuple[acyclic_v2.StateAdmissionSidecarV2, ...]:
        return self._queue

    def bootstrap_v2(self, request: object = None) -> NoReturn:
        """Reject every bootstrap attempt; no initializer is authorized."""

        if request is not None:
            raise RuntimeContractErrorV2(
                RuntimeRejectCodeV2.CALLER_BOOTSTRAP_PAYLOAD_FORBIDDEN,
                "V2 has no caller raw-state or initializer payload surface",
            )
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.BOOTSTRAP_AUTHORITY_UNAVAILABLE,
            "the exact-HEAD coordinator registry authorizes zero initializers",
        )

    def admit_successor_v2(self, request: object) -> NoReturn:
        """Validate only the V2 wrapper shape, then reject before queue mutation."""

        before = self._queue
        if type(request) is not SuccessorAdmissionRequestV2:
            raise RuntimeContractErrorV2(
                RuntimeRejectCodeV2.CALLER_OR_LEGACY_SUCCESSOR_FORBIDDEN,
                "only the factory-sealed acyclic V2 request shape is recognized",
            )
        try:
            _validate_successor_request_v2(request)
        except (acyclic_v2.AcyclicBundleValidationError, AttributeError) as exc:
            if self._queue is not before:
                raise AssertionError("queue changed during rejected V2 validation")
            raise RuntimeContractErrorV2(
                RuntimeRejectCodeV2.V2_BUNDLE_INVALID,
                f"acyclic V2 request failed replay: {exc}",
            ) from exc
        if self._queue is not before:
            raise AssertionError("queue changed before authority rejection")
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.SUCCESSOR_AUTHORITY_UNAVAILABLE,
            "the exact-HEAD coordinator registry authorizes zero successor routes",
        )


def _plain_zero(value: Any) -> bool:
    return type(value) is int and value == 0


def _canonical_snapshot_payload_v2(
    snapshot: ZeroAuthoritySnapshotV2,
) -> dict[str, Any]:
    return {
        field.name: getattr(snapshot, field.name)
        for field in fields(ZeroAuthoritySnapshotV2)
        if field.name != "digest"
    }


def snapshot_to_mapping_v2(snapshot: ZeroAuthoritySnapshotV2) -> dict[str, Any]:
    if type(snapshot) is not ZeroAuthoritySnapshotV2:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "authority snapshot must have the exact V2 type",
        )
    payload = _canonical_snapshot_payload_v2(snapshot)
    expected = acyclic_v2.canonical_digest_v2(payload)
    if snapshot.digest != expected:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "authority snapshot digest does not replay",
        )
    payload["digest"] = snapshot.digest
    return payload


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
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
            f"git {' '.join(args)} failed: {detail}",
        )
    return completed.stdout


def _repository_root_v2(locator: Path) -> Path:
    raw = _run_git_v2(locator.resolve(), ("rev-parse", "--show-toplevel"))
    try:
        return Path(raw.decode("utf-8").strip()).resolve()
    except UnicodeDecodeError as exc:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
            "repository root is not UTF-8",
        ) from exc


def _read_exact_head_blob_v2(
    root: Path, head_sha: str, path: str
) -> _ExactHeadBlobV2:
    raw = _run_git_v2(
        root,
        ("ls-tree", "-z", "--full-tree", head_sha, "--", path),
    )
    records = [record for record in raw.split(b"\0") if record]
    if len(records) != 1:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
            f"{path!r} is not one exact requested-HEAD entry",
        )
    try:
        metadata, encoded_path = records[0].split(b"\t", 1)
        mode, object_type, object_id = metadata.decode("ascii").split(" ")
        observed_path = encoded_path.decode("utf-8")
    except (UnicodeDecodeError, ValueError) as exc:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
            f"invalid Git tree entry for {path!r}",
        ) from exc
    if (
        observed_path != path
        or mode not in REGULAR_GIT_MODES
        or object_type != "blob"
        or len(object_id) != 40
    ):
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
            f"{path!r} is not the required regular Git blob",
        )
    content = _run_git_v2(root, ("cat-file", "blob", object_id))
    return _ExactHeadBlobV2(path, mode, object_id, content)


def _require_executing_dependency_at_head_v2(
    root: Path, head_sha: str, path: str
) -> _ExactHeadBlobV2:
    blob = _read_exact_head_blob_v2(root, head_sha, path)
    worktree = root / path
    if worktree.is_symlink() or not worktree.is_file():
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.EXACT_HEAD_DEPENDENCY_MISMATCH,
            f"{path} is not a regular worktree dependency",
        )
    if worktree.read_bytes() != blob.content:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.EXACT_HEAD_DEPENDENCY_MISMATCH,
            f"{path} differs from the requested-HEAD dependency",
        )
    loaded_module = LOADED_DEPENDENCY_MODULES[path]
    loaded_file = getattr(loaded_module, "__file__", None)
    if not isinstance(loaded_file, str):
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.EXACT_HEAD_DEPENDENCY_MISMATCH,
            f"loaded module for {path} has no regular backing file",
        )
    loaded_path = Path(loaded_file)
    if (
        loaded_path.is_symlink()
        or not loaded_path.is_file()
        or loaded_path.read_bytes() != blob.content
    ):
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.EXACT_HEAD_DEPENDENCY_MISMATCH,
            f"loaded module for {path} differs from the requested-HEAD dependency",
        )
    return blob


def _strict_json_object_v2(raw: bytes, *, source: str) -> dict[str, Any]:
    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}")
            result[key] = value
        return result

    def reject_constant(value: str) -> NoReturn:
        raise ValueError(f"non-finite number {value}")

    try:
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=object_pairs,
            parse_constant=reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
            f"cannot parse {source}: {exc}",
        ) from exc
    if not isinstance(value, dict):
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
            f"{source} must contain one JSON object",
        )
    return value


def _validate_zero_role_authority_v2(resolved: Mapping[str, Any]) -> None:
    unsigned = dict(resolved)
    observed_digest = unsigned.pop("registry_digest", None)
    if (
        type(observed_digest) is not str
        or observed_digest != role_registry.canonical_digest_v1(unsigned)
    ):
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "coordinator resolved-registry digest does not replay",
        )
    required_empty_lists = (
        "resolved_role_grants",
        "authorized_branches",
        "complete_terminal_schedules",
    )
    if any(type(resolved.get(key)) is not list for key in required_empty_lists):
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "coordinator authority collections must be JSON arrays",
        )
    if any(resolved[key] != [] for key in required_empty_lists):
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "this runtime revision cannot activate coordinator role grants",
        )
    count_keys = (
        "active_role_grant_count",
        "active_producer_count",
        "complete_terminal_schedule_count",
    )
    if any(not _plain_zero(resolved.get(key)) for key in count_keys):
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "coordinator authority counts must be exact integer zero",
        )
    role_counts = resolved.get("role_grant_counts")
    expected_role_count_keys = set(role_registry.ROLE_DIGEST_KEYS.values())
    if (
        type(role_counts) is not dict
        or set(role_counts) != expected_role_count_keys
        or any(not _plain_zero(value) for value in role_counts.values())
    ):
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "all coordinator role subregistries must have exact count zero",
        )
    inventory = resolved.get("artifact_evidence_inventory")
    if not isinstance(inventory, Mapping) or inventory.get("role_authority") is not False:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "evidence inventory must remain explicitly non-authorizing",
        )
    if resolved.get("status") != role_registry.RESOLVED_STATUS:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "coordinator status is not the supported zero-authority state",
        )


def _validate_successor_request_v2(request: SuccessorAdmissionRequestV2) -> None:
    target = request.target
    bundle = request.transition_bundle
    sidecar = request.admission_sidecar
    if (
        type(target) is not acyclic_v2.RawTargetStateV2
        or type(bundle) is not acyclic_v2.FinalTransitionReceiptBundleV2
        or type(sidecar) is not acyclic_v2.StateAdmissionSidecarV2
    ):
        raise acyclic_v2.AcyclicBundleValidationError(
            acyclic_v2.AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "request fields must have the exact acyclic V2 artifact types",
        )
    target_mapping = acyclic_v2.artifact_to_mapping_v2(target)
    bundle_mapping = acyclic_v2.artifact_to_mapping_v2(bundle)
    sidecar_mapping = acyclic_v2.artifact_to_mapping_v2(sidecar)
    if (
        target.successor_origin.edge_anchor_id != bundle.edge_anchor_id
        or target.successor_origin.edge_anchor_digest != bundle.edge_anchor_digest
    ):
        raise acyclic_v2.AcyclicBundleValidationError(
            acyclic_v2.AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "target origin and transition bundle name different edge anchors",
        )
    if target_mapping["state_id"] != bundle_mapping["target_state_id"]:
        raise acyclic_v2.AcyclicBundleValidationError(
            acyclic_v2.AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "transition bundle names another target state",
        )
    acyclic_v2.parse_state_admission_sidecar_v2(
        sidecar_mapping,
        target,
        bundle,
    )


def make_successor_admission_request_v2(
    target: acyclic_v2.RawTargetStateV2,
    transition_bundle: acyclic_v2.FinalTransitionReceiptBundleV2,
    admission_sidecar: acyclic_v2.StateAdmissionSidecarV2,
) -> SuccessorAdmissionRequestV2:
    request = object.__new__(SuccessorAdmissionRequestV2)
    object.__setattr__(request, "target", target)
    object.__setattr__(request, "transition_bundle", transition_bundle)
    object.__setattr__(request, "admission_sidecar", admission_sidecar)
    try:
        _validate_successor_request_v2(request)
    except (acyclic_v2.AcyclicBundleValidationError, AttributeError) as exc:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.V2_BUNDLE_INVALID,
            f"cannot construct acyclic V2 request: {exc}",
        ) from exc
    return request


def _make_snapshot_v2(
    *,
    resolved: Mapping[str, Any],
    terminal_registry: terminal_contract.ProductionTerminalScheduleRegistryV1,
    terminal_blob: _ExactHeadBlobV2,
) -> ZeroAuthoritySnapshotV2:
    values: dict[str, Any] = {
        "schema_id": "t6_persistent_selector_zero_authority_snapshot_v2",
        "schema_version": 2,
        "runtime_id": RUNTIME_ID,
        "head_sha": resolved["head_sha"],
        "head_tree_sha": resolved["head_tree_sha"],
        "coordinator_registry_digest": resolved["registry_digest"],
        "terminal_registry_id": terminal_registry.registry_id,
        "terminal_registry_digest": terminal_registry.registry_digest,
        "terminal_registry_git_object_id": terminal_blob.git_object_id,
        "terminal_registry_blob_sha256": terminal_blob.sha256,
        "active_role_grant_count": 0,
        "authorized_route_count": 0,
        "initializer_count": 0,
        "complete_terminal_schedule_count": 0,
        "status": RUNTIME_STATUS,
        "proof_boundary": PROOF_BOUNDARY,
    }
    digest = acyclic_v2.canonical_digest_v2(values)
    return ZeroAuthoritySnapshotV2(**values, digest=digest)


def open_runtime_v2(*, root: Path, requested_head: str) -> PersistentSelectorRuntimeV2:
    """Open the sole V2 runtime shape from fixed exact-HEAD zero-authority data.

    The signature intentionally has no caller registry, callable, receipt,
    evidence-ID or artifact-manifest parameters.
    """

    try:
        resolved = role_registry.resolve_registry_v1(
            root=root,
            requested_head=requested_head,
        )
    except role_registry.RegistryError as exc:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
            f"coordinator role registry rejected: {exc.code}: {exc.detail}",
        ) from exc
    _validate_zero_role_authority_v2(resolved)
    repository = _repository_root_v2(root)
    if resolved.get("head_sha") != requested_head:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
            "resolved coordinator registry changed the requested exact HEAD",
        )
    for path in HEAD_BOUND_DEPENDENCIES:
        _require_executing_dependency_at_head_v2(repository, requested_head, path)
    terminal_blob = _read_exact_head_blob_v2(
        repository,
        requested_head,
        TERMINAL_REGISTRY_PATH,
    )
    terminal_mapping = _strict_json_object_v2(
        terminal_blob.content,
        source=f"{requested_head}:{TERMINAL_REGISTRY_PATH}",
    )
    try:
        terminal_registry = terminal_contract.parse_production_registry_v1(
            terminal_mapping
        )
    except terminal_contract.TerminalReceiptValidationError as exc:
        raise RuntimeContractErrorV2(
            RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
            f"complete-terminal registry rejected: {exc.code.value}: {exc.detail}",
        ) from exc
    snapshot = _make_snapshot_v2(
        resolved=resolved,
        terminal_registry=terminal_registry,
        terminal_blob=terminal_blob,
    )
    runtime = object.__new__(PersistentSelectorRuntimeV2)
    object.__setattr__(runtime, "_authority", snapshot)
    object.__setattr__(runtime, "_queue", ())
    return runtime


__all__ = [
    "PROOF_BOUNDARY",
    "RUNTIME_ID",
    "RUNTIME_STATUS",
    "RUNTIME_VERSION",
    "PersistentSelectorRuntimeV2",
    "RuntimeContractErrorV2",
    "RuntimeRejectCodeV2",
    "SuccessorAdmissionRequestV2",
    "ZeroAuthoritySnapshotV2",
    "make_successor_admission_request_v2",
    "open_runtime_v2",
    "snapshot_to_mapping_v2",
]
