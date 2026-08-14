#!/usr/bin/env python3
"""Verify the fixed root-divisor gate and its canonical-boundary control."""

from __future__ import annotations

import argparse

from type_i_root_capacity_stutter_actual_maximality_boundary import chart


def pair_gate(p: int, u: int, m: int, a: int, e: int) -> tuple[int, int, int]:
    layer = a * m
    shift = m - a
    bound = layer * layer + layer * shift + shift * shift
    h = 3 * u
    p_cyclotomic = p * p + p + 1
    if not (
        layer * p == 9 * u * u + 3 * (a - 1) * u + shift
        and (a + 3 * u) % m == 0
        and (a + 3 * u) // m == e
        and p_cyclotomic % h == 0
        and bound % u == 0
        and layer * layer * p_cyclotomic
        == bound + 3 * u * (e * m - 1) * (layer * p + a * (m - 1) + m)
    ):
        raise AssertionError("pair root-divisor identities changed")
    return layer, shift, bound


def verify_shadow_boundary() -> None:
    p, r = 54_481, 2_543_533_812
    u, m, a, e, d0 = 4_021, 13, 209, 944, 696_191
    layer, shift, bound = pair_gate(p, u, m, a, e)
    state = chart(p, r)
    if not (
        p % 24 == 1
        and p == 7 * 43 * 181
        and state["u"] == u
        and state["h"] == 3 * u < p
        and (layer, shift, bound // u) == (2_717, -196, 1_713)
        and bound == 6_887_973
        and d0 == m * p + 1 - state["h"]
        and e * d0 == p * state["h"] + 1
        and state["D"] == 16 * d0
        and state["D"] % p != (1 - state["h"]) % p
    ):
        raise AssertionError("canonical-boundary control changed")


def verify_residue_forms() -> None:
    # B is a^2 modulo m and m^2 modulo a, the local step behind (10).
    for m, a in ((3, 9), (4, 5), (6, 3), (13, 209)):
        layer = a * m
        shift = m - a
        bound = layer * layer + layer * shift + shift * shift
        if bound % m != (a * a) % m or bound % a != (m * m) % a:
            raise AssertionError("pair root-divisor residue form changed")


def verify() -> None:
    verify_shadow_boundary()
    verify_residue_forms()
    print("verified pair root-divisor gate and canonical-boundary control")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
