#!/usr/bin/env python3
"""Exhaust uniform fixed-gap Type I certificates on the depth-four AC escape ray.

For p(t)=4*S*t+1 and a fixed legal gap m, write

    x(t)=(p(t)+m)/4=S*t+(m+1)/4=E*(u*t+v).

A nonconstant affine divisor d(t)|x(t)^2 giving a Type I certificate is
necessarily a*(u*t+v), with a|E^2, m|u, and
a == -4*E^2*v (mod m).  A constant divisor is a divisor of E^2 and must be
-(m+1)/4 modulo m.  Since gcd(E,m)=1, either case forces m|S.

The program exhausts both forms on the explicit conditional AC escape
progression. It is not a statement about nonaffine divisors or variable gaps.
"""

from __future__ import annotations

import argparse
from functools import cache
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ESCAPE_COEFFICIENT = 245_044_800
RESULTS = ROOT / "reproductions" / "type-i-escape-affine-boundary-results.json"


@cache
def positive_divisors(value: int) -> tuple[int, ...]:
    """Return all positive divisors using exact trial factorization."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: list[tuple[int, int]] = []
    remaining = value
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor:
            factor = 3 if factor == 2 else factor + 2
            continue
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        factors.append((factor, exponent))
        factor = 3 if factor == 2 else factor + 2
    if remaining > 1:
        factors.append((remaining, 1))

    result = [1]
    for prime, exponent in factors:
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return tuple(sorted(result))


def factorization(value: int) -> list[tuple[int, int]]:
    """Return an exact prime factorization for reporting."""
    result: list[tuple[int, int]] = []
    remaining = value
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor:
            factor = 3 if factor == 2 else factor + 2
            continue
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        result.append((factor, exponent))
        factor = 3 if factor == 2 else factor + 2
    if remaining > 1:
        result.append((remaining, 1))
    return result


def fixed_gap_state(coefficient: int, gap: int) -> dict[str, int] | None:
    """Return primitive x(t) data for one legal fixed gap."""
    if coefficient <= 0 or coefficient % 4 or gap < 3 or gap % 4 != 3:
        return None
    scale = coefficient // 4
    offset = (gap + 1) // 4
    common = math.gcd(scale, offset)
    if math.gcd(common, gap) != 1:
        raise AssertionError("a primitive p(t)=coefficient*t+1 has gcd(E,m)=1")
    return {
        "gap": gap,
        "scale": scale,
        "offset": offset,
        "content": common,
        "primitive_scale": scale // common,
        "primitive_offset": offset // common,
    }


def affine_candidate_holds(coefficient: int, state: dict[str, int], a: int) -> bool:
    """Check the exact affine Type I congruence conditions."""
    gap = state["gap"]
    content = state["content"]
    primitive_scale = state["primitive_scale"]
    primitive_offset = state["primitive_offset"]
    if a <= 0 or content * content % a:
        return False
    return (
        primitive_scale % gap == 0
        and (a + 4 * content * content * primitive_offset) % gap == 0
    )


def constant_candidate_holds(state: dict[str, int], divisor: int) -> bool:
    """Check the exact constant Type I congruence after coefficient reduction."""
    return (
        divisor > 0
        and state["content"] * state["content"] % divisor == 0
        and (state["offset"] + divisor) % state["gap"] == 0
    )


def direct_affine_check(
    coefficient: int, state: dict[str, int], a: int, parameter: int
) -> bool:
    """Independently test one affine candidate at a concrete parameter."""
    gap = state["gap"]
    content = state["content"]
    u = state["primitive_scale"]
    v = state["primitive_offset"]
    prime = coefficient * parameter + 1
    x = content * (u * parameter + v)
    divisor = a * (u * parameter + v)
    return (
        divisor > 0
        and x * x % divisor == 0
        and (prime * x + divisor) % gap == 0
    )


def direct_constant_check(
    coefficient: int, state: dict[str, int], divisor: int, parameter: int
) -> bool:
    """Independently test one constant candidate at a concrete parameter."""
    gap = state["gap"]
    x = coefficient // 4 * parameter + state["offset"]
    prime = coefficient * parameter + 1
    return (
        divisor > 0
        and x * x % divisor == 0
        and (prime * x + divisor) % gap == 0
    )


def run_affine_boundary_audit(
    coefficient: int = ESCAPE_COEFFICIENT,
) -> dict[str, object]:
    """Exhaust all fixed-gap constant and affine Type I divisor candidates."""
    if coefficient <= 0 or coefficient % 24:
        raise ValueError("coefficient must be a positive multiple of 24")
    scale = coefficient // 4
    states: list[dict[str, int]] = []
    affine_hits: list[dict[str, int]] = []
    constant_hits: list[dict[str, int]] = []
    affine_candidate_count = 0
    constant_candidate_count = 0

    for gap in positive_divisors(scale):
        if gap % 4 != 3:
            continue
        state = fixed_gap_state(coefficient, gap)
        if state is None:
            raise AssertionError("divisor of the scale should give a legal state")
        if state["primitive_scale"] % gap:
            raise AssertionError("m|S and gcd(E,m)=1 must imply m|u")
        states.append(state)
        for divisor in positive_divisors(state["content"] ** 2):
            affine_candidate_count += 1
            if affine_candidate_holds(coefficient, state, divisor):
                if not all(
                    direct_affine_check(coefficient, state, divisor, parameter)
                    for parameter in range(4)
                ):
                    raise AssertionError("affine criterion disagrees with direct checks")
                affine_hits.append({**state, "a": divisor})

            constant_candidate_count += 1
            if constant_candidate_holds(state, divisor):
                if not all(
                    direct_constant_check(coefficient, state, divisor, parameter)
                    for parameter in range(4)
                ):
                    raise AssertionError("constant criterion disagrees with direct checks")
                constant_hits.append({**state, "divisor": divisor})

    return {
        "arithmetic": (
            "exact divisor enumeration, primitive affine reduction, and direct "
            "integer congruence checks at independent parameter values"
        ),
        "scope_note": (
            "This exhausts fixed-gap constant and nonconstant affine Type I "
            "divisors on one conditional escape progression. It does not "
            "exclude nonaffine divisors, variable gaps, Type II certificates, "
            "or a general strict descent."
        ),
        "coefficient": coefficient,
        "scale": scale,
        "scale_factorization": [
            {"prime": prime, "exponent": exponent}
            for prime, exponent in factorization(scale)
        ],
        "scale_divisor_count": len(positive_divisors(scale)),
        "fixed_gap_state_count": len(states),
        "affine_candidate_count": affine_candidate_count,
        "constant_candidate_count": constant_candidate_count,
        "affine_hits": affine_hits,
        "constant_hits": constant_hits,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coefficient", type=int, default=ESCAPE_COEFFICIENT)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_affine_boundary_audit(args.coefficient)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
