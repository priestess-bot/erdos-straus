#!/usr/bin/env python3
"""Audit preserving n/2 in the standard even source."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from sympy import divisors


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"
OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-even-standard-half-one-denominator-lift-results.json"
)
EXPECTED_INPUT_SHA256 = "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the square-terminal input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    candidates = list(payload.get("candidates", []))
    if len(candidates) != 253:
        raise AssertionError(f"unexpected candidate count: {len(candidates)}")

    summaries: list[dict[str, int]] = []
    target_candidates: list[dict[str, int]] = []
    for candidate in candidates:
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
            summaries.append(summary)
            continue
        preserved = source // 2
        R = 4 * preserved - prime
        S = prime * preserved
        if R != 2 * source - prime or R <= 0:
            raise AssertionError("invalid n/2 source modulus")
        for e in divisors(S * S):
            if e > S:
                break
            summary["divisors_checked"] += 1
            if (S + e) % R:
                continue
            summary["congruence_candidates"] += 1
            complementary = (S * S) // e
            if (S + complementary) % R:
                continue
            u = (S + e) // R
            v = (S + complementary) // R
            if u > v:
                raise AssertionError("n/2 target tails are not ordered")
            summary["target_candidates"] += 1
            if Fraction(4, prime) != sum(
                (Fraction(1, value) for value in (preserved, u, v)), Fraction()
            ):
                raise AssertionError("n/2 target identity failed")
            minimum = min(preserved, u, v)
            natural = 4 * minimum > prime and 2 * minimum <= prime
            summary["natural_candidates"] += int(natural)
            target_candidates.append(
                {
                    "prime": prime,
                    "source": source,
                    "preserved": preserved,
                    "R": R,
                    "S": S,
                    "e": int(e),
                    "u": u,
                    "v": v,
                    "minimum_denominator": minimum,
                    "natural_range": int(natural),
                    "gap": 4 * minimum - prime,
                }
            )
        summaries.append(summary)

    upper = [row for row in summaries if row["upper_half"]]
    lower = [row for row in summaries if not row["upper_half"]]
    natural = [row for row in target_candidates if row["natural_range"]]
    return {
        "arithmetic": (
            "For every square-terminal source with p/2<n<p, start from the standard "
            "even source 4/n=1/(n/2)+1/n+1/n, preserve n/2, and enumerate every "
            "e|(p(n/2))^2 with e<=p(n/2) and (2n-p)|(p(n/2)+e)."
        ),
        "scope_note": (
            "Finite targeted audit of the n/2-preserving coordinate. It is complete for "
            "the 241 upper-half sources; lower-half sources have 2n-p<=0. A miss does "
            "not rule out nonstandard source solutions or multi-coordinate lifts."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "candidate_count": len(candidates),
        "upper_half_count": len(upper),
        "lower_half_count": len(lower),
        "divisors_checked": sum(row["divisors_checked"] for row in upper),
        "congruence_candidate_count": sum(row["congruence_candidates"] for row in upper),
        "target_candidate_count": len(target_candidates),
        "natural_candidate_count": len(natural),
        "target_hit_prime_count": len({row["prime"] for row in target_candidates}),
        "natural_hit_prime_count": len({row["prime"] for row in natural}),
        "summaries": summaries,
        "target_candidates": target_candidates,
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
