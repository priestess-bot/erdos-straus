#!/usr/bin/env python3
"""Verify the automatic-q parameter phase/descent trichotomy.

This replays four actual fresh-root controls and checks the residual identity
n_T = n + 4*A*e.  It classifies only the direct automatic-cofactor target:
no parent, terminal-first, or global solution-lift claim is made here.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import type_i_high_anchor_q2_bku_parameterization as q2
import type_i_high_anchor_q3_bku_parameterization as q3
import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-automatic-q-phase-descent-trichotomy-results.json"

PARAMETER_CLASSES = (
    {"q": 2, "k_mod_q": 0, "h": 1, "e": 0, "small_target": True},
    {"q": 2, "k_mod_q": 1, "h": 0, "e": 1, "small_target": False},
    {"q": 3, "k_mod_q": 0, "h": 1, "e": 1, "small_target": False},
    {"q": 3, "k_mod_q": 1, "h": 0, "e": 2, "small_target": False},
    {"q": 3, "k_mod_q": 2, "h": 2, "e": 0, "small_target": True},
)

SOURCE_CONTROLS = (
    {"q": 2, "label": "p3793", "p": 3_793},
    {"q": 3, "label": "p60913", "p": 60_913},
    {"q": 3, "label": "p41617", "p": 41_617},
    {"q": 3, "label": "p93481", "p": 93_481},
)


def parameter_phase(q: int, k: int) -> tuple[int, int]:
    if q == 2:
        h = (k + 1) % 2
    elif q == 3:
        h = (1 - k) % 3
    else:
        raise AssertionError("automatic-q trichotomy only permits q=2 or q=3")
    return h, q - h - 1


def verify_parameter_classes() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for item in PARAMETER_CLASSES:
        q = int(item["q"])
        k_mod_q = int(item["k_mod_q"])
        h, e = parameter_phase(q, k_mod_q)
        checks = {
            "phase": h == int(item["h"]),
            "excess": e == int(item["e"]),
            "small_target_exactly_at_e_zero": bool(item["small_target"]) == (e == 0),
        }
        if not all(checks.values()):
            raise AssertionError(f"parameter class changed: {item}, {checks}")
        rows.append({"q": q, "k_mod_q": k_mod_q, "h": h, "e": e, "checks": checks})
    return rows


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
    raise AssertionError("missing frozen automatic-q source control")


def replay_residual(control: dict[str, int | str], q: int, label: str) -> dict[str, object]:
    p = int(control["p"])
    A = int(control["A"])
    R = int(control["R"])
    k = int(control["k"])
    K = (p * R + 1) // 4
    B = K // A
    bundle = shared.high_R_path_anchored_bundle(prime=p, R=R, support=A)
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict):
        raise AssertionError(f"{label}: full-excess rechart shape changed")
    M = int(rechart["M"])
    C = int(rechart["C"])
    r = M % p
    phase_numerator = q * r - B
    if phase_numerator % p:
        raise AssertionError(f"{label}: phase stopped being integral")
    h = phase_numerator // p
    parameter_h, e = parameter_phase(q, k)
    d = p - B
    d_target = p - r
    source_defect = p - C
    target_s_numerator = 4 * r * source_defect + 1
    if target_s_numerator % p:
        raise AssertionError(f"{label}: target r-chart stopped being integral")
    target_s = target_s_numerator // p
    R_target = 4 * r - target_s
    K_target = r * C
    n = 4 * A - R
    n_target = 4 * C - R_target
    checks = {
        "core_prime": shared.is_prime(p) and p % 24 == 1,
        "actual_automatic_source": (
            p < R < 4 * A
            and M == A * (R - 1)
            and C == q * A
            and C < p
            and shared.canonical_chart(p, A) == (R, K)
        ),
        "target_canonical_chart": shared.canonical_chart(p, C) == (R_target, K_target),
        "phase_from_parameter": h == parameter_h and 0 <= h < q,
        "residual_identity": q * d_target == d + p * e,
        "canonical_residual_shift": n_target == n + 4 * A * e,
        "minimal_phase_fixed_n": (e == 0) == (n_target == n),
        "nonminimal_leaves_small_domain": (e >= 1) == (n_target > p),
    }
    if e == 0:
        checks["fixed_n_bridge_arithmetic_domain"] = 5 <= n <= p - 4 and d_target >= 2
    if not all(checks.values()):
        raise AssertionError(f"{label}: residual trichotomy failed: {checks}")
    return {
        "label": label,
        "source": {"p": p, "A": A, "R": R, "B": B, "q": q, "k": k},
        "target": {"A_T": C, "R_T": R_target, "K_T": K_target},
        "phase": {"h": h, "e": e, "r": r},
        "residuals": {"n": n, "n_T": n_target, "d": d, "d_T": d_target},
        "checks": checks,
    }


def build_result() -> dict[str, object]:
    parameter_rows = verify_parameter_classes()
    controls = [
        replay_residual(source_control(int(item["q"]), int(item["p"])), int(item["q"]), str(item["label"]))
        for item in SOURCE_CONTROLS
    ]
    minimal = [row["label"] for row in controls if int(row["phase"]["e"]) == 0]
    nonminimal = [row["label"] for row in controls if int(row["phase"]["e"]) >= 1]
    if minimal != ["p3793", "p60913"] or nonminimal != ["p41617", "p93481"]:
        raise AssertionError("frozen phase/descent control partition changed")
    return {
        "schema_version": 1,
        "certificate_type": "automatic_q_parameter_phase_descent_trichotomy_v1",
        "scope": (
            "Exact phase and residual classification for direct automatic C=qA cofactor "
            "targets in the coprime beta_0=2 two-anchor source subfamily. This does not "
            "supply terminal-first admission, a parent receipt, a typed lift, or a global edge."
        ),
        "parameter_classes": parameter_rows,
        "source_controls": controls,
        "partition": {"minimal_phase": minimal, "nonminimal": nonminimal},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified automatic-q phase/descent trichotomy: q2/q3 parameter classes + 4 source controls")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
