#!/usr/bin/env python3
"""Verify the target source-supply spectrum and strict adapter controls."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def factorint(value: int) -> dict[int, int]:
    """Return the prime factorization of a positive integer."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors: dict[int, int] = {}
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def divisors(value: int) -> tuple[int, ...]:
    """Return positive divisors in increasing order."""
    lower: list[int] = []
    upper: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        lower.append(divisor)
        if divisor * divisor != value:
            upper.append(value // divisor)
    return tuple(lower + list(reversed(upper)))


def target_supply_spectrum(
    source_values: dict[int, int], target_value: int, modulus: int
) -> dict[str, object]:
    """Compute the exact owner-height spectrum for one declared source profile."""
    target_factors = factorint(target_value)
    heights: dict[int, int] = {}
    owners: dict[int, int] = {}
    for source_label, source_value in source_values.items():
        for prime, exponent in factorint(source_value).items():
            if prime == 2 or gcd(prime, modulus) != 1:
                continue
            common_height = min(exponent, target_factors.get(prime, 0))
            if common_height > heights.get(prime, 0):
                heights[prime] = common_height
                owners[prime] = source_label

    envelope = 1
    for prime, exponent in sorted(heights.items()):
        envelope *= prime**exponent
    height_spectrum = tuple(divisors(envelope))
    strict_residues = tuple(
        sorted({value % modulus for value in height_spectrum if value > 1})
    )
    return {
        "heights": heights,
        "owners": owners,
        "envelope": envelope,
        "height_spectrum": height_spectrum,
        "strict_residues": strict_residues,
    }


def type_ii_certificate(
    prime: int, target_layer: int, target_a: int, factor: int
) -> tuple[int, int, int]:
    """Return (K, B, C) for a target-layer Type II normal form."""
    modulus = 4 * target_layer
    if factor <= 1 or factor % modulus != modulus - 1:
        raise ValueError("factor is not a strict Type II congruence witness")
    target_value = prime + 4 * target_layer * target_a
    if target_value % factor:
        raise ValueError("factor does not divide the target denominator")
    K = (factor + 1) // modulus
    numerator = K * prime + target_a
    if numerator % factor:
        raise ValueError("normal-form numerator is not divisible")
    B = numerator // factor
    C = target_layer // target_a
    assert factor == 4 * target_a * C * K - 1
    assert B > target_a
    return K, B, C


def raw_candidates(prime: int, factor: int) -> tuple[tuple[int, int, int, int], ...]:
    """Enumerate the finite raw Type II triples for one Hall factor."""
    if factor <= 1 or factor % 4 != 3:
        return ()
    L = (factor + 1) // 4
    candidates: list[tuple[int, int, int, int]] = []
    for a in divisors(L):
        remainder = L // a
        for c in divisors(remainder):
            k = remainder // c
            numerator = k * prime + a
            if numerator % factor:
                continue
            b = numerator // factor
            if a <= b:
                candidates.append((a, c, k, b))
    return tuple(candidates)


def run_verification() -> dict[str, object]:
    # Positive exact spectrum: both 7 and 17 are target-supported, and 7 is 3 mod 4.
    p_positive = 5_113
    positive_sources = {3: p_positive + 24 * 3, 6: p_positive + 24 * 6}
    positive_target = p_positive + 4
    positive = target_supply_spectrum(positive_sources, positive_target, 4)
    assert positive_sources == {3: 5_185, 6: 5_257}
    assert positive_target == 5_117
    assert positive["heights"] == {17: 1, 7: 1}
    assert positive["owners"] == {17: 3, 7: 6}
    assert positive["envelope"] == 119
    assert positive["height_spectrum"] == (1, 7, 17, 119)
    assert positive["strict_residues"] == (1, 3)
    assert type_ii_certificate(p_positive, 1, 1, 7) == (2, 1_461, 1)
    assert type_ii_certificate(p_positive, 1, 1, 119) == (30, 1_289, 1)

    # Negative exact spectrum: the complete D=41 profile supplies only q=5.
    p_negative = 57_399_241
    negative_sources = {
        1: p_negative + 4 * 41,
        41: p_negative + 4 * 41 * 41,
    }
    negative_target = p_negative + 4
    negative = target_supply_spectrum(negative_sources, negative_target, 4)
    assert negative_sources == {1: 57_399_405, 41: 57_405_965}
    assert negative_target == 57_399_245
    assert negative["heights"] == {5: 1}
    assert negative["owners"] == {5: 1}
    assert negative["envelope"] == 5
    assert negative["height_spectrum"] == (1, 5)
    assert negative["strict_residues"] == (1,)
    assert all(prime % 4 == 1 for prime in negative["heights"])
    assert tuple(
        gcd(source_value, negative_target)
        for source_value in negative_sources.values()
    ) == (5, 5)

    # Raw fallback: the old D=1 divisor fiber is empty, but raw is nonempty.
    p_raw = 73
    d0 = 1
    a0 = 8
    h_raw = 15
    assert h_raw % 4 == 3
    assert (p_raw + 4 * d0 * a0) % h_raw == 0
    old_divisor_candidates = [
        a for a in divisors(d0) if a % h_raw == a0 % h_raw
    ]
    assert old_divisor_candidates == []
    raw = raw_candidates(p_raw, h_raw)
    assert raw == ((2, 2, 1, 5),)
    a_raw, c_raw, k_raw, b_raw = raw[0]
    assert h_raw == 4 * a_raw * c_raw * k_raw - 1
    assert h_raw * b_raw == k_raw * p_raw + a_raw

    return {
        "positive": {
            "state": {"p": p_positive, "D": 6, "target": [1, 1]},
            "supply_heights": positive["heights"],
            "owners": positive["owners"],
            "envelope": positive["envelope"],
            "height_spectrum": positive["height_spectrum"],
            "strict_witnesses": {
                7: type_ii_certificate(p_positive, 1, 1, 7),
                119: type_ii_certificate(p_positive, 1, 1, 119),
            },
            "status": "STRICT_ARITHMETIC_ADAPTER",
        },
        "negative": {
            "state": {"p": p_negative, "D": 41, "target": [1, 1]},
            "supply_heights": negative["heights"],
            "owners": negative["owners"],
            "envelope": negative["envelope"],
            "height_spectrum": negative["height_spectrum"],
            "strict_witnesses": (),
            "status": "STRICT_LAYER_MOD4_OBSTRUCTED",
        },
        "raw": {
            "state": {"p": p_raw, "D0": d0, "a0": a0, "h": h_raw},
            "old_divisor_candidates": old_divisor_candidates,
            "raw_candidates": raw,
            "status": "RAW_TYPE_II_TERMINAL",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified target source-supply spectrum and strict adapter controls")
    for branch in ("positive", "negative", "raw"):
        print(branch, result[branch]["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
