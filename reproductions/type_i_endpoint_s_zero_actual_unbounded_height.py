#!/usr/bin/env python3
"""Verify an anchor-local actual endpoint s=0 family with unbounded target height.

The verifier derives the affine raw-path fixtures and checks five Hensel
controls. It does not scan primes, denominators, or selector history.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


P = 97
R0 = 66_988_440
R_STEP = 4_243_815_461_730_835_674_059_638_914_706_837_844_637
LABELS = (97, 67, 131, 3, 42_101)
EXPECTED_EXCESS = (1, 1, 1, 2, 1)
Q0 = 2_107_984_905_029
Q_STEP = 133_543_920_917_590_341_086_691_816_028_640_377_650_310_464
E0 = 369_377_901_007
E_STEP = 23_400_629_237_489_299_674_263_740_436_419_983_401_253_504
H = (
    465_584_032_701_494_897_428_125,
    58_990_856_239_305_572_631_703_764_704_555_659_300_682_708_034_054_096_000,
    1_868_578_428_073_766_217_858_525_191_856_689_368_432_694_029_295_254_181_783_788_414_861_243_374_903_854_993_031_168,
)
HEIGHT_CONTROLS = ((0, 2), (9_021, 3), (178_383, 4), (33_947_284, 5), (1_096_298_656, 6))
SATURATED_HEIGHT_CONTROLS = (
    (13_878_275, 2),
    (1_560_679_851, 3),
    (159_352_884_183, 4),
    (5_530_281_072_792, 5),
    (1_893_346_463_502_273, 6),
)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def evaluate(poly: tuple[int, ...], value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def affine_divide(value: tuple[int, int], divisor: int) -> tuple[int, int]:
    if value[0] % divisor or value[1] % divisor:
        raise AssertionError("affine raw side is not identically divisible")
    return value[0] // divisor, value[1] // divisor


def chart() -> dict[str, tuple[int, int]]:
    r = (R0, R_STEP)
    b = (2 * P * r[0] - 1, 2 * P * r[1])
    n = ((P + 1) * b[0] - 1, (P + 1) * b[1])
    adjustable = (P * P * r[0] - (P + 1) // 2, P * P * r[1])
    support = (
        (P + 1) // 2 * adjustable[0],
        (P + 1) // 2 * adjustable[1],
    )
    capacity = ((P - 1) * support[0], (P - 1) * support[1])
    residual = ((P - 1) * n[0] - 1, (P - 1) * n[1])
    return {
        "r": r,
        "adjustable": adjustable,
        "support": support,
        "capacity": capacity,
        "residual": residual,
    }


def verify_affine_raw_prefix(data: dict[str, tuple[int, int]]) -> None:
    residual = data["residual"]
    capacity = data["capacity"]
    left = (1, 0)
    right = (residual[0] - 1, residual[1])

    for label, expected_excess in zip(LABELS, EXPECTED_EXCESS):
        if not is_prime(label):
            raise AssertionError(f"raw label {label} is not prime")
        candidates = [
            side
            for side in (left, right)
            if side[0] % label == 0 and side[1] % label == 0
        ]
        if len(candidates) != 1:
            raise AssertionError(f"label {label} lost its affine selected side")
        selected = candidates[0]
        other = right if selected == left else left
        selected_base_v = valuation(selected[0], label)
        selected_slope_v = valuation(selected[1], label)
        capacity_base_v = valuation(capacity[0], label)
        capacity_slope_v = valuation(capacity[1], label)
        excess = selected_base_v - capacity_base_v
        if not (
            excess == expected_excess
            and selected_slope_v > selected_base_v
            and capacity_slope_v > capacity_base_v
            and other[0] % label != 0
            and other[1] % label == 0
        ):
            raise AssertionError(f"label {label} lost its exact affine raw cell")
        divided = affine_divide(selected, label)
        translated = (
            residual[0] - divided[0],
            residual[1] - divided[1],
        )
        left, right = sorted((divided, translated), key=lambda side: side[0])

    expected_left = (
        960_741_693,
        60_864_388_718_409_153_172_754_793_872_602_096_902_912,
    )
    expected_right = (58 * Q0, 58 * Q_STEP)
    if (left, right) != (expected_left, expected_right):
        raise AssertionError("five-step affine raw prefix changed")


def verify_linear_gcd(
    value: tuple[int, int], capacity: tuple[int, int], expected_primes: set[int]
) -> None:
    determinant = value[0] * capacity[1] - value[1] * capacity[0]
    remainder = abs(determinant)
    for prime in expected_primes:
        if remainder % prime:
            raise AssertionError("declared determinant prime support changed")
        while remainder % prime == 0:
            remainder //= prime
    if remainder != 1:
        raise AssertionError("linear gcd determinant support changed")
    for prime in expected_primes:
        if value[1] % prime != 0 or value[0] % prime == 0:
            raise AssertionError("linear value no longer has a fixed nonzero residue")


def verify() -> None:
    data = chart()
    verify_affine_raw_prefix(data)
    capacity = data["capacity"]
    support = data["support"]
    common_primes = {2, 3, 7, 17, 23, 29, 67, 97, 131, 331, 42_101, 995_147}
    verify_linear_gcd((Q0, Q_STEP), capacity, common_primes)
    verify_linear_gcd((E0, E_STEP), support, common_primes - {2})

    if not (
        Fraction(1, 28) + Fraction(1, 194) + Fraction(1, 2_716)
        == Fraction(4, P)
        and E0 % (P * P) == 1
        and E_STEP % (P * P) == 0
        and E0 % 2 == 1
        and E_STEP % 2 == 0
        and E0 % 3 == 1
        and E_STEP % 3 == 0
        and capacity[0] % (58 * 331) == 0
        and capacity[1] % (58 * 331) == 0
        and data["residual"] == (58 + 331 * E0, 331 * E_STEP)
    ):
        raise AssertionError("endpoint complete-excess affine receipt changed")

    source_root = (
        (data["residual"][0] - (P + 1)) // P,
        data["residual"][1] // P,
    )
    if not (
        (data["residual"][0] - (P + 1)) % P == 0
        and data["residual"][1] % P == 0
        and tuple(coefficient % P for coefficient in source_root) == (3, 0)
    ):
        raise AssertionError("source root height-one family changed")

    adjustable = data["adjustable"]
    relay = ((E0 - 1) // (P * P), E_STEP // (P * P))
    target_r = (
        R0 + relay[0] * adjustable[0],
        R_STEP + relay[0] * adjustable[1] + relay[1] * adjustable[0],
        relay[1] * adjustable[1],
    )
    target_residual = tuple(2 * P * (P * P - 1) * coefficient for coefficient in target_r)
    target_residual = (
        target_residual[0] - P * P - P + 1,
        target_residual[1],
        target_residual[2],
    )
    derived_height = list(target_residual)
    derived_height[0] -= P + 1
    derived_height = tuple(coefficient // P for coefficient in derived_height)
    if derived_height != H or tuple(coefficient % P for coefficient in H) != (0, 27, 0):
        raise AssertionError("target root-height polynomial changed")

    for index, expected_height in HEIGHT_CONTROLS:
        if valuation(P * evaluate(H, index), P) != expected_height:
            raise AssertionError(f"height control at k={index} changed")

    root_modulus = (P * P + P + 1) // 3
    root_capacity_poly = (
        (2 * target_r[0] + 1) % root_modulus,
        (2 * target_r[1]) % root_modulus,
        (2 * target_r[2]) % root_modulus,
    )
    saturated_classes = tuple(
        index
        for index in range(root_modulus)
        if evaluate(root_capacity_poly, index) % root_modulus == 0
    )
    if root_capacity_poly != (1_264, 1_783, 1_641) or saturated_classes != (
        1_224,
        1_633,
    ):
        raise AssertionError("saturated root-capacity classes changed")
    for index, expected_height in SATURATED_HEIGHT_CONTROLS:
        if not (
            index % root_modulus == 1_224
            and valuation(P * evaluate(H, index), P) == expected_height
        ):
            raise AssertionError(f"saturated height control at k={index} changed")

    print(
        "verified an anchor-local actual endpoint s=0 family, its fixed five-step "
        "raw prefix plus capacity-peeling suffix, and conditional target root "
        "heights 2 through 6 with saturated capacity p^2+p+1"
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
