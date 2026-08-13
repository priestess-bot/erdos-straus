#!/usr/bin/env python3
"""Verify the proper-root h<p stutter exclusion on fixed receipts."""

from __future__ import annotations

import argparse
from math import gcd


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0) + 1
            n //= q
        q = 3 if q == 2 else q + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    cap = factor(capacity)
    q_block = 1
    for q, exponent in factor(value).items():
        if exponent > cap.get(q, 0):
            q_block *= q**exponent
    return q_block, value // q_block


def receipt(prime: int, r: int) -> dict[str, int]:
    m0 = (prime * prime + prime + 1) // 3
    u = gcd(2 * r + 1, m0)
    h = 3 * u
    g = (prime + 1) // 2
    t_value = prime * prime * r - g
    a_value = g * t_value
    k_value = a_value * (prime - 1)
    r_value = 2 * prime**3 * r - prime * prime - 2 * prime * r - prime + 1
    z_value = r_value - h
    q_block, beta = complete_excess(z_value, k_value)
    g_a = gcd(a_value, q_block)
    e_value = q_block // g_a
    d_value = beta * g_a
    return {
        "p": prime,
        "r": r,
        "m0": m0,
        "u": u,
        "h": h,
        "A": a_value,
        "K": k_value,
        "R": r_value,
        "z": z_value,
        "E": e_value,
        "D": d_value,
    }


def verify_receipt(data: dict[str, int]) -> None:
    p, h, m0, d = data["p"], data["h"], data["m0"], data["D"]
    z, k = data["z"], data["K"]
    if not (
        data["u"] < m0
        and h < p
        and k % h == 0
        and k % d == 0
        and z % d == 0
        and gcd(h, z) == 1
        and (p * h + 1) % d == 0
    ):
        raise AssertionError("fixed root receipt no longer satisfies actual hypotheses")

    # The stutter congruence would force D=mp+1-h for m>=1.
    if (d - (1 - h)) % p == 0:
        raise AssertionError("the fixed proper-root receipt entered the stutter gate")

    c = (d * pow(h - 1, -1, p)) % p
    if not 1 <= c <= p - 2:
        raise AssertionError("strict canonical cofactor bound changed")


def verify_algebra(p: int, h: int, m: int) -> None:
    """Check the symbolic identities used after assuming the stutter gate."""
    if not (0 < h < p and m >= 1):
        raise AssertionError("invalid symbolic test parameters")
    d = m * p + 1 - h
    if d <= 0:
        raise AssertionError("the hypothetical divisor must be positive")
    if (p * h + 1) + p * d != m * p * p + p + 1:
        raise AssertionError("first divisibility identity changed")
    if m * (p * p + p + 1) - (m * p * p + p + 1) != (m - 1) * (p + 1):
        raise AssertionError("remainder identity changed")
    g_plus = gcd(d, p + 1)
    if gcd(d // g_plus, (p + 1) // g_plus) != 1:
        raise AssertionError("gcd cancellation precondition changed")
    if d - (m - 1) * (h - 1) != m * (p - h + 1):
        raise AssertionError("strict size identity changed")
    if not d > (m - 1) * (h - 1):
        raise AssertionError("proper-root size contradiction changed")

    # The two divisibility consequences are checked conditionally, exactly as
    # in the proof; the fixed parameter choices need not enter the stutter gate.
    if (p * h + 1) % d == 0:
        if ((m - 1) * (p + 1)) % d != 0:
            raise AssertionError("stutter divisibility remainder changed")
        if (h - 1) % g_plus != 0:
            raise AssertionError("p+1 gcd gate changed")


def verify_m_one_boundary(p: int, h: int) -> None:
    """Check the m=1 branch uses the actual cyclotomic-free receipt facts."""
    m0 = (p * p + p + 1) // 3
    d = p + 1 - h
    if d <= 1:
        raise AssertionError("fixed symbolic boundary divisor is too small")
    if gcd(d, m0) != 1 or d % 3 == 0:
        raise AssertionError("fixed receipt lost its cyclotomic-free factors")
    cyclotomic = p * p + p + 1
    if cyclotomic % d == 0 and d != 1:
        raise AssertionError("m=1 cyclotomic contradiction changed")


def verify() -> None:
    # Both receipts are proper-root examples with h<p.
    verify_receipt(receipt(73, 3))
    verify_receipt(receipt(457, 3))
    verify_m_one_boundary(73, 3)
    for p, h, m in ((73, 3, 1), (73, 3, 4), (457, 21, 2)):
        verify_algebra(p, h, m)
    print("verified proper-root h<p receipts avoid the actual stutter gate")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
