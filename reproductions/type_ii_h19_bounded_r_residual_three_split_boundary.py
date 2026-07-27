#!/usr/bin/env python3
"""Audit n/3 residual splits on bounded-r tail-obstruction source rays."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
OBSTRUCTION_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-tail-obstruction-1b-results.json"
SMALL_R_SCRIPT = ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-residual-three-split-boundary-1b-results.json"


def load_small_r():
    spec = importlib.util.spec_from_file_location(
        "bounded_r_residual_three_split_small_r", SMALL_R_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SMALL_R_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


small_r = load_small_r()


def residual_three_split_witness(prime: int, source: int) -> dict[str, object] | None:
    """Exhaust source solutions retaining source/3 and one tail denominator."""
    first = source // 3
    if source % 3 or not prime // 4 < first <= prime // 2:
        return None
    for factor in sympy.divisors(source * source):
        if factor > source:
            break
        companion = source * source // factor
        left = source + factor
        right = source + companion
        for replaced, preserved in ((left, right), (right, left)):
            denominator = source * prime - 4 * (prime - source) * replaced
            if denominator <= 0 or (source * prime * replaced) % denominator:
                continue
            lifted = source * prime * replaced // denominator
            if preserved < first or lifted < first:
                continue
            source_solution = (first, left, right)
            target_solution = (first, preserved, lifted)
            if (
                Fraction(4, source)
                != sum((Fraction(1, value) for value in source_solution), Fraction())
                or Fraction(4, prime)
                != sum((Fraction(1, value) for value in target_solution), Fraction())
            ):
                raise AssertionError("residual-three lift identity did not verify")
            return {
                "factor": factor,
                "replaced": replaced,
                "source_solution": list(source_solution),
                "target_solution": list(target_solution),
            }
    return None


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Check all supplied rays for the complete n/3 residual split family."""
    records = []
    total_rays = 0
    eligible_rays = 0
    hit_count = 0
    for row in payload["records"]:
        prime = int(row["prime"])
        rays = []
        for state in row["states"]:
            r = int(state["r"])
            for ray in small_r.compatible_rays(prime, r):
                total_rays += 1
                source = prime - int(ray["distance"])
                first = source // 3
                eligible = (
                    source % 3 == 0
                    and prime // 4 < first <= prime // 2
                )
                eligible_rays += eligible
                witness = residual_three_split_witness(prime, source) if eligible else None
                hit_count += witness is not None
                rays.append(
                    {
                        "r": r,
                        "distance": int(ray["distance"]),
                        "d": int(ray["d"]),
                        "source_denominator": source,
                        "eligible_residual_three_split": eligible,
                        "witness": witness,
                    }
                )
        records.append({"prime": prime, "source_rays": rays})
    return {
        "arithmetic": (
            "exact enumeration of every divisor e of each eligible source square, "
            "the exact two-denominator lift criterion, and rational source/target "
            "identity verification"
        ),
        "scope_note": (
            "This only excludes the complete n/3 residual split on the supplied "
            "bounded-r source rays. It does not exclude other source families, "
            "other retained denominators, or multi-step lifts."
        ),
        "prime_limit": payload["prime_limit"],
        "r_cap": payload["r_cap"],
        "residual_prime_count": len(records),
        "source_ray_count": total_rays,
        "eligible_residual_three_split_ray_count": eligible_rays,
        "residual_three_split_hit_count": hit_count,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=OBSTRUCTION_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
