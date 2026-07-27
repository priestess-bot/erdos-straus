#!/usr/bin/env python3
"""Compress fourth-pressure-point even-source rays by their shared r-tail state."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TAIL_INPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-tail-profile-640775689-results.json"
)
DEFAULT_SUBGROUP_INPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-subgroup-profile-640775689-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-r-state-profile-640775689-results.json"
)


def run_profile(
    tail_payload: dict[str, object], subgroup_payload: dict[str, object]
) -> dict[str, object]:
    """Merge all compatible rays with a common r and verify their tail equality."""
    classifications = {
        (int(row["distance"]), int(row["r"])): str(row["classification"])
        for row in subgroup_payload["records"]
    }
    by_r: dict[int, list[dict[str, object]]] = defaultdict(list)
    for ray in tail_payload["rays"]:
        by_r[int(ray["r"])].append(ray)
    records: list[dict[str, object]] = []
    for r, rays in sorted(by_r.items()):
        m1_values = {int(ray["m1"]) for ray in rays}
        hit_counts = {int(ray["target_residue_factor_count"]) for ray in rays}
        state_classes = {
            classifications[(int(ray["distance"]), r)] for ray in rays
        }
        if len(m1_values) != 1 or len(hit_counts) != 1 or len(state_classes) != 1:
            raise AssertionError("common r did not preserve its square-tail state")
        m1 = next(iter(m1_values))
        if 4 * m1 != r * int(tail_payload["prime"]) + 1:
            raise AssertionError("r state did not reconstruct M1")
        records.append(
            {
                "r": r,
                "m1": m1,
                "distances": sorted(int(ray["distance"]) for ray in rays),
                "ray_multiplicity": len(rays),
                "tail_residue_factor_count": next(iter(hit_counts)),
                "classification": next(iter(state_classes)),
            }
        )
    multiplicities = Counter(record["ray_multiplicity"] for record in records)
    classifications_by_state = Counter(record["classification"] for record in records)
    return {
        "arithmetic": (
            "exact identity 4*M1=r*p+1 and cross-checks of all stored "
            "square-tail factor counts and subgroup classifications"
        ),
        "scope_note": (
            "This is a state compression for a fixed p. It does not bound the "
            "number or size of r states for general p."
        ),
        "prime": tail_payload["prime"],
        "compatible_ray_count": len(tail_payload["rays"]),
        "r_state_count": len(records),
        "ray_multiplicity_histogram": {
            str(multiplicity): count
            for multiplicity, count in sorted(multiplicities.items())
        },
        "classification_by_r_state": dict(sorted(classifications_by_state.items())),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail-input", type=Path, default=DEFAULT_TAIL_INPUT)
    parser.add_argument("--subgroup-input", type=Path, default=DEFAULT_SUBGROUP_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    tail_payload = json.loads(args.tail_input.read_text(encoding="utf-8"))
    subgroup_payload = json.loads(args.subgroup_input.read_text(encoding="utf-8"))
    result = run_profile(tail_payload, subgroup_payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
