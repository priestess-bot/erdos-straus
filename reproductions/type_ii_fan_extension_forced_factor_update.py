#!/usr/bin/env python3
"""Verify the exact forced-factor update under a canonical fan extension.

The one-private-cofactor model records the factor forced by a residue class
``p = Q*n + r`` at every shift ``s`` as ``gcd(Q, r + 4*s)``.  When a new
canonical ray enlarges ``Q``, the old factors must be recalculated from the
lifted residue; they are not determined by the old fan alone.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-fan-extension-forced-factor-update-h23.json"
BOUNDARY_SCRIPT = ROOT / "reproductions" / "type_ii_prime_cofactor_boundary.py"

H22_RESIDUE = 529
H23_RESIDUE = 1_474_353_409


def load_boundary_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_fan_extension_boundary", BOUNDARY_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_prime_cofactor_boundary.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


boundary = load_boundary_script()


def collision_primes(shifts: tuple[int, ...]) -> tuple[int, ...]:
    """Return primes that can divide two shifted integers in this fan."""
    return tuple(
        sorted(
            {
                prime
                for index, left in enumerate(shifts)
                for right in shifts[index + 1 :]
                for prime, _ in boundary.prime_factors(abs(right - left))
            }
        )
    )


def forced_factor_updates(
    old_modulus: int,
    new_modulus: int,
    old_residue: int,
    lifted_residue: int,
    old_shifts: tuple[int, ...],
) -> list[dict[str, int]]:
    """Return every old shift whose residue-forced factor changes.

    The calculation is exact for arbitrary nested moduli and a compatible
    residue lift.  It deliberately concerns the modular cofactor model, not
    actual common prime factors of two shifted integers.
    """
    if old_modulus < 1 or new_modulus < old_modulus:
        raise ValueError("moduli must be positive and nested")
    if new_modulus % old_modulus:
        raise ValueError("old_modulus must divide new_modulus")
    if lifted_residue % old_modulus != old_residue % old_modulus:
        raise ValueError("lifted_residue must reduce to old_residue")

    updates: list[dict[str, int]] = []
    for shift in old_shifts:
        old_factor = math.gcd(old_modulus, old_residue + 4 * shift)
        new_factor = math.gcd(new_modulus, lifted_residue + 4 * shift)
        if new_factor % old_factor:
            raise AssertionError("a nested modulus cannot remove a forced factor")
        if new_factor != old_factor:
            updates.append(
                {
                    "shift": shift,
                    "old_forced_factor": old_factor,
                    "new_forced_factor": new_factor,
                    "transferred_factor": new_factor // old_factor,
                }
            )
    return updates


def run_witness() -> dict[str, object]:
    """Rebuild the H=22 to H=23 update, including the no-collision distinction."""
    fan22 = boundary.canonical_fan(22)
    fan23 = boundary.canonical_fan(23)
    old_modulus = boundary.fan_modulus(fan22)
    new_modulus = boundary.fan_modulus(fan23)
    old_shifts = tuple(shift for shift, _, _ in fan22)
    new_shifts = tuple(shift for shift, _, _ in fan23)

    if new_modulus != 23 * old_modulus:
        raise AssertionError("the H=23 modulus growth must be exactly by 23")
    if H23_RESIDUE % old_modulus != H22_RESIDUE:
        raise AssertionError("the displayed H=23 residue must lift the H=22 residue")
    if new_shifts != old_shifts + (23,):
        raise AssertionError("the canonical H=23 fan must append shift 23")

    updates = forced_factor_updates(
        old_modulus,
        new_modulus,
        H22_RESIDUE,
        H23_RESIDUE,
        old_shifts,
    )
    expected_updates = [
        {
            "shift": 5,
            "old_forced_factor": 3,
            "new_forced_factor": 69,
            "transferred_factor": 23,
        }
    ]
    if updates != expected_updates:
        raise AssertionError("unexpected H=22 to H=23 forced-factor update")

    old_collisions = collision_primes(old_shifts)
    new_collisions = collision_primes(new_shifts)
    added_collisions = tuple(prime for prime in new_collisions if prime not in old_collisions)
    if added_collisions:
        raise AssertionError("H=23 renewal must not be caused by a new shift-difference prime")

    return {
        "arithmetic": (
            "exact gcd forced-factor calculations on nested fan moduli, plus the "
            "complete collision-prime comparison for the H=22 and H=23 shifts"
        ),
        "scope_note": (
            "This proves the modular state-update rule inside the one-private-cofactor "
            "model. It does not force an actual Type II certificate, a Type I bridge, "
            "or a terminating descent."
        ),
        "h22_to_h23": {
            "old_modulus": old_modulus,
            "new_modulus": new_modulus,
            "modulus_growth": new_modulus // old_modulus,
            "old_residue": H22_RESIDUE,
            "lifted_residue": H23_RESIDUE,
            "old_shift_count": len(old_shifts),
            "new_shift": new_shifts[-1],
            "old_collision_primes": list(old_collisions),
            "new_collision_primes": list(new_collisions),
            "added_collision_primes": list(added_collisions),
            "forced_factor_updates": updates,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_witness()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
