#!/usr/bin/env python3
"""Verify the finite 10,000 coefficient barrier for actual root stutters."""

from __future__ import annotations

import argparse
from math import gcd


BOUND = 10_000
EXPECTED_CORE_CONGRUENCE_ROWS = (
    (3, 9, 1, 1),
    (4, 5, 1, 1),
    (6, 3, 1, 1),
    (13, 209, 4021, 54_481),
    (15, 225, 5, 1),
    (21, 441, 7, 1),
    (30, 15, 5, 1),
    (34, 17, 6749, 709_801),
    (42, 21, 7, 1),
    (66, 33, 11, 1),
    (78, 39, 13, 1),
    (82, 41, 93029, 23_170_945),
    (102, 51, 17, 1),
    (114, 57, 19, 1),
    (130, 65, 369005, 145_035_865),
    (138, 69, 23, 1),
    (390, 15, 125, 25),
)


def factorization(value: int) -> dict[int, int]:
    if value <= 0:
        raise ValueError("factorization expects a positive integer")
    result: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result[value] = result.get(value, 0) + 1
    return result


def divisors(factors: dict[int, int]) -> tuple[int, ...]:
    result = [1]
    for prime, exponent in factors.items():
        previous = result
        result = []
        prime_power = 1
        for _ in range(exponent + 1):
            result.extend(value * prime_power for value in previous)
            prime_power *= prime
    return tuple(sorted(result))


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


def enumerate_gate(
    bound: int,
) -> tuple[
    int,
    int,
    tuple[tuple[int, int, int, int], ...],
    tuple[tuple[int, int, int, int], ...],
]:
    pair_count = 0
    gate_count = 0
    core_congruence_rows: list[tuple[int, int, int, int]] = []
    root_rows: list[tuple[int, int, int, int]] = []

    for m_value in range(3, bound + 1):
        if m_value % 3 == 2:
            continue
        maximum_a = (bound - 1) // (m_value - 1)
        for a_value in range(1, maximum_a + 1, 2):
            if m_value % 3 == 0 and a_value % 3:
                continue
            if m_value % 3 == 1 and a_value % 3 != 2:
                continue

            pair_count += 1
            layer = a_value * m_value
            shift = m_value - a_value
            root_divisor_bound = layer * layer + layer * shift + shift * shift

            for u_value in divisors(factorization(root_divisor_bound)):
                if gcd(u_value, 6) != 1 or (a_value + 3 * u_value) % m_value:
                    continue

                numerator = 9 * u_value * u_value + 3 * (a_value - 1) * u_value + shift
                if numerator % layer:
                    continue

                gate_count += 1
                p_value = numerator // layer
                e_value = (a_value + 3 * u_value) // m_value
                h_value = 3 * u_value
                d_value = m_value * p_value + 1 - h_value
                if not (
                    p_value > 0
                    and e_value > 0
                    and d_value > 0
                    and e_value * d_value == p_value * h_value + 1
                    and a_value == e_value * m_value - h_value
                ):
                    raise AssertionError("root-divisor reconstruction changed")

                row = (m_value, a_value, u_value, p_value)
                if p_value % 24 != 1:
                    continue
                core_congruence_rows.append(row)
                if not is_prime(p_value):
                    continue
                if h_value < p_value and (p_value * p_value + p_value + 1) % h_value == 0:
                    root_rows.append(row)

    return pair_count, gate_count, tuple(core_congruence_rows), tuple(root_rows)


def verify() -> None:
    pair_count, gate_count, core_congruence_rows, root_rows = enumerate_gate(BOUND)
    if not (
        pair_count == 8549
        and gate_count == 60
        and core_congruence_rows == EXPECTED_CORE_CONGRUENCE_ROWS
        and all(not is_prime(row[3]) for row in core_congruence_rows)
        and root_rows == ()
    ):
        raise AssertionError("10,000 coefficient barrier changed")
    print("verified actual-root 10,000 coefficient barrier")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
