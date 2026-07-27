#!/usr/bin/env python3
"""Reduce nonmultiple scaled-source candidates to finite divisor tables."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
OBSTRUCTION_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-tail-obstruction-1b-results.json"
SMALL_R_SCRIPT = ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-scaled-source-candidates-1b-results.json"


def load_small_r():
    spec = importlib.util.spec_from_file_location(
        "bounded_r_scaled_source_candidates_small_r", SMALL_R_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SMALL_R_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


small_r = load_small_r()


def scaled_candidates(prime: int, source: int) -> list[dict[str, int]]:
    """Enumerate every b=2 or 4 scaled source passing the structural divisibilities."""
    if not 2 <= source < prime:
        raise ValueError("source must be strictly between one and prime")
    distance = prime - source
    candidates = []
    for denominator in (2, 4):
        if source % denominator:
            continue
        for shift in sympy.divisors(source // denominator):
            numerator = denominator * (prime - shift)
            if numerator % (4 * distance):
                continue
            numerator_scale = numerator // (4 * distance)
            if numerator_scale <= 0 or math.gcd(numerator_scale, denominator) != 1:
                continue
            first = numerator_scale * source // denominator
            if first % shift:
                raise AssertionError("divisor reduction did not recover the first-term divisibility")
            candidates.append(
                {
                    "a": numerator_scale,
                    "b": denominator,
                    "shift": int(shift),
                    "source_first_denominator": first,
                }
            )
    return candidates


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compile every finite scaled-source candidate on the bounded-r source rays."""
    records = []
    all_candidates = []
    unique_candidates: set[tuple[int, int, int, int, int]] = set()
    source_ray_count = 0
    for row in payload["records"]:
        prime = int(row["prime"])
        rays = []
        for state in row["states"]:
            r = int(state["r"])
            for ray in small_r.compatible_rays(prime, r):
                source_ray_count += 1
                source = prime - int(ray["distance"])
                candidates = scaled_candidates(prime, source)
                all_candidates.extend(candidates)
                unique_candidates.update(
                    (
                        prime,
                        source,
                        candidate["a"],
                        candidate["b"],
                        candidate["shift"],
                    )
                    for candidate in candidates
                )
                rays.append(
                    {
                        "r": r,
                        "distance": int(ray["distance"]),
                        "d": int(ray["d"]),
                        "source_denominator": source,
                        "candidate_count": len(candidates),
                    }
                )
        records.append({"prime": prime, "source_rays": rays})
    denominator_histogram = Counter(candidate["b"] for candidate in all_candidates)
    return {
        "arithmetic": (
            "exact divisor enumeration of n/2 and n/4 after the scaled-source "
            "shift-divisor reduction"
        ),
        "scope_note": (
            "This is a structural candidate profile only. It does not assert "
            "that any candidate satisfies the remaining square-tail conditions."
        ),
        "prime_limit": payload["prime_limit"],
        "r_cap": payload["r_cap"],
        "residual_prime_count": len(records),
        "source_ray_count": source_ray_count,
        "scaled_source_candidate_count": len(all_candidates),
        "unique_scaled_source_candidate_count": len(unique_candidates),
        "candidate_denominator_histogram": {
            str(key): value for key, value in sorted(denominator_histogram.items())
        },
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
