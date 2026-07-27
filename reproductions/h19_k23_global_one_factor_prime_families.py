#!/usr/bin/env python3
"""Persist the one-new-prime witnesses on global-base pressure progressions."""

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
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-base-only-descent-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-one-factor-prime-families-2097152.json"
BASE_OBSTRUCTION = ROOT / "reproductions" / "h19_k23_global_base_only_prime_obstruction.py"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"
CANONICAL = ROOT / "reproductions" / "h19_k23_canonical_tail_support_defect_audit.py"
NORMAL_FORM = ROOT / "reproductions" / "type_ii_square_root_completion_family.py"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base_obstruction = load_module(
    "h19_k23_global_one_factor_base_obstruction", BASE_OBSTRUCTION
)
global_closure = load_module("h19_k23_global_one_factor_menu", GLOBAL_CLOSURE)
canonical = load_module("h19_k23_global_one_factor_canonical", CANONICAL)
normal_form = load_module("h19_k23_global_one_factor_normal_form", NORMAL_FORM)
boundary = load_module("h19_k23_global_one_factor_branches", BRANCHES)


def one_factor_witness(
    prime: int, gap: int, base_primes: set[int]
) -> tuple[int, int]:
    """Return the canonical divisor and its unique nonbase prime."""
    witness = canonical.support_defect(prime, gap, base_primes, 1)
    if witness is None or int(witness["defect"]) != 1:
        raise AssertionError("pressure record does not have a one-factor witness")
    divisor = int(witness["divisor"])
    nonbase = [
        (int(factor), int(exponent))
        for factor, exponent in sympy.factorint(divisor).items()
        if int(factor) not in base_primes
    ]
    if len(nonbase) != 1 or nonbase[0][1] != 1:
        raise AssertionError("one-factor divisor does not contain exactly one new prime")
    return divisor, nonbase[0][0]


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Freeze both the global base obstruction and its current one-prime rescue."""
    global_factor, bases = global_closure.global_tail_bases()
    forms = {
        int(branch["v_mod_29"]): (
            int(branch["prime_form"]["coefficient"]),
            int(branch["prime_form"]["constant"]),
        )
        for branch in boundary.remaining_branches()
    }
    all_gaps = sorted(bases)
    families = []
    for record in payload["global_base_only_pressure_records"]:
        prime = int(record["prime"])
        gap = int(record["current_global_tail_gap"])
        base = bases[gap]
        divisor, new_prime = one_factor_witness(prime, gap, base)
        residue, coefficient, constant, parameter = base_obstruction.branch_parameter(
            prime, forms
        )
        tail_parameter = (prime - 1) // (gap + 1)
        seed_descent = normal_form.two_tail_witness(
            (gap + 1) // 4, divisor, tail_parameter
        )
        if int(seed_descent["source_denominator"]) != tail_parameter + 1:
            raise AssertionError("seed source denominator is not the tail quotient")
        period, valuation_rows = base_obstruction.period_for_seed(prime, bases)
        u = (prime + gap) // (gap + 1)
        new_exponent = base_obstruction.valuation(u, new_prime)
        if new_exponent < 1:
            raise AssertionError("selected new prime does not divide the tail factor")
        period = math.lcm(period, new_prime ** (new_exponent + 1))
        for row in valuation_rows:
            checked_gap = int(row["tail_gap"])
            if period % checked_gap:
                raise AssertionError("period does not freeze a global target")
            slope = coefficient // (checked_gap + 1)
            original_u = (prime + checked_gap) // (checked_gap + 1)
            shifted_u = original_u + slope * period
            for factor, exponent in row["u_base_valuations"].items():
                factor = int(factor)
                exponent = int(exponent)
                if (slope * period) % factor ** (exponent + 1):
                    raise AssertionError("period does not freeze a base valuation")
                if base_obstruction.valuation(shifted_u, factor) != exponent:
                    raise AssertionError("base valuation changed under the period")
        slope = coefficient // (gap + 1)
        shifted_u = u + slope * period
        if (slope * period) % new_prime ** (new_exponent + 1):
            raise AssertionError("period does not freeze the selected new prime")
        if base_obstruction.valuation(shifted_u, new_prime) != new_exponent:
            raise AssertionError("selected new-prime valuation changed")
        shifted_prime = coefficient * (parameter + period) + constant
        if any(
            base_obstruction.base_only_residue_divisor(
                shifted_prime, checked_gap, bases[checked_gap], False
            )
            is not None
            for checked_gap in all_gaps
        ):
            raise AssertionError("base-only obstruction changed under the period")
        shifted_q = (gap + 1) // 4
        shifted_x = shifted_q * shifted_u
        if divisor > shifted_x or shifted_x * shifted_x % divisor:
            raise AssertionError("one-factor divisor did not persist")
        if divisor % gap != (-shifted_x) % gap:
            raise AssertionError("one-factor target residue did not persist")
        unit_parameter = (shifted_prime - 1) // (gap + 1)
        unit_descent = normal_form.two_tail_witness(
            (gap + 1) // 4, divisor, unit_parameter
        )
        if int(unit_descent["source_denominator"]) != unit_parameter + 1:
            raise AssertionError("unit source denominator is not the tail quotient")
        progression_step = coefficient * period
        if math.gcd(progression_step, prime) != 1:
            raise AssertionError("Dirichlet progression is not primitive")
        if prime % 24 != 1 or progression_step % 24:
            raise AssertionError("progression left the core-prime congruence class")
        families.append(
            {
                "prime_seed": prime,
                "branch_v_mod_29": residue,
                "parameter_seed": parameter,
                "tail_gap": gap,
                "base_primes": sorted(base),
                "one_factor_divisor": divisor,
                "new_prime": new_prime,
                "new_prime_u_valuation": new_exponent,
                "source_denominator": int(seed_descent["source_denominator"]),
                "tail_parameter": tail_parameter,
                "parameter_period": period,
                "prime_progression_offset": prime,
                "prime_progression_step": progression_step,
                "prime_progression_gcd": math.gcd(progression_step, prime),
                "canonical_base_only_miss_gaps": all_gaps,
                "unit_shift_base_only_miss_gaps": all_gaps,
                "unit_shift_one_factor_divisor": divisor,
                "unit_shift_source_denominator": int(
                    unit_descent["source_denominator"]
                ),
                "valuation_constraints": valuation_rows,
            }
        )
    if len(families) != int(payload["global_base_only_pressure_count"]):
        raise AssertionError("not every pressure record produced a one-factor family")
    return {
        "arithmetic": (
            "the all-tail base-only obstruction period is enlarged by "
            "ell^(v_ell(u)+1) for the unique new prime ell in the canonical "
            "one-factor divisor. This freezes the divisor's full prime support, "
            "its Type II target residue, and the zero-support miss at every global tail; "
            "exact two-tail reconstruction at the seed and one period translate checks "
            "the persistent strict source descent"
        ),
        "scope_note": (
            "An infinite family of core primes that require a nonbase factor within the "
            "canonical global-tail menu but retain a one-factor certificate. It does not "
            "show that every core prime has such a factor."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "global_p_minus_one_factor": global_factor,
        "global_tail_count": len(bases),
        "one_factor_prime_progression_count": len(families),
        "distinct_new_prime_count": len({row["new_prime"] for row in families}),
        "families": families,
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
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "families"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
