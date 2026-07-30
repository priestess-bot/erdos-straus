#!/usr/bin/env python3
"""Audit block, modulus-difference, and label-difference q-adic channels."""

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
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-three-channel-capacity-results.json"

EXPECTED_INPUT_SHA256 = "62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5"


def load_capacity_module():
    spec = importlib.util.spec_from_file_location("three_channel_capacity", CAPACITY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {CAPACITY_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


capacity = load_capacity_module()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation_difference(left: int, right: int, prime: int) -> int:
    difference = abs(left - right)
    if difference == 0:
        return 0
    return capacity.valuation(difference, prime)


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
    grouped: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    support_grouped: dict[tuple[int, tuple[int, ...]], list[dict[str, object]]] = defaultdict(list)
    for record in records:
        excess = {
            int(q): int(value)
            for q, value in record["universally_unsupported_excess"].items()
            if int(value) > 0
        }
        for q, amount in excess.items():
            grouped[(int(record["prime"]), q)].append(
                {"R": int(record["R"]), "demand": amount}
            )
        support = tuple(sorted(excess))
        support_grouped[(int(record["prime"]), support)].append(
            {
                "R": int(record["R"]),
                "excess": {str(q): amount for q, amount in sorted(excess.items())},
                "joint_demand": math.prod(excess.values()),
            }
        )

    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    channel_cache: dict[int, dict[str, object]] = {}
    groups: list[dict[str, object]] = []
    for index, ((prime, q), entries) in enumerate(sorted(grouped.items()), start=1):
        if prime not in source_cache:
            _bound, source_cache[prime] = capacity.source.enumerate_linear_source_states(prime)
            all_moduli = sorted(source_cache[prime])
            all_labels = sorted(
                {
                    label
                    for states in source_cache[prime].values()
                    for a, s in states
                    for label in (a, s)
                }
            )
            channel_cache[prime] = {"moduli": all_moduli, "labels": all_labels}
        low = min(int(entry["R"]) for entry in entries)
        high = max(int(entry["R"]) for entry in entries)
        block_capacity = 0
        modulus_difference_capacity = 0
        label_difference_capacity = 0
        independent_sum_capacity = 0
        independent_max_capacity = 0
        source_state_count = 0
        for modulus, states in source_cache[prime].items():
            if not low <= modulus <= high:
                continue
            modulus_height = max(
                (
                    valuation_difference(modulus // 4, other // 4, q)
                    for other in channel_cache[prime]["moduli"]
                    if other != modulus
                ),
                default=0,
            )
            for a, s in states:
                block_height = max(
                    capacity.valuation(a * modulus + 1, q),
                    capacity.valuation(s * modulus + 1, q),
                )
                label_height = max(
                    (
                        valuation_difference(label, other, q)
                        for label in (a, s)
                        for other in channel_cache[prime]["labels"]
                        if other != label
                    ),
                    default=0,
                )
                block_capacity += block_height
                modulus_difference_capacity += modulus_height
                label_difference_capacity += label_height
                independent_sum_capacity += block_height + modulus_height + label_height
                independent_max_capacity += max(block_height, modulus_height, label_height)
                source_state_count += 1

        demand = sum(int(entry["demand"]) for entry in entries)
        groups.append(
            {
                "prime": prime,
                "q": q,
                "record_count": len(entries),
                "R_min": low,
                "R_max": high,
                "demand": demand,
                "ordered_source_state_count": source_state_count,
                "block_capacity": block_capacity,
                "modulus_difference_capacity": modulus_difference_capacity,
                "label_difference_capacity": label_difference_capacity,
                "independent_sum_capacity": independent_sum_capacity,
                "independent_max_capacity": independent_max_capacity,
                "block_ratio": demand / block_capacity if block_capacity else None,
                "modulus_difference_ratio": (
                    demand / modulus_difference_capacity
                    if modulus_difference_capacity
                    else None
                ),
                "label_difference_ratio": (
                    demand / label_difference_capacity if label_difference_capacity else None
                ),
                "independent_sum_ratio": (
                    demand / independent_sum_capacity if independent_sum_capacity else None
                ),
                "independent_max_ratio": (
                    demand / independent_max_capacity if independent_max_capacity else None
                ),
                "entries": entries,
            }
        )
        if index % 50 == 0:
            print(f"processed scalar groups {index}/{len(grouped)}", file=sys.stderr)

    joint_groups: list[dict[str, object]] = []
    for (prime, support), entries in sorted(support_grouped.items()):
        low = min(int(entry["R"]) for entry in entries)
        high = max(int(entry["R"]) for entry in entries)
        if prime not in source_cache:
            _bound, source_cache[prime] = capacity.source.enumerate_linear_source_states(prime)
            all_moduli = sorted(source_cache[prime])
            all_labels = sorted(
                {
                    label
                    for states in source_cache[prime].values()
                    for a, s in states
                    for label in (a, s)
                }
            )
            channel_cache[prime] = {"moduli": all_moduli, "labels": all_labels}
        joint_capacity = 0
        joint_max_capacity = 0
        source_state_count = 0
        for modulus, states in source_cache[prime].items():
            if not low <= modulus <= high:
                continue
            for a, s in states:
                heights = []
                max_heights = []
                for q in support:
                    block_height = max(
                        capacity.valuation(a * modulus + 1, q),
                        capacity.valuation(s * modulus + 1, q),
                    )
                    modulus_height = max(
                        (
                            valuation_difference(modulus // 4, other // 4, q)
                            for other in channel_cache[prime]["moduli"]
                            if other != modulus
                        ),
                        default=0,
                    )
                    label_height = max(
                        (
                            valuation_difference(label, other, q)
                            for label in (a, s)
                            for other in channel_cache[prime]["labels"]
                            if other != label
                        ),
                        default=0,
                    )
                    heights.append(block_height + modulus_height + label_height)
                    max_heights.append(max(block_height, modulus_height, label_height))
                joint_capacity += math.prod(heights)
                joint_max_capacity += math.prod(max_heights)
                source_state_count += 1
        demand = sum(int(entry["joint_demand"]) for entry in entries)
        joint_groups.append(
            {
                "prime": prime,
                "support": list(support),
                "record_count": len(entries),
                "R_min": low,
                "R_max": high,
                "joint_demand": demand,
                "ordered_source_state_count": source_state_count,
                "independent_sum_joint_capacity": joint_capacity,
                "independent_max_joint_capacity": joint_max_capacity,
                "independent_sum_joint_ratio": (
                    demand / joint_capacity if joint_capacity else None
                ),
                "independent_max_joint_ratio": (
                    demand / joint_max_capacity if joint_max_capacity else None
                ),
                "entries": entries,
            }
        )

    aggregate = {
        "demand": sum(int(group["demand"]) for group in groups),
        "block_capacity": sum(int(group["block_capacity"]) for group in groups),
        "modulus_difference_capacity": sum(
            int(group["modulus_difference_capacity"]) for group in groups
        ),
        "label_difference_capacity": sum(int(group["label_difference_capacity"]) for group in groups),
        "independent_sum_capacity": sum(int(group["independent_sum_capacity"]) for group in groups),
        "independent_max_capacity": sum(int(group["independent_max_capacity"]) for group in groups),
    }
    joint_aggregate = {
        "joint_demand": sum(int(group["joint_demand"]) for group in joint_groups),
        "independent_sum_joint_capacity": sum(
            int(group["independent_sum_joint_capacity"]) for group in joint_groups
        ),
        "independent_max_joint_capacity": sum(
            int(group["independent_max_joint_capacity"]) for group in joint_groups
        ),
    }
    return {
        "arithmetic": (
            "For every universal overflow coordinate, allow three independent optimistic channels: "
            "the best current source-block height, the largest q-adic height of a complete-source "
            "modulus difference, and the largest q-adic height of a complete-source label difference. "
            "Also report a joint-support product version."
        ),
        "scope_note": (
            "Finite conditional pressure audit only. The three channels are deliberately additive and "
            "may double-count the same arithmetic resource; no claim is made that a relation-lattice "
            "overflow consumes any of them. A ratio above one remains a candidate obstruction, while "
            "a ratio below one only rules out this generous ledger."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "all_assignment_state_count": int(payload["state_count"]),
        "universal_gap_state_count": len(records),
        "scalar_group_count": len(groups),
        "joint_group_count": len(joint_groups),
        "aggregate": aggregate,
        "joint_aggregate": joint_aggregate,
        "block_capacity": summarize(groups, "block_ratio"),
        "modulus_difference_capacity": summarize(groups, "modulus_difference_ratio"),
        "label_difference_capacity": summarize(groups, "label_difference_ratio"),
        "independent_sum_capacity": summarize(groups, "independent_sum_ratio"),
        "independent_max_capacity": summarize(groups, "independent_max_ratio"),
        "joint_independent_sum_capacity": summarize(
            joint_groups, "independent_sum_joint_ratio"
        ),
        "joint_independent_max_capacity": summarize(
            joint_groups, "independent_max_joint_ratio"
        ),
        "groups": groups,
        "joint_groups": joint_groups,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    compact = {
        "all_assignment_state_count": result["all_assignment_state_count"],
        "universal_gap_state_count": result["universal_gap_state_count"],
        "scalar_group_count": result["scalar_group_count"],
        "joint_group_count": result["joint_group_count"],
        "aggregate": result["aggregate"],
        "joint_aggregate": result["joint_aggregate"],
    }
    for key in (
        "block_capacity",
        "modulus_difference_capacity",
        "label_difference_capacity",
        "independent_sum_capacity",
        "independent_max_capacity",
        "joint_independent_sum_capacity",
        "joint_independent_max_capacity",
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
