#!/usr/bin/env python3
"""Resolve the pressure seed through its complete distance-one even-source fan."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-pressure-even-source-seed-profile-2097152.json"
TARGET_SEED = 748_375_048_866_405_601


def first_distance_one_witness(prime: int) -> tuple[dict[str, object], int, int]:
    """Exhaust the complete c=1 even-source fan and return its first strict lift."""
    source = prime - 1
    compatible_ray_count = 0
    square_divisor_test_count = 0
    for shift in sympy.divisors(source):
        shift = int(shift)
        quotient = source // shift
        r = quotient - 1
        if r <= 0 or (shift * r + 1) % 4:
            continue
        k = (shift * r + 1) // 4
        if shift % 4 != 1 or 4 * k * 1 + shift != prime:
            raise AssertionError("distance-one source ray is inconsistent")
        m1 = k * quotient
        if 4 * m1 != r * prime + 1:
            raise AssertionError("even-source tail product is inconsistent")
        compatible_ray_count += 1
        residues = {1: 1}
        for factor, exponent in sympy.factorint(m1).items():
            next_residues: dict[int, int] = {}
            for residue, divisor in residues.items():
                for power in range(2 * int(exponent) + 1):
                    candidate = divisor * int(factor) ** power
                    new_residue = residue * pow(int(factor), power, r) % r
                    existing = next_residues.get(new_residue)
                    if existing is None or candidate < existing:
                        next_residues[new_residue] = candidate
            residues = next_residues
        square_divisor_test_count += math.prod(
            2 * int(exponent) + 1 for exponent in sympy.factorint(m1).values()
        )
        factor = residues.get((-m1) % r)
        if factor is None:
            continue
        companion = m1 * m1 // factor
        if companion < factor:
            factor = companion
        if factor > m1 or (m1 + factor) % r or (m1 * ((m1 + factor) // r)) % factor:
            raise AssertionError("even-source square-tail witness is invalid")
        u = (m1 + factor) // r
        v = m1 * u // factor
        source_solution = (shift * m1, u, v)
        target_solution = (prime * m1, u, v)
        if (
            Fraction(4, source) != sum((Fraction(1, value) for value in source_solution), Fraction())
            or Fraction(4, prime) != sum((Fraction(1, value) for value in target_solution), Fraction())
        ):
            raise AssertionError("even-source strict lift identities failed")
        gap = (4 * factor + 1) // r
        if 4 * u - prime != gap or not 3 <= gap <= prime - 2 or u * u % factor:
            raise AssertionError("even-source Type I certificate is invalid")
        return (
            {
                "distance": 1,
                "source_denominator": source,
                "shift": shift,
                "r": r,
                "k": k,
                "m1": m1,
                "m1_factorization": {
                    str(key): value for key, value in sorted(sympy.factorint(m1).items())
                },
                "square_tail_factor": factor,
                "source_solution": list(source_solution),
                "target_solution": list(target_solution),
                "certificate": {"gap": gap, "x": u, "divisor": u * u // factor, "y": v, "z": prime * m1},
            },
            compatible_ray_count,
            square_divisor_test_count,
        )
    raise AssertionError("distance-one even-source fan has no witness")


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Verify an exact c=1 even-source strict descent at the pressure seed."""
    if TARGET_SEED not in {int(row["prime_seed"]) for row in payload["rows"]}:
        raise AssertionError("pressure seed is absent from bridge input")
    witness, ray_count, test_count = first_distance_one_witness(TARGET_SEED)
    return {
        "arithmetic": (
            "complete factorization of every compatible c=1 even-source ray through "
            "the first hit, exact M1^2 divisor-residue enumeration, and rational checks "
            "of the source and target strict-lift identities"
        ),
        "scope_note": (
            "An exact descent at one pressure seed. It does not establish that the "
            "distance-one even-source fan uniformly covers the whole pressure ray."
        ),
        "seed_prime": TARGET_SEED,
        "compatible_ray_count_through_first_hit": ray_count,
        "square_divisor_test_count_through_first_hit": test_count,
        "first_witness": witness,
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
