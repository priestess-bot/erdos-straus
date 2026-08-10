#!/usr/bin/env python3
"""Focused checks for Grassmann slice capacity and exterior boundaries."""

from __future__ import annotations

import argparse
from itertools import combinations, product
from math import prod

Vector = tuple[int, ...]
Basis = tuple[Vector, ...]
Selection = tuple[Vector, ...]


def dot(left: Vector, right: Vector, prime: int) -> int:
    return sum(a * b for a, b in zip(left, right)) % prime


def rref_basis(vectors: list[Vector], prime: int) -> Basis:
    if not vectors:
        return ()
    matrix = [[entry % prime for entry in vector] for vector in vectors]
    row = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (index for index in range(row, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        inverse = pow(matrix[row][column], -1, prime)
        matrix[row] = [(entry * inverse) % prime for entry in matrix[row]]
        for index in range(len(matrix)):
            if index == row or matrix[index][column] == 0:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                (left - factor * right) % prime
                for left, right in zip(matrix[index], matrix[row])
            ]
        row += 1
        if row == len(matrix):
            break
    return tuple(tuple(line) for line in matrix[:row])


def rank_mod(vectors: list[Vector], prime: int) -> int:
    return len(rref_basis(vectors, prime))


def gaussian_binomial(dimension: int, rank: int, prime: int) -> int:
    if rank < 0 or rank > dimension:
        return 0
    numerator = 1
    denominator = 1
    for index in range(rank):
        numerator *= prime ** (dimension - index) - 1
        denominator *= prime ** (rank - index) - 1
    return numerator // denominator


def subspaces(dimension: int, rank: int, prime: int) -> tuple[Basis, ...]:
    if rank == 0:
        return ((),)
    nonzero = [
        vector
        for vector in product(range(prime), repeat=dimension)
        if any(vector)
    ]
    spaces = {
        rref_basis(list(generators), prime)
        for generators in combinations(nonzero, rank)
        if rank_mod(list(generators), prime) == rank
    }
    assert len(spaces) == gaussian_binomial(dimension, rank, prime)
    return tuple(sorted(spaces))


def is_annihilated(
    role_space: Basis,
    vectors: Selection,
    prime: int,
) -> bool:
    return all(
        dot(role, vector, prime) == 0
        for role in role_space
        for vector in vectors
    )


def grassmann_incidence(
    feasible: tuple[Selection, ...],
    dimension: int,
    slice_rank: int,
    prime: int,
) -> dict[str, int]:
    assert feasible
    request_count = len(feasible[0])
    assert all(len(selection) == request_count for selection in feasible)
    slices = subspaces(dimension, slice_rank, prime)
    branch_sizes = [
        sum(
            is_annihilated(role_space, selection, prime)
            for selection in feasible
        )
        for role_space in slices
    ]
    incidence_total = sum(branch_sizes)
    exact_total = sum(
        gaussian_binomial(
            dimension - rank_mod(list(selection), prime),
            slice_rank,
            prime,
        )
        for selection in feasible
    )
    lower_bound = (
        gaussian_binomial(
            dimension - request_count,
            slice_rank,
            prime,
        )
        * len(feasible)
    )
    assert incidence_total == exact_total
    assert incidence_total >= lower_bound
    assert max(branch_sizes) * len(slices) >= lower_bound
    return {
        "prime": prime,
        "dimension": dimension,
        "request_count": request_count,
        "slice_rank": slice_rank,
        "slice_count": len(slices),
        "completion_count": len(feasible),
        "incidence_total": incidence_total,
        "lower_bound": lower_bound,
        "largest_branch": max(branch_sizes),
    }


def verify_grassmann_cover() -> tuple[dict[str, int], ...]:
    reports = []
    for prime in (2, 3):
        e1 = (1, 0, 0)
        e2 = (0, 1, 0)
        e3 = (0, 0, 1)
        feasible = ((e1,), (e2,), (e3,))
        report = grassmann_incidence(feasible, 3, 2, prime)
        assert report["incidence_total"] == 3
        assert report["lower_bound"] == 3
        assert report["largest_branch"] >= 1
        reports.append(report)

    e1 = (1, 0, 0, 0)
    e2 = (0, 1, 0, 0)
    e3 = (0, 0, 1, 0)
    e4 = (0, 0, 0, 1)
    coupled = (
        (e1, e2),
        (e1, e3),
        (e2, e4),
    )
    coupled_report = grassmann_incidence(coupled, 4, 2, 2)
    assert coupled_report["incidence_total"] == 3
    assert coupled_report["lower_bound"] == 3
    reports.append(coupled_report)
    return tuple(reports)


def verify_overhead_threshold() -> dict[str, object]:
    e1 = (1, 0)
    e2 = (0, 1)
    e12 = (1, 1)
    overhead = (e1,)
    menu = (e2, e12)
    assert all(rank_mod(list(overhead + (edge,)), 2) == 2 for edge in menu)

    quotient_menu = (((1,),), ((1,),))
    boundary = grassmann_incidence(quotient_menu, 1, 1, 2)
    assert boundary["incidence_total"] == 0
    assert boundary["largest_branch"] == 0
    return {
        "ambient_dimension": 2,
        "complement_budget": 1,
        "defect": 1,
        "overhead_rank": 1,
        "residual_capacity": 0,
        "quotient_branch": boundary,
    }


def matrix_vector(matrix: tuple[Vector, ...], vector: Vector, prime: int) -> Vector:
    return tuple(dot(row, vector, prime) for row in matrix)


def matrix_fourier_case(
    dimension: int,
    menus: tuple[tuple[Vector, ...], ...],
) -> dict[str, int]:
    prime = 2
    assert len(menus) < dimension
    matrices = [
        tuple(
            tuple(entries[row * dimension : (row + 1) * dimension])
            for row in range(dimension)
        )
        for entries in product(range(prime), repeat=dimension * dimension)
    ]
    spectral_sum = 0
    for matrix in matrices:
        if not any(any(row) for row in matrix):
            continue
        trace = sum(matrix[index][index] for index in range(dimension)) % prime
        kernel_hit_product = prod(
            sum(
                matrix_vector(matrix, vector, prime)
                == (0,) * dimension
                for vector in menu
            )
            for menu in menus
        )
        spectral_sum += (-1 if trace else 1) * kernel_hit_product
    zero_frequency = prod(len(menu) for menu in menus)
    assert spectral_sum == -zero_frequency
    return {
        "prime": prime,
        "dimension": dimension,
        "request_count": len(menus),
        "zero_frequency": zero_frequency,
        "nonzero_frequency_sum": spectral_sum,
    }


def verify_matrix_fourier() -> tuple[dict[str, int], ...]:
    rank_one = matrix_fourier_case(
        2,
        (((1, 0), (0, 1)),),
    )
    rank_two = matrix_fourier_case(
        3,
        (
            ((1, 0, 0), (0, 1, 0)),
            ((0, 1, 0), (0, 0, 1)),
        ),
    )
    return (rank_one, rank_two)


def determinant_pair(left: Vector, right: Vector, prime: int) -> int:
    return (left[0] * right[1] - left[1] * right[0]) % prime


def wedge_two(left: Vector, right: Vector, prime: int) -> Vector:
    return tuple(
        (left[i] * right[j] - left[j] * right[i]) % prime
        for i in range(len(left))
        for j in range(i + 1, len(left))
    )


def verify_exterior_boundary() -> dict[str, object]:
    zero = (0, 0)
    e1 = (1, 0)
    e2 = (0, 1)
    x = (e1, zero)
    y = (zero, e2)
    summed = tuple(
        tuple((a + b) % 2 for a, b in zip(left, right))
        for left, right in zip(x, y)
    )
    assert determinant_pair(*x, 2) == 0
    assert determinant_pair(*y, 2) == 0
    assert determinant_pair(*summed, 2) == 1

    e1_4 = (1, 0, 0, 0)
    e2_4 = (0, 1, 0, 0)
    e3_4 = (0, 0, 1, 0)
    e4_4 = (0, 0, 0, 1)
    reachable = tuple(
        wedge_two(e1_4, vector, 2)
        for vector in (e2_4, e3_4, e4_4)
    )
    target = wedge_two(e3_4, e4_4, 2)
    separator_coordinate = 5
    assert all(vector[separator_coordinate] == 0 for vector in reachable)
    assert target[separator_coordinate] == 1
    assert rank_mod(list(reachable), 2) == 3
    assert rank_mod(list(reachable + (target,)), 2) == 4
    return {
        "determinant_nonadditive": True,
        "reachable_plucker_rank": 3,
        "target_augmented_rank": 4,
        "separator_coordinate": separator_coordinate,
    }


def divisors(number: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, number + 1) if number % value == 0)


def is_squarefree(number: int) -> bool:
    prime = 2
    while prime * prime <= number:
        if number % (prime * prime) == 0:
            return False
        prime += 1
    return True


def type_ii_strict_products(p: int, dimension_parameter: int) -> tuple[int, ...]:
    products = []
    for lowered in divisors(dimension_parameter):
        if lowered >= dimension_parameter:
            continue
        for anchor in divisors(lowered):
            if (
                is_squarefree(lowered // anchor)
                and 4 * anchor * lowered < p
            ):
                products.append(anchor * lowered)
    return tuple(sorted(products))


def quadratic_two_character(unit: int) -> int:
    return 1 if unit % 8 in (1, 7) else -1


def mod_three_character(unit: int) -> int:
    return 1 if unit % 3 == 1 else -1


def linear_span(
    vectors: tuple[Vector, ...],
    dimension: int,
    prime: int,
) -> frozenset[Vector]:
    return frozenset(
        tuple(
            sum(coefficient * vector[index] for coefficient, vector in zip(coefficients, vectors))
            % prime
            for index in range(dimension)
        )
        for coefficients in product(range(prime), repeat=len(vectors))
    )


def verify_kernel_filter_not_relay() -> dict[str, object]:
    e1 = (1, 0, 0)
    e2 = (0, 1, 0)
    e3 = (0, 0, 1)
    source_records = (e1, (1, 1, 0))
    joint_kernel = frozenset(
        vector
        for vector in product(range(2), repeat=3)
        if vector[0] == 0
    )
    filtered_records = tuple(
        vector for vector in source_records if vector in joint_kernel
    )
    assert filtered_records == ()
    filtered_source = linear_span(filtered_records, 3, 2)
    full_source = linear_span(source_records, 3, 2)
    kernel_slice = full_source & joint_kernel
    assert filtered_source == frozenset({(0, 0, 0)})
    assert kernel_slice == frozenset({(0, 0, 0), e2})

    target = tuple((left + right) % 2 for left, right in zip(e1, e3))
    assert target not in full_source
    quotient = lambda vector: vector[0]
    assert {quotient(vector) for vector in filtered_source} == {0}
    assert {quotient(vector) for vector in full_source} == {0, 1}
    assert quotient(target) == 1
    return {
        "filtered_record_count": 0,
        "filtered_source_size": len(filtered_source),
        "full_kernel_slice_size": len(kernel_slice),
        "original_quotient_source": (0, 1),
        "target_quotient": quotient(target),
    }


def verify_integer_no_lift() -> dict[str, object]:
    p = 97
    dimension_parameter = 6
    source_anchor = 1
    source_factor = 11
    target = 23
    assert (p + 4 * dimension_parameter * source_anchor) % source_factor == 0
    character = lambda unit: (
        mod_three_character(unit) * quadratic_two_character(unit)
    )
    units = (1, 5, 7, 11, 13, 17, 19, 23)
    assert all(
        character((left * right) % 24)
        == character(left) * character(right)
        for left in units
        for right in units
    )
    character_kernel = tuple(unit for unit in units if character(unit) == 1)
    assert len(character_kernel) == 4
    assert character(source_factor) == 1
    assert character(target) == -1

    products = type_ii_strict_products(p, dimension_parameter)
    assert products == (1, 2, 3, 4, 9)
    source_residue = dimension_parameter * source_anchor % source_factor
    assert source_residue == 6
    assert all(
        product_value % source_factor != source_residue
        for product_value in products
    )
    return {
        "p": p,
        "dimension_parameter": dimension_parameter,
        "source_factor": source_factor,
        "strict_products": products,
        "required_residue": source_residue,
        "character_kernel": character_kernel,
        "character_source_phase": character(source_factor),
        "character_target_phase": character(target),
    }


def verify() -> None:
    grassmann = verify_grassmann_cover()
    threshold = verify_overhead_threshold()
    matrix_fourier = verify_matrix_fourier()
    exterior = verify_exterior_boundary()
    kernel_filter_boundary = verify_kernel_filter_not_relay()
    integer_no_lift = verify_integer_no_lift()
    print("verified: Grassmann branch cover", grassmann)
    print("verified: sharp overhead threshold", threshold)
    print("verified: matrix Fourier identity", matrix_fourier)
    print("verified: exterior and Plucker boundary", exterior)
    print("verified: kernel filter is not a relay", kernel_filter_boundary)
    print("verified: finite-group role with empty integer lift", integer_no_lift)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
