#!/usr/bin/env python3
"""Audit the local sieve geometry for pure-new Type II square rays.

For 5 <= r <= R, the canonical square ray has s=r^2, (A,C)=(r,1),
and modulus 4*r.  A prime q > 4*R^2 with

    q | p + 4*r^2,  q == -1 (mod 4*r)

is a pure-new H19 factor: it cannot also divide p+4*t for 1 <= t <= 19.
This script checks the exact forbidden-root geometry used by the associated
growing-sieve proof.  It does not itself prove a density estimate.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-pure-new-square-ray-sieve-results.json"
H19_BOUND = 19


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


def square_ray_modulus(radius: int) -> int:
    """Return the canonical Type II modulus for the square shift radius^2."""
    if radius < 1:
        raise ValueError("radius must be positive")
    return 4 * radius


def h19_newness_guard(radius: int, radius_bound: int) -> int:
    """Return a strict prime lower bound guaranteeing H19-newness.

    For radius >= 5, radius^2-t is nonzero and has absolute value below
    radius_bound^2 for every H19 shift 1 <= t <= 19.  Any prime greater than
    4*radius_bound^2 therefore cannot divide both shifted integers.
    """
    if radius_bound < 5 or not 5 <= radius <= radius_bound:
        raise ValueError("require 5 <= radius <= radius_bound")
    guard = 4 * radius_bound * radius_bound
    for source_shift in range(1, H19_BOUND + 1):
        difference = radius * radius - source_shift
        if difference == 0 or abs(4 * difference) >= guard:
            raise AssertionError("newness guard is not strict")
    return guard


def eligible_square_radii(prime: int, radius_bound: int) -> tuple[int, ...]:
    """Return r for which prime has the pure square-ray residue."""
    if prime <= 4 * radius_bound * radius_bound:
        raise ValueError("prime must exceed the strict root/newness guard")
    return tuple(
        radius
        for radius in range(5, radius_bound + 1)
        if prime % square_ray_modulus(radius) == square_ray_modulus(radius) - 1
    )


def forbidden_roots(prime: int, radius_bound: int) -> tuple[int, ...]:
    """Return exact p-residue roots excluded by pure-new square-ray failure.

    The zero root sieves primality of p.  Each nonzero root says that the
    corresponding eligible prime cannot divide p+4*r^2 when every pure-new
    square ray fails.
    """
    radii = eligible_square_radii(prime, radius_bound)
    roots = (0,) + tuple((-4 * radius * radius) % prime for radius in radii)
    if len(set(roots)) != len(roots):
        raise AssertionError("large-prime square-ray roots must be distinct")
    for radius, root in zip(radii, roots[1:]):
        if (root + 4 * radius * radius) % prime:
            raise AssertionError("root did not encode the shifted divisibility")
        if prime <= h19_newness_guard(radius, radius_bound):
            raise AssertionError("prime did not meet the newness guard")
    return roots


def reciprocal_phi_sum(radius_bound: int) -> Fraction:
    """Return sum_{5 <= r <= R} 1/phi(4r) exactly."""
    if radius_bound < 5:
        raise ValueError("radius_bound must be at least five")
    return sum(
        (Fraction(1, euler_phi(square_ray_modulus(radius))) for radius in range(5, radius_bound + 1)),
        Fraction(),
    )


def local_geometry(radius_bound: int, prime_bound: int) -> dict[str, object]:
    """Audit every sieving prime in the stated finite interval."""
    if radius_bound < 5:
        raise ValueError("radius_bound must be at least five")
    guard = 4 * radius_bound * radius_bound
    if prime_bound <= guard:
        raise ValueError("prime_bound must exceed 4*radius_bound^2")

    root_histogram: Counter[int] = Counter()
    prime_count = 0
    harmonic_weight = 0.0
    samples: list[dict[str, object]] = []
    for prime in primes_up_to(prime_bound):
        if prime <= guard:
            continue
        roots = forbidden_roots(prime, radius_bound)
        root_count = len(roots)
        root_histogram[root_count] += 1
        prime_count += 1
        harmonic_weight += root_count / prime
        if len(samples) < 12 and root_count > 1:
            radii = eligible_square_radii(prime, radius_bound)
            samples.append(
                {
                    "prime": prime,
                    "eligible_radii": list(radii),
                    "roots_mod_prime": list(roots),
                }
            )

    reciprocal_sum = reciprocal_phi_sum(radius_bound)
    return {
        "radius_bound": radius_bound,
        "h19_bound": H19_BOUND,
        "strict_prime_guard": guard,
        "prime_bound": prime_bound,
        "checked_prime_count": prime_count,
        "all_roots_distinct": True,
        "all_large_primes_h19_new": True,
        "reciprocal_phi_sum": {
            "numerator": reciprocal_sum.numerator,
            "denominator": reciprocal_sum.denominator,
            "float": float(reciprocal_sum),
        },
        "root_count_histogram": {
            str(count): frequency for count, frequency in sorted(root_histogram.items())
        },
        "harmonic_forbidden_root_weight": harmonic_weight,
        "samples": samples,
    }


def run_report(bounds: tuple[int, ...], prime_bound: int) -> dict[str, object]:
    """Build finite local checks for several square-ray radii."""
    if not bounds:
        raise ValueError("at least one radius bound is required")
    return {
        "arithmetic": (
            "exact prime sieve, congruence roots, H19 newness guards, and rational "
            "reciprocal-totient sums"
        ),
        "scope_note": (
            "This checks the local root geometry used by the pure-new square-ray "
            "upper-bound sieve. It is not a finite coverage claim."
        ),
        "geometries": [local_geometry(bound, prime_bound) for bound in bounds],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bounds", type=int, nargs="+", default=[10, 20, 50])
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
