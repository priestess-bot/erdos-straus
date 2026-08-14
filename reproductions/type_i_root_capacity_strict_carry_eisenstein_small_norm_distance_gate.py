#!/usr/bin/env python3
"""Verify small-norm complement-distance bounds for fixed strict root receipts."""

from __future__ import annotations

import argparse
from math import isqrt

from type_i_root_capacity_general_endpoint_divisor_gate import chart


def strict_data(p: int, r: int) -> dict[str, int]:
    receipt = chart(p, r)
    h = receipt["h"]
    d_value = receipt["D"]
    c = (d_value * pow(h - 1, -1, p)) % p
    n = c if c % 2 == 0 else p - c
    delta = p - n
    tau = 1 if c % 2 else -1
    numerator = d_value - tau * delta * (h - 1)
    if numerator % p:
        raise AssertionError("pre-cofactor coordinate is not integral")
    s = numerator // p
    v = (p * p + p + 1) // h
    t = v * s * s + tau * (2 * p + 1) * s * delta + h * delta * delta
    if h % 3:
        raise AssertionError("root endpoint lost its h=3u form")
    radius = isqrt(4 * h * t // 3)
    if not (
        p % 24 == 1
        and receipt["u"] < receipt["M"]
        and 1 <= c <= p - 2
        and t > 0
        and 3 * s * s <= 4 * h * t
        and 3 * (d_value + tau * delta) ** 2 <= 4 * h * t
        and abs(s) <= radius
        and abs(d_value + tau * delta) <= radius
    ):
        raise AssertionError("Eisenstein norm radius identities changed")
    data = {
        "p": p,
        "h": h,
        "D": d_value,
        "c": c,
        "n": n,
        "delta": delta,
        "tau": tau,
        "s": s,
        "t": t,
        "radius": radius,
    }
    if tau == 1:
        odd_bound = radius - 1
        if not (d_value + delta <= radius and delta <= odd_bound):
            raise AssertionError("odd-cofactor small-norm distance gate changed")
        data["distance_bound"] = odd_bound
    else:
        even_bound = (p * radius - 1) // (h - 1)
        if not (
            s > 0
            and p * s == d_value + delta * (h - 1)
            and delta <= even_bound
        ):
            raise AssertionError("even-cofactor small-norm distance gate changed")
        data["distance_bound"] = even_bound
    return data


def verify() -> None:
    odd = strict_data(73, 3)
    unit = strict_data(313, 271)
    nonunit = strict_data(193, 3)

    if not (
        odd
        == {
            "p": 73,
            "h": 3,
            "D": 220,
            "c": 37,
            "n": 36,
            "delta": 37,
            "tau": 1,
            "s": 2,
            "t": 22_189,
            "radius": 297,
            "distance_bound": 296,
        }
        and unit
        == {
            "p": 313,
            "h": 543,
            "D": 8,
            "c": 298,
            "n": 298,
            "delta": 15,
            "tau": -1,
            "s": 26,
            "t": 1,
            "radius": 26,
            "distance_bound": 15,
        }
        and nonunit
        == {
            "p": 193,
            "h": 21,
            "D": 2,
            "c": 58,
            "n": 58,
            "delta": 135,
            "tau": -1,
            "s": 14,
            "t": 763,
            "radius": 146,
            "distance_bound": 1_408,
        }
        and unit["distance_bound"] == unit["delta"]
        and unit["n"] > unit["p"] // 2
        and nonunit["distance_bound"] >= nonunit["p"]
    ):
        raise AssertionError("fixed small-norm distance controls changed")

    print(
        "verified strict-root Eisenstein small-norm distance gates, the sharp "
        "p=313 unit fiber, and the non-small-norm boundary"
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
