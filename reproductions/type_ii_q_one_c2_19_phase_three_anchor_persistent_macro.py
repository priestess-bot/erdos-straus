#!/usr/bin/env python3
"""Verify the q=1 receiver-to-third-anchor persistent macro arithmetic.

The receiver-to-H0 source repair and persistent parent are supplied by the
existing q=1 relay claim.  This reproducer checks the exact new internal word,
its source gates, and its endpoint E5 comparison at two fixed phase primes.
"""

from __future__ import annotations

import argparse
from math import gcd


MODULUS = 2_261


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def macro_data(prime: int) -> dict[str, int]:
    if not (is_prime(prime) and prime % 24 == 1 and prime % 912 == 769):
        raise AssertionError("control is not a q=1 high C=2 core prime")

    boundary = (prime - 1) ** 2 // 4
    receiver_support = (prime - 1) * (2 * prime + 1) // 4
    receiver_residual = prime * (2 * prime - 3)
    receiver_k = receiver_support * (prime - 1)

    f = 2 * prime * prime - 3 * prime - 1
    support_0 = receiver_support * (f // 2)
    capacity_0 = 2
    k_0 = support_0 * capacity_0
    r_0 = (4 * k_0 - 1) // prime
    q_0 = (r_0 - 1) // 2

    capacity_1 = (2 * prime + 4) // 3
    support_1 = support_0 * q_0
    k_1 = support_1 * capacity_1
    r_1 = (4 * k_1 - 1) // prime
    q_1 = (r_1 - 1) // 2

    capacity_2 = (13 * prime + 16) // 19
    support_2 = support_1 * q_1
    k_2 = support_2 * capacity_2
    r_2 = (4 * k_2 - 1) // prime
    q_2 = (r_2 - 1) // 2

    selector = (-1536 * pow(prime, -1, MODULUS)) % MODULUS
    if selector == 0:
        raise AssertionError("third p-anchor selector is not canonical")
    capacity_3 = (1536 + selector * prime) // MODULUS
    support_3 = support_2 * q_2
    k_3 = support_3 * capacity_3
    r_3 = (4 * k_3 - 1) // prime

    if not (
        prime * receiver_residual + 1 == 4 * receiver_k
        and receiver_support > boundary
        and receiver_k // receiver_support == prime - 1
        and receiver_residual % prime == 0
        and support_0 == (prime - 1) * (2 * prime + 1) * f // 8
        and prime * r_0 + 1 == 4 * k_0
        and prime * r_1 + 1 == 4 * k_1
        and prime * r_2 + 1 == 4 * k_2
        and prime * r_3 + 1 == 4 * k_3
        and r_0 % prime == 4
        and r_1 % prime == (25 * pow(6, -1, prime)) % prime
        and r_2 % prime == (3173 * pow(912, -1, prime)) % prime
        and gcd(r_0 - 1, k_0) == 2
        and gcd(r_1 - 1, k_1) == 2
        and gcd(r_2 - 1, k_2) == 2
        and gcd(q_0, support_0) == 1
        and gcd(q_1, support_1) == 1
        and gcd(q_2, support_2) == 1
        and q_0 % prime != 0
        and q_1 % prime != 0
        and q_2 % prime != 0
        and support_3 > support_0 > prime * prime > boundary
        and 1 <= capacity_3 <= prime - 2
        and k_3 // support_3 == capacity_3
        and (capacity_2 * pow(q_2, -1, prime)) % prime == capacity_3
        and (0, capacity_3) < (0, prime - 1)
    ):
        raise AssertionError(f"p={prime}: persistent macro endpoint changed")

    return {
        "prime": prime,
        "receiver_capacity": prime - 1,
        "capacity_1": capacity_1,
        "capacity_2": capacity_2,
        "capacity_3": capacity_3,
        "R_3": r_3,
    }


def verify() -> None:
    first = macro_data(769)
    second = macro_data(15_361)
    if not (
        is_prime(3_797)
        and 3_797 % 912 != 769
        and (first["receiver_capacity"], first["capacity_1"], first["capacity_2"], first["capacity_3"])
        == (768, 514, 527, 535)
        and (second["receiver_capacity"], second["capacity_1"], second["capacity_2"], second["capacity_3"])
        == (15_360, 10_242, 10_511, 89)
    ):
        raise AssertionError("the fixed persistent macro controls changed")
    print(
        "verified q=1 C=2 receiver-to-third-anchor macro: "
        "endpoint capacity p-1 -> c3 <= p-2"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run exact phase controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
