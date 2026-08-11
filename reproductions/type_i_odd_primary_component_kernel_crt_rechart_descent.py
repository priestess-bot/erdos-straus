#!/usr/bin/env python3
"""Verify odd-primary component-kernel CRT rechart controls."""

from __future__ import annotations

import argparse
from math import gcd

from type_i_core_jacobi_punctured_kernel_primary_selector import (
    analyze_core,
    factorint,
    multiplicative_order,
    vector_image,
)


def component_kernel(modulus: int, omega: int) -> tuple[int, int]:
    kernel = 1
    for prime, exponent in factorint(modulus):
        component = prime**exponent
        if omega % component == 1:
            kernel *= component
    complement = modulus // kernel
    assert kernel * complement == modulus
    assert gcd(kernel, complement) == 1
    return kernel, complement


def odd_primary_data(
    prime: int,
    modulus: int,
    K: int,
    vector: tuple[int, ...],
    ell: int,
) -> dict[str, int]:
    assert prime % 24 == 1 and modulus % 4 == 3
    assert 4 * K == prime * modulus + 1
    factors = factorint(K)
    assert len(factors) == len(vector)

    core = analyze_core(prime, modulus, K)
    assert not core["target_hits"] and not core["collisions"]
    record = next(row for row in core["negative_records"] if row[0] == vector)
    _, phase, normalized = record
    assert normalized == (-phase) % modulus

    source_order = multiplicative_order(normalized, modulus)
    assert source_order % ell == 0
    ell_power = 1
    while source_order % (ell_power * ell) == 0:
        ell_power *= ell
    k = source_order // ell_power
    delta = 1 if k % 2 == 0 else 2
    a = 0
    value = ell_power
    while value > 1:
        assert value % ell == 0
        value //= ell
        a += 1

    omega_vector = tuple(delta * ell ** (a - 1) * k * entry for entry in vector)
    relation_vector = tuple(delta * ell**a * k * entry for entry in vector)
    omega = vector_image(modulus, factors, omega_vector)
    assert multiplicative_order(omega, modulus) == ell
    assert vector_image(modulus, factors, relation_vector) == 1

    kernel, complement = component_kernel(modulus, omega)
    result = {
        "phase": phase,
        "normalized": normalized,
        "source_order": source_order,
        "ell": ell,
        "a": a,
        "k": k,
        "delta": delta,
        "omega": omega,
        "kernel": kernel,
        "complement": complement,
    }
    if kernel > 1:
        candidates = [part for part in (kernel, complement) if part % 4 == 3]
        assert len(candidates) == 1
        target_modulus = candidates[0]
        c = modulus // target_modulus
        target_K = (prime * target_modulus + 1) // 4
        debt = (c - 1) // 4
        assert c % 4 == 1 and 1 < target_modulus < modulus
        assert K == c * target_K - debt
        assert gcd(K, target_K) == gcd(target_K, debt)
        result.update(
            {
                "target_modulus": target_modulus,
                "target_K": target_K,
                "complementary_factor": c,
                "support_debt": debt,
            }
        )
    return result


def verify() -> None:
    p73_r95 = odd_primary_data(73, 95, 1734, (0, -1, 1), 3)
    assert p73_r95 == {
        "phase": 69,
        "normalized": 26,
        "source_order": 3,
        "ell": 3,
        "a": 1,
        "k": 1,
        "delta": 2,
        "omega": 11,
        "kernel": 5,
        "complement": 19,
        "target_modulus": 19,
        "target_K": 347,
        "complementary_factor": 5,
        "support_debt": 1,
    }

    p73_r63 = odd_primary_data(73, 63, 1150, (-1, 1, 1), 3)
    assert p73_r63 == {
        "phase": 26,
        "normalized": 37,
        "source_order": 3,
        "ell": 3,
        "a": 1,
        "k": 1,
        "delta": 2,
        "omega": 46,
        "kernel": 9,
        "complement": 7,
        "target_modulus": 7,
        "target_K": 128,
        "complementary_factor": 9,
        "support_debt": 2,
    }

    p97_full_support = odd_primary_data(97, 67, 1625, (-3, 0), 11)
    assert p97_full_support == {
        "phase": 52,
        "normalized": 15,
        "source_order": 11,
        "ell": 11,
        "a": 1,
        "k": 1,
        "delta": 2,
        "omega": 24,
        "kernel": 1,
        "complement": 67,
    }

    print("verified odd-primary component-kernel CRT rechart controls")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if args.verify:
        verify()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
