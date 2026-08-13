#!/usr/bin/env python3
"""Verify an anchor-local actual endpoint s=0 return and p-free interface.

This focused verifier checks one fixed raw path and its canonical checkpoint.
It performs no prime, denominator, selector-history, or certificate-menu scan.
"""

from __future__ import annotations

import argparse
from math import gcd


P = 97
R_PARAMETER = 66_988_440
RAW_LABELS = (97, 67, 131, 3, 42_101, 2_107_984_905_029)
RAW_EXCESS_LAYERS = (1, 1, 1, 2, 1, 1)
EXPECTED_SMALL_SIDES = (
    1,
    1_260_454_486_942,
    1_806_024_339_499,
    919_527_182_396,
    40_448_186_016_993,
    960_741_693,
    58,
)
TARGET_LABELS = (97, 97, 3, 3, 5, 5, 5, 5, 5, 56_886_937_939_854_283)
TARGET_EXCESS_LAYERS = (2, 1, 2, 1, 5, 4, 3, 2, 1, 1)
TARGET_EXPECTED_SMALL_SIDES = (
    98,
    465_584_032_701_494_897_428_125,
    4_799_835_388_675_205_128_125,
    1_599_945_129_558_401_709_375,
    533_315_043_186_133_903_125,
    106_663_008_637_226_780_625,
    21_332_601_727_445_356_125,
    4_266_520_345_489_071_225,
    853_304_069_097_814_245,
    170_660_813_819_562_849,
    3,
)


def is_prime_64(value: int) -> bool:
    if value < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if value % prime == 0:
            return value == prime
    odd = value - 1
    exponent = 0
    while odd % 2 == 0:
        exponent += 1
        odd //= 2
    for base in (2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022):
        if base % value == 0:
            continue
        witness = pow(base, odd, value)
        if witness in (1, value - 1):
            continue
        for _ in range(exponent - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    common = gcd(value, capacity)
    exposed = value // common
    block = gcd(value, pow(exposed, value.bit_length(), value))
    return block, value // block


def replay_raw_path(
    residual: int,
    capacity: int,
    start: int,
    labels: tuple[int, ...],
    excess_layers: tuple[int, ...],
    expected_small_sides: tuple[int, ...],
) -> tuple[int, int]:
    left, right = sorted((start, residual - start))
    if gcd(left, right) != 1 or expected_small_sides[0] != left:
        raise AssertionError("raw path has lost its primitive start")
    for index, (label, excess, expected) in enumerate(
        zip(labels, excess_layers, expected_small_sides[1:]), start=1
    ):
        if not is_prime_64(label):
            raise AssertionError(f"raw label {label} is not prime")
        selected = [side for side in (left, right) if side % label == 0]
        if len(selected) != 1:
            raise AssertionError(f"raw step {index} lost its unique selected side")
        selected_side = selected[0]
        other_side = right if selected_side == left else left
        if valuation(selected_side, label) - valuation(capacity, label) != excess:
            raise AssertionError(f"raw step {index} lost its exact excess layer")
        divided = selected_side // label
        translated = (other_side + residual * (label - 1)) // label
        if not (
            (other_side + residual * (label - 1)) % label == 0
            and gcd(label, residual * other_side) == 1
            and gcd(divided, translated) == 1
            and divided + translated == residual
        ):
            raise AssertionError(f"raw step {index} changed")
        left, right = sorted((divided, translated))
        if left != expected:
            raise AssertionError(f"raw step {index} reached {left}, expected {expected}")
    return left, right


def verify() -> None:
    g = (P + 1) // 2
    b = 2 * P * R_PARAMETER - 1
    n = (P + 1) * b - 1
    adjustable = P * P * R_PARAMETER - g
    support = g * adjustable
    capacity = support * (P - 1)
    residual = (P - 1) * n - 1
    h, z = replay_raw_path(
        residual,
        capacity,
        1,
        RAW_LABELS,
        RAW_EXCESS_LAYERS,
        EXPECTED_SMALL_SIDES,
    )
    block, beta = complete_excess(z, capacity)
    support_gcd = gcd(support, block)
    multiplier = block // support_gcd
    charged_residual = beta * support_gcd

    if not (
        (b, n, adjustable, support, capacity, residual)
        == (
            12_995_757_359,
            1_273_584_221_181,
            630_294_231_911,
            30_884_417_363_639,
            2_964_904_066_909_344,
            122_264_085_233_375,
        )
        and (h, z) == (58, 122_264_085_233_317)
        and (block, beta, support_gcd, multiplier, charged_residual)
        == (369_377_901_007, 331, 1, 369_377_901_007, 331)
        and capacity % (h * beta) == 0
        and multiplier % (P * P) == 1
    ):
        raise AssertionError("actual endpoint s=0 receipt changed")

    relay = (multiplier - 1) // (P * P)
    target_r = R_PARAMETER + relay * adjustable
    target_b = 2 * P * target_r - 1
    target_n = (P + 1) * target_b - 1
    target_adjustable = P * P * target_r - g
    target_support = g * target_adjustable
    target_capacity = target_support * (P - 1)
    target_residual = (P - 1) * target_n - 1
    ordinary_unit = 2 * (P - 1) * target_r - 1
    ordinary_multiplier = P * ordinary_unit

    if not (
        relay == 39_257_934
        and target_r == 24_744_049_357_009_720_314
        and target_b == multiplier * b - P * relay
        and target_n == multiplier * n - P * relay
        and target_adjustable == multiplier * adjustable
        and target_support == multiplier * support
        and ordinary_multiplier == (P - 1) * target_b - 1
        and ordinary_unit % P == 1
        and target_residual - 1 == P * (P + 1) * ordinary_unit
    ):
        raise AssertionError("canonical p-free return normal form changed")

    peeled = (target_residual - 1) // P
    other = target_residual - peeled
    if not (
        peeled == (P + 1) * ordinary_unit
        and other == 1 + (P - 1) * peeled
        and gcd(peeled, target_capacity) == P + 1
        and gcd(other, target_capacity) == 1
    ):
        raise AssertionError("ordinary p-block peel capacities changed")

    root = P + 1
    if not (
        target_residual - root == P * ((P + 1) * ordinary_unit - 1)
        and valuation(target_residual - root, P) == 2
        and gcd(target_residual - root, target_capacity) == 3
    ):
        raise AssertionError("root departure height control changed")

    h3, z3 = replay_raw_path(
        target_residual,
        target_capacity,
        root,
        TARGET_LABELS,
        TARGET_EXCESS_LAYERS,
        TARGET_EXPECTED_SMALL_SIDES,
    )
    block3, beta3 = complete_excess(z3, target_capacity)
    multiplier3 = block3 // gcd(target_support, block3)
    strict_capacity = (-pow(multiplier3, -1, P)) % P
    if not (
        (h3, beta3) == (3, 4)
        and target_capacity % (h3 * beta3) == 0
        and gcd(target_support, block3) == 1
        and multiplier3 % P == 48
        and strict_capacity == 2 < P - 1
    ):
        raise AssertionError("post-return h=3 strict arithmetic candidate changed")

    print(
        "verified an anchor-local actual endpoint s=0 receipt and its p-free "
        "return, a root-height-two control, and an h=3 capacity candidate "
        "96 -> 2 conditional on E1-E5 admission"
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
