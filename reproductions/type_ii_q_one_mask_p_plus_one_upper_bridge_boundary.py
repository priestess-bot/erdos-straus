#!/usr/bin/env python3
"""Verify the q=1-mask p+1 quotient upper-bridge boundary.

The script derives the exact divisor-capacity congruence symbolically and
checks the fixed H3 hard control p=14449, q=5.  It performs no prime-range
scan and makes no assertion about arbitrary Erdos--Straus solutions.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod

import sympy


def is_prime(value: int) -> bool:
    """Deterministically test the small fixed integers used below."""
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


def divisors_from_factorization(factors: dict[int, int]) -> tuple[int, ...]:
    """Enumerate exactly the positive divisors of a supplied factorization."""
    values = [1]
    for prime, exponent in sorted(factors.items()):
        values = [
            value * prime**power
            for value in values
            for power in range(exponent + 1)
        ]
    return tuple(sorted(values))


def assert_egyptian(denominator: int, terms: tuple[int, int, int]) -> None:
    """Check one exact three-term unit-fraction identity."""
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if Fraction(4, denominator) != sum(
        (Fraction(1, term) for term in terms), Fraction()
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def upper_bridge_data(prime: int, factor: int) -> dict[str, int]:
    """Build n=(q-1)h and its exact one-retained-tail capacity data."""
    if (
        not is_prime(prime)
        or prime % 24 != 1
        or not is_prime(factor)
        or factor % 4 != 1
        or (prime + 1) % factor
    ):
        raise AssertionError("input is not a q=1 p+1-mask control")
    h = (prime + 1) // factor
    n = (factor - 1) * h
    slope = 3 * factor - 4
    R = 4 * n - prime
    S = n * prime
    if not (
        prime == factor * h - 1
        and h % 4 == 2
        and n % 2 == 0
        and prime // 2 < n < prime
        and R == slope * h + 1
        and gcd(slope, R) == gcd(R, S) == 1
        and slope * n % R == -(factor - 1) % R
        and slope * prime % R == -4 * (factor - 1) % R
        and slope * slope * S % R == 4 * (factor - 1) ** 2 % R
    ):
        raise AssertionError("q=1 upper-bridge arithmetic changed")
    return {
        "p": prime,
        "q": factor,
        "h": h,
        "n": n,
        "s": slope,
        "R": R,
        "S": S,
    }


def bridge_from_divisor(data: dict[str, int], divisor: int) -> tuple[int, int, int] | None:
    """Realize the complete standard-even lift when its divisor gate opens."""
    prime = data["p"]
    n = data["n"]
    slope = data["s"]
    R = data["R"]
    S = data["S"]
    if divisor <= 0 or S * S % divisor:
        raise AssertionError("candidate was not a divisor of S squared")
    capacity_hit = (slope * slope * divisor + 4 * (data["q"] - 1) ** 2) % R == 0
    raw_hit = (S + divisor) % R == 0
    if capacity_hit != raw_hit:
        raise AssertionError("capacity congruence was not equivalent to the raw lift gate")
    if not raw_hit:
        return None
    u = (S + divisor) // R
    v = (S + S * S // divisor) // R
    source = (n // 2, n, n)
    target = (n, u, v)
    assert_egyptian(n, source)
    assert_egyptian(prime, target)
    return target


def verify_symbolic_capacity_map() -> None:
    """Derive all factor-separable monomial remainders modulo s*h+1."""
    q, h, c = sympy.symbols("q h c", positive=True, integer=True)
    slope = 3 * q - 4
    prime = q * h - 1
    n = (q - 1) * h
    R = slope * h + 1
    S = sympy.expand(n * prime)
    expected = {
        (0, 0): c * slope**2 + 4 * (q - 1) ** 2,
        (0, 1): -4 * (q - 1) * (c * slope - (q - 1)),
        (0, 2): 4 * (4 * c + 1) * (q - 1) ** 2,
        (1, 0): 4 * (q - 1) ** 2 - c * slope,
        (1, 1): 4 * (q - 1) * (c + q - 1),
        (1, 2): 4 * (q - 1) ** 2 * (slope - 4 * c),
        (2, 0): c + 4 * (q - 1) ** 2,
        (2, 1): 4 * (q - 1) * ((q - 1) * slope - c),
        (2, 2): 4 * (q - 1) ** 2 * (4 * c + slope**2),
    }
    for alpha, beta in product(range(3), repeat=2):
        degree = alpha + beta
        e = c * h**alpha * prime**beta
        multiplier = slope ** max(2, degree)
        remainder = sympy.rem(
            sympy.Poly(sympy.expand(multiplier * (S + e)), h),
            sympy.Poly(R, h),
        ).as_expr()
        if sympy.expand(remainder - expected[(alpha, beta)]) != 0:
            raise AssertionError("symbolic q=1 monomial remainder changed")


def verify_hard_control() -> dict[str, object]:
    """Exhaust every divisor gate for the actual H3 q=5 hard control."""
    data = upper_bridge_data(14_449, 5)
    if data != {"p": 14_449, "q": 5, "h": 2_890, "n": 11_560, "s": 11, "R": 31_791, "S": 167_030_440}:
        raise AssertionError("fixed H3 hard control changed")

    square_factors = {2: 6, 5: 2, 17: 4, 14_449: 2}
    divisors = divisors_from_factorization(square_factors)
    if len(divisors) != 315 or data["S"] * data["S"] != prod(
        prime**exponent for prime, exponent in square_factors.items()
    ):
        raise AssertionError("hard-control S-squared factorization changed")
    if any(bridge_from_divisor(data, divisor) is not None for divisor in divisors):
        raise AssertionError("hard control unexpectedly opened the standard upper bridge")

    modulus = 10_597
    group_order = modulus - 1
    if not (
        is_prime(modulus)
        and all(is_prime(value) for value in (2, 3, 883))
        and all(pow(5, group_order // divisor, modulus) != 1 for divisor in (2, 3, 883))
        and pow(5, 2_757, modulus) == 2
        and pow(5, 5_547, modulus) == 17
        and pow(5, 3_688, modulus) == 14_449 % modulus
        and pow(5, 7_160, modulus) == (-data["S"]) % modulus
    ):
        raise AssertionError("hard-control primitive-root certificate changed")
    exponent_hits = [
        (two_power, five_power, seventeen_power, prime_power)
        for two_power, five_power, seventeen_power, prime_power in product(
            range(7), range(3), range(5), range(3)
        )
        if (
            2_757 * two_power
            + five_power
            + 5_547 * seventeen_power
            + 3_688 * prime_power
        )
        % group_order
        == 7_160
    ]
    if exponent_hits:
        raise AssertionError("hard-control exponent box unexpectedly hit the target")
    return {
        "p": data["p"],
        "q": data["q"],
        "n": data["n"],
        "R": data["R"],
        "S_square_divisor_count": len(divisors),
        "exponent_box_hits": exponent_hits,
    }


def verify() -> None:
    verify_symbolic_capacity_map()
    receipt = verify_hard_control()
    if receipt != {
        "p": 14_449,
        "q": 5,
        "n": 11_560,
        "R": 31_791,
        "S_square_divisor_count": 315,
        "exponent_box_hits": [],
    }:
        raise AssertionError("q=1 upper-bridge receipt changed")
    print("verified q=1 p+1 upper-bridge capacity map and p=14449 hard boundary")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact symbolic and fixed checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
