#!/usr/bin/env python3
"""Controlled exact-HEAD assembly of one q=1 actual source-input wrapper.

The public function accepts only a repository locator, full requested commit,
raw q=1 G input, and a V3 production result.  It fresh-loads the V3--V6
registries from that same Git tree, replays V3, reconstructs V4 and V5 through
their existing controlled entry points, makes the V6 source rebind, then emits
a serializable non-authority candidate and its non-E1 V2 projection.

It has no caller path for grants, V4/V5/V6 wires, state wires, target data,
or authority booleans.  The output is replay candidate data only; consumers
must invoke the independent replayer before treating it as exact-HEAD evidence.
"""

from __future__ import annotations

import copy
from contextlib import contextmanager
from enum import Enum
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from types import ModuleType
from typing import Any, Mapping, NoReturn, Sequence


ORCHESTRATOR_ID = "q1_exact_head_source_input_orchestrator_v1"
ORCHESTRATOR_PATH = "scripts/t6_q_one_exact_head_source_input_orchestrator_v1.py"
V6_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v6.py"
V6_RESOLVER_SYMBOL = "resolve_registry_v6"
V3_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v3.py"
V3_RESOLVER_SYMBOL = "resolve_registry_v3"
V4_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v4.py"
V4_RESOLVER_SYMBOL = "resolve_registry_v4"
V5_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v5.py"
V5_RESOLVER_SYMBOL = "resolve_registry_v5"
V3_VERIFIER_PATH = "scripts/t6_q_one_terminal_receipt_verifier_v1.py"
V3_VERIFIER_SYMBOL = "verify_q_one_production_terminal_receipt_v1"
V4_ORCHESTRATOR_PATH = "scripts/t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py"
V4_ORCHESTRATOR_SYMBOL = "assemble_q_one_root_prefix_scoped_e1_v2"
V4_REPLAYER_PATH = "scripts/t6_q_one_root_prefix_scoped_e1_receipt_verifier_v2.py"
V4_REPLAYER_SYMBOL = "verify_q_one_root_prefix_scoped_e1_receipt_v2"
V5_ORCHESTRATOR_PATH = "scripts/t6_q_one_root_v1_base_admission_orchestrator_v1.py"
V5_ORCHESTRATOR_SYMBOL = "assemble_q_one_root_v1_base_admission_v1"
V5_REPLAYER_PATH = "scripts/t6_q_one_root_v1_base_admission_receipt_verifier_v1.py"
V5_REPLAYER_SYMBOL = "verify_q_one_root_v1_base_admission_receipt_v1"
V6_REBIND_PATH = "scripts/t6_q_one_root_source_scoped_e1_rebind_v1.py"
V6_REBIND_SYMBOL = "rebind_q_one_root_source_scoped_e1_v1"
V6_REBIND_SERIALIZER = "root_source_scoped_e1_rebind_receipt_to_mapping_v1"
BINDER_PATH = "scripts/t6_q_one_exact_head_source_input_v1.py"
BINDER_CANDIDATE_SYMBOL = "_build_exact_head_q_one_source_input_replay_candidate_v1"
BINDER_SERIALIZER = "exact_head_q_one_actual_source_input_to_mapping_v1"
BINDER_CANDIDATE_EXTERNAL = "_candidate_external_binding_wire_from_exact_head_source_input_v1"
PRESTATE_PATH = "scripts/t6_q_one_phase_root_prestate_v2.py"
PRESTATE_BINDER = "make_external_q_one_source_binding_v2"
PRESTATE_SERIALIZER = "artifact_to_mapping_v2"
STATE_PATH = "scripts/t6_persistent_selector_state_v1.py"
ROOT_ENVELOPE_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"

V3_MISS_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
V3_MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"
V3_STATUS = "HEAD_BOUND_Q1_ROOT_TERMINAL_DECISION_AUTHORITY_NO_RECURSION"
V4_STATUS = "HEAD_BOUND_Q1_ROOT_PREFIX_SCOPED_E1_AUTHORITY_NO_SUCCESSOR_OR_RECURSION"
V5_STATUS = "HEAD_BOUND_Q1_ROOT_V1_BASE_ADMISSION_AUTHORITY_NO_QUEUE_OR_SUCCESSOR"
V6_STATUS = "HEAD_BOUND_Q1_EXACT_SOURCE_INPUT_CANDIDATE_REPLAY_ONLY"
V6_REGISTRY_ID = "t6_coordinator_role_registry_v6"
V3_REGISTRY_ID = "t6_coordinator_role_registry_v3"
V4_REGISTRY_ID = "t6_coordinator_role_registry_v4"
V5_REGISTRY_ID = "t6_coordinator_role_registry_v5"
BINDER_ROLE = "EXACT_HEAD_Q1_ACTUAL_SOURCE_INPUT_BINDER"
REBIND_ROLE = "INDEPENDENT_Q1_ROOT_SOURCE_SCOPED_E1_REBINDER"

FALSE_AUTHORITIES = (
    "generic_e1", "successor_e1", "e1_authority", "producer_authority", "branch_authority",
    "admission_authority", "queue_authority", "enqueue_authority", "e2_authority",
    "e3_authority", "e4_authority", "e5_authority", "t5_authority", "reentry_authority",
    "global_exhaustion",
)
REGULAR_MODES = frozenset({"100644", "100755"})
OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")


class OrchestratorRejectCode(str, Enum):
    INVALID_ROOT = "INVALID_ROOT"
    INVALID_HEAD = "INVALID_HEAD"
    HEAD_BINDING_ERROR = "HEAD_BINDING_ERROR"
    WORKTREE_BINDING_ERROR = "WORKTREE_BINDING_ERROR"
    MODULE_BINDING_ERROR = "MODULE_BINDING_ERROR"
    REGISTRY_ERROR = "REGISTRY_ERROR"
    V3_RECEIPT_ERROR = "V3_RECEIPT_ERROR"
    TERMINAL_SOURCE_NOT_MISS = "TERMINAL_SOURCE_NOT_MISS"
    ROLE_GRANT_ERROR = "ROLE_GRANT_ERROR"
    ROLE_ERROR = "ROLE_ERROR"
    SOURCE_ERROR = "SOURCE_ERROR"
    AUTHORITY_ERROR = "AUTHORITY_ERROR"
    MALFORMED_INPUT = "MALFORMED_INPUT"


class ExactHeadSourceInputOrchestratorError(ValueError):
    def __init__(self, code: OrchestratorRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: OrchestratorRejectCode, detail: str) -> NoReturn:
    raise ExactHeadSourceInputOrchestratorError(code, detail)


def _copy_json(value: Any, *, path: str = "$") -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(OrchestratorRejectCode.MALFORMED_INPUT, f"{path} non-string key")
            result[key] = _copy_json(child, path=f"{path}.{key}")
        return result
    if type(value) is list:
        return [_copy_json(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(OrchestratorRejectCode.MALFORMED_INPUT, f"{path} contains {type(value).__name__}")


def _mapping(value: Any, name: str) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(OrchestratorRejectCode.MALFORMED_INPUT, f"{name} must be an exact dict")
    return _copy_json(value, path=name)


def _run_git(root: Path, args: Sequence[str]) -> bytes:
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env["GIT_NO_REPLACE_OBJECTS"] = "1"
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, check=False, env=env)
    if result.returncode:
        _reject(OrchestratorRejectCode.HEAD_BINDING_ERROR, result.stderr.decode(errors="replace").strip())
    return result.stdout


@contextmanager
def _sanitized_git_environment() -> Any:
    inherited = {key: value for key, value in os.environ.items() if key.startswith("GIT_")}
    for key in inherited:
        os.environ.pop(key, None)
    os.environ["GIT_NO_REPLACE_OBJECTS"] = "1"
    try:
        yield
    finally:
        os.environ.pop("GIT_NO_REPLACE_OBJECTS", None)
        os.environ.update(inherited)


def _repository(locator: Path) -> Path:
    if type(locator) is not type(Path()):
        _reject(OrchestratorRejectCode.INVALID_ROOT, "root must be the exact platform Path type")
    try:
        return Path(_run_git(locator.resolve(), ("rev-parse", "--show-toplevel")).decode().strip()).resolve()
    except (OSError, UnicodeDecodeError) as exc:
        raise ExactHeadSourceInputOrchestratorError(OrchestratorRejectCode.INVALID_ROOT, str(exc)) from exc


def _exact_head(root: Path, requested_head: str) -> tuple[str, str]:
    fmt = _run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    size = 40 if fmt == "sha1" else 64 if fmt == "sha256" else 0
    if type(requested_head) is not str or len(requested_head) != size or OID_RE.fullmatch(requested_head) is None:
        _reject(OrchestratorRejectCode.INVALID_HEAD, "requested_head must be a full lowercase commit ID")
    if _run_git(root, ("cat-file", "-t", requested_head)).decode().strip() != "commit":
        _reject(OrchestratorRejectCode.INVALID_HEAD, "requested object is not a commit")
    if _run_git(root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}")).decode().strip() != requested_head:
        _reject(OrchestratorRejectCode.INVALID_HEAD, "commit resolution drift")
    return requested_head, _run_git(root, ("rev-parse", f"{requested_head}^{{tree}}")).decode().strip()


def _entries(root: Path, head: str) -> dict[str, tuple[str, str, str]]:
    result: dict[str, tuple[str, str, str]] = {}
    for record in _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head)).split(b"\0"):
        if not record:
            continue
        try:
            metadata, encoded_path = record.split(b"\t", 1)
            mode, kind, object_id = metadata.decode("ascii").split(" ")
            path = encoded_path.decode("utf-8")
        except (UnicodeDecodeError, ValueError) as exc:
            raise ExactHeadSourceInputOrchestratorError(OrchestratorRejectCode.HEAD_BINDING_ERROR, repr(record)) from exc
        pure = PurePosixPath(path)
        if not path or pure.is_absolute() or path != pure.as_posix() or "\\" in path or any(part in {"", ".", ".."} for part in pure.parts) or path in result:
            _reject(OrchestratorRejectCode.HEAD_BINDING_ERROR, f"unsafe tree path {path!r}")
        result[path] = (mode, kind, object_id)
    return result


def _blob(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str) -> bytes:
    pure = PurePosixPath(path) if type(path) is str else PurePosixPath(".")
    if type(path) is not str or PATH_RE.fullmatch(path) is None or pure.is_absolute() or path != pure.as_posix() or "\\" in path or any(part in {"", ".", ".."} for part in pure.parts):
        _reject(OrchestratorRejectCode.MODULE_BINDING_ERROR, f"unsafe path {path!r}")
    entry = entries.get(path)
    if entry is None or entry[0] not in REGULAR_MODES or entry[1] != "blob":
        _reject(OrchestratorRejectCode.MODULE_BINDING_ERROR, f"missing regular blob {path}")
    content = _run_git(root, ("cat-file", "blob", entry[2]))
    worktree = root / path
    if worktree.is_symlink() or not worktree.is_file() or worktree.read_bytes() != content:
        _reject(OrchestratorRejectCode.WORKTREE_BINDING_ERROR, path)
    return content


def _fresh(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str, name: str) -> ModuleType:
    content = _blob(root, entries, path)
    module = ModuleType(name)
    module.__file__ = str((root / path).resolve())
    previous = sys.modules.get(name)
    sys.modules[name] = module
    try:
        exec(compile(content, module.__file__, "exec"), module.__dict__)
    except Exception as exc:
        raise ExactHeadSourceInputOrchestratorError(OrchestratorRejectCode.MODULE_BINDING_ERROR, f"{path}: {exc}") from exc
    finally:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous
    return module


def _fresh_v6_rebind_bundle(root: Path, entries: Mapping[str, tuple[str, str, str]], head: str) -> ModuleType:
    specs = (
        ("t6_persistent_selector_state_v1", STATE_PATH),
        ("t6_q_one_root_initializer_envelope_v2", ROOT_ENVELOPE_PATH),
        (f"_t6_v6_rebind_{head}", V6_REBIND_PATH),
    )
    sentinel = object()
    previous: dict[str, object] = {}
    modules: dict[str, ModuleType] = {}
    try:
        for name, path in specs:
            previous[name] = sys.modules.get(name, sentinel)
            content = _blob(root, entries, path)
            module = ModuleType(name)
            module.__file__ = str((root / path).resolve())
            sys.modules[name] = module
            try:
                exec(compile(content, module.__file__, "exec"), module.__dict__)
            except Exception as exc:
                raise ExactHeadSourceInputOrchestratorError(OrchestratorRejectCode.MODULE_BINDING_ERROR, f"{path}: {exc}") from exc
            modules[name] = module
    finally:
        for name, _path in reversed(specs):
            prior = previous.get(name, sentinel)
            if prior is sentinel:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = prior
    return modules[specs[-1][0]]


def _call(module: ModuleType, symbol: str) -> Any:
    value = getattr(module, symbol, None)
    if not callable(value) or getattr(value, "__name__", None) != symbol or getattr(value, "__module__", None) != module.__name__:
        _reject(OrchestratorRejectCode.MODULE_BINDING_ERROR, f"missing exact callable {symbol}")
    return value


def _resolved_registry(module: ModuleType, symbol: str, *, root: Path, head: str, tree: str, expected_id: str, expected_status: str) -> dict[str, Any]:
    try:
        with _sanitized_git_environment():
            resolved = _call(module, symbol)(root=root, requested_head=head)
    except Exception as exc:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, f"{expected_id}: {exc}")
    if type(resolved) is not dict or resolved.get("head_sha") != head or resolved.get("head_tree_sha") != tree or resolved.get("status") != expected_status:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, f"{expected_id} exact-HEAD result")
    return _copy_json(resolved)


def _grant(resolved: Mapping[str, Any], role: str) -> dict[str, Any]:
    raw = resolved.get("resolved_role_grants")
    if type(raw) is not list:
        _reject(OrchestratorRejectCode.ROLE_GRANT_ERROR, "V6 grants missing")
    found = [item for item in raw if type(item) is dict and item.get("role") == role]
    if len(found) != 1 or type(found[0].get("grant_wire")) is not dict:
        _reject(OrchestratorRejectCode.ROLE_GRANT_ERROR, role)
    return _copy_json(found[0]["grant_wire"])


def _registry_context(v3: Mapping[str, Any], v4: Mapping[str, Any], v5: Mapping[str, Any], v6: Mapping[str, Any]) -> dict[str, Any]:
    for resolved, name in ((v3, "v3"), (v4, "v4"), (v5, "v5")):
        manifest = resolved.get("role_authority_manifest")
        if type(manifest) is not dict or type(manifest.get("digest")) is not str or type(resolved.get("registry_digest")) is not str:
            _reject(OrchestratorRejectCode.REGISTRY_ERROR, f"{name} manifest")
    cross = v6.get("cross_registries")
    manifest = v6.get("role_authority_manifest")
    if type(cross) is not dict or type(manifest) is not dict or type(manifest.get("digest")) is not str or type(v6.get("registry_digest")) is not str:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, "v6 manifest")
    expected = {"v3": v3, "v4": v4, "v5": v5}
    for name, resolved in expected.items():
        row = cross.get(name)
        if type(row) is not dict or row.get("registry_digest") != resolved["registry_digest"] or row.get("role_manifest_digest") != resolved["role_authority_manifest"]["digest"]:
            _reject(OrchestratorRejectCode.REGISTRY_ERROR, f"V6 {name} cross binding")
    return {
        "head_sha": v6["head_sha"],
        "head_tree_sha": v6["head_tree_sha"],
        "registries": {
            "v3": {"registry_id": V3_REGISTRY_ID, "registry_digest": v3["registry_digest"], "role_manifest_digest": v3["role_authority_manifest"]["digest"]},
            "v4": {"registry_id": V4_REGISTRY_ID, "registry_digest": v4["registry_digest"], "role_manifest_digest": v4["role_authority_manifest"]["digest"]},
            "v5": {"registry_id": V5_REGISTRY_ID, "registry_digest": v5["registry_digest"], "role_manifest_digest": v5["role_authority_manifest"]["digest"]},
            "v6": {"registry_id": V6_REGISTRY_ID, "registry_digest": v6["registry_digest"], "role_manifest_digest": manifest["digest"]},
        },
    }


def _verify_v3(result: Any, receipt: Mapping[str, Any], head: str) -> None:
    if (
        getattr(result, "status", None) != "PRODUCTION_Q1_TERMINAL_RECEIPT_VERIFIED"
        or getattr(result, "receipt_type", None) != V3_MISS_TYPE
        or getattr(result, "outcome", None) != V3_MISS_OUTCOME
        or receipt.get("head_sha") != head
    ):
        _reject(OrchestratorRejectCode.TERMINAL_SOURCE_NOT_MISS, "V3 prefix MISS required")


def _verify_replay(result: Any, expected_status: str, name: str) -> None:
    if getattr(result, "status", None) != expected_status or getattr(result, "wire_match", None) is not True or getattr(result, "authority_verified", None) is not True:
        _reject(OrchestratorRejectCode.SOURCE_ERROR, f"{name} replay did not verify")


def _check_output(source_input: Mapping[str, Any], external_binding: Mapping[str, Any]) -> None:
    for name in FALSE_AUTHORITIES:
        if type(source_input.get(name)) is not bool or source_input[name] is not False:
            _reject(OrchestratorRejectCode.AUTHORITY_ERROR, name)
    for name in ("source_actualness_input", "v1_base_admission_evidence", "v6_rebind_evidence"):
        if type(source_input.get(name)) is not bool or source_input[name] is not False:
            _reject(OrchestratorRejectCode.AUTHORITY_ERROR, name)
    if (
        source_input.get("binding_scope") != "EXACT_HEAD_Q1_ROOT_SOURCE_INPUT_REPLAY_CANDIDATE_NOT_E1"
        or external_binding.get("binding_scope") != "EXTERNAL_Q1_SOURCE_PREIMAGE_NOT_E1"
        or external_binding.get("source_binding_id") != source_input.get("external_binding_id")
        or external_binding.get("digest") != source_input.get("external_binding_digest")
    ):
        _reject(OrchestratorRejectCode.AUTHORITY_ERROR, "source binding scope")


def assemble_exact_head_q_one_actual_source_input_v1(
    *, root: Path, requested_head: str, raw_q_one_g: dict[str, Any], production_miss_receipt: dict[str, Any]
) -> dict[str, Any]:
    """Replay V3--V6 and project one source-input-only V2 binding."""

    repository = _repository(root)
    head, tree = _exact_head(repository, requested_head)
    entries = _entries(repository, head)
    own = _blob(repository, entries, ORCHESTRATOR_PATH)
    local = Path(__file__)
    if local.is_symlink() or not local.is_file() or local.resolve() != (repository / ORCHESTRATOR_PATH).resolve() or local.read_bytes() != own:
        _reject(OrchestratorRejectCode.WORKTREE_BINDING_ERROR, ORCHESTRATOR_PATH)
    raw = _mapping(raw_q_one_g, "raw_q_one_g")
    production = _mapping(production_miss_receipt, "production_miss_receipt")

    v3_registry = _resolved_registry(_fresh(repository, entries, V3_RESOLVER_PATH, f"_t6_v6_v3_{head}"), V3_RESOLVER_SYMBOL, root=repository, head=head, tree=tree, expected_id=V3_REGISTRY_ID, expected_status=V3_STATUS)
    v4_registry = _resolved_registry(_fresh(repository, entries, V4_RESOLVER_PATH, f"_t6_v6_v4_{head}"), V4_RESOLVER_SYMBOL, root=repository, head=head, tree=tree, expected_id=V4_REGISTRY_ID, expected_status=V4_STATUS)
    v5_registry = _resolved_registry(_fresh(repository, entries, V5_RESOLVER_PATH, f"_t6_v6_v5_{head}"), V5_RESOLVER_SYMBOL, root=repository, head=head, tree=tree, expected_id=V5_REGISTRY_ID, expected_status=V5_STATUS)
    v6_registry = _resolved_registry(_fresh(repository, entries, V6_RESOLVER_PATH, f"_t6_v6_registry_{head}"), V6_RESOLVER_SYMBOL, root=repository, head=head, tree=tree, expected_id=V6_REGISTRY_ID, expected_status=V6_STATUS)
    context = _registry_context(v3_registry, v4_registry, v5_registry, v6_registry)

    v3_verifier = _fresh(repository, entries, V3_VERIFIER_PATH, f"_t6_v6_v3_replay_{head}")
    try:
        with _sanitized_git_environment():
            v3_result = _call(v3_verifier, V3_VERIFIER_SYMBOL)(root=repository, requested_head=head, raw_q_one_g=raw, receipt=production)
    except Exception as exc:
        _reject(OrchestratorRejectCode.V3_RECEIPT_ERROR, str(exc))
    _verify_v3(v3_result, production, head)

    v4_orchestrator = _fresh(repository, entries, V4_ORCHESTRATOR_PATH, f"_t6_v6_v4_orchestrator_{head}")
    try:
        with _sanitized_git_environment():
            v4_wire = _call(v4_orchestrator, V4_ORCHESTRATOR_SYMBOL)(root=repository, requested_head=head, raw_q_one_g=raw, production_miss_receipt=production)
    except Exception as exc:
        _reject(OrchestratorRejectCode.ROLE_ERROR, f"V4: {exc}")
    v4_wire = _mapping(v4_wire, "v4_consumer_receipt")
    v4_replayer = _fresh(repository, entries, V4_REPLAYER_PATH, f"_t6_v6_v4_replayer_{head}")
    try:
        with _sanitized_git_environment():
            v4_result = _call(v4_replayer, V4_REPLAYER_SYMBOL)(root=repository, requested_head=head, raw_q_one_g=raw, production_miss_receipt=production, receipt=v4_wire)
    except Exception as exc:
        _reject(OrchestratorRejectCode.SOURCE_ERROR, f"V4 replay: {exc}")
    _verify_replay(v4_result, "Q1_ROOT_PREFIX_SCOPED_E1_RECEIPT_REPLAY_VERIFIED", "V4")

    v5_orchestrator = _fresh(repository, entries, V5_ORCHESTRATOR_PATH, f"_t6_v6_v5_orchestrator_{head}")
    try:
        with _sanitized_git_environment():
            v5_wire = _call(v5_orchestrator, V5_ORCHESTRATOR_SYMBOL)(root=repository, requested_head=head, raw_q_one_g=raw, production_miss_receipt=production)
    except Exception as exc:
        _reject(OrchestratorRejectCode.ROLE_ERROR, f"V5: {exc}")
    v5_wire = _mapping(v5_wire, "v5_base_admission_receipt")
    v5_replayer = _fresh(repository, entries, V5_REPLAYER_PATH, f"_t6_v6_v5_replayer_{head}")
    try:
        with _sanitized_git_environment():
            v5_result = _call(v5_replayer, V5_REPLAYER_SYMBOL)(root=repository, requested_head=head, raw_q_one_g=raw, production_miss_receipt=production, receipt=v5_wire)
    except Exception as exc:
        _reject(OrchestratorRejectCode.SOURCE_ERROR, f"V5 replay: {exc}")
    _verify_replay(v5_result, "Q1_ROOT_V1_BASE_ADMISSION_RECEIPT_REPLAY_VERIFIED", "V5")

    rebind_module = _fresh_v6_rebind_bundle(repository, entries, head)
    try:
        rebind_obj = _call(rebind_module, V6_REBIND_SYMBOL)(
            v4_consumer_receipt=v4_wire,
            v5_admission_receipt=v5_wire,
            raw_q_one_g=v4_wire["raw_q_one_g"],
            source_body=v4_wire["source_body"],
            root_anchor=v4_wire["root_anchor"],
            source_state=v4_wire["source_state"],
            v1_state=v5_wire["v1_state"],
            role_grant=_grant(v6_registry, REBIND_ROLE),
        )
        v6_wire = _call(rebind_module, V6_REBIND_SERIALIZER)(rebind_obj)
    except Exception as exc:
        _reject(OrchestratorRejectCode.ROLE_ERROR, f"V6: {exc}")
    v6_wire = _mapping(v6_wire, "v6_rebind_receipt")

    binder = _fresh(repository, entries, BINDER_PATH, f"_t6_v6_source_binder_{head}")
    try:
        source_input_obj = _call(binder, BINDER_CANDIDATE_SYMBOL)(
            registry_context=context,
            v3_prefix_miss_receipt=production,
            v4_consumer_receipt=v4_wire,
            v5_base_admission_receipt=v5_wire,
            v6_rebind_receipt=v6_wire,
            role_grant=_grant(v6_registry, BINDER_ROLE),
        )
        source_input = _call(binder, BINDER_SERIALIZER)(source_input_obj)
        expected_external = _call(binder, BINDER_CANDIDATE_EXTERNAL)(source_input_obj)
    except Exception as exc:
        _reject(OrchestratorRejectCode.ROLE_ERROR, f"source binder: {exc}")
    source_input = _mapping(source_input, "source_input")
    expected_external = _mapping(expected_external, "expected_external_binding")

    prestate = _fresh(repository, entries, PRESTATE_PATH, f"_t6_v6_prestate_{head}")
    try:
        external_obj = _call(prestate, PRESTATE_BINDER)(
            v1_source_state_id=source_input["v1_source_state_id"],
            v1_source_wire_digest=source_input["v1_source_wire_digest"],
            source_prefix_receipt_digest=source_input["v3_prefix_miss_receipt_digest"],
            source_phase_root_preimage_digest=source_input["source_phase_root_preimage_digest"],
        )
        external_binding = _call(prestate, PRESTATE_SERIALIZER)(external_obj)
    except Exception as exc:
        _reject(OrchestratorRejectCode.SOURCE_ERROR, f"V2 external binding: {exc}")
    external_binding = _mapping(external_binding, "external_source_binding")
    if json.dumps(external_binding, sort_keys=True, separators=(",", ":")) != json.dumps(expected_external, sort_keys=True, separators=(",", ":")):
        _reject(OrchestratorRejectCode.SOURCE_ERROR, "V2 binding differs from binder projection")
    _check_output(source_input, external_binding)
    for path in (
        ORCHESTRATOR_PATH, V6_RESOLVER_PATH, V3_RESOLVER_PATH, V4_RESOLVER_PATH, V5_RESOLVER_PATH,
        V3_VERIFIER_PATH, V4_ORCHESTRATOR_PATH, V4_REPLAYER_PATH, V5_ORCHESTRATOR_PATH, V5_REPLAYER_PATH,
        V6_REBIND_PATH, BINDER_PATH, PRESTATE_PATH, STATE_PATH, ROOT_ENVELOPE_PATH,
    ):
        _blob(repository, entries, path)
    return {"source_input": source_input, "external_source_binding": external_binding}


__all__ = [
    "ExactHeadSourceInputOrchestratorError",
    "ORCHESTRATOR_ID",
    "OrchestratorRejectCode",
    "assemble_exact_head_q_one_actual_source_input_v1",
]
