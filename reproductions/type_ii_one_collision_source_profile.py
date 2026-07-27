#!/usr/bin/env python3
"""Audit the source congruences in one-collision H19 Type II witnesses."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-one-collision-source-h19-1b-results.json"


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def run_profile(payload: dict[str, object]) -> dict[str, object]:
    """Extract and verify the forced source class for each one-collision witness."""
    base_shift_bound = int(payload["base_shift_bound"])
    collision_primes = {
        divisor
        for left in range(1, base_shift_bound + 1)
        for right in range(left + 1, base_shift_bound + 1)
        for divisor in range(2, right - left + 1)
        if (right - left) % divisor == 0 and is_prime(divisor)
    }
    records: list[dict[str, object]] = []
    for row in payload["profiles"]:
        if row["minimum_collision_multiplicity"] != 1:
            continue
        witness = row["selected_witness"]
        factors = witness["h_factorization"]
        prime = int(row["prime"])
        shift = int(row["first_minimum_collision_shift"])
        a = int(witness["a"])
        c = int(witness["c"])
        modulus = 4 * a * c
        collision_factors = [
            factor for factor in factors if factor["prime"] in collision_primes
        ]
        if len(collision_factors) != 1 or collision_factors[0]["exponent"] != 1:
            raise AssertionError("expected exactly one first-power collision factor")
        collision_prime = int(collision_factors[0]["prime"])
        new_factors = [
            factor for factor in factors if factor["prime"] != collision_prime
        ]
        if len(new_factors) != 1 or new_factors[0]["exponent"] != 1:
            raise AssertionError("expected exactly one first-power new factor")
        new_prime = int(new_factors[0]["prime"])
        sources = [
            source
            for source in range(1, base_shift_bound + 1)
            if (prime + 4 * source) % collision_prime == 0
        ]
        if not sources:
            raise AssertionError("collision factor has no H19 source")
        if any((shift - source) % collision_prime for source in sources):
            raise AssertionError("target shift violates the collision source class")
        if (collision_prime * new_prime + 1) % modulus:
            raise AssertionError("certificate factor does not meet the Type II residue")
        if modulus % collision_prime == 0:
            raise AssertionError("a collision factor cannot divide the target modulus")
        if new_prime % modulus != (-pow(collision_prime, -1, modulus)) % modulus:
            raise AssertionError("new factor violates the forced inverse residue")
        records.append(
            {
                "prime": prime,
                "collision_prime": collision_prime,
                "new_prime": new_prime,
                "source_shifts": sources,
                "target_shift": shift,
                "a": a,
                "c": c,
                "target_modulus": modulus,
                "new_prime_target_residue": new_prime % modulus,
                "forced_target_residue": (-pow(collision_prime, -1, modulus)) % modulus,
            }
        )
    return {
        "arithmetic": (
            "exact divisibility and modular-inverse checks on the selected "
            "one-collision Type II witnesses"
        ),
        "scope_note": (
            "This records a necessary congruence structure in a finite profile; "
            "it does not prove the one-collision selector."
        ),
        "prime_limit": payload["prime_limit"],
        "base_shift_bound": base_shift_bound,
        "one_collision_state_count": len(records),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_profile(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
