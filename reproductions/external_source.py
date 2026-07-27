#!/usr/bin/env python3
"""Finite audit of external-source Type I certificates.

The experiment first removes four rigorously proved direct families: m=3,
(p+1)/2, p+4, and 4p+1. It then searches the remaining core primes using
the external-source condition with 1 <= i <= source_limit. This is an exact
finite computation, not evidence for a uniform source bound.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "external-source-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location("short_certificate", SHORT_CERTIFICATE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def factorize(value: int, trial_primes: list[int]) -> list[tuple[int, int]]:
    """Return the prime factorization by trial division from a precomputed list."""
    if value <= 0:
        raise ValueError("factorization input must be positive")
    factors: list[tuple[int, int]] = []
    for prime in trial_primes:
        if prime * prime > value:
            break
        if value % prime:
            continue
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        factors.append((prime, exponent))
    if value > 1:
        factors.append((value, 1))
    return factors


def divisors(value: int, trial_primes: list[int]) -> list[int]:
    result = [1]
    for prime, exponent in factorize(value, trial_primes):
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return sorted(result)


def first_prime_factor_in_class(
    value: int, modulus: int, residue: int, trial_primes: list[int]
) -> int | None:
    for prime, _ in factorize(value, trial_primes):
        if prime % modulus == residue:
            return prime
    return None


def covered_by_direct_families(p: int, trial_primes: list[int]) -> bool:
    if first_prime_factor_in_class((p + 1) // 2, 4, 3, trial_primes) is not None:
        return True
    if first_prime_factor_in_class(p + 4, 4, 3, trial_primes) is not None:
        return True
    if first_prime_factor_in_class((p + 3) // 4, 3, 2, trial_primes) is not None:
        return True
    q = first_prime_factor_in_class(4 * p + 1, 4, 3, trial_primes)
    return q is not None and short_certificate.four_p_plus_one_type_ii_certificate(p, q) is not None


def smallest_external_source_witness(
    p: int, source_limit: int, trial_primes: list[int]
) -> tuple[int, int] | None:
    for source in range(1, source_limit + 1):
        for gap in divisors(p + source, trial_primes):
            certificate = short_certificate.external_source_type_i_certificate(p, source, gap)
            if certificate is not None:
                return source, gap
    return None


def external_source_factor_ray_normal_form(
    p: int, source: int, gap: int
) -> dict[str, int] | None:
    """Normalize an external-source witness as a divisor of r*p+1."""
    certificate = short_certificate.external_source_type_i_certificate(
        p, source, gap
    )
    if certificate is None:
        return None
    quotient = (p + source) // gap
    if (p + gap) % (4 * source):
        raise AssertionError("external-source witness lost its tail quotient")
    tail = (p + gap) // (4 * source)
    if (quotient + 1) % source:
        raise AssertionError("external-source factor ray failed to recover r")
    ray_multiplier = (quotient + 1) // source
    if (
        ray_multiplier % 4 != 3
        or ray_multiplier * p + 1 != 4 * quotient * tail
    ):
        raise AssertionError("external-source factor ray did not reconstruct")
    return {
        "source": source,
        "gap": gap,
        "q": quotient,
        "r": ray_multiplier,
        "t": tail,
    }


def external_source_factor_ray_witness(
    p: int, ray_multiplier: int, quotient: int
) -> dict[str, int] | None:
    """Recover an external-source witness from 4*q*t = r*p+1."""
    if (
        p % 24 != 1
        or ray_multiplier < 3
        or ray_multiplier % 4 != 3
        or quotient < 1
        or (quotient + 1) % ray_multiplier
        or (ray_multiplier * p + 1) % (4 * quotient)
    ):
        return None
    source = (quotient + 1) // ray_multiplier
    gap_numerator = p + source
    if gap_numerator % quotient:
        raise AssertionError("factor-ray congruences did not force the gap")
    gap = gap_numerator // quotient
    certificate = short_certificate.external_source_type_i_certificate(
        p, source, gap
    )
    if certificate is None:
        return None
    return {
        "source": source,
        "gap": gap,
        "q": quotient,
        "r": ray_multiplier,
        "t": (ray_multiplier * p + 1) // (4 * quotient),
    }


def run_experiment(limit: int, source_limit: int) -> dict[str, object]:
    if limit < 73 or source_limit < 1:
        raise ValueError("limit must be at least 73 and source_limit must be positive")
    trial_primes = short_certificate.primes_up_to(math.isqrt(4 * limit + source_limit) + 1)
    core_primes = [p for p in short_certificate.primes_up_to(limit) if p % 24 == 1]
    residual = [p for p in core_primes if not covered_by_direct_families(p, trial_primes)]

    witnesses: dict[int, tuple[int, int]] = {}
    missing: list[int] = []
    records: list[dict[str, int]] = []
    largest_source = 0
    for prime in residual:
        witness = smallest_external_source_witness(prime, source_limit, trial_primes)
        if witness is None:
            missing.append(prime)
            continue
        source, gap = witness
        if source > largest_source:
            largest_source = source
            records.append({"prime": prime, "source": source, "gap": gap})
        witnesses[prime] = witness

    return {
        "arithmetic": "exact integer factorization by trial division and fractions.Fraction certificate verification",
        "scope_note": "A finite source-window experiment. Missing values do not refute the conjecture; covered values do not prove a uniform source bound.",
        "prime_limit": limit,
        "source_limit": source_limit,
        "direct_families": ["m=3", "(p+1)/2", "p+4", "4p+1"],
        "core_prime_count": len(core_primes),
        "residual_after_direct_families": len(residual),
        "external_source_certified_count": len(witnesses),
        "external_source_missing": missing,
        "largest_minimal_source_found": largest_source if witnesses else None,
        "source_records": records,
        "sample_witnesses": [
            {"prime": prime, "source": source, "gap": gap}
            for prime, (source, gap) in list(witnesses.items())[:10]
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--source-limit", type=int, default=128)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_experiment(args.limit, args.source_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
