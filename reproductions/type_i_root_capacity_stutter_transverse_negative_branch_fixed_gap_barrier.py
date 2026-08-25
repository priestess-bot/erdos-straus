#!/usr/bin/env python3
"""Verify fixed q-local controls for the negative-root same-carrier barrier."""

from __future__ import annotations

import argparse
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


def same_carrier_candidates(s: int, r: int) -> set[int]:
    """Return all L allowed by L*r+1=t*(s*L+s-1), if any.

    The proof bounds t by t < (r + 1) / s, so this is a finite exact list
    for one fixed gap r.  It is a control for the algebra, not a search.
    """
    candidates: set[int] = set()
    for t in range(1, (r + 1) // s + 1):
        denominator = r - t * s
        numerator = t * (s - 1) - 1
        if denominator and numerator % denominator == 0:
            value = numerator // denominator
            if value > 1:
                candidates.add(value)
    return candidates


def verify_negative_local_control(p: int, q: int, h: int, m: int, s: int) -> None:
    """Check one q-local transverse negative root, not an actual receipt."""
    if not (s in LOW_GAPS and is_prime(p) and p % 24 == 1 and is_prime(q)):
        raise AssertionError("control did not use a core prime, a low gap, and a prime carrier")
    if q % (2 * s) != 2 * s - 1:
        raise AssertionError("carrier did not have the negative-root low-gap residue")

    k, remainder = divmod(q + 1, s)
    if remainder or k <= 2 or k % 2:
        raise AssertionError("carrier did not recover an even K with L greater than one")
    ell = k - 1

    local_d = m * p + 1 - h
    d_star = local_d // gcd(local_d, h * h - 1)
    if local_d <= 0 or local_d % q or d_star % q:
        raise AssertionError("q did not remain in the transverse local residual")
    if (p * h + 1) % q or (h * h - 1) % q == 0:
        raise AssertionError("q-local stutter congruences or transversality changed")
    if h % 3:
        raise AssertionError("control did not retain the h equals three-u height form")
    if (m + h * (h - 1)) % q:
        raise AssertionError("q-local finite-curve consequence changed")

    delta = m * s * s - s + 1
    positive_root = s * h - 1
    negative_root = s * (h - 1) + 1
    if delta % q or positive_root % q == 0 or negative_root % q:
        raise AssertionError("control did not select exactly the negative m-polynomial root")
    if (ell * p - 1) % q or (k * p + 1) % q == 0:
        raise AssertionError("control did not select the negative linear branch")

    for r in LOW_GAPS:
        same_carrier_gate = (p + r) % q == 0
        residue_equivalent_gate = (ell * r + 1) % q == 0
        if same_carrier_gate != residue_equivalent_gate:
            raise AssertionError("same-carrier p-plus-r gate lost its L-residue equivalence")
        if same_carrier_gate:
            raise AssertionError("control unexpectedly entered the finite low-gap menu")


def verify() -> None:
    # Both are q-local controls.  In particular, D need not divide p*h+1.
    verify_negative_local_control(313, 17, 12, 4, 3)
    verify_negative_local_control(3313, 41, 36, 11, 7)

    # The finite candidate equation excludes L=5 for every automatic low gap.
    for s in LOW_GAPS:
        for r in LOW_GAPS:
            if 5 in same_carrier_candidates(s, r):
                raise AssertionError("fixed low-gap candidate calculation changed")

    # A distinct, nonautomatic gap can still hit the same carrier; this is a boundary.
    s, ell, q, r = 3, 5, 17, 27
    t, remainder = divmod(ell * r + 1, q)
    if remainder or ell * (r - t * s) != t * (s - 1) - 1:
        raise AssertionError("same-carrier factor equation changed")

    print("verified q-local negative-root controls and finite same-carrier gap barrier")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
