#!/usr/bin/env python3
"""Verify the odd-owner scale dichotomy and small-cofactor Type II menu."""

from __future__ import annotations

import argparse
from fractions import Fraction

from type_i_core_jacobi_punctured_kernel_primary_selector import factorint
from type_i_odd_owner_fiber_incidence_lattice_source_map import (
    canonical_type_ii_vertex,
    owner_window,
)


def divisors(value: int) -> tuple[int, ...]:
    result = [1]
    for prime, exponent in factorint(value):
        previous = tuple(result)
        result += [
            base * prime**power
            for base in previous
            for power in range(1, exponent + 1)
        ]
    return tuple(sorted(result))


def small_cofactor_menu(
    p: int, q: int, j: int, s: int
) -> dict[str, object]:
    scale = q ** (j + 1)
    assert p < 4 * scale
    assert 0 < 4 * s < p
    shifted = p + 4 * s
    assert shifted % scale == 0
    k = shifted // scale
    assert k in (1, 3, 5, 7)

    D, A, C = canonical_type_ii_vertex(s)
    modulus = 4 * D
    eligible = tuple(
        factor for factor in divisors(shifted) if factor % modulus == modulus - 1
    )
    terminals: list[dict[str, object]] = []
    for h in eligible:
        assert (h + 1) % modulus == 0
        K = (h + 1) // modulus
        assert (K * p + A) % h == 0
        B = (K * p + A) // h
        assert B > A
        x = A * B * C
        y = p * A * C * K
        z = p * B * C * K
        assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        terminals.append(
            {
                "h": h,
                "K": K,
                "B": B,
                "denominators": (x, y, z),
            }
        )

    return {
        "p": p,
        "q": q,
        "j": j,
        "s": s,
        "shifted": shifted,
        "k": k,
        "D": D,
        "A": A,
        "C": C,
        "eligible": eligible,
        "terminals": terminals,
    }


def verify() -> None:
    positive = small_cofactor_menu(409, 11, 1, 49)
    assert positive["k"] == 5
    assert (positive["D"], positive["A"], positive["C"]) == (7, 7, 1)
    assert positive["eligible"] == (55,)
    assert positive["terminals"] == [
        {
            "h": 55,
            "K": 2,
            "B": 15,
            "denominators": (105, 5726, 12270),
        }
    ]

    negative = small_cofactor_menu(97, 11, 1, 6)
    assert negative["k"] == 1
    assert (negative["D"], negative["A"], negative["C"]) == (6, 1, 6)
    assert negative["eligible"] == ()
    assert negative["terminals"] == []

    full_scale = owner_window(97, 3, 1)
    rows = full_scale["rows"]
    assert isinstance(rows, list)
    deep = next(row for row in rows if row["s"] == 5)
    assert 97 > 4 * 3**2
    assert deep["height"] >= 2
    assert (97 + 4 * deep["s"]) // 3**2 == 13
    assert full_scale["full_digit_coverage"]

    print("verified odd-owner scale dichotomy and small-cofactor terminal menu")
    print("p409_q11", "s=49", "k=5", "h=55", "typeII=(105,5726,12270)")
    print("p97_q11", "s=6", "k=1", "terminal_menu=empty")
    print("p97_q3", "large_scale", "deep_cofactor=13", "full_digit_coverage")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
