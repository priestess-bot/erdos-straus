#!/usr/bin/env python3
"""Verify the all-phase affine target and outer-rank exit for automatic q.

For an actual beta_0=2, two-anchor automatic source with C=qA, this fixture
replays the exact target chart in every observed phase. It distinguishes the
loss of a literal n<p predecessor in nonminimal q=3 phases from the separate,
still strict support-rank payment of the H=>T macro. It does not create a
parent receipt, terminal-first guard, typed lift, or selector edge.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import type_i_high_anchor_q2_bku_parameterization as q2
import type_i_high_anchor_q3_bku_parameterization as q3
import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-high-anchor-automatic-q-affine-rank-exit-results.json"
)

CONTROLS = (
    {"q": 2, "p": 3_793, "label": "p3793_q2_h1"},
    {"q": 3, "p": 41_617, "label": "p41617_q3_h0"},
    {"q": 3, "p": 60_913, "label": "p60913_q3_h2"},
    {"q": 3, "p": 93_481, "label": "p93481_q3_h0"},
)


def outer_rank(prime: int, support: int) -> int:
    return (prime - 1) ** 2 // (4 * support)


def source_control(q: int, prime: int) -> dict[str, int | str]:
    if q == 2:
        for control in q2.CONTROLS:
            if int(control["p"]) == prime:
                q2.verify_positive_control(control)
                return control
    if q == 3:
        for control in q3.CONTROLS:
            if int(control["p"]) == prime:
                q3.verify_control(control)
                return control
    raise AssertionError("missing verified automatic-q source control")


def replay(control_spec: dict[str, int | str]) -> dict[str, object]:
    q = int(control_spec["q"])
    label = str(control_spec["label"])
    control = source_control(q, int(control_spec["p"]))
    p = int(control["p"])
    A = int(control["A"])
    R = int(control["R"])
    K = (p * R + 1) // 4
    if K % A:
        raise AssertionError(f"{label}: source support stopped dividing K")
    B = K // A

    bundle = shared.high_R_path_anchored_bundle(prime=p, R=R, support=A)
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict):
        raise AssertionError(f"{label}: automatic bundle shape changed")
    M = int(rechart["M"])
    C = int(rechart["C"])
    r = M % p
    if r == 0:
        raise AssertionError(f"{label}: automatic residue vanished")
    phase_numerator = q * r - B
    if phase_numerator % p:
        raise AssertionError(f"{label}: automatic phase stopped being integral")
    h = phase_numerator // p

    A_T = q * A
    K_T = r * C
    source_defect = p - C
    s_numerator = 4 * r * source_defect + 1
    if s_numerator % p:
        raise AssertionError(f"{label}: cofactor target stopped being integral")
    R_T = 4 * r - s_numerator // p
    n = 4 * A - R
    n_T = 4 * A_T - R_T
    e = q - h - 1

    checks = {
        "actual_strict_automatic_source": (
            shared.is_prime(p)
            and p % 24 == 1
            and p < R < 4 * A
            and M == A * (R - 1)
            and C == q * A < p
            and shared.canonical_chart(p, A) == (R, K)
        ),
        "phase_range": 0 <= h < q,
        "automatic_phase_equation": q * r == B + h * p,
        "affine_target_K": K_T == K + h * p * A,
        "affine_target_R": R_T == R + 4 * h * A,
        "target_support": A_T == C and A_T == q * A,
        "target_quotient": (
            K_T % A_T == 0 and K_T // A_T == r == (B + h * p) // q
        ),
        "target_canonical_high_chart": (
            p < R_T < 4 * A_T
            and shared.canonical_chart(p, A_T) == (R_T, K_T)
        ),
        "residual_shift": n_T == n + 4 * A * e,
        "outer_rank_strict": outer_rank(p, A_T) < outer_rank(p, A),
        "q_times_support_below_p": A_T < p,
    }
    if h == 0:
        checks["zero_phase_same_chart_support_promotion"] = (
            (R_T, K_T) == (R, K) and B % q == 0
        )
    if h == q - 1:
        checks["minimal_phase_fixed_n"] = n_T == n
    if not all(checks.values()):
        raise AssertionError(f"{label}: affine automatic-q exit failed: {checks}")
    return {
        "label": label,
        "source": {"p": p, "A": A, "R": R, "K": K, "B": B, "q": q},
        "target": {"A_T": A_T, "R_T": R_T, "K_T": K_T, "B_T": r},
        "phase": {"h": h, "e": e, "r": r},
        "residuals": {"n": n, "n_T": n_T},
        "outer_rank": {"source": outer_rank(p, A), "target": outer_rank(p, A_T)},
        "checks": checks,
    }


def build_result() -> dict[str, object]:
    controls = [replay(control) for control in CONTROLS]
    labels_by_phase = {
        "q2_h1": [
            row["label"]
            for row in controls
            if row["source"]["q"] == 2 and row["phase"]["h"] == 1
        ],
        "q3_h0": [
            row["label"]
            for row in controls
            if row["source"]["q"] == 3 and row["phase"]["h"] == 0
        ],
        "q3_h2": [
            row["label"]
            for row in controls
            if row["source"]["q"] == 3 and row["phase"]["h"] == 2
        ],
    }
    if labels_by_phase != {
        "q2_h1": ["p3793_q2_h1"],
        "q3_h0": ["p41617_q3_h0", "p93481_q3_h0"],
        "q3_h2": ["p60913_q3_h2"],
    }:
        raise AssertionError("frozen automatic-q affine phase controls changed")
    return {
        "schema_version": 1,
        "certificate_type": "automatic_q_affine_all_phase_outer_rank_exit_v1",
        "scope": (
            "Exact H=>T arithmetic and outer-rank payment for actual automatic C=qA "
            "sources. A strict rank payment is conditional on the separate macro E1--E4 "
            "and terminal-first admission contracts; it is not a literal n<p descent when e>0."
        ),
        "controls": controls,
        "phase_coverage": labels_by_phase,
        "uninstantiated_parameter_class": {
            "q": 3,
            "k_mod_3": 0,
            "h": 1,
            "e": 1,
            "note": (
                "The affine proof covers this source-compatible parameter class, but this "
                "fixture does not claim an actual fresh-root control for it."
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified automatic-q affine all-phase outer-rank exit: q2 h1, q3 h0/h2")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
