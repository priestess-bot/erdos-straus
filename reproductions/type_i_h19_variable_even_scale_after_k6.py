#!/usr/bin/env python3
"""Exhaust the terminal even-source mixed-factor family after the H19 k=2,6 boundary.

For each retained prime p, every integral affine source of this form is indexed by
k | (p-1)/4:

    q = 4k-1,  n = (q*p+1)/(4k).

The script considers every such k for which n is even, then every mixed divisor
g | k*n with g <= n and g == -1 (mod q).  A hit is reconstructed as a Type I
certificate and checked with exact rational arithmetic.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
K6 = ROOT / "reproductions" / "type-i-h19-k6-after-k2-boundary-1b-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-variable-even-scale-after-k6-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("h19_variable_scale_short_certificate", SHORT_CERTIFICATE)


def divisors(factors: dict[int, int]) -> list[int]:
    result = [1]
    for factor, exponent in factors.items():
        result = [value * factor**power for value in result for power in range(exponent + 1)]
    return sorted(result)


def witness(prime: int, k: int, source: int, g: int) -> dict[str, int]:
    q = 4 * k - 1
    if (
        k <= 0
        or source % 2
        or 4 * k * source != q * prime + 1
        or g > source
        or (k * source) % g
        or g % q != q - 1
    ):
        raise AssertionError("invalid mixed-factor even-source candidate")
    u = k * (source + g) // q
    v = source * u // g
    gap = (4 * k * g + 1) // q
    divisor = u * u // (k * g)
    certificate = short_certificate.GapCertificate(prime, "I", gap, u, divisor, v, k * source * prime)
    if not short_certificate.verify_certificate(certificate):
        raise AssertionError("variable-scale certificate did not verify")
    if Fraction(4, source) != Fraction(1, k * source) + Fraction(1, u) + Fraction(1, v):
        raise AssertionError("source identity did not verify")
    if Fraction(4, prime) != Fraction(1, k * source * prime) + Fraction(1, u) + Fraction(1, v):
        raise AssertionError("target identity did not verify")
    return {
        "source_denominator": source,
        "mixed_divisor": g,
        "k": k,
        "q": q,
        "gap": gap,
        "certificate_divisor": divisor,
    }


def run_audit(k6: dict[str, object]) -> dict[str, object]:
    boundary = [int(value) for value in k6["k6_misses"]]
    if len(boundary) != 71:
        raise AssertionError("input is not the exact 71-point k=2,6 boundary")
    records, misses = [], []
    for prime in boundary:
        if prime % 48 != 25:
            raise AssertionError("boundary prime left p=25 (mod 48)")
        scales = divisors({int(factor): int(exponent) for factor, exponent in sympy.factorint((prime - 1) // 4).items()})
        eligible_scales = []
        candidates = []
        for k in scales:
            q = 4 * k - 1
            source = (q * prime + 1) // (4 * k)
            if 4 * k * source != q * prime + 1:
                raise AssertionError("scale divisor did not give an integral source")
            if source % 2:
                continue
            eligible_scales.append(k)
            factors = {int(factor): int(exponent) for factor, exponent in sympy.factorint(k * source).items()}
            candidates.extend((k, source, g) for g in divisors(factors) if g <= source and g % q == q - 1)
        if candidates:
            k, source, g = min(candidates, key=lambda item: (item[0], item[2]))
            records.append(
                {
                    "prime": prime,
                    "eligible_even_scale_count": len(eligible_scales),
                    "candidate_count": len(candidates),
                    "certificate": witness(prime, k, source, g),
                }
            )
        else:
            misses.append({"prime": prime, "eligible_even_scales": eligible_scales})
    return {
        "arithmetic": (
            "for every prime on the exact k=2,6 boundary, enumerate every k|(p-1)/4 whose "
            "affine source n=((4k-1)p+1)/(4k) is even, then every g|kn with g<=n and "
            "g=-1 (mod 4k-1); reconstruct each selected terminal Type I certificate exactly"
        ),
        "scope_note": (
            "This is exhaustive only for the indicated terminal even-source affine mixed-factor family. "
            "A miss excludes every scale in that family for the listed finite input, not other descent "
            "mechanisms or the conjecture."
        ),
        "input_k2_k6_boundary_count": len(boundary),
        "variable_even_scale_terminal_count": len(records),
        "variable_even_scale_miss_count": len(misses),
        "variable_even_scale_misses": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k6", type=Path, default=K6)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.k6.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
