#!/usr/bin/env python3
"""Verify the second p-anchor capacity expansion in the q=1 high C=2 phase.

The verification uses exact identities and two fixed prime controls.  It does
not scan a parameter interval or enumerate Egyptian-fraction solutions.
"""

from __future__ import annotations

import argparse
from math import gcd


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def phase_data(prime: int) -> dict[str, int]:
    if not (is_prime(prime) and prime % 24 == 1 and prime % 912 == 769):
        raise AssertionError("control is not a q=1 high C=2 core prime")

    f = 2 * prime * prime - 3 * prime - 1
    support_0 = (prime - 1) * (2 * prime + 1) * f // 8
    r_0 = 4 * prime**3 - 8 * prime**2 - prime + 4
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

    r_1_numerator = (
        16 * prime**7
        - 32 * prime**6
        - 72 * prime**5
        + 156 * prime**4
        + 37 * prime**3
        - 117 * prime**2
        - 19 * prime
        + 25
    )
    n = 6 * (r_1 - 1)
    h = r_0 - 1
    t = prime * prime - 2 * prime - 1

    if not (
        8 * support_0 == (prime - 1) * (2 * prime + 1) * f
        and prime * r_0 + 1 == 4 * (2 * support_0)
        and q_0 == h // 2
        and 24 * k_1 == (prime - 1) * (prime + 2) * (2 * prime + 1) * f * h
        and prime * r_1 + 1 == 4 * k_1
        and 6 * r_1 == r_1_numerator
        and r_1 % prime == (25 * pow(6, -1, prime)) % prime
        and r_1 % 24 == 23
        and r_1 % 4 == 3
        and gcd(r_1 - 1, k_1) == 2
        and q_1 % 2 == 1
        and gcd(q_1, k_1) == 1
        and gcd(q_1, support_1) == 1
        and q_1 % prime != 0
        and (13 * prime + 16) % 19 == 0
        and 2 < capacity_1 < capacity_2 < prime
        and capacity_2 - capacity_1 == (prime - 28) // 57
        and (capacity_1 * pow(q_1, -1, prime)) % prime == capacity_2
        and prime * r_2 + 1 == 4 * k_2
    ):
        raise AssertionError(f"p={prime}: second p-anchor capacity map changed")

    # Exact divisor eliminations behind gcd(R_1 - 1, K_1)=2.
    if not (
        (n + 12) % (prime - 1) == 0
        and (n - 6) % (2 * prime + 1) == 0
        and (n + 12 * (prime - 1)) % f == 0
        and (n - 8 * t) % h == 0
        and (n + 3) % (prime + 2) == 0
        and f % (prime - 1) == (prime - 3) % (prime - 1)
        and -(prime - 3) * h + (4 * prime * prime - 12 * prime + 3) * t == 6
    ):
        raise AssertionError(f"p={prime}: second-anchor gcd proof identities changed")

    return {
        "prime": prime,
        "R_1": r_1,
        "Q_1": q_1,
        "capacity_1": capacity_1,
        "capacity_2": capacity_2,
        "R_2": r_2,
    }


def verify() -> None:
    first = phase_data(769)
    second = phase_data(2593)
    if not (
        first["capacity_1"] == 514
        and first["capacity_2"] == 527
        and second["capacity_1"] == 1_730
        and second["capacity_2"] == 1_775
    ):
        raise AssertionError("the fixed second p-anchor controls changed")
    print(
        "verified q=1 high C=2 double p-anchor map: "
        "2 -> (2p+4)/3 -> (13p+16)/19"
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
