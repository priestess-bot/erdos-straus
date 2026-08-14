#!/usr/bin/env python3
"""Verify q=1 source compression into standard factor-pair two-tail sources.

The verifier checks the exact gcd identity, the sharp algebraic equality
control, a genuine gap-59 factor-pair terminal, and one canonical-predecessor
carrier that cannot enter a compatible smaller source.  It does not search for
a universal selector or assert E1/E3 provenance.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt

def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def divisors(value: int) -> list[int]:
    result = [1]
    for prime, exponent in factorization(value).items():
        base = tuple(result)
        power = 1
        for _ in range(exponent):
            power *= prime
            result.extend(item * power for item in base)
    return sorted(result)


def source_profile(prime: int, a: int) -> dict[str, int]:
    if not is_prime(prime) or prime % 24 != 1:
        raise AssertionError("control is not a core prime")
    X = (prime + 3) // 4
    U = X - 1
    m = 4 * a - 1
    if not (a > 1 and U % a == 0 and m <= prime - 2):
        raise AssertionError("invalid factor-pair descent parameter")
    n = U // a + 1
    x = a * n
    retained = gcd(X, n)
    if not (
        (a * n == X + a - 1)
        and gcd(a, X) == 1
        and retained == gcd(X, x) == gcd(X, a - 1)
        and retained * retained <= X
        and X % retained == 0
    ):
        raise AssertionError("q=1 source compression identity changed")
    return {
        "p": prime,
        "X": X,
        "a": a,
        "m": m,
        "n": n,
        "x": x,
        "retained": retained,
        "source_loss": X // retained,
    }


def factor_pair_hits(prime: int, a: int) -> list[tuple[int, int, int, int]]:
    profile = source_profile(prime, a)
    x = profile["x"]
    m = profile["m"]
    hits: list[tuple[int, int, int, int]] = []
    for A in divisors(x):
        for B in divisors(x // A):
            C = x // (A * B)
            if A <= B and gcd(A, B) == 1 and (A + B) % m == 0:
                hits.append((A, B, C, (A + B) // m))
    return hits


def canonical_predecessor_carrier(prime: int, d: int) -> int:
    """Rebuild gcd(X, K_d) for one q=1 canonical-root predecessor."""
    X = (prime + 3) // 4
    t = (prime - 1) // 24
    g = (prime + 1) // 2
    T = prime * prime * t - g
    A = g * T
    if not (is_prime(prime) and prime % 24 == 1 and 1 <= d < prime and A % d == 0):
        raise AssertionError("invalid canonical predecessor control")
    K_d = (A // d) * (prime - d)
    return gcd(X, K_d)


def verify() -> dict[str, object]:
    sharp = source_profile(673, 14)
    if not (
        sharp
        == {
            "p": 673,
            "X": 169,
            "a": 14,
            "m": 55,
            "n": 13,
            "x": 182,
            "retained": 13,
            "source_loss": 13,
        }
        and factor_pair_hits(673, 14) == []
    ):
        raise AssertionError("sharp algebraic compression control changed")

    terminal = source_profile(118801, 15)
    terminal_hits = factor_pair_hits(118801, 15)
    if not (
        all(prime % 3 == 1 for prime in factorization(terminal["X"]))
        and terminal
        == {
            "p": 118801,
            "X": 29701,
            "a": 15,
            "m": 59,
            "n": 1981,
            "x": 29715,
            "retained": 7,
            "source_loss": 4243,
        }
        and terminal_hits == [(1, 1415, 21, 24)]
    ):
        raise AssertionError("gap-59 terminal compression control changed")

    separated = source_profile(1033, 43)
    H = canonical_predecessor_carrier(1033, 330)
    if not (
        H == 37
        and separated["retained"] == 7
        and gcd(H, separated["n"]) == gcd(H, separated["a"] - 1) == 1
        and factor_pair_hits(1033, 43) == []
    ):
        raise AssertionError("predecessor carrier separation control changed")

    return {
        "status": "verified",
        "sharp_algebraic_control": sharp,
        "actual_terminal_control": {"profile": terminal, "factor_pair": terminal_hits[0]},
        "predecessor_separation_control": {
            "profile": separated,
            "inverse_divisor": 330,
            "predecessor_carrier": H,
            "carrier_into_n": gcd(H, separated["n"]),
        },
        "scope": (
            "Three fixed core-prime controls; exact gcd and factor-pair checks only; "
            "no prime-range search, source-path search, or global selector claim."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(verify(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
