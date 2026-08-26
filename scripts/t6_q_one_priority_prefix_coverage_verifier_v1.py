#!/usr/bin/env python3
"""Independent, non-authorizing q=1 priority-prefix coverage replay.

This verifier deliberately imports neither the scheduler nor any historical
runtime or reproduction module.  It reconstructs the complete canonical wire
for the registered gaps 3, 7, and 11 from a strict raw q=1 G domain object,
then requires the supplied scheduler evidence to have identical canonical JSON
bytes.  A successful return is evidence only; it grants no terminal, role,
issuance, E1, or queue authority.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
import re
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
VERIFIED_STATUS = "PREFIX_COVERAGE_REPLAY_VERIFIED_EVIDENCE_ONLY"
BLOCKED = "BLOCKED"

Q_ONE = 1
ENDPOINT_FIBER_G_CODE = 2
TYPEII_G_HANDOFF_PHASE_CODE = 3
ORDINARY_ENDPOINT_PROVENANCE_CODE = 1
ROOT_SOL_MARK_CODE = 1

_DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")

_DOMAIN_FIELDS = frozenset(
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
_CERTIFICATE_FIELDS = frozenset(
    {"certificate_type", "gap", "x", "divisor", "y", "z", "candidate_index"}
)
_SCAN_FIELDS = frozenset(
    {
        "gap",
        "x",
        "factorization",
        "divisor_universe",
        "matching_certificates",
        "scan_status",
        "scan_digest",
    }
)
_EVIDENCE_FIELDS = frozenset(
    {
        "schema_id",
        "schema_version",
        "status",
        "schedule_id",
        "domain_input_digest",
        "root_context",
        "ordered_gaps",
        "candidate_order",
        "gap_scans",
        "selected_terminal",
        "coverage_scope",
        "global_exhaustion",
        "next_unchecked_gap",
        "terminal_authority",
        "role_authority",
        "issuance_allowed",
        "digest",
    }
)


class PrefixCoverageRejectCode(str, Enum):
    INPUT_NOT_EXACT_DICT = "INPUT_NOT_EXACT_DICT"
    FIELD_SET_MISMATCH = "FIELD_SET_MISMATCH"
    MALFORMED_FIELD = "MALFORMED_FIELD"
    DOMAIN_SCHEMA_MISMATCH = "DOMAIN_SCHEMA_MISMATCH"
    ROOT_NOT_CORE_PRIME = "ROOT_NOT_CORE_PRIME"
    DOMAIN_ARITHMETIC_MISMATCH = "DOMAIN_ARITHMETIC_MISMATCH"
    DOMAIN_FACTORIZATION_MISMATCH = "DOMAIN_FACTORIZATION_MISMATCH"
    Q_ONE_G_DOMAIN_MISMATCH = "Q_ONE_G_DOMAIN_MISMATCH"
    EVIDENCE_SCHEMA_MISMATCH = "EVIDENCE_SCHEMA_MISMATCH"
    DOMAIN_BINDING_MISMATCH = "DOMAIN_BINDING_MISMATCH"
    SCHEDULE_SCOPE_MISMATCH = "SCHEDULE_SCOPE_MISMATCH"
    GAP_ORDER_MISMATCH = "GAP_ORDER_MISMATCH"
    CANDIDATE_ORDER_MISMATCH = "CANDIDATE_ORDER_MISMATCH"
    FACTORIZATION_MISMATCH = "FACTORIZATION_MISMATCH"
    DIVISOR_UNIVERSE_MISMATCH = "DIVISOR_UNIVERSE_MISMATCH"
    CERTIFICATE_MISMATCH = "CERTIFICATE_MISMATCH"
    SCAN_STATUS_MISMATCH = "SCAN_STATUS_MISMATCH"
    SCAN_DIGEST_MISMATCH = "SCAN_DIGEST_MISMATCH"
    SELECTED_TERMINAL_MISMATCH = "SELECTED_TERMINAL_MISMATCH"
    OUTCOME_MISMATCH = "OUTCOME_MISMATCH"
    GLOBAL_EXHAUSTION_FORBIDDEN = "GLOBAL_EXHAUSTION_FORBIDDEN"
    AUTHORITY_FORBIDDEN = "AUTHORITY_FORBIDDEN"
    OUTER_DIGEST_MISMATCH = "OUTER_DIGEST_MISMATCH"
    WIRE_MISMATCH = "WIRE_MISMATCH"
    INTERNAL_RECONSTRUCTION_FAILURE = "INTERNAL_RECONSTRUCTION_FAILURE"
    OUTPUT_INVARIANT_MISMATCH = "OUTPUT_INVARIANT_MISMATCH"


class PrefixCoverageVerificationError(ValueError):
    """Fail-closed verification error with a stable machine-readable code."""

    def __init__(self, code: PrefixCoverageRejectCode, detail: str):
        super().__init__(f"{code.value}: {detail}")
        self.code = code
        self.detail = detail


def _reject(code: PrefixCoverageRejectCode, detail: str) -> NoReturn:
    raise PrefixCoverageVerificationError(code, detail)


def _plain_int(value: Any) -> bool:
    return type(value) is int


def _require_plain_int(value: Any, name: str, minimum: int = 0) -> int:
    if not _plain_int(value) or value < minimum:
        _reject(
            PrefixCoverageRejectCode.MALFORMED_FIELD,
            f"{name} must be an integer >= {minimum}, not bool",
        )
    return value


def _require_exact_bool(value: Any, expected: bool, name: str) -> None:
    if type(value) is not bool or value is not expected:
        code = (
            PrefixCoverageRejectCode.GLOBAL_EXHAUSTION_FORBIDDEN
            if name == "global_exhaustion"
            else PrefixCoverageRejectCode.AUTHORITY_FORBIDDEN
        )
        _reject(code, f"{name} must be exactly {expected!r}")


def _require_text(value: Any, name: str) -> str:
    if type(value) is not str or not value:
        _reject(PrefixCoverageRejectCode.MALFORMED_FIELD, f"{name} must be text")
    return value


def _require_digest(value: Any, name: str) -> str:
    if type(value) is not str or _DIGEST_RE.fullmatch(value) is None:
        _reject(
            PrefixCoverageRejectCode.MALFORMED_FIELD,
            f"{name} must be a lowercase SHA-256 digest",
        )
    return value


def _require_exact_dict(value: Any, expected: frozenset[str], name: str) -> dict[str, Any]:
    if type(value) is not dict:
        _reject(
            PrefixCoverageRejectCode.INPUT_NOT_EXACT_DICT,
            f"{name} must be a plain JSON object",
        )
    if any(type(key) is not str for key in value):
        _reject(
            PrefixCoverageRejectCode.MALFORMED_FIELD,
            f"{name} keys must be exact strings",
        )
    actual = frozenset(value)
    if actual != expected:
        _reject(
            PrefixCoverageRejectCode.FIELD_SET_MISMATCH,
            f"{name}: missing={sorted(expected - actual)}, extra={sorted(actual - expected)}",
        )
    return value


def _strict_json_copy(value: Any, path: str = "$") -> Any:
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, child in value.items():
            if type(key) is not str:
                _reject(
                    PrefixCoverageRejectCode.MALFORMED_FIELD,
                    f"{path} contains a non-string key",
                )
            result[key] = _strict_json_copy(child, f"{path}.{key}")
        return result
    if type(value) is list:
        return [_strict_json_copy(child, f"{path}[{index}]") for index, child in enumerate(value)]
    if value is None or type(value) in {str, bool, int}:
        return copy.deepcopy(value)
    _reject(
        PrefixCoverageRejectCode.MALFORMED_FIELD,
        f"{path} contains non-exact JSON type {type(value).__name__}",
    )


def _canonical_json_v1(value: Any) -> str:
    try:
        return json.dumps(
            _strict_json_copy(value),
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        _reject(
            PrefixCoverageRejectCode.MALFORMED_FIELD,
            f"canonical JSON encoding failed: {exc}",
        )


def _canonical_digest_v1(value: Any) -> str:
    return hashlib.sha256(_canonical_json_v1(value).encode("ascii")).hexdigest()


def _is_prime_by_six_step_v1(value: int) -> bool:
    """Deterministic exact primality check, independent of scheduler code."""

    if value < 2:
        return False
    if value in (2, 3):
        return True
    if value % 2 == 0 or value % 3 == 0:
        return False
    candidate = 5
    step = 2
    while candidate <= value // candidate:
        if value % candidate == 0:
            return False
        candidate += step
        step = 6 - step
    return True


def _factor_by_odd_trial_v1(value: int) -> tuple[tuple[int, int], ...]:
    """Return the unique prime factorization using an independent odd trial loop."""

    if value < 1:
        _reject(
            PrefixCoverageRejectCode.INTERNAL_RECONSTRUCTION_FAILURE,
            "cannot factor a nonpositive integer",
        )
    remainder = value
    result: list[tuple[int, int]] = []
    exponent = 0
    while remainder % 2 == 0:
        exponent += 1
        remainder //= 2
    if exponent:
        result.append((2, exponent))
    candidate = 3
    while candidate <= remainder // candidate:
        exponent = 0
        while remainder % candidate == 0:
            exponent += 1
            remainder //= candidate
        if exponent:
            result.append((candidate, exponent))
        candidate += 2
    if remainder > 1:
        result.append((remainder, 1))
    return tuple(result)


def _factorization_wire_v1(factors: tuple[tuple[int, int], ...]) -> list[list[int]]:
    return [[prime, exponent] for prime, exponent in factors]


def _parse_domain_factorization_v1(value: Any) -> tuple[tuple[int, int], ...]:
    if type(value) is not list or not value:
        _reject(
            PrefixCoverageRejectCode.DOMAIN_FACTORIZATION_MISMATCH,
            "gap_three_factorization must be a nonempty JSON array",
        )
    factors: list[tuple[int, int]] = []
    previous = 1
    for index, pair in enumerate(value):
        if type(pair) is not list or len(pair) != 2:
            _reject(
                PrefixCoverageRejectCode.DOMAIN_FACTORIZATION_MISMATCH,
                f"factorization entry {index} must be [prime, exponent]",
            )
        prime, exponent = pair
        if (
            not _plain_int(prime)
            or not _plain_int(exponent)
            or prime <= previous
            or exponent <= 0
            or not _is_prime_by_six_step_v1(prime)
        ):
            _reject(
                PrefixCoverageRejectCode.DOMAIN_FACTORIZATION_MISMATCH,
                f"factorization entry {index} is not a strictly ordered prime power",
            )
        factors.append((prime, exponent))
        previous = prime
    return tuple(factors)


def _validate_domain_v1(value: Any) -> tuple[dict[str, Any], int]:
    domain = _require_exact_dict(value, _DOMAIN_FIELDS, "raw_domain")
    _strict_json_copy(domain)
    if (
        domain["schema_id"] != DOMAIN_SCHEMA_ID
        or not _plain_int(domain["schema_version"])
        or domain["schema_version"] != DOMAIN_SCHEMA_VERSION
    ):
        _reject(
            PrefixCoverageRejectCode.DOMAIN_SCHEMA_MISMATCH,
            "raw domain schema identity/version is invalid",
        )
    integer_fields = (
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
    )
    for name in integer_fields:
        _require_plain_int(domain[name], f"raw_domain.{name}", 0)
    prime = domain["root_context"]
    if prime < 2 or prime % 24 != 1 or not _is_prime_by_six_step_v1(prime):
        _reject(
            PrefixCoverageRejectCode.ROOT_NOT_CORE_PRIME,
            "root_context must be a prime congruent to 1 modulo 24",
        )
    gap_three_x = (prime + 3) // 4
    if not (
        domain["equation_rank"] == prime
        and domain["equation_numerator"] == 4
        and domain["equation_denominator"] == prime
        and domain["gap_three_x"] == gap_three_x
        and domain["mark_root_context"] == prime
        and domain["mark_equation_rank"] == prime
    ):
        _reject(
            PrefixCoverageRejectCode.DOMAIN_ARITHMETIC_MISMATCH,
            "equation, mark, or gap-three arithmetic does not bind the root prime",
        )
    if not (
        domain["q"] == Q_ONE
        and domain["endpoint_fiber_code"] == ENDPOINT_FIBER_G_CODE
        and domain["major_phase_code"] == TYPEII_G_HANDOFF_PHASE_CODE
        and domain["provenance_code"] == ORDINARY_ENDPOINT_PROVENANCE_CODE
        and domain["mark_kind_code"] == ROOT_SOL_MARK_CODE
    ):
        _reject(
            PrefixCoverageRejectCode.Q_ONE_G_DOMAIN_MISMATCH,
            "raw domain is not the exact ordinary q=1 G ROOT_SOL source",
        )
    declared = _parse_domain_factorization_v1(domain["gap_three_factorization"])
    independent = _factor_by_odd_trial_v1(gap_three_x)
    if declared != independent:
        _reject(
            PrefixCoverageRejectCode.DOMAIN_FACTORIZATION_MISMATCH,
            "gap-three factorization does not equal the independent factorization",
        )
    if any(prime_factor % 3 != 1 for prime_factor, _ in declared):
        _reject(
            PrefixCoverageRejectCode.Q_ONE_G_DOMAIN_MISMATCH,
            "ordinary q=1 G requires every gap-three prime factor to be 1 modulo 3",
        )
    product = 1
    for prime_factor, exponent in declared:
        product *= prime_factor**exponent
    if product != gap_three_x:
        _reject(
            PrefixCoverageRejectCode.DOMAIN_FACTORIZATION_MISMATCH,
            "gap-three factorization product is incomplete",
        )
    return _strict_json_copy(domain), prime


def _square_divisors_v1(factors: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    divisors = [1]
    for prime, exponent in factors:
        powers: list[int] = []
        current = 1
        for _ in range(2 * exponent + 1):
            powers.append(current)
            current *= prime
        divisors = [base * power for base in divisors for power in powers]
    divisors.sort()
    expected_count = 1
    for _, exponent in factors:
        expected_count *= 2 * exponent + 1
    if len(divisors) != expected_count or len(set(divisors)) != expected_count:
        _reject(
            PrefixCoverageRejectCode.INTERNAL_RECONSTRUCTION_FAILURE,
            "independent divisor lattice construction is not exhaustive",
        )
    return tuple(divisors)


def _equation_holds_v1(prime: int, x: int, y: int, z: int) -> bool:
    return 4 * x * y * z == prime * (x * y + x * z + y * z)


def _type_i_certificate_v1(
    prime: int, gap: int, x: int, divisor: int, candidate_index: int
) -> dict[str, Any] | None:
    if (prime * x + divisor) % gap:
        return None
    y = (prime * x + divisor) // gap
    numerator = prime * (x + prime * (x * x // divisor))
    if numerator % gap:
        _reject(
            PrefixCoverageRejectCode.INTERNAL_RECONSTRUCTION_FAILURE,
            "a matching Type I divisor did not reconstruct integral z",
        )
    z = numerator // gap
    if not (
        0 < x <= y <= z
        and y % prime != 0
        and z % prime == 0
        and _equation_holds_v1(prime, x, y, z)
    ):
        _reject(
            PrefixCoverageRejectCode.INTERNAL_RECONSTRUCTION_FAILURE,
            "a matching Type I divisor failed the root equation or type split",
        )
    return {
        "certificate_type": "TYPE_I",
        "gap": gap,
        "x": x,
        "divisor": divisor,
        "y": y,
        "z": z,
        "candidate_index": candidate_index,
    }


def _type_ii_certificate_v1(
    prime: int, gap: int, x: int, divisor: int, candidate_index: int
) -> dict[str, Any] | None:
    if divisor > x or (x + divisor) % gap:
        return None
    y = prime * (x + divisor) // gap
    numerator = prime * (x + x * x // divisor)
    if numerator % gap:
        _reject(
            PrefixCoverageRejectCode.INTERNAL_RECONSTRUCTION_FAILURE,
            "a matching Type II divisor did not reconstruct integral z",
        )
    z = numerator // gap
    if not (
        0 < x <= y <= z
        and y % prime == 0
        and z % prime == 0
        and _equation_holds_v1(prime, x, y, z)
    ):
        _reject(
            PrefixCoverageRejectCode.INTERNAL_RECONSTRUCTION_FAILURE,
            "a matching Type II divisor failed the root equation or type split",
        )
    return {
        "certificate_type": "TYPE_II",
        "gap": gap,
        "x": x,
        "divisor": divisor,
        "y": y,
        "z": z,
        "candidate_index": candidate_index,
    }


def _rebuild_gap_scan_v1(prime: int, gap: int) -> dict[str, Any]:
    if gap not in ORDERED_GAPS or (prime + gap) % 4:
        _reject(
            PrefixCoverageRejectCode.INTERNAL_RECONSTRUCTION_FAILURE,
            "requested gap is outside the canonical registered prefix",
        )
    x = (prime + gap) // 4
    factors = _factor_by_odd_trial_v1(x)
    divisors = _square_divisors_v1(factors)
    if not divisors or divisors[0] != 1 or divisors[-1] != x * x:
        _reject(
            PrefixCoverageRejectCode.INTERNAL_RECONSTRUCTION_FAILURE,
            "divisor universe does not span 1 through x squared",
        )
    matches: list[dict[str, Any]] = []
    for divisor_index, divisor in enumerate(divisors):
        if x * x % divisor:
            _reject(
                PrefixCoverageRejectCode.INTERNAL_RECONSTRUCTION_FAILURE,
                "divisor universe contains a non-divisor",
            )
        type_i = _type_i_certificate_v1(
            prime, gap, x, divisor, 2 * divisor_index
        )
        if type_i is not None:
            matches.append(type_i)
        type_ii = _type_ii_certificate_v1(
            prime, gap, x, divisor, 2 * divisor_index + 1
        )
        if type_ii is not None:
            matches.append(type_ii)
    unsigned = {
        "gap": gap,
        "x": x,
        "factorization": _factorization_wire_v1(factors),
        "divisor_universe": list(divisors),
        "matching_certificates": matches,
        "scan_status": GAP_HAS_TERMINAL if matches else GAP_PREFIX_MISS,
    }
    return {**unsigned, "scan_digest": _canonical_digest_v1(unsigned)}


def _rebuild_expected_wire_v1(domain: dict[str, Any], prime: int) -> dict[str, Any]:
    scans = [_rebuild_gap_scan_v1(prime, gap) for gap in ORDERED_GAPS]
    selected: dict[str, Any] | None = None
    for scan in scans:
        matches = scan["matching_certificates"]
        if matches:
            selected = _strict_json_copy(matches[0])
            break
    unsigned = {
        "schema_id": EVIDENCE_SCHEMA_ID,
        "schema_version": EVIDENCE_SCHEMA_VERSION,
        "status": ROOT_TERMINAL_HIT if selected is not None else PREFIX_MISS_EVIDENCE_ONLY,
        "schedule_id": SCHEDULE_ID,
        "domain_input_digest": _canonical_digest_v1(domain),
        "root_context": prime,
        "ordered_gaps": list(ORDERED_GAPS),
        "candidate_order": CANDIDATE_ORDER,
        "gap_scans": scans,
        "selected_terminal": selected,
        "coverage_scope": COVERAGE_SCOPE,
        "global_exhaustion": False,
        "next_unchecked_gap": NEXT_UNCHECKED_GAP,
        "terminal_authority": BLOCKED,
        "role_authority": BLOCKED,
        "issuance_allowed": False,
    }
    return {**unsigned, "digest": _canonical_digest_v1(unsigned)}


def _validate_certificate_wire_shape_v1(value: Any, location: str) -> dict[str, Any]:
    certificate = _require_exact_dict(value, _CERTIFICATE_FIELDS, location)
    certificate_type = _require_text(
        certificate["certificate_type"], f"{location}.certificate_type"
    )
    if certificate_type not in ("TYPE_I", "TYPE_II"):
        _reject(
            PrefixCoverageRejectCode.CERTIFICATE_MISMATCH,
            f"{location}.certificate_type is invalid",
        )
    for name in ("gap", "x", "divisor", "y", "z", "candidate_index"):
        _require_plain_int(certificate[name], f"{location}.{name}", 0)
    if certificate["divisor"] < 1 or certificate["x"] < 1:
        _reject(
            PrefixCoverageRejectCode.CERTIFICATE_MISMATCH,
            f"{location} contains a nonpositive divisor or x",
        )
    return certificate


def _validate_factorization_wire_shape_v1(value: Any, location: str) -> None:
    if type(value) is not list or not value:
        _reject(
            PrefixCoverageRejectCode.FACTORIZATION_MISMATCH,
            f"{location} must be a nonempty JSON array",
        )
    previous = 1
    for index, pair in enumerate(value):
        if type(pair) is not list or len(pair) != 2:
            _reject(
                PrefixCoverageRejectCode.FACTORIZATION_MISMATCH,
                f"{location}[{index}] must be [prime, exponent]",
            )
        prime, exponent = pair
        if (
            not _plain_int(prime)
            or not _plain_int(exponent)
            or prime <= previous
            or exponent <= 0
        ):
            _reject(
                PrefixCoverageRejectCode.FACTORIZATION_MISMATCH,
                f"{location}[{index}] is malformed or unordered",
            )
        previous = prime


def _validate_scan_wire_shape_v1(value: Any, index: int) -> dict[str, Any]:
    location = f"scheduler_evidence.gap_scans[{index}]"
    scan = _require_exact_dict(value, _SCAN_FIELDS, location)
    _require_plain_int(scan["gap"], f"{location}.gap", 3)
    _require_plain_int(scan["x"], f"{location}.x", 1)
    _validate_factorization_wire_shape_v1(scan["factorization"], f"{location}.factorization")
    divisors = scan["divisor_universe"]
    if type(divisors) is not list or not divisors:
        _reject(
            PrefixCoverageRejectCode.DIVISOR_UNIVERSE_MISMATCH,
            f"{location}.divisor_universe must be nonempty",
        )
    for divisor_index, divisor in enumerate(divisors):
        _require_plain_int(divisor, f"{location}.divisor_universe[{divisor_index}]", 1)
    if divisors != sorted(divisors) or len(divisors) != len(set(divisors)):
        _reject(
            PrefixCoverageRejectCode.DIVISOR_UNIVERSE_MISMATCH,
            f"{location}.divisor_universe must be strictly increasing",
        )
    certificates = scan["matching_certificates"]
    if type(certificates) is not list:
        _reject(
            PrefixCoverageRejectCode.CERTIFICATE_MISMATCH,
            f"{location}.matching_certificates must be a JSON array",
        )
    for certificate_index, certificate in enumerate(certificates):
        _validate_certificate_wire_shape_v1(
            certificate, f"{location}.matching_certificates[{certificate_index}]"
        )
    scan_status = _require_text(scan["scan_status"], f"{location}.scan_status")
    if scan_status not in (GAP_HAS_TERMINAL, GAP_PREFIX_MISS):
        _reject(
            PrefixCoverageRejectCode.SCAN_STATUS_MISMATCH,
            f"{location}.scan_status is invalid",
        )
    _require_digest(scan["scan_digest"], f"{location}.scan_digest")
    return scan


def _validate_evidence_wire_shape_v1(value: Any) -> dict[str, Any]:
    evidence = _require_exact_dict(value, _EVIDENCE_FIELDS, "scheduler_evidence")
    _strict_json_copy(evidence)
    if (
        evidence["schema_id"] != EVIDENCE_SCHEMA_ID
        or not _plain_int(evidence["schema_version"])
        or evidence["schema_version"] != EVIDENCE_SCHEMA_VERSION
    ):
        _reject(
            PrefixCoverageRejectCode.EVIDENCE_SCHEMA_MISMATCH,
            "scheduler evidence schema identity/version is invalid",
        )
    _require_text(evidence["status"], "scheduler_evidence.status")
    _require_text(evidence["schedule_id"], "scheduler_evidence.schedule_id")
    _require_digest(evidence["domain_input_digest"], "scheduler_evidence.domain_input_digest")
    _require_plain_int(evidence["root_context"], "scheduler_evidence.root_context", 2)
    if type(evidence["ordered_gaps"]) is not list:
        _reject(
            PrefixCoverageRejectCode.GAP_ORDER_MISMATCH,
            "ordered_gaps must be a JSON array",
        )
    for index, gap in enumerate(evidence["ordered_gaps"]):
        _require_plain_int(gap, f"scheduler_evidence.ordered_gaps[{index}]", 3)
    _require_text(evidence["candidate_order"], "scheduler_evidence.candidate_order")
    scans = evidence["gap_scans"]
    if type(scans) is not list:
        _reject(
            PrefixCoverageRejectCode.GAP_ORDER_MISMATCH,
            "gap_scans must be a JSON array",
        )
    for index, scan in enumerate(scans):
        _validate_scan_wire_shape_v1(scan, index)
    selected = evidence["selected_terminal"]
    if selected is not None:
        _validate_certificate_wire_shape_v1(
            selected, "scheduler_evidence.selected_terminal"
        )
    _require_text(evidence["coverage_scope"], "scheduler_evidence.coverage_scope")
    _require_exact_bool(
        evidence["global_exhaustion"], False, "global_exhaustion"
    )
    _require_plain_int(
        evidence["next_unchecked_gap"], "scheduler_evidence.next_unchecked_gap", 3
    )
    if evidence["terminal_authority"] != BLOCKED or evidence["role_authority"] != BLOCKED:
        _reject(
            PrefixCoverageRejectCode.AUTHORITY_FORBIDDEN,
            "terminal_authority and role_authority must both remain BLOCKED",
        )
    _require_exact_bool(evidence["issuance_allowed"], False, "issuance_allowed")
    _require_digest(evidence["digest"], "scheduler_evidence.digest")
    return evidence


def _compare_scans_v1(actual_scans: list[Any], expected_scans: list[Any]) -> None:
    if len(actual_scans) != len(expected_scans):
        _reject(
            PrefixCoverageRejectCode.GAP_ORDER_MISMATCH,
            "gap scan count differs from the registered prefix",
        )
    for index, (actual, expected) in enumerate(zip(actual_scans, expected_scans, strict=True)):
        if actual["gap"] != expected["gap"] or actual["x"] != expected["x"]:
            _reject(
                PrefixCoverageRejectCode.GAP_ORDER_MISMATCH,
                f"gap scan {index} does not bind the canonical gap/x",
            )
        if actual["factorization"] != expected["factorization"]:
            _reject(
                PrefixCoverageRejectCode.FACTORIZATION_MISMATCH,
                f"gap scan {index} factorization differs from independent replay",
            )
        if actual["divisor_universe"] != expected["divisor_universe"]:
            _reject(
                PrefixCoverageRejectCode.DIVISOR_UNIVERSE_MISMATCH,
                f"gap scan {index} divisor universe differs from independent replay",
            )
        if actual["matching_certificates"] != expected["matching_certificates"]:
            _reject(
                PrefixCoverageRejectCode.CERTIFICATE_MISMATCH,
                f"gap scan {index} matching certificate list differs from replay",
            )
        if actual["scan_status"] != expected["scan_status"]:
            _reject(
                PrefixCoverageRejectCode.SCAN_STATUS_MISMATCH,
                f"gap scan {index} status differs from its certificate list",
            )
        unsigned = {key: actual[key] for key in actual if key != "scan_digest"}
        if actual["scan_digest"] != _canonical_digest_v1(unsigned):
            _reject(
                PrefixCoverageRejectCode.SCAN_DIGEST_MISMATCH,
                f"gap scan {index} digest does not replay its supplied payload",
            )
        if actual["scan_digest"] != expected["scan_digest"]:
            _reject(
                PrefixCoverageRejectCode.SCAN_DIGEST_MISMATCH,
                f"gap scan {index} digest differs from independent replay",
            )


@dataclass(frozen=True, slots=True)
class PrefixCoverageVerificationV1:
    """Non-authorizing DTO returned only after full replay by the public verifier."""

    status: str
    evidence_digest: str
    outcome: str
    root_context: int
    global_exhaustion: bool
    terminal_authority: str
    role_authority: str
    issuance_allowed: bool

    def __post_init__(self) -> None:
        if not (
            self.status == VERIFIED_STATUS
            and type(self.evidence_digest) is str
            and _DIGEST_RE.fullmatch(self.evidence_digest) is not None
            and type(self.outcome) is str
            and self.outcome in (ROOT_TERMINAL_HIT, PREFIX_MISS_EVIDENCE_ONLY)
            and _plain_int(self.root_context)
            and self.root_context >= 2
            and self.global_exhaustion is False
            and self.terminal_authority == BLOCKED
            and self.role_authority == BLOCKED
            and self.issuance_allowed is False
        ):
            _reject(
                PrefixCoverageRejectCode.OUTPUT_INVARIANT_MISMATCH,
                "PrefixCoverageVerificationV1 must remain evidence-only",
            )


def verify_q_one_priority_prefix_coverage_v1(
    raw_domain: Any, scheduler_evidence: Any
) -> PrefixCoverageVerificationV1:
    """Independently replay the exact gaps-3/7/11 scheduler evidence wire."""

    domain, prime = _validate_domain_v1(raw_domain)
    actual = _validate_evidence_wire_shape_v1(scheduler_evidence)
    expected = _rebuild_expected_wire_v1(domain, prime)

    if actual["domain_input_digest"] != expected["domain_input_digest"]:
        _reject(
            PrefixCoverageRejectCode.DOMAIN_BINDING_MISMATCH,
            "scheduler evidence is not bound to the exact raw domain",
        )
    if actual["root_context"] != prime:
        _reject(
            PrefixCoverageRejectCode.DOMAIN_BINDING_MISMATCH,
            "scheduler evidence root_context differs from the raw domain",
        )
    if actual["schedule_id"] != SCHEDULE_ID or actual["coverage_scope"] != COVERAGE_SCOPE:
        _reject(
            PrefixCoverageRejectCode.SCHEDULE_SCOPE_MISMATCH,
            "schedule ID or registered prefix scope changed",
        )
    if actual["ordered_gaps"] != list(ORDERED_GAPS) or actual["next_unchecked_gap"] != NEXT_UNCHECKED_GAP:
        _reject(
            PrefixCoverageRejectCode.GAP_ORDER_MISMATCH,
            "ordered gaps or next unchecked gap changed",
        )
    if actual["candidate_order"] != CANDIDATE_ORDER:
        _reject(
            PrefixCoverageRejectCode.CANDIDATE_ORDER_MISMATCH,
            "candidate precedence changed",
        )

    _compare_scans_v1(actual["gap_scans"], expected["gap_scans"])

    if actual["selected_terminal"] != expected["selected_terminal"]:
        _reject(
            PrefixCoverageRejectCode.SELECTED_TERMINAL_MISMATCH,
            "selected terminal is not the first canonical matching certificate",
        )
    if actual["status"] != expected["status"]:
        _reject(
            PrefixCoverageRejectCode.OUTCOME_MISMATCH,
            "outer status disagrees with the independently reconstructed scans",
        )
    unsigned_actual = {key: actual[key] for key in actual if key != "digest"}
    if actual["digest"] != _canonical_digest_v1(unsigned_actual):
        _reject(
            PrefixCoverageRejectCode.OUTER_DIGEST_MISMATCH,
            "outer evidence digest does not replay the supplied payload",
        )
    if actual["digest"] != expected["digest"]:
        _reject(
            PrefixCoverageRejectCode.OUTER_DIGEST_MISMATCH,
            "outer evidence digest differs from independent replay",
        )
    if _canonical_json_v1(actual) != _canonical_json_v1(expected):
        _reject(
            PrefixCoverageRejectCode.WIRE_MISMATCH,
            "scheduler evidence is not byte-identical canonical JSON",
        )

    return PrefixCoverageVerificationV1(
        status=VERIFIED_STATUS,
        evidence_digest=actual["digest"],
        outcome=actual["status"],
        root_context=prime,
        global_exhaustion=False,
        terminal_authority=BLOCKED,
        role_authority=BLOCKED,
        issuance_allowed=False,
    )


__all__ = [
    "BLOCKED",
    "PREFIX_MISS_EVIDENCE_ONLY",
    "PrefixCoverageRejectCode",
    "PrefixCoverageVerificationError",
    "PrefixCoverageVerificationV1",
    "ROOT_TERMINAL_HIT",
    "VERIFIED_STATUS",
    "verify_q_one_priority_prefix_coverage_v1",
]
