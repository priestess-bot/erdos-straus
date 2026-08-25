#!/usr/bin/env python3
"""Verify the exact common-witness criterion for external source scale pairs.

For distinct k < l dividing (p-1)/4, the complete square-factor menus satisfy

    E_k intersection E_l
      = {e | G^2 : e <= M_k and lcm(q_k, q_l) | 4e+1},

where G=gcd(M_k,l-k)=gcd(M_k,M_l), q_j=4j-1,
n_j=p-(p-1)/(4j), and M_j=j*n_j. If l=k*s, then
G=k*gcd(n_k,s-1). This is an exact arithmetic identity, not a claim that
all menu pairs are disjoint. The controls include comparable and
noncomparable pairs, plus a pair where the simple range gate fails but the
exact candidate set remains empty.
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


def collision_state(p: int, k: int, ell: int, spf: list[int]) -> dict[str, object]:
    """Compute both sides of the exact collision formula."""
    base = (p - 1) // 4
    if p % 24 != 1 or not (0 < k < ell and base % k == base % ell == 0):
        raise ValueError("require distinct divisors k < l of (p-1)/4")

    q_k, q_l = 4 * k - 1, 4 * ell - 1
    n_k, n_l = p - base // k, p - base // ell
    M_k, M_l = k * n_k, ell * n_l
    shared = math.gcd(M_k, ell - k)
    modulus = math.lcm(q_k, q_l)

    if math.gcd(M_k, M_l) != shared:
        raise AssertionError("scale-pair gcd formula failed")
    if M_l <= M_k:
        raise AssertionError("larger scale must have larger preserved denominator")
    scale_relation = "noncomparable"
    s: int | None = None
    if ell % k == 0:
        s = ell // k
        if shared != k * math.gcd(n_k, s - 1):
            raise AssertionError("comparable-scale specialization failed")
        scale_relation = "chain"

    left = source_menu(p, k, spf) & source_menu(p, ell, spf)
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
        "l": ell,
        "relation": scale_relation,
        "s": s,
        "n_k": n_k,
        "n_l": n_l,
        "M_k": M_k,
        "M_l": M_l,
        "g": shared if s is None else math.gcd(n_k, s - 1),
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
        (97, 4, 6, True),
        (97, 2, 12, False),
        (193, 1, 6, False),
    )
    limit = max(p for p, _, _, _ in controls)
    spf = short_certificate.smallest_prime_factors(limit)
    records = []
    for p, k, ell, expected_gate in controls:
        record = collision_state(p, k, ell, spf)
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
