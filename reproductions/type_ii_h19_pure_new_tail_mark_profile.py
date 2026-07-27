#!/usr/bin/env python3
"""Measure when a pure-new canonical certificate also gives two-tail descent."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-pure-new-tail-mark-1b-s1008-results.json"


def load_release_script():
    """Load the established factorization and canonical-ray helpers."""
    spec = importlib.util.spec_from_file_location(
        "type_ii_h19_pure_new_tail_mark_release", RELEASE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_single_new_factor_release.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


single = load_release_script()
transition = single.transition


def pure_new_tail_witness(
    prime: int,
    shift: int,
    old_source_primes: set[int],
    trial_primes: list[int],
) -> dict[str, int] | None:
    """Return the least pure-new ray whose own gap gives a two-tail lift."""
    a, c = transition.canonical.canonical_pair(shift)
    modulus = 4 * a * c
    candidates: list[dict[str, int]] = []
    for factor in single.factorization(prime + 4 * shift, trial_primes):
        if factor in old_source_primes or (factor + 1) % modulus:
            continue
        certificate = transition.canonical.ray.short_certificate.type_ii_raw_ray_certificate(
            prime, a, c, (factor + 1) // modulus
        )
        if certificate is None or (prime - 1) % (certificate.gap + 1):
            continue
        source = (prime + certificate.gap) // (certificate.gap + 1)
        if not 2 <= source < prime:
            raise AssertionError("tail source is not strictly smaller")
        source_solution = (
            certificate.x,
            certificate.y // prime,
            certificate.z // prime,
        )
        if certificate.y % prime or certificate.z % prime:
            raise AssertionError("raw Type II certificate lacks two p-tails")
        if Fraction(4, source) != sum(
            (Fraction(1, value) for value in source_solution), Fraction()
        ):
            raise AssertionError("two-tail source did not reconstruct")
        candidates.append(
            {
                "shift": shift,
                "a": a,
                "c": c,
                "h": factor,
                "k": (factor + 1) // modulus,
                "gap": certificate.gap,
                "divisor": certificate.divisor,
                "source_denominator": source,
            }
        )
    return min(candidates, key=lambda row: row["h"]) if candidates else None


def run_profile(payload: dict[str, object], shift_cap: int) -> dict[str, object]:
    """Search the supplied H19 new-factor states through a canonical window."""
    base_shift_bound = int(payload["base_shift_bound"])
    if shift_cap <= base_shift_bound:
        raise ValueError("shift cap must exceed the H19 base shift bound")
    limit = int(payload["prime_limit"])
    targets = [
        row
        for row in payload["profiles"]
        if int(row["selected_witness"]["new_multiplicity"]) > 0
    ]
    trial_primes = single.primes_through(math.isqrt(limit + 4 * shift_cap))
    base_pairs = tuple(
        transition.canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    records: list[dict[str, object]] = []
    missing: list[int] = []
    for row in targets:
        prime = int(row["prime"])
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in single.factorization(prime + 4 * a * a * c, trial_primes)
        }
        selected = None
        for shift in range(base_shift_bound + 1, shift_cap + 1):
            selected = pure_new_tail_witness(
                prime, shift, old_source_primes, trial_primes
            )
            if selected is not None:
                records.append(
                    {
                        "prime": prime,
                        "first_pure_new_tail_shift": shift,
                        "selected_witness": selected,
                    }
                )
                break
        if selected is None:
            missing.append(prime)
    histogram = Counter(row["first_pure_new_tail_shift"] for row in records)
    return {
        "arithmetic": (
            "exact trial-prime factorization, H19 source-label comparison, raw "
            "Type II reconstruction, and exact rational verification of the "
            "two-tail source and target"
        ),
        "scope_note": (
            "A finite same-certificate bridge audit. A miss means that no pure-new "
            "canonical certificate in this window also supplies its own two-tail "
            "strict descent; it does not rule out a separate descent source."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "shift_cap": shift_cap,
        "new_factor_state_count": len(targets),
        "pure_new_tail_descent_count": len(records),
        "missing_through_cap": missing,
        "first_pure_new_tail_shift_histogram": {
            str(shift): count for shift, count in sorted(histogram.items())
        },
        "maximum_first_pure_new_tail_shift": max(histogram, default=None),
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
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
