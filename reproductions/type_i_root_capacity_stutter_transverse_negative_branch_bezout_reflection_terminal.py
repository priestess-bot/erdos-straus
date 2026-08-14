#!/usr/bin/env python3
"""Verify fixed q-local negative-root Bezout and reflection-terminal controls."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


LOW_GAPS = (3, 7, 11, 23)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def valuation(value: int, prime: int) -> int:
    """Return v_prime(value) for a nonzero fixed integer control."""
    if value == 0:
        raise AssertionError("valuation control unexpectedly vanished")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def verify_negative_root_bezout(
    p: int, q: int, h: int, m: int, s: int
) -> tuple[int, int, int, int, int]:
    """Check q-local negative-root identities, never an actual receipt."""
    if not (is_prime(p) and p % 24 == 1 and is_prime(q) and s in LOW_GAPS):
        raise AssertionError("control did not retain a core prime and a prime low-gap carrier")
    if q % (2 * s) != 2 * s - 1:
        raise AssertionError("carrier lost the even-K negative-root residue")

    k, remainder = divmod(q + 1, s)
    if remainder or k <= 1 or k % 2:
        raise AssertionError("carrier did not define an even negative-root K")
    l = k - 1
    local_d = m * p + 1 - h
    d_star = local_d // gcd(local_d, h * h - 1)
    if local_d <= 0 or local_d % q or d_star % q:
        raise AssertionError("carrier left the q-local transverse residual")
    if (p * h + 1) % q or (m + h * (h - 1)) % q:
        raise AssertionError("q-local stutter curve congruences changed")
    if h % 3 or (s * (h - 1) + 1) % q:
        raise AssertionError("control did not select the low-gap negative root")
    if (l * p - 1) % q or (k * p + 1) % q == 0:
        raise AssertionError("control did not select the negative linear branch")
    if m % q != (-l * (l + 1)) % q:
        raise AssertionError("negative-root m residue changed")

    t, remainder = divmod(l * p - 1, q)
    if remainder or t <= 0:
        raise AssertionError("negative linear quotient did not define t")
    b, remainder = divmod((s - 1) * p + s, q)
    if remainder or b <= 0:
        raise AssertionError("negative branch did not define the Bezout B")
    if p != s * t + b or l * b - (s - 1) * t != 1:
        raise AssertionError("negative-root Bezout normal form changed")

    if (p * h + 1) % local_d == 0:
        raise AssertionError("q-local control accidentally claims to be a full receipt")
    return l, t, b, local_d, d_star


def verify_l_one_overlap() -> None:
    p, q, h, m, s = 241, 5, 39, 18, 3
    l, t, b, local_d, d_star = verify_negative_root_bezout(p, q, h, m, s)
    if (l, t, b, local_d, d_star) != (1, 48, 97, 4300, 215):
        raise AssertionError("L=1 overlap control changed")
    if (s, q) != (3, 5) or any(value % q for value in (p - 1, h + 1, m + 2)):
        raise AssertionError("L=1 control left the p-minus-one overlap")
    baseline = valuation(p - 1, q)
    if (baseline, valuation(h + 1, q), valuation(m + 2, q)) != (1, 1, 1):
        raise AssertionError("L=1 overlap valuation alignment changed")
    if valuation(local_d, q) != 2 or valuation(d_star, q) != 1:
        raise AssertionError("L=1 q-primary excess did not survive in D-star")


def verify_pure_t_branch(p: int, q: int, h: int, m: int, s: int) -> tuple[int, int, int]:
    """Check the L>1 exclusions that put a q-local carrier on the T side."""
    l, t, b, local_d, d_star = verify_negative_root_bezout(p, q, h, m, s)
    if l <= 1:
        raise AssertionError("pure-T control did not retain L greater than one")
    if (p * p - 1) % q == 0 or (2 * p + 1) % q == 0:
        raise AssertionError("L greater than one p-side exclusion changed")
    if m % q == 0 or (m + 2) % q == 0 or (m - 1) % q == 0:
        raise AssertionError("L greater than one m-side exclusion changed")
    if (h * h - 1) % q == 0:
        raise AssertionError("pure-T control unexpectedly entered the H overlap")
    if valuation(local_d, q) != valuation(d_star, q):
        raise AssertionError("pure-T q-primary height did not survive in D-star")
    return l, t, b


def verify_reflection_terminal() -> None:
    p, q, h, m, s = 769, 23, 39, 13, 3
    l, t, b = verify_pure_t_branch(p, q, h, m, s)
    if (l + 1) % (4 * (s - 1)):
        raise AssertionError("reflection divisibility changed")
    c = (l + 1) // (4 * (s - 1))
    if q != 4 * s * c * (s - 1) - 1 or b < s:
        raise AssertionError("reflection raw-ray parameters changed")
    mu, remainder = divmod(s + b, s - 1)
    if remainder:
        raise AssertionError("reflection certificate gap lost integrality")
    x = s * b * c
    d = s * s * c
    if d > x or (x * x) % d or (x + d) % mu:
        raise AssertionError("reflection data did not reconstruct a Type II divisor certificate")
    value = (
        Fraction(1, x)
        + Fraction(1, p * s * c * (s - 1))
        + Fraction(1, p * b * c * (s - 1))
    )
    if value != Fraction(4, p):
        raise AssertionError("reflection raw-ray denominators did not recover 4/p")
    if (l, t, b, c, mu, x, d) != (7, 234, 67, 1, 35, 201, 9):
        raise AssertionError("reflection control changed")


def verify() -> None:
    verify_l_one_overlap()
    # These two controls are pure T-side normal forms; neither is a reflection hit.
    if verify_pure_t_branch(313, 17, 12, 4, 3) != (5, 92, 37):
        raise AssertionError("first Bezout control changed")
    if verify_pure_t_branch(3313, 41, 36, 11, 7) != (5, 404, 485):
        raise AssertionError("second Bezout control changed")
    verify_reflection_terminal()
    print("verified q-local negative-root overlap/T-side split and reflection Type II terminal")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
