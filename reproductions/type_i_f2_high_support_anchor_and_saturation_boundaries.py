#!/usr/bin/env python3
"""Verify high-support C=1 anchor and C>1 saturation route exclusions."""

from __future__ import annotations

import argparse
from math import gcd


def r3_anchor_no_reentry(prime: int) -> dict[str, int]:
    if prime % 24 != 1:
        raise AssertionError("control is outside the core residue class")
    boundary = (prime - 1) ** 2 // 4
    N = (3 * prime + 1) // 4
    support = 2 * N
    K = N * (prime + 1)
    R = 3 * prime + 4
    if not (
        N % 2 == 1
        and prime * R + 1 == 4 * K
        and boundary - support == (prime * prime - 8 * prime - 1) // 4
        and support < boundary
        and K // support == (prime + 1) // 2
        and R > prime
    ):
        raise AssertionError("R=3 canonical-anchor boundary changed")
    return {
        "prime": prime,
        "N": N,
        "support": support,
        "K": K,
        "R": R,
        "charged_outer": boundary // support,
        "charged_capacity": K // support,
    }


def saturation_barrier(prime: int, support: int, cofactor: int, q: int) -> dict[str, int]:
    if not (
        prime % 24 == 1
        and support > (prime - 1) ** 2 // 4
        and 1 < cofactor < prime
        and q > 1
        and cofactor % q == 0
    ):
        raise AssertionError("outside the C>1 saturation boundary")
    K = support * cofactor
    d = prime - cofactor
    promoted = support * q
    q_block = 1
    while K % (q_block * q) == 0:
        q_block *= q
    full_excess = q_block * q
    lcm_support = support * full_excess // gcd(support, full_excess)
    if not (
        K % promoted == 0
        and d % q != 0
        and (support * d) % promoted != 0
        and K % lcm_support != 0
    ):
        raise AssertionError("C>1 saturation provenance boundary changed")
    return {
        "prime": prime,
        "support": support,
        "cofactor": cofactor,
        "q": q,
        "K": K,
        "d": d,
        "promoted": promoted,
        "full_excess": full_excess,
        "lcm_support": lcm_support,
    }


def verify() -> None:
    for prime in (73, 241, 1009, 2521, 118801):
        row = r3_anchor_no_reentry(prime)
        if row["charged_outer"] < 1 or row["charged_capacity"] != (prime + 1) // 2:
            raise AssertionError("R=3 anchor did not remain a charged ascent")
    controls = (
        saturation_barrier(73, 1305, 2, 2),
        saturation_barrier(73, 1308, 3, 3),
        saturation_barrier(2137, 1142093, 4, 2),
    )
    if any(row["promoted"] <= row["support"] for row in controls):
        raise AssertionError("saturation control lost its proposed support increase")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified high-support anchor and saturation route exclusions")


if __name__ == "__main__":
    main()
