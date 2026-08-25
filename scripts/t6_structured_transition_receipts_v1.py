#!/usr/bin/env python3
"""Content-bound E1--E5 receipts for T6 transition validation.

This module is deliberately independent of producer registration and queue
mutation.  It turns replay results supplied by a coordinator-owned caller into
sealed receipts, and verifies those receipts against the same caller-owned
inputs and artifact pins.  A content digest detects mutation; it does not grant
authority.  In particular, a track-local claim, validator, projector, grammar,
or taxonomy is rejected unless its exact ID and digest are already pinned by
the caller.

The current runtime's ``TransitionValidationV1`` remains a legacy shape.  Use
``verify_structured_transition_evidence_v1`` as the migration boundary: it
rejects the old E1--E4 booleans and accepts only a complete replayed bundle.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass, fields, replace
from enum import Enum
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, Sequence, TypeVar


SCHEMA_VERSION = 1
ROOT_INITIALIZER = "ROOT_INITIALIZER"
MISS_COMPLETE = "MISS_COMPLETE"
PARENT_TO_FINAL_TARGET = "PARENT_TO_FINAL_TARGET"

T5_TICKET_TYPES = frozenset({"OUTER_RANK_DROP", "PHASE_DROP", "LOCAL_DROP"})

NEGATIVE_MUTATION_IDS = frozenset(
    {
        "CONTROL_AS_ACTUAL_BY_LABEL",
        "LOCAL_MISS_AS_GLOBAL_MISS",
        "SELF_REGISTERED_PRODUCER",
        "SELF_REGISTERED_VALIDATOR",
        "SOURCE_DIGEST_SWAP",
        "OCCURRENCE_PATH_SWAP",
        "CLAIM_HASH_DRIFT",
        "PROJECTOR_HASH_DRIFT",
        "GRAMMAR_HASH_DRIFT",
        "T5_TAXONOMY_DRIFT",
        "PARENT_TRANSITION_REPLAY_BREAK",
    }
)


class ReceiptRejectCode(str, Enum):
    INPUT_NOT_MAPPING = "INPUT_NOT_MAPPING"
    UNKNOWN_RECEIPT_TYPE = "UNKNOWN_RECEIPT_TYPE"
    UNKNOWN_SCHEMA_VERSION = "UNKNOWN_SCHEMA_VERSION"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    UNTRUSTED_ARTIFACT = "UNTRUSTED_ARTIFACT"
    SOURCE_BINDING_MISMATCH = "SOURCE_BINDING_MISMATCH"
    PARENT_BINDING_MISMATCH = "PARENT_BINDING_MISMATCH"
    OCCURRENCE_REPLAY_FAILED = "OCCURRENCE_REPLAY_FAILED"
    TERMINAL_BINDING_MISMATCH = "TERMINAL_BINDING_MISMATCH"
    PROJECTION_BINDING_MISMATCH = "PROJECTION_BINDING_MISMATCH"
    TYPING_BINDING_MISMATCH = "TYPING_BINDING_MISMATCH"
    LIFT_BINDING_MISMATCH = "LIFT_BINDING_MISMATCH"
    TICKET_BINDING_MISMATCH = "TICKET_BINDING_MISMATCH"
    CROSS_RECEIPT_MISMATCH = "CROSS_RECEIPT_MISMATCH"
    LEGACY_BOOLEAN_VALIDATION = "LEGACY_BOOLEAN_VALIDATION"
    UNKNOWN_NEGATIVE_MUTATION = "UNKNOWN_NEGATIVE_MUTATION"


class ReceiptValidationError(ValueError):
    """Fail-closed receipt error with a stable machine-readable code."""

    def __init__(self, code: ReceiptRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


PathSegmentV1 = str | int


def _json_copy(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, child in value.items():
            if not isinstance(key, str):
                raise ReceiptValidationError(
                    ReceiptRejectCode.MALFORMED_FIELD,
                    "canonical JSON object keys must be strings",
                )
            result[key] = _json_copy(child)
        return result
    if isinstance(value, (list, tuple)):
        return [_json_copy(child) for child in value]
    if value is None or isinstance(value, (str, bool, int, float)):
        return copy.deepcopy(value)
    raise ReceiptValidationError(
        ReceiptRejectCode.MALFORMED_FIELD,
        f"value of type {type(value).__name__} is not canonical JSON",
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
    """Return the single canonical JSON representation used by this layer."""

    try:
        return json.dumps(
            _json_copy(value),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise ReceiptValidationError(
            ReceiptRejectCode.MALFORMED_FIELD,
            f"value is not canonical JSON: {exc}",
        ) from exc


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


def _is_digest(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    return all(character in "0123456789abcdef" for character in value)


def _require_digest(value: Any, name: str) -> str:
    if not _is_digest(value):
        raise ReceiptValidationError(
            ReceiptRejectCode.MALFORMED_FIELD,
            f"{name} must be a lowercase SHA-256 digest",
        )
    return value


def _require_text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise ReceiptValidationError(
            ReceiptRejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty string",
        )
    return value


def _plain_nonnegative_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


@dataclass(frozen=True)
class ArtifactDigestManifestV1:
    """Caller-owned artifact pins; constructing a receipt cannot extend them."""

    digests: Mapping[str, str]

    def __post_init__(self) -> None:
        normalized = dict(self.digests)
        for artifact_id, digest in normalized.items():
            _require_text(artifact_id, "artifact ID")
            _require_digest(digest, f"artifact {artifact_id!r} digest")
        object.__setattr__(self, "digests", MappingProxyType(normalized))

    def digest_for(self, artifact_id: str) -> str:
        digest = self.digests.get(artifact_id)
        if digest is None:
            raise ReceiptValidationError(
                ReceiptRejectCode.UNTRUSTED_ARTIFACT,
                f"artifact {artifact_id!r} is not coordinator-pinned",
            )
        return digest

    def require(self, artifact_id: str, digest: str) -> None:
        if self.digest_for(artifact_id) != digest:
            raise ReceiptValidationError(
                ReceiptRejectCode.UNTRUSTED_ARTIFACT,
                f"artifact {artifact_id!r} digest does not match its pin",
            )


@dataclass(frozen=True)
class TransitionReplayContextV1:
    """Trusted replay inputs assembled outside the producer under review."""

    source_state_id: str
    source_state_payload: Any
    parent_transition_id: str
    parent_transition_payload: Mapping[str, Any] | None
    producer_id: str
    branch_id: str
    scope: str
    occurrence_path: tuple[PathSegmentV1, ...]
    provenance_payload: Any
    source_terminal_schedule_id: str
    source_terminal_result: str
    source_terminal_result_payload: Any
    candidate_witness_payload: Any
    target_projection_payload: Mapping[str, Any]
    family_predicate_results: Mapping[str, bool]
    target_owner: str
    target_owner_digest: str
    source_equation_interface: Any
    target_equation_interface: Any
    source_potential_receipt: Mapping[str, Any]
    target_potential_receipt: Mapping[str, Any]
    universal_quantifier_statement: str
    negative_mutation_ids: tuple[str, ...]
    ticket_type: str
    claim_id: str
    reproduction_id: str
    independent_verifier_id: str
    projector_id: str
    tie_break_rule_id: str
    normal_form_verifier_id: str
    precedence_table_id: str
    grammar_id: str
    admission_gate_id: str
    admission_gate_version: int
    lift_map_id: str
    symbolic_verifier_id: str
    lift_reproduction_id: str
    taxonomy_id: str

    def __post_init__(self) -> None:
        text_fields = (
            "source_state_id",
            "parent_transition_id",
            "producer_id",
            "branch_id",
            "scope",
            "source_terminal_schedule_id",
            "source_terminal_result",
            "target_owner",
            "universal_quantifier_statement",
            "ticket_type",
            "claim_id",
            "reproduction_id",
            "independent_verifier_id",
            "projector_id",
            "tie_break_rule_id",
            "normal_form_verifier_id",
            "precedence_table_id",
            "grammar_id",
            "admission_gate_id",
            "lift_map_id",
            "symbolic_verifier_id",
            "lift_reproduction_id",
            "taxonomy_id",
        )
        for name in text_fields:
            _require_text(getattr(self, name), f"replay context {name}")
        _require_digest(self.target_owner_digest, "replay context target_owner_digest")
        if (
            not isinstance(self.admission_gate_version, int)
            or isinstance(self.admission_gate_version, bool)
            or self.admission_gate_version < 1
        ):
            raise ReceiptValidationError(
                ReceiptRejectCode.MALFORMED_FIELD,
                "replay context admission_gate_version must be positive",
            )
        payload_fields = (
            "source_state_payload",
            "provenance_payload",
            "source_terminal_result_payload",
            "candidate_witness_payload",
            "target_projection_payload",
            "source_equation_interface",
            "target_equation_interface",
            "source_potential_receipt",
            "target_potential_receipt",
        )
        for name in payload_fields:
            object.__setattr__(self, name, _freeze_json(getattr(self, name)))
        for name in (
            "source_state_payload",
            "target_projection_payload",
            "source_potential_receipt",
            "target_potential_receipt",
        ):
            if not isinstance(getattr(self, name), Mapping):
                raise ReceiptValidationError(
                    ReceiptRejectCode.MALFORMED_FIELD,
                    f"replay context {name} must be an object",
                )
        if self.parent_transition_payload is not None:
            object.__setattr__(
                self,
                "parent_transition_payload",
                _freeze_json(self.parent_transition_payload),
            )
        object.__setattr__(self, "occurrence_path", tuple(self.occurrence_path))
        if any(
            not isinstance(segment, str)
            and not (
                isinstance(segment, int)
                and not isinstance(segment, bool)
                and segment >= 0
            )
            for segment in self.occurrence_path
        ):
            raise ReceiptValidationError(
                ReceiptRejectCode.MALFORMED_FIELD,
                "replay context occurrence_path has an invalid segment",
            )
        object.__setattr__(
            self, "negative_mutation_ids", tuple(self.negative_mutation_ids)
        )
        predicates = dict(self.family_predicate_results)
        if not predicates or any(
            not isinstance(key, str)
            or not key
            or not isinstance(value, bool)
            for key, value in predicates.items()
        ):
            raise ReceiptValidationError(
                ReceiptRejectCode.MALFORMED_FIELD,
                "family predicate results must be a nonempty string-to-bool mapping",
            )
        object.__setattr__(
            self, "family_predicate_results", MappingProxyType(predicates)
        )


@dataclass(frozen=True)
class E1OccurrenceReceiptV1:
    RECEIPT_TYPE: ClassVar[str] = "E1OccurrenceReceiptV1"

    source_state_id: str
    source_state_digest: str
    parent_transition_id: str
    parent_transition_digest: str
    producer_id: str
    producer_digest: str
    branch_id: str
    scope: str
    occurrence_path: tuple[PathSegmentV1, ...]
    occurrence_value: Any
    provenance_digest: str
    source_terminal_schedule_id: str
    source_terminal_schedule_digest: str
    source_terminal_result: str
    source_terminal_result_digest: str
    claim_id: str
    claim_digest: str
    reproduction_id: str
    reproduction_digest: str
    independent_verifier_id: str
    independent_verifier_digest: str
    digest: str


@dataclass(frozen=True)
class E2ProjectionReceiptV1:
    RECEIPT_TYPE: ClassVar[str] = "E2ProjectionReceiptV1"

    source_state_id: str
    source_state_digest: str
    producer_id: str
    branch_id: str
    candidate_witness_digest: str
    projector_id: str
    projector_digest: str
    tie_break_rule_id: str
    tie_break_rule_digest: str
    canonical_target_payload: Mapping[str, Any]
    target_projection_digest: str
    digest: str


@dataclass(frozen=True)
class E3TypingReceiptV1:
    RECEIPT_TYPE: ClassVar[str] = "E3TypingReceiptV1"

    target_state_id: str
    target_projection_digest: str
    target_schema_id: str
    target_schema_version: int
    normal_form_verifier_id: str
    normal_form_verifier_digest: str
    family_predicate_results: Mapping[str, bool]
    precedence_table_id: str
    precedence_table_digest: str
    owner: str
    owner_digest: str
    grammar_id: str
    grammar_digest: str
    admission_gate_id: str
    admission_gate_version: int
    admission_gate_digest: str
    digest: str


@dataclass(frozen=True)
class E4LiftReceiptV1:
    RECEIPT_TYPE: ClassVar[str] = "E4LiftReceiptV1"

    source_state_id: str
    target_state_id: str
    source_equation_interface: Any
    source_equation_interface_digest: str
    target_equation_interface: Any
    target_equation_interface_digest: str
    lift_map_id: str
    lift_map_digest: str
    universal_quantifier_statement: str
    symbolic_verifier_id: str
    symbolic_verifier_digest: str
    reproduction_id: str
    reproduction_digest: str
    negative_mutation_ids: tuple[str, ...]
    digest: str


@dataclass(frozen=True)
class E5TicketReceiptV1:
    RECEIPT_TYPE: ClassVar[str] = "E5TicketReceiptV1"

    source_state_id: str
    target_state_id: str
    source_potential_receipt: Mapping[str, Any]
    source_potential_receipt_digest: str
    target_potential_receipt: Mapping[str, Any]
    target_potential_receipt_digest: str
    ticket_type: str
    taxonomy_id: str
    taxonomy_digest: str
    source_coordinates: tuple[int, int, int, int, int, int, int]
    target_coordinates: tuple[int, int, int, int, int, int, int]
    first_decreasing_coordinate: int
    comparison_scope: str
    parent_to_final_assertion_digest: str
    digest: str


@dataclass(frozen=True)
class VerifiedTransitionBundleV1:
    RECEIPT_TYPE: ClassVar[str] = "VerifiedTransitionBundleV1"

    transition_id: str
    source_state_id: str
    source_state_digest: str
    target_state_id: str
    producer_id: str
    branch_id: str
    target_projection_digest: str
    e1_occurrence: E1OccurrenceReceiptV1
    e2_projection: E2ProjectionReceiptV1
    e3_typing: E3TypingReceiptV1
    e4_lift: E4LiftReceiptV1
    e5_ticket: E5TicketReceiptV1
    digest: str


LeafReceiptV1 = (
    E1OccurrenceReceiptV1
    | E2ProjectionReceiptV1
    | E3TypingReceiptV1
    | E4LiftReceiptV1
    | E5TicketReceiptV1
)
ReceiptV1 = LeafReceiptV1 | VerifiedTransitionBundleV1
ReceiptT = TypeVar("ReceiptT", bound=ReceiptV1)


def _unsigned_receipt_mapping_v1(receipt: ReceiptV1) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "receipt_type": receipt.RECEIPT_TYPE,
        "schema_version": SCHEMA_VERSION,
    }
    for field in fields(receipt):
        if field.name == "digest":
            continue
        value = getattr(receipt, field.name)
        if isinstance(
            value,
            (
                E1OccurrenceReceiptV1,
                E2ProjectionReceiptV1,
                E3TypingReceiptV1,
                E4LiftReceiptV1,
                E5TicketReceiptV1,
            ),
        ):
            payload[field.name] = receipt_to_mapping_v1(value)
        else:
            payload[field.name] = _json_copy(value)
    return payload


def receipt_to_mapping_v1(receipt: ReceiptV1) -> dict[str, Any]:
    payload = _unsigned_receipt_mapping_v1(receipt)
    payload["digest"] = receipt.digest
    return payload


def _seal_dataclass_v1(cls: type[ReceiptT], **values: Any) -> ReceiptT:
    draft = cls(**values, digest="")
    return replace(draft, digest=canonical_digest_v1(_unsigned_receipt_mapping_v1(draft)))


def _verify_receipt_seal_v1(receipt: ReceiptV1) -> None:
    _require_digest(receipt.digest, f"{receipt.RECEIPT_TYPE}.digest")
    expected = canonical_digest_v1(_unsigned_receipt_mapping_v1(receipt))
    if receipt.digest != expected:
        raise ReceiptValidationError(
            ReceiptRejectCode.DIGEST_MISMATCH,
            f"{receipt.RECEIPT_TYPE}.digest does not replay",
        )


def _parse_leaf_v1(value: Any, cls: type[ReceiptT]) -> ReceiptT:
    if isinstance(value, cls):
        _verify_receipt_seal_v1(value)
        return value
    if not isinstance(value, Mapping):
        raise ReceiptValidationError(
            ReceiptRejectCode.INPUT_NOT_MAPPING,
            f"{cls.RECEIPT_TYPE} must be a mapping",
        )
    expected = {field.name for field in fields(cls)} | {
        "receipt_type",
        "schema_version",
    }
    if set(value) != expected:
        raise ReceiptValidationError(
            ReceiptRejectCode.FIELD_SET_MISMATCH,
            f"{cls.RECEIPT_TYPE} fields differ from the v1 schema",
        )
    if value.get("receipt_type") != cls.RECEIPT_TYPE:
        raise ReceiptValidationError(
            ReceiptRejectCode.UNKNOWN_RECEIPT_TYPE,
            f"expected {cls.RECEIPT_TYPE}",
        )
    if value.get("schema_version") != SCHEMA_VERSION:
        raise ReceiptValidationError(
            ReceiptRejectCode.UNKNOWN_SCHEMA_VERSION,
            f"{cls.RECEIPT_TYPE} is not schema version 1",
        )
    try:
        kwargs = {field.name: value[field.name] for field in fields(cls)}
        if cls is E1OccurrenceReceiptV1:
            kwargs["occurrence_path"] = tuple(kwargs["occurrence_path"])
            kwargs["occurrence_value"] = _freeze_json(kwargs["occurrence_value"])
        elif cls is E2ProjectionReceiptV1:
            kwargs["canonical_target_payload"] = _freeze_json(
                kwargs["canonical_target_payload"]
            )
        elif cls is E3TypingReceiptV1:
            kwargs["family_predicate_results"] = MappingProxyType(
                dict(kwargs["family_predicate_results"])
            )
        elif cls is E4LiftReceiptV1:
            kwargs["source_equation_interface"] = _freeze_json(
                kwargs["source_equation_interface"]
            )
            kwargs["target_equation_interface"] = _freeze_json(
                kwargs["target_equation_interface"]
            )
            kwargs["negative_mutation_ids"] = tuple(kwargs["negative_mutation_ids"])
        elif cls is E5TicketReceiptV1:
            kwargs["source_potential_receipt"] = _freeze_json(
                kwargs["source_potential_receipt"]
            )
            kwargs["target_potential_receipt"] = _freeze_json(
                kwargs["target_potential_receipt"]
            )
            kwargs["source_coordinates"] = tuple(kwargs["source_coordinates"])
            kwargs["target_coordinates"] = tuple(kwargs["target_coordinates"])
        receipt = cls(**kwargs)
    except ReceiptValidationError:
        raise
    except (TypeError, ValueError) as exc:
        raise ReceiptValidationError(
            ReceiptRejectCode.MALFORMED_FIELD,
            f"{cls.RECEIPT_TYPE} contains a malformed structured field",
        ) from exc
    _verify_receipt_seal_v1(receipt)
    return receipt


def parse_verified_transition_bundle_v1(value: Any) -> VerifiedTransitionBundleV1:
    if isinstance(value, VerifiedTransitionBundleV1):
        _verify_receipt_seal_v1(value)
        return value
    if not isinstance(value, Mapping):
        raise ReceiptValidationError(
            ReceiptRejectCode.INPUT_NOT_MAPPING,
            "VerifiedTransitionBundleV1 must be a mapping",
        )
    expected = {field.name for field in fields(VerifiedTransitionBundleV1)} | {
        "receipt_type",
        "schema_version",
    }
    if set(value) != expected:
        raise ReceiptValidationError(
            ReceiptRejectCode.FIELD_SET_MISMATCH,
            "VerifiedTransitionBundleV1 fields differ from the v1 schema",
        )
    if value.get("receipt_type") != VerifiedTransitionBundleV1.RECEIPT_TYPE:
        raise ReceiptValidationError(
            ReceiptRejectCode.UNKNOWN_RECEIPT_TYPE,
            "expected VerifiedTransitionBundleV1",
        )
    if value.get("schema_version") != SCHEMA_VERSION:
        raise ReceiptValidationError(
            ReceiptRejectCode.UNKNOWN_SCHEMA_VERSION,
            "VerifiedTransitionBundleV1 is not schema version 1",
        )
    bundle = VerifiedTransitionBundleV1(
        transition_id=value["transition_id"],
        source_state_id=value["source_state_id"],
        source_state_digest=value["source_state_digest"],
        target_state_id=value["target_state_id"],
        producer_id=value["producer_id"],
        branch_id=value["branch_id"],
        target_projection_digest=value["target_projection_digest"],
        e1_occurrence=_parse_leaf_v1(value["e1_occurrence"], E1OccurrenceReceiptV1),
        e2_projection=_parse_leaf_v1(value["e2_projection"], E2ProjectionReceiptV1),
        e3_typing=_parse_leaf_v1(value["e3_typing"], E3TypingReceiptV1),
        e4_lift=_parse_leaf_v1(value["e4_lift"], E4LiftReceiptV1),
        e5_ticket=_parse_leaf_v1(value["e5_ticket"], E5TicketReceiptV1),
        digest=value["digest"],
    )
    _verify_receipt_seal_v1(bundle)
    return bundle


def _resolve_occurrence_path_v1(source: Any, path: Sequence[PathSegmentV1]) -> Any:
    current = source
    for index, segment in enumerate(path):
        if isinstance(segment, str) and isinstance(current, Mapping):
            if segment not in current:
                raise ReceiptValidationError(
                    ReceiptRejectCode.OCCURRENCE_REPLAY_FAILED,
                    f"occurrence path segment {index} does not exist",
                )
            current = current[segment]
        elif (
            isinstance(segment, int)
            and not isinstance(segment, bool)
            and isinstance(current, (list, tuple))
            and 0 <= segment < len(current)
        ):
            current = current[segment]
        else:
            raise ReceiptValidationError(
                ReceiptRejectCode.OCCURRENCE_REPLAY_FAILED,
                f"occurrence path segment {index} has the wrong container or type",
            )
    return _freeze_json(current)


def _sealed_mapping_digest_v1(value: Mapping[str, Any], name: str) -> str:
    payload = _json_copy(value)
    digest = payload.pop("digest", None)
    _require_digest(digest, f"{name}.digest")
    if canonical_digest_v1(payload) != digest:
        raise ReceiptValidationError(
            ReceiptRejectCode.DIGEST_MISMATCH,
            f"{name}.digest does not replay",
        )
    return digest


def _parent_digest_v1(context: TransitionReplayContextV1) -> str:
    if context.parent_transition_id == ROOT_INITIALIZER:
        if context.parent_transition_payload is not None:
            raise ReceiptValidationError(
                ReceiptRejectCode.PARENT_BINDING_MISMATCH,
                "ROOT_INITIALIZER cannot carry a parent transition payload",
            )
        return ROOT_INITIALIZER
    parent = context.parent_transition_payload
    if not isinstance(parent, Mapping):
        raise ReceiptValidationError(
            ReceiptRejectCode.PARENT_BINDING_MISMATCH,
            "non-root source requires a sealed parent transition",
        )
    if parent.get("transition_id") != context.parent_transition_id:
        raise ReceiptValidationError(
            ReceiptRejectCode.PARENT_BINDING_MISMATCH,
            "parent transition ID does not replay",
        )
    return _sealed_mapping_digest_v1(parent, "parent transition")


def _target_state_fields_v1(context: TransitionReplayContextV1) -> tuple[str, str, int]:
    target = context.target_projection_payload
    state_id = _require_text(target.get("state_id"), "target state_id")
    schema_id = _require_text(target.get("schema_id"), "target schema_id")
    schema_version = target.get("schema_version")
    if not isinstance(schema_version, int) or isinstance(schema_version, bool):
        raise ReceiptValidationError(
            ReceiptRejectCode.MALFORMED_FIELD,
            "target schema_version must be an integer",
        )
    return state_id, schema_id, schema_version


def _potential_receipt_v1(
    value: Mapping[str, Any], expected_state_id: str, name: str
) -> tuple[str, tuple[int, int, int, int, int, int, int]]:
    expected_fields = {
        "schema_id",
        "schema_version",
        "state_id",
        "coordinates",
        "digest",
    }
    if set(value) != expected_fields:
        raise ReceiptValidationError(
            ReceiptRejectCode.TICKET_BINDING_MISMATCH,
            f"{name} is not a t5_n7_potential_receipt_v1",
        )
    if (
        value.get("schema_id") != "t5_n7_potential_receipt_v1"
        or value.get("schema_version") != 1
        or value.get("state_id") != expected_state_id
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.TICKET_BINDING_MISMATCH,
            f"{name} metadata does not bind the expected state",
        )
    digest = _sealed_mapping_digest_v1(value, name)
    coordinates = value.get("coordinates")
    if (
        not isinstance(coordinates, (list, tuple))
        or len(coordinates) != 7
        or any(not _plain_nonnegative_int(item) for item in coordinates)
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.TICKET_BINDING_MISMATCH,
            f"{name} coordinates are not in N^7",
        )
    return digest, tuple(coordinates)  # type: ignore[return-value]


def _first_decreasing_coordinate_v1(
    source: Sequence[int], target: Sequence[int]
) -> int:
    for index, (source_value, target_value) in enumerate(zip(source, target)):
        if source_value != target_value:
            if target_value < source_value:
                return index
            break
    raise ReceiptValidationError(
        ReceiptRejectCode.TICKET_BINDING_MISMATCH,
        "target does not strictly decrease the parent N^7 potential",
    )


def _verify_ticket_type_v1(ticket_type: str, first_coordinate: int) -> None:
    if ticket_type not in T5_TICKET_TYPES:
        raise ReceiptValidationError(
            ReceiptRejectCode.TICKET_BINDING_MISMATCH,
            f"unknown T5 ticket type {ticket_type!r}",
        )
    allowed = {
        "OUTER_RANK_DROP": {0},
        "PHASE_DROP": {1, 2},
        "LOCAL_DROP": {3, 4, 5, 6},
    }[ticket_type]
    if first_coordinate not in allowed:
        raise ReceiptValidationError(
            ReceiptRejectCode.TICKET_BINDING_MISMATCH,
            f"{ticket_type} does not match the first decreasing coordinate",
        )


def _parent_to_final_assertion_digest_v1(
    *,
    source_state_id: str,
    target_state_id: str,
    source_receipt_digest: str,
    target_receipt_digest: str,
    ticket_type: str,
    taxonomy_id: str,
    taxonomy_digest: str,
    source_coordinates: Sequence[int],
    target_coordinates: Sequence[int],
    first_decreasing_coordinate: int,
) -> str:
    return canonical_digest_v1(
        {
            "comparison_scope": PARENT_TO_FINAL_TARGET,
            "source_state_id": source_state_id,
            "target_state_id": target_state_id,
            "source_potential_receipt_digest": source_receipt_digest,
            "target_potential_receipt_digest": target_receipt_digest,
            "ticket_type": ticket_type,
            "taxonomy_id": taxonomy_id,
            "taxonomy_digest": taxonomy_digest,
            "source_coordinates": list(source_coordinates),
            "target_coordinates": list(target_coordinates),
            "first_decreasing_coordinate": first_decreasing_coordinate,
        }
    )


def make_e1_occurrence_receipt_v1(
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
) -> E1OccurrenceReceiptV1:
    occurrence = _resolve_occurrence_path_v1(
        context.source_state_payload, context.occurrence_path
    )
    return _seal_dataclass_v1(
        E1OccurrenceReceiptV1,
        source_state_id=context.source_state_id,
        source_state_digest=canonical_digest_v1(context.source_state_payload),
        parent_transition_id=context.parent_transition_id,
        parent_transition_digest=_parent_digest_v1(context),
        producer_id=context.producer_id,
        producer_digest=artifacts.digest_for(context.producer_id),
        branch_id=context.branch_id,
        scope=context.scope,
        occurrence_path=context.occurrence_path,
        occurrence_value=occurrence,
        provenance_digest=canonical_digest_v1(context.provenance_payload),
        source_terminal_schedule_id=context.source_terminal_schedule_id,
        source_terminal_schedule_digest=artifacts.digest_for(
            context.source_terminal_schedule_id
        ),
        source_terminal_result=context.source_terminal_result,
        source_terminal_result_digest=canonical_digest_v1(
            context.source_terminal_result_payload
        ),
        claim_id=context.claim_id,
        claim_digest=artifacts.digest_for(context.claim_id),
        reproduction_id=context.reproduction_id,
        reproduction_digest=artifacts.digest_for(context.reproduction_id),
        independent_verifier_id=context.independent_verifier_id,
        independent_verifier_digest=artifacts.digest_for(
            context.independent_verifier_id
        ),
    )


def make_e2_projection_receipt_v1(
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
    e1: E1OccurrenceReceiptV1,
) -> E2ProjectionReceiptV1:
    return _seal_dataclass_v1(
        E2ProjectionReceiptV1,
        source_state_id=e1.source_state_id,
        source_state_digest=e1.source_state_digest,
        producer_id=e1.producer_id,
        branch_id=e1.branch_id,
        candidate_witness_digest=canonical_digest_v1(
            context.candidate_witness_payload
        ),
        projector_id=context.projector_id,
        projector_digest=artifacts.digest_for(context.projector_id),
        tie_break_rule_id=context.tie_break_rule_id,
        tie_break_rule_digest=artifacts.digest_for(context.tie_break_rule_id),
        canonical_target_payload=_freeze_json(context.target_projection_payload),
        target_projection_digest=canonical_digest_v1(
            context.target_projection_payload
        ),
    )


def make_e3_typing_receipt_v1(
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
    e2: E2ProjectionReceiptV1,
) -> E3TypingReceiptV1:
    target_state_id, schema_id, schema_version = _target_state_fields_v1(context)
    return _seal_dataclass_v1(
        E3TypingReceiptV1,
        target_state_id=target_state_id,
        target_projection_digest=e2.target_projection_digest,
        target_schema_id=schema_id,
        target_schema_version=schema_version,
        normal_form_verifier_id=context.normal_form_verifier_id,
        normal_form_verifier_digest=artifacts.digest_for(
            context.normal_form_verifier_id
        ),
        family_predicate_results=MappingProxyType(
            dict(context.family_predicate_results)
        ),
        precedence_table_id=context.precedence_table_id,
        precedence_table_digest=artifacts.digest_for(context.precedence_table_id),
        owner=context.target_owner,
        owner_digest=context.target_owner_digest,
        grammar_id=context.grammar_id,
        grammar_digest=artifacts.digest_for(context.grammar_id),
        admission_gate_id=context.admission_gate_id,
        admission_gate_version=context.admission_gate_version,
        admission_gate_digest=artifacts.digest_for(context.admission_gate_id),
    )


def make_e4_lift_receipt_v1(
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
    e1: E1OccurrenceReceiptV1,
    e3: E3TypingReceiptV1,
) -> E4LiftReceiptV1:
    return _seal_dataclass_v1(
        E4LiftReceiptV1,
        source_state_id=e1.source_state_id,
        target_state_id=e3.target_state_id,
        source_equation_interface=_freeze_json(context.source_equation_interface),
        source_equation_interface_digest=canonical_digest_v1(
            context.source_equation_interface
        ),
        target_equation_interface=_freeze_json(context.target_equation_interface),
        target_equation_interface_digest=canonical_digest_v1(
            context.target_equation_interface
        ),
        lift_map_id=context.lift_map_id,
        lift_map_digest=artifacts.digest_for(context.lift_map_id),
        universal_quantifier_statement=context.universal_quantifier_statement,
        symbolic_verifier_id=context.symbolic_verifier_id,
        symbolic_verifier_digest=artifacts.digest_for(
            context.symbolic_verifier_id
        ),
        reproduction_id=context.lift_reproduction_id,
        reproduction_digest=artifacts.digest_for(context.lift_reproduction_id),
        negative_mutation_ids=context.negative_mutation_ids,
    )


def make_e5_ticket_receipt_v1(
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
    e1: E1OccurrenceReceiptV1,
    e3: E3TypingReceiptV1,
) -> E5TicketReceiptV1:
    source_digest, source_coordinates = _potential_receipt_v1(
        context.source_potential_receipt, e1.source_state_id, "source potential"
    )
    target_digest, target_coordinates = _potential_receipt_v1(
        context.target_potential_receipt, e3.target_state_id, "target potential"
    )
    first = _first_decreasing_coordinate_v1(source_coordinates, target_coordinates)
    _verify_ticket_type_v1(context.ticket_type, first)
    taxonomy_digest = artifacts.digest_for(context.taxonomy_id)
    assertion_digest = _parent_to_final_assertion_digest_v1(
        source_state_id=e1.source_state_id,
        target_state_id=e3.target_state_id,
        source_receipt_digest=source_digest,
        target_receipt_digest=target_digest,
        ticket_type=context.ticket_type,
        taxonomy_id=context.taxonomy_id,
        taxonomy_digest=taxonomy_digest,
        source_coordinates=source_coordinates,
        target_coordinates=target_coordinates,
        first_decreasing_coordinate=first,
    )
    return _seal_dataclass_v1(
        E5TicketReceiptV1,
        source_state_id=e1.source_state_id,
        target_state_id=e3.target_state_id,
        source_potential_receipt=_freeze_json(context.source_potential_receipt),
        source_potential_receipt_digest=source_digest,
        target_potential_receipt=_freeze_json(context.target_potential_receipt),
        target_potential_receipt_digest=target_digest,
        ticket_type=context.ticket_type,
        taxonomy_id=context.taxonomy_id,
        taxonomy_digest=taxonomy_digest,
        source_coordinates=source_coordinates,
        target_coordinates=target_coordinates,
        first_decreasing_coordinate=first,
        comparison_scope=PARENT_TO_FINAL_TARGET,
        parent_to_final_assertion_digest=assertion_digest,
    )


def _transition_id_v1(
    *,
    source_state_id: str,
    source_state_digest: str,
    target_state_id: str,
    producer_id: str,
    branch_id: str,
    target_projection_digest: str,
    e1_digest: str,
    e2_digest: str,
    e3_digest: str,
    e4_digest: str,
    e5_digest: str,
) -> str:
    return "transition:" + canonical_digest_v1(
        {
            "source_state_id": source_state_id,
            "source_state_digest": source_state_digest,
            "target_state_id": target_state_id,
            "producer_id": producer_id,
            "branch_id": branch_id,
            "target_projection_digest": target_projection_digest,
            "e1_digest": e1_digest,
            "e2_digest": e2_digest,
            "e3_digest": e3_digest,
            "e4_digest": e4_digest,
            "e5_digest": e5_digest,
        }
    )


def make_verified_transition_bundle_v1(
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
) -> VerifiedTransitionBundleV1:
    e1 = make_e1_occurrence_receipt_v1(context, artifacts)
    e2 = make_e2_projection_receipt_v1(context, artifacts, e1)
    e3 = make_e3_typing_receipt_v1(context, artifacts, e2)
    e4 = make_e4_lift_receipt_v1(context, artifacts, e1, e3)
    e5 = make_e5_ticket_receipt_v1(context, artifacts, e1, e3)
    transition_id = _transition_id_v1(
        source_state_id=e1.source_state_id,
        source_state_digest=e1.source_state_digest,
        target_state_id=e3.target_state_id,
        producer_id=e1.producer_id,
        branch_id=e1.branch_id,
        target_projection_digest=e2.target_projection_digest,
        e1_digest=e1.digest,
        e2_digest=e2.digest,
        e3_digest=e3.digest,
        e4_digest=e4.digest,
        e5_digest=e5.digest,
    )
    bundle = _seal_dataclass_v1(
        VerifiedTransitionBundleV1,
        transition_id=transition_id,
        source_state_id=e1.source_state_id,
        source_state_digest=e1.source_state_digest,
        target_state_id=e3.target_state_id,
        producer_id=e1.producer_id,
        branch_id=e1.branch_id,
        target_projection_digest=e2.target_projection_digest,
        e1_occurrence=e1,
        e2_projection=e2,
        e3_typing=e3,
        e4_lift=e4,
        e5_ticket=e5,
    )
    verify_verified_transition_bundle_v1(bundle, context, artifacts)
    return bundle


def _verify_e1_v1(
    receipt: E1OccurrenceReceiptV1,
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
) -> None:
    _verify_receipt_seal_v1(receipt)
    expected_source_digest = canonical_digest_v1(context.source_state_payload)
    source_payload = context.source_state_payload
    if (
        receipt.source_state_id != context.source_state_id
        or receipt.source_state_digest != expected_source_digest
        or (
            isinstance(source_payload, Mapping)
            and source_payload.get("state_id") != context.source_state_id
        )
        or receipt.producer_id != context.producer_id
        or receipt.branch_id != context.branch_id
        or receipt.scope != context.scope
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.SOURCE_BINDING_MISMATCH,
            "E1 source, producer, branch, scope, or serialized state changed",
        )
    if (
        receipt.parent_transition_id != context.parent_transition_id
        or receipt.parent_transition_digest != _parent_digest_v1(context)
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.PARENT_BINDING_MISMATCH,
            "E1 parent transition does not replay",
        )
    if tuple(receipt.occurrence_path) != context.occurrence_path:
        raise ReceiptValidationError(
            ReceiptRejectCode.OCCURRENCE_REPLAY_FAILED,
            "E1 occurrence path differs from the expected source path",
        )
    replayed = _resolve_occurrence_path_v1(
        context.source_state_payload, receipt.occurrence_path
    )
    if _json_copy(receipt.occurrence_value) != _json_copy(replayed):
        raise ReceiptValidationError(
            ReceiptRejectCode.OCCURRENCE_REPLAY_FAILED,
            "E1 occurrence value does not replay from the source",
        )
    if receipt.provenance_digest != canonical_digest_v1(context.provenance_payload):
        raise ReceiptValidationError(
            ReceiptRejectCode.SOURCE_BINDING_MISMATCH,
            "E1 provenance digest changed",
        )
    if (
        context.source_terminal_result != MISS_COMPLETE
        or receipt.source_terminal_result != MISS_COMPLETE
        or receipt.source_terminal_schedule_id
        != context.source_terminal_schedule_id
        or receipt.source_terminal_result_digest
        != canonical_digest_v1(context.source_terminal_result_payload)
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.TERMINAL_BINDING_MISMATCH,
            "E1 requires the coordinator-replayed complete source terminal miss",
        )
    if isinstance(context.source_terminal_result_payload, Mapping):
        outcome = context.source_terminal_result_payload.get("outcome")
        if outcome is not None and outcome != MISS_COMPLETE:
            raise ReceiptValidationError(
                ReceiptRejectCode.TERMINAL_BINDING_MISMATCH,
                "terminal result payload is not MISS_COMPLETE",
            )
    expected_artifacts = (
        (context.producer_id, receipt.producer_id, receipt.producer_digest),
        (
            context.source_terminal_schedule_id,
            receipt.source_terminal_schedule_id,
            receipt.source_terminal_schedule_digest,
        ),
        (context.claim_id, receipt.claim_id, receipt.claim_digest),
        (
            context.reproduction_id,
            receipt.reproduction_id,
            receipt.reproduction_digest,
        ),
        (
            context.independent_verifier_id,
            receipt.independent_verifier_id,
            receipt.independent_verifier_digest,
        ),
    )
    for expected_id, actual_id, digest in expected_artifacts:
        if actual_id != expected_id:
            raise ReceiptValidationError(
                ReceiptRejectCode.UNTRUSTED_ARTIFACT,
                f"E1 artifact role expected {expected_id!r}, got {actual_id!r}",
            )
        artifacts.require(actual_id, digest)
    if (
        receipt.independent_verifier_id == receipt.producer_id
        or receipt.independent_verifier_digest == receipt.producer_digest
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.UNTRUSTED_ARTIFACT,
            "E1 independent verifier must differ from the producer module",
        )


def _verify_e2_v1(
    receipt: E2ProjectionReceiptV1,
    e1: E1OccurrenceReceiptV1,
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
) -> None:
    _verify_receipt_seal_v1(receipt)
    if (
        receipt.source_state_id != e1.source_state_id
        or receipt.source_state_digest != e1.source_state_digest
        or receipt.producer_id != e1.producer_id
        or receipt.branch_id != e1.branch_id
        or receipt.candidate_witness_digest
        != canonical_digest_v1(context.candidate_witness_payload)
        or _json_copy(receipt.canonical_target_payload)
        != _json_copy(context.target_projection_payload)
        or receipt.target_projection_digest
        != canonical_digest_v1(context.target_projection_payload)
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.PROJECTION_BINDING_MISMATCH,
            "E2 source, witness, or canonical target projection changed",
        )
    for expected_id, actual_id, digest in (
        (context.projector_id, receipt.projector_id, receipt.projector_digest),
        (
            context.tie_break_rule_id,
            receipt.tie_break_rule_id,
            receipt.tie_break_rule_digest,
        ),
    ):
        if actual_id != expected_id:
            raise ReceiptValidationError(
                ReceiptRejectCode.UNTRUSTED_ARTIFACT,
                f"E2 artifact role expected {expected_id!r}, got {actual_id!r}",
            )
        artifacts.require(actual_id, digest)


def _verify_e3_v1(
    receipt: E3TypingReceiptV1,
    e2: E2ProjectionReceiptV1,
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
) -> None:
    _verify_receipt_seal_v1(receipt)
    state_id, schema_id, schema_version = _target_state_fields_v1(context)
    predicates = dict(receipt.family_predicate_results)
    if (
        receipt.target_state_id != state_id
        or receipt.target_projection_digest != e2.target_projection_digest
        or receipt.target_schema_id != schema_id
        or receipt.target_schema_version != schema_version
        or predicates != dict(context.family_predicate_results)
        or not predicates.get(receipt.owner, False)
        or receipt.owner != context.target_owner
        or receipt.owner_digest != context.target_owner_digest
        or receipt.admission_gate_version != context.admission_gate_version
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.TYPING_BINDING_MISMATCH,
            "E3 schema, predicate replay, precedence owner, or gate changed",
        )
    for expected_id, actual_id, digest in (
        (
            context.normal_form_verifier_id,
            receipt.normal_form_verifier_id,
            receipt.normal_form_verifier_digest,
        ),
        (
            context.precedence_table_id,
            receipt.precedence_table_id,
            receipt.precedence_table_digest,
        ),
        (context.grammar_id, receipt.grammar_id, receipt.grammar_digest),
        (
            context.admission_gate_id,
            receipt.admission_gate_id,
            receipt.admission_gate_digest,
        ),
    ):
        if actual_id != expected_id:
            raise ReceiptValidationError(
                ReceiptRejectCode.UNTRUSTED_ARTIFACT,
                f"E3 artifact role expected {expected_id!r}, got {actual_id!r}",
            )
        artifacts.require(actual_id, digest)


def _verify_e4_v1(
    receipt: E4LiftReceiptV1,
    e1: E1OccurrenceReceiptV1,
    e3: E3TypingReceiptV1,
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
) -> None:
    _verify_receipt_seal_v1(receipt)
    negative_ids = tuple(receipt.negative_mutation_ids)
    if (
        receipt.source_state_id != e1.source_state_id
        or receipt.target_state_id != e3.target_state_id
        or _json_copy(receipt.source_equation_interface)
        != _json_copy(context.source_equation_interface)
        or receipt.source_equation_interface_digest
        != canonical_digest_v1(context.source_equation_interface)
        or _json_copy(receipt.target_equation_interface)
        != _json_copy(context.target_equation_interface)
        or receipt.target_equation_interface_digest
        != canonical_digest_v1(context.target_equation_interface)
        or receipt.universal_quantifier_statement
        != context.universal_quantifier_statement
        or not receipt.universal_quantifier_statement
        or negative_ids != context.negative_mutation_ids
        or not negative_ids
        or len(negative_ids) != len(set(negative_ids))
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.LIFT_BINDING_MISMATCH,
            "E4 interfaces, universal statement, or negative controls changed",
        )
    for mutation_id in negative_ids:
        if mutation_id not in NEGATIVE_MUTATION_IDS:
            raise ReceiptValidationError(
                ReceiptRejectCode.LIFT_BINDING_MISMATCH,
                f"E4 names unknown negative mutation {mutation_id!r}",
            )
    for expected_id, actual_id, digest in (
        (context.lift_map_id, receipt.lift_map_id, receipt.lift_map_digest),
        (
            context.symbolic_verifier_id,
            receipt.symbolic_verifier_id,
            receipt.symbolic_verifier_digest,
        ),
        (
            context.lift_reproduction_id,
            receipt.reproduction_id,
            receipt.reproduction_digest,
        ),
    ):
        if actual_id != expected_id:
            raise ReceiptValidationError(
                ReceiptRejectCode.UNTRUSTED_ARTIFACT,
                f"E4 artifact role expected {expected_id!r}, got {actual_id!r}",
            )
        artifacts.require(actual_id, digest)
    if (
        receipt.symbolic_verifier_id == e1.producer_id
        or receipt.symbolic_verifier_digest == e1.producer_digest
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.UNTRUSTED_ARTIFACT,
            "E4 symbolic verifier must differ from the producer module",
        )


def _verify_e5_v1(
    receipt: E5TicketReceiptV1,
    e1: E1OccurrenceReceiptV1,
    e3: E3TypingReceiptV1,
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
) -> None:
    _verify_receipt_seal_v1(receipt)
    source_digest, source_coordinates = _potential_receipt_v1(
        receipt.source_potential_receipt, e1.source_state_id, "source potential"
    )
    target_digest, target_coordinates = _potential_receipt_v1(
        receipt.target_potential_receipt, e3.target_state_id, "target potential"
    )
    first = _first_decreasing_coordinate_v1(source_coordinates, target_coordinates)
    _verify_ticket_type_v1(receipt.ticket_type, first)
    expected_assertion = _parent_to_final_assertion_digest_v1(
        source_state_id=e1.source_state_id,
        target_state_id=e3.target_state_id,
        source_receipt_digest=source_digest,
        target_receipt_digest=target_digest,
        ticket_type=receipt.ticket_type,
        taxonomy_id=receipt.taxonomy_id,
        taxonomy_digest=receipt.taxonomy_digest,
        source_coordinates=source_coordinates,
        target_coordinates=target_coordinates,
        first_decreasing_coordinate=first,
    )
    if (
        receipt.source_state_id != e1.source_state_id
        or receipt.target_state_id != e3.target_state_id
        or _json_copy(receipt.source_potential_receipt)
        != _json_copy(context.source_potential_receipt)
        or _json_copy(receipt.target_potential_receipt)
        != _json_copy(context.target_potential_receipt)
        or receipt.source_potential_receipt_digest != source_digest
        or receipt.target_potential_receipt_digest != target_digest
        or tuple(receipt.source_coordinates) != source_coordinates
        or tuple(receipt.target_coordinates) != target_coordinates
        or receipt.ticket_type != context.ticket_type
        or receipt.first_decreasing_coordinate != first
        or receipt.comparison_scope != PARENT_TO_FINAL_TARGET
        or receipt.parent_to_final_assertion_digest != expected_assertion
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.TICKET_BINDING_MISMATCH,
            "E5 potential receipts or parent-to-final ticket changed",
        )
    if receipt.taxonomy_id != context.taxonomy_id:
        raise ReceiptValidationError(
            ReceiptRejectCode.UNTRUSTED_ARTIFACT,
            "E5 taxonomy ID differs from the expected taxonomy",
        )
    artifacts.require(receipt.taxonomy_id, receipt.taxonomy_digest)


def verify_verified_transition_bundle_v1(
    value: Any,
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
) -> VerifiedTransitionBundleV1:
    """Independently replay every receipt and all cross-receipt bindings."""

    bundle = parse_verified_transition_bundle_v1(value)
    e1 = bundle.e1_occurrence
    e2 = bundle.e2_projection
    e3 = bundle.e3_typing
    e4 = bundle.e4_lift
    e5 = bundle.e5_ticket
    _verify_e1_v1(e1, context, artifacts)
    _verify_e2_v1(e2, e1, context, artifacts)
    _verify_e3_v1(e3, e2, context, artifacts)
    _verify_e4_v1(e4, e1, e3, context, artifacts)
    _verify_e5_v1(e5, e1, e3, context, artifacts)
    expected_transition_id = _transition_id_v1(
        source_state_id=e1.source_state_id,
        source_state_digest=e1.source_state_digest,
        target_state_id=e3.target_state_id,
        producer_id=e1.producer_id,
        branch_id=e1.branch_id,
        target_projection_digest=e2.target_projection_digest,
        e1_digest=e1.digest,
        e2_digest=e2.digest,
        e3_digest=e3.digest,
        e4_digest=e4.digest,
        e5_digest=e5.digest,
    )
    if (
        bundle.transition_id != expected_transition_id
        or bundle.source_state_id != e1.source_state_id
        or bundle.source_state_digest != e1.source_state_digest
        or bundle.target_state_id != e3.target_state_id
        or bundle.producer_id != e1.producer_id
        or bundle.branch_id != e1.branch_id
        or bundle.target_projection_digest != e2.target_projection_digest
    ):
        raise ReceiptValidationError(
            ReceiptRejectCode.CROSS_RECEIPT_MISMATCH,
            "transition bundle does not bind the replayed E1--E5 chain",
        )
    return bundle


def _looks_like_legacy_transition_validation_v1(value: Any) -> bool:
    keys = (
        set(value)
        if isinstance(value, Mapping)
        else {name for name in dir(value) if not name.startswith("_")}
    )
    return {
        "source_state_id",
        "producer_id",
        "branch_id",
        "projection_digest",
        "E1",
        "E2",
        "E3_pre_admission",
        "E4",
        "evidence_ids",
    } <= keys


def legacy_transition_validation_weaknesses_v1(value: Any) -> tuple[str, ...]:
    """Report the authority/binding omissions of the legacy runtime shape."""

    if not _looks_like_legacy_transition_validation_v1(value):
        return ()
    return (
        "BOOLEAN_E1_E4_NOT_REPLAYABLE",
        "FREE_FORM_EVIDENCE_IDS_NOT_CONTENT_BOUND",
        "NO_SOURCE_STATE_DIGEST",
        "NO_PARENT_TRANSITION_BINDING",
        "NO_OCCURRENCE_PATH_REPLAY",
        "NO_COMPLETE_TERMINAL_SCHEDULE_DIGEST",
        "NO_PROJECTOR_GRAMMAR_OR_TAXONOMY_HASH_BINDING",
        "NO_PARENT_TO_FINAL_E5_RECEIPT",
    )


def verify_structured_transition_evidence_v1(
    value: Any,
    context: TransitionReplayContextV1,
    artifacts: ArtifactDigestManifestV1,
) -> VerifiedTransitionBundleV1:
    """Migration boundary that explicitly refuses bare legacy proof booleans."""

    if _looks_like_legacy_transition_validation_v1(value):
        raise ReceiptValidationError(
            ReceiptRejectCode.LEGACY_BOOLEAN_VALIDATION,
            "TransitionValidationV1 booleans/evidence_ids are not proof receipts",
        )
    return verify_verified_transition_bundle_v1(value, context, artifacts)


def _reseal_mapping_v1(value: Mapping[str, Any]) -> dict[str, Any]:
    result = _json_copy(value)
    result.pop("digest", None)
    result["digest"] = canonical_digest_v1(result)
    return result


def _reseal_mutated_bundle_v1(value: Mapping[str, Any]) -> dict[str, Any]:
    result = _json_copy(value)
    for field_name in (
        "e1_occurrence",
        "e2_projection",
        "e3_typing",
        "e4_lift",
        "e5_ticket",
    ):
        result[field_name] = _reseal_mapping_v1(result[field_name])
    result["transition_id"] = _transition_id_v1(
        source_state_id=result["source_state_id"],
        source_state_digest=result["source_state_digest"],
        target_state_id=result["target_state_id"],
        producer_id=result["producer_id"],
        branch_id=result["branch_id"],
        target_projection_digest=result["target_projection_digest"],
        e1_digest=result["e1_occurrence"]["digest"],
        e2_digest=result["e2_projection"]["digest"],
        e3_digest=result["e3_typing"]["digest"],
        e4_digest=result["e4_lift"]["digest"],
        e5_digest=result["e5_ticket"]["digest"],
    )
    return _reseal_mapping_v1(result)


def apply_negative_mutation_v1(value: Any, mutation_id: str) -> dict[str, Any]:
    """Apply a named adversarial mutation and recompute attacker-visible hashes."""

    if mutation_id not in NEGATIVE_MUTATION_IDS:
        raise ReceiptValidationError(
            ReceiptRejectCode.UNKNOWN_NEGATIVE_MUTATION,
            f"unknown negative mutation {mutation_id!r}",
        )
    result = receipt_to_mapping_v1(parse_verified_transition_bundle_v1(value))
    e1 = result["e1_occurrence"]
    e2 = result["e2_projection"]
    e3 = result["e3_typing"]
    e5 = result["e5_ticket"]
    fake_digest = canonical_digest_v1({"mutation_id": mutation_id})
    if mutation_id == "CONTROL_AS_ACTUAL_BY_LABEL":
        e1["evidence_class"] = "ACTUAL_PERSISTENT"
    elif mutation_id == "LOCAL_MISS_AS_GLOBAL_MISS":
        e1["source_terminal_result"] = MISS_COMPLETE
        e1["source_terminal_result_digest"] = fake_digest
    elif mutation_id == "SELF_REGISTERED_PRODUCER":
        for target in (result, e1, e2):
            target["producer_id"] = "producer.self_registered"
        e1["producer_digest"] = fake_digest
    elif mutation_id == "SELF_REGISTERED_VALIDATOR":
        e1["independent_verifier_id"] = "validator.self_registered"
        e1["independent_verifier_digest"] = fake_digest
    elif mutation_id == "SOURCE_DIGEST_SWAP":
        for target in (result, e1, e2):
            target["source_state_digest"] = fake_digest
    elif mutation_id == "OCCURRENCE_PATH_SWAP":
        e1["occurrence_path"] = ["__swapped_occurrence__"]
    elif mutation_id == "CLAIM_HASH_DRIFT":
        e1["claim_digest"] = fake_digest
    elif mutation_id == "PROJECTOR_HASH_DRIFT":
        e2["projector_digest"] = fake_digest
    elif mutation_id == "GRAMMAR_HASH_DRIFT":
        e3["grammar_digest"] = fake_digest
    elif mutation_id == "T5_TAXONOMY_DRIFT":
        e5["taxonomy_digest"] = fake_digest
        e5["parent_to_final_assertion_digest"] = _parent_to_final_assertion_digest_v1(
            source_state_id=e5["source_state_id"],
            target_state_id=e5["target_state_id"],
            source_receipt_digest=e5["source_potential_receipt_digest"],
            target_receipt_digest=e5["target_potential_receipt_digest"],
            ticket_type=e5["ticket_type"],
            taxonomy_id=e5["taxonomy_id"],
            taxonomy_digest=fake_digest,
            source_coordinates=e5["source_coordinates"],
            target_coordinates=e5["target_coordinates"],
            first_decreasing_coordinate=e5["first_decreasing_coordinate"],
        )
    else:
        e1["parent_transition_digest"] = fake_digest
    return _reseal_mutated_bundle_v1(result)


__all__ = [
    "ArtifactDigestManifestV1",
    "E1OccurrenceReceiptV1",
    "E2ProjectionReceiptV1",
    "E3TypingReceiptV1",
    "E4LiftReceiptV1",
    "E5TicketReceiptV1",
    "MISS_COMPLETE",
    "NEGATIVE_MUTATION_IDS",
    "PARENT_TO_FINAL_TARGET",
    "ROOT_INITIALIZER",
    "ReceiptRejectCode",
    "ReceiptValidationError",
    "TransitionReplayContextV1",
    "VerifiedTransitionBundleV1",
    "apply_negative_mutation_v1",
    "canonical_digest_v1",
    "canonical_json_v1",
    "legacy_transition_validation_weaknesses_v1",
    "make_e1_occurrence_receipt_v1",
    "make_e2_projection_receipt_v1",
    "make_e3_typing_receipt_v1",
    "make_e4_lift_receipt_v1",
    "make_e5_ticket_receipt_v1",
    "make_verified_transition_bundle_v1",
    "parse_verified_transition_bundle_v1",
    "receipt_to_mapping_v1",
    "verify_structured_transition_evidence_v1",
    "verify_verified_transition_bundle_v1",
]
