#!/usr/bin/env python3
"""Run Gate 0 verification and emit or verify a HEAD-bound CI manifest.

The checked-in source tree owns the command matrix.  A caller cannot replace
commands or assert a passing status through CLI arguments.  The ``run``
subcommand records every command result and writes the manifest atomically even
when one or more checks fail.  The ``verify`` subcommand distrusts the recorded
digests and recomputes them from the current Git checkout.

The manifest is an audit record, not a signature.  Artifact authenticity still
comes from the GitHub Actions run that uploads it.
"""

from __future__ import annotations

import argparse
import ast
from collections.abc import Mapping, Sequence
import dataclasses
import datetime as dt
import enum
import hashlib
import importlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import subprocess
import sys
import tempfile
import time
from typing import Any


SCHEMA_ID = "t6_ci_run_manifest_v1"
SCHEMA_VERSION = 1
ARTIFACT_ID = "ci_run_manifest_v1"
FILE_SET_SCHEMA_ID = "t6_ci_file_set_v1"
PRODUCER_REGISTRY_SCHEMA_ID = "t6_local_producer_registry_snapshot_v1"
PRODUCER_REGISTRY_STATUS = "LOCAL_RUNTIME_ONLY_NO_SHARED_ALL_PRODUCER_REGISTRY"
DEFAULT_OUTPUT = Path("data/t6-wave1/ci-run-manifest-v1.json")
GRAMMAR_PATH = "data/t6-wave1/family-grammar-freeze-v1.json"
LOCAL_PYTHON_NAMESPACE_ROOTS = ("scripts", "reproductions")
HEX_DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")


class ManifestError(RuntimeError):
    """Raised when a manifest cannot be generated or verified safely."""


@dataclasses.dataclass(frozen=True)
class CommandSpec:
    command_id: str
    argv: tuple[str, ...]
    timeout_seconds: int = 30 * 60

    def payload(self) -> dict[str, Any]:
        return {
            "id": self.command_id,
            "argv": list(self.argv),
            "timeout_seconds": self.timeout_seconds,
        }


@dataclasses.dataclass(frozen=True)
class GitTreeEntry:
    mode: str
    object_type: str
    object_id: str
    size: int | None
    path: str


GATE0_COMMANDS = (
    CommandSpec("kb_validate", ("python", "scripts/kb.py", "validate")),
    CommandSpec("kb_build", ("python", "scripts/kb.py", "build")),
    CommandSpec(
        "generated_indexes_clean",
        ("git", "diff", "--exit-code", "--", "index/"),
    ),
    CommandSpec(
        "pre_t6_contract_audit",
        (
            "python",
            "reproductions/pre_t6_contract_kernel_audit.py",
            "--root",
            ".",
            "--require-full-tree",
        ),
    ),
    CommandSpec(
        "constructor_inventory_audit",
        ("python", "scripts/audit_t6_constructor_inventory_v1.py"),
    ),
    CommandSpec(
        "ruff",
        ("ruff", "check", "scripts", "reproductions", "tests"),
    ),
    CommandSpec(
        "compileall",
        (
            "python",
            "-m",
            "compileall",
            "-q",
            "scripts",
            "reproductions",
            "tests",
        ),
    ),
    CommandSpec("git_diff_check", ("git", "diff", "--check")),
    CommandSpec(
        "full_unittest_discovery",
        (
            "python",
            "-m",
            "unittest",
            "discover",
            "-s",
            "tests",
            "-p",
            "test_*.py",
            "-v",
        ),
        timeout_seconds=5 * 60 * 60,
    ),
)


TOP_LEVEL_FIELDS = frozenset(
    {
        "artifact_id",
        "checkout_state",
        "commands",
        "digest_algorithm",
        "digest_scopes",
        "dirty_paths_after",
        "dirty_paths_before",
        "generated_at",
        "git_object_format",
        "grammar_hash",
        "grammar_source_sha256",
        "head_sha",
        "head_sha_after",
        "head_tree_sha",
        "infrastructure_errors",
        "kb_claim_set_digest",
        "manifest_payload_sha256",
        "producer_registry",
        "producer_registry_digest",
        "producer_registry_status",
        "python_implementation",
        "python_version",
        "results",
        "schema_id",
        "schema_version",
        "source_head_sha",
        "status",
        "test_manifest_digest",
        "tested_head_sha",
        "runtime_source_digest",
        "workflow_event",
        "workflow_job",
        "workflow_ref",
        "workflow_repository",
        "workflow_run_attempt",
        "workflow_run_id",
        "workflow_sha",
    }
)


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize one JSON value for all new v1 manifest digests."""

    try:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        ).encode("ascii")
    except (TypeError, ValueError) as exc:
        raise ManifestError(f"value is not canonical JSON: {exc}") from exc


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_sha256(value: Any) -> str:
    return sha256_bytes(canonical_json_bytes(value))


def _is_sha256(value: Any) -> bool:
    return isinstance(value, str) and HEX_DIGEST_RE.fullmatch(value) is not None


def _is_git_object_id(value: Any, object_format: Any) -> bool:
    expected_length = {"sha1": 40, "sha256": 64}.get(object_format)
    return (
        expected_length is not None
        and isinstance(value, str)
        and len(value) == expected_length
        and re.fullmatch(r"[0-9a-f]+", value) is not None
    )


def _run_bytes(
    argv: Sequence[str],
    *,
    root: Path,
    input_bytes: bytes | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[bytes]:
    try:
        completed = subprocess.run(
            list(argv),
            cwd=root,
            input=input_bytes,
            capture_output=True,
            check=False,
        )
    except OSError as exc:
        raise ManifestError(f"could not execute {argv[0]!r}: {exc}") from exc
    if check and completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise ManifestError(
            f"command failed ({completed.returncode}): {' '.join(argv)}"
            + (f": {detail}" if detail else "")
        )
    return completed


def git_bytes(root: Path, *args: str, check: bool = True) -> bytes:
    return _run_bytes(("git", *args), root=root, check=check).stdout


def git_text(root: Path, *args: str, check: bool = True) -> str:
    return git_bytes(root, *args, check=check).decode("utf-8", errors="strict").strip()


def resolve_repository_root(root: Path) -> Path:
    requested = root.resolve()
    actual = Path(git_text(requested, "rev-parse", "--show-toplevel")).resolve()
    if requested != actual:
        raise ManifestError(f"--root must be the repository root: {actual}")
    return actual


def resolve_output_path(root: Path, output: Path) -> Path:
    resolved = output.resolve() if output.is_absolute() else (root / output).resolve()
    try:
        relative = resolved.relative_to(root).as_posix()
    except ValueError as exc:
        raise ManifestError(
            "manifest output must remain inside the repository"
        ) from exc
    if resolved.exists() and resolved.is_symlink():
        raise ManifestError("refusing to overwrite a symlink manifest output")
    tracked = _run_bytes(
        ("git", "ls-files", "--error-unmatch", "--", relative),
        root=root,
        check=False,
    )
    if tracked.returncode == 0:
        raise ManifestError("CI run manifest must be ephemeral, not tracked by Git")
    ignored = _run_bytes(
        ("git", "check-ignore", "-q", "--", relative),
        root=root,
        check=False,
    )
    if ignored.returncode != 0:
        raise ManifestError("CI run manifest output must be explicitly gitignored")
    return resolved


def checkout_status(root: Path) -> tuple[str, ...]:
    output = (
        git_bytes(
            root,
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
            "--ignored=no",
        )
        .decode("utf-8", errors="strict")
        .rstrip("\n")
    )
    if not output:
        return ()
    return tuple(sorted(output.splitlines()))


def current_revision(root: Path) -> dict[str, str]:
    return {
        "head_sha": git_text(root, "rev-parse", "--verify", "HEAD^{commit}"),
        "head_tree_sha": git_text(root, "rev-parse", "--verify", "HEAD^{tree}"),
        "git_object_format": git_text(root, "rev-parse", "--show-object-format"),
    }


def git_tree_entries(root: Path, head_sha: str) -> tuple[GitTreeEntry, ...]:
    raw = git_bytes(root, "ls-tree", "-r", "-l", "-z", "--full-tree", head_sha)
    entries: list[GitTreeEntry] = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            metadata, path_bytes = record.split(b"\t", 1)
            mode, object_type, object_id, size_text = metadata.decode("ascii").split()
            path = path_bytes.decode("utf-8", errors="strict")
            size = None if size_text == "-" else int(size_text)
        except (UnicodeDecodeError, ValueError) as exc:
            raise ManifestError("could not parse a Git tree entry") from exc
        entries.append(GitTreeEntry(mode, object_type, object_id, size, path))
    if not entries:
        raise ManifestError("HEAD has no tracked files")
    return tuple(entries)


def git_blob_bytes(root: Path, entry: GitTreeEntry) -> bytes:
    if entry.object_type != "blob" or entry.mode not in {"100644", "100755"}:
        raise ManifestError(
            f"digest scope contains unsupported Git entry {entry.mode} "
            f"{entry.object_type} {entry.path}"
        )
    value = git_bytes(root, "cat-file", "blob", entry.object_id)
    if entry.size is not None and len(value) != entry.size:
        raise ManifestError(f"Git reported a stale size for {entry.path}")
    return value


def _local_module_aliases(path: str, namespace_roots: Sequence[str]) -> tuple[str, ...]:
    pure = PurePosixPath(path)
    if pure.suffix != ".py" or not pure.parts or pure.parts[0] not in namespace_roots:
        return ()
    relative = PurePosixPath(*pure.parts[1:])
    if relative.name == "__init__.py":
        module_parts = relative.parent.parts
    else:
        module_parts = relative.with_suffix("").parts
    if not module_parts:
        return (pure.parts[0],)
    unqualified = ".".join(module_parts)
    qualified = ".".join((pure.parts[0], *module_parts))
    return tuple(sorted({unqualified, qualified}))


def _local_module_index(
    entries: Sequence[GitTreeEntry], namespace_roots: Sequence[str]
) -> dict[str, tuple[GitTreeEntry, ...]]:
    candidates: dict[str, dict[str, GitTreeEntry]] = {}
    for entry in entries:
        for alias in _local_module_aliases(entry.path, namespace_roots):
            candidates.setdefault(alias, {})[entry.path] = entry
    return {
        alias: tuple(by_path[path] for path in sorted(by_path))
        for alias, by_path in sorted(candidates.items())
    }


def _current_package_parts(
    path: str, namespace_roots: Sequence[str]
) -> tuple[str, ...]:
    pure = PurePosixPath(path)
    if not pure.parts or pure.parts[0] not in namespace_roots:
        raise ManifestError(
            f"local import source is outside configured namespaces: {path}"
        )
    relative = PurePosixPath(*pure.parts[1:])
    if relative.name == "__init__.py":
        return relative.parent.parts
    return relative.with_suffix("").parent.parts


def _import_targets(
    tree: ast.AST,
    *,
    source_path: str,
    namespace_roots: Sequence[str],
) -> tuple[str, ...]:
    targets: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            targets.update(alias.name for alias in node.names)
            continue
        if isinstance(node, ast.ImportFrom):
            if node.level:
                package_parts = _current_package_parts(source_path, namespace_roots)
                parent_count = node.level - 1
                if parent_count > len(package_parts):
                    raise ManifestError(
                        f"relative import escapes local namespace in {source_path}: "
                        f"level={node.level} module={node.module!r}"
                    )
                remaining = package_parts[: len(package_parts) - parent_count]
                module_parts = tuple((node.module or "").split("."))
                if module_parts == ("",):
                    module_parts = ()
                base_parts = (*remaining, *module_parts)
                if not base_parts:
                    raise ManifestError(
                        f"relative import has no resolvable local package: {source_path}"
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
        is_dynamic_import = (
            isinstance(node.func, ast.Name) and node.func.id == "__import__"
        ) or (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "importlib"
            and node.func.attr == "import_module"
        )
        if not is_dynamic_import:
            continue
        module_value = node.args[0]
        if not isinstance(module_value, ast.Constant) or not isinstance(
            module_value.value, str
        ):
            raise ManifestError(
                f"nonliteral dynamic import prevents a closed runtime digest: {source_path}"
            )
        if module_value.value.startswith("."):
            raise ManifestError(
                f"relative dynamic import is unsupported in runtime digest: {source_path}"
            )
        targets.add(module_value.value)
    return tuple(sorted(targets))


def _resolve_local_import(
    module_name: str,
    *,
    source_path: str,
    module_index: Mapping[str, Sequence[GitTreeEntry]],
) -> tuple[GitTreeEntry, ...]:
    parts = tuple(part for part in module_name.split(".") if part)
    resolved: dict[str, GitTreeEntry] = {}
    for length in range(1, len(parts) + 1):
        alias = ".".join(parts[:length])
        candidates = tuple(module_index.get(alias, ()))
        if len(candidates) > 1:
            paths = [entry.path for entry in candidates]
            raise ManifestError(
                f"ambiguous local module {alias!r} imported by {source_path}: {paths}"
            )
        if candidates:
            resolved[candidates[0].path] = candidates[0]
    return tuple(resolved[path] for path in sorted(resolved))


def local_python_import_closure(
    root: Path,
    entries: Sequence[GitTreeEntry],
    *,
    root_paths: Sequence[str],
    namespace_roots: Sequence[str] = LOCAL_PYTHON_NAMESPACE_ROOTS,
) -> tuple[GitTreeEntry, ...]:
    """Return the tracked-HEAD closure of repository-local Python imports.

    Both bare imports (made possible by the runtime's ``sys.path`` setup) and
    namespace-qualified imports are resolved.  An import that has multiple
    tracked candidates fails closed instead of inheriting interpreter path
    precedence.
    """

    if not namespace_roots or len(set(namespace_roots)) != len(namespace_roots):
        raise ManifestError("local Python namespace roots must be nonempty and unique")
    entry_by_path: dict[str, GitTreeEntry] = {}
    for entry in entries:
        if entry.path in entry_by_path:
            raise ManifestError(f"duplicate Git tree path: {entry.path}")
        entry_by_path[entry.path] = entry
    roots = tuple(sorted(set(root_paths)))
    if not roots:
        raise ManifestError("runtime source root set is empty")
    missing_roots = [path for path in roots if path not in entry_by_path]
    if missing_roots:
        raise ManifestError(
            f"runtime source roots are absent from HEAD: {missing_roots}"
        )
    for path in roots:
        if not _local_module_aliases(path, namespace_roots):
            raise ManifestError(
                f"runtime source root is not a local Python module: {path}"
            )

    module_index = _local_module_index(entries, namespace_roots)
    pending = list(reversed(roots))
    closure: dict[str, GitTreeEntry] = {}
    while pending:
        path = pending.pop()
        if path in closure:
            continue
        entry = entry_by_path[path]
        closure[path] = entry
        try:
            source = git_blob_bytes(root, entry).decode("utf-8", errors="strict")
            tree = ast.parse(source, filename=path)
        except (SyntaxError, UnicodeDecodeError) as exc:
            raise ManifestError(f"cannot parse runtime source {path}: {exc}") from exc
        dependencies: dict[str, GitTreeEntry] = {}
        for module_name in _import_targets(
            tree,
            source_path=path,
            namespace_roots=namespace_roots,
        ):
            for dependency in _resolve_local_import(
                module_name,
                source_path=path,
                module_index=module_index,
            ):
                dependencies[dependency.path] = dependency
        pending.extend(
            path for path in reversed(sorted(dependencies)) if path not in closure
        )
    return tuple(closure[path] for path in sorted(closure))


def runtime_source_entries(
    root: Path, entries: Sequence[GitTreeEntry]
) -> tuple[GitTreeEntry, ...]:
    """Return all tracked T6 script roots and their local import closure."""

    root_paths = tuple(
        sorted(
            entry.path
            for entry in entries
            if PurePosixPath(entry.path).parent == PurePosixPath("scripts")
            and PurePosixPath(entry.path).name.startswith("t6_")
            and PurePosixPath(entry.path).suffix == ".py"
        )
    )
    return local_python_import_closure(root, entries, root_paths=root_paths)


def file_set_receipt(
    root: Path,
    entries: Sequence[GitTreeEntry],
    *,
    scope_id: str,
    patterns: Sequence[str],
) -> dict[str, Any]:
    """Return a path-, mode-, size-, and content-bound HEAD file-set receipt."""

    selected = sorted(entries, key=lambda item: item.path)
    if not selected:
        raise ManifestError(f"digest scope {scope_id!r} is empty")
    if len({entry.path for entry in selected}) != len(selected):
        raise ManifestError(f"digest scope {scope_id!r} contains duplicate paths")
    files: list[dict[str, Any]] = []
    for entry in selected:
        content = git_blob_bytes(root, entry)
        files.append(
            {
                "mode": entry.mode,
                "path": entry.path,
                "sha256": sha256_bytes(content),
                "size": len(content),
            }
        )
    digest_payload = {"schema_id": FILE_SET_SCHEMA_ID, "files": files}
    return {
        "scope_id": scope_id,
        "patterns": list(patterns),
        "file_count": len(files),
        "files": files,
        "digest": canonical_sha256(digest_payload),
    }


def build_digest_scopes(
    root: Path, entries: Sequence[GitTreeEntry]
) -> dict[str, dict[str, Any]]:
    claims = [
        entry
        for entry in entries
        if entry.path.startswith("claims/") and entry.path.endswith(".md")
    ]
    runtime_roots = tuple(
        sorted(
            entry.path
            for entry in entries
            if PurePosixPath(entry.path).parent == PurePosixPath("scripts")
            and PurePosixPath(entry.path).name.startswith("t6_")
            and PurePosixPath(entry.path).suffix == ".py"
        )
    )
    runtime_sources = runtime_source_entries(root, entries)
    tests = [
        entry
        for entry in entries
        if entry.path.startswith("tests/") and entry.path.endswith(".py")
    ]
    scopes = {
        "kb_claim_set": file_set_receipt(
            root,
            claims,
            scope_id="kb_claim_set",
            patterns=("claims/*.md",),
        ),
        "runtime_source": file_set_receipt(
            root,
            runtime_sources,
            scope_id="runtime_source",
            patterns=("scripts/t6_*.py",),
        ),
        "test_manifest": file_set_receipt(
            root,
            tests,
            scope_id="test_manifest",
            patterns=("tests/**/*.py",),
        ),
    }
    scopes["test_manifest"]["discovered_test_file_count"] = sum(
        PurePosixPath(item["path"]).name.startswith("test_")
        for item in scopes["test_manifest"]["files"]
    )
    scopes["runtime_source"].update(
        {
            "selection": "tracked_head_ast_local_import_closure_v1",
            "namespace_roots": list(LOCAL_PYTHON_NAMESPACE_ROOTS),
            "root_file_count": len(runtime_roots),
            "root_paths": list(runtime_roots),
            "transitive_file_count": len(runtime_sources) - len(runtime_roots),
        }
    )
    return scopes


def _jsonable(value: Any) -> Any:
    if dataclasses.is_dataclass(value):
        return {
            field.name: _jsonable(getattr(value, field.name))
            for field in dataclasses.fields(value)
        }
    if isinstance(value, enum.Enum):
        return _jsonable(value.value)
    if isinstance(value, Mapping):
        if any(not isinstance(key, str) for key in value):
            raise ManifestError("registry mappings must use string keys")
        return {key: _jsonable(value[key]) for key in sorted(value)}
    if isinstance(value, (set, frozenset)):
        normalized = [_jsonable(item) for item in value]
        return sorted(normalized, key=canonical_json_bytes)
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise ManifestError(f"registry contains unsupported value {type(value).__name__}")


def producer_registry_payload(root: Path) -> dict[str, Any]:
    """Serialize the instantiated local runtime registry without callable bodies."""

    search_paths = [str(root / "scripts"), str(root / "reproductions")]
    inserted: list[str] = []
    for item in reversed(search_paths):
        if item not in sys.path:
            sys.path.insert(0, item)
            inserted.append(item)
    try:
        importlib.invalidate_caches()
        module = importlib.import_module("t6_q_one_full_carrier_runtime_slice_v1")
        selector = module.build_runtime()
    except Exception as exc:
        raise ManifestError(
            f"could not instantiate the local producer registry: {exc}"
        ) from exc
    finally:
        for item in inserted:
            sys.path.remove(item)

    payload = {
        "schema_id": PRODUCER_REGISTRY_SCHEMA_ID,
        "status": PRODUCER_REGISTRY_STATUS,
        "initializer": _jsonable(selector.initializer),
        "producer_rules": _jsonable(selector.producer_rules_v1()),
        "producers": [
            _jsonable(selector.producers[key]) for key in sorted(selector.producers)
        ],
        "terminal_producers": [
            _jsonable(selector.terminal_producers[key])
            for key in sorted(selector.terminal_producers)
        ],
        "dispatch_precedence": _jsonable(selector.dispatch_precedence),
        "terminal_dispatch_precedence": _jsonable(
            selector.terminal_dispatch_precedence
        ),
        "callable_registry_ids": {
            "executors": sorted(selector.executors),
            "projectors": sorted(selector.projectors),
            "source_terminal_schedulers": sorted(selector.source_terminal_schedulers),
            "target_terminal_schedulers": sorted(selector.target_terminal_schedulers),
            "terminal_executors": sorted(selector.terminal_executors),
            "terminal_verifiers": sorted(selector.terminal_verifiers),
            "transition_validators": sorted(selector.transition_validators),
        },
    }
    return payload


def grammar_receipt(root: Path, entries: Sequence[GitTreeEntry]) -> dict[str, str]:
    matching = [entry for entry in entries if entry.path == GRAMMAR_PATH]
    if len(matching) != 1:
        raise ManifestError(f"HEAD must contain exactly one {GRAMMAR_PATH}")
    source = git_blob_bytes(root, matching[0])
    try:
        document = load_json_bytes_reject_duplicates(source)
    except ManifestError as exc:
        raise ManifestError(f"invalid grammar manifest: {exc}") from exc
    if not isinstance(document, dict) or "grammar" not in document:
        raise ManifestError("grammar manifest has no top-level grammar object")
    completed = _run_bytes(
        ("jq", "-cS", ".grammar"),
        root=root,
        input_bytes=source,
        check=True,
    )
    digest = sha256_bytes(completed.stdout)
    stored = document.get("grammar_hash")
    if stored != digest:
        raise ManifestError(
            f"stored grammar hash does not replay: expected {digest}, got {stored!r}"
        )
    return {"grammar_hash": digest, "grammar_source_sha256": sha256_bytes(source)}


def gate0_command_specs() -> tuple[CommandSpec, ...]:
    return GATE0_COMMANDS


def _execution_argv(spec: CommandSpec) -> tuple[str, ...]:
    if spec.argv and spec.argv[0] == "python":
        return (sys.executable, *spec.argv[1:])
    return spec.argv


def run_command(
    root: Path,
    spec: CommandSpec,
) -> dict[str, Any]:
    """Run one fixed command while streaming its output to the CI log."""

    started = time.monotonic()
    try:
        completed = subprocess.run(
            list(_execution_argv(spec)),
            cwd=root,
            check=False,
            timeout=spec.timeout_seconds,
        )
    except subprocess.TimeoutExpired:
        return {
            "id": spec.command_id,
            "status": "TIMED_OUT",
            "exit_code": None,
            "duration_ms": round((time.monotonic() - started) * 1000),
            "detail": f"exceeded {spec.timeout_seconds} seconds",
        }
    except OSError as exc:
        return {
            "id": spec.command_id,
            "status": "ERROR",
            "exit_code": None,
            "duration_ms": round((time.monotonic() - started) * 1000),
            "detail": str(exc),
        }
    return {
        "id": spec.command_id,
        "status": "PASS" if completed.returncode == 0 else "FAIL",
        "exit_code": completed.returncode,
        "duration_ms": round((time.monotonic() - started) * 1000),
        "detail": None,
    }


def skipped_results(detail: str) -> list[dict[str, Any]]:
    return [
        {
            "id": spec.command_id,
            "status": "SKIPPED",
            "exit_code": None,
            "duration_ms": 0,
            "detail": detail,
        }
        for spec in gate0_command_specs()
    ]


def github_context(*, require_github: bool, head_sha: str) -> dict[str, str | None]:
    in_github = os.environ.get("GITHUB_ACTIONS") == "true"
    required = {
        "GITHUB_RUN_ID": os.environ.get("GITHUB_RUN_ID"),
        "GITHUB_RUN_ATTEMPT": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "GITHUB_REPOSITORY": os.environ.get("GITHUB_REPOSITORY"),
        "GITHUB_SHA": os.environ.get("GITHUB_SHA"),
    }
    if require_github and not in_github:
        raise ManifestError("--require-github requires GITHUB_ACTIONS=true")
    if require_github:
        missing = sorted(key for key, value in required.items() if not value)
        if missing:
            raise ManifestError(f"missing required GitHub context: {missing}")
    workflow_sha = required["GITHUB_SHA"]
    if in_github and workflow_sha != head_sha:
        raise ManifestError(
            f"GITHUB_SHA does not match checkout HEAD: {workflow_sha!r} != {head_sha}"
        )
    return {
        "workflow_run_id": required["GITHUB_RUN_ID"] or "local",
        "workflow_run_attempt": required["GITHUB_RUN_ATTEMPT"] or "local",
        "workflow_repository": required["GITHUB_REPOSITORY"],
        "workflow_ref": os.environ.get("GITHUB_REF"),
        "workflow_event": os.environ.get("GITHUB_EVENT_NAME"),
        "workflow_job": os.environ.get("GITHUB_JOB"),
        "workflow_sha": workflow_sha,
        "source_head_sha": os.environ.get("GITHUB_HEAD_SHA"),
    }


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def derive_status(
    *,
    checkout_state: str,
    results: Sequence[Mapping[str, Any]],
    infrastructure_errors: Sequence[str],
) -> str:
    commands_pass = all(
        result.get("status") == "PASS" and result.get("exit_code") == 0
        for result in results
    )
    if infrastructure_errors or not commands_pass:
        return "FAIL"
    if checkout_state == "DIRTY_ALLOWED":
        return "DIAGNOSTIC_ONLY"
    return "PASS"


def seal_manifest(payload: Mapping[str, Any]) -> dict[str, Any]:
    result = dict(payload)
    result.pop("manifest_payload_sha256", None)
    result["manifest_payload_sha256"] = canonical_sha256(result)
    return result


def build_manifest(
    root: Path,
    *,
    revision: Mapping[str, str],
    head_sha_after: str,
    dirty_before: Sequence[str],
    dirty_after: Sequence[str],
    allow_dirty: bool,
    require_github: bool,
    results: Sequence[Mapping[str, Any]],
    infrastructure_errors: Sequence[str],
) -> dict[str, Any]:
    entries = git_tree_entries(root, revision["head_sha"])
    scopes = build_digest_scopes(root, entries)
    registry = producer_registry_payload(root)
    grammar = grammar_receipt(root, entries)
    checkout_state = (
        "CLEAN"
        if not dirty_before and not dirty_after
        else "DIRTY_ALLOWED"
        if allow_dirty
        else "DIRTY_REJECTED"
    )
    context = github_context(
        require_github=require_github, head_sha=revision["head_sha"]
    )
    errors = list(infrastructure_errors)
    if head_sha_after != revision["head_sha"]:
        errors.append("checkout HEAD changed during the Gate 0 run")
    if checkout_state == "DIRTY_REJECTED":
        errors.append("checkout did not match HEAD")
    payload: dict[str, Any] = {
        "schema_id": SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "artifact_id": ARTIFACT_ID,
        "generated_at": utc_now(),
        "head_sha": revision["head_sha"],
        "tested_head_sha": revision["head_sha"],
        "head_sha_after": head_sha_after,
        "head_tree_sha": revision["head_tree_sha"],
        "git_object_format": revision["git_object_format"],
        "checkout_state": checkout_state,
        "dirty_paths_before": list(dirty_before),
        "dirty_paths_after": list(dirty_after),
        **context,
        "python_implementation": platform.python_implementation(),
        "python_version": platform.python_version(),
        "digest_algorithm": {
            "name": "sha256",
            "canonical_json": "sort_keys,no_whitespace,ensure_ascii,no_nan,no_newline",
            "grammar_hash": "legacy jq -cS .grammar stdout including newline",
        },
        "digest_scopes": scopes,
        "kb_claim_set_digest": scopes["kb_claim_set"]["digest"],
        "runtime_source_digest": scopes["runtime_source"]["digest"],
        "test_manifest_digest": scopes["test_manifest"]["digest"],
        "producer_registry": registry,
        "producer_registry_digest": canonical_sha256(registry),
        "producer_registry_status": PRODUCER_REGISTRY_STATUS,
        **grammar,
        "commands": [spec.payload() for spec in gate0_command_specs()],
        "results": [dict(result) for result in results],
        "infrastructure_errors": list(dict.fromkeys(errors)),
    }
    payload["status"] = derive_status(
        checkout_state=checkout_state,
        results=payload["results"],
        infrastructure_errors=payload["infrastructure_errors"],
    )
    return seal_manifest(payload)


def emergency_manifest(
    *,
    revision: Mapping[str, str] | None,
    results: Sequence[Mapping[str, Any]],
    error: str,
) -> dict[str, Any]:
    """Return a deliberately unverifiable record when full generation crashes."""

    payload = {
        "schema_id": SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "artifact_id": ARTIFACT_ID,
        "generated_at": utc_now(),
        "head_sha": None if revision is None else revision.get("head_sha"),
        "commands": [spec.payload() for spec in gate0_command_specs()],
        "results": [dict(result) for result in results],
        "infrastructure_errors": [error],
        "status": "ERROR",
        "emergency": True,
    }
    return seal_manifest(payload)


def write_manifest_atomic(path: Path, manifest: Mapping[str, Any]) -> None:
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
            json.dump(manifest, handle, ensure_ascii=True, indent=2, sort_keys=True)
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


def load_json_bytes_reject_duplicates(value: bytes) -> Any:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, item in pairs:
            if key in result:
                raise ManifestError(f"duplicate JSON key {key!r}")
            result[key] = item
        return result

    try:
        return json.loads(value.decode("utf-8"), object_pairs_hook=reject_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ManifestError(f"invalid JSON: {exc}") from exc


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        value = load_json_bytes_reject_duplicates(path.read_bytes())
    except OSError as exc:
        raise ManifestError(f"could not read manifest {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ManifestError("manifest top-level value must be an object")
    return value


def _validate_result_records(
    results: Any, errors: list[str]
) -> list[Mapping[str, Any]]:
    if not isinstance(results, list):
        errors.append("results must be an array")
        return []
    expected_ids = [spec.command_id for spec in gate0_command_specs()]
    observed_ids: list[str] = []
    normalized: list[Mapping[str, Any]] = []
    expected_keys = {"id", "status", "exit_code", "duration_ms", "detail"}
    for index, result in enumerate(results):
        if not isinstance(result, dict):
            errors.append(f"results[{index}] must be an object")
            continue
        normalized.append(result)
        if set(result) != expected_keys:
            errors.append(f"results[{index}] has an invalid field set")
        identifier = result.get("id")
        if isinstance(identifier, str):
            observed_ids.append(identifier)
        else:
            errors.append(f"results[{index}].id must be a string")
        status = result.get("status")
        exit_code = result.get("exit_code")
        if status not in {"PASS", "FAIL", "ERROR", "TIMED_OUT", "SKIPPED"}:
            errors.append(f"results[{index}].status is invalid")
        if exit_code is not None and (
            not isinstance(exit_code, int) or isinstance(exit_code, bool)
        ):
            errors.append(f"results[{index}].exit_code must be an integer or null")
        if status == "PASS" and exit_code != 0:
            errors.append(f"results[{index}] claims PASS without exit code 0")
        if status == "FAIL" and (not isinstance(exit_code, int) or exit_code == 0):
            errors.append(f"results[{index}] claims FAIL without a nonzero exit code")
        if status in {"ERROR", "TIMED_OUT", "SKIPPED"} and exit_code is not None:
            errors.append(f"results[{index}] must use a null exit code")
        duration = result.get("duration_ms")
        if not isinstance(duration, int) or isinstance(duration, bool) or duration < 0:
            errors.append(f"results[{index}].duration_ms must be a nonnegative integer")
        detail = result.get("detail")
        if detail is not None and not isinstance(detail, str):
            errors.append(f"results[{index}].detail must be a string or null")
    if observed_ids != expected_ids:
        errors.append("result IDs/order do not match the fixed Gate 0 command matrix")
    return normalized


def verify_manifest(
    root: Path,
    manifest: Mapping[str, Any],
    *,
    require_github: bool = False,
    require_pass: bool = False,
    allow_dirty: bool = False,
) -> tuple[str, ...]:
    """Return every verification error without trusting any stored digest."""

    errors: list[str] = []
    if set(manifest) != TOP_LEVEL_FIELDS:
        missing = sorted(TOP_LEVEL_FIELDS - set(manifest))
        extra = sorted(set(manifest) - TOP_LEVEL_FIELDS)
        errors.append(f"top-level field mismatch: missing={missing}, extra={extra}")
    if manifest.get("schema_id") != SCHEMA_ID:
        errors.append("schema_id is not t6_ci_run_manifest_v1")
    if manifest.get("schema_version") != SCHEMA_VERSION:
        errors.append("schema_version is not 1")
    if manifest.get("artifact_id") != ARTIFACT_ID:
        errors.append("artifact_id is not ci_run_manifest_v1")
    generated_at = manifest.get("generated_at")
    try:
        parsed_generated_at = dt.datetime.fromisoformat(
            str(generated_at).replace("Z", "+00:00")
        )
        if parsed_generated_at.tzinfo is None:
            raise ValueError("timestamp has no timezone")
    except ValueError:
        errors.append("generated_at is not a timezone-qualified ISO timestamp")
    recorded_digest = manifest.get("manifest_payload_sha256")
    unsigned = dict(manifest)
    unsigned.pop("manifest_payload_sha256", None)
    if recorded_digest != canonical_sha256(unsigned):
        errors.append("manifest_payload_sha256 does not replay")
    for field in (
        "manifest_payload_sha256",
        "kb_claim_set_digest",
        "runtime_source_digest",
        "test_manifest_digest",
        "producer_registry_digest",
        "grammar_hash",
        "grammar_source_sha256",
    ):
        if not _is_sha256(manifest.get(field)):
            errors.append(f"{field} is not a lowercase SHA-256 digest")

    revision = current_revision(root)
    object_format = manifest.get("git_object_format")
    for field in ("head_sha", "tested_head_sha", "head_sha_after", "head_tree_sha"):
        if not _is_git_object_id(manifest.get(field), object_format):
            errors.append(
                f"{field} is not valid for Git object format {object_format!r}"
            )
    source_head_sha = manifest.get("source_head_sha")
    if source_head_sha is not None and not _is_git_object_id(
        source_head_sha, object_format
    ):
        errors.append("source_head_sha is not null or a valid Git object ID")
    if manifest.get("head_sha") != revision["head_sha"]:
        errors.append("manifest head_sha does not match checkout HEAD")
    if manifest.get("tested_head_sha") != revision["head_sha"]:
        errors.append("manifest tested_head_sha does not match checkout HEAD")
    if manifest.get("head_sha_after") != revision["head_sha"]:
        errors.append("manifest head_sha_after does not match checkout HEAD")
    if manifest.get("head_tree_sha") != revision["head_tree_sha"]:
        errors.append("manifest head_tree_sha does not match checkout tree")
    if manifest.get("git_object_format") != revision["git_object_format"]:
        errors.append("manifest git_object_format does not match checkout")
    for field in ("workflow_run_id", "workflow_run_attempt"):
        if not isinstance(manifest.get(field), str) or not manifest[field]:
            errors.append(f"{field} must be a nonempty string")
    for field in (
        "workflow_repository",
        "workflow_ref",
        "workflow_event",
        "workflow_job",
        "workflow_sha",
    ):
        if manifest.get(field) is not None and not isinstance(manifest[field], str):
            errors.append(f"{field} must be a string or null")
    for field in ("python_implementation", "python_version"):
        if not isinstance(manifest.get(field), str) or not manifest[field]:
            errors.append(f"{field} must be a nonempty string")

    in_github = os.environ.get("GITHUB_ACTIONS") == "true"
    if allow_dirty and (require_github or in_github):
        errors.append("--allow-dirty is forbidden under GitHub Actions")
    dirty = checkout_status(root)
    if dirty and not allow_dirty:
        errors.append("checkout is dirty")
    checkout_state = manifest.get("checkout_state")
    if checkout_state == "CLEAN":
        if manifest.get("dirty_paths_before") or manifest.get("dirty_paths_after"):
            errors.append("CLEAN manifest records dirty paths")
        if dirty:
            errors.append("CLEAN manifest no longer has a clean checkout")
    elif checkout_state == "DIRTY_ALLOWED":
        if not allow_dirty:
            errors.append("DIRTY_ALLOWED manifest requires --allow-dirty")
        if list(dirty) != manifest.get("dirty_paths_after"):
            errors.append("current dirty paths do not match dirty_paths_after")
    else:
        errors.append("checkout_state is not verifiable")

    try:
        context = github_context(
            require_github=require_github,
            head_sha=revision["head_sha"],
        )
    except ManifestError as exc:
        errors.append(str(exc))
    else:
        if require_github or in_github:
            for key, value in context.items():
                if manifest.get(key) != value:
                    errors.append(f"{key} does not match the GitHub environment")

    expected_commands = [spec.payload() for spec in gate0_command_specs()]
    if manifest.get("commands") != expected_commands:
        errors.append("commands do not match the fixed Gate 0 matrix")
    results = _validate_result_records(manifest.get("results"), errors)
    infrastructure_errors = manifest.get("infrastructure_errors")
    if not isinstance(infrastructure_errors, list) or any(
        not isinstance(item, str) for item in infrastructure_errors
    ):
        errors.append("infrastructure_errors must be an array of strings")
        infrastructure_errors = ["invalid infrastructure_errors"]

    try:
        entries = git_tree_entries(root, revision["head_sha"])
        expected_scopes = build_digest_scopes(root, entries)
        if manifest.get("digest_scopes") != expected_scopes:
            errors.append("digest_scopes do not replay from HEAD")
        for field, scope_id in (
            ("kb_claim_set_digest", "kb_claim_set"),
            ("runtime_source_digest", "runtime_source"),
            ("test_manifest_digest", "test_manifest"),
        ):
            if manifest.get(field) != expected_scopes[scope_id]["digest"]:
                errors.append(f"{field} does not replay from HEAD")
        registry = producer_registry_payload(root)
        if manifest.get("producer_registry") != registry:
            errors.append("producer_registry does not replay")
        if manifest.get("producer_registry_digest") != canonical_sha256(registry):
            errors.append("producer_registry_digest does not replay")
        if manifest.get("producer_registry_status") != PRODUCER_REGISTRY_STATUS:
            errors.append("producer_registry_status is invalid")
        grammar = grammar_receipt(root, entries)
        for field, value in grammar.items():
            if manifest.get(field) != value:
                errors.append(f"{field} does not replay from HEAD")
    except ManifestError as exc:
        errors.append(str(exc))

    expected_digest_algorithm = {
        "name": "sha256",
        "canonical_json": "sort_keys,no_whitespace,ensure_ascii,no_nan,no_newline",
        "grammar_hash": "legacy jq -cS .grammar stdout including newline",
    }
    if manifest.get("digest_algorithm") != expected_digest_algorithm:
        errors.append("digest_algorithm is invalid")
    expected_status = derive_status(
        checkout_state=str(checkout_state),
        results=results,
        infrastructure_errors=infrastructure_errors,
    )
    if manifest.get("status") != expected_status:
        errors.append("status does not follow command results and checkout state")
    if require_pass and manifest.get("status") != "PASS":
        errors.append("manifest does not record a clean PASS")
    return tuple(errors)


def run_gate0(
    root: Path,
    output: Path,
    *,
    require_github: bool,
    allow_dirty: bool,
) -> int:
    revision: dict[str, str] | None = None
    resolved_output: Path | None = None
    results: list[dict[str, Any]] = []
    infrastructure_errors: list[str] = []
    dirty_before: tuple[str, ...] = ()
    dirty_after: tuple[str, ...] = ()
    head_sha_after = ""
    in_github = os.environ.get("GITHUB_ACTIONS") == "true"

    try:
        root = resolve_repository_root(root)
        resolved_output = resolve_output_path(root, output)
        if allow_dirty and (require_github or in_github):
            raise ManifestError("--allow-dirty is forbidden under GitHub Actions")
        revision = current_revision(root)
        github_context(require_github=require_github, head_sha=revision["head_sha"])
        dirty_before = checkout_status(root)
        if dirty_before and not allow_dirty:
            infrastructure_errors.append("checkout was dirty before the Gate 0 run")
            results = skipped_results("dirty checkout rejected")
        else:
            for spec in gate0_command_specs():
                results.append(run_command(root, spec))
        head_sha_after = git_text(root, "rev-parse", "--verify", "HEAD^{commit}")
        dirty_after = checkout_status(root)
        if dirty_after and not allow_dirty:
            infrastructure_errors.append("checkout was dirty after the Gate 0 run")
    except (ManifestError, KeyboardInterrupt) as exc:
        infrastructure_errors.append(str(exc) or type(exc).__name__)
        if not results:
            results = skipped_results("Gate 0 infrastructure preflight failed")
        elif len(results) < len(gate0_command_specs()):
            completed_ids = {result["id"] for result in results}
            results.extend(
                {
                    "id": spec.command_id,
                    "status": "SKIPPED",
                    "exit_code": None,
                    "duration_ms": 0,
                    "detail": "Gate 0 run was interrupted",
                }
                for spec in gate0_command_specs()
                if spec.command_id not in completed_ids
            )

    try:
        if revision is None or resolved_output is None:
            raise ManifestError("repository/output preflight did not complete")
        if not head_sha_after:
            head_sha_after = git_text(root, "rev-parse", "--verify", "HEAD^{commit}")
        if not dirty_after:
            dirty_after = checkout_status(root)
        manifest = build_manifest(
            root,
            revision=revision,
            head_sha_after=head_sha_after,
            dirty_before=dirty_before,
            dirty_after=dirty_after,
            allow_dirty=allow_dirty,
            require_github=require_github,
            results=results,
            infrastructure_errors=infrastructure_errors,
        )
    except Exception as exc:
        manifest = emergency_manifest(
            revision=revision,
            results=results or skipped_results("manifest generation failed"),
            error=f"manifest generation failed: {exc}",
        )

    if resolved_output is None:
        print(json.dumps(manifest, ensure_ascii=True, indent=2, sort_keys=True))
        print("FAIL: could not resolve a safe manifest output", file=sys.stderr)
        return 1
    write_manifest_atomic(resolved_output, manifest)
    print(f"wrote {manifest['status']} manifest: {resolved_output}")
    if manifest["status"] in {"PASS", "DIAGNOSTIC_ONLY"}:
        return 0
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    run_parser = subparsers.add_parser("run", help="run Gate 0 and write a manifest")
    run_parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    run_parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    run_parser.add_argument("--require-github", action="store_true")
    run_parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="run a non-HEAD-bound local diagnostic (forbidden in GitHub Actions)",
    )
    verify_parser = subparsers.add_parser("verify", help="recompute a manifest")
    verify_parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    verify_parser.add_argument("--manifest", type=Path, default=DEFAULT_OUTPUT)
    verify_parser.add_argument("--require-github", action="store_true")
    verify_parser.add_argument("--require-pass", action="store_true")
    verify_parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="verify a local DIAGNOSTIC_ONLY manifest (forbidden in GitHub Actions)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.subcommand == "run":
        return run_gate0(
            args.root,
            args.output,
            require_github=args.require_github,
            allow_dirty=args.allow_dirty,
        )

    try:
        root = resolve_repository_root(args.root)
        manifest_path = (
            args.manifest.resolve()
            if args.manifest.is_absolute()
            else (root / args.manifest).resolve()
        )
        manifest = load_manifest(manifest_path)
        errors = verify_manifest(
            root,
            manifest,
            require_github=args.require_github,
            require_pass=args.require_pass,
            allow_dirty=args.allow_dirty,
        )
    except ManifestError as exc:
        errors = (str(exc),)
    if errors:
        print("FAIL: CI run manifest verification failed", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"PASS: CI run manifest verified at {manifest['head_sha']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
