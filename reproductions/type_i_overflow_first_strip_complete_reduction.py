#!/usr/bin/env python3
"""Verify the four exact routes in the first high-carrier d=1 strip.

This is a focused arithmetic receipt, not a prime-range scan.  It checks the
fixed-s, fixed-n preserving, prime-cofactor transfer, and fixed-n reset routes
used by the companion claim.
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
    denominator: int
    support: int
    expected_route: str


FIXTURES = (
    Fixture("fixed_s", 73, 1332, 73, 6, "fixed_s"),
    Fixture("composite_cofactor", 73, 1332, 73, 18, "fixed_n_preserving"),
    Fixture("prime_below_p_transfer", 73, 1332, 73, 36, "prime_transfer"),
    Fixture("prime_above_p_reset", 73, 1843, 101, 19, "fixed_n_reset"),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def smallest_prime_factor(value: int) -> int:
    if value % 2 == 0:
        return 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return divisor
    return value


def transfer_bit(prime: int, carrier: int, d: int, support: int) -> int:
    if carrier % support:
        return 0
    quotient = carrier // support
    return int(d == 1 and 1 < quotient < prime and is_prime(quotient))


def fixed_n_chart(prime: int, carrier: int, denominator: int, selected: int) -> tuple[int, int]:
    if carrier % selected:
        raise AssertionError("selected fixed-n carrier is not a divisor")
    R = 4 * selected - denominator
    K = selected * (prime - carrier // selected)
    if not (R > 0 and K > 0 and R % 4 == 3 and 4 * K == prime * R + 1 and K % selected == 0):
        raise AssertionError("fixed-n canonical chart changed")
    return R, K


def fixed_s_chart(prime: int, product: int, s: int, selected: int) -> tuple[int, int]:
    if product % selected:
        raise AssertionError("selected fixed-s carrier is not a divisor")
    R = 4 * selected - s
    K = selected * (prime - product // selected)
    if not (R > 0 and K > 0 and R % 4 == 3 and 4 * K == prime * R + 1 and K % selected == 0):
        raise AssertionError("fixed-s canonical chart changed")
    return R, K


def audit(fixture: Fixture) -> str:
    p = fixture.prime
    M = fixture.carrier
    n = fixture.denominator
    A = fixture.support
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4

    if not (is_prime(p) and p % 24 == 1):
        raise AssertionError(f"{fixture.name}: not a core prime")
    if not (p * n == 4 * M + 1 and M > B and p <= n <= 2 * p - 5):
        raise AssertionError(f"{fixture.name}: not a first-strip high carrier")
    if not (1 <= A <= B and M % A == 0):
        raise AssertionError(f"{fixture.name}: invalid absorbed support")
    b = M // A
    if b <= 1 or M % p == 0:
        raise AssertionError(f"{fixture.name}: invalid cofactor split")

    if A < c:
        L = c
        r = M % p
        s, remainder = divmod(4 * r + 1, p)
        if not (
            remainder == 0
            and (r, s) == (c, 1)
            and A < L <= B
            and 4 * L > s
            and B // L < B // A
        ):
            raise AssertionError(f"{fixture.name}: fixed-s route changed")
        fixed_s_chart(p, r, s, L)
        return "fixed_s"

    if not is_prime(b):
        q = smallest_prime_factor(b)
        L = M // q
        if not (
            b % q == 0
            and q <= b // 2 < p
            and L % A == 0
            and L >= 2 * A
            and A < L <= B
            and 4 * L > n
            and B // L < B // A
        ):
            raise AssertionError(f"{fixture.name}: preserving fixed-n route changed")
        fixed_n_chart(p, M, n, L)
        return "fixed_n_preserving"

    if b == p:
        raise AssertionError(f"{fixture.name}: p unexpectedly divided M")
    if b < p:
        M_target = A
        d_target = b
        R_source = 4 * M - n
        R_target = 4 * M_target - n
        K_target = M_target * (p - d_target)
        if not (
            p * n == 4 * M_target * d_target + 1
            and 0 < R_target < 4 * M_target
            and R_target % 4 == 3
            and 4 * K_target == p * R_target + 1
            and K_target % A == 0
            and 1 < d_target < p
            and R_target < R_source
            and B // M_target == B // A
            and transfer_bit(p, M, 1, A) == 1
            and transfer_bit(p, M_target, d_target, A) == 0
        ):
            raise AssertionError(f"{fixture.name}: prime-cofactor transfer changed")
        return "prime_transfer"

    L = b
    if not (
        b < 2 * (p - 1) < B
        and 4 * A < n
        and 2 * A < b
        and A < L <= B
        and M % L == 0
        and 4 * L > n
        and B // L < B // A
        and L % A != 0
    ):
        raise AssertionError(f"{fixture.name}: reset fixed-n route changed")
    fixed_n_chart(p, M, n, L)
    return "fixed_n_reset"


def verify() -> None:
    routes = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_route for fixture in FIXTURES}
    if routes != expected:
        raise AssertionError("first-strip route receipt changed")
    print(f"verified {len(FIXTURES)} focused first-strip reduction receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
