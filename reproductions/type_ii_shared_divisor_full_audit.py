#!/usr/bin/env python3
"""Measure a bounded-gap, unbounded-first-scale Type II shared-divisor fan."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-shared-divisor-10m-gap239-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_shared_divisor_full_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def run_audit(limit: int, gap_cap: int) -> dict[str, object]:
    if limit < 73 or gap_cap < 3:
        raise ValueError("limit >= 73 and gap_cap >= 3 are required")
    spf = short_certificate.smallest_prime_factors(limit + gap_cap)
    core_primes = [
        prime for prime in short_certificate.primes_up_to(limit) if prime % 24 == 1
    ]
    misses = []
    gap_histogram: dict[int, int] = {}
    largest_gap = 0
    largest_scale = 0
    gap_record_holders = []
    scale_record_holders = []

    for prime in core_primes:
        witness = short_certificate.type_ii_shared_divisor_tail_deflation_scan(
            prime, gap_cap, spf
        )
        if witness is None:
            misses.append(prime)
            continue
        gap_histogram[witness.gap] = gap_histogram.get(witness.gap, 0) + 1
        entry = {
            "prime": prime,
            "gap": witness.gap,
            "first_scale": witness.first_scale,
            "source_denominator": witness.source_denominator,
            "divisor": witness.certificate.divisor,
        }
        if witness.gap > largest_gap:
            largest_gap = witness.gap
            gap_record_holders.append(entry)
        if witness.first_scale > largest_scale:
            largest_scale = witness.first_scale
            scale_record_holders.append(entry)

    return {
        "arithmetic": (
            "exact SPF factorization of every p+m in the bounded gap fan, "
            "Type II divisor certification, and fractions.Fraction validation"
        ),
        "scope_note": (
            "A finite bounded-gap profile with no first-scale cutoff. It does "
            "not prove this fixed fan covers all core primes."
        ),
        "prime_limit": limit,
        "gap_cap": gap_cap,
        "core_prime_count": len(core_primes),
        "captured_count": len(core_primes) - len(misses),
        "miss_count": len(misses),
        "misses": misses,
        "largest_minimum_gap": largest_gap if gap_record_holders else None,
        "largest_first_scale": largest_scale if scale_record_holders else None,
        "gap_record_holders": gap_record_holders,
        "scale_record_holders": scale_record_holders,
        "minimum_gap_histogram": dict(sorted(gap_histogram.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--gap-cap", type=int, default=239)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
