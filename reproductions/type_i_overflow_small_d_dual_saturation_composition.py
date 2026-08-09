#!/usr/bin/env python3
"""Verify d=1..8 dual saturation and small-d composition controls."""

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


def verify_dual(
    prime: int, denominator: int, carrier: int, depth: int, support: int
) -> dict[str, int]:
    p, n, M, d, A = prime, denominator, carrier, depth, support
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4
    assert is_prime(p) and p % 24 == 1 and p >= 73
    assert 1 <= d <= 8 and p * n == 4 * M * d + 1
    assert B < M < 2 * B and 1 <= A < c and M % A == 0
    assert 4 * M - n > p

    r = M % p
    assert 1 <= r < p
    s, remainder = divmod(4 * r * d + 1, p)
    assert remainder == 0 and 1 <= s <= 4 * d - 1
    P = r * d
    assert P == (s * p - 1) // 4
    assert c <= P <= B and A < P and 4 * P > s
    assert B // P < B // A

    R = 4 * P - s
    K = P * (p - 1)
    assert 0 < R < 4 * P and R % 4 == 3 and K > 0
    assert p * R + 1 == 4 * K and K % P == 0
    return {"d": d, "r": r, "s": s, "P": P, "R": R, "K": K}


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
    assert B < M < 2 * B and c <= A <= B and M % A == 0 and d * d < p
    assert 4 * M - n > p

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
    assert route == expected_route and target == expected_target
    assert target_M < M and R > 0 and R % 4 == 3
    assert K > 0 and p * R + 1 == 4 * K
    if route == "fold":
        assert B // target_M < B // A
    else:
        assert target_M % A == 0 and K % A == 0
    return route


def verify() -> None:
    dual_fixtures = (
        (73, 73, 1332, 1, 1),
        (73, 145, 1323, 2, 1),
        (73, 217, 1320, 3, 1),
        (73, 297, 1355, 4, 1),
        (73, 357, 1303, 5, 1),
        (73, 433, 1317, 6, 1),
        (73, 509, 1327, 7, 1),
        (73, 569, 1298, 8, 1),
    )
    dual_receipts = [verify_dual(*fixture) for fixture in dual_fixtures]
    assert [receipt["d"] for receipt in dual_receipts] == list(range(1, 9))

    delegated = {
        "d5_exchange": (73, 1376, 5, 377, 32, "exchange", (160, 43, 377)),
        "d6_factor": (73, 1317, 6, 433, 439, "factor", (439, 18, 433)),
        "d7_fold": (73, 1692, 7, 649, 18, "fold", (94, 53, 273)),
        "d8_factor": (73, 1298, 8, 569, 649, "factor", (649, 16, 569)),
    }
    routes = {
        name: verify_small_d_route(*values) for name, values in delegated.items()
    }
    assert routes == {
        "d5_exchange": "exchange",
        "d6_factor": "factor",
        "d7_fold": "fold",
        "d8_factor": "factor",
    }

    print("verified d=1..8 dual saturation and small-d composition")
    for receipt in dual_receipts:
        print("dual", receipt["d"], receipt["r"], receipt["s"], receipt["P"])
    for name, route in routes.items():
        print(name, route)


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
