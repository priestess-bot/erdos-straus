#!/usr/bin/env python3
"""Verify the H4 fresh-q/root-cyclotomic orthogonality boundary.

These are fixed arithmetic controls. The saturated CRT root is deliberately
static: it demonstrates the limit of q-residue reasoning and is not asserted
to be an actual 19-phase H3-to-H4 predecessor.
"""

from __future__ import annotations

import argparse
from math import gcd

from type_ii_q_one_c2_19_phase_h4_p_primary_small_anchor_renewal import (
    FIXTURES as H4_FIXTURES,
    audit as h4_audit,
)


def valuation(value: int, prime: int) -> int:
    """Return the exact prime-adic valuation of a nonzero integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def root_row(prime: int, parameter: int) -> dict[str, int]:
    """Build an a=1 p-free root row from its positive r parameter."""
    p = prime
    r = parameter
    w = (p + 1) // 2
    modulus = (p * p + p + 1) // 3
    b = 2 * p * r - 1
    n = (p + 1) * b - 1
    support = w * (p * p * r - w)
    capacity = support * (p - 1)
    residual = 2 * p**3 * r - p * p - 2 * p * r - p + 1
    multiplier = (p - 1) * b - 1
    a = w // gcd(w, (n + 1) // 2)
    u = gcd(2 * r + 1, modulus)

    if not (
        p % 24 == 1
        and r >= 1
        and n % 4 == 1
        and a == 1
        and multiplier % p == 0
        and p * residual + 1 == 4 * capacity
        and gcd(residual - (p + 1), capacity) == 3 * u
    ):
        raise AssertionError("the p-free a=1 root normal form changed")
    return {
        "p": p,
        "r": r,
        "w": w,
        "M": modulus,
        "b": b,
        "R": residual,
        "E": multiplier,
        "u": u,
    }


def h4_local_q_carrier_control() -> dict[str, int | str]:
    """Retain the q=37 proper-overlap local H4 arithmetic control."""
    fixture = H4_FIXTURES[1]
    receipt = h4_audit(fixture)
    p = fixture.prime
    r4 = 1 + p * fixture.peeled_part
    k4 = (p * r4 + 1) // 4
    w = (p + 1) // 2
    q = w // gcd(w, k4)

    if not (
        receipt["outcome"] == "p_free_top_capacity_a_one"
        and fixture.expected_h == 2
        and q == 37
        and p % q == q - 1
    ):
        raise AssertionError("the local H4 fresh-q carrier changed")
    return {"p": p, "q": q, "outcome": str(receipt["outcome"])}


def regeneration_transport_control() -> dict[str, int]:
    """Check xi'=xi(1-2xi) modulo the H4 fresh q carrier."""
    p = 73
    q = 37
    b0 = 10_583
    e0 = (p - 1) * b0 - 1
    s0 = (e0 - 1) // p
    b1 = b0 * e0 - s0
    xi0 = b0 + 1
    xi1 = b1 + 1
    r1 = (b1 + 1) // (2 * p)

    if not (
        e0 % p == 1
        and valuation(e0 - 1, p) == 1
        and ((xi1 - xi0 * (1 - 2 * xi0)) % q == 0)
        and ((2 * r1 + 1 + b1) % q == 0)
        and xi0 % q == 2
        and xi1 % q == 31
        and b1 % q == 30
        and (2 * r1 + 1) % q == 7
    ):
        raise AssertionError("the a=1 q-residue transport changed")
    return {"xi0": xi0 % q, "xi1": xi1 % q, "root_residue": (2 * r1 + 1) % q}


def saturated_crt_root_control() -> dict[str, int]:
    """Construct one static saturated root with a prescribed q residue."""
    p = 73
    q = 37
    desired_b_residue = 12
    modulus = (p * p + p + 1) // 3
    y = 1
    if not (y > 0 and y % 2 and (modulus * y + desired_b_residue) % q == 0):
        raise AssertionError("the fixed CRT representative changed")
    row = root_row(p, (modulus * y - 1) // 2)
    eta = valuation(row["E"] - 1, p)
    omega = ((row["E"] - 1) // p**eta) % p

    if not (
        row["r"] == 900
        and row["M"] == 1_801
        and row["b"] % q == desired_b_residue
        and row["u"] == row["M"]
        and gcd(q, 3 * row["M"]) == 1
        and gcd(q, 3 * row["u"]) == 1
        and (row["R"] - (p + 1)) % q == 1
        and eta == 0
        and omega == p - 1
        and 9 * row["u"] * row["u"] > p
    ):
        raise AssertionError("the static saturated CRT root boundary changed")
    return {
        "q": q,
        "u": row["u"],
        "b_mod_q": row["b"] % q,
        "root_gap_mod_q": (row["R"] - (p + 1)) % q,
    }


def verify() -> None:
    local = h4_local_q_carrier_control()
    transport = regeneration_transport_control()
    saturated = saturated_crt_root_control()
    if not (
        local == {"p": 73, "q": 37, "outcome": "p_free_top_capacity_a_one"}
        and transport == {"xi0": 2, "xi1": 31, "root_residue": 7}
        and saturated == {"q": 37, "u": 1_801, "b_mod_q": 12, "root_gap_mod_q": 1}
    ):
        raise AssertionError("the fresh-q/root-cyclotomic controls changed")
    print(
        "verified H4 fresh-q/root-cyclotomic orthogonality, q-residue transport, "
        "and the static saturated-root boundary"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused arithmetic controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
