#!/usr/bin/env python3
"""Verify strict descent rays from fixed Type-I normal charts."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    """Use trial division only for the named control parameters."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def fixed_chart_ray(*, A: int, B: int, R: int, C: int) -> dict[str, int]:
    """Recover a Type-I certificate and its explicit normal-tail descent."""
    if not (
        A > 0
        and B > 0
        and R >= 3
        and R % 4 == 3
        and C > 0
        and gcd(A, B) == 1
    ):
        raise ValueError("normal-chart parameters are not admissible")
    H = A * R - B
    m_numerator = 4 * B * B * C + 1
    if H <= B or m_numerator % R:
        raise ValueError("normal-chart integrality or range gate failed")
    m = m_numerator // R
    p = 4 * A * B * C - m
    x = A * B * C
    y = A * C * H
    K = B * C * H
    d = A * A * C
    L = (R + 1) // gcd(R + 1, 4 * B * (A + B))
    if C % L:
        raise ValueError("fixed chart does not pass the exact descent divisor gate")
    if 4 * K % (R + 1):
        raise AssertionError("fixed-chart gate did not imply source integrality")
    n = 4 * K // (R + 1)
    if not (
        p % 24 == 1
        and 3 <= m <= p - 2
        and x == (p + m) // 4
        and x * x % d == 0
        and (p * x + d) % m == 0
        and 4 * K == p * R + 1
        and 2 <= n
        and n < p
        and 4 * x * y * K == n * (x * y + x * K + y * K)
        and 4 * x * y * (p * K) == p * (x * y + x * (p * K) + y * (p * K))
    ):
        raise AssertionError("normal-chart certificate or strict lift failed")
    return {
        "A": A,
        "B": B,
        "R": R,
        "H": H,
        "C": C,
        "m": m,
        "p": p,
        "x": x,
        "d": d,
        "y": y,
        "K": K,
        "n": n,
        "L": L,
    }


def canonical_core_ray(*, A: int, B: int, R: int, C0: int, t: int) -> dict[str, int]:
    """Use the minimal C-step preserving the chart, descent gate, and core class."""
    if t < 0:
        raise ValueError("ray parameter must be nonnegative")
    H = A * R - B
    L = (R + 1) // gcd(R + 1, 4 * B * (A + B))
    lam = 6 // gcd(6, B * H * L)
    record = fixed_chart_ray(A=A, B=B, R=R, C=C0 + lam * R * L * t)
    base = fixed_chart_ray(A=A, B=B, R=R, C=C0)
    if not (
        record["C"] == C0 + lam * R * L * t
        and record["m"] == base["m"] + 4 * B * B * L * lam * t
        and record["p"] == base["p"] + 4 * B * H * L * lam * t
        and record["p"] % 24 == 1
        and record["L"] == L
    ):
        raise AssertionError("canonical core-ray parameterization failed")
    return {**record, "lambda": lam}


def select_from_prime(*, p: int, A: int, B: int, R: int) -> dict[str, int] | None:
    """Recover the exact fixed-chart descent witness from its p-level divisor gate."""
    if not (p > 1 and p % 24 == 1 and A > 0 and B > 0 and R % 4 == 3):
        raise ValueError("p or fixed-chart parameters are not admissible")
    if gcd(A, B) != 1:
        raise ValueError("normal-chart parameters are not coprime")
    H = A * R - B
    L = (R + 1) // gcd(R + 1, 4 * B * (A + B))
    divisor = 4 * B * H * L
    if H <= B or (p * R + 1) % divisor:
        return None
    C = (p * R + 1) // (4 * B * H)
    record = fixed_chart_ray(A=A, B=B, R=R, C=C)
    if not (
        record["p"] == p
        and record["L"] == L
        and C % L == 0
        and (p * R + 1) % divisor == 0
        and record["n"] == (p * R + 1) // (R + 1)
    ):
        raise AssertionError("p-level fixed-chart selector did not reconstruct its witness")
    return record


def verify() -> None:
    b3_first = canonical_core_ray(A=1, B=3, R=23, C0=7, t=0)
    b3_later = canonical_core_ray(A=1, B=3, R=23, C0=7, t=4)
    b1_l3_first = canonical_core_ray(A=1, B=1, R=23, C0=63, t=0)
    b1_l3_later = canonical_core_ray(A=1, B=1, R=23, C0=63, t=2)
    b27_first = canonical_core_ray(A=2, B=27, R=35, C0=19, t=0)
    b27_later = canonical_core_ray(A=2, B=27, R=35, C0=19, t=210)
    assert select_from_prime(p=73, A=1, B=3, R=23) == {k: v for k, v in b3_first.items() if k != "lambda"}
    assert select_from_prime(p=241, A=1, B=1, R=23) == {k: v for k, v in b1_l3_first.items() if k != "lambda"}
    assert select_from_prime(p=1953001, A=2, B=27, R=35) == {k: v for k, v in b27_later.items() if k != "lambda"}
    assert select_from_prime(p=241, A=1, B=3, R=23) is None
    assert b3_first == {
        "A": 1,
        "B": 3,
        "R": 23,
        "H": 20,
        "C": 7,
        "m": 11,
        "p": 73,
        "x": 21,
        "d": 7,
        "y": 140,
        "K": 420,
        "n": 70,
        "L": 1,
        "lambda": 1,
    }
    assert b3_later == {
        "A": 1,
        "B": 3,
        "R": 23,
        "H": 20,
        "C": 99,
        "m": 155,
        "p": 1033,
        "x": 297,
        "d": 99,
        "y": 1980,
        "K": 5940,
        "n": 990,
        "L": 1,
        "lambda": 1,
    }
    assert b1_l3_first == {
        "A": 1,
        "B": 1,
        "R": 23,
        "H": 22,
        "C": 63,
        "m": 11,
        "p": 241,
        "x": 63,
        "d": 63,
        "y": 1386,
        "K": 1386,
        "n": 231,
        "L": 3,
        "lambda": 1,
    }
    assert b1_l3_later == {
        "A": 1,
        "B": 1,
        "R": 23,
        "H": 22,
        "C": 201,
        "m": 35,
        "p": 769,
        "x": 201,
        "d": 201,
        "y": 4422,
        "K": 4422,
        "n": 737,
        "L": 3,
        "lambda": 1,
    }
    assert b27_first["p"] == 2521 and b27_first["n"] == 2451 and b27_first["L"] == 1 and b27_first["lambda"] == 2
    assert b27_later == {
        "A": 2,
        "B": 27,
        "R": 35,
        "H": 43,
        "C": 14719,
        "m": 1226303,
        "p": 1953001,
        "x": 794826,
        "d": 58876,
        "y": 1265834,
        "K": 17088759,
        "n": 1898751,
        "L": 1,
        "lambda": 2,
    }
    assert is_prime(b3_first["p"]) and is_prime(b3_later["p"])
    assert is_prime(b1_l3_first["p"]) and is_prime(b1_l3_later["p"])
    assert is_prime(b27_first["p"]) and is_prime(b27_later["p"])
    assert gcd(73, 240) == gcd(2521, 9288) == 1
    assert b27_first["x"] % b27_first["d"] != 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified fixed normal-chart Type-I strict descent rays")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
