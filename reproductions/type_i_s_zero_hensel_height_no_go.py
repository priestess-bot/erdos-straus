#!/usr/bin/env python3
"""Verify p=73 Hensel candidates and their uniform priority preemption.

This focused verifier derives four small integer polynomials and checks six
Hensel controls. It performs no prime, denominator, or selector-history scan.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, lcm


P = 73
G = 37
V = 12_786_307_560
HENSEL_CONTROLS = (
    (1, 3, 204_414_698_961_777, 4),
    (2, 1_536, 104_660_325_868_400_697, 44),
    (3, 65_484, 4_461_964_048_936_424_217, 33),
    (4, 3_566_637, 243_024_342_886_910_711_937, 65),
    (5, 883_912_108, 60_228_209_155_146_445_501_977, 42),
    (6, 79_660_632_642, 5_427_934_746_871_531_913_488_137, 9),
)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return tuple(
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    )


def scale(poly: tuple[int, ...], factor: int) -> tuple[int, ...]:
    return tuple(factor * coefficient for coefficient in poly)


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] += left_coefficient * right_coefficient
    return tuple(result)


def evaluate(poly: tuple[int, ...], value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def derive_polynomials() -> dict[str, tuple[int, ...]]:
    r = (57, P * P * V)
    x = add(scale(r, 767_232), (-5_326,))
    y = add(scale(r, 10_656), (-75,))
    support = add(scale(r, 197_173), (-1_369,))
    q_x = tuple(coefficient // 2 for coefficient in x)
    q_y = tuple(coefficient // 3 for coefficient in y)
    residual = add(x, y)
    capacity = scale(support, P - 1)
    multiplier = multiply(q_x, q_y)
    relay = tuple(
        (coefficient - (1 if index == 0 else 0)) // (P * P)
        for index, coefficient in enumerate(multiplier)
    )
    adjustable = add(scale(r, P * P), (-G,))
    target_r = add(r, multiply(relay, adjustable))
    height = add(scale(target_r, 2 * (P * P - 1)), (-75,))
    endpoint_q3 = tuple(
        (coefficient - (3 if index == 0 else 0)) // 4
        for index, coefficient in enumerate(residual)
    )
    return {
        "r": r,
        "x": x,
        "y": y,
        "support": support,
        "q_x": q_x,
        "q_y": q_y,
        "residual": residual,
        "capacity": capacity,
        "multiplier": multiplier,
        "relay": relay,
        "adjustable": adjustable,
        "target_r": target_r,
        "height": height,
        "endpoint_q3": endpoint_q3,
    }


def verify_fixed_cell(polys: dict[str, tuple[int, ...]]) -> None:
    if not (
        V == lcm(72, 197_210, 199_911)
        and polys["x"]
        == (43_726_898, 52_277_832_771_266_119_680)
        and polys["y"] == (607_317, 726_081_010_712_029_440)
        and polys["support"]
        == (11_237_492, 13_435_019_812_793_072_520)
        and polys["q_x"]
        == (21_863_449, 26_138_916_385_633_059_840)
        and polys["q_y"] == (202_439, 242_027_003_570_676_480)
    ):
        raise AssertionError("fixed-cell linear polynomials changed")

    determinant_x = 767_232 * (-1_369) - 197_173 * (-5_326)
    determinant_y = 10_656 * (-1_369) - 197_173 * (-75)
    x0, y0, support0 = (
        polys["x"][0],
        polys["y"][0],
        polys["support"][0],
    )
    if not (
        determinant_x == -197_210
        and determinant_y == 199_911
        and V % abs(determinant_x) == V % abs(determinant_y) == V % 72 == 0
        and gcd(x0, support0) == 2
        and gcd(y0, support0) == 1
        and gcd(x0, 72) == 2
        and gcd(y0, 72) == 3
        and gcd(polys["q_x"][0], support0) == 1
        and gcd(polys["q_y"][0], support0) == 1
    ):
        raise AssertionError("resultant or base-cell gcd changed")

    for index in range(7):
        r = evaluate(polys["r"], index)
        x = evaluate(polys["x"], index)
        y = evaluate(polys["y"], index)
        support = evaluate(polys["support"], index)
        residual = evaluate(polys["residual"], index)
        capacity = evaluate(polys["capacity"], index)
        b = 2 * P * r - 1
        n = (P + 1) * b - 1
        if not (
            support == (P * n - 1) // 4
            and capacity == (P - 1) * support
            and residual == (P - 1) * n - 1 == x + y
            and gcd(residual - 1, capacity) == P + 1
            and capacity % (P + 1) == 0
            and gcd(P + 1, residual - (P + 1)) == 1
            and valuation(residual - (P + 1), P) == 1
            and y == (residual - (P + 1)) // P
            and gcd(x, y) == 1
            and gcd(x, support) == 2
            and gcd(y, support) == 1
            and gcd(x, capacity) == 2
            and gcd(y, capacity) == 3
            and x == 2 * evaluate(polys["q_x"], index)
            and y == 3 * evaluate(polys["q_y"], index)
            and gcd(evaluate(polys["q_x"], index), support) == 1
            and gcd(evaluate(polys["q_y"], index), support) == 1
        ):
            raise AssertionError(f"fixed complete-excess cell changed at j={index}")


def verify_hensel_family(polys: dict[str, tuple[int, ...]]) -> None:
    if not (
        polys["multiplier"]
        == (
            4_426_014_752_111,
            10_583_081_143_381_474_116_929_280,
            6_326_323_609_399_226_524_762_256_681_120_563_200,
        )
        and polys["relay"]
        == (
            830_552_590,
            1_985_941_291_683_519_256_320,
            1_187_150_236_329_372_588_621_177_834_700_800,
        )
        and polys["adjustable"] == (303_716, 363_108_643_589_001_960)
        and polys["target_r"]
        == (
            252_252_110_424_497,
            904_742_969_729_252_346_078_548_760,
            1_081_668_969_847_604_900_998_918_562_674_210_560_000,
            431_064_512_049_921_597_708_096_784_888_033_241_161_727_213_568_000,
        )
        and polys["height"]
        == (
            2_687_998_488_683_439_957,
            9_640_941_085_434_912_999_813_015_586_560,
            11_526_264_542_696_077_825_044_476_203_856_387_727_360_000,
            4_593_423_440_403_964_545_177_479_339_766_882_217_819_365_187_780_608_000,
        )
    ):
        raise AssertionError("s=0 relay or height polynomial changed")

    if not (
        tuple(coefficient % (P * P) for coefficient in polys["multiplier"])
        == (1, 0, 0)
        and tuple(coefficient % P for coefficient in polys["relay"]) == (54, 45, 0)
        and tuple(coefficient % P for coefficient in polys["height"]) == (11, 45, 0, 0)
        and evaluate(polys["height"], 3) % P == 0
        and 45 % P != 0
    ):
        raise AssertionError("Hensel congruence changed")

    for expected_height, index, expected_r, expected_unit in HENSEL_CONTROLS:
        source_r = evaluate(polys["r"], index)
        source_residual = evaluate(polys["residual"], index)
        source_capacity = evaluate(polys["capacity"], index)
        multiplier = evaluate(polys["multiplier"], index)
        height = evaluate(polys["height"], index)
        if not (
            source_r == expected_r
            and index % P == 3
            and gcd(source_residual - 1, source_capacity) == P + 1
            and valuation(source_residual - (P + 1), P) == 1
            and valuation(multiplier - 1, P) == 2
            and valuation(height, P) == expected_height
            and (height // P**expected_height) % P == expected_unit
            and valuation(P * height, P) == expected_height + 1
        ):
            raise AssertionError(
                f"Hensel control for target height {expected_height + 1} changed"
            )


def verify_priority_preemption(polys: dict[str, tuple[int, ...]]) -> None:
    q3 = polys["endpoint_q3"]
    support = polys["support"]
    determinant = 194_472 * (-1_369) - 197_173 * (-1_351)
    if not (
        Fraction(1, 20) + Fraction(1, 219) + Fraction(1, 4_380)
        == Fraction(4, P)
        and q3 == (11_083_553, 13_250_978_445_494_537_280)
        and determinant == 148_555 == 5 * 11 * 37 * 73
        and tuple(coefficient % 11 for coefficient in support) == (2, 4)
        and tuple(coefficient % 11 for coefficient in q3) == (8, 5)
        and tuple(coefficient % 72 for coefficient in q3) == (17, 0)
        and tuple(coefficient % P for coefficient in q3) == (36, 0)
    ):
        raise AssertionError("terminal or h=3 priority certificate changed")

    for _, index, _, _ in HENSEL_CONTROLS:
        residual = evaluate(polys["residual"], index)
        capacity = evaluate(polys["capacity"], index)
        support_value = evaluate(support, index)
        q3_value = evaluate(q3, index)
        if not (
            index % 11 != 5
            and residual - 3 == 4 * q3_value
            and capacity % 12 == 0
            and gcd(support_value, q3_value) == 1
            and gcd(q3_value, capacity) == 1
            and q3_value % P == 36
            and (-pow(q3_value, -1, P)) % P == 2
        ):
            raise AssertionError("h=3 strict priority control changed")

    index = 5
    residual = evaluate(polys["residual"], index)
    capacity = evaluate(polys["capacity"], index)
    support_value = evaluate(support, index)
    q3_value = evaluate(q3, index)
    support_gcd = gcd(support_value, q3_value)
    multiplier = q3_value // support_gcd
    if not (
        residual - 3 == 4 * q3_value
        and support_gcd == 11
        and gcd(q3_value, capacity) == 11
        and gcd(multiplier, capacity) == 1
        and capacity % 44 == 0
        and multiplier % P == 63
        and (-pow(multiplier, -1, P)) % P == 22
    ):
        raise AssertionError("j=5 h=3 strict priority branch changed")


def verify() -> None:
    polys = derive_polynomials()
    verify_fixed_cell(polys)
    verify_hensel_family(polys)
    verify_priority_preemption(polys)
    print(
        "verified fixed-cell arithmetic candidates with target root heights "
        "2 through 7, the uniform direct terminal, and h=3 capacities 2/22"
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
