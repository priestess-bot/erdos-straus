#!/usr/bin/env python3
"""Audit scaled-first Type II tail deflation on an input residual set."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-deflation-3m-full-results.json"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-scaled-first-tail-deflation-3m-results.json"
)
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_scaled_first_tail_deflation_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def run_audit(
    input_path: Path = DEFAULT_INPUT,
    first_scale_cap: int = 2_000,
    gap_cap: int = 20_000,
) -> dict[str, object]:
    """Classify every supplied k=1 miss in the stated finite parameter box."""
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    residuals = payload["misses"]
    primes = [record["prime"] for record in residuals]
    if not primes:
        raise ValueError("input residual audit has no records")
    spf = short_certificate.smallest_prime_factors(max(primes))
    records = []
    for prime in primes:
        witness = short_certificate.type_ii_scaled_first_tail_deflation_scan(
            prime, first_scale_cap, gap_cap, spf
        )
        records.append(
            {
                "prime": prime,
                "witness": asdict(witness) if witness is not None else None,
            }
        )
    misses = [record["prime"] for record in records if record["witness"] is None]
    return {
        "arithmetic": (
            "exact divisibility km+1 | kp-1, Type II divisor certificates, "
            "and fractions.Fraction reconstruction in short_certificate.py"
        ),
        "scope_note": (
            "This only audits the supplied finite residual set and finite "
            "(first-scale, gap) box. It is not a uniform selector theorem."
        ),
        "input_artifact": input_path.name,
        "first_scale_cap": first_scale_cap,
        "gap_cap": gap_cap,
        "input_residual_count": len(primes),
        "scaled_first_hit_count": len(records) - len(misses),
        "scaled_first_miss_count": len(misses),
        "scaled_first_misses": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--first-scale-cap", type=int, default=2_000)
    parser.add_argument("--gap-cap", type=int, default=20_000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input, args.first_scale_cap, args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
