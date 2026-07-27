#!/usr/bin/env python3
"""Extend the Dickson escape to every eventual global Type II divisor."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-global-full-divisor-conditional-escape-2097152.json"
FIRST_POWER_ESCAPE = ROOT / "reproductions" / "h19_k23_global_first_power_conditional_escape.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


escape = load_module("h19_k23_full_divisor_escape", FIRST_POWER_ESCAPE)


def divisor_values(factors: dict[int, int]) -> list[int]:
    """Return every divisor of a fixed factorization."""
    values = [1]
    for factor, exponent in sorted(factors.items()):
        values = [
            value * factor**power
            for value in values
            for power in range(exponent + 1)
        ]
    return values


def tail_full_divisor_boundary(
    prime: int,
    gap: int,
    base_primes: set[int],
    frozen_nonbase: dict[int, int],
) -> dict[str, int]:
    """Exhaust all eventual d|x^2 once the remaining quotient is prime.

    Along the escape ray x=B*K*L, where B is base-only, K is fixed nonbase,
    and L is the sole growing prime.  For sufficiently large L, d<=x permits
    exponent zero or one for L; exponent two is already larger than x.
    """
    q = (gap + 1) // 4
    u = (prime + gap) // (gap + 1)
    base_part = math.prod(
        factor ** escape.base_obstruction.valuation(u, factor)
        for factor in base_primes
    )
    fixed_base = q * base_part
    if set(sympy.factorint(fixed_base)) - base_primes:
        raise AssertionError("the claimed base component has a nonbase prime")
    frozen_value = math.prod(
        factor**exponent for factor, exponent in frozen_nonbase.items()
    )
    quotient, remainder = divmod(u, base_part * frozen_value)
    if remainder or quotient <= 0:
        raise AssertionError("tail factorization does not split into base, fixed, quotient")
    if math.gcd(quotient, fixed_base * frozen_value) != 1:
        raise AssertionError("seed quotient overlaps a frozen factor")

    base_factors = {
        int(factor): 2 * int(exponent)
        for factor, exponent in sympy.factorint(fixed_base).items()
    }
    frozen_factors = {
        int(factor): 2 * int(exponent)
        for factor, exponent in frozen_nonbase.items()
    }
    base_divisors = divisor_values(base_factors)
    frozen_divisors = divisor_values(frozen_factors)
    target = (-(fixed_base * frozen_value * quotient)) % gap
    candidate_count = 0
    for base_divisor in base_divisors:
        for frozen_divisor in frozen_divisors:
            # L^0 is eventually below x; L^1 has the stable size ratio below.
            for quotient_exponent in (0, 1):
                divisor = base_divisor * frozen_divisor
                if quotient_exponent:
                    divisor *= quotient
                    if divisor > fixed_base * frozen_value * quotient:
                        continue
                candidate_count += 1
                if divisor % gap == target:
                    raise AssertionError("an eventual full-divisor Type II witness survived")
    return {
        "tail_gap": gap,
        "base_divisor_count": len(base_divisors),
        "frozen_nonbase_divisor_count": len(frozen_divisors),
        "tested_eventual_divisor_count": candidate_count,
        "eventual_variable_prime_threshold": fixed_base * frozen_value,
        "full_divisor_witness_count": 0,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Prove that the existing Dickson tuple escapes all eventual global divisors."""
    first_power = escape.run_audit(payload)
    _, bases = escape.global_closure.global_tail_bases()
    rows_by_gap = {
        int(row["tail_gap"]): row for row in first_power["tail_rows"]
    }
    prime = int(first_power["seed_prime"])
    rows = []
    for gap, base_primes in sorted(bases.items()):
        frozen_nonbase = {
            int(factor): int(exponent)
            for factor, exponent in rows_by_gap[gap]["frozen_nonbase_factorization"].items()
        }
        rows.append(
            tail_full_divisor_boundary(prime, gap, base_primes, frozen_nonbase)
        )
    if len(rows) != len(bases) or any(row["full_divisor_witness_count"] for row in rows):
        raise AssertionError("full-divisor escape did not cover every global tail")
    return {
        "arithmetic": (
            "reuse the 73-form Dickson-admissible escape tuple; for each tail, "
            "exhaust every divisor of the fixed base and fixed nonbase parts squared, "
            "then append the unique growing quotient prime with exponent zero or one"
        ),
        "scope_note": (
            "Assuming Dickson's prime-tuples conjecture, sufficiently large simultaneous "
            "prime values of the inherited tuple have no Type II divisor certificate at "
            "any of the 72 canonical global tails, even with arbitrary nonbase support "
            "and prime powers. This remains a conditional boundary within this fixed "
            "global-tail framework, not an Erdos-Straus counterexample."
        ),
        "seed_prime": prime,
        "global_tail_count": len(rows),
        "inherited_affine_prime_form_count": first_power["affine_prime_form_count"],
        "full_divisor_witness_miss_count": 0,
        "maximum_tested_eventual_divisor_count": max(
            int(row["tested_eventual_divisor_count"]) for row in rows
        ),
        "maximum_eventual_variable_prime_threshold": max(
            int(row["eventual_variable_prime_threshold"]) for row in rows
        ),
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
