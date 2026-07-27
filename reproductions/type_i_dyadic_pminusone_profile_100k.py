#!/usr/bin/env python3
"""Exhaust the complete dyadic p-1 Type I factor-pair selector through 100K."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SELECTOR = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_LIMIT = 100_009
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-dyadic-pminusone-profile-100k-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


selector = load_module("dyadic_pminusone_profile_selector", SELECTOR)
landscape = selector.direct.support_min.landscape


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("value must be positive")
    return (value & -value).bit_length() - 1


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [base * prime**power for base in divisors for power in range(exponent + 1)]
    return sorted(divisors)


def first_dyadic_witness(prime: int) -> dict[str, int] | None:
    """Exhaust every E=2^t allowed by the source-square condition and every BC|K."""
    for exponent in range(2, 2 * v2(prime - 1) - 1):
        R = (1 << exponent) - 1
        K = (prime * R + 1) // 4
        factors = landscape.factor_by_trial_division(K)
        divisors = divisors_from_factorization(factors)
        for B in divisors:
            quotient = K // B
            for C in divisors:
                if quotient % C:
                    continue
                witness = selector.dyadic_p_minus_one_witness(prime, exponent, B, C)
                if witness is not None:
                    return {
                        "exponent": exponent,
                        "B": B,
                        "C": C,
                        "gap": int(witness["gap"]),
                        "source_denominator": int(witness["source_denominator"]),
                    }
    return None


def run_profile(limit: int = DEFAULT_LIMIT) -> dict[str, object]:
    """Profile the full source-square-allowed dyadic p-1 selector."""
    if limit < 73:
        raise ValueError("limit must be at least 73")
    records = []
    misses = []
    for prime in landscape.short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        witness = first_dyadic_witness(prime)
        records.append({"prime": prime, "witness": witness})
        if witness is None:
            misses.append(prime)
    witnesses = [record["witness"] for record in records if record["witness"] is not None]
    exponent_histogram = Counter(str(witness["exponent"]) for witness in witnesses)
    b_histogram = Counter(str(witness["B"]) for witness in witnesses)
    return {
        "arithmetic": (
            "for each core prime p, take every exponent 2<=t<=2v2(p-1)-2 allowed exactly by "
            "2^t|(p-1)^2/4; factor K=((2^t-1)p+1)/4, enumerate every B,C with BC|K, and check the "
            "dyadic p-1 factor-pair criterion with exact source and target identities"
        ),
        "scope_note": (
            "Complete finite profile of the dyadic p-1 maximum-tail subfamily only. A miss does not exclude "
            "other sources, non-dyadic bridges, alternate coordinates, or Type II descent."
        ),
        "prime_limit": limit,
        "core_prime_count": len(records),
        "captured_count": len(witnesses),
        "misses": misses,
        "maximum_allowed_exponent": max((2 * v2(record["prime"] - 1) - 2 for record in records), default=None),
        "maximum_selected_exponent": max((witness["exponent"] for witness in witnesses), default=None),
        "selected_exponent_histogram": dict(sorted(exponent_histogram.items(), key=lambda item: int(item[0]))),
        "selected_b_histogram": dict(sorted(b_histogram.items(), key=lambda item: int(item[0]))),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
