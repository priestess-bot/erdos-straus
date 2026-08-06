#!/usr/bin/env python3
"""Reproduce the p=7393 F-to-F high-R non-return r-chart."""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm
from pathlib import Path

import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-r-chart-7393-nonreturn-results.json"


def gap_seven_type_i_terminal(prime: int) -> dict[str, object]:
    """Verify the terminal-first Type I certificate at the fixed gap m=7."""
    gap = 7
    x = (prime + gap) // 4
    divisor = 5
    if (prime + gap) % 4 or (prime * x + divisor) % gap:
        raise AssertionError("gap-seven Type I input is not integral")
    y = (prime * x + divisor) // gap
    z_numerator = prime * (x + prime * x * x // divisor)
    if z_numerator % gap:
        raise AssertionError("gap-seven Type I final denominator is not integral")
    z = z_numerator // gap
    common = gcd(divisor, x)
    a = divisor // common
    b = x // common
    c = common // a
    if gcd(a, b) != 1 or (b * prime + a) % gap:
        raise AssertionError("gap-seven Type I normal form failed")
    h = (b * prime + a) // gap
    checks = {
        "gap_domain": 3 <= gap <= prime - 2 and gap % 4 == 3,
        "x": 4 * x == prime + gap,
        "type_i_divisor": x * x % divisor == 0 and (prime * x + divisor) % gap == 0,
        "normal_form": x == a * b * c and divisor == a * a * c,
        "denominators": y == a * c * h and z == prime * b * c * h,
        "identity": 4 * x * y * z == prime * (y * z + x * z + x * y),
    }
    if not all(checks.values()):
        raise AssertionError("gap-seven Type I terminal failed")
    return {
        "certificate_type": "type_i_gap_seven_terminal",
        "selector_status": "terminal_leaf",
        "recursive_edge_eligible": False,
        "gap": gap,
        "type_i_normal_form": {"A": a, "B": b, "C": c, "H": h},
        "divisor": divisor,
        "denominators": {"x": x, "y": y, "z": z},
        "checks": checks,
    }


def build_result() -> dict[str, object]:
    prime = 7393
    B_p = (prime - 1) ** 2 // 4
    R_0 = 2491
    K_0 = (prime * R_0 + 1) // 4
    if not (
        shared.is_prime(prime)
        and prime % 24 == 1
        and 3 <= R_0 <= prime - 2
        and R_0 % 4 == 3
        and K_0 == 4_603_991
        and shared.factorization(K_0) == [(7, 2), (17, 1), (5527, 1)]
    ):
        raise AssertionError("p=7393 core root changed")

    root_bundle = shared.high_R_path_anchored_bundle(
        prime=prime,
        R=R_0,
        support=1,
    )
    root_rechart = root_bundle["rechart"]
    Q_0 = int(root_bundle["complete_excess_bundle"]["Q"])
    beta_0 = int(root_bundle["complete_excess_bundle"]["beta"])
    A = int(root_rechart["M"])
    R_1 = int(root_rechart["R"])
    K_1 = int(root_rechart["K"])
    if not (
        (Q_0, beta_0, A, R_1, K_1) == (2490, 1, 2490, 9863, 18_229_290)
        and root_rechart["result_class"] == "overflow"
        and A <= B_p
        and K_1 == A * 7321
    ):
        raise AssertionError("p=7393 first anchor changed")

    anchor_fiber = shared.residue_witness(
        R_1,
        shared.factorization(K_1),
        (0, -9, 0, 7, -1),
    )
    parent_replay = shared.same_chart_parent_replay(
        prime=prime,
        B_p=B_p,
        root_bundle=root_bundle,
        fiber=anchor_fiber,
    )
    high_anchor_state = parent_replay["successor_state"]
    if not isinstance(high_anchor_state, dict) or not shared.verify_charged_parent_replay(
        parent_replay, high_anchor_state
    ):
        raise AssertionError("p=7393 charged parent did not replay")
    if not (
        high_anchor_state["R"] == R_1
        and high_anchor_state["K"] == K_1
        and high_anchor_state["absorbed_support"] == A
        and high_anchor_state["fiber_class"] == "F"
    ):
        raise AssertionError("p=7393 charged high anchor changed")

    high_bundle = shared.high_R_path_anchored_bundle(
        prime=prime,
        R=R_1,
        support=A,
    )
    high_rechart = high_bundle["rechart"]
    Q_1 = int(high_bundle["complete_excess_bundle"]["Q"])
    beta_1 = int(high_bundle["complete_excess_bundle"]["beta"])
    M = int(high_rechart["M"])
    R_M = int(high_rechart["R"])
    K_M = int(high_rechart["K"])
    C = int(high_rechart["C"])
    d = int(high_rechart["d"])
    n = int(high_rechart["n"])
    k, r = divmod(M, prime)
    if not (
        (Q_1, beta_1) == (4931, 2)
        and (M, R_M, K_M, C, d, n, k, r)
        == (12_278_190, 41_891_663, 77_426_266_140, 6306, 1087, 7_221_097, 1660, 5810)
        and M <= B_p
        and prime * n == 4 * M * d + 1
    ):
        raise AssertionError("p=7393 high-R overflow changed")

    g = gcd(A, C)
    a = A // g
    A_C = lcm(A, C)
    s_numerator = 4 * r * d + 1
    if s_numerator % prime:
        raise AssertionError("p=7393 cofactor s is not integral")
    s = s_numerator // prime
    R_r = 4 * r - s
    K_r = r * C
    C_target = r // a
    d_target = prime - C_target
    n_target = 4 * A_C - R_r
    delta_numerator = K_r - K_1
    if delta_numerator % prime:
        raise AssertionError("p=7393 phase delta is not integral")
    delta = delta_numerator // prime
    h = delta // A
    if not (
        (g, a, A_C, s, R_r, K_r, C_target, d_target, n_target, delta, h)
        == (6, 415, 2_616_990, 3417, 19_823, 36_637_860, 14, 7379, 10_448_137, 2490, 1)
        and r % a == 0
        and shared.canonical_chart(prime, A_C) == (R_r, K_r)
        and K_r == A_C * C_target
        and prime * n_target == 4 * A_C * d_target + 1
        and R_r == R_1 + 4 * delta
        and delta == A * h
        and h == 1
        and R_r > prime
        and R_r != R_1
        and K_1 % r != 0
    ):
        raise AssertionError("p=7393 non-return r-chart changed")

    source_fiber = shared.residue_witness(
        R_M,
        shared.factorization(K_M),
        (-26, 5, 0, -9, 8, 5),
    )
    target_fiber = shared.residue_witness(
        R_r,
        shared.factorization(K_r),
        (0, -4, -1, 0, 4, -2),
    )
    scope = "fresh_source_tree_only"
    source_state = shared.make_state(
        prime=prime,
        R=R_M,
        K=K_M,
        support=A,
        state_class="overflow",
        fiber_class=str(source_fiber["classification"]),
        source_tree_scope=scope,
    )
    successor_state = shared.make_state(
        prime=prime,
        R=R_r,
        K=K_r,
        support=A_C,
        state_class="overflow",
        fiber_class=str(target_fiber["classification"]),
        source_tree_scope=scope,
    )
    cofactor_normal_form = shared.verify_cofactor_r_chart_normal_form(
        prime=prime,
        support=A,
        M=M,
        R_M=R_M,
        K_M=K_M,
        C=C,
        d=d,
        n=n,
        r=r,
        s=s,
        R_r=R_r,
        K_r=K_r,
        cofactor_support=A_C,
        source_state=source_state,
        successor_state=successor_state,
        source_fiber=source_fiber,
        successor_fiber=target_fiber,
        charged_parent_replayed=shared.verify_charged_parent_replay(
            parent_replay, high_anchor_state
        ),
    )
    source_potential = B_p // A
    target_potential = B_p // A_C
    if not (
        source_potential == 5486
        and target_potential == 5
        and target_potential < source_potential
        and cofactor_normal_form["passed"]
    ):
        raise AssertionError("p=7393 local potential changed")
    local_e1_e5 = {
        "E1": bool(
            all(bool(value) for value in root_bundle["conditions"].values())
            and shared.verify_charged_parent_replay(parent_replay, high_anchor_state)
            and all(bool(value) for value in high_bundle["conditions"].values())
        ),
        "E2": bool(
            cofactor_normal_form["construction"]
            and shared.canonical_chart(prime, A_C) == (R_r, K_r)
            and delta == A
            and h == 1
        ),
        "E3": cofactor_normal_form["passed"],
        "E4": bool(
            anchor_fiber["classification"] == "F"
            and source_fiber["classification"] == "F"
            and target_fiber["classification"] == "F"
            and anchor_fiber.get("signed_defect")
            and source_fiber.get("signed_defect")
            and target_fiber.get("signed_defect")
        ),
        "E5": target_potential < source_potential,
    }
    if local_e1_e5 != {f"E{index}": True for index in range(1, 6)}:
        raise AssertionError("p=7393 local E1-E5 contract failed")

    p_plus_four_factors = shared.factorization(prime + 4)
    direct_gap_candidates = [
        factor for factor, _exponent in p_plus_four_factors if factor % 4 == 3
    ]
    terminal = gap_seven_type_i_terminal(prime)
    if direct_gap_candidates or terminal["selector_status"] != "terminal_leaf":
        raise AssertionError("p=7393 terminal-first diagnostics changed")
    e1_e5 = dict(local_e1_e5)
    e1_e5["E5"] = False
    return {
        "certificate_type": "type_i_high_r_nonreturn_f_to_f_v1",
        "selector_status": "candidate_transition",
        "recursive_edge_eligible": False,
        "proof_boundary": (
            "the dedicated receipt closes the fresh root, F parent, high-R source, "
            "F-to-F non-return r-chart, and local support decrease; a global "
            "non-resetting phase rank is still absent"
        ),
        "e1_e5": e1_e5,
        "local_e1_e5": local_e1_e5,
        "missing_conditions": ["global_nonresetting_phase_rank"],
        "prime": prime,
        "B_p": B_p,
        "core_anchor": root_bundle,
        "first_overflow": {
            "M": A,
            "R": R_1,
            "K": K_1,
            "C": root_rechart["C"],
            "d": root_rechart["d"],
            "n": root_rechart["n"],
            "fiber": anchor_fiber,
        },
        "same_chart_parent_replay": parent_replay,
        "high_R_anchor": high_bundle,
        "source_overflow": {
            "A": A,
            "M": M,
            "R": R_M,
            "K": K_M,
            "C": C,
            "d": d,
            "n": n,
            "k": k,
            "r": r,
            "inside_support_potential_domain": M <= B_p,
            "fiber": source_fiber,
            "state": source_state,
        },
        "r_chart_target": {
            "A": A_C,
            "R": R_r,
            "K": K_r,
            "C": C_target,
            "d": d_target,
            "n": n_target,
            "fiber": target_fiber,
            "state": successor_state,
        },
        "nonreturn_phase": {
            "anchor_R": R_1,
            "anchor_K": K_1,
            "delta": delta,
            "support_multiple_h": h,
            "formula": "R_r=R_1+4*delta; delta=A*h",
            "large_divisor_return_test": {
                "r_divides_anchor_K": K_1 % r == 0,
                "return_condition": "r|K_1 and K_1/r<p",
                "nonreturn_verified": True,
            },
        },
        "cofactor_normal_form": cofactor_normal_form,
        "local_potential": {"source": source_potential, "target": target_potential},
        "terminal_first_diagnostic": {
            "p_plus_four_factorization": [
                [factor, exponent] for factor, exponent in p_plus_four_factors
            ],
            "p_plus_four_direct_gap_candidates": direct_gap_candidates,
            "gap_seven_type_i_terminal": terminal,
            "preempts_high_r_candidate_for_p7393": True,
            "does_not_rule_out_the_local_nonreturn_construction": True,
        },
        "terminal_first_status": "terminal_leaf",
        "integration_status": "dedicated_reproducer_only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified p=7393 F-to-F high-R non-return r-chart")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
