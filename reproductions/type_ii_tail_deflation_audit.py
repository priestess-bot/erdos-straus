#!/usr/bin/env python3
"""Audit Type II two-tail deflation on prior adaptive-descent escapes."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "adaptive-external-escape-3m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-deflation-3m-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_tail_deflation_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def run_audit(input_path: Path = DEFAULT_INPUT) -> dict[str, object]:
    """Classify every recorded prior escape by the exact divisor-indexed kernel."""
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    records = payload["escape_records"]
    primes = [record["prime"] for record in records]
    if not primes:
        raise ValueError("input escape audit has no records")
    spf = short_certificate.smallest_prime_factors(max(primes))
    audited = []
    for record in records:
        prime = record["prime"]
        witnesses = short_certificate.type_ii_tail_deflation_scan(prime, spf)
        audited.append(
            {
                "prime": prime,
                "witnesses": [asdict(witness) for witness in witnesses],
            }
        )
    misses = [record["prime"] for record in audited if not record["witnesses"]]
    return {
        "arithmetic": (
            "exact SPF factorization, Bradford Type II divisor certificates, "
            "and fractions.Fraction verification in short_certificate.py"
        ),
        "scope_note": (
            "This is a finite audit of the escape records supplied by the input "
            "artifact. Full coverage here does not prove a uniform divisor "
            "selector for all core primes."
        ),
        "input_artifact": input_path.name,
        "input_escape_count": len(records),
        "tail_deflation_hit_count": len(records) - len(misses),
        "tail_deflation_miss_count": len(misses),
        "tail_deflation_misses": misses,
        "records": audited,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
