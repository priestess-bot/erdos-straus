#!/usr/bin/env python3
"""Audit a sparse 500M--600M mixed-terminal family exactly.

The family is ``p = 24q + 1`` with both ``p`` and ``q`` prime.  Its
``p - 1`` divisor lattice has exactly eight candidates for ordinary Type II
two-tail deflation.  Every failure of that first branch is then searched in
increasing ``m`` through Type I normal forms with ``m <= 215`` and ``B = 1``.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path

from sympy import factorint, isprime


ROOT = Path(__file__).resolve().parents[1]
DIRECT = ROOT / "reproductions" / "type_i_direct_small_b_even_source_audit.py"
Q_MIN = 20_833_334
Q_MAX = 24_999_999
GAP_CAP = 215
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-mixed-terminal-sparse-tail-600m-results.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


direct = load_module("mixed_terminal_sparse_tail_direct", DIRECT)


def square_divisors(factors: dict[int, int]) -> list[int]:
    """Return all positive divisors of the square of a factored integer."""
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(2 * exponent + 1)
        ]
    return divisors


def type_ii_tail_witness(prime: int, q: int) -> dict[str, int] | None:
    """Return the first ordinary Type II two-tail witness for p=24q+1.

    Since ``p - 1 = 2^3 * 3 * q`` and ``q`` is prime, this checks every
    divisor ``d | p - 1`` divisible by four.  The Type II divisor residue is
    checked against every divisor of ``x^2``.
    """
    if prime != 24 * q + 1 or not isprime(q) or not isprime(prime):
        raise ValueError("expected p=24q+1 with p and q prime")
    for divisor_gap in (4, 8, 12, 24, 4 * q, 8 * q, 12 * q, 24 * q):
        gap = divisor_gap - 1
        x = (prime + gap) // 4
        if 4 * x != prime + gap:
            raise AssertionError("Type II first denominator was not integral")
        for divisor in square_divisors(factorint(x)):
            if divisor > x or divisor % gap != (-x) % gap:
                continue
            y = prime * (x + divisor) // gap
            z = prime * (x + x * x // divisor) // gap
            if (
                prime * (x + divisor) % gap
                or prime * (x + x * x // divisor) % gap
            ):
                raise AssertionError("Type II residue did not reconstruct")
            if Fraction(4, prime) != Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
                raise AssertionError("Type II target identity did not verify")
            source = (prime + gap) // (gap + 1)
            if (gap + 1) * source != prime + gap or not 2 <= source < prime:
                raise AssertionError("Type II source was not a strict integer")
            if Fraction(4, source) != Fraction(1, x) + Fraction(1, y // prime) + Fraction(1, z // prime):
                raise AssertionError("Type II source identity did not verify")
            return {
                "gap": gap,
                "first_denominator": x,
                "divisor": divisor,
                "source_denominator": source,
            }
    return None


def run_audit(q_min: int = Q_MIN, q_max: int = Q_MAX) -> dict[str, object]:
    """Exhaust the stated sparse family and close every ordinary-tail miss."""
    if q_min < 2 or q_max < q_min:
        raise ValueError("invalid q interval")
    family_count = 0
    ordinary_tail_hits = 0
    records: list[dict[str, object]] = []
    even_source_misses: list[int] = []
    for q in range(q_min, q_max + 1):
        prime = 24 * q + 1
        if not isprime(q) or not isprime(prime):
            continue
        family_count += 1
        tail = type_ii_tail_witness(prime, q)
        if tail is not None:
            ordinary_tail_hits += 1
            continue
        witness = direct.first_witness(prime, 1)
        if witness is None:
            even_source_misses.append(prime)
            continue
        if int(witness["gap"]) > GAP_CAP:
            raise AssertionError("Type I witness exceeded its stated gap cap")
        records.append({"prime": prime, "q": q, "type_i_even_witness": witness})
    return {
        "arithmetic": (
            "for every p=24q+1 with p,q prime in the stated interval, exhaust all "
            "eight d|p-1 divisible-by-four Type II two-tail candidates and every "
            "e|((p+d-1)/4)^2; for each ordinary-tail miss, search m increasingly "
            "through 215, exhaust every B=1 Type I normal form and maximum-tail "
            "E|4K^2 bridge at each reached m, and retain the first even source"
        ),
        "scope_note": (
            "A finite sparse-family audit. The Type I branch is bounded by m<=215 "
            "and B=1, so this result neither proves the mixed terminal lemma nor "
            "rules out a counterexample outside the stated family."
        ),
        "q_interval": [q_min, q_max],
        "prime_interval": [24 * q_min + 1, 24 * q_max + 1],
        "family_count": family_count,
        "ordinary_tail_hit_count": ordinary_tail_hits,
        "ordinary_tail_miss_count": len(records) + len(even_source_misses),
        "type_i_gap_cap": GAP_CAP,
        "type_i_B": 1,
        "even_source_captured_count": len(records),
        "even_source_misses": even_source_misses,
        "maximum_selected_gap": max(
            (int(record["type_i_even_witness"]["gap"]) for record in records),
            default=None,
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--q-min", type=int, default=Q_MIN)
    parser.add_argument("--q-max", type=int, default=Q_MAX)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.q_min, args.q_max)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
