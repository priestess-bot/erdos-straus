#!/usr/bin/env python3
"""Compile the 14 post-affine H19-k23 states for multi-source descent work.

Each state records all 37 stationary external source denominators n_k=F_k*N_k,
their complete square-tail target failure, and the finite source/source,
source/ray, and ray/ray collision-prime label.  It is a state compiler, not
a proof that the remaining private factors select a descent.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "h19-k23-multisource-marked-state.json"
MIXED_BOUNDARY_SCRIPT = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"


def load_mixed_boundary():
    spec = importlib.util.spec_from_file_location(
        "mixed_factor_h19_uniform_affine_boundary_for_state_compiler",
        MIXED_BOUNDARY_SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load mixed-factor boundary")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


mixed_boundary = load_mixed_boundary()
branching = mixed_boundary.branching


def distinct_prime_factors(value: int) -> tuple[int, ...]:
    if value < 1:
        raise ValueError("value must be positive")
    result = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            result.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result.append(value)
    return tuple(result)


def pair_collision_bound(left: int, right: int) -> int:
    return abs(left - right) // math.gcd(left, right)


def source_ray_collision_bound(scale: int, shift: int) -> int:
    return abs(4 * shift * (4 * scale - 1) - 1)


def collision_label(scales: tuple[int, ...], shifts: tuple[int, ...]) -> dict[str, object]:
    """Return the complete finite collision-prime label for this scale set."""
    source_primes: set[int] = set()
    joint_primes: set[int] = set()
    for index, left in enumerate(scales):
        for right in scales[index + 1 :]:
            primes = distinct_prime_factors(pair_collision_bound(left, right))
            source_primes.update(primes)
            joint_primes.update(primes)
    for index, left in enumerate(shifts):
        for right in shifts[index + 1 :]:
            joint_primes.update(distinct_prime_factors(abs(left - right)))
    for scale in scales:
        for shift in shifts:
            joint_primes.update(
                distinct_prime_factors(source_ray_collision_bound(scale, shift))
            )
    return {
        "source_collision_primes": sorted(source_primes),
        "joint_collision_primes": sorted(joint_primes),
    }


def source_state(coefficient: int, constant: int, scale: int) -> dict[str, object]:
    """Compile a stationary source affine form and verify its square-tail miss."""
    profile, _ = branching.source_profile(coefficient, constant, scale)
    q = 4 * scale - 1
    denominator = 4 * scale
    source_coefficient = q * coefficient // denominator
    source_constant = (q * constant + 1) // denominator
    fixed_factor = math.gcd(source_coefficient, source_constant)
    if fixed_factor != profile["fixed_factor"]:
        raise AssertionError("inconsistent fixed source factor")
    if profile["target_hits"]:
        raise AssertionError("post-affine state unexpectedly has source descent")
    return {
        "k": scale,
        "q": q,
        "source_form": {
            "coefficient": source_coefficient,
            "constant": source_constant,
        },
        "fixed_factor": fixed_factor,
        "private_form": {
            "coefficient": source_coefficient // fixed_factor,
            "constant": source_constant // fixed_factor,
        },
        "square_tail_target_residue": profile["target_residue"],
        "square_tail_divisor_residue_count": profile["divisor_residue_count"],
        "complete_square_tail_hit": False,
    }


def run_audit() -> dict[str, object]:
    branches = mixed_boundary.remaining_branches()
    scales = tuple(branching.SCALES)
    shifts = tuple(range(1, 20))
    label = collision_label(scales, shifts)
    rows = []
    for branch in branches:
        form = branch["prime_form"]
        coefficient = int(form["coefficient"])
        constant = int(form["constant"])
        sources = [source_state(coefficient, constant, scale) for scale in scales]
        if branching.ray_hits(coefficient, constant):
            raise AssertionError("post-affine state unexpectedly has an H19 ray")
        rows.append(
            {
                "v_mod_29": branch["v_mod_29"],
                "prime_form": form,
                "h19_ray_certificate": False,
                "sources": sources,
            }
        )
    if len(rows) != 14:
        raise AssertionError("expected fourteen post-affine states")
    return {
        "arithmetic": (
            "exact stationary-source affine forms, complete source square-tail "
            "residue checks, and finite collision-prime extraction"
        ),
        "scope_note": (
            "A canonical finite state description for future multi-source "
            "bridge lemmas. Pairwise private coprimality after stripping this "
            "label does not itself select a certificate or descent."
        ),
        "state_schema": {
            "post_affine_residual_branch_count": len(rows),
            "stationary_scale_count": len(scales),
            "h19_shift_count": len(shifts),
        },
        "collision_label": label,
        "states": rows,
    }


def main() -> int:
    payload = run_audit()
    RESULTS.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
