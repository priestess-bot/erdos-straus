#!/usr/bin/env python3
"""Verify a Type II certificate on the progression closing the j<=37 state."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-gap-207-progression-results.json"
SEED_PRIME = 153_633_769
GAP = 207
FORCED_FACTOR = 9_682
TARGET_FACTOR = 47


def window_modulus(window: int) -> int:
    if window < 1:
        raise ValueError("window must be positive")
    modulus = 24
    for j in range(1, window + 1):
        gap = 4 * j - 1
        modulus = modulus * gap // math.gcd(modulus, gap)
    return modulus


def certificate_at_index(index: int) -> dict[str, int | bool]:
    """Build the gap-207 Type II certificate for p=16*Q*index+seed."""
    if index < 0:
        raise ValueError("index must be nonnegative")
    q37 = window_modulus(37)
    step = 16 * q37
    if math.gcd(step, SEED_PRIME) != 1:
        raise AssertionError("the progression must be primitive for Dirichlet")
    prime = step * index + SEED_PRIME
    x = (prime + GAP) // 4
    if 4 * x != prime + GAP:
        raise AssertionError("progression does not preserve the first denominator")
    if x % FORCED_FACTOR:
        raise AssertionError("forced factor does not divide x")
    cofactor = x // FORCED_FACTOR
    divisor = TARGET_FACTOR * cofactor
    if (
        divisor > x
        or x * x % divisor
        or (x + divisor) % GAP
    ):
        raise AssertionError("constructed divisor is not a Type II certificate")
    y = prime * (x + divisor) // GAP
    z = prime * (x + x * x // divisor) // GAP
    exact_identity = (
        Fraction(4, prime)
        == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
    )
    if not exact_identity:
        raise AssertionError("certificate identity failed")
    return {
        "index": index,
        "prime": prime,
        "x": x,
        "cofactor": cofactor,
        "divisor": divisor,
        "y": y,
        "z": z,
        "exact_identity": exact_identity,
    }


def run_audit() -> dict[str, object]:
    q37 = window_modulus(37)
    step = 16 * q37
    initial_x = (SEED_PRIME + GAP) // 4
    if initial_x % FORCED_FACTOR:
        raise AssertionError("seed x must contain the claimed forced factor")
    quotient_step = 4 * q37 // FORCED_FACTOR
    if quotient_step % GAP:
        raise AssertionError("cofactor residue must be fixed modulo the gap")
    initial_cofactor = initial_x // FORCED_FACTOR
    target = (-initial_x) % GAP
    if (
        initial_cofactor % GAP != 34
        or TARGET_FACTOR * initial_cofactor % GAP != target
    ):
        raise AssertionError("target residue identity failed")

    samples = [certificate_at_index(index) for index in (0, 1, 2)]
    return {
        "arithmetic": (
            "exact integer divisibility, modular arithmetic, and "
            "fractions.Fraction identity verification"
        ),
        "scope_note": (
            "Every prime in the displayed progression has a direct Type II "
            "certificate. The progression is primitive, so Dirichlet's theorem "
            "also gives infinitely many such primes."
        ),
        "window_q37": q37,
        "prime_step": step,
        "prime_residue": SEED_PRIME,
        "primitive_progression": True,
        "gap": GAP,
        "forced_factor": FORCED_FACTOR,
        "target_factor": TARGET_FACTOR,
        "initial_x": initial_x,
        "initial_cofactor": initial_cofactor,
        "cofactor_step": quotient_step,
        "cofactor_residue_mod_gap": initial_cofactor % GAP,
        "target_residue_mod_gap": target,
        "samples": samples,
    }


def main() -> int:
    payload = run_audit()
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
