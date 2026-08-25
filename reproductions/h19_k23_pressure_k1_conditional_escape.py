#!/usr/bin/env python3
"""Build conditional k=1 external-source escapes on the two pressure rays."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-k1-conditional-escape-2097152.json"


def primitive_admissible(forms: list[tuple[int, int]]) -> bool:
    """Check local admissibility of a finite positive affine prime tuple."""
    if any(coefficient <= 0 or constant <= 0 or math.gcd(coefficient, constant) != 1 for coefficient, constant in forms):
        return False
    for prime in sympy.primerange(2, len(forms) + 1):
        roots = set()
        for coefficient, constant in forms:
            if coefficient % prime:
                roots.add((-constant * pow(coefficient, -1, prime)) % prime)
            elif constant % prime == 0:
                return False
        if len(roots) == prime:
            return False
    return True


def k1_escape_row(row: dict[str, object]) -> dict[str, object]:
    """Compile p and its k=1 source quotient into a two-form escape tuple."""
    prime = int(row["prime_seed"])
    prime_coefficient = int(row["pressure_prime_coefficient"])
    source_coefficient, remainder = divmod(3 * prime_coefficient, 4)
    source_constant, remainder_constant = divmod(3 * prime + 1, 4)
    if remainder or remainder_constant:
        raise AssertionError("k=1 source is not affine integral")
    fixed_factor = math.gcd(source_coefficient, source_constant)
    quotient_coefficient = source_coefficient // fixed_factor
    quotient_constant = source_constant // fixed_factor
    if quotient_coefficient % 3:
        raise AssertionError("source quotient residue is not fixed modulo three")
    if any(factor % 3 != 1 for factor in sympy.factorint(fixed_factor)):
        raise AssertionError("fixed source factor has a nontrivial modulo-three residue")
    quotient_residue = quotient_constant % 3
    if quotient_residue != 1:
        raise AssertionError("prime source quotient is not one modulo three")
    target = (-source_constant) % 3
    if target != 2:
        raise AssertionError("k=1 target is unexpectedly available")
    fixed_square_residues = {1}
    for factor, exponent in sympy.factorint(fixed_factor).items():
        fixed_square_residues = {
            residue * pow(int(factor), power, 3) % 3
            for residue in fixed_square_residues
            for power in range(2 * int(exponent) + 1)
        }
    full_residues = {
        residue * pow(quotient_residue, power, 3) % 3
        for residue in fixed_square_residues
        for power in range(3)
    }
    if target in full_residues:
        raise AssertionError("prime quotient does not escape the complete k=1 source")
    forms = [(prime_coefficient, prime), (quotient_coefficient, quotient_constant)]
    if not primitive_admissible(forms):
        raise AssertionError("p and source quotient forms are not admissible")
    return {
        "prime_seed": prime,
        "source_fixed_factor": fixed_factor,
        "source_fixed_factorization": {
            str(factor): int(exponent)
            for factor, exponent in sorted(sympy.factorint(fixed_factor).items())
        },
        "source_quotient_residue_mod_3": quotient_residue,
        "source_target_residue_mod_3": target,
        "complete_source_divisor_residues_mod_3": sorted(full_residues),
        "forms": [
            {"label": "p", "coefficient": prime_coefficient, "constant": prime},
            {
                "label": "k1-source-quotient",
                "coefficient": quotient_coefficient,
                "constant": quotient_constant,
            },
        ],
        "tuple_is_primitive_and_admissible": True,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compile every fixed-bridge miss into a conditional k=1 escape tuple."""
    misses = [row for row in payload["rows"] if row["fixed_factor_bridge"] is None]
    rows = [k1_escape_row(row) for row in misses]
    if len(rows) != 2:
        raise AssertionError("expected exactly two fixed-factor bridge misses")
    return {
        "arithmetic": (
            "exact k=1 source factor extraction, complete divisor-residue enumeration "
            "of (F*L)^2 modulo three under a prime quotient L, and local admissibility "
            "checks for each two-form tuple (p,L)"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, each displayed admissible "
            "two-form tuple has infinitely many simultaneous prime values. Those values "
            "escape the complete k=1 external-source descent only; other scales and "
            "other descent families remain available."
        ),
        "pressure_ray_count": len(rows),
        "rows": rows,
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
