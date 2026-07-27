#!/usr/bin/env python3
"""Audit all uniform affine square-divisor Type II leaves on H19-k23 residuals.

For a residual progression p=P*n+C and a fixed future gap m, put

    x=(p+m)/4=S*n+T,  E=gcd(S,T),  d=a*x/E.

The uniform-affine rigidity theorem reduces every positive nonconstant
square-divisor family to a|E^2, a<=E.  The Type II congruence is m|(E+a).
Because E|T, while m<=E+a<=2E, a fixed E can give at most one gap:

    m == -C (mod 4E),  0<m<4E.

This makes the apparently unbounded gap search finite and exact for each
displayed progression.  The audit stops after finding one verified uniform
certificate for a progression; an empty row exhausts every allowed (E,a,m).
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-h19-affine-square-uniform-audit.json"
BRANCHING_SCRIPT = ROOT / "reproductions" / "type_ii_h19_external_scale_k23_branching.py"
H19_MAX_GAP = 4 * 19 - 1


def load_branching():
    spec = importlib.util.spec_from_file_location(
        "h19_external_scale_k23_branching_for_affine_square", BRANCHING_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load k=23 branching script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


branching = load_branching()


def divisor_records(
    factors: tuple[tuple[int, int], ...], multiplier: int = 1
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Return values and exponent vectors for divisors of a factored integer."""
    records: list[tuple[int, tuple[int, ...]]] = [(1, ())]
    for prime, exponent in factors:
        expanded: list[tuple[int, tuple[int, ...]]] = []
        power = 1
        for index in range(exponent + 1):
            for value, vector in records:
                expanded.append((value * power, vector + (index,)))
            power *= prime
        records = expanded
    if multiplier != 1:
        raise ValueError("multiplier is not used for exponent records")
    return tuple(sorted(records))


def square_divisor_witness(
    fixed_factor: int,
    exponents: tuple[int, ...],
    gap: int,
    primes: tuple[int, ...],
) -> tuple[int | None, int]:
    """Find a<=E with a|E^2 and a=-E mod gap, counting checks exactly."""
    start = (-fixed_factor) % gap
    if start == 0:
        start = gap
    if start > fixed_factor:
        return None, 0

    linear_count = (fixed_factor - start) // gap + 1
    divisor_upper_bound = math.prod(2 * exponent + 1 for exponent in exponents)
    checks = 0

    # Scan the shorter of the congruence progression and the square-divisor set.
    if linear_count <= divisor_upper_bound:
        square = fixed_factor * fixed_factor
        for candidate in range(start, fixed_factor + 1, gap):
            checks += 1
            if square % candidate == 0:
                return candidate, checks
        return None, checks

    def visit(index: int, value: int) -> int | None:
        nonlocal checks
        if value > fixed_factor:
            return None
        if index == len(primes):
            checks += 1
            if (value + fixed_factor) % gap == 0:
                return value
            return None
        power = 1
        for _ in range(2 * exponents[index] + 1):
            found = visit(index + 1, value * power)
            if found is not None:
                return found
            power *= primes[index]
        return None

    return visit(0, 1), checks


def verify_witness(
    coefficient: int, constant: int, gap: int, fixed_factor: int, scale: int
) -> None:
    """Verify both Type II divisibilities and identities on symbolic samples."""
    step = coefficient // 4
    offset = (constant + gap) // 4
    if math.gcd(step, offset) != fixed_factor:
        raise AssertionError("incorrect affine gcd")
    if not (scale <= fixed_factor and fixed_factor * fixed_factor % scale == 0):
        raise AssertionError("invalid square-divisor scale")
    if (fixed_factor + scale) % gap:
        raise AssertionError("missing first Type II congruence")

    for parameter in range(4):
        prime_candidate = coefficient * parameter + constant
        x = step * parameter + offset
        divisor = scale * x // fixed_factor
        if x * x % divisor:
            raise AssertionError("d does not divide x^2")
        if (x + divisor) % gap or (x + x * x // divisor) % gap:
            raise AssertionError("Type II denominator is not integral")
        y = prime_candidate * (x + divisor) // gap
        z = prime_candidate * (x + x * x // divisor) // gap
        if Fraction(4, prime_candidate) != (
            Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        ):
            raise AssertionError("Type II identity failed")


def audit_progression(coefficient: int, constant: int) -> dict[str, object]:
    """Decide whether this progression has a uniform square-affine leaf."""
    if coefficient % 4 or constant % 24 != 1:
        raise AssertionError("progression must preserve core integrality")
    step = coefficient // 4
    factorization = branching.boundary.prime_factors(step)
    primes = tuple(prime for prime, _ in factorization)
    candidates = 0
    square_checks = 0

    for fixed_factor, exponents in divisor_records(factorization):
        gap = (-constant) % (4 * fixed_factor)
        if not (
            H19_MAX_GAP < gap <= constant - 2
            and gap % 4 == 3
            and gap <= 2 * fixed_factor
        ):
            continue
        offset = (constant + gap) // 4
        if math.gcd(step, offset) != fixed_factor:
            continue
        candidates += 1
        scale, checks = square_divisor_witness(
            fixed_factor, exponents, gap, primes
        )
        square_checks += checks
        if scale is None:
            continue
        verify_witness(coefficient, constant, gap, fixed_factor, scale)
        return {
            "prime_step": coefficient,
            "prime_residue": constant,
            "candidate_fixed_factor_count_before_hit": candidates,
            "square_divisor_checks_before_hit": square_checks,
            "uniform_square_affine_certificate": {
                "gap": gap,
                "future_shift": (gap + 1) // 4,
                "fixed_factor": fixed_factor,
                "scale_a": scale,
                "square_only": fixed_factor % scale != 0,
            },
        }

    return {
        "prime_step": coefficient,
        "prime_residue": constant,
        "candidate_fixed_factor_count_exhausted": candidates,
        "square_divisor_checks_exhausted": square_checks,
        "uniform_square_affine_certificate": None,
    }


def run_audit() -> dict[str, object]:
    """Audit every residual progression from the exact k=23 split."""
    source = branching.run_audit()
    residuals = [branch for branch in source["branches"] if branch["admissible_escape"]]
    rows = []
    for branch in residuals:
        form = branch["prime_form"]
        rows.append(
            {
                "v_mod_29": branch["v_mod_29"],
                **audit_progression(int(form["coefficient"]), int(form["constant"])),
            }
        )
    if len(rows) != 18:
        raise AssertionError("unexpected residual branch count")
    hits = [row for row in rows if row["uniform_square_affine_certificate"]]
    return {
        "arithmetic": (
            "complete fixed-factor enumeration E|S; for each E the gcd condition "
            "and m|E+a force at most one candidate gap, followed by exact "
            "a|E^2, a<=E residue selection and Type II identity checks"
        ),
        "scope_note": (
            "A hit is a uniform affine Type II certificate on every prime value "
            "of the displayed progression. An empty row exhausts this full "
            "uniform nonconstant affine square-divisor family only."
        ),
        "source_state": {
            "claim_id": "type-II-h19-external-scale-k23-branching",
            "residual_branch_count": len(rows),
        },
        "residual_progressions": rows,
        "certificate_progression_count": len(hits),
        "square_only_certificate_count": sum(
            bool(row["uniform_square_affine_certificate"])
            and bool(row["uniform_square_affine_certificate"]["square_only"])
            for row in hits
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
