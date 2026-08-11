#!/usr/bin/env python3
"""Check primitive full-box edges and the canonical q=3 carrier threshold."""

from __future__ import annotations

import argparse
from math import gcd

from type_i_core_jacobi_punctured_kernel_primary_selector import factorint, is_prime
from type_i_odd_owner_prime_matched_affine_carrier_fourier_boundary import (
    beta,
    multiplicative_order,
    valuation,
)


def first_prime(residue: int, modulus: int, forbidden: set[int]) -> int:
    candidate = residue % modulus
    if candidate < 2:
        candidate += ((2 - candidate + modulus - 1) // modulus) * modulus
    while True:
        if candidate not in forbidden and is_prime(candidate):
            return candidate
        candidate += modulus


def cyclotomic_prime(q: int) -> int:
    cyclotomic_value = sum(q**power for power in range(q))
    for prime, _ in factorint(cyclotomic_value):
        if multiplicative_order(q, prime) == q and valuation(prime - 1, q) == 1:
            return prime
    raise AssertionError("cyclotomic prime was not found")


def q3_carrier(b_value: int, role_value: int) -> tuple[int, int, int, int, int]:
    q = 3
    modulus = q**q
    r_value = cyclotomic_prime(q)
    alpha = role_value * pow(b_value % q, -1, q) % q
    u_value = first_prime(1 + alpha * q, modulus, {r_value})
    v_value = first_prime(1, modulus, {r_value, u_value})
    lambda_value = first_prime(
        b_value * pow((r_value * u_value) % modulus, -1, modulus) % modulus,
        modulus,
        {r_value, u_value, v_value},
    )
    threshold = 4 * r_value * u_value * u_value * v_value * lambda_value
    return threshold, r_value, u_value, v_value, lambda_value


def verify_primitive_coordinate_edge() -> None:
    bounds = (1, 1, 3, 1)
    elementary_role = (1, 0, 0, 0)
    q = 3

    index = next(
        coordinate
        for coordinate, value in enumerate(elementary_role)
        if value % q != 0
    )
    edge = tuple(1 if coordinate == index else 0 for coordinate in range(len(bounds)))
    assert all(-bound <= value <= bound for value, bound in zip(edge, bounds))
    assert gcd(*edge) == 1
    assert elementary_role[index] % q == 1
    assert valuation(1, q) == 0


def verify_q3_threshold() -> None:
    q = 3
    modulus = q**q
    cases = []
    for b_value in range(1, modulus):
        if gcd(b_value, modulus) != 1 or b_value % q != 2:
            continue
        for role_value in range(1, q):
            cases.append((b_value, role_value, *q3_carrier(b_value, role_value)))

    assert len(cases) == 18
    assert all(case[3] == 13 for case in cases)
    assert {case[4] for case in cases if case[1] == 1} == {7}
    assert {case[4] for case in cases if case[1] == 2} == {31}
    assert {case[5] for case in cases} == {109}

    maximum = max(cases, key=lambda case: case[2])
    assert maximum == (11, 2, 484_778_372, 13, 31, 109, 89)

    p_value = 557_281
    b_value = beta(p_value, modulus)
    assert b_value == 20
    threshold, r_value, u_value, v_value, lambda_value = q3_carrier(b_value, 1)
    assert (r_value, u_value, v_value, lambda_value) == (13, 7, 109, 2)
    assert threshold == 555_464 < p_value

    x_value = r_value * u_value * lambda_value
    s0_value = x_value * v_value
    s1_value = s0_value * u_value
    assert (x_value, s0_value, s1_value) == (182, 19_838, 138_866)
    assert 4 * s1_value == threshold
    heights = tuple(
        valuation(p_value + 4 * value, q)
        for value in (x_value, s0_value, s1_value)
    )
    assert heights == (4, 3, 1)
    assert (s1_value - s0_value) // q % q == 1
    assert multiplicative_order(q, 4 * x_value) % q == 0


def verify() -> None:
    verify_primitive_coordinate_edge()
    verify_q3_threshold()
    print("verified primitive full-box edge and q=3 uniform carrier threshold")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
