#!/usr/bin/env python3
"""Profile minimum Type I overflow at every stored first r-tail hit."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
OVERFLOW_PROFILE = ROOT / "reproductions" / "type_ii_h19_pressure_even_source_overflow_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


overflow_profile = load_module("h19_bounded_r_overflow_tail_profile", OVERFLOW_PROFILE)


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Measure the best tail-induced overflow for each stored first r hit."""
    records = []
    for record in payload["records"]:
        prime = int(record["prime"])
        first_hit = record["first_hit"]
        if first_hit is None:
            continue
        r = int(first_hit["r"])
        m1 = (r * prime + 1) // 4
        tails = overflow_profile.tail_rows(prime, r, m1)
        if len(tails) != int(first_hit["tail_residue_factor_count"]):
            raise AssertionError("first-hit tail count changed under overflow normalization")
        minimum = int(tails[0]["overflow"])
        records.append(
            {
                "prime": prime,
                "r": r,
                "distance": int(first_hit["distance"]),
                "tail_factor_count": len(tails),
                "minimum_overflow": minimum,
                "minimum_overflow_tail_count": sum(int(tail["overflow"]) == minimum for tail in tails),
            }
        )
    histogram = Counter(int(record["minimum_overflow"]) for record in records)
    uncovered = [int(record["prime"]) for record in payload["records"] if record["first_hit"] is None]
    return {
        "arithmetic": (
            "reuses each stored first r=7 mod 8 tail hit, exhausts its M1-squared "
            "residue factors, and normalizes every factor to the exact Type I overflow B"
        ),
        "scope_note": (
            "A finite profile through the r cap used by the input audit. It does not "
            "prove a variable-r or bounded-overflow selector beyond that stored range."
        ),
        "prime_limit": payload["prime_limit"],
        "r_caps": payload["r_caps"],
        "h19_residual_count": int(payload["h19_residual_count"]),
        "first_hit_count": len(records),
        "uncovered_count": len(uncovered),
        "uncovered_primes": uncovered,
        "minimum_overflow_histogram": {str(key): value for key, value in sorted(histogram.items())},
        "zero_overflow_count": histogram[1],
        "positive_overflow_count": len(records) - histogram[1],
        "maximum_minimum_overflow": max(histogram, default=None),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
