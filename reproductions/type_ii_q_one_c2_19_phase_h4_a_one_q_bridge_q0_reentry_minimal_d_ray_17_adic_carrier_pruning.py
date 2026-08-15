#!/usr/bin/env python3
"""Verify the 17-adic H3-to-H4 carrier cut on three minimal-D rays.

The calculation is a congruence proof over each entire arithmetic
progression.  It does not scan primes, H4 payloads, denominators, or reach
histories.
"""

from __future__ import annotations

import argparse

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    h3_data,
    selector_a,
)
from type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_nonminimal_d_lift_finite_phase_exclusion import (
    minimal_d_ray_screen,
)


MODULUS = 17
H3_CAPACITY_DENOMINATOR = 2_261
EXPECTED_PRUNED = (
    (15, 431, 17, 14, 2),
    (83, 1723, 17, 11, 4),
    (117, 2046, 17, 6, 13),
)


def h3_pre_capacity_mod_17() -> int:
    """Evaluate the selector-free H3 carrier M3 at p == -1 modulo 17."""
    p = MODULUS - 1
    inverse_p = pow(p, -1, MODULUS)
    inverse_two = pow(2, -1, MODULUS)

    m0 = (p - 1) * (2 * p + 1) * (2 * p * p - 3 * p - 1)
    m0 = m0 * pow(8, -1, MODULUS) % MODULUS
    k0 = 2 * m0 % MODULUS
    r0 = (4 * k0 - 1) * inverse_p % MODULUS
    q0 = (r0 - 1) * inverse_two % MODULUS
    c1 = (2 * p + 4) * pow(3, -1, MODULUS) % MODULUS
    m1 = m0 * q0 % MODULUS
    k1 = m1 * c1 % MODULUS
    r1 = (4 * k1 - 1) * inverse_p % MODULUS
    q1 = (r1 - 1) * inverse_two % MODULUS
    c2 = (13 * p + 16) * pow(19, -1, MODULUS) % MODULUS
    m2 = m1 * q1 % MODULUS
    k2 = m2 * c2 % MODULUS
    r2 = (4 * k2 - 1) * inverse_p % MODULUS
    q2 = (r2 - 1) * inverse_two % MODULUS
    m3 = m2 * q2 % MODULUS

    if (m0, q0, c1, m1, q1, c2, m2, q2, m3) != (1, 13, 12, 13, 11, 10, 7, 13, 6):
        raise AssertionError("the selector-free H3 recurrence modulo 17 changed")
    return m3


def h3_q3_mod_17(prime: int, c3_mod_17: int, m3_mod_17: int) -> int:
    """Use p*q3 + (p+1)/2 == 2*M3*c3 modulo 17."""
    if prime % MODULUS != MODULUS - 1:
        raise AssertionError("ray point left p == -1 modulo 17")
    # Here w=(p+1)/2 is zero, so -q3=2*M3*c3 modulo 17.
    return (-2 * m3_mod_17 * c3_mod_17) % MODULUS


def prune_d_seventeen_rays() -> dict[str, object]:
    """Prove q3 is a 17-unit on every minimal-D ray with d == 17."""
    m3_mod_17 = h3_pre_capacity_mod_17()
    pruned: list[tuple[int, int, int, int, int]] = []

    for u, selector, d, _delta_d, first, step in minimal_d_ray_screen()["rays"]:
        if d != MODULUS:
            continue
        if not (
            first % MODULUS == MODULUS - 1
            and step % MODULUS == 0
            and step % H3_CAPACITY_DENOMINATOR == 0
            and step % (MODULUS * H3_CAPACITY_DENOMINATOR) == 0
            and selector_a(first) == selector_a(first + step) == selector
        ):
            raise AssertionError("d=17 ray no longer preserves the H3 17-adic input")

        first_data = h3_data(first)
        next_data = h3_data(first + step)
        c3 = int(first_data["c_3"])
        next_c3 = int(next_data["c_3"])
        q3 = (int(first_data["R_3"]) - 1) // 2
        next_q3 = (int(next_data["R_3"]) - 1) // 2
        c3_mod_17 = c3 % MODULUS
        q3_mod_17 = h3_q3_mod_17(first, c3_mod_17, m3_mod_17)

        # c3(p + step) - c3(p) is exact.  Its 17-divisibility makes the
        # displayed c3 residue valid for every nonnegative ray parameter.
        c3_increment = selector * (step // H3_CAPACITY_DENOMINATOR)
        if not (
            next_c3 - c3 == c3_increment
            and c3_increment % MODULUS == 0
            and int(first_data["M_3"]) % MODULUS == m3_mod_17
            and int(next_data["M_3"]) % MODULUS == m3_mod_17
            and q3 % MODULUS == q3_mod_17
            and next_q3 % MODULUS == q3_mod_17
            and q3_mod_17 != 0
        ):
            raise AssertionError("d=17 ray lost its all-parameter 17-adic obstruction")
        pruned.append((u, selector, d, c3_mod_17, q3_mod_17))

    result = {"m3_mod_17": m3_mod_17, "pruned": tuple(pruned)}
    expected = {"m3_mod_17": 6, "pruned": EXPECTED_PRUNED}
    if result != expected:
        raise AssertionError(f"d=17 17-adic carrier map changed: {result}")
    return result


def verify() -> None:
    pruning = prune_d_seventeen_rays()
    print(
        "verified 17-adic H3-to-H4 carrier pruning: "
        f"{len(pruning['pruned'])} minimal-D rays have 17 not dividing q3"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact ray congruence proof")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
