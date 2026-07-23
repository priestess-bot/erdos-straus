#!/usr/bin/env python3
"""Small, exact reproductions of pivotal Erdős-Straus computations."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "results.json"


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def smallest_prime_factors(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for prime in range(2, math.isqrt(limit) + 1):
        if spf[prime] != prime:
            continue
        start = prime * prime
        for value in range(start, limit + 1, prime):
            if spf[value] == value:
                spf[value] = prime
    return spf


def factor_with_spf(value: int, spf: list[int]) -> dict[int, int]:
    factors: dict[int, int] = {}
    while value > 1:
        prime = spf[value]
        factors[prime] = factors.get(prime, 0) + 1
        value //= prime
    return factors


def divisors_from_factors(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        powers = [prime**power for power in range(1, exponent + 1)]
        divisors = [divisor * power for divisor in divisors for power in [1, *powers]]
    return sorted(divisors)


def divisors_of_square(value: int, spf: list[int]) -> list[int]:
    factors = factor_with_spf(value, spf)
    return divisors_from_factors({prime: 2 * exponent for prime, exponent in factors.items()})


def verify_reduction_identities(samples: int = 1000) -> dict[str, int]:
    checked = {"3t-1": 0, "4t-1": 0, "8t-3": 0}
    for t in range(1, samples + 1):
        n = 3 * t - 1
        assert Fraction(4, n) == Fraction(1, t) + Fraction(1, n) + Fraction(1, t * n)
        checked["3t-1"] += 1

        n = 4 * t - 1
        assert Fraction(4, n) == Fraction(1, t) + Fraction(1, t * n)
        checked["4t-1"] += 1

        n = 8 * t - 3
        assert Fraction(4, n) == Fraction(1, 2 * t) + Fraction(1, t * n) + Fraction(1, 2 * t * n)
        checked["8t-3"] += 1
    return checked


def mordell_survivors_mod_840() -> list[int]:
    s5 = {0, 2, 3}
    s7 = {0, 3, 5, 6}
    return [
        residue
        for residue in range(1, 840)
        if residue % 24 == 1
        and residue % 5 not in s5
        and residue % 7 not in s7
        and math.gcd(residue, 840) == 1
    ]


def factor_pair_solution(n: int, spf: list[int]) -> tuple[int, int, int] | None:
    """Find x<=y<=z using (ay-b)(az-b)=b^2 for fixed x."""
    for x in range(ceil_div(n, 4), (3 * n) // 4 + 1):
        numerator = 4 * x - n
        if numerator <= 0:
            continue
        denominator = n * x
        common = math.gcd(numerator, denominator)
        a = numerator // common
        b = denominator // common
        for divisor in divisors_of_square(b, spf):
            paired = b * b // divisor
            if divisor > paired:
                break
            if (b + divisor) % a or (b + paired) % a:
                continue
            y = (b + divisor) // a
            z = (b + paired) // a
            if x <= y <= z and Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
                return x, y, z
    return None


def verify_factor_pair_range(limit: int = 1000) -> dict[str, object]:
    maximum_b = limit * ((3 * limit) // 4)
    spf = smallest_prime_factors(maximum_b)
    solutions: dict[int, tuple[int, int, int]] = {}
    for n in range(2, limit + 1):
        solution = factor_pair_solution(n, spf)
        assert solution is not None, f"no factor-pair certificate for n={n}"
        solutions[n] = solution
    sample_keys = [2, 5, 13, 100, 193, 997]
    return {
        "limit": limit,
        "verified_count": len(solutions),
        "samples": {str(n): list(solutions[n]) for n in sample_keys if n in solutions},
    }


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (((limit - prime * prime) // prime) + 1)
    return [value for value in range(2, limit + 1) if sieve[value]]


def bradford_certificate(p: int, spf: list[int]) -> tuple[str, int, int, int, int] | None:
    for x in range(ceil_div(p, 4), ceil_div(p, 2) + 1):
        modulus = 4 * x - p
        if modulus <= 0:
            continue
        for divisor in divisors_of_square(x, spf):
            if (divisor + p * x) % modulus == 0:
                y = (p * x + divisor) // modulus
                z_numerator = p * (x + p * x * x // divisor)
                if z_numerator % modulus == 0:
                    z = z_numerator // modulus
                    if x <= y <= z and p % y != 0 and Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
                        return "I", x, divisor, y, z
            if divisor <= x and (divisor + x) % modulus == 0:
                y = p * (x + divisor) // modulus
                z_numerator = p * (x + x * x // divisor)
                if z_numerator % modulus == 0:
                    z = z_numerator // modulus
                    if x <= y <= z and y % p == 0 and Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
                        return "II", x, divisor, y, z
    return None


def verify_bradford_range(limit: int = 10000) -> dict[str, object]:
    spf = smallest_prime_factors(ceil_div(limit, 2) + 1)
    certificates: dict[int, tuple[str, int, int, int, int]] = {}
    by_type = {"I": 0, "II": 0}
    for prime in primes_up_to(limit):
        certificate = bradford_certificate(prime, spf)
        assert certificate is not None, f"no Bradford certificate for p={prime}"
        certificates[prime] = certificate
        by_type[certificate[0]] += 1
    sample_keys = [5, 13, 193, 1009, 9973]
    return {
        "limit": limit,
        "prime_count": len(certificates),
        "first_certificate_by_type": by_type,
        "samples": {str(p): list(certificates[p]) for p in sample_keys if p in certificates},
    }


def run(factor_limit: int, bradford_limit: int) -> dict[str, object]:
    survivors = mordell_survivors_mod_840()
    assert survivors == [1, 121, 169, 289, 361, 529]
    return {
        "run_date": str(dt.date.today()),
        "arithmetic": "exact integer arithmetic and fractions.Fraction",
        "reduction_identities": verify_reduction_identities(),
        "mordell_survivors_mod_840": survivors,
        "factor_pair_certificate": verify_factor_pair_range(factor_limit),
        "bradford_divisor_correspondence": verify_bradford_range(bradford_limit),
        "scope_note": "Finite cross-check only; this does not reproduce the reported 10^17 or 10^18 searches.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--factor-limit", type=int, default=1000)
    parser.add_argument("--bradford-limit", type=int, default=10000)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run(args.factor_limit, args.bradford_limit)
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    payload["script_sha256"] = script_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
