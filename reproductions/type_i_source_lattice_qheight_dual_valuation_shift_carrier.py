#!/usr/bin/env python3
"""Focused checks for q-height dual depth and valuation-shift carriers."""

from __future__ import annotations

import argparse
from itertools import product
from math import gcd, lcm

from type_i_core_jacobi_punctured_kernel_primary_selector import is_prime
from type_i_odd_owner_prime_matched_affine_carrier_fourier_boundary import (
    beta,
    is_squarefree,
    multiplicative_order,
    radical,
    valuation,
)


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    assert len(left) == len(right)
    return sum(a * b for a, b in zip(left, right))


def normalized_role_value(
    coefficient: tuple[int, ...],
    lattice_vector: tuple[int, ...],
    q: int,
    layer: int,
) -> int:
    value = dot(coefficient, lattice_vector)
    assert value % q**layer == 0
    return value // q**layer % q


def edge_height_capacity(p: int, q: int) -> int:
    bound = (p - 1) // 4
    layer = 0
    power = 1
    while power * q <= bound:
        power *= q
        layer += 1
    return layer


def owner_digit(p: int, value: int, q: int, layer: int) -> int:
    modulus = q**layer
    prefix = beta(p, modulus)
    assert (value - prefix) % modulus == 0
    return (value - prefix) // modulus % q


def verify_source_lattice_dual_depth() -> dict[str, object]:
    q = 3
    basis = ((3, 0), (0, 1))
    role = (1, 2)

    obstruction = basis[0]
    assert all(value % q == 0 for value in obstruction)
    assert role[0] != 0
    assert all(
        dot(coefficient, obstruction) % q == 0
        for coefficient in product(range(q), repeat=2)
    )

    layer_one_coefficient = (1, 6)
    lifted_values = tuple(
        normalized_role_value(layer_one_coefficient, vector, q, 1)
        for vector in basis
    )
    assert lifted_values == role

    shallow_role = (0, 2)
    layer_zero_coefficient = (0, 2)
    shallow_values = tuple(
        normalized_role_value(layer_zero_coefficient, vector, q, 0)
        for vector in basis
    )
    assert shallow_values == shallow_role

    return {
        "smith_q_valuations": (1, 0),
        "active_role_depth": 1,
        "inactive_deep_direction_depth": 0,
        "layer_one_coefficient": layer_one_coefficient,
    }


def verify_valuation_shifted_carrier() -> dict[str, object]:
    p, q, layer = 97_561, 3, 1
    source_difference = (3,)
    source_content = 3
    source_role_difference = 1
    q_free_content = 1

    assert is_prime(p) and p % 24 == 1
    assert valuation(source_content, q) == layer
    assert all(
        coefficient * source_difference[0] % q == 0
        for coefficient in range(q)
    )

    modulus = q ** (layer + 1)
    b = beta(p, modulus)
    alpha = source_role_difference * pow(b % q, -1, q) % q
    r, u = 13, 7
    assert b == 2 and alpha == 2
    assert u % modulus == 1 + alpha * q**layer

    h = lcm(q_free_content, r, u)
    a0 = h // radical(h)
    v, lam = 19, 2
    assert h == 91 and a0 == 1
    assert all(is_prime(value) for value in (r, u, v, lam))
    assert v % modulus == 1 and gcd(v, h) == 1
    assert lam % modulus == b * pow(a0 * h, -1, modulus) % modulus
    assert gcd(lam, h * v) == 1

    d_star = h * lam
    target_a = a0
    target_c = radical(h) * lam
    target = target_a * d_star
    d0 = d_star * v
    source_as = (a0, a0 * u)
    endpoints = tuple(d0 * source_a for source_a in source_as)

    assert (d_star, target_a, target_c, target) == (182, 1, 182, 182)
    assert d0 == 3_458 and source_as == (1, 7)
    assert endpoints == (3_458, 24_206)
    assert target_c == d_star // target_a and is_squarefree(target_c)
    assert all(d0 % source_a == 0 for source_a in source_as)
    assert all(is_squarefree(d0 // source_a) for source_a in source_as)
    assert d_star < d0 and q not in (r, u, v, lam)
    assert 4 * endpoints[1] == 96_824 < p

    heights = tuple(valuation(p + 4 * value, q) for value in endpoints)
    target_height = valuation(p + 4 * target, q)
    assert heights == (2, 1) and target_height == 2
    assert p + 4 * target == 98_289 == 9 * 10_921
    assert p + 4 * endpoints[0] == 111_393 == 9 * 12_377
    assert p + 4 * endpoints[1] == 194_385 == 3 * 64_795

    endpoint_difference = endpoints[1] - endpoints[0]
    assert endpoint_difference % source_content == 0
    assert valuation(endpoint_difference, q) == layer
    digit_difference = (
        owner_digit(p, endpoints[1], q, layer)
        - owner_digit(p, endpoints[0], q, layer)
    ) % q
    assert endpoint_difference // q**layer == 6_916
    assert digit_difference == source_role_difference

    affine_slope = endpoint_difference // source_content
    assert affine_slope == 6_916
    assert endpoints[0] + affine_slope * source_difference[0] == endpoints[1]
    assert affine_slope % q != 0  # The whole ambient line does not keep the prefix.
    assert normalized_role_value((affine_slope,), source_difference, q, layer) == 1

    target_modulus = 4 * d_star
    assert gcd(q, target_modulus) == 1
    assert multiplicative_order(q, target_modulus) % q == 0
    eta_q = pow(q, (r - 1) // q, r)
    assert multiplicative_order(eta_q, r) == q

    return {
        "p": p,
        "q": q,
        "dual_depth": layer,
        "target": target,
        "d_star": d_star,
        "d0": d0,
        "endpoints": endpoints,
        "heights": heights + (target_height,),
        "digit_difference": digit_difference,
        "ambient_pullback": False,
    }


def verify_fixed_layer_and_window_obstructions() -> dict[str, int]:
    q = 3
    source_difference = 3
    role_value = 1

    # At layer zero every ambient linear form kills the source generator.
    assert all(
        coefficient * source_difference % q != role_value
        for coefficient in range(q)
    )

    # Raising an already fixed layer without a relay kills that old layer's digit.
    deeper_endpoint_difference = q**2
    assert deeper_endpoint_difference // q % q == 0
    assert deeper_endpoint_difference // q**2 % q == 1

    p = 97
    required_depth = valuation(27, q)
    available_height = edge_height_capacity(p, q)
    assert required_depth == 3 and available_height == 2
    assert 4 * q**required_depth > p
    assert all(
        abs(right - left) < q**required_depth
        for left in range(1, (p - 1) // 4 + 1)
        for right in range(left + 1, (p - 1) // 4 + 1)
    )

    return {
        "fixed_layer": 1,
        "retagged_layer": 2,
        "required_depth": required_depth,
        "available_height": available_height,
    }


def verify() -> None:
    dual = verify_source_lattice_dual_depth()
    carrier = verify_valuation_shifted_carrier()
    boundary = verify_fixed_layer_and_window_obstructions()
    print("verified: source-lattice q-height dual depth", dual)
    print("verified: valuation-shifted source-line carrier", carrier)
    print("verified: fixed-layer and owner-window obstructions", boundary)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
