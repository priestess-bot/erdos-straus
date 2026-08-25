#!/usr/bin/env python3
"""Independent algebra replay for the c8 fallback and H4 C1 boundary.

This verifier imports neither the proposed atomic serializer nor the common
admission gate.  It checks the polynomial identities, endpoint inequalities,
and negative-residue H4 C1 gate from their defining integer equations.
"""

from __future__ import annotations

import argparse
from math import gcd

import sympy


def verify_symbolic_c8() -> None:
    s = sympy.symbols("s", integer=True, positive=True)
    p = 48 * s + 1
    m = 9 * s * (176 * s + 5) * (3168 * s**2 + 24 * s - 1)
    r = 3345408 * s**3 + 50688 * s**2 - 1392 * s - 1
    q = 1672704 * s**3 + 25344 * s**2 - 696 * s - 1
    f = 278784 * s**2 - 1584 * s - 83
    if any(
        sympy.expand(value) != 0
        for value in (
            p * r + 1 - 32 * m,
            r - 1 - 2 * q,
            8 * q - 75 - p * f,
        )
    ):
        raise AssertionError("c8 symbolic identities changed")


def verify_capacity_interval(prime: int, capacity: int) -> None:
    if not (
        prime >= 4_129
        and prime % 24 == 1
        and 1 <= capacity < prime
        and (75 * capacity - 64) % prime == 0
        and all(0 < 75 * value - 64 < prime for value in range(1, 9))
        and (75 * (prime - 1) - 64) % prime == (-139) % prime != 0
        and 9 <= capacity <= prime - 2
    ):
        raise AssertionError("c8 final capacity interval changed")


def verify_h4_c1_gate(d: int, q: int, prime: int, carrier_d: int) -> None:
    delta = 2 * d * (4 * d * d - 2 * d + 1)
    divisor = (2 * d - 1) * ((2 * d + 1) * q - 1)
    if not (
        prime == 2 * d * q - 1
        and pow(q, -1, prime) == 2 * d
        and carrier_d % prime == (-delta) % prime
        and divisor % carrier_d == 0
        and 0 < carrier_d < 2 * d * prime
        and (q * q * delta - (q - 1 + 2 * d)) % prime == 0
    ):
        raise AssertionError("H4 C1 negative-residue gate changed")


def verify() -> None:
    verify_symbolic_c8()
    prime = 157_393
    q = 58_971_931_474_577_975
    m = 580_110_575_661_140_706_117
    capacity = (8 * pow(q, -1, prime)) % prime
    support = m * q
    carrier = support * capacity
    residual = (4 * carrier - 1) // prime
    verify_capacity_interval(prime, capacity)
    if not (
        capacity == 4_198
        and gcd(m, q) == 1
        and support
        == 34_210_241_115_566_771_375_771_444_426_075_973_075
        and residual
        == 3_649_834_292_583_515_308_444_175_375_033_627_543
        and prime * residual + 1 == 4 * carrier
        and residual > prime
    ):
        raise AssertionError("independent c8 endpoint replay changed")
    verify_h4_c1_gate(23, 47, 2_161, 4_140)
    verify_h4_c1_gate(35, 71, 4_969, 9_660)
    print(
        "independently replayed c8 symbolic fallback and H4 C1 negative-residue gate"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
