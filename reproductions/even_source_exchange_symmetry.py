#!/usr/bin/env python3
"""Verify the distance--source-divisor exchange symmetry in an even-source fan."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-tail-profile-640775689-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-exchange-symmetry-640775689-results.json"
)


def exchange_state(distance: int, divisor: int, r: int) -> dict[str, int]:
    """Return the two source parameterizations with their shared target state."""
    if min(distance, divisor, r) <= 0:
        raise ValueError("parameters must be positive")
    if distance % 4 != 1 or divisor % 4 != 1 or r % 4 != 3:
        raise ValueError("require distance, divisor = 1 mod 4 and r = 3 mod 4")
    prime = divisor + distance + divisor * distance * r
    first_k = (divisor * r + 1) // 4
    second_k = (distance * r + 1) // 4
    first_s = 1 + distance * r
    second_s = 1 + divisor * r
    first_m1 = first_k * first_s
    second_m1 = second_k * second_s
    if first_m1 != second_m1:
        raise AssertionError("exchange did not preserve M1")
    if prime - distance != divisor * first_s or prime - divisor != distance * second_s:
        raise AssertionError("exchange source factorizations failed")
    return {
        "prime": prime,
        "distance": distance,
        "divisor": divisor,
        "r": r,
        "first_k": first_k,
        "first_s": first_s,
        "second_k": second_k,
        "second_s": second_s,
        "shared_m1": first_m1,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Check every in-window exchange partner recorded by a tail-state profile."""
    rays = payload["rays"]
    index = {
        (int(row["distance"]), int(row["d"]), int(row["r"])): row
        for row in rays
    }
    eligible = [
        row
        for row in rays
        if int(row["distance"]) % 4 == 1 and int(row["d"]) % 4 == 1
    ]
    directed_pairs: list[dict[str, int]] = []
    for row in eligible:
        distance, divisor, r = (
            int(row["distance"]),
            int(row["d"]),
            int(row["r"]),
        )
        state = exchange_state(distance, divisor, r)
        if state["prime"] != int(payload["prime"]) or state["shared_m1"] != int(row["m1"]):
            raise AssertionError("profile ray disagrees with exchange state")
        partner = index.get((divisor, distance, r))
        if partner is None:
            continue
        if int(partner["m1"]) != state["shared_m1"]:
            raise AssertionError("in-window exchange partner changed M1")
        if int(partner["target_residue_factor_count"]) != int(
            row["target_residue_factor_count"]
        ):
            raise AssertionError("in-window exchange partner changed tail condition")
        directed_pairs.append(
            {
                "distance": distance,
                "divisor": divisor,
                "r": r,
                "shared_m1": state["shared_m1"],
            }
        )
    orbits = {
        (min(row["distance"], row["divisor"]), max(row["distance"], row["divisor"]), row["r"])
        for row in directed_pairs
    }
    return {
        "arithmetic": (
            "exact algebraic exchange of compatible even-source parameters, "
            "cross-checked against the stored exhaustive tail profile"
        ),
        "scope_note": (
            "The exchange preserves a tail condition but does not force any "
            "square-tail divisor into its target residue class."
        ),
        "prime": payload["prime"],
        "eligible_ray_count": len(eligible),
        "in_window_directed_partner_count": len(directed_pairs),
        "in_window_exchange_orbit_count": len(orbits),
        "unpaired_eligible_ray_count": len(eligible) - len(directed_pairs),
        "directed_partners": directed_pairs,
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
