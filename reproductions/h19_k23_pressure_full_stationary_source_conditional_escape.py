#!/usr/bin/env python3
"""Build a Dickson escape from every stationary source scale on one pressure ray."""

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
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-full-stationary-source-conditional-escape-2097152.json"
TARGET_SEED = 748_375_048_866_405_601


def primitive_admissibility(forms: list[tuple[int, int]]) -> tuple[bool, list[dict[str, int]]]:
    """Check the complete local condition for a finite affine prime tuple."""
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


def source_escape_row(prime: int, coefficient: int, scale: int) -> tuple[dict[str, object], tuple[int, int]]:
    """Return one source quotient form whose prime values force scale k to fail."""
    q = 4 * scale - 1
    source_coefficient, remainder = divmod(q * coefficient, 4 * scale)
    source_constant, remainder_constant = divmod(q * prime + 1, 4 * scale)
    if remainder or remainder_constant:
        raise AssertionError("scale is not stationary on the pressure ray")
    fixed_factor = math.gcd(source_coefficient, source_constant)
    quotient_coefficient = source_coefficient // fixed_factor
    quotient_constant = source_constant // fixed_factor
    if quotient_coefficient % q:
        raise AssertionError("source quotient residue is not fixed")
    fixed_product = scale * fixed_factor
    fixed_residues = {1}
    for factor, exponent in sympy.factorint(fixed_product).items():
        fixed_residues = {
            residue * pow(int(factor), power, q) % q
            for residue in fixed_residues
            for power in range(2 * int(exponent) + 1)
        }
    quotient_residue = quotient_constant % q
    full_residues = {
        residue * pow(quotient_residue, power, q) % q
        for residue in fixed_residues
        for power in range(3)
    }
    target = (-fixed_product * quotient_residue) % q
    if target in full_residues:
        raise AssertionError("prime source quotient leaves a stationary source witness")
    return (
        {
            "scale": scale,
            "source_modulus": q,
            "fixed_source_factor": fixed_factor,
            "fixed_source_factorization": {
                str(factor): int(exponent)
                for factor, exponent in sorted(sympy.factorint(fixed_factor).items())
            },
            "quotient_residue_mod_q": quotient_residue,
            "target_residue": target,
            "complete_source_divisor_residue_count": len(full_residues),
            "quotient_form": {
                "coefficient": quotient_coefficient,
                "constant": quotient_constant,
            },
        },
        (quotient_coefficient, quotient_constant),
    )


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compile p and all stationary source quotients into one admissible tuple."""
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    if row["fixed_factor_bridge"] is not None:
        raise AssertionError("target must be a fixed-factor bridge miss")
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    stationary_gcd = math.gcd((prime - 1) // 4, coefficient // 4)
    scales = [int(scale) for scale in sympy.divisors(stationary_gcd)]
    source_rows_and_forms = [source_escape_row(prime, coefficient, scale) for scale in scales]
    source_rows = [item[0] for item in source_rows_and_forms]
    forms = [(coefficient, prime)] + [item[1] for item in source_rows_and_forms]
    if len(set(forms)) != len(forms):
        raise AssertionError("stationary source tuple has duplicate forms")
    admissible, local_rows = primitive_admissibility(forms)
    if not admissible:
        raise AssertionError("full stationary source tuple is locally obstructed")
    return {
        "arithmetic": (
            "exact fixed-factor extraction for every stationary standard external-source "
            "scale, complete divisor-residue enumeration of (k*F*L)^2 under a prime "
            "quotient L, and finite-field admissibility of p plus all source quotients"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, sufficiently large simultaneous "
            "prime values of this tuple escape every stationary standard external-source "
            "descent on the displayed pressure ray. This does not exclude nonstationary "
            "or shifted sources, nor other descent families."
        ),
        "seed_prime": prime,
        "stationary_scale_gcd": stationary_gcd,
        "stationary_scale_count": len(scales),
        "affine_prime_form_count": len(forms),
        "tuple_is_primitive_and_admissible": admissible,
        "local_admissibility": local_rows,
        "source_rows": source_rows,
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
    print(json.dumps({key: value for key, value in result.items() if key != "source_rows"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
