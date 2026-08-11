#!/usr/bin/env python3
"""Verify the universal H1 direct-cofactor obstruction at the C=2 boundary."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def factorization(value: int) -> dict[int, int]:
    if value < 1:
        raise AssertionError("factorization requires a positive integer")
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def full_excess_bundle(selected: int, capacity: int) -> tuple[int, int]:
    bundle = 1
    supported = 1
    capacity_factors = factorization(capacity)
    for prime, exponent in factorization(selected).items():
        if exponent > capacity_factors.get(prime, 0):
            bundle *= prime**exponent
        else:
            supported *= prime**exponent
    return bundle, supported


def c2_h1_receipt(prime: int) -> dict[str, int]:
    if not (is_prime(prime) and prime % 24 == 1):
        raise AssertionError("expected a core prime")

    support = (prime - 1) * (2 * prime - 1) // 8
    R = 2 * prime - 3
    K = 2 * support
    if not (
        4 * K == prime * R + 1
        and 8 * support == prime * R + 1
        and prime % R != 0
    ):
        raise AssertionError("C=2 high-support chart identity failed")

    selected = R - 1
    bundle, beta = full_excess_bundle(selected, K)
    if not (
        selected == 2 * (prime - 2)
        and gcd(prime - 2, K) == 1
        and bundle == prime - 2
        and beta == 2
        and gcd(bundle, support) == 1
    ):
        raise AssertionError("H1 complete-excess bundle formula failed")

    M = support * bundle
    r = M % prime
    cofactor = pow((4 * M) % prime, -1, prime)
    d = prime - cofactor
    s_numerator = 4 * r * d + 1
    if s_numerator % prime:
        raise AssertionError("direct-cofactor s was not integral")
    s = s_numerator // prime
    g = gcd(support, cofactor)
    a = support // g
    formal_R_target = 4 * r - s
    phase_numerator = r * cofactor - K

    if not (
        r == (prime - 1) // 4
        and cofactor == prime - 1
        and d == 1
        and s == 1
        and g == (prime - 1) // 8
        and a == 2 * prime - 1
        and r < a
        and r % a != 0
        and phase_numerator < 0
        and formal_R_target == prime - 2 < prime
    ):
        raise AssertionError("universal H1 direct-cofactor obstruction failed")

    return {
        "p": prime,
        "A_2": support,
        "R_2": R,
        "K_2": K,
        "Q": bundle,
        "beta": beta,
        "M": M,
        "r": r,
        "C_M": cofactor,
        "d": d,
        "s": s,
        "gate_factor_a": a,
        "phase_numerator": phase_numerator,
        "formal_R_T": formal_R_target,
    }


def verify() -> list[dict[str, int]]:
    return [c2_h1_receipt(prime) for prime in (73, 193, 241, 337)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    rows = verify()
    if args.verify:
        print(
            "verified universal C=2 H1 direct-cofactor obstruction "
            f"for p={','.join(str(row['p']) for row in rows)}"
        )


if __name__ == "__main__":
    main()
