#!/usr/bin/env python3
"""Profile direct Type I normal-form certificates with a small B parameter.

For x=(p+m)/4, the Type I normal form is x=A*B*C with gcd(A,B)=1 and
m | B*p+A.  The search below is exhaustive in A at every scanned gap and
orders candidates by B, so it measures the least normal-form B rather than
the first gap at which an arbitrary certificate appears.  It is a finite
profile, not a uniform selector theorem.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-i-small-b-normal-form-20m-profile.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_LIMIT = 20_000_000
DEFAULT_GAP_CAP = 239
DEFAULT_B_CAP = 4


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_i_small_b_normal_form_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def first_small_b_certificate(
    prime: int, spf: list[int], gap_cap: int, b_cap: int
) -> dict[str, int | None] | None:
    """Return the first certificate in increasing B, then increasing gap.

    For each admissible pair (B,m), every divisor A of x/B is inspected.
    This is therefore exhaustive for the stated B and gap bounds.
    """
    for b in range(1, b_cap + 1):
        for gap in range(3, gap_cap + 1, 4):
            x = (prime + gap) // 4
            if x % b:
                continue
            for a in short_certificate.positive_divisors_from_spf(x // b, spf):
                if math.gcd(a, b) != 1 or (b * prime + a) % gap:
                    continue
                certificate = short_certificate.type_i_normal_form_certificate(
                    prime, gap, a, b
                )
                if certificate is None:
                    raise AssertionError("normal-form candidate did not verify")
                tail_deflation = short_certificate.type_i_normal_tail_deflation_witness(
                    prime, gap, a, b
                )
                return {
                    "prime": prime,
                    "b": b,
                    "gap": gap,
                    "a": a,
                    "c": x // (a * b),
                    "divisor": certificate.divisor,
                    "first_denominator": certificate.x,
                    "normal_tail_deflation_source": (
                        None
                        if tail_deflation is None
                        else tail_deflation.source_denominator
                    ),
                }
    return None


def run_profile(
    limit: int = DEFAULT_LIMIT,
    gap_cap: int = DEFAULT_GAP_CAP,
    b_cap: int = DEFAULT_B_CAP,
) -> dict[str, object]:
    """Compute the least B through a finite prime, gap, and B range."""
    if limit < 73:
        raise ValueError("limit must be at least 73")
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    if b_cap < 1:
        raise ValueError("b_cap must be positive")

    spf = short_certificate.smallest_prime_factors((limit + gap_cap) // 4 + 1)
    minimum_b_counts: dict[int, int] = {}
    minimum_b_tail_deflation_counts: dict[int, int] = {}
    first_examples: dict[int, dict[str, int | None]] = {}
    non_b_one: list[dict[str, int | None]] = []
    misses: list[int] = []
    core_prime_count = 0

    for prime in short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        core_prime_count += 1
        witness = first_small_b_certificate(prime, spf, gap_cap, b_cap)
        if witness is None:
            misses.append(prime)
            continue
        b = witness["b"]
        minimum_b_counts[b] = minimum_b_counts.get(b, 0) + 1
        if witness["normal_tail_deflation_source"] is not None:
            minimum_b_tail_deflation_counts[b] = (
                minimum_b_tail_deflation_counts.get(b, 0) + 1
            )
        first_examples.setdefault(b, witness)
        if b > 1:
            non_b_one.append(witness)

    return {
        "arithmetic": (
            "for each core prime, scan B in increasing order and every "
            "m=3 (mod 4) through the cap; for each B,m enumerate every "
            "A | ((p+m)/4)/B with gcd(A,B)=1 and test m | Bp+A; every "
            "reported certificate is reconstructed and checked exactly"
        ),
        "scope_note": (
            "Finite minimum-B profile only. It does not prove a fixed B or "
            "gap cap suffices beyond the audited range."
        ),
        "prime_limit": limit,
        "gap_cap": gap_cap,
        "b_cap": b_cap,
        "core_prime_count": core_prime_count,
        "captured_count": core_prime_count - len(misses),
        "misses": misses,
        "minimum_b_counts": {
            str(b): minimum_b_counts[b] for b in sorted(minimum_b_counts)
        },
        "minimum_b_tail_deflation_counts": {
            str(b): minimum_b_tail_deflation_counts.get(b, 0)
            for b in sorted(minimum_b_counts)
        },
        "minimum_b_tail_deflation_count": sum(minimum_b_tail_deflation_counts.values()),
        "first_examples": {
            str(b): first_examples[b] for b in sorted(first_examples)
        },
        "non_b_one_witnesses": non_b_one,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_profile(args.limit, args.gap_cap, args.b_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
