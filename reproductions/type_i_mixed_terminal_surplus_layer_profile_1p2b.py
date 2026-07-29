#!/usr/bin/env python3
"""Profile the extra square-budget layer of the stored 500M--1.2B bridges.

For a maximum-tail reverse bridge, ``S=E/gcd(E,4K)`` measures the part of
the terminal factor that is supplied only by the square budget.  This script
reuses the already verified interval artifacts; it performs no new prime
scan and does not claim that the first stored bridge is the only bridge.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
INTERVALS = (
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json",
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-600m-700m-results.json",
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-700m-800m-results.json",
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-800m-900m-results.json",
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-900m-1b-results.json",
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-1b-1p1b-results.json",
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-1p1b-1p2b-results.json",
)
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-mixed-terminal-surplus-layer-profile-1p2b-results.json"


def stable_sha256(values: list[tuple[int, ...]]) -> str:
    payload = "\n".join(",".join(str(value) for value in row) for row in values)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def classify_surplus(surplus: int) -> str:
    if surplus == 1:
        return "S=1"
    if len(sympy.factorint(surplus)) == 1:
        return "single-prime-power"
    return "multi-prime-support"


def audit_interval(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows: list[tuple[int, ...]] = []
    categories: Counter[str] = Counter()
    side_categories: Counter[tuple[str, str]] = Counter()
    support_histogram: Counter[int] = Counter()
    exponent_histogram: Counter[int] = Counter()
    surplus_values: set[int] = set()
    for record in payload["type_i_even_terminal_bridge_records"]:
        prime = int(record["prime"])
        witness = record["type_i_even_witness"]
        gap = int(witness["gap"])
        A, B, C = (int(value) for value in witness["normal_form"])
        R = (4 * B * B * C + 1) // gap
        H = A * R - B
        K = B * C * H
        lift = witness["reverse_two_tail_lift"]
        E = int(lift["bridge_divisor"]) // (prime * prime)
        if gap * R != 4 * B * B * C + 1 or 4 * K != prime * R + 1:
            raise AssertionError("normal form did not reconstruct")
        if E <= 0 or 4 * K * K % E or E % R != 1 or E % 2:
            raise AssertionError("stored bridge factor failed its defining conditions")
        surplus = E // math.gcd(E, 4 * K)
        factors = sympy.factorint(surplus)
        category = classify_surplus(surplus)
        side = "small-side" if E < 2 * K else "large-side"
        categories[category] += 1
        side_categories[(side, category)] += 1
        support_histogram[len(factors)] += 1
        if len(factors) == 1:
            exponent_histogram[next(iter(factors.values()))] += 1
        surplus_values.add(surplus)
        rows.append((prime, gap, B, R, K, E, surplus))
    return {
        "prime_interval": payload["prime_interval"],
        "record_count": len(rows),
        "category_counts": dict(sorted(categories.items())),
        "side_counts": {
            side: sum(count for (record_side, _), count in side_categories.items() if record_side == side)
            for side in ("small-side", "large-side")
        },
        "side_category_counts": {
            f"{side}:{category}": count
            for (side, category), count in sorted(side_categories.items())
        },
        "support_histogram": {
            str(key): value for key, value in sorted(support_histogram.items())
        },
        "single_prime_power_exponent_histogram": {
            str(key): value for key, value in sorted(exponent_histogram.items())
        },
        "distinct_surplus_value_count": len(surplus_values),
        "maximum_surplus_value": max(surplus_values, default=None),
        "record_sha256": stable_sha256(rows),
    }


def run_audit(paths: tuple[Path, ...] = INTERVALS) -> dict[str, object]:
    profiles = [audit_interval(path) for path in paths]
    return {
        "arithmetic": (
            "reuse each stored first-even Type I bridge, reconstruct K and E exactly, and classify "
            "S=E/gcd(E,4K) by the number of distinct prime factors"
        ),
        "scope_note": (
            "This is a profile of the first stored even bridge in seven finite interval artifacts. "
            "It does not enumerate every possible bridge for a prime and cannot prove that a simpler "
            "bridge does not exist."
        ),
        "interval_count": len(profiles),
        "record_count": sum(int(profile["record_count"]) for profile in profiles),
        "category_counts": {
            category: sum(int(profile["category_counts"].get(category, 0)) for profile in profiles)
            for category in ("S=1", "single-prime-power", "multi-prime-support")
        },
        "side_counts": {
            side: sum(int(profile["side_counts"].get(side, 0)) for profile in profiles)
            for side in ("small-side", "large-side")
        },
        "side_category_counts": {
            f"{side}:{category}": sum(
                int(profile["side_category_counts"].get(f"{side}:{category}", 0))
                for profile in profiles
            )
            for side in ("small-side", "large-side")
            for category in ("S=1", "multi-prime-support", "single-prime-power")
            if any(
                f"{side}:{category}" in profile["side_category_counts"] for profile in profiles
            )
        },
        "support_histogram": {
            str(support): sum(
                int(profile["support_histogram"].get(str(support), 0)) for profile in profiles
            )
            for support in range(7)
            if any(str(support) in profile["support_histogram"] for profile in profiles)
        },
        "single_prime_power_exponent_histogram": {
            str(exponent): sum(
                int(profile["single_prime_power_exponent_histogram"].get(str(exponent), 0))
                for profile in profiles
            )
            for exponent in range(1, 7)
            if any(
                str(exponent) in profile["single_prime_power_exponent_histogram"]
                for profile in profiles
            )
        },
        "distinct_surplus_value_count_by_interval": [
            int(profile["distinct_surplus_value_count"]) for profile in profiles
        ],
        "maximum_surplus_value": max(
            int(profile["maximum_surplus_value"])
            for profile in profiles
            if profile["maximum_surplus_value"] is not None
        ),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit()
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "profiles"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
