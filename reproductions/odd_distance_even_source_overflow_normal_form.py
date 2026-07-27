#!/usr/bin/env python3
"""Normalize every even-source square tail as M=a*g, e=B*g."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-pressure-small-r-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "odd-distance-even-source-overflow-normal-form-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


profile = load_module("odd_distance_even_source_normal_form_profile", PROFILE)


def normalize(m1: int, r: int, factor: int) -> tuple[int, int, int]:
    """Return (a, B, g) for a valid tail factor e=factor."""
    if (
        m1 <= 0
        or r <= 1
        or math.gcd(m1, r) != 1
        or factor <= 0
        or factor > m1
        or m1 * m1 % factor
        or (m1 + factor) % r
    ):
        raise ValueError("invalid even-source square tail")
    g = math.gcd(m1, factor)
    a, overflow = m1 // g, factor // g
    x = (m1 + factor) // r
    if (
        math.gcd(a, overflow) != 1
        or g % overflow
        or overflow > a
        or (a + overflow) % r
        or math.gcd(factor, x) != g
        or factor // math.gcd(factor, x) != overflow
    ):
        raise AssertionError("tail did not satisfy the overflow normal form")
    return a, overflow, g


def reconstruct(a: int, overflow: int, g: int, r: int) -> tuple[int, int]:
    """Reconstruct (M,e) from the overflow normal-form conditions."""
    if (
        a <= 0
        or overflow <= 0
        or g <= 0
        or r <= 1
        or math.gcd(a, overflow) != 1
        or g % overflow
        or overflow > a
        or (a + overflow) % r
    ):
        raise ValueError("invalid overflow normal form")
    m1, factor = a * g, overflow * g
    if factor > m1 or m1 * m1 % factor or (m1 + factor) % r or math.gcd(m1, r) != 1:
        raise AssertionError("normal form did not reconstruct a valid tail")
    return m1, factor


def tail_factors(m1: int, r: int) -> list[int]:
    factors = {int(prime): 2 * int(exponent) for prime, exponent in sympy.factorint(m1).items()}
    target = (-m1) % r
    return [
        divisor
        for divisor in profile.divisors_from_factorization(factors)
        if divisor <= m1 and divisor % r == target
    ]


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Verify both directions on every tail in the stored four-pressure profile."""
    records = []
    for record in payload["records"]:
        prime = int(record["prime"])
        selected = record["first_small_r_tail_hit"]
        if selected is None:
            raise AssertionError("pressure profile must close every selected point")
        r, m1 = int(selected["r"]), int(selected["m1"])
        rows = []
        for factor in tail_factors(m1, r):
            a, overflow, g = normalize(m1, r, factor)
            if reconstruct(a, overflow, g, r) != (m1, factor):
                raise AssertionError("overflow normal form round trip failed")
            rows.append({"a": a, "overflow": overflow, "g": g})
        if len(rows) != int(selected["tail_residue_factor_count"]):
            raise AssertionError("tail factor count disagrees with the stored profile")
        records.append({"prime": prime, "r": r, "tail_count": len(rows), "rows": rows})
    return {
        "arithmetic": (
            "exact M1-squared tail enumeration and bidirectional verification of "
            "M1=a*g, e=B*g with a+B=0 modulo r"
        ),
        "scope_note": "A finite executable check of a general algebraic normal form.",
        "prime_limit": payload["prime_limit"],
        "pressure_point_count": len(records),
        "tail_count": sum(int(record["tail_count"]) for record in records),
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
