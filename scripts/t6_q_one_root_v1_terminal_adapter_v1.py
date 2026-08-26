#!/usr/bin/env python3
"""Project an authorized q=1 V3 prefix MISS to the narrow V1 terminal shape.

This module is a pinned, non-authorizing projection.  Exact-HEAD authentication
belongs to the coordinator and the final admission verifier.  In particular,
this module never consumes a V4 owner or scope receipt, so the materialized V1
state remains prior to its V1 owner classification.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass, fields
from enum import Enum
from types import MappingProxyType
from typing import Any, ClassVar, Mapping


ARTIFACT_ID = "q1_root_v1_terminal_adapter_v1"
ARTIFACT_PATH = "scripts/t6_q_one_root_v1_terminal_adapter_v1.py"
ARTIFACT_CLASS = "CANONICAL_PROJECTION_ONLY"
PUBLIC_SYMBOLS = (
    "project_q_one_v3_miss_to_v1_terminal_first_v1",
    "terminal_projection_to_mapping_v1",
)

RECEIPT_TYPE = "Q1_V3_MISS_TO_V1_TERMINAL_FIRST_PROJECTION_V1"
RECEIPT_ID_PREFIX = "q1-v1-terminal-projection:"
V1_TERMINAL_SCHEMA_ID = "terminal_first_receipt_v1"
V1_TERMINAL_RECEIPT_ID_PREFIX = "q1-v1-terminal-first:"
SCOPE_ID = "q1_root_after_gap_3_7_11_registered_prefix_v1"
V3_MISS_RECEIPT_TYPE = "ProductionQOneRegisteredPrefixMissReceiptV1"
V3_MISS_OUTCOME = "MISS_REGISTERED_PRIORITY_COMPLETE"
COVERAGE_SEMANTICS = "REGISTERED_PRIORITY_ONLY"
ORDERED_GAPS = (3, 7, 11)
NEXT_UNCHECKED_GAP = 15


class TerminalProjectionRejectCode(str, Enum):
    INPUT_NOT_EXACT_MAPPING = "INPUT_NOT_EXACT_MAPPING"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    SOURCE_BINDING_MISMATCH = "SOURCE_BINDING_MISMATCH"
    TERMINAL_SOURCE_NOT_MISS = "TERMINAL_SOURCE_NOT_MISS"
    SCOPE_WIDENING = "SCOPE_WIDENING"
    AUTHORITY_BOUNDARY_VIOLATION = "AUTHORITY_BOUNDARY_VIOLATION"


class TerminalProjectionError(ValueError):
    def __init__(self, code: TerminalProjectionRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: TerminalProjectionRejectCode, detail: str) -> None:
    raise TerminalProjectionError(code, detail)


def _json_copy(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(
                    TerminalProjectionRejectCode.MALFORMED_FIELD,
                    "canonical JSON keys must be exact strings",
                )
            result[key] = _json_copy(child)
        return result
    if type(value) is list or type(value) is tuple:
        return [_json_copy(child) for child in value]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(
        TerminalProjectionRejectCode.MALFORMED_FIELD,
        f"unsupported canonical JSON value {type(value).__name__}",
    )


def canonical_json_v1(value: Any) -> str:
    try:
        return json.dumps(
            _json_copy(value),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise TerminalProjectionError(
            TerminalProjectionRejectCode.MALFORMED_FIELD,
            f"value is not canonical JSON: {exc}",
        ) from exc


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


def _is_digest(value: Any) -> bool:
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _exact_mapping(value: Any, name: str) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(
            TerminalProjectionRejectCode.INPUT_NOT_EXACT_MAPPING,
            f"{name} must be an exact dict",
        )
    return _json_copy(value)


def _verify_content_seal(
    value: Mapping[str, Any], *, id_field: str, id_prefix: str, name: str
) -> None:
    digest = value.get("digest")
    artifact_id = value.get(id_field)
    if not _is_digest(digest) or artifact_id != id_prefix + digest:
        _reject(
            TerminalProjectionRejectCode.DIGEST_MISMATCH,
            f"{name} content ID or digest is malformed",
        )
    unsigned = _json_copy(value)
    unsigned.pop(id_field, None)
    unsigned.pop("digest", None)
    if canonical_digest_v1(unsigned) != digest:
        _reject(
            TerminalProjectionRejectCode.DIGEST_MISMATCH,
            f"{name} digest does not replay",
        )


def _source_refs(
    source_state: Mapping[str, Any], root_actualness: Mapping[str, Any]
) -> tuple[str, str, str, str]:
    state_id = source_state.get("state_id")
    state_digest = source_state.get("digest")
    actualness_id = root_actualness.get("actualness_id")
    actualness_digest = root_actualness.get("digest")
    if not (
        type(state_id) is str
        and state_id.startswith("state:")
        and _is_digest(state_digest)
        and state_id == "state:" + state_digest
        and type(actualness_id) is str
        and actualness_id.startswith("q1-root-source-actualness:")
        and _is_digest(actualness_digest)
        and actualness_id == "q1-root-source-actualness:" + actualness_digest
    ):
        _reject(
            TerminalProjectionRejectCode.SOURCE_BINDING_MISMATCH,
            "source state or actualness content reference is malformed",
        )
    if not (
        root_actualness.get("state_id") == state_id
        and root_actualness.get("state_digest") == state_digest
        and root_actualness.get("source_actualness") is True
        and root_actualness.get("root_initializer_authority") is True
        and root_actualness.get("persistent_admission") is False
        and root_actualness.get("queue_authority") is False
    ):
        _reject(
            TerminalProjectionRejectCode.SOURCE_BINDING_MISMATCH,
            "root actualness does not bind the non-admitted source state",
        )
    return state_id, state_digest, actualness_id, actualness_digest


def _validated_miss(
    terminal_receipt: Mapping[str, Any],
    *,
    source_state_id: str,
    source_state_digest: str,
    actualness_id: str,
    actualness_digest: str,
) -> tuple[str, str, int]:
    if terminal_receipt.get("receipt_type") != V3_MISS_RECEIPT_TYPE:
        _reject(
            TerminalProjectionRejectCode.TERMINAL_SOURCE_NOT_MISS,
            "only the exact V3 production prefix-MISS type can be projected",
        )
    _verify_content_seal(
        terminal_receipt,
        id_field="receipt_id",
        id_prefix="production-q1-prefix-miss:",
        name="terminal receipt",
    )
    nested_actualness = terminal_receipt.get("root_actualness")
    if type(nested_actualness) is not dict:
        _reject(
            TerminalProjectionRejectCode.SOURCE_BINDING_MISMATCH,
            "terminal receipt has no exact nested actualness mapping",
        )
    if not (
        terminal_receipt.get("state_id") == source_state_id
        and terminal_receipt.get("state_digest") == source_state_digest
        and terminal_receipt.get("root_actualness_digest") == actualness_digest
        and nested_actualness.get("actualness_id") == actualness_id
        and nested_actualness.get("digest") == actualness_digest
    ):
        _reject(
            TerminalProjectionRejectCode.SOURCE_BINDING_MISMATCH,
            "terminal receipt belongs to another source occurrence",
        )
    if not (
        terminal_receipt.get("outcome") == V3_MISS_OUTCOME
        and terminal_receipt.get("registered_prefix_miss_authority") is True
        and terminal_receipt.get("terminal_leaf_authority") is False
        and terminal_receipt.get("root_proof_close_authority") is False
        and terminal_receipt.get("selected_certificate") is None
        and terminal_receipt.get("selected_certificate_digest") is None
    ):
        _reject(
            TerminalProjectionRejectCode.TERMINAL_SOURCE_NOT_MISS,
            "terminal receipt is not an authorized registered-prefix MISS",
        )
    if not (
        terminal_receipt.get("coverage_semantics") == COVERAGE_SEMANTICS
        and terminal_receipt.get("ordered_gaps") == list(ORDERED_GAPS)
        and terminal_receipt.get("next_unchecked_gap") == NEXT_UNCHECKED_GAP
        and type(terminal_receipt.get("next_unchecked_gap")) is int
        and terminal_receipt.get("global_exhaustion") is False
    ):
        _reject(
            TerminalProjectionRejectCode.SCOPE_WIDENING,
            "registered-prefix scope was changed or widened",
        )
    for name, expected in (
        ("source_actualness", True),
        ("root_initializer_authority", True),
        ("issuer_authority", True),
        ("issued_under_terminal_issuer", True),
        ("persistent_admission", False),
        ("common_owner_authority", False),
        ("e1_authority", False),
        ("queue_authority", False),
        ("producer_continuation_allowed", False),
    ):
        if terminal_receipt.get(name) is not expected:
            _reject(
                TerminalProjectionRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
                f"terminal receipt authority {name} changed",
            )
    root_context = terminal_receipt.get("root_context")
    if type(root_context) is not int or type(root_context) is bool or root_context <= 1:
        _reject(
            TerminalProjectionRejectCode.MALFORMED_FIELD,
            "terminal receipt root_context must be a positive exact integer",
        )
    return terminal_receipt["receipt_id"], terminal_receipt["digest"], root_context


@dataclass(frozen=True, init=False, slots=True)
class QOneV3MissToV1TerminalProjectionV1:
    ARTIFACT_TYPE: ClassVar[str] = RECEIPT_TYPE

    schema_version: int
    status: str
    artifact_class: str
    source_state_id: str
    source_state_digest: str
    root_actualness_id: str
    root_actualness_digest: str
    v3_terminal_receipt_id: str
    v3_terminal_receipt_digest: str
    root_context: int
    coverage_semantics: str
    ordered_gaps: tuple[int, int, int]
    next_unchecked_gap: int
    global_exhaustion: bool
    v1_terminal_first: Mapping[str, Any]
    v1_terminal_first_digest: str
    projection_binding_digest: str
    terminal_projection_authority: bool
    persistent_admission: bool
    queue_authority: bool
    successor_authority: bool
    e1_authority: bool
    e2_authority: bool
    e3_authority: bool
    e4_authority: bool
    e5_authority: bool
    receipt_id: str
    digest: str


def _unsigned(values: Mapping[str, Any]) -> dict[str, Any]:
    result = {"receipt_type": RECEIPT_TYPE}
    for field in fields(QOneV3MissToV1TerminalProjectionV1):
        if field.name not in {"receipt_id", "digest"}:
            result[field.name] = _json_copy(values[field.name])
    return result


def _construct(values: Mapping[str, Any]) -> QOneV3MissToV1TerminalProjectionV1:
    result = object.__new__(QOneV3MissToV1TerminalProjectionV1)
    for field in fields(QOneV3MissToV1TerminalProjectionV1):
        value = values[field.name]
        if field.name == "v1_terminal_first":
            value = MappingProxyType(_json_copy(value))
        object.__setattr__(result, field.name, value)
    return result


def _validate_projection(receipt: QOneV3MissToV1TerminalProjectionV1) -> None:
    if type(receipt) is not QOneV3MissToV1TerminalProjectionV1:
        _reject(
            TerminalProjectionRejectCode.INPUT_NOT_EXACT_MAPPING,
            "terminal projection must have the exact receipt class",
        )
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    digest = canonical_digest_v1(_unsigned(values))
    if receipt.digest != digest or receipt.receipt_id != RECEIPT_ID_PREFIX + digest:
        _reject(
            TerminalProjectionRejectCode.DIGEST_MISMATCH,
            "terminal projection seal does not replay",
        )
    terminal = _json_copy(receipt.v1_terminal_first)
    expected_terminal_fields = {
        "schema_id",
        "schema_version",
        "receipt_id",
        "scope",
        "outcome",
        "digest",
    }
    if set(terminal) != expected_terminal_fields:
        _reject(
            TerminalProjectionRejectCode.MALFORMED_FIELD,
            "V1 terminal receipt has an inexact field set",
        )
    terminal_unsigned = dict(terminal)
    terminal_digest = terminal_unsigned.pop("digest", None)
    if not (
        terminal["schema_id"] == V1_TERMINAL_SCHEMA_ID
        and terminal["schema_version"] == 1
        and terminal["scope"] == SCOPE_ID
        and terminal["outcome"] == "MISS"
        and terminal["receipt_id"]
        == V1_TERMINAL_RECEIPT_ID_PREFIX + receipt.projection_binding_digest
        and terminal_digest == canonical_digest_v1(terminal_unsigned)
        and receipt.v1_terminal_first_digest == terminal_digest
    ):
        _reject(
            TerminalProjectionRejectCode.DIGEST_MISMATCH,
            "V1 terminal receipt does not replay from the projection binding",
        )
    expected_binding = canonical_digest_v1(
        {
            "source_state_id": receipt.source_state_id,
            "source_state_digest": receipt.source_state_digest,
            "root_actualness_id": receipt.root_actualness_id,
            "root_actualness_digest": receipt.root_actualness_digest,
            "v3_terminal_receipt_id": receipt.v3_terminal_receipt_id,
            "v3_terminal_receipt_digest": receipt.v3_terminal_receipt_digest,
            "root_context": receipt.root_context,
            "scope": SCOPE_ID,
            "coverage_semantics": COVERAGE_SEMANTICS,
            "ordered_gaps": list(ORDERED_GAPS),
            "next_unchecked_gap": NEXT_UNCHECKED_GAP,
            "global_exhaustion": False,
        }
    )
    if receipt.projection_binding_digest != expected_binding:
        _reject(
            TerminalProjectionRejectCode.DIGEST_MISMATCH,
            "terminal projection binding changed",
        )
    if not (
        type(receipt.schema_version) is int
        and receipt.schema_version == 1
        and receipt.status == "V1_TERMINAL_FIRST_PROJECTED_NO_AUTHORITY"
        and receipt.artifact_class == ARTIFACT_CLASS
        and receipt.coverage_semantics == COVERAGE_SEMANTICS
        and receipt.ordered_gaps == ORDERED_GAPS
        and receipt.next_unchecked_gap == NEXT_UNCHECKED_GAP
        and receipt.global_exhaustion is False
    ):
        _reject(
            TerminalProjectionRejectCode.SCOPE_WIDENING,
            "projection identity or registered-prefix scope changed",
        )
    for name in (
        "terminal_projection_authority",
        "persistent_admission",
        "queue_authority",
        "successor_authority",
        "e1_authority",
        "e2_authority",
        "e3_authority",
        "e4_authority",
        "e5_authority",
    ):
        if getattr(receipt, name) is not False:
            _reject(
                TerminalProjectionRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
                f"nonrole projection field {name} must be false",
            )


def project_q_one_v3_miss_to_v1_terminal_first_v1(
    *,
    source_state: dict[str, Any],
    root_actualness: dict[str, Any],
    terminal_receipt: dict[str, Any],
) -> QOneV3MissToV1TerminalProjectionV1:
    """Create only a non-authorizing V3-MISS to V1-terminal projection."""

    state = _exact_mapping(source_state, "source_state")
    actualness = _exact_mapping(root_actualness, "root_actualness")
    terminal = _exact_mapping(terminal_receipt, "terminal_receipt")
    state_id, state_digest, actualness_id, actualness_digest = _source_refs(
        state, actualness
    )
    terminal_id, terminal_digest, root_context = _validated_miss(
        terminal,
        source_state_id=state_id,
        source_state_digest=state_digest,
        actualness_id=actualness_id,
        actualness_digest=actualness_digest,
    )
    binding = canonical_digest_v1(
        {
            "source_state_id": state_id,
            "source_state_digest": state_digest,
            "root_actualness_id": actualness_id,
            "root_actualness_digest": actualness_digest,
            "v3_terminal_receipt_id": terminal_id,
            "v3_terminal_receipt_digest": terminal_digest,
            "root_context": root_context,
            "scope": SCOPE_ID,
            "coverage_semantics": COVERAGE_SEMANTICS,
            "ordered_gaps": list(ORDERED_GAPS),
            "next_unchecked_gap": NEXT_UNCHECKED_GAP,
            "global_exhaustion": False,
        }
    )
    v1_terminal_unsigned = {
        "schema_id": V1_TERMINAL_SCHEMA_ID,
        "schema_version": 1,
        "receipt_id": V1_TERMINAL_RECEIPT_ID_PREFIX + binding,
        "scope": SCOPE_ID,
        "outcome": "MISS",
    }
    v1_terminal = {
        **v1_terminal_unsigned,
        "digest": canonical_digest_v1(v1_terminal_unsigned),
    }
    values: dict[str, Any] = {
        "schema_version": 1,
        "status": "V1_TERMINAL_FIRST_PROJECTED_NO_AUTHORITY",
        "artifact_class": ARTIFACT_CLASS,
        "source_state_id": state_id,
        "source_state_digest": state_digest,
        "root_actualness_id": actualness_id,
        "root_actualness_digest": actualness_digest,
        "v3_terminal_receipt_id": terminal_id,
        "v3_terminal_receipt_digest": terminal_digest,
        "root_context": root_context,
        "coverage_semantics": COVERAGE_SEMANTICS,
        "ordered_gaps": ORDERED_GAPS,
        "next_unchecked_gap": NEXT_UNCHECKED_GAP,
        "global_exhaustion": False,
        "v1_terminal_first": v1_terminal,
        "v1_terminal_first_digest": v1_terminal["digest"],
        "projection_binding_digest": binding,
        "terminal_projection_authority": False,
        "persistent_admission": False,
        "queue_authority": False,
        "successor_authority": False,
        "e1_authority": False,
        "e2_authority": False,
        "e3_authority": False,
        "e4_authority": False,
        "e5_authority": False,
    }
    digest = canonical_digest_v1(_unsigned(values))
    values.update({"receipt_id": RECEIPT_ID_PREFIX + digest, "digest": digest})
    result = _construct(values)
    _validate_projection(result)
    return result


def terminal_projection_to_mapping_v1(
    receipt: QOneV3MissToV1TerminalProjectionV1,
) -> dict[str, Any]:
    _validate_projection(receipt)
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    result = _unsigned(values)
    result["receipt_id"] = receipt.receipt_id
    result["digest"] = receipt.digest
    return result


__all__ = [
    "ARTIFACT_CLASS",
    "ARTIFACT_ID",
    "ARTIFACT_PATH",
    "COVERAGE_SEMANTICS",
    "NEXT_UNCHECKED_GAP",
    "ORDERED_GAPS",
    "PUBLIC_SYMBOLS",
    "QOneV3MissToV1TerminalProjectionV1",
    "SCOPE_ID",
    "TerminalProjectionError",
    "TerminalProjectionRejectCode",
    "canonical_digest_v1",
    "project_q_one_v3_miss_to_v1_terminal_first_v1",
    "terminal_projection_to_mapping_v1",
]
