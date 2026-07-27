#!/usr/bin/env python3
"""Audit pure-new single-prime Type II witnesses on canonical square rays."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE_SCRIPT = ROOT / "reproductions" / "type_ii_single_new_factor_release.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-pure-new-square-ray-1b-results.json"


def load_release_script():
    """Load the established exact factorization and certificate helpers."""
    spec = importlib.util.spec_from_file_location(
        "type_ii_h19_pure_new_square_ray_release", RELEASE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_single_new_factor_release.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


single = load_release_script()
transition = single.transition


def sequence_radius_cap(prime: int) -> int:
    """Return the largest radius not excluded by the Type II order condition.

    For A=r and C=1, the raw-ray order condition has numerator
    K*(p-4*r^2)+2*r.  Since K is positive, it is negative for every K once
    4*r^2-2*r exceeds p.
    """
    if prime < 1:
        raise ValueError("prime must be positive")
    radius = (1 + math.isqrt(1 + 4 * prime)) // 4
    while 4 * (radius + 1) * (radius + 1) - 2 * (radius + 1) <= prime:
        radius += 1
    while 4 * radius * radius - 2 * radius > prime:
        radius -= 1
    return radius


def pure_new_square_witness(
    prime: int, radius: int, old_source_primes: set[int], trial_primes: list[int]
) -> dict[str, int] | None:
    """Return the smallest H19-new prime certificate on shift radius squared."""
    if radius < 5:
        raise ValueError("radius must be at least five")
    modulus = 4 * radius
    candidates: list[dict[str, int]] = []
    for factor in single.factorization(prime + 4 * radius * radius, trial_primes):
        if factor in old_source_primes or factor % modulus != modulus - 1:
            continue
        certificate = transition.canonical.ray.short_certificate.type_ii_raw_ray_certificate(
            prime, radius, 1, (factor + 1) // modulus
        )
        if certificate is None:
            continue
        candidates.append(
            {
                "h": factor,
                "radius": radius,
                "shift": radius * radius,
                "a": radius,
                "c": 1,
                "k": (factor + 1) // modulus,
                "gap": certificate.gap,
                "divisor": certificate.divisor,
            }
        )
    return min(candidates, key=lambda row: row["h"]) if candidates else None


def run_profile(payload: dict[str, object], radius_cap: int) -> dict[str, object]:
    """Audit every H19 new-factor state through the stated square-ray radius."""
    if radius_cap < 5:
        raise ValueError("radius cap must be at least five")
    limit = int(payload["prime_limit"])
    base_shift_bound = int(payload["base_shift_bound"])
    targets = [
        row
        for row in payload["profiles"]
        if int(row["selected_witness"]["new_multiplicity"]) > 0
    ]
    trial_primes = single.primes_through(math.isqrt(limit + 4 * radius_cap * radius_cap))
    base_pairs = tuple(
        transition.canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    profiles: list[dict[str, object]] = []
    missing: list[int] = []
    order_exhausted_missing: list[int] = []
    cap_truncated_missing: list[int] = []
    maximum_sequence_radius_bound = 0
    for row in targets:
        prime = int(row["prime"])
        natural_radius_cap = sequence_radius_cap(prime)
        maximum_sequence_radius_bound = max(
            maximum_sequence_radius_bound, natural_radius_cap
        )
        search_cap = min(radius_cap, natural_radius_cap)
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in single.factorization(prime + 4 * a * a * c, trial_primes)
        }
        selected = None
        for radius in range(5, search_cap + 1):
            selected = pure_new_square_witness(
                prime, radius, old_source_primes, trial_primes
            )
            if selected is not None:
                profiles.append(
                    {
                        "prime": prime,
                        "first_pure_new_square_radius": radius,
                        "selected_witness": selected,
                    }
                )
                break
        if selected is None:
            missing.append(prime)
            if search_cap == natural_radius_cap:
                order_exhausted_missing.append(prime)
            else:
                cap_truncated_missing.append(prime)
    radii = Counter(row["first_pure_new_square_radius"] for row in profiles)
    return {
        "arithmetic": (
            "exact trial-prime factorization of p+4r^2, exact H19 source-label "
            "comparison, and reconstructed Type II raw-ray certificate checks"
        ),
        "scope_note": (
            "A finite audit of the restrictive square-ray subfamily A=r, C=1. "
            "It neither proves a uniform radius nor covers H19 collision-only states."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "radius_cap": radius_cap,
        "shift_cap": radius_cap * radius_cap,
        "maximum_sequence_radius_bound": maximum_sequence_radius_bound,
        "new_factor_state_count": len(targets),
        "pure_new_square_ray_count": len(profiles),
        "missing_through_radius_cap": missing,
        "order_exhausted_missing": order_exhausted_missing,
        "cap_truncated_missing": cap_truncated_missing,
        "first_radius_histogram": {
            str(radius): count for radius, count in sorted(radii.items())
        },
        "maximum_first_radius": max(radii, default=None),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--radius-cap", type=int, default=100)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_profile(payload, args.radius_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
