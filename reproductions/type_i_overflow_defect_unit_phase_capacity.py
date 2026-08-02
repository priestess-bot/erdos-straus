#!/usr/bin/env python3
"""Audit the conditional phase bridge for overflow obstruction units.

For a ledger row with obstruction height h > 0, let b be the q-adic height
of its determinant residue label ell and define the normalized defect unit

    eta = (ell / q**b) mod q**h.

The units are canonical finite labels.  They form a phase cell only when
eta_i = eta_j (mod q**min(h_i, h_j)); that compatibility is an additional
cross-state hypothesis, not a consequence of the local obstruction ledger.
The script applies the existing phase-tree capacity bound to these labels
and records whether the frozen obstruction rows actually force overload.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-overflow-qadic-obstruction-transfer-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-overflow-defect-unit-phase-capacity-results.json"
EXPECTED_INPUT_SHA256 = (
    "c6f529c74493f37a3acd6bbeca1a672bc8a5c35e6390c56d5462debc48228f1a"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def normalize_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for case in payload["cases"]:
        for channel in case["channels"]:
            for raw in channel["q_layers"]:
                height = int(raw["obstruction_height"])
                if height <= 0:
                    continue
                q = int(raw["q"])
                residue_height = int(raw["residue_height"])
                label = int(raw["residue_label"])
                if label <= 0 or label % (q**residue_height):
                    raise AssertionError("residue label is not divisible by its q-height")
                unit = (label // (q**residue_height)) % (q**height)
                if unit <= 0 or unit % q == 0:
                    raise AssertionError("normalized defect is not a q-adic unit")
                modulus = q ** (residue_height + height)
                if (label - (q**residue_height) * unit) % modulus:
                    raise AssertionError("normalized unit lost its exact residue class")
                rows.append(
                    {
                        "case": case["name"],
                        "prime": int(case["prime"]),
                        "A": int(case["A"]),
                        "M": int(case["M"]),
                        "side": channel["side"],
                        "q": q,
                        "support_exponent": int(raw["support_exponent"]),
                        "carrier_height": int(raw["carrier_height"]),
                        "residue_height": residue_height,
                        "obstruction_height": height,
                        "residue_label": label,
                        "normalized_unit": unit,
                        "unit_modulus": q**height,
                    }
                )
    return rows


def compatible(left: dict[str, Any], right: dict[str, Any]) -> bool:
    if int(left["q"]) != int(right["q"]):
        raise AssertionError("phase comparison mixed q")
    q = int(left["q"])
    common_height = min(int(left["obstruction_height"]), int(right["obstruction_height"]))
    return (
        int(left["normalized_unit"]) - int(right["normalized_unit"])
    ) % (q**common_height) == 0


def phase_cells(entries: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    parent = list(range(len(entries)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for index, left in enumerate(entries):
        for right_index, right in enumerate(entries[index + 1 :], index + 1):
            if compatible(left, right):
                union(index, right_index)

    groups: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for index, entry in enumerate(entries):
        groups[find(index)].append(entry)
    result = list(groups.values())
    for group in result:
        for index, left in enumerate(group):
            if any(not compatible(left, right) for right in group[index + 1 :]):
                raise AssertionError("defect-unit compatibility was not transitive")
    return sorted(result, key=lambda group: min(int(row["prime"]) for row in group))


def capacity_for_cell(cell: list[dict[str, Any]], q: int) -> dict[str, Any]:
    labels = [int(row["normalized_unit"]) for row in cell]
    width = max(labels) - min(labels)
    multiplicity = max(Counter(labels).values())
    maximum_height = max(int(row["obstruction_height"]) for row in cell)
    layers: list[dict[str, Any]] = []
    capacity = Fraction(0)
    for height in range(1, maximum_height + 1):
        active = [
            row for row in cell if int(row["obstruction_height"]) >= height
        ]
        residues = sorted(
            {
                int(row["normalized_unit"]) % (q**height)
                for row in active
            }
        )
        slots_per_residue = width // (q**height) + 1
        layer_capacity = multiplicity * len(residues) * slots_per_residue
        active_count = len(active)
        if active_count > layer_capacity:
            raise AssertionError("phase-tree capacity inequality failed")
        capacity += layer_capacity
        layers.append(
            {
                "height": height,
                "active_count": active_count,
                "distinct_residue_count": len(residues),
                "residues": residues,
                "slots_per_residue": slots_per_residue,
                "capacity": layer_capacity,
            }
        )
    demand = sum(int(row["obstruction_height"]) for row in cell)
    return {
        "state_count": len(cell),
        "states": [[row["prime"], row["M"], row["side"]] for row in cell],
        "label_interval": [min(labels), max(labels)],
        "label_interval_width": width,
        "label_multiplicity": multiplicity,
        "maximum_height": maximum_height,
        "demand_height_sum": demand,
        "capacity_bound": pair(capacity),
        "capacity_satisfied": Fraction(demand) <= capacity,
        "layers": layers,
    }


def audit_group(q: int, entries: list[dict[str, Any]]) -> dict[str, Any]:
    cells = phase_cells(entries)
    pair_count = 0
    compatible_pair_count = 0
    for index, left in enumerate(entries):
        for right in entries[index + 1 :]:
            pair_count += 1
            compatible_pair_count += int(compatible(left, right))
    cell_rows = [capacity_for_cell(cell, q) for cell in cells]
    return {
        "q": q,
        "row_count": len(entries),
        "pair_count": pair_count,
        "compatible_pair_count": compatible_pair_count,
        "phase_cell_count": len(cells),
        "non_singleton_cell_count": sum(row["state_count"] > 1 for row in cell_rows),
        "capacity_overload_cell_count": sum(
            not row["capacity_satisfied"] for row in cell_rows
        ),
        "cells": cell_rows,
        "rows": entries,
    }


def build_payload(input_path: Path = INPUT) -> dict[str, Any]:
    if sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen obstruction ledger changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    rows = normalize_rows(payload)
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[int(row["q"])].append(row)
    groups = [audit_group(q, entries) for q, entries in sorted(grouped.items())]
    return {
        "arithmetic": (
            "For each obstruction row, normalize the determinant residue label ell by "
            "removing its q-adic valuation b and retain eta=(ell/q**b) mod q**h, where "
            "h is the unpaid support height. Defect-unit phase compatibility is eta_i = "
            "eta_j modulo q**min(h_i,h_j). Compatible cells then satisfy the usual "
            "nested phase-tree capacity bound."
        ),
        "scope_note": (
            "Conditional bridge only. The local overflow ledger does not prove that an "
            "alternate/source-switch must use these units as phases. The audit therefore "
            "reports the extra compatibility assumption and does not promote any cell "
            "to a recursive edge."
        ),
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "obstruction_row_count": len(rows),
        "q_group_count": len(groups),
        "phase_cell_count": sum(int(group["phase_cell_count"]) for group in groups),
        "non_singleton_cell_count": sum(
            int(group["non_singleton_cell_count"]) for group in groups
        ),
        "compatible_pair_count": sum(
            int(group["compatible_pair_count"]) for group in groups
        ),
        "pair_count": sum(int(group["pair_count"]) for group in groups),
        "capacity_overload_cell_count": sum(
            int(group["capacity_overload_cell_count"]) for group in groups
        ),
        "groups": groups,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_payload(args.input)
    if args.verify:
        if result["obstruction_row_count"] != 17:
            raise AssertionError("obstruction row count changed")
        if result["q_group_count"] != 5:
            raise AssertionError("q group count changed")
        if result["capacity_overload_cell_count"] != 0:
            raise AssertionError("focused defect-unit cells unexpectedly overload")
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "obstruction_row_count",
                    "q_group_count",
                    "phase_cell_count",
                    "non_singleton_cell_count",
                    "compatible_pair_count",
                    "pair_count",
                    "capacity_overload_cell_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
