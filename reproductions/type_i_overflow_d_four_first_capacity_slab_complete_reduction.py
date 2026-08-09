#!/usr/bin/env python3
"""Verify the new d=4 dual fixed-s branch and its small-d composition."""

from __future__ import annotations

import argparse


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def smallest_prime_factor(value: int) -> int:
    if value % 2 == 0:
        return 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return divisor
        divisor += 2
    return value


def verify_dual_fixed_s(prime: int, denominator: int, carrier: int, support: int) -> dict[str, int]:
    p, n, M, A, d = prime, denominator, carrier, support, 4
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4
    assert is_prime(p) and p % 24 == 1
    assert 4 * p - 7 <= n <= 8 * p - 17
    assert p * n == 16 * M + 1
    assert B < M < 2 * B
    assert 1 <= A < c and M % A == 0
    assert 4 * M - n > p

    r = M % p
    assert 1 <= r < p
    s, remainder = divmod(16 * r + 1, p)
    assert remainder == 0
    P = 4 * r
    assert c <= P <= B
    if p % 16 == 1:
        assert (s, P) == (1, c)
    else:
        assert p % 16 == 9
        assert (s, P) == (9, (9 * p - 1) // 4)
    assert A < P and 4 * P > s
    assert B // P < B // A

    R = 4 * P - s
    K = P * (p - 1)
    assert R > 0 and K > 0
    assert R < 4 * P
    assert R % 4 == 3
    assert p * R + 1 == 4 * K
    assert K % P == 0
    assert P == r * d
    return {"p": p, "n": n, "M": M, "A": A, "r": r, "s": s, "P": P, "R": R, "K": K}


def verify_small_d_route(
    prime: int,
    carrier: int,
    depth: int,
    denominator: int,
    support: int,
    expected_route: str,
    expected_target: tuple[int, int, int],
) -> str:
    p, M, d, n, A = prime, carrier, depth, denominator, support
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4
    assert is_prime(p) and p % 24 == 1
    assert p * n == 4 * M * d + 1
    assert B < M < 2 * B and c <= A <= B and M % A == 0
    assert d * d < p and 4 * M - n > p
    b = M // A
    assert 1 < b < 2 * (p - 1) and b != p

    if b <= d:
        g = smallest_prime_factor(b)
        assert 1 < g <= b and d * g < p
        target = (M // g, d * g, n)
        route = "factor"
    elif b < p:
        target = (A * d, b, n)
        route = "exchange"
    else:
        h, delta = divmod(M * d // b, p)
        target = (b, delta, n - 4 * b * h)
        route = "fold"
        assert b > 2 * A and A < b <= B and B // b < B // A and 1 <= delta < p

    target_M, target_d, target_n = target
    R = 4 * target_M - target_n
    K = target_M * (p - target_d)
    assert target == expected_target and route == expected_route
    assert target_M < M and R > 0 and R % 4 == 3
    assert K > 0 and p * R + 1 == 4 * K
    if route == "fold":
        assert B // target_M < B // A
    else:
        assert target_M % A == 0 and K % A == 0
    return route


def verify() -> None:
    dual_receipts = {
        "p73_mod9": verify_dual_fixed_s(73, 297, 1355, 5),
        "p97_mod1": verify_dual_fixed_s(97, 385, 2334, 6),
    }
    assert dual_receipts["p73_mod9"]["s"] == 9
    assert dual_receipts["p97_mod1"]["s"] == 1

    delegated = {
        "d4_factor_b2": (73, 1428, 4, 313, 714, "factor", (714, 8, 313)),
        "d4_factor_b3": (73, 1647, 4, 361, 549, "factor", (549, 12, 361)),
        "d4_exchange": (73, 1355, 4, 297, 271, "exchange", (1084, 5, 297)),
        "d4_quotient_fold": (73, 1501, 4, 329, 19, "fold", (79, 3, 13)),
    }
    routes = {
        name: verify_small_d_route(*values) for name, values in delegated.items()
    }
    assert routes == {
        "d4_factor_b2": "factor",
        "d4_factor_b3": "factor",
        "d4_exchange": "exchange",
        "d4_quotient_fold": "fold",
    }
    print("verified d=4 first-capacity-slab dual and small-d composition")
    for name, receipt in dual_receipts.items():
        print(name, "dual_fixed_s", receipt["s"], receipt["P"])
    for name, route in routes.items():
        print(name, "small_d", route)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
