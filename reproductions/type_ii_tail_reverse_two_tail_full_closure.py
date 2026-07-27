#!/usr/bin/env python3
"""Join the 500M ordinary-tail and reverse-two-tail strict closures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
REVERSE = ROOT / "reproductions" / "type-ii-tail-reverse-two-tail-500m-all-misses-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-reverse-two-tail-full-closure-500m-results.json"


def run_audit(tail: dict[str, object], reverse: dict[str, object]) -> dict[str, object]:
    if tail["prime_limit"] != reverse["input_prime_limit"]:
        raise ValueError("input ranges disagree")
    tail_misses = {int(entry["prime"]) for entry in tail["misses"]}
    reverse_primes = {int(entry["prime"]) for entry in reverse["records"]}
    if tail_misses != reverse_primes:
        raise AssertionError("reverse records do not exactly partition tail misses")
    if reverse["misses"]:
        raise AssertionError("reverse audit still has misses")
    core_count = int(tail["core_prime_count"])
    tail_hits = int(tail["tail_deflation_hit_count"])
    reverse_hits = int(reverse["captured_count"])
    if tail_hits + reverse_hits != core_count:
        raise AssertionError("strict-closure counts do not sum to the core population")
    return {
        "arithmetic": (
            "set equality between all ordinary Type II tail-deflation misses and "
            "the stored reverse-two-tail records, plus exact count partition of "
            "the 500M core-prime population"
        ),
        "scope_note": (
            "A finite strict-edge closure. The reverse branch remains a target-side "
            "certificate selector, not a uniform inductive descent theorem."
        ),
        "prime_limit": tail["prime_limit"],
        "core_prime_count": core_count,
        "ordinary_type_ii_tail_descent_count": tail_hits,
        "reverse_two_tail_descent_count": reverse_hits,
        "unclosed_count": 0,
        "maximum_reverse_gap": reverse["maximum_selected_gap"],
        "even_reverse_source_count": reverse["even_source_count"],
        "odd_reverse_source_count": reverse["odd_source_count"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--reverse", type=Path, default=REVERSE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.tail.read_text(encoding="utf-8")),
        json.loads(args.reverse.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
