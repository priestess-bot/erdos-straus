#!/usr/bin/env python3
"""Verify the q-adic phase-clearing cell and its conditional capacity bound.

The phase center is the exact fixed-B numerator-clearing residue

    gamma = -A * R^{-1} (mod q**e).

This script checks only the arithmetic bridge.  A phase representative is
not treated as an actual lift or a recursive edge unless a separate contract
supplies positivity, the marked solution set, and E1--E5.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-rational-gap-denominator-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-phase-clearing-cell-capacity-results.json"
EXPECTED_INPUT_SHA256 = (
    "60cbb80428d6e2fbb1295138fe265893d7bfecbd23a92ed863edf10e0361b768"
)

# These are deliberately small, named fixtures. Two are compatible cells;
# the third is a phase-incompatible pair and must not receive a capacity bound.
FIXTURES = [
    {
        "cell_id": "q5_distinct_phase_labels",
        "q": 5,
        "rows": [(5596369, 1251), (48991849, 7931)],
    },
    {
        "cell_id": "q151_duplicate_phase_label",
        "q": 151,
        "rows": [(214729, 43), (5596369, 43)],
    },
    {
        "cell_id": "q5_incompatible_phase_pair",
        "q": 5,
        "rows": [(5596369, 1251), (79312489, 6611)],
    },
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def load_rows(path: Path) -> dict[tuple[int, int], dict[str, Any]]:
    if sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen rational-gap input changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("records")
    if not isinstance(rows, list):
        raise AssertionError("the rational-gap input has no records")
    indexed: dict[tuple[int, int], dict[str, Any]] = {}
    for raw in rows:
        row = dict(raw)
        key = (int(row["prime"]), int(row["R"]))
        if key in indexed:
            raise AssertionError(f"duplicate frozen state {key}")
        indexed[key] = row
    return indexed


def phase_record(row: dict[str, Any], q: int) -> dict[str, Any]:
    prime = int(row["prime"])
    R = int(row["R"])
    A = int(row["formal_A"])
    excess = row.get("denominator_excess", {}).get(str(q))
    if excess is None:
        raise AssertionError(f"state ({prime}, {R}) has no q={q} overflow")
    e = int(excess)
    if q <= 2 or not all(q % d for d in range(2, math.isqrt(q) + 1)):
        raise AssertionError("the phase-clearing contract is restricted to odd primes")
    if e <= 0 or math.gcd(q, A) != 1 or math.gcd(q, R) != 1:
        raise AssertionError("invalid q-adic phase-clearing state")

    modulus = q**e
    gamma = (-A * pow(R, -1, modulus)) % modulus
    if gamma == 0:
        raise AssertionError("a valid overflow phase cannot have zero center")

    # The chosen label is the least positive representative. It is a
    # diagnostic bounded label, not evidence that the corresponding lift works.
    label = gamma
    if label % modulus != gamma:
        raise AssertionError("phase label does not hit its exact residue class")
    return {
        "prime": prime,
        "R": R,
        "A": A,
        "q": q,
        "height": e,
        "modulus": modulus,
        "phase_center": gamma,
        "label": label,
        "label_is_minimal_positive_representative": True,
    }


def compatible(left: dict[str, Any], right: dict[str, Any]) -> bool:
    if left["q"] != right["q"]:
        raise AssertionError("phase compatibility compared different primes")
    q = int(left["q"])
    common_height = min(int(left["height"]), int(right["height"]))
    modulus = q**common_height
    return (int(left["phase_center"]) - int(right["phase_center"])) % modulus == 0


def valuation(value: int, prime: int) -> int | None:
    """Return v_prime(value), using None for the zero determinant."""
    if value == 0:
        return None
    value = abs(value)
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def cross_determinant(left: dict[str, Any], right: dict[str, Any]) -> int:
    """The 2x2 wedge A_i R_j - A_j R_i of the phase coordinates."""
    return int(left["A"]) * int(right["R"]) - int(right["A"]) * int(left["R"])


def audit_fixture(fixture: dict[str, Any], indexed: dict[tuple[int, int], dict[str, Any]]) -> dict[str, Any]:
    q = int(fixture["q"])
    entries = [
        phase_record(indexed[(int(prime), int(R))], q)
        for prime, R in fixture["rows"]
    ]
    pair_checks = []
    for index, left in enumerate(entries):
        for right in entries[index + 1 :]:
            common_height = min(int(left["height"]), int(right["height"]))
            required = q**common_height
            divides = compatible(left, right)
            determinant = cross_determinant(left, right)
            determinant_height = valuation(determinant, q)
            determinant_compatible = determinant == 0 or determinant_height >= common_height
            if divides != determinant_compatible:
                raise AssertionError("phase and cross-determinant compatibility disagree")
            pair_checks.append(
                {
                    "left": [left["prime"], left["R"]],
                    "right": [right["prime"], right["R"]],
                    "common_height": common_height,
                    "required_power": required,
                    "phase_difference": int(left["phase_center"])
                    - int(right["phase_center"]),
                    "cross_determinant": determinant,
                    "cross_determinant_q_valuation": determinant_height,
                    "phase_compatible": divides,
                    "cross_determinant_compatible": determinant_compatible,
                }
            )

    phase_compatible = all(check["phase_compatible"] for check in pair_checks)
    labels = [int(entry["label"]) for entry in entries]
    multiplicity = max(Counter(labels).values()) if labels else 0
    result: dict[str, Any] = {
        "cell_id": fixture["cell_id"],
        "q": q,
        "entries": entries,
        "pair_checks": pair_checks,
        "phase_compatible": phase_compatible,
        "label_distinct": len(set(labels)) == len(labels),
        "label_multiplicity_bound": multiplicity,
    }

    if not phase_compatible:
        result["status"] = "phase_incompatible"
        result["capacity_status"] = "not_applicable"
        return result

    label_min, label_max = min(labels), max(labels)
    width = label_max - label_min
    height_sum = sum(int(entry["height"]) for entry in entries)
    maximum_height = max(int(entry["height"]) for entry in entries)
    raw_bound = Fraction(width, q - 1) + maximum_height
    adjusted_bound = multiplicity * raw_bound
    result.update(
        {
            "status": "phase_compatible",
            "label_interval": [label_min, label_max],
            "label_interval_width": width,
            "height_sum": height_sum,
            "maximum_height": maximum_height,
            "raw_capacity_bound": pair(raw_bound),
            "multiplicity_adjusted_capacity_bound": pair(adjusted_bound),
            "capacity_status": (
                "satisfied" if Fraction(height_sum) <= adjusted_bound else "violated"
            ),
        }
    )
    return result


def build_payload(path: Path = INPUT) -> dict[str, Any]:
    indexed = load_rows(path)
    cells = [audit_fixture(fixture, indexed) for fixture in FIXTURES]
    return {
        "arithmetic": (
            "For a fixed-B q-adic overflow e, every numerator-clearing shift s satisfies "
            "s = -A R^{-1} (mod q^e). Within a pairwise compatible phase cell, the "
            "cross determinant A_i R_j - A_j R_i has the same q-adic threshold as the "
            "phase difference. Within a pairwise compatible phase cell, the selected labels "
            "therefore obey q^min(e_i,e_j) | (s_i-s_j); the standard nested q-adic capacity "
            "bound applies."
        ),
        "scope_note": (
            "Conditional bridge only. The least positive phase representative is used as "
            "a bounded diagnostic label in these fixtures; it is not asserted to produce "
            "a positive marked lift. A future recursive edge still needs full E1--E5, "
            "nonempty marked solutions, and a well-founded potential. Incompatible phase "
            "cells receive no capacity bound. Repeated labels are charged by their maximum "
            "multiplicity."
        ),
        "input": path.name,
        "input_sha256": sha256(path),
        "cell_count": len(cells),
        "compatible_cell_count": sum(int(cell["phase_compatible"]) for cell in cells),
        "incompatible_cell_count": sum(not cell["phase_compatible"] for cell in cells),
        "capacity_satisfied_count": sum(
            cell.get("capacity_status") == "satisfied" for cell in cells
        ),
        "cells": cells,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    payload = build_payload(args.input)
    if args.verify:
        if payload["compatible_cell_count"] != 2:
            raise AssertionError("the compatible fixture count changed")
        if payload["incompatible_cell_count"] != 1:
            raise AssertionError("the incompatible fixture count changed")
        for cell in payload["cells"]:
            if cell["phase_compatible"] and cell["capacity_status"] != "satisfied":
                raise AssertionError(f"compatible cell exceeded capacity: {cell['cell_id']}")
        duplicate = next(
            cell for cell in payload["cells"] if cell["cell_id"] == "q151_duplicate_phase_label"
        )
        if duplicate["label_distinct"] or duplicate["label_multiplicity_bound"] != 2:
            raise AssertionError("duplicate-label multiplicity was not recorded")
        expected_separation = {
            "q5_distinct_phase_labels": 1,
            "q151_duplicate_phase_label": None,
            "q5_incompatible_phase_pair": 0,
        }
        for cell in payload["cells"]:
            observed = cell["pair_checks"][0]["cross_determinant_q_valuation"]
            if observed != expected_separation[cell["cell_id"]]:
                raise AssertionError("cross-determinant separation fixture changed")

    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: payload[key]
                for key in (
                    "cell_count",
                    "compatible_cell_count",
                    "incompatible_cell_count",
                    "capacity_satisfied_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
