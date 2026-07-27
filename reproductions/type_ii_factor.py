#!/usr/bin/env python3
"""Finite audit of the Type II affine-factor generator.

After removing four proved direct families, this searches the exact Type II
condition q=4*A*C*K-1 | K*p+A in successively larger parameter boxes.  It is
not a proof of a uniform bound: every fixed finite template box is avoided by
infinitely many core primes, as recorded in type-II-finite-template-obstruction.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-factor-results.json"
EXTERNAL_SOURCE = ROOT / "reproductions" / "external_source.py"


def load_external_source():
    spec = importlib.util.spec_from_file_location("external_source", EXTERNAL_SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load external_source.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


external_source = load_external_source()
short_certificate = external_source.short_certificate


def smallest_box_witness(
    prime: int, parameter_bound: int
) -> tuple[int, int, int, object] | None:
    """Find a witness at the least max(A,C,K), then lexicographically."""
    for radius in range(1, parameter_bound + 1):
        for a in range(1, radius + 1):
            for c in range(1, radius + 1):
                for k in range(1, radius + 1):
                    if max(a, c, k) != radius:
                        continue
                    certificate = short_certificate.type_ii_factor_certificate(prime, a, c, k)
                    if certificate is not None:
                        return a, c, k, certificate
    return None


def run_experiment(limit: int, parameter_bound: int) -> dict[str, object]:
    if limit < 73 or parameter_bound < 1:
        raise ValueError("limit must be at least 73 and parameter_bound must be positive")
    trial_primes = short_certificate.primes_up_to(math.isqrt(4 * limit + 1) + 1)
    core_primes = [prime for prime in short_certificate.primes_up_to(limit) if prime % 24 == 1]
    residual = [
        prime
        for prime in core_primes
        if not external_source.covered_by_direct_families(prime, trial_primes)
    ]

    witnesses: dict[int, tuple[int, int, int, object]] = {}
    missing: list[int] = []
    record_holders: list[dict[str, int]] = []
    largest_box = 0
    for prime in residual:
        witness = smallest_box_witness(prime, parameter_bound)
        if witness is None:
            missing.append(prime)
            continue
        a, c, k, certificate = witness
        box = max(a, c, k)
        if box > largest_box:
            largest_box = box
            record_holders.append(
                {
                    "prime": prime,
                    "box": box,
                    "a": a,
                    "c": c,
                    "k": k,
                    "gap": certificate.gap,
                    "divisor": certificate.divisor,
                }
            )
        witnesses[prime] = witness

    return {
        "arithmetic": "exact integer divisibility plus fractions.Fraction certificate verification",
        "scope_note": (
            "A finite parameter-box experiment. The finite-template obstruction proves that no "
            "fixed box can cover all core primes, so complete coverage in this range is not a "
            "uniform-bound proof."
        ),
        "prime_limit": limit,
        "parameter_box": {"a_max": parameter_bound, "c_max": parameter_bound, "k_max": parameter_bound},
        "factor_generator": "q=4*A*C*K-1 divides K*p+A",
        "direct_families": ["m=3", "(p+1)/2", "p+4", "4p+1"],
        "core_prime_count": len(core_primes),
        "residual_after_direct_families": len(residual),
        "factor_generator_certified_count": len(witnesses),
        "factor_generator_missing": missing,
        "largest_minimal_box_found": largest_box if witnesses else None,
        "box_record_holders": record_holders,
        "sample_witnesses": [
            {
                "prime": prime,
                "a": witness[0],
                "c": witness[1],
                "k": witness[2],
                "gap": witness[3].gap,
                "divisor": witness[3].divisor,
            }
            for prime, witness in list(witnesses.items())[:10]
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--parameter-bound", type=int, default=20)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_experiment(args.limit, args.parameter_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
