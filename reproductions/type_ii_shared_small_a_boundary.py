#!/usr/bin/env python3
"""Exhaustively rule out small-A shared Type II certificates for p=878089."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "type_ii_shared_small_a_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()
BOUNDARY_PRIME = 878_089


def all_shared_normal_forms(prime: int) -> tuple[dict[str, int], ...]:
    """Enumerate every shared-gap Type II normal form at every legal gap."""
    if prime % 24 != 1 or prime < 73:
        raise ValueError("prime must be a core prime at least 73")
    if prime not in short_certificate.primes_up_to(prime):
        raise ValueError("prime must be prime")
    spf = short_certificate.smallest_prime_factors(2 * prime - 2)
    forms = set()
    for gap in range(3, prime - 1, 4):
        x = (prime + gap) // 4
        shared_divisors = [
            divisor
            for divisor in short_certificate.positive_divisors_from_spf(
                prime + gap, spf
            )
            if divisor > 1 and divisor % gap == 1
        ]
        if not shared_divisors:
            continue
        for candidate in short_certificate.divisors_of_square(x, spf):
            if candidate % gap != (-x) % gap:
                continue
            divisor = min(candidate, x * x // candidate)
            normal = short_certificate.type_ii_normal_form(prime, gap, divisor)
            if normal is None:
                raise AssertionError("target divisor did not normalize")
            a, b, c = normal
            for shared_divisor in shared_divisors:
                forms.add(
                    (
                        gap,
                        shared_divisor,
                        divisor,
                        a,
                        b,
                        c,
                        (a + b) // gap,
                    )
                )
    return tuple(
        {
            "gap": gap,
            "shared_divisor": shared_divisor,
            "certificate_divisor": divisor,
            "a": a,
            "b": b,
            "c": c,
            "k": k,
        }
        for gap, shared_divisor, divisor, a, b, c, k in sorted(forms)
    )


def boundary_profile() -> dict[str, object]:
    """Return the exhaustive p=878089 shared-selector small-A boundary."""
    forms = all_shared_normal_forms(BOUNDARY_PRIME)
    if not forms:
        raise AssertionError("the boundary prime must have shared certificates")
    direct = short_certificate.type_ii_factor_certificate(
        BOUNDARY_PRIME, 1, 1, 33
    )
    if direct is None:
        raise AssertionError("the direct A=C=1 certificate did not construct")
    direct_normal = short_certificate.type_ii_normal_form(
        BOUNDARY_PRIME, direct.gap, direct.divisor
    )
    if direct_normal != (1, 221_198, 1):
        raise AssertionError("the direct certificate normalized unexpectedly")
    return {
        "prime": BOUNDARY_PRIME,
        "gap_count": len({entry["gap"] for entry in forms}),
        "normal_form_count": len(forms),
        "minimum_a": min(int(entry["a"]) for entry in forms),
        "forms": forms,
        "direct_a_one_certificate": {
            "gap": direct.gap,
            "divisor": direct.divisor,
            "a": direct_normal[0],
            "b": direct_normal[1],
            "c": direct_normal[2],
            "k": 33,
            "ray_factor": 131,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print(json.dumps(boundary_profile(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
