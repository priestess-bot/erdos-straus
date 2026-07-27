#!/usr/bin/env python3
"""Find uniform external-source descents on global-tail pressure rays."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
FIRST_POWER_ESCAPE = ROOT / "reproductions" / "h19_k23_global_first_power_conditional_escape.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


escape = load_module("h19_k23_pressure_external_escape", FIRST_POWER_ESCAPE)


def fixed_square_divisor_residues(value: int, modulus: int) -> dict[int, int]:
    """Return the least divisor of value squared in each residue class."""
    residues = {1: 1}
    for factor, exponent in sympy.factorint(value).items():
        factor = int(factor)
        exponent = int(exponent)
        next_residues: dict[int, int] = {}
        for residue, divisor in residues.items():
            for power in range(2 * exponent + 1):
                candidate = divisor * factor**power
                new_residue = residue * pow(factor, power, modulus) % modulus
                previous = next_residues.get(new_residue)
                if previous is None or candidate < previous:
                    next_residues[new_residue] = candidate
        residues = next_residues
    return residues


def verify_strict_lift(prime: int, scale: int, divisor: int) -> dict[str, int]:
    """Verify one complete-square-tail external-source lift exactly."""
    q = 4 * scale - 1
    source, remainder = divmod(q * prime + 1, 4 * scale)
    if remainder:
        raise AssertionError("stationary scale does not give an integral source")
    product = scale * source
    first_tail, remainder = divmod(product + divisor, q)
    if remainder or product * first_tail % divisor:
        raise AssertionError("fixed residue divisor does not yield a square-tail lift")
    second_tail = product * first_tail // divisor
    if not divisor <= product or not source < prime:
        raise AssertionError("external-source lift is not strict")
    if (
        Fraction(4, source)
        != Fraction(1, product) + Fraction(1, first_tail) + Fraction(1, second_tail)
        or Fraction(4, prime)
        != Fraction(1, product * prime)
        + Fraction(1, first_tail)
        + Fraction(1, second_tail)
    ):
        raise AssertionError("external-source identity failed")
    return {
        "source_denominator": source,
        "source_product": product,
        "square_tail_divisor": divisor,
        "first_tail": first_tail,
        "second_tail": second_tail,
    }


def fixed_factor_bridge(prime: int, coefficient: int) -> dict[str, object] | None:
    """Find a stationary scale whose fixed source factor forces a descent.

    If p(n)=prime+coefficient*n and k divides both (prime-1)/4 and
    coefficient/4, then M_k=( (4k-1)p+1 )/4 has constant residue modulo
    4k-1.  Any matching divisor of a fixed factor of M_k works for every n.
    """
    if (prime - 1) % 4 or coefficient % 4:
        raise AssertionError("pressure ray is not a core-prime ray")
    stationary_gcd = math.gcd((prime - 1) // 4, coefficient // 4)
    for scale in sympy.divisors(stationary_gcd):
        scale = int(scale)
        q = 4 * scale - 1
        product_seed, remainder = divmod(q * prime + 1, 4)
        if remainder or product_seed % scale:
            raise AssertionError("stationary source product is not integral")
        product_slope = q * coefficient // 4
        source_fixed_factor = math.gcd(product_slope // scale, product_seed // scale)
        fixed_product_factor = scale * source_fixed_factor
        target = (-product_seed) % q
        residues = fixed_square_divisor_residues(fixed_product_factor, q)
        divisor = residues.get(target)
        if divisor is None or divisor > product_seed:
            continue
        seed_lift = verify_strict_lift(prime, scale, divisor)
        next_lift = verify_strict_lift(prime + coefficient, scale, divisor)
        if (product_slope % q) or fixed_product_factor * fixed_product_factor % divisor:
            raise AssertionError("fixed-factor bridge lost its progression invariant")
        return {
            "stationary_scale": scale,
            "source_modulus": q,
            "stationary_scale_gcd": stationary_gcd,
            "stationary_scale_count": len(sympy.divisors(stationary_gcd)),
            "source_fixed_factor": source_fixed_factor,
            "fixed_source_product_factor": fixed_product_factor,
            "fixed_factor_residue_count": len(residues),
            "fixed_square_tail_divisor": divisor,
            "seed_lift": seed_lift,
            "next_parameter_lift": next_lift,
        }
    return None


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Audit every prime progression that preserves a global-base pressure miss."""
    forms = {
        int(branch["v_mod_29"]): (
            int(branch["prime_form"]["coefficient"]),
            int(branch["prime_form"]["constant"]),
        )
        for branch in escape.base_obstruction.boundary.remaining_branches()
    }
    rows = []
    for family in payload["families"]:
        seed = int(family["prime_seed"])
        branch = int(family["branch_v_mod_29"])
        affine_coefficient, _ = forms[branch]
        coefficient = affine_coefficient * int(family["parameter_period"])
        bridge = fixed_factor_bridge(seed, coefficient)
        rows.append(
            {
                "prime_seed": seed,
                "branch_v_mod_29": branch,
                "pressure_parameter_period": int(family["parameter_period"]),
                "pressure_prime_coefficient": coefficient,
                "fixed_factor_bridge": bridge,
            }
        )
    bridges = [row for row in rows if row["fixed_factor_bridge"] is not None]
    misses = [row for row in rows if row["fixed_factor_bridge"] is None]
    if len(rows) != len(payload["families"]):
        raise AssertionError("pressure-family bridge audit is incomplete")
    return {
        "arithmetic": (
            "for every pressure progression p=p0+Pn, exhaust all stationary "
            "external-source scales k dividing gcd((p0-1)/4,P/4); at each scale "
            "enumerate the complete square-divisor residues of the fixed source "
            "factor and verify strict lifts at n=0 and n=1"
        ),
        "scope_note": (
            "A positive uniform bridge for the listed pressure rays. A miss says only "
            "that no stationary scale has a fixed-factor external-source witness; it "
            "does not exclude variable-factor, shifted, or other descents."
        ),
        "pressure_family_count": len(rows),
        "fixed_factor_bridge_count": len(bridges),
        "fixed_factor_bridge_miss_count": len(misses),
        "unbridged_prime_seeds": [int(row["prime_seed"]) for row in misses],
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
    print(json.dumps({key: value for key, value in result.items() if key != "rows"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
