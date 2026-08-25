#!/usr/bin/env python3
"""Generate and verify the ephemeral, HEAD-bound T6 live audit snapshot v2.

The snapshot is deliberately generated from Git objects, not from the working
tree.  A dirty checkout therefore cannot be described as evidence for HEAD.
The output itself is ephemeral because a tracked file cannot contain the SHA
of the commit that contains that same file.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
from typing import Any, Iterable, Mapping, Protocol, Sequence
import urllib.error
import urllib.parse
import urllib.request


SCHEMA_ID = "t6_live_audit_snapshot_v2"
SCHEMA_VERSION = 2
FILE_SET_SCHEMA_ID = "t6_ci_file_set_v1"
DEFAULT_OUTPUT = Path("data/t6-wave1/t6-live-audit-snapshot-v2.json")
LIVE_SNAPSHOT_SCRIPT_PATH = "scripts/t6_live_audit_snapshot_v2.py"
LIVE_SNAPSHOT_SCHEMA_PATH = "schemas/t6-live-audit-snapshot-v2.schema.json"
GATE0_PROVENANCE_SCHEMA_PATH = "schemas/t6-gate0-run-provenance-v1.schema.json"
CI_MANIFEST_TOOL_PATH = "scripts/t6_ci_run_manifest_v1.py"

TRUSTED_REPOSITORY = "priestess-bot/erdos-straus"
TRUSTED_REPOSITORY_ID = 1_313_520_032
TRUSTED_WORKFLOW_ID = 321_454_335
TRUSTED_WORKFLOW_PATH = ".github/workflows/research-kb-ci.yml"
TRUSTED_WORKFLOW_NAME = "T6 Gate 0 and research knowledge base"
TRUSTED_GATE0_JOB_NAME = "gate-zero"
TRUSTED_ARTIFACT_NAME = "ci-run-manifest-v1.json"
LIVE_SNAPSHOT_LOCATOR = "data/t6-wave1/t6-live-audit-snapshot-v2.json"

TOOLCHAIN_PATHS = (
    LIVE_SNAPSHOT_SCRIPT_PATH,
    LIVE_SNAPSHOT_SCHEMA_PATH,
    GATE0_PROVENANCE_SCHEMA_PATH,
    CI_MANIFEST_TOOL_PATH,
)

WORKPACK_PATH = "data/t6-f2-f3-wave1-workpack.json"
PROOF_FRONTIER_PATH = "data/t6-proof-frontier-v2.json"
INVENTORY_PATH = "data/t6-constructor-inventory-v1.json"
RUNTIME_FREEZE_PATH = "data/t6-runtime-protocol-freeze-a-v1.json"
GRAMMAR_PATH = "data/t6-wave1/family-grammar-freeze-v1.json"
RESIDUAL_FRONTIER_PATH = "data/t6-wave1/t6-f2-f3-residual-frontier-v1.json"
T5_PHASE_REGISTRY_PATH = "data/t5-full-phase-registry-v2.json"
T5_TAXONOMY_PATH = "data/t5-full-transition-taxonomy-v2.json"
Q1_RUNTIME_DATA_PATH = "data/t6-wave1/q1-full-carrier-runtime-slice-v1.json"
LEDGER_PATH = "data/t6-selector-obligation-ledger-v1.json"
F1_RECEIPT_PATH = "data/t6-f1-reachability-proof-receipt-v1.json"
README_PATH = "README.md"

CONSUMER_PATHS = {
    "readme": README_PATH,
    "selector_ledger": LEDGER_PATH,
    "proof_frontier": PROOF_FRONTIER_PATH,
    "residual_frontier": RESIDUAL_FRONTIER_PATH,
}

PRODUCER_REGISTRY_FIXED_PATHS = (
    INVENTORY_PATH,
    PROOF_FRONTIER_PATH,
    RESIDUAL_FRONTIER_PATH,
    RUNTIME_FREEZE_PATH,
    Q1_RUNTIME_DATA_PATH,
)

TERMINAL_SCHEDULE_FIXED_PATHS = (
    RUNTIME_FREEZE_PATH,
    Q1_RUNTIME_DATA_PATH,
)

T5_PATHS = (T5_PHASE_REGISTRY_PATH, T5_TAXONOMY_PATH)

INDEPENDENT_REVIEW_PATHS = (
    "data/t6-wave1/f3-qc1-cross-audit-by-agent6-v1.json",
    "docs/T6_F2_F3_GATE_AUDIT_2026-08-25.md",
    "docs/T6_F2_F3_THIRD_WAVE_PROOF_REVIEW_2026-08-25.md",
    "docs/handoffs/F3_HIGH_QC1_INDEPENDENT_REVIEW_2026-08-25.md",
)

MANIFEST_PATHS = {
    "workpack": WORKPACK_PATH,
    "proof_frontier": PROOF_FRONTIER_PATH,
    "constructor_inventory": INVENTORY_PATH,
    "runtime_protocol_freeze": RUNTIME_FREEZE_PATH,
    "family_grammar_freeze": GRAMMAR_PATH,
    "residual_frontier": RESIDUAL_FRONTIER_PATH,
    "t5_phase_registry": T5_PHASE_REGISTRY_PATH,
    "t5_transition_taxonomy": T5_TAXONOMY_PATH,
    "selector_obligation_ledger": LEDGER_PATH,
    "f1_reachability_receipt": F1_RECEIPT_PATH,
    "readme": README_PATH,
}

DIGEST_SCOPES = {
    "claim_set": (
        "All tracked claims/**/*.md plus the repository proof frontier and "
        "wave1 residual frontier at current_observed_head_sha."
    ),
    "runtime_source": (
        "Shared selector state/runtime, scheduler adapter, q=1 runtime slice, "
        "and runtime freeze manifest at current_observed_head_sha."
    ),
    "producer_registry": (
        "File-set digest over the current constructor inventory, local executable "
        "registration dependencies, and frontier manifests. The Gate-0 semantic "
        "registry digest, when attested, remains a separate digest domain."
    ),
    "terminal_schedule": (
        "Current runtime and q=1 source/target terminal schedule surface; this "
        "digest does not assert global schedule completeness."
    ),
    "t5_taxonomy": (
        "T5 phase registry v2 and transition taxonomy v2 at "
        "current_observed_head_sha."
    ),
    "test_manifest": (
        "All tracked tests/**/*.py files recursively at "
        "current_observed_head_sha."
    ),
    "independent_review": (
        "The fixed coordinator/independent cross-audit artifact set at "
        "current_observed_head_sha; track-owned supporting artifacts are excluded."
    ),
}

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")
STATUS_KEYS = ("F1", "F2", "F3", "T6")
HEAD_RELATIONS = {
    "NO_VERIFIED_HEAD",
    "EQUAL",
    "ADVANCED_UNVERIFIED",
    "DIVERGED",
}
VERIFICATION_STATES = {
    "NO_VERIFIED_HEAD",
    "VERIFIED_HEAD",
    "UNVERIFIED_HEAD_ADVANCE",
    "DIVERGED_FROM_VERIFIED_HEAD",
}
INTEGRATION_HEAD_RELATIONS = {"EQUAL", "ADVANCED", "DIVERGED"}
EXPECTED_TOP_LEVEL_KEYS = frozenset(
    {
        "schema_id",
        "schema_version",
        "artifact_policy",
        "observed_at",
        "repository",
        "integration_branch",
        "workpack_origin_sha",
        "integration_audited_sha",
        "integration_head_relation",
        "current_observed_head_sha",
        "last_verified_head_sha",
        "last_verified_basis",
        "head_relation",
        "verification_state",
        "status_upgrade_allowed",
        "execution_binding",
        "current_digest_audit",
        "consumer_policy",
        "digest_algorithm",
        "claim_set_digest",
        "runtime_source_digest",
        "producer_registry_digest",
        "terminal_schedule_digest",
        "grammar_hash",
        "t5_taxonomy_digest",
        "test_manifest_digest",
        "independent_review_digest",
        "digest_inputs",
        "manifest_digests",
        "manifest_statuses",
        "status",
        "proof_boundary",
    }
)
ATTESTATION_BASIS_KEYS = frozenset(
    {"schema_id", "content_replay", "github_provenance"}
)
CONTENT_REPLAY_KEYS = frozenset(
    {
        "schema_id",
        "run_manifest_schema_id",
        "manifest_payload_sha256",
        "manifest_bytes_sha256",
        "head_sha",
        "head_tree_sha",
        "status",
        "content_replay",
        "producer_registry_status",
        "digest_domain",
        "digests",
    }
)
ATTESTATION_DIGEST_KEYS = frozenset(
    {
        "kb_claim_set_digest",
        "runtime_source_digest",
        "producer_registry_digest",
        "grammar_hash",
        "test_manifest_digest",
    }
)
GITHUB_PROVENANCE_KEYS = frozenset(
    {
        "schema_id",
        "schema_version",
        "source",
        "repository",
        "repository_id",
        "workflow_id",
        "workflow_name",
        "workflow_path",
        "workflow_state",
        "run_id",
        "run_attempt",
        "run_head_sha",
        "run_event",
        "run_head_branch",
        "head_repository_id",
        "run_status",
        "run_conclusion",
        "success_basis",
        "job_id",
        "job_name",
        "job_status",
        "job_conclusion",
        "artifact_id",
        "artifact_name",
        "artifact_expired",
        "artifact_expires_at",
        "artifact_size_in_bytes",
        "artifact_digest",
        "artifact_workflow_run_id",
        "artifact_workflow_run_head_sha",
        "environment_cross_check",
    }
)


class SnapshotError(RuntimeError):
    """Raised when the repository cannot produce a trustworthy snapshot."""


@dataclass(frozen=True)
class Gate0RunLocatorV1:
    repository: str
    workflow_id: int
    workflow_path: str
    run_id: int
    run_attempt: int
    job_id: int
    artifact_id: int
    artifact_name: str

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> Gate0RunLocatorV1:
        expected = {
            "schema_id",
            "schema_version",
            "repository",
            "workflow_id",
            "workflow_path",
            "run_id",
            "run_attempt",
            "job_id",
            "artifact_id",
            "artifact_name",
        }
        if set(value) != expected:
            raise SnapshotError("Gate-0 provenance locator has unknown or missing fields")
        if value.get("schema_id") != "t6_gate0_run_locator_v1":
            raise SnapshotError("Gate-0 provenance locator schema_id is invalid")
        if type(value.get("schema_version")) is not int or value.get("schema_version") != 1:
            raise SnapshotError("Gate-0 provenance locator schema_version is invalid")
        fixed = {
            "repository": TRUSTED_REPOSITORY,
            "workflow_id": TRUSTED_WORKFLOW_ID,
            "workflow_path": TRUSTED_WORKFLOW_PATH,
            "artifact_name": TRUSTED_ARTIFACT_NAME,
        }
        for field, expected_value in fixed.items():
            if value.get(field) != expected_value:
                raise SnapshotError(
                    f"Gate-0 provenance locator {field} is not the trusted value"
                )
        integers: dict[str, int] = {}
        for field in ("workflow_id", "run_id", "run_attempt", "job_id", "artifact_id"):
            item = value.get(field)
            if not isinstance(item, int) or isinstance(item, bool) or item <= 0:
                raise SnapshotError(f"Gate-0 provenance locator {field} must be positive")
            integers[field] = item
        return cls(
            repository=TRUSTED_REPOSITORY,
            workflow_id=integers["workflow_id"],
            workflow_path=TRUSTED_WORKFLOW_PATH,
            run_id=integers["run_id"],
            run_attempt=integers["run_attempt"],
            job_id=integers["job_id"],
            artifact_id=integers["artifact_id"],
            artifact_name=TRUSTED_ARTIFACT_NAME,
        )

    def payload(self) -> dict[str, Any]:
        return {
            "schema_id": "t6_gate0_run_locator_v1",
            "schema_version": 1,
            "repository": self.repository,
            "workflow_id": self.workflow_id,
            "workflow_path": self.workflow_path,
            "run_id": self.run_id,
            "run_attempt": self.run_attempt,
            "job_id": self.job_id,
            "artifact_id": self.artifact_id,
            "artifact_name": self.artifact_name,
        }


class GitHubApiClientV1(Protocol):
    def get_workflow(self, repository: str, workflow_id: int) -> Mapping[str, Any]: ...

    def get_run_attempt(
        self, repository: str, run_id: int, run_attempt: int
    ) -> Mapping[str, Any]: ...

    def list_run_attempt_jobs(
        self, repository: str, run_id: int, run_attempt: int
    ) -> Sequence[Mapping[str, Any]]: ...

    def get_artifact(self, repository: str, artifact_id: int) -> Mapping[str, Any]: ...


class CurrentDigestAuditClientV1(Protocol):
    def verify_current_digest_vector(
        self,
        *,
        repository: str,
        head_sha: str,
        digest_vector: Mapping[str, str],
    ) -> Mapping[str, Any]: ...


@dataclass(frozen=True)
class GitHubRestApiClientV1:
    token: str | None = None
    api_url: str = "https://api.github.com"

    def _get(self, endpoint: str) -> dict[str, Any]:
        url = self.api_url.rstrip("/") + endpoint
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "erdos-straus-t6-live-audit-snapshot-v2",
            "X-GitHub-Api-Version": "2026-03-10",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = response.read()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            raise SnapshotError(f"GitHub API request failed for {endpoint}: {exc}") from exc
        return _load_json_object_bytes(payload, source=url)

    @staticmethod
    def _repo_path(repository: str) -> str:
        if repository != TRUSTED_REPOSITORY:
            raise SnapshotError("GitHub API repository is not trusted")
        return urllib.parse.quote(repository, safe="/")

    def get_workflow(self, repository: str, workflow_id: int) -> Mapping[str, Any]:
        repo = self._repo_path(repository)
        return self._get(f"/repos/{repo}/actions/workflows/{workflow_id}")

    def get_run_attempt(
        self, repository: str, run_id: int, run_attempt: int
    ) -> Mapping[str, Any]:
        repo = self._repo_path(repository)
        return self._get(f"/repos/{repo}/actions/runs/{run_id}/attempts/{run_attempt}")

    def list_run_attempt_jobs(
        self, repository: str, run_id: int, run_attempt: int
    ) -> Sequence[Mapping[str, Any]]:
        repo = self._repo_path(repository)
        jobs: list[Mapping[str, Any]] = []
        page = 1
        total: int | None = None
        while total is None or len(jobs) < total:
            payload = self._get(
                f"/repos/{repo}/actions/runs/{run_id}/attempts/{run_attempt}/jobs"
                f"?per_page=100&page={page}"
            )
            page_jobs = payload.get("jobs")
            page_total = payload.get("total_count")
            if (
                not isinstance(page_jobs, list)
                or not all(isinstance(item, dict) for item in page_jobs)
                or not isinstance(page_total, int)
                or page_total < 0
            ):
                raise SnapshotError("GitHub jobs response is invalid")
            if total is None:
                total = page_total
            elif total != page_total:
                raise SnapshotError("GitHub jobs pagination total changed")
            jobs.extend(page_jobs)
            if not page_jobs and len(jobs) < total:
                raise SnapshotError("GitHub jobs pagination ended early")
            page += 1
        if len(jobs) != total:
            raise SnapshotError("GitHub jobs response count is invalid")
        return jobs

    def get_artifact(self, repository: str, artifact_id: int) -> Mapping[str, Any]:
        repo = self._repo_path(repository)
        return self._get(f"/repos/{repo}/actions/artifacts/{artifact_id}")


@dataclass(frozen=True)
class AuditResult:
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    observed_head_sha: str
    head_relation: str | None
    status_upgrade_allowed: bool

    @property
    def ok(self) -> bool:
        return not self.errors

    def payload(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "observed_head_sha": self.observed_head_sha,
            "head_relation": self.head_relation,
            "status_upgrade_allowed": self.status_upgrade_allowed,
            "errors": list(self.errors),
            "warnings": list(self.warnings),
        }


@dataclass(frozen=True)
class VerifiedGate0Attestation:
    head_sha: str
    basis: Mapping[str, Any]


def _git(root: Path, args: Sequence[str], *, check: bool = True) -> bytes:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if check and completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise SnapshotError(f"git {' '.join(args)} failed: {detail}")
    return completed.stdout


def resolve_head(root: Path) -> str:
    value = _git(root, ("rev-parse", "--verify", "HEAD")).decode().strip()
    if not SHA_RE.fullmatch(value):
        raise SnapshotError(f"git returned a non-SHA HEAD: {value!r}")
    return value


def _commit_exists(root: Path, revision: str) -> bool:
    completed = subprocess.run(
        ["git", "cat-file", "-e", f"{revision}^{{commit}}"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    return completed.returncode == 0


def _is_ancestor(root: Path, ancestor: str, descendant: str) -> bool:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", ancestor, descendant],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if completed.returncode not in (0, 1):
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise SnapshotError(f"cannot compare {ancestor} and {descendant}: {detail}")
    return completed.returncode == 0


def head_relation(root: Path, last_verified: str | None, observed: str) -> str:
    if last_verified is None:
        return "NO_VERIFIED_HEAD"
    if last_verified == observed:
        return "EQUAL"
    if not _commit_exists(root, last_verified):
        raise SnapshotError(f"last verified commit is unavailable: {last_verified}")
    if not _commit_exists(root, observed):
        raise SnapshotError(f"observed commit is unavailable: {observed}")
    if _is_ancestor(root, last_verified, observed):
        return "ADVANCED_UNVERIFIED"
    return "DIVERGED"


def integration_head_relation(root: Path, audited: str, observed: str) -> str:
    if audited == observed:
        return "EQUAL"
    if _is_ancestor(root, audited, observed):
        return "ADVANCED"
    return "DIVERGED"


def _verification_state(relation: str) -> str:
    return {
        "NO_VERIFIED_HEAD": "NO_VERIFIED_HEAD",
        "EQUAL": "VERIFIED_HEAD",
        "ADVANCED_UNVERIFIED": "UNVERIFIED_HEAD_ADVANCE",
        "DIVERGED": "DIVERGED_FROM_VERIFIED_HEAD",
    }[relation]


def canonical_json_bytes(value: Any) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("ascii")
    except (TypeError, ValueError) as exc:
        raise SnapshotError(f"value is not canonical JSON: {exc}") from exc


def canonical_json_line_bytes(value: Any) -> bytes:
    """Match ``jq -cS`` for the existing grammar hash contract."""
    return canonical_json_bytes(value) + b"\n"


@lru_cache(maxsize=16)
def _tracked_entries(root: Path, revision: str) -> dict[str, tuple[str, str]]:
    raw = _git(root, ("ls-tree", "-r", "-z", revision))
    entries: dict[str, tuple[str, str]] = {}
    for item in raw.split(b"\0"):
        if not item:
            continue
        try:
            metadata, raw_path = item.split(b"\t", 1)
            mode, object_type, object_id = metadata.decode("ascii").split(" ")
            path = raw_path.decode("utf-8")
        except (UnicodeDecodeError, ValueError) as exc:
            raise SnapshotError(f"cannot parse git ls-tree record: {item!r}") from exc
        if object_type != "blob":
            continue
        entries[path] = (mode, object_id)
    return entries


def _tracked_paths(root: Path, revision: str) -> tuple[str, ...]:
    return tuple(sorted(_tracked_entries(root, revision)))


def _blob(root: Path, revision: str, path: str) -> bytes:
    if PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts:
        raise SnapshotError(f"unsafe snapshot input path: {path!r}")
    return _git(root, ("show", f"{revision}:{path}"))


def _blobs(
    root: Path, revision: str, paths: Sequence[str]
) -> dict[str, bytes]:
    entries = _tracked_entries(root, revision)
    missing = sorted(set(paths) - set(entries))
    if missing:
        raise SnapshotError(f"paths absent at {revision}: {missing}")
    process = subprocess.Popen(
        ["git", "cat-file", "--batch"],
        cwd=root,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    requests = b"".join(
        f"{entries[path][1]}\n".encode("ascii") for path in paths
    )
    stdout, stderr = process.communicate(requests)
    if process.returncode != 0:
        detail = stderr.decode("utf-8", errors="replace").strip()
        raise SnapshotError(f"git cat-file --batch failed: {detail}")
    result: dict[str, bytes] = {}
    cursor = 0
    for path in paths:
        line_end = stdout.find(b"\n", cursor)
        if line_end < 0:
            raise SnapshotError("truncated git cat-file header")
        header = stdout[cursor:line_end].decode("ascii", errors="replace")
        fields = header.split(" ")
        if len(fields) != 3 or fields[1] != "blob":
            raise SnapshotError(f"unexpected git cat-file header: {header!r}")
        try:
            size = int(fields[2])
        except ValueError as exc:
            raise SnapshotError(f"invalid git blob size: {header!r}") from exc
        start = line_end + 1
        end = start + size
        if end >= len(stdout) or stdout[end : end + 1] != b"\n":
            raise SnapshotError("truncated git cat-file payload")
        result[path] = stdout[start:end]
        cursor = end + 1
    if cursor != len(stdout):
        raise SnapshotError("unexpected trailing data from git cat-file --batch")
    return result


def _load_json_object_bytes(value: bytes, *, source: str) -> dict[str, Any]:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, item in pairs:
            if key in result:
                raise SnapshotError(f"duplicate JSON key {key!r} in {source}")
            result[key] = item
        return result

    def reject_constant(value: str) -> None:
        raise SnapshotError(f"non-finite JSON value {value!r} in {source}")

    try:
        decoded = json.loads(
            value.decode("utf-8"),
            object_pairs_hook=reject_duplicates,
            parse_constant=reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SnapshotError(f"invalid JSON in {source}: {exc}") from exc
    if not isinstance(decoded, dict):
        raise SnapshotError(f"top-level JSON is not an object in {source}")
    return decoded


def _json_blob(root: Path, revision: str, path: str) -> dict[str, Any]:
    return _load_json_object_bytes(
        _blob(root, revision, path), source=f"{revision}:{path}"
    )


def _capture_execution_binding(root: Path, revision: str) -> dict[str, Any]:
    """Bind the executing verifier, both schemas and Gate-0 verifier to HEAD."""

    if resolve_head(root) != revision:
        raise SnapshotError("HEAD_DRIFT_BEFORE_EXECUTION_BINDING")
    status = subprocess.run(
        [
            "git",
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
            "--",
            *TOOLCHAIN_PATHS,
        ],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if status.returncode != 0:
        raise SnapshotError("cannot inspect live snapshot toolchain worktree status")
    dirty = status.stdout.decode("utf-8", errors="replace").strip()
    if dirty:
        raise SnapshotError(f"DIRTY_LIVE_SNAPSHOT_TOOLCHAIN: {dirty}")

    tracked = _tracked_entries(root, revision)
    files: list[dict[str, Any]] = []
    for path in sorted(TOOLCHAIN_PATHS):
        entry = tracked.get(path)
        if entry is None:
            raise SnapshotError(f"UNTRACKED_LIVE_SNAPSHOT_TOOLCHAIN: {path}")
        worktree_path = root / path
        if worktree_path.is_symlink() or not worktree_path.is_file():
            raise SnapshotError(f"live snapshot toolchain path is not a regular file: {path}")
        worktree_bytes = worktree_path.read_bytes()
        head_bytes = _blob(root, revision, path)
        if worktree_bytes != head_bytes:
            raise SnapshotError(f"LIVE_SNAPSHOT_TOOLCHAIN_HEAD_MISMATCH: {path}")
        files.append(
            {
                "path": path,
                "mode": entry[0],
                "size": len(head_bytes),
                "sha256": hashlib.sha256(head_bytes).hexdigest(),
            }
        )
    if Path(__file__).resolve().read_bytes() != _blob(
        root, revision, LIVE_SNAPSHOT_SCRIPT_PATH
    ):
        raise SnapshotError("executing live snapshot script is not the HEAD blob")
    return {
        "schema_id": "t6_live_snapshot_toolchain_binding_v1",
        "head_sha": revision,
        "files": files,
        "status": "BOUND_TO_CLEAN_HEAD",
    }


def _assert_execution_binding_unchanged(
    root: Path, revision: str, expected: Mapping[str, Any]
) -> None:
    observed = _capture_execution_binding(root, revision)
    if observed != expected:
        raise SnapshotError("LIVE_SNAPSHOT_TOOLCHAIN_CHANGED_DURING_EXECUTION")


def _materialize_immutable_manifest_copy(
    directory: Path, manifest_bytes: bytes
) -> Path:
    path = directory / "manifest-direct-upload.json"
    try:
        with path.open("xb") as handle:
            handle.write(manifest_bytes)
            handle.flush()
            os.fsync(handle.fileno())
    except OSError as exc:
        raise SnapshotError(f"cannot materialize immutable manifest copy: {exc}") from exc
    if path.is_symlink() or path.read_bytes() != manifest_bytes:
        raise SnapshotError("immutable Gate-0 manifest copy does not match captured bytes")
    return path


def _replay_gate0_manifest_content(
    root: Path, manifest_path: Path
) -> tuple[dict[str, Any], bytes, dict[str, Any]]:
    """Replay manifest content without treating environment data as provenance."""

    manifest_path = manifest_path.resolve()
    try:
        manifest_bytes = manifest_path.read_bytes()
    except OSError as exc:
        raise SnapshotError(f"cannot read Gate-0 run manifest: {exc}") from exc
    manifest = _load_json_object_bytes(manifest_bytes, source=str(manifest_path))
    head_sha = manifest.get("head_sha")
    if not isinstance(head_sha, str) or not SHA_RE.fullmatch(head_sha):
        raise SnapshotError("Gate-0 manifest head_sha is not a commit SHA")
    if not _commit_exists(root, head_sha):
        raise SnapshotError(f"Gate-0 manifest commit is unavailable: {head_sha}")
    if manifest.get("status") != "PASS":
        raise SnapshotError("Gate-0 run manifest status is not PASS")
    if manifest.get("checkout_state") != "CLEAN":
        raise SnapshotError("Gate-0 run manifest checkout_state is not CLEAN")

    tool_path = root / CI_MANIFEST_TOOL_PATH
    with tempfile.TemporaryDirectory(prefix="t6-gate0-replay-") as directory:
        immutable_manifest = _materialize_immutable_manifest_copy(
            Path(directory), manifest_bytes
        )
        checkout = Path(directory) / "checkout"
        clone = subprocess.run(
            [
                "git",
                "clone",
                "--quiet",
                "--shared",
                "--no-checkout",
                str(root),
                str(checkout),
            ],
            check=False,
            capture_output=True,
        )
        if clone.returncode != 0:
            detail = clone.stderr.decode("utf-8", errors="replace").strip()
            raise SnapshotError(f"cannot create Gate-0 replay checkout: {detail}")
        checked_out = subprocess.run(
            ["git", "checkout", "--quiet", "--detach", head_sha],
            cwd=checkout,
            check=False,
            capture_output=True,
        )
        if checked_out.returncode != 0:
            detail = checked_out.stderr.decode("utf-8", errors="replace").strip()
            raise SnapshotError(f"cannot check out Gate-0 manifest commit: {detail}")
        replay_environment = {
            key: value
            for key, value in os.environ.items()
            if not key.startswith("GITHUB_")
        }
        replay = subprocess.run(
            [
                sys.executable,
                str(tool_path),
                "verify",
                "--root",
                str(checkout),
                "--manifest",
                str(immutable_manifest),
                "--require-pass",
            ],
            check=False,
            capture_output=True,
            env=replay_environment,
        )
        if replay.returncode != 0:
            detail = replay.stderr.decode("utf-8", errors="replace").strip()
            raise SnapshotError(
                "Gate-0 run manifest content replay failed"
                + (f": {detail}" if detail else "")
            )
        if (
            immutable_manifest.is_symlink()
            or immutable_manifest.read_bytes() != manifest_bytes
        ):
            raise SnapshotError("immutable Gate-0 manifest copy changed during replay")

    digest_fields = (
        "kb_claim_set_digest",
        "runtime_source_digest",
        "producer_registry_digest",
        "grammar_hash",
        "test_manifest_digest",
    )
    digests: dict[str, str] = {}
    for field in digest_fields:
        value = manifest.get(field)
        if not isinstance(value, str) or not DIGEST_RE.fullmatch(value):
            raise SnapshotError(f"Gate-0 {field} is not a SHA-256 digest")
        digests[field] = value
    content_basis = {
        "schema_id": "t6_gate0_manifest_content_replay_v1",
        "run_manifest_schema_id": manifest.get("schema_id"),
        "manifest_payload_sha256": manifest.get("manifest_payload_sha256"),
        "manifest_bytes_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "head_sha": head_sha,
        "head_tree_sha": manifest.get("head_tree_sha"),
        "status": "PASS",
        "content_replay": "PASS_EXACT_HEAD_COMMANDS_AND_DIGESTS",
        "producer_registry_status": manifest.get("producer_registry_status"),
        "digest_domain": (
            "Gate-0 manifest domains are replayed independently and are not "
            "assumed equal to live snapshot digest domains."
        ),
        "digests": digests,
    }
    return manifest, manifest_bytes, content_basis


def _environment_cross_check(
    *, locator: Gate0RunLocatorV1, head_sha: str
) -> dict[str, Any]:
    expected = {
        "GITHUB_REPOSITORY": locator.repository,
        "GITHUB_RUN_ID": str(locator.run_id),
        "GITHUB_RUN_ATTEMPT": str(locator.run_attempt),
        "GITHUB_SHA": head_sha,
        "GITHUB_EVENT_NAME": "push",
        "GITHUB_REF": "refs/heads/main",
    }
    present = {key: os.environ[key] for key in expected if key in os.environ}
    if os.environ.get("GITHUB_ACTIONS") == "true":
        missing = sorted(set(expected) - set(present))
        if missing:
            raise SnapshotError(f"GitHub environment cross-check is missing {missing}")
    mismatches = {
        key: {"observed": present[key], "expected": expected[key]}
        for key in present
        if present[key] != expected[key]
    }
    if mismatches:
        raise SnapshotError(f"GitHub environment cross-check failed: {mismatches}")
    if not present:
        status = "NOT_PRESENT"
    elif set(present) == set(expected):
        status = "FULL_MATCH"
    else:
        status = "PARTIAL_MATCH"
    return {"status": status, "checked_fields": sorted(present)}


def _verify_github_run_provenance(
    *,
    locator: Gate0RunLocatorV1,
    manifest: Mapping[str, Any],
    manifest_bytes: bytes,
    api_client: GitHubApiClientV1,
    now: datetime | None = None,
) -> dict[str, Any]:
    """Verify official workflow, run, job and direct-upload artifact metadata."""

    workflow = api_client.get_workflow(locator.repository, locator.workflow_id)
    if workflow.get("id") != TRUSTED_WORKFLOW_ID:
        raise SnapshotError("GitHub workflow id is not trusted")
    if workflow.get("path") != TRUSTED_WORKFLOW_PATH:
        raise SnapshotError("GitHub workflow path is not trusted")
    if workflow.get("name") != TRUSTED_WORKFLOW_NAME:
        raise SnapshotError("GitHub workflow name is not trusted")
    if workflow.get("state") != "active":
        raise SnapshotError("GitHub workflow is not active")

    run = api_client.get_run_attempt(
        locator.repository, locator.run_id, locator.run_attempt
    )
    head_sha = manifest.get("head_sha")
    if run.get("id") != locator.run_id:
        raise SnapshotError("GitHub run id does not match the locator")
    if (
        type(run.get("run_attempt")) is not int
        or run.get("run_attempt") != locator.run_attempt
    ):
        raise SnapshotError("GitHub run attempt does not match the locator")
    if run.get("head_sha") != head_sha:
        raise SnapshotError("GitHub run head SHA does not match the manifest")
    if run.get("event") != "push" or run.get("head_branch") != "main":
        raise SnapshotError("GitHub run is not an exact main push run")
    if run.get("workflow_id") != TRUSTED_WORKFLOW_ID:
        raise SnapshotError("GitHub run workflow id is not trusted")
    run_path = run.get("path")
    if not isinstance(run_path, str) or run_path.rsplit("@", 1)[0] != TRUSTED_WORKFLOW_PATH:
        raise SnapshotError("GitHub run workflow path is not trusted")
    repository = run.get("repository")
    if not isinstance(repository, dict):
        raise SnapshotError("GitHub run repository metadata is missing")
    if (
        repository.get("id") != TRUSTED_REPOSITORY_ID
        or repository.get("full_name") != TRUSTED_REPOSITORY
    ):
        raise SnapshotError("GitHub run repository is not trusted")
    head_repository = run.get("head_repository")
    if not isinstance(head_repository, dict) or (
        head_repository.get("id") != TRUSTED_REPOSITORY_ID
        or head_repository.get("full_name") != TRUSTED_REPOSITORY
    ):
        raise SnapshotError("GitHub run head repository metadata is missing")

    jobs = api_client.list_run_attempt_jobs(
        locator.repository, locator.run_id, locator.run_attempt
    )
    named_jobs = [job for job in jobs if job.get("name") == TRUSTED_GATE0_JOB_NAME]
    if len(named_jobs) != 1 or named_jobs[0].get("id") != locator.job_id:
        raise SnapshotError("GitHub Gate-0 job identity is missing, stale, or duplicated")
    job = named_jobs[0]
    if job.get("run_id") != locator.run_id:
        raise SnapshotError("GitHub Gate-0 job run id is stale")
    if (
        type(job.get("run_attempt")) is not int
        or job.get("run_attempt") != locator.run_attempt
    ):
        raise SnapshotError("GitHub Gate-0 job attempt is stale")
    if job.get("head_sha") != head_sha:
        raise SnapshotError("GitHub Gate-0 job head SHA is stale")
    if job.get("status") != "completed":
        raise SnapshotError("GitHub Gate-0 job is not completed")
    run_status = run.get("status")
    run_conclusion = run.get("conclusion")
    if job.get("conclusion") != "success":
        raise SnapshotError("GitHub Gate-0 job did not conclude successfully")
    if run_status == "completed":
        if run_conclusion != "success":
            raise SnapshotError("completed GitHub run did not conclude successfully")
        success_basis = "BOTH"
    elif run_status == "in_progress" and run_conclusion is None:
        success_basis = "JOB_SUCCESS"
    else:
        raise SnapshotError("GitHub run status is not eligible for Gate-0 provenance")

    artifact = api_client.get_artifact(locator.repository, locator.artifact_id)
    local_bytes_sha256 = hashlib.sha256(manifest_bytes).hexdigest()
    expected_server_digest = "sha256:" + local_bytes_sha256
    if artifact.get("id") != locator.artifact_id:
        raise SnapshotError("GitHub artifact id does not match the locator")
    if artifact.get("name") != TRUSTED_ARTIFACT_NAME:
        raise SnapshotError("GitHub artifact name is not the direct manifest name")
    if artifact.get("expired") is not False:
        raise SnapshotError("GitHub artifact is expired or has unknown expiry")
    expires_at = artifact.get("expires_at")
    try:
        expires = datetime.fromisoformat(str(expires_at).replace("Z", "+00:00"))
        if expires.tzinfo is None:
            raise ValueError("no timezone")
    except ValueError as exc:
        raise SnapshotError("GitHub artifact expires_at is invalid") from exc
    current_time = now or datetime.now(timezone.utc)
    if current_time.tzinfo is None:
        raise SnapshotError("provenance verification time must be timezone-aware")
    if expires <= current_time:
        raise SnapshotError("GitHub artifact has passed expires_at")
    if artifact.get("size_in_bytes") != len(manifest_bytes):
        raise SnapshotError("GitHub direct-upload artifact size does not match manifest bytes")
    if artifact.get("digest") != expected_server_digest:
        raise SnapshotError("GitHub artifact server digest does not match manifest bytes")
    artifact_run = artifact.get("workflow_run")
    if not isinstance(artifact_run, dict):
        raise SnapshotError("GitHub artifact workflow_run metadata is missing")
    expected_artifact_run = {
        "id": locator.run_id,
        "repository_id": TRUSTED_REPOSITORY_ID,
        "head_repository_id": head_repository["id"],
        "head_sha": head_sha,
    }
    for field, expected_value in expected_artifact_run.items():
        if artifact_run.get(field) != expected_value:
            raise SnapshotError(f"GitHub artifact workflow_run {field} is stale")

    environment = _environment_cross_check(locator=locator, head_sha=str(head_sha))
    return {
        "schema_id": "t6_gate0_run_provenance_v1",
        "schema_version": 1,
        "source": "GITHUB_REST_API",
        "repository": TRUSTED_REPOSITORY,
        "repository_id": TRUSTED_REPOSITORY_ID,
        "workflow_id": TRUSTED_WORKFLOW_ID,
        "workflow_name": TRUSTED_WORKFLOW_NAME,
        "workflow_path": TRUSTED_WORKFLOW_PATH,
        "workflow_state": "active",
        "run_id": locator.run_id,
        "run_attempt": locator.run_attempt,
        "run_head_sha": head_sha,
        "run_event": "push",
        "run_head_branch": "main",
        "head_repository_id": TRUSTED_REPOSITORY_ID,
        "run_status": run_status,
        "run_conclusion": run_conclusion,
        "success_basis": success_basis,
        "job_id": locator.job_id,
        "job_name": TRUSTED_GATE0_JOB_NAME,
        "job_status": job.get("status"),
        "job_conclusion": job.get("conclusion"),
        "artifact_id": locator.artifact_id,
        "artifact_name": TRUSTED_ARTIFACT_NAME,
        "artifact_expired": False,
        "artifact_expires_at": expires_at,
        "artifact_size_in_bytes": len(manifest_bytes),
        "artifact_digest": expected_server_digest,
        "artifact_workflow_run_id": locator.run_id,
        "artifact_workflow_run_head_sha": head_sha,
        "environment_cross_check": environment,
    }


def _verified_gate0_attestation(
    root: Path,
    manifest_path: Path,
    *,
    locator: Gate0RunLocatorV1,
    api_client: GitHubApiClientV1,
    now: datetime | None = None,
) -> VerifiedGate0Attestation:
    manifest, manifest_bytes, content_basis = _replay_gate0_manifest_content(
        root, manifest_path
    )
    if manifest.get("workflow_repository") != locator.repository:
        raise SnapshotError("Gate-0 manifest repository does not match provenance")
    if manifest.get("workflow_run_id") != str(locator.run_id):
        raise SnapshotError("Gate-0 manifest run id does not match provenance")
    if manifest.get("workflow_run_attempt") != str(locator.run_attempt):
        raise SnapshotError("Gate-0 manifest run attempt does not match provenance")
    if manifest.get("workflow_sha") != manifest.get("head_sha"):
        raise SnapshotError("Gate-0 manifest workflow SHA does not match its HEAD")
    if manifest.get("workflow_event") != "push":
        raise SnapshotError("Gate-0 manifest did not originate from a push run")
    if manifest.get("workflow_ref") != "refs/heads/main":
        raise SnapshotError("Gate-0 manifest did not originate from main")
    if manifest.get("workflow_job") != TRUSTED_GATE0_JOB_NAME:
        raise SnapshotError("Gate-0 manifest workflow job is not gate-zero")
    provenance = _verify_github_run_provenance(
        locator=locator,
        manifest=manifest,
        manifest_bytes=manifest_bytes,
        api_client=api_client,
        now=now,
    )
    basis = {
        "schema_id": "t6_gate0_verified_basis_v2",
        "content_replay": content_basis,
        "github_provenance": provenance,
    }
    return VerifiedGate0Attestation(head_sha=str(manifest["head_sha"]), basis=basis)


def _local_module_aliases(path: str) -> tuple[str, ...]:
    pure = PurePosixPath(path)
    if pure.suffix != ".py" or len(pure.parts) < 2 or pure.parts[0] not in {
        "scripts",
        "reproductions",
    }:
        return ()
    relative = PurePosixPath(*pure.parts[1:])
    module_parts = (
        relative.parent.parts
        if relative.name == "__init__.py"
        else relative.with_suffix("").parts
    )
    if not module_parts:
        return (pure.parts[0],)
    return tuple(
        sorted(
            {
                ".".join(module_parts),
                ".".join((pure.parts[0], *module_parts)),
            }
        )
    )


def _current_package_parts(path: str) -> tuple[str, ...]:
    pure = PurePosixPath(path)
    if not pure.parts or pure.parts[0] not in {"scripts", "reproductions"}:
        raise SnapshotError(f"local import source is outside namespaces: {path}")
    relative = PurePosixPath(*pure.parts[1:])
    if relative.name == "__init__.py":
        return relative.parent.parts
    return relative.with_suffix("").parent.parts


def _import_targets(tree: ast.AST, *, source_path: str) -> tuple[str, ...]:
    targets: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            targets.update(alias.name for alias in node.names)
            continue
        if isinstance(node, ast.ImportFrom):
            if node.level:
                package_parts = _current_package_parts(source_path)
                parent_count = node.level - 1
                if parent_count > len(package_parts):
                    raise SnapshotError(
                        f"relative import escapes local namespace in {source_path}"
                    )
                remaining = package_parts[: len(package_parts) - parent_count]
                module_parts = tuple((node.module or "").split("."))
                if module_parts == ("",):
                    module_parts = ()
                base_parts = (*remaining, *module_parts)
                if not base_parts:
                    raise SnapshotError(
                        f"relative import is not resolvable in {source_path}"
                    )
            else:
                base_parts = tuple((node.module or "").split("."))
                if base_parts == ("",):
                    base_parts = ()
            if base_parts:
                targets.add(".".join(base_parts))
            for alias in node.names:
                if alias.name != "*" and base_parts:
                    targets.add(".".join((*base_parts, alias.name)))
            continue
        if not isinstance(node, ast.Call) or not node.args:
            continue
        is_dynamic = (
            isinstance(node.func, ast.Name) and node.func.id == "__import__"
        ) or (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "importlib"
            and node.func.attr == "import_module"
        )
        if not is_dynamic:
            continue
        module = node.args[0]
        if not isinstance(module, ast.Constant) or not isinstance(module.value, str):
            raise SnapshotError(
                f"nonliteral dynamic import prevents closed digest: {source_path}"
            )
        if module.value.startswith("."):
            raise SnapshotError(
                f"relative dynamic import is unsupported: {source_path}"
            )
        targets.add(module.value)
    return tuple(sorted(targets))


@lru_cache(maxsize=8)
def _runtime_source_paths(root: Path, revision: str) -> tuple[str, ...]:
    """Independently derive the tracked local-import closure for T6 scripts."""

    tracked = _tracked_paths(root, revision)
    roots = tuple(
        path
        for path in tracked
        if path.startswith("scripts/t6_") and path.endswith(".py")
    )
    if not roots:
        raise SnapshotError("runtime source root set is empty")
    module_index: dict[str, set[str]] = {}
    for path in tracked:
        for alias in _local_module_aliases(path):
            module_index.setdefault(alias, set()).add(path)
    pending = list(reversed(roots))
    closure: set[str] = set()
    while pending:
        path = pending.pop()
        if path in closure:
            continue
        closure.add(path)
        try:
            source = _blob(root, revision, path).decode("utf-8")
            tree = ast.parse(source, filename=path)
        except (SyntaxError, UnicodeDecodeError) as exc:
            raise SnapshotError(f"cannot parse runtime source {path}: {exc}") from exc
        dependencies: set[str] = set()
        for module_name in _import_targets(tree, source_path=path):
            parts = tuple(part for part in module_name.split(".") if part)
            for length in range(1, len(parts) + 1):
                alias = ".".join(parts[:length])
                candidates = sorted(module_index.get(alias, set()))
                if len(candidates) > 1:
                    raise SnapshotError(
                        f"ambiguous local module {alias!r} imported by {path}: "
                        f"{candidates}"
                    )
                dependencies.update(candidates)
        pending.extend(
            dependency
            for dependency in reversed(sorted(dependencies))
            if dependency not in closure
        )
    return tuple(sorted(closure))


def file_set_records(
    root: Path, revision: str, paths: Iterable[str]
) -> tuple[dict[str, Any], ...]:
    unique = sorted(set(paths))
    if not unique:
        raise SnapshotError("digest file set is empty")
    entries = _tracked_entries(root, revision)
    blobs = _blobs(root, revision, unique)
    records: list[dict[str, Any]] = []
    for path in unique:
        content = blobs[path]
        records.append(
            {
                "path": path,
                "mode": entries[path][0],
                "size": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
            }
        )
    return tuple(records)


def file_set_digest(
    root: Path, revision: str, paths: Iterable[str]
) -> tuple[str, int]:
    records = file_set_records(root, revision, paths)
    payload = {"schema_id": FILE_SET_SCHEMA_ID, "files": list(records)}
    return hashlib.sha256(canonical_json_bytes(payload)).hexdigest(), len(records)


def _claim_paths(tracked: Sequence[str]) -> tuple[str, ...]:
    claims = tuple(
        path
        for path in tracked
        if path.startswith("claims/") and path.endswith(".md")
    )
    return tuple(sorted({*claims, PROOF_FRONTIER_PATH, RESIDUAL_FRONTIER_PATH}))


def _test_paths(tracked: Sequence[str]) -> tuple[str, ...]:
    return tuple(
        path
        for path in tracked
        if path.startswith("tests/")
        and path.endswith(".py")
    )


def _source_sets(root: Path, revision: str) -> dict[str, tuple[str, ...]]:
    tracked = _tracked_paths(root, revision)
    tracked_set = set(tracked)
    runtime_sources = _runtime_source_paths(root, revision)
    result = {
        "claim_set": tuple(
            sorted(
                {
                    *_claim_paths(tracked),
                    LEDGER_PATH,
                    F1_RECEIPT_PATH,
                    README_PATH,
                }
            )
        ),
        "runtime_source": tuple(
            sorted({*runtime_sources, RUNTIME_FREEZE_PATH})
        ),
        "producer_registry": tuple(
            sorted({*runtime_sources, *PRODUCER_REGISTRY_FIXED_PATHS})
        ),
        "terminal_schedule": tuple(
            sorted({*runtime_sources, *TERMINAL_SCHEDULE_FIXED_PATHS})
        ),
        "t5_taxonomy": tuple(sorted(T5_PATHS)),
        "test_manifest": _test_paths(tracked),
        "independent_review": tuple(sorted(INDEPENDENT_REVIEW_PATHS)),
    }
    for name, paths in result.items():
        missing = sorted(set(paths) - tracked_set)
        if missing:
            raise SnapshotError(f"{name} references paths absent at {revision}: {missing}")
    return result


def _expect_mapping(value: object, name: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise SnapshotError(f"{name} must be an object")
    return value


def _sha_provenance(
    root: Path,
    workpack: Mapping[str, Any],
    runtime_freeze: Mapping[str, Any],
    grammar: Mapping[str, Any],
    residual_frontier: Mapping[str, Any],
) -> tuple[str, str]:
    integration = _expect_mapping(workpack.get("integration"), "workpack.integration")
    origin = integration.get("base_sha")
    audited = integration.get("audited_sha")
    if not isinstance(origin, str) or not SHA_RE.fullmatch(origin):
        raise SnapshotError("workpack.integration.base_sha is not a commit SHA")
    if not isinstance(audited, str) or not SHA_RE.fullmatch(audited):
        raise SnapshotError("workpack.integration.audited_sha is not a commit SHA")
    audited_values = {
        audited,
        runtime_freeze.get("integration_audited_sha"),
        grammar.get("integration_audited_sha"),
        residual_frontier.get("baseline_sha"),
    }
    if audited_values != {audited}:
        raise SnapshotError(
            "integration audited SHA disagrees across workpack/runtime/grammar/frontier: "
            f"{sorted(str(value) for value in audited_values)}"
        )
    if not _commit_exists(root, origin):
        raise SnapshotError(f"workpack origin commit is unavailable: {origin}")
    if not _commit_exists(root, audited):
        raise SnapshotError(f"integration audited commit is unavailable: {audited}")
    if not _is_ancestor(root, origin, audited):
        raise SnapshotError(
            "workpack origin is not an ancestor of the integration audited SHA"
        )
    return origin, audited


def _status_from_manifests(
    workpack: Mapping[str, Any],
    runtime_freeze: Mapping[str, Any],
    residual_frontier: Mapping[str, Any],
    ledger: Mapping[str, Any],
    f1_receipt: Mapping[str, Any],
    inventory: Mapping[str, Any],
    readme: str,
) -> dict[str, str]:
    residual_status = _expect_mapping(
        residual_frontier.get("status"), "residual_frontier.status"
    )
    workpack_status = _expect_mapping(
        workpack.get("status_boundary"), "workpack.status_boundary"
    )
    runtime_status = _expect_mapping(
        runtime_freeze.get("theorem_status_boundary"),
        "runtime_freeze.theorem_status_boundary",
    )
    result: dict[str, str] = {}
    for key in STATUS_KEYS:
        values = {
            residual_status.get(key),
            workpack_status.get(key),
            runtime_status.get(key),
        }
        if len(values) != 1 or not all(isinstance(value, str) for value in values):
            raise SnapshotError(
                f"status {key} disagrees across workpack/runtime/residual frontier: "
                f"{sorted(str(value) for value in values)}"
            )
        result[key] = str(next(iter(values)))
    ledger_status = _expect_mapping(ledger.get("current_status"), "ledger.current_status")
    if ledger_status.get("t6_global_selector_totality") != result["T6"]:
        raise SnapshotError("selector obligation ledger disagrees with T6 status")
    if f1_receipt.get("status") != result["F1"]:
        raise SnapshotError("F1 reachability receipt disagrees with F1 status")
    unknown_items = inventory.get("unknown_items")
    if not isinstance(unknown_items, list):
        raise SnapshotError("constructor inventory unknown_items must be a list")
    open_unknowns = [
        item
        for item in unknown_items
        if isinstance(item, dict) and item.get("status") == "OPEN"
    ]
    closure = _expect_mapping(
        inventory.get("closure_assessment"), "inventory.closure_assessment"
    )
    if closure.get("unknown_item_count") != len(open_unknowns):
        raise SnapshotError(
            "constructor inventory open unknown count disagrees with closure assessment"
        )
    if open_unknowns and result["F1"] == "CLOSED":
        raise SnapshotError("constructor inventory has unknowns but F1 is CLOSED")
    for key in STATUS_KEYS:
        coarse_status = "OPEN" if result[key].startswith("OPEN") else result[key]
        markers = re.findall(rf"`{re.escape(key)}=([A-Z0-9_]+)`", readme)
        if markers != [coarse_status]:
            raise SnapshotError(
                f"README must contain exactly one `{key}=...` marker matching "
                f"{coarse_status}; found {markers}"
            )
    return result


def _grammar_hash(grammar_manifest: Mapping[str, Any]) -> str:
    grammar = grammar_manifest.get("grammar")
    if not isinstance(grammar, dict):
        raise SnapshotError("family grammar manifest has no grammar object")
    digest = hashlib.sha256(canonical_json_line_bytes(grammar)).hexdigest()
    if grammar_manifest.get("grammar_hash") != digest:
        raise SnapshotError("family grammar manifest's embedded grammar_hash is stale")
    return digest


def _manifest_digests(root: Path, revision: str) -> dict[str, str]:
    return {
        name: hashlib.sha256(_blob(root, revision, path)).hexdigest()
        for name, path in MANIFEST_PATHS.items()
    }


def evaluate_consumer_policy_v1(root: Path, revision: str) -> dict[str, Any]:
    """Check exact, coordinator-owned snapshot locator bindings without editing them."""

    consumers: dict[str, dict[str, Any]] = {}
    readme = _blob(root, revision, README_PATH).decode("utf-8", errors="strict")
    readme_count = readme.count(LIVE_SNAPSHOT_LOCATOR)
    consumers["readme"] = {
        "path": README_PATH,
        "binding": "EXACT_STRING_ONCE",
        "observed": readme_count,
        "status": "BOUND" if readme_count == 1 else "MISSING_OR_STALE",
    }
    for consumer_id, path in CONSUMER_PATHS.items():
        if consumer_id == "readme":
            continue
        document = _json_blob(root, revision, path)
        observed = document.get("live_audit_snapshot_locator")
        consumers[consumer_id] = {
            "path": path,
            "binding": "TOP_LEVEL_EXACT_FIELD",
            "observed": observed,
            "status": (
                "BOUND" if observed == LIVE_SNAPSHOT_LOCATOR else "MISSING_OR_STALE"
            ),
        }
    all_bound = all(item["status"] == "BOUND" for item in consumers.values())
    return {
        "schema_id": "t6_live_snapshot_consumer_policy_v1",
        "required_locator": LIVE_SNAPSHOT_LOCATOR,
        "consumers": consumers,
        "all_consumers_bound": all_bound,
        "status": "PASS" if all_bound else "MISSING_OR_STALE",
    }


def _evaluate_current_digest_audit(
    *,
    repository: str,
    head_sha: str,
    digest_vector: Mapping[str, str],
    audit_client: CurrentDigestAuditClientV1 | None,
) -> dict[str, Any]:
    vector = dict(sorted(digest_vector.items()))
    vector_digest = hashlib.sha256(canonical_json_bytes(vector)).hexdigest()
    if audit_client is None:
        return {
            "schema_id": "t6_current_digest_audit_gate_v1",
            "status": "MISSING",
            "digest_vector_sha256": vector_digest,
            "basis": None,
        }
    basis = audit_client.verify_current_digest_vector(
        repository=repository,
        head_sha=head_sha,
        digest_vector=vector,
    )
    expected_keys = {
        "schema_id",
        "schema_version",
        "decision",
        "audited_head_sha",
        "digest_vector",
        "digest_vector_sha256",
        "independent_reviewer_id",
        "evidence_locator",
        "review_method",
    }
    if not isinstance(basis, dict) or set(basis) != expected_keys:
        raise SnapshotError("current digest audit basis has unknown or missing fields")
    if basis.get("schema_id") != "t6_current_digest_audit_basis_v1":
        raise SnapshotError("current digest audit basis schema_id is invalid")
    if (
        type(basis.get("schema_version")) is not int
        or basis.get("schema_version") != 1
        or basis.get("decision") != "PASS"
    ):
        raise SnapshotError("current digest audit did not record PASS")
    if basis.get("audited_head_sha") != head_sha:
        raise SnapshotError("current digest audit head SHA is stale")
    if basis.get("digest_vector") != vector:
        raise SnapshotError("current digest audit vector is stale")
    if basis.get("digest_vector_sha256") != vector_digest:
        raise SnapshotError("current digest audit vector digest is stale")
    for field in ("independent_reviewer_id", "evidence_locator", "review_method"):
        if not isinstance(basis.get(field), str) or not basis[field]:
            raise SnapshotError(f"current digest audit {field} is missing")
    return {
        "schema_id": "t6_current_digest_audit_gate_v1",
        "status": "PASS",
        "digest_vector_sha256": vector_digest,
        "basis": dict(basis),
    }


def _build_expected(
    root: Path,
    *,
    revision: str,
    attestation: VerifiedGate0Attestation | None,
    execution_binding: Mapping[str, Any],
    digest_audit_client: CurrentDigestAuditClientV1 | None,
    observed_at: str,
) -> dict[str, Any]:
    last_verified_head_sha = None if attestation is None else attestation.head_sha

    workpack = _json_blob(root, revision, WORKPACK_PATH)
    proof_frontier = _json_blob(root, revision, PROOF_FRONTIER_PATH)
    inventory = _json_blob(root, revision, INVENTORY_PATH)
    runtime_freeze = _json_blob(root, revision, RUNTIME_FREEZE_PATH)
    grammar = _json_blob(root, revision, GRAMMAR_PATH)
    residual_frontier = _json_blob(root, revision, RESIDUAL_FRONTIER_PATH)
    ledger = _json_blob(root, revision, LEDGER_PATH)
    f1_receipt = _json_blob(root, revision, F1_RECEIPT_PATH)
    try:
        readme = _blob(root, revision, README_PATH).decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SnapshotError(f"README is not UTF-8 at {revision}") from exc

    origin, integration_audited = _sha_provenance(
        root, workpack, runtime_freeze, grammar, residual_frontier
    )
    status = _status_from_manifests(
        workpack,
        runtime_freeze,
        residual_frontier,
        ledger,
        f1_receipt,
        inventory,
        readme,
    )
    if proof_frontier.get("current_status") != status["T6"]:
        raise SnapshotError("proof frontier current_status disagrees with T6 status")

    relation = head_relation(root, last_verified_head_sha, revision)
    integration_relation = integration_head_relation(
        root, integration_audited, revision
    )
    source_sets = _source_sets(root, revision)
    digests: dict[str, str] = {}
    digest_inputs: dict[str, dict[str, Any]] = {}
    for name, paths in source_sets.items():
        digest, count = file_set_digest(root, revision, paths)
        digests[name] = digest
        digest_inputs[name] = {
            "file_count": count,
            "paths": list(paths),
            "scope": DIGEST_SCOPES[name],
        }

    grammar_hash = _grammar_hash(grammar)
    digest_vector = {
        "claim_set_digest": digests["claim_set"],
        "runtime_source_digest": digests["runtime_source"],
        "producer_registry_digest": digests["producer_registry"],
        "terminal_schedule_digest": digests["terminal_schedule"],
        "grammar_hash": grammar_hash,
        "t5_taxonomy_digest": digests["t5_taxonomy"],
        "test_manifest_digest": digests["test_manifest"],
        "independent_review_digest": digests["independent_review"],
    }
    repository_name = workpack.get("repository")
    if repository_name != TRUSTED_REPOSITORY:
        raise SnapshotError("workpack repository is not the trusted repository")
    current_digest_audit = _evaluate_current_digest_audit(
        repository=repository_name,
        head_sha=revision,
        digest_vector=digest_vector,
        audit_client=digest_audit_client,
    )
    consumer_policy = evaluate_consumer_policy_v1(root, revision)
    status_upgrade_allowed = bool(
        relation == "EQUAL"
        and integration_relation != "DIVERGED"
        and current_digest_audit["status"] == "PASS"
        and consumer_policy["status"] == "PASS"
    )

    return {
        "schema_id": SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "artifact_policy": "EPHEMERAL_HEAD_BOUND_NOT_TRACKED",
        "observed_at": observed_at,
        "repository": repository_name,
        "integration_branch": residual_frontier.get("integration_branch"),
        "workpack_origin_sha": origin,
        "integration_audited_sha": integration_audited,
        "integration_head_relation": integration_relation,
        "current_observed_head_sha": revision,
        "last_verified_head_sha": last_verified_head_sha,
        "last_verified_basis": None if attestation is None else dict(attestation.basis),
        "head_relation": relation,
        "verification_state": _verification_state(relation),
        "status_upgrade_allowed": status_upgrade_allowed,
        "execution_binding": dict(execution_binding),
        "current_digest_audit": current_digest_audit,
        "consumer_policy": consumer_policy,
        "digest_algorithm": (
            "sha256(canonical-json({schema_id:t6_ci_file_set_v1,"
            "files:sorted([{path,mode,size,sha256(raw_git_blob)}])}))"
        ),
        **digest_vector,
        "digest_inputs": digest_inputs,
        "manifest_digests": _manifest_digests(root, revision),
        "manifest_statuses": {
            "proof_frontier": proof_frontier.get("current_status"),
            "constructor_inventory": inventory.get("status"),
            "runtime_protocol_freeze": runtime_freeze.get("status"),
            "family_grammar_freeze": grammar.get("status"),
            "residual_frontier": status,
        },
        "status": status,
        "proof_boundary": (
            "A digest is evidence of exact bytes at current_observed_head_sha, "
            "not proof of registry completeness, terminal-schedule completeness, "
            "F1/F2/F3 closure, T6 closure, or the Erdos-Straus conjecture. "
            "Status upgrades additionally require an independent current-digest "
            "audit and exact README/ledger/frontier locator bindings; those remain "
            "coordinator-owned integration steps."
        ),
    }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )


def _validate_timestamp(value: object) -> str:
    if not isinstance(value, str):
        raise SnapshotError("observed_at must be an RFC 3339 string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("timestamp is not timezone-aware")
    except ValueError as exc:
        raise SnapshotError(
            "observed_at must be a timezone-aware RFC 3339 string"
        ) from exc
    return value


def build_snapshot(
    root: Path,
    *,
    run_manifest_path: Path | None = None,
    provenance_locator: Gate0RunLocatorV1 | None = None,
    github_api_client: GitHubApiClientV1 | None = None,
    digest_audit_client: CurrentDigestAuditClientV1 | None = None,
    provenance_now: datetime | None = None,
    last_verified_head_sha: str | None = None,
    observed_at: str | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    revision = resolve_head(root)
    execution_binding = _capture_execution_binding(root, revision)
    if last_verified_head_sha is not None:
        raise SnapshotError(
            "UNATTESTED_LAST_VERIFIED_HEAD: use run_manifest_path; a bare SHA "
            "cannot authorize status upgrades"
        )
    if (run_manifest_path is None) != (provenance_locator is None):
        raise SnapshotError(
            "Gate-0 run manifest and provenance locator must be supplied together"
        )
    attestation: VerifiedGate0Attestation | None = None
    if run_manifest_path is not None and provenance_locator is not None:
        client = github_api_client or GitHubRestApiClientV1(
            token=os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        )
        attestation = _verified_gate0_attestation(
            root,
            run_manifest_path,
            locator=provenance_locator,
            api_client=client,
            now=provenance_now,
        )
    snapshot = _build_expected(
        root,
        revision=revision,
        attestation=attestation,
        execution_binding=execution_binding,
        digest_audit_client=digest_audit_client,
        observed_at=_validate_timestamp(observed_at or _utc_now()),
    )
    _assert_execution_binding_unchanged(root, revision, execution_binding)
    return snapshot


def _validate_shape(snapshot: Mapping[str, Any], errors: list[str]) -> None:
    if set(snapshot) != EXPECTED_TOP_LEVEL_KEYS:
        missing = sorted(EXPECTED_TOP_LEVEL_KEYS - set(snapshot))
        extra = sorted(set(snapshot) - EXPECTED_TOP_LEVEL_KEYS)
        errors.append(f"top-level keys differ: missing={missing}, extra={extra}")
    if snapshot.get("schema_id") != SCHEMA_ID:
        errors.append(f"schema_id must be {SCHEMA_ID!r}")
    if snapshot.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    if snapshot.get("artifact_policy") != "EPHEMERAL_HEAD_BOUND_NOT_TRACKED":
        errors.append("artifact_policy must preserve the ephemeral HEAD boundary")

    for field in (
        "workpack_origin_sha",
        "integration_audited_sha",
        "current_observed_head_sha",
    ):
        value = snapshot.get(field)
        if not isinstance(value, str) or not SHA_RE.fullmatch(value):
            errors.append(f"{field} must be a lowercase 40-hex SHA")
    last_verified = snapshot.get("last_verified_head_sha")
    if last_verified is not None and (
        not isinstance(last_verified, str) or not SHA_RE.fullmatch(last_verified)
    ):
        errors.append("last_verified_head_sha must be null or a lowercase 40-hex SHA")
    basis = snapshot.get("last_verified_basis")
    if last_verified is None and basis is not None:
        errors.append("last_verified_basis must be null when no verified HEAD exists")
    if last_verified is not None:
        if not isinstance(basis, dict) or set(basis) != ATTESTATION_BASIS_KEYS:
            errors.append("last_verified_basis is not a complete Gate-0 attestation")
        else:
            if basis.get("schema_id") != "t6_gate0_verified_basis_v2":
                errors.append("last_verified_basis.schema_id is invalid")
            content = basis.get("content_replay")
            provenance = basis.get("github_provenance")
            if not isinstance(content, dict) or set(content) != CONTENT_REPLAY_KEYS:
                errors.append("last_verified content replay is incomplete")
            else:
                if content.get("schema_id") != "t6_gate0_manifest_content_replay_v1":
                    errors.append("last_verified content replay schema is invalid")
                if content.get("run_manifest_schema_id") != "t6_ci_run_manifest_v1":
                    errors.append("last_verified run manifest schema is invalid")
                if content.get("head_sha") != last_verified:
                    errors.append("last_verified content head SHA does not match")
                if content.get("status") != "PASS":
                    errors.append("last_verified content status is not PASS")
                for field in ("manifest_payload_sha256", "manifest_bytes_sha256"):
                    value = content.get(field)
                    if not isinstance(value, str) or not DIGEST_RE.fullmatch(value):
                        errors.append(f"last_verified content {field} is invalid")
                digests = content.get("digests")
                if not isinstance(digests, dict) or set(digests) != ATTESTATION_DIGEST_KEYS:
                    errors.append("last_verified content digest set is invalid")
                elif not all(
                    isinstance(value, str) and DIGEST_RE.fullmatch(value)
                    for value in digests.values()
                ):
                    errors.append("last_verified content contains invalid digests")
            if not isinstance(provenance, dict) or set(
                provenance
            ) != GITHUB_PROVENANCE_KEYS:
                errors.append("last_verified GitHub provenance is incomplete")
            else:
                if provenance.get("schema_id") != "t6_gate0_run_provenance_v1":
                    errors.append("last_verified GitHub provenance schema is invalid")
                if provenance.get("run_head_sha") != last_verified:
                    errors.append("last_verified GitHub run head SHA does not match")
                if provenance.get("artifact_workflow_run_head_sha") != last_verified:
                    errors.append("last_verified artifact head SHA does not match")
                if isinstance(content, dict) and provenance.get("artifact_digest") != (
                    "sha256:" + str(content.get("manifest_bytes_sha256"))
                ):
                    errors.append("last_verified artifact digest does not bind content")

    for field in (
        "claim_set_digest",
        "runtime_source_digest",
        "producer_registry_digest",
        "terminal_schedule_digest",
        "grammar_hash",
        "t5_taxonomy_digest",
        "test_manifest_digest",
        "independent_review_digest",
    ):
        value = snapshot.get(field)
        if not isinstance(value, str) or not DIGEST_RE.fullmatch(value):
            errors.append(f"{field} must be a lowercase SHA-256 digest")

    if snapshot.get("head_relation") not in HEAD_RELATIONS:
        errors.append("head_relation has an unknown value")
    if snapshot.get("verification_state") not in VERIFICATION_STATES:
        errors.append("verification_state has an unknown value")
    if snapshot.get("integration_head_relation") not in INTEGRATION_HEAD_RELATIONS:
        errors.append("integration_head_relation has an unknown value")
    if not isinstance(snapshot.get("status_upgrade_allowed"), bool):
        errors.append("status_upgrade_allowed must be boolean")

    execution_binding = snapshot.get("execution_binding")
    if not isinstance(execution_binding, dict) or set(execution_binding) != {
        "schema_id",
        "head_sha",
        "files",
        "status",
    }:
        errors.append("execution_binding has unknown or missing fields")
    elif (
        execution_binding.get("schema_id")
        != "t6_live_snapshot_toolchain_binding_v1"
        or execution_binding.get("head_sha")
        != snapshot.get("current_observed_head_sha")
        or execution_binding.get("status") != "BOUND_TO_CLEAN_HEAD"
    ):
        errors.append("execution_binding is not bound to the observed HEAD")

    current_digest_audit = snapshot.get("current_digest_audit")
    if not isinstance(current_digest_audit, dict) or set(current_digest_audit) != {
        "schema_id",
        "status",
        "digest_vector_sha256",
        "basis",
    }:
        errors.append("current_digest_audit has unknown or missing fields")
    elif current_digest_audit.get("status") not in {"MISSING", "PASS"}:
        errors.append("current_digest_audit status is invalid")
    elif (
        current_digest_audit.get("status") == "MISSING"
        and current_digest_audit.get("basis") is not None
    ):
        errors.append("missing current digest audit cannot carry a basis")
    elif (
        current_digest_audit.get("status") == "PASS"
        and not isinstance(current_digest_audit.get("basis"), dict)
    ):
        errors.append("passing current digest audit requires a basis")

    consumer_policy = snapshot.get("consumer_policy")
    if not isinstance(consumer_policy, dict) or set(consumer_policy) != {
        "schema_id",
        "required_locator",
        "consumers",
        "all_consumers_bound",
        "status",
    }:
        errors.append("consumer_policy has unknown or missing fields")
    elif (
        consumer_policy.get("required_locator") != LIVE_SNAPSHOT_LOCATOR
        or consumer_policy.get("status") not in {"PASS", "MISSING_OR_STALE"}
        or not isinstance(consumer_policy.get("all_consumers_bound"), bool)
    ):
        errors.append("consumer_policy state is invalid")

    audit_status = (
        current_digest_audit.get("status")
        if isinstance(current_digest_audit, dict)
        else None
    )
    consumer_status = (
        consumer_policy.get("status") if isinstance(consumer_policy, dict) else None
    )
    expected_upgrade = bool(
        snapshot.get("head_relation") == "EQUAL"
        and snapshot.get("integration_head_relation") != "DIVERGED"
        and audit_status == "PASS"
        and consumer_status == "PASS"
    )
    if snapshot.get("status_upgrade_allowed") is not expected_upgrade:
        errors.append("status_upgrade_allowed disagrees with all authorization gates")

    try:
        _validate_timestamp(snapshot.get("observed_at"))
    except SnapshotError as exc:
        errors.append(str(exc))

    status = snapshot.get("status")
    if not isinstance(status, dict) or set(status) != set(STATUS_KEYS):
        errors.append("status must contain exactly F1, F2, F3, and T6")
    elif not all(isinstance(status[key], str) and status[key] for key in STATUS_KEYS):
        errors.append("all status values must be nonempty strings")

    digest_inputs = snapshot.get("digest_inputs")
    if not isinstance(digest_inputs, dict) or set(digest_inputs) != set(DIGEST_SCOPES):
        errors.append("digest_inputs must contain every frozen digest input group")
    else:
        for name, value in digest_inputs.items():
            if not isinstance(value, dict):
                errors.append(f"digest_inputs.{name} must be an object")
                continue
            if set(value) != {"file_count", "paths", "scope"}:
                errors.append(f"digest_inputs.{name} has unknown or missing keys")
            if not isinstance(value.get("file_count"), int) or value["file_count"] <= 0:
                errors.append(f"digest_inputs.{name}.file_count must be positive")
            paths = value.get("paths")
            if (
                not isinstance(paths, list)
                or not paths
                or not all(isinstance(path, str) and path for path in paths)
                or paths != sorted(set(paths))
            ):
                errors.append(
                    f"digest_inputs.{name}.paths must be a sorted unique string list"
                )
            elif value.get("file_count") != len(paths):
                errors.append(f"digest_inputs.{name}.file_count disagrees with paths")
            if value.get("scope") != DIGEST_SCOPES[name]:
                errors.append(f"digest_inputs.{name}.scope changed")

    manifest_digests = snapshot.get("manifest_digests")
    if not isinstance(manifest_digests, dict) or set(manifest_digests) != set(
        MANIFEST_PATHS
    ):
        errors.append("manifest_digests must contain every audited manifest")
    elif not all(
        isinstance(value, str) and DIGEST_RE.fullmatch(value)
        for value in manifest_digests.values()
    ):
        errors.append("manifest_digests values must be SHA-256 digests")

    manifest_statuses = snapshot.get("manifest_statuses")
    expected_status_keys = {
        "proof_frontier",
        "constructor_inventory",
        "runtime_protocol_freeze",
        "family_grammar_freeze",
        "residual_frontier",
    }
    if not isinstance(manifest_statuses, dict) or set(
        manifest_statuses
    ) != expected_status_keys:
        errors.append("manifest_statuses has unknown or missing keys")


def audit_snapshot(
    root: Path,
    snapshot: Mapping[str, Any],
    *,
    run_manifest_path: Path | None = None,
    provenance_locator: Gate0RunLocatorV1 | None = None,
    github_api_client: GitHubApiClientV1 | None = None,
    digest_audit_client: CurrentDigestAuditClientV1 | None = None,
    provenance_now: datetime | None = None,
    require_verified_head: bool = True,
    require_status_upgrade_authorized: bool = False,
) -> AuditResult:
    root = root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    observed_head = resolve_head(root)
    try:
        execution_binding = _capture_execution_binding(root, observed_head)
    except SnapshotError as exc:
        return AuditResult(
            (str(exc),), (), observed_head, None, False
        )
    _validate_shape(snapshot, errors)
    if snapshot.get("execution_binding") != execution_binding:
        errors.append("snapshot execution_binding is stale")
    recorded_head = snapshot.get("current_observed_head_sha")
    if recorded_head != observed_head:
        errors.append(
            "HEAD_DRIFT: current_observed_head_sha "
            f"{recorded_head!r} != repository HEAD {observed_head}"
        )

    last_verified = snapshot.get("last_verified_head_sha")
    attestation: VerifiedGate0Attestation | None = None
    if last_verified is not None:
        if run_manifest_path is None or provenance_locator is None:
            errors.append(
                "UNATTESTED_LAST_VERIFIED_HEAD: verification requires the manifest "
                "and GitHub provenance locator"
            )
        else:
            try:
                client = github_api_client or GitHubRestApiClientV1(
                    token=os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
                )
                attestation = _verified_gate0_attestation(
                    root,
                    run_manifest_path,
                    locator=provenance_locator,
                    api_client=client,
                    now=provenance_now,
                )
                if snapshot.get("last_verified_basis") != dict(attestation.basis):
                    errors.append(
                        "last_verified_basis does not match the replayed Gate-0 manifest"
                    )
                if last_verified != attestation.head_sha:
                    errors.append(
                        "last_verified_head_sha does not match the Gate-0 manifest"
                    )
            except SnapshotError as exc:
                errors.append(str(exc))
    elif run_manifest_path is not None or provenance_locator is not None:
        errors.append("snapshot has no verified HEAD but provenance inputs were supplied")
    relation: str | None = None
    if last_verified is None or (
        isinstance(last_verified, str) and SHA_RE.fullmatch(last_verified)
    ):
        try:
            relation = head_relation(root, last_verified, observed_head)
        except SnapshotError as exc:
            errors.append(str(exc))

    if relation is not None:
        if snapshot.get("head_relation") != relation:
            errors.append(
                f"head_relation is stale: recorded={snapshot.get('head_relation')!r}, "
                f"actual={relation!r}"
            )
        expected_state = _verification_state(relation)
        if snapshot.get("verification_state") != expected_state:
            errors.append(
                "verification_state is stale: "
                f"recorded={snapshot.get('verification_state')!r}, "
                f"actual={expected_state!r}"
            )
        audit_object = snapshot.get("current_digest_audit")
        consumer_object = snapshot.get("consumer_policy")
        audit_status = (
            audit_object.get("status") if isinstance(audit_object, dict) else None
        )
        consumer_status = (
            consumer_object.get("status")
            if isinstance(consumer_object, dict)
            else None
        )
        expected_allowed = bool(
            relation == "EQUAL"
            and snapshot.get("integration_head_relation") != "DIVERGED"
            and audit_status == "PASS"
            and consumer_status == "PASS"
        )
        if snapshot.get("status_upgrade_allowed") is not expected_allowed:
            errors.append("status_upgrade_allowed disagrees with the live HEAD relation")
        if require_verified_head and not (attestation is not None and relation == "EQUAL"):
            errors.append(
                "VERIFIED_HEAD_REQUIRED: trusted Gate-0 provenance must bind current HEAD"
            )
        if require_status_upgrade_authorized and not expected_allowed:
            errors.append(
                "STATUS_UPGRADE_BLOCKED: one or more provenance, HEAD, digest-audit, "
                "integration, or consumer gates are not PASS"
            )
        elif not expected_allowed:
            warnings.append(
                f"live snapshot is self-consistent but status upgrades remain blocked: {relation}"
            )

    if not errors or recorded_head == observed_head:
        if last_verified is None or (
            isinstance(last_verified, str) and SHA_RE.fullmatch(last_verified)
        ):
            try:
                expected = _build_expected(
                    root,
                    revision=observed_head,
                    attestation=attestation,
                    execution_binding=execution_binding,
                    digest_audit_client=digest_audit_client,
                    observed_at=str(snapshot.get("observed_at")),
                )
            except SnapshotError as exc:
                errors.append(str(exc))
            else:
                for key, expected_value in expected.items():
                    if snapshot.get(key) != expected_value:
                        errors.append(f"snapshot field is stale or forged: {key}")

    try:
        _assert_execution_binding_unchanged(root, observed_head, execution_binding)
    except SnapshotError as exc:
        errors.append(str(exc))

    return AuditResult(
        tuple(dict.fromkeys(errors)),
        tuple(dict.fromkeys(warnings)),
        observed_head,
        relation,
        bool(snapshot.get("status_upgrade_allowed")) and not errors,
    )


def load_snapshot(path: Path) -> dict[str, Any]:
    try:
        return _load_json_object_bytes(path.read_bytes(), source=str(path))
    except FileNotFoundError as exc:
        raise SnapshotError(f"snapshot does not exist: {path}") from exc


def load_provenance_locator(path: Path) -> Gate0RunLocatorV1:
    try:
        value = _load_json_object_bytes(path.read_bytes(), source=str(path))
    except FileNotFoundError as exc:
        raise SnapshotError(f"provenance locator does not exist: {path}") from exc
    return Gate0RunLocatorV1.from_mapping(value)


def resolve_output_path(root: Path, path: Path) -> Path:
    resolved = path.resolve() if path.is_absolute() else (root / path).resolve()
    try:
        relative = resolved.relative_to(root).as_posix()
    except ValueError as exc:
        raise SnapshotError("snapshot output must remain inside the repository") from exc
    if resolved.exists() and resolved.is_symlink():
        raise SnapshotError("refusing to overwrite a symlink snapshot output")
    tracked = subprocess.run(
        ["git", "ls-files", "--error-unmatch", "--", relative],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if tracked.returncode == 0:
        raise SnapshotError("live snapshot must be ephemeral, not tracked by Git")
    ignored = subprocess.run(
        ["git", "check-ignore", "-q", "--", relative],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if ignored.returncode != 0:
        raise SnapshotError("live snapshot output must be explicitly gitignored")
    return resolved


def write_snapshot(path: Path, snapshot: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_name = handle.name
            json.dump(snapshot, handle, ensure_ascii=False, indent=2, sort_keys=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
        temporary_name = None
    finally:
        if temporary_name is not None:
            try:
                Path(temporary_name).unlink()
            except FileNotFoundError:
                pass


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate_parser = subparsers.add_parser("generate")
    generate_parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    generate_parser.add_argument("--run-manifest", type=Path)
    generate_parser.add_argument("--provenance-locator", type=Path)
    generate_parser.add_argument("--observed-at")

    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("--snapshot", type=Path, default=DEFAULT_OUTPUT)
    verify_parser.add_argument("--run-manifest", type=Path)
    verify_parser.add_argument("--provenance-locator", type=Path)
    verify_parser.add_argument(
        "--allow-unverified-head",
        action="store_true",
        help="validate an explicitly unverified snapshot without authorizing status upgrades",
    )
    verify_parser.add_argument(
        "--require-status-upgrade-authorized",
        action="store_true",
        help="fail unless provenance, digest audit, integration and consumers authorize promotion",
    )

    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "generate":
            locator = (
                None
                if args.provenance_locator is None
                else load_provenance_locator(args.provenance_locator)
            )
            snapshot = build_snapshot(
                root,
                run_manifest_path=args.run_manifest,
                provenance_locator=locator,
                observed_at=args.observed_at,
            )
            output = resolve_output_path(root, args.output)
            write_snapshot(output, snapshot)
            print(
                json.dumps(
                    {
                        "output": str(output),
                        "current_observed_head_sha": snapshot[
                            "current_observed_head_sha"
                        ],
                        "last_verified_head_sha": snapshot[
                            "last_verified_head_sha"
                        ],
                        "head_relation": snapshot["head_relation"],
                        "verification_state": snapshot["verification_state"],
                        "status_upgrade_allowed": snapshot[
                            "status_upgrade_allowed"
                        ],
                    },
                    sort_keys=True,
                )
            )
            return 0

        snapshot_path = args.snapshot
        if not snapshot_path.is_absolute():
            snapshot_path = root / snapshot_path
        snapshot = load_snapshot(snapshot_path)
        locator = (
            None
            if args.provenance_locator is None
            else load_provenance_locator(args.provenance_locator)
        )
        result = audit_snapshot(
            root,
            snapshot,
            run_manifest_path=args.run_manifest,
            provenance_locator=locator,
            require_verified_head=not args.allow_unverified_head,
            require_status_upgrade_authorized=args.require_status_upgrade_authorized,
        )
        print(json.dumps(result.payload(), indent=2, sort_keys=True))
        return 0 if result.ok else 1
    except SnapshotError as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
