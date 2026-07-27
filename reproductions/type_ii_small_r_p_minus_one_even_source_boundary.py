#!/usr/bin/env python3
"""Exhaust the odd-distance even-source family on the joint small-r boundary."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE_BOUNDARY_INPUT = ROOT / "reproductions" / "type-ii-small-r-p-minus-one-core-boundary-100k-results.json"
P_MINUS_ONE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_p_minus_one_scaled_source_descent.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-small-r-p-minus-one-even-source-boundary-100k-results.json"


def load_script():
    spec = importlib.util.spec_from_file_location(
        "small_r_p_minus_one_even_source_boundary", P_MINUS_ONE_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {P_MINUS_ONE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


p_minus_one = load_script()


def serialize_witness(witness) -> dict[str, int]:
    return {
        "source_denominator": witness.source_denominator,
        "k": witness.k,
        "q": witness.q,
        "factor": witness.factor,
        "gap": witness.certificate.gap,
        "x": witness.certificate.x,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Search every odd source distance for the seven joint residuals."""
    primes = [int(prime) for prime in payload["joint_unclosed_primes"]]
    spf = p_minus_one.descent.short_certificate.smallest_prime_factors(max(primes))
    records = []
    distance_test_count = 0
    for prime in primes:
        witness = None
        checked = 0
        for distance in range(1, prime, 2):
            checked += 1
            candidate = p_minus_one.descent.short_certificate.even_source_distance_descent_witness(
                prime, distance, spf
            )
            if candidate is not None:
                witness = candidate
                break
        distance_test_count += checked
        records.append(
            {
                "prime": prime,
                "odd_distance_test_count_through_first_hit_or_exhaustion": checked,
                "first_even_source_witness": (
                    None if witness is None else serialize_witness(witness)
                ),
            }
        )
    unclosed = [
        int(record["prime"])
        for record in records
        if record["first_even_source_witness"] is None
    ]
    return {
        "arithmetic": (
            "complete scan of every odd 0<c<p in the exact "
            "even_source_distance_descent_witness constructor, including "
            "source/target rational identities and Type I certificates"
        ),
        "scope_note": (
            "A finite boundary for this standard even-source family. It does "
            "not exclude other sources or Erdős-Straus solutions."
        ),
        "prime_limit": payload["prime_limit"],
        "joint_small_r_p_minus_one_residual_count": len(primes),
        "odd_distance_test_count": distance_test_count,
        "even_source_strict_lift_count": len(primes) - len(unclosed),
        "fully_even_source_unclosed_primes": unclosed,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=CORE_BOUNDARY_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
