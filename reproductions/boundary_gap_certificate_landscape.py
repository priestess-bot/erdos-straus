#!/usr/bin/env python3
"""Enumerate every short-gap certificate at one specified prime.

The input values are deliberately factored by trial division.  The intended
boundary point has first denominators near 1.2e8, whose square-root is small;
this keeps the finite audit independent of a global smallest-prime-factor
table.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
DEFAULT_PRIME = 477_015_289
DEFAULT_GAP_CAP = 27
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-boundary-gap-27-landscape-477015289-results.json"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "boundary_gap_certificate_landscape_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def factor_by_trial_division(value: int) -> dict[int, int]:
    """Return the prime factorization of a positive integer in sorted order."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: dict[int, int] = {}
    while value % 2 == 0 and value > 1:
        factors[2] = factors.get(2, 0) + 1
        value //= 2
    divisor = 3
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor += 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def divisors_of_square(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            base * prime**power
            for base in divisors
            for power in range(2 * exponent + 1)
        ]
    return sorted(divisors)


def gap_landscape(prime: int, gap: int) -> dict[str, object]:
    if prime % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= prime - 2:
        raise ValueError("prime and gap are outside the Type I/II natural range")
    x = (prime + gap) // 4
    if 4 * x != prime + gap:
        raise AssertionError("first denominator was not integral")
    factors = factor_by_trial_division(x)
    square_divisors = divisors_of_square(factors)
    type_i: list[dict[str, object]] = []
    type_ii_divisors: list[int] = []
    for divisor in square_divisors:
        if (prime * x + divisor) % gap == 0:
            normal = short_certificate.type_i_normal_form(prime, gap, divisor)
            if normal is None:
                raise AssertionError("Type I residue did not normalize")
            A, B, C = normal
            certificate = short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
            if certificate is None or certificate.divisor != divisor:
                raise AssertionError("Type I normal form did not recover its certificate")
            witness = short_certificate.type_i_normal_tail_deflation_witness(prime, gap, A, B)
            R = (4 * B * B * C + 1) // gap
            if gap * R != 4 * B * B * C + 1:
                raise AssertionError("normal quotient was not integral")
            type_i.append(
                {
                    "divisor": divisor,
                    "normal_form": [A, B, C],
                    "tail_quotient": R,
                    "tail_condition_remainder": (4 * B * C * (A + B)) % (R + 1),
                    "normal_tail_deflation": None
                    if witness is None
                    else {
                        "source_denominator": witness.source_denominator,
                        "source_solution": list(witness.source_solution),
                    },
                }
            )
        if divisor <= x and (x + divisor) % gap == 0:
            y = prime * (x + divisor) // gap
            numerator = prime * (x + x * x // divisor)
            if numerator % gap:
                raise AssertionError("Type II congruence did not recover its denominator")
            certificate = short_certificate.GapCertificate(
                prime, "II", gap, x, divisor, y, numerator // gap
            )
            if not short_certificate.verify_certificate(certificate):
                raise AssertionError("Type II residue did not recover a certificate")
            type_ii_divisors.append(divisor)
    return {
        "gap": gap,
        "first_denominator": x,
        "factorization": {str(prime): exponent for prime, exponent in factors.items()},
        "square_divisor_count": len(square_divisors),
        "type_i": type_i,
        "type_ii_divisors": type_ii_divisors,
    }


def run_scan(prime: int = DEFAULT_PRIME, gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    gaps = [gap_landscape(prime, gap) for gap in range(3, gap_cap + 1, 4)]
    first_nonempty = next(
        (
            entry["gap"]
            for entry in gaps
            if entry["type_i"] or entry["type_ii_divisors"]
        ),
        None,
    )
    return {
        "arithmetic": (
            "factor every x=(p+m)/4 by trial division; enumerate every d|x^2; "
            "test the exact Type I congruence m|(p*x+d), the exact Type II "
            "congruence m|(x+d) with d<=x, and the established normal-tail "
            "strict-deflation condition for each Type I normal form"
        ),
        "scope_note": (
            "This is a complete finite scan only for the listed prime and gaps "
            "m<=gap_cap. A null normal-tail deflation excludes only the "
            "preserve-first-two-terms p-tail shape."
        ),
        "prime": prime,
        "gap_cap": gap_cap,
        "first_certificate_gap": first_nonempty,
        "gaps": gaps,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=DEFAULT_PRIME)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_scan(args.prime, args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
