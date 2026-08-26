#!/usr/bin/env python3
"""Independent, non-authorizing q=1 G phase-root mathematics replay.

The replay consumes three exact serialized integer records: an ordinary q=1
G source, a proposed full-carrier root candidate, and its proposed canonical
Type-I projection.  It independently recomputes the arithmetic from those raw
integers.  In particular, this module imports no T6 runtime, producer,
projector, validator, scheduler, or historical reproduction module.

Passing this replay produces evidence only.  It does not establish occurrence
of the source in a runtime, terminal-first completeness, role separation,
transition admission, queue eligibility, or T6 totality.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, fields, is_dataclass
from enum import Enum
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path
from typing import Any, Mapping, NoReturn


SCHEMA_ID = "t6_q_one_phase_root_independent_math_replay_v1"
SCHEMA_VERSION = 1
REPLAY_STATUS = "EVIDENCE_ONLY_MATH_REPLAY"
BLOCKED = "BLOCKED"

MARK_ROOT_SOL = 1
ENDPOINT_G = 2
PROVENANCE_ORDINARY_ENDPOINT = 1
PROVENANCE_FULL_CARRIER_POST_G = 2
PHASE_TYPEII_G_HANDOFF = 3
PHASE_TYPEI = 2
PROTOCOL_NONE = 0
PROTOCOL_CHARGED = 4
OWNER_TYPEII_G_ENDPOINT = 1
OWNER_TYPEI_FULL_CARRIER_POST_G = 2
TICKET_PHASE_DROP = 2

SCOPE_EXCLUSIONS = (
    "actual runtime occurrence and terminal-first completeness",
    "producer, projector, validator, scheduler, or T5-ticket authority",
    "complete terminal schedules, Gate 2, and T6 totality",
    "post-root Type-I selector totality and the Erdos-Straus conjecture",
)

SOURCE_FIELDS = frozenset(
    {
        "schema_version",
        "root_context",
        "equation_rank",
        "equation_numerator",
        "equation_denominator",
        "q",
        "gap",
        "u",
        "x",
        "endpoint_fiber_code",
        "major_phase_code",
        "provenance_code",
        "mark_kind_code",
        "mark_root_context",
        "mark_equation_rank",
        "declared_branch_type_code",
        "factorization",
    }
)
CANDIDATE_FIELDS = frozenset(
    {
        "schema_version",
        "root_context",
        "t",
        "x",
        "chart_r",
        "chart_k",
        "support_a",
        "source_u",
        "source_v",
        "source_m",
        "edge_prime",
        "edge_shift",
        "gcd_reduction",
        "anchor_u",
        "anchor_v",
        "anchor_m",
    }
)
PROJECTION_FIELDS = frozenset(
    {
        "schema_version",
        "root_context",
        "equation_rank",
        "equation_numerator",
        "equation_denominator",
        "mark_kind_code",
        "mark_root_context",
        "mark_equation_rank",
        "major_phase_code",
        "type_i_protocol_code",
        "provenance_code",
        "full_carrier_scope_code",
        "support_a",
        "chart_r",
        "chart_k",
        "declared_branch_type_code",
        "ticket_code",
        "source_t5_coordinates",
        "target_t5_coordinates",
    }
)
BUNDLE_FIELDS = frozenset({"source", "candidate", "projection"})


class MathReplayRejectCode(str, Enum):
    INPUT_NOT_OBJECT = "INPUT_NOT_OBJECT"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    WRONG_SCHEMA_VERSION = "WRONG_SCHEMA_VERSION"
    MALFORMED_INTEGER = "MALFORMED_INTEGER"
    CROSS_ARTIFACT_MISMATCH = "CROSS_ARTIFACT_MISMATCH"
    NOT_CORE_PRIME = "NOT_CORE_PRIME"
    NOT_Q_ONE_G = "NOT_Q_ONE_G"
    ROOT_FORMULA_MISMATCH = "ROOT_FORMULA_MISMATCH"
    CHART_IDENTITY_MISMATCH = "CHART_IDENTITY_MISMATCH"
    LOW_CHART_UNIQUENESS_MISMATCH = "LOW_CHART_UNIQUENESS_MISMATCH"
    FRESH_SOURCE_MISMATCH = "FRESH_SOURCE_MISMATCH"
    PROJECTION_MISMATCH = "PROJECTION_MISMATCH"
    MARK_MISMATCH = "MARK_MISMATCH"
    OWNER_MISMATCH = "OWNER_MISMATCH"
    POTENTIAL_MISMATCH = "POTENTIAL_MISMATCH"
    MALFORMED_RECEIPT = "MALFORMED_RECEIPT"
    AUTHORITY_BOUNDARY_VIOLATION = "AUTHORITY_BOUNDARY_VIOLATION"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"


class MathReplayError(ValueError):
    """Fail-closed replay error with a stable code."""

    def __init__(self, code: MathReplayRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


@dataclass(frozen=True, slots=True)
class CoreGReplayV1:
    prime: int
    t: int
    u: int
    x: int
    factorization: tuple[tuple[int, int], ...]
    source_phase: str
    expected_branch_source_type: str


@dataclass(frozen=True, slots=True)
class FullCarrierRootReplayV1:
    x: int
    chart_r: int
    chart_k: int
    support_a: int
    low_r_min: int
    low_r_max: int
    congruence_modulus: int
    previous_congruent_r: int
    next_congruent_r: int


@dataclass(frozen=True, slots=True)
class FreshSourceReplayV1:
    source: tuple[int, int, int]
    edge_prime: int
    edge_shift: int
    gcd_reduction: int
    destination: tuple[int, int, int]


@dataclass(frozen=True, slots=True)
class CanonicalProjectionReplayV1:
    equation_target: tuple[int, int]
    equation_rank: int
    target_phase: str
    target_protocol: str
    target_provenance: str
    target_scope: str
    target_chart: tuple[int, int]
    target_support: int
    expected_branch_target_type: str


@dataclass(frozen=True, slots=True)
class IdentityLiftReplayV1:
    domain: str
    codomain: str
    rule: str
    mark_kind: str
    nonemptiness_claimed: bool
    terminal_membership_claimed: bool


@dataclass(frozen=True, slots=True)
class T5PhaseDropReplayV1:
    source_coordinates: tuple[int, int, int, int, int, int, int]
    target_coordinates: tuple[int, int, int, int, int, int, int]
    ticket: str
    first_strict_coordinate: str
    strict_lexicographic_drop: bool
    admission_ticket_issued: bool


@dataclass(frozen=True, slots=True)
class QOnePhaseRootMathReplayV1:
    schema_id: str
    schema_version: int
    status: str
    source_input_digest: str
    candidate_input_digest: str
    projection_input_digest: str
    core_g: CoreGReplayV1
    full_carrier_root: FullCarrierRootReplayV1
    fresh_source: FreshSourceReplayV1
    canonical_projection: CanonicalProjectionReplayV1
    identity_lift: IdentityLiftReplayV1
    t5_phase_drop: T5PhaseDropReplayV1
    terminal_authority: str
    role_authority: str
    issuance_allowed: bool
    scope_exclusions: tuple[str, ...]
    digest: str


def _reject(code: MathReplayRejectCode, detail: str) -> NoReturn:
    raise MathReplayError(code, detail)


def _plain_int(value: Any) -> bool:
    return type(value) is int


def _require_object(
    value: Any,
    expected: frozenset[str],
    name: str,
    *,
    require_schema_version: bool = True,
) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(MathReplayRejectCode.INPUT_NOT_OBJECT, f"{name} must be an exact object")
    if any(type(key) is not str for key in value):
        _reject(
            MathReplayRejectCode.FIELD_SET_MISMATCH,
            f"{name} keys must be exact strings",
        )
    missing = expected - set(value)
    extra = set(value) - expected
    if missing or extra:
        _reject(
            MathReplayRejectCode.FIELD_SET_MISMATCH,
            f"{name} missing={sorted(missing)} extra={sorted(extra)}",
        )
    result = dict(value)
    if not require_schema_version:
        return result
    if not _plain_int(result["schema_version"]):
        _reject(
            MathReplayRejectCode.WRONG_SCHEMA_VERSION,
            f"{name}.schema_version must be a plain integer",
        )
    if result["schema_version"] != SCHEMA_VERSION:
        _reject(
            MathReplayRejectCode.WRONG_SCHEMA_VERSION,
            f"{name}.schema_version={result['schema_version']!r}",
        )
    return result


def _require_integer_fields(
    value: Mapping[str, Any], names: frozenset[str], record_name: str
) -> None:
    for name in names:
        if not _plain_int(value[name]):
            _reject(
                MathReplayRejectCode.MALFORMED_INTEGER,
                f"{record_name}.{name} must be a plain integer",
            )


def _is_prime_exact(value: int) -> bool:
    """Return exact primality by trial division, with no probable-prime step."""

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


def _factorization_v1(value: Any) -> tuple[tuple[int, int], ...]:
    if type(value) is not list or not value:
        _reject(
            MathReplayRejectCode.NOT_Q_ONE_G,
            "source.factorization must be a nonempty serialized list",
        )
    result: list[tuple[int, int]] = []
    previous = 1
    for index, pair in enumerate(value):
        if type(pair) is not list or len(pair) != 2:
            _reject(
                MathReplayRejectCode.NOT_Q_ONE_G,
                f"source.factorization[{index}] must be [prime, exponent]",
            )
        prime, exponent = pair
        if not (_plain_int(prime) and _plain_int(exponent)):
            _reject(
                MathReplayRejectCode.MALFORMED_INTEGER,
                f"source.factorization[{index}] must contain plain integers",
            )
        if prime <= previous or exponent <= 0 or not _is_prime_exact(prime):
            _reject(
                MathReplayRejectCode.NOT_Q_ONE_G,
                "factorization must list increasing primes with positive exponents",
            )
        result.append((prime, exponent))
        previous = prime
    return tuple(result)


def _potential_v1(value: Any, name: str) -> tuple[int, int, int, int, int, int, int]:
    if type(value) is not list or len(value) != 7:
        _reject(
            MathReplayRejectCode.POTENTIAL_MISMATCH,
            f"{name} must be a serialized length-seven list",
        )
    if any(not _plain_int(item) or item < 0 for item in value):
        _reject(
            MathReplayRejectCode.POTENTIAL_MISMATCH,
            f"{name} must lie in N^7 and contain no booleans",
        )
    return tuple(value)  # type: ignore[return-value]


def _jsonable(value: Any) -> Any:
    if is_dataclass(value) and not isinstance(value, type):
        return {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, tuple):
        return [_jsonable(item) for item in value]
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    if isinstance(value, Mapping):
        return {str(key): _jsonable(child) for key, child in value.items()}
    return value


def canonical_json_v1(value: Any) -> str:
    try:
        return json.dumps(
            _jsonable(value),
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        _reject(MathReplayRejectCode.MALFORMED_INTEGER, f"noncanonical value: {exc}")


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


def loads_strict_v1(encoded: str) -> Any:
    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                _reject(
                    MathReplayRejectCode.FIELD_SET_MISMATCH,
                    f"duplicate JSON key {key!r}",
                )
            result[key] = value
        return result

    try:
        return json.loads(
            encoded,
            object_pairs_hook=object_pairs,
            parse_float=lambda value: _reject(
                MathReplayRejectCode.MALFORMED_INTEGER,
                f"floating-point number {value!r} is forbidden",
            ),
            parse_constant=lambda value: _reject(
                MathReplayRejectCode.MALFORMED_INTEGER,
                f"non-finite number {value!r} is forbidden",
            ),
        )
    except MathReplayError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        _reject(MathReplayRejectCode.INPUT_NOT_OBJECT, f"invalid JSON: {exc}")


def replay_q_one_phase_root_math_v1(
    source_value: Mapping[str, Any],
    candidate_value: Mapping[str, Any],
    projection_value: Mapping[str, Any],
) -> QOnePhaseRootMathReplayV1:
    """Replay the q=1 G phase-root mathematics without granting authority."""

    source = _require_object(source_value, SOURCE_FIELDS, "source")
    candidate = _require_object(candidate_value, CANDIDATE_FIELDS, "candidate")
    projection = _require_object(projection_value, PROJECTION_FIELDS, "projection")
    _require_integer_fields(
        source,
        SOURCE_FIELDS - {"factorization"},
        "source",
    )
    _require_integer_fields(candidate, CANDIDATE_FIELDS, "candidate")
    _require_integer_fields(
        projection,
        PROJECTION_FIELDS - {"source_t5_coordinates", "target_t5_coordinates"},
        "projection",
    )
    factors = _factorization_v1(source["factorization"])

    p = source["root_context"]
    if not (_is_prime_exact(p) and p % 24 == 1):
        _reject(
            MathReplayRejectCode.NOT_CORE_PRIME,
            "source.root_context must be an exact prime congruent to 1 modulo 24",
        )
    t = (p - 1) // 24
    u = (p - 1) // 4
    x = (p + 3) // 4
    product = 1
    for factor, exponent in factors:
        product *= factor**exponent
    if not (
        source["q"] == 1
        and source["gap"] == 3
        and source["u"] == u
        and source["x"] == x
        and x == 6 * t + 1
        and product == x
        and all(factor % 3 == 1 for factor, _exponent in factors)
        and source["endpoint_fiber_code"] == ENDPOINT_G
        and source["major_phase_code"] == PHASE_TYPEII_G_HANDOFF
        and source["provenance_code"] == PROVENANCE_ORDINARY_ENDPOINT
    ):
        _reject(
            MathReplayRejectCode.NOT_Q_ONE_G,
            "raw q/gap/X factorization does not establish an ordinary q=1 G source",
        )
    if not (
        source["equation_rank"] == p
        and source["equation_numerator"] == 4
        and source["equation_denominator"] == p
    ):
        _reject(
            MathReplayRejectCode.CROSS_ARTIFACT_MISMATCH,
            "source equation coordinates do not equal 4/p at rank p",
        )
    if not (
        source["mark_kind_code"] == MARK_ROOT_SOL
        and source["mark_root_context"] == p
        and source["mark_equation_rank"] == p
    ):
        _reject(
            MathReplayRejectCode.MARK_MISMATCH,
            "source mark is not the ordinary ROOT_SOL(p) mark",
        )
    if source["declared_branch_type_code"] != OWNER_TYPEII_G_ENDPOINT:
        _reject(
            MathReplayRejectCode.OWNER_MISMATCH,
            "source declaration is not the branch-local ordinary G type label",
        )

    if candidate["root_context"] != p or projection["root_context"] != p:
        _reject(
            MathReplayRejectCode.CROSS_ARTIFACT_MISMATCH,
            "p was swapped across source, candidate, or projection",
        )
    if candidate["t"] != t or candidate["x"] != x:
        _reject(
            MathReplayRejectCode.ROOT_FORMULA_MISMATCH,
            "candidate t or X does not replay from p",
        )

    chart_r = 16 * t + 3
    chart_k = x * (16 * t + 1)
    if candidate["chart_r"] != chart_r or candidate["chart_k"] != chart_k:
        _reject(
            MathReplayRejectCode.CHART_IDENTITY_MISMATCH,
            "candidate chart is not the closed-form full-carrier chart",
        )
    if not (
        candidate["support_a"] == 1
        and 4 * chart_k == p * chart_r + 1
        and gcd(x, chart_k) == x
        and chart_k % x == 0
        and 3 <= chart_r <= p - 2
    ):
        _reject(
            MathReplayRejectCode.CHART_IDENTITY_MISMATCH,
            "full-carrier Type-I chart identity did not replay",
        )

    period = 4 * x
    previous_r = chart_r - period
    next_r = chart_r + period
    if not (
        gcd(4, x) == 1
        and gcd(3, x) == 1
        and chart_r % 4 == 3
        and (3 * chart_r - 1) % x == 0
        and 3 * chart_r - 1 == 8 * x
        and previous_r < 3
        and next_r > p - 2
    ):
        _reject(
            MathReplayRejectCode.LOW_CHART_UNIQUENESS_MISMATCH,
            "CRT residue class does not isolate one low full-carrier chart",
        )

    expected_source = (
        p,
        chart_r * (p - 1) - p,
        p - 1,
    )
    expected_anchor = (1, chart_r - 1, 1)
    candidate_source = (
        candidate["source_u"],
        candidate["source_v"],
        candidate["source_m"],
    )
    candidate_anchor = (
        candidate["anchor_u"],
        candidate["anchor_v"],
        candidate["anchor_m"],
    )
    if not (
        candidate_source == expected_source
        and candidate_anchor == expected_anchor
        and candidate["edge_prime"] == p
        and candidate["edge_shift"] == 1
        and candidate["gcd_reduction"] == 1
        and min(candidate_source) > 0
        and candidate_source[0] + candidate_source[1]
        == chart_r * candidate_source[2]
        and gcd(candidate_source[0], candidate_source[1]) == 1
        and chart_k % p != 0
        and candidate_source[0] % p == 0
        and (candidate_source[1] + chart_r) % p == 0
        and (candidate_source[2] + 1) % p == 0
        and (
            candidate_source[0] // p,
            (candidate_source[1] + chart_r) // p,
            (candidate_source[2] + 1) // p,
        )
        == expected_anchor
    ):
        _reject(
            MathReplayRejectCode.FRESH_SOURCE_MISMATCH,
            "fresh p-source or its raw p-edge identity did not replay",
        )

    if not (
        projection["equation_rank"] == p
        and projection["equation_numerator"] == 4
        and projection["equation_denominator"] == p
        and projection["major_phase_code"] == PHASE_TYPEI
        and projection["type_i_protocol_code"] == PROTOCOL_CHARGED
        and projection["provenance_code"] == PROVENANCE_FULL_CARRIER_POST_G
        and projection["full_carrier_scope_code"] == 1
        and projection["support_a"] == 1
        and projection["chart_r"] == chart_r
        and projection["chart_k"] == chart_k
    ):
        _reject(
            MathReplayRejectCode.PROJECTION_MISMATCH,
            "projection is not the canonical low full-carrier Type-I root",
        )
    if not (
        projection["mark_kind_code"] == MARK_ROOT_SOL
        and projection["mark_root_context"] == p
        and projection["mark_equation_rank"] == p
        and projection["mark_kind_code"] == source["mark_kind_code"]
        and projection["mark_root_context"] == source["mark_root_context"]
        and projection["mark_equation_rank"] == source["mark_equation_rank"]
    ):
        _reject(
            MathReplayRejectCode.MARK_MISMATCH,
            "source and projection do not carry the same ROOT_SOL(p) mark",
        )
    if projection["declared_branch_type_code"] != OWNER_TYPEI_FULL_CARRIER_POST_G:
        _reject(
            MathReplayRejectCode.OWNER_MISMATCH,
            "projection declaration is not the branch-local full-carrier type label",
        )

    source_coordinates = _potential_v1(
        projection["source_t5_coordinates"], "projection.source_t5_coordinates"
    )
    target_coordinates = _potential_v1(
        projection["target_t5_coordinates"], "projection.target_t5_coordinates"
    )
    b_p = (p - 1) ** 2 // 4
    expected_source_coordinates = (
        p,
        PHASE_TYPEII_G_HANDOFF,
        PROTOCOL_NONE,
        0,
        0,
        0,
        0,
    )
    expected_target_coordinates = (
        p,
        PHASE_TYPEI,
        PROTOCOL_CHARGED,
        b_p,
        chart_k,
        0,
        0,
    )
    if not (
        projection["ticket_code"] == TICKET_PHASE_DROP
        and source_coordinates == expected_source_coordinates
        and target_coordinates == expected_target_coordinates
        and target_coordinates < source_coordinates
        and target_coordinates[0] == source_coordinates[0]
        and target_coordinates[1] < source_coordinates[1]
    ):
        _reject(
            MathReplayRejectCode.POTENTIAL_MISMATCH,
            "the canonical N^7 vectors do not give the TYPEII_G_HANDOFF to TYPEI phase drop",
        )

    core_g = CoreGReplayV1(
        prime=p,
        t=t,
        u=u,
        x=x,
        factorization=factors,
        source_phase="TYPEII_G_HANDOFF",
        expected_branch_source_type="type_ii_relation_g_endpoint",
    )
    root = FullCarrierRootReplayV1(
        x=x,
        chart_r=chart_r,
        chart_k=chart_k,
        support_a=1,
        low_r_min=3,
        low_r_max=p - 2,
        congruence_modulus=period,
        previous_congruent_r=previous_r,
        next_congruent_r=next_r,
    )
    fresh_source = FreshSourceReplayV1(
        source=expected_source,
        edge_prime=p,
        edge_shift=1,
        gcd_reduction=1,
        destination=expected_anchor,
    )
    canonical_projection = CanonicalProjectionReplayV1(
        equation_target=(4, p),
        equation_rank=p,
        target_phase="TYPEI",
        target_protocol="CHARGED",
        target_provenance="FULL_CARRIER_POST_G",
        target_scope="fresh_source_tree_only",
        target_chart=(chart_r, chart_k),
        target_support=1,
        expected_branch_target_type="type_i_full_carrier_post_g",
    )
    identity_lift = IdentityLiftReplayV1(
        domain=f"Sol({p})",
        codomain=f"Sol({p})",
        rule="identity",
        mark_kind="ROOT_SOL",
        nonemptiness_claimed=False,
        terminal_membership_claimed=False,
    )
    phase_drop = T5PhaseDropReplayV1(
        source_coordinates=source_coordinates,
        target_coordinates=target_coordinates,
        ticket="PHASE_DROP_EVIDENCE_ONLY",
        first_strict_coordinate="major_phase",
        strict_lexicographic_drop=True,
        admission_ticket_issued=False,
    )
    payload = {
        "schema_id": SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "status": REPLAY_STATUS,
        "source_input_digest": canonical_digest_v1(source),
        "candidate_input_digest": canonical_digest_v1(candidate),
        "projection_input_digest": canonical_digest_v1(projection),
        "core_g": core_g,
        "full_carrier_root": root,
        "fresh_source": fresh_source,
        "canonical_projection": canonical_projection,
        "identity_lift": identity_lift,
        "t5_phase_drop": phase_drop,
        "terminal_authority": BLOCKED,
        "role_authority": BLOCKED,
        "issuance_allowed": False,
        "scope_exclusions": SCOPE_EXCLUSIONS,
    }
    return QOnePhaseRootMathReplayV1(
        **payload,
        digest=canonical_digest_v1(payload),
    )


def replay_bundle_json_v1(encoded: str) -> QOnePhaseRootMathReplayV1:
    value = loads_strict_v1(encoded)
    bundle = _require_object(
        value, BUNDLE_FIELDS, "bundle", require_schema_version=False
    )
    return replay_q_one_phase_root_math_v1(
        bundle["source"], bundle["candidate"], bundle["projection"]
    )


def _is_bare_digest(value: Any) -> bool:
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _exact_text(value: Any, expected: str) -> bool:
    return type(value) is str and value == expected


def _validate_receipt_v1(receipt: QOnePhaseRootMathReplayV1) -> None:
    """Revalidate every typed output field before trusting its content seal."""

    if type(receipt) is not QOnePhaseRootMathReplayV1:
        _reject(
            MathReplayRejectCode.MALFORMED_RECEIPT,
            "receipt must be an exact QOnePhaseRootMathReplayV1",
        )
    exact_children = (
        (receipt.core_g, CoreGReplayV1, "core_g"),
        (receipt.full_carrier_root, FullCarrierRootReplayV1, "full_carrier_root"),
        (receipt.fresh_source, FreshSourceReplayV1, "fresh_source"),
        (
            receipt.canonical_projection,
            CanonicalProjectionReplayV1,
            "canonical_projection",
        ),
        (receipt.identity_lift, IdentityLiftReplayV1, "identity_lift"),
        (receipt.t5_phase_drop, T5PhaseDropReplayV1, "t5_phase_drop"),
    )
    for value, expected_type, name in exact_children:
        if type(value) is not expected_type:
            _reject(
                MathReplayRejectCode.MALFORMED_RECEIPT,
                f"{name} must be an exact {expected_type.__name__}",
            )
    if not (
        _exact_text(receipt.schema_id, SCHEMA_ID)
        and type(receipt.schema_version) is int
        and receipt.schema_version == SCHEMA_VERSION
        and _exact_text(receipt.status, REPLAY_STATUS)
        and type(receipt.scope_exclusions) is tuple
        and all(type(item) is str for item in receipt.scope_exclusions)
        and receipt.scope_exclusions == SCOPE_EXCLUSIONS
    ):
        _reject(
            MathReplayRejectCode.MALFORMED_RECEIPT,
            "outer receipt identity, status, or scope boundary changed",
        )
    if not all(
        _is_bare_digest(value)
        for value in (
            receipt.source_input_digest,
            receipt.candidate_input_digest,
            receipt.projection_input_digest,
            receipt.digest,
        )
    ):
        _reject(
            MathReplayRejectCode.MALFORMED_RECEIPT,
            "receipt digests must be bare lowercase SHA-256 values",
        )
    if not (
        _exact_text(receipt.terminal_authority, BLOCKED)
        and _exact_text(receipt.role_authority, BLOCKED)
        and receipt.issuance_allowed is False
    ):
        _reject(
            MathReplayRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
            "terminal, role, and issuance authority must remain blocked",
        )

    core = receipt.core_g
    if not (
        type(core.prime) is int
        and _is_prime_exact(core.prime)
        and core.prime % 24 == 1
    ):
        _reject(MathReplayRejectCode.NOT_CORE_PRIME, "receipt core prime changed")
    p = core.prime
    t = (p - 1) // 24
    x = (p + 3) // 4
    if not (
        type(core.t) is int
        and type(core.u) is int
        and type(core.x) is int
        and core.t == t
        and core.u == (p - 1) // 4
        and core.x == x == 6 * t + 1
        and type(core.factorization) is tuple
        and _exact_text(core.source_phase, "TYPEII_G_HANDOFF")
        and _exact_text(
            core.expected_branch_source_type,
            "type_ii_relation_g_endpoint",
        )
    ):
        _reject(
            MathReplayRejectCode.MALFORMED_RECEIPT,
            "core q=1 G coordinates or branch-local type label changed",
        )
    product = 1
    previous_factor = 1
    for pair in core.factorization:
        if not (
            type(pair) is tuple
            and len(pair) == 2
            and type(pair[0]) is int
            and type(pair[1]) is int
            and pair[0] > previous_factor
            and pair[1] > 0
            and _is_prime_exact(pair[0])
            and pair[0] % 3 == 1
        ):
            _reject(
                MathReplayRejectCode.NOT_Q_ONE_G,
                "receipt G factorization is not exact and canonical",
            )
        product *= pair[0] ** pair[1]
        previous_factor = pair[0]
    if not core.factorization or product != x:
        _reject(
            MathReplayRejectCode.NOT_Q_ONE_G,
            "receipt G factorization does not multiply to X",
        )

    root = receipt.full_carrier_root
    chart_r = 16 * t + 3
    chart_k = x * (16 * t + 1)
    if not all(
        type(value) is int
        for value in (
            root.x,
            root.chart_r,
            root.chart_k,
            root.support_a,
            root.low_r_min,
            root.low_r_max,
            root.congruence_modulus,
            root.previous_congruent_r,
            root.next_congruent_r,
        )
    ) or not (
        root.x == x
        and root.chart_r == chart_r
        and root.chart_k == chart_k
        and root.support_a == 1
        and root.low_r_min == 3
        and root.low_r_max == p - 2
        and root.congruence_modulus == 4 * x
        and root.previous_congruent_r == chart_r - 4 * x < 3
        and root.next_congruent_r == chart_r + 4 * x > p - 2
        and 4 * chart_k == p * chart_r + 1
        and gcd(x, chart_k) == x
        and 3 * chart_r - 1 == 8 * x
    ):
        _reject(
            MathReplayRejectCode.LOW_CHART_UNIQUENESS_MISMATCH,
            "receipt full-carrier root or CRT uniqueness witness changed",
        )

    fresh = receipt.fresh_source
    expected_source = (p, chart_r * (p - 1) - p, p - 1)
    expected_destination = (1, chart_r - 1, 1)
    if not (
        type(fresh.source) is tuple
        and type(fresh.destination) is tuple
        and all(type(value) is int for value in fresh.source + fresh.destination)
        and type(fresh.edge_prime) is int
        and type(fresh.edge_shift) is int
        and type(fresh.gcd_reduction) is int
        and fresh.source == expected_source
        and fresh.edge_prime == p
        and fresh.edge_shift == 1
        and fresh.gcd_reduction == 1
        and fresh.destination == expected_destination
        and fresh.source[0] + fresh.source[1] == chart_r * fresh.source[2]
        and gcd(fresh.source[0], fresh.source[1]) == 1
        and chart_k % p != 0
        and (
            fresh.source[0] // p,
            (fresh.source[1] + chart_r) // p,
            (fresh.source[2] + 1) // p,
        )
        == fresh.destination
    ):
        _reject(
            MathReplayRejectCode.FRESH_SOURCE_MISMATCH,
            "receipt fresh source or p-edge identity changed",
        )

    projection = receipt.canonical_projection
    if not (
        type(projection.equation_target) is tuple
        and len(projection.equation_target) == 2
        and all(type(value) is int for value in projection.equation_target)
        and projection.equation_target == (4, p)
        and type(projection.equation_rank) is int
        and projection.equation_rank == p
        and _exact_text(projection.target_phase, "TYPEI")
        and _exact_text(projection.target_protocol, "CHARGED")
        and _exact_text(
            projection.target_provenance,
            "FULL_CARRIER_POST_G",
        )
        and _exact_text(projection.target_scope, "fresh_source_tree_only")
        and type(projection.target_chart) is tuple
        and len(projection.target_chart) == 2
        and all(type(value) is int for value in projection.target_chart)
        and projection.target_chart == (chart_r, chart_k)
        and type(projection.target_support) is int
        and projection.target_support == 1
        and _exact_text(
            projection.expected_branch_target_type,
            "type_i_full_carrier_post_g",
        )
    ):
        _reject(
            MathReplayRejectCode.PROJECTION_MISMATCH,
            "receipt projection or branch-local target type label changed",
        )

    lift = receipt.identity_lift
    if not (
        _exact_text(lift.domain, f"Sol({p})")
        and _exact_text(lift.codomain, f"Sol({p})")
        and _exact_text(lift.rule, "identity")
        and _exact_text(lift.mark_kind, "ROOT_SOL")
        and lift.nonemptiness_claimed is False
        and lift.terminal_membership_claimed is False
    ):
        _reject(
            MathReplayRejectCode.MARK_MISMATCH,
            "receipt identity lift or its non-claim flags changed",
        )

    phase = receipt.t5_phase_drop
    source_coordinates = (p, 3, 0, 0, 0, 0, 0)
    target_coordinates = (p, 2, 4, (p - 1) ** 2 // 4, chart_k, 0, 0)
    if not (
        type(phase.source_coordinates) is tuple
        and type(phase.target_coordinates) is tuple
        and len(phase.source_coordinates) == len(phase.target_coordinates) == 7
        and all(
            type(value) is int and value >= 0
            for value in phase.source_coordinates + phase.target_coordinates
        )
        and phase.source_coordinates == source_coordinates
        and phase.target_coordinates == target_coordinates
        and phase.target_coordinates < phase.source_coordinates
        and _exact_text(phase.ticket, "PHASE_DROP_EVIDENCE_ONLY")
        and _exact_text(phase.first_strict_coordinate, "major_phase")
        and phase.strict_lexicographic_drop is True
        and phase.admission_ticket_issued is False
    ):
        if phase.admission_ticket_issued is not False:
            _reject(
                MathReplayRejectCode.AUTHORITY_BOUNDARY_VIOLATION,
                "the replay cannot issue a T5 admission ticket",
            )
        _reject(
            MathReplayRejectCode.POTENTIAL_MISMATCH,
            "receipt T5 phase-drop evidence changed",
        )


def receipt_to_mapping_v1(receipt: QOnePhaseRootMathReplayV1) -> dict[str, Any]:
    _validate_receipt_v1(receipt)
    result = _jsonable(receipt)
    stored_digest = result.pop("digest")
    if canonical_digest_v1(result) != stored_digest:
        _reject(MathReplayRejectCode.DIGEST_MISMATCH, "receipt seal did not replay")
    result["digest"] = stored_digest
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()
    receipt = replay_bundle_json_v1(args.input.read_text(encoding="utf-8"))
    print(json.dumps(receipt_to_mapping_v1(receipt), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
