#!/usr/bin/env python3
"""Verify the h == 6 mod 8 gap-47 terminal and marked-descent table."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


# (p mod 47, forced divisor d, least positive compatible h).
ROWS = (
    (5, 128, 102),
    (10, 256, 206),
    (11, 9, 302),
    (13, 32, 118),
    (15, 8, 310),
    (22, 18, 230),
    (23, 6, 326),
    (26, 64, 238),
    (30, 16, 246),
    (31, 4, 342),
    (35, 3, 350),
    (39, 2, 358),
    (41, 72, 174),
    (43, 1, 366),
    (44, 36, 86),
    (45, 24, 182),
    (46, 12, 278),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def factor_pair(p: int, d: int) -> tuple[int, int, int, int, int, int]:
    x = (p + 47) // 4
    g = gcd(d, x)
    A, B, C = d // g, x // g, g // (d // g)
    assert x == A * B * C and d == A * A * C and gcd(A, B) == 1
    assert (A + B) % 47 == 0
    K = (A + B) // 47
    n = (p + 47) // 48
    return x, A, B, C, K, n


def verify_row(residue: int, divisor: int, h0: int) -> None:
    assert h0 % 8 == 6
    assert (24 * h0 + 1) % 47 == residue
    assert divisor % 47 and (-4 * divisor) % 47 == residue
    assert 48 * 48 % divisor == 0

    # The two congruences have period lcm(8, 47)=376.
    prior = [h for h in range(1, h0) if h % 8 == 6 and (24 * h + 1) % 47 == residue]
    assert not prior
    assert (24 * (h0 + 376) + 1) % 47 == residue
    x0 = 6 * (h0 + 2)
    assert divisor <= x0


def verify() -> None:
    rows = {residue: (divisor, h0) for residue, divisor, h0 in ROWS}
    assert len(rows) == len(ROWS)
    for row in ROWS:
        verify_row(*row)

    quadratic_residues = {pow(value, 2, 47) for value in range(1, 47)}
    nonresidues = set(range(1, 47)) - quadratic_residues
    assert quadratic_residues == {
        1,
        2,
        3,
        4,
        6,
        7,
        8,
        9,
        12,
        14,
        16,
        17,
        18,
        21,
        24,
        25,
        27,
        28,
        32,
        34,
        36,
        37,
        42,
    }
    assert set(rows) <= nonresidues
    assert nonresidues - set(rows) == {19, 20, 29, 33, 38, 40}

    h, p = 118, 2833
    assert h % 8 == 6 and p == 24 * h + 1 and is_prime(p)
    divisor, h0 = rows[p % 47]
    assert (divisor, h0) == (32, 118)
    x, A, B, C, K, n = factor_pair(p, divisor)
    assert (x, A, B, C, K, n) == (720, 2, 45, 8, 1, 60)
    assert divisor <= x and x * x % divisor == 0 and (x + divisor) % 47 == 0

    source = (A * B * C, A * C * K, B * C * K)
    target = (source[0], p * source[1], p * source[2])
    assert source == (720, 16, 360)
    assert target == (720, 45328, 1019880)
    assert Fraction(4, n) == sum((Fraction(1, value) for value in source), Fraction())
    assert Fraction(4, p) == sum((Fraction(1, value) for value in target), Fraction())
    assert n < p

    print("verified h == 6 mod 8 gap-47 terminal and marked-descent controls")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if args.verify:
        verify()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
