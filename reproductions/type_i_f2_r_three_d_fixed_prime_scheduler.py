#!/usr/bin/env python3
"""Replay fixed-prime R=3 mixed-D arithmetic scheduler controls.

The finite-table theorem is algebraic. This script only checks a few exact
rows and the prime-D/partial-contact boundaries; it is not a global scan.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


def factor(value: int) -> tuple[int, ...]:
    result: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            result.append(divisor)
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result.append(value)
    return tuple(result)


def divisors(value: int) -> tuple[int, ...]:
    factors = factor(value)
    result = {1}
    for prime in sorted(set(factors)):
        exponent = factors.count(prime)
        result = {
            base * prime**power
            for base in result
            for power in range(exponent + 1)
        }
    return tuple(sorted(result))


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return len(factor(value)) == 1 and factor(value)[0] == value


def table(prime: int) -> list[dict[str, int | str]]:
    """Enumerate the finite arithmetic table for one fixed prime."""
    rows: list[dict[str, int | str]] = []
    for A in range(1, prime):
        if 4 * A * A > prime - 5:
            break
        for C in range(1, (prime - 5) // (4 * A * A) + 1):
            M = prime + 4 * A * A * C
            for h in divisors(M):
                if not (3 <= h <= (2 * prime - 5) // 3):
                    continue
                if (h + 1) % (4 * A * C):
                    continue
                K = (h + 1) // (4 * A * C)
                m = M // h
                B = K * m - A
                if m % 4 != 3 or not (3 <= m <= prime - 2):
                    outcome = "FAMILY_EMPTY"
                elif B < A:
                    outcome = "FAMILY_EMPTY"
                elif gcd(A, B) != 1:
                    outcome = "FAMILY_EMPTY"
                else:
                    g = gcd(h, 2 * prime - 3)
                    outcome = (
                        "NON_D_CONTACT"
                        if g == 1
                        else "FULL_CONTACT"
                        if g == h
                        else "TERMINAL"
                    )
                rows.append(
                    {
                        "A": A,
                        "C": C,
                        "h": h,
                        "K": K,
                        "m": m,
                        "B": B,
                        "outcome": outcome,
                    }
                )
    return rows


def reconstruct(prime: int, row: dict[str, int | str]) -> Fraction:
    if row["outcome"] != "TERMINAL":
        raise AssertionError("only mixed rows reconstruct a terminal")
    A, B, C, m = (int(row[key]) for key in ("A", "B", "C", "m"))
    x = A * B * C
    d = A * A * C
    y = prime * (x + d) // m
    z = prime * (x + x * x // d) // m
    if (x + d) % m or (x + x * x // d) % m:
        raise AssertionError("mixed row lost integer reconstruction")
    value = sum((Fraction(1, term) for term in (x, y, z)), Fraction())
    if value != Fraction(4, prime):
        raise AssertionError("mixed row lost the 4/p identity")
    return value


def verify() -> None:
    if not is_prime(769) or 769 % 24 != 1:
        raise AssertionError("terminal control prime changed")
    rows_769 = table(769)
    terminal = [
        row for row in rows_769
        if (row["A"], row["C"], row["h"]) == (1, 14, 55)
    ]
    if len(terminal) != 1 or terminal[0]["outcome"] != "TERMINAL":
        raise AssertionError("positive mixed-D table row changed")
    reconstruct(769, terminal[0])

    rows_2521 = table(2_521)
    if any(row["outcome"] == "TERMINAL" for row in rows_2521):
        raise AssertionError("prime-D control acquired a mixed row")

    rows_1777 = table(1_777)
    if any(
        row["A"] == 1 and row["C"] == 46 and row["h"] == 3_127
        for row in rows_1777
    ):
        raise AssertionError("partial-only h row entered the finite table")
    if not any(row["outcome"] == "FAMILY_EMPTY" for row in rows_1777):
        raise AssertionError("fixed-prime empty rows disappeared")
    print("verified fixed-prime mixed-D table, terminal reconstruction, and empty boundaries")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
