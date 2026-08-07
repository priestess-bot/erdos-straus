#!/usr/bin/env python3
"""Verify a symbolic adaptive c=3 core-19 ambient-character substrate.

The arithmetic progression inherits an established factor-block raw receipt at
every prime point.  It has h=8 mod 19, an ambient order-19 character through
191|R, and avoids the fixed gap-seven leaves.  A finite divisor check excludes
only Type II terminals with one fixed (m, d) over the entire progression.
No F quotient, terminal-free assertion, or selector edge is claimed.
"""

from __future__ import annotations

import argparse
from math import gcd

import type_i_high_r_chart_two_anchor as shared


S0 = 3231
S_STEP = 3629
U0 = 216357456
U_STEP = 243008727
H0 = 7572510960
H_STEP = 8505305445
P0 = 181740263041
P_STEP = 204127330680
R0 = 787541139831
R_STEP = 884551766280


def divisors(value: int) -> list[int]:
    """Enumerate divisors of one explicitly factored finite integer."""
    result = [1]
    for prime, exponent in shared.factorization(value):
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return sorted(result)


def verify_substrate_parameters() -> dict[str, object]:
    """Verify the CRT intersection with the established adaptive raw family."""
    if not (
        S_STEP == 19 * 191
        and U0 == 3 + 66963 * S0
        and U_STEP == 66963 * S_STEP
        and H0 == 35 * U0
        and H_STEP == 35 * U_STEP
        and P0 == 840 * U0 + 1
        and P_STEP == 840 * U_STEP
        and R0 == 104 * H0 - 9
        and R_STEP == 104 * H_STEP
        and gcd(P0, P_STEP) == 1
        and H0 % 19 == 8
        and H_STEP % 19 == 0
        and P0 % 7 == 1
        and P_STEP % 7 == 0
        and R0 % 191 == 0
        and R_STEP % 191 == 0
    ):
        raise AssertionError("adaptive core-19 CRT parameterization changed")

    # These are exactly the residue exclusions required by the existing
    # adaptive factor-block raw-source theorem.
    excluded_residues = ((3, 1), (13, 10), (17, 10), (101, 100))
    for modulus, forbidden in excluded_residues:
        if U0 % modulus == forbidden or U_STEP % modulus:
            raise AssertionError("adaptive raw-source reserve condition changed")
    if not shared.is_prime(191) or 191 % 19 != 1:
        raise AssertionError("ambient q=19 conductor changed")
    if shared.factorization(P0) != [(23, 1), (149, 1), (53031883, 1)]:
        raise AssertionError("candidate base factorization changed")
    return {
        "adaptive_parameter": {"s0": S0, "s_step": S_STEP, "u0": U0, "u_step": U_STEP},
        "h": {"base": H0, "step": H_STEP},
        "p": {"base": P0, "step": P_STEP, "gcd": gcd(P0, P_STEP)},
        "R": {"base": R0, "step": R_STEP},
        "raw_source_scope": "actual_factor_block_receipt_at_every_prime_parameter",
        "ambient_q19_character": "available_via_U(191)_order_190",
        "gap_seven_fixed_leaves": "avoided_by_p_equiv_1_mod_7",
    }


def verify_fixed_pair_screen() -> dict[str, int]:
    """Exclude all fixed (m, d) Type II templates on the whole affine ray."""
    if P_STEP % 4:
        raise AssertionError("fixed-pair screen requires an integral affine x slope")
    expected_factorization = [
        (2, 3),
        (3, 2),
        (5, 1),
        (7, 1),
        (13, 1),
        (17, 1),
        (19, 1),
        (101, 1),
        (191, 1),
    ]
    if shared.factorization(P_STEP) != expected_factorization:
        raise AssertionError("adaptive ray step factorization changed")

    all_divisors = divisors(P_STEP)
    gaps = [gap for gap in all_divisors if gap % 4 == 3]
    candidate_divisors = 0
    hits: list[tuple[int, int]] = []
    slope = P_STEP // 4
    for gap in gaps:
        x0 = (P0 + gap) // 4
        E = gcd(x0, slope)
        for divisor in divisors(E * E):
            candidate_divisors += 1
            if divisor <= x0 and (P0 + 4 * divisor) % gap == 0:
                hits.append((gap, divisor))
    if len(all_divisors) != 1536 or len(gaps) != 192 or candidate_divisors != 976 or hits:
        raise AssertionError("adaptive fixed Type II pair screen changed")
    return {
        "all_step_divisors": len(all_divisors),
        "gaps_congruent_three_mod_four": len(gaps),
        "candidate_d_dividing_E_squared": candidate_divisors,
        "fixed_pair_hits": len(hits),
    }


def build_result() -> dict[str, object]:
    """Build the candidate substrate and its deliberately limited terminal screen."""
    return {
        "certificate_type": "c3_adaptive_core19_ambient19_terminal_screen_v1",
        "scope": (
            "A prime-conditional actual raw-source substrate with only an ambient q=19 "
            "character. The finite screen excludes fixed (m,d) templates on the whole "
            "ray, not parameter-dependent terminals or selector obligations."
        ),
        "parameters": verify_substrate_parameters(),
        "fixed_type_ii_pair_screen": verify_fixed_pair_screen(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified adaptive c=3 core-19 ambient-q19 terminal screen")


if __name__ == "__main__":
    main()
