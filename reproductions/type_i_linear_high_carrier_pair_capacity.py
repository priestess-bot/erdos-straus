#!/usr/bin/env python3
"""Audit pair capacity after height-priority carrier selection.

This is a finite diagnostic for the four frozen adversarial cores.  It uses the
available stabilizer-active directions as input; it does not claim that a
chosen Fourier certificate has the same support.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PAIR_SCRIPT = ROOT / "reproductions" / "type_i_linear_multi_active_pair_divisor_capacity.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-high-carrier-pair-capacity-results.json"
EXPECTED_TOTALS = {
    "state_count": 45,
    "pair_group_count": 40,
    "lower_joint_height_demand": 77,
    "exact_joint_height_demand": 100,
    "pair_capacity": 68,
    "joint_height_capacity": 134,
}


def load_pair_module():
    spec = importlib.util.spec_from_file_location("pair_capacity", PAIR_SCRIPT)
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


def choose_high_pair(
    prime: int, R: int, a: int, s: int, K: int, active: list[int]
) -> tuple[int, int, int, int, int]:
    blocks = ((s, s * R + 1), (a, a * R + 1))
    high: dict[int, tuple[int, int]] = {}
    for q in active:
        candidates = [(index, t, valuation(block, q)) for index, (t, block) in enumerate(blocks)]
        _, t, height = max(candidates, key=lambda item: (item[2], -item[0]))
        if height <= 0:
            raise AssertionError(f"active q has no carrier: {(prime, R, q)}")
        high[q] = (t, height)

    for t, _block in blocks:
        same = sorted(q for q in active if high[q][0] == t)
        if len(same) >= 2:
            q1, q2 = same[:2]
            return t, q1, q2, high[q1][1], high[q2][1]
    raise AssertionError(f"three active directions did not yield a pair: {(prime, R)}")


def run(input_path: Path) -> dict[str, object]:
    rows = pair.load_rows(input_path)
    groups: dict[tuple[int, int, int, int], list[tuple[int, int, int, int]]] = {}
    selected = []
    for prime, R, a, s, K, active in rows:
        t, q1, q2, h1, h2 = choose_high_pair(prime, R, a, s, K, active)
        nu1 = valuation(K, q1)
        nu2 = valuation(K, q2)
        lower1 = (nu1 + (2 if q1 == 2 else 0) + 1) // 2
        lower2 = (nu2 + (2 if q2 == 2 else 0) + 1) // 2
        if h1 < lower1 or h2 < lower2:
            raise AssertionError("height-priority lower bound failed")
        key = (prime, t, q1, q2)
        groups.setdefault(key, []).append((R, h1, h2, lower1 * lower2))
        selected.append(
            {
                "prime": prime,
                "R": R,
                "t": t,
                "pair": [q1, q2],
                "heights": [h1, h2],
                "lower_heights": [lower1, lower2],
            }
        )

    result_groups = {}
    demand = 0
    lower_demand = 0
    capacity = 0
    joint_capacity = 0
    by_prime: dict[str, dict[str, int]] = {}
    for (prime, t, q1, q2), values in groups.items():
        lo = min(row[0] for row in values)
        hi = max(row[0] for row in values)
        exact_demand = sum(row[1] * row[2] for row in values)
        exact_lower_demand = sum(row[3] for row in values)
        group_capacity = pair.pair_capacity(prime, t, q1, q2, lo, hi)
        group_joint_capacity = pair.joint_height_capacity(
            prime, t, q1, q2, lo, hi
        )
        demand += exact_demand
        lower_demand += exact_lower_demand
        capacity += group_capacity
        joint_capacity += group_joint_capacity
        result_groups[f"{prime}:{t}:{q1}:{q2}"] = {
            "state_count": len(values),
            "exact_joint_height_demand": exact_demand,
            "lower_joint_height_demand": exact_lower_demand,
            "pair_capacity": group_capacity,
            "joint_height_capacity": group_joint_capacity,
            "R_min": lo,
            "R_max": hi,
        }
        item = by_prime.setdefault(str(prime), {"states": 0, "lower_demand": 0, "demand": 0, "capacity": 0, "joint_capacity": 0})
        item["states"] += len(values)
        item["lower_demand"] += exact_lower_demand
        item["demand"] += exact_demand
        item["capacity"] += group_capacity
        item["joint_capacity"] += group_joint_capacity

    totals = {
        "state_count": len(rows),
        "pair_group_count": len(groups),
        "lower_joint_height_demand": lower_demand,
        "exact_joint_height_demand": demand,
        "pair_capacity": capacity,
        "joint_height_capacity": joint_capacity,
    }
    if totals != EXPECTED_TOTALS:
        raise AssertionError(f"frozen high-carrier totals changed: {totals}")
    if sum(item["states"] for item in by_prime.values()) != 45:
        raise AssertionError("unexpected frozen state count")
    return {
        "arithmetic": "Select the height-priority carrier for each available active prime, pair two primes sharing a block, and compare exact/lower joint height demand with exact divisor-residue capacity.",
        "scope_note": "Finite diagnostic only. Active directions come from the stabilizer profile; no claim is made that a selected Fourier/格 certificate has this support.",
        "input": input_path.name,
        "input_sha256": pair.sha256(input_path),
        **totals,
        "by_prime": by_prime,
        "groups": result_groups,
        "selected": selected,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=pair.INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run(args.input)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in ("state_count", "pair_group_count", "lower_joint_height_demand", "exact_joint_height_demand", "pair_capacity", "joint_height_capacity", "by_prime")}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
