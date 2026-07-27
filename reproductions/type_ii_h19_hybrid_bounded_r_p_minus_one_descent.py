#!/usr/bin/env python3
"""Close the stored H19 residuals by bounded-r or p-minus-one strict lifts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOUNDARY_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json"
P_MINUS_ONE_INPUT = ROOT / "reproductions" / "type-ii-h19-p-minus-one-scaled-source-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-hybrid-bounded-r-p-minus-one-descent-1b-results.json"
R_CAP = 9_999


def stage_at_cap(payload: dict[str, object], r_cap: int) -> dict[str, object]:
    """Return one stored bounded-r selector stage."""
    for stage in payload["stages"]:
        if int(stage["r_cap"]) == r_cap:
            return stage
    raise ValueError(f"missing r={r_cap} selector stage")


def run_audit(
    boundary_payload: dict[str, object], p_minus_one_payload: dict[str, object]
) -> dict[str, object]:
    """Verify that the two finite strict-lift families partition H19 residuals."""
    stage = stage_at_cap(boundary_payload, R_CAP)
    r_misses = [int(prime) for prime in stage["uncovered_primes"]]
    p_minus_one_records = {
        int(record["prime"]): record for record in p_minus_one_payload["records"]
    }
    if set(r_misses) != set(p_minus_one_records):
        raise AssertionError("p-minus-one input does not match the bounded-r residual")
    p_minus_one_misses = [
        prime
        for prime in r_misses
        if p_minus_one_records[prime]["first_witness"] is None
    ]
    if p_minus_one_payload["prime_limit"] != boundary_payload["prime_limit"]:
        raise AssertionError("input prime limits disagree")
    return {
        "arithmetic": (
            "set-exact composition of the r<=9999 compatible-ray audit and "
            "the exact rational plus Type I certified p-minus-one lifts"
        ),
        "scope_note": (
            "A finite H19 closure over stored p<=10^9 residuals. It does not "
            "prove a universal r bound or p-minus-one selector."
        ),
        "prime_limit": boundary_payload["prime_limit"],
        "r_cap": R_CAP,
        "h19_residual_count": boundary_payload["h19_residual_count"],
        "bounded_r_strict_lift_count": int(stage["covered_count"]),
        "p_minus_one_strict_lift_count": len(r_misses) - len(p_minus_one_misses),
        "unclosed_primes": p_minus_one_misses,
        "p_minus_one_records": [
            p_minus_one_records[prime] for prime in sorted(r_misses)
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boundary", type=Path, default=BOUNDARY_INPUT)
    parser.add_argument("--p-minus-one", type=Path, default=P_MINUS_ONE_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    boundary_payload = json.loads(args.boundary.read_text(encoding="utf-8"))
    p_minus_one_payload = json.loads(args.p_minus_one.read_text(encoding="utf-8"))
    result = run_audit(boundary_payload, p_minus_one_payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
