#!/usr/bin/env python3
"""Audit scaled-first marked tails carried by pure-new canonical certificates.

For a raw Type II certificate with gap m, a scaled-first marked tail exists
exactly when a divisor D of p+m is 1 modulo m.  This script does not search an
unbounded scale parameter: it enumerates those divisors D directly.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE_SCRIPT = ROOT / "reproductions" / "type_ii_single_new_factor_release.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-pure-new-scaled-tail-1b-s1008-results.json"


def load_release_script():
    """Load the established exact factorization and canonical-ray helpers."""
    spec = importlib.util.spec_from_file_location(
        "type_ii_h19_pure_new_scaled_tail_release", RELEASE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_single_new_factor_release.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


single = load_release_script()
transition = single.transition


def scaled_tail_candidates(
    prime: int,
    shift: int,
    old_source_primes: set[int],
    trial_primes: list[int],
) -> list[dict[str, int]]:
    """Return all pure-new ray certificates with a scaled-first marked tail."""
    a, c = transition.canonical.canonical_pair(shift)
    modulus = 4 * a * c
    candidates: list[dict[str, int]] = []
    for factor in single.factorization(prime + 4 * shift, trial_primes):
        if factor in old_source_primes or (factor + 1) % modulus:
            continue
        certificate = transition.canonical.ray.short_certificate.type_ii_raw_ray_certificate(
            prime, a, c, (factor + 1) // modulus
        )
        if certificate is None:
            continue
        gap = certificate.gap
        for shared_divisor in single.divisors(
            single.factorization(prime + gap, trial_primes)
        ):
            if shared_divisor == 1 or (shared_divisor - 1) % gap:
                continue
            first_scale = (shared_divisor - 1) // gap
            source = first_scale * (prime + gap) // shared_divisor
            if shared_divisor * source != first_scale * (prime + gap):
                raise AssertionError("scaled-first source is not integral")
            if not 2 <= source < prime:
                raise AssertionError("scaled-first source is not strictly smaller")
            if certificate.y % prime or certificate.z % prime:
                raise AssertionError("raw Type II certificate lacks two p-tails")
            source_solution = (
                first_scale * certificate.x,
                certificate.y // prime,
                certificate.z // prime,
            )
            target_solution = (certificate.x, certificate.y, certificate.z)
            if Fraction(4, source) != sum(
                (Fraction(1, value) for value in source_solution), Fraction()
            ):
                raise AssertionError("scaled marked source did not reconstruct")
            if Fraction(4, prime) != sum(
                (Fraction(1, value) for value in target_solution), Fraction()
            ):
                raise AssertionError("pure-new target did not reconstruct")
            candidates.append(
                {
                    "shift": shift,
                    "a": a,
                    "c": c,
                    "h": factor,
                    "ray_k": (factor + 1) // modulus,
                    "gap": gap,
                    "certificate_divisor": certificate.divisor,
                    "shared_divisor": shared_divisor,
                    "first_scale": first_scale,
                    "source_denominator": source,
                }
            )
    return candidates


def pure_new_scaled_tail_witness(
    prime: int,
    shift: int,
    old_source_primes: set[int],
    trial_primes: list[int],
) -> dict[str, int] | None:
    """Return a deterministic scaled-first marked tail at one canonical shift."""
    candidates = scaled_tail_candidates(prime, shift, old_source_primes, trial_primes)
    return min(
        candidates,
        key=lambda row: (row["first_scale"], row["h"], row["shared_divisor"]),
        default=None,
    )


def has_unscaled_tail(candidates: list[dict[str, int]]) -> bool:
    """Recognize the k=1 specialization without depending on witness ordering."""
    return any(candidate["first_scale"] == 1 for candidate in candidates)


def run_profile(payload: dict[str, object], shift_cap: int) -> dict[str, object]:
    """Classify all H19 new-factor states in a finite canonical shift window."""
    base_shift_bound = int(payload["base_shift_bound"])
    if shift_cap <= base_shift_bound:
        raise ValueError("shift cap must exceed the H19 base shift bound")
    limit = int(payload["prime_limit"])
    targets = [
        row
        for row in payload["profiles"]
        if int(row["selected_witness"]["new_multiplicity"]) > 0
    ]
    # Ray factors divide p+4s, but the shared-mark condition factors p+m and
    # m can be as large as p-2.  The latter therefore needs trial primes up
    # to sqrt(2*limit), not merely sqrt(limit + 4*shift_cap).
    trial_primes = single.primes_through(math.isqrt(2 * limit))
    base_pairs = tuple(
        transition.canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    records: list[dict[str, object]] = []
    scaled_hits: set[int] = set()
    unscaled_hits: set[int] = set()
    missing: list[int] = []
    for row in targets:
        prime = int(row["prime"])
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in single.factorization(prime + 4 * a * a * c, trial_primes)
        }
        selected = None
        has_unit_scale = False
        for shift in range(base_shift_bound + 1, shift_cap + 1):
            candidates = scaled_tail_candidates(
                prime, shift, old_source_primes, trial_primes
            )
            if has_unscaled_tail(candidates):
                has_unit_scale = True
            if selected is None and candidates:
                selected = min(
                    candidates,
                    key=lambda candidate: (
                        candidate["first_scale"],
                        candidate["h"],
                        candidate["shared_divisor"],
                    ),
                )
                records.append(
                    {
                        "prime": prime,
                        "first_pure_new_scaled_tail_shift": shift,
                        "selected_witness": selected,
                    }
                )
            if selected is not None and has_unit_scale:
                break
        if selected is None:
            missing.append(prime)
            continue
        scaled_hits.add(prime)
        if has_unit_scale:
            unscaled_hits.add(prime)
    scaled_only = sorted(scaled_hits - unscaled_hits)
    histogram = Counter(
        row["first_pure_new_scaled_tail_shift"] for row in records
    )
    return {
        "arithmetic": (
            "exact trial-prime factorization; complete divisor enumeration of "
            "p+m; H19 source-label comparison; and fractions.Fraction "
            "verification of each marked source and Type II target"
        ),
        "scope_note": (
            "A finite audit of the marked scaled-first lift. The lift is "
            "certificate-equivalent, not an unmarked inductive descent; a miss "
            "does not rule out another certificate or descent source."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "shift_cap": shift_cap,
        "new_factor_state_count": len(targets),
        "pure_new_scaled_tail_count": len(scaled_hits),
        "ordinary_same_certificate_tail_count": len(unscaled_hits),
        "scaled_only_count": len(scaled_only),
        "scaled_only_primes": scaled_only,
        "missing_through_cap": missing,
        "first_pure_new_scaled_tail_shift_histogram": {
            str(shift): count for shift, count in sorted(histogram.items())
        },
        "maximum_first_pure_new_scaled_tail_shift": max(histogram, default=None),
        "maximum_selected_first_scale": max(
            (int(row["selected_witness"]["first_scale"]) for row in records),
            default=None,
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--shift-cap", type=int, default=1_008)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_profile(payload, args.shift_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
