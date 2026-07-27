#!/usr/bin/env python3
"""Factor the natural dynamic source at its pressure seed exactly."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-dynamic-scale-seed-profile-2097152.json"
TARGET_SEED = 748_375_048_866_405_601


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Enumerate all square divisors of the one natural dynamic source product."""
    row = next(row for row in payload["rows"] if int(row["prime_seed"]) == TARGET_SEED)
    prime = int(row["prime_seed"])
    coefficient = int(row["pressure_prime_coefficient"])
    global_factor = math.gcd((prime - 1) // 4, coefficient // 4)
    scale = (prime - 1) // (4 * global_factor)
    source = prime - global_factor
    product = scale * source
    modulus = 4 * scale - 1
    factors = {int(factor): int(exponent) for factor, exponent in sympy.factorint(product).items()}
    if math.prod(factor**exponent for factor, exponent in factors.items()) != product:
        raise AssertionError("dynamic product factorization is incomplete")
    if not all(sympy.isprime(factor) for factor in factors):
        raise AssertionError("dynamic product factorization contains a composite")
    residues = {1: 1}
    divisor_count = 1
    for factor, exponent in factors.items():
        divisor_count *= 2 * exponent + 1
        next_residues: dict[int, int] = {}
        for residue, divisor in residues.items():
            for power in range(2 * exponent + 1):
                candidate = divisor * factor**power
                new_residue = residue * pow(factor, power, modulus) % modulus
                existing = next_residues.get(new_residue)
                if existing is None or candidate < existing:
                    next_residues[new_residue] = candidate
        residues = next_residues
    target = (-product) % modulus
    if target in residues:
        raise AssertionError("natural dynamic source unexpectedly has a square-tail witness")
    return {
        "arithmetic": (
            "complete prime factorization of M=h(p-G), exhaustive enumeration of every "
            "divisor of M^2 by its residue modulo 4h-1, and exact target lookup"
        ),
        "scope_note": (
            "An exact profile at one actual pressure seed. It does not establish that "
            "the dynamic source fails at other parameters or exclude other sources."
        ),
        "seed_prime": prime,
        "global_factor": global_factor,
        "dynamic_scale": scale,
        "dynamic_source": source,
        "source_product_factorization": {str(factor): exponent for factor, exponent in sorted(factors.items())},
        "square_divisor_count": divisor_count,
        "distinct_square_divisor_residue_count": len(residues),
        "target_residue": target,
        "square_tail_witness": None,
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
