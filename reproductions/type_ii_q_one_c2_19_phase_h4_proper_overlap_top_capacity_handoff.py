#!/usr/bin/env python3
"""Verify the H4 proper-overlap top-capacity d=1 handoff controls.

The controls separate the all-a>1 d=1 exit from the genuinely remaining
a_alt=1 interface.  They are local arithmetic examples, not 19-phase H3
predecessors.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

from type_i_overflow_d_one_p_free_peeled_small_anchor import (
    FIXTURES as D_ONE_FIXTURES,
    audit as d_one_audit,
)
from type_ii_q_one_c2_19_phase_h4_p_primary_small_anchor_renewal import (
    FIXTURES as H4_FIXTURES,
    audit as h4_audit,
    complete_excess,
)


def full_product_row(prime: int, denominator: int) -> dict[str, int]:
    """Build a d=1 top-capacity row and its a-coordinate."""
    p = prime
    n = denominator
    support = (p * n - 1) // 4
    residual = (p - 1) * n - 1
    capacity = support * (p - 1)
    alpha = (p + 1) // 2
    v = (n + 1) // 2
    shared = gcd(alpha, v)
    a = alpha // shared
    b = v // shared
    multiplier = (p - 1) * b - a
    target_capacity = (-pow(multiplier, -1, p)) % p if multiplier % p else 0

    if not (
        p % 24 == 1
        and n > 1
        and n % 4 == 1
        and support > (p - 1) ** 2 // 4
        and p * residual + 1 == 4 * capacity
        and 4 * support + 1 == p * n
        and gcd(a, b) == 1
    ):
        raise AssertionError("the d=1 normal-form contract changed")
    return {
        "p": p,
        "n": n,
        "A": support,
        "R": residual,
        "a": a,
        "b": b,
        "E": multiplier,
        "target_capacity": target_capacity,
    }


def direct_a_greater_than_one_control() -> dict[str, int]:
    """A non-special multiplier leaves top capacity immediately."""
    row = full_product_row(73, 77)
    if not (
        row["a"] == 37
        and row["b"] == 39
        and row["E"] % row["p"] == -3 % row["p"]
        and row["target_capacity"] == 49
        and 1 <= row["target_capacity"] <= row["p"] - 2
    ):
        raise AssertionError("the direct a>1 strict d=1 control changed")
    return row


def p_free_a_greater_than_one_control() -> dict[str, object]:
    """The p-free terminal class is discharged by the real small-anchor route."""
    row = full_product_row(73, 217)
    receipt = d_one_audit(D_ONE_FIXTURES[0])
    if not (
        row["a"] == 37
        and row["E"] % row["p"] == 0
        and receipt["name"] == "p73_n217_e1_small_anchor_capacity_exit"
        and receipt["target_capacity"] == 3
    ):
        raise AssertionError("the a>1 p-free small-anchor handoff changed")
    return {"row": row, "receipt": receipt}


def proper_overlap_a_one_boundary() -> dict[str, int | str]:
    """Preserve the local a_alt=1 boundary instead of falsely excluding it."""
    fixture = H4_FIXTURES[1]
    receipt = h4_audit(fixture)
    p = fixture.prime
    r4 = 1 + p * fixture.peeled_part
    k4 = (p * r4 + 1) // 4
    bundle = complete_excess(r4 - fixture.expected_h, k4)
    m_alt = lcm(k4, bundle)
    capacity = pow((4 * m_alt) % p, -1, p)
    n_alt = (4 * m_alt + 1) // p
    a_alt = (p + 1) // 2 // gcd((p + 1) // 2, (n_alt + 1) // 2)

    if not (
        receipt["outcome"] == "p_free_top_capacity_a_one"
        and fixture.expected_h < p + 1
        and capacity == p - 1
        and n_alt > 1
        and n_alt % 4 == 1
        and a_alt == 1
        and m_alt % ((p + 1) // 2) == 0
    ):
        raise AssertionError("the proper-overlap a_alt=1 boundary changed")
    return {
        "h": fixture.expected_h,
        "capacity": capacity,
        "a_alt": a_alt,
        "outcome": str(receipt["outcome"]),
    }


def verify() -> None:
    direct = direct_a_greater_than_one_control()
    p_free = p_free_a_greater_than_one_control()
    boundary = proper_overlap_a_one_boundary()
    if not (
        direct["target_capacity"] == 49
        and p_free["receipt"]["target_capacity"] == 3
        and boundary
        == {
            "h": 2,
            "capacity": 72,
            "a_alt": 1,
            "outcome": "p_free_top_capacity_a_one",
        }
    ):
        raise AssertionError("the H4 top-capacity handoff controls changed")
    print(
        "verified H4 proper-overlap top-capacity handoff: direct a>1 exit, "
        "a>1 p-free small-anchor exit, and the retained a_alt=1 boundary"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run d=1 handoff controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
