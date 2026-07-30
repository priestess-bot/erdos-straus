#!/usr/bin/env python3
"""Compare canonical low-rank support with the first affine-box overflow support."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SQUARE_INPUT = ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"
SUPPORT_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
PROFILE_INPUT = ROOT / "reproductions" / "type-i-f-square-half-block-kneser-profile-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-square-terminal-overflow-support-alignment-results.json"

EXPECTED_SQUARE_SHA256 = "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1"
EXPECTED_SUPPORT_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"
EXPECTED_PROFILE_SHA256 = "680d290b79ab9ca4cc6a4d8940c3aa5ad4ef7884a115153c82bb85bba36042c3"
EXPECTED_COUNT = 253


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> dict[str, object]:
    expected = (
        (SQUARE_INPUT, EXPECTED_SQUARE_SHA256, "square"),
        (SUPPORT_INPUT, EXPECTED_SUPPORT_SHA256, "support"),
        (PROFILE_INPUT, EXPECTED_PROFILE_SHA256, "half-block profile"),
    )
    for path, digest, label in expected:
        if sha256(path) != digest:
            raise AssertionError(f"the frozen {label} input changed")
    square = json.loads(SQUARE_INPUT.read_text(encoding="utf-8"))
    support = json.loads(SUPPORT_INPUT.read_text(encoding="utf-8"))
    profile = json.loads(PROFILE_INPUT.read_text(encoding="utf-8"))
    candidates = [dict(row) for row in square.get("candidates", [])]
    support_by_key = {
        (int(row["prime"]), int(row["R"])): dict(row)
        for row in support.get("records", [])
        if row.get("within_radius_cap")
    }
    profile_by_key = {
        (int(row["prime"]), int(row["R"])): dict(row)
        for row in profile.get("records", [])
    }
    if len(candidates) != EXPECTED_COUNT:
        raise AssertionError("the square-terminal candidate count changed")
    if len(support_by_key) != EXPECTED_COUNT or len(profile_by_key) != EXPECTED_COUNT:
        raise AssertionError("the aligned support/profile inputs are incomplete")

    class_counts: Counter[str] = Counter()
    layer_counts: Counter[str] = Counter()
    radius_counts: Counter[int] = Counter()
    rank_class_counts: Counter[str] = Counter()
    records: list[dict[str, object]] = []
    for candidate in sorted(
        candidates,
        key=lambda row: (int(row["prime"]), int(row["R"]), int(row["source"]), int(row["E"])),
    ):
        key = (int(candidate["prime"]), int(candidate["R"]))
        overflow_record = support_by_key[key]
        profile_record = profile_by_key[key]
        canonical = {int(value) for value in profile_record["full_support_primes"]}
        overflow = {int(value) for value in overflow_record["overflow_support"]}
        intersection = canonical & overflow
        if overflow <= canonical:
            category = "canonical_only"
        elif intersection:
            category = "mixed"
        else:
            category = "outside_only"
        class_counts[category] += 1
        radius = int(overflow_record["witness_radius"])
        radius_counts[radius] += 1
        rank = int(profile_record["full_support_rank_with_two"])
        rank_class_counts[f"{rank}:{category}"] += 1
        for prime in overflow:
            layer_counts["canonical" if prime in canonical else "outside"] += 1
        records.append(
            {
                "prime": key[0],
                "R": key[1],
                "witness_radius": radius,
                "canonical_support": sorted(canonical),
                "overflow_support": sorted(overflow),
                "intersection": sorted(intersection),
                "category": category,
                "full_support_rank_with_two": rank,
                "witness_exponents": list(overflow_record["witness_exponents"]),
                "factorization": list(overflow_record["factorization"]),
            }
        )

    return {
        "arithmetic": (
            "For every square-terminal F state with a radius-six affine-lattice witness, "
            "compare its canonical low-rank support primes with the support of the first "
            "box-overflow witness."
        ),
        "scope_note": (
            "Finite alignment boundary only. The overflow witness is the first deterministic "
            "witness within radius six; a support mismatch does not prove target nonexistence "
            "or rule out another witness, terminal, or descent family."
        ),
        "square_input": SQUARE_INPUT.name,
        "square_input_sha256": sha256(SQUARE_INPUT),
        "support_input": SUPPORT_INPUT.name,
        "support_input_sha256": sha256(SUPPORT_INPUT),
        "profile_input": PROFILE_INPUT.name,
        "profile_input_sha256": sha256(PROFILE_INPUT),
        "record_count": len(records),
        "category_counts": dict(sorted(class_counts.items())),
        "radius_histogram": {str(key): int(value) for key, value in sorted(radius_counts.items())},
        "overflow_layer_counts": dict(sorted(layer_counts.items())),
        "rank_category_counts": dict(sorted(rank_class_counts.items())),
        "records": records,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "record_count",
                    "category_counts",
                    "radius_histogram",
                    "overflow_layer_counts",
                    "rank_category_counts",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
