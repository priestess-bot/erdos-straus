#!/usr/bin/env python3
"""Verify the c=8 marker affine-lift and source-allocation identities.

The two stored rows are formal arithmetic controls: they verify the exact
marker equations and source-factor allocation, but do not assert that their q
is a prime factor of V or that they are actual raw endpoints.  No parameter,
prime, or certificate search is performed.
"""

from __future__ import annotations

import argparse
from math import gcd


# One control with 47 | s and one with 47 | (176s+5).  They are deliberately
# formal controls for the algebraic equivalence, not claimed raw receipts.
FORMAL_CONTROLS = ((141, 367), (67, 1423))


def source_data(s: int) -> tuple[int, int, int, int]:
    """Return p, L, E, M in the c=8 high-R source normal form."""
    p = 48 * s + 1
    linear = 176 * s + 5
    quadratic = 3168 * s * s + 24 * s - 1
    support = 9 * s * linear * quadratic
    return p, linear, quadratic, support


def marker_lift(s: int, rho: int) -> dict[str, int]:
    """Reconstruct the exact c=1, g_b=47 arithmetic lift from rho."""
    p, linear, quadratic, support = source_data(s)
    affine = 1 + p * rho
    n, remainder = divmod(affine, 32)
    if remainder:
        raise AssertionError("rho does not give an integral marker lift")
    q = p * p + p - 1 - 47 * n
    carry = 32 * p + 32 - 47 * rho
    return {
        "p": p,
        "L": linear,
        "E": quadratic,
        "M": support,
        "rho": rho,
        "A": affine,
        "n": n,
        "q": q,
        "lambda": carry,
    }


def odd_part(value: int) -> int:
    """Remove the entire dyadic part of a positive integer."""
    while value % 2 == 0:
        value //= 2
    return value


def verify_marker_parity_table() -> None:
    """Check the two residue implications used in the parity exclusion."""
    rows = []
    for n_mod_2 in range(2):
        q_mod_2 = (1 - n_mod_2) % 2
        rows.append((n_mod_2, q_mod_2))
    if tuple(rows) != ((0, 1), (1, 0)):
        raise AssertionError("marker parity table changed")

    mod_three_rows = []
    for n_mod_3 in range(3):
        q_mod_3 = (1 - 2 * n_mod_3) % 3
        rho_mod_3 = (2 * n_mod_3 - 1) % 3
        mod_three_rows.append((n_mod_3, q_mod_3, rho_mod_3))
    if tuple(mod_three_rows) != ((0, 1, 2), (1, 2, 1), (2, 0, 0)):
        raise AssertionError("marker mod-three table changed")

    dyadic_rows = tuple((n_mod_16, (1 + n_mod_16) % 16) for n_mod_16 in range(16))
    if tuple(n for n, q in dyadic_rows if q == 1) != (0,):
        raise AssertionError("zero-epsilon dyadic q residue map changed")


def verify_formal_controls() -> None:
    """Replay exact lift, parity, and source-factor identities on two controls."""
    expected = (
        {
            "s": 141,
            "p": 6769,
            "rho": 367,
            "n": 77632,
            "q": 42177425,
            "lambda": 199391,
            "rho_mod_192": 175,
            "rho_mod_1536": 367,
        },
        {
            "s": 67,
            "p": 3217,
            "rho": 1423,
            "n": 143056,
            "q": 3628673,
            "lambda": 36095,
            "rho_mod_192": 79,
            "rho_mod_1536": 1423,
        },
    )
    rows = []
    for s, rho in FORMAL_CONTROLS:
        data = marker_lift(s, rho)
        p, linear, quadratic, support = (
            data["p"],
            data["L"],
            data["E"],
            data["M"],
        )
        affine, n, q, carry = (
            data["A"],
            data["n"],
            data["q"],
            data["lambda"],
        )
        in_s = s % 47 == 0
        in_linear = linear % 47 == 0
        if not (in_s ^ in_linear):
            raise AssertionError("47 must have exactly one c=8 source allocation")
        reduced_s = s // 47 if in_s else s
        reduced_linear = linear // 47 if in_linear else linear
        source_odd = odd_part(reduced_s)
        h_polynomial = rho * rho - 18 * rho - 11

        if not (
            support % 47 == 0
            and gcd(n, support // 47) == 1
            and gcd(support, p * p + p - 1 - q) == 47
            and p * carry == 32 * q + 79
            and affine == 32 * n
            and affine - rho * (p - 1) == 1 + rho
            and 3 * linear == 11 * p + 4
            and rho * (11 * p + 4) - 11 * affine == 4 * rho - 11
            and 8 * quadratic == 11 * p * p - 18 * p - 1
            and p * h_polynomial - affine * (rho - 11 * p) == 8 * quadratic * rho
            and gcd(source_odd, 1 + rho) == 1
            and gcd(reduced_linear, 4 * rho - 11) == 1
            and gcd(quadratic, affine) == 1
            and gcd(quadratic, h_polynomial) == gcd(quadratic, rho - 11 * p)
            and s % 2 == 1
            and n % 16 == 0
            and q % 2 == 1
            and q % 16 == 1
            and p % 96 == 49
            and n % 3 == 1
            and q % 3 == 2
            and carry % 3 == 2
            and (p * rho) % 64 == 63
            and (p * rho) % 512 == 511
        ):
            raise AssertionError("c=8 marker affine allocation identities changed")

        expected_rho = 175 if s % 4 == 1 else 79
        if rho % 192 != expected_rho:
            raise AssertionError("marker parity-refined rho ray changed")
        rows.append(
            {
                "s": s,
                "p": p,
                "rho": rho,
                "n": n,
                "q": q,
                "lambda": carry,
                "rho_mod_192": rho % 192,
                "rho_mod_1536": rho % 1536,
            }
        )
    if tuple(rows) != expected:
        raise AssertionError("stored marker affine controls changed")


def verify() -> None:
    verify_marker_parity_table()
    verify_formal_controls()
    print(
        "verified c=8 marker affine lift: parity excludes even s, epsilon=0 "
        "forces q=1 mod 16, and source allocation reduces to three rho polynomials"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
