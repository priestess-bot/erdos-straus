#!/usr/bin/env python3
"""Build the R3/R5 quotient-only QC1 arithmetic candidate.

The universal proof is in the accompanying claim.  This module checks the
deterministic arithmetic, materializes an Eisenstein-prime *ideal* factor,
and checks the proposed target shape.  The ideal factor is not an integer raw
complete-excess occurrence and cannot pay E1 or support conservation.  The
local check calls only the frozen family predicates; it does not construct a
producer rule, terminal receipt, persistent state, or common admission.  Fixed
controls never manufacture an ACTUAL_PERSISTENT proper-root state.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from dataclasses import asdict, dataclass
from math import gcd, isqrt
from pathlib import Path
import sys
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "scripts" / "t6_persistent_selector_state_v1.py"
SPEC = importlib.util.spec_from_file_location(
    "t6_persistent_selector_state_v1_for_f3_qc1", CONTRACT_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {CONTRACT_PATH}")
CONTRACT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = CONTRACT
SPEC.loader.exec_module(CONTRACT)


ADAPTER_ID = "f3_qc1_quotient_only_physical_transition_v1"
SOURCE_BINDING_SCHEMA = "f3_qc1_source_binding_v1"
TARGET_OWNER = "type_i_a_gt_one_overflow_residual"
SOURCE_OWNER = "proper_root_stutter_k_gt_one"
R3 = "R3_M3_NONQ5_QUOTIENT_ONLY"
R5 = "R5_MGT3_QUOTIENT_ONLY"
BRANCH_BY_RESIDUAL = {R3: "r3_qc1_target", R5: "r5_qc1_target"}


class QC1ContractError(ValueError):
    """A stable failure of the track-local candidate contract."""


@dataclass(frozen=True)
class QuotientOnlySourceV1:
    evidence_class: str
    state_id: str
    source_producer_id: str
    source_admission_id: str
    source_path_digest: str
    source_receipt_digest: str
    terminal_first_digest: str
    maximal_receipt_digest: str
    p: int
    r: int
    h: int
    m: int
    k: int
    d_star: int
    support: int
    chart_R: int
    chart_K: int
    source_binding_receipt: Mapping[str, object] | None = None


def canonical_digest(payload: object) -> str:
    return CONTRACT.canonical_digest_v1(payload)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def factorization(value: int) -> dict[int, int]:
    if value < 1:
        raise QC1ContractError("factorization requires a positive integer")
    factors: dict[int, int] = {}
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = 1
    return factors


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def quotient_only_part(k: int, h: int) -> int:
    result = 1
    for prime, exponent in factorization(k).items():
        if h % prime:
            result *= prime**exponent
    return result


def canonical_q_perp(k: int, h: int) -> int:
    """Return min{q prime: q|k and q does not divide h}."""

    candidates = [prime for prime in factorization(k) if h % prime]
    if not candidates:
        raise QC1ContractError("K_PERP_ONE")
    return min(candidates)


def residual_id(source: QuotientOnlySourceV1) -> str:
    if source.m == 3 and source.d_star % 5:
        return R3
    if source.m > 3:
        return R5
    raise QC1ContractError("SOURCE_OUTSIDE_R3_R5")


def source_binding_receipt(
    source: QuotientOnlySourceV1, *, status: str
) -> dict[str, object]:
    """Seal control fields; this receipt does not authenticate actualness."""

    core = {
        "schema_id": SOURCE_BINDING_SCHEMA,
        "schema_version": 1,
        "status": status,
        "evidence_class": source.evidence_class,
        "state_id": source.state_id,
        "source_producer_id": source.source_producer_id,
        "source_admission_id": source.source_admission_id,
        "source_path_digest": source.source_path_digest,
        "source_receipt_digest": source.source_receipt_digest,
        "terminal_first_digest": source.terminal_first_digest,
        "maximal_receipt_digest": source.maximal_receipt_digest,
        "p": source.p,
        "r": source.r,
        "h": source.h,
        "m": source.m,
        "k": source.k,
        "d_star": source.d_star,
        "support": source.support,
        "chart_R": source.chart_R,
        "chart_K": source.chart_K,
    }
    return {**core, "digest": canonical_digest(core)}


def verify_source_binding(source: QuotientOnlySourceV1) -> None:
    receipt = source.source_binding_receipt
    if not isinstance(receipt, Mapping):
        raise QC1ContractError("SOURCE_BINDING_RECEIPT_MISSING")
    payload = dict(receipt)
    digest = payload.pop("digest", None)
    if digest != canonical_digest(payload):
        raise QC1ContractError("SOURCE_BINDING_RECEIPT_DIGEST_MISMATCH")
    expected_status = (
        "VERIFIED_ACTUAL_PERSISTENT_SOURCE"
        if source.evidence_class == "ACTUAL_PERSISTENT"
        else "CONTROL_ONLY_NOT_ACTUAL"
    )
    expected = source_binding_receipt(source, status=expected_status)
    if dict(receipt) != expected:
        raise QC1ContractError("SOURCE_BINDING_RECEIPT_FIELD_MISMATCH")
    if source.evidence_class == "ACTUAL_PERSISTENT" and not is_prime(source.p):
        raise QC1ContractError("ACTUAL_SOURCE_P_NOT_PRIME")
    if source.evidence_class == "ACTUAL_PERSISTENT":
        raise QC1ContractError("ACTUAL_SOURCE_RUNTIME_REPLAY_NOT_IMPLEMENTED")


def rebuild_source(source: QuotientOnlySourceV1) -> dict[str, int | str]:
    """Recompute the proper-root arithmetic used by the ideal factor."""

    verify_source_binding(source)
    p, r, h, m, k = source.p, source.r, source.h, source.m, source.k
    if not (
        source.evidence_class
        in {"ACTUAL_PERSISTENT", "CONTRACT_SHAPE_CONTROL_NOT_ACTUAL"}
        and source.state_id
        and source.source_producer_id
        and source.source_admission_id
        and source.source_path_digest
        and source.source_receipt_digest
        and source.terminal_first_digest
        and source.maximal_receipt_digest
        and p % 24 == 1
        and r >= 1
        and 2 <= h < p
        and m >= 3
        and k > 1
        and source.d_star > 1
    ):
        raise QC1ContractError("SOURCE_HEADER_INVALID")

    m_zero = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, m_zero)
    D = m * p + 1 - h
    if D <= 0 or (p * h + 1) % D:
        raise QC1ContractError("STUTTER_DIVISOR_INVALID")
    e = (p * h + 1) // D
    a = e * m - h
    b = e - 1
    norm = a * a - a * b + b * b

    g = (p + 1) // 2
    T = p * p * r - g
    support = g * T
    chart_K = support * (p - 1)
    chart_R_numerator = 4 * chart_K - 1
    if chart_R_numerator % p:
        raise QC1ContractError("SOURCE_CHART_NOT_INTEGRAL")
    chart_R = chart_R_numerator // p

    if not (
        h == 3 * u
        and 0 < u < m_zero
        and m_zero % u == 0
        and a > 0
        and b > 0
        and p * a + b == e * h
        and norm == h * k
        and source.support == support
        and source.chart_R == chart_R
        and source.chart_K == chart_K
        and source.chart_K % source.support == 0
        and 4 * source.chart_K == p * source.chart_R + 1
        and 4 * k < p
        and quotient_only_part(k, h) > 1
    ):
        raise QC1ContractError("SOURCE_ARITHMETIC_DID_NOT_REPLAY")

    selected_residual = residual_id(source)
    expected_d_star = D // gcd(D, h * h - 1)
    if source.d_star != expected_d_star:
        raise QC1ContractError("D_STAR_RECEIPT_MISMATCH")
    return {
        "residual_id": selected_residual,
        "M0": m_zero,
        "u": u,
        "D": D,
        "e": e,
        "a": a,
        "b": b,
        "norm": norm,
        "support": support,
        "chart_R": chart_R,
        "chart_K": chart_K,
        "B_p": (p - 1) ** 2 // 4,
    }


def quotient_ideal_factor(
    source: QuotientOnlySourceV1, arithmetic: Mapping[str, int | str]
) -> dict[str, object]:
    """Bind q_perp to an oriented ideal factor of a-b*omega.

    This is stronger than recording q_perp|k.  The factor records the
    unique root lambda modulo q for which the source Eisenstein element
    beta=a-b*omega vanishes, while its conjugate evaluation is nonzero.
    """

    q = canonical_q_perp(source.k, source.h)
    a, b = int(arithmetic["a"]), int(arithmetic["b"])
    if q >= source.p or source.h % q == 0 or source.k % q:
        raise QC1ContractError("Q_PERP_DOMAIN_INVALID")
    # This is an algebraic factor of a norm.  It is not, by itself, an integer
    # side occurrence in the source raw path and never pays E1.
    actual_occurrence_bound = False
    if a % q == 0 or b % q == 0:
        raise QC1ContractError("QUOTIENT_FACTOR_NOT_PRIMITIVE")
    root = a * pow(b, -1, q) % q
    conjugate_root = (1 - root) % q
    if not (
        is_prime(q)
        and q >= 7
        and q % 3 == 1
        and (root * root - root + 1) % q == 0
        and (a - b * root) % q == 0
        and (a - b * conjugate_root) % q != 0
    ):
        raise QC1ContractError("ORIENTED_EISENSTEIN_OCCURRENCE_FAILED")

    core = {
        "schema_id": "qc1_eisenstein_ideal_factor_v1",
        "schema_version": 1,
        "source_state_id": source.state_id,
        "source_producer_id": source.source_producer_id,
        "source_admission_id": source.source_admission_id,
        "source_path_digest": source.source_path_digest,
        "source_receipt_digest": source.source_receipt_digest,
        "terminal_first_digest": source.terminal_first_digest,
        "maximal_receipt_digest": source.maximal_receipt_digest,
        "residual_id": arithmetic["residual_id"],
        "selection_rule": "least_prime_dividing_k_not_h",
        "q_perp": q,
        "q_exponent_in_k": valuation(source.k, q),
        "oriented_ideal_multiplicity": valuation(source.k, q),
        "proposed_charge_multiplicity": 1,
        "source_element": {"ring": "Z[omega], omega^2-omega+1=0", "a": a, "b": b},
        "oriented_prime_ideal": {
            "notation": "(q_perp,omega-lambda)",
            "lambda": root,
            "conjugate_lambda": conjugate_root,
            "norm": q,
            "source_evaluation_zero": True,
            "conjugate_evaluation_nonzero": True,
        },
        "height_cancellation_excluded": source.h % q != 0,
        "actual_integer_raw_occurrence_bound": actual_occurrence_bound,
        "integer_raw_occurrence_status": "UNPROVED",
        "support_charge_conservation_status": "UNPROVED",
        "binding_rule": (
            "derive the oriented ideal factor from the provided source tuple; "
            "actual runtime replay is not authenticated here"
        ),
    }
    return {**core, "factor_id": "qc1factor:" + canonical_digest(core)}


def target_arithmetic(
    source: QuotientOnlySourceV1,
    arithmetic: Mapping[str, int | str],
    ideal_factor: Mapping[str, object],
) -> dict[str, object]:
    """Construct the conditional support-A*q_perp target shape."""

    p = source.p
    q = int(ideal_factor["q_perp"])
    source_support = int(arithmetic["support"])
    B_p = int(arithmetic["B_p"])
    target_support = source_support * q
    capacity = (-pow(q, -1, p)) % p
    target_K = target_support * capacity
    numerator = 4 * target_K - 1
    if numerator % p:
        raise QC1ContractError("QC1_TARGET_NOT_INTEGRAL")
    target_R = numerator // p
    target_d = p - capacity
    target_n = 4 * target_support - target_R

    if not (
        source_support > B_p
        and q < p // 4
        and q >= 7
        and target_support > source_support
        and 1 <= capacity <= p - 2
        and target_R > p
        and target_R % 4 == 3
        and target_R < 4 * target_support
        and p * target_R + 1 == 4 * target_K
        and target_K % target_support == 0
        and target_d > 0
        and target_n > 0
        and p * target_n == 4 * target_support * target_d + 1
    ):
        raise QC1ContractError("QC1_TARGET_OR_ANCHOR_FAILED")

    source_rank = [p, 2, 4, 0, p - 1, 0, 0]
    target_rank = [p, 2, 4, 0, capacity, 0, 0]
    if not target_rank < source_rank:
        raise QC1ContractError("QC1_N7_DID_NOT_DECREASE")
    return {
        "support": target_support,
        "capacity": capacity,
        "R": target_R,
        "K": target_K,
        "d": target_d,
        "n": target_n,
        "source_rank_N7": source_rank,
        "target_rank_N7": target_rank,
    }


def target_facts(source: QuotientOnlySourceV1, target: Mapping[str, object]) -> dict[str, object]:
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
        "provenance_kind": "OVERFLOW",
        "full_carrier_scope": False,
        "atomic_arm": "NONE",
        "dispatch_status": "NONE",
        "proper_root_k": None,
        "proper_root_height_class": "NONE",
        "proper_root_height": None,
        "is_overflow": True,
        "support_A": int(target["support"]),
        "carrier_M": int(target["support"]),
        "overflow_d": int(target["d"]),
        "chart_R": int(target["R"]),
        "chart_K": int(target["K"]),
        "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }


def classify_target_shape_control(
    source: QuotientOnlySourceV1,
    target: Mapping[str, object],
) -> tuple[dict[str, object], Any]:
    """Classify facts only; this is neither serialization nor admission."""

    selected_residual = residual_id(source)
    facts = target_facts(source, target)
    header = CONTRACT.VerifiedSelectorHeaderV1(
        state_id="shape-control-not-a-state",
        queue_gate=CONTRACT.ADMITTED_SUCCESSOR,
        producer_id=ADAPTER_ID,
        branch_id=BRANCH_BY_RESIDUAL[selected_residual],
        parent_state_id=source.state_id,
        root_context=source.p,
        equation_rank=source.p,
        mark_kind=CONTRACT.ROOT_SOL,
        mark_receipt_digest="NOT_REPLAYED_SHAPE_CONTROL",
        terminal_first_digest="NOT_REPLAYED_SHAPE_CONTROL",
        source_receipt_digest="NOT_REPLAYED_SHAPE_CONTROL",
        facts_digest=canonical_digest(facts),
        facts=facts,
    )
    classification = CONTRACT.classify_selector_owner_v1(header)
    if classification.owner != TARGET_OWNER:
        raise QC1ContractError("TARGET_SHAPE_OWNER_CHANGED")
    return facts, classification


def build_transition(source: QuotientOnlySourceV1) -> dict[str, object]:
    arithmetic = rebuild_source(source)
    ideal_factor = quotient_ideal_factor(source, arithmetic)
    target = target_arithmetic(source, arithmetic, ideal_factor)
    facts, classification = classify_target_shape_control(source, target)
    return {
        "adapter_id": ADAPTER_ID,
        "evidence_class": source.evidence_class,
        "source": asdict(source),
        "source_arithmetic": dict(arithmetic),
        "ideal_factor": ideal_factor,
        "target_arithmetic": target,
        "target_shape_control": {
            "classification_only": True,
            "facts": facts,
            "owner": classification.owner,
            "matched_families": list(classification.matched_families),
            "owner_digest": classification.owner_digest,
        },
        "E1": {
            "algebraic_oriented_ideal_factor": True,
            "path_bound_integer_raw_occurrence": False,
            "support_charge_conservation": False,
            "complete": False,
        },
        "E2": True,
        "E3": "TARGET_SHAPE_ONLY_COMMON_RUNTIME_NOT_REPLAYED",
        "E4": "CONDITIONAL_ON_REAL_SOURCE_MARK_AND_SCOPE_REPLAY",
        "E5": "ARITHMETIC_N7_DROP_CONDITIONAL_ON_E1_E4_AND_FINAL_ADMISSION",
        "T5_ticket": None,
        "recursive_edge_eligible": False,
        "proof_boundary": (
            "The stored control is not actual evidence.  On an ACTUAL_PERSISTENT "
            "source the arithmetic formulas remain valid, but E1 needs a path-bound "
            "integer occurrence and charge-conservation theorem.  Activation also "
            "requires real source/mark replay, coordinator producer registration, "
            "and the common target terminal-first result."
        ),
    }


def control_source() -> QuotientOnlySourceV1:
    """Return a core-congruent nonprime control; never actual evidence."""

    p, r, h, m, k = 54_481, 2_543_533_812, 12_063, 13, 61
    g = (p + 1) // 2
    support = g * (p * p * r - g)
    chart_K = support * (p - 1)
    chart_R = (4 * chart_K - 1) // p
    D = m * p + 1 - h
    d_star = D // gcd(D, h * h - 1)
    source = QuotientOnlySourceV1(
        evidence_class="CONTRACT_SHAPE_CONTROL_NOT_ACTUAL",
        state_id="control:core-congruent-nonprime-r5",
        source_producer_id="control-proper-root-producer",
        source_admission_id="control-proper-root-admission",
        source_path_digest="control-proper-root-path",
        source_receipt_digest="control-source-receipt",
        terminal_first_digest="control-terminal-first",
        maximal_receipt_digest="control-maximal-receipt-not-actual",
        p=p,
        r=r,
        h=h,
        m=m,
        k=k,
        d_star=d_star,
        support=support,
        chart_R=chart_R,
        chart_K=chart_K,
    )
    receipt = source_binding_receipt(source, status="CONTROL_ONLY_NOT_ACTUAL")
    return QuotientOnlySourceV1(
        **{**asdict(source), "source_binding_receipt": receipt}
    )


def raw_side_nonimplication_control() -> dict[str, int]:
    """Show that the norm factor alone does not locate a stutter-side factor."""

    source = control_source()
    arithmetic = rebuild_source(source)
    q = canonical_q_perp(source.k, source.h)
    z = source.chart_R - source.h
    D = int(arithmetic["D"])
    E = z // D
    values = {"z": z, "D": D, "E": E, "K": source.chart_K}
    if not (
        int(arithmetic["norm"]) == source.h * source.k
        and source.k % q == 0
        and all(valuation(value, q) == 0 for value in values.values())
    ):
        raise AssertionError("QC1 norm-to-stutter-side boundary changed")
    return {"q_perp": q, **{f"v_{name}": valuation(value, q) for name, value in values.items()}}


def verify() -> dict[str, object]:
    source = control_source()
    if is_prime(source.p):
        raise AssertionError("the focused control unexpectedly became prime")
    result = build_transition(source)
    ideal_factor = result["ideal_factor"]
    target = result["target_arithmetic"]
    if not (
        result["source_arithmetic"]["residual_id"] == R5
        and ideal_factor["q_perp"] == 61
        and ideal_factor["oriented_prime_ideal"]["lambda"] == 14
        and target["capacity"] == (-pow(61, -1, source.p)) % source.p
        and target["target_rank_N7"] < target["source_rank_N7"]
        and result["target_shape_control"]["owner"] == TARGET_OWNER
        and result["target_shape_control"]["matched_families"] == [TARGET_OWNER]
        and result["E1"]["complete"] is False
        and result["recursive_edge_eligible"] is False
    ):
        raise AssertionError("focused QC1 quotient-only transition changed")
    nonimplication = raw_side_nonimplication_control()
    if nonimplication != {"q_perp": 61, "v_z": 0, "v_D": 0, "v_E": 0, "v_K": 0}:
        raise AssertionError("QC1 raw-side nonimplication control changed")

    for bad_source in (
        QuotientOnlySourceV1(**{**asdict(source), "k": source.h}),
        QuotientOnlySourceV1(**{**asdict(source), "m": 3, "d_star": 5}),
    ):
        try:
            build_transition(bad_source)
        except QC1ContractError:
            pass
        else:  # pragma: no cover
            raise AssertionError("an out-of-scope quotient source was accepted")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = verify()
    if args.verify:
        print(
            "verified QC1 algebraic ideal factor and conditional target shape; "
            "integer occurrence, E1, and runtime admission remain open"
        )
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
