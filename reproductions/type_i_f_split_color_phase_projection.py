#!/usr/bin/env python3
"""Audit two-dimensional Fourier target projections on the split-color branch."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
CROSS_INPUT = ROOT / "reproductions" / "type-i-f-full-cross-color-pair-capacity-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-split-color-phase-projection-results.json"
EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_CROSS_SHA256 = "c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def run() -> dict[str, object]:
    records = load_records()
    projection_counts = Counter()
    order_by_projection = Counter()
    empty_records = []
    detail = []
    for record in records:
        active = [int(index) for index in record["active_support"]]
        if len(active) != 2:
            raise AssertionError("the split-color branch is expected to have two active coordinates")
        factors = [(int(q), int(e)) for q, e in record["factorization"]]
        phases = [Fraction(int(numerator), int(denominator)) for numerator, denominator in record["phase_vector"]]
        target = Fraction(
            int(record["target_phase_mod_one"][0]),
            int(record["target_phase_mod_one"][1]),
        )
        first, second = active
        count = 0
        for left in range(-factors[first][1], factors[first][1] + 1):
            for right in range(-factors[second][1], factors[second][1] + 1):
                if (phases[first] * left + phases[second] * right - target).denominator == 1:
                    count += 1
        projection_counts[count] += 1
        order_by_projection[(count, int(record["character_order"]))] += 1
        item = {
            "prime": int(record["prime"]),
            "R": int(record["R"]),
            "active_primes": [int(record["active_primes"][0]), int(record["active_primes"][1])],
            "character_order": int(record["character_order"]),
            "projection_solution_count": count,
            "box_size": (2 * factors[first][1] + 1) * (2 * factors[second][1] + 1),
        }
        detail.append(item)
        if count == 0:
            empty_records.append(item)
    return {
        "arithmetic": "For every full-spectrum F state that cannot carry two active Fourier directions in one color, enumerate the exact two-coordinate target phase projection inside the exponent box.",
        "scope_note": "Finite state-internal Fourier boundary only. An empty projection is a certificate for the selected character, while a nonempty projection does not prove target membership; no cross-state selector theorem is claimed.",
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "cross_color_input": CROSS_INPUT.name,
        "cross_color_input_sha256": sha256(CROSS_INPUT),
        "record_count": len(records),
        "active_support_size_counts": {"2": len(records)},
        "projection_solution_count_distribution": {
            str(count): int(value) for count, value in sorted(projection_counts.items())
        },
        "empty_projection_count": len(empty_records),
        "nonempty_projection_count": len(records) - len(empty_records),
        "projection_order_distribution": {
            f"{count}:{order}": int(value)
            for (count, order), value in sorted(order_by_projection.items())
        },
        "empty_records": empty_records,
        "records": detail,
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
                    "active_support_size_counts",
                    "projection_solution_count_distribution",
                    "empty_projection_count",
                    "nonempty_projection_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
