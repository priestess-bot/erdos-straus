#!/usr/bin/env python3
"""Exhaust uniform constant Type I divisors on the 14 H19 residuals.

For x=E*(u*n+v), a constant divisor d=a satisfies d|x^2 for every
parameter exactly when a|E^2.  Its Type I congruence is uniform exactly when

    m|u,  a == -4*E^2*v^2 (mod m).

Thus only the finite natural gaps m|S must be examined.  This is the degree
zero complement to the existing affine and quadratic Type I audits.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-i-h19-uniform-constant-boundary.json"
MIXED_BOUNDARY_SCRIPT = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
H19_MAX_GAP = 4 * 19 - 1


def load_mixed_boundary():
    spec = importlib.util.spec_from_file_location(
        "mixed_factor_h19_uniform_affine_boundary_for_constant", MIXED_BOUNDARY_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load mixed-factor boundary")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


mixed_boundary = load_mixed_boundary()
branching = mixed_boundary.branching


def divisor_records(
    factorization: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    records: list[tuple[int, tuple[int, ...]]] = [(1, ())]
    for prime, exponent in factorization:
        records = [
            (value * prime**power, vector + (power,))
            for value, vector in records
            for power in range(exponent + 1)
        ]
    return tuple(sorted(records))


def divisor_residue_witness(
    fixed_factor: int,
    exponents: tuple[int, ...],
    gap: int,
    residue: int,
    primes: tuple[int, ...],
) -> tuple[int | None, int]:
    """Find a|E^2 in a target residue class, using the shorter side."""
    start = residue % gap
    if start == 0:
        start = gap
    square = fixed_factor * fixed_factor
    if start > square:
        return None, 0
    linear_count = (square - start) // gap + 1
    divisor_count = math.prod(2 * exponent + 1 for exponent in exponents)
    checks = 0
    if linear_count <= divisor_count:
        for candidate in range(start, square + 1, gap):
            checks += 1
            if square % candidate == 0:
                return candidate, checks
        return None, checks

    def visit(index: int, value: int) -> int | None:
        nonlocal checks
        if index == len(primes):
            checks += 1
            return value if value % gap == residue % gap else None
        power = 1
        for _ in range(2 * exponents[index] + 1):
            found = visit(index + 1, value * power)
            if found is not None:
                return found
            power *= primes[index]
        return None

    return visit(0, 1), checks


def verify_witness(
    coefficient: int, constant: int, gap: int, fixed_factor: int, divisor: int
) -> None:
    """Verify a constant Type I certificate if one is found."""
    step = coefficient // 4
    offset = (constant + gap) // 4
    if math.gcd(step, offset) != fixed_factor or fixed_factor * fixed_factor % divisor:
        raise AssertionError("invalid constant divisor")
    for parameter in range(4):
        prime_candidate = coefficient * parameter + constant
        x = step * parameter + offset
        if x * x % divisor or (prime_candidate * x + divisor) % gap:
            raise AssertionError("constant Type I condition failed")
        y = (prime_candidate * x + divisor) // gap
        z = prime_candidate * (x + prime_candidate * x * x // divisor) // gap
        if Fraction(4, prime_candidate) != (
            Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        ):
            raise AssertionError("constant Type I identity failed")


def audit_progression(coefficient: int, constant: int) -> dict[str, object]:
    if coefficient % 4 or constant % 24 != 1 or math.gcd(coefficient, constant) != 1:
        raise AssertionError("require a primitive core-prime progression")
    step = coefficient // 4
    factorization = branching.boundary.prime_factors(step)
    records = divisor_records(factorization)
    exponent_by_divisor = dict(records)
    primes = tuple(prime for prime, _ in factorization)
    gap_count = 0
    checks = 0
    for gap, _ in records:
        if not (H19_MAX_GAP < gap <= constant - 2 and gap % 4 == 3):
            continue
        offset = (constant + gap) // 4
        fixed_factor = math.gcd(step, offset)
        quotient_coefficient = step // fixed_factor
        quotient_constant = offset // fixed_factor
        if quotient_coefficient % gap:
            continue
        if math.gcd(fixed_factor, gap) != 1:
            raise AssertionError("primitive progression should make E and m coprime")
        gap_count += 1
        divisor, used = divisor_residue_witness(
            fixed_factor,
            exponent_by_divisor[fixed_factor],
            gap,
            -4 * fixed_factor * fixed_factor * quotient_constant**2,
            primes,
        )
        checks += used
        if divisor is None:
            continue
        verify_witness(coefficient, constant, gap, fixed_factor, divisor)
        return {
            "prime_step": coefficient,
            "prime_residue": constant,
            "candidate_gap_count_before_hit": gap_count,
            "divisor_residue_checks_before_hit": checks,
            "uniform_constant_type_i_certificate": {
                "gap": gap,
                "future_shift": (gap + 1) // 4,
                "fixed_factor_E": fixed_factor,
                "constant_divisor": divisor,
            },
        }
    return {
        "prime_step": coefficient,
        "prime_residue": constant,
        "candidate_gap_count_exhausted": gap_count,
        "divisor_residue_checks_exhausted": checks,
        "uniform_constant_type_i_certificate": None,
    }


def run_audit() -> dict[str, object]:
    branches = mixed_boundary.remaining_branches()
    rows = []
    for branch in branches:
        form = branch["prime_form"]
        rows.append(
            {
                "v_mod_29": branch["v_mod_29"],
                **audit_progression(int(form["coefficient"]), int(form["constant"])),
            }
        )
    if len(rows) != 14 or any(row["uniform_constant_type_i_certificate"] for row in rows):
        raise AssertionError("unexpected constant Type I outcome")
    if any(row["candidate_gap_count_exhausted"] != 564 for row in rows):
        raise AssertionError("incomplete constant-gap enumeration")
    return {
        "arithmetic": (
            "constant-divisor rigidity, exact quadratic coefficient congruences, "
            "and complete E^2 divisor-residue selection"
        ),
        "scope_note": (
            "Empty output excludes uniform constant Type I divisors only. It "
            "does not cover parameter-dependent or multi-source certificates."
        ),
        "source_state": {
            "claim_id": "h19-k23-multisource-marked-state",
            "post_affine_residual_branch_count": len(rows),
        },
        "residual_progressions": rows,
        "total_divisor_residue_checks": sum(
            row["divisor_residue_checks_exhausted"] for row in rows
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
