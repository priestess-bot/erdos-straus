#!/usr/bin/env python3
"""Resolve the two fixed-factor pressure misses at their actual seed primes."""

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
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-external-source-seed-profile-2097152.json"
BRIDGE = ROOT / "reproductions" / "h19_k23_global_tail_pressure_external_source_bridge.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


bridge = load_module("h19_k23_pressure_seed_profile_bridge", BRIDGE)


def source_witness(prime: int, scale: int) -> dict[str, object] | None:
    """Return a complete external-source witness from an actual source factor."""
    q = 4 * scale - 1
    source, remainder = divmod(q * prime + 1, 4 * scale)
    if remainder:
        raise AssertionError("stationary scale has a nonintegral source")
    factors = {int(factor): int(exponent) for factor, exponent in sympy.factorint(source).items()}
    candidates = []
    for factor in sympy.divisors(source):
        factor = int(factor)
        complement = source // factor
        if complement % q == q - 1:
            candidates.append(min(factor, complement))
    if not candidates:
        return None
    factor = min(candidates)
    complement = source // factor
    if complement % q != q - 1:
        factor, complement = complement, factor
    r = (complement + 1) // q
    product = scale * source
    first_tail = scale * factor * r
    second_tail = product * r
    if (
        (complement + 1) % q
        or factor * complement != source
        or Fraction(4, source)
        != Fraction(1, product) + Fraction(1, first_tail) + Fraction(1, second_tail)
        or Fraction(4, prime)
        != Fraction(1, product * prime)
        + Fraction(1, first_tail)
        + Fraction(1, second_tail)
    ):
        raise AssertionError("external-source seed witness failed exact verification")
    return {
        "scale": scale,
        "source_modulus": q,
        "source_denominator": source,
        "source_factorization": {str(key): value for key, value in sorted(factors.items())},
        "selected_factor": factor,
        "complement": complement,
        "r": r,
        "source_product": product,
        "first_tail": first_tail,
        "second_tail": second_tail,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Find direct source descents at every pressure seed lacking a fixed bridge."""
    rows = []
    for row in payload["rows"]:
        if row["fixed_factor_bridge"] is not None:
            continue
        prime = int(row["prime_seed"])
        coefficient = int(row["pressure_prime_coefficient"])
        stationary_gcd = math.gcd((prime - 1) // 4, coefficient // 4)
        witnesses = [
            witness
            for scale in sympy.divisors(stationary_gcd)
            if (witness := source_witness(prime, int(scale))) is not None
        ]
        if not witnesses:
            raise AssertionError("an unbridged seed has no stationary source witness")
        rows.append(
            {
                "prime_seed": prime,
                "stationary_scale_gcd": stationary_gcd,
                "stationary_scale_count": len(sympy.divisors(stationary_gcd)),
                "source_witness_count": len(witnesses),
                "first_source_witness": min(witnesses, key=lambda item: int(item["scale"])),
            }
        )
    if len(rows) != int(payload["fixed_factor_bridge_miss_count"]):
        raise AssertionError("seed profile did not resolve every fixed-factor miss")
    return {
        "arithmetic": (
            "complete factorization of every stationary source denominator at the two "
            "fixed-factor bridge misses, exhaustive divisor checks for n/f=-1 mod 4k-1, "
            "and exact rational verification of the resulting strict lifts"
        ),
        "scope_note": (
            "A two-seed profile only. It proves direct strict descent at these actual "
            "primes, but does not make their variable source factors uniform on the "
            "surrounding pressure progressions."
        ),
        "fixed_factor_miss_seed_count": len(rows),
        "resolved_seed_count": len(rows),
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
