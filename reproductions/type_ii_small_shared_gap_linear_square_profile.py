#!/usr/bin/env python3
"""Profile linear versus square-only Type II hits at shared gaps 3, 7, 11."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-small-shared-gap-linear-square-10m-results.json"
BASE = ROOT / "reproductions" / "type_ii_small_shared_gap_fan.py"


def load_base():
    spec = importlib.util.spec_from_file_location(
        "type_ii_small_shared_gap_linear_square_base", BASE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_small_shared_gap_fan.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_base()
short_certificate = base.short_certificate
SHARED_DIVISORS = {3: 4, 7: 8, 11: 12}


@dataclass(frozen=True)
class LinearSquareProfile:
    prime: int
    category: str
    gap: int | None
    x: int | None
    divisor: int | None


def profile_prime(prime: int, spf: list[int]) -> LinearSquareProfile:
    """Classify the first 3,7,11 Type II hit by its divisor lattice level."""
    if prime % 24 != 1 or prime < 73:
        raise ValueError("prime must be a core prime at least 73")

    for gap in SHARED_DIVISORS:
        x = (prime + gap) // 4
        target = (-x) % gap
        for divisor in short_certificate.positive_divisors_from_spf(x, spf):
            if divisor % gap != target:
                continue
            witness = base.build_witness(
                prime, gap, divisor, SHARED_DIVISORS[gap], "linear"
            )
            return LinearSquareProfile(
                prime, "linear", witness.gap, witness.x, witness.type_ii_divisor
            )

    for gap in SHARED_DIVISORS:
        certificate = short_certificate.type_ii_residue_certificate(prime, gap, spf)
        if certificate is None:
            continue
        if certificate.divisor <= 0 or certificate.divisor > certificate.x:
            raise AssertionError("Type II divisor has invalid size")
        if certificate.x % certificate.divisor == 0:
            raise AssertionError("linear divisor should have been found first")
        return LinearSquareProfile(
            prime,
            "square_only",
            gap,
            certificate.x,
            certificate.divisor,
        )
    return LinearSquareProfile(prime, "no_type_ii", None, None, None)


def run_audit(limit: int, sample_cap: int = 20) -> dict[str, object]:
    """Audit the exact linear/square-only/no-hit partition."""
    if limit < 73 or sample_cap < 0:
        raise ValueError("limit must be at least 73 and sample_cap nonnegative")
    spf = short_certificate.smallest_prime_factors(limit + 11)
    categories = {"linear": 0, "square_only": 0, "no_type_ii": 0}
    gap_counts = {
        category: {str(gap): 0 for gap in SHARED_DIVISORS}
        for category in categories
    }
    samples = {category: [] for category in categories}
    core_prime_count = 0
    for prime in short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        core_prime_count += 1
        profile = profile_prime(prime, spf)
        categories[profile.category] += 1
        if profile.gap is not None:
            gap_counts[profile.category][str(profile.gap)] += 1
        if len(samples[profile.category]) < sample_cap:
            samples[profile.category].append(prime)
    if sum(categories.values()) != core_prime_count:
        raise AssertionError("profile categories did not partition the core primes")
    return {
        "arithmetic": (
            "exact SPF divisors of x and x^2, Type II certificate validation, "
            "and fixed shared divisors 4, 8, 12"
        ),
        "scope_note": (
            "This is an exact classification only for gaps 3, 7, 11. "
            "no_type_ii may still be captured by larger gaps."
        ),
        "prime_limit": limit,
        "core_prime_count": core_prime_count,
        "categories": categories,
        "gap_counts": gap_counts,
        "samples": samples,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--sample-cap", type=int, default=20)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.sample_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
