#!/usr/bin/env python3
"""Verify the H5 a=1 full-overlap finite divisor menu.

This is a finite parameter calculation. It does not scan primes, denominators,
or selector history, and it does not claim the menu has already been discharged.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    FINAL_RESIDUAL,
    base_prime,
    h3_data,
    selector_a,
)
from type_ii_q_one_c2_19_phase_maximal_fourth_anchor_completion import (
    complete_excess,
    positive_divisors,
)


D_OFFSET = 11_943_424
D_MULTIPLIER = 2_261
CAPACITY_NUMERATOR = 4_718_592
MENU_ROW_COUNT = 571_777
MENU_DISTINCT_COUNT = 377_516
MENU_MAXIMUM = 18_768_297_821_013


def anchor_step(prime: int, support: int, capacity: int) -> dict[str, int]:
    """Build one complete-excess anchor step in the local valuation lemma."""
    if (4 * support * capacity - 1) % prime:
        raise AssertionError("the proposed anchor row is not integral")
    residual = (4 * support * capacity - 1) // prime
    if residual <= 1:
        raise AssertionError("the proposed anchor does not have a positive excess side")
    block, beta = complete_excess(residual - 1, support * capacity)
    return {
        "R": residual,
        "K": support * capacity,
        "Q": block,
        "beta": beta,
        "M_next": lcm(support, block),
        "w": (prime + 1) // 2,
    }


def full_overlap_controls() -> None:
    """Check the necessary direction and explicitly retain its non-converse."""
    positive = anchor_step(73, 37, 37)
    converse = anchor_step(73, 110, 37)
    if not (
        positive
        == {"R": 75, "K": 1_369, "Q": 2, "beta": 37, "M_next": 74, "w": 37}
        and positive["M_next"] % positive["w"] == 0
        and positive["K"] % positive["w"] == 0
        and converse
        == {"R": 223, "K": 4_070, "Q": 3, "beta": 74, "M_next": 330, "w": 37}
        and converse["K"] % converse["w"] == 0
        and converse["M_next"] % converse["w"] != 0
    ):
        raise AssertionError("the full-overlap implication or its one-way boundary changed")


def h4_carrier_control(prime: int) -> dict[str, int]:
    """Rebuild an H3-to-H4 receipt and check gcd(w, M4) divides g."""
    data = h3_data(prime)
    phase_selector = int(data["a"])
    c3 = int(data["c_3"])
    m3 = int(data["M_3"])
    k3 = int(data["K_3"])
    r3 = int(data["R_3"])
    block4, beta4 = complete_excess(r3 - 1, k3)
    m4 = lcm(m3, block4)
    multiplier = m4 // m3
    c4 = c3 * pow(multiplier, -1, prime) % prime
    k4 = m4 * c4
    w = (prime + 1) // 2
    g = gcd(w, c3)
    carrier_overlap = gcd(w, m4)
    lambda_value = beta4 * gcd(m3, block4) // 2
    delta = abs(1_536 - phase_selector)
    d_value = D_OFFSET - D_MULTIPLIER * phase_selector
    lift, remainder = divmod(d_value * c4 + CAPACITY_NUMERATOR * lambda_value, prime)

    if not (
        prime % 24 == 1
        and gcd(w, m3) == 1
        and k4 % 2 == 0
        and delta % g == 0
        and g % carrier_overlap == 0
        and delta % carrier_overlap == 0
        and delta % lambda_value == 0
        and 1 <= c4 <= prime - 2
        and remainder == 0
        and lift >= 1
    ):
        raise AssertionError("the H4 carrier-overlap finite-mask contract changed")

    return {
        "p": prime,
        "selector": phase_selector,
        "g": g,
        "lambda": lambda_value,
        "d": carrier_overlap,
        "c4": c4,
        "t": lift,
    }


def finite_divisor_menu() -> dict[str, object]:
    """Enumerate the fixed (u, lambda, d, j) supermenu from the new lemma."""
    rows = 0
    constants: set[int] = set()
    maximum_record: tuple[int, int, int, int, int, int, int] | None = None

    for residue in sorted(FINAL_RESIDUAL):
        phase_selector = selector_a(base_prime(residue))
        delta = abs(1_536 - phase_selector)
        d_value = D_OFFSET - D_MULTIPLIER * phase_selector
        divisors = positive_divisors(delta)
        if not (delta > 0 and d_value > 0):
            raise AssertionError("the H3 finite selector domain changed")
        for lambda_value in divisors:
            for carrier_overlap in divisors:
                for j_value in range(1, 2 * carrier_overlap):
                    candidate = (
                        d_value * j_value
                        + 2 * carrier_overlap * CAPACITY_NUMERATOR * lambda_value
                    )
                    rows += 1
                    constants.add(candidate)
                    record = (
                        candidate,
                        residue,
                        phase_selector,
                        lambda_value,
                        carrier_overlap,
                        j_value,
                        d_value,
                    )
                    if maximum_record is None or record > maximum_record:
                        maximum_record = record

    expected_maximum = (MENU_MAXIMUM, 27, 127, 1_409, 1_409, 2_817, 11_656_277)
    if not (
        rows == MENU_ROW_COUNT
        and len(constants) == MENU_DISTINCT_COUNT
        and maximum_record == expected_maximum
    ):
        raise AssertionError("the H5 a=1 finite divisor menu changed")
    return {
        "rows": rows,
        "distinct_constants": len(constants),
        "maximum": maximum_record[0],
        "maximum_record": maximum_record[1:],
    }


def verify() -> None:
    full_overlap_controls()
    hard = h4_carrier_control(14_449)
    clean = h4_carrier_control(665_617)
    menu = finite_divisor_menu()
    if not (
        hard
        == {
            "p": 14_449,
            "selector": 431,
            "g": 5,
            "lambda": 5,
            "d": 1,
            "c4": 13_391,
            "t": 10_167_387,
        }
        and clean
        == {
            "p": 665_617,
            "selector": 431,
            "g": 1,
            "lambda": 1,
            "d": 1,
            "c4": 20_388,
            "t": 335_988,
        }
        and menu
        == {
            "rows": MENU_ROW_COUNT,
            "distinct_constants": MENU_DISTINCT_COUNT,
            "maximum": MENU_MAXIMUM,
            "maximum_record": (27, 127, 1_409, 1_409, 2_817, 11_656_277),
        }
    ):
        raise AssertionError("the H5 a=1 full-overlap finite sieve receipts changed")
    print(
        "verified the H5 a=1 full-overlap implication, two H4 finite-mask controls, "
        "and a 571777-row / 377516-constant finite divisor menu"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run fixed full-overlap receipts")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
