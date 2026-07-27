#!/usr/bin/env python3
"""Classify half-factor witnesses at later-r zero-overflow releases."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
RAY_SCRIPT = ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py"
HALF_FACTOR_SCRIPT = ROOT / "reproductions" / "type_ii_h19_zero_overflow_half_factor_pair_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-cross-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


rays = load_module("h19_r_release_cross_rays", RAY_SCRIPT)
half_factor = load_module("h19_r_release_cross_half_factor", HALF_FACTOR_SCRIPT)


def ray_kind(prime: int, r: int, ray: dict[str, int]) -> str:
    """Classify whether one side or only a cross product hits -1 modulo r."""
    a, b = half_factor.half_factors(prime, r, int(ray["distance"]), int(ray["d"]))
    witness = half_factor.split_negative_one_divisor(a, b, r)
    left = half_factor.has_negative_one_divisor(a, r)
    right = half_factor.has_negative_one_divisor(b, r)
    if witness is None:
        raise AssertionError("later release ray lacks a zero-overflow cross witness")
    if left and right:
        return "both_sides"
    if left:
        return "left_only"
    if right:
        return "right_only"
    return "cross_essential"


def run_audit(release_payload: dict[str, object]) -> dict[str, object]:
    """Classify every compatible ray at every stored later-r release."""
    records = []
    for record in release_payload["records"]:
        release_r = record["later_zero_overflow_release_r"]
        if release_r is None:
            continue
        prime, r = int(record["prime"]), int(release_r)
        ray_rows = []
        for ray in rays.compatible_rays(prime, r):
            ray_rows.append({**ray, "kind": ray_kind(prime, r, ray)})
        if not ray_rows:
            raise AssertionError("stored release r has no compatible even-source ray")
        kinds = sorted({row["kind"] for row in ray_rows})
        records.append(
            {
                "prime": prime,
                "first_high_overflow_r": int(record["first_high_overflow_r"]),
                "release_r": r,
                "ray_kinds": ray_rows,
                "state_kind_set": kinds,
            }
        )
    ray_histogram = Counter(row["kind"] for record in records for row in record["ray_kinds"])
    state_histogram = Counter(",".join(record["state_kind_set"]) for record in records)
    return {
        "arithmetic": (
            "exact compatible factor-pair enumeration at each stored later-r release, "
            "followed by the cross-half-factor zero-overflow classification"
        ),
        "scope_note": (
            "A finite release-state profile. It does not construct a general r transition or selector."
        ),
        "prime_limit": release_payload["prime_limit"],
        "later_release_state_count": len(records),
        "later_release_ray_kind_histogram": dict(sorted(ray_histogram.items())),
        "later_release_state_kind_set_histogram": dict(sorted(state_histogram.items())),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
