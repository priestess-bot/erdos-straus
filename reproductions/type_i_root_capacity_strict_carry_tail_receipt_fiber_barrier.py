#!/usr/bin/env python3
"""Verify strict-root tail receipt-fiber invariance on fixed controls."""

from __future__ import annotations

import argparse
from math import gcd

from type_i_root_capacity_general_endpoint_divisor_gate import chart
from type_i_root_capacity_strict_carry_complement_tail_bezout_character_gate import (
    root_tail_data,
    selector_factors,
)


def normalized_unit(p: int, cofactor: int, multiplier: int) -> tuple[int, int]:
    """Return the lift-normalized witness and its expected R-shift sign."""
    if (multiplier * cofactor + 1) % p:
        raise AssertionError("multiplier did not belong to the cofactor fiber")
    witness = (multiplier * cofactor + 1) // p
    if cofactor % 2 == 0:
        return multiplier - 4 * witness, -1
    return 3 * multiplier - 4 * witness, 1


def verify_lift_invariance(p: int, root_parameter: int) -> None:
    data = root_tail_data(p, root_parameter)
    cofactor = data["c"]
    remainder = data["R"]
    source = data["n"]
    multiplier = data["E"]
    baseline, sign = normalized_unit(p, cofactor, multiplier)
    shifted, shifted_sign = normalized_unit(p, cofactor, multiplier + p)

    if not (
        baseline == data["a"]
        and sign == shifted_sign
        and shifted - baseline == sign * remainder
        and baseline % remainder == shifted % remainder
        and baseline % remainder == (-pow(source, -1, remainder)) % remainder
    ):
        raise AssertionError("receipt-fiber normalized unit changed")


def verify_p313_direct_receipt_support_boundary() -> None:
    receipt = chart(313, 271)
    data = root_tail_data(313, 271)
    p = data["p"]
    h = receipt["h"]
    d_value = receipt["D"]
    source = data["n"]
    remainder = data["R"]
    product = data["S"]
    direct_support = gcd(p * h + 1, product * product)
    target = (-product) % remainder

    if not (
        (receipt["u"], h, d_value, data["c"], source, remainder, product)
        == (181, 543, 8, 298, 298, 879, 93_274)
        and d_value == gcd(d_value, (p * p - 1) // 2)
        and receipt["K"] % d_value == 0
        and (p * h + 1) % d_value == 0
        and (h * h - 1) % d_value == 0
        and (4 * source) % d_value == 0
        and direct_support == 4
        and target == 779
        and all((factor - target) % remainder for factor in (1, 2, 4))
        and not selector_factors(p, source)
    ):
        raise AssertionError("p=313 direct D-support boundary changed")


def verify() -> None:
    verify_lift_invariance(73, 3)
    verify_lift_invariance(313, 271)
    verify_p313_direct_receipt_support_boundary()
    print(
        "verified strict-root receipt-fiber lift invariance and the p=313 "
        "direct D-support tail boundary"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
