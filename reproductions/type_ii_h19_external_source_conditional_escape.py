#!/usr/bin/env python3
"""Build a conditional escape from H19 and six complete source descents.

Starting from the H19-safe residue p=8328961 modulo Q19, take the n=3m
second-level branch. Alongside the twenty H19 one-prime-cofactor forms, add
the prime quotient forms for n_k at k=1,2,3,4,5,6. Their fixed source factors
make every complete quadratic external-source divisor-residue condition fail.

The resulting 26 affine forms have no covering prime. Dickson's conjecture
or Schinzel's Hypothesis H would therefore yield infinitely many actual
primes escaping both this fixed Type II fan and these four strict-descent
families.  This is a conditional boundary, never a counterexample to
Erdos--Straus.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT
    / "reproductions"
    / "type-ii-h19-external-source-conditional-escape-results.json"
)
BOUNDARY_SCRIPT = ROOT / "reproductions" / "type_ii_prime_cofactor_boundary.py"

H19_RESIDUE = 8_328_961
SECOND_LEVEL_BRANCH = 0
SCALES = (1, 2, 3, 4, 5, 6)


def load_boundary():
    spec = importlib.util.spec_from_file_location(
        "h19_external_source_conditional_boundary", BOUNDARY_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_prime_cofactor_boundary.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


boundary = load_boundary()


def source_state(
    residue_class: int, modulus: int, branch: int, scale: int
) -> tuple[dict[str, object], tuple[int, int, str]]:
    """Return the source-prime quotient form and its full quadratic failure."""
    q = 4 * scale - 1
    denominator = 4 * scale
    coefficient = q * 3 * modulus // denominator
    constant = (q * (modulus * branch + residue_class) + 1) // denominator
    if (
        q * 3 * modulus % denominator
        or (q * (modulus * branch + residue_class) + 1) % denominator
    ):
        raise AssertionError("source form is not integral")
    fixed_factor = math.gcd(coefficient, constant)
    quotient_coefficient = coefficient // fixed_factor
    quotient_constant = constant // fixed_factor
    quotient_residue = quotient_constant % q
    base_residues = boundary.residue.divisor_residues_from_factorization(
        tuple(
            (prime, 2 * exponent)
            for prime, exponent in boundary.prime_factors(scale * fixed_factor)
        ),
        q,
    )
    divisor_residues = {
        value * pow(quotient_residue, exponent, q) % q
        for value in base_residues
        for exponent in range(3)
    }
    target = (-scale * fixed_factor * quotient_residue) % q
    if target in divisor_residues:
        raise AssertionError("the selected source must fail its complete tail")
    return (
        {
            "k": scale,
            "q": q,
            "fixed_factor": fixed_factor,
            "fixed_factorization": [
                {"prime": prime, "exponent": exponent}
                for prime, exponent in boundary.prime_factors(fixed_factor)
            ],
            "quotient_residue_mod_q": quotient_residue,
            "target_residue": target,
            "divisor_residues": sorted(divisor_residues),
            "coefficient": quotient_coefficient,
            "constant": quotient_constant,
        },
        (quotient_coefficient, quotient_constant, f"n_k={scale}"),
    )


def run_witness() -> dict[str, object]:
    """Return the exact H19 plus six-source conditional escape witness."""
    fan = boundary.canonical_fan(19)
    modulus = boundary.fan_modulus(fan)
    if modulus != 77_597_520:
        raise AssertionError("unexpected H19 modulus")
    if not all(
        boundary.ray_safe_with_one_prime_cofactor(
            H19_RESIDUE, modulus, shift, a, c
        )
        for shift, a, c in fan
    ):
        raise AssertionError("seed must be H19-safe at the first level")
    second_level = boundary.second_level_branch(
        H19_RESIDUE, SECOND_LEVEL_BRANCH, modulus, fan
    )
    if second_level is None:
        raise AssertionError("selected H19 branch must survive the ray test")
    h19_forms, h19_factors = second_level
    if boundary.covering_primes(h19_forms):
        raise AssertionError("the H19 branch must be admissible")
    source_rows: list[dict[str, object]] = []
    source_forms: list[tuple[int, int, str]] = []
    for scale in SCALES:
        row, form = source_state(
            H19_RESIDUE, modulus, SECOND_LEVEL_BRANCH, scale
        )
        source_rows.append(row)
        source_forms.append(form)
    forms = h19_forms + tuple(source_forms)
    covering = boundary.covering_primes(forms)
    if covering:
        raise AssertionError("combined H19 and source forms must be admissible")
    return {
        "arithmetic": (
            "exact forced-factor extraction, complete square-divisor residue "
            "sets for the six sources, and finite-field admissibility of all "
            "displayed affine forms"
        ),
        "scope_note": (
            "Conditional statement only. Dickson's prime-tuples conjecture or "
            "Schinzel's Hypothesis H is required to obtain infinitely many "
            "actual primes. This is not a counterexample to Erdos--Straus."
        ),
        "h19": {
            "modulus": modulus,
            "residue_class": H19_RESIDUE,
            "second_level_branch": SECOND_LEVEL_BRANCH,
            "fixed_factors": list(h19_factors),
            "form_count": len(h19_forms),
        },
        "sources": source_rows,
        "combined_form_count": len(forms),
        "covering_primes": list(covering),
        "forms": [
            {"coefficient": coefficient, "constant": constant, "label": label}
            for coefficient, constant, label in forms
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_witness()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
