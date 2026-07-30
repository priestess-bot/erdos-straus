#!/usr/bin/env python3
"""Audit a choice-independent q-adic capacity for universal overflow gaps."""

from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-all-assignment-height-upper-bound-results.json"
CAPACITY_SCRIPT = ROOT / "reproductions" / "type_i_f_same_color_subset_capacity.py"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-cross-state-qadic-capacity-results.json"

EXPECTED_INPUT_SHA256 = "62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5"


def load_capacity_module():
    spec = importlib.util.spec_from_file_location("cross_state_overflow_capacity", CAPACITY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {CAPACITY_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


capacity = load_capacity_module()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def height(value: int, prime: int) -> int:
    return capacity.valuation(value, prime)


def summarize(groups: list[dict[str, object]], field: str) -> dict[str, object]:
    ratios = [float(row[field]) for row in groups if row[field] is not None]
    overloads = [row for row in groups if row[field] is not None and row[field] > 1]
    return {
        "group_count": len(groups),
        "overload_count": len(overloads),
        "maximum_ratio": max(ratios) if ratios else None,
        "saturation_count": sum(ratio == 1 for ratio in ratios),
        "top_groups": sorted(
            groups,
            key=lambda row: (row[field] is not None, row[field] or -1),
            reverse=True,
        )[:50],
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen all-assignment input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records = [
        dict(record)
        for record in payload["records"]
        if record["category"] == "no_assignment_can_carry_all_excess"
    ]

    grouped: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for record in records:
        prime = int(record["prime"])
        modulus = int(record["R"])
        for q_text, excess_value in record["universally_unsupported_excess"].items():
            q = int(q_text)
            excess = int(excess_value)
            maximum_height = int(record["max_height_by_q"][q_text])
            if maximum_height >= excess:
                raise AssertionError("universal overflow row has no positive deficit")
            grouped[(prime, q)].append(
                {
                    "R": modulus,
                    "excess": excess,
                    "maximum_height": maximum_height,
                    "deficit": excess - maximum_height,
                }
            )

    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    groups: list[dict[str, object]] = []
    for (prime, q), entries in sorted(grouped.items()):
        low = min(entry["R"] for entry in entries)
        high = max(entry["R"] for entry in entries)
        excess_demand = sum(entry["excess"] for entry in entries)
        deficit_demand = sum(entry["deficit"] for entry in entries)
        unit_demand = len(entries)

        if prime not in source_cache:
            _bound, source_cache[prime] = capacity.source.enumerate_linear_source_states(prime)

        # Use the best block in each ordered source state. This is deliberately generous:
        # it ignores color conflicts and counts both orientations when the source table has them.
        layer_capacity = 0
        positive_state_capacity = 0
        source_state_count = 0
        distinct_modulus_layer_capacity = 0
        distinct_modulus_positive_capacity = 0
        for modulus, states in source_cache[prime].items():
            if not low <= modulus <= high:
                continue
            best_at_modulus = 0
            for a, s in states:
                best = max(
                    height(a * modulus + 1, q),
                    height(s * modulus + 1, q),
                )
                layer_capacity += best
                positive_state_capacity += int(best > 0)
                source_state_count += 1
                best_at_modulus = max(best_at_modulus, best)
            distinct_modulus_layer_capacity += best_at_modulus
            distinct_modulus_positive_capacity += int(best_at_modulus > 0)

        groups.append(
            {
                "prime": prime,
                "q": q,
                "record_count": len(entries),
                "R_min": low,
                "R_max": high,
                "excess_demand": excess_demand,
                "deficit_demand": deficit_demand,
                "unit_demand": unit_demand,
                "ordered_source_state_count": source_state_count,
                "ordered_layer_capacity": layer_capacity,
                "ordered_positive_state_capacity": positive_state_capacity,
                "distinct_modulus_layer_capacity": distinct_modulus_layer_capacity,
                "distinct_modulus_positive_capacity": distinct_modulus_positive_capacity,
                "excess_ordered_ratio": (
                    excess_demand / layer_capacity if layer_capacity else None
                ),
                "deficit_ordered_ratio": (
                    deficit_demand / layer_capacity if layer_capacity else None
                ),
                "unit_ordered_ratio": (
                    unit_demand / positive_state_capacity
                    if positive_state_capacity
                    else None
                ),
                "excess_distinct_modulus_ratio": (
                    excess_demand / distinct_modulus_layer_capacity
                    if distinct_modulus_layer_capacity
                    else None
                ),
                "deficit_distinct_modulus_ratio": (
                    deficit_demand / distinct_modulus_layer_capacity
                    if distinct_modulus_layer_capacity
                    else None
                ),
                "unit_distinct_modulus_ratio": (
                    unit_demand / distinct_modulus_positive_capacity
                    if distinct_modulus_positive_capacity
                    else None
                ),
                "entries": entries,
            }
        )

    aggregate = {
        "excess_demand": sum(int(group["excess_demand"]) for group in groups),
        "deficit_demand": sum(int(group["deficit_demand"]) for group in groups),
        "unit_demand": sum(int(group["unit_demand"]) for group in groups),
        "ordered_layer_capacity": sum(
            int(group["ordered_layer_capacity"]) for group in groups
        ),
        "ordered_positive_state_capacity": sum(
            int(group["ordered_positive_state_capacity"]) for group in groups
        ),
        "distinct_modulus_layer_capacity": sum(
            int(group["distinct_modulus_layer_capacity"]) for group in groups
        ),
        "distinct_modulus_positive_capacity": sum(
            int(group["distinct_modulus_positive_capacity"]) for group in groups
        ),
    }

    return {
        "arithmetic": (
            "Group every universally unsupported overflow coordinate by (core prime, q). "
            "Demand is recorded as total overflow layers, the positive deficit after the "
            "best admissible assignment, and one unit per state. Capacity is the sum of the "
            "larger q-adic height of the two blocks over every complete linear source state "
            "in the group's R interval."
        ),
        "scope_note": (
            "Finite conditional capacity audit only. The source-state height sum is an "
            "optimistic upper bound: it ignores color conflicts, lets each demand use the "
            "best block independently, and counts ordered source states. A ratio above one "
            "would still require a theorem mapping relation-lattice overflow to q-height "
            "consumption; a ratio below one only rules out this scalar q-only ledger."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "all_assignment_state_count": int(payload["state_count"]),
        "universal_gap_state_count": len(records),
        "universal_gap_coordinate_count": sum(
            len(record["universally_unsupported_excess"]) for record in records
        ),
        "group_count": len(groups),
        "group_prime_count": len({int(group["prime"]) for group in groups}),
        "aggregate": aggregate,
        "ordered_layer_capacity": summarize(groups, "excess_ordered_ratio"),
        "ordered_deficit_capacity": summarize(groups, "deficit_ordered_ratio"),
        "ordered_unit_capacity": summarize(groups, "unit_ordered_ratio"),
        "distinct_modulus_layer_capacity": summarize(
            groups, "excess_distinct_modulus_ratio"
        ),
        "distinct_modulus_deficit_capacity": summarize(
            groups, "deficit_distinct_modulus_ratio"
        ),
        "distinct_modulus_unit_capacity": summarize(
            groups, "unit_distinct_modulus_ratio"
        ),
        "groups": groups,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    compact = {
        key: result[key]
        for key in (
            "all_assignment_state_count",
            "universal_gap_state_count",
            "universal_gap_coordinate_count",
            "group_count",
            "group_prime_count",
            "aggregate",
        )
    }
    for key in (
        "ordered_layer_capacity",
        "ordered_deficit_capacity",
        "ordered_unit_capacity",
        "distinct_modulus_layer_capacity",
        "distinct_modulus_deficit_capacity",
        "distinct_modulus_unit_capacity",
    ):
        summary = result[key]
        compact[key] = {
            field: summary[field]
            for field in ("group_count", "overload_count", "maximum_ratio", "saturation_count")
        }
    print(json.dumps(compact, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
