#!/usr/bin/env python3
"""Audit whether a minimal-offset shifted ray can use an ordinary tail factor."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
TARGETED_DESCENT = ROOT / "reproductions" / "type_ii_h19_targeted_quadratic_descent.py"
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-200m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-square-necessity-200m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("tail_shifted_square_short_certificate", SHORT_CERTIFICATE)
targeted_descent = load_module("tail_shifted_square_targeted_descent", TARGETED_DESCENT)


def factor_exponents(values: tuple[int, ...], spf) -> dict[int, int]:
    """Factor a product whose individual factors are covered by the SPF facade."""
    exponents: dict[int, int] = {}
    for value in values:
        while value > 1:
            prime = spf[value]
            exponents[prime] = exponents.get(prime, 0) + 1
            value //= prime
    return exponents


def exponent_upgrade_profile(factor: int, L_exponents: dict[int, int]) -> tuple[int, int, int]:
    """Measure how many exponents exceed those available in an ordinary L divisor."""
    remaining = factor
    excess = 0
    upgraded_primes = 0
    support = 0
    for prime, exponent in L_exponents.items():
        used = 0
        while remaining % prime == 0:
            remaining //= prime
            used += 1
        if used:
            support += 1
        if used > exponent:
            excess += used - exponent
            upgraded_primes += 1
    if remaining != 1:
        raise AssertionError("square-tail factor has a prime outside L")
    return excess, upgraded_primes, support


def tail_factors(prime: int, shift: int, k: int, spf) -> list[dict[str, int]]:
    """Enumerate the normalized square tails for one compatible (shift, k)."""
    q = 4 * k - 1
    if q % shift:
        return []
    source = (q * prime + shift) // (q + 1)
    if (q + 1) * source != q * prime + shift or source % shift:
        raise AssertionError("minimal-offset ray failed source normalization")
    t = q // shift
    tail_source = source // shift
    L = k * tail_source
    L_exponents = factor_exponents((k, tail_source), spf)
    results = []
    for factor in short_certificate.positive_divisors_square_product_from_spf(k, tail_source, spf):
        if factor > L or (L + factor) % t:
            continue
        if (L + L * L // factor) % t:
            raise AssertionError("normalized first tail congruence must force its companion")
        u = (L + factor) // t
        v = L * u // factor
        gap = (4 * factor + 1) // t
        if (
            (4 * factor + 1) % t
            or 4 * u - prime != gap
            or u * u % factor
            or not 3 <= gap <= prime - 2
        ):
            raise AssertionError("normalized tail did not reconstruct a Type I certificate")
        certificate = short_certificate.GapCertificate(
            prime, "I", gap, u, u * u // factor, v, prime * L
        )
        if not short_certificate.verify_certificate(certificate):
            raise AssertionError("normalized tail certificate did not verify")
        if (
            Fraction(4, source)
            != Fraction(1, shift * L) + Fraction(1, u) + Fraction(1, v)
            or Fraction(4, prime)
            != Fraction(1, prime * L) + Fraction(1, u) + Fraction(1, v)
        ):
            raise AssertionError("normalized tail lift did not verify")
        exponent_excess, upgraded_primes, prime_support = exponent_upgrade_profile(factor, L_exponents)
        results.append(
            {
                "k": k,
                "source_distance": prime - source,
                "t": t,
                "L": L,
                "factor": factor,
                "gap": gap,
                "ordinary_tail_factor": L % factor == 0,
                "exponent_excess_over_L": exponent_excess,
                "upgraded_prime_count": upgraded_primes,
                "prime_support_count": prime_support,
            }
        )
    return results


def ray_profile(prime: int, shift: int, spf) -> dict[str, object]:
    """Exhaust every k for the minimal offset, separating f|L from f|L^2 only."""
    base = (prime - shift) // 4
    factors: list[dict[str, int]] = []
    k_count = 0
    for k in short_certificate.positive_divisors_from_spf(base, spf):
        if (4 * k - 1) % shift:
            continue
        k_count += 1
        factors.extend(tail_factors(prime, shift, k, spf))
    if not factors:
        raise AssertionError("stored minimal offset has no complete square-tail witness")
    ordinary = [entry for entry in factors if entry["ordinary_tail_factor"]]
    minimum_excess = min(entry["exponent_excess_over_L"] for entry in factors)
    minimum_support = min(entry["prime_support_count"] for entry in factors)
    return {
        "prime": prime,
        "minimal_offset": shift,
        "compatible_k_count": k_count,
        "complete_square_tail_witness_count": len(factors),
        "ordinary_tail_witness_count": len(ordinary),
        "square_tail_essential_at_minimal_offset": not ordinary,
        "minimum_exponent_excess_over_L": minimum_excess,
        "minimum_excess_witness": next(
            entry for entry in factors if entry["exponent_excess_over_L"] == minimum_excess
        ),
        "minimum_prime_support_count": minimum_support,
        "minimum_support_witness": next(
            entry for entry in factors if entry["prime_support_count"] == minimum_support
        ),
        "first_complete_witness": factors[0],
        "first_ordinary_witness": ordinary[0] if ordinary else None,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    records_in = payload["records"]
    primes = [int(record["prime"]) for record in records_in]
    if not primes:
        raise ValueError("input profile has no offset records")
    spf = targeted_descent.TrialSmallestFactors(max(primes))
    records = []
    for record in records_in:
        witness = record["offset_descent"]
        if witness is None:
            raise ValueError("input profile must be closed before square-necessity audit")
        records.append(ray_profile(int(record["prime"]), int(witness["shift"]), spf))
    essential = [record["prime"] for record in records if record["square_tail_essential_at_minimal_offset"]]
    essential_records = [record for record in records if record["square_tail_essential_at_minimal_offset"]]
    exponent_histogram = Counter(
        int(record["minimum_exponent_excess_over_L"]) for record in essential_records
    )
    support_histogram = Counter(
        int(record["minimum_prime_support_count"]) for record in essential_records
    )
    multi_upgrade = [
        record["prime"]
        for record in essential_records
        if int(record["minimum_exponent_excess_over_L"]) > 1
    ]
    four_support = [
        record["prime"]
        for record in essential_records
        if int(record["minimum_prime_support_count"]) >= 4
    ]
    return {
        "arithmetic": (
            "complete enumeration of every k compatible with each stored minimal offset, "
            "complete normalized f | L^2 tail enumeration, and exact certificate/lift checks"
        ),
        "scope_note": (
            "This proves square-tail necessity only at each stored minimal offset. A larger "
            "offset may still have an ordinary f | L tail."
        ),
        "prime_limit": payload["prime_limit"],
        "pressure_point_count": len(records),
        "minimal_offset_rays_with_ordinary_tail_count": len(records) - len(essential),
        "square_tail_essential_at_minimal_offset_count": len(essential),
        "square_tail_essential_at_minimal_offset_primes": essential,
        "square_essential_minimum_exponent_excess_histogram": {
            str(exponent): count for exponent, count in sorted(exponent_histogram.items())
        },
        "square_essential_multi_upgrade_primes": multi_upgrade,
        "square_essential_minimum_prime_support_histogram": {
            str(support): count for support, count in sorted(support_histogram.items())
        },
        "square_essential_four_support_primes": four_support,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
