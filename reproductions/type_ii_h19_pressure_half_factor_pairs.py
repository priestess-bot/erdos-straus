#!/usr/bin/env python3
"""Reparameterize bounded-r even-source rays by factor pairs of (r*p+1)/4."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-pressure-small-r-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-pressure-half-factor-pairs-1b-results.json"


def half_factor_pair(prime: int, r: int, distance: int, divisor: int) -> dict[str, int]:
    """Return the oriented half-factor pair attached to one compatible ray.

    For p = d + c + c*d*r, put M=(r*p+1)/4,
    A=(c*r+1)/2, and B=(d*r+1)/2.  Then M=A*B.  The factor B is
    even precisely because the stored source divisor d is 1 modulo 4.
    """
    if prime % 8 != 1:
        raise ValueError("this core parametrization requires a prime 1 modulo 8")
    if r <= 0 or r % 8 != 7:
        raise ValueError("a compatible core ray requires r to be positive and 7 modulo 8")
    if prime != divisor + distance + distance * divisor * r:
        raise ValueError("ray does not reconstruct the prime")
    if distance <= 0 or distance % 2 != 1:
        raise ValueError("distance must be positive and odd")
    if divisor <= 0 or divisor % 4 != 1:
        raise ValueError("source divisor must be positive and 1 modulo 4")

    m = (r * prime + 1) // 4
    a = (distance * r + 1) // 2
    b = (divisor * r + 1) // 2
    residue = (r + 1) // 2
    if 4 * m != r * prime + 1 or a * b != m:
        raise AssertionError("half-factor product identity failed")
    if a % r != residue or b % r != residue or b % 2 != 0:
        raise AssertionError("half-factor congruence conditions failed")
    if (2 * a - 1) // r != distance or (2 * b - 1) // r != divisor:
        raise AssertionError("half-factor recovery failed")
    return {
        "distance": distance,
        "d": divisor,
        "a": a,
        "b": b,
        "a_mod_r": a % r,
        "b_mod_r": b % r,
        "r_mod_8": r % 8,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Certify the half-factor parametrization for every selected pressure state."""
    records: list[dict[str, object]] = []
    for row in payload["records"]:
        state = row["first_small_r_tail_hit"]
        if state is None:
            raise ValueError("input must contain a selected small-r state")
        prime = int(row["prime"])
        r = int(state["r"])
        m = int(state["m1"])
        pairs = [
            half_factor_pair(prime, r, int(ray["distance"]), int(ray["d"]))
            for ray in state["compatible_rays"]
        ]
        if any(pair["a"] * pair["b"] != m for pair in pairs):
            raise AssertionError("stored M1 disagrees with a half-factor pair")
        records.append(
            {
                "prime": prime,
                "r": r,
                "m": m,
                "half_factor_residue": (r + 1) // 2,
                "square_tail_target": (-m) % r,
                "oriented_half_factor_pairs": pairs,
            }
        )
    return {
        "arithmetic": (
            "exact half-factor identities M=A*B for each stored compatible "
            "even-source ray, with A=(c*r+1)/2 and B=(d*r+1)/2"
        ),
        "scope_note": (
            "This establishes an exact reparameterization of the selected "
            "finite states. It does not prove that a suitable r or a square "
            "tail exists for every core prime."
        ),
        "prime_limit": payload["prime_limit"],
        "pressure_state_count": len(records),
        "all_selected_r_are_7_mod_8": all(record["r"] % 8 == 7 for record in records),
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
