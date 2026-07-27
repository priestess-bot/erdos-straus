#!/usr/bin/env python3
"""Exhibit the unavoidable branching of a canonical-fan modulus extension.

An old congruence state ``p == r (mod Q)`` cannot decide whether a newly
adjoined prime ``ell`` divides an old shifted integer ``p + 4*s``.  CRT gives
two reduced lifts modulo ``ell*Q``; Dirichlet then realizes both by infinitely
many core primes.  The finite H22 -> H23 instance is retained as an exact
integer witness, with the first small prime found in each progression.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from sympy import isprime


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-fan-lift-nondeterminism-h23.json"

H22_MODULUS = 77_597_520
H22_RESIDUE = 529
NEW_PRIME = 23
OLD_SHIFT = 5


def crt_lift(modulus: int, residue: int, prime: int, new_residue: int) -> int:
    """Return the least CRT lift of ``residue mod modulus`` and ``new_residue mod prime``."""
    if modulus < 1 or prime < 2 or math.gcd(modulus, prime) != 1:
        raise ValueError("the moduli must be positive and coprime")
    if not 0 <= residue < modulus or not 0 <= new_residue < prime:
        raise ValueError("residues must be reduced")
    multiplier = ((new_residue - residue) * pow(modulus, -1, prime)) % prime
    return residue + modulus * multiplier


def avoiding_unit_residue(prime: int, forbidden: int) -> int:
    """Choose a nonzero residue distinct from ``forbidden`` modulo an odd prime >= 5."""
    if prime < 5 or not isprime(prime):
        raise ValueError("the branching lemma requires an odd prime at least five")
    forbidden %= prime
    for candidate in range(1, prime):
        if candidate != forbidden:
            return candidate
    raise AssertionError("a prime at least five has a second nonzero residue")


def branch_lifts(
    modulus: int, residue: int, prime: int, shift: int
) -> tuple[int, int]:
    """Return reduced hit and miss lifts for ``prime | p+4*shift``."""
    if modulus % 24 or residue % 24 != 1 or math.gcd(modulus, residue) != 1:
        raise ValueError("expected a reduced core-prime progression")
    if shift <= 0 or prime < 5 or not isprime(prime) or math.gcd(modulus, prime) != 1:
        raise ValueError("invalid extension data")
    if shift % prime == 0:
        raise ValueError("the new prime must not divide the selected old shift")

    hit = crt_lift(modulus, residue, prime, (-4 * shift) % prime)
    miss = crt_lift(
        modulus,
        residue,
        prime,
        avoiding_unit_residue(prime, (-4 * shift) % prime),
    )
    expanded = modulus * prime
    if math.gcd(hit, expanded) != 1 or math.gcd(miss, expanded) != 1:
        raise AssertionError("CRT lifts must remain reduced progressions")
    if (hit + 4 * shift) % prime or (miss + 4 * shift) % prime == 0:
        raise AssertionError("CRT lifts did not separate hit and miss branches")
    return hit, miss


def first_prime_in_progression(residue: int, modulus: int, search_limit: int = 10_000) -> tuple[int, int]:
    """Return the first prime among the first ``search_limit`` terms of a reduced progression."""
    if modulus < 1 or math.gcd(residue, modulus) != 1:
        raise ValueError("expected a reduced arithmetic progression")
    for multiplier in range(search_limit):
        candidate = residue + multiplier * modulus
        if candidate >= 2 and isprime(candidate):
            return multiplier, candidate
    raise AssertionError("the stated finite search limit unexpectedly found no prime")


def run_witness() -> dict[str, object]:
    """Rebuild the H22 extension's two incompatible forced-factor branches."""
    hit, miss = branch_lifts(H22_MODULUS, H22_RESIDUE, NEW_PRIME, OLD_SHIFT)
    expanded = H22_MODULUS * NEW_PRIME
    old_factor = math.gcd(H22_MODULUS, H22_RESIDUE + 4 * OLD_SHIFT)
    hit_factor = math.gcd(expanded, hit + 4 * OLD_SHIFT)
    miss_factor = math.gcd(expanded, miss + 4 * OLD_SHIFT)
    if (old_factor, hit_factor, miss_factor) != (3, 69, 3):
        raise AssertionError("the H22 branching factors did not reconstruct")

    hit_multiplier, hit_prime = first_prime_in_progression(hit, expanded)
    miss_multiplier, miss_prime = first_prime_in_progression(miss, expanded)
    for candidate, expected_residue, divides in (
        (hit_prime, hit, True),
        (miss_prime, miss, False),
    ):
        if candidate % 24 != 1 or candidate % expanded != expected_residue:
            raise AssertionError("displayed prime is not in the stated core progression")
        if ((candidate + 4 * OLD_SHIFT) % NEW_PRIME == 0) != divides:
            raise AssertionError("displayed prime has the wrong extension branch")

    return {
        "arithmetic": (
            "CRT lifts of a reduced core-prime progression, exact gcd forced-factor "
            "comparison, and deterministic primality checks for the first displayed "
            "prime in each H22-to-H23 lift"
        ),
        "scope_note": (
            "The general infinite assertion uses Dirichlet's theorem. It proves an "
            "old congruence state cannot determine a fan-extension update; it neither "
            "constructs a Type II certificate nor supplies a terminating descent."
        ),
        "general_branching_conditions": {
            "old_modulus_multiple_of": 24,
            "old_residue_mod_24": 1,
            "new_prime_minimum": 5,
            "new_prime_coprime_to_old_modulus": True,
            "new_prime_does_not_divide_old_shift": True,
        },
        "h22_to_h23": {
            "old_modulus": H22_MODULUS,
            "old_residue": H22_RESIDUE,
            "new_prime": NEW_PRIME,
            "expanded_modulus": expanded,
            "old_shift": OLD_SHIFT,
            "old_forced_factor": old_factor,
            "hit_lift_residue": hit,
            "hit_forced_factor": hit_factor,
            "hit_first_prime_multiplier": hit_multiplier,
            "hit_first_core_prime": hit_prime,
            "miss_lift_residue": miss,
            "miss_forced_factor": miss_factor,
            "miss_first_prime_multiplier": miss_multiplier,
            "miss_first_core_prime": miss_prime,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_witness()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
