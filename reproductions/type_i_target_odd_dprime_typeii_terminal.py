#!/usr/bin/env python3
"""Verify the target-odd D'>1 canonical Type-II terminal controls."""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


def squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def terminal(
    p: int,
    D: int,
    a: int,
    D_prime: int,
    A: int,
    h: int,
) -> dict[str, int]:
    assert is_prime(p) and p % 24 == 1
    assert D % a == 0 and squarefree(D // a) and 4 * a * D < p
    assert D % D_prime == 0 and D_prime % A == 0
    assert squarefree(D_prime // A) and 4 * A * D_prime < p
    assert D_prime > 1 and h > 1

    source = p + 4 * D * a
    target = p + 4 * A * D_prime
    assert source % h == 0 and target % h == 0
    modulus = 4 * D_prime
    assert h % modulus == modulus - 1

    C = D_prime // A
    K = (h + 1) // modulus
    numerator = K * p + A
    assert numerator % h == 0
    B = numerator // h
    assert B > A

    m = (A + B) // K
    x = B * D_prime
    d = A * D_prime
    assert (A + B) % K == 0
    assert m == 4 * x - p and m % 4 == 3
    assert x * x % d == 0 and d <= x and (x + d) % m == 0

    y = p * D_prime * K
    z = p * B * C * K
    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)
    return {"h": h, "A": A, "C": C, "K": K, "B": B, "m": m, "x": x, "d": d, "y": y, "z": z}


def verify() -> None:
    p97 = terminal(97, 4, 4, 2, 1, 7)
    assert p97["x"] == 28 and p97["y"] == 194 and p97["z"] == 2716

    p313 = terminal(313, 6, 3, 2, 2, 7)
    assert p313["x"] == 90 and p313["y"] == 626 and p313["z"] == 14085

    p73, D, a, D_prime, A = 73, 4, 2, 2, 1
    source = p73 + 4 * D * a
    target = p73 + 4 * A * D_prime
    assert source == 105 and target == 81 and math.gcd(source, target) == 3
    assert 3 % (4 * D_prime) != 4 * D_prime - 1

    print("verified target-odd D'>1 canonical Type-II terminal")
    print({"p97": p97, "p313": p313, "p73": {"shared_factor": 3, "branch": "WRONG_MOD_4D_PRIME"}})


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
