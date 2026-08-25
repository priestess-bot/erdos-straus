#!/usr/bin/env python3
"""Build greedy relation-lattice certificates on the split-color F branch."""

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
LATTICE_SCRIPT = ROOT / "reproductions" / "type_i_f_relation_lattice_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-split-color-relation-certificate-results.json"
EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_CROSS_SHA256 = "c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5"


def load_lattice_module():
    spec = importlib.util.spec_from_file_location("split_color_lattice", LATTICE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {LATTICE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


lattice = load_lattice_module()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_pair(value) -> list[int]:
    value = lattice.sympy.Rational(value)
    return [int(value.p), int(value.q)]


def load_records() -> list[dict[str, object]]:
    if sha256(FOURIER_INPUT) != EXPECTED_FOURIER_SHA256:
        raise AssertionError("the frozen Fourier input changed")
    if sha256(CROSS_INPUT) != EXPECTED_CROSS_SHA256:
        raise AssertionError("the frozen cross-color input changed")
    fourier = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    cross = json.loads(CROSS_INPUT.read_text(encoding="utf-8"))
    unresolved = {
        (int(record["prime"]), int(record["R"]))
        for record in cross["unresolved_records"]
    }
    records = [
        dict(record)
        for record in fourier["records"]
        if (int(record["prime"]), int(record["R"])) in unresolved
    ]
    if len(records) != len(unresolved):
        raise AssertionError("cross-color unresolved records did not match Fourier records")
    return records


def equation_holds(point: tuple[int, ...], phase, target) -> bool:
    return (sum(value * coordinate for value, coordinate in zip(phase, point)) - target).q == 1


def reconstruct(record: dict[str, object]) -> dict[str, object]:
    factors = [(int(q), int(e)) for q, e in record["factorization"]]
    R = int(record["R"])
    certificate = lattice.pair.source.unit_group_subgroup_certificate(factors, R)
    if not certificate["target_in_generated_subgroup"]:
        raise AssertionError("split-color state is not in the generated subgroup")
    relation_basis, target_preimage, orders = lattice.solve_relation_lattice(
        factors, certificate
    )
    dual_basis = relation_basis.inv().T
    dimension = len(factors)
    points = list(
        itertools.product(
            *[range(-exponent, exponent + 1) for _prime, exponent in factors]
        )
    )
    available = []
    for column in range(dimension):
        phase = [lattice.sympy.Rational(value) for value in dual_basis[:, column]]
        target = sum(phase[index] * target_preimage[index] for index in range(dimension))
        available.append((column, phase, target))

    remaining = points
    selection = []
    unused = set(range(dimension))
    while remaining and unused:
        candidates = []
        for column in sorted(unused):
            _index, phase, target = available[column]
            survivors = [point for point in remaining if equation_holds(point, phase, target)]
            candidates.append((len(survivors), column, survivors))
        survivors_count, column, survivors = min(candidates, key=lambda item: (item[0], item[1]))
        if survivors_count >= len(remaining):
            break
        _index, phase, target = available[column]
        selection.append(
            {
                "basis_column": column,
                "dual_coordinates": [1 if index == column else 0 for index in range(dimension)],
                "phase_vector": [fraction_pair(value) for value in phase],
                "target_phase_mod_one": fraction_pair(target - lattice.sympy.floor(target)),
                "character_order": math.lcm(
                    *(int(lattice.sympy.Rational(value).q) for value in phase)
                ),
                "remaining_before": len(remaining),
                "remaining_after": survivors_count,
            }
        )
        remaining = survivors
        unused.remove(column)

    if remaining:
        raise AssertionError(
            f"greedy relation certificate did not empty the box for ({record['prime']}, {record['R']})"
        )
    return {
        "prime": int(record["prime"]),
        "R": R,
        "K": int(record["K"]),
        "factorization": [[q, exponent] for q, exponent in factors],
        "box_size": len(points),
        "relation_index": abs(int(relation_basis.det())),
        "certificate_length": len(selection),
        "certificate": selection,
        "target_preimage": target_preimage,
        "target_in_box": False,
    }


def run() -> dict[str, object]:
    records = load_records()
    certificates = [reconstruct(record) for record in records]
    lengths = Counter(int(item["certificate_length"]) for item in certificates)
    box_sizes = [int(item["box_size"]) for item in certificates]
    return {
        "arithmetic": "For every split-color unresolved F state, reconstruct the full relation lattice and greedily select independent dual basis equations until the finite exponent box is empty.",
        "scope_note": "Finite certificate reconstruction only. Greedy length is not a minimal certificate and no cross-state capacity contradiction or arithmetic descent is claimed.",
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "cross_color_input": CROSS_INPUT.name,
        "cross_color_input_sha256": sha256(CROSS_INPUT),
        "record_count": len(certificates),
        "certificate_length_distribution": {
            str(length): int(count) for length, count in sorted(lengths.items())
        },
        "maximum_box_size": max(box_sizes),
        "total_box_points_checked": sum(box_sizes),
        "certificates": certificates,
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
                    "record_count",
                    "certificate_length_distribution",
                    "maximum_box_size",
                    "total_box_points_checked",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
