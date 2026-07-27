#!/usr/bin/env python3
"""Audit the local sieve geometry for pure-new canonical Type II fans."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SCRIPT = ROOT / "reproductions" / "type_ii_canonical_ray.py"
RESULTS = ROOT / "reproductions" / "type-ii-pure-new-canonical-fan-sieve-results.json"
H19_BOUND = 19


def load_canonical_script():
    """Load the repository's canonical shift parametrization."""
    spec = importlib.util.spec_from_file_location(
        "type_ii_pure_new_canonical_fan_canonical", CANONICAL_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_canonical_ray.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


canonical = load_canonical_script()


def primes_up_to(limit: int) -> list[int]:
    """Return all primes up to an inclusive positive limit."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                ((limit - prime * prime) // prime) + 1
            )
    return [prime for prime in range(2, limit + 1) if sieve[prime]]


def euler_phi(value: int) -> int:
    """Compute Euler's totient by exact trial division."""
    if value < 1:
        raise ValueError("value must be positive")
    result = value
    remaining = value
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            result -= result // factor
            while remaining % factor == 0:
                remaining //= factor
        factor = 3 if factor == 2 else factor + 2
    if remaining > 1:
        result -= result // remaining
    return result


def canonical_modulus(shift: int) -> int:
    """Return the canonical Type II modulus associated with one shift."""
    a, c = canonical.canonical_pair(shift)
    return 4 * a * c


def h19_newness_guard(shift: int, shift_bound: int) -> int:
    """Return the strict prime lower bound ensuring H19-newness."""
    if shift_bound <= H19_BOUND or not H19_BOUND < shift <= shift_bound:
        raise ValueError("require 19 < shift <= shift bound")
    guard = 4 * shift_bound
    for base_shift in range(1, H19_BOUND + 1):
        difference = shift - base_shift
        if difference == 0 or abs(4 * difference) >= guard:
            raise AssertionError("newness guard is not strict")
    return guard


def eligible_shifts(prime: int, shift_bound: int) -> tuple[int, ...]:
    """Return canonical shifts whose single-prime ray accepts prime."""
    if shift_bound <= H19_BOUND or prime <= 4 * shift_bound:
        raise ValueError("prime and shift bound must meet the strict guard")
    return tuple(
        shift
        for shift in range(H19_BOUND + 1, shift_bound + 1)
        if prime % canonical_modulus(shift) == canonical_modulus(shift) - 1
    )


def forbidden_roots(prime: int, shift_bound: int) -> tuple[int, ...]:
    """Return the exact roots excluded when all pure-new fan rays fail."""
    shifts = eligible_shifts(prime, shift_bound)
    roots = (0,) + tuple((-4 * shift) % prime for shift in shifts)
    if len(set(roots)) != len(roots):
        raise AssertionError("large-prime canonical-fan roots must be distinct")
    for shift, root in zip(shifts, roots[1:]):
        if (root + 4 * shift) % prime:
            raise AssertionError("root did not encode shifted divisibility")
        if prime <= h19_newness_guard(shift, shift_bound):
            raise AssertionError("prime did not meet the H19-newness guard")
    return roots


def reciprocal_phi_sum(shift_bound: int) -> Fraction:
    """Return the exact single-prime reciprocal-totient mass of the fan."""
    if shift_bound <= H19_BOUND:
        raise ValueError("shift bound must exceed the H19 base window")
    return sum(
        (
            Fraction(1, euler_phi(canonical_modulus(shift)))
            for shift in range(H19_BOUND + 1, shift_bound + 1)
        ),
        Fraction(),
    )


def harmonic_lower_bound(shift_bound: int) -> Fraction:
    """Return the elementary lower bound sum 1/(4s) for the fan mass."""
    if shift_bound <= H19_BOUND:
        raise ValueError("shift bound must exceed the H19 base window")
    return sum(
        (Fraction(1, 4 * shift) for shift in range(H19_BOUND + 1, shift_bound + 1)),
        Fraction(),
    )


def local_geometry(shift_bound: int, prime_bound: int) -> dict[str, object]:
    """Audit roots, H19 guards, and reciprocal mass through one fan size."""
    if shift_bound <= H19_BOUND:
        raise ValueError("shift bound must exceed the H19 base window")
    guard = 4 * shift_bound
    if prime_bound <= guard:
        raise ValueError("prime bound must exceed 4*shift bound")
    root_histogram: Counter[int] = Counter()
    samples: list[dict[str, object]] = []
    checked_prime_count = 0
    harmonic_weight = 0.0
    for prime in primes_up_to(prime_bound):
        if prime <= guard:
            continue
        roots = forbidden_roots(prime, shift_bound)
        root_histogram[len(roots)] += 1
        checked_prime_count += 1
        harmonic_weight += len(roots) / prime
        if len(samples) < 12 and len(roots) > 1:
            shifts = eligible_shifts(prime, shift_bound)
            samples.append(
                {
                    "prime": prime,
                    "eligible_shifts": list(shifts),
                    "roots_mod_prime": list(roots),
                }
            )
    reciprocal_sum = reciprocal_phi_sum(shift_bound)
    lower_sum = harmonic_lower_bound(shift_bound)
    if reciprocal_sum < lower_sum:
        raise AssertionError("reciprocal mass lost its elementary lower bound")
    return {
        "shift_bound": shift_bound,
        "h19_bound": H19_BOUND,
        "strict_prime_guard": guard,
        "prime_bound": prime_bound,
        "checked_prime_count": checked_prime_count,
        "all_roots_distinct": True,
        "all_large_primes_h19_new": True,
        "reciprocal_phi_sum": {
            "numerator": str(reciprocal_sum.numerator),
            "denominator": str(reciprocal_sum.denominator),
            "float": float(reciprocal_sum),
        },
        "harmonic_lower_bound": {
            "numerator": str(lower_sum.numerator),
            "denominator": str(lower_sum.denominator),
            "float": float(lower_sum),
        },
        "root_count_histogram": {
            str(count): frequency for count, frequency in sorted(root_histogram.items())
        },
        "harmonic_forbidden_root_weight": harmonic_weight,
        "samples": samples,
    }


def run_report(bounds: tuple[int, ...], prime_bound: int) -> dict[str, object]:
    """Build finite local checks for several canonical fan sizes."""
    if not bounds:
        raise ValueError("at least one shift bound is required")
    return {
        "arithmetic": (
            "exact canonical squarefree decomposition, prime congruence roots, "
            "H19 newness guards, and rational reciprocal-totient sums"
        ),
        "scope_note": (
            "This checks the local geometry used by the pure-new canonical-fan "
            "upper-bound sieve. It is not a finite coverage claim."
        ),
        "geometries": [local_geometry(bound, prime_bound) for bound in bounds],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bounds", type=int, nargs="+", default=[50, 100, 1008])
    parser.add_argument("--prime-bound", type=int, default=100_000)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_report(tuple(args.bounds), args.prime_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
