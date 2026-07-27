#!/usr/bin/env python3
"""Construct the canonical n=p-m even bridge of a Type I normal form."""

from __future__ import annotations

from fractions import Fraction


def gap_source_even_bridge(
    prime: int, gap: int, A: int, B: int, C: int
) -> dict[str, int] | None:
    """Return the n=p-m bridge exactly when its square condition holds.

    A Type I normal form has p=4ABC-m and mR=4B^2C+1.  Setting n=p-m
    forces E=4K-nR=mR+1.  This routine implements the equivalent
    condition 2B^2C+1 | (A+mB)^2 and verifies both unit-fraction
    identities on a hit.
    """
    if min(prime, gap, A, B, C) <= 0 or gap % 4 != 3:
        raise ValueError("parameters must be positive with gap=3 mod 4")
    if prime != 4 * A * B * C - gap:
        raise ValueError("normal form does not reconstruct its prime")
    numerator_R = 4 * B * B * C + 1
    if numerator_R % gap:
        raise ValueError("normal form does not have an integral R")
    R = numerator_R // gap
    H = A * R - B
    K = B * C * H
    if H <= 0 or 4 * K != prime * R + 1:
        raise ValueError("normal form does not reconstruct its p-tail")
    source = prime - gap
    E = gap * R + 1
    U = E // 2
    if E % 2 or source < 2 or source % 2:
        raise AssertionError("canonical gap source did not have required parity")
    condition = (A + gap * B) ** 2 % U == 0
    square_bridge = (4 * K * K) % E == 0
    if condition != square_bridge:
        raise AssertionError("gap-source square condition was not equivalent")
    if not condition:
        return None
    if E > 4 * K - 2 * R or (source * K) % E:
        raise AssertionError("canonical bridge did not reconstruct an integer source")
    source_term = source * K // E
    target = (A * B * C, A * C * H, prime * K)
    source_solution = (source_term, target[0], target[1])
    if Fraction(4, prime) != sum((Fraction(1, term) for term in target), Fraction()):
        raise AssertionError("target identity did not verify")
    if Fraction(4, source) != sum(
        (Fraction(1, term) for term in source_solution), Fraction()
    ):
        raise AssertionError("source identity did not verify")
    return {
        "R": R,
        "K": K,
        "bridge_factor": E,
        "source_denominator": source,
        "source_term": source_term,
    }
