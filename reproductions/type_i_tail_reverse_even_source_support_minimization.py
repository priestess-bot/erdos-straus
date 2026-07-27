#!/usr/bin/env python3
"""Minimize target-side bridge-factor complexity among 500M even-source edges."""

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
DEFAULT_GAP_CAP = 215
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("even_source_support_min_landscape", LANDSCAPE)
bridge = load_module("even_source_support_min_bridge", BRIDGE)


def factor_E_from_K(E: int, K_factors: dict[int, int]) -> dict[int, int]:
    """Factor E from E|4K^2, without trial-dividing a potentially huge E."""
    remaining = E
    factors: dict[int, int] = {}
    allowed = dict(K_factors)
    allowed[2] = allowed.get(2, 0) + 1  # 4K^2 has two extra powers of 2.
    for prime, K_exponent in sorted(allowed.items()):
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            if exponent > 2 * K_exponent:
                raise AssertionError("E exceeded its 4K^2 prime exponent budget")
            factors[prime] = exponent
    if remaining != 1:
        raise AssertionError("E had a prime factor outside 4K^2")
    return factors


def least_support_edge(prime: int, gap_cap: int) -> tuple[dict[str, object] | None, int, int]:
    """Exhaust all even-source lifts and select the least bridge-factor support."""
    forms = 0
    lifts_checked = 0
    best: dict[str, object] | None = None
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            R = (4 * B * B * C + 1) // gap
            H = A * R - B
            K = B * C * H
            K_factors = bridge.factor_product(B, C, H)
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            for lift in lifts:
                lifts_checked += 1
                source = int(lift["source_denominator"])
                if source % 2:
                    continue
                divisor = int(lift["bridge_divisor"])
                if divisor % (prime * prime):
                    raise AssertionError("bridge divisor did not reconstruct E")
                E = divisor // (prime * prime)
                factors = factor_E_from_K(E, K_factors)
                if E % 2 or (4 * K * K) % E or (4 * K - E) % R:
                    raise AssertionError("candidate did not satisfy the even-source selector")
                candidate = {
                    "gap": gap,
                    "normal_form": [A, B, C],
                    "R": R,
                    "K": K,
                    "E": E,
                    "E_factorization": {str(q): exponent for q, exponent in factors.items()},
                    "E_prime_support_count": len(factors),
                    "E_exponent_count": sum(factors.values()),
                    "reverse_two_tail_lift": lift,
                }
                if best is None or (
                    candidate["E_prime_support_count"],
                    candidate["E_exponent_count"],
                    candidate["E"],
                    candidate["normal_form"][1],
                    candidate["gap"],
                    candidate["reverse_two_tail_lift"]["source_denominator"],
                ) < (
                    best["E_prime_support_count"],
                    best["E_exponent_count"],
                    best["E"],
                    best["normal_form"][1],
                    best["gap"],
                    best["reverse_two_tail_lift"]["source_denominator"],
                ):
                    best = candidate
    return best, forms, lifts_checked


def run_audit(tail: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms = 0
    lifts = 0
    for entry in tail["misses"]:
        prime = int(entry["prime"])
        witness, local_forms, local_lifts = least_support_edge(prime, gap_cap)
        forms += local_forms
        lifts += local_lifts
        if witness is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, "selected_edge": witness})
    support_histogram: dict[str, int] = {}
    exponent_histogram: dict[str, int] = {}
    for record in records:
        edge = record["selected_edge"]
        support = str(edge["E_prime_support_count"])
        exponent = str(edge["E_exponent_count"])
        support_histogram[support] = support_histogram.get(support, 0) + 1
        exponent_histogram[exponent] = exponent_histogram.get(exponent, 0) + 1
    return {
        "arithmetic": (
            "for every ordinary Type II p-1-tail miss, enumerate every Type I normal form "
            "and strict maximum-tail reverse lift through gap_cap; keep even-source lifts and "
            "minimize their bridge divisor E by (prime support, exponent count, value, B, gap, source)"
        ),
        "scope_note": (
            "An exhaustive finite complexity profile of the target-side even-source selector. "
            "It does not prove a global bound on bridge-factor support."
        ),
        "prime_limit": tail["prime_limit"],
        "ordinary_tail_miss_count": len(tail["misses"]),
        "gap_cap": gap_cap,
        "captured_count": len(records),
        "misses": misses,
        "normal_forms_exhaustively_checked": forms,
        "strict_reverse_lifts_exhaustively_checked": lifts,
        "least_E_support_histogram": dict(sorted(support_histogram.items(), key=lambda item: int(item[0]))),
        "least_E_exponent_histogram": dict(sorted(exponent_histogram.items(), key=lambda item: int(item[0]))),
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
