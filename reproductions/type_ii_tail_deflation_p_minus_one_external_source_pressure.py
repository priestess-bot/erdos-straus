#!/usr/bin/env python3
"""Test complete external-source strict descents on a low-shift boundary."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT
    / "reproductions"
    / "type-ii-tail-deflation-p-minus-one-canonical-50m-s2-boundary.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-ii-tail-deflation-p-minus-one-external-source-50m-pressure.json"
)
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "tail_deflation_p_minus_one_external_source_pressure", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SHORT_CERTIFICATE.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def serialize_witness(witness) -> dict[str, object] | None:
    return asdict(witness) if witness is not None else None


def run_audit(input_path: Path = DEFAULT_INPUT) -> dict[str, object]:
    """Run all nested external-source strict-descent constructors on misses."""
    input_payload = json.loads(input_path.read_text(encoding="utf-8"))
    primes = [int(prime) for prime in input_payload["unclosed_primes"]]
    if not primes:
        raise ValueError("input boundary has no residual primes")
    spf = short_certificate.smallest_prime_factors(max(primes))
    records = []
    for prime in primes:
        ordinary = short_certificate.external_source_descent_witness(prime, spf)
        mixed = short_certificate.mixed_factor_external_source_descent_witness(
            prime, spf
        )
        quadratic = short_certificate.quadratic_factor_external_source_descent_witness(
            prime, spf
        )
        records.append(
            {
                "prime": prime,
                "ordinary_external_source_descent": serialize_witness(ordinary),
                "mixed_factor_external_source_descent": serialize_witness(mixed),
                "quadratic_factor_external_source_descent": serialize_witness(
                    quadratic
                ),
            }
        )
    ordinary_misses = [
        record["prime"]
        for record in records
        if record["ordinary_external_source_descent"] is None
    ]
    mixed_misses = [
        record["prime"]
        for record in records
        if record["mixed_factor_external_source_descent"] is None
    ]
    quadratic_misses = [
        record["prime"]
        for record in records
        if record["quadratic_factor_external_source_descent"] is None
    ]
    return {
        "arithmetic": (
            "complete divisor enumeration for the ordinary, mixed-factor, and "
            "quadratic-factor external-source strict-descent constructors, "
            "with exact source and target identity verification"
        ),
        "scope_note": (
            "A finite shared-pressure audit. These misses do not rule out "
            "other strict descents or direct Type I/II certificates."
        ),
        "input_artifact": input_path.name,
        "prime_limit": input_payload["prime_limit"],
        "input_residual_count": len(primes),
        "ordinary_external_source_hit_count": len(records) - len(ordinary_misses),
        "mixed_factor_external_source_hit_count": len(records) - len(mixed_misses),
        "quadratic_factor_external_source_hit_count": len(records)
        - len(quadratic_misses),
        "ordinary_external_source_misses": ordinary_misses,
        "mixed_factor_external_source_misses": mixed_misses,
        "quadratic_factor_external_source_misses": quadratic_misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
