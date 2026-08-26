#!/usr/bin/env python3
"""Acyclic, evidence-only q=1 G root-initializer envelope shapes V2.

This module provides the root analogue of the successor-only acyclic V2
transition shapes.  Its construction order is deliberately one-way::

    raw q=1 G integers
        -> CanonicalQOneGSourceBodyV2
        -> RootInitializerAnchorV2          (contains no state_id)
        -> RawRootSourceStateV2 / state_id  (contains only an anchor ref)

The anchor commits to the canonical source body before the source state ID
exists.  The state then commits to that anchor.  No object in this module
contains a terminal result, schedule, owner, potential, E1--E5 receipt,
transition, admission sidecar, or queue token, so a later terminal issuer can
bind the resulting SOURCE_STATE without creating a content-addressing cycle.

All public factories require exact factory-sealed upstream classes and replay
every typed field and content seal before use.  Frozen slotted dataclasses are
only an API convenience: downstream validation also rejects objects forged via
``object.__new__`` / ``object.__setattr__`` when their typed invariants fail.

These shapes grant no authority.  ``contract_digest`` is a fixed digest of the
structural contract declared in this module, not a Git provenance or role grant.
``domain_replay_digest`` is an opaque evidence pin.  Neither can authorize an
initializer, terminal issuer, admission decision, or queue mutation.
"""

from __future__ import annotations

from dataclasses import dataclass, fields, is_dataclass
from enum import Enum
import hashlib
from math import isqrt
import json
import re
from typing import Any, ClassVar, Mapping, NoReturn, TypeVar


SCHEMA_VERSION = 2
RAW_SCHEMA_ID = "q1_root_initializer_raw_v2"
RAW_SCHEMA_VERSION = 2

SOURCE_TREE_SCOPE = "type_ii_endpoint_only"
EVIDENCE_CLASS = "EVIDENCE_ONLY_ROOT_SOURCE"
ROOT_ORIGIN_KIND = "PARENTLESS_ROOT"

INITIALIZER_ID = "q_one_root_initializer_envelope_v2"
DOMAIN_REPLAY_ID = "q_one_g_raw_integer_replay_v2"

ENDPOINT_G = 2
PHASE_TYPEII_G_HANDOFF = 3
PROVENANCE_ORDINARY_ENDPOINT = 1
MARK_ROOT_SOL = 1

BODY_ID_PREFIX = "q1-source-body:"
ANCHOR_ID_PREFIX = "root-init-anchor:"
STATE_ID_PREFIX = "state:"

RAW_FIELDS = frozenset(
    {
        "schema_id",
        "schema_version",
        "root_context",
        "equation_rank",
        "equation_numerator",
        "equation_denominator",
        "q",
        "gap_three_x",
        "endpoint_fiber_code",
        "major_phase_code",
        "provenance_code",
        "mark_kind_code",
        "mark_root_context",
        "mark_equation_rank",
        "gap_three_factorization",
    }
)

SEMANTIC_FIELD_NAMES = (
    "root_context",
    "equation_rank",
    "equation_numerator",
    "equation_denominator",
    "q",
    "gap_three_x",
    "endpoint_fiber_code",
    "major_phase_code",
    "provenance_code",
    "mark_kind_code",
    "mark_root_context",
    "mark_equation_rank",
    "gap_three_factorization",
)

AUTHORITY_FIELD_NAMES = (
    "initializer_authority",
    "admission_authority",
    "queue_authority",
)

_DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")


class RootInitializerRejectCode(str, Enum):
    """Stable failure codes for the V2 root-initializer boundary."""

    INPUT_NOT_EXACT_TYPE = "INPUT_NOT_EXACT_TYPE"
    INPUT_NOT_EXACT_MAPPING = "INPUT_NOT_EXACT_MAPPING"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    WRONG_ARTIFACT_TYPE = "WRONG_ARTIFACT_TYPE"
    WRONG_SCHEMA = "WRONG_SCHEMA"
    WRONG_SCHEMA_VERSION = "WRONG_SCHEMA_VERSION"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    NOT_CORE_PRIME = "NOT_CORE_PRIME"
    DOMAIN_MISMATCH = "DOMAIN_MISMATCH"
    FACTORIZATION_MISMATCH = "FACTORIZATION_MISMATCH"
    AUTHORITY_BOUNDARY_VIOLATION = "AUTHORITY_BOUNDARY_VIOLATION"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"
    ID_MISMATCH = "ID_MISMATCH"
    DEPENDENCY_MISMATCH = "DEPENDENCY_MISMATCH"


class RootInitializerValidationError(ValueError):
    """Fail-closed error carrying a machine-readable rejection code."""

    def __init__(self, code: RootInitializerRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: RootInitializerRejectCode, detail: str) -> NoReturn:
    raise RootInitializerValidationError(code, detail)


def _plain_int(value: Any) -> bool:
    return type(value) is int


def _require_text(value: Any, name: str) -> str:
    if type(value) is not str or not value or value.strip() != value:
        _reject(
            RootInitializerRejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty trimmed exact string",
        )
    return value


def _require_digest(value: Any, name: str) -> str:
    if type(value) is not str or _DIGEST_RE.fullmatch(value) is None:
        _reject(
            RootInitializerRejectCode.MALFORMED_FIELD,
            f"{name} must be a lowercase SHA-256 digest",
        )
    return value


def _require_content_id(value: Any, name: str, prefix: str) -> str:
    text = _require_text(value, name)
    if not text.startswith(prefix) or _DIGEST_RE.fullmatch(text[len(prefix) :]) is None:
        _reject(
            RootInitializerRejectCode.MALFORMED_FIELD,
            f"{name} must be {prefix!r} followed by a SHA-256 digest",
        )
    return text


def _require_false(value: Any, name: str) -> None:
    if type(value) is not bool or value is not False:
        _reject(
            RootInitializerRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
            f"{name} must be exactly false",
        )


def _json_copy(value: Any, *, path: str = "$") -> Any:
    """Copy the strict JSON subset used by every content seal."""

    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str or not key:
                _reject(
                    RootInitializerRejectCode.MALFORMED_FIELD,
                    f"{path} keys must be nonempty exact strings",
                )
            result[key] = _json_copy(child, path=f"{path}.{key}")
        return result
    if type(value) in {list, tuple}:
        return [
            _json_copy(child, path=f"{path}[{index}]")
            for index, child in enumerate(value)
        ]
    if value is None or type(value) in {str, bool, int}:
        return value
    _reject(
        RootInitializerRejectCode.MALFORMED_FIELD,
        f"{path} contains unsupported type {type(value).__name__}",
    )


def canonical_json_v2(value: Any) -> str:
    """Return the unique ASCII JSON encoding used by this module."""

    try:
        return json.dumps(
            _json_copy(value),
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise RootInitializerValidationError(
            RootInitializerRejectCode.MALFORMED_FIELD,
            f"value is not canonical JSON: {exc}",
        ) from exc


def canonical_digest_v2(value: Any) -> str:
    return hashlib.sha256(canonical_json_v2(value).encode("ascii")).hexdigest()


INITIALIZER_CONTRACT_DIGEST = canonical_digest_v2(
    {
        "contract_id": INITIALIZER_ID,
        "schema_version": SCHEMA_VERSION,
        "raw_schema_id": RAW_SCHEMA_ID,
        "dependency_order": [
            "CanonicalQOneGSourceBodyV2",
            "RootInitializerAnchorV2",
            "RawRootSourceStateV2",
        ],
        "root_origin_kind": ROOT_ORIGIN_KIND,
        "domain_replay_id": DOMAIN_REPLAY_ID,
        "source_tree_scope": SOURCE_TREE_SCOPE,
        "evidence_class": EVIDENCE_CLASS,
        "initializer_authority": False,
        "admission_authority": False,
        "queue_authority": False,
    }
)


def loads_strict_v2(encoded: str) -> dict[str, Any]:
    """Load one exact JSON object, rejecting duplicates and non-integers."""

    if type(encoded) is not str:
        _reject(
            RootInitializerRejectCode.INPUT_NOT_EXACT_TYPE,
            "encoded JSON must be an exact string",
        )

    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                _reject(
                    RootInitializerRejectCode.FIELD_SET_MISMATCH,
                    f"duplicate JSON key {key!r}",
                )
            result[key] = value
        return result

    def reject_number(value: str) -> NoReturn:
        _reject(
            RootInitializerRejectCode.MALFORMED_FIELD,
            f"non-integer JSON number {value!r} is forbidden",
        )

    try:
        value = json.loads(
            encoded,
            object_pairs_hook=object_pairs,
            parse_float=reject_number,
            parse_constant=reject_number,
        )
    except RootInitializerValidationError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        raise RootInitializerValidationError(
            RootInitializerRejectCode.MALFORMED_FIELD,
            f"invalid JSON: {exc}",
        ) from exc
    if type(value) is not dict:
        _reject(
            RootInitializerRejectCode.INPUT_NOT_EXACT_MAPPING,
            "top-level JSON value must be an exact object",
        )
    return _json_copy(value)


class _FactoryOnlyV2:
    __slots__ = ()

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} must be created by its V2 factory")


@dataclass(frozen=True, init=False, slots=True)
class CanonicalQOneGSourceBodyV2(_FactoryOnlyV2):
    ARTIFACT_TYPE: ClassVar[str] = "CanonicalQOneGSourceBodyV2"
    ID_FIELD: ClassVar[str] = "body_id"
    ID_PREFIX: ClassVar[str] = BODY_ID_PREFIX

    root_context: int
    equation_rank: int
    equation_numerator: int
    equation_denominator: int
    q: int
    gap_three_x: int
    endpoint_fiber_code: int
    major_phase_code: int
    provenance_code: int
    mark_kind_code: int
    mark_root_context: int
    mark_equation_rank: int
    gap_three_factorization: tuple[tuple[int, int], ...]
    source_tree_scope: str
    evidence_class: str
    initializer_authority: bool
    admission_authority: bool
    queue_authority: bool
    body_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class RootInitializerAnchorV2(_FactoryOnlyV2):
    ARTIFACT_TYPE: ClassVar[str] = "RootInitializerAnchorV2"
    ID_FIELD: ClassVar[str] = "anchor_id"
    ID_PREFIX: ClassVar[str] = ANCHOR_ID_PREFIX

    body_id: str
    body_digest: str
    initializer_id: str
    contract_digest: str
    root_origin_kind: str
    domain_replay_id: str
    domain_replay_digest: str
    evidence_class: str
    initializer_authority: bool
    admission_authority: bool
    queue_authority: bool
    anchor_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class RootOriginAnchorRefV2(_FactoryOnlyV2):
    """The only root-origin metadata stored inside a raw root source state."""

    root_initializer_anchor_id: str
    digest: str


@dataclass(frozen=True, init=False, slots=True)
class RawRootSourceStateV2(_FactoryOnlyV2):
    ARTIFACT_TYPE: ClassVar[str] = "RawRootSourceStateV2"
    ID_FIELD: ClassVar[str] = "state_id"
    ID_PREFIX: ClassVar[str] = STATE_ID_PREFIX

    body_id: str
    body_digest: str
    root_context: int
    equation_rank: int
    equation_numerator: int
    equation_denominator: int
    q: int
    gap_three_x: int
    endpoint_fiber_code: int
    major_phase_code: int
    provenance_code: int
    mark_kind_code: int
    mark_root_context: int
    mark_equation_rank: int
    gap_three_factorization: tuple[tuple[int, int], ...]
    source_tree_scope: str
    root_origin: RootOriginAnchorRefV2
    evidence_class: str
    initializer_authority: bool
    admission_authority: bool
    queue_authority: bool
    state_id: str
    digest: str


ArtifactV2 = CanonicalQOneGSourceBodyV2 | RootInitializerAnchorV2 | RawRootSourceStateV2
ArtifactT = TypeVar("ArtifactT", bound=ArtifactV2)

_ARTIFACT_CLASSES = frozenset(
    {
        CanonicalQOneGSourceBodyV2,
        RootInitializerAnchorV2,
        RawRootSourceStateV2,
    }
)


def _is_prime_trial_v2(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    if value % 3 == 0:
        return value == 3
    divisor = 5
    step = 2
    limit = isqrt(value)
    while divisor <= limit:
        if value % divisor == 0:
            return False
        divisor += step
        step = 6 - step
    return True


def _factor_trial_v2(value: int) -> tuple[tuple[int, int], ...]:
    remainder = value
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor != 0:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while remainder % divisor == 0:
            remainder //= divisor
            exponent += 1
        factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        factors.append((remainder, 1))
    return tuple(factors)


def _require_exact_mapping(
    value: Any,
    expected_fields: frozenset[str],
    name: str,
) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(
            RootInitializerRejectCode.INPUT_NOT_EXACT_MAPPING,
            f"{name} must be an exact dict",
        )
    if any(type(key) is not str for key in value):
        _reject(
            RootInitializerRejectCode.MALFORMED_FIELD,
            f"{name} keys must be exact strings",
        )
    actual = frozenset(value)
    if actual != expected_fields:
        _reject(
            RootInitializerRejectCode.FIELD_SET_MISMATCH,
            f"{name} missing={sorted(expected_fields - actual)} "
            f"extra={sorted(actual - expected_fields)}",
        )
    return value


def _parse_wire_factorization_v2(
    value: Any,
    *,
    name: str,
) -> tuple[tuple[int, int], ...]:
    if type(value) is not list or not value:
        _reject(
            RootInitializerRejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty exact JSON array",
        )
    factors: list[tuple[int, int]] = []
    previous = 1
    for index, pair in enumerate(value):
        if type(pair) is not list or len(pair) != 2:
            _reject(
                RootInitializerRejectCode.MALFORMED_FIELD,
                f"{name}[{index}] must be an exact [prime, exponent] array",
            )
        prime, exponent = pair
        if (
            not _plain_int(prime)
            or not _plain_int(exponent)
            or prime <= previous
            or exponent <= 0
            or not _is_prime_trial_v2(prime)
        ):
            _reject(
                RootInitializerRejectCode.FACTORIZATION_MISMATCH,
                f"{name}[{index}] is not a strictly ordered prime power",
            )
        factors.append((prime, exponent))
        previous = prime
    return tuple(factors)


def _validate_raw_v2(value: Any) -> dict[str, Any]:
    raw = _require_exact_mapping(value, RAW_FIELDS, "raw q=1 G source")
    if type(raw["schema_id"]) is not str or raw["schema_id"] != RAW_SCHEMA_ID:
        _reject(
            RootInitializerRejectCode.WRONG_SCHEMA,
            f"schema_id must be {RAW_SCHEMA_ID!r}",
        )
    if (
        not _plain_int(raw["schema_version"])
        or raw["schema_version"] != RAW_SCHEMA_VERSION
    ):
        _reject(
            RootInitializerRejectCode.WRONG_SCHEMA_VERSION,
            "schema_version must be the plain integer 2",
        )
    for name in RAW_FIELDS - {"schema_id", "gap_three_factorization"}:
        if not _plain_int(raw[name]):
            _reject(
                RootInitializerRejectCode.MALFORMED_FIELD,
                f"raw.{name} must be a plain integer, not bool or float",
            )

    p = raw["root_context"]
    if not (_is_prime_trial_v2(p) and p % 24 == 1):
        _reject(
            RootInitializerRejectCode.NOT_CORE_PRIME,
            "root_context must be a trial-verified prime congruent to 1 modulo 24",
        )
    x = (p + 3) // 4
    if not (
        raw["equation_rank"] == p
        and raw["equation_numerator"] == 4
        and raw["equation_denominator"] == p
        and raw["q"] == 1
        and raw["gap_three_x"] == x
        and raw["endpoint_fiber_code"] == ENDPOINT_G
        and raw["major_phase_code"] == PHASE_TYPEII_G_HANDOFF
        and raw["provenance_code"] == PROVENANCE_ORDINARY_ENDPOINT
        and raw["mark_kind_code"] == MARK_ROOT_SOL
        and raw["mark_root_context"] == p
        and raw["mark_equation_rank"] == p
    ):
        _reject(
            RootInitializerRejectCode.DOMAIN_MISMATCH,
            "equation, q=1 G, phase, provenance, or ROOT_SOL coordinates mismatch",
        )

    declared = _parse_wire_factorization_v2(
        raw["gap_three_factorization"],
        name="gap_three_factorization",
    )
    actual = _factor_trial_v2(x)
    if declared != actual:
        _reject(
            RootInitializerRejectCode.FACTORIZATION_MISMATCH,
            "gap_three_factorization is not the complete trial factorization of X",
        )
    if any(prime % 3 != 1 for prime, _exponent in actual):
        _reject(
            RootInitializerRejectCode.DOMAIN_MISMATCH,
            "ordinary q=1 G requires every prime factor of X to be 1 modulo 3",
        )
    result = dict(raw)
    result["gap_three_factorization"] = actual
    return result


def _semantic_raw_from_artifact(artifact: Any) -> dict[str, Any]:
    result: dict[str, Any] = {
        "schema_id": RAW_SCHEMA_ID,
        "schema_version": RAW_SCHEMA_VERSION,
    }
    for name in SEMANTIC_FIELD_NAMES:
        value = getattr(artifact, name)
        if name == "gap_three_factorization":
            value = [list(pair) for pair in value]
        result[name] = value
    return result


def _validate_evidence_boundary_v2(artifact: Any) -> None:
    if type(artifact.source_tree_scope) is not str or artifact.source_tree_scope != SOURCE_TREE_SCOPE:
        _reject(
            RootInitializerRejectCode.DOMAIN_MISMATCH,
            f"source_tree_scope must be {SOURCE_TREE_SCOPE!r}",
        )
    if type(artifact.evidence_class) is not str or artifact.evidence_class != EVIDENCE_CLASS:
        _reject(
            RootInitializerRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
            f"evidence_class must be {EVIDENCE_CLASS!r}",
        )
    for name in AUTHORITY_FIELD_NAMES:
        _require_false(getattr(artifact, name), name)


def _validate_factor_tuple_v2(value: Any, name: str) -> None:
    if type(value) is not tuple or not value:
        _reject(
            RootInitializerRejectCode.MALFORMED_FIELD,
            f"{name} must be a nonempty exact tuple",
        )
    for index, pair in enumerate(value):
        if (
            type(pair) is not tuple
            or len(pair) != 2
            or not _plain_int(pair[0])
            or not _plain_int(pair[1])
        ):
            _reject(
                RootInitializerRejectCode.MALFORMED_FIELD,
                f"{name}[{index}] is not an exact integer pair",
            )


def _validate_body_fields_v2(body: CanonicalQOneGSourceBodyV2) -> None:
    _validate_factor_tuple_v2(body.gap_three_factorization, "body factorization")
    _validate_raw_v2(_semantic_raw_from_artifact(body))
    _validate_evidence_boundary_v2(body)
    _require_content_id(body.body_id, "body_id", BODY_ID_PREFIX)
    _require_digest(body.digest, "body.digest")


def _validate_anchor_fields_v2(anchor: RootInitializerAnchorV2) -> None:
    _require_content_id(anchor.body_id, "anchor.body_id", BODY_ID_PREFIX)
    _require_digest(anchor.body_digest, "anchor.body_digest")
    if anchor.body_id != BODY_ID_PREFIX + anchor.body_digest:
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "anchor body ID and digest do not identify the same body",
        )
    if type(anchor.initializer_id) is not str or anchor.initializer_id != INITIALIZER_ID:
        _reject(
            RootInitializerRejectCode.DOMAIN_MISMATCH,
            f"initializer_id must be {INITIALIZER_ID!r}",
        )
    if (
        type(anchor.contract_digest) is not str
        or anchor.contract_digest != INITIALIZER_CONTRACT_DIGEST
    ):
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "anchor contract_digest differs from the fixed structural contract",
        )
    if (
        type(anchor.root_origin_kind) is not str
        or anchor.root_origin_kind != ROOT_ORIGIN_KIND
    ):
        _reject(
            RootInitializerRejectCode.DOMAIN_MISMATCH,
            f"root_origin_kind must be {ROOT_ORIGIN_KIND!r}",
        )
    if (
        type(anchor.domain_replay_id) is not str
        or anchor.domain_replay_id != DOMAIN_REPLAY_ID
    ):
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "anchor domain_replay_id differs from the fixed raw-integer replay",
        )
    expected_domain_digest = _domain_replay_digest_v2(
        anchor.body_id,
        anchor.body_digest,
    )
    if (
        type(anchor.domain_replay_digest) is not str
        or anchor.domain_replay_digest != expected_domain_digest
    ):
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "anchor domain_replay_digest does not replay from its body reference",
        )
    if type(anchor.evidence_class) is not str or anchor.evidence_class != EVIDENCE_CLASS:
        _reject(
            RootInitializerRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
            f"anchor evidence_class must be {EVIDENCE_CLASS!r}",
        )
    for name in AUTHORITY_FIELD_NAMES:
        _require_false(getattr(anchor, name), f"anchor.{name}")
    _require_content_id(anchor.anchor_id, "anchor_id", ANCHOR_ID_PREFIX)
    _require_digest(anchor.digest, "anchor.digest")


def _validate_origin_ref_v2(ref: RootOriginAnchorRefV2) -> None:
    if type(ref) is not RootOriginAnchorRefV2:
        _reject(
            RootInitializerRejectCode.INPUT_NOT_EXACT_TYPE,
            "root_origin must be an exact RootOriginAnchorRefV2",
        )
    for field in fields(RootOriginAnchorRefV2):
        try:
            getattr(ref, field.name)
        except AttributeError as exc:
            raise RootInitializerValidationError(
                RootInitializerRejectCode.MALFORMED_FIELD,
                f"root_origin.{field.name} is missing",
            ) from exc
    _require_content_id(
        ref.root_initializer_anchor_id,
        "root_origin.root_initializer_anchor_id",
        ANCHOR_ID_PREFIX,
    )
    _require_digest(ref.digest, "root_origin.digest")
    if ref.root_initializer_anchor_id != ANCHOR_ID_PREFIX + ref.digest:
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "root_origin anchor ID and digest disagree",
        )


def _body_values_from_semantic_artifact(artifact: Any) -> dict[str, Any]:
    values = {name: getattr(artifact, name) for name in SEMANTIC_FIELD_NAMES}
    values.update(
        {
            "source_tree_scope": artifact.source_tree_scope,
            "evidence_class": artifact.evidence_class,
            "initializer_authority": artifact.initializer_authority,
            "admission_authority": artifact.admission_authority,
            "queue_authority": artifact.queue_authority,
        }
    )
    return values


def _domain_replay_digest_v2(body_id: str, body_digest: str) -> str:
    return canonical_digest_v2(
        {
            "domain_replay_id": DOMAIN_REPLAY_ID,
            "source_body_id": body_id,
            "source_body_digest": body_digest,
            "result": "ORDINARY_Q_ONE_G_RAW_INTEGER_REPLAY",
            "initializer_authority": False,
            "admission_authority": False,
            "queue_authority": False,
        }
    )


def _validate_state_fields_v2(state: RawRootSourceStateV2) -> None:
    _require_content_id(state.body_id, "state.body_id", BODY_ID_PREFIX)
    _require_digest(state.body_digest, "state.body_digest")
    _validate_factor_tuple_v2(state.gap_three_factorization, "state factorization")
    _validate_raw_v2(_semantic_raw_from_artifact(state))
    _validate_evidence_boundary_v2(state)
    _validate_origin_ref_v2(state.root_origin)

    body_unsigned = _unsigned_mapping_v2(
        CanonicalQOneGSourceBodyV2,
        _body_values_from_semantic_artifact(state),
    )
    expected_body_digest = canonical_digest_v2(body_unsigned)
    if (
        state.body_digest != expected_body_digest
        or state.body_id != BODY_ID_PREFIX + expected_body_digest
    ):
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "state repeated semantics do not replay its body reference",
        )
    _require_content_id(state.state_id, "state_id", STATE_ID_PREFIX)
    _require_digest(state.digest, "state.digest")


def _validate_artifact_fields_v2(artifact: ArtifactV2) -> None:
    cls = type(artifact)
    if cls not in _ARTIFACT_CLASSES:
        _reject(
            RootInitializerRejectCode.INPUT_NOT_EXACT_TYPE,
            "artifact must have an exact V2 envelope class",
        )
    for field in fields(cls):
        try:
            getattr(artifact, field.name)
        except AttributeError as exc:
            raise RootInitializerValidationError(
                RootInitializerRejectCode.MALFORMED_FIELD,
                f"{cls.ARTIFACT_TYPE}.{field.name} is missing",
            ) from exc
    if cls is CanonicalQOneGSourceBodyV2:
        _validate_body_fields_v2(artifact)
    elif cls is RootInitializerAnchorV2:
        _validate_anchor_fields_v2(artifact)
    else:
        _validate_state_fields_v2(artifact)


def _origin_ref_mapping_v2(ref: RootOriginAnchorRefV2) -> dict[str, str]:
    _validate_origin_ref_v2(ref)
    return {
        "root_initializer_anchor_id": ref.root_initializer_anchor_id,
        "digest": ref.digest,
    }


def _external_value_v2(value: Any) -> Any:
    if isinstance(value, RootOriginAnchorRefV2):
        if type(value) is not RootOriginAnchorRefV2:
            _reject(
                RootInitializerRejectCode.INPUT_NOT_EXACT_TYPE,
                "root origin subclasses are forbidden",
            )
        return _origin_ref_mapping_v2(value)
    return _json_copy(value)


def _unsigned_mapping_v2(
    cls: type[ArtifactT],
    values: Mapping[str, Any],
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "artifact_type": cls.ARTIFACT_TYPE,
        "schema_version": SCHEMA_VERSION,
    }
    for field in fields(cls):
        if field.name in {cls.ID_FIELD, "digest"}:
            continue
        try:
            value = values[field.name]
        except KeyError as exc:
            raise RootInitializerValidationError(
                RootInitializerRejectCode.MALFORMED_FIELD,
                f"missing value for {cls.ARTIFACT_TYPE}.{field.name}",
            ) from exc
        payload[field.name] = _external_value_v2(value)
    return payload


def _construct_v2(cls: type[ArtifactT], values: Mapping[str, Any]) -> ArtifactT:
    instance = object.__new__(cls)
    for field in fields(cls):
        try:
            value = values[field.name]
        except KeyError as exc:
            raise RootInitializerValidationError(
                RootInitializerRejectCode.MALFORMED_FIELD,
                f"missing construction field {cls.ARTIFACT_TYPE}.{field.name}",
            ) from exc
        object.__setattr__(instance, field.name, value)
    return instance


def _seal_v2(cls: type[ArtifactT], values: Mapping[str, Any]) -> ArtifactT:
    mutable = dict(values)
    digest = canonical_digest_v2(_unsigned_mapping_v2(cls, mutable))
    mutable[cls.ID_FIELD] = cls.ID_PREFIX + digest
    mutable["digest"] = digest
    artifact = _construct_v2(cls, mutable)
    _verify_content_seal_v2(artifact)
    return artifact


def _verify_content_seal_v2(artifact: ArtifactV2) -> None:
    _validate_artifact_fields_v2(artifact)
    cls = type(artifact)
    values = {field.name: getattr(artifact, field.name) for field in fields(cls)}
    expected_digest = canonical_digest_v2(_unsigned_mapping_v2(cls, values))
    if artifact.digest != expected_digest:
        _reject(
            RootInitializerRejectCode.DIGEST_MISMATCH,
            f"{cls.ARTIFACT_TYPE}.digest does not replay",
        )
    expected_id = cls.ID_PREFIX + expected_digest
    if getattr(artifact, cls.ID_FIELD) != expected_id:
        _reject(
            RootInitializerRejectCode.ID_MISMATCH,
            f"{cls.ARTIFACT_TYPE}.{cls.ID_FIELD} does not replay",
        )


def artifact_to_mapping_v2(artifact: ArtifactV2) -> dict[str, Any]:
    """Serialize an exact artifact after complete local invariant replay."""

    if type(artifact) not in _ARTIFACT_CLASSES:
        _reject(
            RootInitializerRejectCode.INPUT_NOT_EXACT_TYPE,
            "artifact_to_mapping_v2 accepts only exact V2 envelope artifacts",
        )
    _verify_content_seal_v2(artifact)
    cls = type(artifact)
    values = {field.name: getattr(artifact, field.name) for field in fields(cls)}
    result = _unsigned_mapping_v2(cls, values)
    result[cls.ID_FIELD] = getattr(artifact, cls.ID_FIELD)
    result["digest"] = artifact.digest
    return result


def _expected_mapping_fields_v2(cls: type[ArtifactT]) -> frozenset[str]:
    return frozenset(
        {
            "artifact_type",
            "schema_version",
            *(field.name for field in fields(cls)),
        }
    )


def _parse_origin_ref_mapping_v2(value: Any) -> RootOriginAnchorRefV2:
    expected = frozenset({"root_initializer_anchor_id", "digest"})
    stored = _require_exact_mapping(value, expected, "root_origin")
    ref = object.__new__(RootOriginAnchorRefV2)
    object.__setattr__(
        ref,
        "root_initializer_anchor_id",
        stored["root_initializer_anchor_id"],
    )
    object.__setattr__(ref, "digest", stored["digest"])
    _validate_origin_ref_v2(ref)
    return ref


def _stored_artifact_v2(value: Any, cls: type[ArtifactT]) -> ArtifactT:
    if type(value) is cls:
        _verify_content_seal_v2(value)
        return value
    if is_dataclass(value):
        _reject(
            RootInitializerRejectCode.INPUT_NOT_EXACT_TYPE,
            f"expected exact {cls.__name__}, got {type(value).__name__}",
        )
    stored = _require_exact_mapping(
        value,
        _expected_mapping_fields_v2(cls),
        cls.ARTIFACT_TYPE,
    )
    if (
        type(stored["artifact_type"]) is not str
        or stored["artifact_type"] != cls.ARTIFACT_TYPE
    ):
        _reject(
            RootInitializerRejectCode.WRONG_ARTIFACT_TYPE,
            f"expected artifact_type={cls.ARTIFACT_TYPE!r}",
        )
    if (
        not _plain_int(stored["schema_version"])
        or stored["schema_version"] != SCHEMA_VERSION
    ):
        _reject(
            RootInitializerRejectCode.WRONG_SCHEMA_VERSION,
            "artifact schema_version must be the plain integer 2",
        )

    values = {field.name: stored[field.name] for field in fields(cls)}
    if cls in {CanonicalQOneGSourceBodyV2, RawRootSourceStateV2}:
        values["gap_three_factorization"] = _parse_wire_factorization_v2(
            values["gap_three_factorization"],
            name=f"{cls.ARTIFACT_TYPE}.gap_three_factorization",
        )
    if cls is RawRootSourceStateV2:
        values["root_origin"] = _parse_origin_ref_mapping_v2(values["root_origin"])
    artifact = _construct_v2(cls, values)
    _verify_content_seal_v2(artifact)
    return artifact


def _require_upstream_v2(value: Any, cls: type[ArtifactT], name: str) -> ArtifactT:
    if type(value) is not cls:
        _reject(
            RootInitializerRejectCode.INPUT_NOT_EXACT_TYPE,
            f"{name} must be an exact factory-sealed {cls.__name__}",
        )
    _verify_content_seal_v2(value)
    return value


def make_canonical_q_one_g_source_body_v2(
    raw: dict[str, Any],
) -> CanonicalQOneGSourceBodyV2:
    """Replay raw integers and seal the canonical ordinary q=1 G source body."""

    validated = _validate_raw_v2(raw)
    values = {name: validated[name] for name in SEMANTIC_FIELD_NAMES}
    values.update(
        {
            "source_tree_scope": SOURCE_TREE_SCOPE,
            "evidence_class": EVIDENCE_CLASS,
            "initializer_authority": False,
            "admission_authority": False,
            "queue_authority": False,
        }
    )
    return _seal_v2(CanonicalQOneGSourceBodyV2, values)


def parse_canonical_q_one_g_source_body_v2(
    value: Any,
    raw: dict[str, Any],
) -> CanonicalQOneGSourceBodyV2:
    """Parse a body only by rebuilding it from the explicit raw dependency."""

    stored = _stored_artifact_v2(value, CanonicalQOneGSourceBodyV2)
    rebuilt = make_canonical_q_one_g_source_body_v2(raw)
    if artifact_to_mapping_v2(stored) != artifact_to_mapping_v2(rebuilt):
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "stored source body differs from the explicit raw q=1 G input",
        )
    return rebuilt


def make_root_initializer_anchor_v2(
    body: CanonicalQOneGSourceBodyV2,
) -> RootInitializerAnchorV2:
    """Seal the last root-initializer object before a source state ID exists."""

    body = _require_upstream_v2(
        body,
        CanonicalQOneGSourceBodyV2,
        "body",
    )
    return _seal_v2(
        RootInitializerAnchorV2,
        {
            "body_id": body.body_id,
            "body_digest": body.digest,
            "initializer_id": INITIALIZER_ID,
            "contract_digest": INITIALIZER_CONTRACT_DIGEST,
            "root_origin_kind": ROOT_ORIGIN_KIND,
            "domain_replay_id": DOMAIN_REPLAY_ID,
            "domain_replay_digest": _domain_replay_digest_v2(
                body.body_id,
                body.digest,
            ),
            "evidence_class": EVIDENCE_CLASS,
            "initializer_authority": False,
            "admission_authority": False,
            "queue_authority": False,
        },
    )


def parse_root_initializer_anchor_v2(
    value: Any,
    body: CanonicalQOneGSourceBodyV2,
) -> RootInitializerAnchorV2:
    """Parse an anchor by rebuilding it against the explicit source body."""

    body = _require_upstream_v2(
        body,
        CanonicalQOneGSourceBodyV2,
        "body",
    )
    stored = _stored_artifact_v2(value, RootInitializerAnchorV2)
    rebuilt = make_root_initializer_anchor_v2(body)
    if artifact_to_mapping_v2(stored) != artifact_to_mapping_v2(rebuilt):
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "stored root initializer anchor belongs to another body or contract",
        )
    return rebuilt


def make_root_origin_anchor_ref_v2(
    anchor: RootInitializerAnchorV2,
) -> RootOriginAnchorRefV2:
    """Create the exact two-field origin reference stored by the root state."""

    anchor = _require_upstream_v2(anchor, RootInitializerAnchorV2, "anchor")
    ref = object.__new__(RootOriginAnchorRefV2)
    object.__setattr__(ref, "root_initializer_anchor_id", anchor.anchor_id)
    object.__setattr__(ref, "digest", anchor.digest)
    _validate_origin_ref_v2(ref)
    return ref


def parse_root_origin_anchor_ref_v2(
    value: Any,
    anchor: RootInitializerAnchorV2,
) -> RootOriginAnchorRefV2:
    """Parse an origin reference only against an explicit anchor."""

    anchor = _require_upstream_v2(anchor, RootInitializerAnchorV2, "anchor")
    if type(value) is RootOriginAnchorRefV2:
        _validate_origin_ref_v2(value)
        stored = _origin_ref_mapping_v2(value)
    else:
        stored = _origin_ref_mapping_v2(_parse_origin_ref_mapping_v2(value))
    expected = make_root_origin_anchor_ref_v2(anchor)
    if stored != _origin_ref_mapping_v2(expected):
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "root origin reference points to another initializer anchor",
        )
    return expected


def make_raw_root_source_state_v2(
    body: CanonicalQOneGSourceBodyV2,
    anchor: RootInitializerAnchorV2,
) -> RawRootSourceStateV2:
    """Create a content-addressed SOURCE_STATE with only root-origin metadata."""

    body = _require_upstream_v2(
        body,
        CanonicalQOneGSourceBodyV2,
        "body",
    )
    anchor = _require_upstream_v2(anchor, RootInitializerAnchorV2, "anchor")
    if anchor.body_id != body.body_id or anchor.body_digest != body.digest:
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "initializer anchor belongs to another canonical source body",
        )
    values: dict[str, Any] = {
        "body_id": body.body_id,
        "body_digest": body.digest,
        **{name: getattr(body, name) for name in SEMANTIC_FIELD_NAMES},
        "source_tree_scope": body.source_tree_scope,
        "root_origin": make_root_origin_anchor_ref_v2(anchor),
        "evidence_class": EVIDENCE_CLASS,
        "initializer_authority": False,
        "admission_authority": False,
        "queue_authority": False,
    }
    return _seal_v2(RawRootSourceStateV2, values)


def parse_raw_root_source_state_v2(
    value: Any,
    body: CanonicalQOneGSourceBodyV2,
    anchor: RootInitializerAnchorV2,
) -> RawRootSourceStateV2:
    """Parse a state by rebuilding it against both explicit upstream objects."""

    body = _require_upstream_v2(
        body,
        CanonicalQOneGSourceBodyV2,
        "body",
    )
    anchor = _require_upstream_v2(anchor, RootInitializerAnchorV2, "anchor")
    stored = _stored_artifact_v2(value, RawRootSourceStateV2)
    parse_root_origin_anchor_ref_v2(stored.root_origin, anchor)
    rebuilt = make_raw_root_source_state_v2(body, anchor)
    if artifact_to_mapping_v2(stored) != artifact_to_mapping_v2(rebuilt):
        _reject(
            RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            "stored root source state differs from its explicit body or anchor",
        )
    return rebuilt


__all__ = [
    "ANCHOR_ID_PREFIX",
    "BODY_ID_PREFIX",
    "CanonicalQOneGSourceBodyV2",
    "DOMAIN_REPLAY_ID",
    "EVIDENCE_CLASS",
    "INITIALIZER_CONTRACT_DIGEST",
    "INITIALIZER_ID",
    "RAW_SCHEMA_ID",
    "RAW_SCHEMA_VERSION",
    "ROOT_ORIGIN_KIND",
    "RawRootSourceStateV2",
    "RootInitializerAnchorV2",
    "RootInitializerRejectCode",
    "RootInitializerValidationError",
    "RootOriginAnchorRefV2",
    "SCHEMA_VERSION",
    "SOURCE_TREE_SCOPE",
    "STATE_ID_PREFIX",
    "artifact_to_mapping_v2",
    "canonical_digest_v2",
    "canonical_json_v2",
    "loads_strict_v2",
    "make_canonical_q_one_g_source_body_v2",
    "make_raw_root_source_state_v2",
    "make_root_initializer_anchor_v2",
    "make_root_origin_anchor_ref_v2",
    "parse_canonical_q_one_g_source_body_v2",
    "parse_raw_root_source_state_v2",
    "parse_root_initializer_anchor_v2",
    "parse_root_origin_anchor_ref_v2",
]
