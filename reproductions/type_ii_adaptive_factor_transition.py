#!/usr/bin/env python3
"""Profile source-minimal factor transitions after a canonical Type II fan.

For every common failure of a base canonical fan, locate its first later
canonical shift with a Type II certificate. At that first shift, enumerate
every valid certificate factor and select one minimizing, in order, the
multiplicity from old private primes, the multiplicity from new primes, the
old collision multiplicity, and the factor itself. This isolates whether an
adaptive next shift can be certified without reusing old private factors.
"""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT / "reproductions" / "type-ii-adaptive-factor-transition-h19-10m-results.json"
)
RELAY_SCRIPT = ROOT / "reproductions" / "type_ii_collision_factor_relay.py"


def load_relay_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_adaptive_factor_transition_relay", RELAY_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_collision_factor_relay.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


relay = load_relay_script()
canonical = relay.canonical


def source_partition(
    factorization: dict[int, int],
    collision_primes: set[int],
    old_source_primes: set[int],
) -> tuple[int, int, int]:
    """Return collision, old-private, and new prime multiplicities."""
    collision = sum(
        exponent for prime, exponent in factorization.items() if prime in collision_primes
    )
    old_private = sum(
        exponent
        for prime, exponent in factorization.items()
        if prime in old_source_primes and prime not in collision_primes
    )
    new = sum(
        exponent for prime, exponent in factorization.items() if prime not in old_source_primes
    )
    return collision, old_private, new


def witnesses_at_shift(
    prime: int,
    shift: int,
    smallest_factors: list[int],
    collision_primes: set[int],
    old_source_primes: set[int],
) -> list[dict[str, object]]:
    """Return every validated witness at one canonical shift."""
    a, c = canonical.canonical_pair(shift)
    modulus = 4 * a * c
    rows: list[dict[str, object]] = []
    for factor in canonical.ray.divisors(prime + 4 * shift, smallest_factors):
        if factor <= 1 or (factor + 1) % modulus:
            continue
        k = (factor + 1) // modulus
        certificate = canonical.ray.short_certificate.type_ii_raw_ray_certificate(
            prime, a, c, k
        )
        if certificate is None:
            continue
        factorization = relay.factorization_dict(factor, smallest_factors)
        collision, old_private, new = source_partition(
            factorization, collision_primes, old_source_primes
        )
        rows.append(
            {
                "h": factor,
                "h_factorization": [
                    {"prime": q, "exponent": exponent}
                    for q, exponent in sorted(factorization.items())
                ],
                "a": a,
                "c": c,
                "k": k,
                "gap": certificate.gap,
                "divisor": certificate.divisor,
                "collision_multiplicity": collision,
                "old_private_multiplicity": old_private,
                "new_multiplicity": new,
            }
        )
    return rows


def run_profile(
    limit: int, base_shift_bound: int, shift_cap: int
) -> dict[str, object]:
    """Compute the exact first-transition source profile in a finite range."""
    if limit < 73 or base_shift_bound < 2 or shift_cap <= base_shift_bound:
        raise ValueError("require limit >= 73 and 2 <= base bound < shift cap")
    smallest_factors = canonical.ray.short_certificate.smallest_prime_factors(
        limit + 4 * shift_cap
    )
    base_pairs = tuple(
        canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    collision_primes = set(
        relay.collision.collision_primes(tuple(range(1, base_shift_bound + 1)))
    )
    core_primes = [
        prime
        for prime in canonical.ray.short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    profiles: list[dict[str, object]] = []
    missing: list[int] = []
    for prime in core_primes:
        if any(
            canonical.witness_for_pair(prime, pair, smallest_factors) is not None
            for pair in base_pairs
        ):
            continue
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in relay.factorization_dict(
                prime + 4 * a * a * c, smallest_factors
            )
        }
        selected = None
        for shift in range(base_shift_bound + 1, shift_cap + 1):
            witnesses = witnesses_at_shift(
                prime,
                shift,
                smallest_factors,
                collision_primes,
                old_source_primes,
            )
            if not witnesses:
                continue
            selected = min(
                witnesses,
                key=lambda row: (
                    row["old_private_multiplicity"],
                    row["new_multiplicity"],
                    row["collision_multiplicity"],
                    row["h"],
                ),
            )
            profiles.append(
                {
                    "prime": prime,
                    "first_later_shift": shift,
                    "first_shift_witness_count": len(witnesses),
                    "selected_witness": selected,
                }
            )
            break
        if selected is None:
            missing.append(prime)
    histogram = Counter(
        (
            row["selected_witness"]["collision_multiplicity"],
            row["selected_witness"]["old_private_multiplicity"],
            row["selected_witness"]["new_multiplicity"],
        )
        for row in profiles
    )
    old_private_free = [
        row for row in profiles if row["selected_witness"]["old_private_multiplicity"] == 0
    ]
    new_factor = [
        row for row in profiles if row["selected_witness"]["new_multiplicity"] > 0
    ]
    return {
        "arithmetic": (
            "exact SPF factorization, complete divisor enumeration at every first "
            "later canonical shift, and reconstructed Type II certificate checks"
        ),
        "scope_note": (
            "A finite first-transition profile. The selected witness minimizes old "
            "private multiplicity only among certificates at its first later shift."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "shift_cap": shift_cap,
        "core_prime_count": len(core_primes),
        "base_residual_count": len(profiles) + len(missing),
        "missing_through_cap": missing,
        "source_minimal_histogram": {
            f"collision:{collision},old_private:{old_private},new:{new}": count
            for (collision, old_private, new), count in sorted(histogram.items())
        },
        "old_private_free_count": len(old_private_free),
        "new_factor_count": len(new_factor),
        "old_private_required_primes": [
            row["prime"]
            for row in profiles
            if row["selected_witness"]["old_private_multiplicity"] > 0
        ],
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--base-shift-bound", type=int, default=19)
    parser.add_argument("--shift-cap", type=int, default=50)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_profile(args.limit, args.base_shift_bound, args.shift_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
