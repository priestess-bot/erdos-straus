#!/usr/bin/env python3
"""Non-authorizing acyclic content-addressed shapes for future T6 receipts.

The module establishes one construction order only::

    projection
      -> preclassification / terminal digests / T5 coordinate draft
      -> edge anchor
      -> raw target state and state_id
      -> final receipt bundle and transition_id
      -> state-admission sidecar

Every object emitted by a public factory is a slotted frozen dataclass with an
exact typed field set and a content seal.  Frozen dataclasses are an ergonomic
API property, not a Python security boundary: every downstream factory fully
revalidates every typed field of its upstream objects before replaying their
bindings.  For the reserved field vocabulary, no target state identifier is an
edge-anchor input and no transition identifier is a target-state input.

These are data shapes, not proof or authority.  This module deliberately has
no producer registration, receipt issuance, admission decision, runtime, or
queue mutation API.  Receipt digests in the final bundle are opaque pins; this
module does not establish E1--E5 correctness and does not accept legacy boolean
validation as a fallback.  Opaque digests are declarations without provenance,
and unreserved semantic synonyms are outside this structural layer.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
from dataclasses import dataclass, fields
from enum import Enum
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, Sequence, TypeVar


SCHEMA_VERSION = 2
DEPENDENCY_ORDER_V2 = (
    "CanonicalTargetProjectionV2",
    (
        "PreclassificationDigestV2",
        "TerminalDigestSetV2",
        "T5CoordinateDraftV2",
    ),
    "EdgeAnchorV2",
    "RawTargetStateV2",
    "FinalTransitionReceiptBundleV2",
    "StateAdmissionSidecarV2",
)


class AcyclicBundleRejectCode(str, Enum):
    INPUT_NOT_MAPPING = "INPUT_NOT_MAPPING"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    WRONG_ARTIFACT_TYPE = "WRONG_ARTIFACT_TYPE"
    WRONG_SCHEMA_VERSION = "WRONG_SCHEMA_VERSION"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    FORBIDDEN_FIELD = "FORBIDDEN_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    ID_MISMATCH = "ID_MISMATCH"
    DEPENDENCY_MISMATCH = "DEPENDENCY_MISMATCH"


class AcyclicBundleValidationError(ValueError):
    """Fail-closed validation error with a stable machine-readable code."""

    def __init__(self, code: AcyclicBundleRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


_JSON_KEY_FORBIDDEN = re.compile(
    r"^(?:"
    r"[eE][1-5](?:_|$)|"
    r"terminal(?:_|$)|"
    r"(?:edge_)?anchor(?:_|$)|"
    r"(?:source_|target_|parent_)?state(?:_|$)|"
    r"owner(?:_|$)|"
    r"potential(?:_|$)|"
    r"(?:parent_)?transition(?:_|$)|"
    r"(?:verified_)?bundle(?:_|$)|"
    r"(?:final_)?receipt(?:_|$)|"
    r"admission(?:_|$)|"
    r"enqueue(?:_|$)|queue(?:_|$)"
    r")"
)


def _malformed(detail: str) -> AcyclicBundleValidationError:
    return AcyclicBundleValidationError(
        AcyclicBundleRejectCode.MALFORMED_FIELD, detail
    )


def _plain_int(value: Any, *, minimum: int | None = None) -> bool:
    if type(value) is not int:
        return False
    return minimum is None or value >= minimum


def _require_text(value: Any, name: str) -> str:
    if type(value) is not str or not value or value.strip() != value:
        raise _malformed(f"{name} must be a nonempty trimmed string")
    return value


def _is_digest(value: Any) -> bool:
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _require_digest(value: Any, name: str) -> str:
    if not _is_digest(value):
        raise _malformed(f"{name} must be a bare lowercase SHA-256 digest")
    return value


def _copy_pure_json(value: Any, *, path: str, reject_dependency_keys: bool) -> Any:
    """Copy the deterministic, authority-free JSON subset used by the shapes."""

    if value is None or isinstance(value, str):
        return copy.deepcopy(value)
    if isinstance(value, bool):
        raise _malformed(f"{path} cannot contain a boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, child in value.items():
            if not isinstance(key, str) or not key:
                raise _malformed(f"{path} object keys must be nonempty strings")
            if reject_dependency_keys and _JSON_KEY_FORBIDDEN.match(key):
                raise AcyclicBundleValidationError(
                    AcyclicBundleRejectCode.FORBIDDEN_FIELD,
                    f"{path}.{key} imports a downstream or authority field",
                )
            result[key] = _copy_pure_json(
                child,
                path=f"{path}.{key}",
                reject_dependency_keys=reject_dependency_keys,
            )
        return result
    if isinstance(value, (list, tuple)):
        return [
            _copy_pure_json(
                child,
                path=f"{path}[{index}]",
                reject_dependency_keys=reject_dependency_keys,
            )
            for index, child in enumerate(value)
        ]
    raise _malformed(
        f"{path} contains unsupported value type {type(value).__name__}"
    )


def _freeze_json(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType(
            {key: _freeze_json(child) for key, child in value.items()}
        )
    if isinstance(value, list):
        return tuple(_freeze_json(child) for child in value)
    return value


def canonical_json_v2(value: Any) -> str:
    """Return the unique ASCII JSON encoding used for all V2 content IDs."""

    normalized = _copy_pure_json(
        value, path="$", reject_dependency_keys=False
    )
    return json.dumps(
        normalized,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


def canonical_digest_v2(value: Any) -> str:
    return hashlib.sha256(canonical_json_v2(value).encode("ascii")).hexdigest()


def loads_strict_v2(encoded: str) -> Any:
    """Decode JSON while rejecting duplicate keys and non-canonical numbers."""

    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise AcyclicBundleValidationError(
                    AcyclicBundleRejectCode.FIELD_SET_MISMATCH,
                    f"duplicate JSON key {key!r}",
                )
            result[key] = value
        return result

    try:
        value = json.loads(
            encoded,
            object_pairs_hook=object_pairs,
            parse_float=lambda _value: (_ for _ in ()).throw(
                _malformed("floating-point JSON numbers are not supported")
            ),
            parse_constant=lambda value: (_ for _ in ()).throw(
                _malformed(f"non-finite JSON constant {value!r} is not supported")
            ),
        )
    except AcyclicBundleValidationError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        raise _malformed(f"invalid JSON: {exc}") from exc
    return _copy_pure_json(value, path="$", reject_dependency_keys=False)


class _FactorySealedV2:
    __slots__ = ()

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} must be created by its V2 factory")


@dataclass(frozen=True, init=False, slots=True)
class CanonicalTargetProjectionV2(_FactorySealedV2):
    ARTIFACT_TYPE: ClassVar[str] = "CanonicalTargetProjectionV2"
    ID_FIELD: ClassVar[str] = "projection_id"
    ID_PREFIX: ClassVar[str] = "projection:"

    target_schema_id: str
    target_schema_version: int
    root_context: str
    equation_rank: int
    facts: Mapping[str, Any]
    mark_behavior: str
    projector_id: str
    projector_digest: str
    tie_break_rule_id: str
    tie_break_rule_digest: str
    projection_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class PreclassificationDigestV2(_FactorySealedV2):
    ARTIFACT_TYPE: ClassVar[str] = "PreclassificationDigestV2"
    ID_FIELD: ClassVar[str] = "preclassification_id"
    ID_PREFIX: ClassVar[str] = "preclassification:"

    projection_id: str
    projection_digest: str
    normal_form_verifier_id: str
    normal_form_verifier_digest: str
    predicate_results_digest: str
    precedence_table_id: str
    precedence_table_digest: str
    preclassification_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class TerminalDigestSetV2(_FactorySealedV2):
    ARTIFACT_TYPE: ClassVar[str] = "TerminalDigestSetV2"
    ID_FIELD: ClassVar[str] = "terminal_digest_set_id"
    ID_PREFIX: ClassVar[str] = "terminal-digests:"

    projection_id: str
    projection_digest: str
    source_state_id: str
    source_state_digest: str
    schedule_id: str
    schedule_digest: str
    result_digest: str
    coverage_scope_digest: str
    terminal_digest_set_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class T5CoordinateDraftV2(_FactorySealedV2):
    ARTIFACT_TYPE: ClassVar[str] = "T5CoordinateDraftV2"
    ID_FIELD: ClassVar[str] = "t5_coordinate_draft_id"
    ID_PREFIX: ClassVar[str] = "t5-coordinate-draft:"

    projection_id: str
    projection_digest: str
    taxonomy_id: str
    taxonomy_digest: str
    coordinates: tuple[int, int, int, int, int, int, int]
    t5_coordinate_draft_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class EdgeAnchorV2(_FactorySealedV2):
    ARTIFACT_TYPE: ClassVar[str] = "EdgeAnchorV2"
    ID_FIELD: ClassVar[str] = "edge_anchor_id"
    ID_PREFIX: ClassVar[str] = "edge-anchor:"

    source_state_id: str
    source_state_digest: str
    producer_id: str
    producer_digest: str
    branch_id: str
    candidate_witness_digest: str
    projection_id: str
    projection_digest: str
    preclassification_id: str
    preclassification_digest: str
    terminal_digest_set_id: str
    terminal_digest_set_digest: str
    t5_coordinate_draft_id: str
    t5_coordinate_draft_digest: str
    edge_anchor_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class SuccessorOriginAnchorRefV2(_FactorySealedV2):
    """The only predecessor/edge metadata embedded in a raw target state."""

    edge_anchor_id: str
    edge_anchor_digest: str


@dataclass(frozen=True, init=False, slots=True)
class RawTargetStateV2(_FactorySealedV2):
    ARTIFACT_TYPE: ClassVar[str] = "RawTargetStateV2"
    ID_FIELD: ClassVar[str] = "state_id"
    ID_PREFIX: ClassVar[str] = "state:"

    target_schema_id: str
    target_schema_version: int
    root_context: str
    equation_rank: int
    facts: Mapping[str, Any]
    mark_behavior: str
    successor_origin: SuccessorOriginAnchorRefV2
    state_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class FinalTransitionReceiptBundleV2(_FactorySealedV2):
    ARTIFACT_TYPE: ClassVar[str] = "FinalTransitionReceiptBundleV2"
    ID_FIELD: ClassVar[str] = "transition_id"
    ID_PREFIX: ClassVar[str] = "transition:"

    source_state_id: str
    source_state_digest: str
    target_state_id: str
    target_state_digest: str
    edge_anchor_id: str
    edge_anchor_digest: str
    e1_occurrence_receipt_digest: str
    e2_projection_receipt_digest: str
    e3_typing_receipt_digest: str
    e4_lift_receipt_digest: str
    e5_ticket_receipt_digest: str
    transition_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class StateAdmissionSidecarV2(_FactorySealedV2):
    ARTIFACT_TYPE: ClassVar[str] = "StateAdmissionSidecarV2"
    ID_FIELD: ClassVar[str] = "sidecar_id"
    ID_PREFIX: ClassVar[str] = "state-admission-sidecar:"

    state_id: str
    state_digest: str
    transition_id: str
    transition_bundle_digest: str
    owner_id: str
    owner_digest: str
    grammar_digest: str
    admission_gate_digest: str
    target_potential_receipt_digest: str
    state_admission_receipt_digest: str
    sidecar_id: str
    digest: str


SealedArtifactV2 = (
    CanonicalTargetProjectionV2
    | PreclassificationDigestV2
    | TerminalDigestSetV2
    | T5CoordinateDraftV2
    | EdgeAnchorV2
    | RawTargetStateV2
    | FinalTransitionReceiptBundleV2
    | StateAdmissionSidecarV2
)
ArtifactT = TypeVar("ArtifactT", bound=SealedArtifactV2)
_MAPPING_PROXY_TYPE = type(MappingProxyType({}))


def _require_content_id(value: Any, name: str, prefix: str) -> str:
    text = _require_text(value, name)
    if not text.startswith(prefix) or not _is_digest(text[len(prefix) :]):
        raise _malformed(f"{name} must be {prefix!r} followed by a SHA-256 digest")
    return text


def _validate_frozen_pure_value_v2(
    value: Any, *, path: str, reject_dependency_keys: bool
) -> None:
    if value is None or type(value) is str or type(value) is int:
        return
    if type(value) is _MAPPING_PROXY_TYPE:
        for key, child in value.items():
            if type(key) is not str or not key:
                raise _malformed(f"{path} object keys must be nonempty strings")
            if reject_dependency_keys and _JSON_KEY_FORBIDDEN.match(key):
                raise AcyclicBundleValidationError(
                    AcyclicBundleRejectCode.FORBIDDEN_FIELD,
                    f"{path}.{key} imports a reserved downstream field",
                )
            _validate_frozen_pure_value_v2(
                child,
                path=f"{path}.{key}",
                reject_dependency_keys=reject_dependency_keys,
            )
        return
    if type(value) is tuple:
        for index, child in enumerate(value):
            _validate_frozen_pure_value_v2(
                child,
                path=f"{path}[{index}]",
                reject_dependency_keys=reject_dependency_keys,
            )
        return
    raise _malformed(
        f"{path} is not in the exact frozen canonical JSON representation"
    )


def _require_projection_reference_fields(artifact: Any) -> None:
    _require_content_id(artifact.projection_id, "projection_id", "projection:")
    _require_digest(artifact.projection_digest, "projection_digest")


def _validate_origin_ref_fields_v2(ref: Any) -> None:
    if type(ref) is not SuccessorOriginAnchorRefV2:
        raise _malformed(
            "successor_origin must be an exact SuccessorOriginAnchorRefV2"
        )
    for field in fields(SuccessorOriginAnchorRefV2):
        try:
            getattr(ref, field.name)
        except AttributeError as exc:
            raise _malformed(f"successor_origin.{field.name} is missing") from exc
    _require_content_id(
        ref.edge_anchor_id,
        "successor_origin.edge_anchor_id",
        "edge-anchor:",
    )
    _require_digest(
        ref.edge_anchor_digest,
        "successor_origin.edge_anchor_digest",
    )


def _require_own_seal_fields_v2(artifact: SealedArtifactV2) -> None:
    cls = type(artifact)
    _require_content_id(
        getattr(artifact, cls.ID_FIELD), cls.ID_FIELD, cls.ID_PREFIX
    )
    _require_digest(artifact.digest, f"{cls.ARTIFACT_TYPE}.digest")


def _validate_artifact_fields_v2(artifact: SealedArtifactV2) -> None:
    """Validate all typed fields before trusting an exact-class object."""

    cls = type(artifact)
    if cls not in _SEALED_CLASSES:
        raise _malformed("value is not an exact V2 artifact class")
    for field in fields(cls):
        try:
            getattr(artifact, field.name)
        except AttributeError as exc:
            raise _malformed(
                f"{cls.ARTIFACT_TYPE}.{field.name} is missing"
            ) from exc
    _require_own_seal_fields_v2(artifact)

    if cls is CanonicalTargetProjectionV2:
        _require_text(artifact.target_schema_id, "target_schema_id")
        if not _plain_int(artifact.target_schema_version, minimum=1):
            raise _malformed(
                "target_schema_version must be a positive plain integer"
            )
        _require_text(artifact.root_context, "root_context")
        if not _plain_int(artifact.equation_rank, minimum=1):
            raise _malformed("equation_rank must be a positive plain integer")
        if type(artifact.facts) is not _MAPPING_PROXY_TYPE:
            raise _malformed("projection.facts must use the frozen mapping shape")
        _validate_frozen_pure_value_v2(
            artifact.facts,
            path="projection.facts",
            reject_dependency_keys=True,
        )
        _require_text(artifact.mark_behavior, "mark_behavior")
        _require_text(artifact.projector_id, "projector_id")
        _require_digest(artifact.projector_digest, "projector_digest")
        _require_text(artifact.tie_break_rule_id, "tie_break_rule_id")
        _require_digest(artifact.tie_break_rule_digest, "tie_break_rule_digest")
        return

    if cls is PreclassificationDigestV2:
        _require_projection_reference_fields(artifact)
        _require_text(
            artifact.normal_form_verifier_id, "normal_form_verifier_id"
        )
        _require_digest(
            artifact.normal_form_verifier_digest,
            "normal_form_verifier_digest",
        )
        _require_digest(
            artifact.predicate_results_digest, "predicate_results_digest"
        )
        _require_text(artifact.precedence_table_id, "precedence_table_id")
        _require_digest(
            artifact.precedence_table_digest, "precedence_table_digest"
        )
        return

    if cls is TerminalDigestSetV2:
        _require_projection_reference_fields(artifact)
        _require_text(artifact.source_state_id, "source_state_id")
        _require_digest(artifact.source_state_digest, "source_state_digest")
        _require_text(artifact.schedule_id, "schedule_id")
        _require_digest(artifact.schedule_digest, "schedule_digest")
        _require_digest(artifact.result_digest, "result_digest")
        _require_digest(
            artifact.coverage_scope_digest, "coverage_scope_digest"
        )
        return

    if cls is T5CoordinateDraftV2:
        _require_projection_reference_fields(artifact)
        _require_text(artifact.taxonomy_id, "taxonomy_id")
        _require_digest(artifact.taxonomy_digest, "taxonomy_digest")
        if (
            type(artifact.coordinates) is not tuple
            or len(artifact.coordinates) != 7
            or any(
                not _plain_int(coordinate, minimum=0)
                for coordinate in artifact.coordinates
            )
        ):
            raise _malformed(
                "coordinates must use the exact length-seven tuple shape in N^7"
            )
        return

    if cls is EdgeAnchorV2:
        _require_text(artifact.source_state_id, "source_state_id")
        _require_digest(artifact.source_state_digest, "source_state_digest")
        _require_text(artifact.producer_id, "producer_id")
        _require_digest(artifact.producer_digest, "producer_digest")
        _require_text(artifact.branch_id, "branch_id")
        _require_digest(
            artifact.candidate_witness_digest, "candidate_witness_digest"
        )
        _require_projection_reference_fields(artifact)
        _require_content_id(
            artifact.preclassification_id,
            "preclassification_id",
            "preclassification:",
        )
        _require_digest(
            artifact.preclassification_digest, "preclassification_digest"
        )
        _require_content_id(
            artifact.terminal_digest_set_id,
            "terminal_digest_set_id",
            "terminal-digests:",
        )
        _require_digest(
            artifact.terminal_digest_set_digest,
            "terminal_digest_set_digest",
        )
        _require_content_id(
            artifact.t5_coordinate_draft_id,
            "t5_coordinate_draft_id",
            "t5-coordinate-draft:",
        )
        _require_digest(
            artifact.t5_coordinate_draft_digest,
            "t5_coordinate_draft_digest",
        )
        return

    if cls is RawTargetStateV2:
        _require_text(artifact.target_schema_id, "target_schema_id")
        if not _plain_int(artifact.target_schema_version, minimum=1):
            raise _malformed(
                "target_schema_version must be a positive plain integer"
            )
        _require_text(artifact.root_context, "root_context")
        if not _plain_int(artifact.equation_rank, minimum=1):
            raise _malformed("equation_rank must be a positive plain integer")
        if type(artifact.facts) is not _MAPPING_PROXY_TYPE:
            raise _malformed("raw_target.facts must use the frozen mapping shape")
        _validate_frozen_pure_value_v2(
            artifact.facts,
            path="raw_target.facts",
            reject_dependency_keys=True,
        )
        _require_text(artifact.mark_behavior, "mark_behavior")
        _validate_origin_ref_fields_v2(artifact.successor_origin)
        return

    if cls is FinalTransitionReceiptBundleV2:
        _require_text(artifact.source_state_id, "source_state_id")
        _require_digest(artifact.source_state_digest, "source_state_digest")
        _require_content_id(
            artifact.target_state_id, "target_state_id", "state:"
        )
        _require_digest(artifact.target_state_digest, "target_state_digest")
        _require_content_id(
            artifact.edge_anchor_id, "edge_anchor_id", "edge-anchor:"
        )
        _require_digest(artifact.edge_anchor_digest, "edge_anchor_digest")
        for name in (
            "e1_occurrence_receipt_digest",
            "e2_projection_receipt_digest",
            "e3_typing_receipt_digest",
            "e4_lift_receipt_digest",
            "e5_ticket_receipt_digest",
        ):
            _require_digest(getattr(artifact, name), name)
        return

    if cls is StateAdmissionSidecarV2:
        _require_content_id(artifact.state_id, "state_id", "state:")
        _require_digest(artifact.state_digest, "state_digest")
        _require_content_id(
            artifact.transition_id, "transition_id", "transition:"
        )
        _require_digest(
            artifact.transition_bundle_digest, "transition_bundle_digest"
        )
        _require_text(artifact.owner_id, "owner_id")
        for name in (
            "owner_digest",
            "grammar_digest",
            "admission_gate_digest",
            "target_potential_receipt_digest",
            "state_admission_receipt_digest",
        ):
            _require_digest(getattr(artifact, name), name)
        return

    raise _malformed(f"unhandled V2 artifact type {cls.__name__}")


def _construct(cls: type[ArtifactT], values: Mapping[str, Any]) -> ArtifactT:
    instance = object.__new__(cls)
    for field in fields(cls):
        object.__setattr__(instance, field.name, values[field.name])
    return instance


def _origin_ref_mapping(ref: SuccessorOriginAnchorRefV2) -> dict[str, str]:
    _validate_origin_ref_fields_v2(ref)
    return {
        "edge_anchor_id": ref.edge_anchor_id,
        "edge_anchor_digest": ref.edge_anchor_digest,
    }


def _external_value(value: Any) -> Any:
    if isinstance(value, SuccessorOriginAnchorRefV2):
        return _origin_ref_mapping(value)
    return _copy_pure_json(value, path="$", reject_dependency_keys=False)


def _unsigned_mapping(
    cls: type[ArtifactT], values: Mapping[str, Any]
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "artifact_type": cls.ARTIFACT_TYPE,
        "schema_version": SCHEMA_VERSION,
    }
    for field in fields(cls):
        if field.name in {cls.ID_FIELD, "digest"}:
            continue
        payload[field.name] = _external_value(values[field.name])
    return payload


def _seal(cls: type[ArtifactT], values: Mapping[str, Any]) -> ArtifactT:
    mutable = dict(values)
    digest = canonical_digest_v2(_unsigned_mapping(cls, mutable))
    mutable[cls.ID_FIELD] = cls.ID_PREFIX + digest
    mutable["digest"] = digest
    artifact = _construct(cls, mutable)
    _verify_content_seal(artifact)
    return artifact


def artifact_to_mapping_v2(artifact: SealedArtifactV2) -> dict[str, Any]:
    """Serialize a V2 artifact without granting it any authority."""

    cls = type(artifact)
    if cls not in _SEALED_CLASSES:
        raise _malformed("value is not a V2 sealed artifact")
    _verify_content_seal(artifact)
    values = {field.name: getattr(artifact, field.name) for field in fields(cls)}
    payload = _unsigned_mapping(cls, values)
    payload[cls.ID_FIELD] = getattr(artifact, cls.ID_FIELD)
    payload["digest"] = artifact.digest
    return payload


def _verify_content_seal(artifact: SealedArtifactV2) -> None:
    cls = type(artifact)
    if cls not in _SEALED_CLASSES:
        raise _malformed("value is not a V2 sealed artifact")
    _validate_artifact_fields_v2(artifact)
    values = {field.name: getattr(artifact, field.name) for field in fields(cls)}
    expected_digest = canonical_digest_v2(_unsigned_mapping(cls, values))
    if artifact.digest != expected_digest:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DIGEST_MISMATCH,
            f"{cls.ARTIFACT_TYPE} content seal does not replay",
        )
    expected_id = cls.ID_PREFIX + expected_digest
    if getattr(artifact, cls.ID_FIELD) != expected_id:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.ID_MISMATCH,
            f"{cls.ARTIFACT_TYPE}.{cls.ID_FIELD} does not replay",
        )


def _mapping_for(
    value: Any, cls: type[ArtifactT]
) -> Mapping[str, Any]:
    if type(value) is cls:
        return artifact_to_mapping_v2(value)
    if not isinstance(value, Mapping):
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.INPUT_NOT_MAPPING,
            f"{cls.ARTIFACT_TYPE} must be a mapping",
        )
    expected = {field.name for field in fields(cls)} | {
        "artifact_type",
        "schema_version",
    }
    if set(value) != expected:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.FIELD_SET_MISMATCH,
            f"{cls.ARTIFACT_TYPE} fields differ from the V2 contract",
        )
    if (
        type(value.get("artifact_type")) is not str
        or value.get("artifact_type") != cls.ARTIFACT_TYPE
    ):
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.WRONG_ARTIFACT_TYPE,
            f"expected artifact_type {cls.ARTIFACT_TYPE!r}",
        )
    if (
        not _plain_int(value.get("schema_version"), minimum=0)
        or value.get("schema_version") != SCHEMA_VERSION
    ):
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.WRONG_SCHEMA_VERSION,
            f"{cls.ARTIFACT_TYPE} is not schema version 2",
        )
    _require_content_id(value[cls.ID_FIELD], cls.ID_FIELD, cls.ID_PREFIX)
    _require_digest(value["digest"], f"{cls.ARTIFACT_TYPE}.digest")
    return value


def _require_same_artifact(
    stored: Mapping[str, Any], replayed: SealedArtifactV2
) -> None:
    if dict(stored) != artifact_to_mapping_v2(replayed):
        if stored.get("digest") != replayed.digest:
            code = AcyclicBundleRejectCode.DIGEST_MISMATCH
        elif stored.get(type(replayed).ID_FIELD) != getattr(
            replayed, type(replayed).ID_FIELD
        ):
            code = AcyclicBundleRejectCode.ID_MISMATCH
        else:
            code = AcyclicBundleRejectCode.DEPENDENCY_MISMATCH
        raise AcyclicBundleValidationError(
            code,
            f"{type(replayed).ARTIFACT_TYPE} does not replay from its dependencies",
        )


def _require_projection(projection: CanonicalTargetProjectionV2) -> None:
    if type(projection) is not CanonicalTargetProjectionV2:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "a sealed CanonicalTargetProjectionV2 is required",
        )
    _verify_content_seal(projection)


def make_canonical_target_projection_v2(
    *,
    target_schema_id: str,
    target_schema_version: int,
    root_context: str,
    equation_rank: int,
    facts: Mapping[str, Any],
    mark_behavior: str,
    projector_id: str,
    projector_digest: str,
    tie_break_rule_id: str,
    tie_break_rule_digest: str,
) -> CanonicalTargetProjectionV2:
    """Seal the authority-free target projection at the head of the DAG."""

    _require_text(target_schema_id, "target_schema_id")
    if not _plain_int(target_schema_version, minimum=1):
        raise _malformed("target_schema_version must be a positive plain integer")
    _require_text(root_context, "root_context")
    if not _plain_int(equation_rank, minimum=1):
        raise _malformed("equation_rank must be a positive plain integer")
    if not isinstance(facts, Mapping):
        raise _malformed("facts must be an object")
    normalized_facts = _copy_pure_json(
        facts, path="projection.facts", reject_dependency_keys=True
    )
    _require_text(mark_behavior, "mark_behavior")
    _require_text(projector_id, "projector_id")
    _require_digest(projector_digest, "projector_digest")
    _require_text(tie_break_rule_id, "tie_break_rule_id")
    _require_digest(tie_break_rule_digest, "tie_break_rule_digest")
    return _seal(
        CanonicalTargetProjectionV2,
        {
            "target_schema_id": target_schema_id,
            "target_schema_version": target_schema_version,
            "root_context": root_context,
            "equation_rank": equation_rank,
            "facts": _freeze_json(normalized_facts),
            "mark_behavior": mark_behavior,
            "projector_id": projector_id,
            "projector_digest": projector_digest,
            "tie_break_rule_id": tie_break_rule_id,
            "tie_break_rule_digest": tie_break_rule_digest,
        },
    )


def parse_canonical_target_projection_v2(
    value: Any,
) -> CanonicalTargetProjectionV2:
    stored = _mapping_for(value, CanonicalTargetProjectionV2)
    replayed = make_canonical_target_projection_v2(
        target_schema_id=stored["target_schema_id"],
        target_schema_version=stored["target_schema_version"],
        root_context=stored["root_context"],
        equation_rank=stored["equation_rank"],
        facts=stored["facts"],
        mark_behavior=stored["mark_behavior"],
        projector_id=stored["projector_id"],
        projector_digest=stored["projector_digest"],
        tie_break_rule_id=stored["tie_break_rule_id"],
        tie_break_rule_digest=stored["tie_break_rule_digest"],
    )
    _require_same_artifact(stored, replayed)
    return replayed


def make_preclassification_digest_v2(
    projection: CanonicalTargetProjectionV2,
    *,
    normal_form_verifier_id: str,
    normal_form_verifier_digest: str,
    predicate_results_digest: str,
    precedence_table_id: str,
    precedence_table_digest: str,
) -> PreclassificationDigestV2:
    _require_projection(projection)
    _require_text(normal_form_verifier_id, "normal_form_verifier_id")
    _require_digest(normal_form_verifier_digest, "normal_form_verifier_digest")
    _require_digest(predicate_results_digest, "predicate_results_digest")
    _require_text(precedence_table_id, "precedence_table_id")
    _require_digest(precedence_table_digest, "precedence_table_digest")
    return _seal(
        PreclassificationDigestV2,
        {
            "projection_id": projection.projection_id,
            "projection_digest": projection.digest,
            "normal_form_verifier_id": normal_form_verifier_id,
            "normal_form_verifier_digest": normal_form_verifier_digest,
            "predicate_results_digest": predicate_results_digest,
            "precedence_table_id": precedence_table_id,
            "precedence_table_digest": precedence_table_digest,
        },
    )


def parse_preclassification_digest_v2(
    value: Any, projection: CanonicalTargetProjectionV2
) -> PreclassificationDigestV2:
    stored = _mapping_for(value, PreclassificationDigestV2)
    replayed = make_preclassification_digest_v2(
        projection,
        normal_form_verifier_id=stored["normal_form_verifier_id"],
        normal_form_verifier_digest=stored["normal_form_verifier_digest"],
        predicate_results_digest=stored["predicate_results_digest"],
        precedence_table_id=stored["precedence_table_id"],
        precedence_table_digest=stored["precedence_table_digest"],
    )
    _require_same_artifact(stored, replayed)
    return replayed


def make_terminal_digest_set_v2(
    projection: CanonicalTargetProjectionV2,
    *,
    source_state_id: str,
    source_state_digest: str,
    schedule_id: str,
    schedule_digest: str,
    result_digest: str,
    coverage_scope_digest: str,
) -> TerminalDigestSetV2:
    _require_projection(projection)
    _require_text(source_state_id, "source_state_id")
    _require_digest(source_state_digest, "source_state_digest")
    _require_text(schedule_id, "schedule_id")
    _require_digest(schedule_digest, "schedule_digest")
    _require_digest(result_digest, "result_digest")
    _require_digest(coverage_scope_digest, "coverage_scope_digest")
    return _seal(
        TerminalDigestSetV2,
        {
            "projection_id": projection.projection_id,
            "projection_digest": projection.digest,
            "source_state_id": source_state_id,
            "source_state_digest": source_state_digest,
            "schedule_id": schedule_id,
            "schedule_digest": schedule_digest,
            "result_digest": result_digest,
            "coverage_scope_digest": coverage_scope_digest,
        },
    )


def parse_terminal_digest_set_v2(
    value: Any, projection: CanonicalTargetProjectionV2
) -> TerminalDigestSetV2:
    stored = _mapping_for(value, TerminalDigestSetV2)
    replayed = make_terminal_digest_set_v2(
        projection,
        source_state_id=stored["source_state_id"],
        source_state_digest=stored["source_state_digest"],
        schedule_id=stored["schedule_id"],
        schedule_digest=stored["schedule_digest"],
        result_digest=stored["result_digest"],
        coverage_scope_digest=stored["coverage_scope_digest"],
    )
    _require_same_artifact(stored, replayed)
    return replayed


def make_t5_coordinate_draft_v2(
    projection: CanonicalTargetProjectionV2,
    *,
    taxonomy_id: str,
    taxonomy_digest: str,
    coordinates: Sequence[int],
) -> T5CoordinateDraftV2:
    _require_projection(projection)
    _require_text(taxonomy_id, "taxonomy_id")
    _require_digest(taxonomy_digest, "taxonomy_digest")
    if (
        not isinstance(coordinates, (list, tuple))
        or len(coordinates) != 7
        or any(not _plain_int(value, minimum=0) for value in coordinates)
    ):
        raise _malformed("coordinates must be a length-seven vector in N^7")
    normalized = tuple(coordinates)
    return _seal(
        T5CoordinateDraftV2,
        {
            "projection_id": projection.projection_id,
            "projection_digest": projection.digest,
            "taxonomy_id": taxonomy_id,
            "taxonomy_digest": taxonomy_digest,
            "coordinates": normalized,
        },
    )


def parse_t5_coordinate_draft_v2(
    value: Any, projection: CanonicalTargetProjectionV2
) -> T5CoordinateDraftV2:
    stored = _mapping_for(value, T5CoordinateDraftV2)
    replayed = make_t5_coordinate_draft_v2(
        projection,
        taxonomy_id=stored["taxonomy_id"],
        taxonomy_digest=stored["taxonomy_digest"],
        coordinates=stored["coordinates"],
    )
    _require_same_artifact(stored, replayed)
    return replayed


def _require_sibling(
    artifact: SealedArtifactV2,
    expected_type: type[ArtifactT],
    projection: CanonicalTargetProjectionV2,
) -> None:
    if type(artifact) is not expected_type:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            f"a sealed {expected_type.ARTIFACT_TYPE} is required",
        )
    _verify_content_seal(artifact)
    if (
        artifact.projection_id != projection.projection_id
        or artifact.projection_digest != projection.digest
    ):
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            f"{expected_type.ARTIFACT_TYPE} belongs to another projection",
        )


def make_edge_anchor_v2(
    projection: CanonicalTargetProjectionV2,
    preclassification: PreclassificationDigestV2,
    terminal_digests: TerminalDigestSetV2,
    t5_draft: T5CoordinateDraftV2,
    *,
    producer_id: str,
    producer_digest: str,
    branch_id: str,
    candidate_witness_digest: str,
) -> EdgeAnchorV2:
    """Bind all pre-state facts without importing a target or transition ID."""

    _require_projection(projection)
    _require_sibling(preclassification, PreclassificationDigestV2, projection)
    _require_sibling(terminal_digests, TerminalDigestSetV2, projection)
    _require_sibling(t5_draft, T5CoordinateDraftV2, projection)
    _require_text(producer_id, "producer_id")
    _require_digest(producer_digest, "producer_digest")
    _require_text(branch_id, "branch_id")
    _require_digest(candidate_witness_digest, "candidate_witness_digest")
    return _seal(
        EdgeAnchorV2,
        {
            "source_state_id": terminal_digests.source_state_id,
            "source_state_digest": terminal_digests.source_state_digest,
            "producer_id": producer_id,
            "producer_digest": producer_digest,
            "branch_id": branch_id,
            "candidate_witness_digest": candidate_witness_digest,
            "projection_id": projection.projection_id,
            "projection_digest": projection.digest,
            "preclassification_id": preclassification.preclassification_id,
            "preclassification_digest": preclassification.digest,
            "terminal_digest_set_id": terminal_digests.terminal_digest_set_id,
            "terminal_digest_set_digest": terminal_digests.digest,
            "t5_coordinate_draft_id": t5_draft.t5_coordinate_draft_id,
            "t5_coordinate_draft_digest": t5_draft.digest,
        },
    )


def parse_edge_anchor_v2(
    value: Any,
    projection: CanonicalTargetProjectionV2,
    preclassification: PreclassificationDigestV2,
    terminal_digests: TerminalDigestSetV2,
    t5_draft: T5CoordinateDraftV2,
) -> EdgeAnchorV2:
    stored = _mapping_for(value, EdgeAnchorV2)
    replayed = make_edge_anchor_v2(
        projection,
        preclassification,
        terminal_digests,
        t5_draft,
        producer_id=stored["producer_id"],
        producer_digest=stored["producer_digest"],
        branch_id=stored["branch_id"],
        candidate_witness_digest=stored["candidate_witness_digest"],
    )
    _require_same_artifact(stored, replayed)
    return replayed


def make_successor_origin_anchor_ref_v2(
    anchor: EdgeAnchorV2,
) -> SuccessorOriginAnchorRefV2:
    if type(anchor) is not EdgeAnchorV2:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "a sealed EdgeAnchorV2 is required",
        )
    _verify_content_seal(anchor)
    ref = object.__new__(SuccessorOriginAnchorRefV2)
    object.__setattr__(ref, "edge_anchor_id", anchor.edge_anchor_id)
    object.__setattr__(ref, "edge_anchor_digest", anchor.digest)
    _validate_origin_ref_fields_v2(ref)
    return ref


def parse_successor_origin_anchor_ref_v2(
    value: Any, anchor: EdgeAnchorV2
) -> SuccessorOriginAnchorRefV2:
    expected_fields = {field.name for field in fields(SuccessorOriginAnchorRefV2)}
    if type(value) is SuccessorOriginAnchorRefV2:
        _validate_origin_ref_fields_v2(value)
        stored = _origin_ref_mapping(value)
    elif isinstance(value, Mapping):
        stored = value
    else:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.INPUT_NOT_MAPPING,
            "SuccessorOriginAnchorRefV2 must be a mapping",
        )
    if set(stored) != expected_fields:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.FIELD_SET_MISMATCH,
            "successor origin must contain only the edge-anchor reference",
        )
    _require_content_id(
        stored["edge_anchor_id"],
        "successor_origin.edge_anchor_id",
        "edge-anchor:",
    )
    _require_digest(
        stored["edge_anchor_digest"],
        "successor_origin.edge_anchor_digest",
    )
    expected = make_successor_origin_anchor_ref_v2(anchor)
    if dict(stored) != _origin_ref_mapping(expected):
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "successor origin references another edge anchor",
        )
    return expected


def make_raw_target_state_v2(
    projection: CanonicalTargetProjectionV2,
    anchor: EdgeAnchorV2,
) -> RawTargetStateV2:
    """Create the state ID from projection content and only an anchor ref."""

    _require_projection(projection)
    if type(anchor) is not EdgeAnchorV2:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "a sealed EdgeAnchorV2 is required",
        )
    _verify_content_seal(anchor)
    if (
        anchor.projection_id != projection.projection_id
        or anchor.projection_digest != projection.digest
    ):
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "edge anchor belongs to another projection",
        )
    normalized_facts = _copy_pure_json(
        projection.facts,
        path="raw_target.facts",
        reject_dependency_keys=True,
    )
    return _seal(
        RawTargetStateV2,
        {
            "target_schema_id": projection.target_schema_id,
            "target_schema_version": projection.target_schema_version,
            "root_context": projection.root_context,
            "equation_rank": projection.equation_rank,
            "facts": _freeze_json(normalized_facts),
            "mark_behavior": projection.mark_behavior,
            "successor_origin": make_successor_origin_anchor_ref_v2(anchor),
        },
    )


def parse_raw_target_state_v2(
    value: Any,
    projection: CanonicalTargetProjectionV2,
    anchor: EdgeAnchorV2,
) -> RawTargetStateV2:
    stored = _mapping_for(value, RawTargetStateV2)
    if not isinstance(stored["facts"], Mapping):
        raise _malformed("raw_target.facts must be an object")
    _copy_pure_json(
        stored["facts"],
        path="raw_target.facts",
        reject_dependency_keys=True,
    )
    parse_successor_origin_anchor_ref_v2(stored["successor_origin"], anchor)
    replayed = make_raw_target_state_v2(projection, anchor)
    _require_same_artifact(stored, replayed)
    return replayed


def make_final_transition_receipt_bundle_v2(
    anchor: EdgeAnchorV2,
    target: RawTargetStateV2,
    *,
    e1_occurrence_receipt_digest: str,
    e2_projection_receipt_digest: str,
    e3_typing_receipt_digest: str,
    e4_lift_receipt_digest: str,
    e5_ticket_receipt_digest: str,
) -> FinalTransitionReceiptBundleV2:
    """Seal opaque receipt pins only after the target state ID exists."""

    if type(anchor) is not EdgeAnchorV2 or type(target) is not RawTargetStateV2:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "sealed edge anchor and raw target state are required",
        )
    _verify_content_seal(anchor)
    _verify_content_seal(target)
    origin = parse_successor_origin_anchor_ref_v2(target.successor_origin, anchor)
    if origin.edge_anchor_id != anchor.edge_anchor_id:
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "raw target state belongs to another edge anchor",
        )
    receipt_values = {
        "e1_occurrence_receipt_digest": e1_occurrence_receipt_digest,
        "e2_projection_receipt_digest": e2_projection_receipt_digest,
        "e3_typing_receipt_digest": e3_typing_receipt_digest,
        "e4_lift_receipt_digest": e4_lift_receipt_digest,
        "e5_ticket_receipt_digest": e5_ticket_receipt_digest,
    }
    for name, digest in receipt_values.items():
        _require_digest(digest, name)
    return _seal(
        FinalTransitionReceiptBundleV2,
        {
            "source_state_id": anchor.source_state_id,
            "source_state_digest": anchor.source_state_digest,
            "target_state_id": target.state_id,
            "target_state_digest": target.digest,
            "edge_anchor_id": anchor.edge_anchor_id,
            "edge_anchor_digest": anchor.digest,
            **receipt_values,
        },
    )


def parse_final_transition_receipt_bundle_v2(
    value: Any, anchor: EdgeAnchorV2, target: RawTargetStateV2
) -> FinalTransitionReceiptBundleV2:
    stored = _mapping_for(value, FinalTransitionReceiptBundleV2)
    replayed = make_final_transition_receipt_bundle_v2(
        anchor,
        target,
        e1_occurrence_receipt_digest=stored["e1_occurrence_receipt_digest"],
        e2_projection_receipt_digest=stored["e2_projection_receipt_digest"],
        e3_typing_receipt_digest=stored["e3_typing_receipt_digest"],
        e4_lift_receipt_digest=stored["e4_lift_receipt_digest"],
        e5_ticket_receipt_digest=stored["e5_ticket_receipt_digest"],
    )
    _require_same_artifact(stored, replayed)
    return replayed


def make_state_admission_sidecar_v2(
    target: RawTargetStateV2,
    bundle: FinalTransitionReceiptBundleV2,
    *,
    owner_id: str,
    owner_digest: str,
    grammar_digest: str,
    admission_gate_digest: str,
    target_potential_receipt_digest: str,
    state_admission_receipt_digest: str,
) -> StateAdmissionSidecarV2:
    """Seal future admission metadata; this does not decide or authorize it."""

    if (
        type(target) is not RawTargetStateV2
        or type(bundle) is not FinalTransitionReceiptBundleV2
    ):
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "sealed raw target and final transition bundle are required",
        )
    _verify_content_seal(target)
    _verify_content_seal(bundle)
    if (
        bundle.target_state_id != target.state_id
        or bundle.target_state_digest != target.digest
    ):
        raise AcyclicBundleValidationError(
            AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            "transition bundle belongs to another target state",
        )
    _require_text(owner_id, "owner_id")
    digest_values = {
        "owner_digest": owner_digest,
        "grammar_digest": grammar_digest,
        "admission_gate_digest": admission_gate_digest,
        "target_potential_receipt_digest": target_potential_receipt_digest,
        "state_admission_receipt_digest": state_admission_receipt_digest,
    }
    for name, digest in digest_values.items():
        _require_digest(digest, name)
    return _seal(
        StateAdmissionSidecarV2,
        {
            "state_id": target.state_id,
            "state_digest": target.digest,
            "transition_id": bundle.transition_id,
            "transition_bundle_digest": bundle.digest,
            "owner_id": owner_id,
            **digest_values,
        },
    )


def parse_state_admission_sidecar_v2(
    value: Any,
    target: RawTargetStateV2,
    bundle: FinalTransitionReceiptBundleV2,
) -> StateAdmissionSidecarV2:
    stored = _mapping_for(value, StateAdmissionSidecarV2)
    replayed = make_state_admission_sidecar_v2(
        target,
        bundle,
        owner_id=stored["owner_id"],
        owner_digest=stored["owner_digest"],
        grammar_digest=stored["grammar_digest"],
        admission_gate_digest=stored["admission_gate_digest"],
        target_potential_receipt_digest=stored[
            "target_potential_receipt_digest"
        ],
        state_admission_receipt_digest=stored[
            "state_admission_receipt_digest"
        ],
    )
    _require_same_artifact(stored, replayed)
    return replayed


_SEALED_CLASSES = frozenset(
    {
        CanonicalTargetProjectionV2,
        PreclassificationDigestV2,
        TerminalDigestSetV2,
        T5CoordinateDraftV2,
        EdgeAnchorV2,
        RawTargetStateV2,
        FinalTransitionReceiptBundleV2,
        StateAdmissionSidecarV2,
    }
)
