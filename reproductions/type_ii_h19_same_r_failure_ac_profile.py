#!/usr/bin/env python3
"""Find direct bounded-AC Type II certificates for same-r external-source misses."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-overflow-tail-deflation-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-same-r-failure-ac-profile-1b-results.json"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "h19_same_r_failure_ac_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def direct_ac_witness(prime: int, ac_bound: int) -> dict[str, int] | None:
    """Return the least-radius exact AC Type II certificate, with K unbounded."""
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
                    if shifted != h * certificate.gap:
                        raise AssertionError("AC ray factor pair did not reconstruct its shift")
                    if not short_certificate.verify_certificate(certificate):
                        raise AssertionError("AC ray certificate did not verify")
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


def run_audit(payload: dict[str, object], ac_bound: int = 6) -> dict[str, object]:
    """Close each same-r external-source miss by a direct AC ray, if present."""
    if ac_bound < 1:
        raise ValueError("ac_bound must be positive")
    misses = [
        record
        for record in payload["records"]
        if not record["same_tail_deflation_witnesses"]
    ]
    records = []
    for record in misses:
        prime = int(record["prime"])
        witness = direct_ac_witness(prime, ac_bound)
        records.append(
            {
                "prime": prime,
                "r": int(record["r"]),
                "minimum_overflow": int(record["minimum_overflow"]),
                "alternative_external_q": int(record["quadratic_external_source"]["q"]),
                "direct_ac_witness": witness,
            }
        )
    captured = [record for record in records if record["direct_ac_witness"] is not None]
    radius_histogram = Counter(int(record["direct_ac_witness"]["radius"]) for record in captured)
    return {
        "arithmetic": (
            "exact factorization of p+4*A^2*C in the stated AC box, followed by "
            "exact Type II certificate reconstruction and factor-pair verification"
        ),
        "scope_note": (
            "A finite direct-certificate profile of the stored same-r external-source "
            "misses. It does not prove a global AC-radius bound."
        ),
        "prime_limit": payload["prime_limit"],
        "same_r_external_source_miss_count": len(records),
        "ac_bound": ac_bound,
        "direct_ac_captured_count": len(captured),
        "direct_ac_missing_primes": [record["prime"] for record in records if record["direct_ac_witness"] is None],
        "minimal_ac_radius_histogram": {str(key): value for key, value in sorted(radius_histogram.items())},
        "maximum_minimal_ac_radius": max(radius_histogram, default=None),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--ac-bound", type=int, default=6)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")), args.ac_bound)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
