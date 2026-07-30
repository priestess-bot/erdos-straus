#!/usr/bin/env python3
"""Audit joint multi-coordinate capacity for universal overflow gaps."""

from __future__ import annotations

from collections import defaultdict
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-all-assignment-height-upper-bound-results.json"
CAPACITY_SCRIPT = ROOT / "reproductions" / "type_i_f_same_color_subset_capacity.py"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-universal-joint-capacity-results.json"

EXPECTED_INPUT_SHA256 = "62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5"


def load_capacity_module():
    spec = importlib.util.spec_from_file_location("universal_joint_capacity", CAPACITY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {CAPACITY_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


capacity = load_capacity_module()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def product(values: list[int]) -> int:
    return math.prod(values) if values else 0


def summarize(groups: list[dict[str, object]], field: str) -> dict[str, object]:
    ratios = [float(row[field]) for row in groups if row[field] is not None]
    return {
        "group_count": len(groups),
        "overload_count": sum(ratio > 1 for ratio in ratios),
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
    if not records:
        raise AssertionError("no universal overflow records")

    grouped: dict[tuple[int, tuple[int, ...]], list[dict[str, object]]] = defaultdict(list)
    for record in records:
        excess = {
            int(q): int(value)
            for q, value in record["universally_unsupported_excess"].items()
            if int(value) > 0
        }
        if not excess:
            raise AssertionError("universal overflow record has no positive excess")
        support = tuple(sorted(excess))
        grouped[(int(record["prime"]), support)].append(
            {
                "R": int(record["R"]),
                "excess": {str(q): value for q, value in sorted(excess.items())},
                "joint_demand": product(list(excess.values())),
                "coordinate_demand": sum(excess.values()),
            }
        )

    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    groups: list[dict[str, object]] = []
    for index, ((prime, support), entries) in enumerate(sorted(grouped.items()), start=1):
        if prime not in source_cache:
            _bound, source_cache[prime] = capacity.source.enumerate_linear_source_states(prime)
        low = min(int(entry["R"]) for entry in entries)
        high = max(int(entry["R"]) for entry in entries)

        joint_demand = sum(int(entry["joint_demand"]) for entry in entries)
        coordinate_demand = sum(int(entry["coordinate_demand"]) for entry in entries)
        unit_demand = len(entries)
        independent_color_capacity = 0
        same_block_capacity = 0
        source_state_count = 0
        distinct_modulus_independent_capacity = 0
        distinct_modulus_same_capacity = 0

        for modulus, states in source_cache[prime].items():
            if not low <= modulus <= high:
                continue
            best_independent_at_modulus = 0
            best_same_at_modulus = 0
            for a, s in states:
                heights_a = [capacity.valuation(a * modulus + 1, q) for q in support]
                heights_s = [capacity.valuation(s * modulus + 1, q) for q in support]

                # This is deliberately more generous than a genuine one-block carrier:
                # each coordinate may choose its better block independently.
                independent = product([
                    max(heights_a[index], heights_s[index])
                    for index in range(len(support))
                ])
                same = max(product(heights_a), product(heights_s))
                independent_color_capacity += independent
                same_block_capacity += same
                source_state_count += 1
                best_independent_at_modulus = max(best_independent_at_modulus, independent)
                best_same_at_modulus = max(best_same_at_modulus, same)
            distinct_modulus_independent_capacity += best_independent_at_modulus
            distinct_modulus_same_capacity += best_same_at_modulus

        groups.append(
            {
                "prime": prime,
                "support": list(support),
                "record_count": len(entries),
                "R_min": low,
                "R_max": high,
                "joint_demand": joint_demand,
                "coordinate_demand": coordinate_demand,
                "unit_demand": unit_demand,
                "ordered_source_state_count": source_state_count,
                "independent_color_capacity": independent_color_capacity,
                "same_block_capacity": same_block_capacity,
                "distinct_modulus_independent_capacity": distinct_modulus_independent_capacity,
                "distinct_modulus_same_capacity": distinct_modulus_same_capacity,
                "joint_independent_ratio": (
                    joint_demand / independent_color_capacity
                    if independent_color_capacity
                    else None
                ),
                "joint_same_block_ratio": (
                    joint_demand / same_block_capacity if same_block_capacity else None
                ),
                "joint_distinct_modulus_ratio": (
                    joint_demand / distinct_modulus_independent_capacity
                    if distinct_modulus_independent_capacity
                    else None
                ),
                "coordinate_independent_ratio": (
                    coordinate_demand / independent_color_capacity
                    if independent_color_capacity
                    else None
                ),
                "entries": entries,
            }
        )
        if index % 25 == 0:
            print(f"processed {index}/{len(grouped)}", file=sys.stderr)

    multi_groups = [group for group in groups if len(group["support"]) >= 2]
    multi_records = sum(int(group["record_count"]) for group in multi_groups)
    multi_aggregate = {
        "joint_demand": sum(int(group["joint_demand"]) for group in multi_groups),
        "coordinate_demand": sum(int(group["coordinate_demand"]) for group in multi_groups),
        "unit_demand": sum(int(group["unit_demand"]) for group in multi_groups),
        "independent_color_capacity": sum(
            int(group["independent_color_capacity"]) for group in multi_groups
        ),
        "same_block_capacity": sum(int(group["same_block_capacity"]) for group in multi_groups),
        "distinct_modulus_independent_capacity": sum(
            int(group["distinct_modulus_independent_capacity"]) for group in multi_groups
        ),
        "distinct_modulus_same_capacity": sum(
            int(group["distinct_modulus_same_capacity"]) for group in multi_groups
        ),
    }
    aggregate = {
        "joint_demand": sum(int(group["joint_demand"]) for group in groups),
        "coordinate_demand": sum(int(group["coordinate_demand"]) for group in groups),
        "unit_demand": sum(int(group["unit_demand"]) for group in groups),
        "independent_color_capacity": sum(
            int(group["independent_color_capacity"]) for group in groups
        ),
        "same_block_capacity": sum(int(group["same_block_capacity"]) for group in groups),
        "distinct_modulus_independent_capacity": sum(
            int(group["distinct_modulus_independent_capacity"]) for group in groups
        ),
        "distinct_modulus_same_capacity": sum(
            int(group["distinct_modulus_same_capacity"]) for group in groups
        ),
    }
    result = {
        "arithmetic": (
            "For each universal overflow state, treat the excess vector e_q as a joint layer "
            "demand product prod_q e_q. Capacity is computed over complete linear source states "
            "in the common R window. The independent-color capacity may choose the better of "
            "the two source blocks separately for every coordinate, so it is an optimistic upper "
            "bound on any single-carrier joint capacity."
        ),
        "scope_note": (
            "Finite conditional pressure boundary only. The product demand is justified only if a "
            "multi-coordinate overflow must consume simultaneous joint height layers; the current "
            "relation-lattice data do not prove that mapping. A ratio above one therefore identifies "
            "a candidate cross-state obstruction, not a selector theorem. A ratio below one only "
            "rules out this particular joint ledger."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "all_assignment_state_count": int(payload["state_count"]),
        "universal_gap_state_count": len(records),
        "single_coordinate_universal_gap_state_count": sum(
            int(group["record_count"]) for group in groups if len(group["support"]) == 1
        ),
        "multi_coordinate_universal_gap_state_count": multi_records,
        "group_count": len(groups),
        "multi_coordinate_group_count": len(multi_groups),
        "group_prime_count": len({int(group["prime"]) for group in groups}),
        "support_size_histogram": {
            str(size): sum(len(group["support"]) == size for group in groups)
            for size in sorted({len(group["support"]) for group in groups})
        },
        "aggregate": aggregate,
        "multi_coordinate_aggregate": multi_aggregate,
        "joint_independent_capacity": summarize(groups, "joint_independent_ratio"),
        "joint_same_block_capacity": summarize(groups, "joint_same_block_ratio"),
        "joint_distinct_modulus_capacity": summarize(groups, "joint_distinct_modulus_ratio"),
        "coordinate_independent_capacity": summarize(groups, "coordinate_independent_ratio"),
        "multi_coordinate_joint_independent_capacity": summarize(
            multi_groups, "joint_independent_ratio"
        ),
        "multi_coordinate_joint_same_block_capacity": summarize(
            multi_groups, "joint_same_block_ratio"
        ),
        "multi_coordinate_joint_distinct_modulus_capacity": summarize(
            multi_groups, "joint_distinct_modulus_ratio"
        ),
        "groups": groups,
    }
    return result


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    compact = {
        key: result[key]
        for key in (
            "all_assignment_state_count",
            "universal_gap_state_count",
            "single_coordinate_universal_gap_state_count",
            "multi_coordinate_universal_gap_state_count",
            "group_count",
            "multi_coordinate_group_count",
            "group_prime_count",
            "support_size_histogram",
            "aggregate",
            "multi_coordinate_aggregate",
        )
    }
    for key in (
        "joint_independent_capacity",
        "joint_same_block_capacity",
        "joint_distinct_modulus_capacity",
        "coordinate_independent_capacity",
        "multi_coordinate_joint_independent_capacity",
        "multi_coordinate_joint_same_block_capacity",
        "multi_coordinate_joint_distinct_modulus_capacity",
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
