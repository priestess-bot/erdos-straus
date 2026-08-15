#!/usr/bin/env python3
"""Verify H4 gates, Type I carrier/reset limits, and carry controls."""

from __future__ import annotations

import argparse
from math import gcd, lcm

import sympy

from short_certificate import GapCertificate, type_ii_raw_ray_certificate, verify_certificate
from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    dispatch_h3,
    h3_data,
    phase_u,
)
from type_ii_q_one_c2_19_phase_maximal_fourth_anchor_completion import complete_excess
from type_i_normal_chart_height_boundary import (
    normal_chart_global_excess_upper_bound,
    normal_chart_global_k_upper_bound,
    normal_chart_global_r_upper_bound,
)


def h4_carry_data(prime: int) -> dict[str, int | str]:
    """Rebuild H4 and expose the exact carry controlling its anchor overlap."""
    dispatch = dispatch_h3(prime)
    if dispatch["branch"] == "bounded_factor_type_ii_terminal":
        raise AssertionError("a terminal-preempted H3 state has no H4 successor")

    data = h3_data(prime)
    a = int(data["a"])
    m3 = int(data["M_3"])
    k3 = int(data["K_3"])
    r3 = int(data["R_3"])
    c3 = int(data["c_3"])
    block, beta = complete_excess(r3 - 1, k3)
    overlap = gcd(m3, block)
    if (beta * overlap) % 2:
        raise AssertionError("the maximal H3 block did not give an integral lambda")
    lambda_value = beta * overlap // 2
    multiplier = block // overlap
    m4 = lcm(m3, block)
    c4 = c3 * pow(multiplier, -1, prime) % prime
    carry_numerator = multiplier * c4 - c3
    if carry_numerator % prime:
        raise AssertionError("the canonical H4 carry was not integral")
    s4 = carry_numerator // prime
    k4 = m4 * c4
    r4 = (4 * k4 - 1) // prime
    w = (prime + 1) // 2
    h4_overlap = gcd(w, k4)
    carry_overlap = gcd(w, c3 - s4)
    capacity_delta = prime * s4 - c3 * (multiplier - 1)
    capacity_direction = "descent" if c4 < c3 else "rise" if c4 > c3 else "flat"

    if not (
        prime % 16 == 1
        and m3 % 2 == 0
        and w % 2 == 1
        and gcd(w, m3) == 1
        and block * beta == r3 - 1
        and m4 == m3 * multiplier == lcm(m3, block)
        and multiplier > 1
        and 1 <= c3 <= prime - 2
        and 1 <= c4 <= prime - 2
        and 0 <= s4 < multiplier
        and capacity_delta == multiplier * (c4 - c3)
        and prime * r4 + 1 == 4 * k4
        and gcd(prime, k4) == 1
        and h4_overlap == carry_overlap
        and gcd(r4 - 1, k4) == 2 * h4_overlap
    ):
        raise AssertionError("the H4 carry-overlap receipt changed")

    return {
        "p": prime,
        "u": phase_u(prime),
        "a": a,
        "h3_g": gcd(w, c3),
        "lambda": lambda_value,
        "h3_branch": str(dispatch["branch"]),
        "c3": c3,
        "c4": c4,
        "capacity_direction": capacity_direction,
        "s4_mod_w": s4 % w,
        "carry_residue_mod_w": (c3 - s4) % w,
        "h4_overlap": h4_overlap,
        "r4_overlap": gcd(r4 - 1, k4),
    }


def h4_overlap_terminal(prime: int) -> tuple[int, GapCertificate] | None:
    """Construct the raw Type II terminal selected by an H4 overlap factor."""
    record = h4_carry_data(prime)
    factors = sympy.factorint(int(record["h4_overlap"]))
    factor = next((value for value in sorted(factors) if value % 4 == 3), None)
    if factor is None:
        return None
    certificate = type_ii_raw_ray_certificate(prime, 1, (factor + 1) // 4, 1)
    if certificate is None or not verify_certificate(certificate):
        raise AssertionError("an H4 overlap factor did not yield its Type II terminal")
    return factor, certificate


def h4_overlap_p_plus_one_preemption(prime: int) -> tuple[int, GapCertificate] | None:
    """Rebuild the root-level p+1 Type I terminal from an H4 overlap factor."""
    record = h4_carry_data(prime)
    factors = sympy.factorint(int(record["h4_overlap"]))
    factor = next((value for value in sorted(factors) if value % 4 == 3), None)
    if factor is None:
        return None
    if ((prime + 1) // 2) % factor:
        raise AssertionError("an H4 overlap factor did not divide the p+1 carrier")
    x = (prime + factor) // 4
    certificate = GapCertificate(
        prime=prime,
        certificate_type="I",
        gap=factor,
        x=x,
        divisor=x,
        y=x * (prime + 1) // factor,
        z=prime * x * (prime + 1) // factor,
    )
    if not verify_certificate(certificate):
        raise AssertionError("the H4 factor did not yield its p+1 preemption terminal")
    return factor, certificate


def h4_type_i_height_and_carrier_reset_boundary(prime: int) -> dict[str, int | bool]:
    """Show H4 needs a carrier-discarding Type I rechart outside the current reset."""
    data = h3_data(prime)
    m3 = int(data["M_3"])
    k3 = int(data["K_3"])
    r3 = int(data["R_3"])
    c3 = int(data["c_3"])
    block, _ = complete_excess(r3 - 1, k3)
    overlap = gcd(m3, block)
    multiplier = block // overlap
    m4 = lcm(m3, block)
    c4 = c3 * pow(multiplier, -1, prime) % prime
    k4 = m4 * c4
    r4 = (4 * k4 - 1) // prime
    m0 = (prime - 1) * (2 * prime + 1) * (2 * prime * prime - 3 * prime - 1) // 8
    global_excess_bound = normal_chart_global_excess_upper_bound(prime)
    global_r_bound = normal_chart_global_r_upper_bound(prime)
    global_k_bound = normal_chart_global_k_upper_bound(prime)
    least_type_i_excess = 3 * r4 - 1
    b_p = (prime - 1) ** 2 // 4
    d4 = prime - c4
    n4 = 4 * m4 - r4

    if not (
        prime % 24 == 1
        and m3 > m0
        and 8 * m0 > prime**4
        and multiplier > 1
        and m4 == m3 * multiplier == lcm(m3, block)
        and 1 <= c4 <= prime - 2
        and k4 == m4 * c4 > m0
        and prime * r4 + 1 == 4 * k4
        and global_excess_bound == (prime - 1) ** 2
        and least_type_i_excess == 3 * r4 - 1 > global_excess_bound
        and r4 > prime * global_r_bound
        and k4 > prime * global_k_bound
        and m4 > b_p
        and m4 > global_k_bound
        and r4 > prime
        and 2 <= d4 <= prime - 1
        and n4 > 0
        and prime * n4 == 4 * m4 * d4 + 1
    ):
        raise AssertionError("the H4 Type I height/carrier-reset boundary changed")

    return {
        "p": prime,
        "minimum_type_i_excess_exceeds_global_bound": least_type_i_excess > global_excess_bound,
        "requires_R_collapse_factor_gt_p": r4 > prime * global_r_bound,
        "requires_K_collapse_factor_gt_p": k4 > prime * global_k_bound,
        "retained_H4_carrier_exceeds_type_i_K_bound": m4 > global_k_bound,
        "joined_support_reset_ineligible_above_Bp": m4 > b_p,
        "same_chart_type_i_normal_form_impossible": True,
    }


def h4_next_maximal_carry_control(prime: int) -> dict[str, int | str]:
    """Rebuild the first H4 anchor candidate and expose its carry direction.

    This is an arithmetic capacity control, not a claim that the resulting
    candidate has already passed source/path and typed-state admission.
    """
    data = h3_data(prime)
    m3 = int(data["M_3"])
    k3 = int(data["K_3"])
    r3 = int(data["R_3"])
    c3 = int(data["c_3"])
    block4, _ = complete_excess(r3 - 1, k3)
    m4 = lcm(m3, block4)
    l4 = m4 // m3
    c4 = c3 * pow(l4, -1, prime) % prime
    k4 = m4 * c4
    r4 = (4 * k4 - 1) // prime
    block5, beta5 = complete_excess(r4 - 1, k4)
    m5 = lcm(m4, block5)
    l5 = m5 // m4
    c5 = c4 * pow(l5, -1, prime) % prime
    carry_numerator = l5 * c5 - c4
    if carry_numerator % prime:
        raise AssertionError("the H4-next canonical carry was not integral")
    s5 = carry_numerator // prime
    b_p = (prime - 1) ** 2 // 4
    direction = "descent" if c5 < c4 else "rise" if c5 > c4 else "stutter"

    if not (
        prime % 24 == 1
        and m4 > b_p
        and 1 <= c4 < prime
        and prime * r4 + 1 == 4 * k4
        and block5 > 1
        and block5 * beta5 == r4 - 1
        and gcd(block5, beta5) == 1
        and k4 % beta5 == 0
        and block5 % prime
        and m5 == m4 * l5 == lcm(m4, block5)
        and l5 > 1
        and 1 <= c5 < prime
        and 0 <= s5 < l5
        and all(factor % 4 == 1 for factor in sympy.factorint((prime + 1) // 2))
        and l5 * (c5 - c4) == prime * s5 - c4 * (l5 - 1)
    ):
        raise AssertionError("the H4-next maximal carry control changed")

    return {
        "p": prime,
        "c4": c4,
        "c5": c5,
        "direction": direction,
    }


def verify() -> None:
    first = h4_carry_data(184_993)
    second = h4_carry_data(727_633)
    hard = h4_carry_data(14_449)
    rise = h4_carry_data(448_561)
    descent = h4_carry_data(665_617)
    terminal = h4_overlap_terminal(114_769)
    preemption = h4_overlap_p_plus_one_preemption(114_769)
    clean_type_i_boundary = h4_type_i_height_and_carrier_reset_boundary(184_993)
    hard_type_i_boundary = h4_type_i_height_and_carrier_reset_boundary(14_449)
    h4_next_descent = h4_next_maximal_carry_control(14_449)
    h4_next_rise = h4_next_maximal_carry_control(665_617)

    label_keys = ("u", "a", "h3_g", "lambda", "h3_branch")
    if not (
        all(first[key] == second[key] for key in label_keys)
        and first
        == {
            "p": 184_993,
            "u": 83,
            "a": 1723,
            "h3_g": 1,
            "lambda": 1,
            "h3_branch": "clean_fourth_p_anchor",
            "c3": 140_975,
            "c4": 178_654,
            "capacity_direction": "rise",
            "s4_mod_w": 48_219,
            "carry_residue_mod_w": 259,
            "h4_overlap": 1,
            "r4_overlap": 2,
        }
        and second
        == {
            "p": 727_633,
            "u": 83,
            "a": 1723,
            "h3_g": 1,
            "lambda": 1,
            "h3_branch": "clean_fourth_p_anchor",
            "c3": 554_495,
            "c4": 594_031,
            "capacity_direction": "rise",
            "s4_mod_w": 167_167,
            "carry_residue_mod_w": 23_511,
            "h4_overlap": 17,
            "r4_overlap": 34,
        }
        and hard
        == {
            "p": 14_449,
            "u": 15,
            "a": 431,
            "h3_g": 5,
            "lambda": 5,
            "h3_branch": "bounded_q_one_mask",
            "c3": 2755,
            "c4": 13_391,
            "capacity_direction": "rise",
            "s4_mod_w": 3168,
            "carry_residue_mod_w": 6812,
            "h4_overlap": 1,
            "r4_overlap": 2,
        }
        and all(rise[key] == descent[key] for key in label_keys)
        and rise["p"] == 448_561
        and rise["c3"] == 85_507
        and rise["c4"] == 423_624
        and rise["capacity_direction"] == "rise"
        and descent["p"] == 665_617
        and descent["c3"] == 126_883
        and descent["c4"] == 20_388
        and descent["capacity_direction"] == "descent"
        and terminal
        == (
            23,
            GapCertificate(
                prime=114_769,
                certificate_type="II",
                gap=4991,
                x=29_940,
                divisor=6,
                y=688_614,
                z=3_436_183_860,
            ),
        )
        and preemption
        == (
            23,
            GapCertificate(
                prime=114_769,
                certificate_type="I",
                gap=23,
                x=28_698,
                divisor=28_698,
                y=143_203_020,
                z=16_435_267_402_380,
            ),
        )
        and h4_overlap_p_plus_one_preemption(14_449) is None
        and clean_type_i_boundary
        == {
            "p": 184_993,
            "minimum_type_i_excess_exceeds_global_bound": True,
            "requires_R_collapse_factor_gt_p": True,
            "requires_K_collapse_factor_gt_p": True,
            "retained_H4_carrier_exceeds_type_i_K_bound": True,
            "joined_support_reset_ineligible_above_Bp": True,
            "same_chart_type_i_normal_form_impossible": True,
        }
        and hard_type_i_boundary
        == {
            "p": 14_449,
            "minimum_type_i_excess_exceeds_global_bound": True,
            "requires_R_collapse_factor_gt_p": True,
            "requires_K_collapse_factor_gt_p": True,
            "retained_H4_carrier_exceeds_type_i_K_bound": True,
            "joined_support_reset_ineligible_above_Bp": True,
            "same_chart_type_i_normal_form_impossible": True,
        }
        and h4_next_descent
        == {
            "p": 14_449,
            "c4": 13_391,
            "c5": 12_552,
            "direction": "descent",
        }
        and h4_next_rise
        == {
            "p": 665_617,
            "c4": 20_388,
            "c5": 94_177,
            "direction": "rise",
        }
    ):
        raise AssertionError("the H4 carry-overlap boundary controls changed")
    print("verified H4 gates, Type I carrier/reset limits, carry controls, and label boundaries")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact H4 carry receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
