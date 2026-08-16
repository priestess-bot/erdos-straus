#!/usr/bin/env python3
"""Verify the b-k-u inverse parameterization of q=3 automatic high sources.

The fixture reconstructs two actual h=0 phase-boundary sources and the
actual p=60913 h=2 source from divisors of N_b^(3)(k).  All controls retain
the coprime beta_0=2 two-anchor source conditions; the h=0 rows prevent an
automatic C=3A rechart from being misclassified as a minimal-positive-phase
fixed-n input.
"""

from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path

import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-q3-bku-parameterization-results.json"

CONTROLS = (
    {
        "label": "p41617_h0_phase_boundary",
        "p": 41_617,
        "A": 11_051,
        "R": 43_811,
        "b": 8_464,
        "k": 2_041,
        "u": 231_066_297,
        "phase_h": 0,
    },
    {
        "label": "p60913_h2_minimal_positive_phase",
        "p": 60_913,
        "A": 18_647,
        "R": 72_259,
        "b": 4_972,
        "k": 1_088,
        "u": 31_281_961,
        "phase_h": 2,
    },
    {
        "label": "p93481_h0_phase_boundary",
        "p": 93_481,
        "A": 26_219,
        "R": 95_387,
        "b": 14_824,
        "k": 2_365,
        "u": 507_142_593,
        "phase_h": 0,
    },
)


def N(b: int, k: int) -> int:
    """Return the q=3 factor polynomial N_b^(3)(k)."""
    return 12 * b**3 + 8 * b * b + 12 * b + 9 + 16 * b * b * k


def strict_odd_excess(value: int, half_p_plus_one: int) -> bool:
    return value > 0 and value % 2 == 1 and all(
        exponent > shared.valuation(half_p_plus_one, prime)
        for prime, exponent in shared.factorization(value)
    )


def recover_from_bku(b: int, k: int, u: int) -> dict[str, int]:
    if b <= 0 or k <= 0 or u <= 0:
        raise AssertionError("b, k, and u must be positive")
    numerator = N(b, k)
    if numerator % u:
        raise AssertionError("u must divide N_b^(3)(k)")
    p = numerator // u
    e_numerator = 16 * b * k - 4 * b - u
    if e_numerator <= 0 or e_numerator % 3:
        raise AssertionError("b-k-u row does not recover a positive integral e")
    e = e_numerator // 3
    if (e * p + 3) % (4 * b * b):
        raise AssertionError("b-k-u row does not recover an integral delta")
    delta = 1 + (e * p + 3) // (4 * b * b)
    if (p - b) % 3:
        raise AssertionError("b-k-u row does not recover an integral support")
    A = (p - b) // 3
    R = p + delta
    return {
        "N": numerator,
        "p": p,
        "e": e,
        "delta": delta,
        "A": A,
        "R": R,
    }


def verify_control(control: dict[str, int | str]) -> dict[str, object]:
    label = str(control["label"])
    b = int(control["b"])
    k = int(control["k"])
    u = int(control["u"])
    expected_h = int(control["phase_h"])
    recovered = recover_from_bku(b, k, u)
    p = recovered["p"]
    A = recovered["A"]
    R = recovered["R"]
    delta = recovered["delta"]
    e = recovered["e"]
    if (p, A, R) != (int(control["p"]), int(control["A"]), int(control["R"])):
        raise AssertionError(f"{label}: b-k-u reconstruction changed")

    B_numerator = p * R + 1
    if B_numerator % (4 * A):
        raise AssertionError(f"{label}: canonical B stopped being integral")
    B = B_numerator // (4 * A)
    root_bundle = shared.high_R_path_anchored_bundle(
        prime=p, R=2 * A + 1, support=1
    )
    root_rechart = root_bundle["rechart"]
    if not isinstance(root_rechart, dict):
        raise AssertionError(f"{label}: root bundle shape changed")
    high_bundle = shared.high_R_path_anchored_bundle(prime=p, R=R, support=A)
    high_rechart = high_bundle["rechart"]
    if not isinstance(high_rechart, dict):
        raise AssertionError(f"{label}: high bundle shape changed")

    Q0 = int(root_bundle["complete_excess_bundle"]["Q"])
    beta0 = int(root_bundle["complete_excess_bundle"]["beta"])
    Q1 = int(high_bundle["complete_excess_bundle"]["Q"])
    beta1 = int(high_bundle["complete_excess_bundle"]["beta"])
    M = int(high_rechart["M"])
    C = int(high_rechart["C"])
    residue = M % p
    phase_numerator = 3 * residue - B
    if phase_numerator % p:
        raise AssertionError(f"{label}: q=3 phase stopped being integral")
    phase_h = phase_numerator // p

    checks = {
        "core_prime": shared.is_prime(p) and p % 24 == 1,
        "b_parity": b % 4 == 0 and A % 4 == 3,
        "q3_b_mod_eight_class": b % 8 in (0, 4),
        "k_window": 1 <= k <= b // 4,
        "factor_equation": recovered["N"] == u * p and 3 * e == 16 * b * k - 4 * b - u,
        "automatic_equation": 4 * b * b * (delta - 1) - 3 == e * p,
        "canonical_parameter_equation": 3 * b * (b + delta) + 3 == (4 * k - 1) * (p - b),
        "delta_window": 0 < 3 * delta < p - 4 * b and delta % 8 == 2,
        "canonical_high_anchor": (
            p < R < 4 * A
            and shared.canonical_chart(p, A) == (R, A * B)
            and B < p
        ),
        "coprime_two_anchor_subfamily": gcd(A, R - 1) == 1,
        "root_valuation_gate": strict_odd_excess(A, (p + 1) // 2),
        "second_valuation_gate": strict_odd_excess((R - 1) // 2, (p + 1) // 2),
        "root_complete_excess": (
            Q0 == A
            and beta0 == 2
            and int(root_rechart["M"]) == A
            and int(root_rechart["R"]) == R
            and int(root_rechart["K"]) == A * B
        ),
        "second_complete_excess": Q1 == R - 1 and beta1 == 1,
        "automatic_q_three": (
            M == A * (R - 1)
            and C == 3 * A
            and 3 * A < p
            and (12 * A * A * (R - 1)) % p == 1
        ),
        "phase_range": 0 <= phase_h < 3,
        "phase_residue": phase_h % 3 == (-B) % 3,
        "phase_matches_control": phase_h == expected_h,
        "minimal_positive_phase_gate": (phase_h == 2) == (B % 3 == 1),
    }
    if not all(checks.values()):
        raise AssertionError(f"{label}: q=3 b-k-u control failed: {checks}")
    return {
        "label": label,
        "input": {"b": b, "k": k, "u": u},
        "recovered": recovered,
        "high_anchor": {"B": B, "Q0": Q0, "beta0": beta0, "Q1": Q1, "beta1": beta1},
        "automatic_q": {"M": M, "C": C, "phase_h": phase_h},
        "checks": checks,
    }


def build_result() -> dict[str, object]:
    controls = [verify_control(control) for control in CONTROLS]
    h_zero_labels = [
        control["label"]
        for control in controls
        if int(control["automatic_q"]["phase_h"]) == 0
    ]
    h_two_labels = [
        control["label"]
        for control in controls
        if int(control["automatic_q"]["phase_h"]) == 2
    ]
    if h_zero_labels != ["p41617_h0_phase_boundary", "p93481_h0_phase_boundary"]:
        raise AssertionError("q=3 h=0 phase-boundary controls changed")
    if h_two_labels != ["p60913_h2_minimal_positive_phase"]:
        raise AssertionError("q=3 h=2 control changed")
    return {
        "schema_version": 1,
        "certificate_type": "q3_bku_automatic_high_source_parameterization_v1",
        "scope": (
            "Exact inverse parameterization of the coprime beta_0=2 q=3 automatic "
            "high-source subfamily. The phase gate is retained explicitly: source "
            "construction does not by itself give the h=2 fixed-n bridge input, a "
            "terminal-free state, or a global selector edge."
        ),
        "controls": controls,
        "phase_boundary": {"h_zero": h_zero_labels, "h_two": h_two_labels},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified q=3 b-k-u automatic source parameterization: 2 h=0 boundaries + p=60913 h=2")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
