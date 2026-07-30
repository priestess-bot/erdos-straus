#!/usr/bin/env python3
"""Audit repeated same-color Fourier-active pairs across the full F spectrum."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-full-same-color-pair-capacity-results.json"


def load_capacity_module():
    spec = importlib.util.spec_from_file_location("same_color_capacity", CAPACITY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {CAPACITY_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


capacity = load_capacity_module()


def run() -> dict[str, object]:
    records, _complete_states = capacity.load_inputs()
    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    pair_groups: dict[tuple[int, str, tuple[int, int]], list[dict[str, object]]] = defaultdict(list)
    assignments = []
    eligible_record_count = 0

    records_by_prime: dict[int, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        if len(record["active_primes"]) >= 2:
            records_by_prime[int(record["prime"])].append(record)

    for index, prime in enumerate(sorted(records_by_prime), start=1):
        _bound, source_cache[prime] = capacity.source.enumerate_linear_source_states(prime)
        for record in records_by_prime[prime]:
            assignment = capacity.choose_same_color_assignment(record, source_cache[prime])
            assignments.append(assignment)
            if assignment["status"] != "same_color_pair":
                continue
            eligible_record_count += 1
            active = tuple(int(q) for q in assignment["eligible_primes"])
            for pair in itertools.combinations(active, 2):
                pair_groups[(prime, str(assignment["label"]), pair)].append(assignment)
        if index % 10 == 0:
            print(f"processed primes {index}/{len(records_by_prime)}", file=sys.stderr)

    group_results = []
    for (prime, label, active), entries in sorted(pair_groups.items()):
        lo = min(int(entry["R"]) for entry in entries)
        hi = max(int(entry["R"]) for entry in entries)
        demand = sum(
            int(entry["required_heights"][str(active[0])])
            * int(entry["required_heights"][str(active[1])])
            for entry in entries
        )
        capacity_value, state_block_count = capacity.capacity_for_group(
            source_cache[prime], label, active, lo, hi
        )
        group_results.append(
            {
                "prime": prime,
                "label": label,
                "active_primes": list(active),
                "record_count": len(entries),
                "R_min": lo,
                "R_max": hi,
                "demand": demand,
                "capacity": capacity_value,
                "ratio": demand / capacity_value if capacity_value else None,
                "state_block_count": state_block_count,
            }
        )

    ratios = [float(group["ratio"]) for group in group_results if group["ratio"] is not None]
    overloads = [group for group in group_results if group["ratio"] is not None and group["ratio"] > 1]
    return {
        "arithmetic": "For every threshold-met bounded Fourier F state with at least two active primes, choose one deterministic same-color carrier subset and expand it to all same-color active pairs. Group repeated pairs by (p,label,pair), and compare the pair demand with exact linear-source block capacity over the induced R window.",
        "scope_note": "Finite full-spectrum negative boundary only. The source/color assignment is a canonical diagnostic; it is not a universal certificate-selection rule. No pair overload does not prove a selector or arithmetic descent.",
        "input_fourier": capacity.FOURIER_INPUT.name,
        "input_fourier_sha256": capacity.sha256(capacity.FOURIER_INPUT),
        "input_spectrum": capacity.SPECTRUM_INPUT.name,
        "input_spectrum_sha256": capacity.sha256(capacity.SPECTRUM_INPUT),
        "certificate_state_count": len(records),
        "active_pair_record_count": sum(1 for record in records if len(record["active_primes"]) >= 2),
        "same_color_pair_record_count": eligible_record_count,
        "unresolved_same_color_record_count": sum(
            assignment["status"] != "same_color_pair" for assignment in assignments
        ),
        "source_prime_count": len(source_cache),
        "pair_group_count": len(group_results),
        "pair_overload_count": len(overloads),
        "maximum_pair_ratio": max(ratios) if ratios else None,
        "pair_saturation_count": sum(ratio == 1 for ratio in ratios),
        "top_pair_groups": sorted(
            group_results,
            key=lambda group: (group["ratio"] is not None, group["ratio"] or -1),
            reverse=True,
        )[:200],
        "overloads": overloads,
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
                    "active_pair_record_count",
                    "same_color_pair_record_count",
                    "unresolved_same_color_record_count",
                    "source_prime_count",
                    "pair_group_count",
                    "pair_overload_count",
                    "maximum_pair_ratio",
                    "pair_saturation_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
