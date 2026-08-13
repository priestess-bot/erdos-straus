#!/usr/bin/env python3
"""Verify the a=1 regeneration terminal digit and root-capacity boundary.

This focused verifier checks fixed symbolic identities with integer arithmetic.
It performs no prime, denominator, selector-history, or historical-result scan.
"""

from __future__ import annotations

import argparse
from math import gcd


P = 73


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def regenerate(b: int) -> tuple[int, int, int]:
    multiplier = (P - 1) * b - 1
    quotient = (multiplier - 1) // P
    return b * multiplier - quotient, multiplier, quotient


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    common = gcd(value, capacity)
    exposed = value // common
    block = gcd(value, pow(exposed, value.bit_length(), value))
    return block, value // block


def terminal_digit(b: int) -> tuple[int, int, int]:
    multiplier = (P - 1) * b - 1
    rho = valuation(multiplier - 1, P)
    omega = ((multiplier - 1) // P**rho) % P
    for _ in range(rho):
        b, _, _ = regenerate(b)
    return b, ((P - 1) * b - 1) % P, omega


def verify_digit_invariant() -> None:
    controls = (
        (10_583, P - 1, 1),
        (772_557, P - 1, 2),
        (5_327, P - 2, 1),
        (388_869, P - 2, 2),
        (10_437, 1, 1),
        (367_553, 2, 2),
    )
    for b, expected_omega, expected_rho in controls:
        initial_multiplier = (P - 1) * b - 1
        final_b, final_multiplier, omega = terminal_digit(b)
        if not (
            valuation(initial_multiplier - 1, P) == expected_rho
            and omega == expected_omega
            and final_multiplier == (1 + omega) % P
            and final_b % P == (-final_multiplier - 1) % P
            and (omega == P - 1) == (final_b % P == P - 1)
            and (omega == P - 2) == (final_b % P == 0)
        ):
            raise AssertionError("regeneration terminal digit changed")


def verify_saturated_root_capacity() -> None:
    m = (P - 1) // 3
    b0 = 2 * P * P * m - P - 2
    b_star, multiplier0, quotient = regenerate(b0)
    r = (b_star + 1) // (2 * P)
    final_multiplier = (P - 1) * b_star - 1
    exponent = valuation(final_multiplier, P)
    unit = final_multiplier // P**exponent

    g = (P + 1) // 2
    n = (P + 1) * b_star - 1
    support = g * (P * P * r - g)
    capacity = support * (P - 1)
    residual = (P - 1) * n - 1
    root_bound = P * P + P + 1
    root_capacity = gcd(residual - (P + 1), capacity)

    if not (
        b0 == 2 * P * P * m - P - 2
        and multiplier0
        == 2 * m * P**3 - 2 * m * P**2 - P**2 - P + 1
        and quotient == 2 * m * P**2 - 2 * m * P - P - 1
        and quotient % P == P - 1
        and b_star == 2 * P * r - 1
        and exponent == 1
        and unit % P == (-2 * m - 3) % P
        and root_capacity
        == 3 * gcd(2 * r + 1, root_bound // 3)
        == root_bound
        == 5_403
    ):
        raise AssertionError("rho=1 p-free return root-capacity boundary changed")


def verify_static_endpoint_boundary() -> None:
    r0 = 21_164_451
    h = 451_141_437_368
    g = (P + 1) // 2
    b = 2 * P * r0 - 1
    n = (P + 1) * b - 1
    support = g * (P * P * r0 - g)
    capacity = support * (P - 1)
    residual = (P - 1) * n - 1
    z = residual - h
    block = 5_337_477_005_573
    beta = 3
    actual_block, actual_beta = complete_excess(z, capacity)
    endpoint_multiplier = block
    relay = (endpoint_multiplier - 1) // P
    checkpoint_b = endpoint_multiplier * b - relay
    final_b, checkpoint_multiplier, _ = regenerate(checkpoint_b)
    final_n = (P + 1) * final_b - 1
    final_support = (P * final_n - 1) // 4
    final_capacity = final_support * (P - 1)
    final_residual = (P - 1) * final_n - 1

    if not (
        gcd(h, z) == 1
        and z == block * beta
        and (actual_block, actual_beta) == (block, beta)
        and gcd(support, block) == 1
        and capacity % (h * beta) == 0
        and capacity // (h * beta) == 222
        and endpoint_multiplier % (P * P) == P + 1
        and relay % P == 1
        and valuation(checkpoint_multiplier - 1, P) == 1
        and ((checkpoint_multiplier - 1) // P) % P == P - 1
        and valuation((P - 1) * final_b - 1, P) == 1
        and gcd(final_residual - (P + 1), final_capacity) == P * P + P + 1
    ):
        raise AssertionError("static endpoint compatibility boundary changed")


def verify() -> None:
    verify_digit_invariant()
    verify_saturated_root_capacity()
    verify_static_endpoint_boundary()
    print(
        "verified the regeneration terminal-digit invariant, a saturated "
        "p^2+p+1 root capacity, and a static endpoint-compatible saturation "
        "that remains outside the path-anchored claim"
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
