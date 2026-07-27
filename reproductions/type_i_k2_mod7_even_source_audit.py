#!/usr/bin/env python3
"""Audit the terminal k=2, q=7 divisor-residue external-source corollary."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
H19 = ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-k2-mod7-even-source-audit-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("k2_mod7_short_certificate", SHORT_CERTIFICATE)
QUADRATIC_RESIDUES_MOD_7 = {1, 2, 4}


def positive_divisors(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for factor, exponent in factors.items():
        divisors = [
            divisor * int(factor) ** power
            for divisor in divisors
            for power in range(int(exponent) + 1)
        ]
    return sorted(divisors)


def terminal_factor_certificate(prime: int, factor: int) -> dict[str, int] | None:
    """Build the k=2 terminal edge from a proper n-divisor congruent to 3 modulo 7."""
    if prime % 48 != 25 or factor <= 1 or factor % 7 != 3:
        return None
    source = (7 * prime + 1) // 8
    if 8 * source != 7 * prime + 1 or source % 2 or source % factor or factor >= source:
        return None
    # Every proper divisor is at most source/2, hence g=2*factor <= source.
    if 2 * factor > source:
        raise AssertionError("proper factor did not make the mixed divisor small enough")
    g = 2 * factor
    multiplier = 2
    q = 7
    if g % q != q - 1:
        raise AssertionError("mixed divisor did not have the required q residue")
    u = multiplier * (source + g) // q
    if q * u != multiplier * (source + g):
        raise AssertionError("first source-tail denominator was not integral")
    v = source * u // g
    if g * v != source * u:
        raise AssertionError("second source-tail denominator was not integral")
    gap = (4 * multiplier * g + 1) // q
    divisor = u * u // (multiplier * g)
    certificate = short_certificate.GapCertificate(
        prime, "I", gap, u, divisor, v, multiplier * source * prime
    )
    if not short_certificate.verify_certificate(certificate):
        raise AssertionError("terminal k=2 certificate did not verify")
    if Fraction(4, source) != Fraction(1, multiplier * source) + Fraction(1, u) + Fraction(1, v):
        raise AssertionError("source identity did not verify")
    if Fraction(4, prime) != Fraction(1, multiplier * source * prime) + Fraction(1, u) + Fraction(1, v):
        raise AssertionError("target identity did not verify")
    return {
        "source_denominator": source,
        "terminal_factor": factor,
        "mixed_divisor": g,
        "k": multiplier,
        "q": q,
        "source_terms": [multiplier * source, u, v],
        "gap": gap,
        "certificate_divisor": divisor,
    }


def run_audit(h19: dict[str, object]) -> dict[str, object]:
    """Apply the proper-divisor k=2 corollary to the stored H19 residuals."""
    records: list[dict[str, object]] = []
    residue_candidates = 0
    residue_misses: list[int] = []
    for profile in h19["profiles"]:
        prime = int(profile["prime"])
        if prime % 48 != 25:
            continue
        residue_candidates += 1
        source = (7 * prime + 1) // 8
        factors = {int(factor): int(exponent) for factor, exponent in sympy.factorint(source).items()}
        divisors = positive_divisors(factors)
        witness = None
        for factor in sorted(divisors):
            witness = terminal_factor_certificate(prime, int(factor))
            if witness is not None:
                break
        two_source_factors = dict(factors)
        two_source_factors[2] = two_source_factors.get(2, 0) + 1
        full_mixed = [
            divisor
            for divisor in positive_divisors(two_source_factors)
            if divisor <= source and divisor % 7 == 6
        ]
        nonquadratic_factors = sorted(
            factor for factor in factors if factor % 7 not in QUADRATIC_RESIDUES_MOD_7
        )
        if bool(witness) != bool(full_mixed) or bool(witness) != bool(nonquadratic_factors):
            raise AssertionError("k=2 divisor, full mixed, and residue-factor criteria diverged")
        if witness is None:
            residue_misses.append(prime)
        else:
            records.append(
                {
                    "prime": prime,
                    "nonquadratic_prime_factor": nonquadratic_factors[0],
                    "least_full_mixed_divisor": full_mixed[0],
                    "certificate": witness,
                }
            )
    return {
        "arithmetic": (
            "for every stored H19 residual p=25 (mod 48), factor n=(7p+1)/8 exactly; "
            "enumerate its proper divisors and all g|2n; verify that the k=2, q=7 mixed-factor "
            "condition is equivalent to one prime factor outside {1,2,4} (mod 7), then reconstruct "
            "the terminal Type I certificate with rational verification"
        ),
        "scope_note": (
            "A finite audit of the exact k=2 divisor-residue criterion. Its misses rule out every "
            "mixed divisor at this fixed scale, but do not refute other external scales or the conjecture."
        ),
        "prime_limit": h19["prime_limit"],
        "h19_source_free_count": len(h19["profiles"]),
        "p_eq_25_mod_48_count": residue_candidates,
        "proper_divisor_terminal_count": len(records),
        "proper_divisor_residue_misses": residue_misses,
        "all_k2_mixed_terminal_count": len(records),
        "quadratic_residue_only_k2_miss_count": len(residue_misses),
        "single_prime_terminal_count": sum(
            any(int(factor) % 7 == 3 for factor in sympy.factorint((7 * int(record["prime"]) + 1) // 8))
            for record in records
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h19", type=Path, default=H19)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.h19.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
