#!/usr/bin/env python3
"""Verify the odd-primary component-torsion rank-collapse control."""

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


def torsion_record(
    prime: int,
    modulus: int,
    K: int,
    vector: tuple[int, ...],
    ell: int,
) -> tuple[tuple[int, ...], int]:
    core = analyze_core(prime, modulus, K)
    assert not core["target_hits"] and not core["collisions"]
    record = next(row for row in core["negative_records"] if row[0] == vector)
    _, phase, normalized = record
    order = multiplicative_order(normalized, modulus)
    assert order % ell == 0
    ell_power = ell
    while order % (ell_power * ell) == 0:
        ell_power *= ell
    k = order // ell_power
    a = 0
    while ell_power > ell**a:
        a += 1
    delta = 1 if k % 2 == 0 else 2
    torsion_vector = tuple(delta * ell ** (a - 1) * k * entry for entry in vector)
    omega = vector_image(modulus, core["factors"], torsion_vector)
    assert multiplicative_order(omega, modulus) == ell
    return torsion_vector, omega


def local_coordinate(component: int, ell: int, value: int) -> int:
    roots = [candidate for candidate in range(1, component) if pow(candidate, ell, component) == 1]
    generator = min(candidate for candidate in roots if candidate != 1)
    current = 1
    for exponent in range(ell):
        if current == value % component:
            return exponent
        current = current * generator % component
    raise AssertionError("value is not in the local ell-torsion group")


def rank_mod(matrix: list[list[int]], ell: int) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((index for index in range(rank, len(rows)) if rows[index][column] % ell), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, ell)
        rows[rank] = [(entry * inverse) % ell for entry in rows[rank]]
        for index, row in enumerate(rows):
            if index == rank:
                continue
            scale = row[column] % ell
            rows[index] = [(entry - scale * base) % ell for entry, base in zip(row, rows[rank], strict=True)]
        rank += 1
        if rank == len(rows):
            break
    return rank


def verify() -> None:
    p, R, K, ell = 73, 63, 1150, 3
    left_vector, left_phase = torsion_record(p, R, K, (0, 1, 0), ell)
    right_vector, right_phase = torsion_record(p, R, K, (1, 1, -1), ell)
    assert (left_vector, left_phase) == ((0, 2, 0), 25)
    assert (right_vector, right_phase) == ((2, 2, -2), 4)
    assert component_kernel(R, left_phase)[0] == 1
    assert component_kernel(R, right_phase)[0] == 1

    components = (9, 7)
    coordinates = [
        [local_coordinate(component, ell, phase) for component in components]
        for phase in (left_phase, right_phase)
    ]
    assert coordinates == [[2, 2], [1, 2]]
    assert rank_mod(coordinates, ell) == 2

    combination_vector = tuple(left - right for left, right in zip(left_vector, right_vector, strict=True))
    combination_phase = vector_image(R, factorint(K), combination_vector)
    assert combination_vector == (-2, 0, 2)
    assert combination_phase == 22
    assert multiplicative_order(combination_phase, R) == ell
    assert vector_image(R, factorint(K), tuple(ell * entry for entry in combination_vector)) == 1
    assert combination_phase % 7 == 1 and combination_phase % 9 != 1
    assert component_kernel(R, combination_phase) == (7, 9)

    target_R = 7
    target_K = (p * target_R + 1) // 4
    c = R // target_R
    debt = (c - 1) // 4
    assert target_K == 128 and c == 9
    assert K == c * target_K - debt
    assert gcd(K, target_K) == gcd(target_K, debt)
    print("verified odd-primary component-torsion rank-collapse control")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused control")
    args = parser.parse_args()
    if args.verify:
        verify()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
