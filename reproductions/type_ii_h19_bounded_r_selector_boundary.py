#!/usr/bin/env python3
"""Measure fixed r caps on all stored 1b H19 residuals."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
DEFAULT_CAPS = (103, 999, 9_999)
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json"


def load_profile():
    spec = importlib.util.spec_from_file_location("bounded_r_selector_profile", PROFILE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PROFILE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


profile = load_profile()


def parse_caps(raw: str) -> tuple[int, ...]:
    caps = tuple(int(part.strip()) for part in raw.split(",") if part.strip())
    if not caps or tuple(sorted(set(caps))) != caps:
        raise ValueError("caps must be distinct, positive, and increasing")
    if any(cap < 7 or cap % 4 != 3 for cap in caps):
        raise ValueError("every cap must be at least seven and 3 modulo 4")
    return caps


def first_hit(prime: int, cap: int) -> dict[str, int] | None:
    """Find the first compatible square-tail state in the necessary r=7 mod 8 class."""
    for r in range(7, cap + 1, 8):
        rays = profile.compatible_rays(prime, r)
        if not rays:
            continue
        hits = profile.tail_hit_count(prime, r)
        if hits:
            ray = rays[0]
            return {
                "r": r,
                "distance": int(ray["distance"]),
                "d": int(ray["d"]),
                "compatible_ray_count": len(rays),
                "tail_residue_factor_count": hits,
            }
    return None


def run_audit(payload: dict[str, object], caps: tuple[int, ...] = DEFAULT_CAPS) -> dict[str, object]:
    """Profile the first r hit once, then report every requested cap cross-section."""
    if not caps or tuple(sorted(set(caps))) != caps:
        raise ValueError("caps must be distinct and increasing")
    primes = [int(record["prime"]) for record in payload["records"]]
    records = [{"prime": prime, "first_hit": first_hit(prime, caps[-1])} for prime in primes]
    stages = []
    for cap in caps:
        covered = [record for record in records if record["first_hit"] and record["first_hit"]["r"] <= cap]
        stages.append(
            {
                "r_cap": cap,
                "covered_count": len(covered),
                "uncovered_count": len(records) - len(covered),
                "first_r_histogram": dict(
                    sorted(Counter(record["first_hit"]["r"] for record in covered).items())
                ),
                "uncovered_primes": [
                    record["prime"]
                    for record in records
                    if record["first_hit"] is None or record["first_hit"]["r"] > cap
                ],
            }
        )
    return {
        "arithmetic": (
            "exact factor-pair enumeration and exact M1-squared divisor-residue "
            "tests for r=7 mod 8, with first hits measured through the largest cap"
        ),
        "scope_note": (
            "This is a finite boundary over the supplied H19 residual profile. "
            "It neither proves nor disproves a variable-r selector."
        ),
        "prime_limit": payload["prime_limit"],
        "h19_residual_count": len(records),
        "r_caps": list(caps),
        "all_checked_r_are_7_mod_8": True,
        "stages": stages,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--caps", default=",".join(str(cap) for cap in DEFAULT_CAPS))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload, parse_caps(args.caps))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
