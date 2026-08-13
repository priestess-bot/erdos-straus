#!/usr/bin/env python3
"""Verify fixed controls for the general h=3u endpoint divisor gate."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def factor(n: int) -> dict[int, int]:
    result: dict[int, int] = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            result[q] = result.get(q, 0) + 1
            n //= q
        q = 3 if q == 2 else q + 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    q_block = 1
    capacity_factors = factor(capacity)
    for q, exponent in factor(value).items():
        if exponent > capacity_factors.get(q, 0):
            q_block *= q**exponent
    return q_block, value // q_block


def chart(p: int, r: int) -> dict[str, int]:
    g = (p + 1) // 2
    M = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, M)
    h = 3 * u
    T = p * p * r - g
    A = g * T
    K = A * (p - 1)
    R = 2 * p**3 * r - p * p - 2 * p * r - p + 1
    z = R - h
    Q, beta = complete_excess(z, K)
    g_A = gcd(A, Q)
    E = Q // g_A
    D = beta * g_A
    return locals()


def verify_hard_strict() -> None:
    s = chart(313, 271)
    expected = {
        "M": 32_761,
        "u": 181,
        "h": 543,
        "T": 26_549_442,
        "A": 4_168_262_394,
        "K": 1_300_497_866_928,
        "R": 16_619_781_047,
        "z": 16_619_780_504,
        "Q": 2_077_472_563,
        "beta": 8,
        "g_A": 1,
        "E": 2_077_472_563,
        "D": 8,
    }
    if any(s[key] != value for key, value in expected.items()):
        raise AssertionError("hard-root complete-excess receipt changed")
    p = s["p"]
    h = s["h"]
    D = s["D"]
    c = (D * pow(h - 1, -1, p)) % p
    if not (
        9 * s["u"] ** 2 > p
        and s["K"] % (h * D) == 0
        and gcd(h, s["z"]) == 1
        and (p * h + 1) % D == 0
        and c == 298 < p - 1
        and (-pow(s["E"], -1, p)) % p == c
    ):
        raise AssertionError("hard-root strict divisor gate changed")


def verify_saturated_boundary() -> None:
    s = chart(73, 900)
    if not (
        s["M"] == s["u"] == 1801
        and s["h"] == 5403
        and s["z"] == 700_088_396
        and s["z"] % 73 == 0
        and s["E"] % 73 == 0
        and gcd(s["h"], s["z"]) == 1
    ):
        raise AssertionError("unique non-p-free root layer changed")


def verify_relaxed_gate_controls() -> None:
    controls = (
        (361, 1029, 55),
        (67, 93, 779),
    )
    for p, h, divisor in controls:
        if not (
            (p * p + p + 1) % h == 0
            and (p * h + 1) % divisor == 0
            and divisor % p == (1 - h) % p
        ):
            raise AssertionError("relaxed abstract divisor-gate control changed")


def verify() -> None:
    verify_hard_strict()
    verify_saturated_boundary()
    verify_relaxed_gate_controls()
    print(
        "verified one actual hard-root strict receipt, the saturated p-free boundary, "
        "and two relaxed abstract stutter-gate controls"
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
