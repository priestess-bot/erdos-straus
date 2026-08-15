#!/usr/bin/env python3
"""Verify fixed controls for the actual-H4 q0 re-entry D residue gate.

The positive control checks the raw H4/source identities used by the proof. It
does not claim an actual 19-phase H3 predecessor or a complete-excess payload.
"""

from __future__ import annotations

import argparse
from math import gcd


P = 769
CARRIER_D = 5
Q = 77
H = 10
GAMMA = 1
Q0 = 77
T = 997
SMALL_D = 141


def positive_residue(value: int, modulus: int) -> int:
    residue = value % modulus
    return residue if residue else modulus


def verify_actual_raw_control() -> None:
    """Check a local H4 raw identity that realizes the nonempty D menu."""
    w = (P + 1) // 2
    multiplier = GAMMA + P * T
    divisor_bound = P * H - Q + 1
    delta = 2 * CARRIER_D * (4 * CARRIER_D * CARRIER_D - 2 * CARRIER_D + 1)
    r4_numerator = GAMMA * Q0 * Q0 * multiplier * SMALL_D - H
    if r4_numerator % (Q - 1):
        raise AssertionError("raw source identity is no longer integral")
    r4 = r4_numerator // (Q - 1)
    k4_numerator = P * r4 + 1
    if k4_numerator % 4:
        raise AssertionError("H4 support identity is no longer integral")
    k4 = k4_numerator // 4

    if (P, w, multiplier, divisor_bound, delta % P) != (769, 385, 766694, 7614, 141):
        raise AssertionError("D-residue raw control constants changed")
    if SMALL_D != positive_residue(delta, P) or divisor_bound % SMALL_D:
        raise AssertionError("D did not pass the forced residue/divisor gate")
    if (Q - 1) * r4 != GAMMA * Q0 * Q0 * multiplier * SMALL_D - H:
        raise AssertionError("actual re-entry source identity changed")
    if P * r4 + 1 != 4 * k4:
        raise AssertionError("actual H4 support identity changed")
    if (r4 % P, r4 % Q, r4 % 4, gcd(r4 - 1, k4), gcd(Q, k4)) != (1, H, 3, H, 1):
        raise AssertionError("H4 proper-overlap control changed")
    if k4 % SMALL_D or gcd(SMALL_D, Q0) != 1:
        raise AssertionError("normalized small divisor no longer divides K4")
    if gcd(w, k4 // 282) != CARRIER_D:
        raise AssertionError("carrier d control changed")


def verify_carrier_d_one_exclusion_control() -> None:
    """For d=1 the two residue candidates both miss the forced divisor."""
    p = 73
    d = 1
    q = (p + 1) // 2
    divisor_bound = p * (2 * d) - q + 1
    delta = 2 * d * (4 * d * d - 2 * d + 1)
    candidates = [positive_residue(delta, p), positive_residue(delta, p) + p]
    if (q, divisor_bound, delta, candidates) != (37, 110, 6, [6, 79]):
        raise AssertionError("carrier d=1 control constants changed")
    if any(divisor_bound % candidate == 0 for candidate in candidates):
        raise AssertionError("a d=1 residue candidate unexpectedly divides the bound")


def verify() -> None:
    verify_actual_raw_control()
    verify_carrier_d_one_exclusion_control()
    print("verified q0 re-entry D-residue gate and original carrier d=1 exclusion controls")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
