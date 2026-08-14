#!/usr/bin/env python3
"""Verify fixed q-primary receipt and checkpoint relays for transverse overlaps."""

from __future__ import annotations

import argparse
from math import gcd


def valuation(value: int, prime: int) -> int:
    count = 0
    while value % prime == 0:
        value //= prime
        count += 1
    return count


def relay_values(p: int, r: int, e_multiplier: int, d: int) -> dict[str, int]:
    if e_multiplier <= 1 or (e_multiplier - 1) % p:
        raise AssertionError("control is not a nonterminal stutter multiplier")
    t_value = p * p * r - (p + 1) // 2
    k_value = (p * p - 1) // 2 * t_value
    if 4 * k_value % d:
        raise AssertionError("control divisor did not divide the capacity product")
    quotient = 4 * k_value // d - p * e_multiplier
    r_value = 2 * p**3 * r - p * p - 2 * p * r - p + 1
    h = r_value - e_multiplier * d
    if quotient * d != p * h + 1 or d * (p * e_multiplier + quotient) != 4 * k_value:
        raise AssertionError("receipt quotient bridge failed")
    if (d + h - 1) % p:
        raise AssertionError("control did not satisfy the stutter congruence")
    m = (d + h - 1) // p
    a = quotient * m - h
    s = (e_multiplier - 1) // p
    b_zero = 2 * p * r - 1
    b_one = b_zero * e_multiplier - s
    e_one = (p - 1) * b_one - 1
    eisenstein_norm = a * a - a * (quotient - 1) + (quotient - 1) ** 2
    return {
        "A": (p + 1) // 2 * t_value,
        "T": t_value,
        "K": k_value,
        "R": r_value,
        "z": e_multiplier * d,
        "h": h,
        "m": m,
        "e": quotient,
        "a": a,
        "s": s,
        "B1": b_one,
        "E1": e_one,
        "N": eisenstein_norm,
    }


def verify_plus_excess_relay() -> None:
    p, r, q, e_multiplier, d = 169, 10, 5, 170, 125
    values = relay_values(p, r, e_multiplier, d)
    b = valuation(p + 1, q)
    t = valuation(d, q) - b
    d_star = d // gcd(d, values["h"] * values["h"] - 1)
    q_block = valuation(values["z"], q)
    expected_e = q_block - valuation(values["A"], q)
    if not (
        p % 24 == 1
        and values["m"] % q == 0
        and values["h"] % q == 1
        and valuation(values["T"], q) == t
        and valuation(d_star, q) == t
        and q_block > valuation(values["K"], q)
        and valuation(e_multiplier, q) > 0
        and valuation(e_multiplier, q) == expected_e
        and valuation(values["e"], q) == 0
        and valuation(values["a"], q) == 0
        and valuation(p * values["h"] + 1, q) == b + t
    ):
        raise AssertionError("p+1 excess receipt relay failed")


def verify_minus_excess_relay() -> None:
    p, r, q, e_multiplier, d = 121, 21, 5, 2300, 25
    values = relay_values(p, r, e_multiplier, d)
    b = valuation(p - 1, q)
    t = valuation(d, q) - b
    d_star = d // gcd(d, values["h"] * values["h"] - 1)
    q_block = valuation(values["z"], q)
    expected_e = q_block - valuation(values["A"], q)
    if not (
        p % 24 == 1
        and (values["m"] + 2) % q == 0
        and values["h"] % q == -1 % q
        and valuation(values["T"], q) == b + t
        and valuation(d_star, q) == t
        and q_block > valuation(values["K"], q)
        and valuation(e_multiplier, q) > b
        and valuation(e_multiplier, q) == expected_e
        and valuation(values["e"], q) == b
        and valuation(values["a"], q) == 0
        and valuation(values["s"] + 1, q) == b
        and valuation(r - 1, q) == b
        and valuation(values["B1"], q) == 0
        and valuation(values["E1"] + 1, q) == b
        and valuation(p * values["h"] + 1, q) == 2 * b + t
        and values["N"] % q == 3 % q
        and valuation(values["N"], q) == 0
    ):
        raise AssertionError("p-1 excess receipt relay failed")


def verify() -> None:
    # Both controls are local receipt arithmetic, not actual root receipts.
    verify_plus_excess_relay()
    verify_minus_excess_relay()
    print("verified transverse overlap receipt relay")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
