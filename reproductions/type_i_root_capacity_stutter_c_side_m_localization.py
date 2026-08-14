#!/usr/bin/env python3
"""Verify fixed controls for the stutter C-side m-localization lemma."""

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


def localization(p: int, h: int, d_value: int) -> dict[str, int]:
    if p % 4 != 1 or d_value <= 0 or (p * h + 1) % d_value:
        raise AssertionError("control does not satisfy the local stutter divisor gate")
    m_value, remainder = divmod(d_value + h - 1, p)
    if remainder or m_value <= 0 or d_value % p != (1 - h) % p:
        raise AssertionError("control does not satisfy the stutter linearization")

    c_value = (p * p - 1) // 2
    d_minus = gcd(d_value, p + 1)
    d_plus = gcd(d_value, p - 1)
    d_c = gcd(d_value, c_value)
    d_t = d_value // d_c
    m_lcm = lcm(m_value, m_value + 2)
    if not (
        (h - 1) % d_minus == 0
        and (h + 1) % d_plus == 0
        and m_value % d_minus == 0
        and (m_value + 2) % d_plus == 0
        and d_c == lcm(d_minus, d_plus)
        and m_lcm == m_value * (m_value + 2) // gcd(m_value, 2)
        and m_lcm % d_c == 0
        and (h * h - 1) % d_c == 0
    ):
        raise AssertionError("C-side m-localization changed")
    return {
        "m": m_value,
        "D_C": d_c,
        "D_T": d_t,
        "d_minus": d_minus,
        "d_plus": d_plus,
        "m_lcm": m_lcm,
    }


def verify_localization_controls() -> None:
    # This is a non-proper core-congruence composite control with odd C-side mass.
    values = localization(361, 1029, 55)
    if values != {
        "m": 3,
        "D_C": 5,
        "D_T": 11,
        "d_minus": 1,
        "d_plus": 5,
        "m_lcm": 15,
    }:
        raise AssertionError("odd C-side control changed")

    # These fixed core-prime proper-shape controls exercise dyadic and mixed
    # C-side mass. They deliberately fail h | p^2+p+1, hence are not receipts.
    controls = (
        (97, 17, 275, 4, 1),
        (3001, 243, 11762, 21, 2),
        (5281, 323, 20802, 286, 6),
    )
    expected = (
        (3, 1, 275, 1, 1, 15),
        (4, 2, 5881, 2, 2, 12),
        (4, 6, 3467, 2, 6, 12),
    )
    for control, expected_values in zip(controls, expected):
        p, h, d_value, root_remainder, expected_d_c = control
        values = localization(p, h, d_value)
        if not (
            is_prime(p)
            and p % 24 == 1
            and 2 <= h < p
            and (p * p + p + 1) % h == root_remainder
            and root_remainder != 0
            and values["D_C"] == expected_d_c
            and tuple(values[key] for key in ("m", "D_C", "D_T", "d_minus", "d_plus", "m_lcm"))
            == expected_values
        ):
            raise AssertionError("core proper-shape localization control changed")


def verify_proper_shape_comparison() -> None:
    # These controls satisfy the numerical m-bounds used in the actual
    # proper-root consequence, but not root provenance; see the check above.
    for p, h, d_value in ((97, 17, 275), (3001, 243, 11762), (5281, 323, 20802)):
        values = localization(p, h, d_value)
        m_value = values["m"]
        if not (
            m_value >= 3
            and (m_value - 1) ** 2 < h < p
            and d_value >= (m_value - 1) * p + 2
            and values["D_C"] < d_value
            and values["D_T"] > 1
        ):
            raise AssertionError("proper-shape comparison hypotheses changed")
        if m_value == 3:
            if not (p >= 73 and d_value > values["m_lcm"] == 15):
                raise AssertionError("m=3 C-side comparison changed")
        else:
            if not (
                p > (m_value - 1) ** 2
                and (m_value - 1) ** 3 >= m_value * (m_value + 2)
                and d_value > values["m_lcm"]
            ):
                raise AssertionError("m>=4 C-side comparison changed")


def verify() -> None:
    verify_localization_controls()
    verify_proper_shape_comparison()
    print("verified fixed stutter C-side m-localization and nontrivial residual controls")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
