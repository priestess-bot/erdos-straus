#!/usr/bin/env python3
"""Verify fixed Bezout and character controls for strict root complements."""

from __future__ import annotations

import argparse

from short_certificate import (
    positive_divisors_square_product_from_spf,
    smallest_prime_factors,
)
from type_i_root_capacity_general_endpoint_divisor_gate import chart


def legendre(value: int, prime: int) -> int:
    """Return the nonzero Legendre symbol as 1 or ``prime - 1``."""
    residue = value % prime
    if residue == 0:
        raise ValueError("Legendre input must be a unit")
    return pow(residue, (prime - 1) // 2, prime)


def root_tail_data(p: int, root_parameter: int) -> dict[str, int]:
    """Build the receipt-normalized tail data for one strict root control."""
    receipt = chart(p, root_parameter)
    multiplier = receipt["E"]
    cofactor = (-pow(multiplier, -1, p)) % p
    witness = (multiplier * cofactor + 1) // p
    if (multiplier * cofactor + 1) % p:
        raise AssertionError("root cofactor did not reconstruct its multiplier witness")

    if cofactor % 2 == 0:
        source = cofactor
        bezout = multiplier - 4 * witness
        sign = -1
    else:
        source = p - cofactor
        bezout = 3 * multiplier - 4 * witness
        sign = 1
    remainder = 4 * source - p
    product = p * source
    if not (
        receipt["u"] < receipt["M"]
        and receipt["Q"] > 1
        and 1 <= cofactor <= p - 2
        and source % 2 == 0
        and remainder > 0
        and p * bezout == sign * multiplier * remainder - 4
        and (source * bezout + 1) % remainder == 0
        and (p * bezout + 4) % remainder == 0
        and (product * bezout * bezout - 4) % remainder == 0
    ):
        raise AssertionError("strict-root Bezout normalization changed")
    return {
        "p": p,
        "E": multiplier,
        "c": cofactor,
        "w": witness,
        "n": source,
        "R": remainder,
        "S": product,
        "a": bezout,
    }


def selector_factors(p: int, source: int) -> list[int]:
    """Return all sorted-tail factors satisfying the complete residue gate."""
    remainder = 4 * source - p
    product = p * source
    spf = smallest_prime_factors(p)
    return [
        factor
        for factor in positive_divisors_square_product_from_spf(p, source, spf)
        if factor <= product and (product + factor) % remainder == 0
    ]


def verify_p73_quadratic_obstruction() -> None:
    data = root_tail_data(73, 3)
    if not (
        data == {
            "p": 73,
            "E": 10_583,
            "c": 37,
            "w": 5_364,
            "n": 36,
            "R": 71,
            "S": 2_628,
            "a": 10_293,
        }
        and legendre(-data["S"], 71) == legendre(-1, 71) == 70
        and legendre(2, 71) == legendre(3, 71) == legendre(73, 71) == 1
        and not selector_factors(data["p"], data["n"])
    ):
        raise AssertionError("p=73 quadratic character obstruction changed")


def discrete_log_table(generator: int, prime: int) -> dict[int, int]:
    table: dict[int, int] = {}
    value = 1
    for exponent in range(prime - 1):
        table[value] = exponent
        value = value * generator % prime
    if value != 1 or len(table) != prime - 1:
        raise AssertionError("declared generator was not primitive")
    return table


def verify_p313_exponent_box_boundary() -> None:
    data = root_tail_data(313, 271)
    q = 293
    logs = discrete_log_table(2, q)
    target = (-data["S"]) % q
    box = {
        (pow(2, alpha, q) * pow(149, beta, q) * pow(313, gamma, q)) % q
        for alpha in range(3)
        for beta in range(3)
        for gamma in range(3)
    }
    if not (
        data == {
            "p": 313,
            "E": 2_077_472_563,
            "c": 298,
            "w": 1_977_913_175,
            "n": 298,
            "R": 879,
            "S": 93_274,
            "a": -5_834_180_137,
        }
        and legendre(-data["S"], 3) == legendre(-1, 3) == 2
        and legendre(2, 3) == legendre(149, 3) == 2
        and legendre(-data["S"], q) == legendre(-1, q) == 1
        and logs[149] == 172
        and logs[313 % q] == 175
        and target == 193
        and logs[target] == 202
        and len(box) == 27
        and target not in box
        and not selector_factors(data["p"], data["n"])
    ):
        raise AssertionError("p=313 higher-order exponent-box boundary changed")


def verify() -> None:
    verify_p73_quadratic_obstruction()
    verify_p313_exponent_box_boundary()
    print(
        "verified strict-root Bezout normalization, the p=73 quadratic no-go, "
        "and the p=313 higher-order exponent-box boundary"
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
