#!/usr/bin/env python3
"""Verify the exact translation between Chamberland forms and AC Type II rays."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "chamberland-ac-ray-translation-results.json"
RAY_SCRIPT = ROOT / "reproductions" / "type_ii_ac_ray.py"


def load_ray_script():
    spec = importlib.util.spec_from_file_location(
        "chamberland_ac_ray_translation_ray", RAY_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_ac_ray.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ray = load_ray_script()


def from_chamberland(q: int, r: int, s1: int, s2: int) -> dict[str, int]:
    """Translate a valid Chamberland form into its AC-ray coordinates."""
    if min(q, r, s1, s2) < 1 or q % 4 != 3:
        raise ValueError("require positive data with q congruent to 3 modulo 4")
    quotient = (q + 1) // 4
    if 4 * quotient != q + 1 or quotient % s1 or quotient % s2:
        raise ValueError("s1 and s2 must divide (q+1)/4")
    a = math.gcd(s1, s2)
    lcm = math.lcm(s1, s2)
    c = lcm // a
    k = quotient // lcm
    p = q * r - 4 * s1 * s2
    b = k * r - a
    if (a * a * c, a * c) != (s1 * s2, lcm):
        raise AssertionError("gcd/lcm conversion lost the divisor pair")
    if q != 4 * a * c * k - 1 or p != q * r - 4 * a * a * c:
        raise AssertionError("Chamberland form did not become an AC ray")
    if q * b != k * p + a:
        raise AssertionError("AC-ray quotient identity failed")
    return {
        "p": p,
        "q": q,
        "r": r,
        "s1": s1,
        "s2": s2,
        "a": a,
        "c": c,
        "k": k,
        "b": b,
    }


def to_chamberland(p: int, a: int, c: int, k: int, q: int) -> dict[str, int]:
    """Translate a successful AC factor ray to a nested Chamberland divisor pair."""
    if min(p, a, c, k, q) < 1 or q != 4 * a * c * k - 1:
        raise ValueError("invalid positive AC ray generator")
    shifted = p + 4 * a * a * c
    if shifted % q:
        raise ValueError("q must divide p+4*A^2*C")
    r = shifted // q
    s1, s2 = a, a * c
    if ((q + 1) // 4) % s1 or ((q + 1) // 4) % s2:
        raise AssertionError("nested pair does not divide (q+1)/4")
    translated = from_chamberland(q, r, s1, s2)
    if (translated["p"], translated["a"], translated["c"], translated["k"]) != (
        p,
        a,
        c,
        k,
    ):
        raise AssertionError("AC-to-Chamberland round trip failed")
    return translated


def run_audit(limit: int = 10_000, ac_bound: int = 14) -> dict[str, object]:
    """Audit every bounded-AC witness in a small exact core-prime range."""
    result = ray.run_experiment(limit, ac_bound)
    spf = ray.short_certificate.smallest_prime_factors(limit + 4 * ac_bound**3)
    records = []
    for prime in ray.short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        witness = ray.ray_witness(prime, ac_bound, spf)
        if witness is None:
            raise AssertionError("the selected finite box unexpectedly missed a core prime")
        a, c, k, q, certificate = witness
        translated = to_chamberland(prime, a, c, k, q)
        if translated["b"] < a:
            raise AssertionError("finite audit witness did not satisfy the AC order condition")
        if Fraction(4, prime) != sum(
            (Fraction(1, value) for value in (certificate.x, certificate.y, certificate.z)),
            Fraction(),
        ):
            raise AssertionError("translated ray certificate failed exact verification")
        records.append(translated)
    return {
        "arithmetic": (
            "exact gcd/lcm translation of divisor pairs and fractions.Fraction "
            "verification of every reconstructed Type II certificate"
        ),
        "scope_note": (
            "The algebraic translation is general. The finite audit only checks "
            "the stated bounded-AC witness sample and does not prove ray saturation."
        ),
        "prime_limit": limit,
        "ac_bound": ac_bound,
        "core_prime_count": result["core_prime_count"],
        "translated_witness_count": len(records),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000)
    parser.add_argument("--ac-bound", type=int, default=14)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.ac_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
