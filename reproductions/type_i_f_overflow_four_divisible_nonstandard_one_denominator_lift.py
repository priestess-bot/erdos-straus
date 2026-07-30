#!/usr/bin/env python3
"""Audit one-denominator lifts from the 4|n nonstandard square-tail source."""

from __future__ import annotations

from collections import Counter
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
    / "type-i-f-overflow-four-divisible-nonstandard-one-denominator-lift-results.json"
)
EXPECTED_INPUT_SHA256 = "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_denominators(source: int) -> tuple[int, int, int]:
    if source < 4 or source % 4:
        raise AssertionError("source is not divisible by four")
    t = source // 4
    return t + 1, (t + 1) ** 2, t * (t + 1) ** 2


def verify_source(source: int, denominators: tuple[int, int, int]) -> None:
    if Fraction(4, source) != sum(
        (Fraction(1, value) for value in denominators), Fraction()
    ):
        raise AssertionError("nonstandard source identity failed")


def audit_coordinate(prime: int, source: int, preserved: int, coordinate: int) -> dict[str, object]:
    summary: dict[str, object] = {
        "prime": prime,
        "source": source,
        "coordinate": coordinate,
        "preserved": preserved,
        "positive_domain": False,
        "divisors_checked": 0,
        "congruence_candidates": 0,
        "target_candidates": 0,
        "natural_candidates": 0,
        "examples": [],
    }
    R = 4 * preserved - prime
    if R <= 0:
        return summary
    summary["positive_domain"] = True
    S = prime * preserved
    values: list[dict[str, int]] = []
    for e in divisors(S * S):
        if e > S:
            break
        summary["divisors_checked"] = int(summary["divisors_checked"]) + 1
        if (S + e) % R:
            continue
        summary["congruence_candidates"] = int(summary["congruence_candidates"]) + 1
        complementary = (S * S) // e
        if (S + complementary) % R:
            continue
        u = (S + e) // R
        v = (S + complementary) // R
        if u > v:
            raise AssertionError("nonstandard target tails are not ordered")
        summary["target_candidates"] = int(summary["target_candidates"]) + 1
        if Fraction(4, prime) != sum(
            (Fraction(1, value) for value in (preserved, u, v)), Fraction()
        ):
            raise AssertionError("nonstandard target identity failed")
        minimum = min(preserved, u, v)
        natural = 4 * minimum > prime and 2 * minimum <= prime
        if natural:
            summary["natural_candidates"] = int(summary["natural_candidates"]) + 1
        if len(values) < 20:
            values.append(
                {
                    "prime": prime,
                    "source": source,
                    "coordinate": coordinate,
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
    summary["examples"] = values
    return summary


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the square-terminal input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    candidates = list(payload.get("candidates", []))
    if len(candidates) != 253:
        raise AssertionError(f"unexpected candidate count: {len(candidates)}")

    summaries: list[dict[str, object]] = []
    for candidate in candidates:
        prime = int(candidate["prime"])
        source = int(candidate["source"])
        denominators = source_denominators(source)
        verify_source(source, denominators)
        for coordinate, preserved in enumerate(denominators):
            summaries.append(audit_coordinate(prime, source, preserved, coordinate))

    positive = [row for row in summaries if row["positive_domain"]]
    target_rows = [
        row for row in positive if int(row["target_candidates"]) > 0
    ]
    natural_rows = [
        row for row in positive if int(row["natural_candidates"]) > 0
    ]
    examples = [
        example
        for row in target_rows
        for example in row["examples"]
    ]
    return {
        "arithmetic": (
            "For every saved source n divisible by four, verify the nonstandard identity "
            "4/n=1/(n/4+1)+1/(n/4+1)^2+1/((n/4)(n/4+1)^2). For each coordinate c with "
            "4c-p>0, enumerate every e|(pc)^2 with e<=pc, test both one-denominator "
            "congruences, reconstruct the two target tails, and verify the rational identity."
        ),
        "scope_note": (
            "Finite targeted audit of the 4|n nonstandard source and the complete "
            "one-denominator-preserving lift criterion. It does not test lower-distance "
            "multi-coordinate lifts, other source identities, or Type II certificates."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "candidate_count": len(candidates),
        "coordinate_count": len(summaries),
        "positive_coordinate_count": len(positive),
        "divisors_checked": sum(int(row["divisors_checked"]) for row in positive),
        "congruence_candidate_count": sum(
            int(row["congruence_candidates"]) for row in positive
        ),
        "target_candidate_count": sum(int(row["target_candidates"]) for row in positive),
        "natural_candidate_count": sum(int(row["natural_candidates"]) for row in positive),
        "target_hit_prime_count": len(
            {int(example["prime"]) for example in examples}
        ),
        "natural_hit_prime_count": len(
            {
                int(example["prime"])
                for example in examples
                if int(example["natural_range"])
            }
        ),
        "coordinate_domain_histogram": dict(
            Counter(
                "positive" if bool(row["positive_domain"]) else "nonpositive"
                for row in summaries
            )
        ),
        "summaries": summaries,
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
                    "coordinate_count",
                    "positive_coordinate_count",
                    "divisors_checked",
                    "congruence_candidate_count",
                    "target_candidate_count",
                    "natural_candidate_count",
                    "target_hit_prime_count",
                    "natural_hit_prime_count",
                    "coordinate_domain_histogram",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
