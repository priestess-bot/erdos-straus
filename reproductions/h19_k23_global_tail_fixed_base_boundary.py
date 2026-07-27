#!/usr/bin/env python3
"""Exhaust fixed canonical-base coverage over every global H19-k23 tail."""

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
RESULTS = ROOT / "reproductions" / "h19-k23-global-tail-fixed-base-boundary.json"
INVARIANTS = ROOT / "reproductions" / "h19_k23_uniform_tail_base_invariants.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


invariants = load_module("h19_k23_invariants_for_fixed_base_boundary", INVARIANTS)


def global_factor_and_forms() -> tuple[int, int, list[tuple[int, int, int]]]:
    """Return G, A, and (branch residue, A, C) data for the fourteen progressions."""
    branches = invariants.load_branches()
    forms = [branch["prime_form"] for branch in branches]
    coefficients = {int(form["coefficient"]) for form in forms}
    if len(coefficients) != 1:
        raise AssertionError("residual branches do not share one coefficient")
    coefficient = coefficients.pop()
    global_factor = math.gcd(
        coefficient, *(int(form["constant"]) - 1 for form in forms)
    )
    branch_forms = [
        (int(branch["v_mod_29"]), coefficient, int(branch["prime_form"]["constant"]))
        for branch in branches
    ]
    return global_factor, coefficient, branch_forms


def first_fixed_base_gap(
    coefficient: int, branch_forms: list[tuple[int, int, int]], denominator: int
) -> dict[str, object] | None:
    """Return an uncovered periodic state, or None if the fixed base covers all states."""
    if denominator % 4:
        raise ValueError("ordinary Type II tail denominator must be divisible by four")
    gap = denominator - 1
    q = denominator // 4
    slope = coefficient // denominator
    intercepts = [
        (residue, (constant + gap) // denominator)
        for residue, _, constant in branch_forms
    ]
    common_u_factor = math.gcd(slope, *(intercept for _, intercept in intercepts))
    fixed_square = (q * common_u_factor) ** 2
    least_divisor_by_residue: dict[int, int] = {}
    for divisor in sympy.divisors(fixed_square):
        residue = divisor % gap
        least_divisor_by_residue[residue] = min(
            divisor, least_divisor_by_residue.get(residue, divisor)
        )
    period = gap // math.gcd(slope, gap)
    for branch_residue, intercept in intercepts:
        for parameter in range(period):
            u = slope * parameter + intercept
            target = (-q * u) % gap
            divisor = least_divisor_by_residue.get(target)
            x = q * u
            if divisor is None or divisor > x:
                return {
                    "v_mod_29": branch_residue,
                    "parameter_mod_period": parameter,
                    "period": period,
                    "target_residue": target,
                    "least_fixed_base_divisor": divisor,
                    "x": x,
                }
    return None


def run_audit() -> dict[str, object]:
    """Check every globally available m=4q-1 tail using its full fixed base."""
    global_factor, coefficient, branch_forms = global_factor_and_forms()
    rows = []
    for denominator in sympy.divisors(global_factor):
        if denominator % 4:
            continue
        gap = denominator - 1
        failure = first_fixed_base_gap(coefficient, branch_forms, denominator)
        if failure is None:
            raise AssertionError("unexpected all-parameter fixed-base global tail")
        rows.append(
            {
                "tail_gap": gap,
                "q": denominator // 4,
                "tail_denominator": denominator,
                "first_uncovered_state": failure,
            }
        )
    return {
        "arithmetic": (
            "G=gcd(A,C_i-1) enumerates every global tail; for m=4q-1, "
            "F=(q*gcd(A/(m+1),(C_i+m)/(m+1)))^2 divides x^2 on every branch. "
            "All divisors of F are reduced modulo m, and every branch is checked over "
            "the exact period m/gcd(A/(m+1),m), including the divisor-size bound d<=x"
        ),
        "scope_note": (
            "This excludes all-parameter selectors using only the fixed canonical base. "
            "It does not exclude selectors using variable factors of u, nor does it turn "
            "uncovered composite parameter values into a claim about prime values."
        ),
        "global_p_minus_one_factor": global_factor,
        "global_tail_count": len(rows),
        "fixed_base_full_cover_count": 0,
        "global_tail_rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit()
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
