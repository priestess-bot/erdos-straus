#!/usr/bin/env python3
"""Expose the exhausted-prime normal form behind deficit-one zero-overflow failures."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFICIT_SCRIPT = ROOT / "reproductions" / "type_ii_h19_zero_overflow_exponent_deficit.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json"
DEFAULT_RELEASE = ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-deficit-one-saturated-prime-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


deficit_profile = load_module("h19_deficit_one_saturated_prime", DEFICIT_SCRIPT)


def saturated_prime_witness(m1: int, r: int) -> dict[str, int] | None:
    """Return q^nu*b=a with q*a=-1 mod r and q^nu exactly exhausted in a."""
    for q, exponent in sorted((int(q), int(e)) for q, e in sympy.factorint(m1).items()):
        q_power = q**exponent
        for b in sympy.divisors(m1 // q_power):
            b = int(b)
            a = q_power * b
            if (q * a) % r != r - 1:
                continue
            if m1 % a or m1 % q_power or a % q_power:
                raise AssertionError("invalid saturated-prime divisor witness")
            if (m1 // a) % q == 0:
                raise AssertionError("q was not exhausted in the divisor")
            return {
                "saturated_prime": q,
                "saturated_exponent": exponent,
                "cofactor": b,
                "ordinary_divisor": a,
            }
    return None


def run_audit(overflow_payload: dict[str, object], release_payload: dict[str, object]) -> dict[str, object]:
    """Audit the saturated-prime form on every high-overflow first-r state."""
    releases = {
        int(record["prime"]): record["later_zero_overflow_release_r"]
        for record in release_payload["records"]
    }
    records = []
    for record in overflow_payload["records"]:
        if int(record["minimum_overflow"]) == 1:
            continue
        prime, r = int(record["prime"]), int(record["r"])
        m1 = (r * prime + 1) // 4
        deficit = deficit_profile.exponent_deficit(m1, r)
        if deficit != 1:
            continue
        witness = saturated_prime_witness(m1, r)
        if witness is None:
            raise AssertionError("deficit-one state has no exhausted-prime witness")
        records.append(
            {
                "prime": prime,
                "r": r,
                "later_zero_overflow_release_r": releases[prime],
                **witness,
            }
        )
    histogram = Counter(str(record["saturated_prime"]) for record in records)
    return {
        "arithmetic": (
            "exact factorization of M1=(r*p+1)/4 and divisor enumeration for a=q^nu*b "
            "with q^nu exactly the q-part of M1 and q*a=-1 modulo r"
        ),
        "scope_note": (
            "A finite normal-form audit for deficit-one high-overflow first-r states. "
            "It does not construct a source conversion or a later-r release."
        ),
        "prime_limit": overflow_payload["prime_limit"],
        "deficit_one_high_overflow_count": len(records),
        "later_zero_overflow_release_count": sum(
            record["later_zero_overflow_release_r"] is not None for record in records
        ),
        "unreleased_through_r_cap_count": sum(
            record["later_zero_overflow_release_r"] is None for record in records
        ),
        "canonical_saturated_prime_histogram": dict(sorted(histogram.items(), key=lambda item: int(item[0]))),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--release", type=Path, default=DEFAULT_RELEASE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.input.read_text(encoding="utf-8")),
        json.loads(args.release.read_text(encoding="utf-8")),
    )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
