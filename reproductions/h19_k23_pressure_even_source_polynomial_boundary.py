#!/usr/bin/env python3
"""Audit uniform polynomial tails in the complete distance-one even-source fan."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-even-source-polynomial-boundary-2097152.json"
TARGET_SEED = 748_375_048_866_405_601

Polynomial = tuple[int, int, int]


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    return (
        left[0] * right[0],
        left[0] * right[1] + left[1] * right[0],
        left[0] * right[2] + left[1] * right[1] + left[2] * right[0],
    )


def power(base: Polynomial, exponent: int) -> Polynomial:
    result = (1, 0, 0)
    for _ in range(exponent):
        result = multiply(result, base)
    return result


def degree(value: Polynomial) -> int:
    if value[2]:
        return 2
    if value[1]:
        return 1
    return 0


def eventually_at_most(candidate: Polynomial, bound: Polynomial) -> bool:
    return degree(candidate) < degree(bound) or (
        degree(candidate) == degree(bound)
        and candidate[degree(candidate)] <= bound[degree(bound)]
    )


def divisible_by(value: Polynomial, modulus: Polynomial) -> bool:
    """Check divisibility by a constant or a primitive linear polynomial."""
    constant, coefficient = modulus[0], modulus[1]
    if coefficient == 0:
        return all(entry % constant == 0 for entry in value)
    numerator = (
        value[2] * constant * constant
        - value[1] * constant * coefficient
        + value[0] * coefficient * coefficient
    )
    return numerator == 0


def divide_content(value: Polynomial) -> tuple[int, Polynomial]:
    content = math.gcd(abs(value[0]), abs(value[1]))
    if content == 0:
        raise AssertionError("zero source factor")
    return content, (value[0] // content, value[1] // content, 0)


def state_polynomials(base: int, h: Polynomial, divisor: int, uses_h: bool) -> tuple[Polynomial, Polynomial, Polynomial]:
    """Return (s, k, r=s-1) for shift d or d*h in the c=1 fan."""
    if uses_h:
        s = (base // divisor, 0, 0)
        r = (s[0] - 1, 0, 0)
        k = (
            (divisor * r[0] * h[0] + 1) // 4,
            divisor * r[0] * h[1] // 4,
            0,
        )
    else:
        s = (base // divisor * h[0], base // divisor * h[1], 0)
        r = (s[0] - 1, s[1], 0)
        k = (
            (base * h[0] - divisor + 1) // 4,
            base * h[1] // 4,
            0,
        )
    if any(value % 1 for value in (*s, *r, *k)):
        raise AssertionError("nonintegral even-source polynomial state")
    return s, k, r


def audit_state(base: int, h: Polynomial, divisor: int, uses_h: bool) -> dict[str, object]:
    """Enumerate every eventual polynomial square divisor at one c=1 ray."""
    s, k, r = state_polynomials(base, h, divisor, uses_h)
    m1 = multiply(s, k)
    factors = [factor for factor in (s, k) if degree(factor) > 0]
    constant_content = math.prod(
        abs(factor[0]) for factor in (s, k) if degree(factor) == 0
    )
    contents_and_primitives = [divide_content(factor) for factor in factors]
    content = constant_content * math.prod(item[0] for item in contents_and_primitives)
    primitives = [item[1] for item in contents_and_primitives]
    candidate_count = 0
    hits = []
    for constant_factor in sympy.divisors(content * content):
        exponents = [range(3) for _ in primitives]
        if not exponents:
            exponents = [range(1)]
        for powers in __import__("itertools").product(*exponents):
            if sum(powers) > degree(m1):
                continue
            candidate = (int(constant_factor), 0, 0)
            for primitive, exponent in zip(primitives, powers):
                candidate = multiply(candidate, power(primitive, exponent))
            if not eventually_at_most(candidate, m1):
                continue
            candidate_count += 1
            total = tuple(m1[index] + candidate[index] for index in range(3))
            if divisible_by(total, r):
                hits.append({"powers": list(powers), "constant_factor": int(constant_factor)})
    return {
        "shift_base_divisor": divisor,
        "shift_uses_h": uses_h,
        "source_degree": degree(s),
        "m1_degree": degree(m1),
        "eventual_polynomial_candidate_count": candidate_count,
        "polynomial_descent_hits": hits,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Exhaust every d and d*h distance-one polynomial ray."""
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    base = math.gcd(prime - 1, coefficient)
    if base % 4 or (prime - 1) % base or coefficient % base:
        raise AssertionError("pressure ray has no common p-1 factorization")
    h = ((prime - 1) // base, coefficient // base, 0)
    if math.gcd(h[0], h[1]) != 1 or h[0] % 4 != 1 or h[1] % 4:
        raise AssertionError("p-1 quotient is not a primitive 1 mod 4 ray")
    rows = [
        audit_state(base, h, int(divisor), uses_h)
        for divisor in sympy.divisors(base)
        if int(divisor) % 4 == 1
        for uses_h in (False, True)
    ]
    hits = [
        {"shift_base_divisor": row["shift_base_divisor"], "shift_uses_h": row["shift_uses_h"], "hits": row["polynomial_descent_hits"]}
        for row in rows
        if row["polynomial_descent_hits"]
    ]
    if hits:
        raise AssertionError("distance-one fan unexpectedly has a uniform polynomial tail")
    return {
        "arithmetic": (
            "p-1=B*h is decomposed into every compatible shift d or d*h; primitive "
            "linear-factor unique factorization then exhausts each M1^2 polynomial "
            "divisor satisfying the eventual size bound and tests M1+e1 modulo r"
        ),
        "scope_note": (
            "This excludes uniform integer-polynomial square tails in the complete "
            "distance-one even-source fan on this pressure ray. It does not exclude "
            "nonpolynomial actual factors, as the seed itself demonstrates."
        ),
        "seed_prime": prime,
        "p_minus_one_base_factor": base,
        "compatible_polynomial_ray_count": len(rows),
        "eventual_polynomial_candidate_count": sum(int(row["eventual_polynomial_candidate_count"]) for row in rows),
        "polynomial_descent_hits": hits,
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({key: value for key, value in result.items() if key != "rows"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
