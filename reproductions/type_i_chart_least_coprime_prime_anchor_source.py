#!/usr/bin/env python3
"""Verify fixed least-coprime-prime anchor-source receipts."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt
from typing import Iterator


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    denominator: int
    expected_source_prime: int
    expected_capacity: int


FIXTURES = (
    Fixture("p73_n145_initial_raw_p_failure", 73, 145, 5, 2),
    Fixture("p73_n9365182993_countdown_raw_p_failure", 73, 9_365_182_993, 11, 2),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def primes() -> Iterator[int]:
    candidate = 2
    while True:
        if is_prime(candidate):
            yield candidate
        candidate += 1


def least_coprime_prime(forbidden: int) -> tuple[int, int]:
    checked = 0
    for q in primes():
        checked += 1
        if forbidden % q:
            return q, checked
    raise AssertionError("unreachable")


def audit(fixture: Fixture) -> dict[str, int | str]:
    p = fixture.prime
    n = fixture.denominator
    A = (p * n - 1) // 4
    R = (p - 1) * n - 1
    K = A * (p - 1)
    alpha = (p + 1) // 2
    v = (n + 1) // 2
    g = gcd(alpha, v)
    a = alpha // g
    b = v // g
    E = (p - 1) * b - a
    forbidden = R * K * (R - 1)
    q, checked = least_coprime_prime(forbidden)
    U, V, m = q, R * (q - 1) - q, q - 1
    capacity = (-pow(E, -1, p)) % p
    M = A * E
    Bp = (p - 1) ** 2 // 4
    source_rank = (Bp // A, p - 1)
    target_rank = (Bp // M, capacity)

    if not (
        is_prime(p)
        and p % 24 == 1
        and n > 1
        and n % 4 == 1
        and b % p == 0
        and R % p == 0
        and n >= 2 * p - 1
        and A > Bp
        and E % p == (-a) % p
        and E % p not in (0, 1)
        and q == fixture.expected_source_prime
        and is_prime(q)
        and forbidden % q != 0
        and (R - 1) % q != 0
        and checked <= forbidden.bit_length()
        and q <= forbidden + 1
        and V > 0
        and U + V == R * m
        and gcd(U, V) == 1
        and K % q != 0
        and m % q == q - 1
        and (U // q, (V + R) // q, (m + 1) // q) == (1, R - 1, 1)
        and capacity == fixture.expected_capacity
        and capacity == (2 * g) % p
        and 1 <= capacity < p - 1
        and M > p * p > Bp
        and target_rank < source_rank
    ):
        raise AssertionError(f"{fixture.name}: auxiliary source receipt changed")

    return {
        "name": fixture.name,
        "q": q,
        "checked_primes": checked,
        "capacity": capacity,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    if [(r["q"], r["capacity"]) for r in receipts] != [(5, 2), (11, 2)]:
        raise AssertionError("fixed auxiliary source controls changed")
    print(
        "verified 2 bounded least-coprime-prime anchor sources and "
        "2 strict d=1 raw-p-gate capacity exits"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
