#!/usr/bin/env python3
"""Verify the q=1 carrier-preserving factor-pair ray.

This focused verifier checks the algebraic template, its primitive J=7
arithmetic progression, and two fixed q=1 G controls.  It does not search
for prime parameters, classify all G states, or assert a global exit.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
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


def q_one_g(value: int) -> bool:
    return all(prime % 3 == 1 for prime in factorization(value))


def template(J: int, k: int, r: int) -> dict[str, int]:
    if not (J > 0 and k > 0 and r > 0 and J % 6 == 1 and (k * r) % 3 == 1):
        raise AssertionError("template congruence conditions changed")
    m = 4 * J + 3
    c = 3 + k * m
    a = J + 1
    L = a * c * r - 1
    X = J * L
    p = 4 * X - 3
    n = J * c * r
    A, B, C, K = J, c * a, r, 1 + k * a
    return {
        "J": J,
        "k": k,
        "r": r,
        "m": m,
        "c": c,
        "a": a,
        "L": L,
        "X": X,
        "p": p,
        "n": n,
        "A": A,
        "B": B,
        "C": C,
        "K": K,
        "x": A * B * C,
    }


def check_instance(J: int, k: int, r: int, require_prime: bool) -> dict[str, int]:
    data = template(J, k, r)
    p, X, m, a, n = (data[key] for key in ("p", "X", "m", "a", "n"))
    A, B, C, K, x = (data[key] for key in ("A", "B", "C", "K", "x"))
    if not (
        p % 24 == 1
        and m % 4 == 3
        and m <= p - 2
        and (p - 1) % (m + 1) == 0
        and x == (p + m) // 4
        and n == (p + m) // (m + 1)
        and n < p
        and A < B
        and gcd(A, B) == 1
        and A + B == m * K
        and gcd(X, n) == J
        and Fraction(4, n)
        == Fraction(1, A * B * C)
        + Fraction(1, A * C * K)
        + Fraction(1, B * C * K)
        and Fraction(4, p)
        == Fraction(1, A * B * C)
        + Fraction(1, p * A * C * K)
        + Fraction(1, p * B * C * K)
    ):
        raise AssertionError("factor-pair template identity changed")
    if require_prime and not is_prime(p):
        raise AssertionError("fixed core-prime control changed")
    return data


def verify() -> dict[str, object]:
    ray_start = check_instance(7, 1, 1, require_prime=False)
    ray_g = check_instance(7, 1, 10, require_prime=True)
    independent_g = check_instance(13, 1, 1, require_prime=True)

    if not (
        ray_start["p"] == 7585
        and ray_start["X"] == 1897
        and ray_start["n"] == 238
        and ray_g["p"] == 76129
        and ray_g["X"] == 19033
        and ray_g["n"] == 2380
        and ray_g["p"] == 7585 + 22848 * 3
        and ray_g["X"] == 7 * (271 + 816 * 3)
        and ray_g["n"] == 238 * (1 + 3 * 3)
        and gcd(7585, 22848) == 1
        and q_one_g(ray_g["X"])
        and factorization(ray_g["X"]) == {7: 1, 2719: 1}
        and independent_g["p"] == 42169
        and independent_g["X"] == 10543
        and independent_g["n"] == 754
        and independent_g["m"] == 55
        and independent_g["A"] == 13
        and independent_g["B"] == 812
        and independent_g["K"] == 15
        and q_one_g(independent_g["X"])
        and factorization(independent_g["X"]) == {13: 1, 811: 1}
    ):
        raise AssertionError("fixed carrier-preserving controls changed")

    return {
        "status": "verified",
        "primitive_j7_progression": {
            "p": "7585 + 22848*s",
            "s_congruence": "s >= 0",
            "coprime_intercept_and_step": gcd(7585, 22848) == 1,
            "template_at_s_zero": ray_start,
        },
        "q_one_g_controls": [
            {
                "parameters": {"J": 7, "k": 1, "r": 10},
                "profile": ray_g,
                "X_factorization": factorization(ray_g["X"]),
                "retained_carrier": gcd(ray_g["X"], ray_g["n"]),
            },
            {
                "parameters": {"J": 13, "k": 1, "r": 1},
                "profile": independent_g,
                "X_factorization": factorization(independent_g["X"]),
                "retained_carrier": gcd(independent_g["X"], independent_g["n"]),
            },
        ],
        "scope": (
            "Two fixed G controls and the template identities only; no prime-range "
            "search, universal G selector, E1/E3 adapter, or global exit claim."
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
