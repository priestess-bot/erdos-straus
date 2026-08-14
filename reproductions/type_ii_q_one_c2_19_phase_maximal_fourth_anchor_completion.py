#!/usr/bin/env python3
"""Verify maximal-complete-excess H3 to H4 completion.

This performs symbolic-free exact integer checks on the H3 maximal block,
then factors only the fixed phase/lambda top-gate constants.  It does not
scan primes or denominators.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm, prod

import sympy

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    FINAL_RESIDUAL,
    MODULUS,
    RESIDUE_DENOMINATOR,
    STEP,
    base_prime,
    dispatch_h3,
    h3_data,
    selector_a,
)


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    """Return the maximal full-prime-power excess without factoring value."""
    shared = gcd(value, capacity)
    residual = value // shared
    block = gcd(value, pow(residual, value.bit_length(), value))
    return block, value // block


def positive_divisors(value: int) -> tuple[int, ...]:
    """Enumerate divisors of one fixed bounded phase constant."""
    if value <= 0:
        raise AssertionError("lambda bound unexpectedly vanished")
    factors = sympy.factorint(value)
    if not (
        prod(prime**exponent for prime, exponent in factors.items()) == value
        and all(sympy.isprime(prime) for prime in factors)
    ):
        raise AssertionError("bounded lambda factorization was not exact")
    values = [1]
    for prime, exponent in factors.items():
        values = [
            divisor * prime**power
            for divisor in values
            for power in range(exponent + 1)
        ]
    return tuple(sorted(values))


def phase_prime_divisors(value: int, u: int) -> tuple[int, ...]:
    """Return the exact prime divisors in one nonnegative H3 phase ray."""
    if value == 0:
        raise AssertionError("top-capacity constant unexpectedly vanished")
    factors = sympy.factorint(abs(value))
    if not (
        prod(prime**exponent for prime, exponent in factors.items()) == abs(value)
        and all(sympy.isprime(prime) for prime in factors)
    ):
        raise AssertionError("top-capacity constant factorization was not exact")
    base = base_prime(u)
    return tuple(
        prime
        for prime in sorted(factors)
        if prime >= base and (prime - base) % STEP == 0 and prime % 24 == 1
    )


def top_constant(a: int, lambda_value: int) -> int:
    """Return the fixed phase constant equivalent to c4 == p - 1."""
    return (
        3_072 * lambda_value * RESIDUE_DENOMINATOR
        + MODULUS * 57 * (MODULUS * a - 11_943_424)
    )


def maximal_h4(prime: int) -> dict[str, int | bool]:
    """Build H4 from H3's true maximal complete-excess block."""
    data = h3_data(prime)
    a = int(data["a"])
    c3 = int(data["c_3"])
    m3 = int(data["M_3"])
    k3 = int(data["K_3"])
    r3 = int(data["R_3"])
    v = r3 - 1
    g = gcd((prime + 1) // 2, c3)
    block, beta = complete_excess(v, k3)
    overlap = gcd(m3, block)
    if (beta * overlap) % 2:
        raise AssertionError("maximal H3 block did not have an even residual")
    lambda_value = beta * overlap // 2
    m4 = lcm(m3, block)
    multiplier = m4 // m3
    c4 = c3 * pow(multiplier, -1, prime) % prime
    k4 = m4 * c4
    r4 = (4 * k4 - 1) // prime
    top_from_capacity = c4 == prime - 1
    top_from_constant = top_constant(a, lambda_value) % prime == 0

    if not (
        prime % 24 == 1
        and gcd(prime, MODULUS * RESIDUE_DENOMINATOR) == 1
        and v % 2 == 0
        and v % 4 == 2
        and gcd(v, k3) == 2 * g
        and block > 1
        and block * beta == v
        and k3 % beta == 0
        and gcd(block, beta) == 1
        and k3 % block != 0
        and block % prime != 0
        and beta % 2 == 0
        and overlap % 2 == 1
        and gcd(beta // 2, overlap) == 1
        and g % lambda_value == 0
        and (1536 - a) % lambda_value == 0
        and multiplier > 1
        and multiplier == block // overlap
        and multiplier == v // (2 * lambda_value)
        and 1 <= c4 <= prime - 1
        and prime * r4 + 1 == 4 * k4
        and k4 % m4 == 0
        and top_from_capacity == top_from_constant
    ):
        raise AssertionError("maximal H3 fourth-anchor receipt changed")
    return {
        "p": prime,
        "a": a,
        "g": g,
        "beta": beta,
        "overlap": overlap,
        "lambda": lambda_value,
        "multiplier_mod_p": multiplier % prime,
        "c4": c4,
        "r4_mod_p": r4 % prime,
        "top_capacity": top_from_capacity,
        "block_bits": block.bit_length(),
    }


def finite_top_gate_exclusion() -> dict[str, object]:
    """Exclude c4 == p - 1 for every H3 phase and every possible lambda."""
    cancellation_factors = sympy.factorint(MODULUS * RESIDUE_DENOMINATOR)
    if cancellation_factors != {2: 9, 3: 2, 7: 2, 17: 2, 19: 3} or any(
        prime % 24 == 1 for prime in cancellation_factors
    ):
        raise AssertionError("the H3 top-gate cancellation constant changed")
    failures: list[tuple[int, int, int, tuple[int, ...]]] = []
    pair_count = 0
    divisor_counts: list[int] = []
    for u in sorted(FINAL_RESIDUAL):
        base = base_prime(u)
        a = selector_a(base)
        if not (0 < base < STEP and selector_a(base + STEP) == a):
            raise AssertionError("phase selector stopped being constant along its progression")
        lambdas = positive_divisors(abs(1536 - a))
        divisor_counts.append(len(lambdas))
        for lambda_value in lambdas:
            pair_count += 1
            constant = top_constant(a, lambda_value)
            candidates = phase_prime_divisors(constant, u)
            if candidates:
                failures.append((u, a, lambda_value, candidates))
    if failures:
        raise AssertionError(f"a maximal H3 top-capacity phase exclusion failed: {failures}")
    if (len(divisor_counts), min(divisor_counts), max(divisor_counts), pair_count) != (31, 2, 18, 213):
        raise AssertionError("finite H3 lambda domain changed")
    return {
        "phase_classes": len(divisor_counts),
        "lambda_divisor_count_range": [min(divisor_counts), max(divisor_counts)],
        "phase_lambda_pairs": pair_count,
        "top_capacity_phase_prime_candidates": failures,
    }


def verify() -> None:
    finite = finite_top_gate_exclusion()
    clean = maximal_h4(18_097)
    hard = maximal_h4(14_449)
    hard_dispatch = dispatch_h3(14_449)
    if not (
        clean == {
            "p": 18_097,
            "a": 583,
            "g": 1,
            "beta": 2,
            "overlap": 1,
            "lambda": 1,
            "multiplier_mod_p": 10_463,
            "c4": 13_680,
            "r4_mod_p": 16_969,
            "top_capacity": False,
            "block_bits": 397,
        }
        and hard == {
            "p": 14_449,
            "a": 431,
            "g": 5,
            "beta": 10,
            "overlap": 1,
            "lambda": 5,
            "multiplier_mod_p": 9_407,
            "c4": 13_391,
            "r4_mod_p": 4_039,
            "top_capacity": False,
            "block_bits": 385,
        }
        and hard_dispatch
        == {"branch": "bounded_q_one_mask", "u": 15, "a": 431, "g": 5, "mask": (5,)}
        and finite
        == {
            "phase_classes": 31,
            "lambda_divisor_count_range": [2, 18],
            "phase_lambda_pairs": 213,
            "top_capacity_phase_prime_candidates": [],
        }
    ):
        raise AssertionError("maximal H3 fourth-anchor completion controls changed")
    print("verified maximal H3 fourth anchor for clean and q=1-mask controls")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact H3 completion receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
