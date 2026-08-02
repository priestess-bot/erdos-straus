#!/usr/bin/env python3
"""Audit actual linear carriers selected by bounded Fourier certificates.

The Fourier input already contains a canonical carrier vector for each frozen
F-state.  This script checks the arithmetic needed before those carriers can
be charged to a cross-state q-adic capacity bound: exact block heights,
pairwise label/modulus divisibility, and the mixed label--modulus capacity
inequality.  It deliberately does not interpret a Fourier certificate as a
marked lift or a recursive edge.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-certificate-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
OUTPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-carrier-capacity-results.json"
EXPECTED_INPUT_SHA256 = (
    "97bd474f82271b3d6a1eb5260fc49b7d48551c4fc2872402b74759f3d817bd68"
)
EXPECTED_SOURCE_SHA256 = (
    "96ee0c6711a4995fe387686a4915b41f1fcefa70cd4fe808c05a4092bf05e07d"
)
EXPECTED_STATE_COUNT = 45


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source() -> Any:
    spec = importlib.util.spec_from_file_location("carrier_capacity_source", SOURCE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


source = load_source()


def valuation(value: int, prime: int) -> int:
    if value <= 0 or prime <= 1:
        raise AssertionError("valuation requires a positive block and a prime")
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def load_records(path: Path) -> list[dict[str, Any]]:
    if sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen bounded-Fourier input changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED_STATE_COUNT:
        raise AssertionError("the frozen bounded-Fourier state count changed")
    return [dict(record) for record in records]


def recover_linear_state(cache: dict[tuple[int, int], tuple[int, int]], prime: int, R: int) -> tuple[int, int]:
    key = (prime, R)
    if key not in cache:
        _bound, states_by_R = source.enumerate_linear_source_states(prime)
        states = states_by_R.get(R)
        if not states:
            raise AssertionError(f"could not recover a linear state for {key}")
        cache[key] = max(states)
    return cache[key]


def carrier_entries(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cache: dict[tuple[int, int], tuple[int, int]] = {}
    entries: list[dict[str, Any]] = []
    seen: set[tuple[int, int, int, str]] = set()
    for record in records:
        prime = int(record["prime"])
        R = int(record["R"])
        a, s = recover_linear_state(cache, prime, R)
        stated_state = record.get("linear_state", {})
        if (int(stated_state.get("a", -1)), int(stated_state.get("s", -1))) != (a, s):
            raise AssertionError(f"linear state mismatch for ({prime}, {R})")
        for direction_index, raw in enumerate(record["carrier_vector"]):
            q = int(raw["prime"])
            label = str(raw["label"])
            if label not in {"s", "a"}:
                raise AssertionError("carrier label must be s or a")
            t = s if label == "s" else a
            block = t * R + 1
            height = valuation(block, q)
            stated_height = int(raw["height"])
            if height != stated_height or height <= 0:
                raise AssertionError(
                    f"carrier height mismatch for ({prime}, {R}, q={q}, {label})"
                )
            key = (prime, R, q, label)
            if key in seen:
                raise AssertionError(f"duplicate carrier direction {key}")
            seen.add(key)
            entries.append(
                {
                    "state_index": records.index(record),
                    "direction_index": direction_index,
                    "prime": prime,
                    "R": R,
                    "a": a,
                    "s": s,
                    "q": q,
                    "label": label,
                    "t": t,
                    "block": block,
                    "height": height,
                    "phase": raw.get("phase"),
                    "character_order": int(record["character_order"]),
                }
            )
    return entries


def capacity_bound(group: list[dict[str, Any]], q: int) -> tuple[Fraction, int, int, int]:
    labels = [int(entry["t"]) for entry in group]
    moduli = [int(entry["R"]) for entry in group]
    M_t = max(labels) - min(labels)
    M_R = max(moduli) - min(moduli)
    H = max(int(entry["height"]) for entry in group)
    bound = (
        Fraction(M_t * M_R, q * q - 1)
        + Fraction(M_t + M_R, q - 1)
        + H
    )
    return bound, M_t, M_R, H


def audit_group(key: tuple[int, int, str] | tuple[int, int], group: list[dict[str, Any]]) -> dict[str, Any]:
    q = int(key[1])
    pair_checks: list[dict[str, Any]] = []
    divisibility_failures = 0
    for index, left in enumerate(group):
        for right in group[index + 1 :]:
            common_height = min(int(left["height"]), int(right["height"]))
            required_power = q**common_height
            if int(left["t"]) != int(right["t"]):
                coordinate = "label"
                difference = abs(int(left["t"]) - int(right["t"]))
            else:
                coordinate = "modulus"
                difference = abs(int(left["R"]) - int(right["R"]))
            divides = difference % required_power == 0
            if not divides:
                divisibility_failures += 1
            pair_checks.append(
                {
                    "left": [int(left["prime"]), int(left["R"]), int(left["t"])],
                    "right": [int(right["prime"]), int(right["R"]), int(right["t"])],
                    "coordinate": coordinate,
                    "common_height": common_height,
                    "required_power": required_power,
                    "coordinate_difference": difference,
                    "divides": divides,
                }
            )
    bound, M_t, M_R, H = capacity_bound(group, q)
    height_sum = sum(int(entry["height"]) for entry in group)
    ratio = Fraction(height_sum, 1) / bound
    same_color = len(key) == 3
    return {
        "key": list(key),
        "q": q,
        "label": key[2] if same_color else None,
        "state_count": len(group),
        "directions": [
            {
                "prime": int(entry["prime"]),
                "R": int(entry["R"]),
                "label": entry["label"],
                "t": int(entry["t"]),
                "height": int(entry["height"]),
                "block": int(entry["block"]),
            }
            for entry in group
        ],
        "pair_checks": pair_checks,
        "pair_check_count": len(pair_checks),
        "divisibility_failure_count": divisibility_failures,
        "M_t": M_t,
        "M_R": M_R,
        "H": H,
        "height_sum": height_sum,
        "capacity_bound": fraction_pair(bound),
        "capacity_ratio": fraction_pair(ratio),
        "capacity_satisfied": Fraction(height_sum, 1) <= bound,
    }


def audit(entries: list[dict[str, Any]]) -> dict[str, Any]:
    same_color_groups: dict[tuple[int, int, str], list[dict[str, Any]]] = defaultdict(list)
    mixed_groups: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        same_color_groups[(int(entry["prime"]), int(entry["q"]), str(entry["label"]))].append(entry)
        mixed_groups[(int(entry["prime"]), int(entry["q"]))].append(entry)

    same_color = [audit_group(key, group) for key, group in sorted(same_color_groups.items())]
    mixed = [audit_group(key, group) for key, group in sorted(mixed_groups.items())]

    def summary(groups: list[dict[str, Any]]) -> dict[str, Any]:
        non_singleton = [group for group in groups if int(group["state_count"]) > 1]
        ratios = [
            Fraction(group["capacity_ratio"][0], group["capacity_ratio"][1])
            for group in groups
        ]
        non_singleton_ratios = [
            Fraction(group["capacity_ratio"][0], group["capacity_ratio"][1])
            for group in non_singleton
        ]
        return {
            "group_count": len(groups),
            "non_singleton_group_count": len(non_singleton),
            "pair_check_count": sum(int(group["pair_check_count"]) for group in groups),
            "divisibility_failure_count": sum(
                int(group["divisibility_failure_count"]) for group in groups
            ),
            "capacity_violation_count": sum(
                not bool(group["capacity_satisfied"]) for group in groups
            ),
            "max_capacity_ratio": fraction_pair(max(ratios)),
            "max_non_singleton_capacity_ratio": (
                fraction_pair(max(non_singleton_ratios)) if non_singleton_ratios else None
            ),
        }

    return {
        "same_color": summary(same_color),
        "mixed_color": summary(mixed),
        "same_color_groups": same_color,
        "mixed_color_groups": mixed,
    }


def build_payload(input_path: Path = INPUT) -> dict[str, Any]:
    records = load_records(input_path)
    entries = carrier_entries(records)
    audited = audit(entries)
    return {
        "arithmetic": (
            "For each frozen bounded-Fourier record, recover the exact linear source blocks "
            "U=sR+1 and V=aR+1 and verify the selected q-adic carrier height. For a fixed "
            "core prime and q, distinct labels are charged by label differences and equal "
            "labels by modulus differences. The mixed label--modulus capacity bound is "
            "then applied to both the same-color fibers and the union of colors."
        ),
        "scope_note": (
            "Finite negative boundary only. Every selected direction has a real positive "
            "carrier and all checked divisibility/capacity inequalities pass, but no group "
            "overloads. This does not prove a global Fourier maximizer, a cross-state demand "
            "lower bound, a marked lift, or a recursive edge. Character order and phase are "
            "kept as metadata and are not added to carrier height."
        ),
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "source_script": SOURCE_SCRIPT.name,
        "source_sha256": sha256(SOURCE_SCRIPT),
        "state_count": len(records),
        "direction_count": len(entries),
        "audit": audited,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if sha256(SOURCE_SCRIPT) != EXPECTED_SOURCE_SHA256:
        raise AssertionError("the frozen linear-source implementation changed")
    payload = build_payload(args.input)
    if args.verify:
        same_color = payload["audit"]["same_color"]
        if payload["state_count"] != EXPECTED_STATE_COUNT:
            raise AssertionError("state count changed")
        if payload["direction_count"] != 141:
            raise AssertionError("carrier direction count changed")
        if same_color["group_count"] != 113:
            raise AssertionError("same-color group count changed")
        if same_color["non_singleton_group_count"] != 15:
            raise AssertionError("same-color non-singleton count changed")
        for family in payload["audit"].values():
            if not isinstance(family, dict) or "divisibility_failure_count" not in family:
                continue
            if family["divisibility_failure_count"] != 0:
                raise AssertionError("carrier divisibility check failed")
            if family["capacity_violation_count"] != 0:
                raise AssertionError("carrier capacity bound was exceeded")
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "state_count": payload["state_count"],
                "direction_count": payload["direction_count"],
                "same_color": payload["audit"]["same_color"],
                "mixed_color": payload["audit"]["mixed_color"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
