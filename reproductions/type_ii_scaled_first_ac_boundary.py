#!/usr/bin/env python3
"""Audit bounded AC Type II rays under the scaled-first descent condition."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-deflation-3m-full-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-scaled-first-ac14-3m-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
AC_RAY = ROOT / "reproductions" / "type_ii_ac_ray.py"


def load_module(name: str, filename: Path):
    spec = importlib.util.spec_from_file_location(name, filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module(
    "type_ii_scaled_first_ac_short_certificate", SHORT_CERTIFICATE
)
ac_ray = load_module("type_ii_scaled_first_ac_ray", AC_RAY)


def bounded_ac_witness(
    prime: int, ac_bound: int, spf: list[int]
) -> dict[str, object] | None:
    """Return the least-radius raw Type II ray admitting a shared D factor."""
    for radius in range(1, ac_bound + 1):
        for a in range(1, radius + 1):
            for c in range(1, radius + 1):
                if max(a, c) != radius:
                    continue
                for h in ac_ray.divisors(prime + 4 * a * a * c, spf):
                    modulus = 4 * a * c
                    if h <= 1 or (h + 1) % modulus:
                        continue
                    ray_k = (h + 1) // modulus
                    certificate = short_certificate.type_ii_raw_ray_certificate(
                        prime, a, c, ray_k
                    )
                    if certificate is None:
                        continue
                    for divisor in short_certificate.positive_divisors_from_spf(
                        prime + certificate.gap, spf
                    ):
                        if divisor == 1 or (divisor - 1) % certificate.gap:
                            continue
                        first_scale = (divisor - 1) // certificate.gap
                        witness = (
                            short_certificate.type_ii_scaled_first_tail_deflation_witness(
                                prime, certificate.gap, first_scale, spf
                            )
                        )
                        if witness is not None:
                            return {
                                "radius": radius,
                                "a": a,
                                "c": c,
                                "ray_k": ray_k,
                                "h": h,
                                "shared_divisor": divisor,
                                "witness": asdict(witness),
                            }
    return None


def run_audit(
    input_path: Path = DEFAULT_INPUT, ac_bound: int = 14
) -> dict[str, object]:
    """Classify supplied residuals through every raw ray in a bounded AC box."""
    if ac_bound < 1:
        raise ValueError("ac_bound must be positive")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    residuals = payload["misses"]
    primes = [record["prime"] for record in residuals]
    if not primes:
        raise ValueError("input residual audit has no records")
    spf = short_certificate.smallest_prime_factors(2 * max(primes))
    records = [
        {
            "prime": prime,
            "witness": bounded_ac_witness(prime, ac_bound, spf),
        }
        for prime in primes
    ]
    misses = [record["prime"] for record in records if record["witness"] is None]
    return {
        "arithmetic": (
            "complete bounded-AC raw-ray enumeration, exact factorization of "
            "p+m, and fractions.Fraction reconstruction of every returned lift"
        ),
        "scope_note": (
            "An empty result excludes only scaled-first lifts based on raw Type II "
            "rays with A,C in the stated finite box; it does not exclude other "
            "Type II certificates or unbounded AC parameters."
        ),
        "input_artifact": input_path.name,
        "ac_bound": ac_bound,
        "input_residual_count": len(primes),
        "bounded_ac_hit_count": len(records) - len(misses),
        "bounded_ac_miss_count": len(misses),
        "bounded_ac_misses": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--ac-bound", type=int, default=14)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input, args.ac_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
