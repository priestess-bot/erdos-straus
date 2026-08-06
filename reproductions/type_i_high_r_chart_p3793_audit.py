#!/usr/bin/env python3
"""Verify the p=3793 G-parented non-return high-R local candidate.

The first high anchor is G, not F.  A same-chart support promotion preserves
its explicit Legendre separator and therefore remains a valid charged parent.
The later F-to-F cofactor transition is a genuine source-local non-return
candidate, though p=3793 is independently terminal by a direct Type I form.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm
from pathlib import Path

from short_certificate import type_i_normal_form_certificate, verify_certificate
from type_i_high_r_chart_two_anchor import (
    canonical_chart,
    factorization,
    high_R_path_anchored_bundle,
    is_prime,
    legendre_g_fiber,
    make_state,
    residue_witness,
    same_chart_parent_replay,
    verify_charged_parent_replay,
    verify_cofactor_r_chart_normal_form,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-r-chart-p3793-audit-results.json"


def type_i_terminal(prime: int) -> dict[str, object]:
    certificate = type_i_normal_form_certificate(prime, 7, 1, 1)
    if certificate is None or not verify_certificate(certificate):
        raise AssertionError("p=3793 Type I gap-7 terminal failed")
    x, y, z = certificate.x, certificate.y, certificate.z
    c = 950
    h = 542
    checks = {
        "normal_form": prime == 4 * c - 7,
        "gap_divides_Bp_plus_A": (prime + 1) % 7 == 0,
        "denominator_parameters": x == c and y == c * h and z == prime * c * h,
        "unit_fraction_identity": 4 * x * y * z == prime * (y * z + x * z + x * y),
    }
    if not all(checks.values()):
        raise AssertionError("p=3793 Type I terminal arithmetic changed")
    return {
        "certificate_type": "type_i_normal_form_terminal",
        "selector_status": "terminal_leaf",
        "recursive_edge_eligible": False,
        "normal_form": {"gap": 7, "A": 1, "B": 1, "C": c, "H": h},
        "denominators": {"x": x, "y": y, "z": z},
        "checks": checks,
    }


def build_result() -> dict[str, object]:
    prime = 3_793
    B_p = (prime - 1) ** 2 // 4
    R_0 = 3_623
    K_0 = (prime * R_0 + 1) // 4
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and 3 <= R_0 <= prime - 2
        and K_0 == 3_435_510
        and factorization(K_0) == [(2, 1), (3, 1), (5, 1), (13, 1), (23, 1), (383, 1)]
    ):
        raise AssertionError("p=3793 core anchor changed")

    root_bundle = high_R_path_anchored_bundle(prime=prime, R=R_0, support=1)
    root_rechart = root_bundle["rechart"]
    Q_0 = int(root_bundle["complete_excess_bundle"]["Q"])
    beta_0 = int(root_bundle["complete_excess_bundle"]["beta"])
    R_1 = int(root_rechart["R"])
    K_1 = int(root_rechart["K"])
    if not (
        (Q_0, beta_0, R_1, K_1) == (1_811, 2, 7_011, 6_648_181)
        and factorization(K_1) == [(1_811, 1), (3_671, 1)]
        and root_rechart["result_class"] == "overflow"
        and R_1 > prime
        and K_1 % Q_0 == 0
    ):
        raise AssertionError("p=3793 first high anchor changed")

    anchor_g_fiber = legendre_g_fiber(R_1, K_1, 19)
    anchor_g_checks = anchor_g_fiber.get("conditions")
    if not isinstance(anchor_g_checks, dict) or not all(anchor_g_checks.values()):
        raise AssertionError("p=3793 first high anchor G separator changed")
    parent_replay = same_chart_parent_replay(
        prime=prime,
        B_p=B_p,
        root_bundle=root_bundle,
        fiber=anchor_g_fiber,
    )
    high_anchor_state = parent_replay["successor_state"]
    if not isinstance(high_anchor_state, dict) or not verify_charged_parent_replay(
        parent_replay, high_anchor_state
    ):
        raise AssertionError("p=3793 G-aware same-chart parent did not replay")

    high_bundle = high_R_path_anchored_bundle(prime=prime, R=R_1, support=Q_0)
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
        (Q_1, beta_1, M, R_M, K_M, C, d, n, k, r)
        == (
            7_010,
            1,
            12_695_110,
            48_491_103,
            45_981_688_420,
            3_622,
            171,
            2_289_337,
            3_346,
            3_732,
        )
        and M == lcm(Q_0, Q_1)
        and K_M == M * C
        and prime * n == 4 * M * d + 1
    ):
        raise AssertionError("p=3793 high overflow changed")

    s_numerator = 4 * r * d + 1
    if s_numerator % prime:
        raise AssertionError("p=3793 r-chart s is not integral")
    s = s_numerator // prime
    R_r = 4 * r - s
    K_r = r * C
    g = gcd(Q_0, C)
    a = Q_0 // g
    A_C = lcm(Q_0, C)
    target_C = r // a
    target_d = prime - target_C
    target_n = 4 * A_C - R_r
    cofactor_checks = {
        "nonreturn": R_r != R_1,
        "cofactor_gate": r % a == 0,
        "strict_support_growth": Q_0 < A_C <= B_p,
        "r_chart": prime * s == 4 * r * d + 1 and K_r == r * C,
        "target_canonical_chart": canonical_chart(prime, A_C) == (R_r, K_r),
        "target_overflow_normal_form": (
            target_C > 0
            and target_d > 0
            and target_n > 0
            and K_r == A_C * target_C
            and prime * target_n == 4 * A_C * target_d + 1
        ),
    }
    if not (
        (s, R_r, K_r, g, a, A_C, target_C, target_d, target_n)
        == (673, 14_255, 13_517_304, 1_811, 1, 3_622, 3_732, 61, 233)
        and all(cofactor_checks.values())
    ):
        raise AssertionError("p=3793 cofactor r-chart normal form changed")

    source_fiber = residue_witness(
        R_M,
        factorization(K_M),
        (0, -133, -11, 1),
    )
    target_fiber = residue_witness(
        R_r,
        factorization(K_r),
        (-1, -3, -2, 9),
    )
    if not (
        source_fiber["classification"] == "F"
        and source_fiber["witness_l1"] == 145
        and target_fiber["classification"] == "F"
        and target_fiber["witness_l1"] == 15
    ):
        raise AssertionError("p=3793 formal F fibers changed")

    source_state = make_state(
        prime=prime,
        R=R_M,
        K=K_M,
        support=Q_0,
        state_class="overflow",
        fiber_class=str(source_fiber["classification"]),
        source_tree_scope="fresh_source_tree_only",
    )
    successor_state = make_state(
        prime=prime,
        R=R_r,
        K=K_r,
        support=A_C,
        state_class="overflow",
        fiber_class=str(target_fiber["classification"]),
        source_tree_scope="fresh_source_tree_only",
    )
    cofactor_normal_form = verify_cofactor_r_chart_normal_form(
        prime=prime,
        support=Q_0,
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
        charged_parent_replayed=verify_charged_parent_replay(
            parent_replay, high_anchor_state
        ),
    )
    if not cofactor_normal_form["passed"]:
        raise AssertionError("p=3793 cofactor normal-form replay failed")

    terminal = type_i_terminal(prime)
    e1_e5 = {
        "E1": bool(
            all(bool(value) for value in root_bundle["conditions"].values())
            and verify_charged_parent_replay(parent_replay, high_anchor_state)
            and all(bool(value) for value in high_bundle["conditions"].values())
        ),
        "E2": bool(cofactor_normal_form["construction"] and cofactor_checks["target_canonical_chart"]),
        "E3": bool(cofactor_normal_form["passed"]),
        "E4": bool(
            anchor_g_fiber["classification"] == "G"
            and source_fiber["classification"] == "F"
            and target_fiber["classification"] == "F"
            and source_fiber.get("signed_defect")
            and target_fiber.get("signed_defect")
        ),
        "E5": B_p // A_C < B_p // Q_0,
    }
    if e1_e5 != {f"E{index}": True for index in range(1, 6)}:
        raise AssertionError("p=3793 local E1-E5 contract failed")

    return {
        "schema_version": 1,
        "certificate_type": "type_i_high_r_chart_p3793_g_parent_nonreturn_v2",
        "selector_status": "candidate_transition",
        "recursive_edge_eligible": False,
        "proof_boundary": (
            "the G-aware same-chart parent and F-to-F cofactor normal form prove a "
            "source-local non-return candidate.  It remains outside the global selector "
            "because no non-resetting phase rank has been proved; terminal-first already "
            "solves this prime by a direct Type I normal form."
        ),
        "prime": prime,
        "B_p": B_p,
        "core_anchor": {"R": R_0, "K": K_0},
        "first_high_anchor": {
            "Q": Q_0,
            "beta": beta_0,
            "R": R_1,
            "K": K_1,
            "fiber": anchor_g_fiber,
            "same_chart_parent_replay": parent_replay,
        },
        "formal_high_overflow": {
            "Q": Q_1,
            "beta": beta_1,
            "M": M,
            "R": R_M,
            "K": K_M,
            "C": C,
            "d": d,
            "n": n,
            "fiber": source_fiber,
            "state": source_state,
        },
        "formal_nonreturn_target": {
            "k": k,
            "r": r,
            "s": s,
            "R": R_r,
            "K": K_r,
            "gcd_A_C": g,
            "A_over_gcd": a,
            "A_C": A_C,
            "C": target_C,
            "d": target_d,
            "n": target_n,
            "checks": cofactor_checks,
            "fiber": target_fiber,
            "state": successor_state,
        },
        "candidate_e1_e5": e1_e5,
        "cofactor_normal_form": cofactor_normal_form,
        "direct_terminal": terminal,
        "p_plus_four_factorization": [[factor, exponent] for factor, exponent in factorization(prime + 4)],
        "conclusion": {
            "source_local_nonreturn_candidate": True,
            "nonreturn_phase": 1,
            "terminal_first_status": "terminal_leaf",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if not args.verify:
        args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "prime": result["prime"],
                "selector_status": result["selector_status"],
                "candidate_e1_e5": result["candidate_e1_e5"],
                "terminal_denominators": result["direct_terminal"]["denominators"],
            },
            ensure_ascii=True,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
