#!/usr/bin/env python3
"""Assemble a typed representation-dual-capacity selector receipt.

The input certificates are deliberately kept at their proven boundary.  An
arithmetic predecessor, a quotient Fourier certificate, or a conditional
capacity ledger is never promoted to a recursive edge without E1--E5.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UNIFIED_INPUT = ROOT / "reproductions" / "type-i-unified-terminal-selector-results.json"
FOURIER_INPUT = ROOT / "reproductions" / "type-i-fixed-layer-stabilizer-fourier-results.json"
QADIC_INPUT = ROOT / "reproductions" / "type-i-overflow-qadic-obstruction-transfer-results.json"
PHASE_INPUT = ROOT / "reproductions" / "type-i-overflow-defect-unit-phase-capacity-results.json"
OVERFLOW_INPUT = ROOT / "reproductions" / "type-i-universal-anchor-overflow-dual-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-representation-dual-capacity-selector-results.json"

SELECTOR_ORDER = [
    "direct_type_i_or_type_ii",
    "target_fiber_neighbor_terminal",
    "generalized_dyadic_terminal",
    "fixed_layer_quotient_fourier",
    "overflow_fixed_n_charged_support",
    "overflow_qadic_phase_capacity",
]

STATUS_LATTICE = [
    "terminal_leaf",
    "analysis_evidence",
    "candidate_transition",
    "verified_edge",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def factorization(value: int) -> list[list[int]]:
    if value <= 0:
        raise AssertionError("factorization requires a positive integer")
    result: list[list[int]] = []
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            result.append([divisor, exponent])
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result.append([value, 1])
    return result


def source_hashes() -> dict[str, str]:
    return {
        UNIFIED_INPUT.name: sha256(UNIFIED_INPUT),
        FOURIER_INPUT.name: sha256(FOURIER_INPUT),
        QADIC_INPUT.name: sha256(QADIC_INPUT),
        PHASE_INPUT.name: sha256(PHASE_INPUT),
        OVERFLOW_INPUT.name: sha256(OVERFLOW_INPUT),
    }


def check_status_boundary(receipt: dict[str, object]) -> None:
    status = receipt.get("selector_status")
    if status not in STATUS_LATTICE:
        raise AssertionError(f"unknown selector status: {status}")
    edge_eligible = receipt.get("recursive_edge_eligible")
    if not isinstance(edge_eligible, bool):
        raise AssertionError("recursive_edge_eligible must be boolean")
    if status == "verified_edge":
        checks = receipt.get("e1_e5")
        if checks != {f"E{i}": True for i in range(1, 6)}:
            raise AssertionError("verified edge lacks complete E1-E5 witness")
        if not edge_eligible:
            raise AssertionError("verified edge must be recursively eligible")
    elif edge_eligible:
        raise AssertionError("non-verified receipt cannot be recursive")


def state_receipt(receipt: dict[str, object], source_name: str) -> dict[str, object]:
    certificate_type = receipt.get("certificate_type")
    if certificate_type not in {
        "target_fiber_neighbor_terminal",
        "generalized_dyadic_terminal",
        "fixed_layer_quotient_fourier",
    }:
        raise AssertionError(f"unexpected unified receipt: {certificate_type}")
    prime = int(receipt["prime"])
    modulus = int(receipt["R"] if "R" in receipt else receipt["quotient_order"])
    K = int(receipt["K"])
    state_descriptor = {
        "equation_target": [4, prime],
        "modulus": modulus,
        "K": K,
        "certificate_type": certificate_type,
    }
    state_id = "state:" + canonical_hash(state_descriptor)

    if certificate_type == "fixed_layer_quotient_fourier":
        target_fiber = {
            "status": "empty",
            "separating_character": {
                "quotient_order": int(receipt["quotient_order"]),
                "character_order": int(receipt["character_order"]),
                "character_amplitude_squared": int(receipt["amplitude_squared"]),
            },
        }
        marked_set = {"status": "empty", "source": "fixed_layer_quotient"}
        signed_defect = {"status": "not_applicable"}
        branch_phase = "DUAL_CERTIFICATE"
        proof_boundary = "state_internal_dual_only"
    elif certificate_type == "target_fiber_neighbor_terminal":
        target_fiber = {
            "status": "nonempty",
            "witness": receipt["near_pair"],
            "witness_type": "coordinate_budget_near_pair",
        }
        marked_set = {"status": "not_carried", "source": "terminal_first"}
        signed_defect = {"status": "not_carried", "source": "terminal_first"}
        branch_phase = "TERMINAL_FIRST"
        proof_boundary = "arithmetic_terminal_only"
    else:
        target_fiber = {
            "status": "nonempty_source_profile",
            "source": "target-fiber-hit-profile",
            "witness_type": "generalized_dyadic_pair",
        }
        marked_set = {"status": "not_carried", "source": "terminal_first"}
        signed_defect = {"status": "not_carried", "source": "terminal_first"}
        branch_phase = "TERMINAL_FIRST"
        proof_boundary = "arithmetic_terminal_only"

    result = {
        "state_id": state_id,
        "state_descriptor": state_descriptor,
        "equation_target": {"numerator": 4, "denominator": prime},
        "modulus_context": {
            "R": modulus,
            "identity": "4K=pR+1",
            "type": "Type_I",
        },
        "K_context": {
            "K": K,
            "factorization": factorization(K),
        },
        "marked_solution_set": marked_set,
        "induction_rank": {"status": "not_assigned", "reason": "no recursive edge"},
        "target_fiber": target_fiber,
        "signed_defect": signed_defect,
        "certificate_context": {
            "certificate_type": certificate_type,
            "source": source_name,
            "phase": branch_phase,
            "proof_boundary": proof_boundary,
        },
        "normal_form": "type-I-terminal-first",
        "potential_record": {
            "status": "absent",
            "reason": "E1-E5 lift and strict potential decrease are not proved",
        },
        "selected_branch": certificate_type,
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "e1_e5": {f"E{i}": False for i in range(1, 6)},
        "proof_boundary": proof_boundary,
        "source_receipt": receipt,
    }
    check_status_boundary(result)
    return result


def capacity_receipt(qadic: dict[str, object], phase: dict[str, object]) -> dict[str, object]:
    if phase.get("input_sha256") != sha256(QADIC_INPUT):
        raise AssertionError("phase audit is stale relative to q-adic ledger")
    summary = {
        key: phase[key]
        for key in (
            "obstruction_row_count",
            "q_group_count",
            "phase_cell_count",
            "non_singleton_cell_count",
            "compatible_pair_count",
            "pair_count",
            "capacity_overload_cell_count",
        )
    }
    if summary["capacity_overload_cell_count"] != 0:
        raise AssertionError("focused capacity audit unexpectedly contains an overload")
    ledger = {
        key: qadic[key]
        for key in (
            "case_count",
            "dual_channel_count",
            "q_layer_row_count",
            "channels_with_obstruction",
            "obstruction_prime_power_rows",
        )
    }
    descriptor = {
        "family": "pn=4Md+1",
        "qadic_ledger": ledger,
        "phase_summary": summary,
    }
    result = {
        "state_id": "family:" + canonical_hash(descriptor),
        "scope": "cross_state_overflow_audit",
        "equation_target": {"relation": "pn=4Md+1"},
        "certificate_context": {
            "certificate_type": "overflow_qadic_phase_capacity",
            "phase": "CAPACITY_AUDIT",
            "carrier_mapping_status": "unproved",
            "proof_boundary": "conditional_phase_compatibility_only",
        },
        "overflow_defect_ledger": ledger,
        "phase_capacity_summary": summary,
        "selected_branch": "overflow_qadic_phase_capacity",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "e1_e5": {f"E{i}": False for i in range(1, 6)},
        "scope_note": (
            "The obstruction units are not assumed to be the phases of an alternate. "
            "No capacity overload or recursive edge is inferred."
        ),
    }
    check_status_boundary(result)
    return result


def verified_fixed_n_edge(payload: dict[str, object]) -> dict[str, object]:
    """Recompute one genuine fixed-n identity-lift edge.

    The selected receipt is deliberately a positive control for the status
    lattice: it has old support A=5, the smallest admissible L=125, and all
    five state-contract checks are arithmetic identities.
    """
    overflow_dual = payload.get("overflow_dual")
    if not isinstance(overflow_dual, dict):
        raise AssertionError("overflow dual payload shape changed")
    case = overflow_dual.get("accumulated_positive_fixed_n_edge")
    if not isinstance(case, dict):
        raise AssertionError("fixed-n positive control missing")
    overflow = case.get("overflow")
    window = case.get("window")
    if not isinstance(overflow, dict) or not isinstance(window, dict):
        raise AssertionError("fixed-n receipt shape changed")

    prime = int(case["prime"])
    support = int(case["A"])
    M = int(overflow["M"])
    R_M = int(overflow["R_M"])
    K_M = int(overflow["K_M"])
    C = int(overflow["C"])
    n = int(overflow["n"])
    d = int(overflow["d"])
    S = M * d
    if not (
        prime == 409
        and support == 5
        and M == 250
        and R_M > prime
        and K_M == M * C
        and prime * n == 4 * M * d + 1
        and M > support
        and 4 * S == prime * n - 1
    ):
        raise AssertionError("fixed-n positive control changed")

    candidates = window.get("support_preserving_candidates")
    if not isinstance(candidates, list) or not candidates:
        raise AssertionError("fixed-n positive control lost its window")
    candidate = min(candidates, key=lambda row: int(row["L"]))
    L = int(candidate["L"])
    R_L = int(candidate["R_L"])
    K_L = int(candidate["K_L"])
    if not (
        L == 125
        and L > support
        and S % L == 0
        and n < 4 * L < prime + n
        and R_L == 4 * L - n
        and K_L == L * (prime - S // L)
        and 3 <= R_L <= prime - 2
        and 4 * K_L == prime * R_L + 1
        and K_L % L == 0
    ):
        raise AssertionError("fixed-n candidate arithmetic changed")

    B_prime = (prime - 1) ** 2 // 4
    source_potential = B_prime // support
    successor_potential = B_prime // L
    if not successor_potential < source_potential:
        raise AssertionError("fixed-n support potential did not decrease")

    source_descriptor = {
        "equation_target": [4, prime],
        "R": R_M,
        "K": K_M,
        "absorbed_support": support,
    }
    successor_descriptor = {
        "equation_target": [4, prime],
        "R": R_L,
        "K": K_L,
        "absorbed_support": L,
    }
    checks = {f"E{i}": True for i in range(1, 6)}
    result = {
        "edge_id": "edge:" + canonical_hash(
            {"source": source_descriptor, "successor": successor_descriptor}
        ),
        "source_state_id": "state:" + canonical_hash(source_descriptor),
        "successor_state_id": "state:" + canonical_hash(successor_descriptor),
        "certificate_type": "overflow_fixed_n_charged_support",
        "phase": "OVERFLOW_DETERMINANT",
        "state_class": "overflow",
        "source_state": source_descriptor,
        "successor_state": successor_descriptor,
        "equation_target": {"numerator": 4, "denominator": prime},
        "marked_solution_set": {
            "source": "Sol(p)",
            "successor": "Sol(p)",
            "lift": "identity",
        },
        "target_fiber": {
            "status": "inherited_full_solution_set",
            "reason": "identity-lift edge does not require a new target-fiber witness",
        },
        "signed_defect": {"status": "not_applicable", "reason": "identity lift"},
        "certificate_context": {
            "source": OVERFLOW_INPUT.name,
            "provenance": "overflow_determinant_fixed_n",
            "determinant": {"pn": prime * n, "four_M_d_plus_1": 4 * M * d + 1},
            "selected_candidate": {"L": L, "R_L": R_L, "K_L": K_L},
        },
        "normal_form": "overflow_fixed_n_charged_support_v1",
        "induction_rank": {
            "kind": "absorbed_support_potential",
            "source": source_potential,
            "successor": successor_potential,
        },
        "potential_record": {
            "B_p": B_prime,
            "source_support": support,
            "successor_support": L,
            "source_value": source_potential,
            "successor_value": successor_potential,
            "strict_decrease": True,
        },
        "e1_e5": checks,
        "selector_status": "verified_edge",
        "recursive_edge_eligible": True,
        "lift_status": "proved_identity",
        "proof_boundary": "fixed_n_identity_lift",
        "scope_note": (
            "This is one verified fixed-n edge; it does not imply that every A>1 overflow "
            "has a nonempty fixed-n window."
        ),
    }
    check_status_boundary(result)
    return result


def build_results() -> dict[str, object]:
    unified = json.loads(UNIFIED_INPUT.read_text(encoding="utf-8"))
    overflow = json.loads(OVERFLOW_INPUT.read_text(encoding="utf-8"))
    qadic = json.loads(QADIC_INPUT.read_text(encoding="utf-8"))
    phase = json.loads(PHASE_INPUT.read_text(encoding="utf-8"))
    fourier_payload = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    fourier_receipt = fourier_payload["receipt"]
    if unified.get("selector_order") != SELECTOR_ORDER[:4]:
        raise AssertionError("unified selector order changed")
    receipts = unified.get("receipts")
    if not isinstance(receipts, list) or len(receipts) != 3:
        raise AssertionError("expected three unified receipts")
    normalized_receipts: list[dict[str, object]] = []
    for receipt in receipts:
        normalized = dict(receipt)
        if normalized.get("certificate_type") == "fixed_layer_quotient_fourier":
            for key in ("prime", "R", "K"):
                normalized[key] = fourier_receipt[key]
        normalized_receipts.append(normalized)
    states = [state_receipt(receipt, UNIFIED_INPUT.name) for receipt in normalized_receipts]
    verified_edge = verified_fixed_n_edge(overflow)
    capacity = capacity_receipt(qadic, phase)
    return {
        "schema_version": 1,
        "arithmetic": "Typed dispatch for the representation-dual-capacity selector.",
        "selector_order": SELECTOR_ORDER,
        "status_lattice": STATUS_LATTICE,
        "states": states,
        "verified_edges": [verified_edge],
        "capacity_receipts": [capacity],
        "invariants": {
            "analysis_evidence_never_recursive": True,
            "verified_edge_requires_E1_E5": True,
            "terminal_leaf_requires_direct_certificate": True,
            "overflow_phase_requires_explicit_cross_state_mapping": True,
        },
        "source_sha256": source_hashes(),
        "scope_note": (
            "This receipt unifies state-local representation, dual, and capacity evidence. "
            "It contains one verified fixed-n identity-lift edge, but does not prove universal "
            "branch existence or well-founded descent for all overflow states."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build_results(), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.verify:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("stored selector result does not match regenerated output")
        print("verified", args.output)
        return
    args.output.write_text(rendered, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
