#!/usr/bin/env python3
"""Direct target-level small-B even-source audit on the H19 and 500M bridge profiles."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
H19 = ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json"
TAIL = ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json"
SUPPORT_MIN = ROOT / "reproductions" / "type_i_tail_reverse_even_source_support_minimization.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-direct-small-b-even-source-audit-results.json"
GAP_CAP = 215


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


support_min = load_module("direct_small_b_support_min", SUPPORT_MIN)


def first_witness(prime: int, B: int) -> dict[str, object] | None:
    for gap in range(3, GAP_CAP + 1, 4):
        for entry in support_min.landscape.gap_landscape(prime, gap)["type_i"]:
            A, form_B, C = (int(value) for value in entry["normal_form"])
            if form_B != B:
                continue
            _, lifts = support_min.bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, form_B, C)
            for lift in lifts:
                source = int(lift["source_denominator"])
                if source % 2:
                    continue
                return {
                    "gap": gap,
                    "normal_form": [A, form_B, C],
                    "source_denominator": source,
                    "source_term": int(lift["source_term"]),
                    "bridge_factor": int(lift["bridge_divisor"]) // (prime * prime),
                }
    return None


def staged_audit(primes: list[int], stages: list[int], label: str) -> dict[str, object]:
    remaining = set(primes)
    stage_records = []
    all_records = []
    for B in stages:
        records = []
        for prime in sorted(remaining):
            witness = first_witness(prime, B)
            if witness is not None:
                records.append({"prime": prime, "B": B, "witness": witness})
        remaining.difference_update(record["prime"] for record in records)
        all_records.extend(records)
        stage_records.append({"B": B, "captured_count": len(records), "records": records})
    return {
        "label": label,
        "input_count": len(primes),
        "gap_cap": GAP_CAP,
        "stages": stage_records,
        "captured_count": len(all_records),
        "misses": sorted(remaining),
        "maximum_selected_gap": max((record["witness"]["gap"] for record in all_records), default=None),
    }


def run_audit(h19: dict[str, object], tail: dict[str, object]) -> dict[str, object]:
    h19_primes = [int(record["prime"]) for record in h19["records"]]
    tail_primes = [int(record["prime"]) for record in tail["records"]]
    if len(h19_primes) != 664 or len(tail_primes) != 1717:
        raise AssertionError("inputs do not match the stored H19 and 500M bridge profiles")
    h19_result = staged_audit(h19_primes, [1], "H19-1B")
    tail_result = staged_audit(tail_primes, [1, 2, 8], "tail-500M")
    if h19_result["misses"] or tail_result["misses"]:
        raise AssertionError("small-B stages did not close the stored direct target sets")
    if [stage["captured_count"] for stage in h19_result["stages"]] != [664]:
        raise AssertionError("H19 direct B=1 closure changed")
    if [stage["captured_count"] for stage in tail_result["stages"]] != [1713, 3, 1]:
        raise AssertionError("500M direct B menu closure changed")
    return {
        "arithmetic": (
            "for every target in each stored bridge profile, enumerate all Type I normal forms through "
            "m<=215 with the staged fixed B values, then all maximum-tail reverse lifts and retain exact "
            "even strict sources"
        ),
        "scope_note": (
            "A direct target-level finite audit independent of which source state was previously selected. "
            "It does not provide a global B menu or a recursive rule selecting a normal form."
        ),
        "profiles": [h19_result, tail_result],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h19", type=Path, default=H19)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.h19.read_text(encoding="utf-8")),
        json.loads(args.tail.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "profiles": [
                    {
                        "label": profile["label"],
                        "input_count": profile["input_count"],
                        "stage_counts": [stage["captured_count"] for stage in profile["stages"]],
                        "misses": profile["misses"],
                        "maximum_selected_gap": profile["maximum_selected_gap"],
                    }
                    for profile in result["profiles"]
                ]
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
