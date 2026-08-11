#!/usr/bin/env python3
"""Verify the mod-3 double-G obstruction and its focused controls."""

from __future__ import annotations

import argparse
import math


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor += 1 if divisor == 2 else 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def square_divisors(value: int) -> list[int]:
    divisors = [1]
    for prime, exponent in factorization(value).items():
        divisors = [
            old * prime**power
            for old in divisors
            for power in range(2 * exponent + 1)
        ]
    return sorted(divisors)


def is_mod_three_g(value: int) -> bool:
    return all(prime % 3 == 1 for prime in factorization(value))


def certificate_at_gap(prime: int, gap: int) -> tuple[str, int] | None:
    x = (prime + gap) // 4
    if 4 * x != prime + gap:
        return None
    for divisor in square_divisors(x):
        if (prime * x + divisor) % gap == 0:
            return ("I", divisor)
        if divisor <= x and (x + divisor) % gap == 0:
            return ("II", divisor)
    return None


def verify() -> None:
    p = 241
    x = (p + 3) // 4
    n = (3 * p + 1) // 4
    assert (x, factorization(x)) == (61, {61: 1})
    assert (n, factorization(n)) == (181, {181: 1})
    assert is_mod_three_g(x) and is_mod_three_g(n)
    assert certificate_at_gap(p, 3) is None
    assert certificate_at_gap(p, 7) == ("II", 1)

    p = 2521
    x = (p + 3) // 4
    n = (3 * p + 1) // 4
    assert (x, factorization(x)) == (631, {631: 1})
    assert (n, factorization(n)) == (1891, {31: 1, 61: 1})
    assert is_mod_three_g(x) and is_mod_three_g(n)

    expected_spectra = {
        3: {1},
        7: {1, 2, 4},
        11: {1, 2, 3, 4, 6, 7, 9},
        15: {1, 2, 4, 8},
        19: {1, 2, 5, 6, 7, 8, 9, 13, 17},
    }
    for gap, expected in expected_spectra.items():
        local_x = (p + gap) // 4
        residues = {divisor % gap for divisor in square_divisors(local_x)}
        assert residues == expected
        assert certificate_at_gap(p, gap) is None

    assert certificate_at_gap(p, 23) == ("II", 8)
    gap = 23
    x = (p + gap) // 4
    divisor = 8
    y = p * (x + divisor) // gap
    z = p * (x + x * x // divisor) // gap
    assert (x, y, z) == (636, 70588, 5611746)
    assert math.gcd(x, gap) == 1
    assert 4 * x * y * z == p * (x * y + x * z + y * z)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified mod-three double-G obstruction and focused controls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

