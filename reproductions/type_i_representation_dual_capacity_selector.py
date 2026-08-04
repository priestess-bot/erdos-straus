#!/usr/bin/env python3
"""Assemble a typed representation-dual-capacity selector receipt.

The input certificates are deliberately kept at their proven boundary.  An
arithmetic predecessor, a quotient Fourier certificate, or a conditional
capacity ledger is never promoted to a recursive edge without E1--E5.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd, lcm
from pathlib import Path

try:
    from fixed_layer_quotient_fourier import cyclic_quotient_fourier_profile
except ModuleNotFoundError:
    from reproductions.fixed_layer_quotient_fourier import cyclic_quotient_fourier_profile


ROOT = Path(__file__).resolve().parents[1]
UNIFIED_INPUT = ROOT / "reproductions" / "type-i-unified-terminal-selector-results.json"
FOURIER_INPUT = ROOT / "reproductions" / "type-i-fixed-layer-stabilizer-fourier-results.json"
BOUNDED_FOURIER_CAPACITY_INPUT = (
    ROOT / "reproductions" / "type-i-f-bounded-fourier-carrier-capacity-results.json"
)
BOUNDED_FOURIER_CERTIFICATE_INPUT = (
    ROOT / "reproductions" / "type-i-f-bounded-fourier-certificate-results.json"
)
BOUNDED_FOURIER_SOURCE = (
    ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
)
QADIC_INPUT = ROOT / "reproductions" / "type-i-overflow-qadic-obstruction-transfer-results.json"
PHASE_INPUT = ROOT / "reproductions" / "type-i-overflow-defect-unit-phase-capacity-results.json"
OVERFLOW_INPUT = ROOT / "reproductions" / "type-i-universal-anchor-overflow-dual-results.json"
UNIVERSAL_ANCHOR_INPUT = OVERFLOW_INPUT
BOTTOM_WORD_CAPACITY_INPUT = (
    ROOT / "reproductions" / "type-i-bottom-word-lattice-pareto-cycle-capacity-results.json"
)
BOTTOM_WORD_CAPACITY_SOURCE = (
    ROOT / "reproductions" / "type_i_bottom_word_lattice_pareto_cycle_capacity.py"
)
BOTTOM_WORD_CLOSURE_SOURCE = (
    ROOT / "reproductions" / "type_i_f_psi_one_formal_transition_closure.py"
)
SOURCE_WORD_CAPACITY_INPUT = (
    ROOT / "reproductions" / "type-i-source-word-joint-capacity-dichotomy-results.json"
)
SOURCE_WORD_FROZEN_INPUT = (
    ROOT / "reproductions" / "type-i-psi-one-full-spectrum-terminal-descent-audit-results.json"
)
LARGE_SLAB_CAPACITY_INPUT = (
    ROOT / "reproductions" / "type-i-large-slab-factor-pair-layer-capacity-results.json"
)
LARGE_SLAB_CAPACITY_SOURCE = (
    ROOT / "reproductions" / "type_i_large_slab_factor_pair_layer_capacity.py"
)
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-representation-dual-capacity-selector-results.json"

SELECTOR_ORDER = [
    "direct_type_i_or_type_ii",
    "target_fiber_neighbor_terminal",
    "generalized_dyadic_terminal",
    "fixed_layer_quotient_fourier",
    "overflow_high_carrier_p_plus_four_complement",
    "bounded_fourier_carrier_capacity",
    "overflow_fixed_n_charged_support",
    "overflow_fixed_n_outer_rank_reset",
    "overflow_fixed_n_bounded_divisor_outer_rank",
    "overflow_same_chart_support_promotion",
    "overflow_a_one_generic_determinant_boundary",
    "overflow_fixed_s_outer_rank_reset",
    "overflow_fixed_s_bounded_divisor_outer_rank",
    "overflow_outer_rank_reset",
    "overflow_hard_core_gap_obstruction",
    "overflow_phase_reset_cycle_boundary",
    "overflow_qadic_phase_capacity",
    "overflow_support_debt_phase_bridge",
    "overflow_d_one_p_minus_two_g_rechart",
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


def divisors(value: int) -> list[int]:
    if value <= 0:
        raise AssertionError("divisors require a positive integer")
    result = [1]
    for prime, exponent in factorization(value):
        old = tuple(result)
        power = 1
        for _ in range(exponent):
            power *= prime
            result.extend(item * power for item in old)
    return sorted(result)


def valuation(value: int, prime: int) -> int:
    if value <= 0 or prime <= 1:
        raise AssertionError("valuation arguments must be positive")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def jacobi_symbol(numerator: int, denominator: int) -> int:
    """Return the Jacobi symbol using exact integer reciprocity steps."""
    if denominator <= 0 or denominator % 2 == 0:
        raise AssertionError("Jacobi denominator must be positive and odd")
    numerator %= denominator
    result = 1
    while numerator:
        while numerator % 2 == 0:
            numerator //= 2
            if denominator % 8 in (3, 5):
                result = -result
        numerator, denominator = denominator, numerator
        if numerator % 4 == denominator % 4 == 3:
            result = -result
        numerator %= denominator
    return result if denominator == 1 else 0


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    if prime <= 1 or support <= 0:
        raise AssertionError("canonical chart arguments must be positive")
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    K = (prime * R + 1) // 4
    if not 1 <= R < modulus or K % support:
        raise AssertionError("canonical chart normalization changed")
    return R, K


def source_hashes() -> dict[str, str]:
    return {
        UNIFIED_INPUT.name: sha256(UNIFIED_INPUT),
        FOURIER_INPUT.name: sha256(FOURIER_INPUT),
        BOUNDED_FOURIER_CAPACITY_INPUT.name: sha256(BOUNDED_FOURIER_CAPACITY_INPUT),
        BOUNDED_FOURIER_CERTIFICATE_INPUT.name: sha256(BOUNDED_FOURIER_CERTIFICATE_INPUT),
        BOUNDED_FOURIER_SOURCE.name: sha256(BOUNDED_FOURIER_SOURCE),
        QADIC_INPUT.name: sha256(QADIC_INPUT),
        PHASE_INPUT.name: sha256(PHASE_INPUT),
        OVERFLOW_INPUT.name: sha256(OVERFLOW_INPUT),
        BOTTOM_WORD_CAPACITY_INPUT.name: sha256(BOTTOM_WORD_CAPACITY_INPUT),
        BOTTOM_WORD_CAPACITY_SOURCE.name: sha256(BOTTOM_WORD_CAPACITY_SOURCE),
        BOTTOM_WORD_CLOSURE_SOURCE.name: sha256(BOTTOM_WORD_CLOSURE_SOURCE),
        SOURCE_WORD_CAPACITY_INPUT.name: sha256(SOURCE_WORD_CAPACITY_INPUT),
        SOURCE_WORD_FROZEN_INPUT.name: sha256(SOURCE_WORD_FROZEN_INPUT),
        LARGE_SLAB_CAPACITY_INPUT.name: sha256(LARGE_SLAB_CAPACITY_INPUT),
        LARGE_SLAB_CAPACITY_SOURCE.name: sha256(LARGE_SLAB_CAPACITY_SOURCE),
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
        generic_profile = receipt.get("generic_spectrum_profile")
        if not isinstance(generic_profile, dict):
            raise AssertionError("fixed-layer receipt lacks generic cyclic spectrum")
        residual_block = receipt.get("residual_block")
        if not isinstance(residual_block, dict):
            raise AssertionError("fixed-layer receipt lacks residual block")
        expected_profile = cyclic_quotient_fourier_profile(
            modulus=modulus,
            group={int(value) for value in receipt["H"]},
            fixed_layer={int(value) for value in receipt["J"]},
            residual_blocks=[
                (int(residual_block["prime"]), int(residual_block["exponent"]))
            ],
            target=int(receipt["target"]),
        )
        if expected_profile != generic_profile:
            raise AssertionError("stored generic cyclic spectrum is stale")
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
        proof_boundary = "state_internal_exact_fourier_only"
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
    if certificate_type == "fixed_layer_quotient_fourier":
        profile = receipt["generic_spectrum_profile"]
        result["certificate_context"]["cyclic_spectrum_profile"] = {
            "quotient_order": profile["quotient_order"],
            "target_count": profile["target_count"],
            "total_representation_count": profile["total_representation_count"],
            "parseval_nontrivial_energy": profile["parseval_nontrivial_energy"],
            "threshold_amplitude_fraction": profile["threshold_amplitude_fraction"],
            "threshold_amplitude_squared_fraction": profile[
                "threshold_amplitude_squared_fraction"
            ],
            "canonical_profile_policy": profile["canonical_profile_policy"],
            "q_primary_projection_rule": profile["q_primary_projection_rule"],
            "qadic_phase_bridge": profile["qadic_phase_bridge"],
            "carrier_mapping_status": profile["carrier_mapping_status"],
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


def bounded_fourier_capacity_receipt(payload: dict[str, object]) -> dict[str, object]:
    """Attach the finite bounded-Fourier carrier audit to the typed selector.

    The audit has already reconstructed the real linear blocks and checked the
    q-adic capacity inequalities.  This wrapper only makes that evidence
    content-addressed and keeps its non-recursive proof boundary explicit.
    """
    if payload.get("input") != BOUNDED_FOURIER_CERTIFICATE_INPUT.name:
        raise AssertionError("bounded-Fourier capacity input name changed")
    if payload.get("input_sha256") != sha256(BOUNDED_FOURIER_CERTIFICATE_INPUT):
        raise AssertionError("bounded-Fourier certificate input is stale")
    if payload.get("source_script") != BOUNDED_FOURIER_SOURCE.name:
        raise AssertionError("bounded-Fourier source name changed")
    if payload.get("source_sha256") != sha256(BOUNDED_FOURIER_SOURCE):
        raise AssertionError("bounded-Fourier source is stale")
    certificate_payload = json.loads(
        BOUNDED_FOURIER_CERTIFICATE_INPUT.read_text(encoding="utf-8")
    )
    if certificate_payload.get("state_count") != 45:
        raise AssertionError("bounded-Fourier certificate state count changed")
    dual_coordinate_box = certificate_payload.get("dual_coordinate_box")
    target_phase_filter = certificate_payload.get("target_phase_filter")
    if dual_coordinate_box != [-1, 1] or target_phase_filter != "nonintegral":
        raise AssertionError("bounded-Fourier canonical selection rule changed")

    expected_counts = {
        "state_count": 45,
        "direction_count": 141,
    }
    for key, expected in expected_counts.items():
        if payload.get(key) != expected:
            raise AssertionError(f"bounded-Fourier {key} changed")
    audit = payload.get("audit")
    if not isinstance(audit, dict):
        raise AssertionError("bounded-Fourier audit is missing")
    expected_families = {
        "same_color": {
            "group_count": 113,
            "non_singleton_group_count": 15,
            "pair_check_count": 50,
        },
        "mixed_color": {
            "group_count": 100,
            "non_singleton_group_count": 21,
            "pair_check_count": 78,
        },
    }
    family_summary: dict[str, dict[str, object]] = {}
    for family_name, expected in expected_families.items():
        family = audit.get(family_name)
        if not isinstance(family, dict):
            raise AssertionError(f"bounded-Fourier {family_name} summary is missing")
        for key, expected_value in expected.items():
            if family.get(key) != expected_value:
                raise AssertionError(f"bounded-Fourier {family_name}.{key} changed")
        if family.get("divisibility_failure_count") != 0:
            raise AssertionError(f"bounded-Fourier {family_name} has a divisibility failure")
        if family.get("capacity_violation_count") != 0:
            raise AssertionError(f"bounded-Fourier {family_name} has a capacity violation")
        family_summary[family_name] = {
            key: family[key]
            for key in (
                "group_count",
                "non_singleton_group_count",
                "pair_check_count",
                "divisibility_failure_count",
                "capacity_violation_count",
                "max_non_singleton_capacity_ratio",
            )
        }

    descriptor = {
        "family": "frozen_bounded_fourier_carrier_capacity",
        "state_count": expected_counts["state_count"],
        "direction_count": expected_counts["direction_count"],
        "input_sha256": payload["input_sha256"],
    }
    result = {
        "state_id": "family:" + canonical_hash(descriptor),
        "scope": "cross_state_frozen_F_capacity_audit",
        "equation_target": {"relation": "frozen Psi_0=1 F states"},
        "certificate_context": {
            "certificate_type": "bounded_fourier_carrier_capacity",
            "source": BOUNDED_FOURIER_CAPACITY_INPUT.name,
            "phase": "CAPACITY_AUDIT",
            "proof_boundary": "finite_frozen_cross_state_capacity_only",
            "dual_coordinate_box": dual_coordinate_box,
            "target_phase_filter": target_phase_filter,
            "real_carrier_vector_status": "recomputed",
            "carrier_mapping_status": "unproved",
            "global_fourier_maximizer_status": "unproved",
        },
        "carrier_capacity_summary": {
            "state_count": expected_counts["state_count"],
            "direction_count": expected_counts["direction_count"],
            "families": family_summary,
        },
        "marked_solution_set": {
            "status": "not_carried",
            "reason": "capacity audit has no marked-lift witness",
        },
        "target_fiber": {
            "status": "not_carried",
            "reason": "family-level Fourier capacity evidence",
        },
        "signed_defect": {"status": "not_carried"},
        "induction_rank": {
            "status": "not_assigned",
            "reason": "no E1-E5 recursive edge",
        },
        "potential_record": {
            "status": "absent",
            "reason": "capacity inequalities do not provide a well-founded descent",
        },
        "selected_branch": "bounded_fourier_carrier_capacity",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "e1_e5": {f"E{i}": False for i in range(1, 6)},
        "proof_boundary": "finite_capacity_negative_boundary",
        "scope_note": (
            "Real carrier heights are verified for the frozen F sample, but character order "
            "and phase are not charged as extra height. No overload, marked lift, or universal "
            "Fourier-to-carrier map is inferred."
        ),
        "source_receipt": {
            "result_file": BOUNDED_FOURIER_CAPACITY_INPUT.name,
            "result_sha256": sha256(BOUNDED_FOURIER_CAPACITY_INPUT),
            "certificate_input": BOUNDED_FOURIER_CERTIFICATE_INPUT.name,
            "certificate_input_sha256": payload["input_sha256"],
            "linear_source": BOUNDED_FOURIER_SOURCE.name,
            "linear_source_sha256": payload["source_sha256"],
        },
    }
    check_status_boundary(result)
    return result


def bottom_word_lattice_capacity_receipt(payload: dict[str, object]) -> dict[str, object]:
    """Attach the exact bottom-word lattice and signed-capacity boundary.

    The matrix/SNF identities and the signed K/x_R capacity dictionary are exact,
    but the focused strong misses still do not supply a marked lift or a global
    carrier map.  Keep this family as non-recursive capacity evidence.
    """
    if payload.get("schema_version") != "type-i-bottom-word-lattice-pareto-cycle-capacity/v1":
        raise AssertionError("bottom-word capacity schema changed")
    inputs = payload.get("inputs")
    summary = payload.get("summary")
    generic = payload.get("generic_bottom_word")
    cycle_case = payload.get("internal_free_cycle_counterexample")
    linear_case = payload.get("linear_strong_miss_counterexample")
    if not isinstance(inputs, dict) or not isinstance(summary, dict):
        raise AssertionError("bottom-word capacity input summary missing")
    if not isinstance(generic, dict) or not isinstance(cycle_case, dict):
        raise AssertionError("bottom-word capacity core payload missing")
    if not isinstance(linear_case, dict):
        raise AssertionError("bottom-word linear miss payload missing")
    if inputs.get("formal_closure_script") != BOTTOM_WORD_CLOSURE_SOURCE.name:
        raise AssertionError("bottom-word closure source name changed")
    if inputs.get("sha256") != sha256(BOTTOM_WORD_CLOSURE_SOURCE):
        raise AssertionError("bottom-word closure source is stale")

    expected_summary = {
        "word_profiles": 2,
        "strong_miss_counterexamples": 2,
        "linear_source_counterexamples": 1,
        "cycle_static_receipts": 4,
        "focused_direct_terminal_primes": [5_596_369, 212_973_049],
        "verified_rechart_count": 1,
        "candidate_rechart_count": 1,
        "pareto_example_bound": 4,
    }
    if summary != expected_summary:
        raise AssertionError("bottom-word capacity summary changed")

    Q = int(generic["Q"])
    A = int(generic["A"])
    B = int(generic["B"])
    R = int(generic["R"])
    root = tuple(int(value) for value in generic["root"])
    endpoint = tuple(int(value) for value in generic["endpoint"])
    matrix = generic.get("matrix")
    if not isinstance(matrix, list) or len(matrix) != 2 or any(
        not isinstance(row, list) or len(row) != 2 for row in matrix
    ):
        raise AssertionError("bottom-word matrix shape changed")
    m00, m01 = (int(value) for value in matrix[0])
    m10, m11 = (int(value) for value in matrix[1])
    determinant = m00 * m11 - m01 * m10
    entry_gcd = gcd(gcd(gcd(abs(m00), abs(m01)), abs(m10)), abs(m11))
    scaled = (m00 * root[0] + m01 * root[1], m10 * root[0] + m11 * root[1])
    if not (
        Q == 8
        and A == 0
        and B == 7
        and R == 35
        and A + B == Q - 1
        and determinant == Q
        and entry_gcd == 1
        and generic.get("smith_diagonal") == [1, Q]
        and root == (32, 3)
        and endpoint == (4, 31)
        and scaled == (Q * endpoint[0], Q * endpoint[1])
        and sum(endpoint) == R
    ):
        raise AssertionError("bottom-word matrix/SNF identity changed")
    roots = [x for x in range(1, R) if (x + A * R) % Q == 0]
    if roots != generic.get("admissible_root_congruence_class"):
        raise AssertionError("bottom-word root lattice changed")
    if generic.get("root_capacity_bound") != 5 or len(roots) > int(generic["root_capacity_bound"]):
        raise AssertionError("bottom-word root capacity bound changed")

    cycle_capacity = cycle_case.get("cycle_capacity")
    cycle_word = cycle_case.get("cycle_word")
    cycle_pairs = cycle_case.get("cycle_entry_common_overload_pairs")
    cycle_split = cycle_case.get("empty_suffix_cross_pair")
    linear_split = linear_case.get("empty_suffix_cross_pair")
    if not isinstance(cycle_capacity, dict) or not isinstance(cycle_word, dict):
        raise AssertionError("bottom-word cycle capacity payload changed")
    if not isinstance(cycle_pairs, list) or not isinstance(cycle_split, dict):
        raise AssertionError("bottom-word cycle pair payload changed")
    if not isinstance(linear_split, dict):
        raise AssertionError("bottom-word linear pair payload changed")
    static_receipts = cycle_capacity.get("static_receipts")
    if not isinstance(static_receipts, dict) or len(static_receipts) != 4:
        raise AssertionError("bottom-word static separator count changed")
    if any(
        not isinstance(receipt, dict)
        or receipt.get("kind") != "MISS_STATIC"
        or receipt.get("prime") != 103
        for receipt in static_receipts.values()
    ):
        raise AssertionError("bottom-word static separator changed")
    if cycle_capacity.get("cycle_Q") != 4141:
        raise AssertionError("bottom-word cycle product changed")
    if cycle_word.get("Q") != 4141 or cycle_word.get("smith_diagonal") != [1, 4141]:
        raise AssertionError("bottom-word cycle lattice changed")
    if cycle_split.get("branch") != "strict_split" or linear_split.get("branch") != "strict_split":
        raise AssertionError("bottom-word strict-split boundary changed")
    if len(cycle_pairs) != 2 or any(
        not isinstance(pair, dict) or pair.get("branch") != "common_overload"
        for pair in cycle_pairs
    ):
        raise AssertionError("bottom-word common-overload boundary changed")

    descriptor = {
        "family": "bottom_word_lattice_pareto_cycle_capacity",
        "input_sha256": sha256(BOTTOM_WORD_CAPACITY_INPUT),
        "closure_sha256": sha256(BOTTOM_WORD_CLOSURE_SOURCE),
    }
    result = {
        "state_id": "family:" + canonical_hash(descriptor),
        "scope": "cross_state_bottom_word_lattice_and_signed_capacity_audit",
        "equation_target": {"relation": "4K=pR+1"},
        "certificate_context": {
            "certificate_type": "bottom_word_lattice_pareto_cycle_capacity",
            "source": BOTTOM_WORD_CAPACITY_INPUT.name,
            "phase": "CAPACITY_AUDIT",
            "proof_boundary": "finite_path_word_cycle_and_signed_capacity_only",
            "carrier_mapping_status": "unproved",
            "formal_edge_status": "candidate_generation_only",
        },
        "lattice_summary": {
            "word_profile_count": int(summary["word_profiles"]),
            "generic_word": {
                "Q": Q,
                "A": A,
                "B": B,
                "R": R,
                "smith_diagonal": generic["smith_diagonal"],
                "root_capacity_bound": int(generic["root_capacity_bound"]),
            },
            "cycle_word": {
                "Q": int(cycle_word["Q"]),
                "R": int(cycle_word["R"]),
                "smith_diagonal": cycle_word["smith_diagonal"],
                "root_capacity_bound": int(cycle_word["root_capacity_bound"]),
            },
        },
        "cycle_capacity_summary": {
            "static_separator_count": len(static_receipts),
            "static_separator_prime": 103,
            "moving_primes": cycle_capacity["moving_valuations"],
            "cycle_Q": int(cycle_capacity["cycle_Q"]),
            "interval_example_kinds": {
                key: value["kind"]
                for key, value in cycle_capacity["interval_receipt_unit_examples"].items()
            },
        },
        "signed_target_fiber_summary": {
            "strong_miss_count": int(summary["strong_miss_counterexamples"]),
            "linear_source_counterexample_count": int(summary["linear_source_counterexamples"]),
            "strict_split_count": 2,
            "common_overload_count": 2,
            "dictionary": "signed_exponents -> K/x_R/joint box overflow",
        },
        "marked_solution_set": {
            "status": "not_carried",
            "reason": "capacity and path-word receipts have no universal marked lift",
        },
        "target_fiber": {
            "status": "recomputed_focused_boundary",
            "reason": "signed target-fiber dictionary is state/family evidence only",
        },
        "signed_defect": {
            "status": "recomputed",
            "direction": "retained in source result; not charged to a carrier map",
        },
        "induction_rank": {
            "status": "not_assigned",
            "reason": "cycle and strong-miss receipts do not prove E5",
        },
        "potential_record": {
            "status": "absent",
            "reason": "path-word capacity does not provide a global well-founded descent",
        },
        "selected_branch": "bottom_word_lattice_pareto_cycle_capacity",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "e1_e5": {f"E{i}": False for i in range(1, 6)},
        "proof_boundary": "finite_path_word_cycle_and_signed_capacity_only",
        "scope_note": (
            "The matrix/SNF normal form, cycle-ray separator, and signed K/x_R capacity "
            "dictionary are exact for the recorded witnesses. They do not imply a universal "
            "carrier map, marked lift, or recursive edge."
        ),
        "source_receipt": {
            "result_file": BOTTOM_WORD_CAPACITY_INPUT.name,
            "result_sha256": sha256(BOTTOM_WORD_CAPACITY_INPUT),
            "generator_file": BOTTOM_WORD_CAPACITY_SOURCE.name,
            "generator_sha256": sha256(BOTTOM_WORD_CAPACITY_SOURCE),
            "formal_closure_file": BOTTOM_WORD_CLOSURE_SOURCE.name,
            "formal_closure_sha256": sha256(BOTTOM_WORD_CLOSURE_SOURCE),
        },
    }
    check_status_boundary(result)
    return result


def source_word_joint_capacity_receipt(payload: dict[str, object]) -> dict[str, object]:
    """Attach the exact common-overload/split-exchange capacity dichotomy."""
    if payload.get("schema_version") != "type-i-source-word-joint-capacity-dichotomy/v2":
        raise AssertionError("source-word capacity schema changed")
    inputs = payload.get("inputs")
    summary = payload.get("summary")
    records = payload.get("path_records")
    counterexample = payload.get("complete_reach_split_counterexample")
    if not isinstance(inputs, dict) or not isinstance(summary, dict):
        raise AssertionError("source-word capacity input summary missing")
    if not isinstance(records, list) or not isinstance(counterexample, dict):
        raise AssertionError("source-word capacity records missing")
    if inputs.get("frozen_psi_one_sha256") != sha256(SOURCE_WORD_FROZEN_INPUT):
        raise AssertionError("source-word frozen spectrum input is stale")
    if inputs.get("formal_closure_sha256") != sha256(BOTTOM_WORD_CLOSURE_SOURCE):
        raise AssertionError("source-word formal closure input is stale")
    expected_summary = {
        "path_case_count": 7,
        "cross_pair_count": 14,
        "branch_histogram": {"common_overload": 7, "split_exchange": 7},
        "split_exchange_path_count": 4,
        "disjoint_common_carrier_path_count": 2,
    }
    if summary != expected_summary or len(records) != expected_summary["path_case_count"]:
        raise AssertionError("source-word capacity summary changed")

    branch_counts = {"common_overload": 0, "split_exchange": 0}
    checked_pairs = 0
    for record in records:
        if not isinstance(record, dict):
            raise AssertionError("source-word path record shape changed")
        prime = int(record["prime"])
        modulus = int(record["R"])
        K = int(record["K"])
        x_value = int(record["x_R"])
        if 4 * K != prime * modulus + 1 or 4 * x_value != prime + modulus:
            raise AssertionError("source-word chart identity changed")
        pairs = record.get("cross_pairs")
        if not isinstance(pairs, list) or len(pairs) != 2:
            raise AssertionError("source-word cross-pair count changed")
        common_capacity = gcd(K, x_value)
        joint_capacity = lcm(K, x_value)
        for pair in pairs:
            if not isinstance(pair, dict):
                raise AssertionError("source-word cross-pair shape changed")
            P = int(pair["P"])
            Q = int(pair["Q"])
            product = int(pair["product"])
            if gcd(P, Q) != 1 or (P + Q) % modulus or P * Q != product:
                raise AssertionError("source-word primitive pair changed")
            capacity = pair.get("capacity")
            if not isinstance(capacity, dict):
                raise AssertionError("source-word capacity payload changed")
            K_defect = product // gcd(product, K)
            x_defect = product // gcd(product, x_value)
            common_overload = product // gcd(product, joint_capacity)
            if capacity.get("K_defect") != K_defect or capacity.get("x_R_defect") != x_defect:
                raise AssertionError("source-word single-capacity defect changed")
            if capacity.get("common_overload_factor") != common_overload:
                raise AssertionError("source-word joint-capacity defect changed")
            branch = str(capacity.get("branch"))
            expected_branch = (
                "common_overload"
                if K_defect > 1 and x_defect > 1 and common_overload > 1
                else "split_exchange"
                if K_defect > 1 and x_defect > 1
                else "not_double_miss"
            )
            if branch != expected_branch or branch not in branch_counts:
                raise AssertionError("source-word capacity branch changed")
            branch_counts[branch] += 1
            checked_pairs += 1
            if branch == "split_exchange":
                exchange = capacity.get("exchange")
                if not isinstance(exchange, dict):
                    raise AssertionError("source-word split exchange missing")
                g = common_capacity
                e_k = K_defect
                e_x = x_defect
                if gcd(e_k, e_x) != 1 or joint_capacity % product:
                    raise AssertionError("source-word split exchange divisibility changed")
                if x_value % (g * e_k) or K % (g * e_x):
                    raise AssertionError("source-word split exchange coordinates changed")
                a = x_value // (g * e_k)
                b = K // (g * e_x)
                delta = (modulus * modulus - 1) // (4 * g)
                if exchange.get("a") != a or exchange.get("b") != b:
                    raise AssertionError("source-word split exchange coordinates changed")
                if exchange.get("reduced_delta") != delta or modulus * e_k * a - e_x * b != delta:
                    raise AssertionError("source-word split exchange identity changed")
            elif capacity.get("exchange") is not None:
                raise AssertionError("common-overload pair unexpectedly has exchange")
    if checked_pairs != 14 or branch_counts != summary["branch_histogram"]:
        raise AssertionError("source-word branch histogram changed")

    counter_capacity = counterexample.get("capacity")
    reach = counterexample.get("endpoint_reach")
    if not isinstance(counter_capacity, dict) or not isinstance(reach, dict):
        raise AssertionError("source-word split counterexample payload changed")
    if counterexample.get("prime") != 2017 or counterexample.get("R") != 207:
        raise AssertionError("source-word split counterexample identity changed")
    if (
        counter_capacity.get("branch") != "split_exchange"
        or counterexample.get("centered_type_i_hit") is not False
    ):
        raise AssertionError("source-word split counterexample boundary changed")
    nodes = reach.get("nodes")
    edges = reach.get("edges")
    if not isinstance(nodes, list) or len(nodes) != 4 or not isinstance(edges, list) or len(edges) != 4:
        raise AssertionError("source-word split Reach boundary changed")

    descriptor = {
        "family": "source_word_joint_capacity_dichotomy",
        "input_sha256": sha256(SOURCE_WORD_CAPACITY_INPUT),
        "frozen_sha256": sha256(SOURCE_WORD_FROZEN_INPUT),
        "closure_sha256": sha256(BOTTOM_WORD_CLOSURE_SOURCE),
    }
    result = {
        "state_id": "family:" + canonical_hash(descriptor),
        "scope": "cross_state_source_word_joint_capacity_audit",
        "equation_target": {"relation": "4K=pR+1; 4x_R=p+R"},
        "certificate_context": {
            "certificate_type": "source_word_joint_capacity_dichotomy",
            "source": SOURCE_WORD_CAPACITY_INPUT.name,
            "phase": "CAPACITY_AUDIT",
            "proof_boundary": "algebraic_joint_capacity_and_focused_path_boundary",
            "carrier_mapping_status": "unproved",
            "formal_edge_status": "candidate_generation_only",
        },
        "joint_capacity_summary": {
            "path_case_count": int(summary["path_case_count"]),
            "cross_pair_count": checked_pairs,
            "branch_histogram": branch_counts,
            "split_exchange_path_count": int(summary["split_exchange_path_count"]),
            "disjoint_common_carrier_path_count": int(summary["disjoint_common_carrier_path_count"]),
            "complete_reach_split_counterexample": {
                "prime": 2017,
                "R": 207,
                "node_count": len(nodes),
            },
        },
        "marked_solution_set": {
            "status": "not_carried",
            "reason": "capacity exchange does not provide a marked lift",
        },
        "target_fiber": {
            "status": "signed_cross_pair_dictionary",
            "reason": "common-overload and split-exchange are capacity branches only",
        },
        "signed_defect": {"status": "recomputed", "source": "cross_pair capacities"},
        "induction_rank": {"status": "not_assigned", "reason": "no E1-E5 recursive edge"},
        "potential_record": {"status": "absent", "reason": "capacity dichotomy supplies no E5"},
        "selected_branch": "source_word_joint_capacity_dichotomy",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "e1_e5": {f"E{i}": False for i in range(1, 6)},
        "proof_boundary": "algebraic_joint_capacity_and_focused_path_boundary",
        "scope_note": (
            "The common-overload/split-exchange dichotomy is exact for each recorded cross pair. "
            "It does not force a shared carrier, a Type I/II terminal, or a recursive E4 edge."
        ),
        "source_receipt": {
            "result_file": SOURCE_WORD_CAPACITY_INPUT.name,
            "result_sha256": sha256(SOURCE_WORD_CAPACITY_INPUT),
            "frozen_input": SOURCE_WORD_FROZEN_INPUT.name,
            "frozen_input_sha256": sha256(SOURCE_WORD_FROZEN_INPUT),
            "formal_closure": BOTTOM_WORD_CLOSURE_SOURCE.name,
            "formal_closure_sha256": sha256(BOTTOM_WORD_CLOSURE_SOURCE),
        },
    }
    check_status_boundary(result)
    return result


def large_slab_factor_pair_capacity_receipt(payload: dict[str, object]) -> dict[str, object]:
    """Attach exact large-slab factor-pair and layer-capacity evidence."""
    if payload.get("schema_version") != "type-i-large-slab-factor-pair-layer-capacity/v1":
        raise AssertionError("large-slab capacity schema changed")
    summary = payload.get("summary")
    slab_records = payload.get("slab_records")
    layer = payload.get("layer_capacity")
    source_records = payload.get("source_word_carrier_records")
    if (
        not isinstance(summary, dict)
        or not isinstance(slab_records, list)
        or not isinstance(layer, dict)
        or not isinstance(source_records, list)
    ):
        raise AssertionError("large-slab capacity payload shape changed")
    expected_summary = {
        "slab_case_count": 4,
        "covered_alpha": [1, 2, 3],
        "admissible_factor_pair_count": 5,
        "layer_gcd_pair_check_count": 105,
        "same_exponent_check_count": 15,
        "repeated_carrier_count": 4,
        "source_word_carrier_case_count": 5,
        "source_word_slab_q_union_hit_count": 4,
    }
    if summary != expected_summary or len(slab_records) != 4 or len(source_records) != 5:
        raise AssertionError("large-slab capacity summary changed")

    expected_betas = {
        (5_596_369, 2, 5, 1): [3],
        (212_973_049, 71, 1, 3): [2],
        (122_014_489, 467, 1, 1): [4, 244],
        (37_793_809, 6_211, 1, 2): [1],
    }
    alpha_branch_records: list[dict[str, object]] = []
    for record in slab_records:
        if not isinstance(record, dict):
            raise AssertionError("large-slab record shape changed")
        prime = int(record["prime"])
        modulus = int(record["R"])
        q = int(record["q"])
        exponent = int(record["e"])
        alpha = int(record["alpha"])
        beta = int(record["beta"])
        Q = int(record["Q"])
        K = int(record["K"])
        N = int(record["N"])
        H = int(record["H"])
        c = int(record["c"])
        if prime % 24 != 1 or alpha not in (1, 2, 3) or alpha % q == 0:
            raise AssertionError("large-slab anchor restriction changed")
        if (
            Q != q**exponent
            or modulus != alpha * Q + beta
            or K != (prime * modulus + 1) // 4
            or 4 * K != prime * modulus + 1
            or N != alpha * prime * Q + 1
            or H != 4 * alpha * c - prime
            or beta * H != N
            or beta >= (4 - alpha) * Q
            or (4 - alpha) * H <= alpha * prime
        ):
            raise AssertionError("large-slab factor-pair normal form changed")
        factor_payload = record.get("N_factorization")
        if not isinstance(factor_payload, dict):
            raise AssertionError("large-slab factorization missing")
        factor_product = 1
        for prime_text, factor_exponent in factor_payload.items():
            factor_prime = int(prime_text)
            factor_exponent = int(factor_exponent)
            if factor_prime < 2 or factor_exponent < 1:
                raise AssertionError("large-slab factorization entry changed")
            factor_product *= factor_prime**factor_exponent
        if factor_product != N:
            raise AssertionError("large-slab factorization no longer factors N")
        admissible = record.get("admissible_records_in_linear_range")
        if not isinstance(admissible, list):
            raise AssertionError("large-slab admissible list missing")
        key = (prime, q, exponent, alpha)
        if [int(candidate["beta"]) for candidate in admissible] != expected_betas[key]:
            raise AssertionError("large-slab admissible beta set changed")
        for candidate in admissible:
            candidate_beta = int(candidate["beta"])
            candidate_H = int(candidate["H"])
            candidate_c = int(candidate["c"])
            candidate_R = int(candidate["R"])
            candidate_K = int(candidate["K"])
            if (
                candidate_beta * candidate_H != N
                or candidate_H != 4 * alpha * candidate_c - prime
                or candidate_R != alpha * Q + candidate_beta
                or candidate_K != alpha * candidate_beta * candidate_c
                or 4 * candidate_K != prime * candidate_R + 1
            ):
                raise AssertionError("large-slab admissible reconstruction changed")
        R_Q = (-pow(prime, -1, 4 * Q)) % (4 * Q)
        rho = (K * pow(prime, -1, Q)) % Q
        if not 1 <= rho < Q or R_Q == modulus:
            raise AssertionError("large-slab canonical Q-chart changed")
        branch: dict[str, object] = {
            "prime": prime,
            "R": modulus,
            "Q": Q,
            "alpha": alpha,
            "beta": beta,
            "R_Q": R_Q,
            "rho": rho,
        }
        if alpha == 1:
            x_three = (prime + 3) // 4
            H_three = 4 * c - prime
            d_three = 3 * c - prime
            W_three = 4 * Q - modulus
            if (
                beta * H_three != prime * Q + 1
                or beta * d_three != (prime * W_three + 3) // 4
                or (prime * W_three + 3) % 4
                or H_three % 4 != 3
                or d_three % 3 != 2
            ):
                raise AssertionError("alpha=1 gap-3 identities changed")
            g_three = gcd(d_three, x_three * x_three)
            if g_three % 3 == 2:
                gap_divisor = min(g_three, x_three * x_three // g_three)
                if (
                    gap_divisor > x_three
                    or (gap_divisor + x_three) % 3
                    or gap_divisor <= 0
                ):
                    raise AssertionError("alpha=1 gap-3 Type II branch changed")
                branch["gap3_branch"] = "type_ii_terminal_candidate"
                branch["gap3_divisor"] = gap_divisor
            else:
                excess = d_three // g_three
                excess_factors = factorization(excess)
                if excess <= 1 or not any(prime_factor % 3 == 2 for prime_factor, _ in excess_factors):
                    raise AssertionError("alpha=1 gap-3 capacity branch changed")
                branch["gap3_branch"] = "gap3_capacity_overflow"
                branch["gap3_excess"] = excess
                branch["gap3_excess_factors"] = excess_factors
        elif alpha == 2:
            complement = 2 * Q - beta
            if modulus % 8 != 7 or complement % 8 != 5:
                raise AssertionError("alpha=2 congruence boundary changed")
            tau = (-rho) % Q
            if not 1 <= tau < Q or (K + prime * tau) % Q:
                raise AssertionError("alpha=2 canonical shift changed")
            h = (complement - 1) // 4
            expected_R_Q = (
                modulus + 4 * tau
                if tau <= h
                else modulus + 4 * tau - 4 * Q
            )
            if R_Q != expected_R_Q:
                raise AssertionError("alpha=2 Q-chart formula changed")
            branch["local_complement_drop"] = complement - 4 * tau
            branch["tau"] = tau
            branch["branch"] = "local_complement_drop"
        else:
            if beta >= Q or modulus % 3 != 2:
                raise AssertionError("alpha=3 congruence boundary changed")
            delta = Q - rho
            branch["branch"] = "farey_pair_candidate" if R_Q > modulus else "q_absorb"
            if R_Q > modulus:
                beta_prime = beta + 4 * delta
                if not 0 < 4 * delta < Q - beta:
                    raise AssertionError("alpha=3 Farey size boundary changed")
                n_star_numerator = prime * beta_prime + 1
                if n_star_numerator % Q:
                    raise AssertionError("alpha=3 Farey divisibility changed")
                n_star = n_star_numerator // Q
                if not 0 < n_star < prime:
                    raise AssertionError("alpha=3 Farey rank boundary changed")
                if (
                    n_star * Q - prime * beta_prime != 1
                    or prime * (Q - beta_prime) - Q * (prime - n_star) != 1
                ):
                    raise AssertionError("alpha=3 Farey determinant changed")
                branch.update(
                    {
                        "delta": delta,
                        "beta_prime": beta_prime,
                        "n_star": n_star,
                        "determinant_pair": [1, 1],
                    }
                )
        alpha_branch_records.append(branch)

    if (
        layer.get("prime") != 337
        or layer.get("q") != 7
        or layer.get("alphas") != [1, 2, 3]
        or layer.get("exponents") != [1, 2, 3, 4, 5]
        or layer.get("pair_check_count") != 105
    ):
        raise AssertionError("large-slab layer grid changed")
    same_exponent = layer.get("same_exponent_checks")
    if not isinstance(same_exponent, list) or len(same_exponent) != 15:
        raise AssertionError("large-slab same-exponent grid changed")
    expected_same = {
        (exponent, tuple(alphas)): gcd(
            337 * 7**exponent * alphas[0] + 1,
            337 * 7**exponent * alphas[1] + 1,
        )
        for exponent in range(1, 6)
        for alphas in ((1, 2), (2, 3), (1, 3))
    }
    for row in same_exponent:
        if not isinstance(row, dict):
            raise AssertionError("large-slab same-exponent row changed")
        exponent = int(row["exponent"])
        alphas = tuple(int(value) for value in row["alphas"])
        if row.get("gcd") != expected_same.get((exponent, alphas)):
            raise AssertionError("large-slab same-exponent gcd changed")
    repeated = layer.get("repeated_carriers")
    expected_repeated = [
        {"alpha": 1, "carrier": 2, "exponents": [1, 2, 3, 4, 5], "order": 1},
        {"alpha": 1, "carrier": 5, "exponents": [1, 5], "order": 4},
        {"alpha": 2, "carrier": 3, "exponents": [1, 2, 3, 4, 5], "order": 1},
        {"alpha": 3, "carrier": 2, "exponents": [1, 2, 3, 4, 5], "order": 1},
    ]
    if not isinstance(repeated, list) or len(repeated) != 4:
        raise AssertionError("large-slab repeated-carrier count changed")
    if [
        {
            key: row[key]
            for key in ("alpha", "carrier", "exponents", "order")
        }
        for row in repeated
    ] != expected_repeated:
        raise AssertionError("large-slab repeated-carrier order changed")
    multi_layer = layer.get("multi_layer_checks")
    if not isinstance(multi_layer, list) or len(multi_layer) != 3:
        raise AssertionError("large-slab multi-layer checks changed")
    for row in multi_layer:
        if not isinstance(row, dict):
            raise AssertionError("large-slab multi-layer row changed")
        alpha = int(row["alpha"])
        exponents = [int(value) for value in row["exponents"]]
        anchor = min(exponents)
        step_gcd = gcd(*(value - anchor for value in exponents if value > anchor))
        values = [alpha * 337 * 7**value + 1 for value in exponents]
        if (
            row.get("step_gcd") != step_gcd
            or row.get("common_gcd") != gcd(*values)
            or gcd(*values) != gcd(values[0], 7**step_gcd - 1)
        ):
            raise AssertionError("large-slab multi-layer gcd identity changed")

    q_union_count = 0
    q_union_false: list[dict[str, object]] = []
    for record in source_records:
        if not isinstance(record, dict):
            raise AssertionError("source-word slab record shape changed")
        prime = int(record["prime"])
        modulus = int(record["R"])
        q = int(record["q"])
        exponent = int(record["e"])
        U = int(record["U"])
        V = int(record["V"])
        theta = int(record["theta"])
        X_U = int(record["X_U"])
        X_V = int(record["X_V"])
        K = (prime * modulus + 1) // 4
        x_R = (prime + modulus) // 4
        if (
            prime % 24 != 1
            or (U + V) % modulus
            or X_U + X_V != modulus
            or K % U
            or K % q == 0
            or valuation(X_U, q) + valuation(X_V, q) != exponent
        ):
            raise AssertionError("source-word slab boundary changed")
        u_numerator = theta * X_U - U
        v_numerator = theta * X_V - V
        if (
            u_numerator % modulus
            or v_numerator % modulus
            or u_numerator // modulus < 0
            or v_numerator // modulus < 0
            or (u_numerator // modulus) + (v_numerator // modulus)
            != theta - (U + V) // modulus
        ):
            raise AssertionError("source-word path quotient identity changed")
        d_U = gcd(U, theta * X_V)
        d_V = gcd(V, theta * X_U)
        L_U = U * theta * X_V // d_U**2
        L_V = V * theta * X_U // d_V**2
        common_capacity = lcm(K, x_R)
        C_U = L_U // gcd(L_U, common_capacity)
        C_V = L_V // gcd(L_V, common_capacity)
        actual_exponents = (valuation(C_U, q), valuation(C_V, q))
        predicted_exponents = (
            max(0, valuation(theta, q) + valuation(X_V, q) - valuation(x_R, q)),
            max(
                0,
                abs(valuation(V, q) - valuation(theta, q) - valuation(X_U, q))
                - valuation(x_R, q),
            ),
        )
        if actual_exponents != predicted_exponents:
            raise AssertionError("source-word q-overload exponent formula changed")
        if bool(record.get("q_in_union")) != bool(any(actual_exponents)):
            raise AssertionError("source-word q-union classification changed")
        if record.get("q_in_union"):
            q_union_count += 1
        else:
            q_union_false.append(record)
        boundary = record.get("boundary")
        if isinstance(boundary, dict):
            expected_R_Q = (-pow(prime, -1, 4 * q**exponent)) % (4 * q**exponent)
            if boundary.get("R_Q") != expected_R_Q or boundary.get("decreases_R") is not True:
                raise AssertionError("source-word anchor boundary changed")
    if q_union_count != 4 or len(q_union_false) != 1:
        raise AssertionError("source-word q-union count changed")
    if (
        int(q_union_false[0]["prime"]) != 10_170_169
        or int(q_union_false[0]["q"]) != 101
    ):
        raise AssertionError("source-word q-union negative boundary changed")
    alpha_branch_counts = {
        str(alpha): sum(int(row["alpha"]) == alpha for row in alpha_branch_records)
        for alpha in (1, 2, 3)
    }
    if alpha_branch_counts != {"1": 2, "2": 1, "3": 1}:
        raise AssertionError("large-slab alpha branch count changed")

    descriptor = {
        "family": "large_slab_factor_pair_layer_capacity",
        "input_sha256": sha256(LARGE_SLAB_CAPACITY_INPUT),
        "source_sha256": sha256(LARGE_SLAB_CAPACITY_SOURCE),
        "summary": expected_summary,
    }
    result = {
        "state_id": "family:" + canonical_hash(descriptor),
        "scope": "large_slab_factor_pair_and_cross_layer_capacity_audit",
        "equation_target": {"relation": "4K=pR+1"},
        "certificate_context": {
            "certificate_type": "large_slab_factor_pair_layer_capacity",
            "source": LARGE_SLAB_CAPACITY_INPUT.name,
            "phase": "CAPACITY_AUDIT",
            "proof_boundary": "large_slab_factor_pair_and_focused_layer_boundary",
            "carrier_mapping_status": "unproved",
            "formal_edge_status": "candidate_generation_only",
        },
        "large_slab_summary": {
            "slab_case_count": int(summary["slab_case_count"]),
            "covered_alpha": list(summary["covered_alpha"]),
            "admissible_factor_pair_count": int(summary["admissible_factor_pair_count"]),
            "layer_gcd_pair_check_count": int(summary["layer_gcd_pair_check_count"]),
            "same_exponent_check_count": int(summary["same_exponent_check_count"]),
            "repeated_carrier_count": int(summary["repeated_carrier_count"]),
            "source_word_carrier_case_count": int(summary["source_word_carrier_case_count"]),
            "source_word_slab_q_union_hit_count": q_union_count,
            "alpha_branch_counts": alpha_branch_counts,
            "alpha_branch_records": alpha_branch_records,
            "source_word_q_union_negative_boundary": {
                "prime": int(q_union_false[0]["prime"]),
                "q": int(q_union_false[0]["q"]),
            },
        },
        "normal_forms": {
            "factor_pair": "N_alpha_e=alpha*p*q^e+1=beta*(4*alpha*c-p)",
            "layer_gcd": "gcd(N_alpha_e,N_alpha2_f)=gcd(N_alpha_e,alpha2*q^(f-e)-alpha)",
            "source_word_q_excess": "v_q(C_U),v_q(C_V) from theta, endpoint and x_R valuations",
        },
        "marked_solution_set": {
            "status": "not_carried",
            "reason": "large-slab capacity does not provide a marked lift",
        },
        "target_fiber": {
            "status": "factor_pair_and_qadic_dictionary",
            "reason": "layer and source-word identities are capacity evidence only",
        },
        "signed_defect": {"status": "not_assigned"},
        "induction_rank": {"status": "not_assigned", "reason": "no E1-E5 recursive edge"},
        "potential_record": {"status": "absent", "reason": "no well-founded descent is supplied"},
        "selected_branch": "large_slab_factor_pair_layer_capacity",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "e1_e5": {f"E{i}": False for i in range(1, 6)},
        "proof_boundary": "large_slab_factor_pair_and_focused_layer_boundary",
        "scope_note": (
            "The factor-pair normal form and layer gcd identities are exact for the recorded "
            "large slabs. The focused examples do not prove source Reach completeness, "
            "cross-state carrier mapping, a Type I/II terminal, or E4."
        ),
        "source_receipt": {
            "result_file": LARGE_SLAB_CAPACITY_INPUT.name,
            "result_sha256": sha256(LARGE_SLAB_CAPACITY_INPUT),
            "generator_file": LARGE_SLAB_CAPACITY_SOURCE.name,
            "generator_sha256": sha256(LARGE_SLAB_CAPACITY_SOURCE),
        },
    }
    check_status_boundary(result)
    return result


def universal_source_anchor_receipt(payload: dict[str, object]) -> dict[str, object]:
    """Attach the universal formal source and focused anchor-orbit evidence.

    The source formula is general, while the orbit rows remain focused arithmetic
    evidence.  Neither is promoted to a recursive edge: an anchor cycle still
    needs a separate terminal or well-founded phase argument.
    """
    summary = payload.get("summary")
    anchor = payload.get("universal_anchor")
    if not isinstance(summary, dict) or not isinstance(anchor, dict):
        raise AssertionError("universal source/anchor payload shape changed")
    if summary.get("universal_p_source_count") != 3:
        raise AssertionError("universal source count changed")
    focused_names = (
        "G_bundle_overflow",
        "G_marked_absorb",
        "accumulated_all_overflow_cycle",
    )
    records: list[dict[str, object]] = []
    classification_counts: dict[str, int] = {}
    cycle_lengths: list[int] = []
    for name in focused_names:
        record = anchor.get(name)
        if not isinstance(record, dict):
            raise AssertionError(f"universal anchor record missing: {name}")
        source_receipt = record.get("source_receipt")
        orbit = record.get("anchor_orbit")
        if not isinstance(source_receipt, dict) or not isinstance(orbit, dict):
            raise AssertionError(f"universal anchor record shape changed: {name}")
        source = source_receipt.get("source")
        edge = source_receipt.get("edge")
        if not isinstance(source, list) or len(source) != 3:
            raise AssertionError(f"universal source shape changed: {name}")
        if not isinstance(edge, dict):
            raise AssertionError(f"universal source edge shape changed: {name}")
        prime = int(record["prime"])
        modulus = int(record["R"])
        K = (prime * modulus + 1) // 4
        expected_source = [prime, modulus * (prime - 1) - prime, prime - 1]
        if source != expected_source:
            raise AssertionError(f"universal source formula changed: {name}")
        if edge.get("q") != prime or edge.get("shift") != 1:
            raise AssertionError(f"universal source edge changed: {name}")
        if edge.get("gcd_reduction") != 1 or edge.get("destination") != [1, modulus - 1, 1]:
            raise AssertionError(f"universal source destination changed: {name}")
        cycle = orbit.get("cycle")
        orbit_nodes = orbit.get("orbit")
        rows = orbit.get("rows")
        if not isinstance(cycle, list) or not isinstance(orbit_nodes, list) or not isinstance(rows, list):
            raise AssertionError(f"anchor orbit shape changed: {name}")
        if cycle != orbit_nodes:
            raise AssertionError(f"focused anchor orbit is not a cycle: {name}")
        cycle_lengths.append(len(cycle))
        row_receipts: list[dict[str, object]] = []
        for row in rows:
            if not isinstance(row, dict):
                raise AssertionError(f"anchor orbit row shape changed: {name}")
            h = int(row["h"])
            other = int(row["other"])
            if h not in orbit_nodes or h <= 0 or other <= 0 or h + other != modulus:
                raise AssertionError(f"anchor orbit coordinates changed: {name}")
            if K % h:
                raise AssertionError(f"anchor orbit capacity coordinate changed: {name}")
            classification = str(row["classification"])
            if classification not in {"marked_absorb", "overflow", "terminal"}:
                raise AssertionError(f"unknown anchor classification: {classification}")
            classification_counts[classification] = classification_counts.get(classification, 0) + 1
            row_receipts.append(
                {
                    "h": h,
                    "other": other,
                    "classification": classification,
                    "M": int(row["M"]) if "M" in row else None,
                    "R_M": int(row["R_M"]) if "R_M" in row else None,
                    "Q": int(row["Q"]) if "Q" in row else None,
                    "next_h": int(row["next_h"]) if "next_h" in row else None,
                }
            )
        records.append(
            {
                "name": name,
                "prime": prime,
                "R": modulus,
                "K": K,
                "source": source,
                "destination": edge["destination"],
                "orbit": [int(value) for value in orbit_nodes],
                "cycle": [int(value) for value in cycle],
                "cycle_product_mod_R": int(orbit.get("cycle_product_mod_R", 0)),
                "rows": row_receipts,
            }
        )
    descriptor = {
        "family": "universal_p_source_anchor_orbit",
        "input_sha256": sha256(UNIVERSAL_ANCHOR_INPUT),
        "record_names": list(focused_names),
    }
    result = {
        "state_id": "family:" + canonical_hash(descriptor),
        "scope": "universal_formal_source_and_capacity_anchor_orbit",
        "equation_target": {"relation": "4K=pR+1"},
        "certificate_context": {
            "certificate_type": "universal_p_source_anchor_orbit",
            "source": UNIVERSAL_ANCHOR_INPUT.name,
            "phase": "FORMAL_SOURCE_AND_ANCHOR",
            "source_formula": "(U,V,m)=(p,R(p-1)-p,p-1)",
            "proof_boundary": "formal_source_and_focused_cycle_lattice_only",
            "recursive_mapping_status": "unproved",
        },
        "source_summary": {
            "universal_p_source_count": int(summary["universal_p_source_count"]),
            "focused_record_count": len(records),
            "cycle_length_histogram": {
                str(length): cycle_lengths.count(length) for length in sorted(set(cycle_lengths))
            },
            "orbit_classification_counts": classification_counts,
            "records": records,
        },
        "marked_solution_set": {
            "status": "not_carried",
            "reason": "formal source and anchor orbit do not provide a marked lift",
        },
        "target_fiber": {
            "status": "not_carried",
            "reason": "source provenance is independent of target-fiber nonemptiness",
        },
        "signed_defect": {"status": "not_carried"},
        "potential_record": {
            "status": "absent",
            "reason": "focused anchor cycles have no global well-founded rank",
        },
        "selected_branch": "universal_p_source_anchor_orbit",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "e1_e5": {f"E{i}": False for i in range(1, 6)},
        "proof_boundary": "formal_source_and_focused_anchor_cycle_only",
        "scope_note": (
            "The universal p-source closes the raw F/G source gap and the focused orbit rows "
            "are replayable capacity/lattice evidence.  A cycle or an overflow row is not a "
            "terminal or recursive edge without an independent E1-E5 mapping and rank."
        ),
        "source_receipt": {
            "result_file": UNIVERSAL_ANCHOR_INPUT.name,
            "result_sha256": sha256(UNIVERSAL_ANCHOR_INPUT),
        },
    }
    check_status_boundary(result)
    return result


def support_debt_phase_receipt(
    outer_rank: dict[str, object], phase: dict[str, object]
) -> dict[str, object]:
    """Match every non-unit support debt to its conditional phase-unit row."""
    if phase.get("input") != QADIC_INPUT.name:
        raise AssertionError("phase capacity input name changed")
    if phase.get("input_sha256") != sha256(QADIC_INPUT):
        raise AssertionError("phase capacity input is stale")
    phase_groups = phase.get("groups")
    if not isinstance(phase_groups, list):
        raise AssertionError("phase capacity groups are missing")
    phase_rows: list[dict[str, object]] = []
    for group in phase_groups:
        if not isinstance(group, dict) or not isinstance(group.get("rows"), list):
            raise AssertionError("phase capacity group shape changed")
        for row in group["rows"]:
            if not isinstance(row, dict):
                raise AssertionError("phase capacity row shape changed")
            phase_rows.append(row)
    if len(phase_rows) != 17:
        raise AssertionError("phase debt row count changed")

    channels = list(outer_rank.get("verified_receipts", [])) + list(
        outer_rank.get("rejected_channels", [])
    )
    links: list[dict[str, object]] = []
    used: set[tuple[int, int, int, str, int]] = set()
    for channel in channels:
        if not isinstance(channel, dict):
            raise AssertionError("outer-rank channel shape changed")
        debt = channel.get("support_debt")
        if not isinstance(debt, dict):
            raise AssertionError("outer-rank channel lacks support debt")
        for raw_factor in debt.get("factorization", []):
            if not isinstance(raw_factor, list) or len(raw_factor) != 2:
                raise AssertionError("support debt factorization shape changed")
            q, height = int(raw_factor[0]), int(raw_factor[1])
            key_prefix = (
                int(channel["equation_target"][1]),
                int(channel["source_support"]),
                int(channel["source_carrier"]),
                str(channel["side"]),
                q,
            )
            matches = [
                row
                for row in phase_rows
                if (
                    int(row["prime"]),
                    int(row["A"]),
                    int(row["M"]),
                    str(row["side"]),
                    int(row["q"]),
                )
                == key_prefix
            ]
            if len(matches) != 1:
                raise AssertionError(f"support debt phase row missing: {key_prefix}")
            row = matches[0]
            if (
                int(row["obstruction_height"]) != height
                or int(row["residue_label"]) != int(debt["residue_label"])
            ):
                raise AssertionError("support debt phase height/label mismatch")
            link_key = key_prefix[:4] + (q,)
            if link_key in used:
                raise AssertionError("support debt phase row was reused")
            used.add(link_key)
            links.append(
                {
                    "channel": [
                        key_prefix[0],
                        key_prefix[1],
                        key_prefix[2],
                        key_prefix[3],
                    ],
                    "q": q,
                    "obstruction_height": height,
                    "residue_label": int(row["residue_label"]),
                    "normalized_unit": int(row["normalized_unit"]),
                    "unit_modulus": int(row["unit_modulus"]),
                }
            )
    all_phase_keys = {
        (
            int(row["prime"]),
            int(row["A"]),
            int(row["M"]),
            str(row["side"]),
            int(row["q"]),
        )
        for row in phase_rows
    }
    if used != all_phase_keys:
        raise AssertionError("not every phase debt row was linked")
    summary = {
        key: phase[key]
        for key in (
            "obstruction_row_count",
            "q_group_count",
            "phase_cell_count",
            "compatible_pair_count",
            "pair_count",
            "capacity_overload_cell_count",
        )
    }
    descriptor = {
        "family": "overflow_support_debt_phase_bridge",
        "phase_input_sha256": phase.get("input_sha256"),
        "link_count": len(links),
    }
    result = {
        "state_id": "family:" + canonical_hash(descriptor),
        "scope": "cross_state_overflow_support_debt_phase_audit",
        "equation_target": {"relation": "pn=4Md+1"},
        "certificate_context": {
            "certificate_type": "overflow_support_debt_phase_bridge",
            "phase": "CONDITIONAL_CAPACITY_AUDIT",
            "source": PHASE_INPUT.name,
            "proof_boundary": "debt_to_phase_unit_identity_only",
            "alternate_phase_mapping_status": "unproved",
        },
        "support_debt_phase_summary": {
            "linked_row_count": len(links),
            "phase_summary": summary,
            "links": links,
        },
        "marked_solution_set": {
            "status": "not_carried",
            "reason": "phase-unit matching has no alternate lift witness",
        },
        "target_fiber": {
            "status": "not_carried",
            "reason": "conditional phase capacity evidence",
        },
        "signed_defect": {"status": "not_carried"},
        "potential_record": {
            "status": "absent",
            "reason": "phase-unit matching does not provide E5",
        },
        "selected_branch": "overflow_support_debt_phase_bridge",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "e1_e5": {f"E{i}": False for i in range(1, 6)},
        "proof_boundary": "conditional_phase_capacity_only",
        "scope_note": (
            "Each non-unit RESET debt is matched to its exact normalized q-adic residue unit. "
            "The matching is not an assertion that an alternate/source-switch uses that unit "
            "as a clearing phase."
        ),
        "source_receipt": {
            "phase_file": PHASE_INPUT.name,
            "phase_sha256": sha256(PHASE_INPUT),
        },
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


def overflow_fixture_rows(payload: dict[str, object]) -> list[dict[str, object]]:
    overflow_dual = payload.get("overflow_dual")
    if not isinstance(overflow_dual, dict):
        raise AssertionError("overflow dual payload shape changed")
    rows: list[dict[str, object]] = []

    def add(name: str, prime: int, support: int, row: object) -> None:
        if not isinstance(row, dict):
            raise AssertionError(f"overflow fixture row changed: {name}")
        data = dict(row["overflow"] if "overflow" in row else row)
        data.update({"name": name, "prime": prime, "A": support})
        rows.append(data)

    add("accumulated_d_one_boundary", 73, 7, overflow_dual["accumulated_d_one_boundary"])
    add(
        "accumulated_positive_fixed_n_edge",
        409,
        5,
        overflow_dual["accumulated_positive_fixed_n_edge"],
    )
    add("empty_fixed_n_window", 241, 38, overflow_dual["empty_fixed_n_window"])
    full_menu = overflow_dual["reachable_accumulated_full_menu_conflict"]
    if not isinstance(full_menu, dict):
        raise AssertionError("reachable conflict fixture changed")
    bundles = full_menu.get("bundle_receipts")
    if not isinstance(bundles, list):
        raise AssertionError("reachable conflict bundles changed")
    for index, row in enumerate(bundles):
        add(f"reachable_conflict_bundle_{index}", 73, 19, row)

    root_edges = overflow_dual.get("root_edges")
    if not isinstance(root_edges, list):
        raise AssertionError("root edge fixtures changed")
    for index, row in enumerate(root_edges):
        if not isinstance(row, dict):
            raise AssertionError("root edge row changed")
        add(f"root_edge_{index}", int(row["prime"]), 1, row)

    cycle = overflow_dual["lcm_dual_cycle"]
    if not isinstance(cycle, dict) or not isinstance(cycle.get("steps"), list):
        raise AssertionError("lcm cycle fixtures changed")
    for index, row in enumerate(cycle["steps"]):
        add(f"lcm_cycle_step_{index}", 73, 66, row)

    add(
        "symmetric_small_chart_support_conflict",
        241,
        8,
        overflow_dual["symmetric_small_chart_support_conflict"],
    )
    if len(rows) != 12:
        raise AssertionError(f"overflow fixture count changed: {len(rows)}")
    return rows


def overflow_direct_type_ii(payload: dict[str, object]) -> dict[str, object]:
    """Reconstruct the established p+4 Type II certificate for overflow fixtures."""
    receipts: list[dict[str, object]] = []
    rows = overflow_fixture_rows(payload)
    for fixture in rows:
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        if prime % 24 != 1:
            raise AssertionError(f"direct p+4 branch received a non-core prime: {name}")
        p_plus_four = prime + 4
        candidates = [
            factor
            for factor, _ in factorization(p_plus_four)
            if factor % 4 == 3
        ]
        if not candidates:
            receipts.append(
                {
                    "fixture_name": name,
                    "prime": prime,
                    "selector_status": "analysis_evidence",
                    "recursive_edge_eligible": False,
                    "certificate_type": "direct_type_ii_p_plus_four",
                    "proof_boundary": "p_plus_four_factor_filter",
                    "missing_conditions": ["q_congruent_3_mod_4_factor"],
                }
            )
            continue
        gap = min(candidates)
        x = (prime + gap) // 4
        if (prime + gap) % 4 or (x + 1) % gap:
            raise AssertionError(f"p+4 Type II congruence changed: {name}")
        y = prime * (x + 1) // gap
        z = prime * x * (x + 1) // gap
        if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, prime):
            raise AssertionError(f"p+4 Type II identity changed: {name}")
        receipt = {
            "fixture_name": name,
            "prime": prime,
            "certificate_type": "direct_type_ii_p_plus_four",
            "selector_status": "terminal_leaf",
            "state_class": "hit",
            "recursive_edge_eligible": False,
            "proof_boundary": "p_plus_four_type_ii_certificate",
            "gap": gap,
            "source_factorization": factorization(p_plus_four),
            "type_ii_parameters": {"m": gap, "x": x, "d": 1},
            "denominators": [x, y, z],
            "identity": {
                "equation": "4/p=1/x+1/y+1/z",
                "verified_exactly": True,
            },
            "scope_note": (
                "Established p+4 Type II certificate; this direct branch has precedence "
                "over overflow descent for the same prime."
            ),
        }
        check_status_boundary(receipt)
        receipts.append(receipt)
    verified = [receipt for receipt in receipts if receipt["selector_status"] == "terminal_leaf"]
    rejected = [receipt for receipt in receipts if receipt["selector_status"] != "terminal_leaf"]
    return {
        "fixture_count": len(receipts),
        "verified_terminal_count": len(verified),
        "d_one_fixture_count": sum(int(fixture["d"]) == 1 for fixture in rows),
        "d_one_direct_terminal_count": sum(
            int(fixture["d"]) == 1
            and any(
                receipt["fixture_name"] == fixture["name"]
                and receipt["selector_status"] == "terminal_leaf"
                for receipt in verified
            )
            for fixture in rows
        ),
        "verified_receipts": verified,
        "rejected_fixtures": rejected,
        "certificate_family": "p_plus_four_type_ii_sqrt_bound",
        "scope_note": (
            "Focused direct Type II reconstruction for the stored overflow fixtures. "
            "It does not assert that every core prime has a 3 mod 4 factor in p+4."
        ),
    }


def high_carrier_complement_classification(
    prime: int, carrier: int, dual_carrier: int
) -> dict[str, object]:
    """Classify the high-carrier complement before the remaining overflow menu.

    The determinant gives n=(4*M*d+1)/p.  If M>B_p, then M*d>B_p, while
    n is 1 mod 4; values n<=p-4 are impossible.  Thus the exact boundary
    is n=p or n>=p+4.  A 3 mod 4 factor of p+4 gives the exact standard
    Type II certificate; otherwise this branch records a hard-core boundary.
    """
    if prime <= 1 or prime % 24 != 1:
        raise AssertionError("high-carrier classification requires a core prime")
    if carrier <= 0 or dual_carrier <= 0 or dual_carrier >= prime:
        raise AssertionError("high-carrier determinant coordinates are out of range")
    determinant = 4 * carrier * dual_carrier + 1
    if determinant % prime:
        raise AssertionError("high-carrier determinant is not divisible by p")
    n = determinant // prime
    R_M = 4 * carrier - n
    if R_M <= prime:
        raise AssertionError("high-carrier classifier received a non-overflow row")
    B_prime = (prime - 1) ** 2 // 4
    base = {
        "prime": prime,
        "carrier": carrier,
        "dual_carrier": dual_carrier,
        "n": n,
        "R_M": R_M,
        "B_p": B_prime,
        "high_carrier": carrier > B_prime,
    }
    if carrier <= B_prime:
        return {
            **base,
            "applicable": False,
            "proof_boundary": "carrier_inside_outer_rank_domain",
            "selector_status": "analysis_evidence",
            "recursive_edge_eligible": False,
        }

    if n % 4 != 1:
        raise AssertionError("determinant complement lost n=1 mod 4")
    # M>B_p implies M*d>B_p.  For n<=p-4 (the largest n below p in this
    # congruence class), (p*n-1)/4 < B_p.  The value n=p is possible and is
    # therefore retained as a separate exact-complement boundary.
    if n < prime:
        raise AssertionError("high-carrier complement bound changed")
    p_plus_four = prime + 4
    q3_factors = [q for q, _ in factorization(p_plus_four) if q % 4 == 3]
    return {
        **base,
        "applicable": True,
        "complement_bound": {
            "necessary_condition": "n=p or n>=p+4",
            "case": "n=p" if n == prime else "n>=p+4",
            "verified": True,
            "p_plus_four": p_plus_four,
            "factorization": factorization(p_plus_four),
            "q_congruent_3_mod_4": q3_factors,
        },
        "direct_terminal_available": bool(q3_factors),
        "selector_status": "terminal_leaf" if q3_factors else "analysis_evidence",
        "recursive_edge_eligible": False,
        "proof_boundary": (
            "high_carrier_p_plus_four_type_ii"
            if q3_factors
            else "high_carrier_p_plus_four_factor_filter"
        ),
    }


def overflow_high_carrier_p_plus_four_complement(
    payload: dict[str, object],
) -> dict[str, object]:
    """Route high-carrier overflow through the p+4 Type II complement."""
    receipts: list[dict[str, object]] = []
    for fixture in overflow_fixture_rows(payload):
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        carrier = int(fixture["M"])
        dual_carrier = int(fixture["d"])
        classification = high_carrier_complement_classification(
            prime, carrier, dual_carrier
        )
        if not classification["applicable"]:
            receipts.append(
                {
                    "fixture_name": name,
                    "classification": classification,
                    "certificate_type": "overflow_high_carrier_p_plus_four_complement",
                    "selector_status": "analysis_evidence",
                    "recursive_edge_eligible": False,
                    "proof_boundary": "carrier_inside_outer_rank_domain",
                }
            )
            continue

        q3_factors = classification["complement_bound"]["q_congruent_3_mod_4"]
        if not q3_factors:
            receipts.append(
                {
                    "fixture_name": name,
                    "classification": classification,
                    "certificate_type": "overflow_high_carrier_p_plus_four_complement",
                    "selector_status": "analysis_evidence",
                    "recursive_edge_eligible": False,
                    "proof_boundary": "high_carrier_p_plus_four_factor_filter",
                    "missing_conditions": ["q_congruent_3_mod_4_factor"],
                }
            )
            continue

        gap = min(int(q) for q in q3_factors)
        p_plus_four = prime + 4
        x = (prime + gap) // 4
        if (prime + gap) % 4 or (x + 1) % gap:
            raise AssertionError(f"high-carrier Type II congruence changed: {name}")
        y = prime * (x + 1) // gap
        z = prime * x * (x + 1) // gap
        if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, prime):
            raise AssertionError(f"high-carrier Type II identity changed: {name}")
        receipt = {
            "fixture_name": name,
            "classification": classification,
            "certificate_type": "overflow_high_carrier_p_plus_four_complement",
            "state_class": "hit",
            "selector_status": "terminal_leaf",
            "recursive_edge_eligible": False,
            "proof_boundary": "high_carrier_p_plus_four_type_ii",
            "gap": gap,
            "source_factorization": factorization(p_plus_four),
            "type_ii_parameters": {"m": gap, "x": x, "d": 1},
            "denominators": [x, y, z],
            "identity": {
                "equation": "4/p=1/x+1/y+1/z",
                "verified_exactly": True,
            },
            "scope_note": (
                "The high-carrier complement is checked before overflow descent; this is a "
                "terminal certificate for the p+4 factor subfamily, not a universal p+4 claim."
            ),
        }
        check_status_boundary(receipt)
        receipts.append(receipt)

    return {
        "fixture_count": len(receipts),
        "high_carrier_count": sum(
            int(receipt["classification"]["high_carrier"]) for receipt in receipts
        ),
        "not_applicable_count": sum(
            int(not receipt["classification"]["high_carrier"]) for receipt in receipts
        ),
        "verified_terminal_count": sum(
            int(receipt["selector_status"] == "terminal_leaf") for receipt in receipts
        ),
        "hard_core_count": sum(
            int(receipt["proof_boundary"] == "high_carrier_p_plus_four_factor_filter")
            for receipt in receipts
        ),
        "receipts": receipts,
        "scope_note": (
            "The determinant complement bound is unconditional for high-carrier overflow. "
            "Only rows with a 3 mod 4 factor in p+4 close in this branch; the remaining "
            "factor-filter rows stay analysis evidence and require another Type I/II, alternate, "
            "capacity, or well-founded reset argument."
        ),
    }


def overflow_d_one_p_minus_two_g_rechart(payload: dict[str, object]) -> dict[str, object]:
    """Record the universal G rechart forced by the d=1 determinant branch.

    This is an arithmetic classification, not a recursive edge: the canonical
    small chart loses the old charged support and its target fiber is empty.
    """
    rows = [row for row in overflow_fixture_rows(payload) if int(row["d"]) == 1]
    receipts: list[dict[str, object]] = []
    for fixture in rows:
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        carrier = int(fixture["M"])
        n = int(fixture["n"])
        if prime % 24 != 1 or prime * n != 4 * carrier + 1 or n % 4 != 1:
            raise AssertionError(f"d=1 determinant normal form changed: {name}")
        r = (prime - 1) // 4
        if carrier % prime != r:
            raise AssertionError(f"d=1 residue reduction changed: {name}")
        chart_R, chart_K = canonical_chart(prime, r)
        expected_R = prime - 2
        expected_K = (prime - 1) ** 2 // 4
        if (chart_R, chart_K) != (expected_R, expected_K) or chart_K != 4 * r * r:
            raise AssertionError(f"d=1 p-2 chart changed: {name}")

        support_values = {
            str(q): jacobi_symbol(q, chart_R)
            for q, _ in factorization(chart_K)
        }
        if any(value != 1 for value in support_values.values()):
            raise AssertionError(f"d=1 G separator failed: {name}")
        target_minus_one = jacobi_symbol(-1, chart_R)
        if target_minus_one != -1:
            raise AssertionError(f"d=1 target Jacobi separator changed: {name}")

        source = [prime, chart_R * (prime - 1) - prime, prime - 1]
        if source[0] + source[1] != chart_R * source[2] or gcd(source[0], source[1]) != 1:
            raise AssertionError(f"d=1 universal source changed: {name}")
        destination = (
            source[0] // prime,
            (source[1] + chart_R) // prime,
            (source[2] + 1) // prime,
        )
        if destination != (1, chart_R - 1, 1):
            raise AssertionError(f"d=1 universal anchor changed: {name}")

        p_plus_four = prime + 4
        p_plus_four_candidates = [
            factor for factor, _ in factorization(p_plus_four) if factor % 4 == 3
        ]
        descriptor = {
            "equation_target": [4, prime],
            "source_carrier": carrier,
            "d": 1,
            "rechart_support": r,
        }
        receipt = {
            "edge_id": "edge:" + canonical_hash(descriptor),
            "certificate_type": "overflow_d_one_p_minus_two_g_rechart",
            "phase": "OVERFLOW_DUAL_DETERMINANT",
            "state_class": "G",
            "source_state": {
                "equation_target": [4, prime],
                "carrier": carrier,
                "R": int(fixture["R_M"]),
                "K": int(fixture["K_M"]),
                "d": 1,
            },
            "successor_state": {
                "equation_target": [4, prime],
                "R": chart_R,
                "K": chart_K,
                "charged_support": r,
                "state_class": "G",
            },
            "equation_target": {"numerator": 4, "denominator": prime},
            "g_separator": {
                "support_values": support_values,
                "target_minus_one": target_minus_one,
                "support_factorization": factorization(chart_K),
            },
            "universal_source": {
                "source": source,
                "q": prime,
                "shift": 1,
                "destination": list(destination),
                "gcd_reduction": 1,
            },
            "p_plus_four_probe": {
                "factorization": factorization(p_plus_four),
                "q_congruent_3_mod_4": p_plus_four_candidates,
                "direct_terminal_available": bool(p_plus_four_candidates),
            },
            "marked_solution_set": {
                "status": "empty_in_support_group",
                "reason": "Jacobi support separator at R=p-2",
            },
            "target_fiber": {
                "status": "empty",
                "reason": "-1 is outside the subgroup generated by K support",
            },
            "signed_defect": {"status": "not_applicable", "reason": "G state"},
            "potential_record": {"status": "absent", "reason": "support is not preserved"},
            "e1_e5": {f"E{i}": False for i in range(1, 6)},
            "selector_status": "analysis_evidence",
            "recursive_edge_eligible": False,
            "lift_status": "unproved",
            "proof_boundary": "d_one_p_minus_two_g_rechart",
            "scope_note": (
                "For every d=1 overflow, the dual residue is (p-1)/4 and the canonical chart "
                "is the universal G state (p-2,(p-1)^2/4).  A p+4 Type II factor, when present, "
                "is a separate terminal-first branch; the G rechart itself is not a recursive edge."
            ),
        }
        check_status_boundary(receipt)
        receipts.append(receipt)
    return {
        "fixture_count": len(rows),
        "g_rechart_count": len(receipts),
        "p_plus_four_terminal_probe_count": sum(
            receipt["p_plus_four_probe"]["direct_terminal_available"] for receipt in receipts
        ),
        "receipts": receipts,
        "normal_form": {
            "determinant": "p*n=4*M+1",
            "residue": "M mod p=(p-1)/4",
            "canonical_chart": "R=p-2; K=(p-1)^2/4",
            "jacobi_separator": "(q/(p-2))=1 for every q|K; (-1/(p-2))=-1",
        },
        "scope_note": (
            "The d=1 branch is universally classified as a p-2 G rechart. This removes any "
            "claim that d=1 alone supplies a support-preserving descent; closure still requires "
            "a separate Type I/II certificate or a non-support marked construction."
        ),
    }


def overflow_menu_receipts(
    overflow_payload: dict[str, object], qadic_payload: dict[str, object]
) -> dict[str, object]:
    """Classify the fixed-n/dual menu without promoting a negative row.

    For L=A*t, the fixed-n window is exactly the open interval
    n < 4*A*t < p+n with t | S/A.  A hard-core row records all divisor data
    needed to replay an empty interval together with the uncapped q-adic
    deficits from both dual channels.
    """
    if qadic_payload.get("input_sha256") != sha256(OVERFLOW_INPUT):
        raise AssertionError("q-adic ledger is stale relative to overflow input")
    qadic_cases = qadic_payload.get("cases")
    if not isinstance(qadic_cases, list) or len(qadic_cases) != 12:
        raise AssertionError("q-adic case count changed")
    qadic_by_name: dict[str, dict[str, object]] = {}
    for case in qadic_cases:
        if not isinstance(case, dict) or not isinstance(case.get("name"), str):
            raise AssertionError("q-adic case shape changed")
        qadic_by_name[str(case["name"])] = case

    receipts: list[dict[str, object]] = []
    counts: dict[str, int] = {}
    support_preserving_channel_count = 0
    for fixture in overflow_fixture_rows(overflow_payload):
        name = str(fixture["name"])
        qadic_case = qadic_by_name.get(name)
        if qadic_case is None:
            raise AssertionError(f"q-adic case missing: {name}")
        channels = qadic_case.get("channels")
        if not isinstance(channels, list) or len(channels) != 2:
            raise AssertionError(f"dual channel count changed: {name}")

        prime = int(fixture["prime"])
        support = int(fixture["A"])
        M = int(fixture["M"])
        R_M = int(fixture["R_M"])
        K_M = int(fixture["K_M"])
        n = int(fixture["n"])
        d = int(fixture["d"])
        S = M * d
        if S % support or K_M % support:
            raise AssertionError(f"charged support does not divide overflow: {name}")
        normalized_size = S // support
        all_t = divisors(normalized_size)
        eligible_t = [
            t for t in all_t if t > 1 and n < 4 * support * t < prime + n
        ]
        eligible_candidates: list[dict[str, int]] = []
        for t in eligible_t:
            L = support * t
            R_L = 4 * L - n
            K_L = L * (prime - S // L)
            if canonical_chart(prime, L) != (R_L, K_L):
                raise AssertionError(f"fixed-n chart changed: {name}, t={t}")
            eligible_candidates.append({"t": t, "L": L, "R_L": R_L, "K_L": K_L})
        below = [t for t in all_t if t > 1 and 4 * support * t <= n]
        above = [t for t in all_t if t > 1 and 4 * support * t >= prime + n]

        normalized_channels: list[dict[str, object]] = []
        for channel in channels:
            if not isinstance(channel, dict):
                raise AssertionError(f"dual channel shape changed: {name}")
            q_layers = channel.get("q_layers")
            if not isinstance(q_layers, list):
                raise AssertionError(f"q-layer shape changed: {name}")
            normalized_channels.append(
                {
                    "side": channel["side"],
                    "carrier": int(channel["carrier"]),
                    "chart_R": int(channel["chart_R"]),
                    "small_chart": bool(channel["small_chart"]),
                    "strict_gain": bool(channel["strict_gain"]),
                    "support_obstruction": int(channel["support_obstruction"]),
                    "support_preserving_edge": bool(channel["support_preserving_edge"]),
                    "q_deficits": [
                        {
                            "q": int(row["q"]),
                            "support_exponent": int(row["support_exponent"]),
                            "carrier_height": int(row["carrier_height"]),
                            "residue_height": int(row["residue_height"]),
                            "paid_height_capped": int(row["paid_height_capped"]),
                            "obstruction_height": int(row["obstruction_height"]),
                        }
                        for row in q_layers
                    ],
                }
            )

        fixed_n_nonempty = bool(eligible_t)
        support_preserving = [
            channel for channel in normalized_channels if channel["support_preserving_edge"]
        ]
        support_preserving_channel_count += len(support_preserving)
        small_reset = [
            channel
            for channel in normalized_channels
            if channel["small_chart"] and channel["strict_gain"]
        ]
        if fixed_n_nonempty:
            classification = "fixed_n_window_nonempty"
        elif support_preserving:
            classification = "dual_support_preserving"
        else:
            classification = "hard_core_fixed_n_gap_and_dual_obstruction"
        counts[classification] = counts.get(classification, 0) + 1

        fixed_n_gap = {
            "S": S,
            "normalized_S_over_A": normalized_size,
            "factorization_S_over_A": factorization(normalized_size),
            "divisor_count": len(all_t),
            "divisors_t": all_t,
            "interval": {
                "lower_numerator": n,
                "upper_numerator": prime + n,
                "scale": 4 * support,
                "strict": True,
            },
            "eligible_t": eligible_t,
            "eligible_candidates": eligible_candidates,
            "predecessor_t": max(below) if below else None,
            "successor_t": min(above) if above else None,
            "empty_verified": not fixed_n_nonempty,
        }
        for key in ("predecessor_t", "successor_t"):
            t = fixed_n_gap[key]
            fixed_n_gap[f"{key}_value"] = None if t is None else 4 * support * int(t)

        descriptor = {
            "equation_target": [4, prime],
            "overflow_support": support,
            "M": M,
            "R_M": R_M,
            "K_M": K_M,
            "classification": classification,
        }
        receipt = {
            "hard_core_id": "hard-core:" + canonical_hash(descriptor),
            "fixture_name": name,
            "state_descriptor": descriptor,
            "overflow_determinant": {
                "pn": prime * n,
                "four_M_d_plus_1": 4 * M * d + 1,
                "n": n,
                "d": d,
            },
            "fixed_n_gap": fixed_n_gap,
            "dual_obstruction": {
                "channels": normalized_channels,
                "support_preserving_channel_count": len(support_preserving),
                "small_reset_channel_count": len(small_reset),
                "both_channels_obstructed": not support_preserving,
            },
            "selected_branch": (
                "overflow_hard_core_gap_obstruction"
                if classification == "hard_core_fixed_n_gap_and_dual_obstruction"
                else classification
            ),
            "selector_status": "analysis_evidence",
            "recursive_edge_eligible": False,
            "e1_e5": {f"E{i}": False for i in range(1, 6)},
            "proof_boundary": "finite_menu_negative_receipt",
            "scope_note": (
                "This receipt proves only that the fixed-n divisor menu and both local dual "
                "support-preserving channels fail for this fixture. A smaller carrier reset, "
                "alternate source, or direct Type I/II certificate is not ruled out."
            ),
        }
        check_status_boundary(receipt)
        receipts.append(receipt)

    hard_core = [
        receipt
        for receipt in receipts
        if receipt["selected_branch"] == "overflow_hard_core_gap_obstruction"
    ]
    return {
        "fixture_count": len(receipts),
        "classification_counts": counts,
        "support_preserving_channel_count": support_preserving_channel_count,
        "hard_core_count": len(hard_core),
        "receipts": receipts,
        "hard_core_receipts": hard_core,
        "scope_note": (
            "The hard-core label is a typed negative boundary for the focused menu, not a "
            "proof that the underlying overflow state has no valid successor."
        ),
    }


def overflow_fixed_n_outer_rank(payload: dict[str, object]) -> dict[str, object]:
    """Promote fixed-n determinant charts even when the target remains overflow."""
    verified: list[dict[str, object]] = []
    rejected: list[dict[str, object]] = []
    rows = overflow_fixture_rows(payload)
    for fixture in rows:
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        support = int(fixture["A"])
        source_carrier = int(fixture["M"])
        source_R = int(fixture["R_M"])
        source_K = int(fixture["K_M"])
        n = int(fixture["n"])
        d = int(fixture["d"])
        S = source_carrier * d
        B_prime = (prime - 1) ** 2 // 4
        joined_support = lcm(support, d)
        if S % joined_support:
            raise AssertionError(f"fixed-n outer support is not a divisor: {name}")
        target_R = 4 * joined_support - n
        target_K = joined_support * (prime - S // joined_support)
        target_positive = target_R > 0
        chart_match = (
            target_positive
            and canonical_chart(prime, joined_support) == (target_R, target_K)
        )
        strict_gain = joined_support > support
        source_potential = B_prime // support
        successor_potential = (
            B_prime // joined_support if joined_support > 0 else source_potential
        )
        strict_potential = successor_potential < source_potential
        source_in_domain = support <= B_prime
        if (
            source_in_domain
            and target_positive
            and chart_match
            and strict_gain
            and strict_potential
        ):
            target_class = "marked_absorb" if target_R < prime else "overflow"
            source_state = {
                "equation_target": [4, prime],
                "R": source_R,
                "K": source_K,
                "absorbed_support": support,
                "state_class": "overflow",
            }
            target_state = {
                "equation_target": [4, prime],
                "R": target_R,
                "K": target_K,
                "absorbed_support": joined_support,
                "state_class": target_class,
            }
            receipt = {
                "edge_id": "edge:" + canonical_hash(
                    {"source": source_state, "successor": target_state}
                ),
                "certificate_type": "overflow_fixed_n_outer_rank_reset",
                "phase": "OVERFLOW_DETERMINANT",
                "state_class": target_class,
                "source_state": source_state,
                "successor_state": target_state,
                "equation_target": {"numerator": 4, "denominator": prime},
                "marked_solution_set": {
                    "source": "Sol(p)",
                    "successor": "Sol(p)",
                    "lift": "identity",
                },
                "target_fiber": {
                    "status": "inherited_full_solution_set",
                    "reason": "fixed-n determinant identity with chart-independent marking",
                },
                "signed_defect": {"status": "not_applicable", "reason": "identity lift"},
                "certificate_context": {
                    "source": OVERFLOW_INPUT.name,
                    "provenance": "overflow_determinant_fixed_n_window_extension",
                    "fixture_name": name,
                    "determinant": {
                        "pn": prime * n,
                        "four_M_d_plus_1": 4 * source_carrier * d + 1,
                        "M": source_carrier,
                        "d": d,
                        "S": S,
                    },
                    "selected_candidate": {
                        "L": joined_support,
                        "R_L": target_R,
                        "K_L": target_K,
                    },
                    "window_position": "inside" if target_R < prime else "above",
                },
                "normal_form": "overflow_fixed_n_outer_rank_reset_v1",
                "induction_rank": {
                    "kind": "absorbed_support_potential",
                    "source": source_potential,
                    "successor": successor_potential,
                },
                "potential_record": {
                    "B_p": B_prime,
                    "source_support": support,
                    "successor_support": joined_support,
                    "source_value": source_potential,
                    "successor_value": successor_potential,
                    "strict_decrease": strict_potential,
                    "support_monotone": strict_gain,
                },
                "e1_e5": {f"E{i}": True for i in range(1, 6)},
                "selector_status": "verified_edge",
                "recursive_edge_eligible": True,
                "lift_status": "proved_identity",
                "proof_boundary": (
                    "fixed_n_absorption"
                    if target_class == "marked_absorb"
                    else "fixed_n_overflow_rank_descent"
                ),
                "scope_note": (
                    "The fixed-n determinant chart is valid above the R<p window as an "
                    "overflow state; the joined support strictly lowers the outer rank."
                ),
            }
            check_status_boundary(receipt)
            verified.append(receipt)
            continue

        missing: list[str] = []
        if not source_in_domain:
            missing.append("source_potential_domain")
        if not target_positive:
            missing.append("positive_target_chart")
        if target_positive and not chart_match:
            missing.append("fixed_n_chart_identity")
        if not strict_gain:
            missing.append("strict_support_gain")
        if not strict_potential:
            missing.append("strict_potential_decrease")
        rejected.append(
            {
                "fixture_name": name,
                "equation_target": [4, prime],
                "source_carrier": source_carrier,
                "dual_carrier": d,
                "source_support": support,
                "joined_support": joined_support,
                "candidate_chart": {
                    "R": target_R,
                    "K": target_K,
                    "positive": target_positive,
                },
                "missing_conditions": missing,
                "selector_status": "analysis_evidence",
                "recursive_edge_eligible": False,
                "proof_boundary": "fixed_n_overflow_rank_filter",
            }
        )
    return {
        "fixture_count": len(rows),
        "verified_edge_count": len(verified),
        "absorption_target_count": sum(
            receipt["state_class"] == "marked_absorb" for receipt in verified
        ),
        "overflow_target_count": sum(
            receipt["state_class"] == "overflow" for receipt in verified
        ),
        "rejected_fixture_count": len(rejected),
        "verified_receipts": verified,
        "rejected_fixtures": rejected,
        "rank_definition": {
            "kind": "absorbed_support_potential",
            "formula": "floor(((p-1)^2)/4 / A)",
            "candidate": "L=lcm(A,d)",
            "target_formula": "R_L=4L-n; K_L=L*(p-M*d/L)",
            "acceptance": (
                "L>A, R_L>0, canonical_chart(p,L)=(R_L,K_L), "
                "and strict potential decrease"
            ),
        },
        "scope_note": (
            "This branch extends the fixed-n determinant menu above the R<p window. "
            "It does not assert that every overflow has a positive candidate."
        ),
    }


def overflow_fixed_n_bounded_divisor_outer_rank(
    payload: dict[str, object],
) -> dict[str, object]:
    """Use any bounded fixed-n divisor, not only lcm(A,d), as a rank edge.

    For S=M*d=(p*n-1)/4 and L|S, the determinant identity gives
    R_L=4*L-n and K_L=L*(p-S/L).  The positivity condition 4*L>n
    forces S/L<p, so every bounded L satisfying the support and potential
    inequalities is a legal identity-lift successor.
    """
    verified: list[dict[str, object]] = []
    rejected: list[dict[str, object]] = []
    rows = overflow_fixture_rows(payload)
    for fixture in rows:
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        support = int(fixture["A"])
        source_carrier = int(fixture["M"])
        source_R = int(fixture["R_M"])
        source_K = int(fixture["K_M"])
        n = int(fixture["n"])
        d = int(fixture["d"])
        S = source_carrier * d
        B_prime = (prime - 1) ** 2 // 4
        source_in_domain = 0 < support <= B_prime
        source_potential = B_prime // support if source_in_domain else 0
        candidates: list[tuple[int, int, int]] = []
        if source_in_domain:
            for L in divisors(S):
                if L <= support or L > B_prime or 4 * L <= n:
                    continue
                target_R = 4 * L - n
                target_K = L * (prime - S // L)
                if target_K <= 0:
                    continue
                successor_potential = B_prime // L
                if successor_potential >= source_potential:
                    continue
                if canonical_chart(prime, L) != (target_R, target_K):
                    raise AssertionError(f"bounded fixed-n chart changed: {name}, L={L}")
                candidates.append((L, target_R, target_K))

        if candidates:
            L, target_R, target_K = max(candidates, key=lambda row: row[0])
            successor_potential = B_prime // L
            support_retained = L % support == 0
            target_class = "marked_absorb" if target_R < prime else "overflow"
            source_state = {
                "equation_target": [4, prime],
                "R": source_R,
                "K": source_K,
                "absorbed_support": support,
                "state_class": "overflow",
            }
            target_state = {
                "equation_target": [4, prime],
                "R": target_R,
                "K": target_K,
                "absorbed_support": L,
                "state_class": target_class,
            }
            receipt = {
                "edge_id": "edge:" + canonical_hash(
                    {"source": source_state, "successor": target_state}
                ),
                "certificate_type": "overflow_fixed_n_bounded_divisor_outer_rank",
                "phase": "OVERFLOW_DETERMINANT",
                "state_class": target_class,
                "source_state": source_state,
                "successor_state": target_state,
                "equation_target": {"numerator": 4, "denominator": prime},
                "marked_solution_set": {
                    "source": "Sol(p)",
                    "successor": "Sol(p)",
                    "lift": "identity",
                },
                "target_fiber": {
                    "status": "inherited_full_solution_set",
                    "reason": "fixed-n determinant identity with chart-independent marking",
                },
                "signed_defect": {"status": "not_applicable", "reason": "identity lift"},
                "certificate_context": {
                    "source": OVERFLOW_INPUT.name,
                    "provenance": "overflow_determinant_fixed_n_bounded_divisor",
                    "fixture_name": name,
                    "determinant": {
                        "pn": prime * n,
                        "four_M_d_plus_1": 4 * source_carrier * d + 1,
                        "M": source_carrier,
                        "d": d,
                        "S": S,
                    },
                    "selected_candidate": {
                        "L": L,
                        "R_L": target_R,
                        "K_L": target_K,
                        "candidate_count": len(candidates),
                        "selection_rule": "maximum admissible L",
                    },
                    "admissibility": {
                        "support_gain": "A<L",
                        "support_containment": "A|L when retained; otherwise paid outer-rank reset",
                        "bounded_support": "L<=B_p",
                        "positive_chart": "4L>n",
                        "strict_potential": "floor(B_p/L)<floor(B_p/A)",
                    },
                },
                "normal_form": "overflow_fixed_n_bounded_divisor_outer_rank_v1",
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
                    "support_monotone": support_retained,
                    "support_reset_paid": not support_retained,
                    "outer_rank_reset": not support_retained,
                },
                "high_carrier_R_descent": {
                    "condition": "M>B_p",
                    "applicable": source_carrier > B_prime,
                    "bounded_successor": (
                        "L<=B_p<M" if source_carrier > B_prime else "L<=B_p"
                    ),
                    "source_carrier": source_carrier,
                    "successor_carrier": L,
                    "source_R": source_R,
                    "successor_R": target_R,
                    "delta_R": source_R - target_R,
                    "identity": "R_M-R_L=4*(M-L)",
                    "strict_decrease": (
                        target_R < source_R if source_carrier > B_prime else False
                    ),
                },
                "e1_e5": {f"E{i}": True for i in range(1, 6)},
                "selector_status": "verified_edge",
                "recursive_edge_eligible": True,
                "lift_status": "proved_identity",
                "proof_boundary": (
                    "fixed_n_bounded_divisor_absorption"
                    if target_class == "marked_absorb"
                    else "fixed_n_bounded_divisor_overflow_rank_descent"
                ),
                "scope_note": (
                    "Any divisor L of S=M*d satisfying the bounded support, positive-chart, "
                    "and strict-potential conditions yields this identity-lift edge; the "
                    "selector chooses the largest admissible L deterministically. If A does "
                    "not divide L, the strict absorbed-support potential explicitly pays "
                    "the support reset."
                ),
            }
            check_status_boundary(receipt)
            verified.append(receipt)
            continue

        rejected.append(
            {
                "fixture_name": name,
                "equation_target": [4, prime],
                "source_carrier": source_carrier,
                "source_support": support,
                "S": S,
                "candidate_count": 0,
                "selector_status": "analysis_evidence",
                "recursive_edge_eligible": False,
                "proof_boundary": "fixed_n_bounded_divisor_rank_filter",
                "missing_conditions": (
                    ["source_potential_domain"] if not source_in_domain else ["admissible_L"]
                ),
            }
        )
    return {
        "fixture_count": len(rows),
        "verified_edge_count": len(verified),
        "absorption_target_count": sum(
            receipt["state_class"] == "marked_absorb" for receipt in verified
        ),
        "overflow_target_count": sum(
            receipt["state_class"] == "overflow" for receipt in verified
        ),
        "rejected_fixture_count": len(rejected),
        "verified_receipts": verified,
        "rejected_fixtures": rejected,
        "high_carrier_verified_edge_count": sum(
            int(
                receipt["certificate_context"]["determinant"]["M"]
                > (int(receipt["equation_target"]["denominator"]) - 1) ** 2 // 4
            )
            for receipt in verified
        ),
        "high_carrier_R_descent_count": sum(
            int(receipt["high_carrier_R_descent"]["strict_decrease"])
            for receipt in verified
        ),
        "rank_definition": {
            "kind": "absorbed_support_potential",
            "formula": "floor(((p-1)^2)/4 / A)",
            "candidate": "any L|M*d with A<L<=B_p and 4L>n",
            "target_formula": "R_L=4L-n; K_L=L*(p-M*d/L)",
            "selection_rule": "maximum admissible L",
            "acceptance": (
                "L|M*d, A<L<=B_p, 4L>n, canonical_chart(p,L)=(R_L,K_L), "
                "and strict potential decrease; A|L is optional only when the same "
                "potential explicitly pays an outer-rank reset"
            ),
            "high_carrier_secondary_rank": (
                "if M>B_p then every accepted L satisfies L<=B_p<M and "
                "R_L=4L-n<R_M=4M-n"
            ),
        },
        "scope_note": (
            "This is the complete bounded fixed-n divisor atlas above and inside the "
            "absorbed-support potential domain. An empty admissible set remains an open "
            "overflow boundary and is not promoted. When M>B_p, an accepted bounded "
            "successor also carries a strict canonical-R descent; this is conditional "
            "on the existence of the accepted divisor and does not supply that divisor."
        ),
    }


def overflow_same_chart_support_promotion(
    payload: dict[str, object],
) -> dict[str, object]:
    """Promote the bundle carrier itself when it lies inside the outer-rank domain.

    Complete-excess bundle construction supplies M/A >= 2.  If M <= B_p, the
    same canonical chart can carry support M, so no dual rechart or new target
    fiber is needed.
    """
    verified: list[dict[str, object]] = []
    rejected: list[dict[str, object]] = []
    for fixture in overflow_fixture_rows(payload):
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        support = int(fixture["A"])
        carrier = int(fixture["M"])
        source_R = int(fixture["R_M"])
        source_K = int(fixture["K_M"])
        n = int(fixture["n"])
        d = int(fixture["d"])
        B_prime = (prime - 1) ** 2 // 4
        if (
            support <= 0
            or carrier <= 0
            or carrier % support
            or carrier // support < 2
            or prime * n != 4 * carrier * d + 1
            or source_R != 4 * carrier - n
            or source_R <= prime
            or source_K != carrier * (prime - d)
            or source_K % carrier
        ):
            raise AssertionError(f"same-chart promotion source invariant changed: {name}")
        if carrier > B_prime:
            if prime % 4 != 1 or n % 4 != 1 or n < prime:
                raise AssertionError(f"high-carrier complement boundary changed: {name}")
            rejected.append(
                {
                    "fixture_name": name,
                    "equation_target": [4, prime],
                    "source_support": support,
                    "source_carrier": carrier,
                    "B_p": B_prime,
                    "selector_status": "analysis_evidence",
                    "recursive_edge_eligible": False,
                    "proof_boundary": "same_chart_support_promotion_domain",
                    "missing_conditions": ["carrier_above_B_p"],
                    "high_carrier_complement_boundary": {
                        "necessary_condition": "n=p or n>=p+4",
                        "case": "n=p" if n == prime else "n>=p+4",
                        "prime_mod_4": prime % 4,
                        "n_mod_4": n % 4,
                        "verified": True,
                    },
                }
            )
            continue
        source_potential = B_prime // support
        successor_potential = B_prime // carrier
        if carrier <= support or successor_potential >= source_potential:
            raise AssertionError(f"same-chart promotion rank changed: {name}")
        source_state = {
            "equation_target": [4, prime],
            "R": source_R,
            "K": source_K,
            "absorbed_support": support,
            "state_class": "overflow",
        }
        successor_state = {
            "equation_target": [4, prime],
            "R": source_R,
            "K": source_K,
            "absorbed_support": carrier,
            "state_class": "overflow",
        }
        receipt = {
            "edge_id": "edge:" + canonical_hash(
                {"source": source_state, "successor": successor_state}
            ),
            "certificate_type": "overflow_same_chart_support_promotion",
            "phase": "OVERFLOW_SUPPORT_PROMOTION",
            "state_class": "overflow",
            "source_state": source_state,
            "successor_state": successor_state,
            "equation_target": {"numerator": 4, "denominator": prime},
            "marked_solution_set": {
                "source": "Sol(p)",
                "successor": "Sol(p)",
                "lift": "identity",
            },
            "target_fiber": {
                "status": "inherited_full_solution_set",
                "reason": "same canonical chart; support metadata only is promoted",
            },
            "signed_defect": {"status": "not_applicable", "reason": "identity lift"},
            "certificate_context": {
                "source": OVERFLOW_INPUT.name,
                "provenance": "verified_overflow_source_atlas",
                "fixture_name": name,
                "determinant": {
                    "pn": prime * n,
                    "four_M_d_plus_1": 4 * carrier * d + 1,
                    "M": carrier,
                    "d": d,
                    "R_M": source_R,
                    "K_M": source_K,
                },
                "support_promotion": {
                    "source": support,
                    "successor": carrier,
                    "ratio_lower_bound": "M/A>=2",
                },
            },
            "normal_form": "overflow_same_chart_support_promotion_v1",
            "induction_rank": {
                "kind": "absorbed_support_potential",
                "source": source_potential,
                "successor": successor_potential,
            },
            "potential_record": {
                "B_p": B_prime,
                "source_support": support,
                "successor_support": carrier,
                "source_value": source_potential,
                "successor_value": successor_potential,
                "strict_decrease": True,
                "support_monotone": True,
            },
            "e1_e5": {f"E{i}": True for i in range(1, 6)},
            "selector_status": "verified_edge",
            "recursive_edge_eligible": True,
            "lift_status": "proved_identity",
            "proof_boundary": "same_chart_support_promotion",
            "scope_note": (
                "The overflow carrier M is already a divisor of K_M.  Promoting the "
                "absorbed support to M keeps the equation chart and Sol(p) unchanged; "
                "the target remains overflow, while the outer support potential strictly "
                "decreases."
            ),
        }
        check_status_boundary(receipt)
        verified.append(receipt)
    return {
        "fixture_count": len(verified) + len(rejected),
        "verified_edge_count": len(verified),
        "rejected_fixture_count": len(rejected),
        "verified_receipts": verified,
        "rejected_fixtures": rejected,
        "promotion_rule": {
            "source_condition": "M|K_M, A|M, M/A>=2, M<=B_p",
            "target": "same (p,R_M,K_M) chart with absorbed_support=M",
            "potential": "floor(B_p/M)<floor(B_p/A)",
        },
        "high_carrier_residual": {
            "condition": "M>B_p",
            "necessary_complement_bound": "n=p or n>=p+4",
            "proof": (
                "S=M*d=(p*n-1)/4>B_p; n<=p-4 forces S<B_p, while n=p "
                "is possible; together with n=1 mod 4 this leaves n=p or n>=p+4."
            ),
        },
        "scope_note": (
            "This closes every source-receipt overflow with A|M, M/A>=2 and carrier "
            "M in the outer-rank domain.  Rows with M>B_p remain outside this same-chart "
            "promotion and require another exit; they have n=p or n>=p+4."
        ),
    }


def overflow_a_one_generic_determinant_boundary(
    payload: dict[str, object],
) -> dict[str, object]:
    """Record the missing-hypothesis boundary for the old A=1 claim.

    This is an arithmetic boundary only: it has no raw Reach/source provenance
    and therefore cannot be used as a counterexample to Erdős--Straus.  It
    shows that the special choice L=d needs the additional M<p hypothesis.
    """
    del payload
    prime = 73
    M = 1297
    d = 29
    n = 2061
    support = 1
    B_prime = (prime - 1) ** 2 // 4
    S = M * d
    R_M = 4 * M - n
    K_M = M * (prime - d)
    residue = M % prime
    s = (4 * residue * d + 1) // prime
    dual_charts = {
        "d": {"t": d, "R": 4 * d - s, "K": d * (prime - residue)},
        "r": {"t": residue, "R": 4 * residue - s, "K": residue * (prime - d)},
    }
    all_divisors = divisors(S)
    bounded_divisors = [L for L in all_divisors if L <= B_prime]
    positive_candidates = [
        L
        for L in bounded_divisors
        if L > support and 4 * L > n and B_prime // L < B_prime // support
    ]
    if positive_candidates or bounded_divisors != [1, d]:
        raise AssertionError("A=1 generic determinant boundary changed")
    receipt = {
        "certificate_type": "overflow_a_one_generic_determinant_boundary",
        "phase": "OVERFLOW_DETERMINANT",
        "state_class": "overflow",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "equation_target": {"numerator": 4, "denominator": prime},
        "source_state": {
            "equation_target": [4, prime],
            "R": R_M,
            "K": K_M,
            "absorbed_support": support,
            "state_class": "overflow",
        },
        "determinant": {
            "p": prime,
            "M": M,
            "d": d,
            "n": n,
            "S": S,
            "R_M": R_M,
            "K_M": K_M,
            "B_p": B_prime,
            "identity": "p*n=4*M*d+1",
        },
        "factorization_S": factorization(S),
        "bounded_divisors": bounded_divisors,
        "positive_candidates": positive_candidates,
        "dual_parameters": {"r": residue, "s": s},
        "dual_charts": dual_charts,
        "selected_dual_reset": {"side": "d", **dual_charts["d"]},
        "small_carrier_candidate": {
            "L": d,
            "R_L": 4 * d - n,
            "K_L_formula": d * (prime - M),
            "positive_chart": False,
        },
        "failure_conditions": {
            "M_less_than_p": M < prime,
            "d_at_least_two": d >= 2,
            "small_carrier_positive": 4 * d > n,
            "bounded_positive_divisor_exists": bool(positive_candidates),
            "dual_reset_positive": dual_charts["d"]["R"] > 0,
            "dual_reset_below_p": dual_charts["d"]["R"] < prime,
            "dual_reset_support_gain": dual_charts["d"]["t"] > support,
        },
        "e1_e5": {f"E{i}": False for i in range(1, 6)},
        "marked_solution_set": {
            "status": "not_carried",
            "reason": "negative arithmetic boundary has no successor",
        },
        "target_fiber": {"status": "not_carried"},
        "signed_defect": {"status": "not_carried"},
        "potential_record": {
            "status": "absent",
            "reason": "no admissible bounded divisor",
        },
        "proof_boundary": "a_one_small_carrier_hypothesis_required",
        "scope_note": (
            "This tuple satisfies the overflow determinant identities but has no raw Reach or "
            "source provenance. It refutes only the unrestricted arithmetic claim that L=d "
            "always works for A=1; the d-side dual RESET (t=29,R=27) remains valid, and it is "
            "not an Erdos-Straus counterexample."
        ),
    }
    check_status_boundary(receipt)
    return receipt


def overflow_a_one_dual_reset_family(payload: dict[str, object]) -> dict[str, object]:
    """Replay the universal A=1 dual-carrier reset on focused source rows."""
    receipts: list[dict[str, object]] = []
    for fixture in overflow_fixture_rows(payload):
        if int(fixture["A"]) != 1:
            continue
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        M = int(fixture["M"])
        d = int(fixture["d"])
        n = int(fixture["n"])
        R_M = int(fixture["R_M"])
        K_M = int(fixture["K_M"])
        r = M % prime
        if (
            not 1 <= r < prime
            or not 1 <= d < prime
            or gcd(M, prime) != 1
            or prime * n != 4 * M * d + 1
        ):
            raise AssertionError(f"A=1 dual reset determinant changed: {name}")
        s_numerator = 4 * r * d + 1
        if s_numerator % prime:
            raise AssertionError(f"A=1 dual reset s changed: {name}")
        s = s_numerator // prime
        candidates: list[tuple[int, str, int, int]] = []
        for side, t, K_formula in (
            ("d", d, d * (prime - r)),
            ("r", r, r * (prime - d)),
        ):
            R_t = 4 * t - s
            K_t = K_formula
            if canonical_chart(prime, t) != (R_t, K_t):
                raise AssertionError(f"A=1 dual chart changed: {name}, side={side}")
            if t > 1 and R_t < prime:
                candidates.append((R_t, side, t, K_t))
        if not candidates:
            raise AssertionError(f"A=1 dual reset candidate disappeared: {name}")
        R_t, side, t, K_t = min(candidates)
        B_prime = (prime - 1) ** 2 // 4
        if t > B_prime or K_t % t or B_prime // t >= B_prime:
            raise AssertionError(f"A=1 dual reset rank changed: {name}")
        source_state = {
            "equation_target": [4, prime],
            "R": R_M,
            "K": K_M,
            "absorbed_support": 1,
            "state_class": "overflow",
        }
        target_state = {
            "equation_target": [4, prime],
            "R": R_t,
            "K": K_t,
            "absorbed_support": t,
            "state_class": "marked_absorb",
        }
        receipt = {
            "edge_id": "edge:" + canonical_hash(
                {"source": source_state, "successor": target_state}
            ),
            "certificate_type": "overflow_a_one_dual_outer_rank_reset",
            "phase": "RESET",
            "state_class": "marked_absorb",
            "source_state": source_state,
            "successor_state": target_state,
            "equation_target": {"numerator": 4, "denominator": prime},
            "marked_solution_set": {
                "source": "Sol(p)",
                "successor": "Sol(p)",
                "lift": "identity",
            },
            "certificate_context": {
                "fixture_name": name,
                "dual_side": side,
                "dual_parameters": {"r": r, "s": s},
                "dual_chart": {"t": t, "R": R_t, "K": K_t},
                "source_determinant": {
                    "M": M,
                    "d": d,
                    "n": n,
                    "R_M": R_M,
                    "K_M": K_M,
                    "identity": "p*n=4*M*d+1",
                },
                "provenance": "overflow_determinant_symmetric_dual",
            },
            "normal_form": "overflow_a_one_dual_outer_rank_reset_v1",
            "induction_rank": {
                "kind": "absorbed_support_potential",
                "source": B_prime,
                "successor": B_prime // t,
            },
            "potential_record": {
                "B_p": B_prime,
                "source_support": 1,
                "successor_support": t,
                "source_value": B_prime,
                "successor_value": B_prime // t,
                "strict_decrease": True,
                "support_monotone": True,
            },
            "e1_e5": {f"E{i}": True for i in range(1, 6)},
            "selector_status": "verified_edge",
            "recursive_edge_eligible": True,
            "lift_status": "proved_identity",
            "proof_boundary": "a_one_dual_reset_universal_subfamily",
            "scope_note": (
                "For A=1 the symmetric d/r chart theorem always supplies t>1 and R_t<p; "
                "this receipt replays the identity-lift RESET on the focused source rows."
            ),
        }
        check_status_boundary(receipt)
        receipts.append(receipt)
    return {
        "fixture_count": len(receipts),
        "verified_edge_count": len(receipts),
        "rejected_fixture_count": 0,
        "verified_receipts": receipts,
        "theorem": {
            "condition": "A=1, pn=4*M*d+1, R_M>p",
            "conclusion": "exists t in {d,r}: t>1, R_t<p, t|K_t, and strict Pi_A descent",
            "proof_boundary": "symmetric_dual_minimum_and_d_or_r_equals_one_split",
        },
        "scope_note": (
            "The algebraic theorem is universal for verified A=1 overflow; the stored rows are "
            "focused replays, not a finite proof of the theorem."
        ),
    }


def overflow_fixed_s_outer_rank(payload: dict[str, object]) -> dict[str, object]:
    """Audit the symmetric r-side fixed-s divisor atlas.

    Writing M=kp+r turns pn=4Md+1 into p*s=4*r*d+1 with
    s=n-4*k*d.  A divisor L of r*d therefore gives a second canonical
    chart, independent of the fixed-n chart used by the d-side branch.
    """
    verified: list[dict[str, object]] = []
    rejected: list[dict[str, object]] = []
    rows = overflow_fixture_rows(payload)
    for fixture in rows:
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        support = int(fixture["A"])
        source_carrier = int(fixture["M"])
        source_R = int(fixture["R_M"])
        source_K = int(fixture["K_M"])
        n = int(fixture["n"])
        d = int(fixture["d"])
        if not (
            support > 0
            and source_carrier > 0
            and source_carrier % support == 0
            and source_K % source_carrier == 0
            and prime * n == 4 * source_carrier * d + 1
            and source_R == 4 * source_carrier - n
        ):
            raise AssertionError(f"bounded fixed-s source invariant changed: {name}")
        residue = source_carrier % prime
        numerator = 4 * residue * d + 1
        integral_s = numerator % prime == 0
        fixed_s = numerator // prime if integral_s else None
        B_prime = (prime - 1) ** 2 // 4
        joined_support = lcm(support, residue) if residue > 0 else 0
        product = residue * d
        divides_product = joined_support > 0 and product % joined_support == 0
        target_R = 4 * joined_support - fixed_s if integral_s else None
        target_K = (
            joined_support * (prime - product // joined_support)
            if divides_product
            else None
        )
        target_positive = isinstance(target_R, int) and target_R > 0
        chart_match = bool(
            divides_product
            and target_positive
            and canonical_chart(prime, joined_support) == (target_R, target_K)
        )
        strict_gain = joined_support > support
        source_in_domain = support <= B_prime
        source_potential = B_prime // support
        successor_potential = (
            B_prime // joined_support if joined_support > 0 else source_potential
        )
        strict_potential = successor_potential < source_potential
        if (
            source_in_domain
            and 1 <= residue < prime
            and integral_s
            and divides_product
            and target_positive
            and chart_match
            and strict_gain
            and strict_potential
        ):
            assert isinstance(target_R, int)
            assert isinstance(target_K, int)
            target_class = "marked_absorb" if target_R < prime else "overflow"
            source_state = {
                "equation_target": [4, prime],
                "R": source_R,
                "K": source_K,
                "absorbed_support": support,
                "state_class": "overflow",
            }
            target_state = {
                "equation_target": [4, prime],
                "R": target_R,
                "K": target_K,
                "absorbed_support": joined_support,
                "state_class": target_class,
            }
            receipt = {
                "edge_id": "edge:" + canonical_hash(
                    {"source": source_state, "successor": target_state}
                ),
                "certificate_type": "overflow_fixed_s_outer_rank_reset",
                "phase": "OVERFLOW_DUAL_DETERMINANT",
                "state_class": target_class,
                "source_state": source_state,
                "successor_state": target_state,
                "equation_target": {"numerator": 4, "denominator": prime},
                "marked_solution_set": {
                    "source": "Sol(p)",
                    "successor": "Sol(p)",
                    "lift": "identity",
                },
                "target_fiber": {
                    "status": "inherited_full_solution_set",
                    "reason": "fixed-s dual determinant identity with chart-independent marking",
                },
                "signed_defect": {"status": "not_applicable", "reason": "identity lift"},
                "certificate_context": {
                    "source": OVERFLOW_INPUT.name,
                    "provenance": "overflow_symmetric_dual_fixed_s",
                    "fixture_name": name,
                    "decomposition": {
                        "M": source_carrier,
                        "r": residue,
                        "d": d,
                        "identity": "p*s=4*r*d+1",
                        "s": fixed_s,
                    },
                    "selected_candidate": {
                        "L": joined_support,
                        "R_L": target_R,
                        "K_L": target_K,
                    },
                },
                "normal_form": "overflow_fixed_s_outer_rank_reset_v1",
                "induction_rank": {
                    "kind": "absorbed_support_potential",
                    "source": source_potential,
                    "successor": successor_potential,
                },
                "potential_record": {
                    "B_p": B_prime,
                    "source_support": support,
                    "successor_support": joined_support,
                    "source_value": source_potential,
                    "successor_value": successor_potential,
                    "strict_decrease": strict_potential,
                    "support_monotone": strict_gain,
                },
                "e1_e5": {f"E{i}": True for i in range(1, 6)},
                "selector_status": "verified_edge",
                "recursive_edge_eligible": True,
                "lift_status": "proved_identity",
                "proof_boundary": (
                    "fixed_s_absorption"
                    if target_class == "marked_absorb"
                    else "fixed_s_overflow_rank_descent"
                ),
                "scope_note": (
                    "The symmetric r-side fixed-s determinant chart preserves the old support "
                    "through L|r*d and strictly lowers the outer rank."
                ),
            }
            check_status_boundary(receipt)
            verified.append(receipt)
            continue

        missing: list[str] = []
        if not source_in_domain:
            missing.append("source_potential_domain")
        if not 1 <= residue < prime:
            missing.append("positive_residue_carrier")
        if not integral_s:
            missing.append("fixed_s_integrality")
        if not divides_product:
            missing.append("fixed_s_support_divisor")
        if not target_positive:
            missing.append("positive_target_chart")
        if target_positive and not chart_match:
            missing.append("fixed_s_chart_identity")
        if not strict_gain:
            missing.append("strict_support_gain")
        if not strict_potential:
            missing.append("strict_potential_decrease")
        rejected.append(
            {
                "fixture_name": name,
                "equation_target": [4, prime],
                "source_carrier": source_carrier,
                "dual_carrier": residue,
                "source_support": support,
                "joined_support": joined_support,
                "fixed_s": fixed_s,
                "candidate_chart": {
                    "R": target_R,
                    "K": target_K,
                    "positive": target_positive,
                },
                "missing_conditions": missing,
                "selector_status": "analysis_evidence",
                "recursive_edge_eligible": False,
                "proof_boundary": "fixed_s_overflow_rank_filter",
            }
        )
    return {
        "fixture_count": len(rows),
        "verified_edge_count": len(verified),
        "absorption_target_count": sum(
            receipt["state_class"] == "marked_absorb" for receipt in verified
        ),
        "overflow_target_count": sum(
            receipt["state_class"] == "overflow" for receipt in verified
        ),
        "rejected_fixture_count": len(rejected),
        "verified_receipts": verified,
        "rejected_fixtures": rejected,
        "rank_definition": {
            "kind": "absorbed_support_potential",
            "formula": "floor(((p-1)^2)/4 / A)",
            "candidate": "L=lcm(A,r)",
            "fixed_identity": "p*s=4*r*d+1; R_L=4L-s; K_L=L*(p-r*d/L)",
            "acceptance": (
                "L|r*d, L>A, R_L>0, canonical_chart(p,L)=(R_L,K_L), "
                "and strict potential decrease"
            ),
        },
        "scope_note": (
            "This branch is the symmetric r-side fixed-s atlas. It complements the d-side "
            "fixed-n branch but does not assert that every overflow has L|r*d."
        ),
    }


def smooth23_fixed_s_parametric_family() -> dict[str, object]:
    """Reconstruct a genuine r,d>1 smooth fixed-s overflow family.

    This is an arithmetic boundary, not a reachability theorem.  For
    P=2^a*3^b and p=4P+1 prime, choosing rd=P, M=k*p+r and A=M forces
    s=1 while every fixed-s divisor remains below the charged support.
    """
    seed_exponents = [(1, 2), (3, 1), (4, 1), (2, 3), (2, 4)]
    seeds: list[dict[str, object]] = []
    for exponent_two, exponent_three in seed_exponents:
        product = 2**exponent_two * 3**exponent_three
        prime = 4 * product + 1
        if (
            prime % 24 != 1
            or factorization(prime) != [[prime, 1]]
            or product < 6
        ):
            raise AssertionError("smooth fixed-s family seed changed")
        residue = 2
        dual_carrier = product // residue
        B_prime = (prime - 1) ** 2 // 4
        max_k = (B_prime - residue) // prime
        if max_k < 1 or residue <= 1 or dual_carrier <= 1:
            raise AssertionError("smooth fixed-s family parameter range changed")
        checked_k = [1] if max_k == 1 else [1, max_k]
        rows: list[dict[str, object]] = []
        for k in checked_k:
            carrier = k * prime + residue
            support = carrier
            n = 4 * k * dual_carrier + 1
            chart_R = 4 * carrier - n
            chart_K = carrier * (prime - dual_carrier)
            fixed_s = (4 * residue * dual_carrier + 1) // prime
            if (
                carrier > B_prime
                or chart_R <= prime
                or prime * n != 4 * carrier * dual_carrier + 1
                or fixed_s != 1
                or canonical_chart(prime, carrier) != (chart_R, chart_K)
                or product >= carrier
            ):
                raise AssertionError("smooth fixed-s family identity changed")
            if any(
                L > support
                for L in divisors(product)
                if L <= B_prime and 4 * L > fixed_s
            ):
                raise AssertionError("smooth fixed-s family lost its empty atlas")
            rows.append(
                {
                    "k": k,
                    "carrier": carrier,
                    "source_support": support,
                    "n": n,
                    "R": chart_R,
                    "K": chart_K,
                    "fixed_s": fixed_s,
                    "product": product,
                    "residue": residue,
                    "dual_carrier": dual_carrier,
                    "max_positive_bounded_divisor": max(
                        (
                            L
                            for L in divisors(product)
                            if L <= B_prime and 4 * L > fixed_s
                        ),
                        default=0,
                    ),
                    "fixed_s_candidate_count": 0,
                }
            )
        seeds.append(
            {
                "exponents": [exponent_two, exponent_three],
                "product": product,
                "prime": prime,
                "residue": residue,
                "dual_carrier": dual_carrier,
                "B_p": B_prime,
                "k_max": max_k,
                "checked_rows": rows,
            }
        )
    return {
        "condition": (
            "P=2^a*3^b, a,b>=1, p=4P+1 prime, r=2, d=P/2, "
            "M=k*p+r, A=M, 1<=k<=floor((B_p-r)/p)"
        ),
        "parameter_range": "1<=k<=floor((B_p-r)/p)",
        "seed_count": len(seeds),
        "seeds": seeds,
        "source_reach_status": "unproved",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "proof_boundary": "smooth23_parametric_fixed_s_support_saturation",
        "k_one_fixed_n_saturation": smooth23_k_one_fixed_n_saturation(),
        "low_k_fixed_n_cofactor": smooth23_low_k_fixed_n_cofactor(),
        "conclusion": (
            "For each listed prime seed and every allowed k, p*n=4*M*d+1, "
            "R_M>p, s=1, and every fixed-s divisor L|r*d is below A=M. "
            "This is a genuine r,d>1 arithmetic overflow boundary. The k=1 "
            "subfamily additionally has a conditional fixed-n saturation edge; "
            "source reachability for the family remains unproved."
        ),
    }


def smooth23_k_one_fixed_n_saturation() -> dict[str, object]:
    """Give the exact fixed-n rank edge for the k=1 smooth family.

    The family remains conditional on source reachability.  Once a member is
    reached, the fixed-n determinant admits the saturated divisor L=M*d,
    because n=2*P+1 <= p-2 and S=M*d <= B_p.
    """
    seed_exponents = [(1, 2), (3, 1), (4, 1), (2, 3), (2, 4)]
    receipts: list[dict[str, object]] = []
    for exponent_two, exponent_three in seed_exponents:
        product = 2**exponent_two * 3**exponent_three
        prime = 4 * product + 1
        if factorization(prime) != [[prime, 1]]:
            raise AssertionError("smooth k=1 fixed-n seed changed")
        residue = 2
        dual_carrier = product // residue
        carrier = prime + residue
        n = 2 * product + 1
        S = carrier * dual_carrier
        B_prime = (prime - 1) ** 2 // 4
        target_R = 4 * S - n
        target_K = S * (prime - 1)
        source_potential = B_prime // carrier
        successor_potential = B_prime // S
        if (
            prime * n != 4 * carrier * dual_carrier + 1
            or n > prime - 2
            or S > B_prime
            or dual_carrier < 2
            or S <= carrier
            or 4 * S <= n
            or target_R != (prime - 1) * n - 1
            or target_R <= prime
            or target_K != S * (prime - 1)
            or canonical_chart(prime, S) != (target_R, target_K)
            or successor_potential >= source_potential
        ):
            raise AssertionError("smooth k=1 fixed-n saturation identity changed")
        source_state = {
            "equation_target": [4, prime],
            "R": 4 * carrier - n,
            "K": carrier * (prime - dual_carrier),
            "absorbed_support": carrier,
            "state_class": "overflow",
        }
        successor_state = {
            "equation_target": [4, prime],
            "R": target_R,
            "K": target_K,
            "absorbed_support": S,
            "state_class": "overflow",
        }
        receipts.append(
            {
                "edge_id": "edge:" + canonical_hash(
                    {"source": source_state, "successor": successor_state}
                ),
                "certificate_type": "smooth23_k_one_fixed_n_saturation",
                "source_state": source_state,
                "successor_state": successor_state,
                "equation_target": {"numerator": 4, "denominator": prime},
                "determinant": {
                    "P": product,
                    "M": carrier,
                    "r": residue,
                    "d": dual_carrier,
                    "n": n,
                    "S": S,
                    "identity": "p*n=4*M*d+1",
                },
                "selected_candidate": {
                    "L": S,
                    "R_L": target_R,
                    "K_L": target_K,
                    "selection_rule": "L=S=M*d",
                },
                "potential_record": {
                    "B_p": B_prime,
                    "source": source_potential,
                    "successor": successor_potential,
                    "strict_decrease": True,
                    "support_monotone": True,
                },
                "e1_e5": {f"E{i}": True for i in range(1, 6)},
                "selector_status": "verified_edge",
                "recursive_edge_eligible": True,
                "source_reach_status": "unproved",
                "proof_boundary": "fixed_n_low_n_saturation",
            }
        )
    return {
        "condition": (
            "P=2^a*3^b, p=4P+1 prime, r=2, d=P/2, M=p+2, "
            "n=2P+1, A=M"
        ),
        "seed_count": len(receipts),
        "source_reach_status": "unproved",
        "selector_status": "verified_edge_conditional_on_reachability",
        "recursive_edge_eligible": True,
        "proof_boundary": "smooth23_k_one_fixed_n_saturation",
        "saturation_lemma": (
            "n<=p-2 and S=M*d<=B_p; L=S gives R_L=(p-1)*n-1, "
            "K_L=S*(p-1), and Pi(S)<Pi(M)"
        ),
        "receipts": receipts,
    }


def smooth23_low_k_fixed_n_cofactor() -> dict[str, object]:
    """Verify the low-k cofactor edge L=q*M for the smooth family.

    Here q is the smallest prime supplied by d=P/2 (2 when a>=2, otherwise
    3).  The edge is conditional on source reachability and is available
    whenever q*M is inside the B_p capacity box.
    """
    seed_exponents = [(1, 2), (3, 1), (4, 1), (2, 3), (2, 4)]
    seeds: list[dict[str, object]] = []
    for exponent_two, exponent_three in seed_exponents:
        product = 2**exponent_two * 3**exponent_three
        prime = 4 * product + 1
        if factorization(prime) != [[prime, 1]]:
            raise AssertionError("smooth low-k fixed-n seed changed")
        residue = 2
        dual_carrier = product // residue
        q = 2 if dual_carrier % 2 == 0 else 3
        if dual_carrier % q:
            raise AssertionError("smooth low-k cofactor is not available")
        B_prime = (prime - 1) ** 2 // 4
        k_global_max = (B_prime - residue) // prime
        k_cofactor_max = (B_prime - q * residue) // (q * prime)
        if k_cofactor_max < 1 or k_cofactor_max > k_global_max:
            raise AssertionError("smooth low-k cofactor range changed")
        checked_k = [1] if k_cofactor_max == 1 else [1, k_cofactor_max]
        rows: list[dict[str, object]] = []
        for k in checked_k:
            carrier = k * prime + residue
            n = 4 * k * dual_carrier + 1
            S = carrier * dual_carrier
            L = q * carrier
            target_R = 4 * L - n
            target_K = L * (prime - dual_carrier // q)
            source_R = 4 * carrier - n
            source_K = carrier * (prime - dual_carrier)
            source_potential = B_prime // carrier
            successor_potential = B_prime // L
            if (
                prime * n != 4 * carrier * dual_carrier + 1
                or source_R <= prime
                or L != S // (dual_carrier // q)
                or L <= carrier
                or L > B_prime
                or 4 * L <= n
                or target_R <= 0
                or target_K != L * (prime - S // L)
                or canonical_chart(prime, L) != (target_R, target_K)
                or successor_potential >= source_potential
            ):
                raise AssertionError("smooth low-k fixed-n cofactor identity changed")
            source_state = {
                "equation_target": [4, prime],
                "R": source_R,
                "K": source_K,
                "absorbed_support": carrier,
                "state_class": "overflow",
            }
            successor_state = {
                "equation_target": [4, prime],
                "R": target_R,
                "K": target_K,
                "absorbed_support": L,
                "state_class": "overflow" if target_R > prime else "marked_absorb",
            }
            rows.append(
                {
                    "k": k,
                    "source_state": source_state,
                    "successor_state": successor_state,
                    "determinant": {
                        "P": product,
                        "M": carrier,
                        "r": residue,
                        "d": dual_carrier,
                        "n": n,
                        "S": S,
                        "q": q,
                        "cofactor": dual_carrier // q,
                        "identity": "p*n=4*M*d+1",
                    },
                    "selected_candidate": {
                        "L": L,
                        "R_L": target_R,
                        "K_L": target_K,
                        "selection_rule": "L=q*M=S/(d/q)",
                    },
                    "potential_record": {
                        "B_p": B_prime,
                        "source": source_potential,
                        "successor": successor_potential,
                        "strict_decrease": True,
                        "support_monotone": True,
                    },
                    "e1_e5": {f"E{i}": True for i in range(1, 6)},
                    "selector_status": "verified_edge",
                    "recursive_edge_eligible": True,
                    "source_reach_status": "unproved",
                }
            )
        seeds.append(
            {
                "exponents": [exponent_two, exponent_three],
                "prime": prime,
                "P": product,
                "d": dual_carrier,
                "q": q,
                "k_global_max": k_global_max,
                "k_cofactor_max": k_cofactor_max,
                "remaining_k_range": [k_cofactor_max + 1, k_global_max]
                if k_cofactor_max < k_global_max
                else [],
                "checked_rows": rows,
            }
        )
    return {
        "condition": (
            "P=2^a*3^b, p=4P+1 prime, r=2, d=P/2, M=k*p+2, "
            "A=M, q=2 if 2|d else 3, 1<=k<=floor((B_p-2q)/(q*p))"
        ),
        "candidate": "L=q*M",
        "seed_count": len(seeds),
        "source_reach_status": "unproved",
        "selector_status": "verified_edge_conditional_on_reachability",
        "recursive_edge_eligible": True,
        "proof_boundary": "smooth23_low_k_fixed_n_cofactor",
        "automatic_checks": (
            "q|d, L=q*M=S/(d/q), L>=2A, L<=B_p, 4L>n, "
            "and Pi(L)<Pi(A)"
        ),
        "multiple_M_atlas": {
            "scope": "fixed-n candidates L=M*u with u|d and u>1",
            "minimum_multiplier": "q=spf(d)",
            "complete_condition": "q*M<=B_p",
            "empty_condition": "q*M>B_p implies no bounded multiple-M candidate",
            "remaining_candidates": "L|M*d with M not dividing L",
        },
        "outer_potential_boundary": smooth23_outer_potential_boundary(),
        "high_k_dual_no_go": smooth23_high_k_dual_no_go(),
        "seeds": seeds,
        "high_k_residual_status": "analysis_evidence",
        "high_k_residual_route": ["fixed_n_factor_divisor", "type_ii", "q_adic_capacity"],
    }


def smooth23_outer_potential_boundary() -> dict[str, object]:
    """Classify the current outer-potential boundary of the smooth family."""
    seed_exponents = [(1, 2), (3, 1), (4, 1), (2, 3), (2, 4)]
    seeds: list[dict[str, object]] = []
    for exponent_two, exponent_three in seed_exponents:
        product = 2**exponent_two * 3**exponent_three
        prime = 4 * product + 1
        dual_carrier = product // 2
        q = 2 if dual_carrier % 2 == 0 else 3
        B_prime = (prime - 1) ** 2 // 4
        global_k_max = (B_prime - 2) // prime
        half_k_min = (B_prime - 4) // (2 * prime) + 1
        third_k_min = (B_prime - 6) // (3 * prime) + 1
        if not (1 <= third_k_min <= half_k_min <= global_k_max + 1):
            raise AssertionError("smooth outer-potential thresholds changed")
        seeds.append(
            {
                "exponents": [exponent_two, exponent_three],
                "prime": prime,
                "B_p": B_prime,
                "q": q,
                "global_k_range": [1, global_k_max],
                "qM_overflow_k_range": [
                    (B_prime - 2 * q) // (q * prime) + 1,
                    global_k_max,
                ],
                "phi_two_k_range": [third_k_min, half_k_min - 1]
                if third_k_min < half_k_min
                else [],
                "phi_one_k_range": [half_k_min, global_k_max]
                if half_k_min <= global_k_max
                else [],
                "half_threshold_identity": "2*(k*p+2)>B_p",
                "third_threshold_identity": "3*(k*p+2)>B_p",
            }
        )
    return {
        "potential": "Phi(A)=floor(B_p/A)",
        "hard_boundary": (
            "M>B_p/2 implies Phi(M)=1; no M<L<=B_p can have strict Phi descent"
        ),
        "intermediate_boundary": (
            "B_p/3<M<=B_p/2 implies Phi(M)=2; any strict target must satisfy L>B_p/2"
        ),
        "q2_consequence": "q=2 and qM>B_p implies the current Phi has no fixed-n E5 target",
        "q3_consequence": (
            "q=3 and qM>B_p splits into a Phi=2 interval and a Phi=1 hard tail"
        ),
        "seeds": seeds,
    }


def smooth23_high_k_dual_no_go() -> dict[str, object]:
    """Record the bounded dual-carrier RESET no-go in the qM>B tail."""
    seed_exponents = [(1, 2), (3, 1), (4, 1), (2, 3), (2, 4)]
    seeds: list[dict[str, object]] = []
    for exponent_two, exponent_three in seed_exponents:
        product = 2**exponent_two * 3**exponent_three
        prime = 4 * product + 1
        dual_carrier = product // 2
        q = 2 if dual_carrier % 2 == 0 else 3
        B_prime = (prime - 1) ** 2 // 4
        k_global_max = (B_prime - 2) // prime
        high_k_min = (B_prime - 2 * q) // (q * prime) + 1
        if not (1 <= high_k_min <= k_global_max + 1):
            raise AssertionError("smooth high-k dual threshold changed")
        seeds.append(
            {
                "exponents": [exponent_two, exponent_three],
                "prime": prime,
                "P": product,
                "d": dual_carrier,
                "q": q,
                "high_k_range": [high_k_min, k_global_max]
                if high_k_min <= k_global_max
                else [],
                "d_channel": {
                    "carrier": "d=P/2",
                    "minimum_gain_multiplier": q,
                    "joined_support": "M*(d/gcd(M,d))",
                    "tail_bound": "q*M>B_p implies joined support>B_p when gain>1",
                },
                "r_channel": {
                    "carrier": 2,
                    "chart": "R_r=7, K_r=2*(p-d)",
                    "gain_multiplier": 2,
                    "divisibility_if_M_odd": "M|p-d",
                    "impossible_interval": "0<p-d<M",
                },
            }
        )
    return {
        "condition": (
            "P=2^a*3^b, p=4P+1 prime, r=2, d=P/2, M=k*p+2, A=M, "
            "q*M>B_p"
        ),
        "selector_status": "verified_arithmetic_no_go",
        "recursive_edge_eligible": False,
        "proof_boundary": "smooth23_high_k_dual_carrier_no_go",
        "fixed_s_reason": "L|r*d=P<M=A",
        "d_reason": "gain>1 gives lcm(M,d)>=q*M>B_p",
        "r_reason": (
            "gain requires M odd and 2M<=B_p; divisibility would force M|p-d, "
            "contradicting 0<p-d<M"
        ),
        "remaining_route": ["type_ii", "alternate_carrier", "second_rank", "q_adic_capacity"],
        "seeds": seeds,
    }


def overflow_fixed_s_bounded_divisor_outer_rank(
    payload: dict[str, object],
) -> dict[str, object]:
    """Use any bounded fixed-s divisor as a support-rank edge.

    Writing ``M = k*p + r`` gives ``p*s = 4*r*d + 1``.  Every divisor
    ``L`` of ``r*d`` therefore yields the dual determinant chart
    ``R_L = 4*L - s`` and ``K_L = L*(p - r*d/L)``.  The old support need
    not divide ``L``: a strict outer-potential decrease explicitly pays the
    support reset, exactly as in the bounded fixed-n atlas.
    """
    verified: list[dict[str, object]] = []
    rejected: list[dict[str, object]] = []
    unconditional_names: list[str] = []
    product_saturation_names: list[str] = []
    d_saturation_names: list[str] = []
    r_one_edge_names: list[str] = []
    r_one_empty_names: list[str] = []
    d_one_edge_names: list[str] = []
    d_one_empty_names: list[str] = []
    cofactor_saturation_names: list[str] = []
    prime_power_cofactor_names: list[str] = []
    large_prime_cofactor_names: list[str] = []
    smooth23_residual_names: list[str] = []
    smooth23_one_dimensional_names: list[str] = []
    smooth23_two_dimensional_names: list[str] = []
    smooth23_grid_receipts: list[dict[str, object]] = []
    rows = overflow_fixture_rows(payload)
    for fixture in rows:
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        support = int(fixture["A"])
        source_carrier = int(fixture["M"])
        source_R = int(fixture["R_M"])
        source_K = int(fixture["K_M"])
        d = int(fixture["d"])
        n = int(fixture["n"])
        if not (
            support > 0
            and source_carrier > 0
            and source_carrier % support == 0
            and source_K % source_carrier == 0
            and 1 <= d < prime
            and prime * n == 4 * source_carrier * d + 1
            and source_R == 4 * source_carrier - n
        ):
            raise AssertionError(f"bounded fixed-s source invariant changed: {name}")
        residue = source_carrier % prime
        numerator = 4 * residue * d + 1
        integral_s = residue > 0 and numerator % prime == 0
        fixed_s = numerator // prime if integral_s else None
        if integral_s and isinstance(fixed_s, int) and prime * fixed_s != numerator:
            raise AssertionError(f"bounded fixed-s integrality changed: {name}")
        product = residue * d
        B_prime = (prime - 1) ** 2 // 4
        source_in_domain = 0 < support <= B_prime
        if integral_s and isinstance(fixed_s, int) and residue >= 2 * support:
            if not (
                residue <= B_prime
                and 4 * residue > fixed_s
                and B_prime // residue < B_prime // support
                and canonical_chart(prime, residue)
                == (4 * residue - fixed_s, residue * (prime - d))
            ):
                raise AssertionError(f"r>=2A fixed-s subfamily changed: {name}")
            unconditional_names.append(name)
        if integral_s and isinstance(fixed_s, int) and 2 * support <= product <= B_prime:
            if not (
                4 * product > fixed_s
                and B_prime // product < B_prime // support
                and canonical_chart(prime, product)
                == (4 * product - fixed_s, product * (prime - 1))
            ):
                raise AssertionError(f"rd saturation subfamily changed: {name}")
            product_saturation_names.append(name)
        if integral_s and isinstance(fixed_s, int) and 2 * support <= d <= B_prime:
            if not (
                4 * d > fixed_s
                and B_prime // d < B_prime // support
                and canonical_chart(prime, d) == (4 * d - fixed_s, d * (prime - residue))
            ):
                raise AssertionError(f"d saturation subfamily changed: {name}")
            d_saturation_names.append(name)
        if integral_s and isinstance(fixed_s, int) and residue == 1:
            expected_d = (prime - 1) // 4
            if fixed_s != 1 or d != expected_d or B_prime != 4 * d * d:
                raise AssertionError(f"r=1 fixed-s normal form changed: {name}")
            if support < d:
                if not (
                    4 * d > fixed_s
                    and B_prime // d < B_prime // support
                    and canonical_chart(prime, d) == (4 * d - fixed_s, d * (prime - 1))
                ):
                    raise AssertionError(f"r=1 fixed-s edge changed: {name}")
                r_one_edge_names.append(name)
            else:
                if any(L > support for L in divisors(product)):
                    raise AssertionError(f"r=1 fixed-s empty boundary changed: {name}")
                r_one_empty_names.append(name)
        if integral_s and isinstance(fixed_s, int) and d == 1:
            expected_r = (prime - 1) // 4
            if (
                residue != expected_r
                or fixed_s != 1
                or B_prime != 4 * residue * residue
            ):
                raise AssertionError(f"d=1 fixed-s normal form changed: {name}")
            if support < residue:
                if not (
                    4 * residue > fixed_s
                    and B_prime // residue < B_prime // support
                    and canonical_chart(prime, residue)
                    == (4 * residue - fixed_s, residue * (prime - 1))
                ):
                    raise AssertionError(f"d=1 fixed-s edge changed: {name}")
                d_one_edge_names.append(name)
            else:
                if any(L > support for L in divisors(product)):
                    raise AssertionError(f"d=1 fixed-s empty boundary changed: {name}")
                d_one_empty_names.append(name)
        if integral_s and isinstance(fixed_s, int) and product > 1:
            factor_rows = factorization(product)
            smallest_factor, smallest_factor_exponent = min(factor_rows)
            cofactor = product // smallest_factor
            if 2 * support <= cofactor <= B_prime:
                if not (
                    smallest_factor < prime
                    and 4 * cofactor > fixed_s
                    and B_prime // cofactor < B_prime // support
                    and canonical_chart(prime, cofactor)
                    == (4 * cofactor - fixed_s, cofactor * (prime - smallest_factor))
                ):
                    raise AssertionError(f"fixed-s cofactor subfamily changed: {name}")
                cofactor_saturation_names.append(name)
            power_exponent = 1
            power_divisor = smallest_factor
            prime_power_cofactor = product // power_divisor
            while (
                prime_power_cofactor > B_prime
                and power_exponent < smallest_factor_exponent
            ):
                power_exponent += 1
                power_divisor *= smallest_factor
                prime_power_cofactor = product // power_divisor
            if (
                power_exponent >= 1
                and prime_power_cofactor <= B_prime
                and 2 * support <= prime_power_cofactor
                and power_divisor < prime
            ):
                if not (
                    4 * prime_power_cofactor > fixed_s
                    and B_prime // prime_power_cofactor < B_prime // support
                    and canonical_chart(prime, prime_power_cofactor)
                    == (
                        4 * prime_power_cofactor - fixed_s,
                        prime_power_cofactor * (prime - power_divisor),
                    )
                ):
                    raise AssertionError(
                        f"fixed-s prime-power cofactor subfamily changed: {name}"
                    )
                prime_power_cofactor_names.append(name)
            large_prime_candidates = []
            if product > B_prime:
                for large_factor, _ in factor_rows:
                    if large_factor < 5 or large_factor >= prime:
                        continue
                    large_cofactor = product // large_factor
                    if 2 * support <= large_cofactor <= B_prime:
                        if not (
                            4 * large_cofactor > fixed_s
                            and B_prime // large_cofactor < B_prime // support
                            and canonical_chart(prime, large_cofactor)
                            == (
                                4 * large_cofactor - fixed_s,
                                large_cofactor * (prime - large_factor),
                            )
                        ):
                            raise AssertionError(
                                f"fixed-s large-prime cofactor changed: {name}"
                            )
                        large_prime_candidates.append(large_factor)
            if large_prime_candidates:
                large_prime_cofactor_names.append(name)
        candidates: list[tuple[int, int, int]] = []
        if source_in_domain and integral_s and isinstance(fixed_s, int):
            for L in divisors(product):
                if L <= support or L > B_prime or 4 * L <= fixed_s:
                    continue
                if B_prime // L >= B_prime // support:
                    continue
                target_R = 4 * L - fixed_s
                target_K = L * (prime - product // L)
                if target_K <= 0:
                    continue
                if canonical_chart(prime, L) != (target_R, target_K):
                    raise AssertionError(f"bounded fixed-s chart changed: {name}, L={L}")
                candidates.append((L, target_R, target_K))

        if candidates:
            L, target_R, target_K = max(candidates, key=lambda row: row[0])
            successor_potential = B_prime // L
            support_retained = L % support == 0
            target_class = "marked_absorb" if target_R < prime else "overflow"
            source_state = {
                "equation_target": [4, prime],
                "R": source_R,
                "K": source_K,
                "absorbed_support": support,
                "state_class": "overflow",
            }
            target_state = {
                "equation_target": [4, prime],
                "R": target_R,
                "K": target_K,
                "absorbed_support": L,
                "state_class": target_class,
            }
            receipt = {
                "edge_id": "edge:" + canonical_hash(
                    {"source": source_state, "successor": target_state}
                ),
                "certificate_type": "overflow_fixed_s_bounded_divisor_outer_rank",
                "phase": "OVERFLOW_DUAL_DETERMINANT",
                "state_class": target_class,
                "source_state": source_state,
                "successor_state": target_state,
                "equation_target": {"numerator": 4, "denominator": prime},
                "marked_solution_set": {
                    "source": "Sol(p)",
                    "successor": "Sol(p)",
                    "lift": "identity",
                },
                "target_fiber": {
                    "status": "inherited_full_solution_set",
                    "reason": "fixed-s dual determinant identity with chart-independent marking",
                },
                "signed_defect": {"status": "not_applicable", "reason": "identity lift"},
                "certificate_context": {
                    "source": OVERFLOW_INPUT.name,
                    "provenance": "overflow_determinant_fixed_s_bounded_divisor",
                    "fixture_name": name,
                    "decomposition": {
                        "M": source_carrier,
                        "r": residue,
                        "d": d,
                        "s": fixed_s,
                        "identity": "p*s=4*r*d+1",
                    },
                    "selected_candidate": {
                        "L": L,
                        "R_L": target_R,
                        "K_L": target_K,
                        "candidate_count": len(candidates),
                        "selection_rule": "maximum admissible L",
                    },
                    "admissibility": {
                        "support_gain": "A<L",
                        "support_containment": "A|L when retained; otherwise paid outer-rank reset",
                        "bounded_support": "L<=B_p",
                        "positive_chart": "4L>s",
                        "strict_potential": "floor(B_p/L)<floor(B_p/A)",
                    },
                },
                "normal_form": "overflow_fixed_s_bounded_divisor_outer_rank_v1",
                "induction_rank": {
                    "kind": "absorbed_support_potential",
                    "source": B_prime // support,
                    "successor": successor_potential,
                },
                "potential_record": {
                    "B_p": B_prime,
                    "source_support": support,
                    "successor_support": L,
                    "source_value": B_prime // support,
                    "successor_value": successor_potential,
                    "strict_decrease": True,
                    "support_monotone": support_retained,
                    "support_reset_paid": not support_retained,
                    "outer_rank_reset": not support_retained,
                },
                "e1_e5": {f"E{i}": True for i in range(1, 6)},
                "selector_status": "verified_edge",
                "recursive_edge_eligible": True,
                "lift_status": "proved_identity",
                "proof_boundary": (
                    "fixed_s_bounded_divisor_absorption"
                    if target_class == "marked_absorb"
                    else "fixed_s_bounded_divisor_overflow_rank_descent"
                ),
                "scope_note": (
                    "Any divisor L of r*d satisfying the bounded support, positive-chart, "
                    "and strict-potential conditions yields this identity-lift edge; the "
                    "selector chooses the largest admissible L deterministically. If A "
                    "does not divide L, the strict absorbed-support potential explicitly "
                    "pays the support reset.",
                ),
            }
            check_status_boundary(receipt)
            verified.append(receipt)
            continue

        missing: list[str] = []
        if not source_in_domain:
            missing.append("source_potential_domain")
        if not 1 <= residue < prime:
            missing.append("positive_dual_carrier")
        if not integral_s:
            missing.append("fixed_s_integrality")
        missing.append("admissible_L")
        smooth23_residual = product > 0 and all(
            q <= 3 for q, _ in factorization(product)
        )
        smooth23_boundary: dict[str, object] | None = None
        if smooth23_residual:
            smooth23_residual_names.append(name)
            if source_in_domain and integral_s and isinstance(fixed_s, int):
                positive_bounded_divisors = [
                    L
                    for L in divisors(product)
                    if L <= B_prime and 4 * L > fixed_s
                ]
                max_positive_bounded_divisor = max(positive_bounded_divisors, default=0)
                one_dimensional = residue == 1 or d == 1
                if one_dimensional:
                    smooth23_one_dimensional_names.append(name)
                else:
                    smooth23_two_dimensional_names.append(name)
                smooth23_boundary = {
                    "fixture_name": name,
                    "product": product,
                    "factorization": factorization(product),
                    "source_support": support,
                    "max_positive_bounded_divisor": max_positive_bounded_divisor,
                    "boundary_gap": 2 * support - max_positive_bounded_divisor,
                    "boundary_condition_verified": max_positive_bounded_divisor < 2 * support,
                    "grid_dimension": (
                        "one_dimensional_boundary"
                        if one_dimensional
                        else "genuine_two_dimensional_grid"
                    ),
                }
                smooth23_grid_receipts.append(smooth23_boundary)
        if smooth23_boundary is not None:
            if residue == 1:
                residual_routing = ["r_one_fixed_s_boundary", "type_ii", "q_adic_capacity"]
            elif d == 1:
                residual_routing = [
                    "d_one_fixed_s_boundary",
                    "overflow_d_one_p_minus_two_g_rechart",
                    "type_ii",
                    "q_adic_capacity",
                ]
            else:
                residual_routing = ["generalized_dyadic", "type_ii", "q_adic_capacity"]
            proof_boundary = (
                "fixed_s_23_smooth_one_dimensional_boundary"
                if residue == 1 or d == 1
                else "fixed_s_23_smooth_residual"
            )
        else:
            residual_routing = (
                ["generalized_dyadic", "type_ii", "q_adic_capacity"]
                if smooth23_residual
                else []
            )
            proof_boundary = (
                "fixed_s_23_smooth_residual"
                if smooth23_residual
                else "fixed_s_bounded_divisor_rank_filter"
            )
        rejected.append(
            {
                "fixture_name": name,
                "equation_target": [4, prime],
                "source_carrier": source_carrier,
                "dual_carrier": residue,
                "source_support": support,
                "fixed_s": fixed_s,
                "candidate_count": 0,
                "missing_conditions": missing,
                "selector_status": "analysis_evidence",
                "recursive_edge_eligible": False,
                "proof_boundary": proof_boundary,
                "residual_routing": residual_routing,
            }
        )
    return {
        "fixture_count": len(rows),
        "verified_edge_count": len(verified),
        "absorption_target_count": sum(
            receipt["state_class"] == "marked_absorb" for receipt in verified
        ),
        "overflow_target_count": sum(
            receipt["state_class"] == "overflow" for receipt in verified
        ),
        "rejected_fixture_count": len(rejected),
        "verified_receipts": verified,
        "rejected_fixtures": rejected,
        "unconditional_fixed_s_subfamily": {
            "condition": "r>=2A",
            "candidate": "L=r",
            "fixture_count": len(unconditional_names),
            "fixture_names": unconditional_names,
            "conclusion": (
                "r<=p-1<=B_p, d<=p-1 implies s<4r; r>=2A gives strict "
                "Pi(r)<Pi(A), so L=r is a complete fixed-s identity-lift edge"
            ),
        },
        "unconditional_product_saturation_subfamily": {
            "condition": "2A<=r*d<=B_p",
            "candidate": "L=r*d",
            "fixture_count": len(product_saturation_names),
            "fixture_names": product_saturation_names,
            "conclusion": (
                "s<4*r*d and r*d>=2A give positive chart and strict Pi(r*d)<Pi(A); "
                "the target has K_L=r*d*(p-1)"
            ),
        },
        "unconditional_d_saturation_subfamily": {
            "condition": "2A<=d<=B_p",
            "candidate": "L=d",
            "fixture_count": len(d_saturation_names),
            "fixture_names": d_saturation_names,
            "conclusion": (
                "d|r*d, s<4d, and 2A<=d<=B_p give strict Pi(d)<Pi(A); "
                "the target has K_L=d*(p-r)"
            ),
        },
        "r_one_fixed_s_boundary": {
            "condition": "r=1, d=(p-1)/4, s=1, B_p=4*d^2",
            "candidate_rule": "A<d => L=d; A>=d => no divisor L|r*d with L>A",
            "fixture_count": len(r_one_edge_names) + len(r_one_empty_names),
            "edge_fixture_names": r_one_edge_names,
            "empty_fixture_names": r_one_empty_names,
            "conclusion": (
                "The fixed-s bounded-divisor atlas is complete for r=1: "
                "L=d is a strict identity-lift edge exactly when A<d; otherwise "
                "every divisor of r*d is at most the charged support."
            ),
        },
        "d_one_fixed_s_boundary": {
            "condition": "d=1, r=(p-1)/4, s=1, B_p=4*r^2",
            "candidate_rule": "A<r => L=r; A>=r => no divisor L|r*d with L>A",
            "fixture_count": len(d_one_edge_names) + len(d_one_empty_names),
            "edge_fixture_names": d_one_edge_names,
            "empty_fixture_names": d_one_empty_names,
            "conclusion": (
                "The fixed-s bounded-divisor atlas is complete for d=1: "
                "L=r is a strict identity-lift edge exactly when A<r; otherwise "
                "every divisor of r*d is at most the charged support."
            ),
        },
        "unconditional_cofactor_saturation_subfamily": {
            "condition": "ell=spf(r*d), 2A<=r*d/ell<=B_p",
            "candidate": "L=r*d/ell",
            "fixture_count": len(cofactor_saturation_names),
            "fixture_names": cofactor_saturation_names,
            "conclusion": (
                "ell< p and s<4L are automatic; K_L=L*(p-ell), so the "
                "cofactor gives a strict fixed-s identity-lift edge"
            ),
        },
        "unconditional_prime_power_cofactor_subfamily": {
            "condition": (
                "ell=spf(r*d), e=min{j>=1: r*d/ell^j<=B_p}, "
                "ell^e<p, 2A<=r*d/ell^e"
            ),
            "candidate": "L=r*d/ell^e",
            "fixture_count": len(prime_power_cofactor_names),
            "fixture_names": prime_power_cofactor_names,
            "conclusion": (
                "For the first bounded power cofactor, s<4L is automatic and "
                "K_L=L*(p-ell^e), giving a strict fixed-s identity-lift edge"
            ),
        },
        "high_product_prime_power_boundary": {
            "condition": "P=r*d>B_p and P<=4B_p",
            "classification": (
                "If P/ell>B_p for ell=spf(P), then ell in {2,3}; "
                "if v_ell(P)>=2, P/ell^2<=B_p and ell^2<p; "
                "otherwise v_ell(P)=1 and the residual is squarefree at ell, "
                "or the bounded cofactor is below 2A."
            ),
            "conclusion": (
                "Prime-power cofactor failure above B_p is reduced to a single "
                "2-or-3 factor boundary or to support saturation A>P/ell^e."
            ),
        },
        "unconditional_large_prime_cofactor_subfamily": {
            "condition": "P=r*d>B_p, q|P, q>=5, 2A<=P/q<=B_p",
            "candidate": "L=P/q",
            "fixture_count": len(large_prime_cofactor_names),
            "fixture_names": large_prime_cofactor_names,
            "conclusion": (
                "P<=4B_p implies P/q<B_p for q>=5; q<p gives positive "
                "chart and K_L=(P/q)*(p-q)"
            ),
        },
        "smooth23_fixed_s_residual": {
            "condition": (
                "no admissible fixed-s L and Supp(r*d) subset {2,3}"
            ),
            "fixture_count": len(smooth23_residual_names),
            "fixture_names": smooth23_residual_names,
            "one_dimensional_fixture_count": len(smooth23_one_dimensional_names),
            "one_dimensional_fixture_names": smooth23_one_dimensional_names,
            "genuine_two_dimensional_fixture_count": len(smooth23_two_dimensional_names),
            "genuine_two_dimensional_fixture_names": smooth23_two_dimensional_names,
            "grid_receipts": smooth23_grid_receipts,
            "selector_status": "analysis_evidence",
            "recursive_edge_eligible": False,
            "boundary_lemma": (
                "For L_plus=max{L|r*d: L<=B_p and 4L>s}, L_plus>=2A "
                "implies an admissible fixed-s edge; every rejected row therefore has L_plus<2A."
            ),
            "routing": {
                "one_dimensional": [
                    "r_one_fixed_s_boundary",
                    "d_one_fixed_s_boundary",
                    "type_ii",
                    "q_adic_capacity",
                ],
                "genuine_two_dimensional": [
                    "generalized_dyadic",
                    "type_ii",
                    "q_adic_capacity",
                ],
            },
            "conclusion": (
                "The fixed-s divisor set is an exponent grid L=2^i*3^j. "
                "If the grid has no admissible point, its positive bounded frontier lies below "
                "2A; r=1 or d=1 rows are exact one-dimensional boundary specializations, not "
                "new two-dimensional overflow residuals."
            ),
            "parametric_family": smooth23_fixed_s_parametric_family(),
        },
        "rank_definition": {
            "kind": "absorbed_support_potential",
            "formula": "floor(((p-1)^2)/4 / A)",
            "candidate": "any L|r*d with A<L<=B_p and 4L>s",
            "target_formula": "R_L=4L-s; K_L=L*(p-r*d/L)",
            "selection_rule": "maximum admissible L",
            "acceptance": (
                "L|r*d, A<L<=B_p, 4L>s, canonical_chart(p,L)=(R_L,K_L), "
                "and strict potential decrease; A|L is optional only when the same "
                "potential explicitly pays an outer-rank reset"
            ),
        },
        "scope_note": (
            "This is the complete bounded fixed-s divisor atlas above the absorbed-support "
            "potential domain. It complements the lcm(A,r) fixed-s branch; an empty "
            "admissible set remains analysis evidence and is not promoted.",
        ),
    }

def overflow_outer_rank_reset(payload: dict[str, object]) -> dict[str, object]:
    """Pay a RESET with the non-resettable absorbed-support potential.

    A dual carrier may be used only after joining it with the old charged
    support.  This keeps the support commitment monotone even when the target
    canonical chart is itself still an overflow chart.
    """
    overflow_dual = payload.get("overflow_dual")
    if not isinstance(overflow_dual, dict):
        raise AssertionError("overflow dual payload shape changed")

    verified: list[dict[str, object]] = []
    rejected: list[dict[str, object]] = []
    channel_count = 0
    for fixture in overflow_fixture_rows(payload):
        name = str(fixture["name"])
        prime = int(fixture["prime"])
        support = int(fixture["A"])
        carrier = int(fixture["M"])
        R_M = int(fixture["R_M"])
        K_M = int(fixture["K_M"])
        n = int(fixture["n"])
        d = int(fixture["d"])
        if not (
            support > 0
            and carrier > 0
            and carrier % support == 0
            and K_M % carrier == 0
            and prime * n == 4 * carrier * d + 1
            and R_M == 4 * carrier - n
        ):
            raise AssertionError(f"outer-rank source invariant changed: {name}")

        residue = carrier % prime
        if not 1 <= residue < prime:
            raise AssertionError(f"outer-rank residue left its range: {name}")
        for side, dual_carrier in (("d", d), ("r", residue)):
            channel_count += 1
            if dual_carrier <= 0:
                raise AssertionError(f"outer-rank dual carrier is not positive: {name}")
            dual_R, dual_K = canonical_chart(prime, dual_carrier)
            joined_support = lcm(support, dual_carrier)
            support_modulus = support // gcd(support, dual_carrier)
            if side == "d":
                residue_label = ((carrier - residue) // prime) + 1
            else:
                residue_label = d * n - 1
            support_debt = joined_support // gcd(joined_support, dual_K)
            expected_support_debt = support_modulus // gcd(
                support_modulus, residue_label
            )
            if support_debt != expected_support_debt:
                raise AssertionError(f"support debt identity changed: {name}, side={side}")
            support_debt_record = {
                "value": support_debt,
                "factorization": factorization(support_debt),
                "support_modulus": support_modulus,
                "residue_label": residue_label,
                "paid_status": support_debt == 1,
            }
            strict_gain = joined_support > support
            support_divisibility = dual_K % joined_support == 0
            B_prime = (prime - 1) ** 2 // 4
            source_potential = B_prime // support
            successor_potential = B_prime // joined_support
            strict_potential = successor_potential < source_potential
            descriptor = {
                "equation_target": [4, prime],
                "phase": "RESET",
                "fixture_name": name,
                "side": side,
                "source_carrier": carrier,
                "dual_carrier": dual_carrier,
                "joined_support": joined_support,
            }
            if strict_gain and support_divisibility and strict_potential:
                target_class = "marked_absorb" if dual_R < prime else "overflow"
                source_state = {
                    "equation_target": [4, prime],
                    "R": R_M,
                    "K": K_M,
                    "absorbed_support": support,
                    "state_class": "overflow",
                }
                target_state = {
                    "equation_target": [4, prime],
                    "R": dual_R,
                    "K": dual_K,
                    "absorbed_support": joined_support,
                    "state_class": target_class,
                }
                receipt = {
                    "edge_id": "edge:" + canonical_hash(
                        {"source": source_state, "successor": target_state}
                    ),
                    "certificate_type": "overflow_outer_rank_reset",
                    "phase": "RESET",
                    "state_class": target_class,
                    "source_state": source_state,
                    "successor_state": target_state,
                    "equation_target": {"numerator": 4, "denominator": prime},
                    "marked_solution_set": {
                        "source": "Sol(p)",
                        "successor": "Sol(p)",
                        "lift": "identity",
                    },
                    "target_fiber": {
                        "status": "inherited_full_solution_set",
                        "reason": "canonical dual chart with chart-independent marking",
                    },
                    "signed_defect": {"status": "not_applicable", "reason": "identity lift"},
                    "support_debt": support_debt_record,
                    "certificate_context": {
                        "source": OVERFLOW_INPUT.name,
                        "provenance": "symmetric_dual_with_joined_support",
                        "fixture_name": name,
                        "dual_side": side,
                        "dual_carrier": dual_carrier,
                        "dual_chart": {"R": dual_R, "K": dual_K},
                        "joined_support": joined_support,
                        "support_debt": support_debt_record,
                        "overflow_determinant": {
                            "pn": prime * n,
                            "four_M_d_plus_1": 4 * carrier * d + 1,
                        },
                    },
                    "normal_form": "overflow_outer_rank_reset_v1",
                    "induction_rank": {
                        "kind": "absorbed_support_potential",
                        "source": source_potential,
                        "successor": successor_potential,
                    },
                    "potential_record": {
                        "B_p": B_prime,
                        "source_support": support,
                        "successor_support": joined_support,
                        "source_value": source_potential,
                        "successor_value": successor_potential,
                        "strict_decrease": successor_potential < source_potential,
                        "support_monotone": joined_support > support,
                    },
                    "e1_e5": {f"E{i}": True for i in range(1, 6)},
                    "selector_status": "verified_edge",
                    "recursive_edge_eligible": True,
                    "lift_status": "proved_identity",
                    "proof_boundary": (
                        "joined_support_rank_descent"
                        if target_class == "overflow"
                        else "joined_support_absorption"
                    ),
                    "scope_note": (
                        "The RESET preserves the old support by joining the dual carrier; "
                        "the target may remain overflow, but the absorbed-support rank is "
                        "strictly smaller and cannot be reset by this edge."
                    ),
                }
                check_status_boundary(receipt)
                verified.append(receipt)
                continue

            missing: list[str] = []
            if not strict_gain:
                missing.append("strict_support_gain")
            if not support_divisibility:
                missing.append("joined_support_divisibility")
            if not strict_potential:
                missing.append("strict_potential_decrease")
            rejected.append(
                {
                    "fixture_name": name,
                    "equation_target": [4, prime],
                    "side": side,
                    "source_carrier": carrier,
                    "dual_carrier": dual_carrier,
                    "dual_chart": {"R": dual_R, "K": dual_K},
                    "source_support": support,
                    "joined_support": joined_support,
                    "support_debt": support_debt_record,
                    "strict_support_gain": strict_gain,
                    "joined_support_divides_dual_K": support_divisibility,
                    "missing_conditions": missing,
                    "selector_status": "analysis_evidence",
                    "recursive_edge_eligible": False,
                    "proof_boundary": "outer_rank_reset_filter",
                }
            )

    if channel_count != 24:
        raise AssertionError(f"outer-rank channel count changed: {channel_count}")
    return {
        "channel_count": channel_count,
        "verified_edge_count": len(verified),
        "rejected_channel_count": len(rejected),
        "verified_receipts": verified,
        "rejected_channels": rejected,
        "rank_definition": {
            "kind": "absorbed_support_potential",
            "formula": "floor(((p-1)^2)/4 / A)",
            "reset_rule": "A_next=lcm(A,dual_carrier)",
            "strict_condition": (
                "A_next>A, A_next divides K_dual, and floor(B_p/A_next)<floor(B_p/A)"
            ),
        },
        "support_debt_definition": {
            "formula": "lcm(A,t)/gcd(lcm(A,t),K_t)",
            "d_label": "k+1",
            "r_label": "d*n-1",
            "identity": "support_debt=O_d or O_r",
            "zero_debt_is_not_sufficient": True,
        },
        "scope_note": (
            "Only support-preserving RESET channels are promoted. Rejected channels retain "
            "their local dual arithmetic but cannot discard the old charged support."
        ),
    }


def phase_reset_boundary(payload: dict[str, object]) -> dict[str, object]:
    """Register the focused RESET re-entry cycle as a non-recursive edge menu.

    The local reset support is smaller than the source carrier and the identity
    lift is harmless, but the ordinary anchor/lcm continuation closes a 132/330
    cycle. This is therefore candidate_transition with E5 missing.
    """
    overflow_dual = payload.get("overflow_dual")
    if not isinstance(overflow_dual, dict):
        raise AssertionError("overflow dual payload shape changed")
    cycle = overflow_dual.get("reset_reentry_cycle")
    if not isinstance(cycle, dict):
        raise AssertionError("reset re-entry fixture missing")
    rows = cycle.get("rows")
    if not isinstance(rows, list) or len(rows) != 3:
        raise AssertionError("reset re-entry row count changed")
    prime = int(cycle["prime"])
    edge_by_carrier: dict[int, int] = {}
    edge_rows: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            raise AssertionError("reset re-entry row shape changed")
        carrier = int(row["carrier"])
        reset_support = int(row["reset_support"])
        next_carrier = int(row["next_carrier"])
        source_R, source_K = canonical_chart(prime, carrier)
        reset_R, reset_K = canonical_chart(prime, reset_support)
        next_R, next_K = canonical_chart(prime, next_carrier)
        if not reset_support < carrier:
            raise AssertionError("reset support did not decrease locally")
        if (
            reset_R != int(row["reset_R"])
            or reset_K != int(row["reset_K"])
            or next_R != int(row["next_R"])
            or next_K != int(row["next_K"])
        ):
            raise AssertionError("reset chart continuation changed")
        source_C = source_K // carrier
        source_n = 4 * carrier - source_R
        source_d = prime - source_C
        if min(source_n, source_d) <= 0 or prime * source_n != 4 * carrier * source_d + 1:
            raise AssertionError("reset source overflow determinant changed")
        if carrier in edge_by_carrier:
            raise AssertionError("reset fixture has duplicate source carrier")
        edge_by_carrier[carrier] = next_carrier
        source_descriptor = {
            "equation_target": [4, prime],
            "R": source_R,
            "K": source_K,
            "charged_support": carrier,
        }
        reset_descriptor = {
            "equation_target": [4, prime],
            "R": reset_R,
            "K": reset_K,
            "charged_support": reset_support,
        }
        successor_descriptor = {
            "equation_target": [4, prime],
            "R": next_R,
            "K": next_K,
            "charged_support": next_carrier,
        }
        edge_rows.append(
            {
                "source_state": source_descriptor,
                "reset_state": reset_descriptor,
                "successor_state": successor_descriptor,
                "local_reset_decrease": True,
                "continuation_carrier_decrease": next_carrier < carrier,
            }
        )
    start = int(rows[0]["carrier"])
    trace: list[int] = []
    seen: dict[int, int] = {}
    current = start
    while current not in seen:
        seen[current] = len(trace)
        trace.append(current)
        if current not in edge_by_carrier:
            raise AssertionError("reset continuation left the focused graph")
        current = edge_by_carrier[current]
    cycle_nodes = trace[seen[current] :]
    if cycle_nodes != [132, 330]:
        raise AssertionError("focused reset cycle changed")
    descriptor = {
        "equation_target": [4, prime],
        "phase": "RESET",
        "cycle_nodes": cycle_nodes,
    }
    result = {
        "receipt_id": "reset-boundary:" + canonical_hash(descriptor),
        "certificate_type": "overflow_phase_reset_cycle_boundary",
        "phase": "RESET",
        "equation_target": {"numerator": 4, "denominator": prime},
        "cycle_witness": {
            "trace": trace,
            "cycle_nodes": cycle_nodes,
            "edges": edge_rows,
        },
        "local_rank": {
            "kind": "carrier_size",
            "strict_on_reset": True,
            "global_status": "rejected_by_reentry_cycle",
        },
        "marked_solution_set": {
            "source": "Sol(p)",
            "reset": "Sol(p)",
            "successor": "Sol(p)",
            "lift": "identity_on_focused_charts",
        },
        "target_fiber": {
            "status": "inherited_full_solution_set",
            "reason": "focused reset uses the chart-independent Sol(p) set",
        },
        "signed_defect": {"status": "not_carried"},
        "certificate_context": {
            "source": OVERFLOW_INPUT.name,
            "proof_boundary": "local_RESET_arithmetic_only",
            "missing_global_condition": "E5_well_founded_phase",
        },
        "normal_form": "overflow_phase_reset_v1",
        "potential_record": {
            "status": "local_only",
            "reason": "carrier decreases at RESET but re-entry closes a 132/330 cycle",
        },
        "e1_e5": {"E1": True, "E2": True, "E3": True, "E4": True, "E5": False},
        "missing_conditions": ["E5"],
        "selected_branch": "overflow_phase_reset_cycle_boundary",
        "selector_status": "candidate_transition",
        "recursive_edge_eligible": False,
        "scope_note": (
            "The local reset and identity lift are verified for this fixture, but the "
            "ordinary anchor/lcm continuation re-enters a carrier cycle; no global rank "
            "is inferred from local carrier decrease."
        ),
    }
    check_status_boundary(result)
    return {
        "cycle_count": 1,
        "receipts": [result],
        "scope_note": "RESET remains candidate_transition until an outer non-resettable rank is supplied.",
    }


def build_results() -> dict[str, object]:
    unified = json.loads(UNIFIED_INPUT.read_text(encoding="utf-8"))
    overflow = json.loads(OVERFLOW_INPUT.read_text(encoding="utf-8"))
    qadic = json.loads(QADIC_INPUT.read_text(encoding="utf-8"))
    phase = json.loads(PHASE_INPUT.read_text(encoding="utf-8"))
    fourier_payload = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    bottom_word_payload = json.loads(
        BOTTOM_WORD_CAPACITY_INPUT.read_text(encoding="utf-8")
    )
    source_word_payload = json.loads(
        SOURCE_WORD_CAPACITY_INPUT.read_text(encoding="utf-8")
    )
    large_slab_payload = json.loads(
        LARGE_SLAB_CAPACITY_INPUT.read_text(encoding="utf-8")
    )
    bounded_fourier_payload = json.loads(
        BOUNDED_FOURIER_CAPACITY_INPUT.read_text(encoding="utf-8")
    )
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
            normalized["generic_spectrum_profile"] = fourier_receipt[
                "generic_spectrum_profile"
            ]
            normalized["H"] = fourier_receipt["H"]
            normalized["J"] = fourier_receipt["J"]
            normalized["residual_block"] = fourier_receipt["residual_block"]
            normalized["target"] = fourier_receipt["target"]
        normalized_receipts.append(normalized)
    states = [state_receipt(receipt, UNIFIED_INPUT.name) for receipt in normalized_receipts]
    verified_edge = verified_fixed_n_edge(overflow)
    direct_type_ii = overflow_direct_type_ii(overflow)
    high_carrier_complement = overflow_high_carrier_p_plus_four_complement(overflow)
    d_one_g_rechart = overflow_d_one_p_minus_two_g_rechart(overflow)
    capacity = capacity_receipt(qadic, phase)
    bounded_fourier = bounded_fourier_capacity_receipt(bounded_fourier_payload)
    bottom_word = bottom_word_lattice_capacity_receipt(bottom_word_payload)
    source_word = source_word_joint_capacity_receipt(source_word_payload)
    large_slab = large_slab_factor_pair_capacity_receipt(large_slab_payload)
    overflow_menu = overflow_menu_receipts(overflow, qadic)
    fixed_n_outer_rank = overflow_fixed_n_outer_rank(overflow)
    fixed_n_bounded_divisor = overflow_fixed_n_bounded_divisor_outer_rank(overflow)
    same_chart_promotion = overflow_same_chart_support_promotion(overflow)
    a_one_boundary = overflow_a_one_generic_determinant_boundary(overflow)
    a_one_dual_reset = overflow_a_one_dual_reset_family(overflow)
    fixed_s_outer_rank = overflow_fixed_s_outer_rank(overflow)
    fixed_s_bounded_divisor = overflow_fixed_s_bounded_divisor_outer_rank(overflow)
    fixed_n_fixture_names = {
        receipt["certificate_context"]["fixture_name"]
        for receipt in fixed_n_outer_rank["verified_receipts"]
    }
    fixed_s_fixture_names = {
        receipt["certificate_context"]["fixture_name"]
        for receipt in fixed_s_outer_rank["verified_receipts"]
    }
    fixed_s_outer_rank["overlap_with_fixed_n_outer_rank_count"] = len(
        fixed_n_fixture_names & fixed_s_fixture_names
    )
    fixed_s_outer_rank["new_after_fixed_n_outer_rank_count"] = len(
        fixed_s_fixture_names - fixed_n_fixture_names
    )
    outer_rank_reset = overflow_outer_rank_reset(overflow)
    reset_boundary = phase_reset_boundary(overflow)
    debt_phase = support_debt_phase_receipt(outer_rank_reset, phase)
    universal_source = universal_source_anchor_receipt(overflow)
    return {
        "schema_version": 1,
        "arithmetic": "Typed dispatch for the representation-dual-capacity selector.",
        "selector_order": SELECTOR_ORDER,
        "status_lattice": STATUS_LATTICE,
        "source_receipts": [universal_source],
        "states": states,
        "verified_edges": [verified_edge],
        "overflow_direct_type_ii": direct_type_ii,
        "overflow_high_carrier_p_plus_four_complement": high_carrier_complement,
        "overflow_d_one_p_minus_two_g_rechart": d_one_g_rechart,
        "overflow_fixed_n_outer_rank": fixed_n_outer_rank,
        "overflow_fixed_n_bounded_divisor_outer_rank": fixed_n_bounded_divisor,
        "overflow_same_chart_support_promotion": same_chart_promotion,
        "overflow_a_one_generic_determinant_boundary": a_one_boundary,
        "overflow_a_one_dual_reset_family": a_one_dual_reset,
        "overflow_fixed_s_outer_rank": fixed_s_outer_rank,
        "overflow_fixed_s_bounded_divisor_outer_rank": fixed_s_bounded_divisor,
        "overflow_menu": overflow_menu,
        "overflow_outer_rank_reset": outer_rank_reset,
        "phase_reset_receipts": reset_boundary,
        "overflow_support_debt_phase_bridge": debt_phase,
        "bounded_fourier_carrier_capacity": bounded_fourier,
        "bottom_word_lattice_capacity": bottom_word,
        "source_word_joint_capacity": source_word,
        "large_slab_factor_pair_capacity": large_slab,
        "capacity_receipts": [
            bounded_fourier,
            debt_phase,
            capacity,
            bottom_word,
            source_word,
            large_slab,
        ],
        "invariants": {
            "analysis_evidence_never_recursive": True,
            "verified_edge_requires_E1_E5": True,
            "terminal_leaf_requires_direct_certificate": True,
            "direct_terminal_precedes_overflow_descent": True,
            "high_carrier_complement_requires_q3_factor": True,
            "high_carrier_complement_bound_replayed": True,
            "overflow_phase_requires_explicit_cross_state_mapping": True,
            "hard_core_negative_receipt_never_recursive": True,
            "fixed_n_overflow_rank_requires_positive_chart": True,
            "fixed_n_bounded_divisor_requires_bounded_support": True,
            "fixed_n_bounded_divisor_high_carrier_R_descent_replayed": True,
            "same_chart_promotion_requires_M_le_B_p": True,
            "a_one_determinant_boundary_requires_M_lt_p": True,
            "a_one_dual_reset_family_replayed": True,
            "fixed_s_overflow_rank_requires_product_divisor": True,
            "fixed_s_bounded_divisor_requires_product_divisor": True,
            "outer_rank_reset_requires_joined_support": True,
            "reset_cycle_boundary_requires_E5": True,
           "support_debt_phase_bridge_requires_alternate_mapping": True,
            "bottom_word_capacity_requires_signed_dictionary": True,
            "large_slab_capacity_requires_carrier_mapping": True,
            "d_one_rechart_is_g_analysis_only": True,
       },
        "source_sha256": source_hashes(),
        "scope_note": (
            "This receipt unifies state-local representation, dual, and capacity evidence. "
            "It contains fixed-n/fixed-s identity-lift edges and focused joined-support RESET edges, "
            "a high-carrier p+4 complement router, and a conditional support-debt phase bridge, "
            "but does not prove universal branch existence or well-founded descent for all overflow states."
        ),
    }


def verify_bounded_fourier_contract(result: dict[str, object]) -> None:
    receipt = result.get("bounded_fourier_carrier_capacity")
    if not isinstance(receipt, dict):
        raise AssertionError("bounded-Fourier carrier receipt missing")
    if receipt.get("selector_status") != "analysis_evidence":
        raise AssertionError("bounded-Fourier carrier receipt crossed status boundary")
    if receipt.get("recursive_edge_eligible") is not False:
        raise AssertionError("bounded-Fourier carrier receipt became recursive")
    if receipt.get("e1_e5") != {f"E{i}": False for i in range(1, 6)}:
        raise AssertionError("bounded-Fourier carrier receipt has an E1-E5 witness")
    summary = receipt.get("carrier_capacity_summary")
    if not isinstance(summary, dict):
        raise AssertionError("bounded-Fourier carrier summary missing")
    if summary.get("state_count") != 45 or summary.get("direction_count") != 141:
        raise AssertionError("bounded-Fourier carrier counts changed")
    families = summary.get("families")
    if not isinstance(families, dict):
        raise AssertionError("bounded-Fourier carrier family summary missing")
    for name, pair_count in (("same_color", 50), ("mixed_color", 78)):
        family = families.get(name)
        if not isinstance(family, dict):
            raise AssertionError(f"bounded-Fourier {name} family missing")
        if family.get("pair_check_count") != pair_count:
            raise AssertionError(f"bounded-Fourier {name} pair count changed")
        if family.get("divisibility_failure_count") != 0:
            raise AssertionError(f"bounded-Fourier {name} divisibility failure")
        if family.get("capacity_violation_count") != 0:
            raise AssertionError(f"bounded-Fourier {name} capacity violation")
    source_receipt = receipt.get("source_receipt")
    if not isinstance(source_receipt, dict):
        raise AssertionError("bounded-Fourier source receipt missing")
    if source_receipt.get("result_sha256") != sha256(BOUNDED_FOURIER_CAPACITY_INPUT):
        raise AssertionError("bounded-Fourier result hash changed")


def verify_bottom_word_lattice_contract(result: dict[str, object]) -> None:
    receipts = result.get("capacity_receipts")
    if not isinstance(receipts, list):
        raise AssertionError("capacity receipt list missing")
    matches = [
        receipt
        for receipt in receipts
        if isinstance(receipt, dict)
        and receipt.get("certificate_context", {}).get("certificate_type")
        == "bottom_word_lattice_pareto_cycle_capacity"
    ]
    if len(matches) != 1:
        raise AssertionError("bottom-word lattice capacity receipt shape changed")
    receipt = matches[0]
    if receipt.get("selector_status") != "analysis_evidence":
        raise AssertionError("bottom-word lattice receipt crossed status boundary")
    if receipt.get("recursive_edge_eligible") is not False:
        raise AssertionError("bottom-word lattice receipt became recursive")
    if receipt.get("e1_e5") != {f"E{i}": False for i in range(1, 6)}:
        raise AssertionError("bottom-word lattice receipt has an E1-E5 witness")
    lattice = receipt.get("lattice_summary")
    if not isinstance(lattice, dict):
        raise AssertionError("bottom-word lattice summary missing")
    generic = lattice.get("generic_word")
    cycle = lattice.get("cycle_word")
    if not isinstance(generic, dict) or not isinstance(cycle, dict):
        raise AssertionError("bottom-word lattice summary shape changed")
    if (
        generic.get("Q") != 8
        or generic.get("smith_diagonal") != [1, 8]
        or generic.get("root_capacity_bound") != 5
        or cycle.get("Q") != 4141
        or cycle.get("smith_diagonal") != [1, 4141]
    ):
        raise AssertionError("bottom-word lattice summary changed")
    cycle_capacity = receipt.get("cycle_capacity_summary")
    if not isinstance(cycle_capacity, dict):
        raise AssertionError("bottom-word cycle summary missing")
    if (
        cycle_capacity.get("static_separator_count") != 4
        or cycle_capacity.get("static_separator_prime") != 103
        or cycle_capacity.get("cycle_Q") != 4141
    ):
        raise AssertionError("bottom-word cycle summary changed")
    signed = receipt.get("signed_target_fiber_summary")
    if not isinstance(signed, dict):
        raise AssertionError("bottom-word signed capacity summary missing")
    if (
        signed.get("strong_miss_count") != 2
        or signed.get("strict_split_count") != 2
        or signed.get("common_overload_count") != 2
    ):
        raise AssertionError("bottom-word signed capacity summary changed")
    source_receipt = receipt.get("source_receipt")
    if not isinstance(source_receipt, dict):
        raise AssertionError("bottom-word lattice source receipt missing")
    if source_receipt.get("result_sha256") != sha256(BOTTOM_WORD_CAPACITY_INPUT):
        raise AssertionError("bottom-word lattice result hash changed")
    if source_receipt.get("generator_sha256") != sha256(BOTTOM_WORD_CAPACITY_SOURCE):
        raise AssertionError("bottom-word lattice generator hash changed")
    if source_receipt.get("formal_closure_sha256") != sha256(BOTTOM_WORD_CLOSURE_SOURCE):
        raise AssertionError("bottom-word lattice closure hash changed")


def verify_support_debt_phase_contract(result: dict[str, object]) -> None:
    receipt = result.get("overflow_support_debt_phase_bridge")
    if not isinstance(receipt, dict):
        raise AssertionError("support-debt phase bridge receipt missing")
    if receipt.get("selector_status") != "analysis_evidence":
        raise AssertionError("support-debt phase bridge crossed status boundary")
    if receipt.get("recursive_edge_eligible") is not False:
        raise AssertionError("support-debt phase bridge became recursive")
    if receipt.get("e1_e5") != {f"E{i}": False for i in range(1, 6)}:
        raise AssertionError("support-debt phase bridge has an E1-E5 witness")
    context = receipt.get("certificate_context")
    if not isinstance(context, dict):
        raise AssertionError("support-debt phase bridge context missing")
    if context.get("alternate_phase_mapping_status") != "unproved":
        raise AssertionError("support-debt phase bridge mapping status changed")
    summary = receipt.get("support_debt_phase_summary")
    if not isinstance(summary, dict) or summary.get("linked_row_count") != 17:
        raise AssertionError("support-debt phase link count changed")
    if summary.get("phase_summary") != {
        "obstruction_row_count": 17,
        "q_group_count": 5,
        "phase_cell_count": 13,
        "compatible_pair_count": 5,
        "pair_count": 31,
        "capacity_overload_cell_count": 0,
    }:
        raise AssertionError("support-debt phase summary changed")
    links = summary.get("links")
    if not isinstance(links, list) or len(links) != 17:
        raise AssertionError("support-debt phase link shape changed")
    for link in links:
        if not isinstance(link, dict):
            raise AssertionError("support-debt phase link is not an object")
        channel = link.get("channel")
        if not isinstance(channel, list) or len(channel) != 4:
            raise AssertionError("support-debt phase channel shape changed")
        q = link.get("q")
        modulus = link.get("unit_modulus")
        unit = link.get("normalized_unit")
        if (
            not isinstance(q, int)
            or not isinstance(modulus, int)
            or not isinstance(unit, int)
            or q <= 1
            or modulus <= 1
            or not 0 < unit < modulus
            or gcd(unit, modulus) != 1
        ):
            raise AssertionError("support-debt phase unit is not normalized")
    source_receipt = receipt.get("source_receipt")
    if not isinstance(source_receipt, dict):
        raise AssertionError("support-debt phase source receipt missing")
    if source_receipt.get("phase_sha256") != sha256(PHASE_INPUT):
        raise AssertionError("support-debt phase result hash changed")


def verify_source_word_joint_capacity_contract(result: dict[str, object]) -> None:
    receipts = result.get("capacity_receipts")
    if not isinstance(receipts, list):
        raise AssertionError("capacity receipt list missing")
    matches = [
        receipt
        for receipt in receipts
        if isinstance(receipt, dict)
        and receipt.get("certificate_context", {}).get("certificate_type")
        == "source_word_joint_capacity_dichotomy"
    ]
    if len(matches) != 1:
        raise AssertionError("source-word capacity receipt shape changed")
    receipt = matches[0]
    if receipt.get("selector_status") != "analysis_evidence":
        raise AssertionError("source-word capacity receipt crossed status boundary")
    if receipt.get("recursive_edge_eligible") is not False:
        raise AssertionError("source-word capacity receipt became recursive")
    if receipt.get("e1_e5") != {f"E{i}": False for i in range(1, 6)}:
        raise AssertionError("source-word capacity receipt has an E1-E5 witness")
    summary = receipt.get("joint_capacity_summary")
    if not isinstance(summary, dict):
        raise AssertionError("source-word joint summary missing")
    if summary.get("cross_pair_count") != 14 or summary.get("branch_histogram") != {
        "common_overload": 7,
        "split_exchange": 7,
    }:
        raise AssertionError("source-word joint summary changed")
    counterexample = summary.get("complete_reach_split_counterexample")
    if counterexample != {"prime": 2017, "R": 207, "node_count": 4}:
        raise AssertionError("source-word split counterexample summary changed")
    source_receipt = receipt.get("source_receipt")
    if not isinstance(source_receipt, dict):
        raise AssertionError("source-word capacity source receipt missing")
    if source_receipt.get("result_sha256") != sha256(SOURCE_WORD_CAPACITY_INPUT):
        raise AssertionError("source-word capacity result hash changed")
    if source_receipt.get("frozen_input_sha256") != sha256(SOURCE_WORD_FROZEN_INPUT):
        raise AssertionError("source-word frozen input hash changed")
    if source_receipt.get("formal_closure_sha256") != sha256(BOTTOM_WORD_CLOSURE_SOURCE):
        raise AssertionError("source-word closure hash changed")


def verify_large_slab_factor_pair_capacity_contract(result: dict[str, object]) -> None:
    receipts = result.get("capacity_receipts")
    if not isinstance(receipts, list):
        raise AssertionError("capacity receipt list missing")
    matches = [
        receipt
        for receipt in receipts
        if isinstance(receipt, dict)
        and receipt.get("certificate_context", {}).get("certificate_type")
        == "large_slab_factor_pair_layer_capacity"
    ]
    if len(matches) != 1:
        raise AssertionError("large-slab capacity receipt shape changed")
    receipt = matches[0]
    if (
        receipt.get("selector_status") != "analysis_evidence"
        or receipt.get("recursive_edge_eligible") is not False
        or receipt.get("e1_e5") != {f"E{i}": False for i in range(1, 6)}
    ):
        raise AssertionError("large-slab capacity receipt crossed status boundary")
    summary = receipt.get("large_slab_summary")
    if not isinstance(summary, dict):
        raise AssertionError("large-slab capacity summary missing")
    expected = {
        "slab_case_count": 4,
        "covered_alpha": [1, 2, 3],
        "admissible_factor_pair_count": 5,
        "layer_gcd_pair_check_count": 105,
        "same_exponent_check_count": 15,
        "repeated_carrier_count": 4,
        "source_word_carrier_case_count": 5,
        "source_word_slab_q_union_hit_count": 4,
        "alpha_branch_counts": {"1": 2, "2": 1, "3": 1},
    }
    if any(summary.get(key) != value for key, value in expected.items()):
        raise AssertionError("large-slab capacity summary changed")
    branch_records = summary.get("alpha_branch_records")
    if (
        not isinstance(branch_records, list)
        or len(branch_records) != 4
        or {int(row["alpha"]) for row in branch_records if isinstance(row, dict)}
        != {1, 2, 3}
    ):
        raise AssertionError("large-slab alpha branch records changed")
    if summary.get("source_word_q_union_negative_boundary") != {
        "prime": 10_170_169,
        "q": 101,
    }:
        raise AssertionError("large-slab q-union negative boundary changed")
    source_receipt = receipt.get("source_receipt")
    if not isinstance(source_receipt, dict):
        raise AssertionError("large-slab capacity source receipt missing")
    if source_receipt.get("result_sha256") != sha256(LARGE_SLAB_CAPACITY_INPUT):
        raise AssertionError("large-slab capacity result hash changed")
    if source_receipt.get("generator_sha256") != sha256(LARGE_SLAB_CAPACITY_SOURCE):
        raise AssertionError("large-slab capacity generator hash changed")


def verify_high_carrier_complement_contract(result: dict[str, object]) -> None:
    receipt = result.get("overflow_high_carrier_p_plus_four_complement")
    if not isinstance(receipt, dict):
        raise AssertionError("high-carrier complement receipt missing")
    if (
        receipt.get("fixture_count") != 12
        or receipt.get("high_carrier_count") != 1
        or receipt.get("not_applicable_count") != 11
        or receipt.get("verified_terminal_count") != 1
        or receipt.get("hard_core_count") != 0
    ):
        raise AssertionError("high-carrier complement counts changed")
    rows = receipt.get("receipts")
    if not isinstance(rows, list) or len(rows) != 12:
        raise AssertionError("high-carrier complement receipt shape changed")
    high_rows = [row for row in rows if row["classification"]["high_carrier"]]
    if len(high_rows) != 1:
        raise AssertionError("high-carrier complement fixture changed")
    high = high_rows[0]
    classification = high.get("classification")
    if not isinstance(classification, dict):
        raise AssertionError("high-carrier classification missing")
    bound = classification.get("complement_bound")
    if (
        classification.get("prime") != 73
        or classification.get("carrier") != 1518
        or classification.get("n") != 2329
        or classification.get("B_p") != 1296
        or not isinstance(bound, dict)
        or bound.get("necessary_condition") != "n=p or n>=p+4"
        or bound.get("case") != "n>=p+4"
        or bound.get("p_plus_four") != 77
        or bound.get("q_congruent_3_mod_4") != [7, 11]
    ):
        raise AssertionError("high-carrier complement boundary changed")
    if (
        high.get("selector_status") != "terminal_leaf"
        or high.get("recursive_edge_eligible") is not False
        or high.get("gap") != 7
        or high.get("identity", {}).get("verified_exactly") is not True
    ):
        raise AssertionError("high-carrier Type II terminal changed")

    # Keep the factor-filter boundary executable even though the focused source
    # fixture currently lies in the terminal subfamily.
    synthetic = high_carrier_complement_classification(97, 2449, 1)
    synthetic_bound = synthetic.get("complement_bound")
    if (
        not synthetic["applicable"]
        or synthetic["direct_terminal_available"]
        or synthetic["selector_status"] != "analysis_evidence"
        or synthetic.get("n") != 101
        or not isinstance(synthetic_bound, dict)
        or synthetic_bound.get("case") != "n>=p+4"
        or synthetic_bound.get("p_plus_four") != 101
        or synthetic_bound.get("q_congruent_3_mod_4") != []
    ):
        raise AssertionError("synthetic high-carrier factor-filter boundary changed")
    exact_boundary = high_carrier_complement_classification(97, 2352, 1)
    exact_bound = exact_boundary.get("complement_bound")
    if (
        not exact_boundary["applicable"]
        or exact_boundary.get("n") != 97
        or not isinstance(exact_bound, dict)
        or exact_bound.get("case") != "n=p"
    ):
        raise AssertionError("n=p high-carrier boundary changed")


def verify_universal_source_anchor_contract(result: dict[str, object]) -> None:
    receipts = result.get("source_receipts")
    if not isinstance(receipts, list) or len(receipts) != 1:
        raise AssertionError("universal source receipt shape changed")
    receipt = receipts[0]
    if not isinstance(receipt, dict):
        raise AssertionError("universal source receipt is not an object")
    if receipt.get("selector_status") != "analysis_evidence":
        raise AssertionError("universal source receipt crossed status boundary")
    if receipt.get("recursive_edge_eligible") is not False:
        raise AssertionError("universal source receipt became recursive")
    if receipt.get("e1_e5") != {f"E{i}": False for i in range(1, 6)}:
        raise AssertionError("universal source receipt has an E1-E5 witness")
    context = receipt.get("certificate_context")
    if not isinstance(context, dict):
        raise AssertionError("universal source context missing")
    if context.get("source_formula") != "(U,V,m)=(p,R(p-1)-p,p-1)":
        raise AssertionError("universal source formula changed")
    summary = receipt.get("source_summary")
    if not isinstance(summary, dict):
        raise AssertionError("universal source summary missing")
    if summary.get("universal_p_source_count") != 3 or summary.get("focused_record_count") != 3:
        raise AssertionError("universal source counts changed")
    if summary.get("cycle_length_histogram") != {"1": 1, "3": 1, "4": 1}:
        raise AssertionError("universal anchor cycle lengths changed")
    if summary.get("orbit_classification_counts") != {"marked_absorb": 4, "overflow": 4}:
        raise AssertionError("universal anchor classifications changed")
    records = summary.get("records")
    if not isinstance(records, list) or len(records) != 3:
        raise AssertionError("universal source records changed")
    for record in records:
        if not isinstance(record, dict):
            raise AssertionError("universal source record shape changed")
        prime = int(record["prime"])
        modulus = int(record["R"])
        if record.get("source") != [prime, modulus * (prime - 1) - prime, prime - 1]:
            raise AssertionError("universal source witness changed")
        if record.get("destination") != [1, modulus - 1, 1]:
            raise AssertionError("universal source destination changed")
        cycle = record.get("cycle")
        rows = record.get("rows")
        if not isinstance(cycle, list) or not isinstance(rows, list) or len(cycle) != len(record["orbit"]):
            raise AssertionError("universal anchor orbit record changed")
        for row in rows:
            if not isinstance(row, dict) or row.get("h") not in cycle:
                raise AssertionError("universal anchor row changed")
    source_receipt = receipt.get("source_receipt")
    if not isinstance(source_receipt, dict):
        raise AssertionError("universal source hash receipt missing")
    if source_receipt.get("result_sha256") != sha256(UNIVERSAL_ANCHOR_INPUT):
        raise AssertionError("universal source input hash changed")


def verify_d_one_g_rechart_contract(result: dict[str, object]) -> None:
    branch = result.get("overflow_d_one_p_minus_two_g_rechart")
    if not isinstance(branch, dict):
        raise AssertionError("d=1 G rechart receipt missing")
    if branch.get("fixture_count") != 1 or branch.get("g_rechart_count") != 1:
        raise AssertionError("focused d=1 G rechart count changed")
    if branch.get("p_plus_four_terminal_probe_count") != 1:
        raise AssertionError("focused d=1 p+4 probe count changed")
    receipts = branch.get("receipts")
    if not isinstance(receipts, list) or len(receipts) != 1:
        raise AssertionError("d=1 G rechart receipt shape changed")
    for receipt in receipts:
        if not isinstance(receipt, dict):
            raise AssertionError("d=1 G rechart row is not an object")
        if (
            receipt.get("certificate_type") != "overflow_d_one_p_minus_two_g_rechart"
            or receipt.get("selector_status") != "analysis_evidence"
            or receipt.get("recursive_edge_eligible") is not False
            or receipt.get("state_class") != "G"
            or receipt.get("e1_e5") != {f"E{i}": False for i in range(1, 6)}
        ):
            raise AssertionError("d=1 G rechart crossed the status boundary")
        separator = receipt.get("g_separator")
        if not isinstance(separator, dict):
            raise AssertionError("d=1 Jacobi separator missing")
        values = separator.get("support_values")
        if not isinstance(values, dict) or any(value != 1 for value in values.values()):
            raise AssertionError("d=1 support Jacobi values changed")
        if separator.get("target_minus_one") != -1:
            raise AssertionError("d=1 target Jacobi value changed")
        successor = receipt.get("successor_state")
        if not isinstance(successor, dict):
            raise AssertionError("d=1 successor state missing")
        prime = int(receipt["equation_target"]["denominator"])
        if successor.get("R") != prime - 2 or successor.get("K") != (prime - 1) ** 2 // 4:
            raise AssertionError("d=1 p-2 successor changed")


def verify_overflow_fixed_n_bounded_divisor_contract(
    result: dict[str, object],
) -> None:
    branch = result.get("overflow_fixed_n_bounded_divisor_outer_rank")
    if not isinstance(branch, dict):
        raise AssertionError("bounded fixed-n divisor receipt missing")
    if (
        branch.get("fixture_count") != 12
        or branch.get("verified_edge_count") != 12
        or branch.get("rejected_fixture_count") != 0
    ):
        raise AssertionError("bounded fixed-n divisor counts changed")
    receipts = branch.get("verified_receipts")
    rejected = branch.get("rejected_fixtures")
    if not isinstance(receipts, list) or len(receipts) != 12:
        raise AssertionError("bounded fixed-n divisor receipt shape changed")
    if not isinstance(rejected, list) or rejected:
        raise AssertionError("bounded fixed-n divisor unexpectedly rejected a fixture")
    for receipt in receipts:
        if not isinstance(receipt, dict):
            raise AssertionError("bounded fixed-n divisor row is not an object")
        if (
            receipt.get("certificate_type")
            != "overflow_fixed_n_bounded_divisor_outer_rank"
            or receipt.get("selector_status") != "verified_edge"
            or receipt.get("recursive_edge_eligible") is not True
            or receipt.get("e1_e5") != {f"E{i}": True for i in range(1, 6)}
        ):
            raise AssertionError("bounded fixed-n divisor crossed the status boundary")
        source = receipt.get("source_state")
        successor = receipt.get("successor_state")
        context = receipt.get("certificate_context")
        potential = receipt.get("potential_record")
        if (
            not isinstance(source, dict)
            or not isinstance(successor, dict)
            or not isinstance(context, dict)
            or not isinstance(potential, dict)
        ):
            raise AssertionError("bounded fixed-n divisor payload is incomplete")
        determinant = context.get("determinant")
        selected = context.get("selected_candidate")
        high_carrier_rank = receipt.get("high_carrier_R_descent")
        if not isinstance(determinant, dict) or not isinstance(selected, dict):
            raise AssertionError("bounded fixed-n divisor determinant payload changed")
        if not isinstance(high_carrier_rank, dict):
            raise AssertionError("high-carrier R descent payload missing")
        prime = int(receipt["equation_target"]["denominator"])
        M = int(determinant["M"])
        d = int(determinant["d"])
        n = int(determinant["pn"]) // prime
        S = int(determinant["S"])
        L = int(selected["L"])
        target_R = int(successor["R"])
        target_K = int(successor["K"])
        source_support = int(source["absorbed_support"])
        B_prime = (prime - 1) ** 2 // 4
        support_retained = L % source_support == 0
        high_carrier = M > B_prime
        if (
            S != M * d
            or prime * n != 4 * S + 1
            or S % L
            or source_support >= L
            or L > B_prime
            or 4 * L <= n
            or target_R != 4 * L - n
            or target_K != L * (prime - S // L)
            or canonical_chart(prime, L) != (target_R, target_K)
            or B_prime // L >= B_prime // source_support
            or potential.get("strict_decrease") is not True
            or potential.get("support_monotone") is not support_retained
            or potential.get("support_reset_paid") is not (not support_retained)
            or potential.get("outer_rank_reset") is not (not support_retained)
        ):
            raise AssertionError("bounded fixed-n divisor identity changed")
        if (
            high_carrier_rank.get("condition") != "M>B_p"
            or high_carrier_rank.get("applicable") is not high_carrier
            or high_carrier_rank.get("bounded_successor")
            != ("L<=B_p<M" if high_carrier else "L<=B_p")
            or high_carrier_rank.get("source_carrier") != M
            or high_carrier_rank.get("successor_carrier") != L
            or high_carrier_rank.get("source_R") != int(source["R"])
            or high_carrier_rank.get("successor_R") != target_R
            or high_carrier_rank.get("delta_R") != int(source["R"]) - target_R
            or high_carrier_rank.get("identity") != "R_M-R_L=4*(M-L)"
            or high_carrier_rank.get("strict_decrease")
            is not (high_carrier and target_R < int(source["R"]))
        ):
            raise AssertionError("high-carrier R descent identity changed")
        if high_carrier and not (L <= B_prime < M and target_R < int(source["R"])):
            raise AssertionError("high-carrier bounded successor did not lower R")
        if successor.get("absorbed_support") != L:
            raise AssertionError("bounded fixed-n divisor support changed")


def verify_overflow_fixed_s_bounded_divisor_contract(
    result: dict[str, object],
) -> None:
    branch = result.get("overflow_fixed_s_bounded_divisor_outer_rank")
    if not isinstance(branch, dict):
        raise AssertionError("bounded fixed-s divisor receipt missing")
    if (
        branch.get("fixture_count") != 12
        or branch.get("verified_edge_count") != 11
        or branch.get("absorption_target_count") != 1
        or branch.get("overflow_target_count") != 10
        or branch.get("rejected_fixture_count") != 1
    ):
        raise AssertionError("bounded fixed-s divisor counts changed")
    receipts = branch.get("verified_receipts")
    rejected = branch.get("rejected_fixtures")
    if not isinstance(receipts, list) or len(receipts) != 11:
        raise AssertionError("bounded fixed-s divisor receipt shape changed")
    if not isinstance(rejected, list) or len(rejected) != 1:
        raise AssertionError("bounded fixed-s divisor rejection shape changed")
    if rejected[0].get("fixture_name") != "reachable_conflict_bundle_3":
        raise AssertionError("bounded fixed-s divisor boundary changed")
    subfamily = branch.get("unconditional_fixed_s_subfamily")
    if not isinstance(subfamily, dict):
        raise AssertionError("bounded fixed-s sufficient subfamily missing")
    if subfamily.get("condition") != "r>=2A" or subfamily.get("candidate") != "L=r":
        raise AssertionError("bounded fixed-s sufficient condition changed")
    expected_subfamily = {
        "accumulated_d_one_boundary",
        "accumulated_positive_fixed_n_edge",
        "empty_fixed_n_window",
        "reachable_conflict_bundle_0",
        "root_edge_0",
        "root_edge_1",
        "symmetric_small_chart_support_conflict",
    }
    if (
        subfamily.get("fixture_count") != len(expected_subfamily)
        or set(subfamily.get("fixture_names", [])) != expected_subfamily
    ):
        raise AssertionError("bounded fixed-s sufficient subfamily coverage changed")
    product_subfamily = branch.get("unconditional_product_saturation_subfamily")
    if not isinstance(product_subfamily, dict):
        raise AssertionError("bounded fixed-s product subfamily missing")
    expected_product_subfamily = {
        "accumulated_d_one_boundary",
        "empty_fixed_n_window",
        "reachable_conflict_bundle_0",
        "reachable_conflict_bundle_1",
        "root_edge_0",
        "root_edge_1",
        "symmetric_small_chart_support_conflict",
    }
    if (
        product_subfamily.get("condition") != "2A<=r*d<=B_p"
        or product_subfamily.get("candidate") != "L=r*d"
        or product_subfamily.get("fixture_count") != len(expected_product_subfamily)
        or set(product_subfamily.get("fixture_names", [])) != expected_product_subfamily
    ):
        raise AssertionError("bounded fixed-s product subfamily coverage changed")
    d_subfamily = branch.get("unconditional_d_saturation_subfamily")
    if not isinstance(d_subfamily, dict):
        raise AssertionError("bounded fixed-s d subfamily missing")
    expected_d_subfamily = {
        "accumulated_positive_fixed_n_edge",
        "reachable_conflict_bundle_2",
        "root_edge_0",
        "root_edge_1",
        "symmetric_small_chart_support_conflict",
    }
    if (
        d_subfamily.get("condition") != "2A<=d<=B_p"
        or d_subfamily.get("candidate") != "L=d"
        or d_subfamily.get("fixture_count") != len(expected_d_subfamily)
        or set(d_subfamily.get("fixture_names", [])) != expected_d_subfamily
    ):
        raise AssertionError("bounded fixed-s d subfamily coverage changed")
    r_one_boundary = branch.get("r_one_fixed_s_boundary")
    if not isinstance(r_one_boundary, dict):
        raise AssertionError("bounded fixed-s r=1 boundary missing")
    if (
        r_one_boundary.get("condition")
        != "r=1, d=(p-1)/4, s=1, B_p=4*d^2"
        or r_one_boundary.get("candidate_rule")
        != "A<d => L=d; A>=d => no divisor L|r*d with L>A"
        or r_one_boundary.get("fixture_count") != 1
        or set(r_one_boundary.get("edge_fixture_names", [])) != set()
        or set(r_one_boundary.get("empty_fixture_names", []))
        != {"reachable_conflict_bundle_3"}
    ):
        raise AssertionError("bounded fixed-s r=1 boundary changed")
    d_one_boundary = branch.get("d_one_fixed_s_boundary")
    if not isinstance(d_one_boundary, dict):
        raise AssertionError("bounded fixed-s d=1 boundary missing")
    if (
        d_one_boundary.get("condition")
        != "d=1, r=(p-1)/4, s=1, B_p=4*r^2"
        or d_one_boundary.get("candidate_rule")
        != "A<r => L=r; A>=r => no divisor L|r*d with L>A"
        or d_one_boundary.get("fixture_count") != 1
        or set(d_one_boundary.get("edge_fixture_names", []))
        != {"accumulated_d_one_boundary"}
        or set(d_one_boundary.get("empty_fixture_names", [])) != set()
    ):
        raise AssertionError("bounded fixed-s d=1 boundary changed")
    cofactor_subfamily = branch.get("unconditional_cofactor_saturation_subfamily")
    if not isinstance(cofactor_subfamily, dict):
        raise AssertionError("bounded fixed-s cofactor subfamily missing")
    expected_cofactor_subfamily = {
        "accumulated_positive_fixed_n_edge",
        "empty_fixed_n_window",
        "reachable_conflict_bundle_0",
        "reachable_conflict_bundle_1",
        "reachable_conflict_bundle_2",
        "root_edge_0",
        "root_edge_1",
        "lcm_cycle_step_0",
        "lcm_cycle_step_1",
        "symmetric_small_chart_support_conflict",
    }
    if (
        cofactor_subfamily.get("condition")
        != "ell=spf(r*d), 2A<=r*d/ell<=B_p"
        or cofactor_subfamily.get("candidate") != "L=r*d/ell"
        or cofactor_subfamily.get("fixture_count")
        != len(expected_cofactor_subfamily)
        or set(cofactor_subfamily.get("fixture_names", []))
        != expected_cofactor_subfamily
    ):
        raise AssertionError("bounded fixed-s cofactor subfamily coverage changed")
    power_cofactor_subfamily = branch.get("unconditional_prime_power_cofactor_subfamily")
    if not isinstance(power_cofactor_subfamily, dict):
        raise AssertionError("bounded fixed-s prime-power cofactor subfamily missing")
    expected_power_cofactor_subfamily = expected_cofactor_subfamily
    if (
        power_cofactor_subfamily.get("condition")
        != (
            "ell=spf(r*d), e=min{j>=1: r*d/ell^j<=B_p}, "
            "ell^e<p, 2A<=r*d/ell^e"
        )
        or power_cofactor_subfamily.get("candidate") != "L=r*d/ell^e"
        or power_cofactor_subfamily.get("fixture_count")
        != len(expected_power_cofactor_subfamily)
        or set(power_cofactor_subfamily.get("fixture_names", []))
        != expected_power_cofactor_subfamily
    ):
        raise AssertionError("bounded fixed-s prime-power cofactor coverage changed")
    high_product_boundary = branch.get("high_product_prime_power_boundary")
    if not isinstance(high_product_boundary, dict):
        raise AssertionError("high-product prime-power boundary missing")
    if (
        high_product_boundary.get("condition") != "P=r*d>B_p and P<=4B_p"
        or high_product_boundary.get("classification")
        != (
            "If P/ell>B_p for ell=spf(P), then ell in {2,3}; "
            "if v_ell(P)>=2, P/ell^2<=B_p and ell^2<p; "
            "otherwise v_ell(P)=1 and the residual is squarefree at ell, "
            "or the bounded cofactor is below 2A."
        )
        or high_product_boundary.get("conclusion")
        != (
            "Prime-power cofactor failure above B_p is reduced to a single "
            "2-or-3 factor boundary or to support saturation A>P/ell^e."
        )
    ):
        raise AssertionError("high-product prime-power boundary changed")
    large_prime_subfamily = branch.get("unconditional_large_prime_cofactor_subfamily")
    if not isinstance(large_prime_subfamily, dict):
        raise AssertionError("bounded fixed-s large-prime cofactor subfamily missing")
    expected_large_prime_subfamily = {
        "accumulated_positive_fixed_n_edge",
        "reachable_conflict_bundle_2",
        "lcm_cycle_step_0",
    }
    if (
        large_prime_subfamily.get("condition")
        != "P=r*d>B_p, q|P, q>=5, 2A<=P/q<=B_p"
        or large_prime_subfamily.get("candidate") != "L=P/q"
        or large_prime_subfamily.get("fixture_count")
        != len(expected_large_prime_subfamily)
        or set(large_prime_subfamily.get("fixture_names", []))
        != expected_large_prime_subfamily
    ):
        raise AssertionError("bounded fixed-s large-prime cofactor coverage changed")
    smooth23_residual = branch.get("smooth23_fixed_s_residual")
    if not isinstance(smooth23_residual, dict):
        raise AssertionError("bounded fixed-s 2,3-smooth residual missing")
    if (
        smooth23_residual.get("condition")
        != "no admissible fixed-s L and Supp(r*d) subset {2,3}"
        or smooth23_residual.get("fixture_count") != 1
        or set(smooth23_residual.get("fixture_names", []))
        != {"reachable_conflict_bundle_3"}
        or smooth23_residual.get("one_dimensional_fixture_count") != 1
        or set(smooth23_residual.get("one_dimensional_fixture_names", []))
        != {"reachable_conflict_bundle_3"}
        or smooth23_residual.get("genuine_two_dimensional_fixture_count") != 0
        or set(smooth23_residual.get("genuine_two_dimensional_fixture_names", []))
        != set()
        or smooth23_residual.get("selector_status") != "analysis_evidence"
        or smooth23_residual.get("recursive_edge_eligible") is not False
        or smooth23_residual.get("boundary_lemma")
        != (
            "For L_plus=max{L|r*d: L<=B_p and 4L>s}, L_plus>=2A "
            "implies an admissible fixed-s edge; every rejected row therefore has L_plus<2A."
        )
        or smooth23_residual.get("routing")
        != {
            "one_dimensional": [
                "r_one_fixed_s_boundary",
                "d_one_fixed_s_boundary",
                "type_ii",
                "q_adic_capacity",
            ],
            "genuine_two_dimensional": [
                "generalized_dyadic",
                "type_ii",
                "q_adic_capacity",
            ],
        }
    ):
        raise AssertionError("bounded fixed-s 2,3-smooth residual changed")
    grid_receipts = smooth23_residual.get("grid_receipts")
    if not isinstance(grid_receipts, list) or len(grid_receipts) != 1:
        raise AssertionError("bounded fixed-s smooth grid receipt changed")
    grid_receipt = grid_receipts[0]
    if (
        not isinstance(grid_receipt, dict)
        or grid_receipt.get("fixture_name") != "reachable_conflict_bundle_3"
        or grid_receipt.get("product") != 18
        or grid_receipt.get("factorization") != [[2, 1], [3, 2]]
        or grid_receipt.get("source_support") != 19
        or grid_receipt.get("max_positive_bounded_divisor") != 18
        or grid_receipt.get("boundary_gap") != 20
        or grid_receipt.get("boundary_condition_verified") is not True
        or grid_receipt.get("grid_dimension") != "one_dimensional_boundary"
    ):
        raise AssertionError("bounded fixed-s smooth grid frontier changed")
    family = smooth23_residual.get("parametric_family")
    if not isinstance(family, dict):
        raise AssertionError("bounded fixed-s smooth parametric family missing")
    if (
        family.get("condition")
        != (
            "P=2^a*3^b, a,b>=1, p=4P+1 prime, r=2, d=P/2, "
            "M=k*p+r, A=M, 1<=k<=floor((B_p-r)/p)"
        )
        or family.get("parameter_range") != "1<=k<=floor((B_p-r)/p)"
        or family.get("seed_count") != 5
        or family.get("source_reach_status") != "unproved"
        or family.get("selector_status") != "analysis_evidence"
        or family.get("recursive_edge_eligible") is not False
        or family.get("proof_boundary")
        != "smooth23_parametric_fixed_s_support_saturation"
    ):
        raise AssertionError("bounded fixed-s smooth parametric family changed")
    seeds = family.get("seeds")
    if not isinstance(seeds, list) or len(seeds) != 5:
        raise AssertionError("bounded fixed-s smooth family seed shape changed")
    expected_seed_pairs = {
        (1, 2, 73),
        (3, 1, 97),
        (4, 1, 193),
        (2, 3, 433),
        (2, 4, 1297),
    }
    actual_seed_pairs = {
        (
            int(seed["exponents"][0]),
            int(seed["exponents"][1]),
            int(seed["prime"]),
        )
        for seed in seeds
        if isinstance(seed, dict)
        and isinstance(seed.get("exponents"), list)
        and len(seed["exponents"]) == 2
    }
    if actual_seed_pairs != expected_seed_pairs:
        raise AssertionError("bounded fixed-s smooth family seed coverage changed")
    for seed in seeds:
        if not isinstance(seed, dict):
            raise AssertionError("bounded fixed-s smooth family seed is not an object")
        rows = seed.get("checked_rows")
        if not isinstance(rows, list) or not rows:
            raise AssertionError("bounded fixed-s smooth family rows missing")
        if int(seed["k_max"]) < 1:
            raise AssertionError("bounded fixed-s smooth family k range changed")
        for row in rows:
            if (
                not isinstance(row, dict)
                or row.get("fixed_s") != 1
                or row.get("fixed_s_candidate_count") != 0
                or int(row["max_positive_bounded_divisor"]) >= int(row["source_support"])
                or int(row["R"]) <= int(seed["prime"])
                or int(row["K"]) % int(row["carrier"])
            ):
                raise AssertionError("bounded fixed-s smooth family row changed")
    k_one = family.get("k_one_fixed_n_saturation")
    if not isinstance(k_one, dict):
        raise AssertionError("smooth k=1 fixed-n saturation receipt missing")
    if (
        k_one.get("condition")
        != (
            "P=2^a*3^b, p=4P+1 prime, r=2, d=P/2, M=p+2, "
            "n=2P+1, A=M"
        )
        or k_one.get("seed_count") != 5
        or k_one.get("source_reach_status") != "unproved"
        or k_one.get("selector_status")
        != "verified_edge_conditional_on_reachability"
        or k_one.get("recursive_edge_eligible") is not True
        or k_one.get("proof_boundary") != "smooth23_k_one_fixed_n_saturation"
    ):
        raise AssertionError("smooth k=1 fixed-n saturation metadata changed")
    k_one_receipts = k_one.get("receipts")
    if not isinstance(k_one_receipts, list) or len(k_one_receipts) != 5:
        raise AssertionError("smooth k=1 fixed-n saturation receipt shape changed")
    for receipt in k_one_receipts:
        if not isinstance(receipt, dict):
            raise AssertionError("smooth k=1 fixed-n saturation row is not an object")
        if (
            receipt.get("certificate_type")
            != "smooth23_k_one_fixed_n_saturation"
            or receipt.get("selector_status") != "verified_edge"
            or receipt.get("recursive_edge_eligible") is not True
            or receipt.get("source_reach_status") != "unproved"
            or receipt.get("e1_e5") != {f"E{i}": True for i in range(1, 6)}
        ):
            raise AssertionError("smooth k=1 fixed-n saturation crossed status boundary")
        source = receipt.get("source_state")
        successor = receipt.get("successor_state")
        determinant = receipt.get("determinant")
        selected = receipt.get("selected_candidate")
        potential = receipt.get("potential_record")
        if not all(
            isinstance(value, dict)
            for value in (source, successor, determinant, selected, potential)
        ):
            raise AssertionError("smooth k=1 fixed-n saturation payload incomplete")
        prime = int(receipt["equation_target"]["denominator"])
        M = int(determinant["M"])
        d = int(determinant["d"])
        n = int(determinant["n"])
        S = int(determinant["S"])
        L = int(selected["L"])
        B_prime = (prime - 1) ** 2 // 4
        if (
            determinant.get("identity") != "p*n=4*M*d+1"
            or prime * n != 4 * M * d + 1
            or L != S
            or L != M * d
            or L > B_prime
            or M >= L
            or 4 * L <= n
            or int(selected["R_L"]) != 4 * L - n
            or int(selected["K_L"]) != L * (prime - 1)
            or canonical_chart(prime, L)
            != (int(selected["R_L"]), int(selected["K_L"]))
            or int(potential["source"]) != B_prime // M
            or int(potential["successor"]) != B_prime // L
            or potential.get("strict_decrease") is not True
            or potential.get("support_monotone") is not True
        ):
            raise AssertionError("smooth k=1 fixed-n saturation identity changed")
    low_k = family.get("low_k_fixed_n_cofactor")
    if not isinstance(low_k, dict):
        raise AssertionError("smooth low-k fixed-n cofactor receipt missing")
    if (
        low_k.get("condition")
        != (
            "P=2^a*3^b, p=4P+1 prime, r=2, d=P/2, M=k*p+2, "
            "A=M, q=2 if 2|d else 3, 1<=k<=floor((B_p-2q)/(q*p))"
        )
        or low_k.get("candidate") != "L=q*M"
        or low_k.get("seed_count") != 5
        or low_k.get("source_reach_status") != "unproved"
        or low_k.get("selector_status")
        != "verified_edge_conditional_on_reachability"
        or low_k.get("recursive_edge_eligible") is not True
        or low_k.get("proof_boundary") != "smooth23_low_k_fixed_n_cofactor"
        or low_k.get("high_k_residual_status") != "analysis_evidence"
        or low_k.get("high_k_residual_route")
        != ["fixed_n_factor_divisor", "type_ii", "q_adic_capacity"]
        or low_k.get("multiple_M_atlas")
        != {
            "scope": "fixed-n candidates L=M*u with u|d and u>1",
            "minimum_multiplier": "q=spf(d)",
            "complete_condition": "q*M<=B_p",
            "empty_condition": "q*M>B_p implies no bounded multiple-M candidate",
            "remaining_candidates": "L|M*d with M not dividing L",
        }
        or not isinstance(low_k.get("outer_potential_boundary"), dict)
    ):
        raise AssertionError("smooth low-k fixed-n cofactor metadata changed")
    potential_boundary = low_k["outer_potential_boundary"]
    if (
        potential_boundary.get("potential") != "Phi(A)=floor(B_p/A)"
        or potential_boundary.get("hard_boundary")
        != "M>B_p/2 implies Phi(M)=1; no M<L<=B_p can have strict Phi descent"
        or potential_boundary.get("intermediate_boundary")
        != "B_p/3<M<=B_p/2 implies Phi(M)=2; any strict target must satisfy L>B_p/2"
        or potential_boundary.get("q2_consequence")
        != "q=2 and qM>B_p implies the current Phi has no fixed-n E5 target"
        or potential_boundary.get("q3_consequence")
        != "q=3 and qM>B_p splits into a Phi=2 interval and a Phi=1 hard tail"
    ):
        raise AssertionError("smooth outer-potential boundary metadata changed")
    boundary_seeds = potential_boundary.get("seeds")
    if not isinstance(boundary_seeds, list) or len(boundary_seeds) != 5:
        raise AssertionError("smooth outer-potential boundary seed shape changed")
    high_k_no_go = low_k.get("high_k_dual_no_go")
    if not isinstance(high_k_no_go, dict):
        raise AssertionError("smooth high-k dual no-go receipt missing")
    if (
        high_k_no_go.get("condition")
        != (
            "P=2^a*3^b, p=4P+1 prime, r=2, d=P/2, M=k*p+2, A=M, "
            "q*M>B_p"
        )
        or high_k_no_go.get("selector_status") != "verified_arithmetic_no_go"
        or high_k_no_go.get("recursive_edge_eligible") is not False
        or high_k_no_go.get("proof_boundary")
        != "smooth23_high_k_dual_carrier_no_go"
        or high_k_no_go.get("fixed_s_reason") != "L|r*d=P<M=A"
        or high_k_no_go.get("d_reason")
        != "gain>1 gives lcm(M,d)>=q*M>B_p"
        or high_k_no_go.get("r_reason")
        != (
            "gain requires M odd and 2M<=B_p; divisibility would force M|p-d, "
            "contradicting 0<p-d<M"
        )
        or high_k_no_go.get("remaining_route")
        != ["type_ii", "alternate_carrier", "second_rank", "q_adic_capacity"]
    ):
        raise AssertionError("smooth high-k dual no-go metadata changed")
    no_go_seeds = high_k_no_go.get("seeds")
    if not isinstance(no_go_seeds, list) or len(no_go_seeds) != 5:
        raise AssertionError("smooth high-k dual no-go seed shape changed")
    expected_no_go_pairs = {
        (1, 2, 73, 3),
        (3, 1, 97, 2),
        (4, 1, 193, 2),
        (2, 3, 433, 2),
        (2, 4, 1297, 2),
    }
    actual_no_go_pairs: set[tuple[int, int, int, int]] = set()
    for seed in no_go_seeds:
        if not isinstance(seed, dict):
            raise AssertionError("smooth high-k dual no-go seed is not an object")
        exponents = seed.get("exponents")
        if not isinstance(exponents, list) or len(exponents) != 2:
            raise AssertionError("smooth high-k dual no-go exponents changed")
        exponent_two, exponent_three = map(int, exponents)
        product = 2**exponent_two * 3**exponent_three
        prime = int(seed["prime"])
        dual_carrier = int(seed["d"])
        q = int(seed["q"])
        if (
            prime != 4 * product + 1
            or dual_carrier != product // 2
            or q != (2 if dual_carrier % 2 == 0 else 3)
        ):
            raise AssertionError("smooth high-k dual no-go seed arithmetic changed")
        actual_no_go_pairs.add((exponent_two, exponent_three, prime, q))
        B_prime = (prime - 1) ** 2 // 4
        k_global_max = (B_prime - 2) // prime
        high_k_min = (B_prime - 2 * q) // (q * prime) + 1
        expected_range = [high_k_min, k_global_max] if high_k_min <= k_global_max else []
        if seed.get("high_k_range") != expected_range:
            raise AssertionError("smooth high-k dual no-go range changed")
        d_channel = seed.get("d_channel")
        r_channel = seed.get("r_channel")
        if (
            d_channel
            != {
                "carrier": "d=P/2",
                "minimum_gain_multiplier": q,
                "joined_support": "M*(d/gcd(M,d))",
                "tail_bound": "q*M>B_p implies joined support>B_p when gain>1",
            }
            or r_channel
            != {
                "carrier": 2,
                "chart": "R_r=7, K_r=2*(p-d)",
                "gain_multiplier": 2,
                "divisibility_if_M_odd": "M|p-d",
                "impossible_interval": "0<p-d<M",
            }
        ):
            raise AssertionError("smooth high-k dual no-go channel metadata changed")
    if actual_no_go_pairs != expected_no_go_pairs:
        raise AssertionError("smooth high-k dual no-go seed coverage changed")
    low_k_seeds = low_k.get("seeds")
    if not isinstance(low_k_seeds, list) or len(low_k_seeds) != 5:
        raise AssertionError("smooth low-k fixed-n cofactor seed shape changed")
    expected_low_k_pairs = {
        (1, 2, 73, 3, 5),
        (3, 1, 97, 2, 11),
        (4, 1, 193, 2, 23),
        (2, 3, 433, 2, 53),
        (2, 4, 1297, 2, 161),
    }
    actual_low_k_pairs = {
        (
            int(seed["exponents"][0]),
            int(seed["exponents"][1]),
            int(seed["prime"]),
            int(seed["q"]),
            int(seed["k_cofactor_max"]),
        )
        for seed in low_k_seeds
        if isinstance(seed, dict)
    }
    if actual_low_k_pairs != expected_low_k_pairs:
        raise AssertionError("smooth low-k fixed-n cofactor seed coverage changed")
    for seed in low_k_seeds:
        if not isinstance(seed, dict):
            raise AssertionError("smooth low-k fixed-n cofactor seed is not an object")
        rows = seed.get("checked_rows")
        if not isinstance(rows, list) or not rows:
            raise AssertionError("smooth low-k fixed-n cofactor rows missing")
        if int(seed["k_cofactor_max"]) > int(seed["k_global_max"]):
            raise AssertionError("smooth low-k cofactor range exceeds global range")
        for receipt in rows:
            if not isinstance(receipt, dict):
                raise AssertionError("smooth low-k cofactor row is not an object")
            if (
                receipt.get("selector_status") != "verified_edge"
                or receipt.get("recursive_edge_eligible") is not True
                or receipt.get("source_reach_status") != "unproved"
                or receipt.get("e1_e5") != {f"E{i}": True for i in range(1, 6)}
            ):
                raise AssertionError("smooth low-k cofactor crossed status boundary")
            source = receipt.get("source_state")
            successor = receipt.get("successor_state")
            determinant = receipt.get("determinant")
            selected = receipt.get("selected_candidate")
            potential = receipt.get("potential_record")
            if not all(
                isinstance(value, dict)
                for value in (source, successor, determinant, selected, potential)
            ):
                raise AssertionError("smooth low-k cofactor payload incomplete")
            prime = int(source["equation_target"][1])
            M = int(determinant["M"])
            d = int(determinant["d"])
            n = int(determinant["n"])
            S = int(determinant["S"])
            q = int(determinant["q"])
            L = int(selected["L"])
            B_prime = (prime - 1) ** 2 // 4
            if (
                determinant.get("identity") != "p*n=4*M*d+1"
                or prime * n != 4 * M * d + 1
                or d % q
                or L != q * M
                or L != S // (d // q)
                or L <= M
                or L > B_prime
                or 4 * L <= n
                or int(selected["R_L"]) != 4 * L - n
                or int(selected["K_L"]) != L * (prime - S // L)
                or canonical_chart(prime, L)
                != (int(selected["R_L"]), int(selected["K_L"]))
                or int(potential["source"]) != B_prime // M
                or int(potential["successor"]) != B_prime // L
                or potential.get("strict_decrease") is not True
                or potential.get("support_monotone") is not True
            ):
                raise AssertionError("smooth low-k cofactor identity changed")
    for receipt in receipts:
        if not isinstance(receipt, dict):
            raise AssertionError("bounded fixed-s divisor row is not an object")
        if (
            receipt.get("certificate_type")
            != "overflow_fixed_s_bounded_divisor_outer_rank"
            or receipt.get("selector_status") != "verified_edge"
            or receipt.get("recursive_edge_eligible") is not True
            or receipt.get("e1_e5") != {f"E{i}": True for i in range(1, 6)}
        ):
            raise AssertionError("bounded fixed-s divisor crossed the status boundary")
        source = receipt.get("source_state")
        successor = receipt.get("successor_state")
        context = receipt.get("certificate_context")
        potential = receipt.get("potential_record")
        if not all(isinstance(item, dict) for item in (source, successor, context, potential)):
            raise AssertionError("bounded fixed-s divisor payload is incomplete")
        decomposition = context.get("decomposition")
        selected = context.get("selected_candidate")
        if not isinstance(decomposition, dict) or not isinstance(selected, dict):
            raise AssertionError("bounded fixed-s divisor arithmetic payload changed")
        prime = int(receipt["equation_target"]["denominator"])
        A = int(source["absorbed_support"])
        M = int(decomposition["M"])
        r = int(decomposition["r"])
        d = int(decomposition["d"])
        s = int(decomposition["s"])
        L = int(selected["L"])
        target_R = int(successor["R"])
        target_K = int(successor["K"])
        B_prime = (prime - 1) ** 2 // 4
        if (
            not 1 <= r < prime
            or prime * s != 4 * r * d + 1
            or r * d % L
            or not A < L <= B_prime
            or 4 * L <= s
            or target_R != 4 * L - s
            or target_K != L * (prime - (r * d) // L)
            or canonical_chart(prime, L) != (target_R, target_K)
            or B_prime // L >= B_prime // A
            or potential.get("strict_decrease") is not True
            or potential.get("support_monotone") is not (L % A == 0)
            or potential.get("support_reset_paid") is not (L % A != 0)
            or potential.get("outer_rank_reset") is not (L % A != 0)
            or successor.get("absorbed_support") != L
        ):
            raise AssertionError("bounded fixed-s divisor identity changed")


def verify_overflow_same_chart_support_promotion_contract(
    result: dict[str, object],
) -> None:
    branch = result.get("overflow_same_chart_support_promotion")
    if not isinstance(branch, dict):
        raise AssertionError("same-chart support promotion receipt missing")
    if (
        branch.get("fixture_count") != 12
        or branch.get("verified_edge_count") != 11
        or branch.get("rejected_fixture_count") != 1
    ):
        raise AssertionError("same-chart support promotion counts changed")
    receipts = branch.get("verified_receipts")
    rejected = branch.get("rejected_fixtures")
    if not isinstance(receipts, list) or len(receipts) != 11:
        raise AssertionError("same-chart promotion receipt shape changed")
    if not isinstance(rejected, list) or len(rejected) != 1:
        raise AssertionError("same-chart promotion rejection shape changed")
    rejected_names = {
        item.get("fixture_name")
        for item in rejected
        if isinstance(item, dict)
    }
    if rejected_names != {"lcm_cycle_step_0"}:
        raise AssertionError("same-chart promotion domain boundary changed")
    residual = branch.get("high_carrier_residual")
    if (
        not isinstance(residual, dict)
        or residual.get("condition") != "M>B_p"
        or residual.get("necessary_complement_bound") != "n=p or n>=p+4"
    ):
        raise AssertionError("high-carrier residual contract changed")
    rejected_boundary = rejected[0].get("high_carrier_complement_boundary")
    if (
        not isinstance(rejected_boundary, dict)
        or rejected_boundary.get("necessary_condition") != "n=p or n>=p+4"
        or rejected_boundary.get("case") != "n>=p+4"
        or rejected_boundary.get("verified") is not True
    ):
        raise AssertionError("high-carrier fixture boundary changed")
    for receipt in receipts:
        if not isinstance(receipt, dict):
            raise AssertionError("same-chart promotion row is not an object")
        if (
            receipt.get("certificate_type")
            != "overflow_same_chart_support_promotion"
            or receipt.get("phase") != "OVERFLOW_SUPPORT_PROMOTION"
            or receipt.get("state_class") != "overflow"
            or receipt.get("selector_status") != "verified_edge"
            or receipt.get("recursive_edge_eligible") is not True
            or receipt.get("e1_e5") != {f"E{i}": True for i in range(1, 6)}
        ):
            raise AssertionError("same-chart promotion crossed the status boundary")
        source = receipt.get("source_state")
        successor = receipt.get("successor_state")
        context = receipt.get("certificate_context")
        potential = receipt.get("potential_record")
        if (
            not isinstance(source, dict)
            or not isinstance(successor, dict)
            or not isinstance(context, dict)
            or not isinstance(potential, dict)
        ):
            raise AssertionError("same-chart promotion payload is incomplete")
        determinant = context.get("determinant")
        promotion = context.get("support_promotion")
        if not isinstance(determinant, dict) or not isinstance(promotion, dict):
            raise AssertionError("same-chart promotion determinant payload missing")
        prime = int(receipt["equation_target"]["denominator"])
        M = int(determinant["M"])
        d = int(determinant["d"])
        n = int(determinant["pn"]) // prime
        R_M = int(determinant["R_M"])
        K_M = int(determinant["K_M"])
        A = int(source["absorbed_support"])
        B_prime = (prime - 1) ** 2 // 4
        if (
            successor.get("R") != R_M
            or successor.get("K") != K_M
            or source.get("R") != R_M
            or source.get("K") != K_M
            or successor.get("absorbed_support") != M
            or M <= A
            or M % A
            or M // A < 2
            or M > B_prime
            or prime * n != 4 * M * d + 1
            or R_M != 4 * M - n
            or R_M <= prime
            or K_M != M * (prime - d)
            or K_M % M
            or potential.get("B_p") != B_prime
            or potential.get("source_support") != A
            or potential.get("successor_support") != M
            or potential.get("source_value") != B_prime // A
            or potential.get("successor_value") != B_prime // M
            or potential.get("strict_decrease") is not True
            or potential.get("support_monotone") is not True
            or promotion.get("source") != A
            or promotion.get("successor") != M
        ):
            raise AssertionError("same-chart promotion identity changed")


def verify_overflow_a_one_generic_boundary_contract(result: dict[str, object]) -> None:
    receipt = result.get("overflow_a_one_generic_determinant_boundary")
    if not isinstance(receipt, dict):
        raise AssertionError("A=1 generic determinant boundary missing")
    if (
        receipt.get("certificate_type")
        != "overflow_a_one_generic_determinant_boundary"
        or receipt.get("selector_status") != "analysis_evidence"
        or receipt.get("recursive_edge_eligible") is not False
        or receipt.get("e1_e5") != {f"E{i}": False for i in range(1, 6)}
    ):
        raise AssertionError("A=1 generic determinant boundary crossed the status boundary")
    determinant = receipt.get("determinant")
    if not isinstance(determinant, dict):
        raise AssertionError("A=1 generic determinant payload missing")
    p = int(determinant["p"])
    M = int(determinant["M"])
    d = int(determinant["d"])
    n = int(determinant["n"])
    S = int(determinant["S"])
    B_prime = int(determinant["B_p"])
    if (
        (p, M, d, n) != (73, 1297, 29, 2061)
        or S != M * d
        or p * n != 4 * S + 1
        or int(determinant["R_M"]) != 4 * M - n
        or int(determinant["K_M"]) != M * (p - d)
        or int(receipt["source_state"]["R"]) <= p
        or B_prime != (p - 1) ** 2 // 4
        or receipt.get("bounded_divisors") != [1, 29]
        or receipt.get("positive_candidates") != []
    ):
        raise AssertionError("A=1 generic determinant boundary arithmetic changed")
    small = receipt.get("small_carrier_candidate")
    failure = receipt.get("failure_conditions")
    dual_parameters = receipt.get("dual_parameters")
    dual_charts = receipt.get("dual_charts")
    selected_dual = receipt.get("selected_dual_reset")
    if (
        not isinstance(small, dict)
        or not isinstance(failure, dict)
        or not isinstance(dual_parameters, dict)
        or not isinstance(dual_charts, dict)
        or not isinstance(selected_dual, dict)
        or small.get("L") != d
        or small.get("R_L") != 4 * d - n
        or small.get("positive_chart") is not False
        or failure.get("M_less_than_p") is not False
        or failure.get("small_carrier_positive") is not False
        or failure.get("bounded_positive_divisor_exists") is not False
        or dual_parameters != {"r": 56, "s": 89}
        or dual_charts.get("d") != {"t": 29, "R": 27, "K": 493}
        or dual_charts.get("r") != {"t": 56, "R": 135, "K": 2464}
        or selected_dual != {"side": "d", "t": 29, "R": 27, "K": 493}
        or failure.get("dual_reset_positive") is not True
        or failure.get("dual_reset_below_p") is not True
        or failure.get("dual_reset_support_gain") is not True
    ):
        raise AssertionError("A=1 generic determinant boundary failure fields changed")


def verify_overflow_a_one_dual_reset_family_contract(
    result: dict[str, object],
) -> None:
    branch = result.get("overflow_a_one_dual_reset_family")
    if not isinstance(branch, dict):
        raise AssertionError("A=1 dual RESET family missing")
    if (
        branch.get("fixture_count") != 2
        or branch.get("verified_edge_count") != 2
        or branch.get("rejected_fixture_count") != 0
    ):
        raise AssertionError("A=1 dual RESET family counts changed")
    theorem = branch.get("theorem")
    if (
        not isinstance(theorem, dict)
        or theorem.get("condition") != "A=1, pn=4*M*d+1, R_M>p"
        or theorem.get("conclusion")
        != "exists t in {d,r}: t>1, R_t<p, t|K_t, and strict Pi_A descent"
        or theorem.get("proof_boundary")
        != "symmetric_dual_minimum_and_d_or_r_equals_one_split"
    ):
        raise AssertionError("A=1 dual RESET theorem metadata changed")
    receipts = branch.get("verified_receipts")
    if not isinstance(receipts, list) or len(receipts) != 2:
        raise AssertionError("A=1 dual RESET family receipt shape changed")
    fixture_names: set[str] = set()
    for receipt in receipts:
        if not isinstance(receipt, dict):
            raise AssertionError("A=1 dual RESET receipt is not an object")
        if (
            receipt.get("certificate_type")
            != "overflow_a_one_dual_outer_rank_reset"
            or receipt.get("phase") != "RESET"
            or receipt.get("state_class") != "marked_absorb"
            or receipt.get("selector_status") != "verified_edge"
            or receipt.get("recursive_edge_eligible") is not True
            or receipt.get("e1_e5") != {f"E{i}": True for i in range(1, 6)}
            or receipt.get("lift_status") != "proved_identity"
        ):
            raise AssertionError("A=1 dual RESET family crossed the status boundary")
        source = receipt.get("source_state")
        successor = receipt.get("successor_state")
        context = receipt.get("certificate_context")
        potential = receipt.get("potential_record")
        if (
            not isinstance(source, dict)
            or not isinstance(successor, dict)
            or not isinstance(context, dict)
            or not isinstance(potential, dict)
        ):
            raise AssertionError("A=1 dual RESET payload is incomplete")
        fixture_name = context.get("fixture_name")
        if not isinstance(fixture_name, str):
            raise AssertionError("A=1 dual RESET fixture name missing")
        fixture_names.add(fixture_name)
        if fixture_name not in {"root_edge_0", "root_edge_1"}:
            raise AssertionError("unexpected A=1 dual RESET fixture")
        equation = receipt.get("equation_target")
        if not isinstance(equation, dict):
            raise AssertionError("A=1 dual RESET equation target missing")
        prime = int(equation["denominator"])
        source_determinant = context.get("source_determinant")
        dual_parameters = context.get("dual_parameters")
        dual_chart = context.get("dual_chart")
        if (
            not isinstance(source_determinant, dict)
            or not isinstance(dual_parameters, dict)
            or not isinstance(dual_chart, dict)
        ):
            raise AssertionError("A=1 dual RESET determinant payload missing")
        M = int(source_determinant["M"])
        d = int(source_determinant["d"])
        n = int(source_determinant["n"])
        R_M = int(source_determinant["R_M"])
        K_M = int(source_determinant["K_M"])
        r = int(dual_parameters["r"])
        s = int(dual_parameters["s"])
        side = context.get("dual_side")
        t = int(dual_chart["t"])
        target_R = int(dual_chart["R"])
        target_K = int(dual_chart["K"])
        if (
            source.get("absorbed_support") != 1
            or source.get("R") != R_M
            or source.get("K") != K_M
            or successor.get("absorbed_support") != t
            or successor.get("R") != target_R
            or successor.get("K") != target_K
            or prime * n != 4 * M * d + 1
            or R_M != 4 * M - n
            or R_M <= prime
            or not 1 <= r < prime
            or prime * s != 4 * r * d + 1
            or s % 4 != 1
            or side not in {"d", "r"}
            or t <= 1
            or target_R <= 0
            or target_R >= prime
            or target_R % 4 != 3
            or target_K != t * (prime - (r if side == "d" else d))
            or prime * target_R + 1 != 4 * target_K
            or canonical_chart(prime, t) != (target_R, target_K)
            or target_K % t
        ):
            raise AssertionError("A=1 dual RESET determinant identity changed")
        B_prime = (prime - 1) ** 2 // 4
        if (
            t > B_prime
            or potential.get("B_p") != B_prime
            or potential.get("source_support") != 1
            or potential.get("successor_support") != t
            or potential.get("source_value") != B_prime
            or potential.get("successor_value") != B_prime // t
            or potential.get("strict_decrease") is not True
            or potential.get("support_monotone") is not True
        ):
            raise AssertionError("A=1 dual RESET potential changed")
    if fixture_names != {"root_edge_0", "root_edge_1"}:
        raise AssertionError("A=1 dual RESET fixture coverage changed")


def verify_overflow_menu_contract(result: dict[str, object]) -> None:
    menu = result.get("overflow_menu")
    if not isinstance(menu, dict):
        raise AssertionError("overflow menu receipt missing")
    if menu.get("fixture_count") != 12:
        raise AssertionError("focused overflow fixture count changed")
    if menu.get("classification_counts") != {
        "fixed_n_window_nonempty": 3,
        "hard_core_fixed_n_gap_and_dual_obstruction": 9,
    }:
        raise AssertionError("focused overflow classification counts changed")
    if menu.get("support_preserving_channel_count") != 3:
        raise AssertionError("focused dual support-preserving channel count changed")
    direct_type_ii = result.get("overflow_direct_type_ii")
    if not isinstance(direct_type_ii, dict):
        raise AssertionError("direct overflow Type II receipt missing")
    if direct_type_ii.get("fixture_count") != 12:
        raise AssertionError("direct overflow Type II fixture count changed")
    if direct_type_ii.get("verified_terminal_count") != 12:
        raise AssertionError("direct overflow Type II terminal count changed")
    if direct_type_ii.get("d_one_fixture_count") != 1:
        raise AssertionError("direct overflow d=1 fixture count changed")
    if direct_type_ii.get("d_one_direct_terminal_count") != 1:
        raise AssertionError("direct overflow d=1 terminal count changed")
    direct_receipts = direct_type_ii.get("verified_receipts")
    direct_rejected = direct_type_ii.get("rejected_fixtures")
    if not isinstance(direct_receipts, list) or len(direct_receipts) != 12:
        raise AssertionError("direct overflow Type II receipt shape changed")
    if not isinstance(direct_rejected, list) or direct_rejected:
        raise AssertionError("direct overflow Type II rejection shape changed")
    for receipt in direct_receipts:
        if not isinstance(receipt, dict):
            raise AssertionError("direct overflow Type II receipt shape changed")
        if receipt.get("selector_status") != "terminal_leaf":
            raise AssertionError("direct overflow Type II lost terminal status")
        if receipt.get("recursive_edge_eligible") is not False:
            raise AssertionError("direct overflow Type II became recursive")
        if receipt.get("identity", {}).get("verified_exactly") is not True:
            raise AssertionError("direct overflow Type II identity lost exact verification")
    fixed_n_outer = result.get("overflow_fixed_n_outer_rank")
    if not isinstance(fixed_n_outer, dict):
        raise AssertionError("fixed-n overflow-rank receipt missing")
    if fixed_n_outer.get("fixture_count") != 12:
        raise AssertionError("fixed-n outer fixture count changed")
    if fixed_n_outer.get("verified_edge_count") != 9:
        raise AssertionError("fixed-n outer verified edge count changed")
    if fixed_n_outer.get("absorption_target_count") != 3:
        raise AssertionError("fixed-n outer absorption count changed")
    if fixed_n_outer.get("overflow_target_count") != 6:
        raise AssertionError("fixed-n outer overflow count changed")
    if fixed_n_outer.get("rejected_fixture_count") != 3:
        raise AssertionError("fixed-n outer rejected count changed")
    fixed_n_verified = fixed_n_outer.get("verified_receipts")
    fixed_n_rejected = fixed_n_outer.get("rejected_fixtures")
    if not isinstance(fixed_n_verified, list) or len(fixed_n_verified) != 9:
        raise AssertionError("fixed-n outer receipt shape changed")
    if not isinstance(fixed_n_rejected, list) or len(fixed_n_rejected) != 3:
        raise AssertionError("fixed-n outer rejection shape changed")
    for receipt in fixed_n_verified:
        if not isinstance(receipt, dict):
            raise AssertionError("fixed-n outer receipt shape changed")
        if receipt.get("selector_status") != "verified_edge":
            raise AssertionError("fixed-n outer edge lost verified status")
        if receipt.get("e1_e5") != {f"E{i}": True for i in range(1, 6)}:
            raise AssertionError("fixed-n outer edge lacks E1-E5")
        if receipt.get("recursive_edge_eligible") is not True:
            raise AssertionError("fixed-n outer edge became nonrecursive")
        potential = receipt.get("potential_record")
        if not isinstance(potential, dict) or potential.get("strict_decrease") is not True:
            raise AssertionError("fixed-n outer potential did not decrease")
    for receipt in fixed_n_rejected:
        if not isinstance(receipt, dict):
            raise AssertionError("fixed-n outer rejection shape changed")
        if receipt.get("selector_status") != "analysis_evidence":
            raise AssertionError("fixed-n outer rejection crossed status boundary")
        if receipt.get("recursive_edge_eligible") is not False:
            raise AssertionError("fixed-n outer rejection became recursive")
    fixed_s_outer = result.get("overflow_fixed_s_outer_rank")
    if not isinstance(fixed_s_outer, dict):
        raise AssertionError("fixed-s overflow-rank receipt missing")
    if fixed_s_outer.get("fixture_count") != 12:
        raise AssertionError("fixed-s outer fixture count changed")
    if fixed_s_outer.get("verified_edge_count") != 7:
        raise AssertionError("fixed-s outer verified edge count changed")
    if fixed_s_outer.get("absorption_target_count") != 0:
        raise AssertionError("fixed-s outer absorption count changed")
    if fixed_s_outer.get("overflow_target_count") != 7:
        raise AssertionError("fixed-s outer overflow count changed")
    if fixed_s_outer.get("rejected_fixture_count") != 5:
        raise AssertionError("fixed-s outer rejected count changed")
    if fixed_s_outer.get("overlap_with_fixed_n_outer_rank_count") != 5:
        raise AssertionError("fixed-s outer overlap count changed")
    if fixed_s_outer.get("new_after_fixed_n_outer_rank_count") != 2:
        raise AssertionError("fixed-s outer new-edge count changed")
    fixed_s_verified = fixed_s_outer.get("verified_receipts")
    fixed_s_rejected = fixed_s_outer.get("rejected_fixtures")
    if not isinstance(fixed_s_verified, list) or len(fixed_s_verified) != 7:
        raise AssertionError("fixed-s outer receipt shape changed")
    if not isinstance(fixed_s_rejected, list) or len(fixed_s_rejected) != 5:
        raise AssertionError("fixed-s outer rejection shape changed")
    for receipt in fixed_s_verified:
        if not isinstance(receipt, dict):
            raise AssertionError("fixed-s outer receipt shape changed")
        if receipt.get("selector_status") != "verified_edge":
            raise AssertionError("fixed-s outer edge lost verified status")
        if receipt.get("e1_e5") != {f"E{i}": True for i in range(1, 6)}:
            raise AssertionError("fixed-s outer edge lacks E1-E5")
        if receipt.get("recursive_edge_eligible") is not True:
            raise AssertionError("fixed-s outer edge became nonrecursive")
        potential = receipt.get("potential_record")
        if not isinstance(potential, dict) or potential.get("strict_decrease") is not True:
            raise AssertionError("fixed-s outer potential did not decrease")
    for receipt in fixed_s_rejected:
        if not isinstance(receipt, dict):
            raise AssertionError("fixed-s outer rejection shape changed")
        if receipt.get("selector_status") != "analysis_evidence":
            raise AssertionError("fixed-s outer rejection crossed status boundary")
        if receipt.get("recursive_edge_eligible") is not False:
            raise AssertionError("fixed-s outer rejection became recursive")
    hard_core = menu.get("hard_core_receipts")
    if not isinstance(hard_core, list) or len(hard_core) != 9:
        raise AssertionError("focused hard-core receipt count changed")
    for receipt in hard_core:
        if not isinstance(receipt, dict):
            raise AssertionError("hard-core receipt shape changed")
        gap = receipt.get("fixed_n_gap")
        obstruction = receipt.get("dual_obstruction")
        if not isinstance(gap, dict) or not isinstance(obstruction, dict):
            raise AssertionError("hard-core receipt payload changed")
        if gap.get("eligible_t") != [] or not gap.get("empty_verified"):
            raise AssertionError("hard-core row has a fixed-n candidate")
        if obstruction.get("support_preserving_channel_count") != 0:
            raise AssertionError("hard-core row retained an old-support dual edge")
        if receipt.get("selector_status") != "analysis_evidence":
            raise AssertionError("hard-core row crossed the status boundary")
        if receipt.get("recursive_edge_eligible") is not False:
            raise AssertionError("hard-core row became recursive")
    outer_rank = result.get("overflow_outer_rank_reset")
    if not isinstance(outer_rank, dict):
        raise AssertionError("outer-rank RESET receipt missing")
    if outer_rank.get("channel_count") != 24:
        raise AssertionError("focused outer-rank channel count changed")
    if outer_rank.get("verified_edge_count") != 8:
        raise AssertionError("focused outer-rank verified edge count changed")
    if outer_rank.get("rejected_channel_count") != 16:
        raise AssertionError("focused outer-rank rejected count changed")
    verified_outer = outer_rank.get("verified_receipts")
    rejected_outer = outer_rank.get("rejected_channels")
    if not isinstance(verified_outer, list) or len(verified_outer) != 8:
        raise AssertionError("outer-rank verified receipt shape changed")
    if not isinstance(rejected_outer, list) or len(rejected_outer) != 16:
        raise AssertionError("outer-rank rejection receipt shape changed")
    for receipt in verified_outer:
        if not isinstance(receipt, dict):
            raise AssertionError("outer-rank receipt shape changed")
        debt = receipt.get("support_debt")
        if (
            not isinstance(debt, dict)
            or not isinstance(debt.get("value"), int)
            or debt["value"] < 1
            or debt.get("paid_status") != (debt["value"] == 1)
        ):
            raise AssertionError("outer-rank verified debt receipt changed")
        if receipt.get("selector_status") != "verified_edge":
            raise AssertionError("outer-rank edge lost verified status")
        if receipt.get("recursive_edge_eligible") is not True:
            raise AssertionError("outer-rank edge became nonrecursive")
        if receipt.get("e1_e5") != {f"E{i}": True for i in range(1, 6)}:
            raise AssertionError("outer-rank edge lacks E1-E5")
        potential = receipt.get("potential_record")
        if not isinstance(potential, dict) or potential.get("strict_decrease") is not True:
            raise AssertionError("outer-rank potential did not decrease")
    for receipt in rejected_outer:
        if not isinstance(receipt, dict):
            raise AssertionError("outer-rank rejection shape changed")
        debt = receipt.get("support_debt")
        if (
            not isinstance(debt, dict)
            or not isinstance(debt.get("value"), int)
            or debt["value"] < 1
            or debt.get("paid_status") != (debt["value"] == 1)
        ):
            raise AssertionError("outer-rank rejected debt receipt changed")
        if receipt.get("selector_status") != "analysis_evidence":
            raise AssertionError("outer-rank rejection crossed status boundary")
        if receipt.get("recursive_edge_eligible") is not False:
            raise AssertionError("outer-rank rejection became recursive")
    reset = result.get("phase_reset_receipts")
    if not isinstance(reset, dict) or reset.get("cycle_count") != 1:
        raise AssertionError("focused reset-cycle receipt changed")
    reset_receipts = reset.get("receipts")
    if not isinstance(reset_receipts, list) or len(reset_receipts) != 1:
        raise AssertionError("focused reset-cycle receipt shape changed")
    reset_receipt = reset_receipts[0]
    if not isinstance(reset_receipt, dict):
        raise AssertionError("focused reset-cycle payload changed")
    if (
        reset_receipt.get("selector_status") != "candidate_transition"
        or reset_receipt.get("recursive_edge_eligible") is not False
        or reset_receipt.get("e1_e5", {}).get("E5") is not False
        or reset_receipt.get("cycle_witness", {}).get("cycle_nodes") != [132, 330]
    ):
        raise AssertionError("reset-cycle status boundary changed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_results()
    rendered = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.verify:
        verify_bounded_fourier_contract(result)
        verify_bottom_word_lattice_contract(result)
        verify_source_word_joint_capacity_contract(result)
        verify_large_slab_factor_pair_capacity_contract(result)
        verify_high_carrier_complement_contract(result)
        verify_support_debt_phase_contract(result)
        verify_universal_source_anchor_contract(result)
        verify_d_one_g_rechart_contract(result)
        verify_overflow_fixed_n_bounded_divisor_contract(result)
        verify_overflow_fixed_s_bounded_divisor_contract(result)
        verify_overflow_same_chart_support_promotion_contract(result)
        verify_overflow_a_one_generic_boundary_contract(result)
        verify_overflow_a_one_dual_reset_family_contract(result)
        verify_overflow_menu_contract(result)
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("stored selector result does not match regenerated output")
        print("verified", args.output)
        return
    args.output.write_text(rendered, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
