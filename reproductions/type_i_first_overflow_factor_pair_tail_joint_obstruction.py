#!/usr/bin/env python3
"""Focused verifier for first-overflow factor pairs and the four-menu obstruction."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt


def factorint(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    n = value
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    prime = 3
    while prime * prime <= n:
        while n % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            n //= prime
        prime += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def divisors_from_factors(factors: dict[int, int]) -> list[int]:
    result = [1]
    for prime, exponent in sorted(factors.items()):
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return sorted(result)


def divisors(value: int) -> list[int]:
    return divisors_from_factors(factorint(value))


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return factorint(value) == {value: 1}


def reciprocal_sum(denominators: tuple[int, int, int]) -> Fraction:
    return sum((Fraction(1, value) for value in denominators), Fraction(0, 1))


def assert_first_overflow(
    p: int, modulus: int, y: int, gap: int, quotient: int
) -> None:
    assert is_prime(p)
    assert p % 24 == 1
    assert modulus >= 3 and modulus % 2 == 1
    assert gcd(p, modulus) == 1
    assert gap == 4 * y - p
    assert 0 < gap < p
    assert quotient * modulus == p + 4 * y == 2 * p + gap
    assert quotient < p
    assert gcd(modulus, y) == 1
    previous_label = y - modulus
    assert previous_label > 0
    assert 4 * previous_label < p < 4 * y


def quotient_rows(p: int, n: int) -> list[tuple[int, int, int, int, bool]]:
    delta = p * p + 4 * n
    rows = []
    for k in range(p // (4 * n) + 1, p // (2 * n) + 1):
        residual = 4 * k * n - p
        original_remainder = (k * p + 1) % residual
        delta_remainder = delta % residual
        hit = original_remainder == 0
        assert hit == ((4 * k * k * n + 1) % residual == 0)
        assert hit == (delta_remainder == 0)
        assert gcd(residual, 4 * n) == 1
        rows.append((k, residual, original_remainder, delta_remainder, hit))
    return rows


def quotient_hit_divisors(p: int, n: int) -> list[int]:
    delta = p * p + 4 * n
    return [
        divisor
        for divisor in divisors(delta)
        if divisor <= p and (divisor + p) % (4 * n) == 0
    ]


def verify_quotient_factor_theorem(
    p: int, modulus: int, gap: int, n: int
) -> list[tuple[int, int, int, int, bool]]:
    rows = quotient_rows(p, n)
    hits = [residual for _, residual, _, _, hit in rows if hit]
    assert hits == quotient_hit_divisors(p, n)
    delta = p * p + 4 * n
    for k, divisor, _, _, hit in rows:
        t = modulus - 8 * k
        assert 2 * divisor == gap - t * n
        assert gcd(t, divisor) == gcd(t, gap)
        assert (
            t * (4 * k * k * n + 1) - (4 * k * k * gap + t)
        ) % divisor == 0
        if gcd(t, gap) == 1:
            assert hit == ((4 * k * k * gap + modulus - 8 * k) % divisor == 0)
        if not hit:
            continue
        dual = delta // divisor
        assert dual % (4 * n) == (-p) % (4 * n)
        ell = (dual + p) // (4 * n)
        assert ell > k
        assert delta == (4 * k * n - p) * (4 * n * ell - p)
        assert k * p + 1 == ell * divisor
    return rows


def direct_target_gate(p: int, c: int) -> list[int]:
    residual = 4 * c - p
    if residual <= 0:
        return []
    scale = p * c
    return [
        e
        for e in divisors(scale * scale)
        if (scale + e) % residual == 0
        and (scale + scale * scale // e) % residual == 0
    ]


def reduced_target_gate(p: int, c: int) -> list[tuple[int, str]]:
    assert c % p != 0
    residual = 4 * c - p
    if residual <= 0:
        return []
    result = []
    for divisor in divisors(c * c):
        if (4 * divisor + 1) % residual == 0:
            result.append((divisor, "4d+1"))
        if (c + divisor) % residual == 0:
            result.append((divisor, "c+d"))
    return result


def verify_exact_target_gate(p: int, c: int) -> None:
    assert c % p != 0
    direct = direct_target_gate(p, c)
    reduced = reduced_target_gate(p, c)
    assert bool(direct) == bool(reduced)


def natural_menu_rows(
    p: int, y: int, gap: int
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    candidates = divisors(y * y)
    type_i = [(d, (p * y + d) % gap) for d in candidates]
    type_ii = [(d, (y + d) % gap) for d in candidates if d <= y]
    return type_i, type_ii


def representatives(
    target: int, multiplier: int, modulus: int, upper: int
) -> list[int]:
    residue = target * pow(multiplier, -1, modulus) % modulus
    if residue == 0:
        residue = modulus
    return list(range(residue, upper + 1, modulus))


def verify_positive_factor_pair_control() -> None:
    p, modulus, y, gap, n = 73, 27, 29, 43, 7
    assert_first_overflow(p, modulus, y, gap, n)
    rows = verify_quotient_factor_theorem(p, modulus, gap, n)
    assert [(k, r, hit) for k, r, _, _, hit in rows] == [
        (3, 11, True),
        (4, 39, False),
        (5, 67, False),
    ]
    delta = p * p + 4 * n
    assert delta == 5_357
    assert factorint(delta) == {11: 1, 487: 1}
    assert quotient_hit_divisors(p, n) == [11]
    assert (11 + p) // (4 * n) == 3
    assert (487 + p) // (4 * n) == 20
    verify_exact_target_gate(p, 21)
    verify_exact_target_gate(p, 210)
    assert 7 in direct_target_gate(p, 21)
    assert 10 in direct_target_gate(p, 210)


def verify_square_quotient_controls() -> None:
    p, modulus, y, gap, n = 73, 21, 29, 43, 9
    assert_first_overflow(p, modulus, y, gap, n)
    type_i, type_ii = natural_menu_rows(p, y, gap)
    assert not any(remainder == 0 for _, remainder in type_i)
    assert not any(remainder == 0 for _, remainder in type_ii)
    rows = verify_quotient_factor_theorem(p, modulus, gap, n)
    assert [(k, r, hit) for k, r, _, _, hit in rows] == [
        (3, 35, False),
        (4, 71, False),
    ]
    delta = p * p + 4 * n
    assert delta == 5_365
    assert factorint(delta) == {5: 1, 29: 1, 37: 1}
    assert all(divisor % 4 == 1 for divisor in divisors(delta))

    p, modulus, y, gap, n = 2_161, 173, 541, 3, 25
    assert is_prime(p)
    assert_first_overflow(p, modulus, y, gap, n)
    rows = verify_quotient_factor_theorem(p, modulus, gap, n)
    assert [k for k, _, _, _, _ in rows] == list(range(22, 44))
    assert not any(hit for _, _, _, _, hit in rows)
    delta = p * p + 4 * n
    assert delta == 4_670_021
    assert factorint(delta) == {193: 1, 24_197: 1}
    assert all(prime % 4 == 1 for prime in factorint(delta))
    assert isqrt(n) ** 2 == n


def verify_p193_joint_obstruction() -> None:
    p, modulus, y, gap, n = 193, 27, 53, 19, 15
    assert is_prime(p)
    assert_first_overflow(p, modulus, y, gap, n)

    type_i, type_ii = natural_menu_rows(p, y, gap)
    assert type_i == [(1, 8), (53, 3), (2_809, 4)]
    assert type_ii == [(1, 16), (53, 11)]
    assert not any(remainder == 0 for _, remainder in type_i)
    assert not any(remainder == 0 for _, remainder in type_ii)

    rows = verify_quotient_factor_theorem(p, modulus, gap, n)
    assert rows == [
        (4, 47, 21, 38, False),
        (5, 107, 3, 73, False),
        (6, 167, 157, 68, False),
    ]
    delta = p * p + 4 * n
    assert delta == 37_309
    assert factorint(delta) == {37_309: 1}

    a = 3 * (n + 1) // 8
    c_one = n * a
    u = (n + 1) // 4
    t = n * u
    b = u * (n * u + 1)
    c_two = n * b
    assert (a, c_one, u, t, b, c_two) == (6, 90, 4, 60, 244, 3_660)
    assert reciprocal_sum((u, c_one, 3 * t)) == Fraction(4, n)
    assert reciprocal_sum((u, t + 1, c_two)) == Fraction(4, n)

    residual_one = 4 * c_one - p
    assert residual_one == 167
    targets_one = ((-pow(4, -1, residual_one)) % residual_one, (-c_one) % residual_one)
    assert targets_one == (125, 77)
    expected_representatives = {
        0: ([125, 292], [77, 244]),
        1: ([25, 192], [149, 316]),
        2: ([5, 172], [130, 297]),
    }
    for exponent in range(3):
        actual = tuple(
            representatives(target, 5**exponent, residual_one, 324)
            for target in targets_one
        )
        assert actual == expected_representatives[exponent]
        assert not any(324 % value == 0 for values in actual for value in values)
    verify_exact_target_gate(p, c_one)
    assert direct_target_gate(p, c_one) == []
    assert reduced_target_gate(p, c_one) == []

    residual_two = 4 * c_two - p
    assert residual_two == 14_447
    targets_two = ((-pow(4, -1, residual_two)) % residual_two, (-c_two) % residual_two)
    assert targets_two == (10_835, 10_787)
    assert all(target > 3_600 for target in targets_two)
    k_mod_61 = [
        (-target * pow(residual_two, -1, 61)) % 61 for target in targets_two
    ]
    k_mod_61_squared = [
        (-target * pow(residual_two, -1, 61**2)) % (61**2)
        for target in targets_two
    ]
    assert k_mod_61 == [16, 60]
    assert k_mod_61_squared == [3_005, 3_354]
    assert min(k_mod_61) > 14
    assert min(k_mod_61_squared) > 926
    verify_exact_target_gate(p, c_two)
    assert direct_target_gate(p, c_two) == []
    assert reduced_target_gate(p, c_two) == []

    terminal_gap, x, terminal_divisor = 7, 50, 20
    assert terminal_divisor in divisors(x * x)
    assert terminal_divisor <= x
    assert (x + terminal_divisor) % terminal_gap == 0
    terminal_solution = (50, 1_930, 4_825)
    assert reciprocal_sum(terminal_solution) == Fraction(4, p)


def verify() -> None:
    verify_positive_factor_pair_control()
    verify_square_quotient_controls()
    verify_p193_joint_obstruction()
    print("PASS: FIRST_OVERFLOW_FACTOR_PAIR_TAIL_JOINT_OBSTRUCTION")
    print("quotient_factor_pair_positive_control=p73_M27_k3")
    print("square_quotient_empty_controls=p73_M21,p2161_M173")
    print("p193_natural=EMPTY quotient=EMPTY tail_c1=EMPTY tail_c2=EMPTY")
    print("p193_scope=TERMINAL_PREEMPTED_BY_TYPE_II_GAP7_D20")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
