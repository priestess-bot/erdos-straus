#!/usr/bin/env python3
"""Measure the first successful squarefree-canonical Type II shift.

For every core prime p in a finite range, scan s=1,2,... in order.  The
canonical factorization s=a^2*c with squarefree c gives the sole ray retained
for that shift.  This is a finite spectrum measurement, not evidence for a
fixed global shift bound.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-minimal-canonical-shift-10m-results.json"
CANONICAL_SCRIPT = ROOT / "reproductions" / "type_ii_canonical_ray.py"


def load_canonical_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_canonical_ray", CANONICAL_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_canonical_ray.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


canonical = load_canonical_script()


def run_experiment(limit: int, shift_cap: int) -> dict[str, object]:
    if limit < 73 or shift_cap < 1:
        raise ValueError("limit >= 73 and shift_cap >= 1 are required")
    smallest_factors = canonical.ray.short_certificate.smallest_prime_factors(
        limit + 4 * shift_cap
    )
    core_primes = [
        prime
        for prime in canonical.ray.short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    pairs = {
        shift: canonical.canonical_pair(shift) for shift in range(1, shift_cap + 1)
    }
    missing: list[int] = []
    record_holders: list[dict[str, int]] = []
    largest_first_shift = 0
    first_shift_histogram: dict[int, int] = {}
    for prime in core_primes:
        first_shift = None
        for shift in range(1, min(shift_cap, prime // 4) + 1):
            witness = canonical.witness_for_pair(
                prime, pairs[shift], smallest_factors
            )
            if witness is None:
                continue
            first_shift = shift
            first_shift_histogram[shift] = first_shift_histogram.get(shift, 0) + 1
            if shift > largest_first_shift:
                largest_first_shift = shift
                record_holders.append(
                    {
                        "prime": prime,
                        "shift": shift,
                        "a": pairs[shift][0],
                        "c": pairs[shift][1],
                        "h": witness["h"],
                        "k": witness["k"],
                        "gap": witness["gap"],
                    }
                )
            break
        if first_shift is None:
            missing.append(prime)
    return {
        "arithmetic": (
            "exact SPF factorization, divisor residues, and reconstructed Type II "
            "certificate verification for every first-shift witness"
        ),
        "scope_note": (
            "A finite minimal-shift spectrum. A completed cap in this range does "
            "not prove any fixed cap covers all core primes."
        ),
        "prime_limit": limit,
        "shift_cap": shift_cap,
        "core_prime_count": len(core_primes),
        "captured_count": len(core_primes) - len(missing),
        "missing": missing,
        "largest_first_shift": largest_first_shift if record_holders else None,
        "record_holders": record_holders,
        "first_shift_histogram": dict(sorted(first_shift_histogram.items())),
    }


def canonical_fan_modulus(pairs: dict[int, tuple[int, int]], shift_bound: int) -> int:
    """Return the joint canonical ray modulus through the stated shift."""
    modulus = 24
    for shift in range(1, shift_bound + 1):
        a, c = pairs[shift]
        modulus = math.lcm(modulus, 4 * a * c)
    return modulus


def transition_profile(
    limit: int, base_shift_bound: int, shift_cap: int
) -> dict[str, object]:
    """Profile actual base-fan misses and their first later canonical ray.

    The unfixed_omega measure counts prime factors outside the joint base
    modulus. It is a finite diagnostic for candidate closure potentials, not
    a certificate criterion.
    """
    if limit < 73 or base_shift_bound < 1 or shift_cap <= base_shift_bound:
        raise ValueError("limit >= 73 and 1 <= base_shift_bound < shift_cap are required")
    smallest_factors = canonical.ray.short_certificate.smallest_prime_factors(
        limit + 4 * shift_cap
    )
    core_primes = [
        prime
        for prime in canonical.ray.short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    pairs = {
        shift: canonical.canonical_pair(shift) for shift in range(1, shift_cap + 1)
    }
    joint_modulus = canonical_fan_modulus(pairs, base_shift_bound)
    forced_primes = frozenset(
        canonical.residue_structure.distinct_prime_factors(joint_modulus)
    )
    residual_primes: list[int] = []
    transition_witnesses: list[dict[str, int]] = []
    missing_through_cap: list[int] = []
    later_shift_histogram: dict[int, int] = {}
    min_unfixed_omega_histogram: dict[int, int] = {}
    total_unfixed_omega_histogram: dict[int, int] = {}
    zero_unfixed_examples: list[dict[str, object]] = []
    failure_class_histogram: dict[str, int] = {}
    inside_ray_count_histogram: dict[int, int] = {}
    first_support_inside_shift_histogram: dict[int, int] = {}
    minimum_support_defect_histogram: dict[int, int] = {}
    minimum_support_defect_witnesses: list[dict[str, int]] = []

    for prime in core_primes:
        if any(
            canonical.witness_for_pair(prime, pairs[shift], smallest_factors)
            is not None
            for shift in range(1, base_shift_bound + 1)
        ):
            continue
        residual_primes.append(prime)

        first_later_witness = None
        for shift in range(base_shift_bound + 1, shift_cap + 1):
            witness = canonical.witness_for_pair(
                prime, pairs[shift], smallest_factors
            )
            if witness is not None:
                first_later_witness = witness
                later_shift_histogram[shift] = (
                    later_shift_histogram.get(shift, 0) + 1
                )
                transition_witnesses.append(
                    {
                        "prime": prime,
                        "shift": shift,
                        "a": witness["a"],
                        "c": witness["c"],
                        "h": witness["h"],
                        "k": witness["k"],
                        "gap": witness["gap"],
                        "divisor": witness["divisor"],
                    }
                )
                break
        if first_later_witness is None:
            missing_through_cap.append(prime)

        unfixed_omegas: list[int] = []
        zero_rows: list[dict[str, object]] = []
        inside_ray_count = 0
        support_inside_options: list[tuple[int, int]] = []
        for shift in range(1, base_shift_bound + 1):
            a, c = pairs[shift]
            analysis = canonical.residue_structure.support_critical_ray_analysis(
                prime, a, c, smallest_factors
            )
            if not analysis["failed"]:
                raise AssertionError("base residual unexpectedly has a ray witness")
            if analysis["target_in_support"]:
                failure_class = f"inside:{len(analysis['defect'])}"
                inside_ray_count += 1
                support_inside_options.append((len(analysis["defect"]), shift))
            else:
                failure_class = (
                    f"outside:{analysis['target_outside_two_power_depth']}"
                )
            failure_class_histogram[failure_class] = (
                failure_class_histogram.get(failure_class, 0) + 1
            )

            shifted = prime + 4 * shift
            factorization = canonical.residue_structure.factorization_from_spf(
                shifted, smallest_factors
            )
            unfixed_omega = sum(
                exponent
                for factor, exponent in factorization
                if factor not in forced_primes
            )
            unfixed_omegas.append(unfixed_omega)
            if unfixed_omega == 0:
                zero_rows.append(
                    {
                        "shift": shift,
                        "pair": {"a": pairs[shift][0], "c": pairs[shift][1]},
                        "shifted": shifted,
                        "factorization": [
                            {"prime": factor, "exponent": exponent}
                            for factor, exponent in factorization
                        ],
                    }
                )
        minimum = min(unfixed_omegas)
        total = sum(unfixed_omegas)
        min_unfixed_omega_histogram[minimum] = (
            min_unfixed_omega_histogram.get(minimum, 0) + 1
        )
        total_unfixed_omega_histogram[total] = (
            total_unfixed_omega_histogram.get(total, 0) + 1
        )
        if zero_rows:
            zero_unfixed_examples.append({"prime": prime, "rows": zero_rows})
        inside_ray_count_histogram[inside_ray_count] = (
            inside_ray_count_histogram.get(inside_ray_count, 0) + 1
        )
        if support_inside_options:
            first_support_shift = support_inside_options[0][1]
            minimum_defect, minimum_defect_shift = min(support_inside_options)
            first_support_inside_shift_histogram[first_support_shift] = (
                first_support_inside_shift_histogram.get(first_support_shift, 0) + 1
            )
            minimum_support_defect_histogram[minimum_defect] = (
                minimum_support_defect_histogram.get(minimum_defect, 0) + 1
            )
            minimum_support_defect_witnesses.append(
                {
                    "prime": prime,
                    "defect": minimum_defect,
                    "shift": minimum_defect_shift,
                }
            )

    return {
        "arithmetic": (
            "exact SPF factorization, canonical Type II certificate reconstruction, "
            "and factor counts outside the joint base modulus"
        ),
        "scope_note": (
            "This finite transition profile does not establish a global shift "
            "selector or a global factor-complexity bound."
        ),
        "prime_limit": limit,
        "base_shift_bound": base_shift_bound,
        "shift_cap": shift_cap,
        "core_prime_count": len(core_primes),
        "joint_base_modulus": joint_modulus,
        "joint_base_prime_divisors": sorted(forced_primes),
        "base_residual_count": len(residual_primes),
        "base_residual_primes": residual_primes,
        "later_first_shift_histogram": dict(sorted(later_shift_histogram.items())),
        "transition_witnesses": transition_witnesses,
        "missing_through_cap": missing_through_cap,
        "min_unfixed_omega_histogram": dict(sorted(min_unfixed_omega_histogram.items())),
        "total_unfixed_omega_histogram": dict(
            sorted(total_unfixed_omega_histogram.items())
        ),
        "zero_unfixed_examples": zero_unfixed_examples,
        "failure_class_histogram": dict(sorted(failure_class_histogram.items())),
        "inside_ray_count_histogram": dict(
            sorted(inside_ray_count_histogram.items())
        ),
        "first_support_inside_shift_histogram": dict(
            sorted(first_support_inside_shift_histogram.items())
        ),
        "minimum_support_defect_histogram": dict(
            sorted(minimum_support_defect_histogram.items())
        ),
        "minimum_support_defect_witnesses": minimum_support_defect_witnesses,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--shift-cap", type=int, default=50)
    parser.add_argument(
        "--base-shift-bound",
        type=int,
        help="profile actual misses of this base fan through --shift-cap",
    )
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = (
        transition_profile(args.limit, args.base_shift_bound, args.shift_cap)
        if args.base_shift_bound is not None
        else run_experiment(args.limit, args.shift_cap)
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
