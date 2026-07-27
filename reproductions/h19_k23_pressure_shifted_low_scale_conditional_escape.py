#!/usr/bin/env python3
"""Combine stationary sources and low-scale shifted factor states on one pressure ray."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-shifted-low-scale-conditional-escape-2097152.json"
TARGET_SEED = 748_375_048_866_405_601
MAX_SHIFTED_SCALE = 1_000


def primitive_admissibility(forms: list[tuple[int, int]]) -> tuple[bool, list[dict[str, int]]]:
    """Check the finite local obstruction condition for affine prime forms."""
    if any(coefficient <= 0 or constant <= 0 or math.gcd(coefficient, constant) != 1 for coefficient, constant in forms):
        return False, []
    rows = []
    for prime in sympy.primerange(2, len(forms) + 1):
        roots = set()
        for coefficient, constant in forms:
            if coefficient % prime:
                roots.add((-constant * pow(coefficient, -1, prime)) % prime)
            elif constant % prime == 0:
                return False, []
        rows.append({"prime": int(prime), "root_count": len(roots)})
        if len(roots) == prime:
            return False, rows
    return True, rows


def stationary_standard_row(
    prime: int, coefficient: int, refinement: int, scale: int
) -> tuple[dict[str, object], tuple[int, int]]:
    """Verify complete standard-source failure under a prime quotient."""
    q = 4 * scale - 1
    source_coefficient = q * coefficient * refinement // (4 * scale)
    source_constant = (q * prime + 1) // (4 * scale)
    fixed_factor = math.gcd(source_coefficient, source_constant)
    quotient_coefficient = source_coefficient // fixed_factor
    quotient_constant = source_constant // fixed_factor
    if quotient_coefficient % q:
        raise AssertionError("standard quotient residue is not fixed after refinement")
    fixed_product = scale * fixed_factor
    residues = {1}
    for factor, exponent in sympy.factorint(fixed_product).items():
        residues = {
            residue * pow(int(factor), power, q) % q
            for residue in residues
            for power in range(2 * int(exponent) + 1)
        }
    quotient_residue = quotient_constant % q
    full_residues = {
        residue * pow(quotient_residue, power, q) % q
        for residue in residues
        for power in range(3)
    }
    target = (-fixed_product * quotient_residue) % q
    if target in full_residues:
        raise AssertionError("refined stationary source has a complete divisor witness")
    return (
        {
            "scale": scale,
            "source_modulus": q,
            "fixed_source_factor": fixed_factor,
            "quotient_residue_mod_q": quotient_residue,
            "complete_divisor_residue_count": len(full_residues),
            "target_residue": target,
            "quotient_form": {"coefficient": quotient_coefficient, "constant": quotient_constant},
        },
        (quotient_coefficient, quotient_constant),
    )


def shifted_states(prime: int, coefficient: int) -> list[tuple[int, int, int, int, int]]:
    """List low-scale shifted states satisfying the established factor criterion's prerequisites."""
    states = []
    for scale in range(1, MAX_SHIFTED_SCALE + 1):
        if coefficient % (4 * scale):
            continue
        q = 4 * scale - 1
        shift = prime % (4 * scale)
        if not shift or shift == 1 or (scale * q) % shift:
            continue
        source_coefficient = q * coefficient // (4 * scale)
        source_constant = (q * prime + shift) // (4 * scale)
        if source_coefficient % shift or source_constant % shift:
            continue
        states.append((scale, q, shift, source_coefficient, source_constant))
    return states


def shifted_factor_row(
    state: tuple[int, int, int, int, int], refinement: int
) -> tuple[dict[str, object], tuple[int, int]]:
    """Exclude every eventual prime-quotient witness in the shifted factor form.

    For n=F*L with L a sufficiently large prime, a divisor f of n satisfying
    shift|k*f must use a fixed divisor f0 of F: a remaining factor of shift
    cannot be supplied by the growing prime L.  The two possible f are f0
    and f0*L, and are exhaustively checked against n/f=-1 mod q.
    """
    scale, q, shift, source_coefficient, source_constant = state
    source_coefficient *= refinement
    fixed_factor = math.gcd(source_coefficient, source_constant)
    quotient_coefficient = source_coefficient // fixed_factor
    quotient_constant = source_constant // fixed_factor
    if quotient_coefficient % q:
        raise AssertionError("shifted quotient residue is not fixed after refinement")
    quotient_residue = quotient_constant % q
    surviving_factor_cases = []
    for fixed_divisor in sympy.divisors(fixed_factor):
        fixed_divisor = int(fixed_divisor)
        if (scale * fixed_divisor) % shift:
            continue
        if (fixed_factor // fixed_divisor * quotient_residue) % q == q - 1:
            surviving_factor_cases.append("fixed")
        if (fixed_factor // fixed_divisor) % q == q - 1:
            surviving_factor_cases.append("quotient")
    if surviving_factor_cases:
        raise AssertionError("shifted factor criterion survived the prime quotient")
    return (
        {
            "scale": scale,
            "shift": shift,
            "source_modulus": q,
            "fixed_source_factor": fixed_factor,
            "quotient_residue_mod_q": quotient_residue,
            "factor_form_witness_case_count": 0,
            "quotient_form": {"coefficient": quotient_coefficient, "constant": quotient_constant},
        },
        (quotient_coefficient, quotient_constant),
    )


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compile all stationary and low shifted states into one conditional escape tuple."""
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    stationary_gcd = math.gcd((prime - 1) // 4, coefficient // 4)
    stationary_scales = [int(scale) for scale in sympy.divisors(stationary_gcd)]
    raw_shifted_states = shifted_states(prime, coefficient)
    refinement = math.lcm(*(state[1] for state in raw_shifted_states))
    standard_rows_and_forms = [
        stationary_standard_row(prime, coefficient, refinement, scale)
        for scale in stationary_scales
    ]
    shifted_rows_and_forms = [
        shifted_factor_row(state, refinement) for state in raw_shifted_states
    ]
    form_labels: dict[tuple[int, int], list[str]] = {(coefficient * refinement, prime): ["p"]}
    for entry, form in standard_rows_and_forms:
        form_labels.setdefault(form, []).append(f"standard-k={entry['scale']}")
    for entry, form in shifted_rows_and_forms:
        form_labels.setdefault(form, []).append(f"shifted-k={entry['scale']}")
    forms = list(form_labels)
    admissible, local_rows = primitive_admissibility(forms)
    if not admissible:
        raise AssertionError("combined stationary and shifted tuple is locally obstructed")
    return {
        "arithmetic": (
            "a common parameter refinement freezes all low-scale shifted quotient "
            "residues; it then exactly enumerates complete standard-source divisor "
            "residues and both possible prime-quotient cases of the shifted factor form"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, sufficiently large simultaneous "
            "prime values escape all 72 stationary standard sources and every shifted "
            "factor-form state with k<=1000 satisfying the stated prerequisites. This does "
            "not exclude general shifted Type I certificates outside that factor form."
        ),
        "seed_prime": prime,
        "parameter_refinement": refinement,
        "stationary_standard_scale_count": len(stationary_scales),
        "low_scale_shifted_state_count": len(raw_shifted_states),
        "unique_affine_prime_form_count": len(forms),
        "tuple_is_primitive_and_admissible": admissible,
        "local_admissibility": local_rows,
        "form_labels": [
            {"coefficient": form[0], "constant": form[1], "labels": labels}
            for form, labels in form_labels.items()
        ],
        "stationary_standard_rows": [entry for entry, _ in standard_rows_and_forms],
        "shifted_factor_rows": [entry for entry, _ in shifted_rows_and_forms],
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
    print(json.dumps({key: value for key, value in result.items() if key not in {"form_labels", "stationary_standard_rows", "shifted_factor_rows"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
