#!/usr/bin/env python3
"""Verify the odd-h quadratic-nonresidue gap-23 Type II sieve."""

from __future__ import annotations

import argparse
import math


MODULUS = 23
QUADRATIC_RESIDUES = {1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 18}
NONRESIDUE_DIVISORS = {
    19: 1,
    15: 2,
    11: 3,
    7: 4,
    22: 6,
    14: 8,
    10: 9,
    21: 12,
    5: 16,
    20: 18,
    17: 36,
}


def type_ii_data(prime: int) -> tuple[int, int, int, int, int, int, int, int]:
    """Return d, x, n, A, B, C, K, and the first lifted tail."""
    assert prime % 24 == 1
    h = (prime - 1) // 24
    assert h % 2 == 1
    divisor = NONRESIDUE_DIVISORS[prime % MODULUS]
    x = (prime + MODULUS) // 4
    assert x == 6 * (h + 1)
    assert divisor <= x
    assert x * x % divisor == 0
    assert (x + divisor) % MODULUS == 0

    common = math.gcd(divisor, x)
    a = divisor // common
    b = x // common
    c = common // a
    k = (a + b) // MODULUS
    n = (prime + MODULUS) // (MODULUS + 1)
    assert x == a * b * c
    assert divisor == a * a * c
    assert math.gcd(a, b) == 1
    assert a <= b
    assert a + b == MODULUS * k
    assert n == h + 1 < prime
    return divisor, x, n, a, b, c, k, a * c * k


def verify_lift(prime: int) -> None:
    divisor, x, n, a, b, c, k, first_tail = type_ii_data(prime)
    second_tail = b * c * k
    target = (x, prime * first_tail, prime * second_tail)
    source = (x, first_tail, second_tail)
    assert 4 * source[0] * source[1] * source[2] == n * (
        source[0] * source[1] + source[0] * source[2] + source[1] * source[2]
    )
    assert 4 * target[0] * target[1] * target[2] == prime * (
        target[0] * target[1] + target[0] * target[2] + target[1] * target[2]
    )
    assert target[1:] == (prime * source[1], prime * source[2])

    y = prime * (x + divisor) // MODULUS
    z = prime * (x + x * x // divisor) // MODULUS
    assert target == (x, y, z)


def verify() -> None:
    nonresidues = set(range(1, MODULUS)) - QUADRATIC_RESIDUES
    assert set(NONRESIDUE_DIVISORS) == nonresidues
    assert set(NONRESIDUE_DIVISORS.values()) <= {d for d in range(1, 145) if 144 % d == 0}
    for residue, divisor in NONRESIDUE_DIVISORS.items():
        assert residue == (-4 * divisor) % MODULUS

    # The d=8 and d=16 rows exercise the two new classes beyond the old 36-table.
    verify_lift(313)
    verify_lift(1753)

    # This is the strict double-G control from the preceding obstruction claim.
    verify_lift(2521)
    assert type_ii_data(2521) == (8, 636, 106, 2, 159, 2, 7, 28)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified odd-h quadratic-nonresidue gap-23 terminals and two-tail lifts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
