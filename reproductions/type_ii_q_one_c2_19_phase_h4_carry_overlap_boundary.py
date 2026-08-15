#!/usr/bin/env python3
"""Verify the H4 carry-overlap identity and its finite-label boundary."""

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
        "c4": c4,
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


def verify() -> None:
    first = h4_carry_data(184_993)
    second = h4_carry_data(727_633)
    hard = h4_carry_data(14_449)
    terminal = h4_overlap_terminal(114_769)

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
            "c4": 178_654,
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
            "c4": 594_031,
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
            "c4": 13_391,
            "s4_mod_w": 3168,
            "carry_residue_mod_w": 6812,
            "h4_overlap": 1,
            "r4_overlap": 2,
        }
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
    ):
        raise AssertionError("the H4 carry-overlap boundary controls changed")
    print("verified H4 carry-overlap identity, terminal gate, and finite-label boundary")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact H4 carry receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
