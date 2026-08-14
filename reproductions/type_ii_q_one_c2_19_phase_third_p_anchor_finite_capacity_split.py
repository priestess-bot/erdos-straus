#!/usr/bin/env python3
"""Verify the third p-anchor finite capacity split in the q=1 high C=2 phase.

The finite loop is over the exact quotient u modulo 7*17, not over primes or
Egyptian-fraction solutions.  All chart assertions use exact integer algebra.
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


def phase_data(prime: int) -> dict[str, int]:
    if not (is_prime(prime) and prime % 24 == 1 and prime % 912 == 769):
        raise AssertionError("control is not a q=1 high C=2 core prime")

    f = 2 * prime * prime - 3 * prime - 1
    support_0 = (prime - 1) * (2 * prime + 1) * f // 8
    r_0 = 4 * prime**3 - 8 * prime**2 - prime + 4
    h = r_0 - 1
    q_0 = h // 2
    capacity_1 = (2 * prime + 4) // 3
    support_1 = support_0 * q_0
    k_1 = support_1 * capacity_1
    r_1 = (4 * k_1 - 1) // prime
    n_1 = 6 * (r_1 - 1)
    q_1 = (r_1 - 1) // 2
    capacity_2 = (13 * prime + 16) // 19
    support_2 = support_1 * q_1
    k_2 = support_2 * capacity_2
    r_2 = (4 * k_2 - 1) // prime
    n_2 = 912 * (r_2 - 1)
    q_2 = (r_2 - 1) // 2

    selector = (-1536 * pow(prime, -1, MODULUS)) % MODULUS
    if selector == 0:
        raise AssertionError("third p-anchor selector is not canonical")
    capacity_3 = (1536 + selector * prime) // MODULUS
    support_3 = support_2 * q_2
    k_3 = support_3 * capacity_3
    r_3 = (4 * k_3 - 1) // prime

    t = prime * prime - 2 * prime - 1
    u_polynomial = (
        16 * prime**6
        - 32 * prime**5
        - 72 * prime**4
        + 156 * prime**3
        + 37 * prime**2
        - 117 * prime
        - 38
    )

    if not (
        3_648 * k_2
        == (prime - 1) * (2 * prime + 1) * (13 * prime + 16) * f * h * n_1
        and prime * r_2 + 1 == 4 * k_2
        and r_2 % prime == (3173 * pow(912, -1, prime)) % prime
        and r_2 % 24 == 23
        and r_2 % 19 == 2
        and gcd(r_2 - 1, k_2) == 2
        and q_2 % 2 == 1
        and gcd(q_2, k_2) == 1
        and gcd(q_2, support_2) == 1
        and q_2 % prime != 0
        and selector * prime % MODULUS == (-1536) % MODULUS
        and selector % 19 == 13
        and selector % 7 != 0
        and selector % 17 != 0
        and 1 <= capacity_3 < prime
        and (capacity_2 * pow(q_2, -1, prime)) % prime == capacity_3
        and (capacity_3 < capacity_2) == (selector <= 1547)
        and prime * r_3 + 1 == 4 * k_3
    ):
        raise AssertionError(f"p={prime}: third p-anchor capacity map changed")

    # Exact divisor eliminations behind gcd(R_2 - 1, K_2)=2.
    if not (
        (n_2 + 1824) % (prime - 1) == 0
        and (n_2 - 912) % (2 * prime + 1) == 0
        and (n_2 + 171) % (13 * prime + 16) == 0
        and (n_2 + 1824 * (prime - 1)) % f == 0
        and (n_2 - 1216 * t) % h == 0
        and (n_2 - 48 * u_polynomial) % n_1 == 0
        and n_1 == prime * u_polynomial + 19 * (prime + 1)
        and n_1 % (prime + 1) == 64
        and f % (prime - 1) == (prime - 3) % (prime - 1)
        and -(prime - 3) * h + (4 * prime * prime - 12 * prime + 3) * t == 6
    ):
        raise AssertionError(f"p={prime}: third-anchor gcd proof identities changed")

    return {
        "prime": prime,
        "selector": selector,
        "capacity_1": capacity_1,
        "capacity_2": capacity_2,
        "capacity_3": capacity_3,
        "R_3": r_3,
    }


def verify_selector_quotient() -> None:
    selectors: list[int] = []
    descending = 0
    for residue in range(119):
        prime_residue = 912 * residue + 769
        if prime_residue % 7 == 0 or prime_residue % 17 == 0:
            continue
        selector = (-1536 * pow(prime_residue, -1, MODULUS)) % MODULUS
        selectors.append(selector)
        if selector <= 1547:
            descending += 1

    expected = [
        13 + 19 * k
        for k in range(119)
        if k % 7 != 3 and k % 17 != 2
    ]
    if not (
        len(selectors) == 96
        and sorted(selectors) == expected
        and descending == 64
        and len(selectors) - descending == 32
    ):
        raise AssertionError("third p-anchor finite selector quotient changed")


def verify() -> None:
    expansion = phase_data(769)
    descent = phase_data(15_361)
    verify_selector_quotient()
    if not (
        expansion["selector"] == 1_571
        and (expansion["capacity_1"], expansion["capacity_2"], expansion["capacity_3"])
        == (514, 527, 535)
        and descent["selector"] == 13
        and (descent["capacity_1"], descent["capacity_2"], descent["capacity_3"])
        == (10_242, 10_511, 89)
    ):
        raise AssertionError("the fixed third p-anchor controls changed")
    print(
        "verified q=1 high C=2 third p-anchor selector: "
        "96 residue classes, 64 capacity descents, 32 expansions"
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
