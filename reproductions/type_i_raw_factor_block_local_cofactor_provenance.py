#!/usr/bin/env python3
"""Verify local raw factor-block to candidate-cofactor receipts.

This is a narrow provenance verifier.  It does not create a slot allocation,
run a terminal scan, or register a selector edge.
"""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_c3_adaptive_core19_q137_first_entry_family as q137
import type_i_c3_adaptive_core19_v5_dual_leaf_f19_control as v5
import type_i_c3_affine_prime_even_tail_root_entry as raw
import type_i_c3_factor_block_even_tail_root_entry as factor_blocks
import type_i_high_r_chart_two_anchor as shared


D_STAR = 6_303
M_STAR = 4 * D_STAR
U_BASE = 194_563
Q137_A = 573
V5_A_VALUES = (1, 3, 11, 33, 191, 573, 2_101, 6_303)
V5_FIRST_FACTORS = (2, 5, 5_623, 92_660_501)
V5_PHASE_11_CANDIDATES = (19, 1_014_049, 3_307_571, 1_334_507_617)


def prime_word(value: int) -> list[int]:
    """Expand a positive factor block into individually replayed prime labels."""
    word: list[int] = []
    for prime, exponent in shared.factorization(value):
        word.extend([prime] * exponent)
    return word


def is_squarefree(value: int) -> bool:
    """Check squarefreeness from the local deterministic factorization helper."""
    return all(exponent == 1 for _prime, exponent in shared.factorization(value))


def candidate_record(*, prime: int, A: int, H: int) -> dict[str, int]:
    """Check the integer candidate data attached to one raw endpoint."""
    N = prime + 4 * D_STAR * A
    if not (
        A in V5_A_VALUES
        and D_STAR % A == 0
        and is_squarefree(D_STAR // A)
        and 4 * A * D_STAR < prime
        and N % H == 0
        and gcd(H, M_STAR) == 1
    ):
        raise AssertionError("candidate cofactor receipt changed")
    return {"D": D_STAR, "A": A, "N": N, "H": H}


def replay_factor_orbit(
    *,
    modulus: int,
    carrier: int,
    first_label: int,
    endpoint: int,
    block: int,
    name: str,
) -> dict[str, object]:
    """Replay the one-first-label factor-orbit lemma at one concrete state."""
    if not (
        shared.is_prime(first_label)
        and (modulus - 1) % first_label == 0
        and endpoint > 0
        and block > 0
    ):
        raise AssertionError(f"{name}: invalid first-label factor-orbit data")
    b = (modulus - 1) // first_label
    S = modulus - b
    if not (
        S == endpoint * block
        and shared.valuation(modulus - 1, first_label) > shared.valuation(carrier, first_label)
        and gcd(S, modulus) == gcd(b, modulus) == 1
    ):
        raise AssertionError(f"{name}: first raw edge lost its local hypotheses")

    first = raw.ordered_raw_step(
        modulus=modulus,
        K=carrier,
        source=(1, modulus - 1, 1),
        selected_coordinate_index=1,
        q=first_label,
        expected_destination=(b, S, 1),
        name=f"{name}_first",
    )
    word = prime_word(block)
    _, rows = factor_blocks.replay_block(
        modulus=modulus,
        K=carrier,
        source=(b, S, 1),
        selected_coordinate_index=1,
        word=word,
        endpoint=(endpoint, modulus - endpoint, 1),
        name=f"{name}_block",
    )
    if not (
        all(
            row["strict_capacity"]
            and row["unit_condition"]
            and row["gcd_reduction"] == 1
            for row in [first, *rows]
        )
        and all(shared.valuation(endpoint, prime) >= shared.valuation(carrier, prime) for prime in word)
    ):
        raise AssertionError(f"{name}: factor block lost actual primitive status")
    return {
        "first_label": first_label,
        "b": b,
        "S": S,
        "endpoint_H": endpoint,
        "block_L": block,
        "word": [first_label, *word],
        "rows": [first, *rows],
        "primitive": True,
    }


def verify_v5_first_edge_catalog() -> dict[str, object]:
    """Classify every one-first-edge intersection with the fixed D=6303 menu."""
    if not (
        v5.R - 1 == 2 * 5 * 5_623 * 92_660_501
        and all(shared.is_prime(value) for value in V5_FIRST_FACTORS)
        and v5.K
        == 2 * 19**2 * 193 * 5_351 * 66_383 * 31_641_497_801
    ):
        raise AssertionError("v=5 first-label factorization changed")
    strict = {
        label: shared.valuation(v5.R - 1, label) > shared.valuation(v5.K, label)
        for label in V5_FIRST_FACTORS
    }
    usable = tuple(label for label in V5_FIRST_FACTORS if strict[label])
    if not (strict == {2: False, 5: True, 5_623: True, 92_660_501: True} and usable == V5_FIRST_FACTORS[1:]):
        raise AssertionError("v=5 usable first-label menu changed")

    S_values = {label: v5.R - (v5.R - 1) // label for label in usable}
    expected_S = {
        5: 4_168_239_976_985,
        5_623: 5_209_373_366_221,
        92_660_501: 5_210_299_915_001,
    }
    if not (
        S_values == expected_S
        and S_values[5] == 5 * 7 * 119_092_570_771
        and S_values[5_623] == 41 * 101 * 127 * 1_423 * 6_961
        and S_values[92_660_501] == 1_213 * 7_603 * 564_959
        and all(
            shared.is_prime(prime)
            for prime in (5, 7, 119_092_570_771, 41, 101, 127, 1_423, 6_961, 1_213, 7_603, 564_959)
        )
    ):
        raise AssertionError("v=5 first-edge cofactor factorizations changed")

    intersections = {
        (label, A): gcd(S, v5.P + 4 * D_STAR * A)
        for label, S in S_values.items()
        for A in V5_A_VALUES
    }
    nontrivial = {
        pair: value for pair, value in intersections.items() if value > 1
    }
    if nontrivial != {(5, 11): 7}:
        raise AssertionError("v=5 first-edge candidate intersections changed")

    N_573 = v5.P + 4 * D_STAR * 573
    phase_candidate_gcds = {
        (label, H): gcd(S, H)
        for label, S in S_values.items()
        for H in V5_PHASE_11_CANDIDATES
    }
    if not (
        N_573 == 1_202_391_362_917
        and N_573 == 17 * 19**3 * 53**2 * 3_671
        and all(N_573 % H == 0 for H in V5_PHASE_11_CANDIDATES)
        and all(value == 1 for value in phase_candidate_gcds.values())
        and [gcd(endpoint, N_573) for endpoint in (v5.P - 3, 19, 38)] == [19, 19, 19]
    ):
        raise AssertionError("v=5 A=573 local-provenance boundary changed")
    return {
        "strict_first_labels": strict,
        "usable_first_labels": list(usable),
        "S_values": S_values,
        "all_first_edge_candidate_intersections": {
            f"{label}:{A}": value for (label, A), value in intersections.items()
        },
        "nontrivial_intersections": {"5:11": 7},
        "A573_phase11_candidate_gcds": {
            f"{label}:{H}": value for (label, H), value in phase_candidate_gcds.items()
        },
        "occurrence_to_A573_resource_incidence": {
            "C0": 19,
            "C1": 19,
            "C38": 19,
        },
    }


def verify_v5_positive_control() -> dict[str, object]:
    """Replay the unique nontrivial v=5 first-edge/candidate incidence."""
    H = 7
    orbit = replay_factor_orbit(
        modulus=v5.R,
        carrier=v5.K,
        first_label=5,
        endpoint=H,
        block=595_462_853_855,
        name="v5_A11_H7",
    )
    candidate = candidate_record(prime=v5.P, A=11, H=H)
    if not (
        orbit["word"] == [5, 5, 119_092_570_771]
        and orbit["rows"][1]["destination"] == [833_647_995_397, 4_376_651_975_834, 1]
        and orbit["rows"][-1]["destination"] == [7, v5.R - 7, 1]
        and candidate["N"] == 1_202_377_193_773
    ):
        raise AssertionError("v=5 H=7 local receipt changed")
    return {
        "raw_orbit": orbit,
        "candidate": candidate,
        "scope": (
            "A local H=7 incidence only; v=5 remains terminal-preempted and H is "
            "not a target-odd factor."
        ),
    }


def verify_q137_family_boundary() -> dict[str, object]:
    """Prove the exact raw-Q versus candidate-N CRT separation."""
    raw_gate = q137.verify_capacity_subray()
    N_base = q137.P0 + 4 * D_STAR * Q137_A
    if not (
        raw_gate["stable_subray"] == {"v": "12369*w", "p": [q137.P0, q137.P_STEP]}
        and N_base == 14_446_669
        and q137.Q0 == 43
        and q137.Q_STEP == 174_947_136
        and q137.Q0 % 19 == 5
        and q137.Q_STEP % 19 == 0
        and N_base % (19**2) == 171
        and q137.P_STEP % (19**2) == 0
        and gcd(q137.Q_STEP, U_BASE) == gcd(q137.P_STEP, U_BASE) == 1
        and N_base % 19 == q137.P_STEP % 19 == 0
        and gcd(19, M_STAR) == 1
        and D_STAR % Q137_A == 0
        and D_STAR // Q137_A == 11
        and is_squarefree(D_STAR // Q137_A)
        and 4 * D_STAR * Q137_A < q137.P0 + q137.P_STEP
    ):
        raise AssertionError("q=137 family alignment data changed")
    q_residue = (-q137.Q0 * pow(q137.Q_STEP, -1, U_BASE)) % U_BASE
    n_residue = (-N_base * pow(q137.P_STEP, -1, U_BASE)) % U_BASE
    if not (
        (q_residue, n_residue) == (7_666, 92_963)
        and q_residue != n_residue
        and (q137.Q0 + q137.Q_STEP * q_residue) % U_BASE == 0
        and (N_base + q137.P_STEP * n_residue) % U_BASE == 0
        and (N_base + q137.P_STEP * q_residue) % U_BASE == 53_329
        and (q137.Q0 + q137.Q_STEP * n_residue) % U_BASE == 129_594
    ):
        raise AssertionError("q=137 U-base CRT classes changed")
    return {
        "N_573": [N_base, q137.P_STEP],
        "Q": [q137.Q0, q137.Q_STEP],
        "U": U_BASE,
        "U_divides_Q_w_residue": q_residue,
        "U_divides_N_w_residue": n_residue,
        "H19_family_incidence": {
            "raw_endpoint": 19,
            "candidate_A": Q137_A,
            "N_573_divisible_by_19_for_every_parameter": True,
        },
        "v19_Q": 0,
        "v19_N": 1,
        "conclusion": (
            "The same one-edge factor orbit cannot align U with the A=573 candidate "
            "record; 19^3*U is excluded already by the one-layer 19 budgets."
        ),
    }


def verify_q137_positive_control() -> dict[str, object]:
    """Replay an actual q=137 endpoint H=19*U at the raw-Q CRT class."""
    w = 7_666
    prime = q137.P0 + q137.P_STEP * w
    R = q137.R0 + q137.R_STEP * w
    h = q137.H0 + q137.H_STEP * w
    carrier = (26 * h + 1) * (prime - 3)
    H = 19 * U_BASE
    Q = q137.Q0 + q137.Q_STEP * w
    L = Q // U_BASE
    N = prime + 4 * D_STAR * Q137_A
    if not (
        shared.is_prime(prime)
        and prime == 5_923_642_144_081
        and R == 25_669_115_957_671
        and Q == 1_341_144_744_619 == 53 * 113 * 3_671 * 61_001
        and H == 3_696_697
        and L == 6_893_113 == 113 * 61_001
        and R - (R - 1) // q137.FIRST_LABEL == H * L
        and gcd(Q, carrier * R) == 1
        and N == 5_923_656_590_557
        and N % H == 2_777_211
    ):
        raise AssertionError("q=137 positive raw-H control data changed")
    orbit = replay_factor_orbit(
        modulus=R,
        carrier=carrier,
        first_label=q137.FIRST_LABEL,
        endpoint=H,
        block=L,
        name="q137_H19U",
    )
    if not (
        orbit["word"] == [137, 113, 61_001]
        and orbit["rows"][-1]["destination"] == [H, R - H, 1]
    ):
        raise AssertionError("q=137 H=19U raw orbit changed")
    return {
        "w": w,
        "p": prime,
        "raw_orbit": orbit,
        "candidate_N_573": N,
        "candidate_remainder_mod_H": N % H,
        "scope": "Actual raw endpoint provenance, but no same-parameter candidate-factor incidence.",
    }


def build_result() -> dict[str, object]:
    """Build local receipts and exact nonalignment boundaries only."""
    return {
        "certificate_type": "raw_factor_block_local_cofactor_provenance_v1",
        "scope": (
            "State-local raw endpoint plus candidate-divisibility receipts; no target "
            "factor, demand-to-slot injection, capacity conclusion, or selector edge."
        ),
        "v5_first_edge_catalog": verify_v5_first_edge_catalog(),
        "v5_unique_positive_control": verify_v5_positive_control(),
        "q137_family_boundary": verify_q137_family_boundary(),
        "q137_actual_raw_H_control": verify_q137_positive_control(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified local raw-to-cofactor factor-orbit receipts and boundaries")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
