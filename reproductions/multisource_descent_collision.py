#!/usr/bin/env python3
"""Verify the finite-collision decomposition for external-source denominators.

For B=(p-1)/4 and k | B, define n_k=p-B/k.  For distinct divisors k,l of B,
writing g=gcd(k,l), the exact identity

  a(4*g*b-1) n_k - b(4*g*a-1) n_l = b-a,

where k=g*a and l=g*b, shows

  gcd(n_k,n_l) | |k-l|/gcd(k,l).

Thus a finite scale set has a finite, p-independent collision-prime set.
After stripping those primes from every n_k, all remaining source parts are
pairwise coprime.  This is the source-side analogue of the Type II
multi-shift collision decomposition.
"""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / "reproductions" / "type-ii-multisource-descent-state-h19-20m-results.json"
)
RESULTS = (
    ROOT / "reproductions" / "multisource-descent-collision-h19-20m-results.json"
)
SHORT_CERTIFICATE_SCRIPT = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "multisource_collision_short_certificate", SHORT_CERTIFICATE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def source_denominator(prime: int, scale: int) -> int:
    """Return n_k=p-(p-1)/(4k), requiring k | (p-1)/4."""
    base = (prime - 1) // 4
    if prime % 24 != 1 or scale < 1 or base % scale:
        raise ValueError("require a core prime and scale | (p-1)/4")
    return prime - base // scale


def pair_collision_bound(left: int, right: int) -> int:
    """Return the p-independent bound on gcd(n_left,n_right)."""
    if left < 1 or right < 1 or left == right:
        raise ValueError("scales must be distinct positive integers")
    return abs(left - right) // math.gcd(left, right)


def prime_factors(value: int) -> tuple[int, ...]:
    """Return the distinct prime factors of a positive integer."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append(value)
    return tuple(factors)


def collision_primes(scales: tuple[int, ...]) -> tuple[int, ...]:
    """Return all primes that can occur in cross-source gcds for these scales."""
    result: set[int] = set()
    for index, left in enumerate(scales):
        for right in scales[index + 1 :]:
            result.update(prime_factors(pair_collision_bound(left, right)))
    return tuple(sorted(result))


def strip_primes(value: int, primes: tuple[int, ...]) -> int:
    for prime in primes:
        while value % prime == 0:
            value //= prime
    return value


def source_ray_collision_bound(scale: int, shift: int) -> int:
    """Return the p-independent bound on gcd(n_k,p+4s)."""
    if scale < 1 or shift < 1:
        raise ValueError("scale and shift must be positive")
    return abs(4 * shift * (4 * scale - 1) - 1)


def profile(prime: int, scales: tuple[int, ...]) -> dict[str, object]:
    """Verify the exact collision decomposition for one source-scale path."""
    if tuple(sorted(set(scales))) != scales:
        raise ValueError("scales must be increasing and distinct")
    sources = {scale: source_denominator(prime, scale) for scale in scales}
    bounds: list[dict[str, int]] = []
    actual_collisions: list[dict[str, int]] = []
    for index, left in enumerate(scales):
        for right in scales[index + 1 :]:
            bound = pair_collision_bound(left, right)
            gcd = math.gcd(sources[left], sources[right])
            if bound % gcd:
                raise AssertionError("source gcd violates the scale-difference bound")
            bounds.append({"left_k": left, "right_k": right, "bound": bound})
            if gcd > 1:
                actual_collisions.append(
                    {"left_k": left, "right_k": right, "gcd": gcd}
                )
    primes = collision_primes(scales)
    private = {scale: strip_primes(value, primes) for scale, value in sources.items()}
    for index, left in enumerate(scales):
        for right in scales[index + 1 :]:
            if math.gcd(private[left], private[right]) != 1:
                raise AssertionError("stripped source parts must be pairwise coprime")
    return {
        "prime": prime,
        "scales": list(scales),
        "collision_primes": list(primes),
        "source_denominators": {str(scale): value for scale, value in sources.items()},
        "private_source_parts": {str(scale): value for scale, value in private.items()},
        "pair_bounds": bounds,
        "actual_collisions": actual_collisions,
    }


def joint_profile(
    prime: int, scales: tuple[int, ...], shifts: tuple[int, ...]
) -> dict[str, object]:
    """Strip every fixed source/source, ray/ray, and source/ray collision."""
    source_values = {f"source:{scale}": source_denominator(prime, scale) for scale in scales}
    ray_values = {f"ray:{shift}": prime + 4 * shift for shift in shifts}
    values = {**source_values, **ray_values}
    collision: set[int] = set(collision_primes(scales))
    for index, left in enumerate(shifts):
        for right in shifts[index + 1 :]:
            collision.update(prime_factors(abs(left - right)))
    for scale in scales:
        for shift in shifts:
            bound = source_ray_collision_bound(scale, shift)
            collision.update(prime_factors(bound))
            if bound % math.gcd(source_values[f"source:{scale}"], ray_values[f"ray:{shift}"]):
                raise AssertionError("source/ray gcd violates its fixed bound")
    primes = tuple(sorted(collision))
    private = {label: strip_primes(value, primes) for label, value in values.items()}
    ordered = tuple(private)
    for index, left in enumerate(ordered):
        for right in ordered[index + 1 :]:
            if math.gcd(private[left], private[right]) != 1:
                raise AssertionError("joint private parts must be pairwise coprime")
    return {
        "prime": prime,
        "scales": list(scales),
        "shifts": list(shifts),
        "joint_collision_primes": list(primes),
        "joint_private_parts_pairwise_coprime": True,
    }


def run_audit(input_path: Path = DEFAULT_INPUT, shift_bound: int = 19) -> dict[str, object]:
    """Verify the collision decomposition for every saved H19 state path."""
    source = json.loads(input_path.read_text(encoding="utf-8"))
    if shift_bound < 1:
        raise ValueError("shift_bound must be positive")
    shifts = tuple(range(1, shift_bound + 1))
    profiles = []
    joint_profiles = []
    collision_histogram: Counter[tuple[int, ...]] = Counter()
    with_actual_collision = 0
    for state_path in source["profiles"]:
        scales = tuple(
            int(state["k"]) for state in state_path["states_through_first_success"]
        )
        row = profile(int(state_path["prime"]), scales)
        profiles.append(row)
        joint_profiles.append(joint_profile(int(state_path["prime"]), scales, shifts))
        collision_histogram[tuple(row["collision_primes"])] += 1
        if row["actual_collisions"]:
            with_actual_collision += 1
    return {
        "arithmetic": (
            "exact source-denominator identities, integer gcd checks, and "
            "finite collision-prime stripping"
        ),
        "scope_note": (
            "A finite verification of a general gcd lemma on the H19 state "
            "paths. Pairwise private coprimality alone does not select a "
            "descent factor or prove the conjecture."
        ),
        "input_artifact": input_path.name,
        "residual_count": len(profiles),
        "joint_shift_bound": shift_bound,
        "all_private_source_parts_pairwise_coprime": True,
        "all_joint_private_parts_pairwise_coprime": True,
        "profiles_with_actual_source_collision": with_actual_collision,
        "collision_prime_set_histogram": {
            ",".join(str(prime) for prime in primes) or "empty": count
            for primes, count in sorted(collision_histogram.items())
        },
        "profiles": profiles,
        "joint_profiles": joint_profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--shift-bound", type=int, default=19)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.input, args.shift_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
