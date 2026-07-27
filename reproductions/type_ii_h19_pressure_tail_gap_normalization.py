#!/usr/bin/env python3
"""Normalize the bounded-r pressure tails to their Type I gaps."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-hybrid-small-r-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-pressure-tail-gap-normalization-1b-results.json"


def normalize_record(record: dict[str, object]) -> dict[str, int]:
    """Recover e, g, and x from one certified compatible r-ray witness."""
    prime = int(record["prime"])
    r = int(record["r"])
    d = int(record["d"])
    witness = record["witness"]
    factor = int(witness["factor"])
    certificate = witness["certificate"]
    if factor % d:
        raise AssertionError("stored source factor is not d times a tail factor")
    tail_factor = factor // d
    m1 = (r * prime + 1) // 4
    if m1 % r != pow(4, -1, r):
        raise AssertionError("M1 did not have the universal quarter residue")
    if tail_factor % r != (-m1) % r:
        raise AssertionError("tail factor missed the required square-tail residue")
    numerator = 4 * tail_factor + 1
    if numerator % r:
        raise AssertionError("tail residue did not produce an integral Type I gap")
    gap = numerator // r
    x_numerator = m1 + tail_factor
    if x_numerator % r:
        raise AssertionError("tail factor did not produce an integral Type I x")
    x = x_numerator // r
    if gap != int(certificate["gap"]) or x != int(certificate["x"]):
        raise AssertionError("tail-to-gap normalization disagrees with certificate")
    if 4 * x != prime + gap:
        raise AssertionError("normalized x is not the Type I first denominator")
    inverse_tail_numerator = r * gap - 1
    if inverse_tail_numerator % 4 or inverse_tail_numerator // 4 != tail_factor:
        raise AssertionError("gap did not invert to the stored tail factor")
    return {
        "prime": prime,
        "r": r,
        "d": d,
        "m1": m1,
        "tail_factor": tail_factor,
        "gap": gap,
        "x": x,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Normalize every bounded-r witness in the stored H19 pressure closure."""
    records = [normalize_record(record) for record in payload["bounded_r_records"]]
    return {
        "arithmetic": (
            "exact identities e=(r*g-1)/4 and x=(M1+e)/r=(p+g)/4 "
            "on certified bounded-r even-source witnesses"
        ),
        "scope_note": (
            "The normalization identity is algebraic; the four listed records "
            "are the finite H19 pressure-witness cross-check."
        ),
        "prime_limit": payload["prime_limit"],
        "record_count": len(records),
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
