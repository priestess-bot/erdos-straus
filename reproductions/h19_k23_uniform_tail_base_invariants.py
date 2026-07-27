#!/usr/bin/env python3
"""Extract maximal branch-uniform Type II tail bases for H19-k23.

For a globally available ordinary tail ``m=4q-1`` and every residual
progression ``p=A*t+C_i``, write ``u=(p+m)/(m+1)=a*t+b_i``.  The gcd of
``a,b_1,...,b_r`` is exactly the largest integer dividing every such ``u``.
Together with the primes of ``q``, this supplies a canonical support base.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "h19-k23-uniform-tail-base-invariants.json"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"
TAIL_GAPS = (31, 35, 39, 47, 59, 63, 71, 79, 91, 95)


def load_branches() -> list[dict[str, object]]:
    spec = importlib.util.spec_from_file_location("h19_k23_tail_base_branches", BRANCHES)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BRANCHES.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.remaining_branches()


def prime_support(value: int) -> list[int]:
    return sorted(int(prime) for prime in sympy.factorint(value))


def tail_base_invariant(
    branches: list[dict[str, object]], gap: int
) -> dict[str, object]:
    """Return the exact all-branch factor invariant for one proposed tail."""
    denominator = gap + 1
    q, remainder = divmod(denominator, 4)
    if remainder:
        raise ValueError("tail gap is not 3 modulo 4")
    forms = [branch["prime_form"] for branch in branches]
    coefficients = {int(form["coefficient"]) for form in forms}
    if len(coefficients) != 1:
        raise AssertionError("residual branches do not share one affine coefficient")
    coefficient = coefficients.pop()
    constants = [int(form["constant"]) for form in forms]
    available = coefficient % denominator == 0 and all(
        (constant - 1) % denominator == 0 for constant in constants
    )
    row: dict[str, object] = {
        "tail_gap": gap,
        "q": q,
        "tail_denominator": denominator,
        "globally_available": available,
    }
    if not available:
        return row

    slope = coefficient // denominator
    intercepts = [(constant + gap) // denominator for constant in constants]
    uniform_u_factor = math.gcd(slope, *intercepts)
    if any((slope * parameter + intercept) % uniform_u_factor for intercept in intercepts for parameter in range(3)):
        raise AssertionError("computed uniform factor does not divide an affine u value")
    row.update(
        {
            "u_slope": slope,
            "u_intercepts": sorted(intercepts),
            "uniform_u_factor": uniform_u_factor,
            "canonical_base_primes": prime_support(q * uniform_u_factor),
        }
    )
    return row


def run_audit() -> dict[str, object]:
    branches = load_branches()
    if len(branches) != 14:
        raise AssertionError("expected fourteen H19-k23 residual branches")
    rows = [tail_base_invariant(branches, gap) for gap in TAIL_GAPS]
    return {
        "arithmetic": (
            "exact affine divisibility: for p=A*t+C_i and a globally available "
            "m=4q-1, u=(p+m)/(m+1)=a*t+b_i; gcd(a,b_1,...,b_14) is the "
            "maximal integer dividing every u across all branches and parameters"
        ),
        "scope_note": (
            "This extracts bases only for the fixed 14 H19-k23 progressions and "
            "the listed tail gaps. It does not prove a bounded-support selector."
        ),
        "residual_branch_count": len(branches),
        "tail_invariants": rows,
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
