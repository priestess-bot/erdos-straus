#!/usr/bin/env python3
"""Collision-state decomposition for a direct Type II moving-window failure."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
RESULTS = (
    ROOT
    / "reproductions"
    / "type-ii-moving-window-collision-p153633769-j31-results.json"
)


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_moving_window_collision_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def factorization_from_spf(value: int, spf: list[int]) -> tuple[tuple[int, int], ...]:
    """Return the prime factorization of a positive SPF-covered integer."""
    if value < 1 or value >= len(spf):
        raise ValueError("SPF table does not cover the requested value")
    factors: list[tuple[int, int]] = []
    while value > 1:
        prime = spf[value]
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        factors.append((prime, exponent))
    return tuple(factors)


def divisor_residues_of_square(
    factorization: tuple[tuple[int, int], ...], modulus: int
) -> frozenset[int]:
    """Return divisor residues of the square of the factorized integer."""
    residues = {1}
    for prime, exponent in factorization:
        if math.gcd(prime, modulus) != 1:
            raise ValueError("moving-window factors must be units modulo the gap")
        powers = [pow(prime, power, modulus) for power in range(2 * exponent + 1)]
        residues = {
            residue * power % modulus for residue in residues for power in powers
        }
    return frozenset(residues)


def collision_primes(window: int) -> tuple[int, ...]:
    """Return every prime which can divide two distinct x_j values."""
    if window < 2:
        raise ValueError("window must be at least two")
    primes = []
    for candidate in range(2, window):
        if all(candidate % divisor for divisor in range(2, math.isqrt(candidate) + 1)):
            primes.append(candidate)
    return tuple(primes)


def split_factorization(
    factorization: tuple[tuple[int, int], ...], collision_set: set[int]
) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
    collision = tuple(
        (prime, exponent)
        for prime, exponent in factorization
        if prime in collision_set
    )
    private = tuple(
        (prime, exponent)
        for prime, exponent in factorization
        if prime not in collision_set
    )
    return collision, private


def window_failure_profile(
    prime: int, window: int, spf: list[int]
) -> dict[str, object]:
    """Decompose every direct Type II failure in a fixed moving window."""
    if prime < 4 * window or prime % 24 != 1:
        raise ValueError("prime must be a sufficiently large core residue")
    collision = collision_primes(window)
    collision_set = set(collision)
    rows: list[dict[str, object]] = []
    private_values: list[int] = []
    for j in range(1, window + 1):
        gap = 4 * j - 1
        x = (prime + gap) // 4
        if 4 * x != prime + gap:
            raise AssertionError("moving-window x was not integral")
        if short_certificate.type_ii_residue_certificate(prime, gap, spf) is not None:
            raise ValueError("profile input must fail at every window position")
        factorization = factorization_from_spf(x, spf)
        collision_factors, private_factors = split_factorization(
            factorization, collision_set
        )
        collision_residues = divisor_residues_of_square(collision_factors, gap)
        private_residues = divisor_residues_of_square(private_factors, gap)
        full_residues = divisor_residues_of_square(factorization, gap)
        reconstructed = frozenset(
            left * right % gap
            for left in collision_residues
            for right in private_residues
        )
        if reconstructed != full_residues:
            raise AssertionError("collision/private residue decomposition failed")
        target = (-x) % gap
        if target in full_residues:
            raise AssertionError("failure profile unexpectedly contains Type II target")
        forbidden_private_targets = frozenset(
            target * pow(residue, -1, gap) % gap
            for residue in collision_residues
        )
        if forbidden_private_targets & private_residues:
            raise AssertionError("private residues meet a collision-induced target")
        private_value = math.prod(
            factor**exponent for factor, exponent in private_factors
        )
        private_values.append(private_value)
        rows.append(
            {
                "j": j,
                "gap": gap,
                "x": x,
                "target": target,
                "collision_factorization": collision_factors,
                "private_factorization": private_factors,
                "collision_residue_count": len(collision_residues),
                "private_residue_count": len(private_residues),
                "full_residue_count": len(full_residues),
                "forbidden_private_target_count": len(forbidden_private_targets),
            }
        )
    private_coprime = all(
        math.gcd(left, right) == 1
        for index, left in enumerate(private_values)
        for right in private_values[index + 1 :]
    )
    if not private_coprime:
        raise AssertionError("private moving-window cofactors must be pairwise coprime")
    return {
        "prime": prime,
        "window_j": window,
        "collision_primes": collision,
        "private_cofactors_pairwise_coprime": private_coprime,
        "rows": rows,
    }


def run_audit(prime: int, window: int) -> dict[str, object]:
    """Run an exact collision-state audit for one all-failure window."""
    if window < 2:
        raise ValueError("window must be at least two")
    max_x = (prime + 4 * window - 1) // 4 + 1
    spf = short_certificate.smallest_prime_factors(max_x)
    return {
        "arithmetic": (
            "exact SPF factorization and complete divisor-residue product sets "
            "for x_j^2 at every window position"
        ),
        "scope_note": (
            "This is a finite collision-state decomposition. It does not prove "
            "that private residues from different gaps are incompatible."
        ),
        **window_failure_profile(prime, window, spf),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=153_633_769)
    parser.add_argument("--window", type=int, default=31)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.prime, args.window)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
