#!/usr/bin/env python3
"""Verify the v=5 character/provenance boundary for candidate-fiber lifts."""

from __future__ import annotations

import argparse
import json

import type_i_c3_adaptive_core19_v5_c38_q19_phase_leaf as c38
import type_i_c3_adaptive_core19_v5_d6303_fiber_catalog as catalog
import type_i_c3_adaptive_core19_v5_dual_leaf_f19_control as v5
import type_i_c3_adaptive_core19_v5_q19_phase_compatible_fiber as candidate


Q = 19
CONDUCTOR = 191
ZETA = 150
H_BASE = 194_563
H2_NEUTRAL = H_BASE * Q**2
RAW_MARKS = {
    "C0": (candidate.MU0, 16),
    "C1": (candidate.MU1, 8),
    "C38": (c38.MU2, 11),
}


def record_rows(phase: int) -> list[tuple[int, int, int, int, int]]:
    """Enumerate tagged candidate cofactors in one exact character fiber."""
    rows = []
    for a, factors in catalog.FIBERS.items():
        N = v5.P + 4 * catalog.D * a
        nu_N = catalog.valuation(N, Q)
        for H in catalog.divisors(factors):
            if catalog.phase_exponent(H) == phase:
                nu_H = catalog.valuation(H, Q)
                rows.append((a, H, nu_H, nu_N - nu_H, nu_N))
    return rows


def verify_raw_phase_fibers() -> dict[str, object]:
    """Show phase equality is a relation, not a height or label certificate."""
    catalog.verify_complete_catalog()
    expected = {
        16: [
            (1, 1_437_973, 0, 0, 0),
            (573, 194_563, 0, 3, 3),
            (2_101, 13, 0, 0, 0),
        ],
        8: [
            (1, 11_237_167_679, 0, 0, 0),
            (573, 2_809, 0, 3, 3),
            (573, 3_696_697, 1, 2, 3),
        ],
        11: [
            (3, 19, 1, 0, 1),
            (11, 70_715_591, 0, 0, 0),
            (11, 495_009_137, 0, 0, 0),
            (11, 3_465_063_959, 0, 0, 0),
            (573, 19, 1, 2, 3),
            (573, 1_014_049, 2, 1, 3),
            (573, 3_307_571, 0, 3, 3),
            (573, 1_334_507_617, 3, 0, 3),
        ],
    }
    actual = {phase: record_rows(phase) for phase in expected}
    if not (
        actual == expected
        and all(
            pow(mark, 10, CONDUCTOR) == pow(ZETA, phase, CONDUCTOR)
            for mark, phase in RAW_MARKS.values()
        )
    ):
        raise AssertionError("v=5 raw phase candidate fibers changed")

    summary = {}
    for leaf, (_mark, phase) in RAW_MARKS.items():
        rows = actual[phase]
        summary[leaf] = {
            "phase": phase,
            "candidate_count": len(rows),
            "cofactor_q_heights": sorted({row[2] for row in rows}),
            "record_q_heights": sorted({row[4] for row in rows}),
        }
    if summary != {
        "C0": {
            "phase": 16,
            "candidate_count": 3,
            "cofactor_q_heights": [0],
            "record_q_heights": [0, 3],
        },
        "C1": {
            "phase": 8,
            "candidate_count": 3,
            "cofactor_q_heights": [0, 1],
            "record_q_heights": [0, 3],
        },
        "C38": {
            "phase": 11,
            "candidate_count": 8,
            "cofactor_q_heights": [0, 1, 2, 3],
            "record_q_heights": [0, 1, 3],
        },
    }:
        raise AssertionError("v=5 phase information boundary changed")
    return {"phase_rows": actual, "raw_phase_summary": summary}


def verify_height_disguise() -> dict[str, object]:
    """Give a same-record four-height witness with one identical phase."""
    U_values = (3_307_571, 1, 2_809, H_BASE)
    H_values = [Q**index * value for index, value in enumerate(U_values)]
    phases = [catalog.phase_exponent(value) for value in H_values]
    U_phases = [catalog.phase_exponent(value) for value in U_values]
    if not (
        H_values == [3_307_571, 19, 1_014_049, 1_334_507_617]
        and phases == [11, 11, 11, 11]
        and U_phases == [11, 0, 8, 16]
        and all(
            U_phases[index] == (11 * (1 - index)) % 19
            for index in range(4)
        )
        and all(
            catalog.valuation(value, Q) == index
            for index, value in enumerate(H_values)
        )
        and all(
            (v5.P + 4 * catalog.D * 573) % value == 0
            for value in H_values
        )
    ):
        raise AssertionError("v=5 same-record q-height disguise changed")
    return {
        "A": 573,
        "same_phase": 11,
        "cofactor_height_witnesses": [
            {"H": value, "q_height": index, "q_free_base": U_values[index]}
            for index, value in enumerate(H_values)
        ],
        "conclusion": "phase alone cannot recover the cofactor q-height, even after A=573 is known",
    }


def verify_conditional_chain_reconstruction() -> dict[str, object]:
    """Record the positive reconstruction available after q-free provenance."""
    chain = [H_BASE * Q**index for index in range(4)]
    phase_to_index = {catalog.phase_exponent(value): index for index, value in enumerate(chain)}
    selected = {
        leaf: phase_to_index[phase] for leaf, (_mark, phase) in RAW_MARKS.items()
    }
    if not (
        chain == [194_563, 3_696_697, H2_NEUTRAL, 1_334_507_617]
        and [catalog.phase_exponent(value) for value in chain] == [16, 8, 0, 11]
        and catalog.chi(Q) == pow(ZETA, 11, CONDUCTOR)
        and len({catalog.phase_exponent(value) for value in chain}) == 4
        and selected == {"C0": 0, "C1": 1, "C38": 3}
    ):
        raise AssertionError("v=5 conditional q-free chain reconstruction changed")
    return {
        "hypothesis": "A=573 and a common q-free base H_base=194563 are independently proven",
        "chain": chain,
        "forced_indices": selected,
        "scope": (
            "A conditional cofactor reconstruction only; the chain remains nested in "
            "one N_573 and does not allocate requests or physical slots."
        ),
    }


def verify_conductor_target_phase_barrier() -> dict[str, object]:
    """Separate direct target identification from future phase-corrected maps."""
    target_phase = pow(-1, 10, CONDUCTOR)
    H2_factor = (H2_NEUTRAL + 1) // 4
    if not (
        catalog.D % CONDUCTOR == 0
        and target_phase == 1
        and all(pow(mark, 10, CONDUCTOR) != target_phase for mark, _phase in RAW_MARKS.values())
        and H2_NEUTRAL == 70_237_243
        and catalog.phase_exponent(H2_NEUTRAL) == 0
        and H2_NEUTRAL % CONDUCTOR == 49
        and H2_factor == 17_559_311 == 7 * 11 * 457 * 499
        and H2_factor % CONDUCTOR != 0
    ):
        raise AssertionError("conductor-191 target phase barrier changed")
    return {
        "general_rule": (
            "If 191 divides D and h is congruent to -1 modulo 4D, then "
            "chi(h)=h^10=1 modulo 191."
        ),
        "raw_nonzero_phases": {leaf: phase for leaf, (_mark, phase) in RAW_MARKS.items()},
        "neutral_chain_control": {
            "H2": H2_NEUTRAL,
            "chi": target_phase,
            "H2_mod_191": H2_NEUTRAL % CONDUCTOR,
            "not_target_for_any_D_divisible_by_191": True,
        },
        "scope": (
            "It blocks only an eta-preserving direct raw-mark-to-target identification; "
            "a phase correction, a nonidentity mark map, or a different adapter remains open."
        ),
    }


def build_result() -> dict[str, object]:
    """Build the finite provenance boundary and its conditional reconstruction."""
    return {
        "certificate_type": "v5_phase_provenance_boundary_v1",
        "status": "analysis_evidence_only",
        "raw_phase_fibers": verify_raw_phase_fibers(),
        "same_record_height_disguise": verify_height_disguise(),
        "conditional_chain_reconstruction": verify_conditional_chain_reconstruction(),
        "conductor_target_phase_barrier": verify_conductor_target_phase_barrier(),
        "minimum_missing_provenance": [
            "raw occurrence and entry digest with signed-tail receipt",
            "candidate fiber label (D_star, A, b, N_A)",
            "factor receipt H divides N_A or an equivalent q-free base plus exponent",
            "shared-q source labels, layer ledger, and residual budget",
            "demand_to_slot injection with nonreuse/subset-divisibility receipts",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified v=5 phase provenance boundary")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
