#!/usr/bin/env python3
"""Measure Type I target-divisor overflow induced by small-r even-source tails."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-pressure-small-r-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-pressure-even-source-overflow-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


profile = load_module("h19_even_source_overflow_profile", PROFILE)
short_certificate = load_module("h19_even_source_overflow_short_certificate", SHORT_CERTIFICATE)


def tail_rows(prime: int, r: int, m1: int) -> list[dict[str, object]]:
    """Normalize every selected M1-squared residue factor into a Type I overflow."""
    factorization = {
        int(factor): 2 * int(exponent)
        for factor, exponent in sympy.factorint(m1).items()
    }
    target = (-m1) % r
    rows = []
    for factor in profile.divisors_from_factorization(factorization):
        if factor > m1 or factor % r != target:
            continue
        gap = (4 * factor + 1) // r
        x = (prime + gap) // 4
        if m1 + factor != r * x or x * x % factor:
            raise AssertionError("even-source tail did not normalize to a target divisor")
        normal_form = short_certificate.type_i_normal_form_from_target_divisor(prime, gap, factor)
        if normal_form is None:
            raise AssertionError("normalized even-source tail lacks a Type I normal form")
        overflow = short_certificate.target_divisor_overflow_factor(x, factor)
        if overflow != normal_form[1]:
            raise AssertionError("normal-form overflow is inconsistent")
        rows.append(
            {
                "tail_factor": factor,
                "gap": gap,
                "x": x,
                "overflow": overflow,
                "normal_form": list(normal_form),
            }
        )
    if not rows:
        raise AssertionError("stored small-r tail state has no factors")
    return sorted(rows, key=lambda row: (int(row["overflow"]), int(row["gap"]), int(row["tail_factor"])))


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Profile the minimum target-divisor overflow at each first small-r state."""
    records = []
    for record in payload["records"]:
        prime = int(record["prime"])
        selected = record["first_small_r_tail_hit"]
        if selected is None:
            raise AssertionError("profile input must close every pressure point")
        r = int(selected["r"])
        m1 = int(selected["m1"])
        rows = tail_rows(prime, r, m1)
        minimum = int(rows[0]["overflow"])
        records.append(
            {
                "prime": prime,
                "r": r,
                "m1": m1,
                "tail_factor_count": len(rows),
                "minimum_overflow": minimum,
                "minimum_overflow_rows": [row for row in rows if int(row["overflow"]) == minimum],
                "all_overflows": [int(row["overflow"]) for row in rows],
            }
        )
    return {
        "arithmetic": (
            "exact M1-squared divisor-residue enumeration, followed by the exact map "
            "e -> gap=(4e+1)/r and Type I normal-form overflow B=e/gcd(e,x)"
        ),
        "scope_note": (
            "A finite overflow profile of the four stored small-r pressure witnesses. "
            "It does not establish a variable-r or bounded-overflow selector generally."
        ),
        "prime_limit": payload["prime_limit"],
        "pressure_point_count": len(records),
        "all_minimum_overflows_are_one": all(record["minimum_overflow"] == 1 for record in records),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
