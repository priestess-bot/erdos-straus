#!/usr/bin/env python3
"""Profile alternative strict descents for pure-new marked-tail misses.

This is a derived finite audit.  It joins three independently checked H19
artifacts: the pure-new scaled-first marked-tail profile, the unrestricted
ordinary Type II tail profile, and the strict-descent closure.  It does not
search for a new universal selector.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MARKED = ROOT / "reproductions" / "type-ii-h19-pure-new-scaled-tail-1b-s1008-results.json"
DEFAULT_TAILS = ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json"
DEFAULT_CLOSURE = ROOT / "reproductions" / "type-ii-h19-all-strict-descent-closure-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-pure-new-marked-tail-bridge-1b-results.json"


def as_prime_set(values: object, label: str) -> set[int]:
    """Normalize a stored prime list and reject duplicate records."""
    if not isinstance(values, list):
        raise AssertionError(f"{label} must be a list")
    primes = [int(value) for value in values]
    if len(primes) != len(set(primes)):
        raise AssertionError(f"{label} contains duplicate primes")
    return set(primes)


def tail_map(payload: dict[str, object]) -> dict[int, dict[str, int]]:
    """Index the independently checked least-gap ordinary-tail witnesses."""
    records = payload.get("tail_records")
    if not isinstance(records, list):
        raise AssertionError("tail profile has no tail_records list")
    indexed: dict[int, dict[str, int]] = {}
    for record in records:
        if not isinstance(record, dict) or "prime" not in record:
            raise AssertionError("malformed ordinary-tail record")
        witness = record.get("tail_deflation_witness")
        if not isinstance(witness, dict):
            raise AssertionError("ordinary-tail record has no witness")
        prime = int(record["prime"])
        if prime in indexed:
            raise AssertionError("ordinary-tail profile contains duplicate primes")
        indexed[prime] = {
            "gap": int(witness["gap"]),
            "source_denominator": int(witness["source_denominator"]),
            "certificate_divisor": int(witness["divisor"]),
        }
    return indexed


def external_map(payload: dict[str, object]) -> dict[int, dict[str, int]]:
    """Index the exact external fallback witnesses from the strict closure."""
    records = payload.get("adaptive_external_fallback_records")
    if not isinstance(records, list):
        raise AssertionError("strict closure has no external fallback list")
    indexed: dict[int, dict[str, int]] = {}
    for record in records:
        if not isinstance(record, dict) or "prime" not in record:
            raise AssertionError("malformed external fallback record")
        witness = record.get("adaptive_external_descent")
        if not isinstance(witness, dict):
            raise AssertionError("external fallback record has no witness")
        prime = int(record["prime"])
        if prime in indexed:
            raise AssertionError("strict closure contains duplicate external primes")
        indexed[prime] = {
            "source_denominator": int(witness["source_denominator"]),
            "k": int(witness["k"]),
            "q": int(witness["q"]),
            "factor": int(witness["factor"]),
            "gap": int(witness["gap"]),
        }
    return indexed


def run_profile(
    marked_payload: dict[str, object],
    tail_payload: dict[str, object],
    closure_payload: dict[str, object],
) -> dict[str, object]:
    """Partition pure-new marked misses by their independently checked closure."""
    marked_misses = as_prime_set(marked_payload.get("missing_through_cap"), "marked misses")
    tails = tail_map(tail_payload)
    externals = external_map(closure_payload)
    prime_limit = int(marked_payload["prime_limit"])
    base_shift_bound = int(marked_payload["base_shift_bound"])
    if int(tail_payload["prime_limit"]) != prime_limit or int(
        closure_payload["prime_limit"]
    ) != prime_limit:
        raise AssertionError("input profiles have different prime limits")
    if int(tail_payload["base_shift_bound"]) != base_shift_bound or int(
        closure_payload["base_shift_bound"]
    ) != base_shift_bound:
        raise AssertionError("input profiles have different H19 base bounds")
    if int(tail_payload["tail_deflation_count"]) != len(tails):
        raise AssertionError("ordinary-tail count does not match its records")
    if int(closure_payload["two_tail_descent_count"]) != len(tails):
        raise AssertionError("strict closure does not retain the ordinary-tail count")
    if int(closure_payload["adaptive_external_fallback_count"]) != len(externals):
        raise AssertionError("external fallback count does not match its records")
    tail_primes = marked_misses & set(tails)
    external_primes = marked_misses & set(externals)
    if tail_primes & external_primes:
        raise AssertionError("ordinary-tail and external branches overlap")
    if tail_primes | external_primes != marked_misses:
        unresolved = sorted(marked_misses - tail_primes - external_primes)
        raise AssertionError(f"marked misses are not closed: {unresolved}")
    if closure_payload.get("unclosed_primes") != []:
        raise AssertionError("input strict closure is itself incomplete")

    independent_records = [
        {"prime": prime, **tails[prime]} for prime in sorted(tail_primes)
    ]
    gap_histogram = Counter(record["gap"] for record in independent_records)
    high_gap_records = [
        record for record in independent_records if record["gap"] > 23
    ]
    high_gap_records.sort(key=lambda record: (record["gap"], record["prime"]))
    external_records = [
        {"prime": prime, **externals[prime]} for prime in sorted(external_primes)
    ]
    return {
        "arithmetic": (
            "deterministic set intersection of three checked finite artifacts: "
            "the pure-new marked-tail misses, exact ordinary two-tail witnesses, "
            "and exact adaptive-external strict descents"
        ),
        "scope_note": (
            "A finite H19 bridge profile. It records how this marked-window "
            "failure set is closed by other branches; it is not a universal "
            "alternative-certificate or external-source selector."
        ),
        "prime_limit": prime_limit,
        "base_shift_bound": base_shift_bound,
        "marked_shift_cap": int(marked_payload["shift_cap"]),
        "pure_new_marked_miss_count": len(marked_misses),
        "independent_two_tail_count": len(independent_records),
        "adaptive_external_count": len(external_records),
        "unclosed_primes": [],
        "independent_tail_primes": [record["prime"] for record in independent_records],
        "independent_tail_gap_histogram": {
            str(gap): count for gap, count in sorted(gap_histogram.items())
        },
        "independent_tail_gap_at_most_23": sum(
            count for gap, count in gap_histogram.items() if gap <= 23
        ),
        "independent_tail_gap_at_most_63": sum(
            count for gap, count in gap_histogram.items() if gap <= 63
        ),
        "maximum_minimal_independent_tail_gap": max(gap_histogram, default=None),
        "high_gap_threshold": 23,
        "high_gap_record_count": len(high_gap_records),
        "high_gap_records": high_gap_records,
        "adaptive_external_records": external_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--marked-profile", type=Path, default=DEFAULT_MARKED)
    parser.add_argument("--tail-profile", type=Path, default=DEFAULT_TAILS)
    parser.add_argument("--strict-closure", type=Path, default=DEFAULT_CLOSURE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(
        json.loads(args.marked_profile.read_text(encoding="utf-8")),
        json.loads(args.tail_profile.read_text(encoding="utf-8")),
        json.loads(args.strict_closure.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
