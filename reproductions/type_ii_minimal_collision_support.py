#!/usr/bin/env python3
"""Measure the least collision support needed by H19 one-new-factor witnesses."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE_SCRIPT = ROOT / "reproductions" / "type_ii_single_new_factor_release.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-source-free-transition-h19-200m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-minimal-collision-support-h19-200m-results.json"


def load_release_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_minimal_collision_support_single", RELEASE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_single_new_factor_release.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


single = load_release_script()
transition = single.transition


def run_profile(
    payload: dict[str, object], shift_cap_override: int | None = None
) -> dict[str, object]:
    """Find each state\'s least collision multiplicity over the audited window."""
    limit = int(payload["prime_limit"])
    base_shift_bound = int(payload["base_shift_bound"])
    shift_cap = (
        int(payload["shift_cap"])
        if shift_cap_override is None
        else shift_cap_override
    )
    if shift_cap <= base_shift_bound:
        raise ValueError("shift cap must exceed the H19 base shift bound")
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
        candidates: list[tuple[int, int, dict[str, object]]] = []
        for shift in range(int(row["first_source_free_shift"]), shift_cap + 1):
            witness = single.source_free_one_new_witness(
                prime, shift, old_source_primes, collision_primes, trial_primes
            )
            if witness is not None:
                candidates.append((int(witness["collision_multiplicity"]), shift, witness))
        if not candidates:
            missing.append(prime)
            continue
        multiplicity, shift, witness = min(candidates, key=lambda item: (item[0], item[1], item[2]["h"]))
        profiles.append(
            {
                "prime": prime,
                "first_new_factor_shift": row["first_source_free_shift"],
                "minimum_collision_multiplicity": multiplicity,
                "first_minimum_collision_shift": shift,
                "selected_witness": witness,
            }
        )
    multiplicities = Counter(row["minimum_collision_multiplicity"] for row in profiles)
    one_collision_primes = Counter(
        factor["prime"]
        for row in profiles
        if row["minimum_collision_multiplicity"] == 1
        for factor in row["selected_witness"]["h_factorization"]
        if factor["prime"] in collision_primes
    )
    return {
        "arithmetic": (
            "exact trial-prime factorization, complete divisor enumeration at every "
            "canonical shift, and reconstructed Type II certificate checks"
        ),
        "scope_note": (
            "A finite minimal-collision-support audit. A positive minimum means only "
            "that pure-new witnesses do not occur within the stated window."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "shift_cap": shift_cap,
        "new_factor_state_count": len(targets),
        "one_new_witness_count": len(profiles),
        "missing_through_cap": missing,
        "minimum_collision_multiplicity_distribution": dict(sorted(multiplicities.items())),
        "one_collision_prime_distribution": dict(sorted(one_collision_primes.items())),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--shift-cap",
        type=int,
        help="override the input profile's later canonical-shift cap",
    )
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_profile(payload, args.shift_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
