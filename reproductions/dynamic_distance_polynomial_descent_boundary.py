#!/usr/bin/env python3
"""Audit polynomial even-source descents on the explicit AC escape progression.

For p(t)=N*t+1, take the dynamic external scale k=N*t/(4*c), where c is
an odd divisor of N/4. Its source is p(t)-c. This script exhausts every
fixed source shift and every polynomial divisor e(t) of M1(t)^2 that is
eventually at most M1(t), then checks the complete square-tail congruence
e(t) == -M1(t) modulo r(t).
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COEFFICIENT = 245_044_800
RESULTS = ROOT / "reproductions" / "dynamic-distance-polynomial-descent-boundary-results.json"


def positive_divisors(value: int) -> tuple[int, ...]:
    if value < 1:
        raise ValueError("value must be positive")
    divisors = [1]
    remaining = value
    trial = 2
    while trial * trial <= remaining:
        if remaining % trial == 0:
            powers = [1]
            power = 1
            while remaining % trial == 0:
                remaining //= trial
                power *= trial
                powers.append(power)
            divisors = [left * right for left in divisors for right in powers]
        trial = 3 if trial == 2 else trial + 2
    if remaining > 1:
        divisors += [divisor * remaining for divisor in divisors]
    return tuple(sorted(divisors))


def multiply_polynomials(
    left: tuple[int, int, int], right: tuple[int, int, int]
) -> tuple[int, int, int]:
    """Multiply polynomials known to have total degree at most two."""
    return (
        left[0] * right[0],
        left[0] * right[1] + left[1] * right[0],
        left[0] * right[2] + left[1] * right[1] + left[2] * right[0],
    )


def polynomial_power(
    polynomial: tuple[int, int], exponent: int
) -> tuple[int, int, int]:
    result = (1, 0, 0)
    for _ in range(exponent):
        result = multiply_polynomials(
            result, (polynomial[0], polynomial[1], 0)
        )
    return result


def polynomial_degree(polynomial: tuple[int, int, int]) -> int:
    if polynomial[2]:
        return 2
    if polynomial[1]:
        return 1
    return 0


def eventually_at_most(
    candidate: tuple[int, int, int], bound: tuple[int, int, int]
) -> bool:
    candidate_degree = polynomial_degree(candidate)
    bound_degree = polynomial_degree(bound)
    return candidate_degree < bound_degree or (
        candidate_degree == bound_degree
        and candidate[candidate_degree] <= bound[bound_degree]
    )


def run_audit(coefficient: int = COEFFICIENT) -> dict[str, object]:
    if coefficient <= 0 or coefficient % 24:
        raise ValueError("coefficient must be a positive multiple of 24")
    base = coefficient // 4
    divisor_cache: dict[int, tuple[int, ...]] = {}
    state_count = 0
    candidate_count = 0
    hits: list[dict[str, object]] = []
    for distance in positive_divisors(base):
        if distance % 2 == 0:
            continue
        for shift in positive_divisors(math.gcd(coefficient, distance - 1)):
            source_coefficient = coefficient // shift
            source_constant = (1 - distance) // shift
            if (
                source_coefficient % distance
                or (source_constant - 1) % distance
            ):
                continue
            r_coefficient = source_coefficient // distance
            r_constant = (source_constant - 1) // distance
            if (
                shift * r_coefficient % 4
                or (shift * r_constant + 1) % 4
            ):
                continue
            k_coefficient = shift * r_coefficient // 4
            k_constant = (shift * r_constant + 1) // 4
            state_count += 1
            s_content = math.gcd(source_coefficient, abs(source_constant))
            k_content = math.gcd(k_coefficient, abs(k_constant))
            s_primitive = (
                source_constant // s_content,
                source_coefficient // s_content,
            )
            k_primitive = (
                k_constant // k_content,
                k_coefficient // k_content,
            )
            content = s_content * k_content
            if content * content not in divisor_cache:
                divisor_cache[content * content] = positive_divisors(content * content)
            m1 = multiply_polynomials(
                (source_constant, source_coefficient, 0),
                (k_constant, k_coefficient, 0),
            )
            for constant_factor in divisor_cache[content * content]:
                for s_exponent in range(3):
                    for k_exponent in range(3):
                        if s_exponent + k_exponent > 2:
                            continue
                        s_power = polynomial_power(s_primitive, s_exponent)
                        k_power = polynomial_power(k_primitive, k_exponent)
                        product = multiply_polynomials(s_power, k_power)
                        factor = (
                            constant_factor * product[0],
                            constant_factor * product[1],
                            constant_factor * product[2],
                        )
                        if not eventually_at_most(factor, m1):
                            continue
                        candidate_count += 1
                        total = tuple(
                            left + right for left, right in zip(m1, factor)
                        )
                        remainder_numerator = (
                            total[2] * r_constant * r_constant
                            - total[1] * r_constant * r_coefficient
                            + total[0] * r_coefficient * r_coefficient
                        )
                        if remainder_numerator == 0:
                            hits.append(
                                {
                                    "distance": distance,
                                    "shift": shift,
                                    "factor": factor,
                                }
                            )
    return {
        "arithmetic": (
            "complete integer-polynomial divisor enumeration for dynamic "
            "even-source square tails on the explicit escape progression"
        ),
        "scope_note": (
            "This excludes fixed-shift polynomial square-tail factors in this "
            "dynamic-distance family, not nonpolynomial factors or all descents."
        ),
        "progression": {"coefficient": coefficient, "constant": 1},
        "dynamic_distance_state_count": state_count,
        "eventual_square_tail_factor_count": candidate_count,
        "polynomial_descent_hits": hits,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coefficient", type=int, default=COEFFICIENT)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.coefficient)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
