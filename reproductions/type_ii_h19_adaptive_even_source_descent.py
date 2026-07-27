#!/usr/bin/env python3
"""Close quadratic H19 descent misses with a bounded odd-distance even-source fan."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGETED_SCRIPT = ROOT / "reproductions" / "type_ii_h19_targeted_quadratic_descent.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-300m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-adaptive-even-source-descent-300m-results.json"


def load_targeted_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_h19_adaptive_even_source_targeted", TARGETED_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_h19_targeted_quadratic_descent.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


targeted = load_targeted_script()
short_certificate = targeted.short_certificate


def verify_witness(prime: int, distance: int, witness) -> None:
    if witness.source_denominator != prime - distance:
        raise AssertionError("even-source denominator does not match its distance")
    if not 2 <= witness.source_denominator < prime:
        raise AssertionError("even-source lift is not strict")
    if Fraction(4, witness.source_denominator) != sum(
        (Fraction(1, value) for value in witness.source_solution), Fraction()
    ):
        raise AssertionError("even-source source identity failed")
    if Fraction(4, prime) != sum(
        (Fraction(1, value) for value in witness.target_solution), Fraction()
    ):
        raise AssertionError("even-source target identity failed")


def serialize_witness(witness) -> dict[str, object]:
    return {
        "source_denominator": witness.source_denominator,
        "k": witness.k,
        "q": witness.q,
        "factor": witness.factor,
        "source_solution": list(witness.source_solution),
        "target_solution": list(witness.target_solution),
        "certificate": {
            "type": witness.certificate.certificate_type,
            "gap": witness.certificate.gap,
            "x": witness.certificate.x,
            "divisor": witness.certificate.divisor,
            "y": witness.certificate.y,
            "z": witness.certificate.z,
        },
    }


def run_audit(payload: dict[str, object], distance_cap: int) -> dict[str, object]:
    """Try each odd distance through the cap only after quadratic descent fails."""
    if distance_cap < 1 or distance_cap % 2 == 0:
        raise ValueError("distance cap must be a positive odd integer")
    residuals = payload["records"]
    primes = [int(row["prime"]) for row in residuals]
    spf = targeted.TrialSmallestFactors(max(primes))
    fallbacks: list[dict[str, object]] = []
    missing: list[int] = []
    quadratic_count = 0
    for record in residuals:
        prime = int(record["prime"])
        if record["quadratic_factor_external_source_descent"] is not None:
            quadratic_count += 1
            continue
        selected = None
        for distance in range(1, distance_cap + 1, 2):
            witness = short_certificate.even_source_distance_descent_witness(
                prime, distance, spf
            )
            if witness is None:
                continue
            verify_witness(prime, distance, witness)
            selected = {
                "prime": prime,
                "distance": distance,
                "witness": serialize_witness(witness),
            }
            fallbacks.append(selected)
            break
        if selected is None:
            missing.append(prime)
    return {
        "arithmetic": (
            "exact trial-prime factorization in each complete odd-distance "
            "even-source fan, with exact rational source/target lift checks"
        ),
        "scope_note": (
            "A finite two-layer descent audit. Neither the quadratic family "
            "nor the odd-distance cap is asserted to be universal."
        ),
        "prime_limit": payload["prime_limit"],
        "base_shift_bound": payload["base_shift_bound"],
        "h19_residual_count": len(residuals),
        "quadratic_factor_descent_count": quadratic_count,
        "odd_distance_cap": distance_cap,
        "odd_distance_fallback_count": len(fallbacks),
        "missing_through_cap": missing,
        "fallbacks": fallbacks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--distance-cap", type=int, default=7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload, args.distance_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
