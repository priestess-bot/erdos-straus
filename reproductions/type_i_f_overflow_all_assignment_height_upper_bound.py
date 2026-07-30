#!/usr/bin/env python3
"""Find overflow layers that no admissible source assignment can carry."""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
CROSS_INPUT = ROOT / "reproductions" / "type-i-f-full-cross-color-pair-capacity-results.json"
SUPPORT_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
SQUARE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"
CAPACITY_SCRIPT = ROOT / "reproductions" / "type_i_f_same_color_subset_capacity.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-all-assignment-height-upper-bound-results.json"

EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_CROSS_SHA256 = "c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5"
EXPECTED_SUPPORT_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"
EXPECTED_SQUARE_SHA256 = "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1"
EXPECTED_STATE_COUNT = 253


def load_capacity_module():
    spec = importlib.util.spec_from_file_location("all_assignment_capacity", CAPACITY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {CAPACITY_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


capacity = load_capacity_module()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inputs() -> tuple[dict[tuple[int, int], dict[str, object]], dict[tuple[int, int], dict[str, object]], dict[tuple[int, int], dict[str, object]]]:
    expected = (
        (FOURIER_INPUT, EXPECTED_FOURIER_SHA256, "Fourier"),
        (CROSS_INPUT, EXPECTED_CROSS_SHA256, "cross-color"),
        (SUPPORT_INPUT, EXPECTED_SUPPORT_SHA256, "support"),
        (SQUARE_INPUT, EXPECTED_SQUARE_SHA256, "square-terminal"),
    )
    for path, digest, label in expected:
        if sha256(path) != digest:
            raise AssertionError(f"the frozen {label} input changed")
    fourier = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    cross = json.loads(CROSS_INPUT.read_text(encoding="utf-8"))
    support = json.loads(SUPPORT_INPUT.read_text(encoding="utf-8"))
    square = json.loads(SQUARE_INPUT.read_text(encoding="utf-8"))
    fourier_by_key = {
        (int(row["prime"]), int(row["R"])): dict(row)
        for row in fourier["records"]
    }
    cross_by_key = {
        (int(row["prime"]), int(row["R"])): dict(row)
        for row in cross["unresolved_records"]
    }
    support_by_key = {
        (int(row["prime"]), int(row["R"])): dict(row)
        for row in support["records"]
        if row.get("within_radius_cap")
    }
    square_keys = {
        (int(row["prime"]), int(row["R"])) for row in square["candidates"]
    }
    if len(square_keys) != EXPECTED_STATE_COUNT:
        raise AssertionError("the square-terminal key set changed")
    if not square_keys <= set(fourier_by_key) & set(cross_by_key) & set(support_by_key):
        raise AssertionError("square-terminal keys are not covered by all frozen inputs")
    return (
        {key: fourier_by_key[key] for key in square_keys},
        {key: cross_by_key[key] for key in square_keys},
        {key: support_by_key[key] for key in square_keys},
    )


def admissible_assignments(
    record: dict[str, object], states_by_R: dict[int, list[tuple[int, int]]]
) -> list[tuple[int, int, tuple[int, ...]]]:
    R = int(record["R"])
    active = tuple(sorted(int(value) for value in record["active_primes"]))
    if len(active) < 2:
        raise AssertionError("height-capacity audit requires at least two active directions")
    required = capacity.required_heights(record)
    assignments = []
    for a, s in states_by_R[R]:
        blocks = (a * R + 1, s * R + 1)
        for q_a, q_s in itertools.permutations(active, 2):
            if capacity.valuation(blocks[0], q_a) < required[q_a]:
                continue
            if capacity.valuation(blocks[1], q_s) < required[q_s]:
                continue
            assignments.append((a, s, (q_a, q_s)))
    return assignments


def run() -> dict[str, object]:
    fourier_by_key, _cross_by_key, support_by_key = load_inputs()
    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    records: list[dict[str, object]] = []
    state_category_counts: Counter[str] = Counter()
    radius_counts: Counter[int] = Counter()
    assignment_counts: Counter[str] = Counter()
    layer_count = 0
    universally_unsupported_layer_count = 0
    total_assignment_count = 0

    for index, key in enumerate(sorted(support_by_key), start=1):
        record = fourier_by_key[key]
        prime, R = key
        if prime not in source_cache:
            _bound, source_cache[prime] = capacity.source.enumerate_linear_source_states(prime)
        assignments = admissible_assignments(record, source_cache[prime])
        overflow = support_by_key[key]
        excess_by_q = {}
        for pair, value in zip(overflow["factorization"], overflow["witness_exponents"]):
            q, exponent = int(pair[0]), int(pair[1])
            amount = max(0, abs(int(value)) - exponent)
            if amount:
                excess_by_q[q] = amount
        if not excess_by_q:
            raise AssertionError("a radius-six witness has no overflow coordinates")
        max_height_by_q = {q: 0 for q in excess_by_q}
        best_excess_assignment_count = 0
        best_baseline_assignment_count = 0
        for a, s, _directions in assignments:
            blocks = (a * R + 1, s * R + 1)
            all_excess = True
            all_baseline = True
            for q, excess in excess_by_q.items():
                height = max(
                    capacity.valuation(blocks[0], q),
                    capacity.valuation(blocks[1], q),
                )
                max_height_by_q[q] = max(max_height_by_q[q], height)
                all_excess &= height >= excess
                required = capacity.required_heights(record)
                baseline = required[q] if q in required else 1
                all_baseline &= height >= baseline + excess
            best_excess_assignment_count += int(all_excess)
            best_baseline_assignment_count += int(all_baseline)

        layer_count += sum(excess_by_q.values())
        unsupported_q = {
            q: excess
            for q, excess in excess_by_q.items()
            if max_height_by_q[q] < excess
        }
        universally_unsupported_layer_count += sum(unsupported_q.values())
        if best_excess_assignment_count:
            category = "some_assignment_can_carry_all_excess"
        else:
            category = "no_assignment_can_carry_all_excess"
        state_category_counts[category] += 1
        assignment_counts["with_any_admissible_assignment" if assignments else "no_admissible_assignment"] += 1
        radius_counts[int(overflow["witness_radius"])] += 1
        total_assignment_count += len(assignments)
        records.append(
            {
                "prime": prime,
                "R": R,
                "witness_radius": int(overflow["witness_radius"]),
                "overflow_excess": {str(q): int(value) for q, value in sorted(excess_by_q.items())},
                "admissible_assignment_count": len(assignments),
                "assignment_can_carry_all_excess_count": best_excess_assignment_count,
                "assignment_can_carry_baseline_plus_excess_count": best_baseline_assignment_count,
                "max_height_by_q": {str(q): int(value) for q, value in sorted(max_height_by_q.items())},
                "universally_unsupported_excess": {
                    str(q): int(value) for q, value in sorted(unsupported_q.items())
                },
                "category": category,
            }
        )
        if index % 25 == 0:
            print(f"processed {index}/{len(support_by_key)}", file=sys.stderr)

    return {
        "arithmetic": (
            "For every frozen square-terminal F state, enumerate every admissible linear source "
            "and active-direction assignment. For each overflow coordinate, allow the best of the "
            "two source blocks as carrier, giving an optimistic height upper bound."
        ),
        "scope_note": (
            "Finite optimistic upper bound only. It ignores conflicts between multiple overflow "
            "coordinates and therefore can only certify universal height insufficiency, not prove "
            "that a feasible assignment exists. It does not search new source families."
        ),
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "cross_input": CROSS_INPUT.name,
        "cross_input_sha256": sha256(CROSS_INPUT),
        "support_input": SUPPORT_INPUT.name,
        "support_input_sha256": sha256(SUPPORT_INPUT),
        "square_input": SQUARE_INPUT.name,
        "square_input_sha256": sha256(SQUARE_INPUT),
        "state_count": len(records),
        "total_admissible_assignment_count": total_assignment_count,
        "overflow_layer_count": layer_count,
        "universally_unsupported_excess_layer_count": universally_unsupported_layer_count,
        "state_category_counts": dict(sorted(state_category_counts.items())),
        "assignment_counts": dict(sorted(assignment_counts.items())),
        "radius_histogram": {str(key): int(value) for key, value in sorted(radius_counts.items())},
        "records": records,
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
                    "state_count",
                    "total_admissible_assignment_count",
                    "overflow_layer_count",
                    "universally_unsupported_excess_layer_count",
                    "state_category_counts",
                    "assignment_counts",
                    "radius_histogram",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
