#!/usr/bin/env python3
"""Verify the high-window R-1 carrier exclusion at its natural gap.

The arithmetic statement needs only p < R < 2p, R == 3 (mod 8), and the
carrier Q = R - 1.  It is therefore broader than the automatic-q source
subfamily.  The fixture includes an actual non-automatic high-R full-excess
row at p=1033, two automatic-q corollaries, and a sharp d=1 Type-II row.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt

import type_i_high_anchor_q2_bku_parameterization as q2
import type_i_high_anchor_q3_bku_parameterization as q3
import type_i_high_r_chart_two_anchor as shared


def positive_divisors(value: int) -> tuple[int, ...]:
    if value <= 0:
        raise AssertionError("positive divisor input is required")
    result: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        result.append(divisor)
        partner = value // divisor
        if partner != divisor:
            result.append(partner)
    return tuple(sorted(result))


def radical(value: int) -> int:
    if value <= 0:
        raise AssertionError("radical input is required")
    result = 1
    remaining = value
    divisor = 2
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
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != prime * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def high_window_profile(*, prime: int, high_r: int) -> dict[str, object]:
    """Exhaust Q-supported Bradford divisors for one fixed high-window row."""
    if not (
        shared.is_prime(prime)
        and prime % 24 == 1
        and prime < high_r < 2 * prime
        and high_r % 8 == 3
    ):
        raise AssertionError("profile requires a core high-window R == 3 (mod 8) row")

    carrier = high_r - 1
    gap = high_r - prime + 1
    x = (high_r + 1) // 4
    q_supported = tuple(
        divisor
        for divisor in positive_divisors(x * x)
        if carrier % radical(divisor) == 0
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
        "natural_gap": 3 <= gap <= prime - 2 and gap % 4 == 3,
        "natural_x": 4 * x == prime + gap and x % 2 == 1,
        "carrier_coprime_to_x": gcd(carrier, x) == 1,
        "complete_q_supported_menu_is_d_one": q_supported == (1,),
        "type_i_d_one_impossible": not d_one_type_i,
        "type_i_target_equivalence": d_one_type_i == ((prime * prime + 4) % gap == 0),
        "type_ii_target_equivalence": d_one_type_ii == ((prime + 4) % gap == 0),
        "q_supported_type_i_empty": type_i == (),
        "q_supported_type_ii_exact": type_ii == ((1,) if d_one_type_ii else ()),
    }
    if not all(checks.values()):
        raise AssertionError(f"high-window carrier exclusion failed: {checks}")
    return {
        "p": prime,
        "R": high_r,
        "Q": carrier,
        "m": gap,
        "x": x,
        "q_supported_divisors": q_supported,
        "q_supported_type_i": type_i,
        "q_supported_type_ii": type_ii,
        "checks": checks,
    }


def actual_nonautomatic_full_excess_control() -> dict[str, object]:
    prime, support, high_r = 1_033, 351, 1_211
    bundle = shared.high_R_path_anchored_bundle(
        prime=prime, R=high_r, support=support
    )
    complete_excess = bundle["complete_excess_bundle"]
    rechart = bundle["rechart"]
    if not isinstance(rechart, dict):
        raise AssertionError("non-automatic control lost its rechart")
    profile = high_window_profile(prime=prime, high_r=high_r)
    checks = {
        "actual_second_full_excess": (
            complete_excess["Q"] == high_r - 1
            and complete_excess["beta"] == 1
        ),
        "not_automatic_q_support_multiple": int(rechart["C"]) % support != 0,
        "natural_gap_not_d_one_type_ii": profile["q_supported_type_ii"] == (),
    }
    if not all(checks.values()):
        raise AssertionError(f"non-automatic full-excess control failed: {checks}")
    return {
        "high_anchor": {"p": prime, "A": support, "R": high_r},
        "bundle": complete_excess,
        "rechart": {"M": rechart["M"], "C": rechart["C"]},
        "natural_gap": profile,
        "checks": checks,
    }


def automatic_q_corollaries() -> dict[str, object]:
    q2_control = next(item for item in q2.CONTROLS if item["p"] == 3_793)
    q3_control = next(item for item in q3.CONTROLS if int(item["p"]) == 60_913)
    q2_source = q2.verify_positive_control(q2_control)
    q3_source = q3.verify_control(q3_control)
    q2_profile = high_window_profile(prime=int(q2_control["p"]), high_r=int(q2_control["R"]))
    q3_profile = high_window_profile(prime=int(q3_control["p"]), high_r=int(q3_control["R"]))
    checks = {
        "q2_full_excess": q2_source["high_anchor"]["Q1"] == q2_control["R"] - 1,
        "q3_full_excess": q3_source["high_anchor"]["Q1"] == q3_control["R"] - 1,
        "q2_carrier_menu_empty": q2_profile["q_supported_type_ii"] == (),
        "q3_carrier_menu_empty": q3_profile["q_supported_type_ii"] == (),
    }
    if not all(checks.values()):
        raise AssertionError(f"automatic-q corollary controls failed: {checks}")
    return {
        "q2": {"source": q2_source, "natural_gap": q2_profile},
        "q3": {"source": q3_source, "natural_gap": q3_profile},
        "checks": checks,
    }


def sharp_type_ii_control() -> dict[str, object]:
    profile = high_window_profile(prime=73, high_r=83)
    gap = int(profile["m"])
    x = int(profile["x"])
    if profile["q_supported_type_ii"] != (1,):
        raise AssertionError("sharp d=1 Type-II control disappeared")
    terms = (x, 73 * (x + 1) // gap, 73 * (x + x * x) // gap)
    assert_egyptian_identity(73, terms)
    return {"natural_gap": profile, "terms": terms}


def build_result() -> dict[str, object]:
    nonautomatic = actual_nonautomatic_full_excess_control()
    automatic = automatic_q_corollaries()
    sharp = sharp_type_ii_control()
    if not (
        nonautomatic["natural_gap"]["m"] == 179
        and nonautomatic["natural_gap"]["x"] == 303
        and sharp["terms"] == (21, 146, 3066)
    ):
        raise AssertionError("fixed high-window controls changed")
    return {
        "certificate_type": "high_window_natural_gap_r_minus_one_carrier_exclusion_v1",
        "scope": (
            "The proof uses only the core high-window hypotheses p < R < 2p, "
            "R == 3 (mod 8), and Q = R - 1. It excludes only Bradford divisors "
            "whose prime support lies in Q at m = R - p + 1."
        ),
        "actual_nonautomatic_full_excess": nonautomatic,
        "automatic_q_corollaries": automatic,
        "sharp_type_ii_control": sharp,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print(
            "verified high-window natural-gap R-1 carrier exclusion: "
            "non-automatic, q=2, q=3, sharp Type II"
        )


if __name__ == "__main__":
    main()
