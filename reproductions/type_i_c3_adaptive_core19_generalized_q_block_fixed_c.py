#!/usr/bin/env python3
"""Verify the generalized q-block C=19^2 reserve-stable raw/reset ray."""

from __future__ import annotations

import argparse
import json
from math import gcd, prod

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
RESERVE_PRIMES = (2, 3, 7, 13, 17, 19, 29, 61, 101, 167, 191, 193, 5623)
RESERVE_PERIOD = 1_090_735_887_676_059_709_266


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


def factor_product(factors: tuple[tuple[int, int], ...]) -> int:
    """Materialize one small declared factorization exactly."""
    return prod(prime**exponent for prime, exponent in factors)


def verify_c361_reserve_stable_subray() -> dict[str, object]:
    """Close every Q_i reserve and R-unit gate on one CRT subray."""
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
    M_step = 26 * H_STEP * FULL_PERIOD
    R_step = R_STEP * FULL_PERIOD
    Q_steps = (
        R_step // (Q * B),
        (Q - 1) * R_step // (Q * A),
        R_step // (Q * C),
    )
    determinant_factors = (
        (
            ((2, 1), (3, 1), (7, 2), (13, 2), (17, 1), (19, 2), (101, 1), (191, 1), (193, 1)),
            ((2, 4), (3, 1), (7, 1), (13, 1), (17, 1), (19, 2), (101, 1), (191, 1), (193, 1)),
        ),
        (
            ((2, 1), (3, 1), (7, 1), (13, 2), (17, 1), (19, 2), (29, 1), (101, 1), (191, 1), (193, 1), (5623, 1)),
            ((2, 3), (3, 1), (7, 1), (13, 1), (17, 1), (19, 2), (101, 2), (167, 1), (191, 1), (5623, 1)),
        ),
        (
            ((2, 1), (3, 2), (7, 2), (13, 2), (17, 1), (19, 1), (101, 1), (191, 1), (193, 1), (5623, 1)),
            ((2, 3), (3, 1), (7, 1), (13, 1), (17, 1), (19, 1), (61, 1), (101, 1), (191, 1), (193, 1), (5623, 1)),
        ),
    )
    Q_bases = (Q1, Q2, Q3)
    M_x_bases = (M, C0)
    M_x_steps = (M_step, p_step)
    determinants = []
    for index, (Q_base, Q_step) in enumerate(zip(Q_bases, Q_steps)):
        row = []
        for column, (base, step) in enumerate(zip(M_x_bases, M_x_steps)):
            determinant = Q_base * step - Q_step * base
            if abs(determinant) != factor_product(determinant_factors[index][column]):
                raise AssertionError("C=19^2 determinant factorization changed")
            row.append(determinant)
        determinants.append(row)
    if not (
        h % C == 160
        and K % C == 0
        and K % Q != 0
        and M % C == 190
        and C0 % C == 228
        and M_step * RESERVE_PERIOD % C == 0
        and p_step * RESERVE_PERIOD % C == 0
        and R - 1 == Q * B * Q1
        and (Q - 1) * R + B == Q * A * Q2
        and R - A == Q * C * Q3
        and R_step == Q * B * Q_steps[0]
        and (Q - 1) * R_step == Q * A * Q_steps[1]
        and R_step == Q * C * Q_steps[2]
        and (RHO * p + 1) % (4 * C) == 0
        and RHO * p_step * RESERVE_PERIOD % (4 * C) == 0
        and shared.canonical_chart(p, C) == (RHO, (RHO * p + 1) // 4)
        and p
        == 2_579 * 282_413 * 304_153_543
        and RESERVE_PERIOD == prod(RESERVE_PRIMES)
        and all(Q_base % prime != 0 for Q_base in Q_bases for prime in RESERVE_PRIMES)
        and all(Q_step * RESERVE_PERIOD % prime == 0 for Q_step in Q_steps for prime in RESERVE_PRIMES)
        and R_step * RESERVE_PERIOD % Q == 0
        and M_step * RESERVE_PERIOD % Q == 0
        and p_step * RESERVE_PERIOD % Q == 0
        and R % Q == 1
        and K % Q != 0
        and gcd(Q1, R) == 1
        and gcd(Q2, R) == 1
        and gcd(Q3, R) == 1
        and gcd(p, p_step * RESERVE_PERIOD) == 1
    ):
        raise AssertionError("C=19^2 reserve-stable arithmetic changed")

    # A common Q_i/M or Q_i/(p-3) prime divides the corresponding determinant.
    # The period freezes all Q_i away from every possible determinant prime.
    if any(
        set(prime for factors in row for prime, _exponent in factors) - set(RESERVE_PRIMES)
        for row in determinant_factors
    ):
        raise AssertionError("reserve prime set no longer contains every determinant prime")
    return {
        "parameter": {
            "v": v,
            "period": FULL_PERIOD,
            "reserve_multiplier": RESERVE_PERIOD,
            "h_mod_361": h % C,
        },
        "chart": {"p": p, "R": R, "K_divisible_by_361": True},
        "q_blocks": {"b": B, "a": A, "Q1": Q1, "Q2": Q2, "Q3": Q3},
        "fixed_c_reset": {"rho": RHO, "K": (RHO * p + 1) // 4},
        "all_t_invariants": {
            "q_block_identities": "each of the three affine identities holds on z=reserve_multiplier*t",
            "C_divides_K": True,
            "q_is_a_KR_unit": True,
            "rho_reset_congruence": "747*p(t) == -1 mod 1444",
        },
        "determinants": determinants,
        "reserve_gate": {
            "gcd_Q_product_with_K": "one for every z = reserve_multiplier*t",
            "R_units": (
                "Q1 divides R-1; Q2 cannot share R outside b=2*5623; "
                "Q3 cannot share R outside a=2*193"
            ),
        },
        "prime_status": "base_parameter_composite; reserve-stable progression_is_primitive",
        "raw_admission": (
            "Every prime p on v = 1085244 + 20619541*1090735887676059709266*t "
            "has an actual primitive C=361 raw receipt and the fixed R=747 reset."
        ),
    }


def build_result() -> dict[str, object]:
    """Build the reserve-stable C=19^2 construction, not a selector edge."""
    return {
        "certificate_type": "c3_core19_generalized_q_block_fixed_c_v1",
        "q_block_congruences": verify_q_block_congruences(),
        "c361_reserve_stable_subray": verify_c361_reserve_stable_subray(),
        "selector_status": "actual_raw_family_when_prime_no_registered_edge",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified generalized q-block C=19^2 reserve-stable reset ray")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
