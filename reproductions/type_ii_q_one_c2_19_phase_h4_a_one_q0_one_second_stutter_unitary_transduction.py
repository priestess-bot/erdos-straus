#!/usr/bin/env python3
"""Verify focused signed second-stutter unitary-carrier controls.

The p=73 rows reuse the local H4 arithmetic skeleton from the q0=1 double-q
bridge.  Their E=q**2+p*s values are synthetic top-capacity support values,
not asserted complete-excess blocks of an actual H4 endpoint.  The remaining
small rows only exercise the unitary-divisor dichotomy algebraically.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Case:
    signed_s: int
    expected_e: int
    expected_n: int
    expected_a: int
    expected_b: int | None


P = 73
Q = 37
D4 = 1
B = 10_799_471_865
T = (P * B - 1) // 2
U = T // Q
RHO = gcd(Q, 2 * U)
QHAT = Q // RHO
M2_BASE = D4 * U
M_ALT = Q * Q * M2_BASE
N_ALT = (4 * M_ALT + 1) // P

CASES = (
    Case(0, 1_369, 799_160_918_009, 1, 10_799_471_865),
    Case(1, 1_442, 841_775_050_233, 37, None),
    Case(37, 4_070, 2_375_883_810_297, 1, 32_106_537_977),
    Case(-1, 1_296, 756_546_785_785, 37, None),
)


def a_coordinate(q: int, u: int, signed_s: int) -> int:
    rho = gcd(q, 2 * u)
    qhat = q // rho
    return qhat // gcd(qhat, signed_s)


def verify_fixture() -> None:
    if not (
        P % 24 == 1
        and (P + 1) // 2 == Q * D4
        and B % 2 == 1
        and 2 * T == P * B - 1
        and T == Q * U
        and RHO == 1
        and QHAT == Q
        and M_ALT == (P * N_ALT - 1) // 4
        and N_ALT % 4 == 1
    ):
        raise AssertionError("p=73 second-stutter skeleton changed")

    for case in CASES:
        e_value = Q * Q + P * case.signed_s
        support = M2_BASE * e_value
        n_value = (4 * support + 1) // P
        a_value = a_coordinate(Q, U, case.signed_s)

        if not (
            e_value == case.expected_e
            and support > 0
            and 4 * support + 1 == P * n_value
            and n_value == case.expected_n
            and n_value % 4 == 1
            and pow((4 * support) % P, -1, P) == P - 1
            and a_value == case.expected_a
            and a_value == QHAT // gcd(QHAT, case.signed_s)
        ):
            raise AssertionError(f"signed second-stutter case {case.signed_s} changed")

        if case.expected_b is not None:
            t_value = case.signed_s // QHAT
            b_value = (n_value + 1) // (P + 1)
            b_formula = B + (2 * U // RHO) * t_value
            if not (
                case.signed_s % QHAT == 0
                and QHAT * t_value == case.signed_s
                and b_value == b_formula == case.expected_b
                and (Q * RHO * (2 * U // RHO)) % P == (P * B - 1) % P
                and b_value % P == (B - pow(Q * RHO, -1, P) * t_value) % P
            ):
                raise AssertionError(f"a=1 residue map {case.signed_s} changed")


def verify_unitary_dichotomy() -> None:
    # A proper unitary allocation: rho belongs to y2 and qhat to x2.
    q_value = 45
    u_value = 5
    rho = gcd(q_value, 2 * u_value)
    qhat = q_value // rho
    signed_s = qhat
    if not (
        rho == 5
        and qhat == 9
        and gcd(rho, qhat) == 1
        and a_coordinate(q_value, u_value, signed_s) == 1
        and qhat % 2 == 1
    ):
        raise AssertionError("proper unitary carrier control changed")

    # If rho and qhat overlap, primitive x2,y2 cannot carry them separately.
    q_value = 9
    u_value = 3
    rho = gcd(q_value, 2 * u_value)
    qhat = q_value // rho
    signed_s = qhat
    if not (
        rho == qhat == 3
        and gcd(rho, qhat) > 1
        and a_coordinate(q_value, u_value, signed_s) == 1
    ):
        raise AssertionError("non-unitary obstruction control changed")

    # rho=q means q divides U, hence the third raw q carrier is available.
    q_value = 37
    u_value = 37
    rho = gcd(q_value, 2 * u_value)
    qhat = q_value // rho
    m_alt = q_value * q_value * u_value
    if not (
        rho == q_value
        and qhat == 1
        and m_alt % (q_value**3) == 0
        and a_coordinate(q_value, u_value, 0) == 1
    ):
        raise AssertionError("third q-carrier control changed")


def verify() -> None:
    verify_fixture()
    verify_unitary_dichotomy()
    print("verified signed second-stutter unitary carrier transduction")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused transduction controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
