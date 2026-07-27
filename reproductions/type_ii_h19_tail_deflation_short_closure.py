#!/usr/bin/env python3
"""Close the stored H19 residuals by two-tail descent or direct AC proof."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("h19_tail_closure_short_certificate", SHORT_CERTIFICATE)
targeted_descent = load_module("h19_tail_closure_targeted_descent", TARGETED_DESCENT)


def verify_direct_ac(prime: int, witness: dict[str, int]) -> dict[str, int]:
    a = int(witness["a"])
    c = int(witness["c"])
    k = int(witness["k"])
    h = int(witness["h"])
    gap = int(witness["gap"])
    if h != 4 * a * c * k - 1 or prime + 4 * a * a * c != h * gap:
        raise AssertionError("AC factor pair did not reconstruct")
    solution = tuple(int(witness[key]) for key in ("x", "y", "z"))
    if Fraction(4, prime) != sum((Fraction(1, value) for value in solution), Fraction()):
        raise AssertionError("direct AC certificate did not verify")
    return {key: int(witness[key]) for key in ("radius", "a", "c", "k", "h", "gap", "divisor")}


def serialize_tail_witness(witness) -> dict[str, int]:
    if not 2 <= witness.source_denominator < witness.prime:
        raise AssertionError("two-tail source is not strict")
    if Fraction(4, witness.source_denominator) != sum(
        (Fraction(1, value) for value in witness.source_solution), Fraction()
    ):
        raise AssertionError("two-tail source solution did not verify")
    if Fraction(4, witness.prime) != sum(
        (Fraction(1, value) for value in witness.target_solution), Fraction()
    ):
        raise AssertionError("two-tail target solution did not verify")
    return {
        "source_denominator": witness.source_denominator,
        "gap": witness.gap,
        "divisor": witness.certificate.divisor,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Use least-gap two-tail descent, with direct AC only for its misses."""
    records = payload["records"]
    spf = targeted_descent.TrialSmallestFactors(max(int(record["prime"]) for record in records))
    tail_records = []
    ac_fallbacks = []
    for record in records:
        prime = int(record["prime"])
        witness = short_certificate.first_type_ii_tail_deflation_witness(prime, spf)
        if witness is not None:
            tail_records.append({"prime": prime, "tail_deflation_witness": serialize_tail_witness(witness)})
            continue
        direct_ac = record["direct_ac_witness"]
        if direct_ac is None:
            raise AssertionError("tail miss has no stored direct AC certificate")
        ac_fallbacks.append({"prime": prime, "direct_ac_witness": verify_direct_ac(prime, direct_ac)})
    gap_histogram = Counter(int(record["tail_deflation_witness"]["gap"]) for record in tail_records)
    return {
        "arithmetic": (
            "exact factorization of every p-1 controlled Type II tail, with exact "
            "source/target verification after tail division and direct AC verification "
            "for the two remaining points"
        ),
        "scope_note": (
            "A finite H19 closure. It does not establish a universal two-tail "
            "deflation selector or a global AC-radius bound."
        ),
        "prime_limit": payload["prime_limit"],
        "base_shift_bound": payload["base_shift_bound"],
        "h19_residual_count": len(records),
        "tail_deflation_count": len(tail_records),
        "tail_deflation_missing_primes": [record["prime"] for record in ac_fallbacks],
        "minimal_tail_deflation_gap_histogram": {
            str(key): value for key, value in sorted(gap_histogram.items())
        },
        "maximum_minimal_tail_deflation_gap": max(gap_histogram, default=None),
        "direct_ac_fallback_count": len(ac_fallbacks),
        "direct_ac_fallback_records": ac_fallbacks,
        "tail_records": tail_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "tail_records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
