#!/usr/bin/env python3
"""Exact-HEAD orchestrator for the q=1 root prefix-scoped E1 roles.

This is the only controlled-loader component in the V4 role layer.  It binds
the requested commit and worktree, fresh-executes the V4 resolver, the V3
production receipt verifier, the root initializer, and the three loader-free
roles, and returns the consumer's serialized receipt.  Owner, validation, and
authority mappings are always derived internally; callers may provide only a
repository locator, an exact HEAD, raw q=1 G integers, and the V3 production
receipt.

The returned receipt is still scoped evidence.  This module does not issue a
generic transition, producer continuation, queue admission, or E2--E5 ticket.
"""

from __future__ import annotations

import copy
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


ORCHESTRATOR_ID = "q1_root_prefix_scoped_e1_orchestrator_v2"
ORCHESTRATOR_PATH = "scripts/t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py"
V4_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v4.py"
V4_RESOLVER_SYMBOL = "resolve_registry_v4"
V3_VERIFIER_PATH = "scripts/t6_q_one_terminal_receipt_verifier_v1.py"
V3_VERIFIER_SYMBOL = "verify_q_one_production_terminal_receipt_v1"
V3_RESOLVER_PATH = "scripts/t6_coordinator_role_registry_v3.py"
ROOT_INITIALIZER_PATH = "scripts/t6_q_one_root_initializer_envelope_v2.py"
OWNER_PATH = "scripts/t6_q_one_root_owner_classifier_v2.py"
OWNER_SYMBOL = "classify_q_one_root_owner_v2"
OWNER_SERIALIZER = "root_owner_receipt_to_mapping_v2"
VALIDATOR_PATH = "scripts/t6_q_one_scope_aware_e1_validator_v2.py"
VALIDATOR_SYMBOL = "validate_q_one_registered_prefix_e1_scope_v2"
VALIDATOR_SERIALIZER = "scope_validation_receipt_to_mapping_v2"
CONSUMER_PATH = "scripts/t6_q_one_registered_prefix_e1_consumer_v2.py"
CONSUMER_SYMBOL = "consume_q_one_registered_prefix_miss_for_e1_v2"
CONSUMER_SERIALIZER = "root_source_scoped_e1_receipt_to_mapping_v2"

ROLE_OWNER = "COMMON_ROOT_OWNER_CLASSIFIER"
ROLE_VALIDATOR = "INDEPENDENT_SCOPE_AWARE_E1_VALIDATOR"
ROLE_CONSUMER = "REGISTERED_PREFIX_E1_CONSUMER"
OWNER_ARTIFACT_ID = "q1_root_owner_classifier_v2"
VALIDATOR_ARTIFACT_ID = "q1_scope_aware_e1_validator_v2"
CONSUMER_ARTIFACT_ID = "q1_registered_prefix_e1_consumer_v2"
OWNER_GRANT_ID = "q1_common_root_owner_classifier_grant_v4"
VALIDATOR_GRANT_ID = "q1_scope_aware_e1_validator_grant_v4"
CONSUMER_GRANT_ID = "q1_registered_prefix_e1_consumer_grant_v4"
ROOT_INITIALIZER_ARTIFACT_ID = "v3_root_initializer_dependency"
V3_VERIFIER_ARTIFACT_ID = "v3_production_receipt_verifier_dependency"

V4_STATUS = "HEAD_BOUND_Q1_ROOT_PREFIX_SCOPED_E1_AUTHORITY_NO_SUCCESSOR_OR_RECURSION"
V3_STATUS = "HEAD_BOUND_Q1_ROOT_TERMINAL_DECISION_AUTHORITY_NO_RECURSION"
V3_MISS_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
V3_MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"
V4_SCOPE_ID = "q1_root_after_gap_3_7_11_registered_prefix_v1"
V4_SCOPE_GAPS = (3, 7, 11)
V4_SCOPE_NEXT = 15

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
    ROLE_GRANT_ERROR = "ROLE_GRANT_ERROR"
    SOURCE_ERROR = "SOURCE_ERROR"
    TERMINAL_SOURCE_NOT_MISS = "TERMINAL_SOURCE_NOT_MISS"
    ROLE_ERROR = "ROLE_ERROR"
    AUTHORITY_ERROR = "AUTHORITY_ERROR"
    MALFORMED_INPUT = "MALFORMED_INPUT"


class OrchestratorError(ValueError):
    def __init__(self, code: OrchestratorRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: OrchestratorRejectCode, detail: str) -> NoReturn:
    raise OrchestratorError(code, detail)


def _json_copy(value: Any, *, path: str = "$") -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(OrchestratorRejectCode.MALFORMED_INPUT, f"{path} key is not a string")
            result[key] = _json_copy(child, path=f"{path}.{key}")
        return result
    if type(value) is list:
        return [_json_copy(child, path=f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(OrchestratorRejectCode.MALFORMED_INPUT, f"{path} contains {type(value).__name__}")


def _run_git(root: Path, args: Sequence[str]) -> bytes:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(
        ["git", *args], cwd=root, check=False, capture_output=True, env=environment
    )
    if completed.returncode:
        _reject(
            OrchestratorRejectCode.HEAD_BINDING_ERROR,
            f"git {' '.join(args)} failed: {completed.stderr.decode(errors='replace').strip()}",
        )
    return completed.stdout


def _repository_root(locator: Path) -> Path:
    if type(locator) is not type(Path()):
        _reject(OrchestratorRejectCode.INVALID_ROOT, "root must be the exact platform Path type")
    try:
        return Path(_run_git(locator.resolve(), ("rev-parse", "--show-toplevel")).decode().strip()).resolve()
    except (UnicodeDecodeError, OSError) as exc:
        raise OrchestratorError(OrchestratorRejectCode.INVALID_ROOT, str(exc)) from exc


def _exact_head(root: Path, requested_head: str) -> tuple[str, str]:
    fmt = _run_git(root, ("rev-parse", "--show-object-format")).decode().strip()
    length = 40 if fmt == "sha1" else 64 if fmt == "sha256" else 0
    if type(requested_head) is not str or len(requested_head) != length or not OID_RE.fullmatch(requested_head):
        _reject(OrchestratorRejectCode.INVALID_HEAD, "requested_head must be a full lowercase commit ID")
    if _run_git(root, ("cat-file", "-t", requested_head)).decode().strip() != "commit":
        _reject(OrchestratorRejectCode.INVALID_HEAD, "requested object is not a commit")
    resolved = _run_git(root, ("rev-parse", "--verify", f"{requested_head}^{{commit}}"))
    if resolved.decode().strip() != requested_head:
        _reject(OrchestratorRejectCode.INVALID_HEAD, "commit resolution changed")
    tree = _run_git(root, ("rev-parse", f"{requested_head}^{{tree}}")).decode().strip()
    return requested_head, tree


def _tree_entries(root: Path, head: str) -> dict[str, tuple[str, str, str]]:
    raw = _run_git(root, ("ls-tree", "-r", "-z", "--full-tree", head))
    result: dict[str, tuple[str, str, str]] = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, encoded = record.split(b"\t", 1)
        mode, kind, object_id = metadata.decode("ascii").split(" ")
        path = encoded.decode("utf-8")
        pure = PurePosixPath(path)
        if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
            _reject(OrchestratorRejectCode.HEAD_BINDING_ERROR, f"unsafe tree path {path!r}")
        if path in result:
            _reject(OrchestratorRejectCode.HEAD_BINDING_ERROR, f"duplicate tree path {path!r}")
        result[path] = (mode, kind, object_id)
    return result


def _blob(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str) -> bytes:
    if type(path) is not str or PATH_RE.fullmatch(path) is None:
        _reject(OrchestratorRejectCode.MODULE_BINDING_ERROR, f"unsafe path {path!r}")
    entry = entries.get(path)
    if entry is None or entry[0] not in REGULAR_MODES or entry[1] != "blob":
        _reject(OrchestratorRejectCode.MODULE_BINDING_ERROR, f"missing regular blob {path}")
    content = _run_git(root, ("cat-file", "blob", entry[2]))
    worktree = root / path
    if worktree.is_symlink() or not worktree.is_file() or worktree.read_bytes() != content:
        _reject(OrchestratorRejectCode.WORKTREE_BINDING_ERROR, path)
    return content


def _fresh_module(root: Path, entries: Mapping[str, tuple[str, str, str]], path: str, name: str) -> ModuleType:
    content = _blob(root, entries, path)
    module = ModuleType(name)
    module.__file__ = str((root / path).resolve())
    previous = sys.modules.get(name)
    sys.modules[name] = module
    try:
        exec(compile(content, module.__file__, "exec"), module.__dict__)
    except Exception as exc:
        raise OrchestratorError(OrchestratorRejectCode.MODULE_BINDING_ERROR, f"fresh {path}: {exc}") from exc
    finally:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous
    return module


def _require_callable(module: ModuleType, symbol: str) -> Any:
    value = getattr(module, symbol, None)
    if not callable(value) or getattr(value, "__name__", None) != symbol or getattr(value, "__module__", None) != module.__name__:
        _reject(OrchestratorRejectCode.MODULE_BINDING_ERROR, f"missing exact callable {symbol}")
    return value


def _canonical_digest(value: Any) -> str:
    try:
        encoded = json.dumps(_json_copy(value), ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("ascii")
    except (TypeError, ValueError) as exc:
        _reject(OrchestratorRejectCode.MALFORMED_INPUT, str(exc))
    return hashlib.sha256(encoded).hexdigest()


def _resolved_grants(resolved: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    if type(resolved) is not dict:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, "resolved V4 output must be an exact dict")
    if resolved.get("status") != V4_STATUS or resolved.get("authorized_branches") != []:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, "V4 status or branch boundary changed")
    if resolved.get("new_role_grant_count") != 3 or resolved.get("effective_role_capability_count") != 7:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, "V4 role counts changed")
    grants = resolved.get("resolved_role_grants")
    if type(grants) is not list or len(grants) != 3:
        _reject(OrchestratorRejectCode.ROLE_GRANT_ERROR, "V4 must resolve exactly three new grants")
    by_role: dict[str, dict[str, Any]] = {}
    expected = {
        ROLE_OWNER: (
            OWNER_GRANT_ID,
            OWNER_ARTIFACT_ID,
            OWNER_PATH,
            [OWNER_SYMBOL, OWNER_SERIALIZER],
            ["CLASSIFY_COMMON_Q1_ROOT_OWNER"],
        ),
        ROLE_VALIDATOR: (
            VALIDATOR_GRANT_ID,
            VALIDATOR_ARTIFACT_ID,
            VALIDATOR_PATH,
            [VALIDATOR_SYMBOL, VALIDATOR_SERIALIZER],
            ["VALIDATE_REGISTERED_PREFIX_ROOT_SOURCE_E1_SCOPE"],
        ),
        ROLE_CONSUMER: (
            CONSUMER_GRANT_ID,
            CONSUMER_ARTIFACT_ID,
            CONSUMER_PATH,
            [CONSUMER_SYMBOL, CONSUMER_SERIALIZER],
            ["ISSUE_REGISTERED_PREFIX_ROOT_SOURCE_SCOPED_E1"],
        ),
    }
    artifacts = resolved.get("resolved_artifacts")
    if type(artifacts) is not list:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, "V4 resolved artifacts are missing")
    artifact_map = {item.get("artifact_id"): item for item in artifacts if type(item) is dict}
    for item in grants:
        if type(item) is not dict or item.get("role") not in expected or item["role"] in by_role:
            _reject(OrchestratorRejectCode.ROLE_GRANT_ERROR, "V4 grant role set changed")
        grant_id, artifact_id, expected_path, expected_symbols, expected_capabilities = expected[item["role"]]
        wire = item.get("grant_wire")
        if type(wire) is not dict or wire.get("grant_id") != grant_id or wire.get("role") != item["role"] or wire.get("artifact_id") != artifact_id:
            _reject(OrchestratorRejectCode.ROLE_GRANT_ERROR, f"grant wire mismatch for {item['role']}")
        required = {"grant_id", "role", "artifact_id", "artifact_path", "artifact_symbols", "capabilities", "authority_class", "artifact_semantic_sha256"}
        artifact = artifact_map.get(artifact_id)
        if artifact is None:
            _reject(OrchestratorRejectCode.REGISTRY_ERROR, f"artifact {artifact_id} is missing")
        if (
            set(wire) != required
            or wire.get("authority_class") != "HEAD_BOUND_EXECUTABLE_CAPABILITY_V4"
            or wire.get("artifact_path") != expected_path
            or wire.get("artifact_symbols") != expected_symbols
            or wire.get("capabilities") != expected_capabilities
            or wire.get("artifact_semantic_sha256") != artifact.get("semantic_sha256")
        ):
            _reject(OrchestratorRejectCode.ROLE_GRANT_ERROR, f"grant wire fields changed for {item['role']}")
        by_role[item["role"]] = _json_copy(wire)
    if set(by_role) != set(expected):
        _reject(OrchestratorRejectCode.ROLE_GRANT_ERROR, "V4 grant roles incomplete")
    scope = resolved.get("authorized_consumer_scopes")
    expected_scope = {
        "scope_id": V4_SCOPE_ID, "owner_domain_id": "ordinary_parentless_q1_g_root_v1", "owner": "type_ii_relation_g_endpoint",
        "owner_scope": "ROOT_SOURCE_DISPATCH_ONLY", "source_terminal_outcome": V3_MISS_OUTCOME, "coverage_semantics": "REGISTERED_PRIORITY_ONLY",
        "ordered_gaps": list(V4_SCOPE_GAPS), "next_unchecked_gap": V4_SCOPE_NEXT, "global_exhaustion": False,
        "remaining_domain_unchecked": True, "same_head_consumption_required": True,
    }
    if scope != [expected_scope]:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, "V4 consumer scope changed")
    denials = resolved.get("authority_denials")
    if type(denials) is not dict or any(value is not False for value in denials.values()):
        _reject(OrchestratorRejectCode.AUTHORITY_ERROR, "V4 authority denials changed")
    return by_role


def _verify_v3_result(result: Any, *, head: str, receipt: Mapping[str, Any]) -> None:
    if getattr(result, "status", None) != "PRODUCTION_Q1_TERMINAL_RECEIPT_VERIFIED":
        _reject(OrchestratorRejectCode.V3_RECEIPT_ERROR, "V3 production receipt was not independently verified")
    if getattr(result, "receipt_type", None) != V3_MISS_TYPE or getattr(result, "outcome", None) != V3_MISS_OUTCOME:
        _reject(OrchestratorRejectCode.TERMINAL_SOURCE_NOT_MISS, "only a registered-prefix MISS may feed V4 E1")
    if receipt.get("head_sha") != head or receipt.get("receipt_type") != V3_MISS_TYPE or receipt.get("outcome") != V3_MISS_OUTCOME:
        _reject(OrchestratorRejectCode.TERMINAL_SOURCE_NOT_MISS, "production receipt HEAD/outcome mismatch")


def _authority_check(receipt: Mapping[str, Any]) -> None:
    if type(receipt) is not dict:
        _reject(OrchestratorRejectCode.ROLE_ERROR, "consumer serializer did not return an exact dict")
    for name, expected in {
        "source_actualness": True,
        "common_owner_authority": True,
        "registered_prefix_miss_authority": True,
        "scope_validation_authority": True,
        "root_source_scoped_e1": True,
        "scope_aware_consumer_authority": True,
        "root_source_occurrence_authority": True,
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
        "terminal_receipt_direct_continuation_authority": False,
    }.items():
        if type(receipt.get(name)) is not bool or receipt.get(name) is not expected:
            _reject(OrchestratorRejectCode.AUTHORITY_ERROR, f"consumer.{name} is not {expected!r}")


def assemble_q_one_root_prefix_scoped_e1_v2(
    *, root: Path, requested_head: str, raw_q_one_g: dict[str, Any], production_miss_receipt: dict[str, Any]
) -> dict[str, Any]:
    """Assemble and return one exact-HEAD root-source-scoped E1 receipt."""
    repository = _repository_root(root)
    head, tree = _exact_head(repository, requested_head)
    entries = _tree_entries(repository, head)
    # The running orchestrator is checked before it is allowed to load any role.
    own_blob = _blob(repository, entries, ORCHESTRATOR_PATH)
    expected_orchestrator_path = (repository / ORCHESTRATOR_PATH).resolve()
    if (
        Path(__file__).is_symlink()
        or Path(__file__).resolve() != expected_orchestrator_path
        or Path(__file__).read_bytes() != own_blob
    ):
        _reject(OrchestratorRejectCode.WORKTREE_BINDING_ERROR, "orchestrator is not backed by requested HEAD")

    v4 = _fresh_module(repository, entries, V4_RESOLVER_PATH, f"_t6_v4_resolver_{head}")
    resolve_v4 = _require_callable(v4, V4_RESOLVER_SYMBOL)
    try:
        resolved = resolve_v4(root=repository, requested_head=head)
    except Exception as exc:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, f"V4 resolver rejected HEAD: {exc}")
    if resolved.get("head_sha") != head or resolved.get("head_tree_sha") != tree:
        _reject(OrchestratorRejectCode.REGISTRY_ERROR, "V4 resolver returned another HEAD")
    grants = _resolved_grants(resolved)

    v3_verifier = _fresh_module(repository, entries, V3_VERIFIER_PATH, f"_t6_v3_receipt_verifier_{head}")
    verify_v3 = _require_callable(v3_verifier, V3_VERIFIER_SYMBOL)
    try:
        v3_result = verify_v3(root=repository, requested_head=head, raw_q_one_g=raw_q_one_g, receipt=production_miss_receipt)
    except Exception as exc:
        _reject(OrchestratorRejectCode.V3_RECEIPT_ERROR, f"V3 production receipt rejected: {exc}")
    _verify_v3_result(v3_result, head=head, receipt=production_miss_receipt)

    initializer = _fresh_module(repository, entries, ROOT_INITIALIZER_PATH, f"_t6_root_initializer_{head}")
    make_body = _require_callable(initializer, "make_canonical_q_one_g_source_body_v2")
    make_anchor = _require_callable(initializer, "make_root_initializer_anchor_v2")
    make_state = _require_callable(initializer, "make_raw_root_source_state_v2")
    serialize = _require_callable(initializer, "artifact_to_mapping_v2")
    try:
        body_obj = make_body(raw_q_one_g)
        anchor_obj = make_anchor(body_obj)
        state_obj = make_state(body_obj, anchor_obj)
        body = serialize(body_obj)
        anchor = serialize(anchor_obj)
        state = serialize(state_obj)
    except Exception as exc:
        _reject(OrchestratorRejectCode.SOURCE_ERROR, f"fresh root initializer rejected raw source: {exc}")
    actualness = production_miss_receipt.get("root_actualness")
    if type(actualness) is not dict:
        _reject(OrchestratorRejectCode.SOURCE_ERROR, "production receipt has no explicit actualness mapping")
    if actualness.get("head_sha") != head:
        _reject(OrchestratorRejectCode.SOURCE_ERROR, "actualness is bound to another HEAD")

    owner_module = _fresh_module(repository, entries, OWNER_PATH, f"_t6_owner_{head}")
    validator_module = _fresh_module(repository, entries, VALIDATOR_PATH, f"_t6_validator_{head}")
    consumer_module = _fresh_module(repository, entries, CONSUMER_PATH, f"_t6_consumer_{head}")
    classify = _require_callable(owner_module, OWNER_SYMBOL)
    owner_serialize = _require_callable(owner_module, OWNER_SERIALIZER)
    validate = _require_callable(validator_module, VALIDATOR_SYMBOL)
    validation_serialize = _require_callable(validator_module, VALIDATOR_SERIALIZER)
    consume = _require_callable(consumer_module, CONSUMER_SYMBOL)
    consumer_serialize = _require_callable(consumer_module, CONSUMER_SERIALIZER)
    try:
        owner_obj = classify(raw_q_one_g=raw_q_one_g, source_body=body, root_anchor=anchor, source_state=state, root_actualness=actualness, role_grant=grants[ROLE_OWNER])
        owner_wire = owner_serialize(owner_obj)
        validation_obj = validate(raw_q_one_g=raw_q_one_g, source_body=body, root_anchor=anchor, source_state=state, root_actualness=actualness, owner_receipt=owner_wire, terminal_receipt=production_miss_receipt, role_grant=grants[ROLE_VALIDATOR])
        validation_wire = validation_serialize(validation_obj)
        consumer_obj = consume(raw_q_one_g=raw_q_one_g, source_body=body, root_anchor=anchor, source_state=state, root_actualness=actualness, owner_receipt=owner_wire, terminal_receipt=production_miss_receipt, scope_validation_receipt=validation_wire, role_grant=grants[ROLE_CONSUMER])
        result = consumer_serialize(consumer_obj)
    except Exception as exc:
        _reject(OrchestratorRejectCode.ROLE_ERROR, f"V4 role chain rejected source: {exc}")
    _authority_check(result)
    if result.get("state_id") != state.get("state_id") or result.get("root_actualness_id") != actualness.get("actualness_id"):
        _reject(OrchestratorRejectCode.SOURCE_ERROR, "consumer result changed the source subject")
    # Detect a worktree replacement that happened while the role chain ran.
    for path in (V4_RESOLVER_PATH, V3_VERIFIER_PATH, ROOT_INITIALIZER_PATH, OWNER_PATH, VALIDATOR_PATH, CONSUMER_PATH):
        _blob(repository, entries, path)
    return result


__all__ = ["OrchestratorError", "OrchestratorRejectCode", "assemble_q_one_root_prefix_scoped_e1_v2"]
