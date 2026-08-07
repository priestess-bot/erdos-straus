#!/usr/bin/env python3
"""Verify the generalized q-block C=19^2 conditional raw/reset ray."""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_high_r_chart_two_anchor as shared


P0 = 181_740_263_041
P_STEP = 204_127_330_680
R0 = 787_541_139_831
R_STEP = 884_551_766_280
H0 = 7_572_510_960
H_STEP = 8_505_305_445
Q = 5
C = 361
B = 11_246
A = 386
FIRST_PERIOD = 1_085_239
FULL_PERIOD = 20_619_541
FIRST_ROOT = 1_085_244
RHO = 747


def affine(value0: int, step: int, v: int) -> int:
    """Evaluate one of the fixed affine rays."""
    return value0 + step * v


def linear_root(constant: int, slope: int, modulus: int) -> tuple[int, int]:
    """Solve one affine congruence, returning its root and reduced period."""
    divisor = gcd(slope, modulus)
    if constant % divisor:
        raise AssertionError("affine congruence has no solution")
    reduced_modulus = modulus // divisor
    root = (-constant // divisor * pow(slope // divisor, -1, reduced_modulus)) % reduced_modulus
    return root, reduced_modulus


def verify_q_block_congruences() -> dict[str, object]:
    """Derive the three exact divisibility conditions without a range scan."""
    first = linear_root(R0 - 1, R_STEP, Q * B)
    second = linear_root(4 * R0 + B, 4 * R_STEP, Q * A)
    third = linear_root(R0 - A, R_STEP, Q * C)
    if not (
        first == (5, 5_623)
        and second == (5, 193)
        and third == (2, 19)
        and FIRST_PERIOD == first[1] * second[1]
        and gcd(first[1], second[1]) == 1
        and FULL_PERIOD == FIRST_PERIOD * third[1]
        and FIRST_ROOT % FIRST_PERIOD == 5
        and FIRST_ROOT % third[1] == 2
    ):
        raise AssertionError("C=19^2 q-block CRT changed")
    return {
        "q": Q,
        "c": C,
        "roots": {
            "R_minus_one": list(first),
            "four_R_plus_b": list(second),
            "R_minus_a": list(third),
        },
        "combined_progression": [FIRST_ROOT, FULL_PERIOD],
    }


def verify_c361_candidate() -> dict[str, object]:
    """Verify the arithmetic candidate, keeping raw admission conditional."""
    v = FIRST_ROOT
    p = affine(P0, P_STEP, v)
    R = affine(R0, R_STEP, v)
    h = affine(H0, H_STEP, v)
    M = 26 * h + 1
    C0 = p - 3
    K = M * C0
    Q1 = (R - 1) // (Q * B)
    Q2 = ((Q - 1) * R + B) // (Q * A)
    Q3 = (R - A) // (Q * C)
    p_step = P_STEP * FULL_PERIOD
    if not (
        h % C == 160
        and K % C == 0
        and K % Q != 0
        and R - 1 == Q * B * Q1
        and (Q - 1) * R + B == Q * A * Q2
        and R - A == Q * C * Q3
        and (RHO * p + 1) % (4 * C) == 0
        and shared.canonical_chart(p, C) == (RHO, (RHO * p + 1) // 4)
        and p
        == 2_579 * 282_413 * 304_153_543
        and gcd(p, p_step) == 1
    ):
        raise AssertionError("C=19^2 candidate arithmetic changed")
    return {
        "parameter": {"v": v, "period": FULL_PERIOD, "h_mod_361": h % C},
        "chart": {"p": p, "R": R, "K_divisible_by_361": True},
        "q_blocks": {"b": B, "a": A, "Q1": Q1, "Q2": Q2, "Q3": Q3},
        "fixed_c_reset": {"rho": RHO, "K": (RHO * p + 1) // 4},
        "prime_status": "base_parameter_composite; progression_is_primitive",
        "raw_admission": (
            "conditional on p primality and all factor-reserve/R-unit checks for Q1,Q2,Q3"
        ),
    }


def build_result() -> dict[str, object]:
    """Build the conditional C=19^2 construction, not a selector edge."""
    return {
        "certificate_type": "c3_core19_generalized_q_block_fixed_c_v1",
        "q_block_congruences": verify_q_block_congruences(),
        "c361_candidate": verify_c361_candidate(),
        "selector_status": "conditional_raw_family_no_registered_edge",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified generalized q-block C=19^2 conditional reset ray")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
