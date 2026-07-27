#!/usr/bin/env python3
"""Audit common local character conductors across bounded-r subgroup failures."""

from __future__ import annotations

import argparse
import json
import math
from functools import reduce
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-tail-obstruction-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-character-conductor-boundary-1b-results.json"


def common_modulus(values: list[int]) -> int:
    if not values:
        raise ValueError("at least one modulus is required")
    return reduce(math.gcd, values)


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Measure the common divisor of every prime's subgroup-character moduli."""
    records = []
    for row in payload["records"]:
        moduli = [
            int(state["r"])
            for state in row["states"]
            if state["classification"] == "subgroup-character"
        ]
        if not moduli:
            raise AssertionError("tail residual unexpectedly lacks subgroup-character states")
        records.append(
            {
                "prime": int(row["prime"]),
                "subgroup_character_state_count": len(moduli),
                "common_state_modulus": common_modulus(moduli),
                "state_moduli": moduli,
            }
        )
    return {
        "arithmetic": (
            "exact gcd of all r moduli carrying a subgroup-character square-tail "
            "obstruction for each fixed residual prime"
        ),
        "scope_note": (
            "This only rules out a common nontrivial conductor required to divide "
            "every local state modulus. It does not rule out cross-modulus or "
            "nonlocal character arguments."
        ),
        "prime_limit": payload["prime_limit"],
        "r_cap": payload["r_cap"],
        "residual_prime_count": len(records),
        "all_common_state_moduli_are_one": all(
            record["common_state_modulus"] == 1 for record in records
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
