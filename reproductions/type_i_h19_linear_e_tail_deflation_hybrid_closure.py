#!/usr/bin/env python3
"""Close the full-box linear-E residual by exact Type II tail deflation."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINEAR = ROOT / "reproductions" / "type-i-h19-reverse-two-tail-linear-e-full-b-boundary-1b-results.json"
TAIL = ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json"
TAIL_CLOSURE = ROOT / "reproductions" / "type_ii_h19_tail_deflation_short_closure.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-linear-e-tail-deflation-hybrid-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


tail_closure = load_module("h19_linear_e_tail_hybrid_closure", TAIL_CLOSURE)


def run_closure(linear: dict[str, object], tail: dict[str, object]) -> dict[str, object]:
    linear_misses = [int(value) for value in linear["unbounded_b_linear_e_misses"]]
    if len(linear_misses) != int(linear["unbounded_b_audited_count"]):
        raise AssertionError("linear residual count did not reconstruct")
    tail_rows = {int(record["prime"]): record["tail_deflation_witness"] for record in tail["tail_records"]}
    tail_misses = {int(value) for value in tail["tail_deflation_missing_primes"]}
    if tail_misses & set(linear_misses):
        raise AssertionError("a full-box linear residual escaped Type II tail deflation")
    spf = tail_closure.targeted_descent.TrialSmallestFactors(max(linear_misses))
    records: list[dict[str, object]] = []
    for prime in linear_misses:
        expected = tail_rows.get(prime)
        if expected is None:
            raise AssertionError("linear residual was absent from the tail-deflation archive")
        witness = tail_closure.short_certificate.first_type_ii_tail_deflation_witness(prime, spf)
        if witness is None:
            raise AssertionError("stored Type II tail witness did not rebuild")
        rebuilt = tail_closure.serialize_tail_witness(witness)
        if rebuilt != expected:
            raise AssertionError("stored Type II tail witness changed")
        records.append({"prime": prime, "tail_deflation_witness": rebuilt})
    linear_captured = int(linear["full_box_linear_e_captured_count"])
    if linear_captured + len(records) != int(linear["h19_residual_count"]):
        raise AssertionError("hybrid branches did not partition the H19 residuals")
    return {
        "arithmetic": (
            "take the exact full-box Type I linear-E residual set, rebuild each stored "
            "Type II p-1 tail-deflation witness with exact source and target identities, "
            "and verify that the two branches partition the H19 residuals"
        ),
        "scope_note": (
            "Finite hybrid strict-descent closure for the stored H19 residuals. It does "
            "not prove a universal linear-E or Type II tail selector."
        ),
        "linear_e_full_box_artifact": "type-i-h19-reverse-two-tail-linear-e-full-b-boundary-1b-results.json",
        "tail_deflation_artifact": "type-ii-h19-tail-deflation-short-closure-1b-results.json",
        "prime_limit": linear["prime_limit"],
        "base_shift_bound": linear["base_shift_bound"],
        "h19_residual_count": linear["h19_residual_count"],
        "linear_e_full_box_descent_count": linear_captured,
        "tail_deflation_fallback_count": len(records),
        "unclosed_primes": [],
        "maximum_tail_deflation_gap_on_linear_residual": max(
            (int(record["tail_deflation_witness"]["gap"]) for record in records), default=None
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--linear", type=Path, default=LINEAR)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_closure(
        json.loads(args.linear.read_text(encoding="utf-8")),
        json.loads(args.tail.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
