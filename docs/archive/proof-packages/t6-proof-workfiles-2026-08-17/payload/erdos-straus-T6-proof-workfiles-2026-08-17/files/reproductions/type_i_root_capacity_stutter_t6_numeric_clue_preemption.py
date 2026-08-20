#!/usr/bin/env python3
"""Audit the T6-V1 proper-root numeric clue and its gap-3 preemption."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import isqrt

P = 20_065_847_377
M = 6_768
A = 141
EXPECTED_K = 3


def is_prime_64(value: int) -> bool:
    """Deterministic Miller--Rabin for unsigned 64-bit integers."""
    if value < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return value == prime

    odd_part = value - 1
    exponent = 0
    while odd_part % 2 == 0:
        exponent += 1
        odd_part //= 2

    for base in (2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022):
        if base % value == 0:
            continue
        residue = pow(base, odd_part, value)
        if residue in (1, value - 1):
            continue
        for _ in range(exponent - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def verify() -> None:
    if P % 24 != 1 or not is_prime_64(P):
        raise AssertionError("the recorded p stopped being a core prime")

    layer = A * M
    shift = M - A
    linear = 3 * (A - 1)
    discriminant = linear * linear - 36 * (shift - layer * P)
    square_root = isqrt(discriminant)
    if square_root * square_root != discriminant:
        raise AssertionError("the root-gate discriminant stopped being square")

    numerator = -linear + square_root
    if numerator <= 0 or numerator % 18:
        raise AssertionError("the unique positive root stopped being integral")
    u_value = numerator // 18
    if 9 * u_value * u_value + linear * u_value + shift != layer * P:
        raise AssertionError("the reconstructed root no longer solves the pair gate")

    h_value = 3 * u_value
    if (A + h_value) % M:
        raise AssertionError("the reconstructed e stopped being integral")
    e_value = (A + h_value) // M
    d_value = M * P + 1 - h_value
    norm = A * A - A * (e_value - 1) + (e_value - 1) ** 2

    if (u_value, h_value, e_value, d_value) != (
        46_126_129,
        138_378_387,
        20_446,
        135_805_516_669_150,
    ):
        raise AssertionError("the forced stutter reconstruction changed")
    if not (
        e_value * d_value == P * h_value + 1
        and A == e_value * M - h_value
        and norm == EXPECTED_K * h_value
    ):
        raise AssertionError("the abstract quotient identities changed")

    cyclotomic = P * P + P + 1
    quotient, remainder = divmod(cyclotomic, h_value)
    if (quotient, remainder) != (2_909_690_159_758, 39_277_161):
        raise AssertionError("the exact cyclotomic division changed")
    if remainder == 0:
        raise AssertionError("the clue unexpectedly acquired actual root provenance")

    gap = 3
    x_value = (P + gap) // 4
    divisor = 5
    if not (
        x_value == 5_016_461_845
        and x_value % divisor == 0
        and divisor <= x_value
        and (x_value + divisor) % gap == 0
    ):
        raise AssertionError("the gap-3 Type II certificate changed")

    y_value = P * (x_value + divisor) // gap
    z_value = P * (x_value + x_value * x_value // divisor) // gap
    if (y_value, z_value) != (
        33_553_185_951_547_689_150,
        33_663_655_420_825_800_263_779_096_350,
    ):
        raise AssertionError("the recovered denominators changed")
    if Fraction(1, x_value) + Fraction(1, y_value) + Fraction(1, z_value) != Fraction(4, P):
        raise AssertionError("the terminal Egyptian-fraction identity failed")

    print("verified T6 numeric clue provenance failure and gap-3 terminal preemption")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
