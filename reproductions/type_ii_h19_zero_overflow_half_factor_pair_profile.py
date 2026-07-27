#!/usr/bin/env python3
"""Recast zero-overflow even-source tails as cross-half-factor residue hits."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json"
DEFAULT_OVERFLOW = ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-zero-overflow-half-factor-pair-profile-1b-results.json"


def split_negative_one_divisor(a: int, b: int, r: int) -> tuple[int, int] | None:
    """Find alpha|a, beta|b with alpha*beta=-1 modulo r, if one exists."""
    beta_by_residue: dict[int, int] = {}
    for beta in sympy.divisors(b):
        beta = int(beta)
        beta_by_residue.setdefault(beta % r, beta)
    for alpha in sympy.divisors(a):
        alpha = int(alpha)
        beta = beta_by_residue.get((-pow(alpha, -1, r)) % r)
        if beta is not None:
            if a % alpha or b % beta or (alpha * beta) % r != r - 1:
                raise AssertionError("cross-half-factor residue witness failed")
            return alpha, beta
    return None


def has_negative_one_divisor(value: int, r: int) -> bool:
    """Return whether one side alone already supplies the target residue."""
    return any(int(divisor) % r == r - 1 for divisor in sympy.divisors(value))


def half_factors(prime: int, r: int, distance: int, divisor: int) -> tuple[int, int]:
    """Return A=(c*r+1)/2 and B=(d*r+1)/2 for one compatible even-source ray."""
    a = (distance * r + 1) // 2
    b = (divisor * r + 1) // 2
    m1 = (r * prime + 1) // 4
    if (
        distance % 2 != 1
        or divisor % 4 != 1
        or r % 8 != 7
        or prime != divisor + distance + distance * divisor * r
        or a * b != m1
        or a % r != (r + 1) // 2
        or b % r != (r + 1) // 2
        or b % 2 != 0
    ):
        raise AssertionError("invalid compatible even-source half-factor pair")
    return a, b


def run_audit(selector_payload: dict[str, object], overflow_payload: dict[str, object]) -> dict[str, object]:
    """Check the cross-factor criterion against each stored first-r overflow state."""
    overflow = {int(record["prime"]): record for record in overflow_payload["records"]}
    records = []
    for record in selector_payload["records"]:
        hit = record["first_hit"]
        if hit is None:
            continue
        prime = int(record["prime"])
        r, distance, divisor = int(hit["r"]), int(hit["distance"]), int(hit["d"])
        a, b = half_factors(prime, r, distance, divisor)
        witness = split_negative_one_divisor(a, b, r)
        left_hit = has_negative_one_divisor(a, r)
        right_hit = has_negative_one_divisor(b, r)
        expected = int(overflow[prime]["minimum_overflow"]) == 1
        if (witness is not None) != expected:
            raise AssertionError("cross-half-factor test disagrees with zero-overflow profile")
        if (left_hit or right_hit) and witness is None:
            raise AssertionError("one-side target hit failed to give a cross witness")
        if witness is None:
            zero_overflow_kind = "none"
        elif left_hit and right_hit:
            zero_overflow_kind = "both_sides"
        elif left_hit:
            zero_overflow_kind = "left_only"
        elif right_hit:
            zero_overflow_kind = "right_only"
        else:
            zero_overflow_kind = "cross_essential"
        row = {
            "prime": prime,
            "r": r,
            "distance": distance,
            "d": divisor,
            "left_half_factor": a,
            "right_half_factor": b,
            "zero_overflow": witness is not None,
            "left_half_factor_hits_target": left_hit,
            "right_half_factor_hits_target": right_hit,
            "zero_overflow_kind": zero_overflow_kind,
        }
        if witness is not None:
            alpha, beta = witness
            row.update(
                {
                    "left_divisor": alpha,
                    "right_divisor": beta,
                    "ordinary_divisor": alpha * beta,
                    "tail_factor": a * b // (alpha * beta),
                }
            )
        records.append(row)
    kind_histogram = {
        kind: sum(record["zero_overflow_kind"] == kind for record in records)
        for kind in ("left_only", "right_only", "both_sides", "cross_essential", "none")
    }
    return {
        "arithmetic": (
            "exact factorization of the compatible half factors A=(c*r+1)/2 and "
            "B=(d*r+1)/2, followed by the cross-divisor residue test alpha*beta=-1 modulo r"
        ),
        "scope_note": (
            "An exact reparameterization of stored first-r zero-overflow states. "
            "It does not prove that a compatible factor pair exists generally."
        ),
        "prime_limit": selector_payload["prime_limit"],
        "first_r_state_count": len(records),
        "cross_half_factor_zero_overflow_count": sum(record["zero_overflow"] for record in records),
        "cross_half_factor_high_overflow_count": sum(not record["zero_overflow"] for record in records),
        "zero_overflow_kind_histogram": kind_histogram,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--overflow", type=Path, default=DEFAULT_OVERFLOW)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.input.read_text(encoding="utf-8")),
        json.loads(args.overflow.read_text(encoding="utf-8")),
    )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
