#!/usr/bin/env python3
"""Audit the saturated-support criterion for composite even-source overflow tails."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
TAIL_PROFILE = ROOT / "reproductions" / "type_ii_h19_pressure_even_source_overflow_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-composite-overflow-support-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


tail_profile = load_module("h19_composite_overflow_tail_profile", TAIL_PROFILE)


def saturated_support_part(m1: int, overflow: int) -> int:
    """Return the full M1-part supported on primes dividing the overflow."""
    factors = sympy.factorint(m1)
    return math.prod(int(q) ** int(factors[int(q)]) for q in sympy.factorint(overflow))


def fixed_overflow_witnesses(m1: int, r: int, overflow: int) -> list[dict[str, int]]:
    """Enumerate exactly the tails with prescribed normal-form overflow B."""
    if overflow <= 0:
        raise ValueError("overflow must be positive")
    saturated = saturated_support_part(m1, overflow)
    if saturated % overflow:
        return []
    witnesses = []
    for a in sympy.divisors(m1 // saturated):
        a = int(a)
        if a < overflow or a % r != (-overflow) % r:
            continue
        g = m1 // a
        e = overflow * g
        x = (m1 + e) // r
        if (
            (m1 + e) % r
            or e > m1
            or m1 * m1 % e
            or e % r != (-m1) % r
            or e // math.gcd(e, x) != overflow
        ):
            raise AssertionError("fixed-overflow support criterion produced an invalid tail")
        witnesses.append(
            {
                "overflow": overflow,
                "saturated_support_part": saturated,
                "a": a,
                "g": g,
                "tail_factor": e,
            }
        )
    return sorted(witnesses, key=lambda row: (row["a"], row["tail_factor"]))


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Validate every composite first-r tail through its saturated support."""
    records = []
    for row in payload["records"]:
        if int(row["minimum_overflow"]) == 1:
            continue
        prime, r = int(row["prime"]), int(row["r"])
        m1 = (r * prime + 1) // 4
        tails = tail_profile.tail_rows(prime, r, m1)
        tail_by_overflow: dict[int, set[int]] = {}
        for tail in tails:
            overflow, e = int(tail["overflow"]), int(tail["tail_factor"])
            tail_by_overflow.setdefault(overflow, set()).add(e)
        for overflow, tail_factors in tail_by_overflow.items():
            criterion_factors = {
                int(witness["tail_factor"])
                for witness in fixed_overflow_witnesses(m1, r, overflow)
            }
            if criterion_factors != tail_factors:
                raise AssertionError("fixed-overflow support criterion disagrees with complete tail enumeration")
        if any(sympy.isprime(overflow) for overflow in tail_by_overflow):
            continue
        support_size = min(len(sympy.factorint(overflow)) for overflow in tail_by_overflow)
        omega = min(sum(sympy.factorint(overflow).values()) for overflow in tail_by_overflow)
        canonical_overflow = min(
            overflow
            for overflow in tail_by_overflow
            if len(sympy.factorint(overflow)) == support_size
        )
        canonical_witness = fixed_overflow_witnesses(m1, r, canonical_overflow)[0]
        records.append(
            {
                "prime": prime,
                "r": r,
                "minimum_overflow": int(row["minimum_overflow"]),
                "tail_overflows": sorted(tail_by_overflow),
                "minimum_distinct_prime_support": support_size,
                "minimum_omega": omega,
                "canonical_support_witness": canonical_witness,
            }
        )
    support_histogram = Counter(int(record["minimum_distinct_prime_support"]) for record in records)
    omega_histogram = Counter(int(record["minimum_omega"]) for record in records)
    multi_support = [record for record in records if int(record["minimum_distinct_prime_support"]) >= 3]
    return {
        "arithmetic": (
            "exact factorization of M1, full saturation of every prescribed overflow "
            "support, and equality with exhaustive M1-squared tail enumeration"
        ),
        "scope_note": (
            "A finite classification of composite-only first-r tails. It does not "
            "prove a bounded overflow-support selector generally."
        ),
        "prime_limit": payload["prime_limit"],
        "composite_only_overflow_state_count": len(records),
        "minimum_distinct_prime_support_histogram": {
            str(key): value for key, value in sorted(support_histogram.items())
        },
        "minimum_omega_histogram": {str(key): value for key, value in sorted(omega_histogram.items())},
        "single_prime_support_state_count": support_histogram[1],
        "two_prime_support_state_count": support_histogram[2],
        "at_least_three_prime_support_state_count": len(multi_support),
        "at_least_three_prime_support_records": multi_support,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
