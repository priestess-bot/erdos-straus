#!/usr/bin/env python3
"""Stress-test a conditional overflow-weighted two-color capacity demand."""

from __future__ import annotations

from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
CROSS_INPUT = ROOT / "reproductions" / "type-i-f-full-cross-color-pair-capacity-results.json"
OVERFLOW_INPUT = ROOT / "reproductions" / "type-i-f-split-color-overflow-radius-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-weighted-cross-capacity-results.json"
CAPACITY_SCRIPT = ROOT / "reproductions" / "type_i_f_same_color_subset_capacity.py"
CROSS_SCRIPT = ROOT / "reproductions" / "type_i_f_full_cross_color_pair_capacity.py"

EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_CROSS_SHA256 = "c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5"
EXPECTED_OVERFLOW_SHA256 = "9de8b20c36592af8a9abcb61de34c145978e533a876d909ebf832a193169aabf"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


capacity = load_module("overflow_capacity_base", CAPACITY_SCRIPT)
cross = load_module("overflow_cross_capacity", CROSS_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def group_capacity(
    entries: list[dict[str, object]],
    source_cache: dict[int, dict[int, list[tuple[int, int]]]],
) -> dict[str, object]:
    prime = int(entries[0]["prime"])
    q_a = int(entries[0]["q_a"])
    q_s = int(entries[0]["q_s"])
    lo = min(int(entry["R"]) for entry in entries)
    hi = max(int(entry["R"]) for entry in entries)
    base_demand = sum(
        int(entry["required_a"]) * int(entry["required_s"]) for entry in entries
    )
    unit_overflow_demand = sum(
        int(entry["required_a"]) * int(entry["required_s"]) + int(entry["radius_lower_bound"])
        for entry in entries
    )
    minimum_product_demand = sum(
        int(entry["required_a"]) * int(entry["required_s"])
        + int(entry["radius_lower_bound"])
        * min(int(entry["required_a"]), int(entry["required_s"]))
        for entry in entries
    )
    exact_capacity = 0
    state_count = 0
    for modulus, states in source_cache[prime].items():
        if not lo <= modulus <= hi:
            continue
        for a, s in states:
            exact_capacity += capacity.valuation(a * modulus + 1, q_a) * capacity.valuation(
                s * modulus + 1, q_s
            )
            state_count += 1
    return {
        "prime": prime,
        "q_a": q_a,
        "q_s": q_s,
        "record_count": len(entries),
        "R_min": lo,
        "R_max": hi,
        "base_demand": base_demand,
        "unit_overflow_demand": unit_overflow_demand,
        "minimum_product_demand": minimum_product_demand,
        "capacity": exact_capacity,
        "base_ratio": base_demand / exact_capacity if exact_capacity else None,
        "unit_overflow_ratio": unit_overflow_demand / exact_capacity if exact_capacity else None,
        "minimum_product_ratio": minimum_product_demand / exact_capacity if exact_capacity else None,
        "state_count": state_count,
    }


def summarize(groups: list[dict[str, object]], field: str) -> dict[str, object]:
    ratios = [float(group[field]) for group in groups if group[field] is not None]
    overloads = [group for group in groups if group[field] is not None and group[field] > 1]
    return {
        "group_count": len(groups),
        "overload_count": len(overloads),
        "maximum_ratio": max(ratios) if ratios else None,
        "saturation_count": sum(ratio == 1 for ratio in ratios),
        "top_groups": sorted(
            groups,
            key=lambda group: (group[field] is not None, group[field] or -1),
            reverse=True,
        )[:50],
    }


def run() -> dict[str, object]:
    for path, expected, label in (
        (FOURIER_INPUT, EXPECTED_FOURIER_SHA256, "Fourier"),
        (CROSS_INPUT, EXPECTED_CROSS_SHA256, "cross-color"),
        (OVERFLOW_INPUT, EXPECTED_OVERFLOW_SHA256, "overflow"),
    ):
        if sha256(path) != expected:
            raise AssertionError(f"the {label} input changed")

    fourier_payload = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    cross_payload = json.loads(CROSS_INPUT.read_text(encoding="utf-8"))
    overflow_payload = json.loads(OVERFLOW_INPUT.read_text(encoding="utf-8"))
    fourier_by_key = {
        (int(record["prime"]), int(record["R"])): dict(record)
        for record in fourier_payload["records"]
    }
    overflow_by_key = {
        (int(record["prime"]), int(record["R"])): dict(record)
        for record in overflow_payload["records"]
    }

    unresolved = [
        dict(record)
        for record in cross_payload["unresolved_records"]
    ]
    if len(unresolved) != int(cross_payload["same_color_unresolved_record_count"]):
        raise AssertionError("cross-color unresolved record count changed")

    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    grouped: dict[tuple[int, int, int], list[dict[str, object]]] = defaultdict(list)
    assignment_count = 0
    for index, record in enumerate(unresolved, start=1):
        key = (int(record["prime"]), int(record["R"]))
        if key not in fourier_by_key or key not in overflow_by_key:
            raise AssertionError("cross-color record lacks Fourier or overflow input")
        Fourier = fourier_by_key[key]
        if Fourier["status"] != "bounded_fourier_certificate":
            raise AssertionError("cross-color unresolved record is not threshold-met")
        if key[0] not in source_cache:
            _bound, source_cache[key[0]] = capacity.source.enumerate_linear_source_states(key[0])
        assignments = cross.cross_color_assignments(Fourier, source_cache[key[0]])
        radius = int(overflow_by_key[key]["capped_radius"])
        for assignment in assignments:
            row = {
                **assignment,
                "radius_lower_bound": radius,
                "character_order": int(Fourier["character_order"]),
            }
            grouped[(key[0], int(row["q_a"]), int(row["q_s"]))].append(row)
            assignment_count += 1
        if index % 50 == 0:
            print(f"processed {index}/{len(unresolved)}", file=sys.stderr)

    groups = [
        group_capacity(entries, source_cache)
        for _key, entries in sorted(grouped.items())
    ]
    return {
        "arithmetic": (
            "For the 291 split-color F states, use the exact capped affine-box overflow radius "
            "as a conditional extra demand. The minimum-product model assumes that an overflow "
            "of delta forces at least delta extra layers on one of the two carrier directions, "
            "so (h_a+x)(h_s+y) >= h_a h_s + delta min(h_a,h_s) when max(x,y)>=delta."
        ),
        "scope_note": (
            "Conditional stress test only. The missing theorem is the arithmetic implication from "
            "relation-lattice overflow to q-adic carrier-height consumption. Neither weighted "
            "overload nor its absence is a selector theorem. Radius 5 means only delta>=5 because "
            "the upstream overflow audit is capped at 4."
        ),
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "cross_input": CROSS_INPUT.name,
        "cross_input_sha256": sha256(CROSS_INPUT),
        "overflow_input": OVERFLOW_INPUT.name,
        "overflow_input_sha256": sha256(OVERFLOW_INPUT),
        "unresolved_record_count": len(unresolved),
        "assignment_count": assignment_count,
        "group_count": len(groups),
        "radius_distribution": dict(
            sorted(
                {
                    str(radius): sum(
                        1 for record in overflow_payload["records"] if int(record["capped_radius"]) == radius
                    )
                    for radius in {int(record["capped_radius"]) for record in overflow_payload["records"]}
                }.items(),
                key=lambda item: int(item[0]),
            )
        ),
        "base_capacity": summarize(groups, "base_ratio"),
        "unit_overflow_capacity": summarize(groups, "unit_overflow_ratio"),
        "minimum_product_overflow_capacity": summarize(groups, "minimum_product_ratio"),
        "groups": groups,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "unresolved_record_count",
                    "assignment_count",
                    "group_count",
                    "radius_distribution",
                    "base_capacity",
                    "unit_overflow_capacity",
                    "minimum_product_overflow_capacity",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
