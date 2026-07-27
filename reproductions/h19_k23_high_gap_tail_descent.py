#!/usr/bin/env python3
"""Close the high-gap H19-k23 shared-selector records by ordinary tail descent.

The shared selector's least direct Type II gap need not be a p-1 indexed
two-tail gap.  This audit selects the high-gap rows from its checked artifact
and exhausts every 4-divisible divisor of p-1 for an ordinary Type II
two-tail descent.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-shared-selector-audit-16384.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-high-gap-tail-descent.json"
ALTERNATIVE_TAIL = ROOT / "reproductions" / "type_ii_collision_alternative_tail_descent.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


alternative_tail = load_module("h19_k23_high_gap_alternative_tail", ALTERNATIVE_TAIL)


def run_audit(payload: dict[str, object], minimum_shared_gap: int = 43) -> dict[str, object]:
    """Exhaust p-1 indexed tail gaps for every selected high-gap record."""
    if minimum_shared_gap < 3 or minimum_shared_gap % 4 != 3:
        raise ValueError("minimum_shared_gap must be at least 3 and 3 modulo 4")
    selected = [
        record
        for record in payload["records"]
        if int(record["first_witness"]["gap"]) >= minimum_shared_gap
    ]
    records = []
    for record in selected:
        prime = int(record["prime"])
        witness, candidate_gap_count = alternative_tail.first_alternative_tail_descent(prime)
        records.append(
            {
                "prime": prime,
                "shared_selector_gap": int(record["first_witness"]["gap"]),
                "candidate_tail_gap_count": candidate_gap_count,
                "ordinary_tail_witness": witness,
            }
        )
    return {
        "arithmetic": (
            "complete factorization of p-1, exhaustive enumeration of its "
            "4-divisible divisor gaps, complete Type II square-divisor checks, "
            "and exact Fraction verification of the strict source solution"
        ),
        "scope_note": (
            "This closes only the selected finite high-gap shared-selector rows. "
            "It does not establish ordinary tail descent for every H19-k23 row."
        ),
        "input_parameter_limit_exclusive": payload["parameter_limit_exclusive"],
        "minimum_shared_gap": minimum_shared_gap,
        "selected_record_count": len(records),
        "ordinary_tail_descent_count": sum(
            record["ordinary_tail_witness"] is not None for record in records
        ),
        "ordinary_tail_descent_misses": [
            record["prime"] for record in records if record["ordinary_tail_witness"] is None
        ],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--minimum-shared-gap", type=int, default=43)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload, args.minimum_shared_gap)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
