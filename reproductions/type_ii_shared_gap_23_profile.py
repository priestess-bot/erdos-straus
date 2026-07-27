#!/usr/bin/env python3
"""Audit the automatic-shared m=23 branch after the 3,7,11 Type II fan."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-shared-gap-23-10m-results.json"
BASE = ROOT / "reproductions" / "type_ii_small_shared_gap_fan.py"


def load_base():
    spec = importlib.util.spec_from_file_location(
        "type_ii_shared_gap_23_base", BASE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_small_shared_gap_fan.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_base()
short_certificate = base.short_certificate

# For p=1 mod 24, x_23=(p+23)/4 is divisible by 6.
BASE_DIVISORS = (1, 2, 3, 4, 6, 9, 12, 18, 36)


@dataclass(frozen=True)
class Gap23Profile:
    prime: int
    category: str
    gap: int | None
    divisor: int | None


def m23_base_witness(prime: int) -> base.SmallSharedGapWitness | None:
    """Return the fixed 2,3-divisor m=23 witness, if its residue matches."""
    if prime % 24 != 1 or prime < 73:
        return None
    x = (prime + 23) // 4
    target = (-x) % 23
    for divisor in BASE_DIVISORS:
        if divisor <= x and divisor % 23 == target:
            return base.build_witness(prime, 23, divisor, 24, "m23_base")
    return None


def profile_prime(prime: int, spf: list[int]) -> Gap23Profile:
    """Classify p after the full Type II tests at gaps 3,7,11."""
    if prime % 24 != 1 or prime < 73:
        raise ValueError("prime must be a core prime at least 73")
    for gap in (3, 7, 11):
        if short_certificate.type_ii_residue_certificate(prime, gap, spf):
            return Gap23Profile(prime, "earlier_type_ii", gap, None)
    base_witness = m23_base_witness(prime)
    if base_witness is not None:
        return Gap23Profile(prime, "m23_base", 23, base_witness.type_ii_divisor)
    certificate = short_certificate.type_ii_residue_certificate(prime, 23, spf)
    if certificate is not None:
        return Gap23Profile(prime, "m23_general", 23, certificate.divisor)
    return Gap23Profile(prime, "no_type_ii_3_7_11_23", None, None)


def run_audit(limit: int, sample_cap: int = 20) -> dict[str, object]:
    """Run the exact 3,7,11,23 profile with all Type II divisor tests."""
    if limit < 73 or sample_cap < 0:
        raise ValueError("limit must be at least 73 and sample_cap nonnegative")
    spf = short_certificate.smallest_prime_factors(limit + 23)
    counts = {
        "earlier_type_ii": 0,
        "m23_base": 0,
        "m23_general": 0,
        "no_type_ii_3_7_11_23": 0,
    }
    samples = {key: [] for key in counts}
    core_prime_count = 0
    for prime in short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        core_prime_count += 1
        profile = profile_prime(prime, spf)
        counts[profile.category] += 1
        if len(samples[profile.category]) < sample_cap:
            samples[profile.category].append(prime)
    return {
        "arithmetic": (
            "exact SPF factorization, full Type II divisor tests at 3,7,11,23, "
            "and exact verification of the fixed m=23 shared divisor 24"
        ),
        "scope_note": (
            "This is an exact profile only for gaps 3,7,11,23. The residual "
            "can still be captured by larger shared-selector gaps."
        ),
        "prime_limit": limit,
        "core_prime_count": core_prime_count,
        "counts": counts,
        "captured_count": core_prime_count - counts["no_type_ii_3_7_11_23"],
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
