#!/usr/bin/env python3
"""Close H19 radius-six AC misses by exact Type II two-tail deflation."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
TARGETED_DESCENT = ROOT / "reproductions" / "type_ii_h19_targeted_quadratic_descent.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-residual-ac-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-ac6-tail-deflation-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("h19_ac6_tail_short_certificate", SHORT_CERTIFICATE)
targeted_descent = load_module("h19_ac6_tail_targeted_descent", TARGETED_DESCENT)


def serialize_witness(witness) -> dict[str, object]:
    source_solution = list(witness.source_solution)
    target_solution = list(witness.target_solution)
    if not 2 <= witness.source_denominator < witness.prime:
        raise AssertionError("two-tail source is not strict")
    if Fraction(4, witness.source_denominator) != sum(
        (Fraction(1, value) for value in source_solution), Fraction()
    ):
        raise AssertionError("two-tail source solution did not verify")
    if Fraction(4, witness.prime) != sum(
        (Fraction(1, value) for value in target_solution), Fraction()
    ):
        raise AssertionError("two-tail target solution did not verify")
    return {
        "source_denominator": witness.source_denominator,
        "gap": witness.gap,
        "source_solution": source_solution,
        "target_solution": target_solution,
        "certificate": {
            "type": witness.certificate.certificate_type,
            "gap": witness.certificate.gap,
            "x": witness.certificate.x,
            "divisor": witness.certificate.divisor,
            "y": witness.certificate.y,
            "z": witness.certificate.z,
        },
    }


def run_audit(payload: dict[str, object], ac_bound: int = 6) -> dict[str, object]:
    """Find the least-gap Type II two-tail descent for every AC-box miss."""
    misses = [
        record
        for record in payload["records"]
        if int(record["direct_ac_witness"]["radius"]) > ac_bound
    ]
    spf = targeted_descent.TrialSmallestFactors(max(int(record["prime"]) for record in misses))
    records = []
    for record in misses:
        prime = int(record["prime"])
        witness = short_certificate.first_type_ii_tail_deflation_witness(prime, spf)
        records.append(
            {
                "prime": prime,
                "direct_ac_radius": int(record["direct_ac_witness"]["radius"]),
                "tail_deflation_witness": None if witness is None else serialize_witness(witness),
            }
        )
    captured = [record for record in records if record["tail_deflation_witness"] is not None]
    gap_histogram = Counter(int(record["tail_deflation_witness"]["gap"]) for record in captured)
    return {
        "arithmetic": (
            "exact factorization of each divisor-controlled Type II tail, followed by "
            "exact source and target unit-fraction verification after dividing both tails by p"
        ),
        "scope_note": (
            "A finite direct-certificate-or-two-tail-descent profile of the stored H19 "
            "residuals. It does not prove a global AC or tail-deflation selector."
        ),
        "prime_limit": payload["prime_limit"],
        "base_shift_bound": payload["base_shift_bound"],
        "h19_residual_count": len(payload["records"]),
        "ac_radius_bound": ac_bound,
        "direct_ac_short_count": len(payload["records"]) - len(misses),
        "direct_ac_short_miss_count": len(misses),
        "tail_deflation_captured_count": len(captured),
        "tail_deflation_missing_primes": [
            record["prime"] for record in records if record["tail_deflation_witness"] is None
        ],
        "minimal_tail_deflation_gap_histogram": {
            str(key): value for key, value in sorted(gap_histogram.items())
        },
        "maximum_minimal_tail_deflation_gap": max(gap_histogram, default=None),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--ac-bound", type=int, default=6)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")), args.ac_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
