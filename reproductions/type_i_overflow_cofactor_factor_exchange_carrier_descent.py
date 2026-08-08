#!/usr/bin/env python3
"""Verify focused cofactor factor-transfer and exchange descent receipts.

This checks four exact instances of the general carrier-rank lemma.  It is not
a prime-range scan.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    carrier: int
    d: int
    denominator: int
    support: int
    expected_route: str
    expected_factor: int | None
    expected_target: tuple[int, int]


FIXTURES = (
    Fixture("d_one_full_factor", 73, 1332, 1, 73, 36, "factor", 37, (36, 37)),
    Fixture("proper_composite_factor", 73, 2050, 3, 337, 41, "factor", 10, (205, 30)),
    Fixture("factor_free_exchange", 73, 666, 2, 73, 18, "exchange", None, (36, 37)),
    Fixture("d_two_square_transfer", 73, 1396, 2, 153, 698, "factor", 2, (698, 4)),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def divisors(value: int) -> tuple[int, ...]:
    result: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        result.append(divisor)
        if divisor * divisor != value:
            result.append(value // divisor)
    return tuple(sorted(result))


def transfer_factors(cofactor: int, d: int, prime: int) -> tuple[int, ...]:
    return tuple(g for g in divisors(cofactor) if 1 < g and d * g < prime)


def chart(prime: int, carrier: int, d: int, denominator: int, support: int) -> tuple[int, int]:
    R = 4 * carrier - denominator
    K = carrier * (prime - d)
    if not (
        prime * denominator == 4 * carrier * d + 1
        and 0 < R < 4 * carrier
        and R % 4 == 3
        and K > 0
        and 4 * K == prime * R + 1
        and carrier % support == 0
        and K % support == 0
        and 1 < d < prime
    ):
        raise AssertionError("target canonical chart changed")
    return R, K


def audit(fixture: Fixture) -> str:
    p = fixture.prime
    M = fixture.carrier
    d = fixture.d
    n = fixture.denominator
    A = fixture.support
    B = (p - 1) ** 2 // 4

    if not (is_prime(p) and p % 24 == 1):
        raise AssertionError(f"{fixture.name}: not a core prime")
    if not (p * n == 4 * M * d + 1 and n > 1 and 1 <= d < p):
        raise AssertionError(f"{fixture.name}: source determinant changed")
    if not (1 <= A <= B and M % A == 0 and 4 * M - n > p):
        raise AssertionError(f"{fixture.name}: source is not a valid overflow state")

    b = M // A
    choices = transfer_factors(b, d, p)
    source_rank = (B // A, M)

    if choices:
        g = max(choices)
        target = (M // g, d * g)
        if fixture.expected_route != "factor" or g != fixture.expected_factor:
            raise AssertionError(f"{fixture.name}: canonical factor choice changed")
    else:
        if not (d < b < p and fixture.expected_route == "exchange"):
            raise AssertionError(f"{fixture.name}: exchange gate changed")
        target = (A * d, b)

    if target != fixture.expected_target:
        raise AssertionError(f"{fixture.name}: target coordinates changed")
    R_target, _ = chart(p, target[0], target[1], n, A)
    R_source = 4 * M - n
    target_rank = (B // A, target[0])
    if not (target[0] < M and R_target < R_source and target_rank < source_rank):
        raise AssertionError(f"{fixture.name}: carrier-rank descent changed")
    return fixture.expected_route


def verify() -> None:
    routes = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_route for fixture in FIXTURES}
    if routes != expected:
        raise AssertionError("cofactor transfer route receipt changed")
    print(f"verified {len(FIXTURES)} focused cofactor transfer/exchange descent receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
