#!/usr/bin/env python3
"""Exact support-defect formulation for ordinary Type II tail selectors."""

from __future__ import annotations

from itertools import combinations, product

import sympy

from reproductions import type_ii_square_root_completion_family as family


def prime_powers(prime: int, exponent: int) -> list[int]:
    value = 1
    result = []
    for _ in range(exponent):
        value *= prime
        result.append(value)
    return result


def support_witness(
    q: int, u: int, base_primes: set[int], max_support: int
) -> dict[str, int] | None:
    """Find the least Type II tail divisor using at most max_support new primes.

    The base consists of every power of ``base_primes`` that divides
    ``(q*u)^2``. Each non-base prime is charged once, independent of its
    chosen exponent. The return value is exact rather than heuristic.
    """
    if q < 1 or u < 2 or max_support < 0:
        raise ValueError("q, u, and max_support are out of range")
    gap = 4 * q - 1
    parameter = u - 1
    prime = 4 * q * parameter + 1
    x = q * u
    factors = {
        int(factor): 2 * int(exponent)
        for factor, exponent in sympy.factorint(q * u).items()
    }
    base_values = [1]
    new_powers: dict[int, list[int]] = {}
    for factor, exponent in sorted(factors.items()):
        powers = prime_powers(factor, exponent)
        if factor in base_primes:
            base_values = [value * power for value in base_values for power in [1, *powers]]
        else:
            new_powers[factor] = powers
    target = (-x) % gap
    candidates: list[tuple[int, tuple[int, ...]]] = []
    ordered_new = sorted(new_powers.items())
    for support in range(max_support + 1):
        for selected in combinations(ordered_new, support):
            for powers in product(*(values for _, values in selected)):
                new_part = 1
                for power in powers:
                    new_part *= power
                for base in base_values:
                    divisor = base * new_part
                    if divisor <= x and divisor % gap == target:
                        candidates.append((divisor, tuple(factor for factor, _ in selected)))
    if not candidates:
        return None
    divisor, selected = min(candidates)
    witness = family.verify_normal_form(prime, gap, divisor)
    witness["support"] = len(selected)
    return witness
