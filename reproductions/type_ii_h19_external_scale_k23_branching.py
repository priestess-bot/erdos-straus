#!/usr/bin/env python3
"""Classify the first nontrivial covered scale branch after H19 renewal.

In the c=2 child of the k=10 modulus-5 renewal, all stationary scales are
the divisors of 1800.  Restricting its parameter to enable k=23 yields

    p = 6*Q19*(115*v + 47) + 8328961.

The H19 fan plus all 36 stationary sources and k=23 has covering prime 29.
This script splits v modulo 29 and classifies every child without stopping
after its first outcome: a child can have a direct H19 certificate, a strict
complete external-source descent, both, be nonprimitive, or remain an
admissible conditional escape state.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-h19-external-scale-k23-branching.json"
RENEWAL_SCRIPT = (
    ROOT / "reproductions" / "type_ii_h19_external_scale_renewal.py"
)


def load_renewal():
    spec = importlib.util.spec_from_file_location(
        "h19_external_scale_renewal", RENEWAL_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load H19 scale renewal script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


renewal = load_renewal()
boundary = renewal.boundary
external = renewal.external

SCALES = renewal.divisors(1800) + (23,)
PARAMETER_SCALE = 115
PARAMETER_OFFSET = 47
SPLIT_PRIME = 29


def positive_divisors(value: int) -> tuple[int, ...]:
    return renewal.divisors(value)


def source_profile(
    coefficient: int, constant: int, scale: int
) -> tuple[dict[str, object], tuple[int, int, str]]:
    """Return a source state, including a target hit instead of raising."""
    q = 4 * scale - 1
    denominator = 4 * scale
    if coefficient % denominator or (q * constant + 1) % denominator:
        raise AssertionError("source does not persist throughout this branch")
    source_coefficient = q * coefficient // denominator
    source_constant = (q * constant + 1) // denominator
    fixed_factor = math.gcd(source_coefficient, source_constant)
    quotient_coefficient = source_coefficient // fixed_factor
    quotient_constant = source_constant // fixed_factor
    quotient_residue = quotient_constant % q
    base_factor = scale * fixed_factor
    base_residues = boundary.residue.divisor_residues_from_factorization(
        tuple(
            (prime, 2 * exponent)
            for prime, exponent in boundary.prime_factors(base_factor)
        ),
        q,
    )
    divisor_residues = {
        value * pow(quotient_residue, exponent, q) % q
        for value in base_residues
        for exponent in range(3)
    }
    target = (-base_factor * quotient_residue) % q
    target_hits: list[dict[str, int]] = []
    for divisor in positive_divisors(base_factor * base_factor):
        for exponent in range(3):
            if divisor * pow(quotient_residue, exponent, q) % q == target:
                target_hits.append(
                    {
                        "base_divisor": divisor,
                        "quotient_exponent": exponent,
                    }
                )
    if bool(target_hits) != (target in divisor_residues):
        raise AssertionError("source residue witness mismatch")
    return (
        {
            "k": scale,
            "q": q,
            "fixed_factor": fixed_factor,
            "target_residue": target,
            "divisor_residue_count": len(divisor_residues),
            "target_hits": target_hits,
        },
        (quotient_coefficient, quotient_constant, f"n_k={scale}"),
    )


def ray_hits(coefficient: int, constant: int) -> list[dict[str, object]]:
    """Return explicit H19 divisor forms that meet a Type II ray target."""
    result: list[dict[str, object]] = []
    for shift, a, c in boundary.canonical_fan(19):
        ray_modulus = 4 * a * c
        fixed_factor = boundary.forced_divisor(coefficient, constant, shift)
        quotient_coefficient = coefficient // fixed_factor
        quotient_constant = (constant + 4 * shift) // fixed_factor
        if quotient_coefficient % ray_modulus:
            raise AssertionError("ray quotient residue must be parameter-independent")
        target = ray_modulus - 1
        for divisor in positive_divisors(fixed_factor):
            if divisor % ray_modulus == target:
                result.append(
                    {
                        "shift": shift,
                        "ray_modulus": ray_modulus,
                        "fixed_factor": fixed_factor,
                        "divisor_form": {
                            "coefficient": 0,
                            "constant": divisor,
                        },
                    }
                )
            if divisor * (quotient_constant % ray_modulus) % ray_modulus == target:
                result.append(
                    {
                        "shift": shift,
                        "ray_modulus": ray_modulus,
                        "fixed_factor": fixed_factor,
                        "divisor_form": {
                            "coefficient": divisor * quotient_coefficient,
                            "constant": divisor * quotient_constant,
                        },
                    }
                )
    return result


def branch(residue_class: int) -> dict[str, object]:
    """Classify v=SPLIT_PRIME*w+residue_class in the covered parent."""
    parameter_scale = PARAMETER_SCALE * SPLIT_PRIME
    parameter_offset = PARAMETER_OFFSET + PARAMETER_SCALE * residue_class
    coefficient = 6 * 77_597_520 * parameter_scale
    constant = 6 * 77_597_520 * parameter_offset + renewal.H19_RESIDUE
    primitive = constant % 24 == 1 and math.gcd(coefficient, constant) == 1
    result: dict[str, object] = {
        "v_mod_29": residue_class,
        "parameter_scale": parameter_scale,
        "parameter_offset": parameter_offset,
        "prime_form": {"coefficient": coefficient, "constant": constant},
        "primitive_core_prime_form": primitive,
        "prime_form_gcd": math.gcd(coefficient, constant),
    }
    if not primitive:
        result.update(
            {
                "h19_ray_hits": [],
                "source_hits": [],
                "combined_form_count": 0,
                "covering_primes": [],
                "admissible_escape": False,
            }
        )
        return result

    h19_hits = ray_hits(coefficient, constant)
    source_rows: list[dict[str, object]] = []
    source_forms: list[tuple[int, int, str]] = []
    for scale in SCALES:
        row, form = source_profile(coefficient, constant, scale)
        source_rows.append(row)
        source_forms.append(form)
    sources_with_hits = [row for row in source_rows if row["target_hits"]]

    h19_forms = boundary.affine_forms(
        constant, coefficient, boundary.canonical_fan(19)
    )
    forms = h19_forms + tuple(source_forms)
    covering = list(boundary.covering_primes(forms))
    admissible = not h19_hits and not sources_with_hits and not covering
    result.update(
        {
            "h19_ray_hits": h19_hits,
            "source_hits": sources_with_hits,
            "combined_form_count": len(forms),
            "covering_primes": covering,
            "admissible_escape": admissible,
        }
    )
    return result


def run_audit() -> dict[str, object]:
    """Build the parent cover and its complete residue-class partition."""
    parent = renewal.state(PARAMETER_SCALE, PARAMETER_OFFSET, SCALES)
    if parent["covering_primes"] != [SPLIT_PRIME]:
        raise AssertionError("the k=23 parent must have exactly the 29 cover")
    root_map = renewal.covering_root_map(parent["forms"], SPLIT_PRIME)
    branches = [branch(residue_class) for residue_class in range(SPLIT_PRIME)]
    histogram = {
        "nonprimitive": sum(
            not branch["primitive_core_prime_form"] for branch in branches
        ),
        "h19_ray_certificate": sum(
            bool(branch["h19_ray_hits"]) for branch in branches
        ),
        "external_source_descent": sum(
            bool(branch["source_hits"]) for branch in branches
        ),
        "admissible_escape": sum(
            bool(branch["admissible_escape"]) for branch in branches
        ),
    }
    resolved = sum(
        (not branch["primitive_core_prime_form"])
        or bool(branch["h19_ray_hits"])
        or bool(branch["source_hits"])
        for branch in branches
    )
    if histogram != {
        "nonprimitive": 1,
        "h19_ray_certificate": 5,
        "external_source_descent": 9,
        "admissible_escape": 18,
    }:
        raise AssertionError("unexpected k=23 covered-branch classification")
    if resolved != 11:
        raise AssertionError("the covered split must have eleven resolved children")

    return {
        "arithmetic": (
            "exact forced-factor extraction, complete square-divisor source "
            "residue sets, explicit ray-divisor forms, and a complete split "
            "of the locally covered parameter modulo 29"
        ),
        "scope_note": (
            "An admissible child is conditional on Dickson's prime-tuples "
            "conjecture or Schinzel's Hypothesis H. Certificate and descent "
            "children are exact arithmetic exits, not prime-tuple assumptions."
        ),
        "path": {
            "from_k10_renewal_child": 2,
            "stationary_scale_gcd": 1800,
            "stationary_scales": list(renewal.divisors(1800)),
            "enabled_scale": 23,
            "parent_progression": "p=6*Q19*(115*v+47)+8328961",
        },
        "parent": parent,
        "covering_root_map_mod_29": root_map,
        "branches": branches,
        "histogram": histogram,
        "resolved_branch_count": resolved,
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
