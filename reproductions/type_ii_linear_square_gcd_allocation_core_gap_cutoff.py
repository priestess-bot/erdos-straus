#!/usr/bin/env python3
"""Focused verifier for the Type II linear-square and p/3 cutoff theorem."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


def factorint(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= n:
        while n % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            n //= prime
        prime += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def divisors_from_factors(factors: dict[int, int]) -> list[int]:
    values = [1]
    for prime, exponent in sorted(factors.items()):
        values = [value * prime**power for value in values for power in range(exponent + 1)]
    return sorted(values)


def divisors(n: int) -> list[int]:
    return divisors_from_factors(factorint(n))


def square_root_kernel(n: int) -> int:
    result = 1
    for prime, exponent in factorint(n).items():
        result *= prime ** ((exponent + 1) // 2)
    return result


def type_ii_divisors(m: int, y: int) -> list[int]:
    return [d for d in divisors(y * y) if d <= y and (y + d) % m == 0]


def linear_square_rows(m: int, y: int) -> list[tuple[int, int, int, bool]]:
    lower = y // m + 1
    upper = 2 * y // m
    rows = []
    for linear_parameter in range(lower, upper + 1):
        d = linear_parameter * m - y
        common = gcd(d, linear_parameter)
        hit = d % 1 == 0 and linear_parameter * linear_parameter % d == 0
        rows.append((linear_parameter, d, common, hit))
    return rows


def check_bijection(m: int, y: int) -> list[tuple[int, int, int, bool]]:
    p = 4 * y - m
    assert p % 4 == 1
    assert 3 <= m <= p - 2
    assert gcd(m, y) == 1
    rows = linear_square_rows(m, y)
    hit_divisors = sorted(d for _, d, _, hit in rows if hit)
    assert hit_divisors == type_ii_divisors(m, y)
    for linear_parameter, d, common, hit in rows:
        assert gcd(d, m) == 1
        assert gcd(d, linear_parameter) == gcd(y, linear_parameter) == gcd(d, y)
        assert hit == ((d // common) != 0 and common % (d // common) == 0)
        if hit:
            a = d // common
            b = y // common
            c = common * common // d
            k = linear_parameter // common
            assert y == a * b * c
            assert d == a * a * c
            assert gcd(a, b) == 1
            assert a <= b
            assert a + b == k * m
    return rows


def verify() -> None:
    # Equality boundary for primes congruent to 2 modulo 3.
    p_boundary, m_boundary = 17, 7
    y_boundary = (p_boundary + m_boundary) // 4
    assert p_boundary == 3 * m_boundary - 4
    assert y_boundary == 6
    boundary_rows = check_bijection(m_boundary, y_boundary)
    assert boundary_rows == [(1, 1, 1, True)]
    assert m_boundary * 3 > p_boundary

    # Core large-gap control: the entire Type II window is empty.
    p_empty, modulus_empty, m_empty, y_empty = 73, 27, 43, 29
    assert m_empty * 3 > p_empty
    assert p_empty % 3 == 1
    empty_rows = check_bijection(m_empty, y_empty)
    assert empty_rows == [(1, 14, 1, False)]
    assert type_ii_divisors(m_empty, y_empty) == []
    type_i_residues = [(p_empty * y_empty + d) % m_empty for d in divisors(y_empty * y_empty)]
    assert type_i_residues == [11, 39, 34]

    # First-residual positive control.
    p_hit, modulus_hit, m_hit, y_hit = 557_281, 27, 79, 139_340
    hit_rows = check_bijection(m_hit, y_hit)
    l_zero = y_hit // m_hit + 1
    residual = l_zero * m_hit - y_hit
    root_kernel = square_root_kernel(residual)
    assert (l_zero, residual, root_kernel) == (1764, 16, 4)
    assert l_zero % root_kernel == 0
    assert any(row == (1764, 16, 4, True) for row in hit_rows)
    assert 16 in type_ii_divisors(m_hit, y_hit)

    common = gcd(residual, l_zero)
    a = residual // common
    b = y_hit // common
    c = common * common // residual
    k = l_zero // common
    assert (a, b, c, k) == (4, 34_835, 1, 441)
    assert a + b == k * m_hit
    assert gcd(residual, modulus_hit) == 1

    solution = (139_340, 983_043_684, 8_561_081_683_035)
    assert sum((Fraction(1, value) for value in solution), Fraction(0, 1)) == Fraction(4, p_hit)

    # The first-overflow modulus contributes no prime factor to Type II d.
    assert gcd(modulus_empty, y_empty) == 1
    assert gcd(modulus_hit, y_hit) == 1
    assert all(gcd(d, modulus_hit) == 1 for d in type_ii_divisors(m_hit, y_hit))

    print("PASS: TYPE_II_LINEAR_SQUARE_GCD_ALLOCATION_CORE_GAP_CUTOFF")
    print(f"boundary_p17_rows={boundary_rows}")
    print(f"core_p73_rows={empty_rows} type_ii_hits=0")
    print(f"p557281_L0={l_zero} residual={residual} rho={root_kernel}")
    print(f"p557281_normal_form={(a, b, c, k)}")
    print(f"p557281_linear_window={len(hit_rows)} type_ii_hits={len(type_ii_divisors(m_hit, y_hit))}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
