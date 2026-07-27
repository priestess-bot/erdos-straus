#!/usr/bin/env python3
"""Resolve multi-new-factor source-free witnesses using only trial factorization."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_SCRIPT = ROOT / "reproductions" / "type_ii_source_free_transition_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-source-free-transition-h19-200m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-single-new-factor-release-h19-200m-results.json"


def load_profile_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_single_new_factor_release_profile", PROFILE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_source_free_transition_profile.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


profile = load_profile_script()
transition = profile.transition


def primes_through(limit: int) -> list[int]:
    """Return the small trial primes needed for exact factorization."""
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


def factorization(value: int, primes: list[int]) -> dict[int, int]:
    """Return the exact prime-power factorization using a trial-prime table."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: dict[int, int] = {}
    remainder = value
    for prime in primes:
        if prime * prime > remainder:
            break
        if remainder % prime:
            continue
        exponent = 0
        while remainder % prime == 0:
            remainder //= prime
            exponent += 1
        factors[prime] = exponent
    if remainder > 1:
        factors[remainder] = factors.get(remainder, 0) + 1
    return factors


def divisors(factors: dict[int, int]) -> list[int]:
    values = [1]
    for prime, exponent in sorted(factors.items()):
        previous = tuple(values)
        power = 1
        for _ in range(exponent):
            power *= prime
            values.extend(value * power for value in previous)
    return values


def source_free_one_new_witness(
    prime: int,
    shift: int,
    old_source_primes: set[int],
    collision_primes: set[int],
    trial_primes: list[int],
) -> dict[str, object] | None:
    """Return the source-minimal one-new-factor Type II witness at one shift."""
    a, c = transition.canonical.canonical_pair(shift)
    modulus = 4 * a * c
    candidates: list[dict[str, object]] = []
    for divisor in divisors(factorization(prime + 4 * shift, trial_primes)):
        if divisor <= 1 or (divisor + 1) % modulus:
            continue
        certificate = transition.canonical.ray.short_certificate.type_ii_raw_ray_certificate(
            prime, a, c, (divisor + 1) // modulus
        )
        if certificate is None:
            continue
        factors = factorization(divisor, trial_primes)
        collision = sum(exponent for q, exponent in factors.items() if q in collision_primes)
        old_private = sum(
            exponent
            for q, exponent in factors.items()
            if q in old_source_primes and q not in collision_primes
        )
        new = sum(exponent for q, exponent in factors.items() if q not in old_source_primes)
        if old_private or new != 1:
            continue
        candidates.append(
            {
                "h": divisor,
                "h_factorization": [
                    {"prime": q, "exponent": exponent} for q, exponent in sorted(factors.items())
                ],
                "a": a,
                "c": c,
                "k": (divisor + 1) // modulus,
                "gap": certificate.gap,
                "divisor": certificate.divisor,
                "collision_multiplicity": collision,
                "old_private_multiplicity": old_private,
                "new_multiplicity": new,
            }
        )
    if not candidates:
        return None
    return min(candidates, key=lambda row: (row["collision_multiplicity"], row["h"]))


def run_profile(payload: dict[str, object]) -> dict[str, object]:
    """Find the first later one-new-factor witness for each multi-new profile."""
    limit = int(payload["prime_limit"])
    base_shift_bound = int(payload["base_shift_bound"])
    shift_cap = int(payload["shift_cap"])
    targets = [
        row
        for row in payload["profiles"]
        if row["selected_witness"]["new_multiplicity"] >= 2
    ]
    trial_primes = primes_through(math.isqrt(limit + 4 * shift_cap))
    base_pairs = tuple(
        transition.canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    collision_primes = set(
        transition.relay.collision.collision_primes(tuple(range(1, base_shift_bound + 1)))
    )
    profiles: list[dict[str, object]] = []
    missing: list[int] = []
    for row in targets:
        prime = int(row["prime"])
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in factorization(prime + 4 * a * a * c, trial_primes)
        }
        selected = None
        for shift in range(int(row["first_source_free_shift"]) + 1, shift_cap + 1):
            selected = source_free_one_new_witness(
                prime, shift, old_source_primes, collision_primes, trial_primes
            )
            if selected is not None:
                profiles.append(
                    {
                        "prime": prime,
                        "first_multi_new_shift": row["first_source_free_shift"],
                        "first_multi_new_multiplicity": row["selected_witness"][
                            "new_multiplicity"
                        ],
                        "first_one_new_shift": shift,
                        "selected_witness": selected,
                    }
                )
                break
        if selected is None:
            missing.append(prime)
    return {
        "arithmetic": (
            "exact trial-prime factorization, complete divisor enumeration at every "
            "later canonical shift, and reconstructed Type II certificate checks"
        ),
        "scope_note": (
            "A finite one-new-factor release audit. It does not assert that every "
            "multi-new state eventually releases at a fixed depth."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "shift_cap": shift_cap,
        "multi_new_first_count": len(targets),
        "one_new_release_count": len(profiles),
        "missing_through_cap": missing,
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_profile(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
