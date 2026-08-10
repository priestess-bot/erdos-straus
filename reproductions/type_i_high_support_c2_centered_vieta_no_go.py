#!/usr/bin/env python3
"""Verify the C=2 centered antipodal Vieta no-go identities."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd

import sympy


def symbolic_vieta_identities() -> None:
    a, b, c, h, X = sympy.symbols("a b c h X", nonzero=True)
    polynomial = X**2 + (2 * a + 3 * h - 8 * a * c * h**2) * X + (a + h) * (a + 2 * h)
    equation_difference = (a + X + h) * (a + X + 2 * h) - (8 * a * X * c * h**2)
    if sympy.expand(polynomial - equation_difference) != 0:
        raise AssertionError("Vieta polynomial expansion changed")

    constant = (a + h) * (a + 2 * h)
    other_root = constant / b
    root_transport = sympy.factor(
        b**2 * polynomial.subs(X, other_root) - constant * polynomial.subs(X, b)
    )
    if root_transport != 0:
        raise AssertionError("Vieta root transport identity changed")

    at_a = sympy.expand(polynomial.subs(X, a))
    expected_at_a = (4 - 8 * c * h**2) * a**2 + 6 * a * h + 2 * h**2
    if sympy.expand(at_a - expected_at_a) != 0:
        raise AssertionError("F(a) identity changed")

    exceptional = sympy.expand(polynomial.subs({a: 1, h: 1, c: 1}))
    if exceptional != X**2 - 3 * X + 6 or sympy.discriminant(exceptional, X) != -15:
        raise AssertionError("exceptional Vieta boundary changed")


def centered_divisors(U: int) -> tuple[int, ...]:
    R = 8 * U - 1
    K = U * (8 * U + 1)
    return tuple(
        divisor
        for divisor in sympy.divisors(K * K)
        if divisor < K and (divisor + K) % R == 0
    )


def antipodal_pairs(U: int) -> tuple[tuple[int, int], ...]:
    R = 8 * U - 1
    K = U * (8 * U + 1)
    divisors = sympy.divisors(K)
    return tuple(
        (a, b)
        for a in divisors
        for b in divisors
        if a <= b and gcd(a, b) == 1 and K % (a * b) == 0 and (a + b) % R == 0
    )


def verify_antipodal_controls() -> None:
    for U in range(1, 65):
        if centered_divisors(U):
            raise AssertionError(f"U={U} acquired a centered divisor")
    for U in (1, 18, 24, 48):
        if antipodal_pairs(U):
            raise AssertionError(f"U={U} acquired an antipodal divisor pair")


def verify_prime_embedding(prime: int) -> dict[str, int]:
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise ValueError("expected a core prime")
    U = (prime - 1) // 4
    R = 8 * U - 1
    K = U * (8 * U + 1)
    A = K // 2
    n = prime - 1
    E = 2 * n
    if not (
        R == 2 * prime - 3
        and K == (prime - 1) * (2 * prime - 1) // 4
        and A == (prime - 1) * (2 * prime - 1) // 8
        and 4 * K == prime * R + 1
        and (4 * K - E) // R == n
        and n * K // E == A
        and Fraction(4, n) - Fraction(1, A) == Fraction(R, K)
        and Fraction(4, prime) - Fraction(1, prime * K) == Fraction(R, K)
        and not centered_divisors(U)
    ):
        raise AssertionError("core C=2 embedding changed")
    return {"p": prime, "U": U, "R": R, "K": K, "A": A}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--verify", action="store_true", help="run focused theorem controls"
    )
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")

    symbolic_vieta_identities()
    verify_antipodal_controls()
    rows = [verify_prime_embedding(prime) for prime in (73, 97, 193)]
    print("verified C=2 centered antipodal Vieta no-go")
    for row in rows:
        print(
            f"p={row['p']} U={row['U']} "
            f"state=({row['R']},{row['K']};{row['A']}) centered=miss"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
