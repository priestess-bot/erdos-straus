#!/usr/bin/env python3
"""Aggregate the disjoint high-r release intervals into one exact empty-gap audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE = ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-profile-1b-results.json"
DEFAULT_INTERVALS = [
    ROOT / "reproductions" / f"type-ii-h19-zero-overflow-r-release-profile-1b-r{start}-{start + 9_992}-results.json"
    for start in range(10_007, 100_000, 10_000)
]
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-zero-overflow-high-r-gap-profile-1b-r99999-results.json"


def run_audit(base_payload: dict[str, object], interval_payloads: list[dict[str, object]]) -> dict[str, object]:
    """Verify consecutive r=7 mod 8 intervals contain no additional release."""
    base_records = base_payload["records"]
    base_primes = [int(record["prime"]) for record in base_records]
    expected_start = int(interval_payloads[0]["r_start"]) if interval_payloads else None
    interval_bounds = []
    for payload in interval_payloads:
        start, cap = int(payload["r_start"]), int(payload["r_cap"])
        if start != expected_start or start % 8 != 7 or cap % 8 != 7:
            raise AssertionError("intervals are not consecutive r=7 mod 8 scans")
        if int(payload["high_overflow_first_hit_count"]) != len(base_records):
            raise AssertionError("interval lost a high-overflow state")
        records = payload["records"]
        if [int(record["prime"]) for record in records] != base_primes:
            raise AssertionError("interval changed the high-overflow state order")
        if any(record["later_zero_overflow_release_r"] is not None for record in records):
            raise AssertionError("empty-gap aggregation received a nonempty release interval")
        interval_bounds.append({"r_start": start, "r_cap": cap})
        expected_start = cap + 8
    if not interval_bounds:
        raise ValueError("at least one interval is required")
    return {
        "arithmetic": (
            "exact aggregation of consecutive later-r ordinary-divisor release scans; every "
            "interval separately enumerates compatible factor pairs and divisors a|(r*p+1)/4 with a=-1 modulo r"
        ),
        "scope_note": (
            "A finite empty-gap audit from the stored r<=9999 release profile. It does not show that no release exists above its cap."
        ),
        "prime_limit": base_payload["prime_limit"],
        "high_overflow_first_hit_count": len(base_records),
        "initial_r_cap": base_payload["r_cap"],
        "initial_later_release_count": base_payload["later_zero_overflow_release_count"],
        "additional_release_count_in_high_r_gap": 0,
        "cumulative_r_cap": interval_bounds[-1]["r_cap"],
        "cumulative_later_zero_overflow_release_count": base_payload["later_zero_overflow_release_count"],
        "cumulative_unreleased_count": base_payload["unreleased_through_r_cap_count"],
        "intervals": interval_bounds,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--interval", type=Path, action="append", default=DEFAULT_INTERVALS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.base.read_text(encoding="utf-8")),
        [json.loads(path.read_text(encoding="utf-8")) for path in args.interval],
    )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
