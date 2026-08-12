#!/usr/bin/env python3
"""Verify the colored split-carrier relay and the fixed infinite-family receipt.

This focused verifier checks only the formulas introduced by the accompanying
claim. It performs no prime-range, denominator, or historical scan.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm


P = 73
BASE_PARAMETER = 50
PERIOD = 2_464_177_192_963_200
CHECKPOINTS = (0, 1, 2)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def chart(prime: int, parameter: int) -> dict[str, int]:
    g = (prime + 1) // 2
    b = 2 * prime * parameter - 1
    n = (prime + 1) * b - 1
    support = (prime * n - 1) // 4
    residual = (prime - 1) * n - 1
    capacity = support * (prime - 1)
    adjustable = prime * prime * parameter - g
    return {
        "g": g,
        "b": b,
        "n": n,
        "support": support,
        "residual": residual,
        "capacity": capacity,
        "adjustable": adjustable,
    }


def peeled_pair(data: dict[str, int], anchor: int) -> tuple[int, int]:
    departure = data["residual"] - anchor
    if valuation(departure, P) != 1:
        raise AssertionError("root departure is not exactly p-primary")
    y = departure // P
    x = data["residual"] - y
    if gcd(x, y) != 1:
        raise AssertionError("root p-peel unexpectedly needs gcd reduction")
    return x, y


def verify_symbolic_specialization() -> None:
    p = P
    expected_period = p * (p * p - 1) * (p * p + p + 1) * (p * p + 1) * (3 * p + 1)
    if PERIOD != expected_period:
        raise AssertionError("infinite-family period changed")
    for modulus in (p, p * p - 1, p * p + p + 1, p * p + 1, 3 * p + 1):
        if PERIOD % modulus:
            raise AssertionError("period no longer freezes a required modulus")

    # Each pair is (coefficient of r, constant term).
    t = (p * p, -(p + 1) // 2)
    x = (2 * (p - 1) * (p - 1) * (p + 1), -p * p + 3)
    y = (2 * (p * p - 1), -p - 2)
    z = (2 * p * (p * p - 1), -p * p - p - 2)

    def affine_linear_combination(
        left_scale: int,
        left: tuple[int, int],
        right_scale: int,
        right: tuple[int, int],
    ) -> tuple[int, int]:
        return (
            left_scale * left[0] + right_scale * right[0],
            left_scale * left[1] + right_scale * right[1],
        )

    identities = (
        (
            affine_linear_combination(p * p, x, -2 * (p - 1) * (p * p - 1), t),
            (0, p * p + 1),
        ),
        (
            affine_linear_combination(p * p, y, -2 * (p * p - 1), t),
            (0, -(p * p + p + 1)),
        ),
        (
            affine_linear_combination(p * p, z, -2 * p * (p * p - 1), t),
            (0, -p * (3 * p + 1)),
        ),
    )
    if any(actual != expected for actual, expected in identities):
        raise AssertionError("an elimination identity changed")


def verify_colored_source_and_noncommutation() -> None:
    data = chart(P, 1)
    x, y = peeled_pair(data, anchor=1)
    if (x, y) != (761_905, 10_582):
        raise AssertionError("strict colored-source fixture changed")

    q_x, beta_x = x, 1
    q_y, beta_y = 143, 74
    if not (
        y == q_y * beta_y
        and data["capacity"] % (beta_x * beta_y) == 0
        and gcd(q_x * beta_x, q_y * beta_y) == 1
    ):
        raise AssertionError("colored complete-excess decomposition changed")

    c0 = data["capacity"] // (beta_x * beta_y)
    if 4 * c0 * beta_x * beta_y != P * q_x * beta_x + P * q_y * beta_y + 1:
        raise AssertionError("colored source identity changed")

    target_support = lcm(data["support"], q_x, q_y)
    multiplier = target_support // data["support"]
    target_cofactor = pow(4 * target_support, -1, P)
    if (multiplier, target_cofactor) != (108_952_415, 67):
        raise AssertionError("strict split canonical arithmetic changed")

    cap_x = gcd(x, data["capacity"])
    cap_y = gcd(y, data["capacity"])
    excess_x = x // cap_x
    excess_y = y // cap_y
    if not (
        (cap_x, cap_y, excess_x, excess_y) == (1, 74, 761_905, 143)
        and (excess_x - 1) % q_y == 0
        and (excess_y - 1) % q_x != 0
        and (data["residual"] - cap_x) % q_y == 0
        and (data["residual"] - cap_y) % q_x != 0
    ):
        raise AssertionError("fixed noncommuting branch receipt changed")


def verify_receipt_cell_quadratic() -> None:
    p = P
    roots = (50, 57)
    if any((2 * r * r + 5 * r + 6) % p for r in roots):
        raise AssertionError("minimal receipt-cell roots changed")
    if ((roots[0] + roots[1]) * 2 + 5) % p:
        raise AssertionError("quadratic root sum changed")
    if (2 * roots[0] * roots[1] - 6) % p:
        raise AssertionError("quadratic root product changed")
    if (5 * 5 - 4 * 2 * 6) % p != (-23) % p:
        raise AssertionError("minimal receipt-cell discriminant changed")

    data = chart(p, BASE_PARAMETER)
    x, y = peeled_pair(data, anchor=p + 1)
    cell = 2 * 3
    if not (
        x % p == (2 * BASE_PARAMETER + 3) % p
        and y % p == (-2 * (BASE_PARAMETER + 1)) % p
        and (x * y * pow(cell, -1, p)) % p == 1
    ):
        raise AssertionError("receipt-cell multiplier congruence changed")


def verify_family_member(index: int) -> None:
    p = P
    parameter = BASE_PARAMETER + index * PERIOD
    data = chart(p, parameter)
    x, y = peeled_pair(data, anchor=p + 1)
    z = data["residual"] - 3
    t = data["adjustable"]

    if not (
        p * data["residual"] + 1 == 4 * data["capacity"]
        and data["support"] == data["g"] * t
        and data["capacity"] == ((p * p - 1) // 2) * t
        and data["capacity"] % (p + 1) == 0
    ):
        raise AssertionError("a=1 chart normalization changed")

    if not (
        p * p * x - 2 * (p - 1) * (p * p - 1) * t == p * p + 1
        and p * p * y - 2 * (p * p - 1) * t == -(p * p + p + 1)
        and p * p * z - 2 * p * (p * p - 1) * t == -p * (3 * p + 1)
    ):
        raise AssertionError("family elimination receipt changed")

    if not (
        gcd(x, t) == gcd(y, t) == gcd(z, t) == 1
        and gcd(x, p * p - 1) == 2
        and gcd(y, p * p - 1) == 3
        and gcd(z, p * p - 1) == 4
        and gcd(x, data["capacity"]) == 2
        and gcd(y, data["capacity"]) == 3
        and gcd(z, data["capacity"]) == 4
    ):
        raise AssertionError("family gcd invariants changed")

    q_x, q_y, q_3 = x // 2, y // 3, z // 4
    if not (
        gcd(q_x, data["support"]) == 1
        and gcd(q_y, data["support"]) == 1
        and gcd(q_3, data["support"]) == 1
        and gcd(q_x, q_y) == 1
        and (q_x * q_y * q_3) % p != 0
        and (q_x % (p + 1), q_y % (p + 1), q_3 % (p + 1)) == (1, 49, 55)
    ):
        raise AssertionError("family support-coprimality receipt changed")

    multiplier = q_x * q_y
    c0 = data["capacity"] // 6
    if not (
        multiplier % p == 1
        and 4 * c0 * 6 == p * q_x * 2 + p * q_y * 3 + 1
        and pow(4 * data["support"] * multiplier, -1, p) == p - 1
    ):
        raise AssertionError("family split stutter changed")

    if not (
        3 + 4 * q_3 == data["residual"]
        and data["capacity"] % 12 == 0
        and gcd(q_3, 12) == 1
        and q_3 % p == (p - 1) // 2
    ):
        raise AssertionError("h=3 path-anchored receipt changed")

    endpoint_support = data["support"] * q_3
    endpoint_cofactor = pow(4 * endpoint_support, -1, p)
    endpoint_capacity = endpoint_support * endpoint_cofactor
    endpoint_residual = (4 * endpoint_capacity - 1) // p
    if not (
        endpoint_cofactor == 2
        and endpoint_cofactor < data["capacity"] // data["support"]
        and p * endpoint_residual + 1 == 4 * endpoint_capacity
    ):
        raise AssertionError("h=3 strict canonical target changed")


def verify_base_stutter_relay() -> None:
    p = P
    data = chart(p, BASE_PARAMETER)
    x, y = peeled_pair(data, anchor=p + 1)
    multiplier = (x // 2) * (y // 3)
    s = (multiplier - 1) // p
    target_n = multiplier * data["n"] - s
    target_b = data["b"] * multiplier - s
    target_support = data["support"] * multiplier
    next_excess = (p - 1) * target_b - 1

    if not (
        multiplier == 3_405_557_677_775
        and s % p == 65
        and target_support == (p * target_n - 1) // 4
        and target_n == (p + 1) * target_b - 1
        and next_excess % p == s % p
        and (-pow(next_excess, -1, p)) % p == 64
    ):
        raise AssertionError("base split-stutter relay changed")


def verify() -> None:
    verify_symbolic_specialization()
    verify_colored_source_and_noncommutation()
    verify_receipt_cell_quadratic()
    for index in CHECKPOINTS:
        verify_family_member(index)
    verify_base_stutter_relay()
    print(
        "verified 1 colored split source, 1 noncommuting branch, "
        "1 stutter relay, and 3 infinite-family checkpoints with h=3 strict exits"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify to run the fixed receipt")
    verify()


if __name__ == "__main__":
    main()
