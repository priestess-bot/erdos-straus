#!/usr/bin/env python3
"""Separate source-ray compatibility from square-tail residue hits at the 1b outlier."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADAPTIVE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_adaptive_even_source_descent.py"
PRIME = 640_775_689
DISTANCE_CAP = 34_091
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-tail-profile-640775689-results.json"
)


def load_adaptive_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_h19_fourth_even_source_tail_adaptive", ADAPTIVE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_h19_adaptive_even_source_descent.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


adaptive = load_adaptive_script()


def run_profile(distance_cap: int = DISTANCE_CAP) -> dict[str, object]:
    """Compile every compatible source ray and its exact square-tail residue test."""
    if distance_cap < 1 or distance_cap % 2 == 0:
        raise ValueError("distance cap must be a positive odd integer")
    short_certificate = adaptive.short_certificate
    spf = adaptive.targeted.TrialSmallestFactors(PRIME)
    rays: list[dict[str, object]] = []
    for distance in range(1, distance_cap + 1, 2):
        source = PRIME - distance
        for divisor in short_certificate.positive_divisors_from_spf(source, spf):
            quotient = source // divisor
            if quotient <= 1 or (quotient - 1) % distance:
                continue
            r = (quotient - 1) // distance
            if (divisor * r + 1) % 4:
                continue
            k = (divisor * r + 1) // 4
            m1 = k * quotient
            if 4 * m1 != r * PRIME + 1:
                raise AssertionError("source-ray identity failed")
            factors = short_certificate.positive_divisors_square_product_from_spf(
                k, quotient, spf
            )
            admissible = [
                factor
                for factor in factors
                if factor <= m1 and (m1 + factor) % r == 0
            ]
            rays.append(
                {
                    "distance": distance,
                    "source_denominator": source,
                    "d": divisor,
                    "r": r,
                    "s": quotient,
                    "k": k,
                    "m1": m1,
                    "square_tail_divisor_count": sum(
                        factor <= m1 for factor in factors
                    ),
                    "target_residue_factor_count": len(admissible),
                    "least_target_residue_factor": min(admissible, default=None),
                }
            )
    distances_with_rays = sorted({row["distance"] for row in rays})
    successful = [
        row for row in rays if row["target_residue_factor_count"] > 0
    ]
    return {
        "arithmetic": (
            "exact factorization of every even source, exhaustive compatible "
            "source-ray enumeration, and exhaustive divisors of each M1 squared"
        ),
        "scope_note": (
            "A one-prime finite state profile. It isolates the two conditions "
            "of the even-source theorem but does not establish a general selector."
        ),
        "prime": PRIME,
        "scanned_odd_distances_through": distance_cap,
        "compatible_source_ray_count": len(rays),
        "distances_with_compatible_source_rays": distances_with_rays,
        "compatible_distance_count": len(distances_with_rays),
        "tail_residue_success_count": len(successful),
        "first_tail_residue_success": min(
            successful, key=lambda row: (row["distance"], row["d"], row["r"])
        )
        if successful
        else None,
        "r_histogram": {str(r): count for r, count in sorted(Counter(row["r"] for row in rays).items())},
        "rays": rays,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--distance-cap", type=int, default=DISTANCE_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(args.distance_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
