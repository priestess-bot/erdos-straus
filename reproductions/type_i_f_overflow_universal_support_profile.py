#!/usr/bin/env python3
"""Profile the coordinate support and signs of universal overflow gaps."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSIGNMENT_INPUT = ROOT / "reproductions" / "type-i-f-overflow-all-assignment-height-upper-bound-results.json"
SUPPORT_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-universal-support-profile-results.json"

EXPECTED_ASSIGNMENT_SHA256 = "62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5"
EXPECTED_SUPPORT_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> dict[str, object]:
    if sha256(ASSIGNMENT_INPUT) != EXPECTED_ASSIGNMENT_SHA256:
        raise AssertionError("the frozen all-assignment input changed")
    if sha256(SUPPORT_INPUT) != EXPECTED_SUPPORT_SHA256:
        raise AssertionError("the frozen support input changed")

    assignment = json.loads(ASSIGNMENT_INPUT.read_text(encoding="utf-8"))
    support = json.loads(SUPPORT_INPUT.read_text(encoding="utf-8"))
    support_by_key = {
        (int(row["prime"]), int(row["R"])): row for row in support["records"]
    }
    universal = [
        row
        for row in assignment["records"]
        if row["category"] == "no_assignment_can_carry_all_excess"
    ]

    support_size_histogram: Counter[int] = Counter()
    sign_counts: Counter[str] = Counter()
    active_counts: Counter[str] = Counter()
    excess_histogram: Counter[int] = Counter()
    records: list[dict[str, object]] = []

    for row in universal:
        key = (int(row["prime"]), int(row["R"]))
        witness = support_by_key.get(key)
        if witness is None or not witness.get("within_radius_cap"):
            raise AssertionError(f"universal row lacks a capped witness: {key}")
        exponents = [int(value) for value in witness["witness_exponents"]]
        factorization = [
            (int(pair[0]), int(pair[1])) for pair in witness["factorization"]
        ]
        overflow = [
            max(0, abs(value) - exponent)
            for value, (_prime, exponent) in zip(exponents, factorization)
        ]
        indices = [index for index, value in enumerate(overflow) if value]
        if not indices:
            raise AssertionError(f"universal row has no overflow: {key}")
        support_size_histogram[len(indices)] += 1
        total_excess = sum(overflow)
        universal_unsupported_excess = sum(
            int(value) for value in row["universally_unsupported_excess"].values()
        )
        excess_histogram[total_excess] += 1
        signs = ["+" if exponents[index] > 0 else "-" for index in indices]
        if all(sign == "+" for sign in signs):
            sign_class = "all_positive"
        elif all(sign == "-" for sign in signs):
            sign_class = "all_negative"
        else:
            sign_class = "mixed"
        sign_counts[sign_class] += 1
        active = {int(value) for value in witness["active_primes"]}
        active_class = (
            "all_active"
            if all(factorization[index][0] in active for index in indices)
            else "has_inactive"
        )
        active_counts[active_class] += 1
        records.append(
            {
                "prime": key[0],
                "R": key[1],
                "witness_radius": int(witness["witness_radius"]),
                "overflow_support_size": len(indices),
                "total_excess": total_excess,
                "universal_unsupported_excess": universal_unsupported_excess,
                "sign_class": sign_class,
                "active_support_class": active_class,
                "overflow_support": [factorization[index][0] for index in indices],
                "witness_exponents": exponents,
                "factorization": [list(pair) for pair in factorization],
            }
        )

    result = {
        "arithmetic": (
            "For every universal height-gap state, reuse the first capped target-affine witness "
            "and classify the number, signs, and active/inactive support of its overflow coordinates."
        ),
        "scope_note": (
            "Finite profile only. The witness search is capped by the upstream radius-six audit; "
            "the profile does not prove that a larger-radius witness cannot have a different support. "
            "It does prove that every saved universal-gap witness in this frozen input is at least "
            "two-coordinate and therefore cannot be closed by a single-q bridge on this evidence."
        ),
        "assignment_input": ASSIGNMENT_INPUT.name,
        "assignment_input_sha256": sha256(ASSIGNMENT_INPUT),
        "support_input": SUPPORT_INPUT.name,
        "support_input_sha256": sha256(SUPPORT_INPUT),
        "universal_gap_state_count": len(universal),
        "single_coordinate_count": sum(
            count for size, count in support_size_histogram.items() if size == 1
        ),
        "support_size_histogram": {
            str(size): int(count)
            for size, count in sorted(support_size_histogram.items())
        },
        "sign_class_counts": dict(sorted(sign_counts.items())),
        "active_support_class_counts": dict(sorted(active_counts.items())),
        "total_excess": sum(int(row["total_excess"]) for row in records),
        "universal_unsupported_excess": sum(
            int(row["universal_unsupported_excess"]) for row in records
        ),
        "minimum_total_excess": min(int(row["total_excess"]) for row in records),
        "maximum_total_excess": max(int(row["total_excess"]) for row in records),
        "total_excess_histogram": {
            str(value): int(count)
            for value, count in sorted(excess_histogram.items())
        },
        "records": records,
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    result = run()
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "universal_gap_state_count",
                    "single_coordinate_count",
                    "support_size_histogram",
                    "sign_class_counts",
                    "active_support_class_counts",
                    "total_excess",
                    "minimum_total_excess",
                    "maximum_total_excess",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
