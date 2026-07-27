#!/usr/bin/env python3
"""Profile first direct Type I certificates in a variable small-gap fan.

For every core prime p through a finite limit, enumerate m == 3 (mod 4) up
to a stated cap. At each gap, the complete divisor-residue Type I criterion
is checked. This is a finite profile of an adaptive divisor fan, not a claim
that a fixed finite collection of gaps proves the conjecture.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-i-small-gap-10m-profile.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_LIMIT = 10_000_000
DEFAULT_GAP_CAP = 239


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_i_small_gap_profile_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def run_profile(
    limit: int = DEFAULT_LIMIT, gap_cap: int = DEFAULT_GAP_CAP
) -> dict[str, object]:
    """Compute the first complete Type I divisor-residue hit for each prime."""
    if limit < 73:
        raise ValueError("limit must be at least 73")
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    spf = short_certificate.smallest_prime_factors(limit + gap_cap)
    first_gap_counts: dict[int, int] = {}
    first_gap_examples: dict[int, dict[str, int]] = {}
    misses: list[int] = []
    core_prime_count = 0

    for prime in short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        core_prime_count += 1
        for gap in range(3, gap_cap + 1, 4):
            certificate = short_certificate.type_i_residue_certificate(
                prime, gap, spf
            )
            if certificate is None:
                continue
            first_gap_counts[gap] = first_gap_counts.get(gap, 0) + 1
            first_gap_examples.setdefault(
                gap,
                {
                    "prime": prime,
                    "divisor": certificate.divisor,
                    "first_denominator": certificate.x,
                },
            )
            break
        else:
            misses.append(prime)

    return {
        "arithmetic": (
            "complete SPF factorization of x=(p+m)/4 and exhaustive divisors "
            "of x^2 at every m=3 (mod 4) through the cap; each returned "
            "certificate is checked by exact rational reconstruction"
        ),
        "scope_note": (
            "A finite profile for a variable-divisor, bounded-gap Type I fan. "
            "It neither proves a uniform gap bound nor supplies a theorem "
            "forcing one of these gaps beyond the audited range."
        ),
        "prime_limit": limit,
        "gap_cap": gap_cap,
        "core_prime_count": core_prime_count,
        "captured_count": core_prime_count - len(misses),
        "misses": misses,
        "maximum_first_gap": max(first_gap_counts, default=None),
        "first_gap_counts": {
            str(gap): first_gap_counts[gap] for gap in sorted(first_gap_counts)
        },
        "first_gap_examples": {
            str(gap): first_gap_examples[gap] for gap in sorted(first_gap_examples)
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_profile(args.limit, args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
