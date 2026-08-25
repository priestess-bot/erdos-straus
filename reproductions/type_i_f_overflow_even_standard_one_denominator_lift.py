#!/usr/bin/env python3
"""Audit one-denominator-preserving lifts from even square-terminal sources."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from sympy import divisors


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-even-standard-one-denominator-lift-results.json"
EXPECTED_INPUT_SHA256 = "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_candidate(candidate: dict[str, int]) -> tuple[dict[str, int], list[dict[str, int]]]:
    prime = int(candidate["prime"])
    source = int(candidate["source"])
    if source % 2 or not (2 <= source < prime):
        raise AssertionError("invalid even square-terminal source")
    summary = {
        "prime": prime,
        "source": source,
        "upper_half": int(2 * source > prime),
        "divisors_checked": 0,
        "congruence_candidates": 0,
        "target_candidates": 0,
        "natural_candidates": 0,
    }
    if 2 * source <= prime:
        return summary, []

    R = 4 * source - prime
    S = prime * source
    if R <= 0 or R % 4 != 3:
        raise AssertionError("invalid upper-half source modulus")
    values: list[dict[str, int]] = []
    for e in divisors(S * S):
        summary["divisors_checked"] += 1
        if e > S or (S + e) % R:
            continue
        summary["congruence_candidates"] += 1
        complementary = (S * S) // e
        if (S + complementary) % R:
            raise AssertionError("coprime complement congruence failed")
        u = (S + e) // R
        v = (S + complementary) // R
        summary["target_candidates"] += 1
        if u > v:
            raise AssertionError("factor ordering failed")
        if Fraction(4, prime) != sum(
            (Fraction(1, value) for value in (source, u, v)), Fraction()
        ):
            raise AssertionError("one-denominator target identity failed")
        x = min(source, u, v)
        natural = 4 * x > prime and 2 * x <= prime
        if natural:
            summary["natural_candidates"] += 1
        values.append(
            {
                "prime": prime,
                "source": source,
                "R": R,
                "S": S,
                "e": int(e),
                "u": u,
                "v": v,
                "minimum_denominator": x,
                "natural_range": int(natural),
                "gap": 4 * x - prime,
            }
        )
    return summary, values


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the square-terminal input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    candidates = list(payload.get("candidates", []))
    if len(candidates) != 253:
        raise AssertionError(f"unexpected candidate count: {len(candidates)}")

    summaries: list[dict[str, int]] = []
    values: list[dict[str, int]] = []
    for candidate in candidates:
        summary, local_values = audit_candidate(candidate)
        summaries.append(summary)
        values.extend(local_values)

    upper_summaries = [row for row in summaries if row["upper_half"]]
    lower_summaries = [row for row in summaries if not row["upper_half"]]
    natural_values = [row for row in values if row["natural_range"]]
    return {
        "arithmetic": (
            "For every square-terminal source n with p/2<n<p, start from "
            "4/n=1/(n/2)+1/n+1/n, preserve 1/n, and enumerate every e|(np)^2 with "
            "e<=np and (4n-p)|(np+e). Reconstruct both target tails and verify the "
            "rational identity and natural certificate range."
        ),
        "scope_note": (
            "Finite targeted audit of the one-denominator-preserving standard-even-source "
            "lift. It is complete for the 241 upper-half sources among the 253 saved "
            "square terminals; the 12 lower-half sources are outside this theorem's "
            "R=4n-p>0 domain. A miss does not rule out other source solutions or "
            "multi-coordinate lifts."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "candidate_count": len(candidates),
        "upper_half_count": len(upper_summaries),
        "lower_half_count": len(lower_summaries),
        "divisors_checked": sum(row["divisors_checked"] for row in upper_summaries),
        "congruence_candidate_count": sum(
            row["congruence_candidates"] for row in upper_summaries
        ),
        "target_candidate_count": sum(row["target_candidates"] for row in upper_summaries),
        "natural_candidate_count": len(natural_values),
        "target_hit_prime_count": len({row["prime"] for row in values}),
        "natural_hit_prime_count": len({row["prime"] for row in natural_values}),
        "source_half_histogram": {
            "upper": len(upper_summaries),
            "lower_or_equal": len(lower_summaries),
        },
        "summaries": summaries,
        "target_candidates": values,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "candidate_count",
                    "upper_half_count",
                    "lower_half_count",
                    "divisors_checked",
                    "congruence_candidate_count",
                    "target_candidate_count",
                    "natural_candidate_count",
                    "target_hit_prime_count",
                    "natural_hit_prime_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
