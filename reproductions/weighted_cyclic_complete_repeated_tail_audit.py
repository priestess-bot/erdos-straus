#!/usr/bin/env python3
"""Exhaust every repeated-tail source for a bounded weighted cyclic box.

Any source of the form 4/n = 1/a + 2/b that can enter a weighted cyclic
target must have b = n*k. Its source equation then forces

    a = n*k / (4*k - 2).

The least possible source denominator is (4*k - 2) / gcd(k, 4*k - 2).
It is below p exactly when some repeated-tail source with this k is below p.
Thus the audit is complete for this source shape in its p and weight box.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "weighted-cyclic-complete-repeated-tail-5k-s50-results.json"


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


cyclic = load_module("complete_repeated_tail_cyclic", "cyclic_reciprocal_lift.py")


def weights(weight_denominator_bound: int):
    """Yield every reduced r/s with 0 < r < s <= the stated bound."""
    if weight_denominator_bound < 2:
        raise ValueError("weight_denominator_bound must be at least 2")
    for denominator in range(2, weight_denominator_bound + 1):
        for numerator in range(1, denominator):
            if math.gcd(numerator, denominator) == 1:
                yield numerator, denominator


def minimal_source(k: int) -> tuple[int, tuple[int, int, int]]:
    """Return the least positive repeated-tail source for a fixed b/n = k."""
    if k < 1:
        raise ValueError("k must be positive")
    source_denominator = (4 * k - 2) // math.gcd(k, 4 * k - 2)
    first_numerator = source_denominator * k
    if first_numerator % (4 * k - 2):
        raise AssertionError("minimal source denominator failed integrality")
    first = first_numerator // (4 * k - 2)
    repeated = source_denominator * k
    source = (first, repeated, repeated)
    if sum((Fraction(1, value) for value in source), Fraction()) != Fraction(
        4, source_denominator
    ):
        raise AssertionError("minimal repeated-tail source failed reconstruction")
    return source_denominator, source


def witness_at(
    prime: int, numerator: int, denominator: int, k: int
) -> dict[str, object] | None:
    """Recover and exactly verify a complete repeated-tail weighted witness."""
    source_denominator, source = minimal_source(k)
    if source_denominator >= prime:
        return None
    divisor_a = 4 * numerator * k + denominator - 3 * numerator
    divisor_c = (
        4 * (denominator - numerator) * k - 2 * denominator + 3 * numerator
    )
    product = prime * denominator * k
    if product % divisor_a or product % divisor_c:
        return None
    target = (
        product // divisor_a,
        prime * k,
        product // divisor_c,
    )
    expected = cyclic.weighted_cyclic_target(
        prime, source_denominator, source, numerator, denominator
    )
    if tuple(target) != expected:
        raise AssertionError("closed-form target disagrees with cyclic transport")
    p_divisible_indices = [
        index for index, value in enumerate(target) if value % prime == 0
    ]
    return {
        "weight_numerator": numerator,
        "weight_denominator": denominator,
        "k": k,
        "source_denominator": source_denominator,
        "source_solution": list(source),
        "target_solution": list(target),
        "p_divisible_indices": p_divisible_indices,
        "p_divisible_count": len(p_divisible_indices),
    }


def has_integral_target(
    prime: int, numerator: int, denominator: int, k: int
) -> bool:
    """Check the two closed-form divisibility conditions without reconstruction."""
    divisor_a = 4 * numerator * k + denominator - 3 * numerator
    divisor_c = (
        4 * (denominator - numerator) * k - 2 * denominator + 3 * numerator
    )
    product = prime * denominator * k
    return product % divisor_a == 0 and product % divisor_c == 0


def run_audit(limit: int, weight_denominator_bound: int) -> dict[str, object]:
    """Exhaust all repeated-tail source shapes in the stated finite box."""
    if limit < 2:
        raise ValueError("limit must be at least 2")
    weight_list = list(weights(weight_denominator_bound))
    records = []
    candidates_checked = 0
    for prime in cyclic.core_primes(limit):
        witnesses = []
        valid_k = [
            k
            for k in range(1, (prime + 1) // 2 + 1)
            if minimal_source(k)[0] < prime
        ]
        for numerator, denominator in weight_list:
            for k in valid_k:
                candidates_checked += 1
                if has_integral_target(prime, numerator, denominator, k):
                    witness = witness_at(prime, numerator, denominator, k)
                    if witness is None:
                        raise AssertionError("fast divisibility check disagrees with witness")
                    witnesses.append(witness)
        records.append({"prime": prime, "witnesses": witnesses})
    witnesses = [
        witness
        for record in records
        for witness in record["witnesses"]
    ]
    return {
        "arithmetic": "exact integer divisibility and fractions.Fraction verification",
        "scope_note": (
            "This exhausts sources with exactly two equal denominators inside "
            "the stated p and rational-weight box. It does not exclude three "
            "distinct source terms, offsets, or noncyclic transports."
        ),
        "limit": limit,
        "weight_denominator_bound": weight_denominator_bound,
        "core_primes": len(records),
        "weights": len(weight_list),
        "candidates_checked": candidates_checked,
        "records": records,
        "witnesses": len(witnesses),
        "witnesses_with_two_p_divisible_target_terms": sum(
            witness["p_divisible_count"] >= 2 for witness in witnesses
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5_000)
    parser.add_argument("--weight-denominator-bound", type=int, default=50)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.weight_denominator_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
