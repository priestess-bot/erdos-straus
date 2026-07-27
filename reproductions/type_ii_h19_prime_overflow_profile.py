#!/usr/bin/env python3
"""Audit the exact prime-overflow slice of first-r even-source tails.

For a tail normalized by M=a*g and e=B*g, the case B=q prime is equivalent
to a divisor a of M with its full q-part removed, satisfying a=-q (mod r).
This script checks that criterion independently against full tail enumeration.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
TAIL_PROFILE = ROOT / "reproductions" / "type_ii_h19_pressure_even_source_overflow_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-prime-overflow-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


tail_profile = load_module("h19_prime_overflow_tail_profile", TAIL_PROFILE)


def prime_overflow_witnesses(m1: int, r: int) -> list[dict[str, int]]:
    """Enumerate q-prime overflow tails using the divisor-only criterion."""
    witnesses = []
    for q, exponent in sorted(sympy.factorint(m1).items()):
        q = int(q)
        q_power = q ** int(exponent)
        for a in sympy.divisors(m1 // q_power):
            a = int(a)
            if a < q or a % r != (-q) % r:
                continue
            g = m1 // a
            e = q * g
            x = (m1 + e) // r
            if (
                (m1 + e) % r
                or e > m1
                or m1 * m1 % e
                or e % r != (-m1) % r
                or e // math.gcd(e, x) != q
            ):
                raise AssertionError("prime-overflow divisor criterion produced an invalid tail")
            witnesses.append({"overflow_prime": q, "a": a, "g": g, "tail_factor": e})
    return sorted(witnesses, key=lambda row: (row["overflow_prime"], row["a"], row["tail_factor"]))


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Compare the prime-overflow criterion with exhaustive first-r tail rows."""
    records = []
    for row in payload["records"]:
        if int(row["minimum_overflow"]) == 1:
            continue
        prime, r = int(row["prime"]), int(row["r"])
        m1 = (r * prime + 1) // 4
        tails = tail_profile.tail_rows(prime, r, m1)
        tail_primes = sorted(
            {int(tail["overflow"]) for tail in tails if sympy.isprime(int(tail["overflow"]))}
        )
        witnesses = prime_overflow_witnesses(m1, r)
        criterion_primes = sorted({int(witness["overflow_prime"]) for witness in witnesses})
        if criterion_primes != tail_primes:
            raise AssertionError("prime-overflow criterion disagrees with complete tail enumeration")
        records.append(
            {
                "prime": prime,
                "r": r,
                "minimum_overflow": int(row["minimum_overflow"]),
                "tail_overflows": [int(tail["overflow"]) for tail in tails],
                "prime_overflow_primes": criterion_primes,
                "canonical_prime_overflow_witness": witnesses[0] if witnesses else None,
            }
        )
    prime_overflow_records = [record for record in records if record["prime_overflow_primes"]]
    composite_only_records = [record for record in records if not record["prime_overflow_primes"]]
    return {
        "arithmetic": (
            "exact factorization of M1=(r*p+1)/4, divisor enumeration after removing "
            "the full q-part, and equality with exhaustive M1-squared tail enumeration"
        ),
        "scope_note": (
            "A finite profile of the established prime-overflow criterion on stored "
            "first-r H19 states. It does not select such a prime for general inputs."
        ),
        "prime_limit": payload["prime_limit"],
        "high_overflow_state_count": len(records),
        "prime_overflow_state_count": len(prime_overflow_records),
        "composite_only_overflow_state_count": len(composite_only_records),
        "minimum_overflow_is_prime_count": sum(
            sympy.isprime(int(record["minimum_overflow"])) for record in records
        ),
        "maximum_prime_overflow": max(
            (max(record["prime_overflow_primes"]) for record in prime_overflow_records),
            default=None,
        ),
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
