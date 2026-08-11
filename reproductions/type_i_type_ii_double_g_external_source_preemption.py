#!/usr/bin/env python3
"""Verify the p=5209 double-G external-source miss and gap-11 preemption."""

from __future__ import annotations

import argparse


def factorization(value: int) -> dict[int, int]:
    """Return the exact trial-division factorization of a positive integer."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
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


def positive_divisors(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def square_divisors(value: int) -> list[int]:
    return positive_divisors(
        {prime: 2 * exponent for prime, exponent in factorization(value).items()}
    )


def is_prime(value: int) -> bool:
    return value > 1 and factorization(value) == {value: 1}


def assert_egyptian_identity(denominator: int, terms: tuple[int, int, int]) -> None:
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator is nonpositive")
    if 4 * first * second * third != denominator * (
        first * second + first * third + second * third
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def verify() -> None:
    prime = 5_209
    assert is_prime(prime) and prime % 24 == 1

    type_ii_g = (prime + 3) // 4
    type_i_g = (3 * prime + 1) // 4
    assert (type_ii_g, factorization(type_ii_g)) == (1_303, {1_303: 1})
    assert (type_i_g, factorization(type_i_g)) == (3_907, {3_907: 1})
    assert all(q % 3 == 1 for q in factorization(type_ii_g))
    assert all(q % 3 == 1 for q in factorization(type_i_g))

    base = (prime - 1) // 4
    assert (base, factorization(base)) == (1_302, {2: 1, 3: 1, 7: 1, 31: 1})
    allowed_k = positive_divisors(factorization(base))
    assert len(allowed_k) == 16

    # This is the complete zero-shift external-source menu, not a bounded k scan.
    menu_hits: list[tuple[int, int]] = []
    for k in allowed_k:
        q = 4 * k - 1
        source = (q * prime + 1) // (q + 1)
        preserved = k * source
        assert (q + 1) * source == q * prime + 1
        assert 2 <= source < prime
        for e in square_divisors(preserved):
            if e <= preserved and e % q == (-preserved) % q:
                menu_hits.append((k, e))
    assert menu_hits == []

    h = (prime - 1) // 24
    source = 2 * h + 1
    r = 29
    c = (3 * r + 1) // 11
    divisor = source // r
    x = 3 * source
    assert (h, source, factorization(source)) == (217, 435, {3: 1, 5: 1, 29: 1})
    assert r % 11 == 7 and source % r == 0
    assert (c, divisor, x) == (8, 15, 1_305)
    assert x == (prime + 11) // 4
    assert x + divisor == 11 * c * divisor

    a, b, c_factor, k = 1, 87, 15, 8
    assert x == a * b * c_factor
    assert a + b == 11 * k
    terminal = (x, prime * a * c_factor * k, prime * b * c_factor * k)
    descent = (x, a * c_factor * k, b * c_factor * k)
    assert terminal == (1_305, 625_080, 54_381_960)
    assert descent == (1_305, 120, 10_440)
    assert source == (prime + 11) // 12 < prime
    assert_egyptian_identity(prime, terminal)
    assert_egyptian_identity(source, descent)
    assert terminal == (descent[0], prime * descent[1], prime * descent[2])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()
    print("verified p=5209 double-G external-source miss and gap-11 terminal preemption")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
