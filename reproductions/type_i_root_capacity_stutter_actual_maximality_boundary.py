#!/usr/bin/env python3
"""Verify fixed counterexamples to relaxing root-stutter actual maximality."""

from __future__ import annotations

import argparse
from math import gcd


def factor(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("factorization input must be positive")
    result: dict[int, int] = {}
    for q in (2, 3):
        while n % q == 0:
            result[q] = result.get(q, 0) + 1
            n //= q
    q, step = 5, 2
    while q * q <= n:
        while n % q == 0:
            result[q] = result.get(q, 0) + 1
            n //= q
        q += step
        step = 6 - step
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def complete_excess(z: int, capacity: int) -> tuple[int, int]:
    capacity_factors = factor(capacity)
    q_block = 1
    for q, exponent in factor(z).items():
        if exponent > capacity_factors.get(q, 0):
            q_block *= q**exponent
    return q_block, z // q_block


def valuation(n: int, q: int) -> int:
    exponent = 0
    while n % q == 0:
        exponent += 1
        n //= q
    return exponent


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


def check_shadow_stutter(p: int, h: int, D0: int, m: int, e: int) -> None:
    a = e * m - h
    F = e * e * m * m - e * e * m + e * e + e * m - 2 * e + 1
    if not (
        D0 == m * p + 1 - h
        and e * D0 == p * h + 1
        and a > 0
        and p * a == e * (h - 1) + 1
        and (p * p + p + 1) % h == 0
        and F % h == 0
        and D0 % p == (1 - h) % p
    ):
        raise AssertionError("relaxed shadow stutter gate changed")


def check_actual_receipt(s: dict[str, int]) -> None:
    if not (
        s["Q"] * s["beta"] == s["z"]
        and s["E"] * s["D"] == s["z"]
        and s["K"] % s["D"] == 0
        and s["g_A"] == gcd(s["A"], s["Q"])
    ):
        raise AssertionError("canonical complete-excess receipt changed")


def verify_residual_absorption_control() -> None:
    # This control has the core congruence and h<p, but p is deliberately composite.
    p, r = 54_481, 2_543_533_812
    D0, m, e = 696_191, 13, 944
    s = chart(p, r)
    expected = {
        "M": 989_411_281,
        "u": 4_021,
        "h": 12_063,
        "T": 7_549_664_564_784_026_891,
        "z": 822_626_550_030_848_606_861_936,
        "Q": 73_850_652_158_571_481,
        "beta": 11_139_056,
        "g_A": 1,
        "E": 73_850_652_158_571_481,
        "D": 11_139_056,
    }
    if any(s[key] != value for key, value in expected.items()):
        raise AssertionError("residual-absorption control changed")
    check_actual_receipt(s)
    if not (p % 24 == 1 and p == 7 * 43 * 181 and 2 <= s["h"] < p):
        raise AssertionError("core-congruent proper-root boundary changed")
    check_shadow_stutter(p, s["h"], D0, m, e)
    if not (s["z"] % D0 == 0 and s["K"] % D0 == 0):
        raise AssertionError("shadow divisor no longer lies in z and K")
    if factor(s["z"]) != {
        2: 4,
        19: 1,
        421: 1,
        743: 1,
        937: 1,
        9_232_485_580_519: 1,
    }:
        raise AssertionError("residual-absorption z factorization changed")
    if factor(s["K"]) != {
        2: 4,
        3: 1,
        5: 1,
        227: 1,
        743: 1,
        937: 1,
        1321: 1,
        4021: 1,
        27241: 1,
        2_041_561: 1,
    }:
        raise AssertionError("residual-absorption K factorization changed")
    if not (
        valuation(s["z"], 2) == valuation(s["K"], 2) == valuation(s["D"], 2) == 4
        and s["D"] == 16 * D0
        and (p * s["h"] + 1) % s["D"] == 0
        and D0 % p == (1 - s["h"]) % p
        and s["D"] % p != (1 - s["h"]) % p
    ):
        raise AssertionError("residual capacity was incorrectly treated as optional")


def verify_normalization_absorption_control() -> None:
    # This control is prime, but deliberately outside p=1 mod 24 and h<p.
    p, r = 67, 25_311
    D0, m, e = 779, 13, 8
    s = chart(p, r)
    expected = {
        "M": 1_519,
        "u": 31,
        "h": 93,
        "T": 113_621_045,
        "z": 15_221_828_264,
        "Q": 19_540_216,
        "beta": 779,
        "g_A": 2,
        "E": 9_770_108,
        "D": 1_558,
    }
    if any(s[key] != value for key, value in expected.items()):
        raise AssertionError("normalization-absorption control changed")
    check_actual_receipt(s)
    if not (p % 24 != 1 and s["h"] > p):
        raise AssertionError("prime non-core boundary changed")
    check_shadow_stutter(p, s["h"], D0, m, e)
    if not (s["z"] % D0 == 0 and s["K"] % D0 == 0):
        raise AssertionError("shadow divisor no longer lies in z and K")
    if factor(s["z"]) != {2: 3, 19: 1, 41: 1, 2_442_527: 1}:
        raise AssertionError("normalization-absorption z factorization changed")
    if factor(s["K"]) != {
        2: 2,
        3: 1,
        5: 1,
        11: 1,
        17: 1,
        19: 1,
        31: 1,
        41: 1,
        941: 1,
    }:
        raise AssertionError("normalization-absorption K factorization changed")
    if not (
        valuation(s["z"], 2) == 3
        and valuation(s["K"], 2) == 2
        and valuation(s["A"], 2) == valuation(s["D"], 2) == 1
        and s["D"] == 2 * D0
        and s["g_A"] == 2
        and (p * s["h"] + 1) % s["D"] == 0
        and D0 % p == (1 - s["h"]) % p
        and s["D"] % p != (1 - s["h"]) % p
    ):
        raise AssertionError("normalization factor was incorrectly discarded")


def verify() -> None:
    verify_residual_absorption_control()
    verify_normalization_absorption_control()
    print("verified two fixed boundaries for root-stutter actual maximality")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
