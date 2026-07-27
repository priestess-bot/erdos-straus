#!/usr/bin/env python3
"""Audit at-most-one-prime square-surplus reverse edges on 500M tail misses."""

from __future__ import annotations

import argparse
from fractions import Fraction
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
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("tail_single_surplus_landscape", LANDSCAPE)
bridge = load_module("tail_single_surplus_bridge", BRIDGE)


def verified_single_surplus_edge(
    prime: int, gap_cap: int
) -> tuple[dict[str, object] | None, int, int]:
    """Find one strict reverse edge whose square surplus has support at most one."""
    forms = 0
    lifts_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            certificate = bridge.short_certificate.type_i_normal_form_certificate(
                prime, gap, A, B
            )
            if certificate is None:
                raise AssertionError("stored normal form did not rebuild")
            R = (4 * B * B * C + 1) // gap
            K = B * C * (A * R - B)
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            for lift in lifts:
                lifts_checked += 1
                E = int(lift["bridge_divisor"]) // (prime * prime)
                surplus = E // math.gcd(E, 4 * K)
                factors = landscape.factor_by_trial_division(surplus)
                # S=1 is the linear-E case, the degenerate support-zero member
                # of the same at-most-one-extra-prime selector family.
                if len(factors) > 1:
                    continue
                target = (certificate.x, certificate.y, certificate.z)
                source = (int(lift["source_term"]), certificate.x, certificate.y)
                if Fraction(4, prime) != sum((Fraction(1, term) for term in target), Fraction()):
                    raise AssertionError("target identity did not verify")
                source_prime = int(lift["source_denominator"])
                if Fraction(4, source_prime) != sum(
                    (Fraction(1, term) for term in source), Fraction()
                ):
                    raise AssertionError("source identity did not verify")
                return (
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
                        "target_solution": list(target),
                        "reverse_two_tail_lift": lift,
                        "source_solution": list(source),
                    },
                    forms,
                    lifts_checked,
                )
    return None, forms, lifts_checked


def run_audit(tail: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    total_forms = 0
    total_lifts = 0
    for entry in tail["misses"]:
        prime = int(entry["prime"])
        witness, forms, lifts = verified_single_surplus_edge(prime, gap_cap)
        total_forms += forms
        total_lifts += lifts
        if witness is None:
            misses.append(prime)
        else:
            records.append({"prime": prime, **witness})
    exponent_histogram: dict[str, int] = {}
    surplus_support_class_histogram: dict[str, int] = {}
    for record in records:
        exponent = str(record["extra_exponent_count"])
        exponent_histogram[exponent] = exponent_histogram.get(exponent, 0) + 1
        factors = record["square_surplus_factorization"]
        support_class = "linear" if not factors else f"prime:{next(iter(factors))}"
        surplus_support_class_histogram[support_class] = (
            surplus_support_class_histogram.get(support_class, 0) + 1
        )
    return {
        "arithmetic": (
            "for each ordinary Type II p-1-tail miss, enumerate Type I normal certificates "
            "with m=3 (mod 4) through gap_cap, then scan strict maximum-tail reverse lifts "
            "until one has square surplus S=E/gcd(E,4K) supported on at most one prime "
            "(including the linear case S=1); "
            "verify both Egyptian-fraction identities exactly"
        ),
        "scope_note": (
            "strict reverse edge but does not furnish a uniform selector for arbitrary primes."
            "A finite, target-side profile through the stated gap cap. A hit proves an explicit "
            "strict reverse edge but does not furnish a uniform selector for arbitrary primes."
            "strict reverse edge but does not furnish a uniform selector for arbitrary primes."
        ),
        "input_tail_audit": TAIL.name,
        "prime_limit": tail["prime_limit"],
        "ordinary_tail_miss_count": len(tail["misses"]),
        "gap_cap": gap_cap,
        "single_surplus_captured_count": len(records),
        "single_surplus_misses": misses,
        "normal_forms_checked_until_first_hit_or_exhaustion": total_forms,
        "strict_reverse_lifts_checked_until_first_hit_or_exhaustion": total_lifts,
        "maximum_selected_gap": max((int(record["gap"]) for record in records), default=None),
        "maximum_selected_B": max(
            (int(record["normal_form"][1]) for record in records), default=None
        ),
        "selected_surplus_exponent_histogram": dict(
            sorted(exponent_histogram.items(), key=lambda item: int(item[0]))
        ),
        "selected_surplus_support_class_histogram": dict(
            sorted(
                surplus_support_class_histogram.items(),
                key=lambda item: (-1 if item[0] == "linear" else int(item[0].split(":")[1])),
            )
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
