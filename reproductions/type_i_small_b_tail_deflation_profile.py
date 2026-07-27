#!/usr/bin/env python3
"""Profile small-B Type I certificates that also give a strict source lift.

This searches the same complete normal-form box as the small-B profile, but
does not stop at the least B certificate. A hit must also satisfy the
certificate-side tail-deflation condition, equivalently belong to the known
complete quadratic external-source descent family.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
RESULTS = ROOT / "reproductions" / "type-i-small-b-tail-deflation-20m-profile.json"
DEFAULT_LIMIT = 20_000_000
DEFAULT_GAP_CAP = 239
DEFAULT_B_CAP = 4


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_i_small_b_tail_deflation_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def first_joint_witness(
    prime: int, spf: list[int], gap_cap: int, b_cap: int
) -> dict[str, int] | None:
    """Find the least B, then gap, certificate that also has a strict source."""
    for b in range(1, b_cap + 1):
        for gap in range(3, gap_cap + 1, 4):
            x = (prime + gap) // 4
            if x % b:
                continue
            for a in short_certificate.positive_divisors_from_spf(x // b, spf):
                if math.gcd(a, b) != 1 or (b * prime + a) % gap:
                    continue
                witness = short_certificate.type_i_normal_tail_deflation_witness(
                    prime, gap, a, b
                )
                if witness is None:
                    continue
                return {
                    "prime": prime,
                    "b": b,
                    "gap": gap,
                    "a": a,
                    "c": x // (a * b),
                    "source_denominator": witness.source_denominator,
                    "quotient": witness.quotient,
                    "divisor": witness.certificate.divisor,
                }
    return None


def run_profile(
    limit: int = DEFAULT_LIMIT,
    gap_cap: int = DEFAULT_GAP_CAP,
    b_cap: int = DEFAULT_B_CAP,
) -> dict[str, object]:
    """Audit the complete small-B, small-gap, certificate-and-source box."""
    if limit < 73:
        raise ValueError("limit must be at least 73")
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    if b_cap < 1:
        raise ValueError("b_cap must be positive")
    spf = short_certificate.smallest_prime_factors((limit + gap_cap) // 4 + 1)
    counts: dict[int, int] = {}
    examples: dict[int, dict[str, int]] = {}
    misses: list[int] = []
    core_prime_count = 0
    for prime in short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        core_prime_count += 1
        witness = first_joint_witness(prime, spf, gap_cap, b_cap)
        if witness is None:
            misses.append(prime)
            continue
        b = witness["b"]
        counts[b] = counts.get(b, 0) + 1
        examples.setdefault(b, witness)
    return {
        "arithmetic": (
            "for each core prime, enumerate every normal-form A at each "
            "B=1,...,B_cap and m=3 (mod 4) through the gap cap; retain only "
            "certificates whose p-divisible tail has the exact strict source "
            "deflation, and verify both source and target identities"
        ),
        "scope_note": (
            "Finite joint selector profile. Its tail deflations are a "
            "certificate-side parametrization of the existing complete "
            "quadratic external-source family, not a new descent mechanism."
        ),
        "prime_limit": limit,
        "gap_cap": gap_cap,
        "b_cap": b_cap,
        "core_prime_count": core_prime_count,
        "captured_count": core_prime_count - len(misses),
        "misses": misses,
        "first_joint_b_counts": {str(b): counts[b] for b in sorted(counts)},
        "first_joint_examples": {str(b): examples[b] for b in sorted(examples)},
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
