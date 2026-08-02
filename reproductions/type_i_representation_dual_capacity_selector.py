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
from math import lcm
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
    "overflow_fixed_n_outer_rank_reset",
    "overflow_outer_rank_reset",
    "overflow_hard_core_gap_obstruction",
    "overflow_phase_reset_cycle_boundary",
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
                    "certificate_context": {
                        "source": OVERFLOW_INPUT.name,
                        "provenance": "symmetric_dual_with_joined_support",
                        "fixture_name": name,
                        "dual_side": side,
                        "dual_carrier": dual_carrier,
                        "dual_chart": {"R": dual_R, "K": dual_K},
                        "joined_support": joined_support,
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
    overflow_menu = overflow_menu_receipts(overflow, qadic)
    fixed_n_outer_rank = overflow_fixed_n_outer_rank(overflow)
    outer_rank_reset = overflow_outer_rank_reset(overflow)
    reset_boundary = phase_reset_boundary(overflow)
    return {
        "schema_version": 1,
        "arithmetic": "Typed dispatch for the representation-dual-capacity selector.",
        "selector_order": SELECTOR_ORDER,
        "status_lattice": STATUS_LATTICE,
        "states": states,
        "verified_edges": [verified_edge],
        "overflow_fixed_n_outer_rank": fixed_n_outer_rank,
        "overflow_menu": overflow_menu,
        "overflow_outer_rank_reset": outer_rank_reset,
        "phase_reset_receipts": reset_boundary,
        "capacity_receipts": [capacity],
        "invariants": {
            "analysis_evidence_never_recursive": True,
            "verified_edge_requires_E1_E5": True,
            "terminal_leaf_requires_direct_certificate": True,
            "overflow_phase_requires_explicit_cross_state_mapping": True,
            "hard_core_negative_receipt_never_recursive": True,
            "fixed_n_overflow_rank_requires_positive_chart": True,
            "outer_rank_reset_requires_joined_support": True,
            "reset_cycle_boundary_requires_E5": True,
        },
        "source_sha256": source_hashes(),
        "scope_note": (
            "This receipt unifies state-local representation, dual, and capacity evidence. "
            "It contains fixed-n identity-lift edges and focused joined-support RESET edges, "
            "but does not prove universal branch existence or "
            "well-founded descent for all overflow states."
        ),
    }


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
        verify_overflow_menu_contract(result)
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("stored selector result does not match regenerated output")
        print("verified", args.output)
        return
    args.output.write_text(rendered, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
