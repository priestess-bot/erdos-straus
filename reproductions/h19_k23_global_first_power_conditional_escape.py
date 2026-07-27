#!/usr/bin/env python3
"""Build a Dickson-admissible 72-tail escape from global first-power witnesses."""

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
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-first-power-conditional-escape-2097152.json"
GLOBAL_CLOSURE = ROOT / "reproductions" / "h19_k23_full_global_tail_closure.py"
BASE_OBSTRUCTION = ROOT / "reproductions" / "h19_k23_global_base_only_prime_obstruction.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


global_closure = load_module("h19_k23_conditional_first_power_global", GLOBAL_CLOSURE)
base_obstruction = load_module(
    "h19_k23_conditional_first_power_base_obstruction", BASE_OBSTRUCTION
)


def base_divisor_residues(x: int, gap: int, base_primes: set[int]) -> set[int]:
    """Return all unit residues represented by canonical base divisors of x squared."""
    values = [1]
    for prime in sorted(base_primes):
        exponent = base_obstruction.valuation(x, prime)
        values = [
            value * prime**power
            for value in values
            for power in range(2 * exponent + 1)
        ]
    residues = {value % gap for value in values}
    if any(math.gcd(residue, gap) != 1 for residue in residues):
        raise AssertionError("base divisor residue is not a unit")
    return residues


def first_power_allowed_residues(
    x: int, gap: int, base_primes: set[int]
) -> set[int]:
    """Return prime residues that can extend some base divisor to a witness."""
    target = (-x) % gap
    return {
        target * pow(residue, -1, gap) % gap
        for residue in base_divisor_residues(x, gap, base_primes)
    }


def primitive_admissibility(
    forms: list[tuple[int, int]]
) -> tuple[bool, list[dict[str, int]]]:
    """Check the complete local obstruction condition for a finite affine tuple."""
    if any(math.gcd(a, b) != 1 or a <= 0 or b <= 0 for a, b in forms):
        return False, []
    local_rows = []
    for prime in sympy.primerange(2, len(forms) + 1):
        roots = set()
        for coefficient, constant in forms:
            if coefficient % prime:
                roots.add((-constant * pow(coefficient, -1, prime)) % prime)
            elif constant % prime == 0:
                return False, []
        local_rows.append({"prime": int(prime), "root_count": len(roots)})
        if len(roots) == prime:
            return False, []
    return True, local_rows


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compile one pressure ray into an admissible first-power escape tuple."""
    _, bases = global_closure.global_tail_bases()
    family = next(
        row
        for row in payload["families"]
        if int(row["prime_seed"]) == 955_643_834_512_728_001
    )
    forms = {
        int(branch["v_mod_29"]): (
            int(branch["prime_form"]["coefficient"]),
            int(branch["prime_form"]["constant"]),
        )
        for branch in base_obstruction.boundary.remaining_branches()
    }
    prime_seed = int(family["prime_seed"])
    parameter_seed = int(family["parameter_seed"])
    coefficient, constant = forms[int(family["branch_v_mod_29"])]
    period = int(family["parameter_period"])
    period_primes = set(sympy.factorint(period))
    provisional = []
    for gap, base_primes in sorted(bases.items()):
        u = (prime_seed + gap) // (gap + 1)
        base_part = math.prod(
            factor ** base_obstruction.valuation(u, factor)
            for factor in base_primes
        )
        nonbase = u // base_part
        frozen_nonbase = math.prod(
            int(factor) ** int(exponent)
            for factor, exponent in sympy.factorint(nonbase).items()
            if int(factor) in period_primes
        )
        for factor, exponent in sympy.factorint(frozen_nonbase).items():
            period = math.lcm(period, int(factor) ** (int(exponent) + 1))
        provisional.append((gap, base_primes, base_part, frozen_nonbase))

    tuple_forms = [(coefficient * period, prime_seed)]
    tail_rows = []
    for gap, base_primes, base_part, frozen_nonbase in provisional:
        q = (gap + 1) // 4
        u = (prime_seed + gap) // (gap + 1)
        slope = coefficient // (gap + 1)
        if period % gap or period % base_part or period % frozen_nonbase:
            raise AssertionError("escape period did not absorb a fixed tail factor")
        shifted_u = u + slope * period
        for factor in base_primes:
            exponent = base_obstruction.valuation(u, factor)
            if base_obstruction.valuation(shifted_u, factor) != exponent:
                raise AssertionError("base valuation changed on the escape ray")
        for factor, exponent in sympy.factorint(frozen_nonbase).items():
            factor = int(factor)
            exponent = int(exponent)
            if base_obstruction.valuation(shifted_u, factor) != exponent:
                raise AssertionError("frozen nonbase valuation changed on the escape ray")
        quotient = u // base_part // frozen_nonbase
        quotient_coefficient = slope * period // base_part // frozen_nonbase
        if math.gcd(quotient_coefficient, quotient) != 1:
            raise AssertionError("tail quotient form is not primitive")
        if quotient_coefficient % gap:
            raise AssertionError("tail quotient residue is not fixed")
        x = q * u
        allowed = first_power_allowed_residues(x, gap, base_primes)
        forbidden = {
            residue
            for residue in range(1, gap)
            if math.gcd(residue, gap) == 1 and residue not in allowed
        }
        frozen_factors = {
            int(factor): int(exponent)
            for factor, exponent in sympy.factorint(frozen_nonbase).items()
        }
        if any(factor % gap not in forbidden for factor in frozen_factors):
            raise AssertionError("a fixed nonbase prime is a first-power witness")
        if quotient % gap not in forbidden:
            raise AssertionError("the variable prime quotient is a first-power witness")
        tuple_forms.append((quotient_coefficient, quotient))
        tail_rows.append(
            {
                "tail_gap": gap,
                "base_primes": sorted(base_primes),
                "frozen_nonbase_factorization": {
                    str(factor): exponent
                    for factor, exponent in sorted(frozen_factors.items())
                },
                "variable_quotient_residue": quotient % gap,
                "allowed_first_power_residue_count": len(allowed),
                "forbidden_first_power_residue_count": len(forbidden),
                "variable_quotient_coefficient_gcd": math.gcd(
                    quotient_coefficient, quotient
                ),
            }
        )
    if len(tuple_forms) != len(bases) + 1:
        raise AssertionError("conditional tuple does not contain p and every tail quotient")
    if len(set(tuple_forms)) != len(tuple_forms):
        raise AssertionError("conditional tuple has duplicate affine forms")
    admissible, local_rows = primitive_admissibility(tuple_forms)
    if not admissible:
        raise AssertionError("conditional affine prime tuple is locally obstructed")
    p_shift = coefficient * (parameter_seed + period) + constant
    if p_shift % 24 != 1 or coefficient * period % 24:
        raise AssertionError("conditional escape left the core-prime class")
    return {
        "arithmetic": (
            "base and ramified nonbase valuations are frozen on one pressure ray; "
            "every remaining tail quotient has a forbidden first-power residue. "
            "The target p form and all 72 quotient forms are positive, primitive, "
            "distinct, and locally admissible"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, this admissible 73-form tuple "
            "has infinitely many simultaneous prime values. Those core primes escape "
            "every canonical global first-power witness. This is a conditional method "
            "boundary, not an Erdos-Straus counterexample."
        ),
        "seed_prime": prime_seed,
        "seed_branch_v_mod_29": int(family["branch_v_mod_29"]),
        "global_tail_count": len(bases),
        "affine_prime_form_count": len(tuple_forms),
        "escape_parameter_period": period,
        "escape_parameter_period_prime_count": len(sympy.factorint(period)),
        "tuple_is_primitive_and_admissible": admissible,
        "local_admissibility": local_rows,
        "tail_rows": tail_rows,
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
