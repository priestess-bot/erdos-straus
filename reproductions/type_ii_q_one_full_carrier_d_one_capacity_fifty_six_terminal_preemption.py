#!/usr/bin/env python3
"""Verify the gap-seven terminal preemption of the q=1 zero-k c=56 ray.

The checks replay the exact phase congruence and two fixed macro controls.
They do not search primes, factor ranges, or claim a terminal for the c=8 ray.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import type_ii_q_one_full_carrier_d_one_capacity_two_rigidity as capacity_two
import type_ii_q_one_full_carrier_d_one_zero_k_capacity_ray as zero_k


@dataclass(frozen=True)
class TypeIITerminal:
    prime: int
    gap: int
    x: int
    divisor: int
    y: int
    z: int


def assert_type_ii_identity(certificate: TypeIITerminal) -> None:
    """Check the integral Type II normal-form certificate directly."""
    p, h, x, divisor, y, z = (
        certificate.prime,
        certificate.gap,
        certificate.x,
        certificate.divisor,
        certificate.y,
        certificate.z,
    )
    if not (
        p % 24 == 1
        and h % 4 == 3
        and 3 <= h <= p - 2
        and 4 * x == p + h
        and divisor > 0
        and x * x % divisor == 0
        and 4 * x * y * z == p * (x * y + x * z + y * z)
        and min(x, y, z) > 0
    ):
        raise AssertionError("Type II terminal identity changed")


def gap_seven_terminal(s: int) -> TypeIITerminal:
    """Build the fixed h=7 Type II terminal for s == 2 (mod 7)."""
    if s < 2 or s % 7 != 2:
        raise ValueError("gap-seven construction requires s == 2 (mod 7)")
    p = 48 * s + 1
    h = 7
    x = (p + h) // 4
    b = 6 * s + 1
    divisor = 2
    if not (
        4 * x == p + h
        and x == 2 * b
        and math.gcd(1, b) == 1
        and (1 + b) % h == 0
        and x * x % divisor == 0
    ):
        raise AssertionError("gap-seven normal form changed")
    y = p * (x + divisor) // h
    z = p * (x + x * x // divisor) // h
    certificate = TypeIITerminal(p, h, x, divisor, y, z)
    assert_type_ii_identity(certificate)
    return certificate


def c_fifty_six_phase_forces_gap_seven() -> dict[str, int]:
    """Replay g=7 | (24s+1), hence the c=56 phase has s == 2 mod 7."""
    if (56, 11, 7) not in zero_k.zero_k_shapes():
        raise AssertionError("zero-k c=56 shape changed")
    s_mod_7 = (-pow(24, -1, 7)) % 7
    if not (
        s_mod_7 == 2
        and (24 * s_mod_7 + 1) % 7 == 0
        and (6 * s_mod_7 + 2) % 7 == 0
    ):
        raise AssertionError("c=56 gap-seven phase changed")
    return {"s_mod_7": s_mod_7, "gap": 7}


def c_eight_is_disjoint_from_the_gap_seven_phase() -> None:
    """For j=11, s == 2 mod 7 would force 7 | g, unlike c=8."""
    if (8, 11, 1) not in zero_k.zero_k_shapes():
        raise AssertionError("zero-k c=8 shape changed")
    # Write s=7u+2.  Both gcd inputs are multiples of seven for every u.
    if not (
        (24 * 7) % 7 == 0
        and (24 * 2 + 1) % 7 == 0
        and (66 * 7) % 7 == 0
        and (66 * 2 + 1) % 7 == 0
    ):
        raise AssertionError("c=8/gap-seven disjointness changed")


def p_plus_four_terminal(prime: int, gap: int) -> TypeIITerminal:
    """Build the standard p+4 Type II terminal for one supplied divisor."""
    if not (
        prime % 24 == 1
        and gap % 4 == 3
        and 3 <= gap <= prime - 2
        and (prime + 4) % gap == 0
    ):
        raise ValueError("invalid p+4 Type II input")
    x = (prime + gap) // 4
    y = prime * (x + 1) // gap
    z = prime * x * (x + 1) // gap
    certificate = TypeIITerminal(prime, gap, x, 1, y, z)
    assert_type_ii_identity(certificate)
    return certificate


def actual_controls() -> dict[str, int]:
    """Replay the two q-star=103 macro roots with their direct terminals."""
    c_fifty_six = capacity_two.receiver_data("even", 172)
    if not (
        c_fifty_six["prime"] == 4129
        and c_fifty_six["s"] == 86
        and c_fifty_six["j"] == 11
        and c_fifty_six["g"] == 7
        and c_fifty_six["c"] == 56
    ):
        raise AssertionError("c=56 q-star=103 macro control changed")
    gap_seven = gap_seven_terminal(86)
    if gap_seven != TypeIITerminal(4129, 7, 1034, 2, 611092, 315934564):
        raise AssertionError("p=4129 gap-seven terminal changed")

    c_eight = capacity_two.receiver_data("even", 6558)
    if not (
        c_eight["prime"] == 157393
        and c_eight["s"] == 3279
        and c_eight["j"] == 11
        and c_eight["g"] == 1
        and c_eight["c"] == 8
    ):
        raise AssertionError("c=8 q-star=103 macro control changed")
    p_plus_four = p_plus_four_terminal(157393, 107)
    if p_plus_four != TypeIITerminal(
        157393, 107, 39375, 1, 57920624, 2280624570000
    ):
        raise AssertionError("p=157393 p-plus-four terminal changed")
    return {"c_fifty_six_prime": 4129, "c_eight_control_prime": 157393}


def verify() -> None:
    phase = c_fifty_six_phase_forces_gap_seven()
    c_eight_is_disjoint_from_the_gap_seven_phase()
    controls = actual_controls()
    if not (
        phase == {"s_mod_7": 2, "gap": 7}
        and controls == {"c_fifty_six_prime": 4129, "c_eight_control_prime": 157393}
    ):
        raise AssertionError("terminal-preemption receipt changed")
    print(
        "verified q=1 zero-k c=56 gap-7 terminal preemption; "
        "c=8 remains outside this fixed-gap template"
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
