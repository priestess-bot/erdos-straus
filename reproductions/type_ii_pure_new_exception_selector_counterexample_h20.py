#!/usr/bin/env python3
"""Independently exhaust three H=20 counterexamples to Selector-Enew.

This module deliberately does not import the dynamic-selector implementation.
It uses SymPy's complete divisor lists directly for every q|B and k|B, so a
result here independently checks the primary SPF-based search.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import prod
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
COUNTEREXAMPLE_PRIMES = (214_729, 297_049, 878_089)
SHIFT_BOUND = 20
H19_BOUND = 19
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-ii-pure-new-exception-selector-counterexample-1m-h20.json"
)


def factorization(value: int) -> list[list[int]]:
    """Return a JSON-stable prime factorization of a positive integer."""
    return [
        [int(prime), int(exponent)]
        for prime, exponent in sorted(sympy.factorint(value).items())
    ]


def prime_support(value: int) -> set[int]:
    """Return the exact prime support without using repository factor helpers."""
    return {int(prime) for prime in sympy.factorint(value)}


def canonical_modulus(shift: int) -> int:
    """Independently calculate 4*a*c for shift=a^2*c with c squarefree."""
    factors = sympy.factorint(shift)
    square_part = prod(
        int(prime) ** (int(exponent) // 2)
        for prime, exponent in factors.items()
    )
    squarefree_part = shift // (square_part * square_part)
    return 4 * square_part * squarefree_part


def pure_new_audit(prime: int) -> dict[str, object]:
    """Check the exact E_new(prime, 20) condition from its definition."""
    old_support: set[int] = set()
    for shift in range(1, H19_BOUND + 1):
        old_support.update(prime_support(prime + 4 * shift))

    modulus = canonical_modulus(SHIFT_BOUND)
    shifted = prime + 4 * SHIFT_BOUND
    qualifying_factors = [
        factor
        for factor in sorted(prime_support(shifted))
        if factor % modulus == modulus - 1 and factor not in old_support
    ]
    return {
        "old_support": sorted(old_support),
        "shift": SHIFT_BOUND,
        "canonical_modulus": modulus,
        "shifted_integer": shifted,
        "shifted_factorization": factorization(shifted),
        "qualifying_new_prime_factors": qualifying_factors,
    }


def tail_audit(prime: int) -> dict[str, object]:
    """Exhaust every ordinary Type II divisor, without any support cutoff."""
    base = (prime - 1) // 4
    eligible_divisors = 0
    matching_divisors: list[dict[str, int]] = []
    scales = [int(scale) for scale in sympy.divisors(base)]
    for scale in scales:
        gap = 4 * scale - 1
        x = base + scale
        for divisor in sympy.divisors(x * x):
            divisor = int(divisor)
            if divisor > x:
                continue
            eligible_divisors += 1
            if divisor % gap == (-x) % gap:
                matching_divisors.append(
                    {"scale": scale, "gap": gap, "x": x, "divisor": divisor}
                )
    return {
        "base": base,
        "base_factorization": factorization(base),
        "scale_count": len(scales),
        "eligible_divisor_count": eligible_divisors,
        "matching_divisors": matching_divisors,
    }


def external_audit(prime: int) -> dict[str, object]:
    """Exhaust every complete-square external exit over every k|B."""
    base = (prime - 1) // 4
    eligible_divisors = 0
    matching_divisors: list[dict[str, int]] = []
    scales = [int(scale) for scale in sympy.divisors(base)]
    for scale in scales:
        modulus = 4 * scale - 1
        source = prime - base // scale
        source_product = scale * source
        if modulus * prime + 1 != 4 * scale * source:
            raise AssertionError("external-source normalization failed")
        if not 2 <= source < prime:
            raise AssertionError("external source is not strictly smaller")
        for divisor in sympy.divisors(source_product * source_product):
            divisor = int(divisor)
            if divisor > source_product:
                continue
            eligible_divisors += 1
            if divisor % modulus != (-source_product) % modulus:
                continue
            first_tail, remainder = divmod(source_product + divisor, modulus)
            if remainder or source_product * first_tail % divisor:
                raise AssertionError("square-tail reconstruction failed")
            second_tail = source_product * first_tail // divisor
            if Fraction(4, source) != sum(
                (Fraction(1, value) for value in (source_product, first_tail, second_tail)),
                Fraction(),
            ):
                raise AssertionError("source identity failed")
            if Fraction(4, prime) != sum(
                (
                    Fraction(1, value)
                    for value in (source_product * prime, first_tail, second_tail)
                ),
                Fraction(),
            ):
                raise AssertionError("target identity failed")
            matching_divisors.append(
                {
                    "scale": scale,
                    "source_modulus": modulus,
                    "source_denominator": source,
                    "source_product": source_product,
                    "square_tail_divisor": divisor,
                }
            )
    return {
        "base": base,
        "scale_count": len(scales),
        "eligible_square_divisor_count": eligible_divisors,
        "matching_square_divisors": matching_divisors,
    }


def audit_prime(prime: int) -> dict[str, object]:
    """Produce a complete independent counterexample audit for one prime."""
    if not sympy.isprime(prime) or prime % 24 != 1 or prime <= 4 * SHIFT_BOUND:
        raise ValueError("candidate is not above the strict core-prime boundary")
    pure_new = pure_new_audit(prime)
    tail = tail_audit(prime)
    external = external_audit(prime)
    if pure_new["qualifying_new_prime_factors"]:
        raise AssertionError("candidate is not in E_new(X, 20)")
    if tail["matching_divisors"]:
        raise AssertionError("candidate has a Type II tail after all")
    if external["matching_square_divisors"]:
        raise AssertionError("candidate has an external exit after all")
    return {
        "prime": prime,
        "pure_new": pure_new,
        "dynamic_low_defect_tail": tail,
        "dynamic_external_source_exit": external,
    }


def audit_counterexamples() -> dict[str, object]:
    """Audit all known first H=20 counterexamples independently."""
    return {
        "arithmetic": (
            "independent SymPy factorization and direct complete divisor enumeration; "
            "this script does not import the SPF-based selector implementation"
        ),
        "scope": {
            "prime_limit": 1_000_000,
            "shift_bound": SHIFT_BOUND,
            "max_support_refuted": 2,
        },
        "selector_consequence": (
            "Each listed prime lies in E_new(1000000,20), has no ordinary Type II "
            "tail divisor at any scale, and has no complete-square external exit at "
            "any scale. Thus it refutes the current universal Selector-Enew."
        ),
        "counterexamples": [audit_prime(prime) for prime in COUNTEREXAMPLE_PRIMES],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    report = audit_counterexamples()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
