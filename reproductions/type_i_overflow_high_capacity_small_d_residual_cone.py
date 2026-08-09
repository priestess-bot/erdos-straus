#!/usr/bin/env python3
"""Verify the high-capacity small-d route split and residual cone."""

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


def divisors(value: int) -> list[int]:
    factors: list[tuple[int, int]] = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        factors.append((remaining, 1))

    values = [1]
    for prime, exponent in factors:
        values = [
            base * prime**power
            for base in values
            for power in range(exponent + 1)
        ]
    return sorted(values)


def factor_route(p: int, n: int, M: int, d: int, A: int, b: int) -> dict[str, int]:
    g = smallest_prime_factor(b)
    assert 1 < g and b % g == 0 and d * g < p
    target_M, target_d = M // g, d * g
    assert target_M < M and target_M % A == 0
    assert p * n == 4 * target_M * target_d + 1
    R = 4 * target_M - n
    K = target_M * (p - target_d)
    assert R > 0 and R % 4 == 3 and K > 0 and p * R + 1 == 4 * K
    return {"M": target_M, "d": target_d, "n": n, "g": g}


def exchange_route(p: int, n: int, M: int, d: int, A: int, b: int) -> dict[str, int]:
    assert d < b < p
    target_M, target_d = A * d, b
    assert target_M < M and target_M % A == 0
    assert p * n == 4 * target_M * target_d + 1
    R = 4 * target_M - n
    K = target_M * (p - target_d)
    assert R > 0 and R % 4 == 3 and K > 0 and p * R + 1 == 4 * K
    return {"M": target_M, "d": target_d, "n": n}


def fold_route(p: int, n: int, M: int, d: int, A: int, carrier: int) -> dict[str, int]:
    B = (p - 1) ** 2 // 4
    assert 2 * A <= carrier <= B and M % carrier == 0
    assert (M * d) % carrier == 0 and B // carrier < B // A
    quotient, remainder = divmod(M * d // carrier, p)
    assert 1 <= remainder < p
    target_n = n - 4 * carrier * quotient
    assert target_n > 0 and p * target_n == 4 * carrier * remainder + 1
    R = 4 * carrier - target_n
    K = carrier * (p - remainder)
    assert R > 0 and R % 4 == 3 and K > 0 and p * R + 1 == 4 * K
    return {"M": carrier, "d": remainder, "n": target_n, "h": quotient}


def classify(p: int, n: int, M: int, d: int, A: int) -> str:
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4
    assert is_prime(p) and p % 24 == 1 and p >= 73
    assert B < M and M >= 2 * B and c <= A <= B and M % A == 0
    assert 1 <= d < p and d * d < p and p * n == 4 * M * d + 1
    r = M % p
    assert 1 <= r < p
    s, remainder = divmod(4 * r * d + 1, p)
    assert remainder == 0 and 1 <= s <= 4 * d - 1
    P = r * d
    assert c <= P <= B
    b = M // A
    assert b > 1 and b != p

    if P >= 2 * A:
        assert P > A and B // P < B // A
        R, K = 4 * P - s, P * (p - 1)
        assert R > 0 and R % 4 == 3 and p * R + 1 == 4 * K
        return "dual"

    g = smallest_prime_factor(b)
    if d * g < p:
        factor_route(p, n, M, d, A, b)
        return "factor"
    if d < b < p:
        exchange_route(p, n, M, d, A, b)
        return "exchange"
    middle_divisors = [candidate for candidate in divisors(b) if 2 * A <= candidate <= B]
    if middle_divisors:
        carrier = max(middle_divisors)
        fold_route(p, n, M, d, A, carrier)
        return "cofactor_divisor_fold"

    assert P < 2 * A and b > p and not middle_divisors
    assert d * smallest_prime_factor(b) >= p
    assert b > B or b < 2 * A
    if b < 2 * A:
        assert A > (p - 1) // 2
        return "high_support_residual"
    assert b >= 2 * A and b > B
    if is_prime(b):
        return "ultra_prime_residual"
    return "composite_gap_residual"


def verify() -> None:
    fixtures = {
        "dual": (73, 1129, 5151, 4, 51),
        "factor": (73, 145, 2646, 1, 49),
        "exchange": (73, 337, 3075, 2, 75),
        "cofactor_divisor_fold": (73, 161, 2938, 1, 26),
        "intermediate_divisor_fold": (73, 27505, 501966, 1, 18),
        "high_support_residual": (73, 317, 5785, 1, 65),
        "ultra_prime_residual": (73, 1585, 28926, 1, 18),
        "composite_gap_residual": (73, 23381, 426703, 1, 53),
    }
    routes = {name: classify(*fixture) for name, fixture in fixtures.items()}
    assert routes == {
        **{name: name for name in fixtures if name != "intermediate_divisor_fold"},
        "intermediate_divisor_fold": "cofactor_divisor_fold",
    }
    print("verified high-capacity small-d route split and residual cone")
    for name, fixture in fixtures.items():
        p, n, M, d, A = fixture
        r = M % p
        P = r * d
        b = M // A
        middle_divisors = [candidate for candidate in divisors(b) if 2 * A <= candidate <= (p - 1) ** 2 // 4]
        print(name, "p", p, "n", n, "M", M, "d", d, "A", A, "r", r, "P", P, "b", b, "middle", middle_divisors)


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
