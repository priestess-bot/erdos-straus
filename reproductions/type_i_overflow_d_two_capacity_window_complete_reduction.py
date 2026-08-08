#!/usr/bin/env python3
"""Verify exact routes in the high-carrier d=2 capacity window.

This is a focused arithmetic receipt, not a prime-range scan.  It checks the
fixed-s, fixed-n preserving, odd-prime transfer, b=2 transfer, and fixed-n
reset routes used by the companion claim.
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
    Fixture("fixed_s", 73, 1323, 145, 3, "fixed_s"),
    Fixture("composite_cofactor", 73, 1323, 145, 21, "fixed_n_preserving"),
    Fixture("odd_prime_below_p_transfer", 73, 1323, 145, 189, "prime_transfer"),
    Fixture("prime_two_transfer", 73, 1396, 153, 698, "prime_two_transfer"),
    Fixture("prime_above_p_reset", 97, 2825, 233, 25, "fixed_n_reset"),
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


def d_two_transfer_bit(prime: int, carrier: int, d: int, support: int) -> int:
    if carrier % support:
        return 0
    quotient = carrier // support
    return int(d == 2 and 1 < quotient < prime and is_prime(quotient))


def fixed_n_chart(prime: int, product: int, denominator: int, selected: int) -> tuple[int, int]:
    if product % selected:
        raise AssertionError("selected fixed-n carrier is not a divisor")
    R = 4 * selected - denominator
    K = selected * (prime - product // selected)
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


def transfer_chart(prime: int, denominator: int, carrier: int, d: int, support: int) -> tuple[int, int]:
    R = 4 * carrier - denominator
    K = carrier * (prime - d)
    if not (
        prime * denominator == 4 * carrier * d + 1
        and 0 < R < 4 * carrier
        and R % 4 == 3
        and K > 0
        and 4 * K == prime * R + 1
        and K % support == 0
        and 1 < d < prime
    ):
        raise AssertionError("denominator-transfer canonical chart changed")
    return R, K


def audit(fixture: Fixture) -> str:
    p = fixture.prime
    M = fixture.carrier
    n = fixture.denominator
    A = fixture.support
    d = 2
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4

    if not (is_prime(p) and p % 24 == 1):
        raise AssertionError(f"{fixture.name}: not a core prime")
    if not (p * n == 4 * M * d + 1 and M > B and 2 * p - 1 <= n <= 4 * p - 11):
        raise AssertionError(f"{fixture.name}: not a d=2 high-carrier capacity-window state")
    if not (1 <= A <= B and M % A == 0 and 4 * M - n > p):
        raise AssertionError(f"{fixture.name}: invalid absorbed support or overflow")
    if not (n % 8 == 1 and M < 2 * B):
        raise AssertionError(f"{fixture.name}: d=2 window arithmetic changed")

    b = M // A
    if b <= 1 or M % p == 0:
        raise AssertionError(f"{fixture.name}: invalid cofactor split")

    if A < c:
        L = c
        r = M % p
        s, remainder = divmod(4 * r * d + 1, p)
        if not (
            remainder == 0
            and (r, s, r * d) == ((p - 1) // 8, 1, c)
            and A < L <= B
            and 4 * L > s
            and B // L < B // A
        ):
            raise AssertionError(f"{fixture.name}: fixed-s route changed")
        fixed_s_chart(p, r * d, s, L)
        return "fixed_s"

    if not is_prime(b):
        q = smallest_prime_factor(b)
        L = M // q
        if not (
            b % q == 0
            and q * q <= b < 2 * (p - 1)
            and 2 * q < p
            and L % A == 0
            and L >= 2 * A
            and A < L <= B
            and 4 * L > n
            and B // L < B // A
        ):
            raise AssertionError(f"{fixture.name}: preserving fixed-n route changed")
        fixed_n_chart(p, M * d, n, L)
        return "fixed_n_preserving"

    if b == p:
        raise AssertionError(f"{fixture.name}: p unexpectedly divided M")
    if 2 < b < p:
        M_target = 2 * A
        d_target = b
        R_source = 4 * M - n
        R_target, _ = transfer_chart(p, n, M_target, d_target, A)
        if not (
            R_target < R_source
            and M_target % A == 0
            and d_two_transfer_bit(p, M, d, A) == 1
            and d_two_transfer_bit(p, M_target, d_target, A) == 0
        ):
            raise AssertionError(f"{fixture.name}: odd prime-cofactor transfer changed")
        return "prime_transfer"

    if b == 2:
        M_target = A
        d_target = 4
        R_source = 4 * M - n
        R_target, _ = transfer_chart(p, n, M_target, d_target, A)
        if not (
            R_target < R_source
            and d_two_transfer_bit(p, M, d, A) == 1
            and d_two_transfer_bit(p, M_target, d_target, A) == 0
        ):
            raise AssertionError(f"{fixture.name}: b=2 transfer changed")
        return "prime_two_transfer"

    L = b
    if not (
        b < 2 * (p - 1) < B
        and 8 * A < n
        and A < L <= B
        and M % L == 0
        and 4 * L > n
        and B // L < B // A
        and L % A != 0
    ):
        raise AssertionError(f"{fixture.name}: reset fixed-n route changed")
    fixed_n_chart(p, M * d, n, L)
    return "fixed_n_reset"


def verify() -> None:
    routes = {fixture.name: audit(fixture) for fixture in FIXTURES}
    expected = {fixture.name: fixture.expected_route for fixture in FIXTURES}
    if routes != expected:
        raise AssertionError("d=2 capacity-window route receipt changed")
    print(f"verified {len(FIXTURES)} focused d=2 capacity-window reduction receipts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
