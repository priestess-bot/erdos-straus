#!/usr/bin/env python3
"""Verify the b-k-u inverse parameterization of q=2 automatic high sources.

This fixture covers the coprime beta_0=2, minimal-positive-phase subfamily.
It reconstructs four fixed valid source rows from divisors of N_b(k), and
keeps p=673 as the root-parity boundary: its formal high chart exists but its
first complete excess is 2A rather than A.
"""

from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path

import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-q2-bku-parameterization-results.json"

CONTROLS = (
    {"p": 3_793, "A": 1_811, "R": 7_011, "b": 171, "k": 80, "u": 5_119},
    {
        "p": 34_897,
        "A": 13_635,
        "R": 39_827,
        "b": 7_627,
        "k": 1_756,
        "u": 37_139_375,
    },
    {
        "p": 67_801,
        "A": 26_491,
        "R": 84_187,
        "b": 14_819,
        "k": 4_364,
        "u": 152_540_695,
    },
    {
        "p": 68_713,
        "A": 31_143,
        "R": 103_067,
        "b": 6_427,
        "k": 2_104,
        "u": 12_787_511,
    },
)

PARITY_BOUNDARY = {"p": 673, "A": 317, "R": 699, "b": 39, "k": 2, "u": 199}


def N(b: int, k: int) -> int:
    return 2 * b * (b * b + b + 1) + 1 + 4 * b * b * k


def strict_odd_excess(value: int, half_p_plus_one: int) -> bool:
    if value <= 0 or value % 2 == 0:
        return False
    return all(
        exponent > shared.valuation(half_p_plus_one, prime)
        for prime, exponent in shared.factorization(value)
    )


def recover_from_bku(b: int, k: int, u: int) -> dict[str, int]:
    if b <= 0 or k <= 0 or u <= 0:
        raise AssertionError("b, k, and u must be positive")
    numerator = N(b, k)
    if numerator % u:
        raise AssertionError("u must divide N_b(k)")
    p = numerator // u
    e = 4 * b * k - u
    if e <= 0 or (e * p + 1) % (2 * b * b):
        raise AssertionError("b-k-u row does not recover an integral delta")
    delta = 1 + (e * p + 1) // (2 * b * b)
    if (p - b) % 2:
        raise AssertionError("b-k-u row does not recover an integral support")
    A = (p - b) // 2
    R = p + delta
    return {
        "N": numerator,
        "p": p,
        "e": e,
        "delta": delta,
        "A": A,
        "R": R,
    }


def verify_positive_control(control: dict[str, int]) -> dict[str, object]:
    b = control["b"]
    k = control["k"]
    u = control["u"]
    recovered = recover_from_bku(b, k, u)
    p = recovered["p"]
    A = recovered["A"]
    R = recovered["R"]
    delta = recovered["delta"]
    e = recovered["e"]
    if (p, A, R) != (control["p"], control["A"], control["R"]):
        raise AssertionError("b-k-u reconstruction changed")
    B = (p * R + 1) // (4 * A)
    s = (p + 1) // 2
    root_R = 2 * A + 1
    root_bundle = shared.high_R_path_anchored_bundle(
        prime=p, R=root_R, support=1
    )
    root_rechart = root_bundle["rechart"]
    if not isinstance(root_rechart, dict):
        raise AssertionError("root bundle shape changed")
    high_bundle = shared.high_R_path_anchored_bundle(prime=p, R=R, support=A)
    high_rechart = high_bundle["rechart"]
    if not isinstance(high_rechart, dict):
        raise AssertionError("high bundle shape changed")
    Q0 = int(root_bundle["complete_excess_bundle"]["Q"])
    beta0 = int(root_bundle["complete_excess_bundle"]["beta"])
    Q1 = int(high_bundle["complete_excess_bundle"]["Q"])
    beta1 = int(high_bundle["complete_excess_bundle"]["beta"])
    M = int(high_rechart["M"])
    C = int(high_rechart["C"])
    residue = M % p
    phase_numerator = 2 * residue - B
    phase_h = phase_numerator // p if phase_numerator % p == 0 else -1
    checks = {
        "core_prime": shared.is_prime(p) and p % 24 == 1,
        "b_parity": b % 8 == 3 and A % 4 == 3,
        "k_window": 1 <= k <= (b - 1) // 2,
        "factor_equation": recovered["N"] == u * p and e == 4 * b * k - u,
        "delta_window": 0 < delta < p - 2 * b and delta % 8 == 2,
        "canonical_high_anchor": (
            p < R < 4 * A
            and shared.canonical_chart(p, A) == (R, A * B)
            and B < p
            and B % 2 == 1
        ),
        "coprime_two_anchor_subfamily": gcd(A, R - 1) == 1,
        "root_valuation_gate": strict_odd_excess(A, s),
        "second_valuation_gate": strict_odd_excess((R - 1) // 2, s),
        "root_complete_excess": (
            Q0 == A
            and beta0 == 2
            and int(root_rechart["M"]) == A
            and int(root_rechart["R"]) == R
            and int(root_rechart["K"]) == A * B
        ),
        "second_complete_excess": Q1 == R - 1 and beta1 == 1,
        "automatic_q_two": (
            M == A * (R - 1)
            and C == 2 * A
            and 2 * A < p
            and (8 * A * A * (R - 1)) % p == 1
        ),
        "phase_range": 0 <= phase_h < 2,
        "phase_parameter_parity": B % 2 == (k + 1) % 2 and phase_h == (k + 1) % 2,
        "minimal_positive_phase": (
            phase_h == 1 and B % 2 == 1 and k % 2 == 0
        ),
    }
    if not all(checks.values()):
        raise AssertionError(f"positive b-k-u control failed: {checks}")
    return {
        "input": {"b": b, "k": k, "u": u},
        "recovered": recovered,
        "high_anchor": {"B": B, "Q0": Q0, "beta0": beta0, "Q1": Q1, "beta1": beta1},
        "automatic_q": {"M": M, "C": C, "phase_h": phase_h, "k_mod_2": k % 2},
        "checks": checks,
    }


def verify_parity_boundary() -> dict[str, object]:
    recovered = recover_from_bku(
        PARITY_BOUNDARY["b"], PARITY_BOUNDARY["k"], PARITY_BOUNDARY["u"]
    )
    p = recovered["p"]
    A = recovered["A"]
    R = recovered["R"]
    if (p, A, R) != (
        PARITY_BOUNDARY["p"],
        PARITY_BOUNDARY["A"],
        PARITY_BOUNDARY["R"],
    ):
        raise AssertionError("parity boundary reconstruction changed")
    root_bundle = shared.high_R_path_anchored_bundle(
        prime=p, R=2 * A + 1, support=1
    )
    root_rechart = root_bundle["rechart"]
    if not isinstance(root_rechart, dict):
        raise AssertionError("parity boundary root shape changed")
    Q0 = int(root_bundle["complete_excess_bundle"]["Q"])
    beta0 = int(root_bundle["complete_excess_bundle"]["beta"])
    checks = {
        "formal_bku_chart": shared.canonical_chart(p, A)[0] == R,
        "wrong_b_parity": PARITY_BOUNDARY["b"] % 8 == 7 and A % 4 == 1,
        "root_bundle_is_not_beta_two": (Q0, beta0) == (2 * A, 1),
        "root_rechart_skips_formal_A_chart": int(root_rechart["M"]) == 2 * A,
    }
    if not all(checks.values()):
        raise AssertionError(f"parity boundary changed: {checks}")
    return {"input": PARITY_BOUNDARY, "recovered": recovered, "checks": checks}


def build_result() -> dict[str, object]:
    controls = [verify_positive_control(control) for control in CONTROLS]
    boundary = verify_parity_boundary()
    return {
        "schema_version": 1,
        "certificate_type": "q2_bku_automatic_high_source_parameterization_v1",
        "scope": (
            "Exact inverse parameterization of the coprime beta_0=2 q=2 h=1 automatic "
            "high-source subfamily. It is a source-construction interface, not a "
            "terminal-free existence theorem or a global selector edge."
        ),
        "positive_controls": controls,
        "parity_boundary": boundary,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified q=2 b-k-u automatic source parameterization: 4 controls + parity boundary")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
