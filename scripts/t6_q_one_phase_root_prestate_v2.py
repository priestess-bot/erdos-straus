#!/usr/bin/env python3
"""Zero-authority q=1 phase-root target-prestate shapes.

This module intentionally stops before owner classification, structured E1--E5
receipts, admission, and queue mutation.  It provides only the acyclic
construction

    P -> {C, L, D} -> A -> Q,

where Q is a non-persistent semantic target prestate.  Its ``state_id`` is a
future semantic identity, not a queue ticket.

``ExternalQOneSourceBindingV2`` binds externally supplied source wire material
only.  It deliberately does not establish source actualness or generic E1.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from dataclasses import dataclass, fields
from enum import Enum
from math import isqrt
from pathlib import Path
import sys
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, Sequence, TypeVar


STATE_CONTRACT_PATH = Path(__file__).resolve().with_name(
    "t6_persistent_selector_state_v1.py"
)
STATE_CONTRACT_PRIVATE_MODULE_NAME = (
    "_t6_q_one_phase_root_prestate_v2_private_state_contract"
)
STATE_CONTRACT_BYTES = STATE_CONTRACT_PATH.read_bytes()
STATE_CONTRACT_MODULE_DIGEST = hashlib.sha256(STATE_CONTRACT_BYTES).hexdigest()
_STATE_CONTRACT_SPEC = importlib.util.spec_from_file_location(
    STATE_CONTRACT_PRIVATE_MODULE_NAME, STATE_CONTRACT_PATH
)
if _STATE_CONTRACT_SPEC is None or _STATE_CONTRACT_SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot load {STATE_CONTRACT_PATH}")
state_contract = importlib.util.module_from_spec(_STATE_CONTRACT_SPEC)
sys.modules[STATE_CONTRACT_PRIVATE_MODULE_NAME] = state_contract
_STATE_CONTRACT_SPEC.loader.exec_module(state_contract)


SCHEMA_VERSION = 1
PERSISTENT_SELECTOR_FACTS_CONTRACT_ID = state_contract.CONTRACT_ID
PHASE_ROOT_PRESTATE_KIND = "NONAUTHORIZING_Q1_PHASE_ROOT_TARGET"
PHASE_ROOT_TRANSITION_KIND = "Q1_G_FULL_CARRIER_PHASE_ROOT"
ROOT_SOL = "ROOT_SOL"
TARGET_SCOPE_HIT = "TARGET_SCOPE_HIT"
TARGET_SCOPE_MISS = "TARGET_SCOPE_MISS"
T5_DRAFT_STATUS = "TARGET_ONLY_NO_TICKET"
EXTERNAL_SOURCE_BINDING_SCOPE = "EXTERNAL_Q1_SOURCE_PREIMAGE_NOT_E1"

FAMILY_PRECEDENCE_V1 = tuple(state_contract.FAMILY_PRECEDENCE_V1)
PREDICTED_OWNER_LABEL = "type_i_full_carrier_post_g"
PREDICTED_OWNER_INDEX = 14

FACT_FIELDS = frozenset(
    {
        "major_phase",
        "type_i_protocol",
        "t5_eta_p",
        "pre_a",
        "absorb_m",
        "absorb_r_epsilon",
        "reset_carrier",
        "endpoint_fiber",
        "relation_q",
        "provenance_kind",
        "full_carrier_scope",
        "atomic_arm",
        "dispatch_status",
        "proper_root_k",
        "proper_root_height_class",
        "proper_root_height",
        "proper_root_r",
        "is_overflow",
        "support_A",
        "carrier_M",
        "overflow_d",
        "chart_R",
        "chart_K",
        "sink_scc_receipt",
        "same_chart_promotion_receipt",
    }
)


class PrestateRejectCode(str, Enum):
    INPUT_NOT_MAPPING = "INPUT_NOT_MAPPING"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    WRONG_ARTIFACT_TYPE = "WRONG_ARTIFACT_TYPE"
    WRONG_SCHEMA_VERSION = "WRONG_SCHEMA_VERSION"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    ID_MISMATCH = "ID_MISMATCH"
    DEPENDENCY_MISMATCH = "DEPENDENCY_MISMATCH"
    MATH_MISMATCH = "MATH_MISMATCH"
    TARGET_SCOPE_HIT = "TARGET_SCOPE_HIT"


class PrestateValidationError(ValueError):
    """Fail-closed validation error with a stable code."""

    def __init__(self, code: PrestateRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: PrestateRejectCode, detail: str) -> PrestateValidationError:
    return PrestateValidationError(code, detail)


def _plain_int(value: Any, minimum: int | None = None) -> bool:
    return type(value) is int and (minimum is None or value >= minimum)


def _require_int(value: Any, name: str, minimum: int | None = None) -> int:
    if not _plain_int(value, minimum):
        suffix = "" if minimum is None else f" >= {minimum}"
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, f"{name} must be an exact int{suffix}")
    return value


def _require_bool(value: Any, name: str) -> bool:
    if type(value) is not bool:
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, f"{name} must be an exact bool")
    return value


def _require_text(value: Any, name: str) -> str:
    if type(value) is not str or not value or value.strip() != value:
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, f"{name} must be a nonempty trimmed string")
    return value


def _is_digest(value: Any) -> bool:
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _require_digest(value: Any, name: str) -> str:
    if not _is_digest(value):
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, f"{name} must be a bare lowercase SHA-256 digest")
    return value


def _require_content_id(value: Any, name: str, prefix: str) -> str:
    text = _require_text(value, name)
    if not text.startswith(prefix) or not _is_digest(text[len(prefix) :]):
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, f"{name} must be {prefix!r} plus a digest")
    return text


def _copy_json(value: Any, path: str = "$") -> Any:
    if value is None or type(value) in {str, int, bool}:
        return value
    if isinstance(value, Mapping):
        copied: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                raise _reject(PrestateRejectCode.MALFORMED_FIELD, f"{path} keys must be nonempty strings")
            copied[key] = _copy_json(child, f"{path}.{key}")
        return copied
    if isinstance(value, (list, tuple)):
        return [_copy_json(child, f"{path}[{index}]") for index, child in enumerate(value)]
    raise _reject(PrestateRejectCode.MALFORMED_FIELD, f"{path} has unsupported type {type(value).__name__}")


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(child) for key, child in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(child) for child in value)
    return value


def canonical_json_v2(value: Any) -> str:
    return json.dumps(
        _copy_json(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


def canonical_digest_v2(value: Any) -> str:
    return hashlib.sha256(canonical_json_v2(value).encode("ascii")).hexdigest()


def loads_strict_v2(encoded: str) -> Any:
    def unique_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise _reject(PrestateRejectCode.FIELD_SET_MISMATCH, f"duplicate JSON key {key!r}")
            result[key] = value
        return result

    try:
        value = json.loads(
            encoded,
            object_pairs_hook=unique_pairs,
            parse_float=lambda _value: (_ for _ in ()).throw(
                _reject(PrestateRejectCode.MALFORMED_FIELD, "floating-point JSON is forbidden")
            ),
            parse_constant=lambda value: (_ for _ in ()).throw(
                _reject(PrestateRejectCode.MALFORMED_FIELD, f"non-finite JSON constant {value!r} is forbidden")
            ),
        )
    except PrestateValidationError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, f"invalid JSON: {exc}") from exc
    return _copy_json(value)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _factorization(value: int) -> tuple[tuple[int, int], ...]:
    """Return a complete factorization without scanning the X^2 divisor range.

    Trial division is a deliberately finite baseline for this zero-authority
    shape.  It is not a claim about large-input terminal-schedule resources.
    """

    value = _require_int(value, "factorization input", 1)
    remaining = value
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def _square_divisors(factors: Sequence[tuple[int, int]]) -> tuple[int, ...]:
    """Generate divisors of X^2 from the already computed factorization of X."""

    divisors = [1]
    for prime, exponent in factors:
        powers = [prime**power for power in range(2 * exponent + 1)]
        divisors = [base * power for base in divisors for power in powers]
    return tuple(sorted(divisors))


def _egyptian_identity(prime: int, denominators: Sequence[int]) -> bool:
    if len(denominators) != 3 or any(not _plain_int(value, 1) for value in denominators):
        return False
    x, y, z = denominators
    return 4 * x * y * z == prime * (x * y + x * z + y * z)


class _FactorySealed:
    __slots__ = ()

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} must be created by its factory")


@dataclass(frozen=True, init=False, slots=True)
class FiniteTerminalFamilyV2(_FactorySealed):
    family_id: str
    family_kind: str
    gap: int | None
    family_digest: str


@dataclass(frozen=True, slots=True)
class _PredicateViewV2:
    """The minimal duck-typed view consumed by public V1 predicates."""

    root_context: int
    equation_rank: int
    mark_kind: str
    facts: Mapping[str, Any]


@dataclass(frozen=True, init=False, slots=True)
class ExternalQOneSourceBindingV2(_FactorySealed):
    """External source binding only; this is explicitly not actual E1."""

    ARTIFACT_TYPE: ClassVar[str] = "ExternalQOneSourceBindingV2"
    ID_FIELD: ClassVar[str] = "source_binding_id"
    ID_PREFIX: ClassVar[str] = "external-q1-source-binding:"

    binding_scope: str
    v1_source_state_id: str
    v1_source_wire_digest: str
    source_prefix_receipt_digest: str
    source_phase_root_preimage_digest: str
    source_binding_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class CanonicalPhaseRootProjectionV2(_FactorySealed):
    ARTIFACT_TYPE: ClassVar[str] = "CanonicalPhaseRootProjectionV2"
    ID_FIELD: ClassVar[str] = "projection_id"
    ID_PREFIX: ClassVar[str] = "phase-root-projection:"

    root_context: int
    equation_rank: int
    t: int
    x: int
    x_factorization: tuple[tuple[int, int], ...]
    mark_kind: str
    facts: Mapping[str, Any]
    projection_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class PhaseRootPreclassificationV2(_FactorySealed):
    ARTIFACT_TYPE: ClassVar[str] = "PhaseRootPreclassificationV2"
    ID_FIELD: ClassVar[str] = "preclassification_id"
    ID_PREFIX: ClassVar[str] = "phase-root-preclassification:"

    projection_id: str
    projection_digest: str
    facts_contract_id: str
    facts_contract_digest: str
    predicate_table_id: str
    predicate_table_digest: str
    precedence_table_id: str
    precedence_table_digest: str
    family_precedence: tuple[str, ...]
    predicate_results: tuple[bool, ...]
    predicted_owner_label: str
    predicted_precedence_index: int
    preclassification_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class PhaseRootFiniteTargetScopeV2(_FactorySealed):
    ARTIFACT_TYPE: ClassVar[str] = "PhaseRootFiniteTargetScopeV2"
    ID_FIELD: ClassVar[str] = "terminal_scope_id"
    ID_PREFIX: ClassVar[str] = "phase-root-terminal-scope:"

    source_binding_id: str
    source_binding_digest: str
    projection_id: str
    projection_digest: str
    target_subject_kind: str
    finite_scope_policy_id: str
    finite_scope_policy_digest: str
    ordered_families: tuple[FiniteTerminalFamilyV2, ...]
    family_replay_digests: tuple[str, ...]
    scope_outcome: str
    hit_index: int | None
    hit_certificate_digest: str | None
    next_unchecked_gap: int | None
    global_exhaustion: bool
    terminal_scope_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class PhaseRootT5CoordinateDraftV2(_FactorySealed):
    ARTIFACT_TYPE: ClassVar[str] = "PhaseRootT5CoordinateDraftV2"
    ID_FIELD: ClassVar[str] = "t5_draft_id"
    ID_PREFIX: ClassVar[str] = "phase-root-t5-draft:"

    projection_id: str
    projection_digest: str
    taxonomy_id: str
    taxonomy_digest: str
    target_coordinates: tuple[int, int, int, int, int, int, int]
    draft_status: str
    t5_draft_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class PhaseRootEdgeAnchorV2(_FactorySealed):
    ARTIFACT_TYPE: ClassVar[str] = "PhaseRootEdgeAnchorV2"
    ID_FIELD: ClassVar[str] = "edge_anchor_id"
    ID_PREFIX: ClassVar[str] = "phase-root-edge-anchor:"

    source_binding_id: str
    source_binding_digest: str
    transition_kind: str
    candidate_witness_digest: str
    projection_id: str
    projection_digest: str
    preclassification_id: str
    preclassification_digest: str
    terminal_scope_id: str
    terminal_scope_digest: str
    t5_draft_id: str
    t5_draft_digest: str
    edge_anchor_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class SuccessorOriginAnchorRefV2(_FactorySealed):
    edge_anchor_id: str
    edge_anchor_digest: str


@dataclass(frozen=True, init=False, slots=True)
class PhaseRootTargetPrestateV2(_FactorySealed):
    ARTIFACT_TYPE: ClassVar[str] = "PhaseRootTargetPrestateV2"
    ID_FIELD: ClassVar[str] = "state_id"
    ID_PREFIX: ClassVar[str] = "state:"

    prestate_kind: str
    root_context: int
    equation_rank: int
    mark_kind: str
    facts: Mapping[str, Any]
    successor_origin: SuccessorOriginAnchorRefV2
    state_id: str
    digest: str


SealedArtifactV2 = (
    ExternalQOneSourceBindingV2
    | CanonicalPhaseRootProjectionV2
    | PhaseRootPreclassificationV2
    | PhaseRootFiniteTargetScopeV2
    | PhaseRootT5CoordinateDraftV2
    | PhaseRootEdgeAnchorV2
    | PhaseRootTargetPrestateV2
)
ArtifactT = TypeVar("ArtifactT", bound=SealedArtifactV2)
_ARTIFACT_CLASSES = frozenset(
    {
        ExternalQOneSourceBindingV2,
        CanonicalPhaseRootProjectionV2,
        PhaseRootPreclassificationV2,
        PhaseRootFiniteTargetScopeV2,
        PhaseRootT5CoordinateDraftV2,
        PhaseRootEdgeAnchorV2,
        PhaseRootTargetPrestateV2,
    }
)


def _facts_for(prime: int) -> dict[str, Any]:
    t = (prime - 1) // 24
    x = 6 * t + 1
    return {
        "major_phase": "TYPEI",
        "type_i_protocol": "CHARGED",
        "t5_eta_p": 0,
        "pre_a": None,
        "absorb_m": None,
        "absorb_r_epsilon": 0,
        "reset_carrier": None,
        "endpoint_fiber": "NONE",
        "relation_q": None,
        "provenance_kind": "FULL_CARRIER_POST_G",
        "full_carrier_scope": True,
        "atomic_arm": "NONE",
        "dispatch_status": "NONE",
        "proper_root_k": None,
        "proper_root_height_class": "NONE",
        "proper_root_height": None,
        "proper_root_r": None,
        "is_overflow": False,
        "support_A": 1,
        "carrier_M": None,
        "overflow_d": None,
        "chart_R": 16 * t + 3,
        "chart_K": x * (16 * t + 1),
        "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }


def _facts_mapping(value: Any, prime: int, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping) or set(value) != FACT_FIELDS:
        raise _reject(PrestateRejectCode.FIELD_SET_MISMATCH, f"{name} must contain exactly the V1 fact fields")
    expected = _facts_for(prime)
    copied = _copy_json(value, name)
    if copied != expected:
        raise _reject(PrestateRejectCode.MATH_MISMATCH, f"{name} is not the canonical q=1 full-carrier target facts")
    return _freeze(copied)


def _q_one_g_factorization(
    prime: int, x: int, value: Any | None = None
) -> tuple[tuple[int, int], ...]:
    expected = _factorization(x)
    if any(factor % 3 != 1 for factor, _exponent in expected):
        raise _reject(
            PrestateRejectCode.MATH_MISMATCH,
            "X=(p+3)/4 is not an ordinary q=1 G factorization",
        )
    if value is None:
        return expected
    if type(value) is not tuple or any(
        type(item) is not tuple
        or len(item) != 2
        or not _plain_int(item[0], 2)
        or not _plain_int(item[1], 1)
        for item in value
    ):
        raise _reject(
            PrestateRejectCode.MALFORMED_FIELD,
            "x_factorization must be an exact tuple of positive prime/exponent pairs",
        )
    if value != expected:
        raise _reject(
            PrestateRejectCode.MATH_MISMATCH,
            "x_factorization does not replay from X",
        )
    return expected


def _factorization_from_wire(value: Any) -> tuple[tuple[int, int], ...]:
    if not isinstance(value, (list, tuple)):
        raise _reject(
            PrestateRejectCode.MALFORMED_FIELD,
            "x_factorization must be an array of prime/exponent pairs",
        )
    pairs: list[tuple[int, int]] = []
    for item in value:
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            raise _reject(
                PrestateRejectCode.MALFORMED_FIELD,
                "x_factorization entries must be two-item arrays",
            )
        pairs.append((item[0], item[1]))
    return tuple(pairs)


def _finite_family(family_id: str, family_kind: str, gap: int | None) -> FiniteTerminalFamilyV2:
    if family_kind not in {"BRADFORD_GAP", "ANCHOR_SINK"}:
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, "unknown finite terminal family kind")
    if family_kind == "BRADFORD_GAP":
        _require_int(gap, "family gap", 1)
    elif gap is not None:
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, "anchor-sink family has no gap")
    payload = {"family_id": family_id, "family_kind": family_kind, "gap": gap}
    instance = object.__new__(FiniteTerminalFamilyV2)
    object.__setattr__(instance, "family_id", family_id)
    object.__setattr__(instance, "family_kind", family_kind)
    object.__setattr__(instance, "gap", gap)
    object.__setattr__(instance, "family_digest", canonical_digest_v2(payload))
    return instance


FIXED_FAMILIES = (
    _finite_family("bradford_gap_3", "BRADFORD_GAP", 3),
    _finite_family("bradford_gap_7", "BRADFORD_GAP", 7),
    _finite_family("bradford_gap_11", "BRADFORD_GAP", 11),
    _finite_family("phase_root_anchor_sink", "ANCHOR_SINK", None),
)
FACTS_CONTRACT_DIGEST = canonical_digest_v2(
    {
        "contract_id": PERSISTENT_SELECTOR_FACTS_CONTRACT_ID,
        "module_sha256": STATE_CONTRACT_MODULE_DIGEST,
        "fact_fields": sorted(FACT_FIELDS),
    }
)
PREDICATE_TABLE_ID = "persistent_selector_state_v1.family_predicates"
PREDICATE_TABLE_DIGEST = canonical_digest_v2(
    {
        "module_sha256": STATE_CONTRACT_MODULE_DIGEST,
        "family_precedence": list(FAMILY_PRECEDENCE_V1),
    }
)
PRECEDENCE_TABLE_ID = "persistent_selector_state_v1.family_precedence"
PRECEDENCE_TABLE_DIGEST = canonical_digest_v2(
    {
        "module_sha256": STATE_CONTRACT_MODULE_DIGEST,
        "family_precedence": list(FAMILY_PRECEDENCE_V1),
    }
)
FINITE_SCOPE_POLICY_ID = "q1_phase_root_bradford_3_7_11_then_anchor_v1"
FINITE_SCOPE_POLICY_DIGEST = canonical_digest_v2(
    {
        "policy_id": FINITE_SCOPE_POLICY_ID,
        "families": [
            {
                "family_id": family.family_id,
                "family_kind": family.family_kind,
                "gap": family.gap,
                "family_digest": family.family_digest,
            }
            for family in FIXED_FAMILIES
        ],
        "next_unchecked_gap": 15,
        "global_exhaustion": False,
    }
)
T5_TAXONOMY_ID = "t5_n7_phase_taxonomy_v1"
T5_TAXONOMY_DIGEST = canonical_digest_v2(
    {"taxonomy_id": T5_TAXONOMY_ID, "phase_ranks": {"TYPEII_G_HANDOFF": 3, "TYPEI": 2}, "charged_rank": 4}
)


def _family_mapping(family: FiniteTerminalFamilyV2) -> dict[str, Any]:
    if type(family) is not FiniteTerminalFamilyV2:
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, "terminal family must have the exact V2 type")
    _require_text(family.family_id, "family_id")
    _require_text(family.family_kind, "family_kind")
    if family.family_kind == "BRADFORD_GAP":
        _require_int(family.gap, "family.gap", 1)
    elif family.family_kind != "ANCHOR_SINK" or family.gap is not None:
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, "terminal family kind/gap mismatch")
    _require_digest(family.family_digest, "family_digest")
    expected = _finite_family(family.family_id, family.family_kind, family.gap)
    if family.family_digest != expected.family_digest:
        raise _reject(PrestateRejectCode.DIGEST_MISMATCH, "terminal family digest does not replay")
    return {
        "family_id": family.family_id,
        "family_kind": family.family_kind,
        "gap": family.gap,
        "family_digest": family.family_digest,
    }


def _origin_mapping(origin: SuccessorOriginAnchorRefV2) -> dict[str, str]:
    if type(origin) is not SuccessorOriginAnchorRefV2:
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, "successor_origin has the wrong type")
    _require_content_id(origin.edge_anchor_id, "successor_origin.edge_anchor_id", PhaseRootEdgeAnchorV2.ID_PREFIX)
    _require_digest(origin.edge_anchor_digest, "successor_origin.edge_anchor_digest")
    return {"edge_anchor_id": origin.edge_anchor_id, "edge_anchor_digest": origin.edge_anchor_digest}


def _external(value: Any) -> Any:
    if type(value) is FiniteTerminalFamilyV2:
        return _family_mapping(value)
    if type(value) is SuccessorOriginAnchorRefV2:
        return _origin_mapping(value)
    if isinstance(value, (list, tuple)):
        return [_external(child) for child in value]
    return _copy_json(value)


def _unsigned_mapping(cls: type[ArtifactT], values: Mapping[str, Any]) -> dict[str, Any]:
    payload: dict[str, Any] = {"artifact_type": cls.ARTIFACT_TYPE, "schema_version": SCHEMA_VERSION}
    for field in fields(cls):
        if field.name not in {cls.ID_FIELD, "digest"}:
            payload[field.name] = _external(values[field.name])
    return payload


def _construct(cls: type[ArtifactT], values: Mapping[str, Any]) -> ArtifactT:
    instance = object.__new__(cls)
    for field in fields(cls):
        object.__setattr__(instance, field.name, values[field.name])
    return instance


def _seal(cls: type[ArtifactT], values: Mapping[str, Any]) -> ArtifactT:
    mutable = dict(values)
    digest = canonical_digest_v2(_unsigned_mapping(cls, mutable))
    mutable[cls.ID_FIELD] = cls.ID_PREFIX + digest
    mutable["digest"] = digest
    artifact = _construct(cls, mutable)
    _verify_own_seal(artifact)
    return artifact


def _verify_own_seal(artifact: SealedArtifactV2) -> None:
    cls = type(artifact)
    if cls not in _ARTIFACT_CLASSES:
        raise _reject(PrestateRejectCode.MALFORMED_FIELD, "not a supported prestate artifact")
    for field in fields(cls):
        if not hasattr(artifact, field.name):
            raise _reject(PrestateRejectCode.MALFORMED_FIELD, f"missing {cls.__name__}.{field.name}")
    _require_content_id(getattr(artifact, cls.ID_FIELD), cls.ID_FIELD, cls.ID_PREFIX)
    _require_digest(artifact.digest, f"{cls.__name__}.digest")
    values = {field.name: getattr(artifact, field.name) for field in fields(cls)}
    expected = canonical_digest_v2(_unsigned_mapping(cls, values))
    if artifact.digest != expected:
        raise _reject(PrestateRejectCode.DIGEST_MISMATCH, f"{cls.__name__} digest does not replay")
    if getattr(artifact, cls.ID_FIELD) != cls.ID_PREFIX + expected:
        raise _reject(PrestateRejectCode.ID_MISMATCH, f"{cls.__name__} ID does not replay")


def _require_ref(
    value: Any, name: str, prefix: str, digest: Any
) -> None:
    _require_content_id(value, name, prefix)
    _require_digest(digest, f"{name}_digest")


def _validate_local_semantics(artifact: SealedArtifactV2) -> None:
    """Validate fixed typed invariants without traversing upstream artifacts."""

    cls = type(artifact)
    if cls is ExternalQOneSourceBindingV2:
        if artifact.binding_scope != EXTERNAL_SOURCE_BINDING_SCOPE:
            raise _reject(
                PrestateRejectCode.MATH_MISMATCH,
                "external source binding must remain explicitly non-E1",
            )
        _require_content_id(artifact.v1_source_state_id, "v1_source_state_id", "state:")
        for name in (
            "v1_source_wire_digest",
            "source_prefix_receipt_digest",
            "source_phase_root_preimage_digest",
        ):
            _require_digest(getattr(artifact, name), name)
        return

    if cls is CanonicalPhaseRootProjectionV2:
        prime = _require_int(artifact.root_context, "projection.root_context", 2)
        if not _is_prime(prime) or prime % 24 != 1:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "projection root_context is not a core prime")
        if artifact.equation_rank != prime or artifact.t != (prime - 1) // 24:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "projection root/t coordinates do not replay")
        if artifact.x != 6 * artifact.t + 1:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "projection X does not replay")
        _q_one_g_factorization(prime, artifact.x, artifact.x_factorization)
        if artifact.mark_kind != ROOT_SOL:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "projection mark must be ROOT_SOL")
        _facts_mapping(artifact.facts, prime, "projection.facts")
        return

    if cls is PhaseRootPreclassificationV2:
        _require_ref(
            artifact.projection_id,
            "projection_id",
            CanonicalPhaseRootProjectionV2.ID_PREFIX,
            artifact.projection_digest,
        )
        expected_constants = {
            "facts_contract_id": PERSISTENT_SELECTOR_FACTS_CONTRACT_ID,
            "facts_contract_digest": FACTS_CONTRACT_DIGEST,
            "predicate_table_id": PREDICATE_TABLE_ID,
            "predicate_table_digest": PREDICATE_TABLE_DIGEST,
            "precedence_table_id": PRECEDENCE_TABLE_ID,
            "precedence_table_digest": PRECEDENCE_TABLE_DIGEST,
            "predicted_owner_label": PREDICTED_OWNER_LABEL,
            "predicted_precedence_index": PREDICTED_OWNER_INDEX,
        }
        for name, expected in expected_constants.items():
            if getattr(artifact, name) != expected:
                raise _reject(PrestateRejectCode.MATH_MISMATCH, f"{name} differs from the fixed V1 predicate view")
        if type(artifact.family_precedence) is not tuple or artifact.family_precedence != FAMILY_PRECEDENCE_V1:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "family precedence differs from the loaded V1 table")
        if (
            type(artifact.predicate_results) is not tuple
            or len(artifact.predicate_results) != len(FAMILY_PRECEDENCE_V1)
            or any(type(value) is not bool for value in artifact.predicate_results)
            or artifact.predicate_results.count(True) != 1
            or not artifact.predicate_results[PREDICTED_OWNER_INDEX]
        ):
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "predicate result vector is not the unique phase-root match")
        return

    if cls is PhaseRootFiniteTargetScopeV2:
        _require_ref(
            artifact.source_binding_id,
            "source_binding_id",
            ExternalQOneSourceBindingV2.ID_PREFIX,
            artifact.source_binding_digest,
        )
        _require_ref(
            artifact.projection_id,
            "projection_id",
            CanonicalPhaseRootProjectionV2.ID_PREFIX,
            artifact.projection_digest,
        )
        if (
            artifact.target_subject_kind != "TARGET_PROJECTION"
            or artifact.finite_scope_policy_id != FINITE_SCOPE_POLICY_ID
            or artifact.finite_scope_policy_digest != FINITE_SCOPE_POLICY_DIGEST
            or type(artifact.global_exhaustion) is not bool
            or artifact.global_exhaustion
        ):
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "finite target scope changed its fixed non-global policy")
        if type(artifact.ordered_families) is not tuple:
            raise _reject(PrestateRejectCode.MALFORMED_FIELD, "ordered_families must be an exact tuple")
        actual_families = tuple(_family_mapping(item) for item in artifact.ordered_families)
        expected_families = tuple(_family_mapping(item) for item in FIXED_FAMILIES)
        if actual_families != expected_families:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "finite target family order changed")
        if (
            type(artifact.family_replay_digests) is not tuple
            or len(artifact.family_replay_digests) != len(FIXED_FAMILIES)
        ):
            raise _reject(PrestateRejectCode.MALFORMED_FIELD, "family replay digest vector has the wrong shape")
        for digest in artifact.family_replay_digests:
            _require_digest(digest, "family_replay_digest")
        if artifact.scope_outcome == TARGET_SCOPE_HIT:
            if (
                not _plain_int(artifact.hit_index, 0)
                or artifact.hit_index >= len(FIXED_FAMILIES)
                or artifact.hit_certificate_digest is None
                or artifact.next_unchecked_gap is not None
            ):
                raise _reject(PrestateRejectCode.MATH_MISMATCH, "finite HIT fields do not replay")
            _require_digest(artifact.hit_certificate_digest, "hit_certificate_digest")
            return
        if artifact.scope_outcome != TARGET_SCOPE_MISS:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "unknown finite target outcome")
        if (
            artifact.hit_index is not None
            or artifact.hit_certificate_digest is not None
            or artifact.next_unchecked_gap != 15
        ):
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "finite MISS fields do not replay")
        return

    if cls is PhaseRootT5CoordinateDraftV2:
        _require_ref(
            artifact.projection_id,
            "projection_id",
            CanonicalPhaseRootProjectionV2.ID_PREFIX,
            artifact.projection_digest,
        )
        if (
            artifact.taxonomy_id != T5_TAXONOMY_ID
            or artifact.taxonomy_digest != T5_TAXONOMY_DIGEST
            or artifact.draft_status != T5_DRAFT_STATUS
            or type(artifact.target_coordinates) is not tuple
            or len(artifact.target_coordinates) != 7
            or any(not _plain_int(value, 0) for value in artifact.target_coordinates)
        ):
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "T5 draft local fields do not replay")
        return

    if cls is PhaseRootEdgeAnchorV2:
        _require_ref(
            artifact.source_binding_id,
            "source_binding_id",
            ExternalQOneSourceBindingV2.ID_PREFIX,
            artifact.source_binding_digest,
        )
        if artifact.transition_kind != PHASE_ROOT_TRANSITION_KIND:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "edge anchor has the wrong transition kind")
        _require_digest(artifact.candidate_witness_digest, "candidate_witness_digest")
        for identifier, prefix, digest in (
            (artifact.projection_id, CanonicalPhaseRootProjectionV2.ID_PREFIX, artifact.projection_digest),
            (artifact.preclassification_id, PhaseRootPreclassificationV2.ID_PREFIX, artifact.preclassification_digest),
            (artifact.terminal_scope_id, PhaseRootFiniteTargetScopeV2.ID_PREFIX, artifact.terminal_scope_digest),
            (artifact.t5_draft_id, PhaseRootT5CoordinateDraftV2.ID_PREFIX, artifact.t5_draft_digest),
        ):
            _require_ref(identifier, "edge_anchor_dependency", prefix, digest)
        return

    if cls is PhaseRootTargetPrestateV2:
        if artifact.prestate_kind != PHASE_ROOT_PRESTATE_KIND:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "prestate kind is not the fixed zero-authority kind")
        prime = _require_int(artifact.root_context, "prestate.root_context", 2)
        if artifact.equation_rank != prime or artifact.mark_kind != ROOT_SOL:
            raise _reject(PrestateRejectCode.MATH_MISMATCH, "prestate root/equation/mark fields do not replay")
        _facts_mapping(artifact.facts, prime, "prestate.facts")
        _origin_mapping(artifact.successor_origin)
        return

    raise _reject(PrestateRejectCode.MALFORMED_FIELD, "unsupported local artifact type")


def artifact_to_mapping_v2(artifact: SealedArtifactV2) -> dict[str, Any]:
    _verify_own_seal(artifact)
    _validate_local_semantics(artifact)
    cls = type(artifact)
    values = {field.name: getattr(artifact, field.name) for field in fields(cls)}
    mapping = _unsigned_mapping(cls, values)
    mapping[cls.ID_FIELD] = getattr(artifact, cls.ID_FIELD)
    mapping["digest"] = artifact.digest
    return mapping


def _mapping_for(value: Any, cls: type[ArtifactT]) -> Mapping[str, Any]:
    if type(value) is cls:
        return artifact_to_mapping_v2(value)
    if not isinstance(value, Mapping):
        raise _reject(PrestateRejectCode.INPUT_NOT_MAPPING, f"{cls.__name__} must be a mapping")
    expected = {"artifact_type", "schema_version"} | {field.name for field in fields(cls)}
    if set(value) != expected:
        raise _reject(PrestateRejectCode.FIELD_SET_MISMATCH, f"{cls.__name__} has an unknown, forbidden, or missing field")
    if value.get("artifact_type") != cls.ARTIFACT_TYPE:
        raise _reject(PrestateRejectCode.WRONG_ARTIFACT_TYPE, f"expected {cls.ARTIFACT_TYPE}")
    if type(value.get("schema_version")) is not int or value.get("schema_version") != SCHEMA_VERSION:
        raise _reject(PrestateRejectCode.WRONG_SCHEMA_VERSION, f"expected schema version {SCHEMA_VERSION}")
    _require_content_id(value[cls.ID_FIELD], cls.ID_FIELD, cls.ID_PREFIX)
    _require_digest(value["digest"], f"{cls.__name__}.digest")
    unsigned = {
        key: item
        for key, item in value.items()
        if key not in {cls.ID_FIELD, "digest"}
    }
    expected_digest = canonical_digest_v2(unsigned)
    if value["digest"] != expected_digest:
        raise _reject(PrestateRejectCode.DIGEST_MISMATCH, f"{cls.__name__} wire digest does not replay")
    if value[cls.ID_FIELD] != cls.ID_PREFIX + expected_digest:
        raise _reject(PrestateRejectCode.ID_MISMATCH, f"{cls.__name__} wire ID does not replay")
    return value


def _same(stored: Mapping[str, Any], replayed: SealedArtifactV2) -> None:
    expected = artifact_to_mapping_v2(replayed)
    if canonical_json_v2(dict(stored)) != canonical_json_v2(expected):
        if stored.get("digest") != replayed.digest:
            code = PrestateRejectCode.DIGEST_MISMATCH
        elif stored.get(type(replayed).ID_FIELD) != getattr(replayed, type(replayed).ID_FIELD):
            code = PrestateRejectCode.ID_MISMATCH
        else:
            code = PrestateRejectCode.DEPENDENCY_MISMATCH
        raise _reject(code, f"{type(replayed).__name__} does not replay from its dependencies")


def make_external_q_one_source_binding_v2(
    *,
    v1_source_state_id: str,
    v1_source_wire_digest: str,
    source_prefix_receipt_digest: str,
    source_phase_root_preimage_digest: str,
) -> ExternalQOneSourceBindingV2:
    """Bind externally supplied source material without asserting actual E1."""

    _require_content_id(v1_source_state_id, "v1_source_state_id", "state:")
    _require_digest(v1_source_wire_digest, "v1_source_wire_digest")
    _require_digest(source_prefix_receipt_digest, "source_prefix_receipt_digest")
    _require_digest(
        source_phase_root_preimage_digest, "source_phase_root_preimage_digest"
    )
    return _seal(
        ExternalQOneSourceBindingV2,
        {
            "binding_scope": EXTERNAL_SOURCE_BINDING_SCOPE,
            "v1_source_state_id": v1_source_state_id,
            "v1_source_wire_digest": v1_source_wire_digest,
            "source_prefix_receipt_digest": source_prefix_receipt_digest,
            "source_phase_root_preimage_digest": source_phase_root_preimage_digest,
        },
    )


def _require_source_binding(value: Any) -> ExternalQOneSourceBindingV2:
    if type(value) is not ExternalQOneSourceBindingV2:
        raise _reject(
            PrestateRejectCode.DEPENDENCY_MISMATCH,
            "an ExternalQOneSourceBindingV2 is required",
        )
    _verify_own_seal(value)
    expected = make_external_q_one_source_binding_v2(
        v1_source_state_id=value.v1_source_state_id,
        v1_source_wire_digest=value.v1_source_wire_digest,
        source_prefix_receipt_digest=value.source_prefix_receipt_digest,
        source_phase_root_preimage_digest=value.source_phase_root_preimage_digest,
    )
    _same(artifact_to_mapping_v2(value), expected)
    return value


def parse_external_q_one_source_binding_v2(
    value: Any,
) -> ExternalQOneSourceBindingV2:
    stored = _mapping_for(value, ExternalQOneSourceBindingV2)
    if stored["binding_scope"] != EXTERNAL_SOURCE_BINDING_SCOPE:
        raise _reject(
            PrestateRejectCode.DEPENDENCY_MISMATCH,
            "source binding cannot claim actual E1 or another scope",
        )
    replayed = make_external_q_one_source_binding_v2(
        v1_source_state_id=stored["v1_source_state_id"],
        v1_source_wire_digest=stored["v1_source_wire_digest"],
        source_prefix_receipt_digest=stored["source_prefix_receipt_digest"],
        source_phase_root_preimage_digest=stored[
            "source_phase_root_preimage_digest"
        ],
    )
    _same(stored, replayed)
    return replayed


def _require_projection(value: Any) -> CanonicalPhaseRootProjectionV2:
    if type(value) is not CanonicalPhaseRootProjectionV2:
        raise _reject(PrestateRejectCode.DEPENDENCY_MISMATCH, "a canonical phase-root projection is required")
    _verify_own_seal(value)
    prime = _require_int(value.root_context, "projection.root_context", 2)
    if not _is_prime(prime) or prime % 24 != 1:
        raise _reject(PrestateRejectCode.MATH_MISMATCH, "projection root_context is not a core prime")
    if value.equation_rank != prime or value.t != (prime - 1) // 24 or value.x != 6 * value.t + 1:
        raise _reject(PrestateRejectCode.MATH_MISMATCH, "projection p/t/x coordinates do not replay")
    _q_one_g_factorization(prime, value.x, value.x_factorization)
    if value.mark_kind != ROOT_SOL:
        raise _reject(PrestateRejectCode.MATH_MISMATCH, "phase-root prestate requires ROOT_SOL")
    _facts_mapping(value.facts, prime, "projection.facts")
    return value


def make_canonical_phase_root_projection_v2(prime: int) -> CanonicalPhaseRootProjectionV2:
    prime = _require_int(prime, "prime", 2)
    if not _is_prime(prime) or prime % 24 != 1:
        raise _reject(PrestateRejectCode.MATH_MISMATCH, "prime must be a core prime")
    t = (prime - 1) // 24
    x = 6 * t + 1
    values: dict[str, Any] = {
        "root_context": prime,
        "equation_rank": prime,
        "t": t,
        "x": x,
        "x_factorization": _q_one_g_factorization(prime, x),
        "mark_kind": ROOT_SOL,
        "facts": _freeze(_facts_for(prime)),
    }
    return _seal(CanonicalPhaseRootProjectionV2, values)


def parse_canonical_phase_root_projection_v2(value: Any) -> CanonicalPhaseRootProjectionV2:
    stored = _mapping_for(value, CanonicalPhaseRootProjectionV2)
    prime = _require_int(stored["root_context"], "projection.root_context", 2)
    x = _require_int(stored["x"], "projection.x", 1)
    _facts_mapping(stored["facts"], prime, "projection.facts")
    _q_one_g_factorization(
        prime, x, _factorization_from_wire(stored["x_factorization"])
    )
    replayed = make_canonical_phase_root_projection_v2(prime)
    _same(stored, replayed)
    return replayed


def _predicate_view(
    projection: CanonicalPhaseRootProjectionV2,
) -> _PredicateViewV2:
    """Expose only the four attributes read by the public V1 predicates."""

    return _PredicateViewV2(
        root_context=projection.root_context,
        equation_rank=projection.equation_rank,
        mark_kind=state_contract.ROOT_SOL,
        facts=MappingProxyType(dict(projection.facts)),
    )


def _replay_v1_preclassification(
    projection: CanonicalPhaseRootProjectionV2,
) -> tuple[tuple[bool, ...], str, int]:
    header = _predicate_view(projection)
    predicates = tuple(state_contract.FAMILY_PREDICATES_V1)
    family_precedence = tuple(item.family_id for item in predicates)
    if family_precedence != FAMILY_PRECEDENCE_V1:
        raise _reject(
            PrestateRejectCode.DEPENDENCY_MISMATCH,
            "loaded V1 predicate order differs from its public precedence table",
        )
    results = tuple(bool(item.predicate(header)) for item in predicates)
    matches = tuple(
        family_id
        for family_id, matched in zip(family_precedence, results)
        if matched
    )
    if matches != (PREDICTED_OWNER_LABEL,):
        raise _reject(
            PrestateRejectCode.MATH_MISMATCH,
            "canonical phase-root facts do not have the unique expected V1 match",
        )
    return results, matches[0], family_precedence.index(matches[0])


def make_phase_root_preclassification_v2(
    projection: CanonicalPhaseRootProjectionV2,
) -> PhaseRootPreclassificationV2:
    projection = _require_projection(projection)
    predicate_results, predicted_owner, predicted_index = _replay_v1_preclassification(
        projection
    )
    return _seal(
        PhaseRootPreclassificationV2,
        {
            "projection_id": projection.projection_id,
            "projection_digest": projection.digest,
            "facts_contract_id": PERSISTENT_SELECTOR_FACTS_CONTRACT_ID,
            "facts_contract_digest": FACTS_CONTRACT_DIGEST,
            "predicate_table_id": PREDICATE_TABLE_ID,
            "predicate_table_digest": PREDICATE_TABLE_DIGEST,
            "precedence_table_id": PRECEDENCE_TABLE_ID,
            "precedence_table_digest": PRECEDENCE_TABLE_DIGEST,
            "family_precedence": FAMILY_PRECEDENCE_V1,
            "predicate_results": predicate_results,
            "predicted_owner_label": predicted_owner,
            "predicted_precedence_index": predicted_index,
        },
    )


def _require_preclassification(value: Any, projection: CanonicalPhaseRootProjectionV2) -> PhaseRootPreclassificationV2:
    if type(value) is not PhaseRootPreclassificationV2:
        raise _reject(PrestateRejectCode.DEPENDENCY_MISMATCH, "a phase-root preclassification is required")
    _verify_own_seal(value)
    expected = make_phase_root_preclassification_v2(projection)
    _same(artifact_to_mapping_v2(value), expected)
    return value


def parse_phase_root_preclassification_v2(
    value: Any, projection: CanonicalPhaseRootProjectionV2
) -> PhaseRootPreclassificationV2:
    stored = _mapping_for(value, PhaseRootPreclassificationV2)
    replayed = make_phase_root_preclassification_v2(projection)
    _same(stored, replayed)
    return replayed


def _bradford_candidate(prime: int, gap: int) -> dict[str, Any] | None:
    x = (prime + gap) // 4
    if 4 * x != prime + gap:
        raise _reject(PrestateRejectCode.MATH_MISMATCH, "Bradford gap does not yield an integer first denominator")
    for divisor in _square_divisors(_factorization(x)):
        cofactor = x * x // divisor
        if (prime * x + divisor) % gap == 0 and (prime * (x + prime * cofactor)) % gap == 0:
            denominators = (x, (prime * x + divisor) // gap, prime * (x + prime * cofactor) // gap)
            if _egyptian_identity(prime, denominators):
                return {
                    "candidate_kind": "TYPEI",
                    "gap": gap,
                    "divisor": divisor,
                    "denominators": list(denominators),
                }
        if (
            divisor <= x
            and (x + divisor) % gap == 0
            and (prime * (x + divisor)) % gap == 0
            and (prime * (x + cofactor)) % gap == 0
        ):
            denominators = (x, prime * (x + divisor) // gap, prime * (x + cofactor) // gap)
            if _egyptian_identity(prime, denominators):
                return {
                    "candidate_kind": "TYPEII",
                    "gap": gap,
                    "divisor": divisor,
                    "denominators": list(denominators),
                }
    return None


def _anchor_candidate(projection: CanonicalPhaseRootProjectionV2) -> dict[str, Any] | None:
    facts = projection.facts
    chart_r = int(facts["chart_R"])
    chart_k = int(facts["chart_K"])
    anchor = chart_r - 1
    if chart_k % anchor:
        return None
    denominators = (chart_k // anchor, chart_k, projection.root_context * chart_k)
    if not _egyptian_identity(projection.root_context, denominators):
        raise _reject(PrestateRejectCode.MATH_MISMATCH, "anchor candidate lost the reciprocal identity")
    return {
        "candidate_kind": "ANCHOR_SINK",
        "gap": None,
        "divisor": anchor,
        "denominators": list(denominators),
    }


def _scope_results(projection: CanonicalPhaseRootProjectionV2) -> tuple[tuple[str, ...], int | None, str | None]:
    results: list[str] = []
    hit_index: int | None = None
    hit_digest: str | None = None
    for index, family in enumerate(FIXED_FAMILIES):
        candidate = (
            _bradford_candidate(projection.root_context, int(family.gap))
            if family.family_kind == "BRADFORD_GAP"
            else _anchor_candidate(projection)
        )
        result = {
            "family_id": family.family_id,
            "family_digest": family.family_digest,
            "outcome": "HIT" if candidate is not None else "MISS",
            "candidate": candidate,
        }
        results.append(canonical_digest_v2(result))
        if candidate is not None and hit_index is None:
            hit_index = index
            hit_digest = canonical_digest_v2(candidate)
    return tuple(results), hit_index, hit_digest


def make_phase_root_finite_target_scope_v2(
    projection: CanonicalPhaseRootProjectionV2,
    source_binding: ExternalQOneSourceBindingV2,
) -> PhaseRootFiniteTargetScopeV2:
    projection = _require_projection(projection)
    source_binding = _require_source_binding(source_binding)
    replay_digests, hit_index, hit_digest = _scope_results(projection)
    outcome = TARGET_SCOPE_HIT if hit_index is not None else TARGET_SCOPE_MISS
    return _seal(
        PhaseRootFiniteTargetScopeV2,
        {
            "source_binding_id": source_binding.source_binding_id,
            "source_binding_digest": source_binding.digest,
            "projection_id": projection.projection_id,
            "projection_digest": projection.digest,
            "target_subject_kind": "TARGET_PROJECTION",
            "finite_scope_policy_id": FINITE_SCOPE_POLICY_ID,
            "finite_scope_policy_digest": FINITE_SCOPE_POLICY_DIGEST,
            "ordered_families": FIXED_FAMILIES,
            "family_replay_digests": replay_digests,
            "scope_outcome": outcome,
            "hit_index": hit_index,
            "hit_certificate_digest": hit_digest,
            "next_unchecked_gap": None if hit_index is not None else 15,
            "global_exhaustion": False,
        },
    )


def _require_terminal_scope(
    value: Any,
    projection: CanonicalPhaseRootProjectionV2,
    source_binding: ExternalQOneSourceBindingV2,
) -> PhaseRootFiniteTargetScopeV2:
    if type(value) is not PhaseRootFiniteTargetScopeV2:
        raise _reject(PrestateRejectCode.DEPENDENCY_MISMATCH, "a phase-root target scope is required")
    _verify_own_seal(value)
    expected = make_phase_root_finite_target_scope_v2(projection, source_binding)
    _same(artifact_to_mapping_v2(value), expected)
    return value


def parse_phase_root_finite_target_scope_v2(
    value: Any,
    projection: CanonicalPhaseRootProjectionV2,
    source_binding: ExternalQOneSourceBindingV2,
) -> PhaseRootFiniteTargetScopeV2:
    stored = _mapping_for(value, PhaseRootFiniteTargetScopeV2)
    replayed = make_phase_root_finite_target_scope_v2(projection, source_binding)
    _same(stored, replayed)
    return replayed


def make_phase_root_t5_coordinate_draft_v2(
    projection: CanonicalPhaseRootProjectionV2,
) -> PhaseRootT5CoordinateDraftV2:
    projection = _require_projection(projection)
    chart_k = int(projection.facts["chart_K"])
    b_p = (projection.root_context - 1) ** 2 // 4
    return _seal(
        PhaseRootT5CoordinateDraftV2,
        {
            "projection_id": projection.projection_id,
            "projection_digest": projection.digest,
            "taxonomy_id": T5_TAXONOMY_ID,
            "taxonomy_digest": T5_TAXONOMY_DIGEST,
            "target_coordinates": (projection.root_context, 2, 4, b_p, chart_k, 0, 0),
            "draft_status": T5_DRAFT_STATUS,
        },
    )


def _require_t5_draft(value: Any, projection: CanonicalPhaseRootProjectionV2) -> PhaseRootT5CoordinateDraftV2:
    if type(value) is not PhaseRootT5CoordinateDraftV2:
        raise _reject(PrestateRejectCode.DEPENDENCY_MISMATCH, "a phase-root T5 draft is required")
    _verify_own_seal(value)
    expected = make_phase_root_t5_coordinate_draft_v2(projection)
    _same(artifact_to_mapping_v2(value), expected)
    return value


def parse_phase_root_t5_coordinate_draft_v2(
    value: Any, projection: CanonicalPhaseRootProjectionV2
) -> PhaseRootT5CoordinateDraftV2:
    stored = _mapping_for(value, PhaseRootT5CoordinateDraftV2)
    replayed = make_phase_root_t5_coordinate_draft_v2(projection)
    _same(stored, replayed)
    return replayed


def _candidate_witness_digest(projection: CanonicalPhaseRootProjectionV2) -> str:
    return canonical_digest_v2(
        {
            "transition_kind": PHASE_ROOT_TRANSITION_KIND,
            "prime": projection.root_context,
            "q": 1,
            "formula": "R=16t+3,K=(6t+1)(16t+1),A=1",
        }
    )


def make_phase_root_edge_anchor_v2(
    projection: CanonicalPhaseRootProjectionV2,
    preclassification: PhaseRootPreclassificationV2,
    terminal_scope: PhaseRootFiniteTargetScopeV2,
    t5_draft: PhaseRootT5CoordinateDraftV2,
    source_binding: ExternalQOneSourceBindingV2,
) -> PhaseRootEdgeAnchorV2:
    projection = _require_projection(projection)
    preclassification = _require_preclassification(preclassification, projection)
    source_binding = _require_source_binding(source_binding)
    terminal_scope = _require_terminal_scope(
        terminal_scope, projection, source_binding
    )
    t5_draft = _require_t5_draft(t5_draft, projection)
    if terminal_scope.scope_outcome != TARGET_SCOPE_MISS:
        raise _reject(
            PrestateRejectCode.TARGET_SCOPE_HIT,
            "a finite target-scope HIT must preempt edge-anchor construction",
        )
    return _seal(
        PhaseRootEdgeAnchorV2,
        {
            "source_binding_id": source_binding.source_binding_id,
            "source_binding_digest": source_binding.digest,
            "transition_kind": PHASE_ROOT_TRANSITION_KIND,
            "candidate_witness_digest": _candidate_witness_digest(projection),
            "projection_id": projection.projection_id,
            "projection_digest": projection.digest,
            "preclassification_id": preclassification.preclassification_id,
            "preclassification_digest": preclassification.digest,
            "terminal_scope_id": terminal_scope.terminal_scope_id,
            "terminal_scope_digest": terminal_scope.digest,
            "t5_draft_id": t5_draft.t5_draft_id,
            "t5_draft_digest": t5_draft.digest,
        },
    )


def _require_anchor(
    value: Any,
    projection: CanonicalPhaseRootProjectionV2,
    preclassification: PhaseRootPreclassificationV2,
    terminal_scope: PhaseRootFiniteTargetScopeV2,
    t5_draft: PhaseRootT5CoordinateDraftV2,
    source_binding: ExternalQOneSourceBindingV2,
) -> PhaseRootEdgeAnchorV2:
    if type(value) is not PhaseRootEdgeAnchorV2:
        raise _reject(PrestateRejectCode.DEPENDENCY_MISMATCH, "a phase-root edge anchor is required")
    _verify_own_seal(value)
    expected = make_phase_root_edge_anchor_v2(
        projection,
        preclassification,
        terminal_scope,
        t5_draft,
        source_binding,
    )
    _same(artifact_to_mapping_v2(value), expected)
    return value


def parse_phase_root_edge_anchor_v2(
    value: Any,
    projection: CanonicalPhaseRootProjectionV2,
    preclassification: PhaseRootPreclassificationV2,
    terminal_scope: PhaseRootFiniteTargetScopeV2,
    t5_draft: PhaseRootT5CoordinateDraftV2,
    source_binding: ExternalQOneSourceBindingV2,
) -> PhaseRootEdgeAnchorV2:
    stored = _mapping_for(value, PhaseRootEdgeAnchorV2)
    replayed = make_phase_root_edge_anchor_v2(
        projection,
        preclassification,
        terminal_scope,
        t5_draft,
        source_binding,
    )
    _same(stored, replayed)
    return replayed


def make_successor_origin_anchor_ref_v2(anchor: PhaseRootEdgeAnchorV2) -> SuccessorOriginAnchorRefV2:
    if type(anchor) is not PhaseRootEdgeAnchorV2:
        raise _reject(PrestateRejectCode.DEPENDENCY_MISMATCH, "an edge anchor is required")
    _verify_own_seal(anchor)
    ref = object.__new__(SuccessorOriginAnchorRefV2)
    object.__setattr__(ref, "edge_anchor_id", anchor.edge_anchor_id)
    object.__setattr__(ref, "edge_anchor_digest", anchor.digest)
    _origin_mapping(ref)
    return ref


def parse_successor_origin_anchor_ref_v2(
    value: Any, anchor: PhaseRootEdgeAnchorV2
) -> SuccessorOriginAnchorRefV2:
    expected_fields = {field.name for field in fields(SuccessorOriginAnchorRefV2)}
    if type(value) is SuccessorOriginAnchorRefV2:
        stored = _origin_mapping(value)
    elif isinstance(value, Mapping):
        stored = value
    else:
        raise _reject(PrestateRejectCode.INPUT_NOT_MAPPING, "successor_origin must be a mapping")
    if set(stored) != expected_fields:
        raise _reject(PrestateRejectCode.FIELD_SET_MISMATCH, "successor_origin contains a forbidden field")
    _require_content_id(stored["edge_anchor_id"], "successor_origin.edge_anchor_id", PhaseRootEdgeAnchorV2.ID_PREFIX)
    _require_digest(stored["edge_anchor_digest"], "successor_origin.edge_anchor_digest")
    expected = make_successor_origin_anchor_ref_v2(anchor)
    if dict(stored) != _origin_mapping(expected):
        raise _reject(PrestateRejectCode.DEPENDENCY_MISMATCH, "successor_origin refers to another edge anchor")
    return expected


def make_phase_root_target_prestate_v2(
    projection: CanonicalPhaseRootProjectionV2,
    anchor: PhaseRootEdgeAnchorV2,
    terminal_scope: PhaseRootFiniteTargetScopeV2,
    source_binding: ExternalQOneSourceBindingV2,
) -> PhaseRootTargetPrestateV2:
    projection = _require_projection(projection)
    preclassification = make_phase_root_preclassification_v2(projection)
    t5_draft = make_phase_root_t5_coordinate_draft_v2(projection)
    source_binding = _require_source_binding(source_binding)
    anchor = _require_anchor(
        anchor,
        projection,
        preclassification,
        terminal_scope,
        t5_draft,
        source_binding,
    )
    terminal_scope = _require_terminal_scope(
        terminal_scope, projection, source_binding
    )
    if terminal_scope.scope_outcome != TARGET_SCOPE_MISS:
        raise _reject(PrestateRejectCode.TARGET_SCOPE_HIT, "a finite target-scope HIT must preempt prestate construction")
    return _seal(
        PhaseRootTargetPrestateV2,
        {
            "prestate_kind": PHASE_ROOT_PRESTATE_KIND,
            "root_context": projection.root_context,
            "equation_rank": projection.equation_rank,
            "mark_kind": projection.mark_kind,
            "facts": _freeze(_copy_json(projection.facts)),
            "successor_origin": make_successor_origin_anchor_ref_v2(anchor),
        },
    )


def parse_phase_root_target_prestate_v2(
    value: Any,
    projection: CanonicalPhaseRootProjectionV2,
    anchor: PhaseRootEdgeAnchorV2,
    terminal_scope: PhaseRootFiniteTargetScopeV2,
    source_binding: ExternalQOneSourceBindingV2,
) -> PhaseRootTargetPrestateV2:
    stored = _mapping_for(value, PhaseRootTargetPrestateV2)
    preclassification = make_phase_root_preclassification_v2(projection)
    t5_draft = make_phase_root_t5_coordinate_draft_v2(projection)
    _require_anchor(
        anchor,
        projection,
        preclassification,
        terminal_scope,
        t5_draft,
        source_binding,
    )
    parse_successor_origin_anchor_ref_v2(stored["successor_origin"], anchor)
    replayed = make_phase_root_target_prestate_v2(
        projection, anchor, terminal_scope, source_binding
    )
    _same(stored, replayed)
    return replayed


__all__ = [
    "CanonicalPhaseRootProjectionV2",
    "EXTERNAL_SOURCE_BINDING_SCOPE",
    "ExternalQOneSourceBindingV2",
    "FiniteTerminalFamilyV2",
    "PHASE_ROOT_PRESTATE_KIND",
    "PREDICTED_OWNER_INDEX",
    "PREDICTED_OWNER_LABEL",
    "PhaseRootEdgeAnchorV2",
    "PhaseRootFiniteTargetScopeV2",
    "PhaseRootPreclassificationV2",
    "PhaseRootT5CoordinateDraftV2",
    "PhaseRootTargetPrestateV2",
    "PrestateRejectCode",
    "PrestateValidationError",
    "SuccessorOriginAnchorRefV2",
    "TARGET_SCOPE_HIT",
    "TARGET_SCOPE_MISS",
    "artifact_to_mapping_v2",
    "canonical_digest_v2",
    "canonical_json_v2",
    "loads_strict_v2",
    "make_canonical_phase_root_projection_v2",
    "make_external_q_one_source_binding_v2",
    "make_phase_root_edge_anchor_v2",
    "make_phase_root_finite_target_scope_v2",
    "make_phase_root_preclassification_v2",
    "make_phase_root_t5_coordinate_draft_v2",
    "make_phase_root_target_prestate_v2",
    "parse_canonical_phase_root_projection_v2",
    "parse_external_q_one_source_binding_v2",
    "parse_phase_root_edge_anchor_v2",
    "parse_phase_root_finite_target_scope_v2",
    "parse_phase_root_preclassification_v2",
    "parse_phase_root_t5_coordinate_draft_v2",
    "parse_phase_root_target_prestate_v2",
]
