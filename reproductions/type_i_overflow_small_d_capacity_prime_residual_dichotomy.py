#!/usr/bin/env python3
"""Verify focused routes for the small-d high-carrier capacity dichotomy.

This is a five-receipt arithmetic check.  It does not scan primes or assert
that the final residual has source reachability.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    d: int
    denominator: int
    carrier: int
    support: int
    expected_route: str
    expected_target: tuple[int, int] | None = None


FIXTURES = (
    Fixture("composite_factor", 73, 3, 337, 2050, 41, "factor", (205, 30)),
    Fixture("small_prime_factor", 73, 2, 153, 1396, 698, "factor", (698, 4)),
    Fixture("small_prime_exchange", 73, 2, 273, 2491, 53, "exchange", (106, 47)),
    Fixture("large_prime_reset", 73, 1, 141, 2573, 31, "reset"),
    Fixture("large_prime_residual", 73, 4, 329, 1501, 19, "residual"),
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


def movable_factors(cofactor: int, d: int, prime: int) -> tuple[int, ...]:
    return tuple(g for g in divisors(cofactor) if 1 < g and d * g < prime)


def transfer_chart(prime: int, carrier: int, d: int, denominator: int, support: int) -> tuple[int, int]:
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
        raise AssertionError("transfer target chart changed")
    return R, K


def fixed_n_chart(prime: int, product: int, denominator: int, selected: int) -> tuple[int, int]:
    R = 4 * selected - denominator
    K = selected * (prime - product // selected)
    if not (
        product % selected == 0
        and R > 0
        and K > 0
        and R % 4 == 3
        and 4 * K == prime * R + 1
        and K % selected == 0
    ):
        raise AssertionError("fixed-n reset chart changed")
    return R, K


def audit(fixture: Fixture) -> str:
    p = fixture.prime
    d = fixture.d
    n = fixture.denominator
    M = fixture.carrier
    A = fixture.support
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4

    if not (is_prime(p) and p % 24 == 1):
        raise AssertionError(f"{fixture.name}: not a core prime")
    if not (p * n == 4 * M * d + 1 and B < M < 2 * B and 1 <= d < p):
        raise AssertionError(f"{fixture.name}: capacity state changed")
    if not (c <= A <= B and M % A == 0 and 2 * d * d <= p - 1 and 4 * M - n > p):
        raise AssertionError(f"{fixture.name}: support or small-d gate changed")

    b = M // A
    if not (b > 1 and b < 2 * (p - 1) and b != p):
        raise AssertionError(f"{fixture.name}: cofactor range changed")

    source_rank = (B // A, M)
    choices = movable_factors(b, d, p)

    if not is_prime(b):
        if not choices:
            raise AssertionError(f"{fixture.name}: composite cofactor lost a movable factor")
        target = (M // max(choices), d * max(choices))
        route = "factor"
    elif b < p and b <= d:
        if b not in choices:
            raise AssertionError(f"{fixture.name}: small prime factor gate changed")
        target = (M // b, d * b)
        route = "factor"
    elif b < p:
        target = (A * d, b)
        route = "exchange"
    elif 4 * b > n:
        L = b
        if not (
            b > 2 * A
            and A < L <= B
            and B // L < B // A
            and L % A != 0
        ):
            raise AssertionError(f"{fixture.name}: prime-large reset gate changed")
        fixed_n_chart(p, M * d, n, L)
        route = "reset"
        target = None
    else:
        if not (is_prime(b) and b > p and 4 * b <= n and not choices):
            raise AssertionError(f"{fixture.name}: residual boundary changed")
        route = "residual"
        target = None

    if route != fixture.expected_route or target != fixture.expected_target:
        raise AssertionError(f"{fixture.name}: route changed")
    if target is not None:
        R_target, _ = transfer_chart(p, target[0], target[1], n, A)
        if not (target[0] < M and R_target < 4 * M - n and (B // A, target[0]) < source_rank):
            raise AssertionError(f"{fixture.name}: carrier-rank descent changed")
    return route


def verify() -> None:
    routes = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_route for fixture in FIXTURES}
    if routes != expected:
        raise AssertionError("small-d capacity dichotomy receipt changed")
    print(f"verified {len(FIXTURES)} focused small-d capacity dichotomy receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
