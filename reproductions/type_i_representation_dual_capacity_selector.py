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
QADIC_INPUT = ROOT / "reproductions" / "type-i-overflow-qadic-obstruction-transfer-results.json"
PHASE_INPUT = ROOT / "reproductions" / "type-i-overflow-defect-unit-phase-capacity-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-representation-dual-capacity-selector-results.json"

SELECTOR_ORDER = [
    "direct_type_i_or_type_ii",
    "target_fiber_neighbor_terminal",
    "generalized_dyadic_terminal",
    "fixed_layer_quotient_fourier",
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
        QADIC_INPUT.name: sha256(QADIC_INPUT),
        PHASE_INPUT.name: sha256(PHASE_INPUT),
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


def build_results() -> dict[str, object]:
    unified = json.loads(UNIFIED_INPUT.read_text(encoding="utf-8"))
    qadic = json.loads(QADIC_INPUT.read_text(encoding="utf-8"))
    phase = json.loads(PHASE_INPUT.read_text(encoding="utf-8"))
    fourier_source = ROOT / "reproductions" / "type-i-fixed-layer-stabilizer-fourier-results.json"
    fourier_payload = json.loads(fourier_source.read_text(encoding="utf-8"))
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
    capacity = capacity_receipt(qadic, phase)
    return {
        "schema_version": 1,
        "arithmetic": "Typed dispatch for the representation-dual-capacity selector.",
        "selector_order": SELECTOR_ORDER,
        "status_lattice": STATUS_LATTICE,
        "states": states,
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
            "It does not prove universal branch existence, marked lifting, or well-founded descent."
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
