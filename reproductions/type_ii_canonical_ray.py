#!/usr/bin/env python3
"""Canonicalize the Type II ``A,C`` factor rays by their common shift.

Every raw ray has shifted integer ``p + 4*A^2*C``.  Writing
``s=A^2*C`` uniquely as ``a^2*c`` with squarefree ``c`` gives the canonical
ray for that shift.  Its modulus ``4*a*c`` divides the raw ray modulus, so
away from the finite order boundary it dominates every other representation
of the same shift.

The finite profile below is intentionally an exploratory coverage audit.  It
does not assert a global bound on the canonical shifts.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-canonical-rays-1m-results.json"
RAY_SCRIPT = ROOT / "reproductions" / "type_ii_ac_ray.py"
RESIDUE_SCRIPT = ROOT / "reproductions" / "divisor_residue_structure.py"


def load_ray_script():
    spec = importlib.util.spec_from_file_location("type_ii_ac_ray", RAY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_ac_ray.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ray = load_ray_script()


def load_residue_script():
    spec = importlib.util.spec_from_file_location(
        "divisor_residue_structure", RESIDUE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load divisor_residue_structure.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


residue_structure = load_residue_script()


def canonical_pair(shift_index: int) -> tuple[int, int]:
    """Return the unique ``(a,c)`` with ``shift_index=a^2*c`` and c squarefree."""
    if shift_index < 1:
        raise ValueError("shift_index must be positive")
    remaining = shift_index
    square_root = 1
    factor = 2
    while factor * factor <= remaining:
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        square_root *= factor ** (exponent // 2)
        factor = 3 if factor == 2 else factor + 2
    if remaining > 1:
        # The remaining prime has exponent one after trial division.
        pass
    squarefree = shift_index // (square_root * square_root)
    return square_root, squarefree


def canonical_modulus(shift_index: int) -> int:
    """Return ``4*a*c`` for the canonical representation of a shift."""
    a, c = canonical_pair(shift_index)
    return 4 * a * c


def canonical_dominates_raw_pair(a: int, c: int) -> bool:
    """Check the divisibility relation behind canonical-ray domination."""
    if a < 1 or c < 1:
        raise ValueError("a and c must be positive")
    shift_index = a * a * c
    canonical_a, canonical_c = canonical_pair(shift_index)
    return (
        canonical_a % a == 0
        and 4 * canonical_a * canonical_c <= 4 * a * c
        and (4 * a * c) % (4 * canonical_a * canonical_c) == 0
    )


def canonical_pairs_from_box(ac_bound: int) -> tuple[tuple[int, int], ...]:
    """Deduplicate an AC box into its canonical shifts."""
    if ac_bound < 1:
        raise ValueError("ac_bound must be positive")
    return tuple(
        sorted(
            {
                canonical_pair(a * a * c)
                for a in range(1, ac_bound + 1)
                for c in range(1, ac_bound + 1)
            }
        )
    )


def witness_for_pair(
    prime: int, pair: tuple[int, int], smallest_factors: list[int]
) -> dict[str, int] | None:
    """Return one exact canonical-ray witness, if it exists."""
    a, c = pair
    shifted = prime + 4 * a * a * c
    for h in ray.divisors(shifted, smallest_factors):
        modulus = 4 * a * c
        if h <= 1 or (h + 1) % modulus:
            continue
        k = (h + 1) // modulus
        certificate = ray.short_certificate.type_ii_raw_ray_certificate(
            prime, a, c, k
        )
        if certificate is not None:
            return {
                "a": a,
                "c": c,
                "shift_index": a * a * c,
                "h": h,
                "k": k,
                "gap": certificate.gap,
                "divisor": certificate.divisor,
            }
    return None


def joint_failure_profile(
    primes: list[int],
    pairs: set[tuple[int, int]],
    smallest_factors: list[int],
) -> dict[str, object]:
    """Describe every failure of a fixed canonical-ray family exactly.

    The labels deliberately retain full factorization data.  A support-outside
    failure and a support-inside defect have different algebraic constraints,
    so collapsing them to a Boolean miss would discard the information needed
    for a prospective multi-shift argument.
    """
    profiles: list[dict[str, object]] = []
    signature_histogram: dict[str, int] = {}
    ordered_pairs = tuple(sorted(pairs))
    for prime in primes:
        ray_profiles: list[dict[str, object]] = []
        signature: list[str] = []
        for a, c in ordered_pairs:
            analysis = residue_structure.support_critical_ray_analysis(
                prime, a, c, smallest_factors
            )
            if not analysis["failed"]:
                raise AssertionError("joint failure profile received a captured prime")
            if analysis["target_in_support"]:
                label = f"inside:{len(analysis['defect'])}"
            else:
                label = f"outside:{analysis['target_outside_two_power_depth']}"
            signature.append(label)
            ray_profiles.append(
                {
                    "pair": {"a": a, "c": c},
                    "shift_index": a * a * c,
                    "modulus": analysis["modulus"],
                    "shifted": analysis["shifted"],
                    "factorization": analysis["factorization"],
                    "class": label,
                    "target_in_support": analysis["target_in_support"],
                    "defect_size": (
                        len(analysis["defect"])
                        if analysis["target_in_support"]
                        else None
                    ),
                    "two_power_depth": analysis["target_outside_two_power_depth"],
                }
            )
        signature_key = ",".join(signature)
        signature_histogram[signature_key] = signature_histogram.get(signature_key, 0) + 1
        profiles.append(
            {
                "prime": prime,
                "signature": signature,
                "rays": ray_profiles,
            }
        )
    return {
        "profiles": profiles,
        "signature_histogram": signature_histogram,
    }


def run_profile(
    limit: int, ac_bound: int, base_shift_bound: int
) -> dict[str, object]:
    """Audit canonical shifts and a deterministic greedy complement."""
    if limit < 73 or ac_bound < 1 or base_shift_bound < 1:
        raise ValueError("limit >= 73 and positive bounds are required")
    pairs = canonical_pairs_from_box(ac_bound)
    max_shift = max(a * a * c for a, c in pairs)
    smallest_factors = ray.short_certificate.smallest_prime_factors(
        limit + 4 * max_shift
    )
    primes = [
        prime
        for prime in ray.short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    captures: dict[tuple[int, int], set[int]] = {pair: set() for pair in pairs}
    for prime in primes:
        for pair in pairs:
            if witness_for_pair(prime, pair, smallest_factors) is not None:
                captures[pair].add(prime)

    base_pairs = {
        canonical_pair(shift_index)
        for shift_index in range(1, base_shift_bound + 1)
    }
    if not base_pairs.issubset(captures):
        raise AssertionError("base shifts must be available in the selected box")
    remaining = set(primes)
    for pair in base_pairs:
        remaining.difference_update(captures[pair])
    base_missing = sorted(remaining)
    joint_profiles = joint_failure_profile(base_missing, base_pairs, smallest_factors)

    candidate_pairs = set(pairs) - base_pairs
    greedy: list[dict[str, object]] = []
    while remaining:
        best = max(
            candidate_pairs,
            key=lambda pair: (len(remaining & captures[pair]), -pair[0], -pair[1]),
        )
        covered = sorted(remaining & captures[best])
        if not covered:
            break
        greedy.append(
            {
                "pair": {"a": best[0], "c": best[1]},
                "shift_index": best[0] * best[0] * best[1],
                "covered_count": len(covered),
                "covered_primes": covered,
            }
        )
        remaining.difference_update(covered)
        candidate_pairs.remove(best)

    return {
        "arithmetic": (
            "exact SPF factorization, divisor residue tests, and Type II "
            "certificate verification"
        ),
        "scope_note": (
            "The greedy list is a finite diagnostic, not a proof that this or any "
            "fixed canonical-shift set covers all core primes."
        ),
        "prime_limit": limit,
        "source_ac_box": {"a_max": ac_bound, "c_max": ac_bound},
        "canonical_pair_count": len(pairs),
        "largest_shift_index": max_shift,
        "base_shift_bound": base_shift_bound,
        "base_pair_count": len(base_pairs),
        "core_prime_count": len(primes),
        "base_captured_count": len(primes) - len(base_missing),
        "base_missing": base_missing,
        "joint_base_failure_profiles": joint_profiles["profiles"],
        "joint_base_failure_signature_histogram": joint_profiles[
            "signature_histogram"
        ],
        "greedy_complement": greedy,
        "remaining_after_greedy": sorted(remaining),
        "canonical_box_captured_count": len(primes) - len(remaining),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--ac-bound", type=int, default=14)
    parser.add_argument("--base-shift-bound", type=int, default=14)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_profile(args.limit, args.ac_bound, args.base_shift_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
