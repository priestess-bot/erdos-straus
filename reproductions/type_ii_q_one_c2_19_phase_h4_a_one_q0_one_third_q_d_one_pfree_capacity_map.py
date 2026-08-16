#!/usr/bin/env python3
"""Verify focused arithmetic controls for the d=1 third q-carrier capacity map.

The controls cover the exact modular capacity/source-D identities and a
composite-q unitary allocation.  They do not search primes or H4 histories.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def positive_divisors(value: int) -> tuple[int, ...]:
    divisors: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        divisors.append(divisor)
        paired = value // divisor
        if paired != divisor:
            divisors.append(paired)
    return tuple(sorted(divisors))


def verify_p73_source_d_gate() -> None:
    p = 73
    q = (p + 1) // 2
    source_dividend = q**3 - 4 * q + 1
    stutter_residue = (2**3) * (2**3 + 1) % p
    matching_divisors = tuple(
        divisor
        for divisor in positive_divisors(source_dividend)
        if divisor % p == stutter_residue
    )

    if not (
        p % 24 == 1
        and q == 37
        and 8 * source_dividend == p**3 + 3 * p**2 - 13 * p - 7
        and source_dividend % 4 == 2
        and stutter_residue == 72
        and (q**3 * stutter_residue) % p == 9
        and matching_divisors == ()
    ):
        raise AssertionError("p=73 third-carrier source-D gate control changed")


def verify_capacity_residue() -> None:
    p = 73
    q = (p + 1) // 2
    e_stutter = q**3
    e_strict = q**3 + 1
    c_stutter = (-q**3 * pow(e_stutter, -1, p)) % p
    c_strict = (-q**3 * pow(e_strict, -1, p)) % p

    if not (
        e_stutter % p != 0
        and c_stutter == p - 1
        and c_strict != p - 1
        and 1 <= c_strict <= p - 2
    ):
        raise AssertionError("third-carrier capacity residue control changed")


def verify_composite_unitary_allocation() -> None:
    p = 409
    q = (p + 1) // 2
    u_value = 5
    s_value = 41
    e_value = q**3 + p * s_value
    allocation = gcd(q, u_value)
    a_coordinate = q // gcd(q, u_value * s_value)

    if not (
        p % 24 == 1
        and q == 5 * 41
        and gcd(u_value, e_value) == 1
        and allocation == 5
        and q % allocation == 0
        and gcd(allocation, q // allocation) == 1
        and (q // allocation) == 41
        and s_value % (q // allocation) == 0
        and e_value % (q // allocation) == 0
        and a_coordinate == 1
    ):
        raise AssertionError("composite-q unitary allocation control changed")


def verify() -> None:
    verify_p73_source_d_gate()
    verify_capacity_residue()
    verify_composite_unitary_allocation()
    print("verified d=1 third q-carrier p-free capacity map")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
