#!/usr/bin/env python3
"""Focused checks for filtered source-dual tail capacity."""

from __future__ import annotations

import argparse
from itertools import product


Vector = tuple[int, ...]
Basis = tuple[Vector, ...]


def dot_mod(left: Vector, right: Vector, q: int) -> int:
    return sum(a * b for a, b in zip(left, right)) % q


def vector_space_dimension(size: int, q: int) -> int:
    dimension = 0
    power = 1
    while power < size:
        power *= q
        dimension += 1
    assert power == size
    return dimension


def rank_mod(rows: Basis, q: int) -> int:
    if not rows:
        return 0
    matrix = [[value % q for value in row] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, q)
        matrix[pivot_row] = [value * inverse % q for value in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or matrix[row][column] == 0:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                (value - scale * pivot_value) % q
                for value, pivot_value in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def obstruction_indices(q_valuations: tuple[int, ...], layer: int) -> tuple[int, ...]:
    return tuple(
        index for index, valuation in enumerate(q_valuations)
        if valuation >= layer + 1
    )


def obstruction_rank(
    basis: Basis,
    q_valuations: tuple[int, ...],
    q: int,
    layer: int,
) -> int:
    indices = obstruction_indices(q_valuations, layer)
    restricted = tuple(tuple(row[index] for index in indices) for row in basis)
    return rank_mod(restricted, q)


def role_depth(role: Vector, q_valuations: tuple[int, ...]) -> int:
    active = [
        valuation for coefficient, valuation in zip(role, q_valuations)
        if coefficient
    ]
    return max(active, default=0)


def tail_capacities(capacities: tuple[int, ...]) -> tuple[int, ...]:
    tails = [0] * (len(capacities) + 2)
    for layer in range(len(capacities), 0, -1):
        tails[layer] = tails[layer + 1] + capacities[layer - 1]
    return tuple(tails)


def subspace_tail_deficits(
    basis: Basis,
    q_valuations: tuple[int, ...],
    q: int,
    capacities: tuple[int, ...],
) -> tuple[int, ...]:
    dimension = rank_mod(basis, q)
    height = len(capacities)
    tails = tail_capacities(capacities)
    deficits = [dimension - tails[1]]
    for threshold in range(2, height + 1):
        deficits.append(
            obstruction_rank(basis, q_valuations, q, threshold - 1)
            - tails[threshold]
        )
    deficits.append(obstruction_rank(basis, q_valuations, q, height))
    return tuple(deficits)


def named_tail_deficits(
    roles: Basis,
    q_valuations: tuple[int, ...],
    capacities: tuple[int, ...],
) -> tuple[int, ...]:
    height = len(capacities)
    releases = tuple(
        max(1, depth) if (depth := role_depth(role, q_valuations)) <= height
        else height + 1
        for role in roles
    )
    tails = tail_capacities(capacities)
    return tuple(
        sum(release >= threshold for release in releases) - tails[threshold]
        for threshold in range(1, height + 2)
    )


def has_named_assignment(releases: tuple[int, ...], capacities: tuple[int, ...]) -> bool:
    height = len(capacities)
    remaining = list(capacities)

    def assign(index: int) -> bool:
        if index == len(releases):
            return True
        release = releases[index]
        for layer in range(release, height + 1):
            if remaining[layer - 1] == 0:
                continue
            remaining[layer - 1] -= 1
            if assign(index + 1):
                return True
            remaining[layer - 1] += 1
        return False

    return assign(0)


def vectors_in_span(basis: Basis, q: int) -> tuple[Vector, ...]:
    if not basis:
        return ((0, 0),)
    return tuple(
        tuple(
            sum(coefficient * row[column] for coefficient, row in zip(coefficients, basis)) % q
            for column in range(len(basis[0]))
        )
        for coefficients in product(range(q), repeat=len(basis))
    )


def independent_basis(vectors: tuple[Vector, ...], q: int) -> Basis:
    basis: list[Vector] = []
    for vector in vectors:
        if rank_mod(tuple(basis) + (vector,), q) > len(basis):
            basis.append(vector)
    return tuple(basis)


def enumerate_obstacle_space(
    smith_diagonal: tuple[int, ...], q: int, layer: int
) -> tuple[Vector, ...]:
    modulus = q ** (layer + 1)
    residues = {
        tuple(coefficient % q for coefficient in coefficients)
        for coefficients in product(range(modulus), repeat=len(smith_diagonal))
        if all(
            diagonal * coefficient % modulus == 0
            for diagonal, coefficient in zip(smith_diagonal, coefficients)
        )
    }
    return tuple(sorted(residues))


def enumerate_rho_image(
    smith_diagonal: tuple[int, ...], q: int, layer: int
) -> tuple[Vector, ...]:
    coefficient_modulus = q ** (layer + 1)
    divisibility = q**layer
    image = {
        tuple(
            diagonal * coefficient // divisibility % q
            for diagonal, coefficient in zip(smith_diagonal, coefficients)
        )
        for coefficients in product(
            range(coefficient_modulus), repeat=len(smith_diagonal)
        )
        if all(
            diagonal * coefficient % divisibility == 0
            for diagonal, coefficient in zip(smith_diagonal, coefficients)
        )
    }
    return tuple(sorted(image))


def restriction_rank_by_enumeration(
    role_basis: Basis, obstacle_basis: Basis, q: int
) -> int:
    restriction_image = {
        tuple(dot_mod(role, obstacle, q) for obstacle in obstacle_basis)
        for role in vectors_in_span(role_basis, q)
    }
    return vector_space_dimension(len(restriction_image), q)


def has_basis_flexible_assignment(
    subspace_basis: Basis,
    q_valuations: tuple[int, ...],
    q: int,
    capacities: tuple[int, ...],
) -> bool:
    dimension = rank_mod(subspace_basis, q)
    if dimension == 0:
        return True
    nonzero = tuple(vector for vector in vectors_in_span(subspace_basis, q) if any(vector))
    for candidate in product(nonzero, repeat=dimension):
        if rank_mod(candidate, q) != dimension:
            continue
        releases = tuple(max(1, role_depth(role, q_valuations)) for role in candidate)
        if max(releases) <= len(capacities) and has_named_assignment(releases, capacities):
            return True
    return False


def verify_exact_sequence_and_rank_formula() -> dict[str, object]:
    q = 3
    smith_diagonal = (3, 9)
    valuations = (1, 2)
    full_space = ((1, 0), (0, 1))
    mixed_line = ((1, 1),)

    obstruction_dimensions: list[int] = []
    dual_dimensions: list[int] = []
    enumerated_mixed_ranks: list[int] = []
    all_roles = tuple(product(range(q), repeat=len(smith_diagonal)))
    for layer in range(3):
        obstacles = enumerate_obstacle_space(smith_diagonal, q, layer)
        obstacle_basis = independent_basis(obstacles, q)
        rho_image = set(enumerate_rho_image(smith_diagonal, q, layer))
        restriction_kernel = {
            role for role in all_roles
            if all(dot_mod(role, obstacle, q) == 0 for obstacle in obstacles)
        }
        restriction_image = {
            tuple(dot_mod(role, obstacle, q) for obstacle in obstacle_basis)
            for role in all_roles
        }
        full_dual = set(product(range(q), repeat=len(obstacle_basis)))

        assert rho_image == restriction_kernel
        assert restriction_image == full_dual
        assert len(rho_image) * len(restriction_image) == q ** len(smith_diagonal)

        obstruction_dimension = vector_space_dimension(len(obstacles), q)
        dual_dimension = vector_space_dimension(len(rho_image), q)
        assert obstruction_dimension == len(obstruction_indices(valuations, layer))
        obstruction_dimensions.append(obstruction_dimension)
        dual_dimensions.append(dual_dimension)
        enumerated_mixed_ranks.append(
            restriction_rank_by_enumeration(mixed_line, obstacle_basis, q)
        )

    obstruction_dimensions_tuple = tuple(obstruction_dimensions)
    dual_dimensions_tuple = tuple(dual_dimensions)
    assert obstruction_dimensions_tuple == (2, 1, 0)
    assert dual_dimensions_tuple == (0, 1, 2)
    assert all(
        obstruction + dual == 2
        for obstruction, dual in zip(
            obstruction_dimensions_tuple, dual_dimensions_tuple
        )
    )

    full_obstruction_ranks = tuple(
        obstruction_rank(full_space, valuations, q, layer) for layer in range(3)
    )
    mixed_obstruction_ranks = tuple(
        obstruction_rank(mixed_line, valuations, q, layer) for layer in range(3)
    )
    assert full_obstruction_ranks == (2, 1, 0)
    assert mixed_obstruction_ranks == (1, 1, 0)
    assert full_obstruction_ranks == obstruction_dimensions_tuple
    assert tuple(enumerated_mixed_ranks) == mixed_obstruction_ranks
    assert tuple(2 - value for value in full_obstruction_ranks) == dual_dimensions_tuple
    assert tuple(1 - value for value in mixed_obstruction_ranks) == (0, 0, 1)
    assert mixed_obstruction_ranks[1] == 1 and mixed_obstruction_ranks[2] == 0

    return {
        "obstruction_dimensions": obstruction_dimensions_tuple,
        "dual_dimensions": dual_dimensions_tuple,
        "full_role_obstruction_ranks": full_obstruction_ranks,
        "mixed_line_obstruction_ranks": mixed_obstruction_ranks,
        "image_equals_kernel": True,
        "restriction_surjective": True,
        "fixed_layer_not_retagged": True,
    }


def verify_tail_capacity_and_basis_boundary() -> dict[str, object]:
    q = 3
    valuations = (1, 2)
    adapted_basis = ((1, 0), (0, 1))
    displayed_named_basis = ((1, 1), (0, 1))

    positive_capacities = (1, 1)
    positive_deficits = subspace_tail_deficits(
        adapted_basis, valuations, q, positive_capacities
    )
    assert positive_deficits == (0, 0, 0)
    assert has_basis_flexible_assignment(
        adapted_basis, valuations, q, positive_capacities
    )

    total_only_capacities = (2, 0)
    total_only_deficits = subspace_tail_deficits(
        adapted_basis, valuations, q, total_only_capacities
    )
    assert total_only_deficits == (0, 1, 0)
    assert not has_basis_flexible_assignment(
        adapted_basis, valuations, q, total_only_capacities
    )

    named_deficits = named_tail_deficits(
        displayed_named_basis, valuations, positive_capacities
    )
    assert tuple(role_depth(role, valuations) for role in displayed_named_basis) == (2, 2)
    assert named_deficits == (0, 1, 0)
    assert not has_named_assignment((2, 2), positive_capacities)
    assert rank_mod(displayed_named_basis, q) == rank_mod(adapted_basis, q) == 2

    # Exhaust the six subspaces of F_3^2 and small two-layer capacities.
    subspaces = (
        (),
        ((1, 0),),
        ((1, 1),),
        ((1, 2),),
        ((0, 1),),
        adapted_basis,
    )
    checked_cases = 0
    for subspace in subspaces:
        for capacities in product(range(3), repeat=2):
            criterion = max(
                subspace_tail_deficits(subspace, valuations, q, capacities)
            ) <= 0
            brute_force = has_basis_flexible_assignment(
                subspace, valuations, q, capacities
            )
            assert criterion == brute_force
            checked_cases += 1

    # Tail capacity can pass before a label gate removes the only layer-1 edge.
    assert has_named_assignment((1, 2), positive_capacities)
    assert not has_named_assignment((2, 2), positive_capacities)

    return {
        "positive_deficits": positive_deficits,
        "total_capacity_only_deficits": total_only_deficits,
        "displayed_named_basis_deficits": named_deficits,
        "checked_small_cases": checked_cases,
    }


def verify() -> None:
    exact = verify_exact_sequence_and_rank_formula()
    capacity = verify_tail_capacity_and_basis_boundary()
    print("verified: filtered source-dual exact sequence", exact)
    print("verified: basis-flexible and named tail capacity", capacity)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
