#!/usr/bin/env python3
"""Extend the 3,7,11 shared Type II fan by one selected prime factor."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-small-shared-gap-single-prime-10m-results.json"
BASE = ROOT / "reproductions" / "type_ii_small_shared_gap_fan.py"


def load_base():
    spec = importlib.util.spec_from_file_location(
        "type_ii_small_shared_gap_single_prime_base", BASE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_small_shared_gap_fan.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_base()
short_certificate = base.short_certificate


@dataclass(frozen=True)
class SinglePrimeFanWitness:
    prime: int
    gap: int
    x: int
    type_ii_divisor: int
    shared_divisor: int
    selected_prime: int | None
    branch: str


def factor_in_residues(
    value: int, modulus: int, residues: frozenset[int], spf: list[int]
) -> int | None:
    """Return one prime factor of value in a permitted nonzero residue class."""
    if value < 1 or value >= len(spf):
        raise ValueError("SPF table does not cover the value")
    while value > 1:
        prime = spf[value]
        if prime % modulus in residues:
            return prime
        while value % prime == 0:
            value //= prime
    return None


def from_base(
    witness: base.SmallSharedGapWitness,
) -> SinglePrimeFanWitness:
    return SinglePrimeFanWitness(
        witness.prime,
        witness.gap,
        witness.x,
        witness.type_ii_divisor,
        witness.shared_divisor,
        None,
        witness.branch,
    )


def single_prime_fan_witness(
    prime: int, spf: list[int]
) -> SinglePrimeFanWitness | None:
    """Return the first shared Type II witness in the one-prime 3,7,11 fan."""
    witness = base.small_shared_gap_witness(prime, spf)
    if witness is not None:
        return from_base(witness)
    if prime % 24 != 1 or prime < 73:
        return None

    residue_seven = prime % 7
    m7_conditions = {
        1: (frozenset({5}), 1),
        2: (frozenset({3}), 1),
        4: (frozenset({3}), 2),
    }
    allowed_seven, multiplier_seven = m7_conditions[residue_seven]
    selected = factor_in_residues(
        (prime + 7) // 8, 7, allowed_seven, spf
    )
    if selected is not None:
        witness = base.build_witness(
            prime,
            7,
            multiplier_seven * selected,
            8,
            "m7_single_prime",
        )
        return SinglePrimeFanWitness(
            witness.prime,
            witness.gap,
            witness.x,
            witness.type_ii_divisor,
            witness.shared_divisor,
            selected,
            witness.branch,
        )

    residue_eleven = prime % 11
    if residue_eleven in {7, 8, 10}:
        raise AssertionError("the base fan should already capture this residue")
    target = (-3 * residue_eleven) % 11
    selected = factor_in_residues(
        (prime + 11) // 12, 11, frozenset({target, (4 * target) % 11}), spf
    )
    if selected is None:
        return None
    multiplier_eleven = 1 if selected % 11 == target else 3
    witness = base.build_witness(
        prime,
        11,
        multiplier_eleven * selected,
        12,
        "m11_single_prime",
    )
    return SinglePrimeFanWitness(
        witness.prime,
        witness.gap,
        witness.x,
        witness.type_ii_divisor,
        witness.shared_divisor,
        selected,
        witness.branch,
    )


def run_audit(limit: int, sample_cap: int = 20) -> dict[str, object]:
    """Audit the proved single-prime fan with exact SPF factorization."""
    if limit < 73 or sample_cap < 0:
        raise ValueError("limit must be at least 73 and sample_cap nonnegative")
    spf = short_certificate.smallest_prime_factors(limit + 11)
    counts = {
        "m3_factor_2_mod_3": 0,
        "m7_explicit_residue": 0,
        "m7_single_prime": 0,
        "m11_explicit_residue": 0,
        "m11_single_prime": 0,
        "single_prime_residual": 0,
    }
    samples = {key: [] for key in counts}
    core_prime_count = 0
    for prime in short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        core_prime_count += 1
        witness = single_prime_fan_witness(prime, spf)
        branch = witness.branch if witness is not None else "single_prime_residual"
        counts[branch] += 1
        if len(samples[branch]) < sample_cap:
            samples[branch].append(prime)
    covered = core_prime_count - counts["single_prime_residual"]
    return {
        "arithmetic": (
            "exact SPF factorization and exact integer verification of every "
            "one-prime Type II divisor and shared divisor"
        ),
        "scope_note": (
            "This is a proved sufficient one-prime subfan. Its residual can "
            "still have multi-prime divisor certificates at the same gaps."
        ),
        "prime_limit": limit,
        "core_prime_count": core_prime_count,
        "counts": counts,
        "covered_count": covered,
        "covered_ratio": covered / core_prime_count,
        "samples": samples,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--sample-cap", type=int, default=20)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.sample_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
