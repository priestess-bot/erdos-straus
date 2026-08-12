#!/usr/bin/env python3
"""Verify the fixed a=1 p-primary no-go receipts.

This focused verifier replays one four-cycle, its binary complement exit,
and one eight-edge repunit transient. It performs no historical range scan.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt, lcm


P = 73
CYCLE_R = 4_796_963
LONG_TRANSIENT_R = 19_417_619_893_481_921_408_946_372_694_037_294_710_514_909_893


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def chart(prime: int, parameter: int) -> tuple[int, int, int, int, int, int]:
    b = 2 * prime * parameter - 1
    n = (prime + 1) * b - 1
    A = (prime * n - 1) // 4
    R = (prime - 1) * n - 1
    K = A * (prime - 1)
    T = prime * prime * parameter - (prime + 1) // 2
    return b, n, A, R, K, T


def raw_divide_side(selected: int, residual: int, prime: int) -> tuple[int, int]:
    if selected % prime:
        raise AssertionError("selected raw side is not divisible by its edge prime")
    next_selected = selected // prime
    next_other = residual - next_selected
    if gcd(next_selected, next_other) != 1:
        raise AssertionError("unexpected gcd reduction in a bottom raw edge")
    return next_selected, next_other


def capacity_peel(
    selected: int, residual: int, capacity: int, forced_first: int | None = None
) -> int:
    endpoint = gcd(selected, capacity)
    peel_factors = factorization(selected // endpoint)
    peel_order: list[int] = []
    if forced_first is not None:
        if peel_factors.get(forced_first, 0) == 0:
            raise AssertionError("forced raw edge is absent")
        peel_order.append(forced_first)
        peel_factors[forced_first] -= 1
    for prime, exponent in sorted(peel_factors.items()):
        peel_order.extend([prime] * exponent)

    other = residual - selected
    for prime in peel_order:
        if valuation(selected, prime) <= valuation(capacity, prime):
            raise AssertionError("raw capacity peel stopped early")
        selected, other = raw_divide_side(selected, residual, prime)
    if selected != endpoint or other != residual - endpoint:
        raise AssertionError("raw capacity endpoint changed")
    return endpoint


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    bundle = 1
    for prime, exponent in factorization(value).items():
        if exponent > valuation(capacity, prime):
            bundle *= prime**exponent
    return bundle, value // bundle


def verify_cycle_and_binary_exit() -> None:
    p = P
    b, n, A, R, K, T = chart(p, CYCLE_R)
    C = (p * p - 1) // 2
    anchors = (1, 74, 5_403, 394_420, 1)
    bundles = (
        50_425_674_983,
        690_634_823,
        9_460_727,
        3_731_499_554_323,
    )

    if not (
        is_prime(p)
        and p % 24 == 1
        and (b, n, A, R, K)
        == (
            700_356_597,
            51_826_388_177,
            945_831_584_230,
            3_731_499_948_743,
            68_099_874_064_560,
        )
        and A == (p + 1) // 2 * T
        and K == C * T
        and p * R + 1 == 4 * K
        and gcd(R, K) == 1
    ):
        raise AssertionError("fixed a=1 chart changed")

    for index, (anchor, next_anchor) in enumerate(zip(anchors, anchors[1:])):
        departure = R - anchor
        bundle, beta = complete_excess(departure, K)
        endpoint = capacity_peel(departure, R, K, forced_first=p)
        if not (
            K % (anchor * next_anchor) == 0
            and gcd(anchor, next_anchor) == 1
            and valuation(departure, p) == 1
            and endpoint == gcd(departure, K) == next_anchor
            and departure > next_anchor
            and bundle == bundles[index]
            and beta == next_anchor
            and bundle % p == 0
        ):
            raise AssertionError(f"four-cycle edge {index} changed")

    anchor = 74
    departure = R - anchor
    y = departure // p
    x = R - y
    if not (
        valuation(departure, p) == 1
        and 4 * K == p * p * y + p * anchor + 1
        and gcd(y, 4 * K) == gcd(y, p * anchor + 1)
        and gcd(x, 4 * K) == gcd(x, p * y + 1)
        and gcd(x, K) == 5_330
    ):
        raise AssertionError("binary peeled-node identity changed")

    alternate_anchors = (5_330, 3, 20, 3)
    for anchor, next_anchor in zip(alternate_anchors, alternate_anchors[1:]):
        departure = R - anchor
        if capacity_peel(departure, R, K) != next_anchor:
            raise AssertionError("alternate capacity orbit changed")

    for anchor, expected_capacity in ((3, 10), (20, 4)):
        departure = R - anchor
        bundle, beta = complete_excess(departure, K)
        multiplier = bundle // gcd(A, bundle)
        target_capacity = (-pow(multiplier, -1, p)) % p
        target_support = lcm(A, bundle)
        target_K = target_support * target_capacity
        target_R = (4 * target_K - 1) // p
        if not (
            bundle % p != 0
            and beta == gcd(departure, K)
            and multiplier > 1
            and target_capacity == expected_capacity < p - 1
            and target_support == A * multiplier
            and p * target_R + 1 == 4 * target_K
        ):
            raise AssertionError(f"p-free binary exit at anchor {anchor} changed")

    if Fraction(4, p) != (
        Fraction(1, 20) + Fraction(1, 219) + Fraction(1, 4_380)
    ):
        raise AssertionError("fixed p=73 terminal-first certificate changed")


def verify_long_transient() -> None:
    p = P
    _, _, _, R, K, T = chart(p, LONG_TRANSIENT_R)
    C = (p * p - 1) // 2
    anchors = [1]
    for _ in range(8):
        anchors.append(p * anchors[-1] + 1)

    required_modulus = 1
    for anchor in anchors[1:]:
        required_modulus = lcm(required_modulus, anchor // gcd(anchor, C))

    forbidden_classes = ((-pow(2, -1, p)) % p, p - 1)
    if not (
        T % required_modulus == 0
        and LONG_TRANSIENT_R % p not in forbidden_classes
        and anchors[-1] == 817_660_926_503_721
    ):
        raise AssertionError("fixed CRT transient fixture changed")

    for index, (anchor, next_anchor) in enumerate(zip(anchors, anchors[1:])):
        departure = R - anchor
        selected, _ = raw_divide_side(departure, R, p)
        if not (
            K % (anchor * next_anchor) == 0
            and gcd(anchor, next_anchor) == 1
            and valuation(departure, p) == 1
            and gcd(departure, K) == next_anchor
            and gcd(selected, K) == next_anchor
            and departure > next_anchor
        ):
            raise AssertionError(f"eight-edge transient step {index} changed")


def verify() -> None:
    verify_cycle_and_binary_exit()
    verify_long_transient()
    print(
        "verified 1 exact four-cycle, 4 p-containing bundles, 1 eight-edge "
        "p-primary transient, 1 binary complement exit, and 2 strict p-free capacities"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify to run the fixed receipt")
    verify()


if __name__ == "__main__":
    main()
