#!/usr/bin/env python3
"""Close the Type II tail/quadratic-external pressure set with radius-two AC rays."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-10m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-external-ac2-closure-10m-results.json"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location("tail_external_ac2_short_certificate", SHORT_CERTIFICATE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def direct_ac_witness(prime: int, ac_bound: int = 2) -> dict[str, int] | None:
    """Return the least-radius AC Type II certificate, with K unbounded."""
    for radius in range(1, ac_bound + 1):
        for a in range(1, radius + 1):
            for c in range(1, radius + 1):
                if max(a, c) != radius:
                    continue
                shifted = prime + 4 * a * a * c
                for h in sympy.divisors(shifted):
                    h = int(h)
                    modulus = 4 * a * c
                    if h <= 1 or (h + 1) % modulus:
                        continue
                    k = (h + 1) // modulus
                    certificate = short_certificate.type_ii_raw_ray_certificate(prime, a, c, k)
                    if certificate is None:
                        continue
                    if shifted != h * certificate.gap or not short_certificate.verify_certificate(certificate):
                        raise AssertionError("AC certificate did not reconstruct")
                    return {
                        "radius": radius,
                        "a": a,
                        "c": c,
                        "k": k,
                        "h": h,
                        "gap": certificate.gap,
                        "divisor": certificate.divisor,
                        "x": certificate.x,
                        "y": certificate.y,
                        "z": certificate.z,
                    }
    return None


def run_audit(payload: dict[str, object], ac_bound: int = 2) -> dict[str, object]:
    """Close every tail/quadratic-external miss by a direct AC ray."""
    shared_misses = [int(prime) for prime in payload["quadratic_factor_misses"]]
    records = []
    for prime in shared_misses:
        witness = direct_ac_witness(prime, ac_bound)
        records.append({"prime": prime, "direct_ac_witness": witness})
    captured = [record for record in records if record["direct_ac_witness"] is not None]
    tail_count = int(payload["core_prime_count"]) - int(payload["tail_deflation_miss_count"])
    mixed_count = int(payload["mixed_factor_descent_count"])
    return {
        "arithmetic": (
            "exact factorization of p+4*A^2*C in the stated AC box, with exact "
            "Type II certificate reconstruction after the independently checked tail/external audit"
        ),
        "scope_note": (
            f"A finite three-branch closure of all core primes up to {payload['prime_limit']}. "
            "It does not prove a universal fixed AC box or descent selector."
        ),
        "prime_limit": payload["prime_limit"],
        "core_prime_count": payload["core_prime_count"],
        "two_tail_descent_count": tail_count,
        "mixed_factor_descent_count_on_tail_misses": mixed_count,
        "quadratic_factor_descent_count_on_tail_misses": int(payload["quadratic_factor_descent_count"]),
        "tail_quadratic_miss_count": len(records),
        "ac_radius_bound": ac_bound,
        "direct_ac_captured_count": len(captured),
        "direct_ac_missing_primes": [record["prime"] for record in records if record["direct_ac_witness"] is None],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--ac-bound", type=int, default=2)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")), args.ac_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
