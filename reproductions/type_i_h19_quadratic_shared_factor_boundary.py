#!/usr/bin/env python3
"""Exhaust the shared-factor quadratic Type I family on 14 H19 residuals.

With x=E*N on a residual progression, the quadratic divisor

    d=x^2/h=(E^2/h)*N^2,  h|E,

is a valid nonaffine Type I candidate.  Its Type I congruence is exactly
m|(4*h+1), because the natural-gap progression is primitive and hence
gcd(m,E)=1.  Meanwhile E|x forces m=-C mod 4E.  As m<=4h+1<=4E+1,
each pair E|S, h|E has at most two possible gaps, so this subfamily has a
complete finite audit without factoring arbitrary parameter values.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-i-h19-quadratic-shared-factor-boundary.json"
MIXED_BOUNDARY_SCRIPT = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
H19_MAX_GAP = 4 * 19 - 1


def load_mixed_boundary():
    spec = importlib.util.spec_from_file_location(
        "mixed_factor_h19_uniform_affine_boundary_for_quadratic", MIXED_BOUNDARY_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load mixed-factor boundary")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


mixed_boundary = load_mixed_boundary()
branching = mixed_boundary.branching


def factor_records(
    factorization: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    records: list[tuple[int, tuple[int, ...]]] = [(1, ())]
    for prime, exponent in factorization:
        records = [
            (value * prime**power, vector + (power,))
            for value, vector in records
            for power in range(exponent + 1)
        ]
    return tuple(records)


def divisor_values(
    primes: tuple[int, ...], exponents: tuple[int, ...]
) -> tuple[int, ...]:
    values = [1]
    for prime, exponent in zip(primes, exponents):
        values = [
            value * prime**power
            for value in values
            for power in range(exponent + 1)
        ]
    return tuple(values)


def quadratic_pairs(step: int) -> tuple[tuple[int, int], ...]:
    """Return every E|S, h|E once, using S's fixed prime factorization."""
    factorization = branching.boundary.prime_factors(step)
    primes = tuple(prime for prime, _ in factorization)
    pairs = []
    for fixed_factor, exponents in factor_records(factorization):
        for shared_factor in divisor_values(primes, exponents):
            pairs.append((fixed_factor, shared_factor))
    return tuple(pairs)


def verify_witness(
    coefficient: int, constant: int, gap: int, fixed_factor: int, shared_factor: int
) -> None:
    """Verify a quadratic certificate directly if a future audit finds one."""
    step = coefficient // 4
    offset = (constant + gap) // 4
    if math.gcd(step, offset) != fixed_factor or fixed_factor % shared_factor:
        raise AssertionError("invalid quadratic fixed data")
    for parameter in range(4):
        prime_candidate = coefficient * parameter + constant
        x = step * parameter + offset
        divisor = x * x // shared_factor
        if x * x % divisor or (prime_candidate * x + divisor) % gap:
            raise AssertionError("quadratic Type I condition failed")
        y = (prime_candidate * x + divisor) // gap
        z = prime_candidate * (x + prime_candidate * x * x // divisor) // gap
        if Fraction(4, prime_candidate) != (
            Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        ):
            raise AssertionError("quadratic Type I identity failed")


def audit_progression(
    coefficient: int, constant: int, pairs: tuple[tuple[int, int], ...]
) -> dict[str, object]:
    """Exhaust d=x^2/h with E|S and h|E on one residual progression."""
    if coefficient % 4 or constant % 24 != 1 or math.gcd(coefficient, constant) != 1:
        raise AssertionError("require a primitive core-prime progression")
    step = coefficient // 4
    gap_tests = 0
    for fixed_factor, shared_factor in pairs:
        residue = (-constant) % (4 * fixed_factor)
        for gap in (residue, residue + 4 * fixed_factor):
            if not (
                H19_MAX_GAP < gap <= constant - 2
                and gap % 4 == 3
                and gap <= 4 * shared_factor + 1
            ):
                continue
            offset = (constant + gap) // 4
            if math.gcd(step, offset) != fixed_factor:
                continue
            if math.gcd(fixed_factor, gap) != 1:
                raise AssertionError("primitive progression should make E and m coprime")
            gap_tests += 1
            if (4 * shared_factor + 1) % gap:
                continue
            verify_witness(
                coefficient, constant, gap, fixed_factor, shared_factor
            )
            return {
                "prime_step": coefficient,
                "prime_residue": constant,
                "pair_count_before_hit": pairs.index((fixed_factor, shared_factor)) + 1,
                "eligible_gap_tests_before_hit": gap_tests,
                "quadratic_shared_factor_certificate": {
                    "gap": gap,
                    "future_shift": (gap + 1) // 4,
                    "fixed_factor_E": fixed_factor,
                    "shared_factor_h": shared_factor,
                },
            }
    return {
        "prime_step": coefficient,
        "prime_residue": constant,
        "pair_count_exhausted": len(pairs),
        "eligible_gap_tests_exhausted": gap_tests,
        "quadratic_shared_factor_certificate": None,
    }


def run_audit() -> dict[str, object]:
    branches = mixed_boundary.remaining_branches()
    first_form = branches[0]["prime_form"]
    step = int(first_form["coefficient"]) // 4
    pairs = quadratic_pairs(step)
    rows = []
    for branch in branches:
        form = branch["prime_form"]
        rows.append(
            {
                "v_mod_29": branch["v_mod_29"],
                **audit_progression(
                    int(form["coefficient"]), int(form["constant"]), pairs
                ),
            }
        )
    if len(rows) != 14 or any(row["quadratic_shared_factor_certificate"] for row in rows):
        raise AssertionError("unexpected quadratic shared-factor outcome")
    return {
        "arithmetic": (
            "complete E|S, h|E enumeration; exact gap congruence; and the "
            "quadratic Type I equivalence m|(4*h+1)"
        ),
        "scope_note": (
            "Empty output excludes d=x^2/h where h is a fixed divisor of E. "
            "It does not exhaust the larger h|E^2 family, other nonaffine "
            "divisors, or multi-source lifts."
        ),
        "source_state": {
            "claim_id": "mixed-factor-h19-uniform-affine-boundary",
            "post_affine_residual_branch_count": len(rows),
            "quadratic_pair_count_per_progression": len(pairs),
        },
        "residual_progressions": rows,
        "total_eligible_gap_tests": sum(
            row["eligible_gap_tests_exhausted"] for row in rows
        ),
    }


def main() -> int:
    payload = run_audit()
    RESULTS.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
