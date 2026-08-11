#!/usr/bin/env python3
"""Verify the exact common-witness criterion for comparable external sources.

For k | l = k*s | (p-1)/4, the complete square-factor menus satisfy

    E_k intersection E_l
      = {e | (k*g)^2 : e <= M_k and lcm(q_k, q_l) | 4e+1},

where g=gcd(n_k,s-1), q_j=4j-1, n_j=p-(p-1)/(4j), and M_j=j*n_j.
This is an exact arithmetic identity, not a claim that all menu pairs are
disjoint. The controls include one pair where the simple range gate is
decisive and one where it fails but the exact candidate set remains empty.
"""

from __future__ import annotations

import argparse
import json
import math

import short_certificate


def source_menu(p: int, k: int, spf: list[int]) -> set[int]:
    """Return the complete zero-shift square-factor menu at one scale."""
    base = (p - 1) // 4
    if p % 24 != 1 or k < 1 or base % k:
        raise ValueError("require p == 1 (mod 24) and k | (p-1)/4")
    q = 4 * k - 1
    n = p - base // k
    preserved = k * n
    if 4 * preserved != q * p + 1 or preserved % q != k % q:
        raise AssertionError("source normalization failed")
    return {
        e
        for e in short_certificate.positive_divisors_square_product_from_spf(
            k, n, spf
        )
        if e <= preserved and (4 * e + 1) % q == 0
    }


def collision_state(p: int, k: int, l: int, spf: list[int]) -> dict[str, object]:
    """Compute both sides of the exact collision formula."""
    base = (p - 1) // 4
    if p % 24 != 1 or not (0 < k < l and base % k == base % l == 0):
        raise ValueError("require comparable proper divisors k | l | (p-1)/4")
    if l % k:
        raise ValueError("require k | l")

    s = l // k
    q_k, q_l = 4 * k - 1, 4 * l - 1
    n_k, n_l = p - base // k, p - base // l
    M_k, M_l = k * n_k, l * n_l
    g = math.gcd(n_k, s - 1)
    shared = k * g
    modulus = math.lcm(q_k, q_l)

    if math.gcd(M_k, M_l) != shared:
        raise AssertionError("chain gcd formula failed")
    if M_l <= M_k:
        raise AssertionError("larger scale must have larger preserved denominator")

    left = source_menu(p, k, spf) & source_menu(p, l, spf)
    right = {
        e
        for e in short_certificate.positive_divisors_square_product_from_spf(
            shared, 1, spf
        )
        if e <= M_k and (4 * e + 1) % modulus == 0
    }
    if left != right:
        raise AssertionError("exact common-witness formula failed")

    range_bound = 4 * shared * shared + 1
    range_gate = range_bound < modulus
    if range_gate and left:
        raise AssertionError("strict range gate must rule out all collisions")

    return {
        "prime": p,
        "k": k,
        "l": l,
        "s": s,
        "n_k": n_k,
        "n_l": n_l,
        "M_k": M_k,
        "M_l": M_l,
        "g": g,
        "shared_gcd": shared,
        "lcm_modulus": modulus,
        "range_bound": range_bound,
        "range_gate": range_gate,
        "left_menu_intersection": sorted(left),
        "right_collision_candidates": sorted(right),
    }


def verify() -> dict[str, object]:
    """Run focused controls for the formula and its two distinct outcomes."""
    controls = (
        (193, 1, 2, True),
        (409, 2, 6, True),
        (97, 2, 12, False),
        (193, 1, 6, False),
    )
    limit = max(p for p, _, _, _ in controls)
    spf = short_certificate.smallest_prime_factors(limit)
    records = []
    for p, k, l, expected_gate in controls:
        record = collision_state(p, k, l, spf)
        if bool(record["range_gate"]) != expected_gate:
            raise AssertionError("control did not exercise its intended gate state")
        if record["left_menu_intersection"] or record["right_collision_candidates"]:
            raise AssertionError("focused control unexpectedly has a common witness")
        records.append(record)
    return {
        "arithmetic": (
            "exact SPF factorization, complete square-divisor menus, and the "
            "two-sided common-witness formula"
        ),
        "controls": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
