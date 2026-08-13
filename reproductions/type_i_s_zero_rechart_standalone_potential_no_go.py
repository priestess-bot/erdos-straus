#!/usr/bin/env python3
"""Verify focused controls for the formal s=0 standalone-potential no-go."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt


def prime_support(n: int) -> set[int]:
    support: set[int] = set()
    q = 2
    while q * q <= n:
        if n % q == 0:
            support.add(q)
            while n % q == 0:
                n //= q
        q = 3 if q == 2 else q + 2
    if n > 1:
        support.add(n)
    return support


def valuation(n: int, p: int) -> int:
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent


def normal_state(p: int, r: int) -> dict[str, int | tuple[int, int]]:
    g = (p + 1) // 2
    C = (p * p - 1) // 2
    T = p * p * r - g
    A = g * T
    K = C * T
    R = 2 * p**3 * r - p * p - 2 * p * r - p + 1
    J = (R - (p + 1)) // p
    U = (p * p + 1) // 2
    V = (p * p + p + 1) // 3
    capacities = (2 * gcd(r + g, U), 3 * gcd(2 * r + 1, V))
    return {
        "r": r,
        "T": T,
        "A": A,
        "K": K,
        "R": R,
        "J": J,
        "height": 1 + valuation(J, p),
        "capacities": capacities,
    }


def phi(p: int, r: int, t: int) -> int:
    T = int(normal_state(p, r)["T"])
    return r + t * T


def verify_formal_controls() -> None:
    p = 73
    r0 = 1
    r1 = phi(p, r0, 4)
    r2 = phi(p, r1, 2)
    states = [normal_state(p, r) for r in (r0, r1, r2)]
    if not (
        (r1, int(states[1]["T"])) == (21_169, 112_809_564)
        and (r2, int(states[2]["T"])) == (225_640_297, 1_202_437_142_676)
        and [state["height"] for state in states] == [1, 2, 1]
        and [state["capacities"] for state in states] == [(2, 3)] * 3
        and r2 == phi(p, r0, 42_638)
        and (1 + p * p * 4) * (1 + p * p * 2) == 1 + p * p * 42_638
    ):
        raise AssertionError("formal height/composition control changed")

    g = (p + 1) // 2
    C = (p * p - 1) // 2
    for state in states:
        T = int(state["T"])
        A = int(state["A"])
        K = int(state["K"])
        if not (A == g * T and K == C * T and K == (p - 1) * A):
            raise AssertionError("projective s=0 invariants changed")

    # Reusing one multiplier changes the state but not its prime-support set.
    repeated_t = 1
    repeated_L = 1 + p * p * repeated_t
    k0 = int(states[0]["K"])
    k1 = repeated_L * k0
    k2 = repeated_L * k1
    if not (k2 != k1 and prime_support(k2) == prime_support(k1)):
        raise AssertionError("equal-support formal edge control changed")

    # One fixed CRT injection control; the general statement is proved in text.
    Q = 25 * 7 * 11
    t = (-pow(p * p, -1, Q)) % Q
    if (1 + p * p * t) % Q != 0:
        raise AssertionError("finite-support CRT injection changed")


def verify_p97_reset(j: int) -> None:
    p = 97
    U = (p * p + 1) // 2
    V = (p * p + p + 1) // 3
    D0 = U * V
    k = 14_392_062 + D0 * j
    r = 66_988_440 + 4_243_815_461_730_835_674_059_638_914_706_837_844_637 * k
    E = 369_377_901_007 + 23_400_629_237_489_299_674_263_740_436_419_983_401_253_504 * k
    source = normal_state(p, r)
    T = int(source["T"])
    A = int(source["A"])
    K = int(source["K"])
    R = int(source["R"])
    t = (E - 1) // (p * p)
    target_r = r + t * T
    target = normal_state(p, target_r)

    if not (
        source["capacities"] == (2, 3)
        and target["capacities"] == (9410, 9507)
        and E % D0 == 0
        and gcd(T, D0) == 1
        and E % (p * p) == 1
        and gcd(E, A) == gcd(E, K) == 1
        and R - 58 == 331 * E
        and K % (58 * 331) == 0
    ):
        raise AssertionError("p=97 conditional capacity-reset control changed")

    if j == 0:
        if not (
            r == 61_077_255_241_788_814_332_878_114_958_073_522_084_029_059_934
            and E == 336_783_306_824_958_725_248_583_556_712_863_459_150_180_685_186_255
            and t == 35_793_740_761_500_555_345_794_830_132_093_044_866_636_272_206
            and (r + 49) % U == 2583
            and (2 * r + 1) % V == 1849
            and T % U == 2122
            and T % V == 1300
            and t % U == 1
            and t % V == 3072
        ):
            raise AssertionError("p=97 representative residue table changed")


def verify() -> None:
    verify_formal_controls()
    verify_p97_reset(0)
    verify_p97_reset(1)
    if Fraction(1, 28) + Fraction(1, 194) + Fraction(1, 2716) != Fraction(4, 97):
        raise AssertionError("p=97 terminal-first control changed")
    print(
        "verified formal semigroup/height/support controls and two source-side "
        "receipt-associated conditional p=97 capacity resets"
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
