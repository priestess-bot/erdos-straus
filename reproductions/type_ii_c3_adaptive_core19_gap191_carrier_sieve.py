#!/usr/bin/env python3
"""Verify the adaptive core-19 gap-191 carrier and strict-descent controls.

The program proves an infinite parameter subray with a moving square divisor,
checks its explicit l=61 two-tail lift, and records one exact gap-191 miss.
It does not claim that gap 191, or this carrier sieve, covers every prime point.
"""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_high_r_chart_two_anchor as shared


GAP = 191
N0 = 946_563_871
N_STEP = 8_505_305_445
P0 = 181_740_263_041
P_STEP = 1_633_018_645_440
EXPECTED_S = {
    1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 36, 48, 64, 65, 69, 72, 96, 97,
    128, 130, 144,
}
EXPECTED_T = {
    47, 61, 63, 94, 95, 119, 122, 126, 127, 143, 155, 159, 167, 175,
    179, 183, 185, 187, 188, 189, 190,
}


def assert_egyptian(denominator: int, terms: tuple[int, int, int]) -> None:
    """Check one displayed three-unit-fraction identity exactly."""
    first, second, third = terms
    if min(terms) <= 0 or 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity changed")


def ray(w: int) -> tuple[int, int, int]:
    """Return (N, p, x) on the v=8w gap-191 subray."""
    if w < 0:
        raise AssertionError("the focused ray has nonnegative parameters")
    N = N0 + N_STEP * w
    p = 192 * N - GAP
    x = (p + GAP) // 4
    if p != P0 + P_STEP * w or x != 48 * N or (p - 1) % 192:
        raise AssertionError("gap-191 affine normalization changed")
    return N, p, x


def divisors_of_48() -> tuple[int, ...]:
    return tuple(value for value in range(1, 49) if 48 % value == 0)


def signed_ratio_box_48() -> set[int]:
    """Build R_191(48) from coprime factor-pair orientations."""
    residues: set[int] = set()
    for left in divisors_of_48():
        for right in divisors_of_48():
            if gcd(left, right) == 1:
                residues.add(left * pow(right, -1, GAP) % GAP)
    return residues


def factor_pair_lift(*, p: int, N: int, A: int, B: int, C: int) -> dict[str, object]:
    """Verify the complete gap-191 factor pair and its strict two-tail lift."""
    x = (p + GAP) // 4
    if not (
        p % 24 == 1
        and (p - 1) % (GAP + 1) == 0
        and (p + GAP) // (GAP + 1) == N
        and x == A * B * C
        and gcd(A, B) == 1
        and A <= B
        and (A + B) % GAP == 0
    ):
        raise AssertionError("gap-191 factor-pair normal form failed")
    carrier = (A + B) // GAP
    divisor = A * A * C
    if x * x % divisor or divisor > x or (x + divisor) % GAP:
        raise AssertionError("gap-191 Type II divisor conditions failed")

    descent = (x, A * C * carrier, B * C * carrier)
    terminal = (x, p * descent[1], p * descent[2])
    assert_egyptian(N, descent)
    assert_egyptian(p, terminal)
    if N >= p:
        raise AssertionError("gap-191 source was not strictly smaller")
    return {
        "p": p,
        "source": N,
        "x": x,
        "A": A,
        "B": B,
        "C": C,
        "carrier": carrier,
        "divisor": divisor,
        "descent_denominators": list(descent),
        "terminal_denominators": list(terminal),
    }


def verify_carrier_box() -> dict[str, object]:
    """Verify the exact finite ratio carrier and its residue complement."""
    ratios = signed_ratio_box_48()
    targets = {(-pow(value, -1, GAP)) % GAP for value in ratios}
    if ratios != EXPECTED_S or targets != EXPECTED_T:
        raise AssertionError("gap-191 carrier residue sets changed")
    if gcd(N0, N_STEP) != 1 or gcd(P0, P_STEP) != 1:
        raise AssertionError("the two affine prime progressions ceased to be primitive")
    return {
        "ratio_box_R_191_48": sorted(ratios),
        "carrier_residue_classes": sorted(targets),
        "primitive_N_progression": True,
        "primitive_p_progression": True,
    }


def verify_l61_subray() -> dict[str, object]:
    """Check the explicit l=61 moving-square terminal family at z=0."""
    ell = 61
    if ell not in EXPECTED_T or (3 * ell + 8) != GAP:
        raise AssertionError("the l=61 carrier relation changed")
    if N0 % ell != 31 or N_STEP % ell != 49 or (31 + 49 * 28) % ell:
        raise AssertionError("the l=61 parameter congruence changed")

    w = 28
    N, p, x = ray(w)
    M = N // ell
    if N % ell or M != 3_919_592_071 or p != 45_906_262_335_361:
        raise AssertionError("the l=61 focused subray changed")
    if gcd(p, P_STEP * ell) != 1:
        raise AssertionError("the l=61 prime progression ceased to be primitive")
    if not shared.is_prime(p):
        raise AssertionError("the displayed l=61 prime point is no longer prime")
    receipt = factor_pair_lift(p=p, N=N, A=8, B=183, C=2 * M)
    if receipt["divisor"] != 128 * M or x != 2_928 * M:
        raise AssertionError("the moving square-only divisor changed")
    if receipt["descent_denominators"] != [2_928 * M, 16 * M, 366 * M]:
        raise AssertionError("the l=61 descent shape changed")
    if receipt["terminal_denominators"] != [2_928 * M, 16 * M * p, 366 * M * p]:
        raise AssertionError("the l=61 terminal shape changed")

    # On v=224+488z, x=2928M and d=128M.  This is square-only: 128|E^2
    # but 128 does not divide E=2928.
    E = 2_928
    if not (E == gcd(2_928 * N_STEP, 2_928 * M) and E * E % 128 == 0 and E % 128 != 0):
        raise AssertionError("the square-only affine divisor boundary changed")
    if (E + 128) % GAP:
        raise AssertionError("the moving divisor lost its gap congruence")
    return {
        "ell": ell,
        "w": w,
        "M": M,
        "primitive_p_progression": True,
        "receipt": receipt,
    }


def verify_v32_gap_miss() -> dict[str, object]:
    """Prove one prime point has no complete Type II factor pair at gap 191."""
    w = 4
    N, p, x = ray(w)
    if (N, p) != (34_967_785_651, 6_713_814_844_801):
        raise AssertionError("v=32 gap-191 control changed")
    if not shared.is_prime(N) or not shared.is_prime(p) or gcd(N, 48) != 1:
        raise AssertionError("v=32 factorization control changed")
    if N % GAP != 150:
        raise AssertionError("v=32 carrier residue changed")
    ratios = signed_ratio_box_48()
    full_ratio_box = {
        residue * pow(N, exponent, GAP) % GAP
        for residue in ratios
        for exponent in (-1, 0, 1)
    }
    targets = {(-pow(N, -exponent, GAP)) % GAP for exponent in (-1, 0, 1)}
    if targets != {14, 41, 190} or not targets.isdisjoint(ratios):
        raise AssertionError("v=32 no-gap-191 witness changed")
    if (GAP - 1) in full_ratio_box:
        raise AssertionError("v=32 unexpectedly acquired a gap-191 factor pair")
    return {
        "v": 32,
        "w": w,
        "p": p,
        "N": N,
        "x": x,
        "complete_gap_191_factor_pair": False,
        "excluded_carrier_targets": sorted(targets),
    }


def build_result() -> dict[str, object]:
    """Build the carrier-family, strict-lift, and exact-miss control receipt."""
    return {
        "certificate_type": "c3_adaptive_core19_gap191_carrier_sieve_v1",
        "scope": (
            "An infinite moving-divisor terminal family and one complete gap-191 miss. "
            "It does not prove a pointwise terminal cover or a selector."
        ),
        "carrier_box": verify_carrier_box(),
        "l61_strict_descent": verify_l61_subray(),
        "v32_gap_191_miss": verify_v32_gap_miss(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified adaptive core-19 gap-191 carrier sieve controls")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
