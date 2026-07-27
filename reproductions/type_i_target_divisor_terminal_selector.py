#!/usr/bin/env python3
"""Normalize a Type I even terminal bridge by its two target-side factors.

For ``x=(p+m)/4``, a Type I certificate is equivalently a target divisor
``e | x^2`` with ``4*e == -1 (mod m)``.  Its normal-form quotient and tail
scale are already determined by

    R = (4*e + 1) / m,    K = x*R - e,

so the maximum-tail even terminal condition has a two-factor expression:
choose an even ``E | 4*K^2`` with ``E == 1 (mod R)`` and
``E <= 4*K-2*R``.  This module reconstructs both Egyptian-fraction
identities without selecting A, B, or C first.
"""

from __future__ import annotations

from fractions import Fraction


def terminal_witness_from_target_divisors(
    prime: int, gap: int, target_divisor: int, bridge_factor: int
) -> dict[str, object] | None:
    """Return the exact Type I even terminal bridge encoded by ``(m,e,E)``.

    ``target_divisor`` is the complement of the ordinary Type I certificate
    divisor. ``bridge_factor`` is the normal maximum-tail factor E, not the
    generic reverse divisor p^2 E.
    """
    if prime % 24 != 1 or gap % 4 != 3 or not 3 <= gap <= prime - 2:
        return None
    x = (prime + gap) // 4
    if 4 * x != prime + gap or target_divisor <= 0 or x * x % target_divisor:
        return None
    if target_divisor % gap != (-pow(4, -1, gap)) % gap:
        return None
    if (4 * target_divisor + 1) % gap:
        raise AssertionError("target divisor residue did not reconstruct R")

    R = (4 * target_divisor + 1) // gap
    K = x * R - target_divisor
    if R <= 0 or K <= 0 or 4 * K != prime * R + 1:
        raise AssertionError("target divisor did not reconstruct the normal tail scale")
    if (
        bridge_factor <= 0
        or (4 * K * K) % bridge_factor
        or bridge_factor % R != 1
        or bridge_factor % 2
        or bridge_factor > 4 * K - 2 * R
    ):
        return None

    numerator = 4 * K - bridge_factor
    if numerator % R:
        raise AssertionError("bridge factor residue did not reconstruct a source")
    source_denominator = numerator // R
    if not 2 <= source_denominator < prime or source_denominator % 2:
        raise AssertionError("accepted bridge factor did not give a strict even source")
    if (source_denominator * K) % bridge_factor:
        raise AssertionError("bridge factor did not divide nK")

    source_first = source_denominator * K // bridge_factor
    second_target = x * K // target_divisor
    if target_divisor * second_target != x * K:
        raise AssertionError("target divisor did not reconstruct the second target term")
    target_solution = (x, second_target, prime * K)
    source_solution = (source_first, x, second_target)
    if Fraction(4, prime) != sum(
        (Fraction(1, value) for value in target_solution), Fraction()
    ):
        raise AssertionError("target identity did not verify")
    if Fraction(4, source_denominator) != sum(
        (Fraction(1, value) for value in source_solution), Fraction()
    ):
        raise AssertionError("source identity did not verify")
    return {
        "prime": prime,
        "gap": gap,
        "x": x,
        "target_divisor": target_divisor,
        "R": R,
        "K": K,
        "bridge_factor": bridge_factor,
        "source_denominator": source_denominator,
        "target_solution": target_solution,
        "source_solution": source_solution,
    }


def serialize_witness(witness: dict[str, object]) -> dict[str, object]:
    """Convert tuple-valued solutions to JSON-compatible lists."""
    return {
        key: list(value) if key.endswith("solution") else value
        for key, value in witness.items()
    }
