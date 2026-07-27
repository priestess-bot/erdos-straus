#!/usr/bin/env python3
"""Measure the delayed one-new-factor release at the first two-collision state."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SINGLE_SCRIPT = ROOT / "reproductions" / "type_ii_single_new_factor_release.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-two-collision-release-372271201-results.json"
)
PRIME = 372_271_201
BASE_SHIFT_BOUND = 19
CAPS = (200, 400, 401, 483, 484)


def load_single_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_h19_two_collision_release_single", SINGLE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_single_new_factor_release.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


single = load_single_script()


def serialize(
    prime: int,
    shift: int,
    witness: dict[str, object],
    collision_primes: set[int],
) -> dict[str, object]:
    """Record each collision factor together with its forced H19 source class."""
    labels: list[dict[str, object]] = []
    for factor in witness["h_factorization"]:
        collision_prime = int(factor["prime"])
        if collision_prime not in collision_primes:
            continue
        sources = [
            source
            for source in range(1, BASE_SHIFT_BOUND + 1)
            if (prime + 4 * source) % collision_prime == 0
        ]
        if not sources or any((shift - source) % collision_prime for source in sources):
            raise AssertionError("collision factor violates its H19 source class")
        labels.append(
            {
                "prime": collision_prime,
                "source_shifts": sources,
                "target_shift_residue": shift % collision_prime,
            }
        )
    return {
        "shift": shift,
        "h": witness["h"],
        "h_factorization": witness["h_factorization"],
        "a": witness["a"],
        "c": witness["c"],
        "k": witness["k"],
        "collision_multiplicity": witness["collision_multiplicity"],
        "new_multiplicity": witness["new_multiplicity"],
        "collision_source_labels": labels,
    }


def run_audit(prime: int = PRIME, caps: tuple[int, ...] = CAPS) -> dict[str, object]:
    """Enumerate every single-new witness through the requested depth caps."""
    if tuple(sorted(set(caps))) != caps or caps[0] <= BASE_SHIFT_BOUND:
        raise ValueError("caps must be increasing and exceed the H19 bound")
    trial_primes = single.primes_through(math.isqrt(prime + 4 * caps[-1]))
    base_pairs = tuple(
        single.transition.canonical.canonical_pair(shift)
        for shift in range(1, BASE_SHIFT_BOUND + 1)
    )
    old_source_primes = {
        factor
        for a, c in base_pairs
        for factor in single.factorization(prime + 4 * a * a * c, trial_primes)
    }
    collision_primes = set(
        single.transition.relay.collision.collision_primes(
            tuple(range(1, BASE_SHIFT_BOUND + 1))
        )
    )
    candidates: list[tuple[int, dict[str, object]]] = []
    for shift in range(BASE_SHIFT_BOUND + 1, caps[-1] + 1):
        witness = single.source_free_one_new_witness(
            prime, shift, old_source_primes, collision_primes, trial_primes
        )
        if witness is not None:
            candidates.append((shift, witness))
    rows: list[dict[str, object]] = []
    for cap in caps:
        through = [(shift, witness) for shift, witness in candidates if shift <= cap]
        best = min(
            through,
            key=lambda item: (
                int(item[1]["collision_multiplicity"]),
                item[0],
                int(item[1]["h"]),
            ),
            default=None,
        )
        first_zero_or_one = next(
            (
                (shift, witness)
                for shift, witness in through
                if int(witness["collision_multiplicity"]) <= 1
            ),
            None,
        )
        first_pure = next(
            (
                (shift, witness)
                for shift, witness in through
                if int(witness["collision_multiplicity"]) == 0
            ),
            None,
        )
        rows.append(
            {
                "shift_cap": cap,
                "single_new_candidate_count": len(through),
                "best_witness": (
                    None
                    if best is None
                    else serialize(prime, *best, collision_primes)
                ),
                "first_zero_or_one_collision": (
                    None
                    if first_zero_or_one is None
                    else serialize(prime, *first_zero_or_one, collision_primes)
                ),
                "first_pure_new": (
                    None
                    if first_pure is None
                    else serialize(prime, *first_pure, collision_primes)
                ),
            }
        )
    return {
        "arithmetic": (
            "exact trial factorization and complete one-new-factor Type II "
            "enumeration at every shift through each stated cap"
        ),
        "scope_note": (
            "A single-state release-depth audit. It does not give a uniform "
            "release bound for the H19 residual family."
        ),
        "prime": prime,
        "base_shift_bound": BASE_SHIFT_BOUND,
        "collision_primes": sorted(collision_primes),
        "caps": list(caps),
        "records": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
