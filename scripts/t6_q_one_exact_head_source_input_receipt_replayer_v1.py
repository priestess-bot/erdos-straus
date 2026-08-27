#!/usr/bin/env python3
"""Independent exact-HEAD replay for one non-authority source-input candidate.

This verifier deliberately imports neither the V6 source-input orchestrator nor
the V3 production issuer.  It validates the supplied V3 MISS, independently
replays the embedded V4 and V5 wires through their post-issuance verifiers,
rebuilds V6 directly, then reconstructs both the candidate wire and its
explicitly non-E1 V2 projection.  ``authority_verified`` appears only in this
runtime result, never in a serializable candidate wire.
"""

from __future__ import annotations

import copy
from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from types import ModuleType
from typing import Any, Mapping, NoReturn, Sequence


VERIFIER_ID = "q1_exact_head_source_input_receipt_replayer_v1"
VERIFIER_PATH = "scripts/t6_q_one_exact_head_source_input_receipt_replayer_v1.py"
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
V4_REPLAYER_PATH = "scripts/t6_q_one_root_prefix_scoped_e1_receipt_verifier_v2.py"
V4_REPLAYER_SYMBOL = "verify_q_one_root_prefix_scoped_e1_receipt_v2"
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
V3_REGISTRY_ID = "t6_coordinator_role_registry_v3"
V4_REGISTRY_ID = "t6_coordinator_role_registry_v4"
V5_REGISTRY_ID = "t6_coordinator_role_registry_v5"
V6_REGISTRY_ID = "t6_coordinator_role_registry_v6"
BINDER_ROLE = "EXACT_HEAD_Q1_ACTUAL_SOURCE_INPUT_BINDER"
REBIND_ROLE = "INDEPENDENT_Q1_ROOT_SOURCE_SCOPED_E1_REBINDER"
REGULAR_MODES = frozenset({"100644", "100755"})
OID_RE = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
PATH_RE = re.compile(r"[A-Za-z0-9._/-]+\Z")


class ReceiptReplayRejectCode(str, Enum):
    INVALID_ROOT = "INVALID_ROOT"
    INVALID_HEAD = "INVALID_HEAD"
    HEAD_BINDING_ERROR = "HEAD_BINDING_ERROR"
    WORKTREE_BINDING_ERROR = "WORKTREE_BINDING_ERROR"
    MODULE_BINDING_ERROR = "MODULE_BINDING_ERROR"
    REGISTRY_ERROR = "REGISTRY_ERROR"
    V3_RECEIPT_ERROR = "V3_RECEIPT_ERROR"
    TERMINAL_SOURCE_NOT_MISS = "TERMINAL_SOURCE_NOT_MISS"
    RECEIPT_TYPE_ERROR = "RECEIPT_TYPE_ERROR"
    WIRE_MISMATCH = "WIRE_MISMATCH"
    SOURCE_MISMATCH = "SOURCE_MISMATCH"
    AUTHORITY_MISMATCH = "AUTHORITY_MISMATCH"


class ExactHeadSourceInputReceiptReplayError(ValueError):
    def __init__(self, code: ReceiptReplayRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: ReceiptReplayRejectCode, detail: str) -> NoReturn:
    raise ExactHeadSourceInputReceiptReplayError(code, detail)


def _copy_json(value: Any, *, path: str = "$") -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(ReceiptReplayRejectCode.RECEIPT_TYPE_ERROR, f"{path} non-string key")
            result[key] = _copy_json(child, path=f"{path}.{key}")
        return result
    if type(value) is list:
        return [_copy_json(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(ReceiptReplayRejectCode.RECEIPT_TYPE_ERROR, f"{path} contains {type(value).__name__}")


def _mapping(value: Any, name: str) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(ReceiptReplayRejectCode.RECEIPT_TYPE_ERROR, f"{name} must be an exact dict")
    return _copy_json(value, path=name)


def _canonical(value: Any) -> str:
    return json.dumps(_copy_json(value), ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _run_git(root: Path, args: Sequence[str]) -> bytes:
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(["git", *args], cwd=root, capture_output=True, check=False, env=env)
    if completed.returncode:
        _reject(ReceiptReplayRejectCode.HEAD_BINDING_ERROR, completed.stderr.decode(errors="replace").strip())
    return completed.stdout


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
        _reject(ReceiptReplayRejectCode.INVALID_ROOT, "exact platform Path required")
    try:
        return Path(_run_git(locator.resolve(), ("rev-parse", "--show-toplevel")).decode().strip()).resolve()
    except (OSError, UnicodeDecodeError) as exc:
        raise ExactHeadSourceInputReceiptReplayError(ReceiptReplayRejectCode.INVALID_ROOT, str(exc)) from exc


def _exact_head(root: Path, requested_head: str) -> tuple[str, str]:
    fmt = _run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    size = 40 if fmt == "sha1" else 64 if fmt == "sha256" else 0
    if type(requested_head) is not str or len(requested_head) != size or OID_RE.fullmatch(requested_head) is None:
        _reject(ReceiptReplayRejectCode.INVALID_HEAD, "full lowercase commit ID required")
    if _run_git(root, ("cat-file", "-t", requested_head)).decode().strip() != "commit":
        _reject(ReceiptReplayRejectCode.INVALID_HEAD, "not a commit")
    if _run_git(root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}")).decode().strip() != requested_head:
        _reject(ReceiptReplayRejectCode.INVALID_HEAD, "resolution drift")
    return requested_head, _run_git(root, ("rev-parse", f"{requested_head}^{{tree}}")).decode().strip()


def _entries(root: Path, head: str) -> dict[str, tuple[str, str, str]]:
    result: dict[str, tuple[str, str, str]] = {}
    for record in _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head)).split(b"\0"):
        if not record:
            continue
        try:
            metadata, raw_path = record.split(b"\t", 1)
            mode, kind, object_id = metadata.decode("ascii").split(" ")
            path = raw_path.decode("utf-8")
        except (UnicodeDecodeError, ValueError) as exc:
            raise ExactHeadSourceInputReceiptReplayError(ReceiptReplayRejectCode.HEAD_BINDING_ERROR, repr(record)) from exc
        pure = PurePosixPath(path)
        if not path or pure.is_absolute() or path != pure.as_posix() or "\\" in path or any(part in {"", ".", ".."} for part in pure.parts) or path in result:
            _reject(ReceiptReplayRejectCode.HEAD_BINDING_ERROR, f"unsafe tree path {path!r}")
        result[path] = (mode, kind, object_id)
    return result


def _blob(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str) -> bytes:
    pure = PurePosixPath(path) if type(path) is str else PurePosixPath(".")
    if type(path) is not str or PATH_RE.fullmatch(path) is None or pure.is_absolute() or path != pure.as_posix() or "\\" in path or any(part in {"", ".", ".."} for part in pure.parts):
        _reject(ReceiptReplayRejectCode.MODULE_BINDING_ERROR, f"unsafe path {path!r}")
    entry = entries.get(path)
    if entry is None or entry[0] not in REGULAR_MODES or entry[1] != "blob":
        _reject(ReceiptReplayRejectCode.MODULE_BINDING_ERROR, f"missing regular blob {path}")
    content = _run_git(root, ("cat-file", "blob", entry[2]))
    worktree = root / path
    if worktree.is_symlink() or not worktree.is_file() or worktree.read_bytes() != content:
        _reject(ReceiptReplayRejectCode.WORKTREE_BINDING_ERROR, path)
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
        raise ExactHeadSourceInputReceiptReplayError(ReceiptReplayRejectCode.MODULE_BINDING_ERROR, f"{path}: {exc}") from exc
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
        (f"_t6_v6_rebind_replay_{head}", V6_REBIND_PATH),
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
                raise ExactHeadSourceInputReceiptReplayError(ReceiptReplayRejectCode.MODULE_BINDING_ERROR, f"{path}: {exc}") from exc
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
        _reject(ReceiptReplayRejectCode.MODULE_BINDING_ERROR, f"missing exact callable {symbol}")
    return value


def _resolved_registry(module: ModuleType, symbol: str, *, root: Path, head: str, tree: str, expected_status: str) -> dict[str, Any]:
    try:
        with _sanitized_git_environment():
            result = _call(module, symbol)(root=root, requested_head=head)
    except Exception as exc:
        _reject(ReceiptReplayRejectCode.REGISTRY_ERROR, str(exc))
    if type(result) is not dict or result.get("head_sha") != head or result.get("head_tree_sha") != tree or result.get("status") != expected_status:
        _reject(ReceiptReplayRejectCode.REGISTRY_ERROR, "registry HEAD/status")
    return _copy_json(result)


def _grant(registry: Mapping[str, Any], role: str) -> dict[str, Any]:
    grants = registry.get("resolved_role_grants")
    found = [item for item in grants if type(item) is dict and item.get("role") == role] if type(grants) is list else []
    if len(found) != 1 or type(found[0].get("grant_wire")) is not dict:
        _reject(ReceiptReplayRejectCode.REGISTRY_ERROR, f"V6 grant {role}")
    return _copy_json(found[0]["grant_wire"])


def _context(v3: Mapping[str, Any], v4: Mapping[str, Any], v5: Mapping[str, Any], v6: Mapping[str, Any]) -> dict[str, Any]:
    manifest_v6 = v6.get("role_authority_manifest")
    crosses = v6.get("cross_registries")
    if type(manifest_v6) is not dict or type(manifest_v6.get("digest")) is not str or type(crosses) is not dict:
        _reject(ReceiptReplayRejectCode.REGISTRY_ERROR, "V6 manifest")
    rows = {"v3": v3, "v4": v4, "v5": v5}
    identities = {"v3": V3_REGISTRY_ID, "v4": V4_REGISTRY_ID, "v5": V5_REGISTRY_ID}
    out: dict[str, Any] = {"head_sha": v6["head_sha"], "head_tree_sha": v6["head_tree_sha"], "registries": {}}
    for name, registry in rows.items():
        manifest = registry.get("role_authority_manifest")
        cross = crosses.get(name)
        if type(manifest) is not dict or type(cross) is not dict or cross.get("registry_digest") != registry.get("registry_digest") or cross.get("role_manifest_digest") != manifest.get("digest"):
            _reject(ReceiptReplayRejectCode.REGISTRY_ERROR, f"V6 {name} cross binding")
        out["registries"][name] = {"registry_id": identities[name], "registry_digest": registry["registry_digest"], "role_manifest_digest": manifest["digest"]}
    out["registries"]["v6"] = {"registry_id": V6_REGISTRY_ID, "registry_digest": v6["registry_digest"], "role_manifest_digest": manifest_v6["digest"]}
    return out


@dataclass(frozen=True, slots=True)
class ExactHeadQOneSourceInputReplayResultV1:
    status: str
    receipt_id: str
    receipt_digest: str
    external_binding_id: str
    external_binding_digest: str
    root_context: int
    wire_match: bool
    authority_verified: bool


def verify_exact_head_q_one_actual_source_input_v1(
    *, root: Path, requested_head: str, raw_q_one_g: dict[str, Any], production_miss_receipt: dict[str, Any], source_input: dict[str, Any], external_source_binding: dict[str, Any]
) -> ExactHeadQOneSourceInputReplayResultV1:
    """Rebuild one exact source-input wire without an issuer or orchestrator."""

    repository = _repository(root)
    head, tree = _exact_head(repository, requested_head)
    entries = _entries(repository, head)
    own = _blob(repository, entries, VERIFIER_PATH)
    local = Path(__file__)
    if local.is_symlink() or not local.is_file() or local.resolve() != (repository / VERIFIER_PATH).resolve() or local.read_bytes() != own:
        _reject(ReceiptReplayRejectCode.WORKTREE_BINDING_ERROR, VERIFIER_PATH)
    raw = _mapping(raw_q_one_g, "raw_q_one_g")
    production = _mapping(production_miss_receipt, "production_miss_receipt")
    supplied = _mapping(source_input, "source_input")
    supplied_external = _mapping(external_source_binding, "external_source_binding")

    v3_registry = _resolved_registry(_fresh(repository, entries, V3_RESOLVER_PATH, f"_t6_v6r_v3_{head}"), V3_RESOLVER_SYMBOL, root=repository, head=head, tree=tree, expected_status=V3_STATUS)
    v4_registry = _resolved_registry(_fresh(repository, entries, V4_RESOLVER_PATH, f"_t6_v6r_v4_{head}"), V4_RESOLVER_SYMBOL, root=repository, head=head, tree=tree, expected_status=V4_STATUS)
    v5_registry = _resolved_registry(_fresh(repository, entries, V5_RESOLVER_PATH, f"_t6_v6r_v5_{head}"), V5_RESOLVER_SYMBOL, root=repository, head=head, tree=tree, expected_status=V5_STATUS)
    v6_registry = _resolved_registry(_fresh(repository, entries, V6_RESOLVER_PATH, f"_t6_v6r_v6_{head}"), V6_RESOLVER_SYMBOL, root=repository, head=head, tree=tree, expected_status=V6_STATUS)
    context = _context(v3_registry, v4_registry, v5_registry, v6_registry)

    if (
        supplied.get("receipt_type") != "EXACT_HEAD_Q_ONE_ACTUAL_SOURCE_INPUT_V1"
        or supplied.get("status") != "EXACT_HEAD_Q1_SOURCE_INPUT_REPLAY_CANDIDATE_NONAUTHORITY"
        or supplied.get("binding_scope") != "EXACT_HEAD_Q1_ROOT_SOURCE_INPUT_REPLAY_CANDIDATE_NOT_E1"
    ):
        _reject(ReceiptReplayRejectCode.RECEIPT_TYPE_ERROR, "candidate wire identity")
    for required in (
        "v3_prefix_miss_receipt", "v4_consumer_receipt", "v5_base_admission_receipt",
        "v6_rebind_receipt", "head_sha", "head_tree_sha", "v3_registry_id",
        "v3_registry_digest", "v3_role_manifest_digest", "v4_registry_id",
        "v4_registry_digest", "v4_role_manifest_digest", "v5_registry_id",
        "v5_registry_digest", "v5_role_manifest_digest", "v6_registry_id",
        "v6_registry_digest", "v6_role_manifest_digest",
    ):
        if required not in supplied:
            _reject(ReceiptReplayRejectCode.RECEIPT_TYPE_ERROR, f"source-input missing {required}")
    input_wire = supplied
    if input_wire.get("head_sha") != head or input_wire.get("head_tree_sha") != tree or _canonical({"head_sha": input_wire["head_sha"], "head_tree_sha": input_wire["head_tree_sha"], "registries": {"v3": {"registry_id": input_wire["v3_registry_id"], "registry_digest": input_wire["v3_registry_digest"], "role_manifest_digest": input_wire["v3_role_manifest_digest"]}, "v4": {"registry_id": input_wire["v4_registry_id"], "registry_digest": input_wire["v4_registry_digest"], "role_manifest_digest": input_wire["v4_role_manifest_digest"]}, "v5": {"registry_id": input_wire["v5_registry_id"], "registry_digest": input_wire["v5_registry_digest"], "role_manifest_digest": input_wire["v5_role_manifest_digest"]}, "v6": {"registry_id": input_wire["v6_registry_id"], "registry_digest": input_wire["v6_registry_digest"], "role_manifest_digest": input_wire["v6_role_manifest_digest"]}}}) != _canonical(context):
        _reject(ReceiptReplayRejectCode.REGISTRY_ERROR, "source-input registry context")
    if input_wire["v3_prefix_miss_receipt"] != production:
        _reject(ReceiptReplayRejectCode.SOURCE_MISMATCH, "source-input V3 wire")
    # Candidate wires are never accepted by the public parser.  Rebuild one
    # only after V3--V6 have been independently replayed below.
    binder = _fresh(repository, entries, BINDER_PATH, f"_t6_v6r_binder_{head}")

    v3_verifier = _fresh(repository, entries, V3_VERIFIER_PATH, f"_t6_v6r_v3_replay_{head}")
    try:
        with _sanitized_git_environment():
            v3_result = _call(v3_verifier, V3_VERIFIER_SYMBOL)(root=repository, requested_head=head, raw_q_one_g=raw, receipt=production)
    except Exception as exc:
        _reject(ReceiptReplayRejectCode.V3_RECEIPT_ERROR, str(exc))
    if getattr(v3_result, "status", None) != "PRODUCTION_Q1_TERMINAL_RECEIPT_VERIFIED" or getattr(v3_result, "receipt_type", None) != V3_MISS_TYPE or getattr(v3_result, "outcome", None) != V3_MISS_OUTCOME:
        _reject(ReceiptReplayRejectCode.TERMINAL_SOURCE_NOT_MISS, "V3 prefix MISS required")

    v4_wire = _mapping(input_wire["v4_consumer_receipt"], "V4 receipt")
    v4_replayer = _fresh(repository, entries, V4_REPLAYER_PATH, f"_t6_v6r_v4_replay_{head}")
    try:
        with _sanitized_git_environment():
            v4_result = _call(v4_replayer, V4_REPLAYER_SYMBOL)(root=repository, requested_head=head, raw_q_one_g=raw, production_miss_receipt=production, receipt=v4_wire)
    except Exception as exc:
        _reject(ReceiptReplayRejectCode.SOURCE_MISMATCH, f"V4 replay: {exc}")
    if getattr(v4_result, "status", None) != "Q1_ROOT_PREFIX_SCOPED_E1_RECEIPT_REPLAY_VERIFIED" or getattr(v4_result, "wire_match", None) is not True or getattr(v4_result, "authority_verified", None) is not True:
        _reject(ReceiptReplayRejectCode.SOURCE_MISMATCH, "V4 replay result")

    v5_wire = _mapping(input_wire["v5_base_admission_receipt"], "V5 receipt")
    v5_replayer = _fresh(repository, entries, V5_REPLAYER_PATH, f"_t6_v6r_v5_replay_{head}")
    try:
        with _sanitized_git_environment():
            v5_result = _call(v5_replayer, V5_REPLAYER_SYMBOL)(root=repository, requested_head=head, raw_q_one_g=raw, production_miss_receipt=production, receipt=v5_wire)
    except Exception as exc:
        _reject(ReceiptReplayRejectCode.SOURCE_MISMATCH, f"V5 replay: {exc}")
    if getattr(v5_result, "status", None) != "Q1_ROOT_V1_BASE_ADMISSION_RECEIPT_REPLAY_VERIFIED" or getattr(v5_result, "wire_match", None) is not True or getattr(v5_result, "authority_verified", None) is not True:
        _reject(ReceiptReplayRejectCode.SOURCE_MISMATCH, "V5 replay result")

    rebind = _fresh_v6_rebind_bundle(repository, entries, head)
    try:
        v6_obj = _call(rebind, V6_REBIND_SYMBOL)(
            v4_consumer_receipt=v4_wire,
            v5_admission_receipt=v5_wire,
            raw_q_one_g=v4_wire["raw_q_one_g"],
            source_body=v4_wire["source_body"],
            root_anchor=v4_wire["root_anchor"],
            source_state=v4_wire["source_state"],
            v1_state=v5_wire["v1_state"],
            role_grant=_grant(v6_registry, REBIND_ROLE),
        )
        expected_v6 = _call(rebind, V6_REBIND_SERIALIZER)(v6_obj)
    except Exception as exc:
        _reject(ReceiptReplayRejectCode.SOURCE_MISMATCH, f"V6 replay: {exc}")
    if _canonical(expected_v6) != _canonical(input_wire["v6_rebind_receipt"]):
        _reject(ReceiptReplayRejectCode.WIRE_MISMATCH, "V6 rebind wire")

    try:
        expected_input_obj = _call(binder, BINDER_CANDIDATE_SYMBOL)(
            registry_context=context,
            v3_prefix_miss_receipt=production,
            v4_consumer_receipt=v4_wire,
            v5_base_admission_receipt=v5_wire,
            v6_rebind_receipt=expected_v6,
            role_grant=_grant(v6_registry, BINDER_ROLE),
        )
        expected_input = _call(binder, BINDER_SERIALIZER)(expected_input_obj)
        expected_external = _call(binder, BINDER_CANDIDATE_EXTERNAL)(expected_input_obj)
    except Exception as exc:
        _reject(ReceiptReplayRejectCode.SOURCE_MISMATCH, f"source-input rebuild: {exc}")
    if _canonical(expected_input) != _canonical(supplied):
        _reject(ReceiptReplayRejectCode.WIRE_MISMATCH, "source-input wire")

    prestate = _fresh(repository, entries, PRESTATE_PATH, f"_t6_v6r_prestate_{head}")
    try:
        external_obj = _call(prestate, PRESTATE_BINDER)(
            v1_source_state_id=expected_input["v1_source_state_id"],
            v1_source_wire_digest=expected_input["v1_source_wire_digest"],
            source_prefix_receipt_digest=expected_input["v3_prefix_miss_receipt_digest"],
            source_phase_root_preimage_digest=expected_input["source_phase_root_preimage_digest"],
        )
        actual_external = _call(prestate, PRESTATE_SERIALIZER)(external_obj)
    except Exception as exc:
        _reject(ReceiptReplayRejectCode.SOURCE_MISMATCH, f"V2 projection: {exc}")
    if _canonical(expected_external) != _canonical(actual_external) or _canonical(actual_external) != _canonical(supplied_external):
        _reject(ReceiptReplayRejectCode.WIRE_MISMATCH, "ExternalQOneSourceBindingV2 wire")
    for name in ("source_actualness_input", "v1_base_admission_evidence", "v6_rebind_evidence", "generic_e1", "successor_e1", "e1_authority", "producer_authority", "branch_authority", "admission_authority", "queue_authority", "enqueue_authority", "e2_authority", "e3_authority", "e4_authority", "e5_authority", "t5_authority", "reentry_authority", "global_exhaustion"):
        if type(expected_input.get(name)) is not bool or expected_input[name] is not False:
            _reject(ReceiptReplayRejectCode.AUTHORITY_MISMATCH, name)
    for path in (
        VERIFIER_PATH, V6_RESOLVER_PATH, V3_RESOLVER_PATH, V4_RESOLVER_PATH, V5_RESOLVER_PATH,
        V3_VERIFIER_PATH, V4_REPLAYER_PATH, V5_REPLAYER_PATH, V6_REBIND_PATH, BINDER_PATH,
        PRESTATE_PATH, STATE_PATH, ROOT_ENVELOPE_PATH,
    ):
        _blob(repository, entries, path)
    return ExactHeadQOneSourceInputReplayResultV1(
        status="EXACT_HEAD_Q_ONE_SOURCE_INPUT_CANDIDATE_REPLAY_VERIFIED",
        receipt_id=expected_input["receipt_id"],
        receipt_digest=expected_input["digest"],
        external_binding_id=actual_external["source_binding_id"],
        external_binding_digest=actual_external["digest"],
        root_context=expected_input["v3_prefix_miss_receipt"]["root_context"],
        wire_match=True,
        authority_verified=True,
    )


__all__ = [
    "ExactHeadSourceInputReceiptReplayError",
    "ExactHeadQOneSourceInputReplayResultV1",
    "ReceiptReplayRejectCode",
    "VERIFIER_ID",
    "verify_exact_head_q_one_actual_source_input_v1",
]
