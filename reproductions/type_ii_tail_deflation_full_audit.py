#!/usr/bin/env python3
"""Measure divisor-marked Type II tail deflation on every core prime in a range."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-tail-deflation-1m-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_tail_deflation_full_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def factorization(value: int, spf: list[int]) -> list[dict[str, int]]:
    factors = []
    while value > 1:
        prime = spf[value]
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        factors.append({"prime": prime, "exponent": exponent})
    return factors


def run_audit(limit: int) -> dict[str, object]:
    if limit < 73:
        raise ValueError("limit must be at least 73")
    spf = short_certificate.smallest_prime_factors(limit)
    core_primes = [
        prime for prime in short_certificate.primes_up_to(limit) if prime % 24 == 1
    ]
    hits = []
    misses = []
    gap_histogram: dict[int, int] = {}
    largest_minimum_gap = 0
    record_holders = []

    for prime in core_primes:
        witness = short_certificate.first_type_ii_tail_deflation_witness(prime, spf)
        if witness is None:
            divisors = short_certificate.positive_divisors_from_spf(prime - 1, spf)
            ordinary = short_certificate.shortest_gap_certificate(prime, prime, spf)
            misses.append(
                {
                    "prime": prime,
                    "p_minus_one_factorization": factorization(prime - 1, spf),
                    "eligible_gap_count": sum(divisor % 4 == 0 for divisor in divisors),
                    "eligible_gaps": [
                        divisor - 1 for divisor in divisors if divisor % 4 == 0
                    ],
                    "shortest_bradford_certificate": (
                        asdict(ordinary) if ordinary is not None else None
                    ),
                }
            )
            continue
        gap_histogram[witness.gap] = gap_histogram.get(witness.gap, 0) + 1
        compact = {
            "prime": prime,
            "gap": witness.gap,
            "source_denominator": witness.source_denominator,
            "divisor": witness.certificate.divisor,
        }
        hits.append(compact)
        if witness.gap > largest_minimum_gap:
            largest_minimum_gap = witness.gap
            record_holders.append(compact)

    return {
        "arithmetic": (
            "exact SPF factorization, divisor residues, reconstructed Type II "
            "certificates, and fractions.Fraction checks in short_certificate.py"
        ),
        "scope_note": (
            "This is a finite coverage profile for the divisor-marked selector. "
            "It neither proves a uniform selector nor makes a high coverage rate "
            "a density theorem."
        ),
        "prime_limit": limit,
        "core_prime_count": len(core_primes),
        "tail_deflation_hit_count": len(hits),
        "tail_deflation_miss_count": len(misses),
        "largest_minimum_gap": largest_minimum_gap if hits else None,
        "record_holders": record_holders,
        "minimum_gap_histogram": dict(sorted(gap_histogram.items())),
        "misses": misses,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    summary = {key: value for key, value in payload.items() if key not in {"hits", "misses"}}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
