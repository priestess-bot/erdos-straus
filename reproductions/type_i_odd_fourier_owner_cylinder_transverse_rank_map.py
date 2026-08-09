#!/usr/bin/env python3
"""Verify the odd Fourier owner-cylinder transverse rank map."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd, isqrt


def divisors(value: int) -> tuple[int, ...]:
    return tuple(
        divisor
        for divisor in range(1, value + 1)
        if value % divisor == 0
    )


def squarefree(value: int) -> bool:
    return all(value % (prime * prime) for prime in range(2, isqrt(value) + 1))


def canonical_pair(shift: int) -> tuple[int, int]:
    original = shift
    square = 1
    factor = 2
    while factor * factor <= shift:
        exponent = 0
        while shift % factor == 0:
            shift //= factor
            exponent += 1
        square *= factor ** (exponent // 2)
        factor = 3 if factor == 2 else factor + 2
    return square, original // (square * square)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def multiplicative_order(value: int, modulus: int) -> int:
    assert gcd(value, modulus) == 1
    current = 1
    for exponent in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return exponent
    raise AssertionError("order search did not terminate")


def euler_phi(value: int) -> int:
    result = value
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            result -= result // prime
            while value % prime == 0:
                value //= prime
        prime = 3 if prime == 2 else prime + 2
    if value > 1:
        result -= result // value
    return result


def beta(prime: int, owner_prime: int, layer: int) -> int:
    modulus = owner_prime**layer
    return (-prime * pow(4, -1, modulus)) % modulus


def core_phase_rows(modulus: int, owner_prime: int) -> tuple[dict[str, int], ...]:
    coordinates = {pow(4, exponent, modulus): exponent for exponent in range(33)}
    rows: list[dict[str, int]] = []
    for z5 in range(-3, 4):
        for z13 in range(-1, 2):
            image = pow(5, z5, modulus) * pow(13, z13, modulus) % modulus
            if pow(image, (modulus - 1) // 2, modulus) != modulus - 1:
                continue
            normalized = (-image) % modulus
            coordinate = coordinates[normalized]
            phase = coordinate % owner_prime
            assert phase == (2 * z5 + 4 * z13) % owner_prime
            rows.append(
                {
                    "z5": z5,
                    "z13": z13,
                    "coordinate": coordinate,
                    "phase": phase,
                }
            )
    return tuple(rows)


def source_switch_menu(
    prime: int, source_d: int, source_label: int, owner_prime: int
) -> tuple[tuple[int, int, int], ...]:
    rows: list[tuple[int, int, int]] = []
    for target_d in divisors(source_d):
        for target_a in divisors(target_d):
            if not squarefree(target_d // target_a):
                continue
            label = target_a * target_d
            if 4 * label >= prime:
                continue
            if (label - source_label) % owner_prime:
                continue
            rows.append((target_d, target_a, label))
    return tuple(rows)


def verify() -> dict[str, object]:
    prime = 97
    owner_prime = 11
    modulus = 67

    beta_1 = beta(prime, owner_prime, 1)
    beta_2 = beta(prime, owner_prime, 2)
    assert (beta_1, beta_2) == (6, 6)

    window = tuple(s for s in range(1, prime // 4 + 1) if 4 * s < prime)
    owners = tuple(s for s in window if (prime + 4 * s) % owner_prime == 0)
    assert owners == (6, 17)
    heights = tuple(valuation(prime + 4 * s, owner_prime) for s in owners)
    digits = tuple(((s - beta_1) // owner_prime) % owner_prime for s in owners)
    assert heights == (2, 1)
    assert digits == (0, 1)
    assert valuation(owners[1] - owners[0], owner_prime) == 1
    assert min(heights) == 1

    all_phase_rows = core_phase_rows(modulus, owner_prime)
    assert len(all_phase_rows) == 10
    assert sorted(row["coordinate"] for row in all_phase_rows) == [
        6,
        7,
        8,
        9,
        11,
        22,
        24,
        25,
        26,
        27,
    ]
    assert len({row["phase"] for row in all_phase_rows}) > 1

    coordinates = {pow(4, exponent, modulus): exponent for exponent in range(33)}
    phase_rows: list[dict[str, int]] = []
    for exponent in (1, -1):
        image = pow(5, exponent, modulus)
        normalized = (-image) % modulus
        coordinate = coordinates[normalized]
        phase = coordinate % owner_prime
        value = Fraction(5) ** exponent
        sigma = value.numerator + value.denominator
        phase_rows.append(
            {
                "z5": exponent,
                "coordinate": coordinate,
                "phase": phase,
                "sigma": sigma,
            }
        )
    assert phase_rows == [
        {"z5": 1, "coordinate": 24, "phase": 2, "sigma": 6},
        {"z5": -1, "coordinate": 9, "phase": 9, "sigma": 6},
    ]

    slope = 8
    offset = 6
    mapped_digits = tuple(
        (slope * row["phase"] + offset) % owner_prime for row in phase_rows
    )
    assert mapped_digits == digits
    assert (
        slope * (phase_rows[1]["phase"] - phase_rows[0]["phase"])
        - (digits[1] - digits[0])
    ) % owner_prime == 0

    for unit_slope in range(1, owner_prime):
        assert (
            unit_slope * phase_rows[0]["phase"]
            - unit_slope * phase_rows[1]["phase"]
        ) % owner_prime

    fibers: list[dict[str, object]] = []
    for shift in owners:
        a, c = canonical_pair(shift)
        assert c > 0 and squarefree(c) and a * a * c == shift
        d = a * c
        ray_modulus = 4 * d
        shifted = prime + 4 * shift
        eligible_factors = tuple(
            factor
            for factor in divisors(shifted)
            if factor > 1 and (factor + 1) % ray_modulus == 0
        )
        assert not eligible_factors
        menu = source_switch_menu(prime, d, shift, owner_prime)
        assert menu == ((d, a, shift),)
        fibers.append(
            {
                "shift": shift,
                "a": a,
                "c": c,
                "d": d,
                "modulus": ray_modulus,
                "shifted": shifted,
                "owner_height": valuation(shifted, owner_prime),
                "order_of_11": multiplicative_order(owner_prime, ray_modulus),
                "eligible_factors": eligible_factors,
                "source_switch_menu": menu,
            }
        )

    unit_group_orders = tuple(euler_phi(int(row["modulus"])) for row in fibers)
    pooled_modulus = 24 * 68 // gcd(24, 68)
    pooled_unit_group_order = euler_phi(pooled_modulus)
    assert [row["order_of_11"] for row in fibers] == [2, 16]
    assert unit_group_orders == (8, 32)
    assert pooled_modulus == 408 and pooled_unit_group_order == 128
    assert all(order % owner_prime for order in (*unit_group_orders, pooled_unit_group_order))

    independent = (
        Fraction(1, 28) + Fraction(1, 194) + Fraction(1, 2716)
    )
    assert independent == Fraction(4, prime)

    return {
        "prime": prime,
        "q": owner_prime,
        "beta": {"layer_1": beta_1, "layer_2": beta_2},
        "owners": [
            {"shift": shift, "height": height, "digit": digit}
            for shift, height, digit in zip(owners, heights, digits, strict=True)
        ],
        "inversion_pair": phase_rows,
        "all_negative_phase_rows": all_phase_rows,
        "transverse_affine_map": {"slope": slope, "offset": offset},
        "transverse_rank": 1,
        "fibers": fibers,
        "unit_group_orders": list(unit_group_orders),
        "pooled_modulus": pooled_modulus,
        "pooled_unit_group_order": pooled_unit_group_order,
        "direct_terminal_on_q11_route": False,
        "strict_source_switch_on_q11_route": False,
        "independent_type_ii_terminal": [28, 194, 2716],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    print(json.dumps(verify(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
