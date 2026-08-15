#!/usr/bin/env python3
"""Exactly discharge the H5 a=1 full-overlap finite divisor supermenu.

Every integer factored here is fixed by the 31 H3 phase selectors. The script
does not scan primes or denominators: it factors those fixed integers, then
rebuilds the one surviving affine row from the actual H3-to-H4 receipt.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm, prod

import sympy

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    FINAL_RESIDUAL,
    STEP,
    base_prime,
    h3_data,
    selector_a,
)
from type_ii_q_one_c2_19_phase_h5_a_one_full_overlap_finite_sieve import (
    CAPACITY_NUMERATOR,
    D_MULTIPLIER,
    D_OFFSET,
    MENU_DISTINCT_COUNT,
    MENU_ROW_COUNT,
)
from type_ii_q_one_c2_19_phase_maximal_fourth_anchor_completion import (
    complete_excess,
    positive_divisors,
)


PHASE_FACTOR_ROWS = (
    (280_759_115_953, 1, 564, 243, 486, 799, 1_123_036_463_812),
    (280_759_115_953, 1, 564, 243, 972, 1_598, 2_246_072_927_624),
    (17_587_777, 6, 2_122, 1, 293, 61, 3_200_975_414),
    (17_587_777, 6, 2_122, 1, 586, 122, 6_401_950_828),
    (17_587_777, 6, 2_122, 2, 293, 122, 6_401_950_828),
    (17_587_777, 6, 2_122, 2, 586, 244, 12_803_901_656),
    (14_449, 15, 431, 85, 1_105, 139, 887_912_188_887),
    (14_449, 15, 431, 1_105, 85, 139, 887_912_188_887),
    (14_449, 15, 431, 1_105, 1_105, 1_807, 11_542_858_455_531),
    (16_842_673, 22, 165, 1, 457, 588, 11_116_164_180),
    (147_076_273, 22, 165, 1, 1_371, 1_691, 32_503_856_333),
    (16_842_673, 22, 165, 1, 1_371, 1_764, 33_348_492_540),
    (24_481, 26, 317, 53, 1_219, 2_089, 633_160_695_831),
    (14_893_729, 27, 127, 1_409, 1_409, 161, 18_737_338_749_301),
    (425_032_897, 40, 184, 2, 1_352, 1_031, 37_402_894_936),
    (425_032_897, 40, 184, 4, 676, 1_031, 37_402_894_936),
    (425_032_897, 40, 184, 4, 1_352, 2_062, 74_805_789_872),
    (2_765_953, 57, 830, 1, 353, 617, 9_542_537_850),
    (2_765_953, 57, 830, 1, 706, 1_234, 19_085_075_700),
    (19_495_681, 75, 1_115, 1, 421, 317, 6_959_958_117),
    (8_145_219_601, 92, 1_761, 225, 225, 353, 480_567_956_459),
    (1_071_457, 103, 2_179, 643, 643, 1_117, 3_909_631_947_101),
    (49_692_913, 104, 260, 11, 1_276, 1_621, 150_867_683_868),
)
AFFINE_ROW = (14_449, 15, 431, 1_105, 85, 139, 11_815, 9_330_195, 887_912_188_887)


def menu_rows():
    """Yield the finite supermenu used by the full-overlap theorem."""
    for residue in sorted(FINAL_RESIDUAL):
        base = base_prime(residue)
        selector = selector_a(base)
        delta = abs(1_536 - selector)
        d_value = D_OFFSET - D_MULTIPLIER * selector
        for lambda_value in positive_divisors(delta):
            for carrier_overlap in positive_divisors(delta):
                for j_value in range(1, 2 * carrier_overlap):
                    candidate = (
                        d_value * j_value
                        + 2 * carrier_overlap * CAPACITY_NUMERATOR * lambda_value
                    )
                    yield (
                        residue,
                        base,
                        selector,
                        lambda_value,
                        carrier_overlap,
                        j_value,
                        candidate,
                    )


def actual_h4_receipt(prime: int) -> dict[str, int]:
    """Rebuild the true maximal H3-to-H4 data for one fixed phase prime."""
    data = h3_data(prime)
    m3 = int(data["M_3"])
    k3 = int(data["K_3"])
    r3 = int(data["R_3"])
    c3 = int(data["c_3"])
    block4, beta4 = complete_excess(r3 - 1, k3)
    overlap4 = gcd(m3, block4)
    lambda_value = beta4 * overlap4 // 2
    m4 = lcm(m3, block4)
    c4 = c3 * pow(m4 // m3, -1, prime) % prime
    w = (prime + 1) // 2
    d_value = D_OFFSET - D_MULTIPLIER * int(data["a"])
    lift, remainder = divmod(d_value * c4 + CAPACITY_NUMERATOR * lambda_value, prime)
    if not (
        prime % 24 == 1
        and gcd(w, m3) == 1
        and remainder == 0
        and lift >= 1
        and 1 <= c4 <= prime - 2
    ):
        raise AssertionError("the actual H3-to-H4 receipt changed")
    return {
        "selector": int(data["a"]),
        "g": gcd(w, c3),
        "lambda": lambda_value,
        "d": gcd(w, m4),
        "c4": c4,
        "t": lift,
    }


def factor_phase_menu() -> dict[str, object]:
    """Factor every fixed menu integer and retain only exact phase factors."""
    rows = 0
    factor_cache: dict[int, tuple[int, ...]] = {}
    phase_rows: list[tuple[int, int, int, int, int, int, int]] = []
    affine_rows: list[tuple[int, int, int, int, int, int, int, int, int]] = []
    actual_h4_rows: list[tuple[int, int, int, int, int, int, int, int, int]] = []

    for residue, base, selector, lambda_value, d, j_value, candidate in menu_rows():
        rows += 1
        factors = factor_cache.get(candidate)
        if factors is None:
            factorization = sympy.factorint(candidate)
            if not (
                prod(prime**exponent for prime, exponent in factorization.items()) == candidate
                and all(sympy.isprime(prime) for prime in factorization)
            ):
                raise AssertionError("a fixed menu integer was not factored exactly")
            factors = tuple(sorted(factorization))
            factor_cache[candidate] = factors

        for prime in factors:
            if not (prime >= base and (prime - base) % STEP == 0 and prime % 24 == 1):
                continue
            phase_rows.append(
                (prime, residue, selector, lambda_value, d, j_value, candidate)
            )
            if (prime + 1) % (2 * d):
                continue
            c4 = j_value * (prime + 1) // (2 * d)
            if not (1 <= c4 <= prime - 2):
                continue
            d_value = D_OFFSET - D_MULTIPLIER * selector
            lift, remainder = divmod(d_value * c4 + CAPACITY_NUMERATOR * lambda_value, prime)
            if remainder or lift < 1:
                continue
            row = (prime, residue, selector, lambda_value, d, j_value, c4, lift, candidate)
            affine_rows.append(row)
            actual = actual_h4_receipt(prime)
            if (
                actual["lambda"] == lambda_value
                and actual["d"] == d
                and actual["c4"] == c4
            ):
                actual_h4_rows.append(row)

    if not (
        rows == MENU_ROW_COUNT
        and len(factor_cache) == MENU_DISTINCT_COUNT
        and tuple(phase_rows) == PHASE_FACTOR_ROWS
        and tuple(affine_rows) == (AFFINE_ROW,)
        and actual_h4_rows == []
    ):
        raise AssertionError("the H5 a=1 finite factor screen changed")
    return {
        "rows": rows,
        "distinct_constants": len(factor_cache),
        "phase_factor_rows": len(phase_rows),
        "affine_rows": affine_rows,
        "actual_h4_rows": actual_h4_rows,
        "p14449_actual_h4": actual_h4_receipt(14_449),
    }


def verify() -> None:
    result = factor_phase_menu()
    if result != {
        "rows": MENU_ROW_COUNT,
        "distinct_constants": MENU_DISTINCT_COUNT,
        "phase_factor_rows": 23,
        "affine_rows": [AFFINE_ROW],
        "actual_h4_rows": [],
        "p14449_actual_h4": {
            "selector": 431,
            "g": 5,
            "lambda": 5,
            "d": 1,
            "c4": 13_391,
            "t": 10_167_387,
        },
    }:
        raise AssertionError("the H5 a=1 completion receipt changed")
    print(
        "verified 377516 exact fixed-constant factorizations: 23 phase-factor rows, "
        "1 affine row, and 0 actual H3-to-H4 receipts"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="factor and discharge the finite menu")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
