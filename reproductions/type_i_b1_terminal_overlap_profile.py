#!/usr/bin/env python3
"""Classify selected B=1 terminal bridges by their same-gap Type II overlap."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
B1 = ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-b1-terminal-overlap-profile-500m-results.json"


def classify_record(record: dict[str, object], ordinary_tail_misses: set[int]) -> dict[str, object]:
    """Classify one stored least-source B=1 bridge against the overlap criterion."""
    prime = int(record["prime"])
    witness = record["minimum_b1_source_witness"]
    gap = int(witness["gap"])
    A, B, C = (int(value) for value in witness["normal_form"])
    R = int(witness["R"])
    K = int(witness["K"])
    E = int(witness["E"])
    source = int(witness["reverse_two_tail_lift"]["source_denominator"])
    if (
        prime not in ordinary_tail_misses
        or B != 1
        or gap % 4 != 3
        or (4 * C + 1) != gap * R
        or 4 * K != prime * R + 1
        or E % R != 1
        or E % 2
        or E > 4 * K - 2 * R
        or (4 * K * K) % E
    ):
        raise AssertionError("stored B=1 terminal record failed reconstruction")
    if source != prime - 1:
        return {
            "prime": prime,
            "kind": "other_even_source",
            "gap": gap,
            "source_distance": prime - source,
        }
    if R % 4 != 3 or E != R + 1:
        raise AssertionError("p-1 B=1 bridge did not have the forced bridge factor")
    q = (gap + 1) // 4
    r = (R + 1) // 4
    if (A * r) % q == 0:
        # The exact same-gap criterion would explicitly construct a Type II ordinary tail,
        # contradicting that this prime belongs to the complete tail-miss input.
        raise AssertionError("ordinary-tail miss violated the B=1 same-gap criterion")
    return {
        "prime": prime,
        "kind": "p_minus_one_q_not_divide_Ar",
        "gap": gap,
        "A": A,
        "q": q,
        "r": r,
        "source_distance": 1,
    }


def run_profile(tail: dict[str, object], b1: dict[str, object]) -> dict[str, object]:
    """Validate the overlap split on the stored 500M ordinary-tail residual."""
    ordinary_tail_misses = {int(entry["prime"]) for entry in tail["misses"]}
    if len(ordinary_tail_misses) != 1_717 or int(b1["captured_count"]) != 1_713:
        raise AssertionError("input artifacts do not match the stated 500M profile")
    if int(b1["ordinary_tail_miss_count"]) != len(ordinary_tail_misses):
        raise AssertionError("the B=1 input does not cover the complete tail residual")
    classifications = [
        classify_record(record, ordinary_tail_misses) for record in b1["records"]
    ]
    if len(classifications) != int(b1["captured_count"]):
        raise AssertionError("the B=1 records were not classified exactly once")
    counts = Counter(entry["kind"] for entry in classifications)
    expected = {"p_minus_one_q_not_divide_Ar": 1_400, "other_even_source": 313}
    if dict(counts) != expected:
        raise AssertionError("the selected B=1 overlap profile changed")
    examples = {
        kind: next(entry for entry in classifications if entry["kind"] == kind)
        for kind in sorted(counts)
    }
    return {
        "arithmetic": (
            "validate every stored least-source B=1 terminal bridge on the complete 500M ordinary "
            "Type II tail residual; for p-1 sources write q=(m+1)/4 and r=(R+1)/4, then apply the "
            "exact same-gap criterion q|Ar => an ordinary Type II tail"
        ),
        "scope_note": (
            "This profiles only the selected least-source B=1 bridge in the stated finite box. It does "
            "not classify all B=1 bridges for a prime, bound q or r, or prove a global selector."
        ),
        "ordinary_tail_miss_count": len(ordinary_tail_misses),
        "b1_captured_count": len(classifications),
        "b1_miss_count": len(b1["misses"]),
        "counts": dict(sorted(counts.items())),
        "examples": examples,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--b1", type=Path, default=B1)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(
        json.loads(args.tail.read_text(encoding="utf-8")),
        json.loads(args.b1.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
