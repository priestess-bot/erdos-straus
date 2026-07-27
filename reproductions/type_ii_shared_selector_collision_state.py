#!/usr/bin/env python3
"""Compile the coupled shared-Type-II state of a finite gap window.

For x_j=(p+4j-1)/4, a shared Type II hit has two different divisor-residue
requirements at the same gap: a nontrivial divisor of 4x_j is 1 modulo the
gap, while a divisor of x_j^2 is -x_j modulo the gap.  This program separates
both requirements into the finite collision part forced by gap differences and
the pairwise-coprime private parts.

The result is an exact state decomposition, not a claim that either condition
is forced in every window.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-shared-selector-collision-p33011449-j31-results.json"


Factorization = tuple[tuple[int, int], ...]


def factorization(value: int) -> Factorization:
    """Return a complete prime factorization with a product check."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors = tuple(sorted((int(q), int(e)) for q, e in sympy.factorint(value).items()))
    if math.prod(q**e for q, e in factors) != value:
        raise AssertionError("factorization product mismatch")
    return factors


def collision_primes(window: int) -> tuple[int, ...]:
    """Return the primes which can divide a nonzero difference x_j-x_k."""
    if window < 3:
        raise ValueError("window must be at least three so that 4 is collision data")
    return tuple(
        candidate
        for candidate in range(2, window)
        if all(candidate % divisor for divisor in range(2, math.isqrt(candidate) + 1))
    )


def split_factorization(
    factors: Factorization, collision_set: set[int]
) -> tuple[Factorization, Factorization]:
    """Split a factorization into its collision and private prime powers."""
    collision = tuple((q, e) for q, e in factors if q in collision_set)
    private = tuple((q, e) for q, e in factors if q not in collision_set)
    return collision, private


def add_four(factors: Factorization) -> Factorization:
    """Return the factorization after multiplying the represented number by 4."""
    exponents = dict(factors)
    exponents[2] = exponents.get(2, 0) + 2
    return tuple(sorted(exponents.items()))


def divisor_residue_profile(
    factors: Factorization, modulus: int, multiplier: int = 1
) -> tuple[frozenset[int], frozenset[int]]:
    """Return all and nontrivial divisor residues of a factored power."""
    residues: dict[int, bool] = {1: False}
    for prime, exponent in factors:
        if math.gcd(prime, modulus) != 1:
            raise ValueError("all divisor factors must be units modulo the gap")
        next_residues: dict[int, bool] = {}
        for residue, is_nontrivial in residues.items():
            for power in range(multiplier * exponent + 1):
                value = residue * pow(prime, power, modulus) % modulus
                next_residues[value] = next_residues.get(value, False) or (
                    is_nontrivial or power > 0
                )
        residues = next_residues
    all_residues = frozenset(residues)
    nontrivial_residues = frozenset(
        residue for residue, is_nontrivial in residues.items() if is_nontrivial
    )
    return all_residues, nontrivial_residues


def product_residues(left: frozenset[int], right: frozenset[int], modulus: int) -> frozenset[int]:
    return frozenset(a * b % modulus for a in left for b in right)


def shared_hit_from_profiles(
    left_all: frozenset[int],
    left_nontrivial: frozenset[int],
    right_all: frozenset[int],
    right_nontrivial: frozenset[int],
    modulus: int,
) -> bool:
    """Decide whether a nontrivial product divisor is 1 modulo ``modulus``."""
    for residue in left_all:
        inverse = pow(residue, -1, modulus)
        if inverse not in right_all:
            continue
        if residue in left_nontrivial or inverse in right_nontrivial:
            return True
    return False


def position_state(prime: int, j: int, collision_set: set[int]) -> dict[str, object]:
    """Compile both divisor targets at one moving-window position."""
    gap = 4 * j - 1
    x = (prime + gap) // 4
    if 4 * x != prime + gap or math.gcd(x, gap) != 1:
        raise AssertionError("invalid core-prime window position")

    factors = factorization(x)
    collision_factors, private_factors = split_factorization(factors, collision_set)

    type_collision, _ = divisor_residue_profile(collision_factors, gap, 2)
    type_private, _ = divisor_residue_profile(private_factors, gap, 2)
    type_full, _ = divisor_residue_profile(factors, gap, 2)
    if product_residues(type_collision, type_private, gap) != type_full:
        raise AssertionError("Type II collision/private product decomposition failed")
    type_target = (-x) % gap
    type_state_hit = type_target in product_residues(type_collision, type_private, gap)
    if type_state_hit != (type_target in type_full):
        raise AssertionError("Type II state hit did not match the full divisor set")

    shared_collision_factors = add_four(collision_factors)
    shared_collision, shared_collision_nontrivial = divisor_residue_profile(
        shared_collision_factors, gap
    )
    shared_private, shared_private_nontrivial = divisor_residue_profile(
        private_factors, gap
    )
    shared_full, shared_full_nontrivial = divisor_residue_profile(add_four(factors), gap)
    if product_residues(shared_collision, shared_private, gap) != shared_full:
        raise AssertionError("shared collision/private product decomposition failed")
    shared_state_hit = shared_hit_from_profiles(
        shared_collision,
        shared_collision_nontrivial,
        shared_private,
        shared_private_nontrivial,
        gap,
    )
    if shared_state_hit != (1 in shared_full_nontrivial):
        raise AssertionError("shared state hit did not match the full divisor set")

    type_private_targets = frozenset(
        type_target * pow(residue, -1, gap) % gap for residue in type_collision
    )
    shared_private_targets = frozenset(
        pow(residue, -1, gap) for residue in shared_collision
    )
    private_value = math.prod(q**e for q, e in private_factors)
    return {
        "j": j,
        "gap": gap,
        "x": x,
        "x_factorization": factors,
        "collision_factorization": collision_factors,
        "private_factorization": private_factors,
        "private_value": private_value,
        "type_ii_target": type_target,
        "type_ii_collision_residue_count": len(type_collision),
        "type_ii_private_residue_count": len(type_private),
        "type_ii_private_target_count": len(type_private_targets),
        "type_ii_hit": type_state_hit,
        "shared_collision_residue_count": len(shared_collision),
        "shared_private_residue_count": len(shared_private),
        "shared_private_target_count": len(shared_private_targets),
        "shared_hit": shared_state_hit,
        "joint_hit": type_state_hit and shared_state_hit,
    }


def run_audit(prime: int = 33_011_449, window: int = 31) -> dict[str, object]:
    """Compile an exact coupled state for a prime and a finite gap window."""
    if prime % 24 != 1 or not sympy.isprime(prime):
        raise ValueError("prime must be an actual core prime")
    primes = collision_primes(window)
    collision_set = set(primes)
    rows = [position_state(prime, j, collision_set) for j in range(1, window + 1)]
    private_values = [int(row["private_value"]) for row in rows]
    pairwise_coprime = all(
        math.gcd(left, right) == 1
        for index, left in enumerate(private_values)
        for right in private_values[index + 1 :]
    )
    if not pairwise_coprime:
        raise AssertionError("private parts must be pairwise coprime after collision stripping")
    return {
        "arithmetic": (
            "complete integer factorization and exact divisor-residue product sets; "
            "the shared profile tracks nontrivial divisors separately"
        ),
        "scope_note": (
            "This is a finite coupled-state compilation. It does not prove that a "
            "joint hit is forced in an arbitrary or growing window."
        ),
        "prime": prime,
        "window_j": window,
        "collision_primes": primes,
        "private_cofactors_pairwise_coprime": pairwise_coprime,
        "type_ii_hit_positions": sum(bool(row["type_ii_hit"]) for row in rows),
        "shared_hit_positions": sum(bool(row["shared_hit"]) for row in rows),
        "joint_hit_positions": sum(bool(row["joint_hit"]) for row in rows),
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=33_011_449)
    parser.add_argument("--window", type=int, default=31)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.prime, args.window)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
