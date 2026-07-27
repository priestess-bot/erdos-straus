#!/usr/bin/env python3
"""Audit uniform affine Type I square-divisor certificates on H19-k23 residuals.

For p=P*n+C, x=(p+m)/4=S*n+T, E=gcd(S,T), and N=x/E,
every positive nonconstant affine divisor d|x^2 has d=a*N with a|E^2.
Unlike Type II, Type I does not require a<=E.  Requiring m|p*x+d for every
parameter forces, exactly,

    m | S/E,              a == -4*E^2*(T/E) (mod m).

Thus every uniform affine Type I family is found by the finite enumeration
of m divisors of S and a divisors of E^2.  The script returns the first
certificate on a progression and exhausts all candidates on an empty row.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-i-h19-affine-uniform-square-audit.json"
BRANCHING_SCRIPT = ROOT / "reproductions" / "type_ii_h19_external_scale_k23_branching.py"
H19_MAX_GAP = 4 * 19 - 1


def load_branching():
    spec = importlib.util.spec_from_file_location(
        "h19_external_scale_k23_branching_for_type_i_affine", BRANCHING_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load k=23 branching script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


branching = load_branching()


def divisor_records(
    factors: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Return every divisor together with its exponent vector."""
    records: list[tuple[int, tuple[int, ...]]] = [(1, ())]
    for prime, exponent in factors:
        records = [
            (value * prime**power, vector + (power,))
            for value, vector in records
            for power in range(exponent + 1)
        ]
    return tuple(sorted(records))


def square_divisor_witness(
    fixed_factor: int,
    exponents: tuple[int, ...],
    gap: int,
    residue: int,
    primes: tuple[int, ...],
) -> tuple[int | None, int]:
    """Find a|E^2 in one target residue class, counting all tested values."""
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
    coefficient: int, constant: int, gap: int, fixed_factor: int, scale: int
) -> None:
    """Check the Type I congruence and reconstructed identity on samples."""
    step = coefficient // 4
    offset = (constant + gap) // 4
    if math.gcd(step, offset) != fixed_factor:
        raise AssertionError("incorrect affine gcd")
    if fixed_factor * fixed_factor % scale:
        raise AssertionError("scale does not divide E^2")
    quotient_coefficient = step // fixed_factor
    quotient_constant = offset // fixed_factor
    coefficients = (
        4 * fixed_factor * fixed_factor * quotient_coefficient**2,
        quotient_coefficient
        * (8 * fixed_factor * fixed_factor * quotient_constant + scale),
        quotient_constant
        * (4 * fixed_factor * fixed_factor * quotient_constant + scale),
    )
    if any(value % gap for value in coefficients):
        raise AssertionError("Type I affine congruence does not hold identically")
    for parameter in range(4):
        prime_candidate = coefficient * parameter + constant
        x = step * parameter + offset
        divisor = scale * x // fixed_factor
        if x * x % divisor or (prime_candidate * x + divisor) % gap:
            raise AssertionError("Type I certificate condition failed")
        y = (prime_candidate * x + divisor) // gap
        z = prime_candidate * (x + prime_candidate * x * x // divisor) // gap
        if Fraction(4, prime_candidate) != (
            Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        ):
            raise AssertionError("Type I identity failed")


def audit_progression(coefficient: int, constant: int) -> dict[str, object]:
    """Decide the full uniform nonconstant affine Type I family."""
    if coefficient % 4 or constant % 24 != 1:
        raise AssertionError("progression must preserve core integrality")
    step = coefficient // 4
    factorization = branching.boundary.prime_factors(step)
    primes = tuple(prime for prime, _ in factorization)
    records = divisor_records(factorization)
    exponent_by_divisor = dict(records)
    gaps = sorted(
        gap
        for gap, _ in records
        if H19_MAX_GAP < gap <= constant - 2 and gap % 4 == 3
    )
    states = 0
    checks = 0

    for gap in gaps:
        offset = (constant + gap) // 4
        fixed_factor = math.gcd(step, offset)
        quotient = step // fixed_factor
        if quotient % gap:
            continue
        fixed_vector = exponent_by_divisor[fixed_factor]
        residue = -4 * fixed_factor * fixed_factor * (offset // fixed_factor)
        states += 1
        scale, used = square_divisor_witness(
            fixed_factor, fixed_vector, gap, residue, primes
        )
        checks += used
        if scale is None:
            continue
        verify_witness(coefficient, constant, gap, fixed_factor, scale)
        return {
            "prime_step": coefficient,
            "prime_residue": constant,
            "candidate_gap_count_before_hit": states,
            "square_divisor_checks_before_hit": checks,
            "uniform_affine_type_i_certificate": {
                "gap": gap,
                "future_shift": (gap + 1) // 4,
                "fixed_factor": fixed_factor,
                "scale_a": scale,
                "type_ii_sized": scale <= fixed_factor,
            },
        }

    if states != len(gaps):
        raise AssertionError("a candidate gap failed the necessary m|S/E test")
    return {
        "prime_step": coefficient,
        "prime_residue": constant,
        "candidate_gap_count_exhausted": states,
        "square_divisor_checks_exhausted": checks,
        "uniform_affine_type_i_certificate": None,
    }


def run_audit() -> dict[str, object]:
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
    hits = [row for row in rows if row["uniform_affine_type_i_certificate"]]
    return {
        "arithmetic": (
            "rigid affine divisor reduction d=a*x/E, exact coefficient "
            "congruences for m|p*x+d, and complete divisor-residue selection"
        ),
        "scope_note": (
            "This decides uniform nonconstant affine Type I divisors on the "
            "displayed progressions. It does not cover nonaffine or "
            "parameter-dependent Type I certificates."
        ),
        "source_state": {
            "claim_id": "type-II-h19-external-scale-k23-branching",
            "residual_branch_count": len(rows),
        },
        "residual_progressions": rows,
        "certificate_progression_count": len(hits),
        "strictly_type_i_sized_certificate_count": sum(
            bool(row["uniform_affine_type_i_certificate"])
            and not bool(row["uniform_affine_type_i_certificate"]["type_ii_sized"])
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
