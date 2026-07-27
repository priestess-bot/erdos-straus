#!/usr/bin/env python3
"""Test which small odd distances resolve the quadratic H19 descent misses."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGETED_SCRIPT = ROOT / "reproductions" / "type_ii_h19_targeted_quadratic_descent.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-300m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-even-source-distance-boundary-300m-results.json"
DEFAULT_DISTANCES = (1, 3, 5, 7)


def load_targeted_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_h19_even_source_distance_targeted", TARGETED_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_h19_targeted_quadratic_descent.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


targeted = load_targeted_script()


def run_audit(payload: dict[str, object], distances: tuple[int, ...]) -> dict[str, object]:
    """Evaluate each requested complete even-source fan on every quadratic miss."""
    if not distances or any(distance <= 0 or distance % 2 == 0 for distance in distances):
        raise ValueError("distances must be positive odd integers")
    misses = [
        int(record["prime"])
        for record in payload["records"]
        if record["quadratic_factor_external_source_descent"] is None
    ]
    spf = targeted.TrialSmallestFactors(max(misses))
    records: list[dict[str, object]] = []
    for prime in misses:
        hits: list[dict[str, int]] = []
        for distance in distances:
            witness = targeted.short_certificate.even_source_distance_descent_witness(
                prime, distance, spf
            )
            if witness is None:
                continue
            if witness.source_denominator != prime - distance:
                raise AssertionError("distance did not reconstruct the source")
            hits.append(
                {
                    "distance": distance,
                    "gap": witness.certificate.gap,
                    "k": witness.k,
                    "factor": witness.factor,
                }
            )
        records.append({"prime": prime, "hits": hits})
    hit_counts = {
        str(distance): sum(
            any(hit["distance"] == distance for hit in record["hits"])
            for record in records
        )
        for distance in distances
    }
    return {
        "arithmetic": (
            "exact trial-prime factorization in every requested complete "
            "odd-distance even-source fan"
        ),
        "scope_note": (
            "A finite irredundancy audit of selected distances. It does not "
            "assert a universal distance bound."
        ),
        "prime_limit": payload["prime_limit"],
        "quadratic_descent_miss_count": len(misses),
        "distances": list(distances),
        "distance_hit_counts": hit_counts,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload, DEFAULT_DISTANCES)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
