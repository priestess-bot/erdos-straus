#!/usr/bin/env python3
"""Verify focused d=1 q0=1 second-reentry capacity-map controls.

The p=73 rows are static normal-form controls.  They verify the integer
capacity and q-lock identities only; they do not assert an actual H4
predecessor or that the selected E_zeta is an actual maximal block.
"""

from __future__ import annotations

import argparse
from math import gcd


P = 73
Q = 37
M4 = 1
B0 = 10_799_471_865
T = (P * B0 - 1) // 2
U_T = T // Q
N0 = (P + 1) * B0 - 1
M_ALT = (P * N0 - 1) // 4
L0 = M_ALT // M4
RHO = 1
QHAT = Q
SMALL_T = 1
F = Q * RHO + P * SMALL_T
E_X2 = QHAT * F


def p_adic_digit(value: int, p: int) -> tuple[int, int]:
    """Return v_p(value-1) and its first nonzero p-adic digit."""
    shifted = value - 1
    valuation = 0
    while shifted % p == 0:
        shifted //= p
        valuation += 1
    return valuation, shifted % p


def is_unitary_divisor(divisor: int, value: int) -> bool:
    return divisor > 0 and value % divisor == 0 and gcd(divisor, value // divisor) == 1


def capacity_row(e_zeta: int) -> tuple[int, int, int]:
    product = F * e_zeta
    sigma = (product - L0) // P
    n_re = N0 + 4 * M4 * sigma
    a_re = Q // gcd(Q, sigma)
    if not (
        product > 0
        and (product - L0) % P == 0
        and 4 * M4 * product + 1 == P * n_re
        and n_re > 0
        and n_re % 4 == 1
        and a_re == Q // gcd(Q, sigma)
    ):
        raise AssertionError("second-reentry capacity row changed")
    return sigma, n_re, a_re


def verify_base_normal_form() -> None:
    if not (
        P % 24 == 1
        and P == 2 * Q - 1
        and gcd(Q, M4) == 1
        and B0 % 2 == 1
        and (B0 + 1) % Q == 0
        and 2 * T == P * B0 - 1
        and T == Q * U_T
        and M_ALT == Q * T
        and L0 == Q * Q * U_T
        and L0 % (Q * Q) == 0
        and N0 % 4 == 1
        and M_ALT == (P * N0 - 1) // 4
        and E_X2 == Q * Q + P * Q
        and E_X2 == QHAT * F
    ):
        raise AssertionError("q0=1 d=1 skeleton changed")


def verify_non_lock_handoff() -> None:
    e_zeta = 109
    sigma, _n_re, a_re = capacity_row(e_zeta)
    if not (
        gcd(F, e_zeta) == 1
        and (F * e_zeta) % P == L0 % P
        and sigma % Q == (SMALL_T * e_zeta) % Q == 35
        and a_re == Q
    ):
        raise AssertionError("non-lock a>1 handoff control changed")


def verify_unitary_q_lock_controls() -> None:
    # A composite-q allocation has complete prime-power ownership on each side.
    composite_q = 45
    composite_t = 5
    composite_e = 9
    composite_lambda = gcd(composite_q, composite_t)
    if not (
        composite_q % composite_lambda == 0
        and is_unitary_divisor(composite_lambda, composite_q)
        and composite_q % (composite_t * composite_e) == 0
        and (composite_q // composite_lambda) % composite_e == 0
        and gcd(composite_t, composite_e) == 1
    ):
        raise AssertionError("composite unitary q-lock allocation changed")

    # These p=73 controls use lambda=1: all q-capacity belongs to E_zeta.
    for root_multiplier, expected_r, expected_u, residual in (
        (2, 223, 1, False),
        (2022, 222_423, 1_801, True),
    ):
        lift_index = 1 + P * root_multiplier
        e_zeta = Q * (72 + P * lift_index)
        sigma, _n_re, a_re = capacity_row(e_zeta)
        v_value = sigma // Q
        b_re = B0 + 2 * M4 * v_value
        ordinary_multiplier = (P - 1) * b_re - 1
        eta, omega = p_adic_digit(ordinary_multiplier, P)
        r_value = (b_re + 1) // (2 * P)
        root_modulus = (P * P + P + 1) // 3
        u_value = gcd(2 * r_value + 1, root_modulus)
        lambda_value = gcd(Q, SMALL_T)

        if not (
            gcd(F, e_zeta) == 1
            and sigma % Q == 0
            and a_re == 1
            and is_unitary_divisor(lambda_value, Q)
            and e_zeta % (Q // lambda_value) == 0
            and b_re > 0
            and b_re % P == P - 1
            and eta == 0
            and omega == P - 1
            and (b_re + 1) % (2 * P) == 0
            and r_value == expected_r
            and u_value == expected_u
            and (9 * u_value * u_value >= P) == residual
        ):
            raise AssertionError("q-lock root-fan control changed")


def verify() -> None:
    verify_base_normal_form()
    verify_non_lock_handoff()
    verify_unitary_q_lock_controls()
    print("verified q0=1 d=1 p-free second-reentry capacity map")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
