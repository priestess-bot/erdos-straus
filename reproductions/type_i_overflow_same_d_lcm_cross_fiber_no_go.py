#!/usr/bin/env python3
"""Verify the overflow same-d lcm cross-fiber hard gate."""

from __future__ import annotations

import argparse
from math import gcd


P = 73
D = 1
R_D = 18
B_P = (P - 1) ** 2 // 4
ROWS = ((1332, 73), (2646, 145), (675, 37))


def lcm(left: int, right: int) -> int:
    return left * right // gcd(left, right)


def determinant_parameter(carrier: int) -> int:
    return (-pow((4 * carrier) % P, -1, P)) % P


def verify() -> None:
    if P % 24 != 1 or not (0 < D < P):
        raise AssertionError("core parameters changed")
    if (-pow((4 * D) % P, -1, P)) % P != R_D:
        raise AssertionError("fixed-d residue changed")

    for carrier, n_value in ROWS:
        if P * n_value != 4 * D * carrier + 1:
            raise AssertionError("overflow determinant row changed")
        if carrier % P != R_D:
            raise AssertionError("overflow residue changed")
        if 4 * carrier - n_value <= P:
            raise AssertionError("row is no longer overflow")

    same_left, same_right = ROWS[0][0], ROWS[1][0]
    same_gcd = gcd(same_left, same_right)
    same_lcm = lcm(same_left, same_right)
    if same_gcd != R_D or same_gcd % P != R_D:
        raise AssertionError("same-d gcd control changed")
    if same_lcm != 195804 or same_lcm <= B_P:
        raise AssertionError("same-d lcm high-carrier control changed")
    if determinant_parameter(same_lcm) != D:
        raise AssertionError("same-d lcm determinant changed")

    reset_left, reset_right = ROWS[2][0], ROWS[1][0]
    reset_gcd = gcd(reset_left, reset_right)
    reset_lcm = lcm(reset_left, reset_right)
    if reset_gcd != 27 or reset_gcd % P == R_D:
        raise AssertionError("cross-fiber gcd control changed")
    if reset_lcm != 66150 or determinant_parameter(reset_lcm) != 38:
        raise AssertionError("determinant reset control changed")
    if determinant_parameter(reset_lcm) == D:
        raise AssertionError("old determinant was incorrectly reused")

    # The general hard gate: same-d gcd residue implies lcm leaves the normal domain.
    threshold = (P + 1) * (P * P + 1) / (4 * (P - D))
    if same_lcm <= threshold or threshold <= B_P:
        raise AssertionError("strict same-d lcm bound changed")

    print(
        "verified overflow lcm gate: same-d lcm > B_p; "
        "different gcd residue forces determinant reset"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
