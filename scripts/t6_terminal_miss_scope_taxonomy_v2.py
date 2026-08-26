#!/usr/bin/env python3
"""Exact, non-authorizing scope taxonomy for T6 terminal misses.

The two v2 receipt types deliberately mean different things:

* ``RegisteredPriorityPrefixMissReceiptV2`` exhausts one coordinator-registered
  finite priority prefix.  It says nothing about unregistered terminal families.
* ``TerminalUniverseMissReceiptV2`` declares evidence about the full natural
  Bradford range.  Parsing it does not establish that the declaration is true.

This module parses and audits evidence shapes only.  It has no issuer, callable
registry, E1 admission, producer-continuation, or queue-authority API.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, fields, is_dataclass
from enum import Enum
import hashlib
import json
import re
from typing import Any, ClassVar, Mapping, NoReturn, TypeVar


SCHEMA_VERSION = 2
SOURCE_STATE = "SOURCE_STATE"
TARGET_PROJECTION = "TARGET_PROJECTION"
SUBJECT_KINDS = frozenset({SOURCE_STATE, TARGET_PROJECTION})

EVIDENCE_ONLY = "EVIDENCE_ONLY_NO_E1_OR_QUEUE_AUTHORITY"
COORDINATOR_ROLE_REGISTRY_ID_V2 = "t6_coordinator_role_registry_v2"
COORDINATOR_ROLE_REGISTRY_VERSION_V2 = 2

REGISTERED_PRIORITY_ONLY = "REGISTERED_PRIORITY_ONLY"
MISS_REGISTERED_PRIORITY_COMPLETE = "MISS_REGISTERED_PRIORITY_COMPLETE"
TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY = "TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY"

_DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")
_HEAD_RE = re.compile(r"[0-9a-f]{40}\Z")


class TerminalMissScopeRejectCode(str, Enum):
    INPUT_NOT_EXACT_TYPE = "INPUT_NOT_EXACT_TYPE"
    SUBCLASS_REJECTED = "SUBCLASS_REJECTED"
    LEGACY_OR_LOCAL_RECEIPT = "LEGACY_OR_LOCAL_RECEIPT"
    RECEIPT_TYPE_MISMATCH = "RECEIPT_TYPE_MISMATCH"
    SCHEMA_VERSION_MISMATCH = "SCHEMA_VERSION_MISMATCH"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    SCOPE_SEMANTICS_MISMATCH = "SCOPE_SEMANTICS_MISMATCH"
    REGISTRY_V2_AUTHORIZATION_REQUIRED = "REGISTRY_V2_AUTHORIZATION_REQUIRED"
    TERMINAL_UNIVERSE_FORBIDS_PRODUCER = "TERMINAL_UNIVERSE_FORBIDS_PRODUCER"


class TerminalMissScopeValidationError(ValueError):
    def __init__(self, code: TerminalMissScopeRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _json_copy(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                raise TerminalMissScopeValidationError(
                    TerminalMissScopeRejectCode.MALFORMED_FIELD,
                    "canonical JSON object keys must be exact builtin strings",
                )
            result[key] = _json_copy(child)
        return result
    if isinstance(value, (list, tuple)):
        return [_json_copy(child) for child in value]
    if value is None or type(value) in {str, bool, int, float}:
        return copy.deepcopy(value)
    raise TerminalMissScopeValidationError(
        TerminalMissScopeRejectCode.MALFORMED_FIELD,
        f"value of type {type(value).__name__} is not canonical JSON",
    )


def canonical_json_v2(value: Any) -> str:
    try:
        return json.dumps(
            _json_copy(value),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.MALFORMED_FIELD,
            f"value is not canonical JSON: {exc}",
        ) from exc


def canonical_digest_v2(value: Any) -> str:
    return hashlib.sha256(canonical_json_v2(value).encode("ascii")).hexdigest()


def _require_text(value: Any, name: str) -> str:
    if type(value) is not str or not value:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty exact builtin string",
        )
    return value


def _require_digest(value: Any, name: str) -> str:
    if type(value) is not str or _DIGEST_RE.fullmatch(value) is None:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.MALFORMED_FIELD,
            f"{name} must be a lowercase SHA-256 digest",
        )
    return value


def _require_head(value: Any) -> str:
    if type(value) is not str or _HEAD_RE.fullmatch(value) is None:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.MALFORMED_FIELD,
            "head_sha must be a lowercase 40-character Git object ID",
        )
    return value


def _plain_int(value: Any) -> bool:
    return type(value) is int


def _require_plain_int(value: Any, name: str, minimum: int = 0) -> int:
    if not _plain_int(value) or value < minimum:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.MALFORMED_FIELD,
            f"{name} must be an integer >= {minimum}, not bool",
        )
    return value


def _require_exact_bool(value: Any, expected: bool, name: str) -> None:
    if type(value) is not bool or value is not expected:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            f"{name} must be exactly {expected!r}",
        )


@dataclass(frozen=True, slots=True)
class RegisteredPriorityPrefixMissReceiptV2:
    RECEIPT_TYPE: ClassVar[str] = "RegisteredPriorityPrefixMissReceiptV2"

    head_sha: str
    evidence_class: str
    e1_authority: bool
    queue_authority: bool
    registry_id: str
    registry_version: int
    registry_digest: str
    schedule_id: str
    schedule_digest: str
    subject_kind: str
    subject_id: str
    subject_digest: str
    scheduler_input_digest: str
    owner_domain_id: str
    owner_domain_digest: str
    domain_membership_replay_id: str
    domain_membership_replay_artifact_digest: str
    domain_membership_replay_digest: str
    ordered_gaps: tuple[int, ...]
    ordered_family_ids: tuple[str, ...]
    ordered_family_definition_digests: tuple[str, ...]
    ordered_local_miss_digests: tuple[str, ...]
    next_unchecked_gap: int
    coverage_semantics: str
    coverage_theorem_id: str
    coverage_theorem_digest: str
    coverage_reproduction_id: str
    coverage_reproduction_digest: str
    coverage_verifier_id: str
    coverage_verifier_digest: str
    coverage_replay_digest: str
    global_exhaustion: bool
    outcome: str
    digest: str


@dataclass(frozen=True, slots=True)
class TerminalUniverseMissReceiptV2:
    RECEIPT_TYPE: ClassVar[str] = "TerminalUniverseMissReceiptV2"

    head_sha: str
    evidence_class: str
    e1_authority: bool
    queue_authority: bool
    registry_id: str
    registry_version: int
    registry_digest: str
    terminal_universe_id: str
    terminal_universe_digest: str
    subject_kind: str
    subject_id: str
    subject_digest: str
    scheduler_input_digest: str
    owner_domain_id: str
    owner_domain_digest: str
    domain_membership_replay_id: str
    domain_membership_replay_artifact_digest: str
    domain_membership_replay_digest: str
    root_prime: int
    root_primality_verifier_id: str
    root_primality_verifier_artifact_digest: str
    root_primality_replay_digest: str
    natural_gap_start: int
    natural_gap_stop: int
    natural_gap_step: int
    natural_gap_count: int
    checked_gap_count: int
    checked_divisor_count: int
    hit_count: int
    range_definition_id: str
    range_definition_digest: str
    scan_algorithm_id: str
    scan_algorithm_digest: str
    factorization_verifier_id: str
    factorization_verifier_digest: str
    factorization_manifest_digest: str
    divisor_lattice_manifest_digest: str
    scan_transcript_digest: str
    reverse_equivalence_claim_id: str
    reverse_equivalence_claim_digest: str
    reverse_equivalence_proof_id: str
    reverse_equivalence_proof_digest: str
    reverse_equivalence_verifier_id: str
    reverse_equivalence_verifier_digest: str
    reverse_equivalence_replay_digest: str
    global_exhaustion: bool
    outcome: str
    digest: str


ScopeReceiptV2 = RegisteredPriorityPrefixMissReceiptV2 | TerminalUniverseMissReceiptV2
ReceiptT = TypeVar(
    "ReceiptT", RegisteredPriorityPrefixMissReceiptV2, TerminalUniverseMissReceiptV2
)


_TUPLE_FIELDS = frozenset(
    {
        "ordered_gaps",
        "ordered_family_ids",
        "ordered_family_definition_digests",
        "ordered_local_miss_digests",
    }
)


def _unsigned_receipt_mapping_v2(receipt: ScopeReceiptV2) -> dict[str, Any]:
    result: dict[str, Any] = {
        "receipt_type": receipt.RECEIPT_TYPE,
        "schema_version": SCHEMA_VERSION,
    }
    for field in fields(receipt):
        if field.name == "digest":
            continue
        result[field.name] = _json_copy(getattr(receipt, field.name))
    return result


def receipt_to_mapping_v2(receipt: ScopeReceiptV2) -> dict[str, Any]:
    parsed = parse_terminal_miss_scope_receipt_v2(receipt)
    result = _unsigned_receipt_mapping_v2(parsed)
    result["digest"] = parsed.digest
    return result


def _check_canonical_seal_v2(receipt: ScopeReceiptV2) -> None:
    _require_digest(receipt.digest, "digest")
    expected = canonical_digest_v2(_unsigned_receipt_mapping_v2(receipt))
    if receipt.digest != expected:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.DIGEST_MISMATCH,
            "receipt digest does not replay",
        )


def _expected_mapping_fields(cls: type[ReceiptT]) -> frozenset[str]:
    return frozenset(
        {"receipt_type", "schema_version", *(field.name for field in fields(cls))}
    )


def _parse_exact_v2(value: Any, cls: type[ReceiptT]) -> ReceiptT:
    if is_dataclass(value):
        if type(value) is not cls:
            code = (
                TerminalMissScopeRejectCode.SUBCLASS_REJECTED
                if isinstance(value, cls)
                else TerminalMissScopeRejectCode.RECEIPT_TYPE_MISMATCH
            )
            raise TerminalMissScopeValidationError(
                code,
                f"expected exact {cls.__name__}, got {type(value).__name__}",
            )
        receipt = value
    else:
        if type(value) is not dict:
            raise TerminalMissScopeValidationError(
                TerminalMissScopeRejectCode.INPUT_NOT_EXACT_TYPE,
                "receipt must be an exact v2 dataclass or a plain JSON object",
            )
        _json_copy(value)
        receipt_type = value.get("receipt_type")
        if receipt_type in {
            "LocalTerminalMissReceiptV1",
            "CompleteTerminalMissReceiptV1",
            "TerminalMissV1",
        }:
            raise TerminalMissScopeValidationError(
                TerminalMissScopeRejectCode.LEGACY_OR_LOCAL_RECEIPT,
                f"{receipt_type} cannot enter the v2 scope taxonomy",
            )
        if receipt_type != cls.RECEIPT_TYPE:
            raise TerminalMissScopeValidationError(
                TerminalMissScopeRejectCode.RECEIPT_TYPE_MISMATCH,
                f"expected {cls.RECEIPT_TYPE}, got {receipt_type!r}",
            )
        version = value.get("schema_version")
        if not _plain_int(version) or version != SCHEMA_VERSION:
            raise TerminalMissScopeValidationError(
                TerminalMissScopeRejectCode.SCHEMA_VERSION_MISMATCH,
                "schema_version must be the integer 2, not bool",
            )
        expected = _expected_mapping_fields(cls)
        actual = frozenset(value)
        if actual != expected:
            raise TerminalMissScopeValidationError(
                TerminalMissScopeRejectCode.FIELD_SET_MISMATCH,
                f"missing={sorted(expected - actual)}, extra={sorted(actual - expected)}",
            )
        values: dict[str, Any] = {}
        for field in fields(cls):
            child = value[field.name]
            if field.name in _TUPLE_FIELDS:
                if type(child) is not list:
                    raise TerminalMissScopeValidationError(
                        TerminalMissScopeRejectCode.MALFORMED_FIELD,
                        f"{field.name} must be a JSON array",
                    )
                child = tuple(child)
            values[field.name] = child
        receipt = cls(**values)
    _validate_common_v2(receipt)
    if type(receipt) is RegisteredPriorityPrefixMissReceiptV2:
        _validate_prefix_v2(receipt)
    else:
        _validate_universe_v2(receipt)
    _check_canonical_seal_v2(receipt)
    return receipt


def _validate_common_v2(receipt: ScopeReceiptV2) -> None:
    _require_head(receipt.head_sha)
    _require_text(receipt.evidence_class, "evidence_class")
    if receipt.evidence_class != EVIDENCE_ONLY:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            "v2 scope receipts are evidence-only",
        )
    _require_exact_bool(receipt.e1_authority, False, "e1_authority")
    _require_exact_bool(receipt.queue_authority, False, "queue_authority")
    _require_text(receipt.registry_id, "registry_id")
    if (
        receipt.registry_id != COORDINATOR_ROLE_REGISTRY_ID_V2
        or not _plain_int(receipt.registry_version)
        or receipt.registry_version != COORDINATOR_ROLE_REGISTRY_VERSION_V2
    ):
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            "receipt must name the still-ungranted coordinator role registry v2",
        )
    _require_digest(receipt.registry_digest, "registry_digest")
    _require_text(receipt.subject_kind, "subject_kind")
    if receipt.subject_kind not in SUBJECT_KINDS:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.MALFORMED_FIELD,
            "subject_kind is not SOURCE_STATE or TARGET_PROJECTION",
        )
    for name in (
        "subject_id",
        "owner_domain_id",
        "domain_membership_replay_id",
    ):
        _require_text(getattr(receipt, name), name)
    for name in (
        "subject_digest",
        "scheduler_input_digest",
        "owner_domain_digest",
        "domain_membership_replay_artifact_digest",
        "domain_membership_replay_digest",
    ):
        _require_digest(getattr(receipt, name), name)


def _validate_prefix_v2(receipt: RegisteredPriorityPrefixMissReceiptV2) -> None:
    for name in (
        "schedule_id",
        "coverage_theorem_id",
        "coverage_reproduction_id",
        "coverage_verifier_id",
    ):
        _require_text(getattr(receipt, name), name)
    for name in (
        "schedule_digest",
        "coverage_theorem_digest",
        "coverage_reproduction_digest",
        "coverage_verifier_digest",
        "coverage_replay_digest",
    ):
        _require_digest(getattr(receipt, name), name)
    tuple_fields = (
        receipt.ordered_gaps,
        receipt.ordered_family_ids,
        receipt.ordered_family_definition_digests,
        receipt.ordered_local_miss_digests,
    )
    if any(type(value) is not tuple for value in tuple_fields):
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.MALFORMED_FIELD,
            "parsed prefix sequence fields must be exact tuples",
        )
    gaps, families, definitions, misses = tuple_fields
    for index, gap in enumerate(gaps):
        _require_plain_int(gap, f"ordered_gaps[{index}]", 3)
    if not gaps or not (len(gaps) == len(families) == len(definitions) == len(misses)):
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.MALFORMED_FIELD,
            "prefix needs one family definition and local miss per ordered gap",
        )
    if gaps != tuple(range(3, gaps[-1] + 1, 4)):
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            "ordered_gaps must be the contiguous natural prefix 3,7,11,...",
        )
    if len(families) != len(set(families)):
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.MALFORMED_FIELD,
            "ordered_family_ids contains a duplicate",
        )
    for family_id in families:
        _require_text(family_id, "ordered family ID")
    for digest in (*definitions, *misses):
        _require_digest(digest, "ordered family/local miss digest")
    _require_plain_int(receipt.next_unchecked_gap, "next_unchecked_gap", 3)
    if receipt.next_unchecked_gap != gaps[-1] + 4:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            "next_unchecked_gap must immediately follow the registered prefix",
        )
    _require_text(receipt.coverage_semantics, "coverage_semantics")
    if receipt.coverage_semantics != REGISTERED_PRIORITY_ONLY:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            "prefix coverage must be REGISTERED_PRIORITY_ONLY",
        )
    _require_exact_bool(receipt.global_exhaustion, False, "global_exhaustion")
    _require_text(receipt.outcome, "outcome")
    if receipt.outcome != MISS_REGISTERED_PRIORITY_COMPLETE:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            "prefix receipt has the wrong outcome",
        )


def _validate_universe_v2(receipt: TerminalUniverseMissReceiptV2) -> None:
    for name in (
        "terminal_universe_id",
        "root_primality_verifier_id",
        "range_definition_id",
        "scan_algorithm_id",
        "factorization_verifier_id",
        "reverse_equivalence_claim_id",
        "reverse_equivalence_proof_id",
        "reverse_equivalence_verifier_id",
    ):
        _require_text(getattr(receipt, name), name)
    for name in (
        "terminal_universe_digest",
        "root_primality_verifier_artifact_digest",
        "root_primality_replay_digest",
        "range_definition_digest",
        "scan_algorithm_digest",
        "factorization_verifier_digest",
        "factorization_manifest_digest",
        "divisor_lattice_manifest_digest",
        "scan_transcript_digest",
        "reverse_equivalence_claim_digest",
        "reverse_equivalence_proof_digest",
        "reverse_equivalence_verifier_digest",
        "reverse_equivalence_replay_digest",
    ):
        _require_digest(getattr(receipt, name), name)
    prime = _require_plain_int(receipt.root_prime, "root_prime", 2)
    if prime % 24 != 1:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            "root_prime must lie in the core class 1 modulo 24",
        )
    for name, expected in (
        ("natural_gap_start", 3),
        ("natural_gap_stop", prime - 2),
        ("natural_gap_step", 4),
        ("natural_gap_count", (prime - 1) // 4),
        ("checked_gap_count", (prime - 1) // 4),
        ("hit_count", 0),
    ):
        actual = _require_plain_int(getattr(receipt, name), name, 0)
        if actual != expected:
            raise TerminalMissScopeValidationError(
                TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
                f"{name} must be {expected}, got {actual}",
            )
    checked_divisors = _require_plain_int(
        receipt.checked_divisor_count, "checked_divisor_count", 1
    )
    if checked_divisors < receipt.checked_gap_count:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            "a full divisor scan must check at least one divisor per gap",
        )
    _require_exact_bool(receipt.global_exhaustion, True, "global_exhaustion")
    _require_text(receipt.outcome, "outcome")
    if receipt.outcome != TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
            "universe receipt must remain explicitly evidence-only",
        )


def parse_registered_priority_prefix_miss_receipt_v2(
    value: Any,
) -> RegisteredPriorityPrefixMissReceiptV2:
    return _parse_exact_v2(value, RegisteredPriorityPrefixMissReceiptV2)


def parse_terminal_universe_miss_receipt_v2(
    value: Any,
) -> TerminalUniverseMissReceiptV2:
    return _parse_exact_v2(value, TerminalUniverseMissReceiptV2)


def parse_terminal_miss_scope_receipt_v2(value: Any) -> ScopeReceiptV2:
    if type(value) is RegisteredPriorityPrefixMissReceiptV2:
        return parse_registered_priority_prefix_miss_receipt_v2(value)
    if type(value) is TerminalUniverseMissReceiptV2:
        return parse_terminal_universe_miss_receipt_v2(value)
    if is_dataclass(value):
        if isinstance(value, (RegisteredPriorityPrefixMissReceiptV2, TerminalUniverseMissReceiptV2)):
            raise TerminalMissScopeValidationError(
                TerminalMissScopeRejectCode.SUBCLASS_REJECTED,
                "receipt subclasses cannot add authority",
            )
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.LEGACY_OR_LOCAL_RECEIPT,
            f"unsupported receipt dataclass {type(value).__name__}",
        )
    if type(value) is not dict:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.INPUT_NOT_EXACT_TYPE,
            "receipt must be a plain JSON object",
        )
    receipt_type = value.get("receipt_type")
    if receipt_type == RegisteredPriorityPrefixMissReceiptV2.RECEIPT_TYPE:
        return parse_registered_priority_prefix_miss_receipt_v2(value)
    if receipt_type == TerminalUniverseMissReceiptV2.RECEIPT_TYPE:
        return parse_terminal_universe_miss_receipt_v2(value)
    raise TerminalMissScopeValidationError(
        TerminalMissScopeRejectCode.LEGACY_OR_LOCAL_RECEIPT,
        f"receipt type {receipt_type!r} has no v2 scope authority",
    )


def reject_producer_continuation_v2(value: Any) -> NoReturn:
    receipt = parse_terminal_miss_scope_receipt_v2(value)
    if type(receipt) is TerminalUniverseMissReceiptV2:
        raise TerminalMissScopeValidationError(
            TerminalMissScopeRejectCode.TERMINAL_UNIVERSE_FORBIDS_PRODUCER,
            "universe-miss evidence can never continue to a producer",
        )
    raise TerminalMissScopeValidationError(
        TerminalMissScopeRejectCode.REGISTRY_V2_AUTHORIZATION_REQUIRED,
        "a prefix-complete miss needs a future HEAD-bound registry-v2 grant before E1 use",
    )


def scope_taxonomy_summary_v2() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "registry_id_required": COORDINATOR_ROLE_REGISTRY_ID_V2,
        "production_issuer_present": False,
        "semantic_verifier_present": False,
        "declared_artifacts_executed": False,
        "shape_only": True,
        "e1_authority_present": False,
        "queue_authority_present": False,
        "prefix_outcome": MISS_REGISTERED_PRIORITY_COMPLETE,
        "prefix_global_exhaustion": False,
        "universe_outcome": TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY,
        "universe_global_exhaustion": True,
    }


__all__ = [
    "COORDINATOR_ROLE_REGISTRY_ID_V2",
    "EVIDENCE_ONLY",
    "MISS_REGISTERED_PRIORITY_COMPLETE",
    "REGISTERED_PRIORITY_ONLY",
    "TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY",
    "RegisteredPriorityPrefixMissReceiptV2",
    "SOURCE_STATE",
    "TARGET_PROJECTION",
    "TerminalMissScopeRejectCode",
    "TerminalMissScopeValidationError",
    "TerminalUniverseMissReceiptV2",
    "canonical_digest_v2",
    "canonical_json_v2",
    "parse_registered_priority_prefix_miss_receipt_v2",
    "parse_terminal_miss_scope_receipt_v2",
    "parse_terminal_universe_miss_receipt_v2",
    "receipt_to_mapping_v2",
    "reject_producer_continuation_v2",
    "scope_taxonomy_summary_v2",
]
