#!/usr/bin/env python3
"""Verify the quadratic height bound for standard Type I normal charts."""

from __future__ import annotations

import argparse
from math import gcd

from short_certificate import type_i_normal_form, type_i_normal_form_certificate, verify_certificate


def normal_chart_excess_upper_bound(prime: int, gap: int) -> int:
    """Return the necessary upper bound (p+m)^2/4 for mR-1."""
    if prime % 24 != 1 or gap % 4 != 3 or not 3 <= gap <= prime - 2:
        raise ValueError("prime and gap must be in the standard Type I range")
    if (prime + gap) % 4:
        raise AssertionError("a legal Type I chart must have integral first denominator")
    return (prime + gap) ** 2 // 4


def normal_chart_global_excess_upper_bound(prime: int) -> int:
    """Return the uniform legal-gap bound (p-1)^2 for mR-1."""
    if prime % 24 != 1:
        raise ValueError("prime must be a core prime")
    return (prime - 1) ** 2


def normal_chart_global_r_upper_bound(prime: int) -> int:
    """Return floor(((p+3)^2+4)/12), the legal-gap uniform R bound."""
    if prime % 24 != 1:
        raise ValueError("prime must be a core prime")
    return ((prime + 3) ** 2 + 4) // 12


def normal_chart_global_k_upper_bound(prime: int) -> int:
    """Return the K bound induced by the uniform standard-normal R bound."""
    return (prime * normal_chart_global_r_upper_bound(prime) + 1) // 4


def normal_form_chart_height_receipt(
    prime: int, gap: int, a: int, b: int, c: int
) -> dict[str, int]:
    """Rebuild one normal form and its exact chart-height inequalities."""
    if a <= 0 or b <= 0 or c <= 0 or gcd(a, b) != 1:
        raise ValueError("normal-form factors must be positive and A,B coprime")
    if prime != 4 * a * b * c - gap:
        raise AssertionError("normal-form target identity failed")

    numerator = 4 * b * b * c + 1
    if numerator % gap:
        raise AssertionError("normal-form R was not integral")
    r = numerator // gap
    h = a * r - b
    k = b * c * h
    chart_excess = gap * r - 1
    gap_bound = normal_chart_excess_upper_bound(prime, gap)
    global_excess_bound = normal_chart_global_excess_upper_bound(prime)
    global_r_bound = normal_chart_global_r_upper_bound(prime)
    global_k_bound = normal_chart_global_k_upper_bound(prime)
    certificate = type_i_normal_form_certificate(prime, gap, a, b)

    if not (
        h > 0
        and chart_excess == 4 * b * b * c
        and chart_excess * a == b * (prime + gap)
        and chart_excess <= gap_bound <= global_excess_bound
        and r <= global_r_bound
        and 4 * k == prime * r + 1
        and k <= global_k_bound
        and certificate is not None
        and verify_certificate(certificate)
        and type_i_normal_form(prime, gap, certificate.divisor) == (a, b, c)
    ):
        raise AssertionError("Type I normal chart height receipt changed")

    return {
        "p": prime,
        "m": gap,
        "A": a,
        "B": b,
        "C": c,
        "R": r,
        "chart_excess": chart_excess,
        "gap_bound": gap_bound,
        "global_R_bound": global_r_bound,
        "global_K_bound": global_k_bound,
    }


def verify() -> None:
    b_one = normal_form_chart_height_receipt(193, 15, 2, 1, 26)
    general_b = normal_form_chart_height_receipt(2_377, 71, 3, 2, 102)

    if not (
        b_one
        == {
            "p": 193,
            "m": 15,
            "A": 2,
            "B": 1,
            "C": 26,
            "R": 7,
            "chart_excess": 104,
            "gap_bound": 10_816,
            "global_R_bound": 3_201,
            "global_K_bound": 154_448,
        }
        and general_b
        == {
            "p": 2_377,
            "m": 71,
            "A": 3,
            "B": 2,
            "C": 102,
            "R": 23,
            "chart_excess": 1_632,
            "gap_bound": 1_498_176,
            "global_R_bound": 472_033,
            "global_K_bound": 280_505_610,
        }
    ):
        raise AssertionError("normal-chart height controls changed")
    print("verified Type I normal-chart quadratic height bounds")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused normal-chart controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
