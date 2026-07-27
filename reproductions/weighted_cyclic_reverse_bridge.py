#!/usr/bin/env python3
"""Exact reverse audit for weighted cyclic three-coordinate lifts.

For source reciprocal vector t and target vector t', the weighted cyclic map is

    t' = n/(p*s) (r I + (s-r) P) t,

where P cycles coordinates forward. The inverse is explicit because P^3 = I.
For a fixed target and reduced r/s, each source coordinate is H_i / n. The
least possible n is the least common multiple of the reduced H_i numerators,
so this decides exactly whether a strict integer source exists.
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
RESULTS = ROOT / "reproductions" / "weighted-cyclic-reverse-bridge-2451289-ac14-s20-results.json"


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


targeted_bridge = load_module("weighted_cyclic_targeted_bridge", "targeted_descent_bridge.py")


def weights(weight_denominator_bound: int):
    """Yield every reduced r/s with 0 < r < s <= the given bound."""
    if weight_denominator_bound < 2:
        raise ValueError("weight_denominator_bound must be at least 2")
    for denominator in range(2, weight_denominator_bound + 1):
        for numerator in range(1, denominator):
            if math.gcd(numerator, denominator) == 1:
                yield numerator, denominator


def inverse_profile(
    prime: int,
    target: tuple[int, int, int],
    numerator: int,
    denominator: int,
) -> tuple[Fraction, Fraction, Fraction]:
    """Return H such that every inverse source reciprocal vector is H / n."""
    if (
        prime < 2
        or numerator <= 0
        or numerator >= denominator
        or math.gcd(numerator, denominator) != 1
    ):
        raise ValueError("invalid prime or reduced weight")
    q = denominator - numerator
    target_reciprocals = tuple(Fraction(1, value) for value in target)
    inverse_denominator = numerator**3 + q**3
    profile = tuple(
        Fraction(prime * denominator, inverse_denominator)
        * (
            numerator * numerator * target_reciprocals[index]
            - numerator * q * target_reciprocals[(index + 1) % 3]
            + q * q * target_reciprocals[(index + 2) % 3]
        )
        for index in range(3)
    )
    return profile


def least_source_denominator(profile: tuple[Fraction, Fraction, Fraction]) -> int | None:
    """Return the least n >= 2 making all coordinates n / H_i integral."""
    if any(value <= 0 for value in profile):
        return None
    multiple = 1
    for value in profile:
        multiple = math.lcm(multiple, value.numerator)
    return multiple if multiple >= 2 else 2


def reverse_lift(
    prime: int,
    target: tuple[int, int, int],
    numerator: int,
    denominator: int,
) -> dict[str, object] | None:
    """Return the least strict integer inverse source, if one exists."""
    profile = inverse_profile(prime, target, numerator, denominator)
    source_denominator = least_source_denominator(profile)
    if source_denominator is None or source_denominator >= prime:
        return None
    source = tuple(
        source_denominator * value.denominator // value.numerator for value in profile
    )
    if sum((Fraction(1, value) for value in source), Fraction()) != Fraction(
        4, source_denominator
    ):
        raise AssertionError("inverse profile did not reconstruct the source equation")

    q = denominator - numerator
    recovered = []
    for first, second in zip(source, source[1:] + source[:1]):
        reciprocal = Fraction(source_denominator, prime * denominator) * (
            Fraction(numerator, first) + Fraction(q, second)
        )
        if reciprocal.numerator != 1:
            raise AssertionError("inverse profile did not recover unit target terms")
        recovered.append(reciprocal.denominator)
    if tuple(recovered) != target:
        raise AssertionError("inverse profile recovered the wrong target")
    return {
        "weight_numerator": numerator,
        "weight_denominator": denominator,
        "source_denominator": source_denominator,
        "source_solution": list(source),
        "source_distinct_denominators": len(set(source)),
        "target_solution": list(target),
    }


def ac_reverse_audit(
    prime: int, ac_bound: int, weight_denominator_bound: int
) -> dict[str, object]:
    """Audit every bounded-AC target solution against all bounded weights."""
    if ac_bound < 1:
        raise ValueError("ac_bound must be positive")
    raw = targeted_bridge.ac_first_term_audit(prime, ac_bound)
    records = []
    weight_list = list(weights(weight_denominator_bound))
    for record in raw["records"]:
        solution = targeted_bridge.type_ii_solution(
            prime, record["a"], record["c"], record["k"]
        )
        target = (solution["x"], solution["y"], solution["z"])
        lifts = [
            lift
            for numerator, denominator in weight_list
            if (
                lift := reverse_lift(prime, target, numerator, denominator)
            )
            is not None
        ]
        records.append(
            {
                "a": record["a"],
                "c": record["c"],
                "k": record["k"],
                "h": record["h"],
                "gap": solution["gap"],
                "target_solution": list(target),
                "reverse_weighted_cyclic_lifts": lifts,
            }
        )
    return {
        "arithmetic": "exact fractions.Fraction inverse matrix and integer reconstruction",
        "scope_note": (
            "This fixes the target AC box and the rational-weight denominator "
            "bound. Empty output excludes every strict weighted cyclic inverse "
            "source for those targets and weights, but not larger boxes, "
            "noncyclic maps, or offset transports."
        ),
        "prime": prime,
        "ac_bound": ac_bound,
        "weight_denominator_bound": weight_denominator_bound,
        "target_solutions": len(records),
        "records": records,
        "reverse_weighted_cyclic_lifts": sum(
            len(record["reverse_weighted_cyclic_lifts"]) for record in records
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=2_451_289)
    parser.add_argument("--ac-bound", type=int, default=14)
    parser.add_argument("--weight-denominator-bound", type=int, default=20)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = ac_reverse_audit(
        args.prime, args.ac_bound, args.weight_denominator_bound
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
