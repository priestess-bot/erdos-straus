#!/usr/bin/env python3
"""Verify focused controls for the H4 proper-overlap d=1 handoff.

The H4 q-carrier control is a c4=1 local arithmetic specialization, not an
actual 19-phase H3 predecessor. The terminal root-fan control is a generic
admitted d=1 suffix calculation, also not an H4 predecessor witness.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

from type_i_overflow_d_one_p_free_peeled_small_anchor import (
    FIXTURES as D_ONE_FIXTURES,
    audit as d_one_audit,
)
from type_i_root_coprime_capacity_fan_half_descent import audit as root_fan_audit
from type_ii_q_one_c2_19_phase_h4_p_primary_small_anchor_renewal import (
    FIXTURES as H4_FIXTURES,
    audit as h4_audit,
    complete_excess,
)


def valuation(value: int, prime: int) -> int:
    """Return the exact prime-adic valuation of a nonzero integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def regenerate_a_one(prime: int, parameter: int) -> int:
    """Apply one a=1 canonical d=1 regeneration step."""
    multiplier = (prime - 1) * parameter - 1
    if (multiplier - 1) % prime:
        raise AssertionError("the requested a=1 regeneration is not canonical")
    return parameter * multiplier - (multiplier - 1) // prime


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


def proper_overlap_a_one_q_carrier_control() -> dict[str, int | str]:
    """Check the q identities only in the local c4=1 H4 specialization."""
    fixture = H4_FIXTURES[1]
    receipt = h4_audit(fixture)
    p = fixture.prime
    r4 = 1 + p * fixture.peeled_part
    k4_local = (p * r4 + 1) // 4
    m4_local = k4_local
    c4_local = 1
    bundle = complete_excess(r4 - fixture.expected_h, k4_local)
    m_alt = lcm(m4_local, bundle)
    capacity = pow((4 * m_alt) % p, -1, p)
    n_alt = (4 * m_alt + 1) // p
    a_alt = (p + 1) // 2 // gcd((p + 1) // 2, (n_alt + 1) // 2)
    w = (p + 1) // 2
    d4_local = gcd(w, m4_local)
    q = w // d4_local
    multiplier = m_alt // m4_local

    if not (
        receipt["outcome"] == "p_free_top_capacity_a_one"
        and fixture.expected_h < p + 1
        and capacity == p - 1
        and (4 * m_alt + 1) % p == 0
        and n_alt > 1
        and n_alt % 4 == 1
        and a_alt == 1
        and m_alt % w == 0
        and k4_local == m4_local * c4_local
        and q > 1
        and multiplier % q == 0
        and bundle % q == 0
        and (r4 - fixture.expected_h) % q == 0
        and (4 * k4_local - (1 - fixture.expected_h)) % q == 0
    ):
        raise AssertionError("the local proper-overlap q-carrier control changed")
    return {
        "h": fixture.expected_h,
        "capacity": capacity,
        "a_alt": a_alt,
        "q": q,
        "outcome": str(receipt["outcome"]),
    }


def a_one_terminal_root_fan_control() -> dict[str, int]:
    """Follow one a=1 regeneration into the explicit u=1 strict root fan."""
    p = 73
    b0 = 10_583
    n0 = (p + 1) * b0 - 1
    initial = full_product_row(p, n0)
    initial_multiplier = initial["E"]
    eta = valuation(initial_multiplier - 1, p)
    omega = ((initial_multiplier - 1) // p**eta) % p
    b_star = b0
    for _ in range(eta):
        b_star = regenerate_a_one(p, b_star)
    n_star = (p + 1) * b_star - 1
    terminal = full_product_row(p, n_star)
    r = (b_star + 1) // (2 * p)
    root_modulus = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, root_modulus)
    h_three_gcd = gcd(r - 3, (3 * p + 1) // 4)
    strict_capacity = 2 * h_three_gcd
    root_fan_audit(p, r, 1, h_three_gcd)

    if not (
        initial["a"] == 1
        and initial_multiplier % p == 1
        and eta == 1
        and omega == p - 1
        and terminal["a"] == 1
        and terminal["E"] % p == 0
        and b_star == 2 * p * r - 1
        and r == 55_232_678
        and u == 1
        and 9 * u * u < p
        and h_three_gcd == 5
        and strict_capacity == 10
        and 1 <= strict_capacity <= p - 2
    ):
        raise AssertionError("the a=1 terminal root-fan strict control changed")
    return {
        "eta": eta,
        "omega": omega,
        "u": u,
        "capacity": strict_capacity,
    }


def verify() -> None:
    direct = direct_a_greater_than_one_control()
    p_free = p_free_a_greater_than_one_control()
    q_carrier = proper_overlap_a_one_q_carrier_control()
    root_fan = a_one_terminal_root_fan_control()
    if not (
        direct["target_capacity"] == 49
        and p_free["receipt"]["target_capacity"] == 3
        and q_carrier
        == {
            "h": 2,
            "capacity": 72,
            "a_alt": 1,
            "q": 37,
            "outcome": "p_free_top_capacity_a_one",
        }
        and root_fan == {"eta": 1, "omega": 72, "u": 1, "capacity": 10}
    ):
        raise AssertionError("the H4 top-capacity handoff controls changed")
    print(
        "verified H4 proper-overlap top-capacity handoff: direct a>1 exit, "
        "a>1 p-free small-anchor exit, local q-carrier, and a=1 root-fan exit"
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
