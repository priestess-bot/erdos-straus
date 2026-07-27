#!/usr/bin/env python3
"""Exhibit a modulus-expansion renewal in the Type II cofactor model.

The H=22 canonical fan has no admissible second-level one-prime-cofactor
branch at its fixed modulus.  The next canonical ray introduces the prime 23
into the modulus.  This script gives an exact CRT lift of an H=22-safe residue
whose H=23 second-level branch is admissible again.

This is a boundary witness for the simplified cofactor model.  Conditional
prime-tuple consequences must not be read as counterexamples to, or proofs of,
the Erdos--Straus conjecture.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT / "reproductions" / "type-ii-prime-cofactor-renewal-h23-witness.json"
)
BOUNDARY_SCRIPT = ROOT / "reproductions" / "type_ii_prime_cofactor_boundary.py"

H22_RESIDUE = 529
H23_RESIDUE = 1_474_353_409
CHANGED_SHIFT = 5
SECOND_LEVEL_BRANCH = 0


def load_boundary_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_prime_cofactor_boundary", BOUNDARY_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_prime_cofactor_boundary.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


boundary = load_boundary_script()


def run_witness() -> dict[str, object]:
    """Return the exact H=22 to H=23 modulus-renewal witness."""
    fan22 = boundary.canonical_fan(22)
    fan23 = boundary.canonical_fan(23)
    modulus22 = boundary.fan_modulus(fan22)
    modulus23 = boundary.fan_modulus(fan23)

    if modulus23 != 23 * modulus22:
        raise AssertionError("H=23 must introduce exactly the modulus prime 23")
    if H23_RESIDUE % modulus22 != H22_RESIDUE:
        raise AssertionError("the selected residue is not an H=22 CRT lift")
    if H23_RESIDUE % 23 != 3:
        raise AssertionError("the lift must force the new divisor at shift five")

    h22_safe = all(
        boundary.ray_safe_with_one_prime_cofactor(
            H22_RESIDUE, modulus22, shift, a, c
        )
        for shift, a, c in fan22
    )
    h23_safe = all(
        boundary.ray_safe_with_one_prime_cofactor(
            H23_RESIDUE, modulus23, shift, a, c
        )
        for shift, a, c in fan23
    )
    if not h22_safe or not h23_safe:
        raise AssertionError("the selected residues must be safe in both fans")

    h22_branches: dict[int, tuple[int, ...]] = {}
    for branch in range(3):
        value = boundary.second_level_branch(
            H22_RESIDUE, branch, modulus22, fan22
        )
        if value is None:
            raise AssertionError("the H=22 branch must survive the ray test")
        forms, _ = value
        h22_branches[branch] = boundary.covering_primes(forms)
    if h22_branches != {0: (23,), 1: (23,), 2: (3, 23)}:
        raise AssertionError("unexpected H=22 obstruction profile")

    h23 = boundary.second_level_branch(
        H23_RESIDUE, SECOND_LEVEL_BRANCH, modulus23, fan23
    )
    if h23 is None:
        raise AssertionError("the H=23 branch must survive the ray test")
    forms, factors = h23
    h23_covering_primes = boundary.covering_primes(forms)
    if h23_covering_primes:
        raise AssertionError("the H=23 linear forms must be admissible")

    changed = next(
        row for row in factors if row["shift"] == CHANGED_SHIFT
    )
    if changed != {
        "shift": CHANGED_SHIFT,
        "forced_divisor": 69,
        "extra_three_power": 0,
        "fixed_factor": 69,
    }:
        raise AssertionError("unexpected new forced factor at shift five")

    return {
        "arithmetic": (
            "exact CRT congruences, exact forced-divisor computations, and "
            "finite-field admissibility checks for the displayed linear forms"
        ),
        "scope_note": (
            "This is a renewal witness only in the one-prime-private-cofactor "
            "model. Under a Dickson/Schinzel prime-tuple hypothesis its "
            "admissible forms give a conditional escape family; it is neither "
            "an unconditional family nor a counterexample to Erdos--Straus."
        ),
        "h22": {
            "fan_bound": 22,
            "modulus": modulus22,
            "residue_class": H22_RESIDUE,
            "second_level_covering_primes": {
                str(branch): list(primes)
                for branch, primes in sorted(h22_branches.items())
            },
        },
        "h23": {
            "fan_bound": 23,
            "modulus": modulus23,
            "residue_class": H23_RESIDUE,
            "residue_mod_h22_modulus": H23_RESIDUE % modulus22,
            "residue_mod_23": H23_RESIDUE % 23,
            "changed_shift": CHANGED_SHIFT,
            "changed_shift_forced_factor": changed,
            "second_level_branch": SECOND_LEVEL_BRANCH,
            "second_level_form_count": len(forms),
            "second_level_covering_primes": list(h23_covering_primes),
            "forms": [
                {"coefficient": coefficient, "constant": constant, "label": label}
                for coefficient, constant, label in forms
            ],
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
