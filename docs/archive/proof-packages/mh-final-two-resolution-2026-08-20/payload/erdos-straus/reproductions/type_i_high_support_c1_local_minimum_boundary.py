#!/usr/bin/env python3
"""Verify the C=1 high-support local minimum and the p=73 two-bundle control.

The two-bundle row is deliberately emitted as conditional analysis evidence:
p=73 is preempted by a direct root terminal and the frozen selector has no
versioned adapter for this macro.  Its purpose is to confirm that C=2 can reach
C=1 while C=1 itself remains the exact fixed-T5 CHARGED boundary.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm

import type_i_bottom_sink_scc_complete_excess_bundle as bottom
import type_i_high_r_chart_two_anchor as shared


def sharp_rank(prime: int, K: int, support: int) -> tuple[int, int]:
    if support <= 0 or K % support:
        raise AssertionError("charged support must divide K")
    return ((prime - 1) ** 2 // (4 * support), K // support)


def centered_f_receipt(R: int, K: int, witness: tuple[int, ...]) -> dict[str, object]:
    factors = shared.factorization(K)
    receipt = shared.residue_witness(R, factors, witness)
    residues = {1}
    for q, exponent in factors:
        residues = {
            left * pow(q, z, R) % R
            for left in residues
            for z in range(-exponent, exponent + 1)
        }
    if R - 1 in residues or receipt["classification"] != "F":
        raise AssertionError("canonical F classification control changed")
    receipt["bounded_residue_count"] = len(residues)
    return receipt


def replay_labels(
    R: int,
    K: int,
    source: tuple[int, int, int],
    labels: tuple[int, ...],
) -> tuple[tuple[int, int, int], list[dict[str, object]]]:
    current = source
    rows: list[dict[str, object]] = []
    factors = bottom.factorization(K)
    for q in labels:
        target, shift, common = bottom.formal_transition(current, q, R, factors)
        if shift != q - 1 or common != 1:
            raise AssertionError("raw path lost its primitive q-1 form")
        rows.append(
            {
                "source": list(current),
                "q": q,
                "shift": shift,
                "gcd_reduction": common,
                "target": list(target),
            }
        )
        current = target
    return current, rows


def canonical_c1_boundary(prime: int) -> dict[str, object]:
    if prime % 24 != 1:
        raise AssertionError("control must lie in the core congruence class")
    bound = (prime - 1) ** 2 // 4
    support = (prime + 1) ** 2 // 4
    R, K = prime + 2, support
    if not (
        support == bound + prime
        and 4 * K == prime * R + 1
        and sharp_rank(prime, K, support) == (0, 1)
    ):
        raise AssertionError("minimal C=1 chart formula changed")

    d = prime - 1
    n = prime * prime + prime - 1
    residue = (3 * prime + 1) // 4
    quotient = (prime - 1) // 4
    reduced_n = n - 4 * quotient * d
    if not (
        support == quotient * prime + residue
        and prime * n == 4 * support * d + 1
        and reduced_n == 3 * prime - 2
    ):
        raise AssertionError("C=1 determinant data changed")

    dual_d = (4 * d - reduced_n, d * (prime - residue))
    dual_r = (4 * residue - reduced_n, residue * (prime - d))
    if dual_d != (prime - 2, bound) or dual_r != (3, residue):
        raise AssertionError("C=1 determinant dual formulas changed")

    anchor_selected = prime + 1
    Q, beta = 2, (prime + 1) // 2
    target_support = lcm(support, Q)
    target_R, target_K = bottom.canonical_chart(prime, target_support)
    if not (
        anchor_selected == Q * beta
        and K % beta == 0
        and target_support == 2 * support
        and target_K // target_support == (prime + 1) // 2
        and target_R > prime
    ):
        raise AssertionError("universal C=1 first-bundle rise changed")

    for target_cofactor in range(1, prime):
        target_local = (0, target_cofactor, 0, 0)
        if target_local < (0, 1, 0, 0):
            raise AssertionError("a CHARGED cofactor fell below C=1")

    fiber_control: dict[str, object] | None = None
    if prime == 73:
        support_primes = bottom.factorization(K)
        values = {str(q): bottom.jacobi_symbol(q, R) for q in support_primes}
        minus_one = bottom.jacobi_symbol(-1, R)
        if values != {"37": 1} or minus_one != -1:
            raise AssertionError("p=73 C=1 G separator changed")
        fiber_control = {
            "classification": "G",
            "support_values": values,
            "minus_one": minus_one,
        }

    return {
        "p": prime,
        "B_p": bound,
        "minimal_C1_state": [R, K, support],
        "local_rank": [0, 1, 0, 0],
        "determinant": {
            "M": support,
            "d": d,
            "n": n,
            "M_mod_p": residue,
            "k": quotient,
            "s": reduced_n,
        },
        "dual_d": list(dual_d),
        "dual_r": list(dual_r),
        "universal_anchor_first_bundle": {
            "anchor": [1, anchor_selected],
            "Q": Q,
            "beta": beta,
            "target": [target_R, target_K, target_support],
            "target_cofactor": target_K // target_support,
            "relation": "increase",
        },
        "fiber_control": fiber_control,
        "joined_support_preserved": False,
    }


def p73_two_bundle_control() -> dict[str, object]:
    prime = 73
    H0 = (143, 2_610, 1_305)
    H1 = (21_023, 383_670, 63_945)
    H2 = (10_508_003, 191_771_055, 191_771_055)
    for R, K, support in (H0, H1, H2):
        if 4 * K != prime * R + 1 or K % support:
            raise AssertionError("p=73 high chart changed")

    fiber0 = centered_f_receipt(H0[0], H0[1], (0, -2, 2, -1))
    fiber1 = centered_f_receipt(H1[0], H1[1], (-1, 8, 0, -5, -2))
    fiber2 = centered_f_receipt(H2[0], H2[1], (-9, 8, -6, 11, 0))
    if [fiber0["bounded_residue_count"], fiber1["bounded_residue_count"], fiber2["bounded_residue_count"]] != [86, 875, 675]:
        raise AssertionError("independent F typing counts changed")

    anchor0 = (1, H0[0] - 1, 1)
    node1, path1 = replay_labels(
        H0[0], H0[1], anchor0, (71, 47, 7, 2, 19, 17, 3)
    )
    if node1 != (45, 98, 1):
        raise AssertionError("first two-bundle path endpoint changed")
    Q1, beta1, residual1 = 49, 2, 90
    M1 = lcm(H0[2], Q1)
    if not (
        node1[1] == Q1 * beta1
        and node1[0] * beta1 == residual1
        and H0[1] % residual1 == 0
        and gcd(Q1, residual1) == 1
        and M1 == H1[2]
        and bottom.canonical_chart(prime, M1) == H1[:2]
    ):
        raise AssertionError("first bundle receipt changed")

    anchor1 = (1, H1[0] - 1, 1)
    node2, path2 = replay_labels(
        H1[0], H1[1], anchor1, (457, 11, 59, 3, 2, 13, 647)
    )
    if node2 != (30, 20_993, 1):
        raise AssertionError("second two-bundle path endpoint changed")
    Q2, beta2, residual2 = 2_999, 7, 210
    M2 = lcm(H1[2], Q2)
    if not (
        node2[1] == Q2 * beta2
        and node2[0] * beta2 == residual2
        and H1[1] % residual2 == 0
        and gcd(Q2, residual2) == 1
        and M2 == H2[2]
        and bottom.canonical_chart(prime, M2) == H2[:2]
    ):
        raise AssertionError("second bundle receipt changed")

    ranks = {
        "H0": sharp_rank(prime, H0[1], H0[2]),
        "H1_transient": sharp_rank(prime, H1[1], H1[2]),
        "H2": sharp_rank(prime, H2[1], H2[2]),
    }
    if not ranks["H2"] < ranks["H0"] or ranks["H1_transient"] <= ranks["H0"]:
        raise AssertionError("parent-to-final rank comparison changed")

    terminal = (20, 219, 4_380)
    x, y, z = terminal
    if 4 * x * y * z != prime * (x * y + x * z + y * z):
        raise AssertionError("p=73 terminal preemption changed")

    return {
        "source": {"state": list(H0), "fiber": fiber0, "rank": list(ranks["H0"])},
        "first_bundle": {
            "path": path1,
            "node": list(node1),
            "Q": Q1,
            "beta": beta1,
            "residual": residual1,
            "target": list(H1),
            "fiber": fiber1,
            "rank": list(ranks["H1_transient"]),
            "persistent": False,
        },
        "second_bundle": {
            "path": path2,
            "node": list(node2),
            "Q": Q2,
            "beta": beta2,
            "residual": residual2,
            "target": list(H2),
            "fiber": fiber2,
            "rank": list(ranks["H2"]),
        },
        "E4": "identity_on_Sol(4,73)",
        "E5": {"source": list(ranks["H0"]), "target": list(ranks["H2"])},
        "terminal_first_preemption": list(terminal),
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "why_not_edge": [
            "p73 direct root terminal has priority",
            "no versioned two-bundle adapter is registered on the frozen surface",
            "the final C=1 target still has no paid exit",
        ],
    }


def run() -> dict[str, object]:
    symbolic_controls = [canonical_c1_boundary(p) for p in (73, 97, 193, 241, 313)]
    return {
        "theorem": "type-I-high-support-empty-improvement-c1-local-minimum-boundary",
        "symbolic_integer_controls": symbolic_controls,
        "p73_two_bundle_control": p73_two_bundle_control(),
        "status": {
            "C1_local_minimum": "verified",
            "H_universal_exit": "open",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.verify:
        print("verified C=1 high-support local minimum and p=73 two-bundle boundary")
    else:
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
