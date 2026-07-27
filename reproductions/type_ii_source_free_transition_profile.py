#!/usr/bin/env python3
"""Profile the first canonical Type II witness avoiding H19 old-private factors."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from array import array
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE_SCRIPT = ROOT / "reproductions" / "type_ii_old_private_release.py"
RESULTS = ROOT / "reproductions" / "type-ii-source-free-transition-h19-100m-results.json"


def load_release_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_source_free_transition_release", RELEASE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_old_private_release.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


release = load_release_script()
transition = release.transition


class PackedSmallestFactors:
    """Two-byte SPF storage with zero denoting a prime index."""

    def __init__(self, values: array):
        self.values = values

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, value: int) -> int:
        factor = self.values[value]
        return factor if factor else value


def packed_smallest_prime_factors(limit: int) -> PackedSmallestFactors:
    """Build an exact SPF table using two bytes per composite entry."""
    if limit < 2:
        raise ValueError("limit must be at least two")
    if math.isqrt(limit) >= 2**16:
        raise ValueError("packed SPF requires square root below 2**16")
    factors = array("H", [0]) * (limit + 1)
    for prime in range(2, math.isqrt(limit) + 1):
        if factors[prime]:
            continue
        for value in range(prime * prime, limit + 1, prime):
            if not factors[value]:
                factors[value] = prime
    return PackedSmallestFactors(factors)


def concise_witness(row: dict[str, object]) -> dict[str, int]:
    return {
        key: row[key]
        for key in (
            "h",
            "a",
            "c",
            "k",
            "gap",
            "divisor",
            "collision_multiplicity",
            "old_private_multiplicity",
            "new_multiplicity",
        )
    }


def segmented_core_primes_up_to(limit: int, segment_size: int = 1_000_000):
    """Yield p=1 mod 24 primes without retaining a limit-sized sieve."""
    if limit < 2 or segment_size < 2:
        raise ValueError("limit and segment size must be at least two")
    root = math.isqrt(limit)
    base_sieve = bytearray(b"\x01") * (root + 1)
    base_sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(root) + 1):
        if base_sieve[prime]:
            base_sieve[prime * prime : root + 1 : prime] = b"\x00" * (
                ((root - prime * prime) // prime) + 1
            )
    base_primes = [prime for prime in range(2, root + 1) if base_sieve[prime]]
    for lower in range(2, limit + 1, segment_size):
        upper = min(limit + 1, lower + segment_size)
        sieve = bytearray(b"\x01") * (upper - lower)
        for prime in base_primes:
            start = max(prime * prime, ((lower + prime - 1) // prime) * prime)
            if start >= upper:
                continue
            sieve[start - lower : upper - lower : prime] = b"\x00" * (
                ((upper - start - 1) // prime) + 1
            )
        for offset, is_prime in enumerate(sieve):
            prime = lower + offset
            if is_prime and prime % 24 == 1:
                yield prime


def run_profile(limit: int, base_shift_bound: int, shift_cap: int) -> dict[str, object]:
    """Find the first source-free certificate for every H19 common residual."""
    if limit < 73 or base_shift_bound < 2 or shift_cap <= base_shift_bound:
        raise ValueError("require limit >= 73 and 2 <= base bound < shift cap")
    smallest_factors = packed_smallest_prime_factors(limit + 4 * shift_cap)
    base_pairs = tuple(
        transition.canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    collision_primes = set(
        transition.relay.collision.collision_primes(tuple(range(1, base_shift_bound + 1)))
    )
    profiles: list[dict[str, object]] = []
    missing: list[int] = []
    residual_count = 0
    for prime in segmented_core_primes_up_to(limit):
        if any(
            transition.canonical.witness_for_pair(prime, pair, smallest_factors) is not None
            for pair in base_pairs
        ):
            continue
        residual_count += 1
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in transition.relay.factorization_dict(
                prime + 4 * a * a * c, smallest_factors
            )
        }
        selected = None
        for shift in range(base_shift_bound + 1, shift_cap + 1):
            eligible = [
                witness
                for witness in transition.witnesses_at_shift(
                    prime,
                    shift,
                    smallest_factors,
                    collision_primes,
                    old_source_primes,
                )
                if witness["old_private_multiplicity"] == 0
            ]
            if not eligible:
                continue
            selected = min(
                eligible,
                key=lambda witness: (
                    witness["new_multiplicity"],
                    witness["collision_multiplicity"],
                    witness["h"],
                ),
            )
            profiles.append(
                {
                    "prime": prime,
                    "first_source_free_shift": shift,
                    "selected_witness": concise_witness(selected),
                }
            )
            break
        if selected is None:
            missing.append(prime)
    histogram = Counter(row["first_source_free_shift"] for row in profiles)
    mechanism_histogram = Counter(
        (
            row["selected_witness"]["collision_multiplicity"],
            row["selected_witness"]["new_multiplicity"],
        )
        for row in profiles
    )
    collision_only_count = sum(
        row["selected_witness"]["new_multiplicity"] == 0 for row in profiles
    )
    new_factor_count = len(profiles) - collision_only_count
    pure_new_factor_count = sum(
        row["selected_witness"]["collision_multiplicity"] == 0
        and row["selected_witness"]["new_multiplicity"] > 0
        for row in profiles
    )
    return {
        "arithmetic": (
            "exact compact SPF factorization, complete divisor enumeration at every "
            "canonical shift, and reconstructed Type II certificate checks"
        ),
        "scope_note": (
            "A finite source-free depth profile. It does not assert a fixed "
            "universal depth or a descent theorem."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "shift_cap": shift_cap,
        "base_residual_count": residual_count,
        "source_free_count": len(profiles),
        "missing_through_cap": missing,
        "first_source_free_shift_histogram": {
            str(shift): count for shift, count in sorted(histogram.items())
        },
        "maximum_first_source_free_shift": max(
            (row["first_source_free_shift"] for row in profiles), default=None
        ),
        "source_mechanism_histogram": {
            f"collision:{collision},new:{new}": count
            for (collision, new), count in sorted(mechanism_histogram.items())
        },
        "collision_only_count": collision_only_count,
        "new_factor_count": new_factor_count,
        "pure_new_factor_count": pure_new_factor_count,
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100_000_000)
    parser.add_argument("--base-shift-bound", type=int, default=19)
    parser.add_argument("--shift-cap", type=int, default=125)
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
