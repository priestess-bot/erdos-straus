#!/usr/bin/env python3
"""Verify that higher M powers cannot extend the same even-source tail ansatz."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-finite-product-exponent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-tail-exponent-rigidity-1b-results.json"


def m_from_factorization(raw: dict[str, int]) -> int:
    return math_prod(int(prime) ** int(exponent) for prime, exponent in raw.items())


def math_prod(values):
    result = 1
    for value in values:
        result *= value
    return result


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Check every first higher-power target divisor against the original v integrality."""
    records = []
    candidate_count = 0
    candidate_at_most_m_count = 0
    integral_v_count = 0
    for row in payload["records"]:
        m = m_from_factorization(row["m_factorization"])
        r = int(row["r"])
        power = int(row["first_cover_power_through_cap"])
        target = (-m) % r
        if sympy.gcd(r, m) != 1:
            raise AssertionError("tail state lost r-M coprimality")
        state_candidates = []
        for divisor in sympy.divisors(m**power):
            if divisor % r != target:
                continue
            u = (m + divisor) // r
            if r * u != m + divisor:
                raise AssertionError("target divisor does not reconstruct an integral u")
            square_tail = m * m % divisor == 0
            integral_v = (m * u) % divisor == 0
            if integral_v != square_tail:
                raise AssertionError("v integrality and the square-tail condition diverged")
            candidate_count += 1
            candidate_at_most_m_count += divisor <= m
            integral_v_count += integral_v
            state_candidates.append(
                {
                    "e": divisor,
                    "e_at_most_m": divisor <= m,
                    "e_divides_m_squared": square_tail,
                    "v_is_integral": integral_v,
                }
            )
        if not state_candidates:
            raise AssertionError("stored first cover power has no target divisor")
        records.append(
            {
                "prime": int(row["prime"]),
                "r": r,
                "power": power,
                "target_candidate_count": len(state_candidates),
                "candidates": state_candidates,
            }
        )
    return {
        "arithmetic": (
            "exact enumeration of each first higher-power target divisor e, with "
            "direct checks of u=(M+e)/r and v=M*u/e integrality"
        ),
        "scope_note": (
            "This is rigidity of the existing even-source tail ansatz. It does "
            "not rule out a different source, a different tail formula, or a "
            "multi-step marked lift."
        ),
        "prime_limit": payload["prime_limit"],
        "r_cap": payload["r_cap"],
        "state_count": len(records),
        "target_candidate_count": candidate_count,
        "target_candidate_at_most_m_count": candidate_at_most_m_count,
        "integral_v_count": integral_v_count,
        "all_higher_power_candidates_fail_original_tail": integral_v_count == 0,
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
