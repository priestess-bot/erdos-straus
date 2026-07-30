#!/usr/bin/env python3
"""Audit exact multi-active joint divisor capacity on frozen F profiles."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
PAIR_SCRIPT = ROOT / "reproductions" / "type_i_linear_multi_active_pair_divisor_capacity.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-multi-active-joint-divisor-capacity-results.json"
EXPECTED_TOTALS = {
    "state_count": 45,
    "block_record_count": 79,
    "lower_joint_demand": 114,
    "exact_joint_demand": 139,
    "joint_capacity": 139,
}


def load_pair_module():
    spec = importlib.util.spec_from_file_location("pair_capacity_for_joint", PAIR_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PAIR_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


pair = load_pair_module()


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def candidate_moduli(
    prime: int, label: int, directions: tuple[int, ...], lo: int, hi: int
) -> list[int]:
    product = math.prod(directions)
    if (prime - label) % product:
        return []
    result = []
    for divisor in sympy.divisors((prime - label) // product):
        if (product * divisor - 1) % label:
            continue
        modulus = (product * divisor - 1) // label
        if lo <= modulus <= hi:
            result.append(int(modulus))
    return result


def run(input_path: Path) -> dict[str, object]:
    rows = pair.load_rows(input_path)
    groups: dict[tuple[int, int, tuple[int, ...]], list[tuple[int, tuple[int, ...], int]]] = {}
    for prime, R, a, s, K, active in rows:
        blocks = ((s, s * R + 1), (a, a * R + 1))
        high_labels = {
            q: (s if valuation(s * R + 1, q) >= valuation(a * R + 1, q) else a)
            for q in active
        }
        for label, _block in blocks:
            directions = tuple(sorted(q for q in active if high_labels[q] == label))
            if len(directions) < 2:
                continue
            heights = tuple(valuation(label * R + 1, q) for q in directions)
            groups.setdefault((prime, label, directions), []).append((R, heights, K))

    lower_demand = exact_demand = joint_capacity = 0
    by_prime: dict[str, dict[str, int]] = {}
    group_rows = []
    for (prime, label, directions), values in sorted(groups.items()):
        lo = min(row[0] for row in values)
        hi = max(row[0] for row in values)
        exact = sum(math.prod(heights) for _R, heights, _K in values)
        lower = sum(
            math.prod(
                (valuation(K, q) + (2 if q == 2 else 0) + 1) // 2
                for q in directions
            )
            for _R, _heights, K in values
        )
        capacity = sum(
            math.prod(valuation(label * modulus + 1, q) for q in directions)
            for modulus in candidate_moduli(prime, label, directions, lo, hi)
        )
        lower_demand += lower
        exact_demand += exact
        joint_capacity += capacity
        item = by_prime.setdefault(
            str(prime),
            {"block_records": 0, "lower_demand": 0, "exact_demand": 0, "capacity": 0},
        )
        item["block_records"] += len(values)
        item["lower_demand"] += lower
        item["exact_demand"] += exact
        item["capacity"] += capacity
        group_rows.append(
            {
                "prime": prime,
                "label": label,
                "directions": list(directions),
                "record_count": len(values),
                "lower_demand": lower,
                "exact_demand": exact,
                "capacity": capacity,
                "R_min": lo,
                "R_max": hi,
            }
        )

    totals = {
        "state_count": len(rows),
        "block_record_count": sum(len(values) for values in groups.values()),
        "lower_joint_demand": lower_demand,
        "exact_joint_demand": exact_demand,
        "joint_capacity": joint_capacity,
    }
    if totals != EXPECTED_TOTALS:
        raise AssertionError(f"frozen joint-capacity totals changed: {totals}")
    return {
        "arithmetic": "For each frozen state and each height-priority block with at least two active directions, retain the full direction tuple and compare product-height demand with exact multi-divisor capacity.",
        "scope_note": "Finite diagnostic only. Stabilizer-active directions are not asserted to equal a selected Fourier/格 support.",
        "input": input_path.name,
        "input_sha256": pair.sha256(input_path),
        **totals,
        "by_prime": by_prime,
        "groups": group_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=pair.INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run(args.input)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: payload[key] for key in EXPECTED_TOTALS},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
