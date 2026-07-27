#!/usr/bin/env python3
"""Audit nonuniform cyclic lifts from a minimal nonstandard repeated-tail source.

For k >= 1, n = 4k - 2 has the explicit source solution

    4/n = 1/k + 2/(n*k).

For reduced 0 < r < s, the weighted cyclic transport has target denominators

    A = p*s*k / (4*r*k + s - 3*r),
    B = p*k,
    C = p*s*k / (4*(s-r)*k - 2*s + 3*r).

This turns the search into two exact divisibility checks. It is a finite
boundary audit, not a claim that the bounded weight box is globally complete.
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
RESULTS = ROOT / "reproductions" / "weighted-cyclic-repeated-tail-5k-s50-results.json"


def load_cyclic_module():
    spec = importlib.util.spec_from_file_location(
        "weighted_repeated_tail_cyclic", ROOT / "reproductions" / "cyclic_reciprocal_lift.py"
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load cyclic_reciprocal_lift.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


cyclic = load_cyclic_module()


def weights(weight_denominator_bound: int):
    """Yield every reduced r/s with 0 < r < s <= the stated bound."""
    if weight_denominator_bound < 2:
        raise ValueError("weight_denominator_bound must be at least 2")
    for denominator in range(2, weight_denominator_bound + 1):
        for numerator in range(1, denominator):
            if math.gcd(numerator, denominator) == 1:
                yield numerator, denominator


def witness_at(
    prime: int, numerator: int, denominator: int, k: int
) -> dict[str, object] | None:
    """Recover and exactly verify one repeated-tail weighted cyclic witness."""
    source_denominator = 4 * k - 2
    if source_denominator >= prime:
        return None
    first = k
    repeated = source_denominator * k
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
    source = (first, repeated, repeated)
    if sum((Fraction(1, value) for value in source), Fraction()) != Fraction(
        4, source_denominator
    ):
        raise AssertionError("repeated-tail source reconstruction failed")
    if target != cyclic.weighted_cyclic_target(
        prime, source_denominator, source, numerator, denominator
    ):
        raise AssertionError("closed-form target disagrees with cyclic transport")
    return {
        "weight_numerator": numerator,
        "weight_denominator": denominator,
        "k": k,
        "source_denominator": source_denominator,
        "source_solution": list(source),
        "target_solution": list(target),
    }


def run_audit(limit: int, weight_denominator_bound: int) -> dict[str, object]:
    """Search the stated core-prime and rational-weight box exactly."""
    if limit < 2:
        raise ValueError("limit must be at least 2")
    weight_list = list(weights(weight_denominator_bound))
    records = []
    candidates_checked = 0
    for prime in cyclic.core_primes(limit):
        witnesses = []
        for numerator, denominator in weight_list:
            for k in range(1, (prime + 1) // 4 + 1):
                candidates_checked += 1
                witness = witness_at(prime, numerator, denominator, k)
                if witness is not None:
                    witnesses.append(witness)
        records.append({"prime": prime, "witnesses": witnesses})
    return {
        "arithmetic": "exact integer divisibility and fractions.Fraction verification",
        "scope_note": (
            "The source family, prime range, and rational-weight denominator "
            "bound are finite. Empty output does not exclude larger weights, "
            "other nonstandard sources, offsets, or noncyclic transports."
        ),
        "limit": limit,
        "weight_denominator_bound": weight_denominator_bound,
        "core_primes": len(records),
        "weights": len(weight_list),
        "candidates_checked": candidates_checked,
        "records": records,
        "witnesses": sum(len(record["witnesses"]) for record in records),
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
