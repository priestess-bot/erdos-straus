#!/usr/bin/env python3
"""Verify complete-excess valuation pruning on the seven final minimal-D rays.

For each ray the receipt works modulo one fixed ell**2.  It proves the
displayed valuations for every ray parameter, rather than sampling primes or
H4 payloads.
"""

from __future__ import annotations

import argparse
from math import gcd

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    h3_data,
    selector_a,
)
from type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_nonminimal_d_lift_finite_phase_exclusion import (
    minimal_d_ray_screen,
)


H3_CAPACITY_DENOMINATOR = 2_261
TERMINAL_PRUNED = frozenset(
    {
        (8, 491),
        (34, 611),
        (43, 191),
        (78, 11),
        (83, 11),
        (85, 179),
        (104, 11),
    }
)
SEVENTEEN_ADIC_PRUNED = frozenset({(15, 17), (83, 17), (117, 17)})
EXPECTED_RAY_RECEIPTS = (
    # u, a, d, ell, p mod ell**2, w/ell, c3/ell, q3/ell, M3 mod ell
    (15, 431, 65, 5, 4, 3, 2, 2, 4),
    (15, 431, 221, 13, 103, 4, 3, 9, 10),
    (19, 583, 953, 953, 1905, 1, 261, 538, 826),
    (26, 317, 53, 53, 105, 1, 43, 10, 19),
    (27, 127, 1409, 1409, 2817, 1, 551, 102, 1290),
    (57, 830, 353, 353, 705, 1, 335, 215, 104),
    (104, 260, 29, 29, 57, 1, 16, 17, 14),
)


def h3_modular_data(prime: int, selector: int, modulus: int) -> tuple[int, int, int]:
    """Return M3, c3, q3 modulo a modulus of unit H3 denominators."""
    p = prime % modulus
    inverse = lambda value: pow(value % modulus, -1, modulus)
    inverse_two = inverse(2)
    f = (2 * p * p - 3 * p - 1) % modulus
    m0 = (p - 1) * (2 * p + 1) * f * inverse(8) % modulus
    k0 = 2 * m0 % modulus
    r0 = (4 * k0 - 1) * inverse(p) % modulus
    q0 = (r0 - 1) * inverse_two % modulus
    c1 = (2 * p + 4) * inverse(3) % modulus
    m1 = m0 * q0 % modulus
    k1 = m1 * c1 % modulus
    r1 = (4 * k1 - 1) * inverse(p) % modulus
    q1 = (r1 - 1) * inverse_two % modulus
    c2 = (13 * p + 16) * inverse(19) % modulus
    m2 = m1 * q1 % modulus
    k2 = m2 * c2 % modulus
    r2 = (4 * k2 - 1) * inverse(p) % modulus
    q2 = (r2 - 1) * inverse_two % modulus
    c3 = (1536 + selector * p) * inverse(H3_CAPACITY_DENOMINATOR) % modulus
    m3 = m2 * q2 % modulus
    k3 = m3 * c3 % modulus
    r3 = (4 * k3 - 1) * inverse(p) % modulus
    q3 = (r3 - 1) * inverse_two % modulus
    return m3, c3, q3


def unit_quotient(value: int, prime: int) -> int:
    """Return value/prime modulo prime after proving exact first valuation."""
    modulus = prime * prime
    residue = value % modulus
    if residue % prime or residue == 0:
        raise AssertionError("expected an exact first prime valuation")
    return residue // prime


def complete_excess_valuation_pruning() -> dict[str, object]:
    """Prove one non-excess carrier prime for every remaining ray."""
    ray_map = {
        (u, d): (selector, first, step)
        for u, selector, d, _delta_d, first, step in minimal_d_ray_screen()["rays"]
    }
    all_keys = frozenset(ray_map)
    valuation_keys = frozenset((u, d) for u, _a, d, *_rest in EXPECTED_RAY_RECEIPTS)
    if not (
        len(all_keys) == 17
        and len(TERMINAL_PRUNED) == 7
        and len(SEVENTEEN_ADIC_PRUNED) == 3
        and all_keys
        == TERMINAL_PRUNED | SEVENTEEN_ADIC_PRUNED | valuation_keys
        and not (TERMINAL_PRUNED & SEVENTEEN_ADIC_PRUNED)
        and not (TERMINAL_PRUNED & valuation_keys)
        and not (SEVENTEEN_ADIC_PRUNED & valuation_keys)
    ):
        raise AssertionError("the three-way minimal-D ray partition changed")

    receipts: list[tuple[int, int, int, int, int, int, int, int, int]] = []
    for expected in EXPECTED_RAY_RECEIPTS:
        u, selector, d, ell, p_residue, w_unit, c3_unit, q3_unit, m3_unit = expected
        actual_selector, first, step = ray_map[(u, d)]
        modulus = ell * ell
        if not (
            actual_selector == selector
            and d % ell == 0
            and gcd(ell, 2 * 3 * 19 * H3_CAPACITY_DENOMINATOR) == 1
            and first % ell == ell - 1
            and step % modulus == 0
            and step % H3_CAPACITY_DENOMINATOR == 0
            and selector_a(first) == selector_a(first + step) == selector
        ):
            raise AssertionError("remaining ray lost its fixed local valuation input")

        m3_modulus, c3_modulus, q3_modulus = h3_modular_data(first, selector, modulus)
        exact = h3_data(first)
        exact_q3 = (int(exact["R_3"]) - 1) // 2
        if not (
            (m3_modulus, c3_modulus, q3_modulus)
            == (int(exact["M_3"]) % modulus, int(exact["c_3"]) % modulus, exact_q3 % modulus)
        ):
            raise AssertionError("modular H3 recurrence no longer matches the exact receipt")

        w = (first + 1) // 2
        receipt = (
            u,
            selector,
            d,
            ell,
            first % modulus,
            unit_quotient(w, ell),
            unit_quotient(c3_modulus, ell),
            unit_quotient(q3_modulus, ell),
            m3_modulus % ell,
        )
        if not (
            receipt == expected
            and receipt[5] != 0
            and receipt[6] != 0
            and receipt[7] != 0
            and receipt[8] != 0
        ):
            raise AssertionError("remaining ray lost its exact complete-excess valuation")
        receipts.append(receipt)

    result = {
        "terminal_pruned": len(TERMINAL_PRUNED),
        "seventeen_adic_pruned": len(SEVENTEEN_ADIC_PRUNED),
        "valuation_pruned": tuple(receipts),
        "large_p_minimal_d_residual": (),
    }
    expected = {
        "terminal_pruned": 7,
        "seventeen_adic_pruned": 3,
        "valuation_pruned": EXPECTED_RAY_RECEIPTS,
        "large_p_minimal_d_residual": (),
    }
    if result != expected:
        raise AssertionError(f"complete-excess valuation pruning changed: {result}")
    return result


def verify() -> None:
    pruning = complete_excess_valuation_pruning()
    print(
        "verified minimal-D complete-excess valuation pruning: "
        f"{len(pruning['valuation_pruned'])} final rays removed and no large-p ray remains"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the whole-ray valuation receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
