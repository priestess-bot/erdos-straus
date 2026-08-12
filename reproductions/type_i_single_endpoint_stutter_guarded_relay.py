#!/usr/bin/env python3
"""Verify reachable endpoint stutters and a guarded-relay arithmetic candidate.

This focused verifier checks fixed integers only. It does not scan primes,
denominators, selector history, or certificate menus.
"""

from __future__ import annotations

import argparse
from math import gcd


P = 97
RELAY_R_PARAMETER = 6_618
RELAY_RAW_LABELS = (5, 67, 3_793, 5_393, 208_217_357)
RELAY_EXPECTED_SMALL_SIDES = (
    1,
    2_415_769_286,
    36_056_258,
    9_506,
    2_239_725,
    58,
)
NO_DESCENT_R_PARAMETER = 36
NO_DESCENT_RAW_LABELS = (97, 6_911, 3, 37, 71, 11, 62_851)
NO_DESCENT_EXPECTED_SMALL_SIDES = (
    1,
    677_278,
    98,
    21_898_623,
    1_183_712,
    16_672,
    5_970_845,
    95,
)


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    common = gcd(value, capacity)
    exposed = value // common
    exponent = value.bit_length()
    residue = pow(exposed, exponent, value) if value > 1 else 0
    block = gcd(value, residue)
    return block, value // block


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


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def chart(r_parameter: int, expected: tuple[int, ...]) -> dict[str, int]:
    g = (P + 1) // 2
    b = 2 * P * r_parameter - 1
    n = (P + 1) * b - 1
    adjustable = P * P * r_parameter - g
    support = g * adjustable
    capacity = support * (P - 1)
    residual = (P - 1) * n - 1
    if not (
        (g, b, n, adjustable, support, capacity, residual) == expected
        and support == (P * n - 1) // 4
        and P * residual + 1 == 4 * capacity
    ):
        raise AssertionError("a=1,d=1 source fixture changed")
    return {
        "b": b,
        "n": n,
        "support": support,
        "capacity": capacity,
        "residual": residual,
    }


def replay_raw_path(
    residual: int,
    capacity: int,
    labels: tuple[int, ...],
    expected_small_sides: tuple[int, ...],
) -> tuple[int, int]:
    left, right = 1, residual - 1
    if gcd(left, right) != 1:
        raise AssertionError("canonical anchor is not primitive")
    if len(expected_small_sides) != len(labels) + 1:
        raise AssertionError("raw path fixture length does not match its labels")
    if expected_small_sides[0] != 1:
        raise AssertionError("raw path fixture does not start at the canonical anchor")

    for index, (label, expected) in enumerate(
        zip(labels, expected_small_sides[1:]), start=1
    ):
        if not is_prime(label):
            raise AssertionError(f"raw step {index} label is not prime")
        divisible = [side for side in (left, right) if side % label == 0]
        if (
            len(divisible) != 1
            or valuation(divisible[0], label) != valuation(capacity, label) + 1
        ):
            raise AssertionError(f"raw step {index} lost its unique excess label")
        selected = divisible[0]
        other = right if selected == left else left
        shift = label - 1
        divided = selected // label
        translated = (other + residual * shift) // label
        if not (
            selected % label == 0
            and (other + residual * shift) % label == 0
            and gcd(label, residual * other) == 1
            and gcd(divided, translated) == 1
            and divided + translated == residual
        ):
            raise AssertionError(f"raw step {index} changed")
        left, right = sorted((divided, translated))
        if left != expected:
            raise AssertionError(f"raw step {index} reached {left}, expected {expected}")

    expected_endpoint = tuple(
        sorted((expected_small_sides[-1], residual - expected_small_sides[-1]))
    )
    if (left, right) != expected_endpoint:
        raise AssertionError("raw path fixture did not reach its declared endpoint")
    return left, right


def verify() -> None:
    data = chart(
        RELAY_R_PARAMETER,
        (
            49,
            1_283_891,
            125_821_317,
            62_268_713,
            3_051_166_937,
            292_912_025_952,
            12_078_846_431,
        ),
    )
    h, z = replay_raw_path(
        data["residual"],
        data["capacity"],
        RELAY_RAW_LABELS,
        RELAY_EXPECTED_SMALL_SIDES,
    )
    q, beta = complete_excess(z, data["capacity"])
    g_a = gcd(data["support"], q)
    multiplier = q // g_a
    charged_residual = beta * g_a
    quotient = (P * h + 1) // charged_residual
    stutter_index = (charged_residual + h - 1) // P

    if not (
        (h, z) == (58, 12_078_846_373)
        and (q, beta, g_a, multiplier, charged_residual)
        == (36_491_983, 331, 1, 36_491_983, 331)
        and gcd(q, h * beta) == 1
        and data["capacity"] % (h * beta) == 0
        and data["capacity"] % z != 0
        and gcd(z, data["capacity"])
        == gcd(P * h + 1, data["capacity"])
        == charged_residual
        and (stutter_index, quotient) == (4, 17)
        and charged_residual == stutter_index * P + 1 - h
        and charged_residual * quotient == P * h + 1
        and (stutter_index * quotient * quotient - quotient + 1)
        % (P + quotient)
        == 0
        and multiplier % P == 1
    ):
        raise AssertionError("endpoint stutter receipt changed")

    relay = (multiplier - 1) // P
    target_n = multiplier * data["n"] - relay
    target_b = multiplier * data["b"] - relay
    target_support = data["support"] * multiplier
    target_residual = (P - 1) * target_n - 1
    target_capacity = target_support * (P - 1)
    next_multiplier = (P - 1) * target_b - 1
    final_cofactor = (-pow(next_multiplier, -1, P)) % P

    if not (
        relay == 376_206
        and relay % P == 40
        and target_n == 4_591_469_360_625_405
        and target_b == 46_851_728_169_647
        and target_support == 111_343_131_995_166_071
        and target_residual == 440_781_058_620_038_879
        and target_capacity == 10_688_940_671_535_942_816
        and target_support == (P * target_n - 1) // 4
        and target_n == (P + 1) * target_b - 1
        and P * target_residual + 1 == 4 * target_capacity
        and next_multiplier == 4_497_765_904_286_111
        and next_multiplier % P == relay % P == 40
        and target_b % P not in (0, P - 1)
        and final_cofactor == 80 < P - 1
    ):
        raise AssertionError("ordinary relay arithmetic candidate changed")

    no_descent = chart(
        NO_DESCENT_R_PARAMETER,
        (
            49,
            6_983,
            684_333,
            338_675,
            16_595_075,
            1_593_127_200,
            65_695_967,
        ),
    )
    h2, z2 = replay_raw_path(
        no_descent["residual"],
        no_descent["capacity"],
        NO_DESCENT_RAW_LABELS,
        NO_DESCENT_EXPECTED_SMALL_SIDES,
    )
    q2, beta2 = complete_excess(z2, no_descent["capacity"])
    g_a2 = gcd(no_descent["support"], q2)
    multiplier2 = q2 // g_a2
    charged_residual2 = beta2 * g_a2
    stutter_index2 = (charged_residual2 + h2 - 1) // P
    quotient2 = (P * h2 + 1) // charged_residual2

    if not (
        (h2, z2) == (95, 65_695_872)
        and (q2, beta2, g_a2, multiplier2, charged_residual2)
        == (21_898_624, 3, 1, 21_898_624, 3)
        and gcd(z2, no_descent["capacity"]) == 96 != charged_residual2
        and gcd(q2, h2 * beta2) == 1
        and no_descent["capacity"] % (h2 * beta2) == 0
        and no_descent["capacity"] % z2 != 0
        and multiplier2 % P == 1
        and (stutter_index2, quotient2) == (1, 3_072)
        and charged_residual2 == stutter_index2 * P + 1 - h2
        and charged_residual2 * quotient2 == P * h2 + 1
        and (stutter_index2 * quotient2 * quotient2 - quotient2 + 1)
        % (P + quotient2)
        == 0
    ):
        raise AssertionError("m=1 endpoint stutter obstruction changed")

    print(
        "verified two reachable endpoint stutters, the m=1 no-descent "
        "obstruction, and the strict arithmetic capacity candidate 96 -> 80 "
        "conditional on all E1-E5 guards"
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
