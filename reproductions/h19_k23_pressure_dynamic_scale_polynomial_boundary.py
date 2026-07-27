#!/usr/bin/env python3
"""Audit polynomial square-tail factors for the natural growing external scale."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-dynamic-scale-polynomial-boundary-2097152.json"
TARGET_SEED = 748_375_048_866_405_601

Polynomial = tuple[int, int, int]


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    """Multiply degree-at-most-two polynomials in increasing coefficient order."""
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
    candidate_degree = degree(candidate)
    bound_degree = degree(bound)
    return candidate_degree < bound_degree or (
        candidate_degree == bound_degree
        and candidate[candidate_degree] <= bound[bound_degree]
    )


def divisible_by_linear(value: Polynomial, modulus: tuple[int, int]) -> bool:
    """Check q(t)|value(t) by evaluating at the rational root of q."""
    constant, coefficient = modulus
    numerator = (
        value[2] * constant * constant
        - value[1] * constant * coefficient
        + value[0] * coefficient * coefficient
    )
    return numerator == 0


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Exhaust every integral polynomial divisor of M(t)^2 allowed by size."""
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    global_factor = math.gcd((prime - 1) // 4, coefficient // 4)
    h = ((prime - 1) // (4 * global_factor), coefficient // (4 * global_factor), 0)
    source = (prime - global_factor, coefficient, 0)
    if math.gcd(h[0], h[1]) != 1 or math.gcd(source[0], source[1]) != 1:
        raise AssertionError("dynamic linear factors are not primitive")
    if source != (4 * global_factor * h[0] + 1 - global_factor, 4 * global_factor * h[1], 0):
        raise AssertionError("dynamic source is not p-G")
    modulus = (4 * h[0] - 1, 4 * h[1])
    product = multiply(h, source)
    rows = []
    hits = []
    # Primitive distinct linear factors h and source generate every polynomial
    # divisor of (h*source)^2 in Z[t], up to a unit.
    for h_exponent in range(3):
        for source_exponent in range(3):
            if h_exponent + source_exponent > 2:
                continue
            candidate = multiply(power(h, h_exponent), power(source, source_exponent))
            if not eventually_at_most(candidate, product):
                continue
            target_sum = tuple(product[index] + candidate[index] for index in range(3))
            congruence_holds = divisible_by_linear(target_sum, modulus)
            record = {
                "h_exponent": h_exponent,
                "source_exponent": source_exponent,
                "candidate_degree": degree(candidate),
                "congruence_holds": congruence_holds,
            }
            rows.append(record)
            if congruence_holds:
                hits.append(record)
    if len(rows) != 5 or hits:
        raise AssertionError("unexpected dynamic polynomial tail result")
    return {
        "arithmetic": (
            "the natural scale h=(p-1)/(4G) makes the source p-G and product "
            "M=h(p-G); primitive linear-factor unique factorization exhausts every "
            "integer-polynomial divisor of M^2 that is eventually at most M"
        ),
        "scope_note": (
            "This excludes only integer-polynomial square-tail factors for this one "
            "natural parameter-growing standard source. It does not exclude selecting "
            "nonpolynomial factors of p-G or another dynamic descent state."
        ),
        "seed_prime": prime,
        "global_factor": global_factor,
        "dynamic_scale": {"constant": h[0], "coefficient": h[1]},
        "dynamic_source": {"constant": source[0], "coefficient": source[1]},
        "eventual_polynomial_candidate_count": len(rows),
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
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
