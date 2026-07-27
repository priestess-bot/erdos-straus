#!/usr/bin/env python3
"""Test one-prime mixed-factor descents on the H19 radius-six misses."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-mixed-short-or-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-mixed-only-prime-factor-profile-1b-results.json"


def prime_mixed_witness(prime: int) -> dict[str, int] | None:
    """Find the least scale with a prime g satisfying the mixed criterion."""
    for k in sympy.divisors((prime - 1) // 4):
        k = int(k)
        q = 4 * k - 1
        n = (q * prime + 1) // (q + 1)
        if (q + 1) * n != q * prime + 1:
            raise AssertionError("external source denominator did not reconstruct")
        for factor in sympy.factorint(k * n):
            factor = int(factor)
            if factor <= n and factor % q == q - 1:
                return {"k": k, "q": q, "source_denominator": n, "factor": factor}
    return None


def minimum_support_mixed_witness(prime: int) -> dict[str, object] | None:
    """Find a mixed witness with the fewest distinct prime factors in g."""
    best: dict[str, object] | None = None
    for k in sympy.divisors((prime - 1) // 4):
        k = int(k)
        q = 4 * k - 1
        n = (q * prime + 1) // (q + 1)
        if (q + 1) * n != q * prime + 1:
            raise AssertionError("external source denominator did not reconstruct")
        for factor in sympy.divisors(k * n):
            factor = int(factor)
            if factor > n or factor % q != q - 1:
                continue
            factorization = sympy.factorint(factor)
            candidate = {
                "distinct_prime_support": len(factorization),
                "k": k,
                "q": q,
                "source_denominator": n,
                "factor": factor,
                "factorization": {str(key): value for key, value in factorization.items()},
            }
            if best is None or (
                candidate["distinct_prime_support"],
                candidate["k"],
                candidate["factor"],
            ) < (
                best["distinct_prime_support"],
                best["k"],
                best["factor"],
            ):
                best = candidate
    return best


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Measure which mixed-only points need a composite divisor g."""
    records = payload["mixed_factor_only_records"]
    if not records:
        raise ValueError("input profile has no mixed-factor-only records")
    audited = []
    for record in records:
        prime = int(record["prime"])
        composite = record["mixed_factor_descent"]
        one_prime = prime_mixed_witness(prime)
        minimum_support = minimum_support_mixed_witness(prime)
        if minimum_support is None:
            raise AssertionError("stored mixed-factor point has no mixed witness")
        if one_prime is None:
            factor = int(composite["factor"])
            factorization = {str(key): value for key, value in sympy.factorint(factor).items()}
            if len(factorization) < 2:
                raise AssertionError("one-prime miss did not use a composite stored factor")
        else:
            factorization = None
        audited.append(
            {
                "prime": prime,
                "one_prime_mixed_witness": one_prime,
                "minimum_support_mixed_witness": minimum_support,
                "stored_mixed_factor_descent": composite,
                "stored_factor_factorization": factorization,
            }
        )
    one_prime = [record for record in audited if record["one_prime_mixed_witness"] is not None]
    composite_only = [record for record in audited if record["one_prime_mixed_witness"] is None]
    support_histogram: dict[str, int] = {}
    for record in audited:
        support = str(record["minimum_support_mixed_witness"]["distinct_prime_support"])
        support_histogram[support] = support_histogram.get(support, 0) + 1
    return {
        "arithmetic": (
            "exact factorization of k*n for every k dividing (p-1)/4, with "
            "the mixed congruence g=-1 mod (4k-1) checked for each prime factor"
        ),
        "scope_note": (
            "A finite audit of the 17 H19 states that require mixed-factor descent "
            "after the radius-six AC filter. It does not prove a global selector."
        ),
        "prime_limit": payload["prime_limit"],
        "mixed_factor_only_count": len(audited),
        "one_prime_mixed_captured_count": len(one_prime),
        "one_prime_mixed_missing_primes": [record["prime"] for record in composite_only],
        "minimum_distinct_prime_support_histogram": support_histogram,
        "two_prime_mixed_missing_primes": [
            record["prime"]
            for record in audited
            if record["minimum_support_mixed_witness"]["distinct_prime_support"] > 2
        ],
        "composite_factor_required_records": composite_only,
        "records": audited,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
