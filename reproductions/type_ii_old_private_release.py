#!/usr/bin/env python3
"""Audit whether first-transition old-private use persists under fan expansion."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from array import array
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRANSITION_SCRIPT = ROOT / "reproductions" / "type_ii_adaptive_factor_transition.py"
RESULTS = ROOT / "reproductions" / "type-ii-old-private-release-h19-20m-results.json"


def load_transition_script():
    spec = importlib.util.spec_from_file_location("type_ii_old_private_release", TRANSITION_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_adaptive_factor_transition.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


transition = load_transition_script()


def compact_smallest_prime_factors(limit: int) -> array:
    """Return an SPF table without allocating one Python integer per entry."""
    if limit < 2:
        raise ValueError("limit must be at least two")
    spf = array("I", range(limit + 1))
    for prime in range(2, math.isqrt(limit) + 1):
        if spf[prime] != prime:
            continue
        for value in range(prime * prime, limit + 1, prime):
            if spf[value] == value:
                spf[value] = prime
    return spf


def core_primes_up_to(limit: int):
    """Yield core primes without materializing the full prime list."""
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                ((limit - prime * prime) // prime) + 1
            )
    for prime in range(1, limit + 1, 24):
        if sieve[prime]:
            yield prime


def concise_witness(row: dict[str, object]) -> dict[str, int]:
    """Keep the exact source multiplicities needed for the transition comparison."""
    return {
        key: row[key]
        for key in (
            "h",
            "collision_multiplicity",
            "old_private_multiplicity",
            "new_multiplicity",
        )
    }


def first_transition_profile(
    limit: int, base_shift_bound: int, first_shift_cap: int, smallest_factors: array
) -> dict[str, object]:
    """Rebuild the base residuals using a compact factor table."""
    base_pairs = tuple(
        transition.canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    collision_primes = set(
        transition.relay.collision.collision_primes(tuple(range(1, base_shift_bound + 1)))
    )
    profiles: list[dict[str, object]] = []
    missing: list[int] = []
    for prime in core_primes_up_to(limit):
        if any(
            transition.canonical.witness_for_pair(prime, pair, smallest_factors) is not None
            for pair in base_pairs
        ):
            continue
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in transition.relay.factorization_dict(
                prime + 4 * a * a * c, smallest_factors
            )
        }
        selected = None
        for shift in range(base_shift_bound + 1, first_shift_cap + 1):
            witnesses = transition.witnesses_at_shift(
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
                    "selected_witness": selected,
                }
            )
            break
        if selected is None:
            missing.append(prime)
    return {
        "base_pairs": base_pairs,
        "collision_primes": collision_primes,
        "profiles": profiles,
        "missing": missing,
    }


def run_release_profile(
    limit: int, base_shift_bound: int, first_shift_cap: int, release_shift_cap: int
) -> dict[str, object]:
    """Find the first later certificate without an old-private source, if one exists."""
    if release_shift_cap <= first_shift_cap:
        raise ValueError("release cap must exceed the cap used to define first transitions")
    smallest_factors = compact_smallest_prime_factors(limit + 4 * release_shift_cap)
    initial = first_transition_profile(
        limit, base_shift_bound, first_shift_cap, smallest_factors
    )
    targets = [
        row
        for row in initial["profiles"]
        if row["selected_witness"]["old_private_multiplicity"] > 0
    ]
    base_pairs = initial["base_pairs"]
    collision_primes = initial["collision_primes"]
    late_first_profiles: list[dict[str, object]] = []
    late_first_missing: list[int] = []
    for prime in initial["missing"]:
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in transition.relay.factorization_dict(
                prime + 4 * a * a * c, smallest_factors
            )
        }
        selected = None
        for shift in range(first_shift_cap + 1, release_shift_cap + 1):
            witnesses = transition.witnesses_at_shift(
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
                key=lambda witness: (
                    witness["old_private_multiplicity"],
                    witness["new_multiplicity"],
                    witness["collision_multiplicity"],
                    witness["h"],
                ),
            )
            late_first_profiles.append(
                {
                    "prime": prime,
                    "first_later_shift": shift,
                    "selected_witness": concise_witness(selected),
                }
            )
            break
        if selected is None:
            late_first_missing.append(prime)
    rows: list[dict[str, object]] = []
    release_missing: list[int] = []
    for target in targets:
        prime = target["prime"]
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in transition.relay.factorization_dict(
                prime + 4 * a * a * c, smallest_factors
            )
        }
        released = None
        for shift in range(first_shift_cap + 1, release_shift_cap + 1):
            witnesses = transition.witnesses_at_shift(
                prime,
                shift,
                smallest_factors,
                collision_primes,
                old_source_primes,
            )
            eligible = [
                witness
                for witness in witnesses
                if witness["old_private_multiplicity"] == 0
            ]
            if eligible:
                released = min(
                    eligible,
                    key=lambda witness: (
                        witness["new_multiplicity"],
                        witness["collision_multiplicity"],
                        witness["h"],
                    ),
                )
                rows.append(
                    {
                        "prime": prime,
                        "first_transition": {
                            "shift": target["first_later_shift"],
                            "witness": concise_witness(target["selected_witness"]),
                        },
                        "first_old_private_free_transition": {
                            "shift": shift,
                            "witness": concise_witness(released),
                        },
                    }
                )
                break
        if released is None:
            release_missing.append(prime)
    first_window_free = sum(
        row["selected_witness"]["old_private_multiplicity"] == 0
        for row in initial["profiles"]
    )
    late_first_free = sum(
        row["selected_witness"]["old_private_multiplicity"] == 0
        for row in late_first_profiles
    )
    return {
        "arithmetic": (
            "exact SPF factorization, complete divisor enumeration at each later "
            "canonical shift, and reconstructed Type II certificate checks"
        ),
        "scope_note": (
            "A finite release audit. It does not assert a uniform shift bound or "
            "that a first-transition source classification is invariant."
        ),
        "factor_table": "exact compact unsigned-integer smallest-prime-factor table",
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "first_shift_cap": first_shift_cap,
        "release_shift_cap": release_shift_cap,
        "base_residual_count": len(initial["profiles"]) + len(initial["missing"]),
        "first_transition_count": len(initial["profiles"]),
        "missing_through_first_shift_cap": initial["missing"],
        "first_old_private_required_primes": [row["prime"] for row in targets],
        "first_window_old_private_free_count": first_window_free,
        "late_first_transition_profiles": late_first_profiles,
        "missing_through_release_cap": late_first_missing,
        "released_count": len(rows),
        "old_private_release_missing_through_cap": release_missing,
        "old_private_free_count_through_release_cap": first_window_free
        + late_first_free
        + len(rows),
        "profiles": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=20_000_000)
    parser.add_argument("--base-shift-bound", type=int, default=19)
    parser.add_argument("--first-shift-cap", type=int, default=50)
    parser.add_argument("--release-shift-cap", type=int, default=125)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_release_profile(
        args.limit, args.base_shift_bound, args.first_shift_cap, args.release_shift_cap
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
