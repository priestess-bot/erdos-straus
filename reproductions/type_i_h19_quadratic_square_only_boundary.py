#!/usr/bin/env python3
"""Exhaust square-only quadratic Type I divisors on 14 H19 residuals.

For x=E*N, every h|E^2 with h<=E gives the nonaffine Type I divisor

    d=x^2/h.

The Type I congruence is m|(4*h+1), and E|x gives m=-C mod 4E.  Since
m<=4*h+1<=4E+1, each (E,h) has at most two gap candidates.  This script
exhausts the full h|E^2, h<=E family, including h that divide E and the
genuinely square-only cases h does not divide E.  It streams candidates and
audits the fourteen independent progressions in parallel.
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
import importlib.util
import json
import math
import os
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-i-h19-quadratic-square-only-boundary.json"
MIXED_BOUNDARY_SCRIPT = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
H19_MAX_GAP = 4 * 19 - 1


def load_mixed_boundary():
    spec = importlib.util.spec_from_file_location(
        "mixed_factor_h19_uniform_affine_boundary_for_square_quadratic",
        MIXED_BOUNDARY_SCRIPT,
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


def pair_count(step: int) -> int:
    """Count E|S, h|E^2, h<=E without retaining the pairs."""
    factors = branching.boundary.prime_factors(step)
    total = 0
    for fixed_factor, exponents in factor_records(factors):
        values = [1]
        for (prime, _), exponent in zip(factors, exponents):
            values = [
                value * prime**power
                for value in values
                for power in range(2 * exponent + 1)
            ]
        total += sum(value <= fixed_factor for value in values)
    return total


def verify_witness(
    coefficient: int, constant: int, gap: int, fixed_factor: int, shared_factor: int
) -> None:
    """Verify a discovered quadratic Type I leaf symbolically on samples."""
    step = coefficient // 4
    offset = (constant + gap) // 4
    if math.gcd(step, offset) != fixed_factor:
        raise AssertionError("incorrect quadratic fixed factor")
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
    coefficient: int, constant: int, factorization: tuple[tuple[int, int], ...]
) -> dict[str, object]:
    """Stream every h|E^2 with h<=E for one primitive progression."""
    if coefficient % 4 or constant % 24 != 1 or math.gcd(coefficient, constant) != 1:
        raise AssertionError("require a primitive core-prime progression")
    step = coefficient // 4
    records = factor_records(factorization)
    pair_total = 0
    eligible_gaps = 0
    factors = tuple(prime for prime, _ in factorization)

    def visit_h(index: int, value: int, fixed_factor: int, exponents: tuple[int, ...]) -> dict[str, int] | None:
        nonlocal pair_total, eligible_gaps
        if value > fixed_factor:
            return None
        if index == len(factors):
            pair_total += 1
            if value < 19:
                return None
            modulus = 4 * fixed_factor
            residue = (-constant) % modulus
            for gap in (residue, residue + modulus):
                if not (
                    H19_MAX_GAP < gap <= constant - 2
                    and gap % 4 == 3
                    and gap <= 4 * value + 1
                ):
                    continue
                offset = (constant + gap) // 4
                if math.gcd(step, offset) != fixed_factor:
                    continue
                if math.gcd(fixed_factor, gap) != 1:
                    raise AssertionError("primitive progression should make E and m coprime")
                eligible_gaps += 1
                if (4 * value + 1) % gap:
                    continue
                verify_witness(coefficient, constant, gap, fixed_factor, value)
                return {
                    "gap": gap,
                    "future_shift": (gap + 1) // 4,
                    "fixed_factor_E": fixed_factor,
                    "square_factor_h": value,
                }
            return None
        power = 1
        for _ in range(2 * exponents[index] + 1):
            found = visit_h(index + 1, value * power, fixed_factor, exponents)
            if found is not None:
                return found
            power *= factors[index]
        return None

    for fixed_factor, exponents in records:
        found = visit_h(0, 1, fixed_factor, exponents)
        if found is not None:
            return {
                "prime_step": coefficient,
                "prime_residue": constant,
                "pair_count_before_hit": pair_total,
                "eligible_gap_tests_before_hit": eligible_gaps,
                "quadratic_square_only_certificate": found,
            }
    return {
        "prime_step": coefficient,
        "prime_residue": constant,
        "pair_count_exhausted": pair_total,
        "eligible_gap_tests_exhausted": eligible_gaps,
        "quadratic_square_only_certificate": None,
    }


def audit_task(
    task: tuple[int, int, tuple[tuple[int, int], ...]]
) -> dict[str, object]:
    """Pickle-friendly worker entry point for one residual progression."""
    return audit_progression(*task)


def run_audit() -> dict[str, object]:
    branches = mixed_boundary.remaining_branches()
    first_form = branches[0]["prime_form"]
    step = int(first_form["coefficient"]) // 4
    factorization = branching.boundary.prime_factors(step)
    expected_pairs = pair_count(step)
    tasks = [
        (int(branch["prime_form"]["coefficient"]), int(branch["prime_form"]["constant"]), factorization)
        for branch in branches
    ]
    workers = min(len(tasks), os.cpu_count() or 1)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        audits = list(executor.map(audit_task, tasks))
    rows = [
        {"v_mod_29": branch["v_mod_29"], **audit}
        for branch, audit in zip(branches, audits)
    ]
    if len(rows) != 14 or any(row["quadratic_square_only_certificate"] for row in rows):
        raise AssertionError("unexpected square-only quadratic outcome")
    if any(row["pair_count_exhausted"] != expected_pairs for row in rows):
        raise AssertionError("incomplete square-only pair enumeration")
    return {
        "arithmetic": (
            "streaming complete E|S, h|E^2, h<=E enumeration; exact two-gap "
            "reduction; and the quadratic Type I condition m|(4*h+1)"
        ),
        "scope_note": (
            "Empty output excludes every quadratic d=x^2/h with h|E^2 and "
            "h<=E. It does not cover h>E, other parameter-dependent divisors, "
            "or coupled multi-source lifts."
        ),
        "source_state": {
            "claim_id": "type-I-h19-quadratic-shared-factor-boundary",
            "post_affine_residual_branch_count": len(rows),
            "quadratic_pair_count_per_progression": expected_pairs,
            "parallel_worker_count": workers,
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
