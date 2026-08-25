#!/usr/bin/env python3
"""Audit which prime coordinates support the first relation-lattice overflow."""

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
LATTICE_SCRIPT = ROOT / "reproductions" / "type_i_f_relation_lattice_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_CROSS_SHA256 = "c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5"
RADIUS_CAP = 6


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


lattice = load_module("overflow_support_lattice", LATTICE_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_witness(logs, orders, target, factorization, radius):
    ranges = [
        range(-exponent - radius, exponent + radius + 1)
        for _q, exponent in factorization
    ]
    split = len(ranges) // 2
    left: dict[tuple[int, ...], tuple[int, ...]] = {}
    for exponents in itertools.product(*(ranges[index] for index in range(split))):
        residue = [0] * len(orders)
        for index, exponent in zip(range(split), exponents):
            for component, logarithm in enumerate(logs[index]):
                residue[component] = (
                    residue[component] + logarithm * exponent
                ) % orders[component]
        left.setdefault(tuple(residue), tuple(exponents))
    for exponents in itertools.product(
        *(ranges[index] for index in range(split, len(ranges)))
    ):
        residue = [0] * len(orders)
        for index, exponent in zip(range(split, len(ranges)), exponents):
            for component, logarithm in enumerate(logs[index]):
                residue[component] = (
                    residue[component] + logarithm * exponent
                ) % orders[component]
        needed = tuple(
            (target[component] - residue[component]) % orders[component]
            for component in range(len(orders))
        )
        if needed in left:
            return left[needed] + tuple(exponents)
    return None


def run() -> dict[str, object]:
    if sha256(FOURIER_INPUT) != EXPECTED_FOURIER_SHA256:
        raise AssertionError("the corrected Fourier input changed")
    if sha256(CROSS_INPUT) != EXPECTED_CROSS_SHA256:
        raise AssertionError("the corrected cross-color input changed")
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
        raise AssertionError("unresolved cross-color keys did not match Fourier records")

    details = []
    radius_counts: Counter[int] = Counter()
    support_counts: Counter[str] = Counter()
    overflow_coordinate_counts: Counter[str] = Counter()
    witness_found = 0
    for record in records:
        factorization = [
            (int(q), int(exponent)) for q, exponent in record["factorization"]
        ]
        certificate = lattice.pair.source.unit_group_subgroup_certificate(
            factorization, int(record["R"])
        )
        logs = [
            [int(value) for value in row]
            for row in certificate["generator_log_vectors"]
        ]
        orders = [int(component["order"]) for component in certificate["components"]]
        target = [order // 2 for order in orders]
        witness = None
        first_radius = None
        for radius in range(1, RADIUS_CAP + 1):
            witness = find_witness(logs, orders, target, factorization, radius)
            if witness is not None:
                first_radius = radius
                break

        active = {int(q) for q in record["active_primes"]}
        if witness is None:
            details.append(
                {
                    "prime": int(record["prime"]),
                    "R": int(record["R"]),
                    "active_primes": sorted(active),
                    "witness_radius": None,
                    "within_radius_cap": False,
                }
            )
            continue

        witness_found += 1
        excess = [
            max(0, abs(value) - exponent)
            for value, (_q, exponent) in zip(witness, factorization)
        ]
        support = [
            q for (q, _exponent), amount in zip(factorization, excess) if amount
        ]
        active_support = [q for q in support if q in active]
        inactive_support = [q for q in support if q not in active]
        active_excess = sum(
            amount
            for (q, _exponent), amount in zip(factorization, excess)
            if q in active
        )
        inactive_excess = sum(
            amount
            for (q, _exponent), amount in zip(factorization, excess)
            if q not in active
        )
        radius_counts[first_radius] += 1
        support_counts[
            "active_only"
            if inactive_excess == 0
            else "mixed"
            if active_excess
            else "inactive_only"
        ] += 1
        for q, amount in zip((q for q, _exponent in factorization), excess):
            if amount:
                overflow_coordinate_counts["active" if q in active else "inactive"] += 1
        details.append(
            {
                "prime": int(record["prime"]),
                "R": int(record["R"]),
                "active_primes": sorted(active),
                "witness_radius": first_radius,
                "within_radius_cap": True,
                "witness_exponents": list(witness),
                "factorization": [[int(q), int(exponent)] for q, exponent in factorization],
                "overflow_support": support,
                "active_overflow_support": active_support,
                "inactive_overflow_support": inactive_support,
                "active_excess": active_excess,
                "inactive_excess": inactive_excess,
            }
        )

    return {
        "arithmetic": (
            "For every split-color unresolved F state, find one target affine-lattice witness "
            "in an expanded exponent box up to radius six and classify whether its overflow "
            "coordinates lie in the selected Fourier-active support."
        ),
        "scope_note": (
            "Finite witness-support boundary. A missing witness beyond radius six is not a target "
            "nonexistence result. The support split tests whether a two-active-direction overflow "
            "to carrier-height implication is even compatible with the selected witnesses."
        ),
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "cross_input": CROSS_INPUT.name,
        "cross_input_sha256": sha256(CROSS_INPUT),
        "record_count": len(records),
        "radius_cap": RADIUS_CAP,
        "witness_found_count": witness_found,
        "witness_missing_count": len(records) - witness_found,
        "witness_radius_counts": {str(key): int(value) for key, value in sorted(radius_counts.items())},
        "support_class_counts": dict(sorted(support_counts.items())),
        "overflow_coordinate_counts": dict(sorted(overflow_coordinate_counts.items())),
        "records": details,
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
                    "record_count",
                    "radius_cap",
                    "witness_found_count",
                    "witness_missing_count",
                    "witness_radius_counts",
                    "support_class_counts",
                    "overflow_coordinate_counts",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
