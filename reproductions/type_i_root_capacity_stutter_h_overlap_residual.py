#!/usr/bin/env python3
"""Verify fixed controls for the stutter h^2-1 overlap residual bound."""

from __future__ import annotations

import argparse
from math import gcd, lcm


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def overlap_data(p: int, h: int, d_value: int) -> dict[str, int]:
    if h % 2 != 1 or d_value <= 0 or (p * h + 1) % d_value:
        raise AssertionError("control does not satisfy the odd-h stutter divisor gate")
    m_value, remainder = divmod(d_value + h - 1, p)
    if remainder or m_value <= 0 or d_value % p != (1 - h) % p:
        raise AssertionError("control does not satisfy the stutter linearization")

    h_minus = gcd(d_value, h - 1)
    h_plus = gcd(d_value, h + 1)
    h_overlap = gcd(d_value, h * h - 1)
    local_lcm = lcm(h_minus, h_plus)
    m_lcm = lcm(m_value, m_value + 2)
    if not (
        m_value % h_minus == 0
        and (m_value + 2) % h_plus == 0
        and m_lcm % local_lcm == 0
        and (2 * m_lcm) % h_overlap == 0
    ):
        raise AssertionError("h^2-1 overlap localization changed")
    return {
        "m": m_value,
        "b_minus": h_minus,
        "b_plus": h_plus,
        "D_H": h_overlap,
        "D_star": d_value // h_overlap,
        "m_lcm": m_lcm,
    }


def verify_overlap_controls() -> None:
    controls = (
        (361, 1029, 55, (3, 1, 5, 5, 11, 15)),
        (97, 17, 275, (3, 1, 1, 1, 275, 15)),
        (3001, 243, 11762, (4, 2, 2, 2, 5881, 12)),
        (5281, 323, 20802, (4, 2, 6, 6, 3467, 12)),
        (54481, 12063, 696191, (13, 1, 1, 1, 696191, 195)),
    )
    for p, h, d_value, expected in controls:
        values = overlap_data(p, h, d_value)
        if tuple(values[key] for key in ("m", "b_minus", "b_plus", "D_H", "D_star", "m_lcm")) != expected:
            raise AssertionError("fixed h-overlap control changed")

    # The first is a non-proper composite control. The next three are core-prime
    # proper-shape controls but fail h | p^2+p+1, so none is an actual receipt.
    if not (361 % 24 == 1 and not is_prime(361) and 1029 > 361):
        raise AssertionError("odd overlap boundary provenance changed")
    for p, h, root_remainder in ((97, 17, 4), (3001, 243, 21), (5281, 323, 286)):
        if not (
            is_prime(p)
            and p % 24 == 1
            and 2 <= h < p
            and (p * p + p + 1) % h == root_remainder
            and root_remainder != 0
        ):
            raise AssertionError("proper-shape control provenance changed")

    # This existing m=13 gate is core-congruent and root-shaped, but composite
    # p and noncanonical D keep it outside the actual-receipt scope.
    if not (
        54481 % 24 == 1
        and not is_prime(54481)
        and 2 <= 12063 < 54481
        and (54481 * 54481 + 54481 + 1) % 12063 == 0
    ):
        raise AssertionError("m=13 shadow provenance changed")


def verify_three_m_regimes() -> None:
    for p, h, d_value in ((97, 17, 275), (3001, 243, 11762), (54481, 12063, 696191)):
        values = overlap_data(p, h, d_value)
        m_value = values["m"]
        if not (
            m_value >= 3
            and m_value % 3 != 2
            and (m_value - 1) ** 2 < h < p
            and d_value >= (m_value - 1) * p + 2
            and values["D_H"] < d_value
            and values["D_star"] > 1
        ):
            raise AssertionError("proper-shape numerical hypotheses changed")
        if m_value == 3:
            if not (p >= 73 and d_value > 2 * values["m_lcm"] == 30):
                raise AssertionError("m=3 overlap comparison changed")
        elif m_value == 4:
            if not (p >= 73 and d_value > 2 * values["m_lcm"] == 24):
                raise AssertionError("m=4 overlap comparison changed")
        else:
            if not (
                m_value >= 6
                and p > (m_value - 1) ** 2
                and (m_value - 1) ** 3 > 2 * m_value * (m_value + 2)
                and d_value > 2 * values["m_lcm"]
            ):
                raise AssertionError("m>=6 overlap comparison changed")


def verify() -> None:
    verify_overlap_controls()
    verify_three_m_regimes()
    print("verified fixed stutter h^2-1 overlap bounds and nontrivial D-star controls")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
