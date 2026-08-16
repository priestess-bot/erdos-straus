#!/usr/bin/env python3
"""Verify the high-H4 exclusion of the y-side single-side endpoint.

The two high fixtures are fixed local H4 arithmetic controls.  The third row
is a low-height algebraic control showing that x | K can occur when the H4
height inequality is removed.  No prime-range, denominator, or selector scan
is performed.
"""

from __future__ import annotations

import argparse
from math import gcd

from type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge import (
    FIXTURES,
    complete_excess,
)


def high_endpoint_audit(fixture: object) -> dict[str, int | str]:
    prime = int(getattr(fixture, "prime"))
    peeled_part = int(getattr(fixture, "peeled_part"))
    residue = 1 + prime * peeled_part
    carrier = (prime * residue + 1) // 4
    height = gcd(residue - 1, carrier)
    divisor = gcd((prime + 1) // 2, carrier)
    q = (prime + 1) // (2 * divisor)
    endpoint_y = (residue - height) // q
    endpoint_x = residue - endpoint_y
    q_x = complete_excess(endpoint_x, carrier)
    q_y = complete_excess(endpoint_y, carrier)
    upper = 2 * height * height - 2 * height - 1
    lower = prime * height + 1

    if not (
        prime % 24 == 1
        and residue % 4 == 3
        and prime * residue + 1 == 4 * carrier
        and height == 2 * divisor
        and height * q == prime + 1
        and q > 1
        and q % 2 == 1
        and q >= 3
        and endpoint_x == (q - 1) * endpoint_y + height
        and endpoint_y > lower
        and lower >= 3 * height * height - height + 1
        and lower > upper
        and q_x > 1
        and q_y > 1
        and carrier % endpoint_x != 0
    ):
        raise AssertionError(f"{getattr(fixture, 'name')}: high single-side exclusion changed")

    return {
        "name": str(getattr(fixture, "name")),
        "q": q,
        "y": endpoint_y,
        "upper": upper,
        "lower": lower,
        "q_x": q_x,
        "q_y": q_y,
    }


def low_height_sharpness_audit() -> dict[str, int | str]:
    prime = 433
    height = 62
    q = 7
    endpoint_y = 71
    endpoint_x = 488
    residue = endpoint_x + endpoint_y
    carrier = 60_512
    quotient = (prime * endpoint_y + 1) // endpoint_x
    j = quotient - height
    delta = height - 1 - j * (q - 1)

    if not (
        prime % 24 == 1
        and prime == height * q - 1
        and residue == q * endpoint_y + height
        and residue % 4 == 3
        and prime * residue + 1 == 4 * carrier
        and gcd(residue - 1, carrier) == height
        and gcd(q, carrier) == 1
        and carrier % endpoint_x == 0
        and complete_excess(endpoint_x, carrier) == 1
        and complete_excess(endpoint_y, carrier) == 71
        and endpoint_x == (q - 1) * endpoint_y + height
        and (prime * endpoint_y + 1) % endpoint_x == 0
        and quotient == 63
        and j == 1
        and delta * endpoint_y == height * (height + j) - 1
        and endpoint_y < prime * height + 1
    ):
        raise AssertionError("low-height single-side sharpness control changed")

    return {
        "name": "low_height_single_side_control",
        "q": q,
        "y": endpoint_y,
        "ph_plus_one": prime * height + 1,
        "q_x": complete_excess(endpoint_x, carrier),
        "q_y": complete_excess(endpoint_y, carrier),
    }


def verify() -> None:
    receipts = [high_endpoint_audit(fixture) for fixture in FIXTURES]
    receipts.append(low_height_sharpness_audit())
    if receipts != [
        {
            "name": "prime_q37_atomic_split_strict",
            "q": 37,
            "y": 6_641,
            "upper": 3,
            "lower": 147,
            "q_x": 119_539,
            "q_y": 6_641,
        },
        {
            "name": "composite_q121_atomic_split_strict",
            "q": 121,
            "y": 59_525,
            "upper": 3,
            "lower": 483,
            "q_x": 3_571_501,
            "q_y": 59_525,
        },
        {
            "name": "low_height_single_side_control",
            "q": 7,
            "y": 71,
            "ph_plus_one": 26_847,
            "q_x": 1,
            "q_y": 71,
        },
    ]:
        raise AssertionError("H4 single-side exclusion controls changed")
    print("verified high-H4 single-side exclusion and low-height sharpness control")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
