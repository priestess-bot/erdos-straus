#!/usr/bin/env python3
"""Minimize terminal factors among all one-prime-surplus reverse edges at 500M."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_GAP_CAP = 127
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-terminal-min-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("single_surplus_terminal_min_landscape", LANDSCAPE)
bridge = load_module("single_surplus_terminal_min_bridge", BRIDGE)


def terminal_factor(source: int) -> tuple[dict[int, int], int | None]:
    factors = landscape.factor_by_trial_division(source)
    terminal = next((q for q in factors if q % 24 != 1), None)
    return factors, terminal


def best_terminal_edge(prime: int, gap_cap: int) -> tuple[dict[str, object] | None, int, int]:
    """Minimize terminal factor; q=2 is globally optimal and ends the scan."""
    forms = 0
    lifts = 0
    best: dict[str, object] | None = None
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            R = (4 * B * B * C + 1) // gap
            K = B * C * (A * R - B)
            _, reverse_lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            for lift in reverse_lifts:
                lifts += 1
                E = int(lift["bridge_divisor"]) // (prime * prime)
                surplus = E // math.gcd(E, 4 * K)
                surplus_factors = landscape.factor_by_trial_division(surplus)
                if len(surplus_factors) > 1:
                    continue
                source = int(lift["source_denominator"])
                source_factors, terminal = terminal_factor(source)
                if terminal is None:
                    continue
                candidate = {
                    "gap": gap,
                    "normal_form": [A, B, C],
                    "K": K,
                    "E": E,
                    "square_surplus": surplus,
                    "square_surplus_factorization": {
                        str(q): exponent for q, exponent in surplus_factors.items()
                    },
                    "extra_prime_support_count": len(surplus_factors),
                    "reverse_two_tail_lift": lift,
                    "source_factorization": {str(q): exponent for q, exponent in source_factors.items()},
                    "terminal_prime": terminal,
                    "terminal_prime_mod_24": terminal % 24,
                }
                if best is None or (
                    candidate["terminal_prime"],
                    candidate["extra_prime_support_count"],
                    candidate["square_surplus"],
                    candidate["normal_form"][1],
                    candidate["gap"],
                    candidate["reverse_two_tail_lift"]["source_denominator"],
                ) < (
                    best["terminal_prime"],
                    best["extra_prime_support_count"],
                    best["square_surplus"],
                    best["normal_form"][1],
                    best["gap"],
                    best["reverse_two_tail_lift"]["source_denominator"],
                ):
                    best = candidate
                if terminal == 2:
                    return best, forms, lifts
    return best, forms, lifts


def run_audit(tail: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms = 0
    lifts = 0
    for entry in tail["misses"]:
        prime = int(entry["prime"])
        witness, local_forms, local_lifts = best_terminal_edge(prime, gap_cap)
        forms += local_forms
        lifts += local_lifts
        if witness is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, "selected_edge": witness})
    terminal_histogram: dict[str, int] = {}
    for record in records:
        terminal = str(record["selected_edge"]["terminal_prime"])
        terminal_histogram[terminal] = terminal_histogram.get(terminal, 0) + 1
    return {
        "arithmetic": (
            "for every ordinary-tail miss, scan Type I normal certificates with m=3 (mod 4) "
            "through gap_cap and strict reverse lifts; retain lifts whose square surplus has "
            "support at most one, factor each source, then minimize by (least non-core terminal "
            "prime, support, surplus, B, gap, source), stopping safely once terminal prime 2 occurs"
        ),
        "scope_note": (
            "A finite target-side terminal-factor optimization. The q=2 early stop is exact "
            "because 2 is the least possible terminal prime; this does not prove a uniform "
            "terminal-prime bound beyond the stated box."
        ),
        "prime_limit": tail["prime_limit"],
        "ordinary_tail_miss_count": len(tail["misses"]),
        "gap_cap": gap_cap,
        "captured_count": len(records),
        "misses": misses,
        "normal_forms_checked_until_terminal_minimum_or_exhaustion": forms,
        "strict_reverse_lifts_checked_until_terminal_minimum_or_exhaustion": lifts,
        "maximum_selected_terminal_prime": max(
            (int(record["selected_edge"]["terminal_prime"]) for record in records), default=None
        ),
        "selected_terminal_prime_histogram": dict(
            sorted(terminal_histogram.items(), key=lambda item: int(item[0]))
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tail", type=Path, default=TAIL)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.tail.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
