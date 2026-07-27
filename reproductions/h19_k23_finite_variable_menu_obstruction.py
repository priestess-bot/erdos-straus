#!/usr/bin/env python3
"""Exhibit the CRT obstruction to finite variable-prime template libraries."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
RESULTS = ROOT / "reproductions" / "h19-k23-finite-variable-menu-obstruction.json"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
GAP = 31
DEFAULT_VARIABLE_PRIMES = (37, 41, 43, 59, 73, 89, 103)


def load_branches():
    spec = importlib.util.spec_from_file_location("h19_k23_finite_menu_branches", BRANCHES)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BRANCHES.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.remaining_branches()


def crt_pair(residue: int, modulus: int, other_residue: int, other_modulus: int) -> tuple[int, int]:
    """Combine coprime congruences in normalized form."""
    if math.gcd(modulus, other_modulus) != 1:
        raise ValueError("CRT moduli must be coprime")
    multiplier = ((other_residue - residue) * pow(modulus, -1, other_modulus)) % other_modulus
    combined_modulus = modulus * other_modulus
    return (residue + modulus * multiplier) % combined_modulus, combined_modulus


def finite_menu_prime_avoidance(
    coefficient: int,
    constant: int,
    slope: int,
    intercept: int,
    target_parameter_residue: int,
    gap: int,
    primes: tuple[int, ...],
) -> tuple[int, int]:
    """Choose a prime-admissible parameter progression avoiding a finite variable menu.

    The target residue remains fixed modulo ``gap``.  Every usable variable prime
    is coprime to both ``slope`` and ``gap``; it divides the affine u-factor on one
    residue class only. CRT selects a different class while also avoiding the unique
    class that makes the affine prime candidate divisible by that prime.
    """
    if target_parameter_residue % gap != target_parameter_residue:
        raise ValueError("target parameter residue must be normalized")
    residue, modulus = target_parameter_residue, gap
    for prime in primes:
        if prime < 2 or not sympy.isprime(prime):
            raise ValueError("variable menu entries must be prime")
        if math.gcd(prime, coefficient * slope * gap) != 1:
            raise ValueError(
                "a usable variable prime must be coprime to coefficient, slope, and gap"
            )
        u_root = (-intercept * pow(slope, -1, prime)) % prime
        p_root = (-constant * pow(coefficient, -1, prime)) % prime
        local_residue = next(
            candidate
            for candidate in range(prime)
            if candidate not in {u_root, p_root}
        )
        residue, modulus = crt_pair(residue, modulus, local_residue, prime)
    return residue, modulus


def m31_uncovered_state() -> dict[str, int]:
    """Return the exact m=31 fixed-base gap on the v=0 residual progression."""
    branch = next(branch for branch in load_branches() if int(branch["v_mod_29"]) == 0)
    form = branch["prime_form"]
    coefficient = int(form["coefficient"])
    constant = int(form["constant"])
    denominator = GAP + 1
    q = denominator // 4
    slope = coefficient // denominator
    intercept = (constant + GAP) // denominator
    uniform_u_factor = math.gcd(slope, intercept)
    fixed_square = (q * uniform_u_factor) ** 2
    target = (-q * intercept) % GAP
    if any(divisor % GAP == target for divisor in sympy.divisors(fixed_square)):
        raise AssertionError("chosen state is not outside the full fixed base")
    return {
        "v_mod_29": int(branch["v_mod_29"]),
        "coefficient": coefficient,
        "constant": constant,
        "q": q,
        "slope": slope,
        "intercept": intercept,
        "uniform_u_factor": uniform_u_factor,
        "fixed_square": fixed_square,
        "target_parameter_residue": 0,
        "target_residue": target,
    }


def run_audit(primes: tuple[int, ...] = DEFAULT_VARIABLE_PRIMES) -> dict[str, object]:
    """Build one infinite parameter progression avoiding an arbitrary finite menu."""
    state = m31_uncovered_state()
    parameter, period = finite_menu_prime_avoidance(
        state["coefficient"],
        state["constant"],
        state["slope"],
        state["intercept"],
        state["target_parameter_residue"],
        GAP,
        primes,
    )
    u = state["slope"] * parameter + state["intercept"]
    if (-state["q"] * u) % GAP != state["target_residue"]:
        raise AssertionError("CRT parameter changed the fixed target residue")
    if any(u % prime == 0 for prime in primes):
        raise AssertionError("CRT parameter did not avoid the finite variable-prime menu")
    prime_offset = state["coefficient"] * parameter + state["constant"]
    prime_step = state["coefficient"] * period
    if math.gcd(prime_step, prime_offset) != 1:
        raise AssertionError("CRT progression is not primitive for Dirichlet's theorem")
    return {
        "arithmetic": (
            "for u=a*t+b and each usable variable prime ell, ell|u and ell|p each "
            "occupy one residue class modulo ell; CRT preserves t modulo the tail gap "
            "while avoiding both root classes, and the resulting p progression is primitive"
        ),
        "scope_note": (
            "Dirichlet's theorem gives infinitely many core primes in the displayed CRT "
            "progression, so this excludes prime-parameter coverage by any finite preselected "
            "nonbase variable-prime library. It does not exclude unbounded adaptive factors."
        ),
        "gap": GAP,
        "state": state,
        "variable_prime_menu": list(primes),
        "avoidance_parameter": parameter,
        "avoidance_period": period,
        "u_at_avoidance_parameter": u,
        "prime_progression_offset": prime_offset,
        "prime_progression_step": prime_step,
        "prime_progression_gcd": math.gcd(prime_step, prime_offset),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RESULTS)
    parser.add_argument("--prime", type=int, action="append")
    args = parser.parse_args()
    primes = tuple(args.prime) if args.prime else DEFAULT_VARIABLE_PRIMES
    payload = run_audit(primes)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
