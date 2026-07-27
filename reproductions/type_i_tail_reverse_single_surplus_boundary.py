#!/usr/bin/env python3
"""Classify the multi-prime square-surplus boundary left by the 500M audit."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-500m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-boundary-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("single_surplus_boundary_landscape", LANDSCAPE)
bridge = load_module("single_surplus_boundary_bridge", BRIDGE)


def least_surplus_record(prime: int, gap_cap: int) -> tuple[dict[str, object], int, int]:
    """Inspect every strict reverse lift and return the least non-linear surplus."""
    forms = 0
    lifts_checked = 0
    candidates: list[dict[str, object]] = []
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            R = (4 * B * B * C + 1) // gap
            K = B * C * (A * R - B)
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            for lift in lifts:
                lifts_checked += 1
                E = int(lift["bridge_divisor"]) // (prime * prime)
                surplus = E // math.gcd(E, 4 * K)
                factors = landscape.factor_by_trial_division(surplus)
                candidates.append(
                    {
                        "gap": gap,
                        "normal_form": [A, B, C],
                        "K": K,
                        "E": E,
                        "square_surplus": surplus,
                        "square_surplus_factorization": {
                            str(q): exponent for q, exponent in factors.items()
                        },
                        "extra_exponent_count": sum(factors.values()),
                        "extra_prime_support_count": len(factors),
                        "reverse_two_tail_lift": lift,
                    }
                )
    if not candidates:
        raise AssertionError("boundary prime had no strict reverse lift")
    return (
        min(
            candidates,
            key=lambda item: (
                item["extra_prime_support_count"],
                item["extra_exponent_count"],
                item["square_surplus"],
                item["normal_form"][1],
                item["gap"],
                item["reverse_two_tail_lift"]["source_denominator"],
            ),
        ),
        forms,
        lifts_checked,
    )


def run_audit(profile: dict[str, object]) -> dict[str, object]:
    gap_cap = int(profile["gap_cap"])
    residuals = [int(prime) for prime in profile["single_surplus_misses"]]
    records: list[dict[str, object]] = []
    total_forms = 0
    total_lifts = 0
    for prime in residuals:
        witness, forms, lifts = least_surplus_record(prime, gap_cap)
        total_forms += forms
        total_lifts += lifts
        if int(witness["extra_prime_support_count"]) <= 1:
            raise AssertionError("at-most-one-prime residual reconstructed a qualifying witness")
        records.append({"prime": prime, "least_square_surplus": witness})
    support_histogram: dict[str, int] = {}
    exponent_histogram: dict[str, int] = {}
    terminal_residue_counts: dict[str, int] = {}
    maximum_terminal_factor = 0
    for record in records:
        witness = record["least_square_surplus"]
        support = str(witness["extra_prime_support_count"])
        exponent = str(witness["extra_exponent_count"])
        support_histogram[support] = support_histogram.get(support, 0) + 1
        exponent_histogram[exponent] = exponent_histogram.get(exponent, 0) + 1
        source = int(witness["reverse_two_tail_lift"]["source_denominator"])
        source_factors = landscape.factor_by_trial_division(source)
        terminal_prime = next((q for q in source_factors if q % 24 != 1), None)
        if terminal_prime is None:
            raise AssertionError("least boundary source had only core prime factors")
        residue = str(terminal_prime % 24)
        terminal_residue_counts[residue] = terminal_residue_counts.get(residue, 0) + 1
        maximum_terminal_factor = max(maximum_terminal_factor, terminal_prime)
    return {
        "arithmetic": (
            "for each residual from the one-prime square-surplus profile, enumerate every "
            "Type I normal certificate with m=3 (mod 4) through the inherited gap cap and "
            "every strict maximum-tail reverse lift; select the lexicographically least "
            "surplus by (prime support, exponent count, value, B, gap, source)"
        ),
        "scope_note": (
            "An exhaustive target-side boundary within the inherited finite box. It classifies "
            "the obstruction to a one-prime surplus rule but is not a global selector theorem."
        ),
        "input_single_surplus_profile": PROFILE.name,
        "prime_limit": profile["prime_limit"],
        "gap_cap": gap_cap,
        "boundary_residual_count": len(records),
        "normal_forms_exhaustively_checked": total_forms,
        "strict_reverse_lifts_exhaustively_checked": total_lifts,
        "least_surplus_support_histogram": dict(
            sorted(support_histogram.items(), key=lambda item: int(item[0]))
        ),
        "least_surplus_exponent_histogram": dict(
            sorted(exponent_histogram.items(), key=lambda item: int(item[0]))
        ),
        "unresolved_core_source_count": 0,
        "terminal_prime_residue_counts_mod_24": dict(
            sorted(terminal_residue_counts.items(), key=lambda item: int(item[0]))
        ),
        "maximum_selected_terminal_prime": maximum_terminal_factor,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.profile.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
