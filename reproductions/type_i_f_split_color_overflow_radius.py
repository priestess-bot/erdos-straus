#!/usr/bin/env python3
"""Measure capped overflow radii of split-color F target affine lattices."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
CROSS_INPUT = ROOT / "reproductions" / "type-i-f-full-cross-color-pair-capacity-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_f_relation_lattice_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-split-color-overflow-radius-results.json"
EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_CROSS_SHA256 = "c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5"
RADIUS_CAP = 4


def load_source():
    spec = importlib.util.spec_from_file_location("overflow_radius_lattice", SOURCE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


lattice = load_source()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def in_expanded_box(logs, orders, target, factorization, radius):
    ranges = [range(-exponent - radius, exponent + radius + 1) for _q, exponent in factorization]
    split = len(ranges) // 2

    def partial_sums(indices):
        values = set()
        for exponents in itertools.product(*(ranges[index] for index in indices)):
            residue = [0] * len(orders)
            for index, exponent in zip(indices, exponents):
                for component, logarithm in enumerate(logs[index]):
                    residue[component] = (residue[component] + logarithm * exponent) % orders[component]
            values.add(tuple(residue))
        return values

    left = partial_sums(range(split))
    for right in partial_sums(range(split, len(ranges))):
        needed = tuple((target[index] - right[index]) % orders[index] for index in range(len(orders)))
        if needed in left:
            return True
    return False


def run() -> dict[str, object]:
    if sha256(FOURIER_INPUT) != EXPECTED_FOURIER_SHA256:
        raise AssertionError("the frozen Fourier input changed")
    if sha256(CROSS_INPUT) != EXPECTED_CROSS_SHA256:
        raise AssertionError("the frozen cross-color input changed")
    fourier = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    cross = json.loads(CROSS_INPUT.read_text(encoding="utf-8"))
    unresolved = {(int(record["prime"]), int(record["R"])) for record in cross["unresolved_records"]}
    records = [
        record for record in fourier["records"]
        if (int(record["prime"]), int(record["R"])) in unresolved
    ]
    if len(records) != len(unresolved):
        raise AssertionError("unresolved records did not match Fourier input")

    details = []
    distribution = Counter()
    total_capped_defect = 0
    for record in records:
        factorization = [(int(q), int(exponent)) for q, exponent in record["factorization"]]
        certificate = lattice.pair.source.unit_group_subgroup_certificate(factorization, int(record["R"]))
        logs = [[int(value) for value in row] for row in certificate["generator_log_vectors"]]
        orders = [int(component["order"]) for component in certificate["components"]]
        target = [order // 2 for order in orders]
        first_radius = None
        for radius in range(1, RADIUS_CAP + 1):
            if in_expanded_box(logs, orders, target, factorization, radius):
                first_radius = radius
                break
        capped_radius = first_radius if first_radius is not None else RADIUS_CAP + 1
        distribution[capped_radius] += 1
        total_capped_defect += capped_radius
        details.append(
            {
                "prime": int(record["prime"]),
                "R": int(record["R"]),
                "active_primes": [int(q) for q in record["active_primes"]],
                "character_order": int(record["character_order"]),
                "first_radius_at_most": first_radius,
                "capped_radius": capped_radius,
                "box_size": math.prod(2 * exponent + 1 for _q, exponent in factorization),
            }
        )
    return {
        "arithmetic": "For every split-color unresolved F state, use meet-in-the-middle to find the first radius delta up to four for which the target affine subgroup enters the exponent box with every coordinate bound expanded by delta.",
        "scope_note": "Finite capped overflow profile only. The overflow radius is not yet proved to consume a carrier height; the conditional capacity implication is recorded as an open bridge, not a theorem.",
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "cross_color_input": CROSS_INPUT.name,
        "cross_color_input_sha256": sha256(CROSS_INPUT),
        "record_count": len(records),
        "radius_cap": RADIUS_CAP,
        "capped_radius_distribution": {str(radius): int(count) for radius, count in sorted(distribution.items())},
        "within_cap_count": sum(count for radius, count in distribution.items() if radius <= RADIUS_CAP),
        "beyond_cap_count": distribution[RADIUS_CAP + 1],
        "capped_defect_sum": total_capped_defect,
        "records": details,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run()
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in ("record_count", "radius_cap", "capped_radius_distribution", "within_cap_count", "beyond_cap_count", "capped_defect_sum")}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
