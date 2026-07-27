#!/usr/bin/env python3
"""Measure later-r releases of high-overflow first even-source tail hits."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
R_PROFILE = ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json"
DEFAULT_R_CAP = 9_999
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


r_profile = load_module("h19_zero_overflow_r_release_profile", R_PROFILE)


def first_later_zero_overflow(prime: int, first_r: int, r_cap: int, r_start: int | None = None) -> int | None:
    """Find the first compatible r in the requested later-r interval with a zero-overflow divisor."""
    start = first_r + 8 if r_start is None else max(first_r + 8, r_start)
    start += (first_r - start) % 8
    for r in range(start, r_cap + 1, 8):
        if not r_profile.compatible_rays(prime, r):
            continue
        m1 = (r * prime + 1) // 4
        if any(int(divisor) % r == r - 1 for divisor in sympy.divisors(m1)):
            return r
    return None


def run_audit(payload: dict[str, object], r_cap: int = DEFAULT_R_CAP, r_start: int | None = None) -> dict[str, object]:
    """Profile later-r zero-overflow releases after every high-overflow first hit."""
    if r_cap < 7 or r_cap % 4 != 3:
        raise ValueError("r_cap must be at least 7 and 3 modulo 4")
    if r_start is not None and r_start < 7:
        raise ValueError("r_start must be at least 7 when supplied")
    records = []
    for record in payload["records"]:
        if int(record["minimum_overflow"]) == 1:
            continue
        prime, first_r = int(record["prime"]), int(record["r"])
        release = first_later_zero_overflow(prime, first_r, r_cap, r_start)
        records.append(
            {
                "prime": prime,
                "first_high_overflow_r": first_r,
                "later_zero_overflow_release_r": release,
            }
        )
    result = {
        "arithmetic": (
            "exact factor-pair enumeration of later r*p+1 values and ordinary-divisor "
            "tests for a=-1 modulo r after each stored high-overflow first hit"
        ),
        "scope_note": (
            "A finite later-r release profile through the supplied cap. It does not show "
            "that every high-overflow state releases at a larger r."
        ),
        "prime_limit": payload["prime_limit"],
        "r_cap": r_cap,
        "high_overflow_first_hit_count": len(records),
        "later_zero_overflow_release_count": sum(record["later_zero_overflow_release_r"] is not None for record in records),
        "unreleased_through_r_cap_count": sum(record["later_zero_overflow_release_r"] is None for record in records),
        "records": records,
    }
    if r_start is not None:
        result["r_start"] = r_start
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--r-cap", type=int, default=DEFAULT_R_CAP)
    parser.add_argument("--r-start", type=int)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")), args.r_cap, args.r_start)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
