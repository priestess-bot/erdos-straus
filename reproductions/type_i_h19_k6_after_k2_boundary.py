#!/usr/bin/env python3
"""Audit terminal k=6 mixed-factor edges after the exact k=2 H19 boundary."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
K2 = ROOT / "reproductions" / "type-i-k2-mod7-even-source-audit-1b-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-k6-after-k2-boundary-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("h19_k6_short_certificate", SHORT_CERTIFICATE)


def divisors(factors: dict[int, int]) -> list[int]:
    result = [1]
    for factor, exponent in factors.items():
        result = [value * factor**power for value in result for power in range(exponent + 1)]
    return sorted(result)


def witness(prime: int, source: int, g: int) -> dict[str, int]:
    k, q = 6, 23
    if source % 2 or g > source or (6 * source) % g or g % q != q - 1:
        raise AssertionError("invalid k=6 mixed divisor")
    u = k * (source + g) // q
    v = source * u // g
    gap = (4 * k * g + 1) // q
    divisor = u * u // (k * g)
    certificate = short_certificate.GapCertificate(prime, "I", gap, u, divisor, v, k * source * prime)
    if not short_certificate.verify_certificate(certificate):
        raise AssertionError("k=6 certificate did not verify")
    if Fraction(4, source) != Fraction(1, k * source) + Fraction(1, u) + Fraction(1, v):
        raise AssertionError("k=6 source identity did not verify")
    if Fraction(4, prime) != Fraction(1, k * source * prime) + Fraction(1, u) + Fraction(1, v):
        raise AssertionError("k=6 target identity did not verify")
    return {"source_denominator": source, "mixed_divisor": g, "k": k, "q": q, "gap": gap, "certificate_divisor": divisor}


def run_audit(k2: dict[str, object]) -> dict[str, object]:
    boundary = [int(value) for value in k2["proper_divisor_residue_misses"]]
    if len(boundary) != 119:
        raise AssertionError("input is not the exact 119-point k=2 boundary")
    records, misses = [], []
    for prime in boundary:
        source = (23 * prime + 1) // 24
        if 24 * source != 23 * prime + 1 or source % 2:
            raise AssertionError("k=6 source was not terminal even")
        factors = {int(p): int(e) for p, e in sympy.factorint(6 * source).items()}
        candidates = [g for g in divisors(factors) if g <= source and g % 23 == 22]
        if not candidates:
            misses.append(prime)
        else:
            records.append({"prime": prime, "certificate": witness(prime, source, candidates[0])})
    return {
        "arithmetic": "for every exact k=2 subgroup-boundary prime, enumerate all g|6n with g<=n and g=-1 (mod 23), then verify the terminal even-source Type I certificate exactly",
        "scope_note": "A finite second-scale audit after the exact k=2 boundary; misses rule out k=6 only, not other scales or the conjecture.",
        "input_k2_subgroup_boundary_count": len(boundary),
        "k6_terminal_count": len(records),
        "k6_misses": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k2", type=Path, default=K2)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.k2.read_text(encoding="utf-8")))
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
