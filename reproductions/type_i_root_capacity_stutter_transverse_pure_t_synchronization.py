#!/usr/bin/env python3
"""Verify a depth-two pure-T q-adic synchronization control."""

from __future__ import annotations

import argparse
from math import gcd


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def valuation(value: int, prime: int) -> int:
    """Return v_prime(value) for a nonzero fixed positive control."""
    if value <= 0:
        raise AssertionError("valuation input ceased to be positive")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def verify() -> None:
    p, q, s, ell = 230017, 17, 3, 5
    u, h, m, r = 157, 471, 4, 26297
    q_square = q * q
    m0 = (p * p + p + 1) // 3
    t_value = p * p * r - (p + 1) // 2
    d_value = m * p + 1 - h
    h_square_minus_one = h * h - 1
    d_star = d_value // gcd(d_value, h_square_minus_one)
    ph_plus_one = p * h + 1

    if not (is_prime(p) and p % 24 == 1):
        raise AssertionError("control did not retain a core prime")
    if h != 3 * u or (p * p + p + 1) % h:
        raise AssertionError("control lost its root-height shape")
    if gcd(2 * r + 1, m0) != u:
        raise AssertionError("control lost the exact root-capacity gcd")
    if t_value % u:
        raise AssertionError("root-capacity quotient T/u stopped being integral")

    k, remainder = divmod(q + 1, s)
    if remainder or k != ell + 1 or k % 2:
        raise AssertionError("control lost the even low-gap negative-root carrier")
    if (s * (h - 1) + 1) % q or (ell * p - 1) % q:
        raise AssertionError("control lost the negative-root congruences")
    if m % q != (-ell * (ell + 1)) % q:
        raise AssertionError("negative-root m residue changed")

    if (m + h * (h - 1)) % q_square:
        raise AssertionError("q-square stutter-curve lift changed")
    if ph_plus_one % q_square or d_value % q_square:
        raise AssertionError("q-square receipt-side lift changed")
    if d_value != 919598 or d_star != 459799:
        raise AssertionError("fixed q-square D control changed")
    if gcd(d_value, h_square_minus_one) != 2:
        raise AssertionError("control unexpectedly entered the H overlap")

    pure_t_exclusions = (
        h_square_minus_one,
        p * p - 1,
        2 * p + 1,
        m,
        m + 2,
        m - 1,
    )
    if any(value % q == 0 for value in pure_t_exclusions):
        raise AssertionError("control unexpectedly left the pure-T branch")
    if q % (4 * s * (s - 1)) == 4 * s * (s - 1) - 1:
        raise AssertionError("control unexpectedly hit the reflection subclass")
    if q % 4 != 1:
        raise AssertionError("control unexpectedly permits q as a raw-ray modulus")
    if ph_plus_one % d_value == 0:
        raise AssertionError("q-local control accidentally claims to be an actual receipt")

    t_over_u = t_value // u
    m_plus_two_r = m + 2 * r
    if (
        valuation(d_value, q),
        valuation(d_star, q),
        valuation(t_over_u, q),
        valuation(m_plus_two_r, q),
        valuation(ph_plus_one, q),
    ) != (2, 2, 2, 2, 2):
        raise AssertionError("q-square synchronized height changed")

    # At every q-layer carried by D, the two apparent T-side conditions coincide.
    for exponent in (1, 2):
        modulus = q**exponent
        if (t_over_u % modulus == 0) != (m_plus_two_r % modulus == 0):
            raise AssertionError("T/u and m+2r stopped being equivalent at a forced q-layer")

    d_hat = d_value // q_square
    t_hat = t_over_u // q_square
    m_hat = m_plus_two_r // q_square
    ph_hat = ph_plus_one // q_square
    if (d_hat, t_hat, m_hat, ph_hat) != (3182, 30663984088, 182, 374872):
        raise AssertionError("q-square normalized control changed")

    # This is the exact local predecessor of the actual normalized e-identity.
    if p * p * m_hat - 2 * u * t_hat != p * d_hat + ph_hat:
        raise AssertionError("normalized receipt-side difference changed")
    e_residue = ph_hat * pow(d_hat, -1, q) % q
    if e_residue != 13:
        raise AssertionError("local receipt-quotient residue changed")
    if (2 * u * t_hat - p * p * m_hat + (p + e_residue) * d_hat) % q:
        raise AssertionError("normalized q-adic receipt relation changed")

    print("verified depth-two pure-T synchronization and nonreflection control")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
