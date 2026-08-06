#!/usr/bin/env python3
"""Verify the fixed gap-27 square-carrier ray and its local group table.

The verifier checks one prime control, the finite U(27) square carrier, and
the exact two-tail identity.  It does not search a progression for primes.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    """Use trial division for the fixed numerical control."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def factorization(value: int) -> list[tuple[int, int]]:
    """Return the factorization of a small fixed integer."""
    factors: list[tuple[int, int]] = []
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def divisors(value: int) -> list[int]:
    """Enumerate divisors of a fixed positive integer."""
    values = [1]
    for prime, exponent in factorization(value):
        values = [
            divisor * prime_power
            for divisor in values
            for prime_power in (prime**power for power in range(exponent + 1))
        ]
    return values


def signed_ratio_box(value: int, modulus: int) -> set[int]:
    """Compute the coprime-divisor signed ratio box modulo 27."""
    if gcd(value, modulus) != 1:
        raise AssertionError("carrier input was not a unit modulo 27")
    return {
        numerator * pow(denominator, -1, modulus) % modulus
        for numerator in divisors(value)
        for denominator in divisors(value)
        if gcd(numerator, denominator) == 1
    }


def assert_egyptian_identity(denominator: int, terms: tuple[int, int, int]) -> None:
    """Check 4/denominator exactly against the three displayed terms."""
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def verify_gap27_control() -> dict[str, object]:
    """Check u=2 on the fixed non-square-five ray."""
    u = 2
    T = 6 * u + 5
    t = 455 * u + 379
    h = 7 * t
    p = 24 * h + 1
    m = 27
    x = (p + m) // 4
    n = (p + m) // (m + 1)
    A, B, C, K = 5, 49, 13 * T, 2
    d = A * A * C

    expected = {
        "p": 216553,
        "h": 9023,
        "t": 1289,
        "T": 17,
        "x": 54145,
        "n": 7735,
        "d": 5525,
    }
    actual = {"p": p, "h": h, "t": t, "T": T, "x": x, "n": n, "d": d}
    if actual != expected or not is_prime(p):
        raise AssertionError("gap-27 ray control changed")
    if (p - 1) % 28 or gcd(x, 27) != 1:
        raise AssertionError("gap-27 strict-source conditions failed")
    if x != A * B * C or gcd(A, B) != 1 or A > B or A + B != m * K:
        raise AssertionError("gap-27 factor-pair normal form failed")
    if x * x % d or d > x or (x + d) % m:
        raise AssertionError("gap-27 Type II divisor conditions failed")
    if 637 > x or x % 637:
        raise AssertionError("gap-27 carrier did not divide x")

    descent = (x, A * C * K, B * C * K)
    terminal = (x, p * A * C * K, p * B * C * K)
    if descent != (54145, 2210, 21658):
        raise AssertionError("gap-27 descent denominators changed")
    assert_egyptian_identity(n, descent)
    assert_egyptian_identity(p, terminal)

    return {
        **actual,
        "factor_pair": {"A": A, "B": B, "C": C, "K": K},
        "descent_denominators": list(descent),
        "terminal_denominators": list(terminal),
    }


def verify_square_carrier() -> dict[str, object]:
    """Check the exact QR_27 carrier and the strict smaller automatic carrier."""
    modulus = 27
    squares = {value * value % modulus for value in range(1, modulus) if gcd(value, modulus) == 1}
    full = signed_ratio_box(637, modulus)
    small = signed_ratio_box(7, modulus)
    if full != squares:
        raise AssertionError("F=7^2*13 no longer covers QR_27")
    if small != {1, 4, 7}:
        raise AssertionError("automatic F=7 capacity boundary changed")
    if pow(7, 9, modulus) != 1 or pow(7, 3, modulus) == 1 or 13 % modulus != pow(7, 5, modulus):
        raise AssertionError("QR_27 generator identities changed")
    if 5 in squares or (-5) % modulus not in squares:
        raise AssertionError("fixed non-square-five trigger changed")
    return {"QR_27": sorted(squares), "R_27_637": sorted(full), "R_27_7": sorted(small)}


def build_result() -> dict[str, object]:
    """Build only the fixed control and its finite carrier table."""
    if gcd(76440, 63673) != 1:
        raise AssertionError("Dirichlet ray residue stopped being primitive")
    return {
        "certificate_type": "gap27_square_carrier_strict_descent_v1",
        "scope": (
            "One fixed prime control and finite U(27) arithmetic only; no "
            "progression scan or full-core coverage claim is made."
        ),
        "control": verify_gap27_control(),
        "carrier": verify_square_carrier(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified gap-27 square-carrier strict-descent control: u=2")


if __name__ == "__main__":
    main()
