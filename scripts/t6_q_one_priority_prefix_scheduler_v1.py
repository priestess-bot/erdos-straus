#!/usr/bin/env python3
"""Independent evidence-only q=1 root priority-prefix scheduler.

The scheduler first replays a schedule-independent ordinary q=1 G domain from
raw integers.  It then exhausts every Bradford Type-I/II divisor candidate for
the frozen gaps 3, 7, and 11.  Passing this module proves completeness only for
that registered prefix.  It grants no terminal, role, issuance, transition, or
queue authority and makes no global root-terminal exhaustion claim.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, NoReturn


DOMAIN_SCHEMA_ID = "q1_priority_prefix_domain_v1"
DOMAIN_SCHEMA_VERSION = 1
EVIDENCE_SCHEMA_ID = "t6_q_one_priority_prefix_evidence_v1"
EVIDENCE_SCHEMA_VERSION = 1

SCHEDULE_ID = "q1_root_gap_3_7_11_registered_priority_prefix_v1"
ORDERED_GAPS = (3, 7, 11)
CANDIDATE_ORDER = "gap_ascending_divisor_ascending_type_I_before_II"
COVERAGE_SCOPE = "REGISTERED_PRIORITY_PREFIX_GAPS_3_7_11"
NEXT_UNCHECKED_GAP = 15

ROOT_TERMINAL_HIT = "ROOT_TERMINAL_HIT"
PREFIX_MISS_EVIDENCE_ONLY = "PREFIX_MISS_EVIDENCE_ONLY"
GAP_HAS_TERMINAL = "GAP_HAS_TERMINAL"
GAP_PREFIX_MISS = "GAP_PREFIX_MISS"
BLOCKED = "BLOCKED"

MARK_ROOT_SOL = 1
ENDPOINT_G = 2
PHASE_TYPEII_G_HANDOFF = 3
PROVENANCE_ORDINARY_ENDPOINT = 1

DOMAIN_FIELDS = frozenset(
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


class PriorityPrefixRejectCode(str, Enum):
    INPUT_NOT_OBJECT = "INPUT_NOT_OBJECT"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    WRONG_SCHEMA = "WRONG_SCHEMA"
    WRONG_SCHEMA_VERSION = "WRONG_SCHEMA_VERSION"
    MALFORMED_INTEGER = "MALFORMED_INTEGER"
    MALFORMED_FACTORIZATION = "MALFORMED_FACTORIZATION"
    NOT_CORE_PRIME = "NOT_CORE_PRIME"
    DOMAIN_MISMATCH = "DOMAIN_MISMATCH"
    FACTORIZATION_MISMATCH = "FACTORIZATION_MISMATCH"
    CERTIFICATE_REPLAY_FAILED = "CERTIFICATE_REPLAY_FAILED"
    MALFORMED_EVIDENCE = "MALFORMED_EVIDENCE"
    DIGEST_MISMATCH = "DIGEST_MISMATCH"


class PriorityPrefixError(ValueError):
    """Fail-closed scheduler error with a stable rejection code."""

    def __init__(self, code: PriorityPrefixRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


@dataclass(frozen=True, slots=True)
class QOnePriorityPrefixDomainV1:
    root_context: int
    gap_three_x: int
    gap_three_factorization: tuple[tuple[int, int], ...]
    input_digest: str


@dataclass(frozen=True, slots=True)
class PriorityPrefixCertificateV1:
    certificate_type: str
    gap: int
    x: int
    divisor: int
    y: int
    z: int
    candidate_index: int


@dataclass(frozen=True, slots=True)
class PriorityPrefixGapScanV1:
    gap: int
    x: int
    factorization: tuple[tuple[int, int], ...]
    divisor_universe: tuple[int, ...]
    matching_certificates: tuple[PriorityPrefixCertificateV1, ...]
    scan_status: str
    scan_digest: str


@dataclass(frozen=True, slots=True)
class QOnePriorityPrefixEvidenceV1:
    schema_id: str
    schema_version: int
    status: str
    schedule_id: str
    domain_input_digest: str
    root_context: int
    ordered_gaps: tuple[int, ...]
    candidate_order: str
    gap_scans: tuple[PriorityPrefixGapScanV1, ...]
    selected_terminal: PriorityPrefixCertificateV1 | None
    coverage_scope: str
    global_exhaustion: bool
    next_unchecked_gap: int
    terminal_authority: str
    role_authority: str
    issuance_allowed: bool
    digest: str


def _reject(code: PriorityPrefixRejectCode, detail: str) -> NoReturn:
    raise PriorityPrefixError(code, detail)


def _is_plain_int(value: Any) -> bool:
    return type(value) is int


def _is_sha256(value: Any) -> bool:
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def canonical_json_v1(value: Any) -> str:
    try:
        return json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            f"value is not canonical JSON: {exc}",
        )


def canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(canonical_json_v1(value).encode("ascii")).hexdigest()


def _is_prime_exact(value: int) -> bool:
    if value < 2:
        return False
    if value in (2, 3):
        return True
    if value % 2 == 0 or value % 3 == 0:
        return False
    divisor = 5
    step = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += step
        step = 6 - step
    return True


def _factor_integer_exact(value: int) -> tuple[tuple[int, int], ...]:
    if not _is_plain_int(value) or value <= 0:
        _reject(
            PriorityPrefixRejectCode.MALFORMED_INTEGER,
            "factorization input must be a positive plain integer",
        )
    remaining = value
    factors: list[tuple[int, int]] = []
    for divisor in (2, 3):
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
    divisor = 5
    step = 2
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor += step
        step = 6 - step
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def _parse_factorization(
    value: Any,
) -> tuple[tuple[int, int], ...]:
    if type(value) is not list or not value:
        _reject(
            PriorityPrefixRejectCode.MALFORMED_FACTORIZATION,
            "gap_three_factorization must be a nonempty JSON array",
        )
    result: list[tuple[int, int]] = []
    previous = 1
    for index, pair in enumerate(value):
        if type(pair) is not list or len(pair) != 2:
            _reject(
                PriorityPrefixRejectCode.MALFORMED_FACTORIZATION,
                f"factorization entry {index} must be [prime, exponent]",
            )
        prime, exponent = pair
        if (
            not _is_plain_int(prime)
            or not _is_plain_int(exponent)
            or prime <= previous
            or exponent <= 0
            or not _is_prime_exact(prime)
        ):
            _reject(
                PriorityPrefixRejectCode.MALFORMED_FACTORIZATION,
                f"factorization entry {index} is not a strictly ordered prime power",
            )
        result.append((prime, exponent))
        previous = prime
    return tuple(result)


def _replay_domain_v1(value: Any) -> QOnePriorityPrefixDomainV1:
    if type(value) is not dict:
        _reject(
            PriorityPrefixRejectCode.INPUT_NOT_OBJECT,
            "domain input must be an exact raw dict",
        )
    if any(type(key) is not str for key in value):
        _reject(
            PriorityPrefixRejectCode.FIELD_SET_MISMATCH,
            "domain keys must be exact strings",
        )
    fields = frozenset(value)
    if fields != DOMAIN_FIELDS:
        missing = sorted(DOMAIN_FIELDS - fields)
        extra = sorted(fields - DOMAIN_FIELDS)
        _reject(
            PriorityPrefixRejectCode.FIELD_SET_MISMATCH,
            f"domain fields differ: missing={missing}, extra={extra}",
        )
    if type(value["schema_id"]) is not str or value["schema_id"] != DOMAIN_SCHEMA_ID:
        _reject(
            PriorityPrefixRejectCode.WRONG_SCHEMA,
            f"schema_id must be {DOMAIN_SCHEMA_ID!r}",
        )
    if (
        not _is_plain_int(value["schema_version"])
        or value["schema_version"] != DOMAIN_SCHEMA_VERSION
    ):
        _reject(
            PriorityPrefixRejectCode.WRONG_SCHEMA_VERSION,
            "schema_version must be the plain integer 1",
        )

    integer_fields = DOMAIN_FIELDS - {
        "schema_id",
        "gap_three_factorization",
    }
    for name in integer_fields:
        if not _is_plain_int(value[name]):
            _reject(
                PriorityPrefixRejectCode.MALFORMED_INTEGER,
                f"{name} must be a plain integer, not bool or float",
            )

    p = value["root_context"]
    if not (_is_prime_exact(p) and p % 24 == 1):
        _reject(
            PriorityPrefixRejectCode.NOT_CORE_PRIME,
            "root_context must be an exact prime congruent to 1 modulo 24",
        )
    x_three = (p + 3) // 4
    if not (
        value["equation_rank"] == p
        and value["equation_numerator"] == 4
        and value["equation_denominator"] == p
        and value["q"] == 1
        and value["gap_three_x"] == x_three
        and value["endpoint_fiber_code"] == ENDPOINT_G
        and value["major_phase_code"] == PHASE_TYPEII_G_HANDOFF
        and value["provenance_code"] == PROVENANCE_ORDINARY_ENDPOINT
        and value["mark_kind_code"] == MARK_ROOT_SOL
        and value["mark_root_context"] == p
        and value["mark_equation_rank"] == p
    ):
        _reject(
            PriorityPrefixRejectCode.DOMAIN_MISMATCH,
            "raw equation, q=1 G, phase, provenance, or ROOT_SOL coordinates mismatch",
        )

    declared_factors = _parse_factorization(value["gap_three_factorization"])
    actual_factors = _factor_integer_exact(x_three)
    if declared_factors != actual_factors:
        _reject(
            PriorityPrefixRejectCode.FACTORIZATION_MISMATCH,
            "gap-three factorization is not the complete canonical factorization of X",
        )
    if any(prime % 3 != 1 for prime, _exponent in actual_factors):
        _reject(
            PriorityPrefixRejectCode.DOMAIN_MISMATCH,
            "gap-three X contains a prime factor not congruent to 1 modulo 3",
        )
    return QOnePriorityPrefixDomainV1(
        root_context=p,
        gap_three_x=x_three,
        gap_three_factorization=actual_factors,
        input_digest=canonical_digest_v1(value),
    )


def _divisors_of_square(
    factorization: tuple[tuple[int, int], ...],
) -> tuple[int, ...]:
    divisors = [1]
    for prime, exponent in factorization:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(2 * exponent + 1)
        ]
    return tuple(sorted(divisors))


def _root_equation_holds(p: int, x: int, y: int, z: int) -> bool:
    return x > 0 and y > 0 and z > 0 and 4 * x * y * z == p * (x * y + x * z + y * z)


def _certificate_mapping(
    certificate: PriorityPrefixCertificateV1,
) -> dict[str, Any]:
    return {
        "certificate_type": certificate.certificate_type,
        "gap": certificate.gap,
        "x": certificate.x,
        "divisor": certificate.divisor,
        "y": certificate.y,
        "z": certificate.z,
        "candidate_index": certificate.candidate_index,
    }


def _make_certificate(
    *,
    certificate_type: str,
    p: int,
    gap: int,
    x: int,
    divisor: int,
    divisor_index: int,
) -> PriorityPrefixCertificateV1:
    quotient = x * x // divisor
    if certificate_type == "TYPE_I":
        y_numerator = p * x + divisor
        z_numerator = p * (x + p * quotient)
        type_rank = 0
    elif certificate_type == "TYPE_II":
        y_numerator = p * (x + divisor)
        z_numerator = p * (x + quotient)
        type_rank = 1
    else:
        _reject(
            PriorityPrefixRejectCode.CERTIFICATE_REPLAY_FAILED,
            f"unknown certificate type {certificate_type!r}",
        )
    if y_numerator % gap or z_numerator % gap:
        _reject(
            PriorityPrefixRejectCode.CERTIFICATE_REPLAY_FAILED,
            f"{certificate_type} reconstruction is nonintegral at gap={gap}, d={divisor}",
        )
    y = y_numerator // gap
    z = z_numerator // gap
    if not _root_equation_holds(p, x, y, z):
        _reject(
            PriorityPrefixRejectCode.CERTIFICATE_REPLAY_FAILED,
            f"{certificate_type} root equation failed at gap={gap}, d={divisor}",
        )
    return PriorityPrefixCertificateV1(
        certificate_type=certificate_type,
        gap=gap,
        x=x,
        divisor=divisor,
        y=y,
        z=z,
        candidate_index=2 * divisor_index + type_rank,
    )


def _scan_unsigned_mapping(scan: PriorityPrefixGapScanV1) -> dict[str, Any]:
    return {
        "gap": scan.gap,
        "x": scan.x,
        "factorization": [[prime, exponent] for prime, exponent in scan.factorization],
        "divisor_universe": list(scan.divisor_universe),
        "matching_certificates": [
            _certificate_mapping(certificate)
            for certificate in scan.matching_certificates
        ],
        "scan_status": scan.scan_status,
    }


def _scan_gap_v1(p: int, gap: int) -> PriorityPrefixGapScanV1:
    if gap not in ORDERED_GAPS:
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            f"gap {gap} is outside the frozen prefix",
        )
    x = (p + gap) // 4
    factors = _factor_integer_exact(x)
    divisors = _divisors_of_square(factors)
    matches: list[PriorityPrefixCertificateV1] = []
    for divisor_index, divisor in enumerate(divisors):
        if (p * x + divisor) % gap == 0:
            matches.append(
                _make_certificate(
                    certificate_type="TYPE_I",
                    p=p,
                    gap=gap,
                    x=x,
                    divisor=divisor,
                    divisor_index=divisor_index,
                )
            )
        if divisor <= x and (x + divisor) % gap == 0:
            matches.append(
                _make_certificate(
                    certificate_type="TYPE_II",
                    p=p,
                    gap=gap,
                    x=x,
                    divisor=divisor,
                    divisor_index=divisor_index,
                )
            )
    scan = PriorityPrefixGapScanV1(
        gap=gap,
        x=x,
        factorization=factors,
        divisor_universe=divisors,
        matching_certificates=tuple(matches),
        scan_status=GAP_HAS_TERMINAL if matches else GAP_PREFIX_MISS,
        scan_digest="",
    )
    return PriorityPrefixGapScanV1(
        gap=scan.gap,
        x=scan.x,
        factorization=scan.factorization,
        divisor_universe=scan.divisor_universe,
        matching_certificates=scan.matching_certificates,
        scan_status=scan.scan_status,
        scan_digest=canonical_digest_v1(_scan_unsigned_mapping(scan)),
    )


def _evidence_unsigned_mapping(
    evidence: QOnePriorityPrefixEvidenceV1,
) -> dict[str, Any]:
    scans = []
    for scan in evidence.gap_scans:
        mapping = _scan_unsigned_mapping(scan)
        mapping["scan_digest"] = scan.scan_digest
        scans.append(mapping)
    return {
        "schema_id": evidence.schema_id,
        "schema_version": evidence.schema_version,
        "status": evidence.status,
        "schedule_id": evidence.schedule_id,
        "domain_input_digest": evidence.domain_input_digest,
        "root_context": evidence.root_context,
        "ordered_gaps": list(evidence.ordered_gaps),
        "candidate_order": evidence.candidate_order,
        "gap_scans": scans,
        "selected_terminal": (
            None
            if evidence.selected_terminal is None
            else _certificate_mapping(evidence.selected_terminal)
        ),
        "coverage_scope": evidence.coverage_scope,
        "global_exhaustion": evidence.global_exhaustion,
        "next_unchecked_gap": evidence.next_unchecked_gap,
        "terminal_authority": evidence.terminal_authority,
        "role_authority": evidence.role_authority,
        "issuance_allowed": evidence.issuance_allowed,
    }


def replay_q_one_priority_prefix_v1(
    domain_value: dict[str, Any],
) -> QOnePriorityPrefixEvidenceV1:
    """Replay the exact q=1 G domain and exhaust the frozen priority prefix."""

    domain = _replay_domain_v1(domain_value)
    scans = tuple(_scan_gap_v1(domain.root_context, gap) for gap in ORDERED_GAPS)
    selected = next(
        (
            scan.matching_certificates[0]
            for scan in scans
            if scan.matching_certificates
        ),
        None,
    )
    evidence = QOnePriorityPrefixEvidenceV1(
        schema_id=EVIDENCE_SCHEMA_ID,
        schema_version=EVIDENCE_SCHEMA_VERSION,
        status=ROOT_TERMINAL_HIT if selected is not None else PREFIX_MISS_EVIDENCE_ONLY,
        schedule_id=SCHEDULE_ID,
        domain_input_digest=domain.input_digest,
        root_context=domain.root_context,
        ordered_gaps=ORDERED_GAPS,
        candidate_order=CANDIDATE_ORDER,
        gap_scans=scans,
        selected_terminal=selected,
        coverage_scope=COVERAGE_SCOPE,
        global_exhaustion=False,
        next_unchecked_gap=NEXT_UNCHECKED_GAP,
        terminal_authority=BLOCKED,
        role_authority=BLOCKED,
        issuance_allowed=False,
        digest="",
    )
    return QOnePriorityPrefixEvidenceV1(
        schema_id=evidence.schema_id,
        schema_version=evidence.schema_version,
        status=evidence.status,
        schedule_id=evidence.schedule_id,
        domain_input_digest=evidence.domain_input_digest,
        root_context=evidence.root_context,
        ordered_gaps=evidence.ordered_gaps,
        candidate_order=evidence.candidate_order,
        gap_scans=evidence.gap_scans,
        selected_terminal=evidence.selected_terminal,
        coverage_scope=evidence.coverage_scope,
        global_exhaustion=evidence.global_exhaustion,
        next_unchecked_gap=evidence.next_unchecked_gap,
        terminal_authority=evidence.terminal_authority,
        role_authority=evidence.role_authority,
        issuance_allowed=evidence.issuance_allowed,
        digest=canonical_digest_v1(_evidence_unsigned_mapping(evidence)),
    )


def _validate_evidence_v1(evidence: QOnePriorityPrefixEvidenceV1) -> None:
    if type(evidence) is not QOnePriorityPrefixEvidenceV1:
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            "evidence must be the exact frozen slots v1 dataclass",
        )
    if not _is_sha256(evidence.domain_input_digest):
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            "domain_input_digest must be lowercase sha256",
        )
    fixed = (
        type(evidence.schema_id) is str
        and evidence.schema_id == EVIDENCE_SCHEMA_ID
        and _is_plain_int(evidence.schema_version)
        and evidence.schema_version == EVIDENCE_SCHEMA_VERSION
        and type(evidence.status) is str
        and type(evidence.schedule_id) is str
        and evidence.schedule_id == SCHEDULE_ID
        and type(evidence.ordered_gaps) is tuple
        and all(_is_plain_int(gap) for gap in evidence.ordered_gaps)
        and evidence.ordered_gaps == ORDERED_GAPS
        and type(evidence.candidate_order) is str
        and evidence.candidate_order == CANDIDATE_ORDER
        and type(evidence.coverage_scope) is str
        and evidence.coverage_scope == COVERAGE_SCOPE
        and evidence.global_exhaustion is False
        and _is_plain_int(evidence.next_unchecked_gap)
        and evidence.next_unchecked_gap == NEXT_UNCHECKED_GAP
        and type(evidence.terminal_authority) is str
        and evidence.terminal_authority == BLOCKED
        and type(evidence.role_authority) is str
        and evidence.role_authority == BLOCKED
        and evidence.issuance_allowed is False
        and _is_plain_int(evidence.root_context)
        and _is_prime_exact(evidence.root_context)
        and evidence.root_context % 24 == 1
    )
    if not fixed:
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            "evidence constants, authority boundary, or root context changed",
        )
    if type(evidence.gap_scans) is not tuple or len(evidence.gap_scans) != len(ORDERED_GAPS):
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            "evidence must contain exactly three typed gap scans",
        )
    expected_scans = tuple(
        _scan_gap_v1(evidence.root_context, gap) for gap in ORDERED_GAPS
    )
    if any(type(scan) is not PriorityPrefixGapScanV1 for scan in evidence.gap_scans):
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            "every gap scan must be the exact frozen slots v1 dataclass",
        )
    if evidence.gap_scans != expected_scans:
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            "gap scans do not replay from the root context",
        )
    for scan in evidence.gap_scans:
        if any(
            type(certificate) is not PriorityPrefixCertificateV1
            for certificate in scan.matching_certificates
        ):
            _reject(
                PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
                "matching certificate has a non-v1 runtime type",
            )
        if not _is_sha256(scan.scan_digest):
            _reject(
                PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
                "scan_digest must be lowercase sha256",
            )
    expected_selected = next(
        (
            scan.matching_certificates[0]
            for scan in expected_scans
            if scan.matching_certificates
        ),
        None,
    )
    if evidence.selected_terminal != expected_selected or (
        evidence.selected_terminal is not None
        and type(evidence.selected_terminal) is not PriorityPrefixCertificateV1
    ):
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            "selected terminal is not the first candidate in the frozen total order",
        )
    expected_status = (
        ROOT_TERMINAL_HIT
        if expected_selected is not None
        else PREFIX_MISS_EVIDENCE_ONLY
    )
    if evidence.status != expected_status:
        _reject(
            PriorityPrefixRejectCode.MALFORMED_EVIDENCE,
            "outer status disagrees with the replayed prefix result",
        )
    if not _is_sha256(evidence.digest) or evidence.digest != canonical_digest_v1(
        _evidence_unsigned_mapping(evidence)
    ):
        _reject(
            PriorityPrefixRejectCode.DIGEST_MISMATCH,
            "outer evidence digest does not replay",
        )


def evidence_to_mapping_v1(
    evidence: QOnePriorityPrefixEvidenceV1,
) -> dict[str, Any]:
    """Validate and serialize one typed evidence object to its exact wire form."""

    _validate_evidence_v1(evidence)
    mapping = _evidence_unsigned_mapping(evidence)
    mapping["digest"] = evidence.digest
    return mapping


def evidence_to_json_v1(
    evidence: QOnePriorityPrefixEvidenceV1, *, pretty: bool = False
) -> str:
    mapping = evidence_to_mapping_v1(evidence)
    if pretty:
        return json.dumps(mapping, ensure_ascii=True, sort_keys=True, indent=2)
    return canonical_json_v1(mapping)


def loads_strict_v1(encoded: str) -> dict[str, Any]:
    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                _reject(
                    PriorityPrefixRejectCode.FIELD_SET_MISMATCH,
                    f"duplicate JSON key {key!r}",
                )
            result[key] = value
        return result

    def reject_number(value: str) -> NoReturn:
        _reject(
            PriorityPrefixRejectCode.MALFORMED_INTEGER,
            f"noninteger or nonfinite JSON number {value!r} is forbidden",
        )

    try:
        value = json.loads(
            encoded,
            object_pairs_hook=object_pairs,
            parse_float=reject_number,
            parse_constant=reject_number,
        )
    except PriorityPrefixError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        _reject(
            PriorityPrefixRejectCode.INPUT_NOT_OBJECT,
            f"invalid JSON: {exc}",
        )
    if type(value) is not dict:
        _reject(
            PriorityPrefixRejectCode.INPUT_NOT_OBJECT,
            "top-level JSON value must be an object",
        )
    return value


def _read_input(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default="-",
        help="exact q1_priority_prefix_domain_v1 JSON file, or '-' for stdin",
    )
    parser.add_argument("--pretty", action="store_true", help="pretty-print JSON")
    args = parser.parse_args(argv)
    evidence = replay_q_one_priority_prefix_v1(loads_strict_v1(_read_input(args.input)))
    print(evidence_to_json_v1(evidence, pretty=args.pretty))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
