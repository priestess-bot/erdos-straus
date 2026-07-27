#!/usr/bin/env python3
"""Verify zero-overflow even-source tails using ordinary M divisors only."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json"
DEFAULT_OVERFLOW = ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-zero-overflow-divisor-profile-1b-results.json"


def zero_overflow_divisors(m1: int, r: int) -> list[dict[str, int]]:
    """Return a|M with a=-1 mod r and its equivalent zero-overflow tail e=M/a."""
    rows = []
    for divisor in sympy.divisors(m1):
        divisor = int(divisor)
        if divisor % r != r - 1:
            continue
        factor = m1 // divisor
        x = (m1 + factor) // r
        if (
            (m1 + factor) % r
            or m1 % factor
            or factor > m1
            or x % factor
            or factor % r != (-m1) % r
        ):
            raise AssertionError("ordinary divisor did not reconstruct a zero-overflow tail")
        rows.append({"ordinary_divisor": divisor, "tail_factor": factor, "x": x})
    return rows


def run_audit(bounded_payload: dict[str, object], overflow_payload: dict[str, object]) -> dict[str, object]:
    """Cross-check ordinary residue divisors against all normalized M1-squared tails."""
    overflow = {int(record["prime"]): record for record in overflow_payload["records"]}
    records = []
    for record in bounded_payload["records"]:
        prime = int(record["prime"])
        hit = record["first_hit"]
        if hit is None:
            continue
        r = int(hit["r"])
        m1 = (r * prime + 1) // 4
        rows = zero_overflow_divisors(m1, r)
        normalized = overflow.get(prime)
        if normalized is None:
            raise AssertionError("first r hit is absent from overflow profile")
        expected = int(normalized["minimum_overflow_tail_count"]) if int(normalized["minimum_overflow"]) == 1 else 0
        if len(rows) != expected:
            raise AssertionError("ordinary divisor count disagrees with normalized B=1 tails")
        records.append({"prime": prime, "r": r, "zero_overflow_tail_count": len(rows)})
    return {
        "arithmetic": (
            "ordinary divisor enumeration a|M1 with a=-1 mod r, followed by the exact "
            "bijection e=M1/a to zero-overflow M1-squared tails"
        ),
        "scope_note": (
            "A finite verification of the zero-overflow divisor criterion on the stored "
            "first-r-hit profile. It does not establish an ordinary-divisor selector."
        ),
        "prime_limit": bounded_payload["prime_limit"],
        "first_hit_count": len(records),
        "zero_overflow_state_count": sum(record["zero_overflow_tail_count"] > 0 for record in records),
        "zero_overflow_tail_count": sum(int(record["zero_overflow_tail_count"]) for record in records),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--overflow", type=Path, default=DEFAULT_OVERFLOW)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.input.read_text(encoding="utf-8")),
        json.loads(args.overflow.read_text(encoding="utf-8")),
    )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
