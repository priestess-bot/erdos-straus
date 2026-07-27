#!/usr/bin/env python3
"""Exact collision-state decomposition for a finite canonical Type II fan.

For distinct shifts s and t, gcd(p+4s, p+4t) divides s-t.  Thus all
cross-ray common prime factors lie in one finite, shift-dependent set.  This
script separates those factors from the pairwise-coprime private cofactors
and verifies the corresponding product-residue decomposition on the common
misses of a small canonical fan.
"""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-canonical-collision-1m-results.json"
CANONICAL_SCRIPT = ROOT / "reproductions" / "type_ii_canonical_ray.py"


def load_canonical_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_canonical_ray", CANONICAL_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_canonical_ray.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


canonical = load_canonical_script()
residue = canonical.residue_structure


def distinct_prime_factors(value: int) -> tuple[int, ...]:
    """Return the distinct prime factors of a positive integer."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append(value)
    return tuple(factors)


def collision_primes(shifts: tuple[int, ...]) -> tuple[int, ...]:
    """Primes that can divide two different shifted integers in the fan."""
    if len(shifts) < 2 or len(set(shifts)) != len(shifts) or min(shifts) < 1:
        raise ValueError("shifts must be at least two distinct positive integers")
    return tuple(
        sorted(
            {
                prime
                for index, left in enumerate(shifts)
                for right in shifts[index + 1 :]
                for prime in distinct_prime_factors(abs(right - left))
            }
        )
    )


def split_factorization(
    factorization: tuple[tuple[int, int], ...], collision_set: set[int]
) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
    """Split a factorization into collision-prime and private-prime parts."""
    shared = tuple(
        (prime, exponent)
        for prime, exponent in factorization
        if prime in collision_set
    )
    private = tuple(
        (prime, exponent)
        for prime, exponent in factorization
        if prime not in collision_set
    )
    return shared, private


def residue_products(
    factorization: tuple[tuple[int, int], ...], modulus: int
) -> frozenset[int]:
    return residue.divisor_residues_from_factorization(factorization, modulus)


def collision_profile_for_prime(
    prime: int,
    pairs: tuple[tuple[int, int], ...],
    smallest_factors: list[int],
    collision_set: set[int],
) -> dict[str, object]:
    """Verify the finite-state/private-factor decomposition for one prime."""
    rows: list[dict[str, object]] = []
    private_values: list[int] = []
    for a, c in pairs:
        shift = a * a * c
        modulus = 4 * a * c
        shifted = prime + 4 * shift
        factorization = residue.factorization_from_spf(shifted, smallest_factors)
        shared, private = split_factorization(factorization, collision_set)
        shared_residues = residue_products(shared, modulus)
        private_residues = residue_products(private, modulus)
        full_residues = residue_products(factorization, modulus)
        reconstructed = frozenset(
            left * right % modulus
            for left in shared_residues
            for right in private_residues
        )
        if reconstructed != full_residues:
            raise AssertionError("residue product decomposition failed")
        target = modulus - 1
        forbidden_private_targets = frozenset(
            (-pow(value, -1, modulus)) % modulus for value in shared_residues
        )
        if target in full_residues:
            raise AssertionError("profile input must be a common fan failure")
        if forbidden_private_targets & private_residues:
            raise AssertionError("failed ray contains a target product")
        private_value = math.prod(
            factor**exponent for factor, exponent in private
        )
        private_values.append(private_value)
        rows.append(
            {
                "pair": {"a": a, "c": c},
                "shift_index": shift,
                "modulus": modulus,
                "shifted": shifted,
                "collision_factorization": shared,
                "private_factorization": private,
                "collision_residue_count": len(shared_residues),
                "private_residue_count": len(private_residues),
                "full_residue_count": len(full_residues),
                "forbidden_private_target_count": len(forbidden_private_targets),
            }
        )
    return {
        "prime": prime,
        "private_cofactors_pairwise_coprime": all(
            math.gcd(left, right) == 1
            for index, left in enumerate(private_values)
            for right in private_values[index + 1 :]
        ),
        "rays": rows,
    }


def run_profile(limit: int, base_shift_bound: int) -> dict[str, object]:
    if limit < 73 or base_shift_bound < 2:
        raise ValueError("limit >= 73 and base_shift_bound >= 2 are required")
    pairs = tuple(
        sorted(
            {
                canonical.canonical_pair(shift)
                for shift in range(1, base_shift_bound + 1)
            }
        )
    )
    shifts = tuple(sorted(a * a * c for a, c in pairs))
    collision = collision_primes(shifts)
    max_shift = max(shifts)
    smallest_factors = canonical.ray.short_certificate.smallest_prime_factors(
        limit + 4 * max_shift
    )
    core_primes = [
        prime
        for prime in canonical.ray.short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    misses = [
        prime
        for prime in core_primes
        if all(
            canonical.witness_for_pair(prime, pair, smallest_factors) is None
            for pair in pairs
        )
    ]
    profiles = [
        collision_profile_for_prime(prime, pairs, smallest_factors, set(collision))
        for prime in misses
    ]
    if not all(profile["private_cofactors_pairwise_coprime"] for profile in profiles):
        raise AssertionError("private cofactors must be pairwise coprime")
    collision_factor_histogram = Counter(
        prime
        for profile in profiles
        for row in profile["rays"]
        for prime, _ in row["collision_factorization"]
    )
    return {
        "arithmetic": (
            "exact SPF factorization and complete divisor-residue product sets"
        ),
        "scope_note": (
            "This separates finite shared-factor states from private factors. It "
            "does not establish an incompatibility among the private factor residues."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "canonical_pairs": [{"a": a, "c": c} for a, c in pairs],
        "shifts": shifts,
        "collision_primes": collision,
        "core_prime_count": len(core_primes),
        "common_failure_count": len(misses),
        "common_failures": misses,
        "all_private_cofactors_pairwise_coprime": True,
        "collision_factor_occurrences": dict(sorted(collision_factor_histogram.items())),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--base-shift-bound", type=int, default=14)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_profile(args.limit, args.base_shift_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
