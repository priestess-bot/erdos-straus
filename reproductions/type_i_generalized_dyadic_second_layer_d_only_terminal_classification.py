#!/usr/bin/env python3
"""Verify generalized-dyadic second-layer D-only terminal classification."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, prod


def factorint(value: int) -> tuple[tuple[int, int], ...]:
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return tuple(factors)


def divisors(value: int) -> list[int]:
    values = [1]
    for prime, exponent in factorint(value):
        values = [base * prime**power for base in values for power in range(exponent + 1)]
    return sorted(values)


def d_only_candidates(prime: int, n: int) -> list[int]:
    N = n * prime
    C = 4 * (prime - n)
    return [
        delta
        for delta in divisors(N * N)
        if 0 < delta < n * n
        and (delta - N) % C == 0
        and (N * N // delta - N) % C == 0
    ]


def lift_coordinates(prime: int, n: int, delta: int) -> tuple[int, int]:
    N = n * prime
    C = 4 * (prime - n)
    assert N * N % delta == 0
    a, rem_a = divmod(N - delta, C)
    a_prime, rem_a_prime = divmod(N * N // delta - N, C)
    assert rem_a == rem_a_prime == 0 and a > 0 and a_prime > 0
    assert Fraction(1, a_prime) == Fraction(1, a) + Fraction(4, prime) - Fraction(4, n)
    return a, a_prime


def marked_tail(prime: int, n: int, delta: int) -> tuple[int, int, int, int, int]:
    a, a_prime = lift_coordinates(prime, n, delta)
    M = 4 * a - n
    S = n * a
    common = gcd(M, S)
    mu, sigma = M // common, S // common
    for z in divisors(sigma * sigma):
        if (z + sigma) % mu == 0:
            b = (sigma + z) // mu
            c = (sigma + sigma * sigma // z) // mu
            assert Fraction(4, n) == Fraction(1, a) + Fraction(1, b) + Fraction(1, c)
            assert Fraction(4, prime) == Fraction(1, a_prime) + Fraction(1, b) + Fraction(1, c)
            return a, a_prime, b, c, z
    raise AssertionError("marked tail is empty")


def reverse_coordinates(prime: int, n: int, ell: int) -> tuple[int, int] | None:
    r = prime - n
    H_star = n + 4 * r * ell
    numerator = n * prime * ell
    if numerator % H_star:
        return None
    a = numerator // H_star
    delta = n * prime - 4 * r * a
    assert prime * n * n % H_star == 0
    assert delta == prime * n * n // H_star
    return a, delta


def classify_witness(
    prime: int,
    n: int,
    delta: int,
    witness: tuple[int, int, int, int, int],
) -> str:
    a, a_prime, b, c, _ = witness
    assert a_prime % prime == 0
    ell = a_prime // prime
    if n * n % delta == 0:
        h = n * n // delta
        k, remainder = divmod(h - 1, prime - n)
        assert remainder == 0 and 4 * ell == prime * k + 1
        assert a == n * ell // h
        assert Fraction(1, b) + Fraction(1, c) == Fraction(k, ell)
        return "type_I"

    assert (4 * ell - 1) % prime != 0
    tail_divisibility = (b % prime == 0, c % prime == 0)
    assert sum(tail_divisibility) == 1
    x = c if tail_divisibility[0] else b
    y = b // prime if tail_divisibility[0] else c // prime
    z = ell
    assert 4 * x > prime and 2 * x < prime
    m = 4 * x - prime
    left, right = m * y - x, m * z - x
    assert left > 0 and right > 0 and left * right == x * x
    d = min(left, right)
    assert x * x % d == 0 and d <= x and (d + x) % m == 0
    return "type_II"


def dyadic_result(
    prime: int,
    modulus: int,
    K: int,
    relation: tuple[int, ...],
) -> tuple[int, int]:
    factors = factorint(K)
    assert len(factors) == len(relation)
    numerator = prod(q**max(exponent, 0) for (q, _), exponent in zip(factors, relation, strict=True))
    denominator = prod(q**max(-exponent, 0) for (q, _), exponent in zip(factors, relation, strict=True))
    assert numerator < denominator
    assert numerator * pow(denominator, -1, modulus) % modulus == 1
    E = 4 * K * numerator // denominator
    n = (4 * K - E) // modulus
    assert E % 2 == 0 and E % modulus == 1 and 0 < n < prime and n % 2 == 0
    return E, n


def verify() -> None:
    prime, modulus, K = 433, 15, 1624

    E, n = dyadic_result(prime, modulus, K, (-1, -1, -1))
    assert (E, n) == (16, 432)
    natural = n * n // E
    assert natural == 11664
    candidates = d_only_candidates(prime, n)
    assert natural in candidates and 2916 in candidates
    witness = marked_tail(prime, n, 2916)
    assert witness[:4] == (46035, 2953060, 110, 6820)
    assert classify_witness(prime, n, 2916, witness) == "type_I"
    assert 2916 != natural and n * n % 2916 == 0
    assert reverse_coordinates(prime, n, 6820) == (46035, 2916)
    assert reverse_coordinates(prime, n, K) == (n * K // E, natural)

    # A centered Type I chart need not pull back to a prescribed n.
    assert 4 * 639 == 73 * 35 + 1
    assert reverse_coordinates(73, 36, 639) is None

    E_outer, n_outer = dyadic_result(prime, modulus, K, (-4, 0, 0))
    assert (E_outer, n_outer) == (406, 406)
    assert d_only_candidates(prime, n_outer) == [406]
    assert n_outer * n_outer // E_outer == 406

    noncore = marked_tail(7, 6, 14)
    assert noncore[:4] == (7, 21, 2, 42)
    assert noncore[1] % 7 == 0
    assert sum(value % 7 == 0 for value in noncore[2:4]) == 1
    assert 6 * 6 % 14 != 0
    assert classify_witness(7, 6, 14, noncore) == "type_II"

    print("verified generalized-dyadic second-layer D-only classification")
    print("p433_nonnatural_type_I", witness[:4], "natural_delta", natural)
    print("p433_outer_relation_candidates", [406])
    print("noncore_type_II_algebraic_boundary", noncore[:4])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
