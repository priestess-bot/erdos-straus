#!/usr/bin/env python3
"""Rule out aggregate-residue forcing of one-factor witnesses at pressure states."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-one-factor-aggregate-residue-boundary-2097152.json"
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


global_closure = load_module("h19_k23_aggregate_residue_menu", GLOBAL_CLOSURE)
base_obstruction = load_module(
    "h19_k23_aggregate_residue_base_obstruction", BASE_OBSTRUCTION
)


def exact_forbidden_pattern(
    modulus: int, forbidden: set[int], length: int, target: int
) -> list[int] | None:
    """Find a length-exact forbidden-residue product equal to the target."""
    parents: list[dict[int, tuple[int, int]]] = [{1: (0, 0)}]
    states = {1}
    for _ in range(length):
        next_parents: dict[int, tuple[int, int]] = {}
        for state in states:
            for residue in sorted(forbidden):
                product = state * residue % modulus
                next_parents.setdefault(product, (state, residue))
        parents.append(next_parents)
        states = set(next_parents)
    if target not in states:
        return None
    pattern = []
    current = target
    for depth in range(length, 0, -1):
        previous, residue = parents[depth][current]
        pattern.append(residue)
        current = previous
    if current != 1:
        raise AssertionError("residue predecessor chain did not return to identity")
    return list(reversed(pattern))


def base_divisor_residues(x: int, gap: int, base_primes: set[int]) -> set[int]:
    """Return residues represented by canonical base-only divisors of x squared."""
    values = [1]
    for prime in sorted(base_primes):
        exponent = base_obstruction.valuation(x, prime)
        values = [
            value * prime**power
            for value in values
            for power in range(2 * exponent + 1)
        ]
    return {value % gap for value in values if math.gcd(value, gap) == 1}


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Show exact aggregate data remains compatible with all forbidden residues."""
    _, bases = global_closure.global_tail_bases()
    rows = []
    for record in payload["global_base_only_pressure_records"]:
        prime = int(record["prime"])
        gap = int(record["current_global_tail_gap"])
        q = (gap + 1) // 4
        u = (prime + gap) // (gap + 1)
        x = q * u
        base = bases[gap]
        divisor_residues = base_divisor_residues(x, gap, base)
        target = (-x) % gap
        allowed = {
            target * pow(residue, -1, gap) % gap
            for residue in divisor_residues
        }
        units = {residue for residue in range(1, gap) if math.gcd(residue, gap) == 1}
        forbidden = units - allowed
        nonbase = x
        for factor in base:
            while nonbase % factor == 0:
                nonbase //= factor
        if math.gcd(nonbase, gap) != 1:
            raise AssertionError("pressure nonbase part is not a unit modulo its tail")
        factors = sympy.factorint(nonbase)
        omega = sum(int(exponent) for exponent in factors.values())
        pattern = exact_forbidden_pattern(gap, forbidden, omega, nonbase % gap)
        if pattern is None:
            raise AssertionError("aggregate residue would force an allowed factor")
        if len(pattern) != omega or math.prod(pattern) % gap != nonbase % gap:
            raise AssertionError("forbidden pattern has the wrong aggregate residue")
        rows.append(
            {
                "prime": prime,
                "tail_gap": gap,
                "nonbase_omega": omega,
                "nonbase_residue": nonbase % gap,
                "allowed_prime_residue_count": len(allowed),
                "forbidden_prime_residue_count": len(forbidden),
                "exact_omega_forbidden_residue_pattern": pattern,
            }
        )
    if len(rows) != int(payload["global_base_only_pressure_count"]):
        raise AssertionError("pressure records were not fully profiled")
    return {
        "arithmetic": (
            "at one tail, a one-new-prime divisor must have its nonbase prime in "
            "target times the inverse of a canonical base-divisor residue. For each "
            "pressure record, exhaustive dynamic programming constructs an equally "
            "long product of forbidden unit residues with the same total nonbase "
            "residue, so aggregate residue and exact Omega alone cannot force a usable "
            "prime factor"
        ),
        "scope_note": (
            "An information boundary for single-tail aggregate-residue arguments at the "
            "checked pressure states. It does not construct actual affine u-values with "
            "the forbidden factorization and does not exclude cross-tail or factor-size "
            "arguments."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "pressure_record_count": len(rows),
        "aggregate_residue_forcing_count": 0,
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
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "rows"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
