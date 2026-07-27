#!/usr/bin/env python3
"""Reconstruct Type I even terminal bridges from two ordinary divisor pairs.

The target-side square divisor and the terminal square divisor admit compatible
coprime-pair normalizations.  For ``x = (p + m) / 4``, the first pair ``(A, B)``
selects the Type I normal form; the second pair ``(u, v)`` selects the terminal
factor from ``L = 2K``.  No square divisor needs to be searched explicitly.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def terminal_witness_from_divisor_pairs(
    prime: int,
    gap: int,
    target_a: int,
    target_b: int,
    bridge_u: int,
    bridge_v: int,
) -> dict[str, object] | None:
    """Return the bridge encoded by target and terminal ordinary divisor pairs.

    ``(target_a, target_b)`` is the coprime Type I pair ``(A, B)``.  The
    coprime pair ``(bridge_u, bridge_v)`` is the reduced quotient ``E / L``
    for ``L = 2K``.
    """
    if prime % 24 != 1 or gap % 4 != 3 or not 3 <= gap <= prime - 2:
        return None
    if min(target_a, target_b, bridge_u, bridge_v) <= 0:
        return None

    x = (prime + gap) // 4
    if 4 * x != prime + gap or gcd(target_a, target_b) != 1:
        return None
    if x % (target_a * target_b) or (target_b * prime + target_a) % gap:
        return None

    target_c = x // (target_a * target_b)
    target_divisor = target_b * target_b * target_c
    if x * x % target_divisor or (4 * target_divisor + 1) % gap:
        raise AssertionError("target divisor pair did not recover the Type I state")

    R = (4 * target_divisor + 1) // gap
    H = target_a * R - target_b
    K = target_b * target_c * H
    if R <= 0 or H <= 0 or K <= 0 or 4 * K != prime * R + 1:
        raise AssertionError("target divisor pair did not recover the normal tail")

    L = 2 * K
    if gcd(bridge_u, bridge_v) != 1 or L % bridge_u or L % bridge_v:
        return None
    if (bridge_u - 2 * bridge_v) % R:
        return None

    bridge_factor = L * bridge_u // bridge_v
    if (
        bridge_factor % 2
        or bridge_factor > 2 * L - 2 * R
        or (L * L) % bridge_factor
        or bridge_factor % R != 1
    ):
        return None

    source_numerator = 2 * L - bridge_factor
    if source_numerator % R:
        raise AssertionError("terminal pair did not recover a source denominator")
    source_denominator = source_numerator // R
    if not 2 <= source_denominator < prime or source_denominator % 2:
        return None
    if (source_denominator * K) % bridge_factor:
        raise AssertionError("terminal pair did not recover an integral source term")

    source_first = source_denominator * K // bridge_factor
    second_target = target_a * target_c * H
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
        "target_pair": (target_a, target_b),
        "target_c": target_c,
        "target_divisor": target_divisor,
        "R": R,
        "H": H,
        "K": K,
        "L": L,
        "bridge_pair": (bridge_u, bridge_v),
        "bridge_factor": bridge_factor,
        "source_denominator": source_denominator,
        "target_solution": target_solution,
        "source_solution": source_solution,
    }
