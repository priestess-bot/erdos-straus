#!/usr/bin/env python3
"""Profile collision-induced target sets inside private Type II product sets.

For a finite canonical fan, write p+4s=E_s R_s after extracting every prime
that can occur in two shifts.  Full-ray failure says that the private divisor
residue set of R_s avoids every target induced by a divisor residue of E_s.
This script records whether those targets lie outside the private support or
inside its missing product set, and verifies the private one-hole congruence
trap exactly.
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
RESULTS = ROOT / "reproductions" / "type-ii-private-product-state-h14-10m-results.json"
COLLISION_SCRIPT = ROOT / "reproductions" / "type_ii_multishift_collision.py"


def load_collision_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_private_state_collision", COLLISION_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_multishift_collision.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


collision = load_collision_script()
canonical = collision.canonical
residue = canonical.residue_structure


def product_residue(
    factorization: tuple[tuple[int, int], ...], modulus: int
) -> int:
    """Return the residue of the whole integer represented by a factorization."""
    return math.prod(prime**exponent for prime, exponent in factorization) % modulus


def euler_phi(value: int) -> int:
    """Return Euler's totient of a positive integer."""
    if value < 1:
        raise ValueError("value must be positive")
    result = value
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            result -= result // divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        result -= result // remaining
    return result


def private_state(
    prime: int,
    pair: tuple[int, int],
    smallest_factors: list[int],
    collision_set: set[int],
) -> dict[str, object]:
    """Return the complete collision/private product-set state of one failed ray."""
    a, c = pair
    shift = a * a * c
    modulus = 4 * a * c
    shifted = prime + 4 * shift
    factorization = residue.factorization_from_spf(shifted, smallest_factors)
    collision_factors, private_factors = collision.split_factorization(
        factorization, collision_set
    )
    collision_residues = residue.divisor_residues_from_factorization(
        collision_factors, modulus
    )
    private_residues = residue.divisor_residues_from_factorization(
        private_factors, modulus
    )
    sequence = tuple(
        factor % modulus
        for factor, exponent in private_factors
        for _ in range(exponent)
    )
    private_support = residue.generated_subgroup(frozenset(sequence), modulus)
    induced_targets = frozenset(
        (-pow(value, -1, modulus)) % modulus for value in collision_residues
    )
    if induced_targets & private_residues:
        raise AssertionError("the ray is not a collision/private failure state")
    inside_targets = induced_targets & private_support
    private_defect = private_support - private_residues
    if not inside_targets.issubset(private_defect):
        raise AssertionError("support targets must be private product-set defects")
    if not inside_targets:
        mode = "all_outside"
    elif induced_targets <= private_support:
        mode = "all_inside"
    else:
        mode = "mixed"

    private_total = product_residue(private_factors, modulus)
    collision_total = product_residue(collision_factors, modulus)
    one_hole_target = None
    one_hole_congruence = None
    if len(private_defect) == 1 and inside_targets:
        one_hole_target = next(iter(private_defect))
        if private_total != one_hole_target * one_hole_target % modulus:
            raise AssertionError("private complement involution did not fix one hole")
        one_hole_congruence = (
            collision_total * one_hole_target * one_hole_target % modulus
        )
        if prime % modulus != one_hole_congruence:
            raise AssertionError("private one-hole congruence trap failed")

    return {
        "prime": prime,
        "pair": {"a": a, "c": c},
        "shift_index": shift,
        "modulus": modulus,
        "shifted": shifted,
        "collision_factorization": collision_factors,
        "private_factorization": private_factors,
        "collision_residue_count": len(collision_residues),
        "private_residue_count": len(private_residues),
        "private_support_size": len(private_support),
        "private_support_index": euler_phi(modulus) // len(private_support),
        "private_support_saturated": private_residues == private_support,
        "private_defect_size": len(private_defect),
        "induced_targets": tuple(sorted(induced_targets)),
        "inside_induced_targets": tuple(sorted(inside_targets)),
        "mode": mode,
        "collision_total_residue": collision_total,
        "private_total_residue": private_total,
        "private_one_hole_target": one_hole_target,
        "private_one_hole_congruence": one_hole_congruence,
    }


def run_profile(limit: int, base_shift_bound: int) -> dict[str, object]:
    """Audit private product states for every common miss of a canonical fan."""
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
    collision_primes = collision.collision_primes(shifts)
    smallest_factors = canonical.ray.short_certificate.smallest_prime_factors(
        limit + 4 * max(shifts)
    )
    core_primes = [
        prime
        for prime in canonical.ray.short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    common_misses = [
        prime
        for prime in core_primes
        if all(
            canonical.witness_for_pair(prime, pair, smallest_factors) is None
            for pair in pairs
        )
    ]
    rows = [
        private_state(prime, pair, smallest_factors, set(collision_primes))
        for prime in common_misses
        for pair in pairs
    ]
    mode_histogram = Counter(str(row["mode"]) for row in rows)
    all_outside_rows = [row for row in rows if row["mode"] == "all_outside"]
    private_one_holes = [
        row for row in rows if row["private_one_hole_target"] is not None
    ]
    return {
        "arithmetic": (
            "exact SPF factorization, complete divisor-residue product sets, "
            "and finite unit-group support calculations"
        ),
        "scope_note": (
            "This is a finite-state decomposition of common failures. The "
            "one-hole congruence is exact, but the profile does not prove that "
            "all-outside private states are impossible."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "canonical_pairs": [{"a": a, "c": c} for a, c in pairs],
        "shifts": shifts,
        "collision_primes": collision_primes,
        "core_prime_count": len(core_primes),
        "common_failure_count": len(common_misses),
        "common_failures": common_misses,
        "state_count": len(rows),
        "mode_histogram": dict(sorted(mode_histogram.items())),
        "all_outside_support_saturated_count": sum(
            bool(row["private_support_saturated"]) for row in all_outside_rows
        ),
        "all_outside_support_index_histogram": dict(
            sorted(
                Counter(
                    int(row["private_support_index"]) for row in all_outside_rows
                ).items()
            )
        ),
        "private_one_hole_count": len(private_one_holes),
        "private_one_hole_samples": private_one_holes[:10],
        "states": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000_000)
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
