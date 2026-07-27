#!/usr/bin/env python3
"""Audit external-source descents on stored Type II tail-deflation misses."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
TARGETED_DESCENT = ROOT / "reproductions" / "type_ii_h19_targeted_quadratic_descent.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-deflation-10m-full-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-10m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("tail_external_boundary_short_certificate", SHORT_CERTIFICATE)
targeted_descent = load_module("tail_external_boundary_targeted_descent", TARGETED_DESCENT)


def serialize_witness(witness) -> dict[str, int] | None:
    if witness is None:
        return None
    if not 2 <= witness.source_denominator < witness.prime:
        raise AssertionError("external source is not strict")
    if Fraction(4, witness.source_denominator) != sum(
        (Fraction(1, value) for value in witness.source_solution), Fraction()
    ):
        raise AssertionError("external source solution did not verify")
    if Fraction(4, witness.prime) != sum(
        (Fraction(1, value) for value in witness.target_solution), Fraction()
    ):
        raise AssertionError("external target lift did not verify")
    return {
        "source_denominator": witness.source_denominator,
        "k": witness.k,
        "q": witness.q,
        "factor": witness.factor,
        "gap": witness.certificate.gap,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Test all three nested external-source families on each tail miss."""
    primes = [int(record["prime"]) for record in payload["misses"]]
    if not primes:
        raise ValueError("input profile has no tail-deflation misses")
    spf = targeted_descent.TrialSmallestFactors(max(primes))
    records = []
    for prime in primes:
        adaptive = serialize_witness(short_certificate.external_source_descent_witness(prime, spf))
        mixed = serialize_witness(short_certificate.mixed_factor_external_source_descent_witness(prime, spf))
        quadratic = serialize_witness(short_certificate.quadratic_factor_external_source_descent_witness(prime, spf))
        records.append(
            {
                "prime": prime,
                "adaptive_external_descent": adaptive,
                "mixed_factor_descent": mixed,
                "quadratic_factor_descent": quadratic,
            }
        )
    labels = ("adaptive_external_descent", "mixed_factor_descent", "quadratic_factor_descent")
    misses = {
        label: [record["prime"] for record in records if record[label] is None]
        for label in labels
    }
    return {
        "arithmetic": (
            "exact trial-prime factorization of every admissible external source and "
            "exact rational verification of each strict source-to-target lift"
        ),
        "scope_note": (
            "A finite counterexample boundary for deriving external-source descent from "
            "ordinary Type II tail-deflation failure. It is not a conjecture counterexample."
        ),
        "prime_limit": payload["prime_limit"],
        "core_prime_count": payload["core_prime_count"],
        "tail_deflation_miss_count": len(records),
        "adaptive_external_descent_count": len(records) - len(misses["adaptive_external_descent"]),
        "mixed_factor_descent_count": len(records) - len(misses["mixed_factor_descent"]),
        "quadratic_factor_descent_count": len(records) - len(misses["quadratic_factor_descent"]),
        "adaptive_external_misses": misses["adaptive_external_descent"],
        "mixed_factor_misses": misses["mixed_factor_descent"],
        "quadratic_factor_misses": misses["quadratic_factor_descent"],
        "shared_external_misses": sorted(
            set(misses["adaptive_external_descent"])
            & set(misses["mixed_factor_descent"])
            & set(misses["quadratic_factor_descent"])
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {
        key: value
        for key, value in result.items()
        if key not in {"records", "adaptive_external_misses", "mixed_factor_misses", "quadratic_factor_misses", "shared_external_misses"}
    }
    summary["shared_external_miss_count"] = len(result["shared_external_misses"])
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
