#!/usr/bin/env python3
"""Verify the T6-F3 proper-root v1 routing partition.

The program checks the domain predicates, fixed precedence, seven-way residual
partition, and the machine-readable no-active-serializer boundary.  Its local
fixtures are contract-shape controls only; they are not evidence that an actual
persistent proper-root state exists.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, replace
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "data" / "t6-f3-proper-root-routing-v1.json"
FRONTIER_PATH = ROOT / "data" / "t6-proof-frontier-v2.json"

ACTUAL_PERSISTENT = "ACTUAL_PERSISTENT"
TERMINAL_HIT = "HIT"
TERMINAL_MISS = "MISS"

RESIDUAL_CODES = (
    "HIGH_ENDPOINT_RESIDUAL",
    "R1_M3_Q5_PATH_UNBOUND",
    "R2_M3_Q5_PATH_BOUND_NO_SERIALIZER",
    "R3_M3_NONQ5_QUOTIENT_ONLY",
    "R4_M3_NONQ5_H_SUPPORTED",
    "R5_MGT3_QUOTIENT_ONLY",
    "R6_MGT3_H_SUPPORTED",
)


class RoutingContractError(ValueError):
    """Raised when a header is outside the v1 routing contract."""


@dataclass(frozen=True)
class ReceiptRoutingHeaderV1:
    """The routing header consumed after the arithmetic receipt was verified.

    The digest fields bind this header to an upstream active receipt.  This
    class does not manufacture or independently prove that receipt.
    """

    source_class: str
    state_id: str
    producer_id: str
    admission_id: str
    source_path_digest: str
    terminal_first_digest: str
    maximal_receipt_digest: str
    arithmetic_receipt_verified: bool
    p: int
    r: int
    h: int
    m: int | None
    k: int | None
    d_star: int | None
    terminal_first_status: str
    terminal_certificate_id: str | None = None
    raw_path_bound: bool = False
    active_serializer_id: str | None = None


def load_spec() -> dict[str, object]:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


def is_prime(value: int) -> bool:
    """Return primality by exact trial division for focused controls."""

    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def proper_factor_root(p: int, h: int) -> bool:
    """Check the weak proper-divisor meaning of proper root."""

    if p % 3 != 1 or h <= 0 or h % 3:
        return False
    m_zero = (p * p + p + 1) // 3
    u = h // 3
    return 0 < u < m_zero and m_zero % u == 0


def strict_proper_height(p: int, h: int) -> bool:
    """Check the low proper-height subdomain used by current k theorems."""

    return 2 <= h < p


def root_height_matches_r(p: int, r: int, h: int) -> bool:
    """Check h=3*gcd(2r+1,M0) for the actual root-height header."""

    if p % 3 != 1 or r < 0:
        return False
    m_zero = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, m_zero)
    return 0 < u < m_zero and h == 3 * u


def factorization(value: int) -> dict[int, int]:
    if value < 1:
        raise RoutingContractError("factorization expects a positive integer")
    result: dict[int, int] = {}
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def quotient_only_part(k: int, h: int) -> int:
    """Return the part of k supported on primes not dividing h."""

    result = 1
    for prime, exponent in factorization(k).items():
        if h % prime:
            result *= prime**exponent
    return result


def least_prime_factor(value: int) -> int:
    factors = factorization(value)
    if not factors:
        raise RoutingContractError("no prime factor for one")
    return min(factors)


def domain_errors(header: ReceiptRoutingHeaderV1) -> list[str]:
    errors: list[str] = []
    if header.source_class != ACTUAL_PERSISTENT:
        errors.append("SOURCE_NOT_ACTUAL_PERSISTENT")
    for name in (
        "state_id",
        "producer_id",
        "admission_id",
        "source_path_digest",
        "terminal_first_digest",
        "maximal_receipt_digest",
    ):
        if not getattr(header, name):
            errors.append(f"MISSING_{name.upper()}")
    if not header.arithmetic_receipt_verified:
        errors.append("ARITHMETIC_RECEIPT_NOT_VERIFIED")
    if not (is_prime(header.p) and header.p % 24 == 1):
        errors.append("P_NOT_CORE_PRIME")
    if not proper_factor_root(header.p, header.h):
        errors.append("NOT_PROPER_FACTOR_ROOT")
    if not root_height_matches_r(header.p, header.r, header.h):
        errors.append("ROOT_HEIGHT_RECEIPT_MISMATCH")
    if not (header.h > header.p or strict_proper_height(header.p, header.h)):
        errors.append("HEIGHT_PARTITION_FAILED")
    if strict_proper_height(header.p, header.h):
        if header.m is None:
            errors.append("LOW_HEIGHT_M_MISSING")
        elif header.m < 3:
            errors.append("M_BELOW_ACTUAL_STUTTER_BOUND")
        if header.k is None:
            errors.append("LOW_HEIGHT_K_MISSING")
        elif header.k < 1:
            errors.append("K_NOT_POSITIVE")
        if header.d_star is None:
            errors.append("LOW_HEIGHT_D_STAR_MISSING")
        elif header.d_star <= 1:
            errors.append("D_STAR_NOT_NONTRIVIAL")
    if header.terminal_first_status not in {TERMINAL_HIT, TERMINAL_MISS}:
        errors.append("INVALID_TERMINAL_FIRST_STATUS")
    if (
        header.terminal_first_status == TERMINAL_HIT
        and not header.terminal_certificate_id
    ):
        errors.append("TERMINAL_HIT_WITHOUT_CERTIFICATE")
    if (
        header.terminal_first_status == TERMINAL_MISS
        and header.terminal_certificate_id is not None
    ):
        errors.append("TERMINAL_MISS_WITH_CERTIFICATE")
    return errors


def residual_predicates(
    header: ReceiptRoutingHeaderV1,
) -> dict[str, bool]:
    if not strict_proper_height(header.p, header.h):
        raise RoutingContractError("low residual predicates used outside low height")
    if header.m is None or header.k is None or header.d_star is None:
        raise RoutingContractError("low residual payload is incomplete")
    k_perp = quotient_only_part(header.k, header.h)
    m_is_three = header.m == 3
    q5 = header.d_star % 5 == 0
    quotient_only = k_perp > 1
    return {
        "R1_M3_Q5_PATH_UNBOUND": (
            m_is_three and q5 and not header.raw_path_bound
        ),
        "R2_M3_Q5_PATH_BOUND_NO_SERIALIZER": (
            m_is_three and q5 and header.raw_path_bound
        ),
        "R3_M3_NONQ5_QUOTIENT_ONLY": (
            m_is_three and not q5 and quotient_only
        ),
        "R4_M3_NONQ5_H_SUPPORTED": (
            m_is_three and not q5 and not quotient_only
        ),
        "R5_MGT3_QUOTIENT_ONLY": (
            not m_is_three and quotient_only
        ),
        "R6_MGT3_H_SUPPORTED": (
            not m_is_three and not quotient_only
        ),
    }


def active_serializer_kind(
    serializer_id: str, spec: dict[str, object]
) -> str | None:
    registry = spec["active_physical_serializers"]
    if not isinstance(registry, dict):
        raise RoutingContractError("invalid serializer registry")
    for kind in ("QC1", "TR1"):
        entries = registry.get(kind)
        if not isinstance(entries, list):
            raise RoutingContractError(f"invalid {kind} serializer list")
        if serializer_id in entries:
            return kind
    return None


def route(
    header: ReceiptRoutingHeaderV1,
    spec: dict[str, object] | None = None,
) -> dict[str, object]:
    """Apply the v1 route precedence to one already-bound header."""

    errors = domain_errors(header)
    if errors:
        return {
            "outcome": "OUTSIDE_DOMAIN",
            "errors": errors,
            "active_edge": False,
        }

    if header.terminal_first_status == TERMINAL_HIT:
        return {
            "outcome": "TERMINAL",
            "certificate_id": header.terminal_certificate_id,
            "active_edge": False,
        }

    if header.h > header.p:
        return {
            "outcome": "OPEN_MINIMAL_GAP",
            "route_code": "HIGH_ENDPOINT_RESIDUAL",
            "active_edge": False,
            "active_serializer": None,
            "low_height_payload_consumed": False,
            "low_height_theorems_applicable": False,
        }

    if header.m is None or header.k is None or header.d_star is None:
        raise RoutingContractError("validated low-height payload is missing")

    if header.k == 1:
        return {
            "outcome": "COVERED_EMPTY_THEOREM",
            "route_code": "K_ONE_ACTUAL_EMPTY",
            "actual_instance_consistent": False,
            "active_edge": False,
        }

    if spec is None:
        spec = load_spec()
    if header.active_serializer_id is not None:
        kind = active_serializer_kind(header.active_serializer_id, spec)
        if kind is None:
            raise RoutingContractError(
                "serializer is not active on the v1 physical surface"
            )
        return {
            "outcome": f"{kind}_PHYSICAL_EDGE",
            "serializer_id": header.active_serializer_id,
            "active_edge": True,
        }

    predicates = residual_predicates(header)
    selected = [code for code, matched in predicates.items() if matched]
    if len(selected) != 1:
        raise RoutingContractError(
            f"residual partition selected {len(selected)} branches"
        )

    code = selected[0]
    k_perp = quotient_only_part(header.k, header.h)
    result: dict[str, object] = {
        "outcome": "OPEN_MINIMAL_GAP",
        "route_code": code,
        "active_edge": False,
        "k_perp": k_perp,
        "transverse_prime_candidate": least_prime_factor(header.d_star),
        "active_serializer": None,
    }
    if k_perp > 1:
        result["quotient_only_prime_candidate"] = least_prime_factor(k_perp)
    else:
        result["h_supported_prime_candidate"] = least_prime_factor(header.k)
    if code.startswith(("R1_", "R2_")):
        result["m3_q5_slice"] = True
        result["q5_raw_path_bound"] = header.raw_path_bound
        result["p2_gate_status"] = "OPEN"
    return result


def fixture(**updates: object) -> ReceiptRoutingHeaderV1:
    """Return a contract-shape fixture, never an actualness witness."""

    base = ReceiptRoutingHeaderV1(
        source_class=ACTUAL_PERSISTENT,
        state_id="fixture-state",
        producer_id="fixture-producer",
        admission_id="fixture-admission",
        source_path_digest="fixture-source-path",
        terminal_first_digest="fixture-terminal-first",
        maximal_receipt_digest="fixture-maximal-receipt",
        arithmetic_receipt_verified=True,
        p=73,
        r=1,
        h=3,
        m=3,
        k=5,
        d_star=5,
        terminal_first_status=TERMINAL_MISS,
    )
    return replace(base, **updates)


def verify_spec(spec: dict[str, object]) -> None:
    if spec.get("theorem_status") != "ESTABLISHED_DOMAIN_PARTITION":
        raise AssertionError("domain-partition theorem status changed")
    if spec.get("physicalization_status") != "OPEN_MINIMAL_GAPS":
        raise AssertionError("physicalization boundary changed")
    if spec.get("f3_status") != "OPEN" or spec.get("t6_status") != "OPEN":
        raise AssertionError("F3/T6 was silently upgraded")

    registry = spec.get("active_physical_serializers")
    if registry != {"QC1": [], "TR1": []}:
        raise AssertionError("v1 unexpectedly gained a physical serializer")

    rows = spec.get("residual_families")
    if not isinstance(rows, list):
        raise AssertionError("residual registry is not a list")
    ids = tuple(row["id"] for row in rows)
    if ids != RESIDUAL_CODES:
        raise AssertionError("JSON and implementation residual orders differ")
    if any(row.get("status") != "OPEN_MINIMAL_GAP" for row in rows):
        raise AssertionError("a residual was silently marked closed")

    slice_rows = spec.get("arithmetic_only_slice_tags")
    if not isinstance(slice_rows, list):
        raise AssertionError("slice tag registry is not a list")
    q5 = next(row for row in slice_rows if row["id"] == "M3_Q5_RAW_POLICY_AND_P2_GATE")
    if q5.get("domain") != "LOW_PROPER_HEIGHT":
        raise AssertionError("m=3 q=5 escaped the low-height domain")
    if q5.get("routes_only_to") != list(RESIDUAL_CODES[1:3]):
        raise AssertionError("m=3 q=5 slice escaped its two residuals")
    if q5.get("active_serializer") is not None:
        raise AssertionError("m=3 q=5 acquired an unreviewed serializer")
    if q5.get("p2_gate_status") != "OPEN":
        raise AssertionError("the p^2 gate was silently closed")

    high = rows[0]
    if high.get("id") != "HIGH_ENDPOINT_RESIDUAL":
        raise AssertionError("high endpoint is not the first residual")
    if high.get("active_serializer") is not None:
        raise AssertionError("high endpoint acquired an unreviewed serializer")
    forbidden = high.get("forbidden_low_height_inferences")
    if not isinstance(forbidden, list) or len(forbidden) < 4:
        raise AssertionError("high endpoint lacks low-theorem firewalls")

    frontier = json.loads(FRONTIER_PATH.read_text(encoding="utf-8"))
    theorems = frontier.get("frontier_theorems")
    if not isinstance(theorems, list):
        raise AssertionError("active T6 frontier theorem list is missing")
    f3 = next(
        row
        for row in theorems
        if row.get("id") == "T6-F3-PROPER-ROOT-PHYSICALIZATION"
    )
    if f3.get("status") != "OPEN":
        raise AssertionError("active T6 frontier no longer records F3 as open")
    if frontier.get("current_status") != "OPEN":
        raise AssertionError("active T6 frontier was silently upgraded")


def verify_partition(spec: dict[str, object]) -> dict[str, str]:
    controls = {
        "HIGH_ENDPOINT_RESIDUAL": fixture(
            p=313, r=90, h=543, m=None, k=None, d_star=None
        ),
        "R1_M3_Q5_PATH_UNBOUND": fixture(),
        "R2_M3_Q5_PATH_BOUND_NO_SERIALIZER": fixture(raw_path_bound=True),
        "R3_M3_NONQ5_QUOTIENT_ONLY": fixture(d_star=7),
        "R4_M3_NONQ5_H_SUPPORTED": fixture(d_star=7, k=3),
        "R5_MGT3_QUOTIENT_ONLY": fixture(m=4, d_star=7),
        "R6_MGT3_H_SUPPORTED": fixture(m=4, d_star=7, k=3),
    }
    observed: dict[str, str] = {}
    for expected, header in controls.items():
        if expected != "HIGH_ENDPOINT_RESIDUAL":
            predicates = residual_predicates(header)
            if sum(predicates.values()) != 1:
                raise AssertionError("low residual predicates are not a partition")
        result = route(header, spec)
        if result.get("route_code") != expected:
            raise AssertionError(f"expected {expected}, got {result}")
        if result.get("active_edge") is not False:
            raise AssertionError("a residual fixture became an active edge")
        observed[expected] = str(result["outcome"])
    return observed


def verify_precedence(spec: dict[str, object]) -> None:
    terminal = fixture(
        p=313,
        r=90,
        h=543,
        m=None,
        k=None,
        d_star=None,
        terminal_first_status=TERMINAL_HIT,
        terminal_certificate_id="fixture-terminal-certificate",
        active_serializer_id="not-active-and-must-not-be-read",
    )
    if route(terminal, spec).get("outcome") != "TERMINAL":
        raise AssertionError("terminal-first no longer preempts serializer routing")

    k_one = fixture(k=1, d_star=7)
    result = route(k_one, spec)
    if result.get("route_code") != "K_ONE_ACTUAL_EMPTY":
        raise AssertionError("k=1 empty theorem lost precedence")

    try:
        route(fixture(active_serializer_id="unregistered-qc1"), spec)
    except RoutingContractError:
        pass
    else:  # pragma: no cover - negative control
        raise AssertionError("unregistered serializer did not fail closed")

    high = fixture(
        p=313,
        r=90,
        h=543,
        m=None,
        k=1,
        d_star=None,
        active_serializer_id="must-not-be-read-on-high",
    )
    if not proper_factor_root(high.p, high.h):
        raise AssertionError("weak proper-factor fixture changed")
    if strict_proper_height(high.p, high.h):
        raise AssertionError("the two meanings of proper collapsed")
    high_result = route(high, spec)
    if high_result.get("route_code") != "HIGH_ENDPOINT_RESIDUAL":
        raise AssertionError("high endpoint was dropped or sent through low k")
    if high_result.get("low_height_payload_consumed") is not False:
        raise AssertionError("high endpoint consumed low-height payload")


def run() -> dict[str, object]:
    spec = load_spec()
    verify_spec(spec)
    observed = verify_partition(spec)
    verify_precedence(spec)
    return {
        "theorem": "type-I-t6-f3-proper-root-routing-with-explicit-residuals",
        "status": "ESTABLISHED_DOMAIN_PARTITION",
        "physicalization": "OPEN_MINIMAL_GAPS",
        "residual_controls": observed,
        "fixtures_are_actual_receipt_evidence": False,
        "active_physical_serializers": {"QC1": [], "TR1": []},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.verify:
        print("verified F3 proper-factor domain and seven-way open residual partition")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
