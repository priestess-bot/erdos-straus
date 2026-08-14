#!/usr/bin/env python3
"""Verify the inverse full-product normal form for the q=1 canonical root.

This is a focused algebraic verifier.  It classifies the legal d < p factor
pairs that would fold to the canonical root and checks the p-only d = g
pre-root seed.  It deliberately does not search raw reachability or create an
E1/E3-qualified state.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt


CONTROLS = (73, 97, 193, 433)


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


def canonical_root(prime: int) -> dict[str, int]:
    if not is_prime(prime) or prime % 24 != 1:
        raise AssertionError("control is not a core prime")
    p = prime
    t = (p - 1) // 24
    g = (p + 1) // 2
    T = p * p * t - g
    A = g * T
    n = (4 * A + 1) // p
    K = A * (p - 1)
    R = 4 * A - n
    B = (p - 1) ** 2 // 4
    if not (
        t >= 3
        and T > p * p
        and p * n == 4 * A + 1
        and n == 2 * p * t * (p + 1) - p - 2
        and p * R + 1 == 4 * K
        and A > B
    ):
        raise AssertionError("canonical root identities changed")
    return {"p": p, "t": t, "g": g, "T": T, "A": A, "n": n, "K": K, "R": R, "B": B}


def inverse_predecessor(root: dict[str, int], d: int) -> dict[str, int]:
    p = root["p"]
    A = root["A"]
    n = root["n"]
    B = root["B"]
    if not (1 <= d < p and A % d == 0):
        raise AssertionError("d is not a legal inverse full-product divisor")
    M = A // d
    C = p - d
    K = M * C
    R = 4 * M - n
    target_R = (p - 1) * n - 1
    target_K = M * d * (p - 1)
    if not (
        p * n == 4 * M * d + 1
        and p * R + 1 == 4 * K
        and M * d == A
        and M > B
        and R > p
        and target_R == root["R"]
        and target_K == root["K"]
    ):
        raise AssertionError("inverse full-product predecessor changed")
    return {"d": d, "M": M, "C": C, "K": K, "R": R}


def verify_pre_root(root: dict[str, int]) -> dict[str, int]:
    p = root["p"]
    t = root["t"]
    g = root["g"]
    T = root["T"]
    C = (p - 1) // 2
    b = 2 * t * (p - 1) - 1
    R = p * b
    K = T * C
    predecessor = inverse_predecessor(root, g)
    source_rank = (root["B"], K)
    target_rank = (0, p - 1)
    if not (
        predecessor == {"d": g, "M": T, "C": C, "K": K, "R": R}
        and 4 * T - R == root["n"]
        and p * R + 1 == 4 * K
        and p * root["n"] == 4 * T * g + 1
        and R % C == C - 1
        and gcd(C, R - C) == 1
        and gcd(C, K) == C
        and K // C == T
        and source_rank > target_rank
    ):
        raise AssertionError("canonical g pre-root seed changed")
    return {"d": g, "C": C, "M": T, "R": R, "K": K, "b": b}


def verify() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for prime in CONTROLS:
        root = canonical_root(prime)
        legal_divisors = [d for d in divisors(root["A"]) if d < prime]
        predecessors = [inverse_predecessor(root, d) for d in legal_divisors]
        if not (
            root["g"] in legal_divisors
            and predecessors[0]["d"] == 1
            and predecessors[0]["M"] == root["A"]
            and predecessors[0]["R"] == root["R"]
            and all(row["M"] > root["B"] and row["R"] > prime for row in predecessors)
        ):
            raise AssertionError("inverse divisor classification changed")
        rows.append(
            {
                "p": prime,
                "legal_divisor_count": len(legal_divisors),
                "pre_root": verify_pre_root(root),
            }
        )
    return {
        "status": "verified",
        "controls": rows,
        "scope": (
            "Four fixed core primes; all d < p divisors of each canonical root support; "
            "no prime-range, denominator-range, selector-history, or raw-reach search."
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
