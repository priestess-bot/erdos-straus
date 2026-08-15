#!/usr/bin/env python3
"""Verify H3 terminal-first pruning of minimal-D q0 re-entry phase rays.

The finite 17-ray map is imported from the existing D-lift receipt.  This
verifier does not search a prime range: it proves a congruence valid on each
whole progression, then audits the three already-known prime first points.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

import sympy

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    dispatch_h3,
    h3_data,
    selector_a,
)
from type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_nonminimal_d_lift_finite_phase_exclusion import (
    minimal_d_ray_screen,
)
from type_ii_q_one_c2_19_phase_maximal_fourth_anchor_completion import (
    complete_excess,
)


H3_CAPACITY_DENOMINATOR = 2_261
PHASE_PERIOD = 912 * 119

EXPECTED_PRUNED = (
    (8, 491, 491),
    (34, 611, 47),
    (43, 191, 191),
    (78, 11, 11),
    (83, 11, 11),
    (85, 179, 179),
    (104, 11, 11),
)
EXPECTED_RETAINED = (
    (15, 17),
    (15, 65),
    (15, 221),
    (19, 953),
    (26, 53),
    (27, 1409),
    (57, 353),
    (83, 17),
    (104, 29),
    (117, 17),
)


def first_three_mod_four_factor(value: int) -> int | None:
    """Return the least 3 mod 4 prime factor of one bounded ray divisor."""
    return next(
        (prime for prime in sorted(sympy.factorint(value)) if prime % 4 == 3),
        None,
    )


def h3_capacity(prime: int, selector: int) -> int:
    """Return c3 from its exact phase-normal form."""
    numerator = 1_536 + selector * prime
    quotient, remainder = divmod(numerator, H3_CAPACITY_DENOMINATOR)
    if remainder:
        raise AssertionError("ray point left the H3 capacity lattice")
    return quotient


def terminal_pruning_map() -> dict[str, object]:
    """Prove the whole-ray H3 terminal cut and list the residual rays."""
    pruned: list[tuple[int, int, int]] = []
    retained: list[tuple[int, int]] = []
    denominator_overlap: list[tuple[int, int]] = []

    for u, selector, d, delta_d, first, step in minimal_d_ray_screen()["rays"]:
        if not (
            delta_d == 2 * d * (4 * d * d - 2 * d + 1)
            and step % PHASE_PERIOD == 0
            and (first + 1) % (2 * d) == 0
            and first % d == d - 1
            and (selector - 1_536) % d == 0
            and selector_a(first) == selector_a(first + step) == selector
        ):
            raise AssertionError("minimal-D ray no longer preserves its H3 congruences")

        factor = first_three_mod_four_factor(d)
        if factor is None:
            retained.append((u, d))
            continue
        if gcd(d, H3_CAPACITY_DENOMINATOR) != 1:
            denominator_overlap.append((u, d))
            retained.append((u, d))
            continue

        # The same calculation holds for first + j*step because both p=-1
        # modulo d and the H3 selector remain fixed on the progression.
        for prime in (first, first + step):
            c3 = h3_capacity(prime, selector)
            w = (prime + 1) // 2
            if not (c3 % d == 0 and w % d == 0 and gcd(w, c3) % d == 0):
                raise AssertionError("ray divisor stopped entering the H3 overlap")
        pruned.append((u, d, factor))

    result = {
        "pruned": tuple(pruned),
        "retained": tuple(retained),
        "denominator_overlap": tuple(denominator_overlap),
    }
    expected = {
        "pruned": EXPECTED_PRUNED,
        "retained": EXPECTED_RETAINED,
        "denominator_overlap": (),
    }
    if result != expected:
        raise AssertionError(f"H3 terminal ray-pruning map changed: {result}")
    return result


def exact_h4_carrier(prime: int) -> tuple[int, int]:
    """Rebuild the actual maximal H4 carrier and return lambda and d4."""
    data = h3_data(prime)
    m3 = int(data["M_3"])
    k3 = int(data["K_3"])
    r3 = int(data["R_3"])
    block, beta = complete_excess(r3 - 1, k3)
    overlap = gcd(m3, block)
    lambda_value, remainder = divmod(beta * overlap, 2)
    if remainder:
        raise AssertionError("H3 maximal block no longer has an integral lambda")
    m4 = lcm(m3, block)
    d4 = gcd((prime + 1) // 2, m4)
    if not (
        lambda_value > 0
        and m4 == m3 * (block // overlap)
        and m4 % m3 == 0
    ):
        raise AssertionError("exact H4 carrier reconstruction changed")
    return lambda_value, d4


def prime_first_point_prefix_audit() -> dict[str, object]:
    """Audit all prime first points presently present in the 17-ray map."""
    terminal: list[tuple[int, int, int, int]] = []
    carrier_mismatch: list[tuple[int, int, int, int, int]] = []
    prime_first_points = 0

    for u, _selector, d, _delta_d, first, _step in minimal_d_ray_screen()["rays"]:
        if not sympy.isprime(first):
            continue
        prime_first_points += 1
        dispatch = dispatch_h3(first)
        if dispatch["branch"] == "bounded_factor_type_ii_terminal":
            terminal.append((first, u, d, int(dispatch["factor"])))
            continue
        if (first, u, d) != (7_606_503_424_129, 15, 65):
            raise AssertionError("an unexpected nonterminal prime ray first point appeared")
        lambda_value, d4 = exact_h4_carrier(first)
        carrier_mismatch.append((first, u, d, lambda_value, d4))

    result = {
        "prime_first_points": prime_first_points,
        "h3_terminal": tuple(sorted(terminal)),
        "h4_carrier_mismatch": tuple(sorted(carrier_mismatch)),
    }
    expected = {
        "prime_first_points": 3,
        "h3_terminal": (
            (2_025_421_441, 78, 11, 11),
            (430_576_893_658_129, 85, 179, 179),
        ),
        "h4_carrier_mismatch": (
            (7_606_503_424_129, 15, 65, 65, 1),
        ),
    }
    if result != expected:
        raise AssertionError(f"prime first-point H3/H4 audit changed: {result}")
    return result


def verify() -> None:
    pruning = terminal_pruning_map()
    audit = prime_first_point_prefix_audit()
    print(
        "verified minimal-D H3 terminal pruning: "
        f"{len(pruning['pruned'])} of 17 rays removed, "
        f"{len(pruning['retained'])} retained, and "
        f"{audit['prime_first_points']} prime first points rejected"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused ray checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
