#!/usr/bin/env python3
"""Replay fixed controls for the R=3 universal raw-menu boundary.

The script checks only the arithmetic menu.  It does not create a persistent
source, certify a terminal-first miss, or emulate a selector transition.
"""

from __future__ import annotations

import argparse
from math import gcd


def factor(value: int) -> tuple[int, ...]:
    """Return the prime factors of a positive fixed control, with multiplicity."""
    if value < 1:
        raise ValueError("factor input must be positive")
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors.append(divisor)
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append(value)
    return tuple(factors)


def raw_menu(prime: int) -> dict[str, object]:
    """Compute the non-p first raw menu of the R=3 universal source."""
    if prime % 24 != 1:
        raise ValueError("expected a core-prime congruence representative")
    p_plus_four = prime + 4
    chart_carrier = (3 * prime + 1) // 4
    source_coordinate = 2 * prime - 3
    if 8 * chart_carrier - 3 * source_coordinate != 11:
        raise AssertionError("R=3 Bezout identity changed")
    labels = factor(source_coordinate)
    children = tuple(
        (source_coordinate // label, (source_coordinate // label + 3) // 2,
         (source_coordinate // label + 1) // 2)
        for label in labels
    )
    if any(gcd(child[0], child[1]) != 1 for child in children):
        raise AssertionError("raw menu unexpectedly needs gcd reduction")
    return {
        "p": prime,
        "P": p_plus_four,
        "N": chart_carrier,
        "D": source_coordinate,
        "P_factors": factor(p_plus_four),
        "N_factors": factor(chart_carrier),
        "D_factors": labels,
        "children": children,
    }


def verify() -> None:
    prime_menu = raw_menu(2_521)
    if not (
        prime_menu["P_factors"] == (5, 5, 101)
        and prime_menu["N_factors"] == (31, 61)
        and prime_menu["D_factors"] == (5_039,)
        and prime_menu["children"] == ((1, 2, 1),)
    ):
        raise AssertionError("prime-D hard-core control changed")

    composite_menu = raw_menu(118_801)
    if not (
        composite_menu["P_factors"] == (5, 23_761)
        and composite_menu["N_factors"] == (89_101,)
        and composite_menu["D_factors"] == (53, 4_483)
        and all(child[0] > 1 for child in composite_menu["children"])
    ):
        raise AssertionError("composite-D non-anchor control changed")

    for menu in (prime_menu, composite_menu):
        if not (
            all(q % 4 == 1 for q in menu["P_factors"])
            and all(q % 3 == 1 for q in menu["N_factors"])
            and gcd(int(menu["D"]), int(menu["N"])) == 1
        ):
            raise AssertionError("hard-core menu control changed")
    print("verified R=3 prime-D anchor-only and composite-D non-anchor raw-menu controls")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
