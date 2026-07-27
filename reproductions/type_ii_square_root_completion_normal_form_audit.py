#!/usr/bin/env python3
"""Normalize every stored ordinary Type II tail certificate to (q,d,t)."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-262144.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-square-root-completion-normal-form-262144.json"


def load_family():
    path = ROOT / "reproductions" / "type_ii_square_root_completion_family.py"
    spec = importlib.util.spec_from_file_location("type_ii_square_root_completion_family", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


family = load_family()


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Check the reverse normal form without refactoring the stored divisors."""
    tail_gap_counts: Counter[int] = Counter()
    route_counts: Counter[str] = Counter()
    shared_27_tail_counts: Counter[int] = Counter()
    failures: list[dict[str, object]] = []
    for record in payload["records"]:
        witness = record["tail_witness"]
        if witness is None:
            failures.append({"prime": int(record["prime"]), "reason": "missing tail witness"})
            continue
        prime = int(record["prime"])
        gap = int(witness["gap"])
        divisor = int(witness["divisor"])
        try:
            normalized = family.verify_normal_form(prime, gap, divisor)
        except ValueError as error:
            failures.append({"prime": prime, "reason": str(error)})
            continue
        if normalized["source_denominator"] != int(witness["source_denominator"]):
            failures.append({"prime": prime, "reason": "source denominator mismatch"})
            continue
        tail_gap_counts[gap] += 1
        route_counts[str(record["route"])] += 1
        if int(record["shared_selector_gap"]) == 27:
            shared_27_tail_counts[gap] += 1
    return {
        "arithmetic": (
            "exact recovery q=(m+1)/4 and t=(p-1)/(m+1), followed by "
            "the Type II congruence, coprimality, core-divisibility, square-divisor, "
            "and source-denominator checks for every stored ordinary tail witness"
        ),
        "scope_note": (
            "This proves that the supplied finite certificates have the square-root "
            "completion normal form. It does not select a certificate for an arbitrary prime."
        ),
        "input_parameter_limit_exclusive": payload["input_parameter_limit_exclusive"],
        "record_count": len(payload["records"]),
        "normal_form_count": len(payload["records"]) - len(failures),
        "failures": failures,
        "route_counts": dict(sorted(route_counts.items())),
        "tail_gap_histogram": {str(gap): count for gap, count in sorted(tail_gap_counts.items())},
        "shared_gap_27_tail_gap_histogram": {
            str(gap): count for gap, count in sorted(shared_27_tail_counts.items())
        },
        "shared_gap_27_to_tail_gap_31_count": shared_27_tail_counts[31],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
