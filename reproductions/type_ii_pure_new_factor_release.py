#!/usr/bin/env python3
"""Audit whether source-free new-factor states later admit a pure-new witness."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE_SCRIPT = ROOT / "reproductions" / "type_ii_single_new_factor_release.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-source-free-transition-h19-200m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-pure-new-factor-release-h19-200m-results.json"


def load_release_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_pure_new_factor_release_single", RELEASE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_single_new_factor_release.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


single = load_release_script()
transition = single.transition


def run_profile(payload: dict[str, object]) -> dict[str, object]:
    """Find the first later one-new witness with no collision factors."""
    limit = int(payload["prime_limit"])
    base_shift_bound = int(payload["base_shift_bound"])
    shift_cap = int(payload["shift_cap"])
    targets = [
        row
        for row in payload["profiles"]
        if row["selected_witness"]["new_multiplicity"] > 0
    ]
    trial_primes = single.primes_through(math.isqrt(limit + 4 * shift_cap))
    base_pairs = tuple(
        transition.canonical.canonical_pair(shift)
        for shift in range(1, base_shift_bound + 1)
    )
    collision_primes = set(
        transition.relay.collision.collision_primes(tuple(range(1, base_shift_bound + 1)))
    )
    profiles: list[dict[str, object]] = []
    missing: list[int] = []
    for row in targets:
        prime = int(row["prime"])
        old_source_primes = {
            factor
            for a, c in base_pairs
            for factor in single.factorization(prime + 4 * a * a * c, trial_primes)
        }
        selected = None
        for shift in range(int(row["first_source_free_shift"]), shift_cap + 1):
            candidate = single.source_free_one_new_witness(
                prime, shift, old_source_primes, collision_primes, trial_primes
            )
            if candidate is None or candidate["collision_multiplicity"]:
                continue
            selected = candidate
            profiles.append(
                {
                    "prime": prime,
                    "first_new_factor_shift": row["first_source_free_shift"],
                    "first_pure_new_shift": shift,
                    "selected_witness": selected,
                }
            )
            break
        if selected is None:
            missing.append(prime)
    return {
        "arithmetic": (
            "exact trial-prime factorization, complete divisor enumeration at every "
            "canonical shift, and reconstructed Type II certificate checks"
        ),
        "scope_note": (
            "A finite pure-new release audit. Missing points may release beyond the "
            "cap; the result does not assert a permanent obstruction."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "shift_cap": shift_cap,
        "new_factor_state_count": len(targets),
        "pure_new_release_count": len(profiles),
        "missing_through_cap": missing,
        "maximum_first_pure_new_shift": max(
            (row["first_pure_new_shift"] for row in profiles), default=None
        ),
        "profiles": profiles,
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
