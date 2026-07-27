#!/usr/bin/env python3
"""Audit a direct Type II window together with traps and strict descent."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT
    / "reproductions"
    / "type-ii-hybrid-window20-descent-10m-results.json"
)


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


moving_window = load_module("hybrid_moving_window", "moving_window.py")
progression_trap = load_module("hybrid_progression_trap", "type_ii_progression_trap.py")
short_certificate = load_module("hybrid_short_certificate", "short_certificate.py")


def serialize_witness(witness) -> dict[str, object] | None:
    if witness is None:
        return None
    return {
        "source_denominator": witness.source_denominator,
        "k": witness.k,
        "q": witness.q,
        "factor": witness.factor,
        "source_solution": witness.source_solution,
        "target_solution": witness.target_solution,
        "certificate": {
            "gap": witness.certificate.gap,
            "x": witness.certificate.x,
            "divisor": witness.certificate.divisor,
        },
    }


def run_audit(limit: int = 10_000_000, window: int = 20) -> dict[str, object]:
    window_result = moving_window.run_experiment(limit, window)
    residual = window_result["missing"]
    if not isinstance(residual, list):
        raise AssertionError("moving-window output must list its residual")
    spf = short_certificate.smallest_prime_factors(limit)
    records: list[dict[str, object]] = []
    for prime in residual:
        candidate_gap_count, traps = progression_trap.find_all_divisor_traps(
            prime, window
        )
        trap_certificates = [
            progression_trap.certificate_at_index(trap, 0) for trap in traps
        ]
        quadratic = short_certificate.quadratic_factor_external_source_descent_witness(
            prime, spf
        )
        labels: list[str] = []
        if traps:
            labels.append("fixed-factor-progression-trap")
        if quadratic is not None:
            labels.append("quadratic-external-strict-descent")
        records.append(
            {
                "prime": prime,
                "complete_fixed_factor_candidate_gap_count": candidate_gap_count,
                "fixed_factor_traps": list(traps),
                "fixed_factor_trap_certificates_at_seed": trap_certificates,
                "quadratic_external_source_descent": serialize_witness(quadratic),
                "classification": labels,
            }
        )

    uncovered = [
        record["prime"]
        for record in records
        if not record["classification"]
    ]
    return {
        "arithmetic": (
            "exact direct Type II divisor enumeration, complete fixed-factor "
            "candidate-gap enumeration, and explicit strict-descent verification"
        ),
        "scope_note": (
            "A finite hybrid audit only. It does not assert uniform bounds for "
            "the direct window, the trap mechanism, or the descent family."
        ),
        "prime_limit": limit,
        "window_j": window,
        "direct_window_core_prime_count": window_result["core_prime_count"],
        "direct_window_captured_count": window_result["captured_count"],
        "direct_window_residual_count": len(residual),
        "records": records,
        "hybrid_uncovered": uncovered,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--window", type=int, default=20)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.window)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
