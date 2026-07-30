#!/usr/bin/env python3
"""Audit cross-color pair capacity for F states without a same-color pair."""

from __future__ import annotations

import argparse
from collections import defaultdict
import importlib.util
import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
CAPACITY_SCRIPT = ROOT / "reproductions" / "type_i_f_same_color_subset_capacity.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-full-cross-color-pair-capacity-results.json"


def load_capacity_module():
    spec = importlib.util.spec_from_file_location("cross_color_capacity", CAPACITY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {CAPACITY_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


capacity = load_capacity_module()


def cross_color_assignments(
    record: dict[str, object],
    states_by_R: dict[int, list[tuple[int, int]]],
) -> list[dict[str, object]]:
    prime = int(record["prime"])
    R = int(record["R"])
    active = tuple(sorted(int(q) for q in record["active_primes"]))
    required = capacity.required_heights(record)
    best: dict[tuple[int, int], dict[str, object]] = {}
    for a, s in states_by_R[R]:
        a_block = a * R + 1
        s_block = s * R + 1
        for q_a, q_s in itertools.permutations(active, 2):
            h_a = capacity.valuation(a_block, q_a)
            h_s = capacity.valuation(s_block, q_s)
            if h_a < required[q_a] or h_s < required[q_s]:
                continue
            choice = {
                "prime": prime,
                "R": R,
                "q_a": q_a,
                "q_s": q_s,
                "a": a,
                "s": s,
                "a_block": a_block,
                "s_block": s_block,
                "required_a": required[q_a],
                "required_s": required[q_s],
                "actual_a": h_a,
                "actual_s": h_s,
                "actual_product": h_a * h_s,
            }
            previous = best.get((q_a, q_s))
            if previous is None or (
                choice["actual_product"], -a, -s
            ) > (previous["actual_product"], -int(previous["a"]), -int(previous["s"])):
                best[(q_a, q_s)] = choice
    return list(best.values())


def run() -> dict[str, object]:
    records, _complete_states = capacity.load_inputs()
    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    cross_groups: dict[tuple[int, int, int], list[dict[str, object]]] = defaultdict(list)
    unresolved_records = []
    all_active_records = [record for record in records if len(record["active_primes"]) >= 2]
    records_by_prime: dict[int, list[dict[str, object]]] = defaultdict(list)
    for record in all_active_records:
        records_by_prime[int(record["prime"])].append(record)

    for index, prime in enumerate(sorted(records_by_prime), start=1):
        _bound, source_cache[prime] = capacity.source.enumerate_linear_source_states(prime)
        for record in records_by_prime[prime]:
            same_color = capacity.choose_same_color_assignment(record, source_cache[prime])
            if same_color["status"] == "same_color_pair":
                continue
            unresolved_records.append(record)
            for assignment in cross_color_assignments(record, source_cache[prime]):
                cross_groups[(prime, int(assignment["q_a"]), int(assignment["q_s"]))].append(
                    assignment
                )
        if index % 10 == 0:
            print(f"processed primes {index}/{len(records_by_prime)}", file=sys.stderr)

    group_results = []
    for (prime, q_a, q_s), entries in sorted(cross_groups.items()):
        lo = min(int(entry["R"]) for entry in entries)
        hi = max(int(entry["R"]) for entry in entries)
        demand = sum(int(entry["required_a"]) * int(entry["required_s"]) for entry in entries)
        exact_capacity = 0
        state_count = 0
        for R, states in source_cache[prime].items():
            if not lo <= R <= hi:
                continue
            for a, s in states:
                exact_capacity += capacity.valuation(a * R + 1, q_a) * capacity.valuation(
                    s * R + 1, q_s
                )
                state_count += 1
        group_results.append(
            {
                "prime": prime,
                "q_a": q_a,
                "q_s": q_s,
                "record_count": len(entries),
                "R_min": lo,
                "R_max": hi,
                "demand": demand,
                "capacity": exact_capacity,
                "ratio": demand / exact_capacity if exact_capacity else None,
                "state_count": state_count,
            }
        )

    ratios = [float(group["ratio"]) for group in group_results if group["ratio"] is not None]
    overloads = [group for group in group_results if group["ratio"] is not None and group["ratio"] > 1]
    return {
        "arithmetic": "For every full-spectrum F state with at least two active primes but no deterministic same-color eligible pair, enumerate all admissible cross-color (a-block,s-block) direction pairs. Group by (p,q_a,q_s) and compare demand with the exact shared-R capacity sum v_{q_a}(aR+1)v_{q_s}(sR+1).",
        "scope_note": "Finite negative boundary only. The same-color exclusion and cross-color assignment are diagnostic choices; no overload does not prove the general two-color Fourier bridge or arithmetic descent.",
        "input_fourier": capacity.FOURIER_INPUT.name,
        "input_fourier_sha256": capacity.sha256(capacity.FOURIER_INPUT),
        "input_spectrum": capacity.SPECTRUM_INPUT.name,
        "input_spectrum_sha256": capacity.sha256(capacity.SPECTRUM_INPUT),
        "certificate_state_count": len(records),
        "active_record_count": len(all_active_records),
        "same_color_unresolved_record_count": len(unresolved_records),
        "cross_color_assignment_count": sum(len(entries) for entries in cross_groups.values()),
        "source_prime_count": len(source_cache),
        "cross_color_group_count": len(group_results),
        "cross_color_overload_count": len(overloads),
        "maximum_cross_color_ratio": max(ratios) if ratios else None,
        "cross_color_saturation_count": sum(ratio == 1 for ratio in ratios),
        "top_groups": sorted(
            group_results,
            key=lambda group: (group["ratio"] is not None, group["ratio"] or -1),
            reverse=True,
        )[:200],
        "overloads": overloads,
        "unresolved_records": [
            {
                "prime": int(record["prime"]),
                "R": int(record["R"]),
                "active_primes": [int(q) for q in record["active_primes"]],
            }
            for record in unresolved_records
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run()
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: payload[key]
                for key in (
                    "certificate_state_count",
                    "active_record_count",
                    "same_color_unresolved_record_count",
                    "cross_color_assignment_count",
                    "source_prime_count",
                    "cross_color_group_count",
                    "cross_color_overload_count",
                    "maximum_cross_color_ratio",
                    "cross_color_saturation_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
