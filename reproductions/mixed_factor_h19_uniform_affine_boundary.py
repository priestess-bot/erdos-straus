#!/usr/bin/env python3
"""Exhaust uniform affine mixed-factor lifts on the 14 H19-k23 residuals.

For a stationary external scale k, write its source denominator as

    n_k=F*(u*n+v),  q=4*k-1.

Every positive nonconstant affine g that divides k*n_k for every parameter
has the rigid form g=b*(u*n+v), b|kF.  It gives the mixed-factor strict lift
exactly when b<=F and q divides both b*u and b*v+1.  Hence each source has a
finite, complete divisor audit.  This script applies it to the 14 branches
remaining after the uniform affine Type I/II certificate audits.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "mixed-factor-h19-uniform-affine-boundary.json"
BRANCHING_SCRIPT = ROOT / "reproductions" / "type_ii_h19_external_scale_k23_branching.py"
TYPE_I_SCRIPT = ROOT / "reproductions" / "type_i_h19_affine_uniform_square_audit.py"
TYPE_II_SCRIPT = ROOT / "reproductions" / "type_ii_h19_affine_square_uniform_audit.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


branching = load_module("h19_k23_branching_for_mixed_boundary", BRANCHING_SCRIPT)
type_i = load_module("h19_type_i_affine_for_mixed_boundary", TYPE_I_SCRIPT)
type_ii = load_module("h19_type_ii_affine_for_mixed_boundary", TYPE_II_SCRIPT)


def verify_witness(
    coefficient: int, constant: int, scale: int, fixed_factor: int, multiplier: int
) -> None:
    """Check a proposed uniform mixed-factor lift on symbolic samples."""
    q = 4 * scale - 1
    source_coefficient = q * coefficient // (4 * scale)
    source_constant = (q * constant + 1) // (4 * scale)
    quotient_coefficient = source_coefficient // fixed_factor
    quotient_constant = source_constant // fixed_factor
    if (
        multiplier * quotient_coefficient % q
        or (multiplier * quotient_constant + 1) % q
    ):
        raise AssertionError("mixed-factor congruence is not uniform")

    for parameter in range(4):
        prime_candidate = coefficient * parameter + constant
        source = source_coefficient * parameter + source_constant
        private_part = quotient_coefficient * parameter + quotient_constant
        factor = multiplier * private_part
        if scale * source % factor or factor > source or factor % q != q - 1:
            raise AssertionError("invalid mixed factor")
        first_tail = scale * (source + factor) // q
        second_tail = source * first_tail // factor
        if Fraction(4, source) != (
            Fraction(1, scale * source)
            + Fraction(1, first_tail)
            + Fraction(1, second_tail)
        ):
            raise AssertionError("source identity failed")
        if Fraction(4, prime_candidate) != (
            Fraction(1, scale * source * prime_candidate)
            + Fraction(1, first_tail)
            + Fraction(1, second_tail)
        ):
            raise AssertionError("strict lift identity failed")


def source_audit(coefficient: int, constant: int, scale: int) -> dict[str, object]:
    """Exhaust uniform affine mixed factors at one stationary source scale."""
    q = 4 * scale - 1
    denominator = 4 * scale
    if coefficient % denominator or (q * constant + 1) % denominator:
        raise AssertionError("scale is not stationary on this progression")
    source_coefficient = q * coefficient // denominator
    source_constant = (q * constant + 1) // denominator
    fixed_factor = math.gcd(source_coefficient, source_constant)
    quotient_coefficient = source_coefficient // fixed_factor
    quotient_constant = source_constant // fixed_factor
    candidates = [
        value
        for value in branching.positive_divisors(scale * fixed_factor)
        if value <= fixed_factor
    ]
    hits = []
    for multiplier in candidates:
        if (
            multiplier * quotient_coefficient % q == 0
            and (multiplier * quotient_constant + 1) % q == 0
        ):
            verify_witness(
                coefficient, constant, scale, fixed_factor, multiplier
            )
            hits.append(multiplier)
    return {
        "k": scale,
        "q": q,
        "fixed_factor": fixed_factor,
        "candidate_multiplier_count": len(candidates),
        "uniform_affine_mixed_factor_hits": hits,
    }


def remaining_branches() -> list[dict[str, object]]:
    """Return exactly the k=23 children not closed by either affine audit."""
    source = branching.run_audit()
    type_i_rows = {
        row["v_mod_29"]: row
        for row in type_i.run_audit()["residual_progressions"]
    }
    type_ii_rows = {
        row["v_mod_29"]: row
        for row in type_ii.run_audit()["residual_progressions"]
    }
    result = []
    for branch in source["branches"]:
        if not branch["admissible_escape"]:
            continue
        residue = branch["v_mod_29"]
        if (
            type_i_rows[residue]["uniform_affine_type_i_certificate"] is None
            and type_ii_rows[residue]["uniform_square_affine_certificate"] is None
        ):
            result.append(branch)
    return result


def run_audit() -> dict[str, object]:
    """Audit every remaining branch and every stationary external scale."""
    branches = remaining_branches()
    rows = []
    for branch in branches:
        form = branch["prime_form"]
        coefficient = int(form["coefficient"])
        constant = int(form["constant"])
        sources = [
            source_audit(coefficient, constant, scale)
            for scale in branching.SCALES
        ]
        if any(source["uniform_affine_mixed_factor_hits"] for source in sources):
            raise AssertionError("unexpected uniform affine mixed-factor lift")
        rows.append(
            {
                "v_mod_29": branch["v_mod_29"],
                "prime_form": form,
                "source_audits": sources,
                "candidate_multiplier_count": sum(
                    source["candidate_multiplier_count"] for source in sources
                ),
            }
        )
    if len(rows) != 14:
        raise AssertionError("expected fourteen post-affine residual branches")
    return {
        "arithmetic": (
            "uniform affine divisor rigidity for g|k*n_k, complete divisors "
            "b|kF with b<=F, and exact source/target unit-fraction checks"
        ),
        "scope_note": (
            "Empty output excludes only one-source mixed-factor lifts whose "
            "selected factor is affine throughout the progression. It does "
            "not exclude nonaffine factors or coupled multi-source descents."
        ),
        "source_state": {
            "claim_id": "type-II-h19-external-scale-k23-branching",
            "post_affine_residual_branch_count": len(rows),
            "stationary_scale_count": len(branching.SCALES),
        },
        "residual_progressions": rows,
        "total_candidate_multiplier_count": sum(
            row["candidate_multiplier_count"] for row in rows
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
