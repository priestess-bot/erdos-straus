#!/usr/bin/env python3
"""Verify fixed low-defect Type II tails on both full pressure rays."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from reproductions import type_ii_square_root_completion_family as family  # noqa: E402


DEFAULT_INPUT = (
    ROOT
    / "reproductions"
    / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "h19-k23-unbridged-pressure-full-low-defect-rays.json"
)
SELECTORS = {
    2_220_549_727_681_245_601: {
        "q": 15,
        "gap": 59,
        "divisor": 37_845,
    },
    748_375_048_866_405_601: {
        "q": 90,
        "gap": 359,
        "divisor": 121_014,
    },
}


def prime_support(value: int) -> set[int]:
    """Return the distinct prime support of a positive integer."""
    if value < 1:
        raise ValueError("value must be positive")
    return {int(prime) for prime in sympy.factorint(value)}


def verify_certificate(prime: int, q: int, divisor: int) -> dict[str, object]:
    """Replay one ordinary Type II certificate and its strict source identity."""
    gap = 4 * q - 1
    normalized = family.verify_normal_form(prime, gap, divisor)
    parameter = int(normalized["parameter"])
    checked = family.two_tail_witness(q, divisor, parameter)
    if checked["prime"] != prime:
        raise AssertionError("normal-form and completed-divisor primes disagree")

    x = q * (parameter + 1)
    first_tail, remainder = divmod(prime * (x + divisor), gap)
    if remainder:
        raise AssertionError("first Type II tail is not integral")
    second_tail, remainder = divmod(prime * (x + x * x // divisor), gap)
    if remainder or first_tail % prime or second_tail % prime:
        raise AssertionError("Type II tails do not descend through the prime")
    source = parameter + 1
    source_terms = [x, first_tail // prime, second_tail // prime]
    target_terms = [x, first_tail, second_tail]
    if Fraction(4, prime) != sum(
        (Fraction(1, value) for value in target_terms), Fraction()
    ):
        raise AssertionError("target Erdős--Straus identity failed")
    if Fraction(4, source) != sum(
        (Fraction(1, value) for value in source_terms), Fraction()
    ):
        raise AssertionError("strict source identity failed")
    if not 2 <= source < prime:
        raise AssertionError("ordinary Type II source is not a strict descent")
    return {
        "parameter": parameter,
        "prime": prime,
        "x": x,
        "divisor": divisor,
        "target_denominators": target_terms,
        "source_denominator": source,
        "source_denominators": source_terms,
        "target_identity_verified": True,
        "source_identity_verified": True,
        "strict_source_descent": True,
    }


def verify_full_ray(row: dict[str, object], selector: dict[str, int]) -> dict[str, object]:
    """Prove that one fixed divisor works on an unrefined pressure ray."""
    prime_seed = int(row["prime_seed"])
    prime_step = int(row["pressure_prime_coefficient"])
    q = int(selector["q"])
    gap = int(selector["gap"])
    divisor = int(selector["divisor"])
    if gap != 4 * q - 1:
        raise AssertionError("stored gap does not equal 4q-1")
    if row["fixed_factor_bridge"] is not None:
        raise AssertionError("selected pressure ray is not an unbridged row")
    if prime_seed % 24 != 1 or prime_step % 24:
        raise AssertionError("pressure ray does not remain in the core residue class")
    if math.gcd(prime_seed, prime_step) != 1:
        raise AssertionError("pressure ray is not primitive")

    b_seed, b_remainder = divmod(prime_seed - 1, 4)
    b_step, step_remainder = divmod(prime_step, 4)
    if b_remainder or step_remainder:
        raise AssertionError("affine (p-1)/4 parameters are not integral")
    if b_seed % q or b_step % q:
        raise AssertionError("q does not divide every affine B(n)")
    x_seed = b_seed + q
    if x_seed * x_seed % divisor or b_step % divisor:
        raise AssertionError("divisor does not divide every affine x(n)^2")
    if (x_seed + divisor) % gap or b_step % gap:
        raise AssertionError("divisor loses the target residue along the ray")
    if divisor > x_seed or math.gcd(divisor, gap) != 1:
        raise AssertionError("divisor violates the Type II size or unit guard")

    new_support = sorted(prime_support(divisor) - prime_support(q))
    if len(new_support) > 2:
        raise AssertionError("fixed tail exceeds support defect two")
    seed_witness = verify_certificate(prime_seed, q, divisor)
    next_witness = verify_certificate(prime_seed + prime_step, q, divisor)
    return {
        "progression_scope": "full_original_pressure_ray",
        "uses_original_pressure_step": True,
        "step_refinement_multiplier": 1,
        "prime_seed": prime_seed,
        "prime_step": prime_step,
        "prime_seed_mod_24": prime_seed % 24,
        "prime_step_mod_24": prime_step % 24,
        "primitive_progression_gcd": math.gcd(prime_seed, prime_step),
        "b_seed": b_seed,
        "b_step": b_step,
        "q": q,
        "gap": gap,
        "divisor": divisor,
        "divisor_factorization": {
            str(prime): int(exponent)
            for prime, exponent in sympy.factorint(divisor).items()
        },
        "new_support": new_support,
        "witness_new_support_size": len(new_support),
        "selector_defect_upper_bound": len(new_support),
        "q_divides_b_seed_and_step": True,
        "divisor_divides_x_seed_squared_and_b_step": True,
        "gap_divides_x_seed_plus_divisor_and_b_step": True,
        "divisor_at_most_x_seed": True,
        "seed_witness": seed_witness,
        "next_parameter_witness": next_witness,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Extract and verify both complete original rays from the bridge artifact."""
    rows = {int(row["prime_seed"]): row for row in payload["rows"]}
    missing = sorted(set(SELECTORS) - set(rows))
    if missing:
        raise AssertionError(f"missing pressure seeds: {missing}")
    verified = [
        verify_full_ray(rows[seed], selector)
        for seed, selector in SELECTORS.items()
    ]
    return {
        "input_artifact": DEFAULT_INPUT.name,
        "arithmetic": (
            "exact affine divisibility and residue invariants on the unrefined "
            "pressure steps; exact support counts; primitive progression gcds; "
            "and target/source Type II identities at n=0 and n=1"
        ),
        "scope_note": (
            "The fixed witness applies to every n>=0 on each full original pressure "
            "ray, not only to a periodically refined subray. Dirichlet supplies "
            "infinitely many prime values on each primitive ray."
        ),
        "full_original_ray_count": len(verified),
        "all_rays_use_original_pressure_step": all(
            row["uses_original_pressure_step"] for row in verified
        ),
        "all_rays_primitive": all(
            row["primitive_progression_gcd"] == 1 for row in verified
        ),
        "all_selector_defect_upper_bounds_at_most_two": all(
            row["selector_defect_upper_bound"] <= 2 for row in verified
        ),
        "witness_new_support_size_histogram": {
            str(size): sum(row["witness_new_support_size"] == size for row in verified)
            for size in sorted(
                {int(row["witness_new_support_size"]) for row in verified}
            )
        },
        "rays": verified,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
