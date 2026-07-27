#!/usr/bin/env python3
"""Split B=1 source-state misses into one-repeat closure and two-repeat boundary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
OVERFLOW = ROOT / "reproductions" / "type-i-source-state-b1-overflow-profile-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-source-state-one-repeat-boundary-results.json"
INPUT_COUNTS = {"H19-1B": 664, "tail-500M": 1717}


def summarize(profile: dict[str, object]) -> dict[str, object]:
    label = str(profile["label"])
    records = profile["records"]
    one_repeat = [record for record in records if int(record["extra_exponent_count"]) == 1]
    two_repeat = [record for record in records if int(record["extra_exponent_count"]) == 2]
    if len(one_repeat) + len(two_repeat) != len(records):
        raise AssertionError("overflow profile exceeded the one/two-repeat boundary")
    if not all(sympy.isprime(int(record["witness"]["B"])) for record in one_repeat):
        raise AssertionError("one-repeat witness did not recover a marked prime B")
    input_count = INPUT_COUNTS[label]
    return {
        "label": label,
        "input_count": input_count,
        "B_eq_1_realization_count": input_count - len(records),
        "one_repeat_realization_count": len(one_repeat),
        "B_eq_1_or_one_repeat_count": input_count - len(two_repeat),
        "two_repeat_boundary_count": len(two_repeat),
        "two_repeat_boundary": two_repeat,
    }


def run_audit(overflow: dict[str, object]) -> dict[str, object]:
    profiles = [summarize(profile) for profile in overflow["profiles"]]
    if [(profile["label"], profile["two_repeat_boundary_count"]) for profile in profiles] != [
        ("H19-1B", 2),
        ("tail-500M", 6),
    ]:
        raise AssertionError("one-repeat boundary did not match the stored overflow profile")
    return {
        "arithmetic": (
            "partition every stored B=1 miss by its verified least square-divisor exponent excess; "
            "an excess of one canonically has prime B and is a one-repeat normal realization"
        ),
        "scope_note": (
            "A finite partition of two stored source-state profiles. It does not prove that one repeat "
            "always suffices or supply a global rule selecting the marked prime."
        ),
        "profiles": profiles,
        "total_two_repeat_boundary_count": sum(profile["two_repeat_boundary_count"] for profile in profiles),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--overflow", type=Path, default=OVERFLOW)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.overflow.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
