#!/usr/bin/env python3
"""Verify the a=1 root coprime-capacity fan and h=3 half descent.

The script checks four fixed arithmetic controls.  It performs no prime-range,
denominator, selector-history, or historical-result scan.
"""

from __future__ import annotations

import argparse
from math import gcd


FIXTURES = (
    (73, 1, 1, 1),
    (73, 8, 1, 5),
    (73, 3, 1, 55),
    (457, 3, 7, None),
)


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    common = gcd(value, capacity)
    exposed = value // common
    block = gcd(value, pow(exposed, value.bit_length(), value))
    return block, value // block


def audit(prime: int, parameter: int, expected_u: int, expected_g: int | None) -> None:
    p = prime
    r = parameter
    root_g = (p + 1) // 2
    T = p * p * r - root_g
    A = root_g * T
    K = A * (p - 1)
    R = 2 * p**3 * r - p * p - 2 * p * r - p + 1
    root_modulus = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, root_modulus)
    h = 3 * u
    root_capacity = gcd(R - (p + 1), K)

    if not (
        4 * K == p * R + 1
        and root_capacity == 3 * u
        and u == expected_u
        and (root_modulus % u == 0)
    ):
        raise AssertionError("root capacity layer changed")

    if 9 * u * u < p:
        z = R - h
        if K % h or gcd(h, z) != 1:
            raise AssertionError("small endpoint is not a primitive capacity anchor")
        if K % z == 0:
            if K % (h * z):
                raise AssertionError("bottom Type I terminal lost its product divisor")
        else:
            Q, beta = complete_excess(z, K)
            g_A = gcd(A, Q)
            E = Q // g_A
            residual = beta * g_A
            cofactor = (-pow(E, -1, p)) % p
            if not (
                Q > 1
                and Q % p != 0
                and K % (h * residual) == 0
                and E * residual == z
                and residual % beta == 0
                and 1 <= cofactor <= p - 2
            ):
                raise AssertionError("small-endpoint strict receipt changed")

    if u != 1:
        return

    h = 3
    z = R - h
    Q_3 = z // 4
    H = (3 * p + 1) // 4
    local_g = gcd(r - 3, H)
    Q, beta = complete_excess(z, K)
    g_A = gcd(A, Q)
    E = Q // g_A
    residual = beta * g_A
    cofactor = (-pow(E, -1, p)) % p
    expected_cofactor = 2 * local_g if local_g < H else (p + 1) // 2

    if not (
        local_g == expected_g
        and Q_3 % local_g == 0
        and gcd(T, Q_3) == local_g
        and gcd(A, Q_3) == local_g
        and gcd(R - 3, K) == 4 * local_g
        and E == Q_3 // local_g
        and residual == 4 * local_g
        and E * residual == z
        and K % (3 * residual) == 0
        and cofactor == expected_cofactor
        and cofactor == (2 * local_g) % p
        and 1 <= cofactor <= (p + 1) // 2 < p - 1
        and z > gcd(z, K)
    ):
        raise AssertionError("explicit h=3 half-descent receipt changed")

    # Q need not equal Q_3; p=73,r=3 is the fixed maximal-block boundary.
    if r == 3 and not (Q != Q_3 and Q == 10_583 and beta == 220):
        raise AssertionError("maximal complete-excess boundary disappeared")


def verify() -> None:
    for fixture in FIXTURES:
        audit(*fixture)
    print(
        "verified 3 coprime-root h=3 half descents (g=1, proper, saturated) "
        "and 1 nontrivial small-capacity layer"
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
