#!/usr/bin/env python3
"""Audit the unbounded-first-scale shared-divisor selector on residuals."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-deflation-10m-full-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-shared-divisor-tail-10m-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_shared_divisor_tail_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def run_audit(
    input_path: Path = DEFAULT_INPUT, gap_cap: int = 20_000
) -> dict[str, object]:
    """Test all first scales induced by p+m divisors for each bounded gap."""
    if gap_cap < 3:
        raise ValueError("gap_cap must be at least 3")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    residuals = payload["misses"]
    primes = [record["prime"] for record in residuals]
    if not primes:
        raise ValueError("input residual audit has no records")
    spf = short_certificate.smallest_prime_factors(max(primes) + gap_cap)
    records = []
    for prime in primes:
        witness = short_certificate.type_ii_shared_divisor_tail_deflation_scan(
            prime, gap_cap, spf
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
            "complete divisor enumeration of p+m for every m in the stated "
            "range, exact Type II certification, and fractions.Fraction checks"
        ),
        "scope_note": (
            "There is no first-scale cutoff: every positive k induced by a "
            "shared divisor of p+m is tested. The gap bound and input residual "
            "set remain finite."
        ),
        "input_artifact": input_path.name,
        "gap_cap": gap_cap,
        "input_residual_count": len(primes),
        "shared_divisor_hit_count": len(records) - len(misses),
        "shared_divisor_miss_count": len(misses),
        "shared_divisor_misses": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--gap-cap", type=int, default=20_000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input, args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
