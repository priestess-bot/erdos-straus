#!/usr/bin/env python3
"""Verify the finite phase screen for nonminimal H4 q0 re-entry D lifts.

The search is over the bounded (u, d, k, ell) menu forced by the D-residue
identity. It does not scan prime ranges, denominators, Reach graphs, or H4
predecessor histories.
"""

from __future__ import annotations

import argparse
from math import prod

import sympy

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    FINAL_RESIDUAL,
    selector_a,
)


PHASE_STEP = 912
PHASE_OFFSET = 769


def positive_divisors(value: int) -> tuple[int, ...]:
    if value <= 0:
        raise AssertionError("selector delta unexpectedly vanished")
    factors = sympy.factorint(value)
    if not (
        prod(prime**exponent for prime, exponent in factors.items()) == value
        and all(sympy.isprime(prime) for prime in factors)
    ):
        raise AssertionError("bounded selector-delta factorization was not exact")
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return tuple(sorted(divisors))


def delta(d: int) -> int:
    return 2 * d * (4 * d * d - 2 * d + 1)


def nonminimal_phase_screen() -> dict[str, object]:
    all_divisor_pairs = 0
    odd_divisor_pairs = 0
    triples = 0
    integral_p = 0
    above_delta = 0
    prime_p = 0
    phase_prime_p = 0
    admitted: list[tuple[int, int, int, int, int, int, int, int]] = []

    for u in sorted(FINAL_RESIDUAL):
        base_prime = PHASE_STEP * u + PHASE_OFFSET
        a = selector_a(base_prime)
        if selector_a(base_prime + PHASE_STEP * 119) != a:
            raise AssertionError("phase selector stopped being constant on its progression")
        divisors = positive_divisors(abs(1536 - a))
        all_divisor_pairs += len(divisors)
        for d in divisors:
            if d % 2 == 0:
                continue
            odd_divisor_pairs += 1
            delta_d = delta(d)
            for ell in range(1, 2 * d):
                max_k = (4 * d * d - 2) // (2 * d * ell)
                for k in range(1, max_k + 1):
                    triples += 1
                    denominator = 4 * d * d - 1 - 2 * d * k * ell
                    numerator = 2 * d * ell * delta_d - (2 * d - 1)
                    if denominator <= 0:
                        raise AssertionError("nonminimal lift bound admitted a nonpositive denominator")
                    if numerator % denominator:
                        continue
                    integral_p += 1
                    p = numerator // denominator
                    if p <= delta_d or p < 73:
                        continue
                    above_delta += 1
                    if not sympy.isprime(p):
                        continue
                    prime_p += 1
                    if (p - PHASE_OFFSET) % PHASE_STEP:
                        continue
                    phase_u = (p - PHASE_OFFSET) // PHASE_STEP
                    if phase_u % 119 not in FINAL_RESIDUAL:
                        continue
                    phase_prime_p += 1
                    if selector_a(p) != a or (1536 - a) % d:
                        continue
                    if (p + 1) % (2 * d):
                        continue
                    q = (p + 1) // (2 * d)
                    if q <= 1:
                        continue
                    divisor = delta_d + k * p
                    bound = 2 * d * p - q + 1
                    if bound % divisor or bound // divisor != ell:
                        raise AssertionError("candidate no longer reconstructs the D divisor identity")
                    admitted.append((p, u, a, d, k, ell, q, divisor))

    result = {
        "phase_classes": len(FINAL_RESIDUAL),
        "all_divisor_pairs": all_divisor_pairs,
        "odd_divisor_pairs": odd_divisor_pairs,
        "triples": triples,
        "integral_p": integral_p,
        "above_delta": above_delta,
        "prime_p": prime_p,
        "phase_prime_p": phase_prime_p,
        "admitted": tuple(admitted),
    }
    expected = {
        "phase_classes": 31,
        "all_divisor_pairs": 213,
        "odd_divisor_pairs": 109,
        "triples": 233_378,
        "integral_p": 137,
        "above_delta": 89,
        "prime_p": 7,
        "phase_prime_p": 0,
        "admitted": (),
    }
    if result != expected:
        raise AssertionError(f"nonminimal D-lift phase screen changed: {result}")
    return result


def verify_minimal_mod_three_obstruction() -> None:
    """The D=delta branch is incompatible with d == 1 modulo 3."""
    for d in (1, 7, 13):
        support = 4 * d * d - 2 * d + 1
        if not (d % 3 == 1 and support % 3 == 0 and (2 * (d - 1)) % 3 == 0):
            raise AssertionError("minimal D modulo-three obstruction changed")
        if (2 * d - 1) % 3 != 1:
            raise AssertionError("minimal D contradiction no longer has nonzero constant term")


def verify() -> None:
    screen = nonminimal_phase_screen()
    verify_minimal_mod_three_obstruction()
    if screen["admitted"]:
        raise AssertionError("a nonminimal D lift survived the actual phase screen")
    print(
        "verified q0 re-entry nonminimal D-lift phase exclusion: "
        "233378 bounded triples and no actual phase-prime candidate"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
