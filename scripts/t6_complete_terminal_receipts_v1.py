#!/usr/bin/env python3
"""Non-authorizing terminal miss receipt types for the T6 Gate-4 boundary.

This module deliberately cannot issue or verify a production ``MISS_COMPLETE``.
It defines a strict ``MISS_LOCAL`` record, the future production complete-miss
shape, canonical seals, source/projection binding, and a fixed production
registry parser. The production registry has no COMPLETE schedule, so every
well-formed complete claim is rejected with ``SCHEDULE_NOT_COMPLETE`` after its
type and binding checks.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, fields, replace
from enum import Enum
import hashlib
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, NoReturn, TypeVar


SCHEMA_VERSION = 1
MISS_LOCAL = "MISS_LOCAL"
MISS_COMPLETE = "MISS_COMPLETE"
SOURCE_STATE = "SOURCE_STATE"
TARGET_PROJECTION = "TARGET_PROJECTION"
PRODUCTION = "PRODUCTION"
LOCAL_ONLY = "LOCAL_ONLY"
NO_COMPLETE_SCHEDULE_AUTHORITY = "NO_COMPLETE_SCHEDULE_AUTHORITY"
HEAD_ROLE_REGISTRY_REQUIRED = "HEAD_ROLE_REGISTRY_REQUIRED"

PRODUCTION_REGISTRY_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "t6-wave1"
    / "t6-complete-terminal-schedule-registry-v1.json"
)


class TerminalReceiptRejectCode(str, Enum):
    INPUT_NOT_MAPPING = "INPUT_NOT_MAPPING"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    UNKNOWN_RECEIPT_TYPE = "UNKNOWN_RECEIPT_TYPE"
    UNKNOWN_SCHEMA_VERSION = "UNKNOWN_SCHEMA_VERSION"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    REGISTRY_INVALID = "REGISTRY_INVALID"
    REGISTRY_BINDING_MISMATCH = "REGISTRY_BINDING_MISMATCH"
    SUBJECT_BINDING_MISMATCH = "SUBJECT_BINDING_MISMATCH"
    SCHEDULE_BINDING_MISMATCH = "SCHEDULE_BINDING_MISMATCH"
    SCHEDULE_NOT_COMPLETE = "SCHEDULE_NOT_COMPLETE"
    LOCAL_AS_GLOBAL = "LOCAL_AS_GLOBAL"
    DUPLICATE_IDENTIFIER = "DUPLICATE_IDENTIFIER"


class TerminalReceiptValidationError(ValueError):
    """Fail-closed receipt error with a stable machine-readable code."""

    def __init__(self, code: TerminalReceiptRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _json_copy(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, child in value.items():
            if not isinstance(key, str):
                raise TerminalReceiptValidationError(
                    TerminalReceiptRejectCode.MALFORMED_FIELD,
                    "canonical JSON object keys must be strings",
                )
            result[key] = _json_copy(child)
        return result
    if isinstance(value, (list, tuple)):
        return [_json_copy(child) for child in value]
    if value is None or isinstance(value, (str, bool, int, float)):
        return copy.deepcopy(value)
    raise TerminalReceiptValidationError(
        TerminalReceiptRejectCode.MALFORMED_FIELD,
        f"{type(value).__name__} is not canonical JSON",
    )


def _freeze_json(value: Any) -> Any:
    normalized = _json_copy(value)
    if isinstance(normalized, dict):
        return MappingProxyType(
            {key: _freeze_json(child) for key, child in normalized.items()}
        )
    if isinstance(normalized, list):
        return tuple(_freeze_json(child) for child in normalized)
    return normalized


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
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.MALFORMED_FIELD,
            f"value is not canonical JSON: {exc}",
        ) from exc


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


def _plain_int(value: Any) -> bool:
    return type(value) is int


def _require_text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty string",
        )
    return value


def _require_digest(value: Any, name: str) -> str:
    if not (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.MALFORMED_FIELD,
            f"{name} must be a lowercase SHA-256 digest",
        )
    return value


def _require_head_sha(value: Any, name: str = "head_sha") -> str:
    if not (
        isinstance(value, str)
        and len(value) == 40
        and all(character in "0123456789abcdef" for character in value)
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.MALFORMED_FIELD,
            f"{name} must be a lowercase 40-character Git SHA",
        )
    return value


def _require_exact_fields(
    value: Mapping[str, Any], expected: set[str], name: str
) -> None:
    if set(value) != expected:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.FIELD_SET_MISMATCH,
            f"{name} fields differ from the v1 contract",
        )


def _require_payload_mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping) or not value:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty mapping",
        )
    frozen = _freeze_json(value)
    assert isinstance(frozen, Mapping)
    return frozen


@dataclass(frozen=True, slots=True)
class TerminalSubjectBindingV1:
    """Digest-only binding for a source state or target projection."""

    subject_kind: str
    subject_id: str
    subject_digest: str
    scheduler_input_digest: str
    source_state_id: str
    source_state_digest: str
    projection_id: str | None = None
    projection_digest: str | None = None

    def __post_init__(self) -> None:
        if self.subject_kind not in {SOURCE_STATE, TARGET_PROJECTION}:
            raise TerminalReceiptValidationError(
                TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
                "subject_kind must be SOURCE_STATE or TARGET_PROJECTION",
            )
        for name in ("subject_id", "source_state_id"):
            _require_text(getattr(self, name), name)
        for name in (
            "subject_digest",
            "scheduler_input_digest",
            "source_state_digest",
        ):
            _require_digest(getattr(self, name), name)
        if self.subject_kind == SOURCE_STATE:
            if (
                self.subject_id != self.source_state_id
                or self.subject_digest != self.source_state_digest
                or self.projection_id is not None
                or self.projection_digest is not None
            ):
                raise TerminalReceiptValidationError(
                    TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
                    "SOURCE_STATE subject must be exactly the bound source",
                )
        else:
            _require_text(self.projection_id, "projection_id")
            _require_digest(self.projection_digest, "projection_digest")
            if (
                self.subject_id != self.projection_id
                or self.subject_digest != self.projection_digest
            ):
                raise TerminalReceiptValidationError(
                    TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
                    "TARGET_PROJECTION subject must be exactly the bound projection",
                )


def bind_source_subject_v1(
    source_state_payload: Mapping[str, Any],
    scheduler_input_payload: Mapping[str, Any],
) -> TerminalSubjectBindingV1:
    source = _require_payload_mapping(source_state_payload, "source_state_payload")
    scheduler_input = _require_payload_mapping(
        scheduler_input_payload, "scheduler_input_payload"
    )
    source_state_id = _require_text(source.get("state_id"), "source state_id")
    source_digest = canonical_digest_v1(source)
    expected_binding = {
        "subject_kind": SOURCE_STATE,
        "source_state_id": source_state_id,
        "source_state_digest": source_digest,
    }
    if _json_copy(scheduler_input.get("subject_binding")) != expected_binding:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
            "source scheduler input does not repeat its exact source binding",
        )
    return TerminalSubjectBindingV1(
        subject_kind=SOURCE_STATE,
        subject_id=source_state_id,
        subject_digest=source_digest,
        scheduler_input_digest=canonical_digest_v1(scheduler_input),
        source_state_id=source_state_id,
        source_state_digest=source_digest,
    )


def bind_target_projection_subject_v1(
    source_state_payload: Mapping[str, Any],
    projection_payload: Mapping[str, Any],
    scheduler_input_payload: Mapping[str, Any],
) -> TerminalSubjectBindingV1:
    source = _require_payload_mapping(source_state_payload, "source_state_payload")
    projection = _require_payload_mapping(projection_payload, "projection_payload")
    scheduler_input = _require_payload_mapping(
        scheduler_input_payload, "scheduler_input_payload"
    )
    source_state_id = _require_text(source.get("state_id"), "source state_id")
    projection_id = _require_text(projection.get("projection_id"), "projection_id")
    source_digest = canonical_digest_v1(source)
    projection_digest = canonical_digest_v1(projection)
    expected_binding = {
        "subject_kind": TARGET_PROJECTION,
        "source_state_id": source_state_id,
        "source_state_digest": source_digest,
        "projection_id": projection_id,
        "projection_digest": projection_digest,
    }
    if _json_copy(scheduler_input.get("subject_binding")) != expected_binding:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
            "target scheduler input does not repeat source and projection bindings",
        )
    return TerminalSubjectBindingV1(
        subject_kind=TARGET_PROJECTION,
        subject_id=projection_id,
        subject_digest=projection_digest,
        scheduler_input_digest=canonical_digest_v1(scheduler_input),
        source_state_id=source_state_id,
        source_state_digest=source_digest,
        projection_id=projection_id,
        projection_digest=projection_digest,
    )


@dataclass(frozen=True, slots=True)
class LocalTerminalMissReceiptV1:
    RECEIPT_TYPE: ClassVar[str] = "LocalTerminalMissReceiptV1"

    subject_kind: str
    subject_id: str
    subject_digest: str
    scheduler_input_digest: str
    schedule_id: str
    schedule_registry_digest: str
    family_id: str
    attempt_index: int
    evaluator_id: str
    evaluator_digest: str
    input_digest: str
    output_digest: str
    outcome: str
    digest: str


@dataclass(frozen=True, slots=True)
class CompleteTerminalMissReceiptV1:
    RECEIPT_TYPE: ClassVar[str] = "CompleteTerminalMissReceiptV1"

    head_sha: str
    authority_class: str
    registry_id: str
    registry_class: str
    registry_digest: str
    schedule_id: str
    schedule_digest: str
    schedule_registry_digest: str
    subject_kind: str
    subject_id: str
    subject_digest: str
    scheduler_input_digest: str
    owner_domain_id: str
    owner_domain_digest: str
    domain_membership_replay_id: str
    domain_membership_replay_artifact_digest: str
    domain_membership_replay_digest: str
    ordered_family_ids: tuple[str, ...]
    ordered_local_miss_digests: tuple[str, ...]
    coverage_theorem_id: str
    coverage_theorem_digest: str
    coverage_reproduction_id: str
    coverage_reproduction_digest: str
    coverage_verifier_id: str
    coverage_verifier_digest: str
    coverage_replay_digest: str
    outcome: str
    digest: str


ReceiptT = TypeVar(
    "ReceiptT", LocalTerminalMissReceiptV1, CompleteTerminalMissReceiptV1
)


def _unsigned_receipt_mapping_v1(receipt: ReceiptT) -> dict[str, Any]:
    result: dict[str, Any] = {
        "receipt_type": receipt.RECEIPT_TYPE,
        "schema_version": SCHEMA_VERSION,
    }
    for field in fields(receipt):
        if field.name != "digest":
            result[field.name] = _json_copy(getattr(receipt, field.name))
    return result


def receipt_to_mapping_v1(receipt: ReceiptT) -> dict[str, Any]:
    result = _unsigned_receipt_mapping_v1(receipt)
    result["digest"] = receipt.digest
    return result


def _seal_receipt_v1(cls: type[ReceiptT], **values: Any) -> ReceiptT:
    draft = cls(**values, digest="")
    return replace(
        draft, digest=canonical_digest_v1(_unsigned_receipt_mapping_v1(draft))
    )


def _verify_receipt_seal_v1(receipt: ReceiptT) -> None:
    _require_digest(receipt.digest, f"{receipt.RECEIPT_TYPE}.digest")
    expected = canonical_digest_v1(_unsigned_receipt_mapping_v1(receipt))
    if receipt.digest != expected:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.DIGEST_MISMATCH,
            f"{receipt.RECEIPT_TYPE} digest does not replay",
        )


def _parse_receipt_v1(value: Any, cls: type[ReceiptT]) -> ReceiptT:
    if type(value) is cls:
        _validate_receipt_fields_v1(value)
        _verify_receipt_seal_v1(value)
        return value
    if not isinstance(value, Mapping):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.INPUT_NOT_MAPPING,
            f"{cls.RECEIPT_TYPE} must be a mapping",
        )
    receipt_type = value.get("receipt_type")
    if receipt_type != cls.RECEIPT_TYPE:
        code = (
            TerminalReceiptRejectCode.LOCAL_AS_GLOBAL
            if cls is CompleteTerminalMissReceiptV1
            and receipt_type == LocalTerminalMissReceiptV1.RECEIPT_TYPE
            else TerminalReceiptRejectCode.UNKNOWN_RECEIPT_TYPE
        )
        raise TerminalReceiptValidationError(code, f"expected {cls.RECEIPT_TYPE}")
    expected = {field.name for field in fields(cls)} | {
        "receipt_type",
        "schema_version",
    }
    _require_exact_fields(value, expected, cls.RECEIPT_TYPE)
    if not _plain_int(value.get("schema_version")) or value.get("schema_version") != 1:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.UNKNOWN_SCHEMA_VERSION,
            "receipt schema_version must be the integer 1",
        )
    kwargs = {field.name: value[field.name] for field in fields(cls)}
    if cls is CompleteTerminalMissReceiptV1:
        for name in ("ordered_family_ids", "ordered_local_miss_digests"):
            if not isinstance(kwargs[name], list):
                raise TerminalReceiptValidationError(
                    TerminalReceiptRejectCode.MALFORMED_FIELD,
                    f"{name} must be a JSON array",
                )
            kwargs[name] = tuple(kwargs[name])
    try:
        receipt = cls(**kwargs)
    except (TypeError, ValueError) as exc:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.MALFORMED_FIELD,
            f"malformed {cls.RECEIPT_TYPE}",
        ) from exc
    _validate_receipt_fields_v1(receipt)
    _verify_receipt_seal_v1(receipt)
    return receipt


def _validate_receipt_fields_v1(receipt: ReceiptT) -> None:
    if receipt.subject_kind not in {SOURCE_STATE, TARGET_PROJECTION}:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.MALFORMED_FIELD, "invalid subject_kind"
        )
    for name in ("subject_id", "schedule_id"):
        _require_text(getattr(receipt, name), name)
    for name in ("subject_digest", "schedule_registry_digest"):
        _require_digest(getattr(receipt, name), name)
    if type(receipt) is LocalTerminalMissReceiptV1:
        for name in ("family_id", "evaluator_id"):
            _require_text(getattr(receipt, name), name)
        for name in (
            "scheduler_input_digest",
            "evaluator_digest",
            "input_digest",
            "output_digest",
        ):
            _require_digest(getattr(receipt, name), name)
        if not _plain_int(receipt.attempt_index) or receipt.attempt_index < 0:
            raise TerminalReceiptValidationError(
                TerminalReceiptRejectCode.MALFORMED_FIELD,
                "attempt_index must be a nonnegative integer, not bool",
            )
        if receipt.outcome != MISS_LOCAL:
            raise TerminalReceiptValidationError(
                TerminalReceiptRejectCode.LOCAL_AS_GLOBAL,
                "local receipt outcome must be MISS_LOCAL",
            )
        return
    _require_head_sha(receipt.head_sha)
    if receipt.authority_class != PRODUCTION or receipt.registry_class != PRODUCTION:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_BINDING_MISMATCH,
            "complete receipt authority and registry class must be PRODUCTION",
        )
    for name in (
        "registry_id",
        "owner_domain_id",
        "domain_membership_replay_id",
        "coverage_theorem_id",
        "coverage_reproduction_id",
        "coverage_verifier_id",
    ):
        _require_text(getattr(receipt, name), name)
    for name in (
        "registry_digest",
        "schedule_digest",
        "scheduler_input_digest",
        "owner_domain_digest",
        "domain_membership_replay_artifact_digest",
        "domain_membership_replay_digest",
        "coverage_theorem_digest",
        "coverage_reproduction_digest",
        "coverage_verifier_digest",
        "coverage_replay_digest",
    ):
        _require_digest(getattr(receipt, name), name)
    if not receipt.ordered_family_ids or len(receipt.ordered_family_ids) != len(
        receipt.ordered_local_miss_digests
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.MALFORMED_FIELD,
            "complete receipt needs one local digest per ordered family",
        )
    if len(set(receipt.ordered_family_ids)) != len(receipt.ordered_family_ids):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.DUPLICATE_IDENTIFIER,
            "complete receipt repeats a family",
        )
    for family_id in receipt.ordered_family_ids:
        _require_text(family_id, "ordered family_id")
    for digest in receipt.ordered_local_miss_digests:
        _require_digest(digest, "ordered local miss digest")
    if receipt.outcome != MISS_COMPLETE:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.LOCAL_AS_GLOBAL,
            "complete receipt outcome must be MISS_COMPLETE",
        )


def parse_local_terminal_miss_receipt_v1(value: Any) -> LocalTerminalMissReceiptV1:
    return _parse_receipt_v1(value, LocalTerminalMissReceiptV1)


def parse_complete_terminal_miss_receipt_v1(
    value: Any,
) -> CompleteTerminalMissReceiptV1:
    if type(value) is LocalTerminalMissReceiptV1:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.LOCAL_AS_GLOBAL,
            "MISS_LOCAL cannot be parsed as MISS_COMPLETE",
        )
    return _parse_receipt_v1(value, CompleteTerminalMissReceiptV1)


_LOCAL_SCHEDULE_FIELDS = {
    "schedule_id",
    "classification",
    "subject_kind",
    "ordered_family_ids",
    "evidence_refs",
}
_REGISTRY_FIELDS = {
    "schema_id",
    "schema_version",
    "registry_id",
    "registry_class",
    "status",
    "head_authority_status",
    "digest_algorithm",
    "local_schedules",
    "complete_schedules",
    "invariants",
    "registry_digest",
}
_INVARIANT_FIELDS = {
    "complete_schedule_count",
    "complete_miss_issuance_enabled",
    "local_miss_implies_complete_miss",
    "terminal_receipt_grants_queue_authority",
}


@dataclass(frozen=True, slots=True)
class ProductionTerminalScheduleRegistryV1:
    registry_id: str
    registry_digest: str
    local_schedules: tuple[Mapping[str, Any], ...]

    def local_schedule(self, schedule_id: str) -> Mapping[str, Any]:
        for schedule in self.local_schedules:
            if schedule["schedule_id"] == schedule_id:
                return schedule
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.SCHEDULE_BINDING_MISMATCH,
            f"unknown LOCAL_ONLY schedule {schedule_id!r}",
        )


def seal_registry_mapping_v1(value: Mapping[str, Any]) -> dict[str, Any]:
    """Canonical helper for the fixed registry file; it grants no authority."""

    result = _json_copy(value)
    result.pop("registry_digest", None)
    result["registry_digest"] = canonical_digest_v1(result)
    return result


def _no_duplicate_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise TerminalReceiptValidationError(
                TerminalReceiptRejectCode.DUPLICATE_IDENTIFIER,
                f"duplicate JSON key {key!r}",
            )
        result[key] = value
    return result


def load_production_registry_v1() -> ProductionTerminalScheduleRegistryV1:
    """Load only the repository-fixed production registry path."""

    try:
        value = json.loads(
            PRODUCTION_REGISTRY_PATH.read_text(encoding="utf-8"),
            object_pairs_hook=_no_duplicate_json_object,
        )
    except (OSError, json.JSONDecodeError) as exc:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_INVALID,
            f"cannot load fixed production registry: {exc}",
        ) from exc
    return parse_production_registry_v1(value)


def parse_production_registry_v1(value: Any) -> ProductionTerminalScheduleRegistryV1:
    if not isinstance(value, Mapping):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.INPUT_NOT_MAPPING,
            "production registry must be a mapping",
        )
    _require_exact_fields(value, _REGISTRY_FIELDS, "production registry")
    if not _plain_int(value.get("schema_version")) or value.get("schema_version") != 1:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_INVALID,
            "registry schema_version must be the integer 1",
        )
    if value.get("schema_id") != "t6_complete_terminal_schedule_registry_v1":
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_INVALID, "unknown registry schema_id"
        )
    if (
        value.get("registry_class") != PRODUCTION
        or value.get("status") != NO_COMPLETE_SCHEDULE_AUTHORITY
        or value.get("head_authority_status") != HEAD_ROLE_REGISTRY_REQUIRED
        or value.get("digest_algorithm") != "sha256-canonical-json-v1"
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_INVALID,
            "registry does not preserve the production no-authority boundary",
        )
    registry_id = _require_text(value.get("registry_id"), "registry_id")
    registry_digest = _require_digest(value.get("registry_digest"), "registry_digest")
    unsigned = _json_copy(value)
    unsigned.pop("registry_digest")
    if canonical_digest_v1(unsigned) != registry_digest:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.DIGEST_MISMATCH,
            "production registry digest does not replay",
        )
    local_values = value.get("local_schedules")
    complete_values = value.get("complete_schedules")
    invariants = value.get("invariants")
    if not isinstance(local_values, list) or not isinstance(complete_values, list):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_INVALID,
            "registry schedule collections must be JSON arrays",
        )
    if complete_values:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_INVALID,
            "production registry must contain zero COMPLETE schedules",
        )
    if not isinstance(invariants, Mapping):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_INVALID,
            "registry invariants must be a mapping",
        )
    _require_exact_fields(invariants, _INVARIANT_FIELDS, "registry invariants")
    count = invariants.get("complete_schedule_count")
    if not _plain_int(count) or count != 0:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_INVALID,
            "complete_schedule_count must be the integer zero, not bool",
        )
    if (
        invariants.get("complete_miss_issuance_enabled") is not False
        or invariants.get("local_miss_implies_complete_miss") is not False
        or invariants.get("terminal_receipt_grants_queue_authority") is not False
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_INVALID,
            "registry invariants attempt to grant missing authority",
        )
    local_schedules: list[Mapping[str, Any]] = []
    schedule_ids: list[str] = []
    for raw in local_values:
        if not isinstance(raw, Mapping):
            raise TerminalReceiptValidationError(
                TerminalReceiptRejectCode.REGISTRY_INVALID,
                "local schedule entry must be a mapping",
            )
        _require_exact_fields(raw, _LOCAL_SCHEDULE_FIELDS, "local schedule")
        schedule_id = _require_text(raw.get("schedule_id"), "local schedule_id")
        if raw.get("classification") != LOCAL_ONLY or raw.get("subject_kind") not in {
            SOURCE_STATE,
            TARGET_PROJECTION,
        }:
            raise TerminalReceiptValidationError(
                TerminalReceiptRejectCode.REGISTRY_INVALID,
                f"schedule {schedule_id!r} must remain LOCAL_ONLY",
            )
        families = raw.get("ordered_family_ids")
        evidence = raw.get("evidence_refs")
        if not isinstance(families, list) or not isinstance(evidence, list):
            raise TerminalReceiptValidationError(
                TerminalReceiptRejectCode.REGISTRY_INVALID,
                "local family/evidence collections must be JSON arrays",
            )
        if not families or not evidence:
            raise TerminalReceiptValidationError(
                TerminalReceiptRejectCode.REGISTRY_INVALID,
                "local family/evidence arrays cannot be empty",
            )
        for item in (*families, *evidence):
            _require_text(item, "local schedule entry")
        if len(set(families)) != len(families):
            raise TerminalReceiptValidationError(
                TerminalReceiptRejectCode.DUPLICATE_IDENTIFIER,
                f"schedule {schedule_id!r} repeats a family",
            )
        schedule_ids.append(schedule_id)
        local_schedules.append(_freeze_json(raw))
    if len(set(schedule_ids)) != len(schedule_ids):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.DUPLICATE_IDENTIFIER,
            "production registry repeats a schedule_id",
        )
    return ProductionTerminalScheduleRegistryV1(
        registry_id=registry_id,
        registry_digest=registry_digest,
        local_schedules=tuple(local_schedules),
    )


def make_local_terminal_miss_receipt_v1(
    *,
    subject: TerminalSubjectBindingV1,
    schedule_id: str,
    family_id: str,
    attempt_index: int,
    evaluator_id: str,
    evaluator_digest: str,
    input_digest: str,
    output_digest: str,
) -> LocalTerminalMissReceiptV1:
    """Seal a non-authorizing local miss against the fixed registry."""

    registry = load_production_registry_v1()
    schedule = registry.local_schedule(schedule_id)
    if schedule["subject_kind"] != subject.subject_kind:
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
            "local schedule subject kind differs from its bound subject",
        )
    families = tuple(schedule["ordered_family_ids"])
    if (
        family_id not in families
        or not _plain_int(attempt_index)
        or attempt_index < 0
        or attempt_index >= len(families)
        or families[attempt_index] != family_id
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.SCHEDULE_BINDING_MISMATCH,
            "local family and index do not match the frozen LOCAL_ONLY order",
        )
    receipt = _seal_receipt_v1(
        LocalTerminalMissReceiptV1,
        subject_kind=subject.subject_kind,
        subject_id=subject.subject_id,
        subject_digest=subject.subject_digest,
        scheduler_input_digest=subject.scheduler_input_digest,
        schedule_id=schedule_id,
        schedule_registry_digest=registry.registry_digest,
        family_id=family_id,
        attempt_index=attempt_index,
        evaluator_id=evaluator_id,
        evaluator_digest=evaluator_digest,
        input_digest=input_digest,
        output_digest=output_digest,
        outcome=MISS_LOCAL,
    )
    _validate_receipt_fields_v1(receipt)
    return receipt


def verify_local_terminal_miss_binding_v1(
    value: Any, subject: TerminalSubjectBindingV1
) -> LocalTerminalMissReceiptV1:
    """Verify shape/binding only; the return value has no global authority."""

    receipt = parse_local_terminal_miss_receipt_v1(value)
    registry = load_production_registry_v1()
    schedule = registry.local_schedule(receipt.schedule_id)
    if (
        receipt.schedule_registry_digest != registry.registry_digest
        or receipt.subject_kind != subject.subject_kind
        or receipt.subject_id != subject.subject_id
        or receipt.subject_digest != subject.subject_digest
        or receipt.scheduler_input_digest != subject.scheduler_input_digest
        or schedule["subject_kind"] != subject.subject_kind
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
            "local receipt is not bound to this subject and fixed registry",
        )
    families = tuple(schedule["ordered_family_ids"])
    if (
        receipt.attempt_index >= len(families)
        or families[receipt.attempt_index] != receipt.family_id
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.SCHEDULE_BINDING_MISMATCH,
            "local receipt family/index differs from the fixed schedule",
        )
    return receipt


def verify_complete_terminal_miss_receipt_v1(
    value: Any,
    subject: TerminalSubjectBindingV1,
    expected_head_sha: str,
) -> NoReturn:
    """Fail closed: the fixed production registry has no COMPLETE schedule."""

    receipt = parse_complete_terminal_miss_receipt_v1(value)
    expected_head_sha = _require_head_sha(expected_head_sha, "expected_head_sha")
    registry = load_production_registry_v1()
    if (
        receipt.head_sha != expected_head_sha
        or receipt.authority_class != PRODUCTION
        or receipt.registry_id != registry.registry_id
        or receipt.registry_class != PRODUCTION
        or receipt.registry_digest != registry.registry_digest
        or receipt.schedule_registry_digest != registry.registry_digest
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.REGISTRY_BINDING_MISMATCH,
            "complete claim is not bound to the expected HEAD and fixed registry",
        )
    if (
        receipt.subject_kind != subject.subject_kind
        or receipt.subject_id != subject.subject_id
        or receipt.subject_digest != subject.subject_digest
        or receipt.scheduler_input_digest != subject.scheduler_input_digest
    ):
        raise TerminalReceiptValidationError(
            TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
            "complete claim is not bound to the exact scheduler subject/input",
        )
    raise TerminalReceiptValidationError(
        TerminalReceiptRejectCode.SCHEDULE_NOT_COMPLETE,
        f"production schedule {receipt.schedule_id!r} has no COMPLETE authority",
    )


def production_registry_summary_v1() -> dict[str, Any]:
    registry = load_production_registry_v1()
    return {
        "registry_id": registry.registry_id,
        "registry_class": PRODUCTION,
        "status": NO_COMPLETE_SCHEDULE_AUTHORITY,
        "head_authority_status": HEAD_ROLE_REGISTRY_REQUIRED,
        "registry_digest": registry.registry_digest,
        "local_schedule_count": len(registry.local_schedules),
        "complete_schedule_count": 0,
        "complete_miss_issuance_enabled": False,
    }


__all__ = [
    "CompleteTerminalMissReceiptV1",
    "HEAD_ROLE_REGISTRY_REQUIRED",
    "LOCAL_ONLY",
    "LocalTerminalMissReceiptV1",
    "MISS_COMPLETE",
    "MISS_LOCAL",
    "NO_COMPLETE_SCHEDULE_AUTHORITY",
    "PRODUCTION",
    "SOURCE_STATE",
    "TARGET_PROJECTION",
    "TerminalReceiptRejectCode",
    "TerminalReceiptValidationError",
    "TerminalSubjectBindingV1",
    "bind_source_subject_v1",
    "bind_target_projection_subject_v1",
    "canonical_digest_v1",
    "canonical_json_v1",
    "load_production_registry_v1",
    "make_local_terminal_miss_receipt_v1",
    "parse_complete_terminal_miss_receipt_v1",
    "parse_local_terminal_miss_receipt_v1",
    "parse_production_registry_v1",
    "production_registry_summary_v1",
    "receipt_to_mapping_v1",
    "seal_registry_mapping_v1",
    "verify_complete_terminal_miss_receipt_v1",
    "verify_local_terminal_miss_binding_v1",
]


if __name__ == "__main__":
    print(canonical_json_v1(production_registry_summary_v1()))
