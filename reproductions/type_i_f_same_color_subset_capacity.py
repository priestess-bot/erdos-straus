#!/usr/bin/env python3
"""Audit same-color joint q-adic capacity for Fourier-active F states."""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
import itertools
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
SPECTRUM_INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-same-color-subset-capacity-results.json"
EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_SPECTRUM_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source():
    spec = importlib.util.spec_from_file_location("same_color_linear_source", SOURCE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


source = load_source()


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def load_inputs() -> tuple[list[dict[str, object]], dict[int, list[dict[str, int]]]]:
    if sha256(FOURIER_INPUT) != EXPECTED_FOURIER_SHA256:
        raise AssertionError("the frozen Fourier input changed")
    if sha256(SPECTRUM_INPUT) != EXPECTED_SPECTRUM_SHA256:
        raise AssertionError("the frozen full spectrum input changed")
    fourier = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    spectrum = json.loads(SPECTRUM_INPUT.read_text(encoding="utf-8"))
    records = [
        dict(record)
        for record in fourier["records"]
        if record["status"] == "bounded_fourier_certificate"
    ]
    states = {
        int(profile["prime"]): [
            {"R": int(record["R"]), "K": int(record["K"])}
            for record in profile["records"]
        ]
        for profile in spectrum["profiles"]
    }
    return records, states


def required_heights(record: dict[str, object]) -> dict[int, int]:
    factorization = {
        int(prime): int(exponent) for prime, exponent in record["factorization"]
    }
    return {
        int(prime): (factorization[int(prime)] + (2 if int(prime) == 2 else 0) + 1) // 2
        for prime in record["active_primes"]
    }


def naive_overload_groups(
    records: list[dict[str, object]],
    complete_states: dict[int, list[dict[str, int]]],
) -> list[dict[str, object]]:
    grouped: dict[tuple[int, tuple[int, ...]], list[dict[str, object]]] = defaultdict(list)
    for record in records:
        active = tuple(sorted(int(prime) for prime in record["active_primes"]))
        if len(active) >= 2:
            grouped[(int(record["prime"]), active)].append(record)

    candidates = []
    for (prime, active), entries in sorted(grouped.items()):
        demand = sum(
            math.prod(required_heights(entry)[q] for q in active) for entry in entries
        )
        capacity = 0
        for state in complete_states[prime]:
            product = 1
            for q in active:
                product *= valuation(int(state["K"]), q)
            capacity += product
        if demand > capacity:
            candidates.append(
                {
                    "prime": prime,
                    "active_primes": list(active),
                    "record_count": len(entries),
                    "naive_demand": demand,
                    "naive_capacity": capacity,
                    "naive_ratio": demand / capacity if capacity else None,
                    "records": entries,
                }
            )
    return candidates


def choose_same_color_assignment(
    record: dict[str, object],
    states_by_R: dict[int, list[tuple[int, int]]],
) -> dict[str, object]:
    prime = int(record["prime"])
    R = int(record["R"])
    active = tuple(sorted(int(q) for q in record["active_primes"]))
    required = required_heights(record)
    source_states = states_by_R.get(R)
    if not source_states:
        raise AssertionError(f"no source state for ({prime}, {R})")

    choices = []
    for a, s in source_states:
        blocks = (("a", a, a * R + 1), ("s", s, s * R + 1))
        for label, coordinate, block in blocks:
            heights = {q: valuation(block, q) for q in active}
            eligible = tuple(q for q in active if heights[q] >= required[q])
            if len(eligible) < 2:
                continue
            actual_product = math.prod(heights[q] for q in eligible)
            choices.append(
                {
                    "score": (-len(eligible), -actual_product, eligible, label, coordinate, a, s),
                    "label": label,
                    "coordinate": coordinate,
                    "block": block,
                    "a": a,
                    "s": s,
                    "eligible_primes": list(eligible),
                    "required_heights": {str(q): required[q] for q in eligible},
                    "actual_heights": {str(q): heights[q] for q in eligible},
                }
            )

    if not choices:
        return {
            "prime": prime,
            "R": R,
            "active_primes": list(active),
            "required_heights": {str(q): required[q] for q in active},
            "status": "no_same_color_pair",
        }

    selected = min(choices, key=lambda choice: choice["score"])
    selected = dict(selected)
    selected.pop("score")
    selected.update(
        {
            "prime": prime,
            "R": R,
            "active_primes": list(active),
            "status": "same_color_pair",
        }
    )
    return selected


def capacity_for_group(
    states_by_R: dict[int, list[tuple[int, int]]],
    label: str,
    active: tuple[int, ...],
    lo: int,
    hi: int,
) -> tuple[int, int]:
    capacity = 0
    state_blocks = 0
    for R, states in states_by_R.items():
        if not lo <= R <= hi:
            continue
        for a, s in states:
            block = a * R + 1 if label == "a" else s * R + 1
            capacity += math.prod(valuation(block, q) for q in active)
            state_blocks += 1
    return capacity, state_blocks


def run() -> dict[str, object]:
    records, complete_states = load_inputs()
    candidates = naive_overload_groups(records, complete_states)
    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    assignments = []
    groups: dict[tuple[int, str, tuple[int, ...]], list[dict[str, object]]] = defaultdict(list)

    for index, candidate in enumerate(candidates, start=1):
        prime = int(candidate["prime"])
        if prime not in source_cache:
            _bound, source_cache[prime] = source.enumerate_linear_source_states(prime)
        for record in candidate["records"]:
            assignment = choose_same_color_assignment(record, source_cache[prime])
            assignments.append(assignment)
            if assignment["status"] == "same_color_pair":
                key = (
                    prime,
                    str(assignment["label"]),
                    tuple(int(q) for q in assignment["eligible_primes"]),
                )
                groups[key].append(assignment)
        if index % 20 == 0:
            print(f"processed candidate groups {index}/{len(candidates)}", file=sys.stderr)

    group_results = []
    for (prime, label, active), entries in sorted(groups.items()):
        lo = min(int(entry["R"]) for entry in entries)
        hi = max(int(entry["R"]) for entry in entries)
        demand = sum(
            math.prod(
                int(entry["required_heights"][str(q)])
                for q in active
            )
            for entry in entries
        )
        capacity, state_block_count = capacity_for_group(
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
                "capacity": capacity,
                "ratio": demand / capacity if capacity else None,
                "state_block_count": state_block_count,
            }
        )

    pair_groups: dict[tuple[int, str, tuple[int, int]], list[dict[str, object]]] = defaultdict(list)
    for assignment in assignments:
        if assignment["status"] != "same_color_pair":
            continue
        eligible = tuple(int(q) for q in assignment["eligible_primes"])
        for pair in itertools.combinations(eligible, 2):
            pair_groups[
                (
                    int(assignment["prime"]),
                    str(assignment["label"]),
                    pair,
                )
            ].append(assignment)

    pair_group_results = []
    for (prime, label, active), entries in sorted(pair_groups.items()):
        lo = min(int(entry["R"]) for entry in entries)
        hi = max(int(entry["R"]) for entry in entries)
        demand = sum(
            math.prod(int(entry["required_heights"][str(q)]) for q in active)
            for entry in entries
        )
        capacity, state_block_count = capacity_for_group(
            source_cache[prime], label, active, lo, hi
        )
        pair_group_results.append(
            {
                "prime": prime,
                "label": label,
                "active_primes": list(active),
                "record_count": len(entries),
                "R_min": lo,
                "R_max": hi,
                "demand": demand,
                "capacity": capacity,
                "ratio": demand / capacity if capacity else None,
                "state_block_count": state_block_count,
            }
        )

    ratios = [float(group["ratio"]) for group in group_results if group["ratio"] is not None]
    overloads = [group for group in group_results if group["ratio"] is not None and group["ratio"] > 1]
    pair_ratios = [
        float(group["ratio"])
        for group in pair_group_results
        if group["ratio"] is not None
    ]
    pair_overloads = [
        group
        for group in pair_group_results
        if group["ratio"] is not None and group["ratio"] > 1
    ]
    unresolved = [assignment for assignment in assignments if assignment["status"] != "same_color_pair"]
    return {
        "arithmetic": "First identify full-spectrum Fourier active-prime product-capacity overloads. For each record choose one deterministic source state and one carrier label whose same-color eligible active set is maximal under the generous q-adic height demand; compare that demand with exact same-color block capacity across all linear source states in the induced R window.",
        "scope_note": "Finite negative boundary only. The source/color assignment is a canonical diagnostic, not a proof that every Fourier certificate must use this subset. No same-color capacity overload is not an arithmetic descent or a selector theorem.",
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "spectrum_input": SPECTRUM_INPUT.name,
        "spectrum_input_sha256": sha256(SPECTRUM_INPUT),
        "certificate_state_count": len(records),
        "naive_overload_group_count": len(candidates),
        "naive_overload_prime_count": len({int(candidate["prime"]) for candidate in candidates}),
        "same_color_assignment_count": len(assignments),
        "same_color_unresolved_count": len(unresolved),
        "same_color_group_count": len(group_results),
        "same_color_overload_count": len(overloads),
        "maximum_same_color_ratio": max(ratios) if ratios else None,
        "same_color_saturation_count": sum(ratio == 1 for ratio in ratios),
        "same_color_pair_group_count": len(pair_group_results),
        "same_color_pair_overload_count": len(pair_overloads),
        "maximum_same_color_pair_ratio": max(pair_ratios) if pair_ratios else None,
        "same_color_pair_saturation_count": sum(ratio == 1 for ratio in pair_ratios),
        "top_same_color_groups": sorted(
            group_results,
            key=lambda group: (group["ratio"] is not None, group["ratio"] or -1),
            reverse=True,
        )[:100],
        "top_same_color_pair_groups": sorted(
            pair_group_results,
            key=lambda group: (group["ratio"] is not None, group["ratio"] or -1),
            reverse=True,
        )[:100],
        "overloads": overloads,
        "pair_overloads": pair_overloads,
        "assignments": assignments,
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
                    "naive_overload_group_count",
                    "naive_overload_prime_count",
                    "same_color_assignment_count",
                    "same_color_unresolved_count",
                    "same_color_group_count",
                    "same_color_overload_count",
                    "maximum_same_color_ratio",
                    "same_color_saturation_count",
                    "same_color_pair_group_count",
                    "same_color_pair_overload_count",
                    "maximum_same_color_pair_ratio",
                    "same_color_pair_saturation_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
