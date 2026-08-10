#!/usr/bin/env python3
"""Focused checks for the q-height tail and staircase kernel relay."""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm

from type_i_core_jacobi_punctured_kernel_primary_selector import is_prime
from type_i_odd_owner_prime_matched_affine_carrier_fourier_boundary import (
    is_squarefree,
    radical,
    valuation,
)


def beta(p: int, modulus: int) -> int:
    return (-p * pow(4, -1, modulus)) % modulus


def assert_canonical_row(base: int, coefficient: int) -> None:
    assert base % coefficient == 0
    assert is_squarefree(base // coefficient)


def units(modulus: int) -> tuple[int, ...]:
    return tuple(value for value in range(modulus) if gcd(value, modulus) == 1)


def eta(value: int, cyclotomic_prime: int, q: int) -> int:
    return pow(value % cyclotomic_prime, (cyclotomic_prime - 1) // q, cyclotomic_prime)


def verify_single_edge_candidate() -> dict[str, object]:
    p, range_fail_p = 557_281, 555_337
    q, layer, depth = 3, 1, 2
    source_content, role_value = 3, 1
    modulus = q ** (layer + depth)

    assert all(is_prime(value) and value % 24 == 1 for value in (p, range_fail_p))
    assert p % modulus == range_fail_p % modulus
    b = beta(p, modulus)
    alpha = role_value * pow(b % q, -1, q) % q
    r, u, v, lam = 13, 7, 109, 2
    assert b == 20 and alpha == 2
    assert all(is_prime(value) for value in (r, u, v, lam))
    assert u % modulus == 1 + alpha * q**layer

    h = lcm(1, r, u)
    a0 = h // radical(h)
    assert h == 91 and a0 == 1
    assert v % modulus == 1 and gcd(v, h) == 1
    assert lam % modulus == b * pow(a0 * h, -1, modulus) % modulus
    assert gcd(lam, h * v) == 1

    d_star = h * lam
    target = a0 * d_star
    d0 = d_star * v
    source_as = (a0, a0 * u)
    endpoints = tuple(d0 * source_a for source_a in source_as)
    assert (d_star, target, d0, endpoints) == (
        182,
        182,
        19_838,
        (19_838, 138_866),
    )
    assert_canonical_row(d_star, a0)
    for source_a in source_as:
        assert_canonical_row(d0, source_a)
    assert d_star < d0

    assert 4 * endpoints[1] == 555_464 < p
    assert 4 * endpoints[1] > range_fail_p
    heights = (
        valuation(p + 4 * target, q),
        valuation(p + 4 * endpoints[0], q),
        valuation(p + 4 * endpoints[1], q),
    )
    assert heights == (4, 3, 1)

    difference = endpoints[1] - endpoints[0]
    assert difference % source_content == 0
    assert valuation(difference, q) == layer
    assert difference // q**layer % q == role_value
    affine_slope = difference // source_content
    assert affine_slope == 39_676
    assert endpoints[0] + affine_slope * source_content == endpoints[1]

    target_modulus = 4 * d_star
    target_units = units(target_modulus)
    kernel = tuple(value for value in target_units if eta(value, r, q) == 1)
    prefix = {pow(q, exponent, target_modulus) for exponent in range(depth + 1)}
    assert prefix == {1, 3, 9}
    assert {eta(value, r, q) for value in prefix} == {1, 3, 9}
    assert eta(target_modulus - 1, r, q) == 1
    assert len(kernel) == 96

    missing_target = target_modulus - 1
    kernel_slice = tuple(
        value
        for value in kernel
        if missing_target * value % target_modulus in prefix
    )
    assert kernel_slice == (missing_target,)
    fourier_energy = len(kernel_slice) * (len(kernel) - len(kernel_slice))
    assert fourier_energy == 95

    return {
        "p": p,
        "target": target,
        "source_rows": endpoints,
        "q_heights": heights,
        "prefix": sorted(prefix),
        "kernel_size": len(kernel),
        "kernel_slice": kernel_slice,
        "fourier_energy": fourier_energy,
        "range_fail_p": range_fail_p,
        "typed_realization": "conditional",
    }


def verify_layered_staircase() -> dict[str, object]:
    p, q, layer = 673_184_521, 3, 1
    height = q - 1
    modulus = q ** (layer + height)
    r0, v, lam = 13, 109, 47
    primes_u = (7, 19)

    assert is_prime(p) and p % 24 == 1
    assert all(is_prime(value) for value in (r0, *primes_u, v, lam))
    b = beta(p, modulus)
    inverse_digit = pow(b % q, -1, q)
    assert b == 20 and inverse_digit == 2
    for index, prime_u in enumerate(primes_u, start=1):
        stopping_layer = layer + index - 1
        assert prime_u % modulus == 1 + inverse_digit * q**stopping_layer

    h = lcm(r0, *primes_u)
    a0 = h // radical(h)
    assert h == 1_729 and a0 == 1
    assert v % modulus == 1 and gcd(v, h) == 1
    assert lam % modulus == b * pow(a0 * h, -1, modulus) % modulus
    assert gcd(lam, h * v) == 1

    d_star = h * lam
    target = a0 * d_star
    d0 = d_star * v
    source_as = (a0, *(a0 * prime_u for prime_u in primes_u))
    source_rows = tuple(d0 * source_a for source_a in source_as)
    assert (target, d_star, d0) == (81_263, 81_263, 8_857_667)
    assert source_rows == (8_857_667, 62_003_669, 168_295_673)
    assert_canonical_row(d_star, a0)
    for source_a in source_as:
        assert_canonical_row(d0, source_a)
    assert 4 * max(source_rows) == 673_182_692 < p

    q_heights = (
        valuation(p + 4 * target, q),
        *(valuation(p + 4 * source_row, q) for source_row in source_rows),
    )
    assert q_heights == (4, 3, 1, 2)

    source_keys = []
    target_keys = []
    affine_slopes = []
    for index, shallow in enumerate(source_rows[1:], start=1):
        stopping_layer = layer + index - 1
        difference = shallow - source_rows[0]
        source_content = q**stopping_layer
        assert valuation(difference, q) == stopping_layer
        assert difference // q**stopping_layer % q == 1
        assert difference % source_content == 0
        affine_slope = difference // source_content
        assert source_rows[0] + affine_slope * source_content == shallow
        affine_slopes.append(affine_slope)
        charged_layer = stopping_layer + 1
        source_keys.append(("S", source_rows[0], q, charged_layer))
        target_keys.append(("T", target, q, charged_layer))

    occurrence_keys = tuple(source_keys + target_keys)
    assert len(set(occurrence_keys)) == 2 * height
    assert {key[-1] for key in source_keys} == {2, 3}
    assert {key[-1] for key in target_keys} == {2, 3}
    assert tuple(affine_slopes) == (17_715_334, 17_715_334)
    free_lattice_vertices = ((0, 0), (3, 0), (0, 9))
    affine_images = tuple(
        source_rows[0] + affine_slopes[0] * (left + right)
        for left, right in free_lattice_vertices
    )
    assert affine_images == source_rows

    q_prefix = {q**exponent for exponent in range(height + 1)}
    assert q_prefix == {1, 3, 9}
    assert {eta(value, r0, q) for value in q_prefix} == {1, 3, 9}
    assert all(
        len({eta(q**exponent, r0, q) for exponent in range(count + 1)}) < q
        for count in range(height)
    )

    return {
        "p": p,
        "target": target,
        "common_source_base": d0,
        "source_rows": source_rows,
        "q_heights": q_heights,
        "charged_layers": tuple(key[-1] for key in source_keys),
        "matched_layer_tokens": height,
        "q_prefix_lineages": 1,
        "elementary_role_rank": 1,
        "q_prefix": sorted(q_prefix),
        "typed_realization": "conditional",
    }


def verify_capacity_and_window_obstructions() -> dict[str, object]:
    p, q, layer = 97, 3, 1
    assert is_prime(p)
    first_owners = tuple(beta(p, q**layer) + index * q**layer for index in range(q))
    assert first_owners == (2, 5, 8)
    heights = tuple(valuation(p + 4 * owner, q) for owner in first_owners)
    assert heights == (1, 2, 1)
    deep_owner = first_owners[heights.index(layer + 1)]
    shallow_owners = tuple(
        owner for owner, owner_height in zip(first_owners, heights) if owner_height == layer
    )
    star_source_keys = tuple(("S", deep_owner, q, layer + 1) for _ in shallow_owners)
    assert len(star_source_keys) == q - 1
    assert len(set(star_source_keys)) == 1
    assert len(set(star_source_keys)) < len(star_source_keys)

    window_p, window_layer = 73, 3
    required_height = window_layer + q - 1
    assert is_prime(window_p)
    assert q**required_height == 243 >= 2 * window_p
    strict_owners = range(1, (window_p - 1) // 4 + 1)
    assert all(valuation(window_p + 4 * owner, q) < required_height for owner in strict_owners)

    return {
        "fixed_layer_star": first_owners,
        "deep_owner": deep_owner,
        "edge_requests": len(star_source_keys),
        "source_slot_capacity": len(set(star_source_keys)),
        "window_no_go": (window_p, q, window_layer, required_height),
    }


def verify() -> None:
    receipt = {
        "status": "PASS",
        "single_edge_candidate": verify_single_edge_candidate(),
        "layered_staircase": verify_layered_staircase(),
        "strict_obstructions": verify_capacity_and_window_obstructions(),
    }
    print(json.dumps(receipt, ensure_ascii=True, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
