#!/usr/bin/env python3
"""Construct Type II two-tail descents by square-root completing a divisor."""

from __future__ import annotations

from fractions import Fraction

import sympy


def completion_factor(q: int, divisor: int) -> int:
    """Least a such that divisor divides q^2*a^2."""
    if q < 1 or divisor < 1:
        raise ValueError("q and divisor must be positive")
    q_factors = sympy.factorint(q)
    result = 1
    for prime, exponent in sympy.factorint(divisor).items():
        missing = max(0, int(exponent) - 2 * int(q_factors.get(prime, 0)))
        result *= int(prime) ** ((missing + 1) // 2)
    return result


def normal_form_parameters(prime: int, gap: int) -> tuple[int, int]:
    """Recover q and t from an ordinary tail gap m=4q-1."""
    if gap < 3 or gap % 4 != 3:
        raise ValueError("gap must have the form 4q-1")
    gap_plus_one = gap + 1
    if (prime - 1) % gap_plus_one:
        raise ValueError("gap+1 must divide prime-1")
    return gap_plus_one // 4, (prime - 1) // gap_plus_one


def verify_normal_form(prime: int, gap: int, divisor: int) -> dict[str, int]:
    """Check the completed-divisor conditions recovered from a tail certificate.

    This avoids factoring ``divisor``: d | q^2(t+1)^2 is equivalent to the
    existence of its minimal square-root completion factor dividing t+1.
    """
    q, parameter = normal_form_parameters(prime, gap)
    x = q * (parameter + 1)
    if math_gcd(divisor, gap) != 1:
        raise ValueError("divisor must be coprime to the gap")
    if parameter % gap != (-4 * divisor - 1) % gap:
        raise ValueError("parameter misses the Type II residue")
    if q * parameter % 6:
        raise ValueError("prime is not in the core congruence class")
    if divisor > x or x * x % divisor:
        raise ValueError("divisor does not divide the recovered square")
    return {
        "gap": gap,
        "q": q,
        "parameter": parameter,
        "prime": prime,
        "x": x,
        "divisor": divisor,
        "source_denominator": parameter + 1,
    }


def two_tail_witness(q: int, divisor: int, parameter: int) -> dict[str, int]:
    """Verify the completed-divisor Type II certificate and its strict source."""
    gap = 4 * q - 1
    completion = completion_factor(q, divisor)
    prime = 4 * q * parameter + 1
    if math_gcd(divisor, gap) != 1:
        raise ValueError("divisor must be coprime to the gap")
    if parameter < 1 or parameter % gap != (-4 * divisor - 1) % gap:
        raise ValueError("parameter misses the Type II residue")
    if parameter % completion != (-1) % completion:
        raise ValueError("parameter misses the square-root completion")
    if q * parameter % 6:
        raise ValueError("prime is not in the core congruence class")
    x = q * (parameter + 1)
    if divisor > x or x * x % divisor or divisor % gap != (-x) % gap:
        raise AssertionError("completed divisor failed the Type II criterion")
    y = prime * (x + divisor) // gap
    z = prime * (x + x * x // divisor) // gap
    source = parameter + 1
    if y % prime or z % prime or (prime - 1) % (gap + 1):
        raise AssertionError("two-tail divisibility failed")
    if Fraction(4, prime) != Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
        raise AssertionError("target identity failed")
    if Fraction(4, source) != Fraction(1, x) + Fraction(1, y // prime) + Fraction(1, z // prime):
        raise AssertionError("source identity failed")
    return {
        "gap": gap,
        "completion_factor": completion,
        "prime": prime,
        "x": x,
        "divisor": divisor,
        "source_denominator": source,
    }


def math_gcd(left: int, right: int) -> int:
    while right:
        left, right = right, left % right
    return left
