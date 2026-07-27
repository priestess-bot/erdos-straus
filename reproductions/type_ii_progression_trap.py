#!/usr/bin/env python3
"""Find fixed-factor Type II certificates on moving-window progressions.

For p=p0+16*Q*k, where Q is the lcm of 24 and a finite moving window,
x=(p+m)/4 has the form E*N with E=gcd(4*Q,x0).  If N is fixed modulo
the future gap m and a divisor a of E gives a*N=-x modulo m, then
d=a*N is a direct Type II certificate throughout the progression.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-progression-trap-results.json"


def window_modulus(window: int) -> int:
    if window < 1:
        raise ValueError("window must be positive")
    modulus = 24
    for j in range(1, window + 1):
        modulus = math.lcm(modulus, 4 * j - 1)
    return modulus


def factorization(value: int) -> tuple[tuple[int, int], ...]:
    """Factor a fixed divisor whose primes come from the window modulus."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            exponent = 0
            while value % divisor == 0:
                value //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return tuple(factors)


def divisors(factors: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    values = [1]
    for prime, exponent in factors:
        values = [
            value * prime**power
            for value in values
            for power in range(exponent + 1)
        ]
    return tuple(sorted(values))


def find_traps(
    seed_prime: int, window: int, extension_window: int
) -> tuple[dict[str, int | tuple[tuple[int, int], ...]], ...]:
    """Return every fixed-factor progression certificate in the scan interval."""
    if (
        seed_prime % 24 != 1
        or window < 1
        or extension_window <= window
    ):
        raise ValueError("seed must be core-residue and the scan must extend window")
    modulus = window_modulus(window)
    x_step = 4 * modulus
    traps: list[dict[str, int | tuple[tuple[int, int], ...]]] = []
    for j in range(window + 1, extension_window + 1):
        gap = 4 * j - 1
        if not 3 <= gap <= seed_prime - 2:
            continue
        x0 = (seed_prime + gap) // 4
        if 4 * x0 != seed_prime + gap:
            raise AssertionError("gap did not preserve integrality")
        fixed_factor = math.gcd(x_step, x0)
        if x_step // fixed_factor % gap:
            continue
        cofactor0 = x0 // fixed_factor
        factors = factorization(fixed_factor)
        target = (-x0) % gap
        for scale in divisors(factors):
            if scale * cofactor0 % gap != target:
                continue
            traps.append(
                {
                    "window_j": window,
                    "future_j": j,
                    "gap": gap,
                    "window_modulus": modulus,
                    "prime_step": 16 * modulus,
                    "seed_prime": seed_prime,
                    "fixed_factor": fixed_factor,
                    "fixed_factorization": factors,
                    "cofactor0": cofactor0,
                    "cofactor_residue_mod_gap": cofactor0 % gap,
                    "target_scale": scale,
                    "target_residue_mod_gap": target,
                }
            )
            break
    return tuple(traps)


def find_all_divisor_traps(
    seed_prime: int, window: int
) -> tuple[int, tuple[dict[str, int | tuple[tuple[int, int], ...]], ...]]:
    """Exhaust every future gap that can satisfy the fixed-factor condition.

    Condition m | 4Q/E from the trap lemma implies m | 4Q.  Thus enumerating
    the divisors of 4Q is a complete finite check for this mechanism, not a
    bounded future-window scan.
    """
    if seed_prime % 24 != 1 or window < 1:
        raise ValueError("seed must be core-residue and window positive")
    modulus = window_modulus(window)
    x_step = 4 * modulus
    first_gap = 4 * window - 1
    candidates = 0
    traps: list[dict[str, int | tuple[tuple[int, int], ...]]] = []
    for gap in divisors(factorization(x_step)):
        if gap % 4 != 3 or not first_gap < gap <= seed_prime - 2:
            continue
        candidates += 1
        x0 = (seed_prime + gap) // 4
        fixed_factor = math.gcd(x_step, x0)
        if x_step // fixed_factor % gap:
            continue
        cofactor0 = x0 // fixed_factor
        factors = factorization(fixed_factor)
        target = (-x0) % gap
        for scale in divisors(factors):
            if scale * cofactor0 % gap != target:
                continue
            traps.append(
                {
                    "window_j": window,
                    "future_j": (gap + 1) // 4,
                    "gap": gap,
                    "window_modulus": modulus,
                    "prime_step": 16 * modulus,
                    "seed_prime": seed_prime,
                    "fixed_factor": fixed_factor,
                    "fixed_factorization": factors,
                    "cofactor0": cofactor0,
                    "cofactor_residue_mod_gap": cofactor0 % gap,
                    "target_scale": scale,
                    "target_residue_mod_gap": target,
                }
            )
            break
    return candidates, tuple(sorted(traps, key=lambda trap: int(trap["gap"])))


def certificate_at_index(
    trap: dict[str, int | tuple[tuple[int, int], ...]], index: int
) -> dict[str, int | bool]:
    """Construct and verify the direct certificate for one progression member."""
    if index < 0:
        raise ValueError("index must be nonnegative")
    step = int(trap["prime_step"])
    seed = int(trap["seed_prime"])
    gap = int(trap["gap"])
    fixed = int(trap["fixed_factor"])
    scale = int(trap["target_scale"])
    prime = step * index + seed
    if not 3 <= gap <= prime - 2:
        raise AssertionError("gap lies outside the Type II natural range")
    x = (prime + gap) // 4
    if x % fixed:
        raise AssertionError("fixed factor does not divide x")
    cofactor = x // fixed
    divisor = scale * cofactor
    if (
        divisor > x
        or x * x % divisor
        or (x + divisor) % gap
    ):
        raise AssertionError("trap did not reconstruct a Type II certificate")
    y = prime * (x + divisor) // gap
    z = prime * (x + x * x // divisor) // gap
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


def run_audit(
    seed_prime: int = 153_633_769,
    window: int = 31,
    extension_window: int = 131,
    all_divisors: bool = False,
) -> dict[str, object]:
    candidate_gap_count = None
    if all_divisors:
        candidate_gap_count, traps = find_all_divisor_traps(seed_prime, window)
    else:
        traps = find_traps(seed_prime, window, extension_window)
    if not traps:
        return {
            "arithmetic": (
                "exact gcd extraction, divisor enumeration of the fixed factor, "
                "and fractions.Fraction certificate verification"
            ),
            "scope_note": (
                "No fixed-factor progression trap was found in the stated "
                "finite extension interval."
            ),
            "seed_prime": seed_prime,
            "window_j": window,
            "extension_window_j": extension_window,
            "all_divisor_mode": all_divisors,
            "candidate_gap_count": candidate_gap_count,
            "traps": [],
        }
    first = traps[0]
    primitive_progression = math.gcd(
        int(first["prime_step"]), int(first["seed_prime"])
    ) == 1
    return {
        "arithmetic": (
            "exact gcd extraction, divisor enumeration of the fixed factor, "
            "and fractions.Fraction certificate verification"
        ),
        "scope_note": (
            "Each listed trap gives a direct Type II certificate for every core "
            "prime in its displayed arithmetic progression. A primitive listed "
            "progression contains infinitely many primes by Dirichlet's theorem."
        ),
        "seed_prime": seed_prime,
        "window_j": window,
        "extension_window_j": extension_window,
        "all_divisor_mode": all_divisors,
        "candidate_gap_count": candidate_gap_count,
        "primitive_progression": primitive_progression,
        "traps": list(traps),
        "first_trap_samples": [
            certificate_at_index(first, index) for index in (0, 1, 2)
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-prime", type=int, default=153_633_769)
    parser.add_argument("--window", type=int, default=31)
    parser.add_argument("--extension-window", type=int, default=131)
    parser.add_argument(
        "--all-divisors",
        action="store_true",
        help="exhaust every gap divisor of 4Q permitted by the trap lemma",
    )
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(
        args.seed_prime, args.window, args.extension_window, args.all_divisors
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
