#!/usr/bin/env python3
"""Close every stored H19 residual by a verified strict descent."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TAIL = ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json"
DEFAULT_EXTERNAL = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-all-strict-descent-closure-1b-results.json"


def verify_external_descent(prime: int, witness: dict[str, object]) -> dict[str, int]:
    source = int(witness["source_denominator"])
    source_solution = tuple(int(value) for value in witness["source_solution"])
    target_solution = tuple(int(value) for value in witness["target_solution"])
    if not 2 <= source < prime:
        raise AssertionError("external source is not strict")
    if Fraction(4, source) != sum((Fraction(1, value) for value in source_solution), Fraction()):
        raise AssertionError("external source solution did not verify")
    if Fraction(4, prime) != sum((Fraction(1, value) for value in target_solution), Fraction()):
        raise AssertionError("external target lift did not verify")
    return {
        "source_denominator": source,
        "k": int(witness["k"]),
        "q": int(witness["q"]),
        "factor": int(witness["factor"]),
        "gap": int(witness["certificate"]["gap"]),
    }


def run_audit(tail_payload: dict[str, object], external_payload: dict[str, object]) -> dict[str, object]:
    """Replace the two ordinary-tail misses with adaptive external descents."""
    tail_records = tail_payload["tail_records"]
    tail_primes = {int(record["prime"]) for record in tail_records}
    external_records = {int(record["prime"]): record for record in external_payload["records"]}
    tail_misses = [int(prime) for prime in tail_payload["tail_deflation_missing_primes"]]
    if len(tail_records) + len(tail_misses) != int(tail_payload["h19_residual_count"]):
        raise AssertionError("tail profile does not partition the H19 residuals")
    fallbacks = []
    for prime in tail_misses:
        record = external_records.get(prime)
        if record is None:
            raise AssertionError("tail miss is absent from external-source profile")
        witness = record["adaptive_external_source_descent"]
        if witness is None:
            raise AssertionError("tail miss has no adaptive external strict descent")
        fallbacks.append({"prime": prime, "adaptive_external_descent": verify_external_descent(prime, witness)})
    if tail_primes & {record["prime"] for record in fallbacks}:
        raise AssertionError("tail and fallback branches overlap")
    return {
        "arithmetic": (
            "exact two-tail source/target verification for the stored tail branch, "
            "plus exact rational verification of the two adaptive external lifts"
        ),
        "scope_note": (
            "A finite H19 strict-descent closure. It does not establish a universal "
            "tail-deflation or external-source selector."
        ),
        "prime_limit": tail_payload["prime_limit"],
        "base_shift_bound": tail_payload["base_shift_bound"],
        "h19_residual_count": tail_payload["h19_residual_count"],
        "two_tail_descent_count": len(tail_records),
        "adaptive_external_fallback_count": len(fallbacks),
        "unclosed_primes": [],
        "adaptive_external_fallback_records": fallbacks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail-profile", type=Path, default=DEFAULT_TAIL)
    parser.add_argument("--external-profile", type=Path, default=DEFAULT_EXTERNAL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.tail_profile.read_text(encoding="utf-8")),
        json.loads(args.external_profile.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
