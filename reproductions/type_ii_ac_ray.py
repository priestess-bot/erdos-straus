#!/usr/bin/env python3
"""Exact finite audit of Type II rays with bounded A,C and unbounded K.

For fixed positive A,C, put h=4*A*C*K-1. The Type II generator condition
h | K*p+A is equivalent to h | p+4*A*A*C, with K=(h+1)/(4*A*C).
Thus all possible K values can be enumerated by factoring the small shifts
p+4*A*A*C. This is finite evidence only; it does not prove a global A,C
bound.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-ac-ray-results.json"
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


def bounded_k_avoidance_modulus(
    ac_pairs: tuple[tuple[int, int], ...], k_bound: int
) -> int:
    """Return a CRT modulus that excludes every listed ray with K <= bound.

    For p == 1 modulo this modulus, h=4*A*C*K-1 divides the modulus and
    K*p+A is congruent to K+A modulo h. Since 0 < K+A < h, no listed
    generator can succeed. Linnik's theorem can then choose such a prime
    with quantitative size control; this routine implements only the exact
    finite algebraic part of that argument.
    """
    if not ac_pairs or k_bound < 1:
        raise ValueError("ac_pairs must be nonempty and k_bound must be positive")
    modulus = 24
    for a, c in ac_pairs:
        if a < 1 or c < 1:
            raise ValueError("A and C must be positive")
        for k in range(1, k_bound + 1):
            modulus = math.lcm(modulus, 4 * a * c * k - 1)
    return modulus


def divisors(value: int, spf: list[int]) -> list[int]:
    """Return all positive divisors using an SPF table that covers value."""
    if value <= 0 or value >= len(spf):
        raise ValueError("SPF table does not cover the requested value")
    factors: list[tuple[int, int]] = []
    while value > 1:
        prime = spf[value]
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        factors.append((prime, exponent))

    result = [1]
    for prime, exponent in factors:
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return sorted(result)


def ray_witness(
    prime: int, ac_bound: int, spf: list[int]
) -> tuple[int, int, int, int, object] | None:
    """Return the least max(A,C) witness, then lexicographically.

    The fourth returned component is h=4*A*C*K-1. K is deliberately not
    bounded: every eligible factor h of p+4*A*A*C is tested.
    """
    for radius in range(1, ac_bound + 1):
        for a in range(1, radius + 1):
            for c in range(1, radius + 1):
                if max(a, c) != radius:
                    continue
                for h in divisors(prime + 4 * a * a * c, spf):
                    modulus = 4 * a * c
                    if h <= 1 or (h + 1) % modulus:
                        continue
                    k = (h + 1) // modulus
                    certificate = short_certificate.type_ii_raw_ray_certificate(
                        prime, a, c, k
                    )
                    if certificate is not None:
                        return a, c, k, h, certificate
    return None


def run_experiment(limit: int, ac_bound: int) -> dict[str, object]:
    if limit < 73 or ac_bound < 1:
        raise ValueError("limit must be at least 73 and ac_bound must be positive")
    max_shifted_value = limit + 4 * ac_bound**3
    spf = short_certificate.smallest_prime_factors(max_shifted_value)
    core_primes = [
        prime for prime in short_certificate.primes_up_to(limit) if prime % 24 == 1
    ]

    missing: list[int] = []
    record_holders: list[dict[str, int]] = []
    sample_witnesses: list[dict[str, int]] = []
    largest_radius = 0
    for prime in core_primes:
        witness = ray_witness(prime, ac_bound, spf)
        if witness is None:
            missing.append(prime)
            continue
        a, c, k, h, certificate = witness
        radius = max(a, c)
        entry = {
            "prime": prime,
            "radius": radius,
            "a": a,
            "c": c,
            "k": k,
            "h": h,
            "gap": certificate.gap,
            "divisor": certificate.divisor,
        }
        if radius > largest_radius:
            largest_radius = radius
            record_holders.append(entry)
        if len(sample_witnesses) < 10:
            sample_witnesses.append(entry)

    return {
        "arithmetic": "exact SPF factorization, divisibility, and fractions.Fraction certificate verification",
        "scope_note": (
            "A finite A,C-ray audit. It leaves K unbounded by enumerating divisors of "
            "p+4*A^2*C, but finite coverage does not prove a global A,C bound."
        ),
        "prime_limit": limit,
        "ac_box": {"a_max": ac_bound, "c_max": ac_bound},
        "ray_generator": (
            "h=4*A*C*K-1 divides p+4*A^2*C, "
            "K=(h+1)/(4*A*C), equivalently h divides K*p+A"
        ),
        "core_prime_count": len(core_primes),
        "captured_count": len(core_primes) - len(missing),
        "missing": missing,
        "largest_minimal_ac_radius": largest_radius if record_holders else None,
        "ac_radius_record_holders": record_holders,
        "sample_witnesses": sample_witnesses,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--ac-bound", type=int, default=14)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_experiment(args.limit, args.ac_bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
