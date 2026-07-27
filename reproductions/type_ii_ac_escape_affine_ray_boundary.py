#!/usr/bin/env python3
"""Exhaust uniform affine AC Type II factors on the depth-four escape ray.

For p(t)=N*t+1, a nonconstant affine divisor h(t) of
p(t)+4*A^2*C must have a constant complementary factor L:

    p(t)+4*A^2*C = L*h(t).

If h(t) is a Type II raw-ray factor, then h(t) is -1 modulo 4*A*C
coefficientwise. Thus L divides both N and 1+4*A^2*C, while
4*A*C divides N/L. The latter makes the apparent unbounded AC search finite:
4*A*C divides N. This script enumerates every resulting factorization.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ESCAPE_COEFFICIENT = 245_044_800
RESULTS = ROOT / "reproductions" / "type-ii-ac-escape-affine-ray-boundary-results.json"


def positive_divisors(value: int) -> tuple[int, ...]:
    """Return all positive divisors of a positive integer."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: list[tuple[int, int]] = []
    trial = 2
    remaining = value
    while trial * trial <= remaining:
        if remaining % trial == 0:
            exponent = 0
            while remaining % trial == 0:
                remaining //= trial
                exponent += 1
            factors.append((trial, exponent))
        trial = 3 if trial == 2 else trial + 2
    if remaining > 1:
        factors.append((remaining, 1))
    divisors = [1]
    for prime, exponent in factors:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return tuple(sorted(divisors))


def run_affine_ray_audit(coefficient: int = ESCAPE_COEFFICIENT) -> dict[str, object]:
    """Enumerate every uniform affine raw AC ray on p(t)=coefficient*t+1."""
    if coefficient <= 0 or coefficient % 24:
        raise ValueError("coefficient must be a positive multiple of 24")
    coefficient_divisors = positive_divisors(coefficient)
    candidate_ac_pairs = 0
    fixed_divisor_cases = 0
    hits: list[dict[str, int]] = []
    for fixed_factor in coefficient_divisors:
        quotient_coefficient = coefficient // fixed_factor
        for modulus in positive_divisors(quotient_coefficient):
            if modulus % 4:
                continue
            ac_product = modulus // 4
            for a in positive_divisors(ac_product):
                c = ac_product // a
                candidate_ac_pairs += 1
                shifted_constant = 1 + 4 * a * a * c
                if shifted_constant % fixed_factor:
                    continue
                fixed_divisor_cases += 1
                factor_constant = shifted_constant // fixed_factor
                if factor_constant % modulus != modulus - 1:
                    continue
                hits.append(
                    {
                        "a": a,
                        "c": c,
                        "fixed_factor": fixed_factor,
                        "modulus": modulus,
                        "factor_coefficient": quotient_coefficient,
                        "factor_constant": factor_constant,
                    }
                )
    return {
        "arithmetic": (
            "complete divisor enumeration for constant complementary factors "
            "of affine divisors on the explicit depth-four escape progression"
        ),
        "scope_note": (
            "This excludes uniform affine Type II raw-ray factors on one "
            "progression. It does not exclude parameter-dependent nonlinear "
            "factors, Type I certificates, or strict descents."
        ),
        "progression": {"coefficient": coefficient, "constant": 1},
        "coefficient_divisor_count": len(coefficient_divisors),
        "candidate_ac_pair_count": candidate_ac_pairs,
        "fixed_divisor_case_count": fixed_divisor_cases,
        "uniform_affine_raw_ray_hits": hits,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coefficient", type=int, default=ESCAPE_COEFFICIENT)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_affine_ray_audit(args.coefficient)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
