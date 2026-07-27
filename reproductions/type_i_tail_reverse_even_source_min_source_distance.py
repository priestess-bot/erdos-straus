#!/usr/bin/env python3
"""Minimize Type I even-source distance on all 500M ordinary-tail misses."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_GAP_CAP = 215
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-tail-reverse-even-source-min-source-distance-500m-results.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("minimum_even_source_distance_landscape", LANDSCAPE)
bridge = load_module("minimum_even_source_distance_bridge", BRIDGE)


def minimum_source_edge(
    prime: int, gap_cap: int
) -> tuple[dict[str, object] | None, int, int]:
    """Exhaust the stated Type I box and select its least even source distance."""
    best: dict[str, object] | None = None
    forms = 0
    lifts_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            for lift in lifts:
                lifts_checked += 1
                source = int(lift["source_denominator"])
                if source % 2:
                    continue
                bridge_divisor = int(lift["bridge_divisor"])
                if bridge_divisor % (prime * prime):
                    raise AssertionError("bridge divisor did not reconstruct E")
                E = bridge_divisor // (prime * prime)
                distance = prime - source
                candidate = {
                    "source_distance": distance,
                    "gap": gap,
                    "normal_form": [A, B, C],
                    "E": E,
                    "reverse_two_tail_lift": lift,
                }
                key = (
                    distance,
                    gap,
                    B,
                    E,
                    int(lift["source_term"]),
                )
                if best is None or key < (
                    int(best["source_distance"]),
                    int(best["gap"]),
                    int(best["normal_form"][1]),
                    int(best["E"]),
                    int(best["reverse_two_tail_lift"]["source_term"]),
                ):
                    best = candidate
    return best, forms, lifts_checked


def distance_bucket(distance: int, prime: int) -> str:
    if distance <= 29:
        return "<=29"
    if distance <= 1_000:
        return "<=1000"
    if distance * 1_000 <= prime:
        return "<=p/1000"
    if distance * 100 <= prime:
        return "<=p/100"
    if distance * 10 <= prime:
        return "<=p/10"
    return ">p/10"


def run_audit(tail: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    """Compute the exact minimum source distance within the stated finite box."""
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms = 0
    lifts = 0
    for entry in tail["misses"]:
        prime = int(entry["prime"])
        witness, local_forms, local_lifts = minimum_source_edge(prime, gap_cap)
        forms += local_forms
        lifts += local_lifts
        if witness is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, "minimum_source_witness": witness})
    bucket_histogram: dict[str, int] = {}
    for record in records:
        distance = int(record["minimum_source_witness"]["source_distance"])
        bucket = distance_bucket(distance, int(record["prime"]))
        bucket_histogram[bucket] = bucket_histogram.get(bucket, 0) + 1
    return {
        "arithmetic": (
            "for every stored ordinary Type II p-1-tail miss, enumerate every Type I "
            "normal form and strict maximum-tail reverse lift through gap_cap; retain "
            "even sources and select the least source distance p-n with deterministic ties"
        ),
        "scope_note": (
            "A complete finite minimum-distance profile for the target-side Type I "
            "selector. It does not bound source distance outside the stated prime and gap box."
        ),
        "input_tail_audit": TAIL.name,
        "prime_limit": tail["prime_limit"],
        "ordinary_tail_miss_count": len(tail["misses"]),
        "gap_cap": gap_cap,
        "captured_count": len(records),
        "misses": misses,
        "normal_forms_exhaustively_checked": forms,
        "strict_reverse_lifts_exhaustively_checked": lifts,
        "short_distance_le_29_count": sum(
            int(record["minimum_source_witness"]["source_distance"]) <= 29
            for record in records
        ),
        "maximum_minimum_source_distance": max(
            (int(record["minimum_source_witness"]["source_distance"]) for record in records),
            default=None,
        ),
        "minimum_source_distance_bucket_histogram": bucket_histogram,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.tail.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
