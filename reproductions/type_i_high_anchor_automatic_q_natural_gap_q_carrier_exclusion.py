#!/usr/bin/env python3
"""Verify the natural-gap Q-carrier exclusion for strict automatic-q sources."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

import type_i_high_anchor_q2_bku_parameterization as q2
import type_i_high_anchor_q3_bku_parameterization as q3


def positive_divisors(value: int) -> tuple[int, ...]:
    """Return the positive divisors of one fixed control integer."""
    divisors: list[int] = []
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate:
            continue
        divisors.append(candidate)
        partner = value // candidate
        if partner != candidate:
            divisors.append(partner)
    return tuple(sorted(divisors))


def radical(value: int) -> int:
    """Return rad(value) by trial division on the fixed control divisors."""
    result = 1
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        if remaining % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        result *= divisor
        while remaining % divisor == 0:
            remaining //= divisor
    if remaining > 1:
        result *= remaining
    return result


def assert_egyptian_identity(prime: int, terms: tuple[int, int, int]) -> None:
    """Check one three-unit-fraction identity without floating-point arithmetic."""
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != prime * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def natural_gap_profile(*, prime: int, high_r: int) -> dict[str, object]:
    """Exhaust Q-supported divisors at m=R-p+1 for one fixed row."""
    delta = high_r - prime
    gap = delta + 1
    x = (high_r + 1) // 4
    carrier = high_r - 1
    divisors = positive_divisors(x * x)
    q_supported = tuple(
        divisor for divisor in divisors if carrier % radical(divisor) == 0
    )
    type_i = tuple(
        divisor for divisor in q_supported if (prime * x + divisor) % gap == 0
    )
    type_ii = tuple(
        divisor
        for divisor in q_supported
        if divisor <= x and (x + divisor) % gap == 0
    )
    d_one_type_i = (prime * x + 1) % gap == 0
    d_one_type_ii = (x + 1) % gap == 0
    checks = {
        "core_prime_class": prime % 24 == 1,
        "strict_high_window": prime < high_r < 2 * prime,
        "second_full_excess_shape": carrier == high_r - 1,
        "natural_gap_range": 3 <= gap <= prime - 2 and gap % 4 == 3,
        "natural_x": 4 * x == prime + gap and x % 2 == 1,
        "carrier_coprime_to_x": gcd(x, carrier) == 1,
        "complete_q_supported_menu_is_d_one": q_supported == (1,),
        "type_i_d_one_impossible": not d_one_type_i,
        "type_i_target_equivalence": d_one_type_i == ((prime * prime + 4) % gap == 0),
        "type_ii_target_equivalence": d_one_type_ii == ((prime + 4) % gap == 0),
        "q_supported_type_i_empty": type_i == (),
        "q_supported_type_ii_exact": type_ii == ((1,) if d_one_type_ii else ()),
    }
    if not all(checks.values()):
        raise AssertionError(
            f"natural-gap Q-carrier exclusion failed for p={prime}: {checks}"
        )
    return {
        "p": prime,
        "R": high_r,
        "Q": carrier,
        "delta": delta,
        "m": gap,
        "x": x,
        "q_supported_divisors": q_supported,
        "q_supported_type_i": type_i,
        "q_supported_type_ii": type_ii,
        "checks": checks,
    }


def actual_q2_control() -> dict[str, object]:
    """Replay the q=2 source before applying the independent natural-gap gate."""
    control = next(item for item in q2.CONTROLS if item["p"] == 3_793)
    source = q2.verify_positive_control(control)
    profile = natural_gap_profile(prime=control["p"], high_r=control["R"])
    if not (
        source["high_anchor"]["Q1"] == control["R"] - 1
        and source["automatic_q"]["C"] == 2 * control["A"]
        and profile["q_supported_type_ii"] == ()
    ):
        raise AssertionError("q=2 automatic source no longer witnesses the exclusion")
    return {"source": source, "natural_gap": profile}


def actual_q3_control() -> dict[str, object]:
    """Replay the q=3 source before applying the independent natural-gap gate."""
    control = next(item for item in q3.CONTROLS if int(item["p"]) == 60_913)
    source = q3.verify_control(control)
    profile = natural_gap_profile(prime=int(control["p"]), high_r=int(control["R"]))
    if not (
        source["high_anchor"]["Q1"] == int(control["R"]) - 1
        and source["automatic_q"]["C"] == 3 * int(control["A"])
        and profile["q_supported_type_ii"] == ()
    ):
        raise AssertionError("q=3 automatic source no longer witnesses the exclusion")
    return {"source": source, "natural_gap": profile}


def sharp_type_ii_control() -> dict[str, object]:
    """Show that the remaining d=1 Type-II condition is genuinely sharp."""
    profile = natural_gap_profile(prime=73, high_r=83)
    gap = int(profile["m"])
    x = int(profile["x"])
    if profile["q_supported_type_ii"] != (1,):
        raise AssertionError("sharp d=1 control lost its Type-II terminal")
    numerator_y = 73 * (x + 1)
    numerator_z = 73 * (x + x * x)
    if numerator_y % gap or numerator_z % gap:
        raise AssertionError("sharp d=1 Type-II reconstruction was not integral")
    terms = (x, numerator_y // gap, numerator_z // gap)
    assert_egyptian_identity(73, terms)
    return {"natural_gap": profile, "terms": terms}


def build_result() -> dict[str, object]:
    q2_row = actual_q2_control()
    q3_row = actual_q3_control()
    sharp_row = sharp_type_ii_control()
    if not (
        q2_row["natural_gap"]["m"] == 3_219
        and q3_row["natural_gap"]["m"] == 11_347
        and sharp_row["terms"] == (21, 146, 3066)
    ):
        raise AssertionError("fixed natural-gap controls changed")
    return {
        "certificate_type": "automatic_q_natural_gap_q_carrier_exclusion_v1",
        "scope": (
            "The result exhausts only square divisors supported on the second full-excess "
            "carrier Q=R-1 at the natural gap R-p+1. It does not exclude non-Q divisors, "
            "other gaps, or an admitted automatic macro."
        ),
        "actual_q2_control": q2_row,
        "actual_q3_control": q3_row,
        "sharp_type_ii_control": sharp_row,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified automatic-q natural-gap Q-carrier exclusion: q=2, q=3, sharp d=1")


if __name__ == "__main__":
    main()
