#!/usr/bin/env python3
"""Focused checks for dependent-role evaluation and tensor selectors."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product

Vector = tuple[int, ...]
Matrix = tuple[int, ...]
Menu = tuple[Vector, ...]


def rank_mod(vectors: list[Vector], prime: int) -> int:
    if not vectors:
        return 0
    matrix = [[entry % prime for entry in vector] for vector in vectors]
    row = 0
    width = len(matrix[0])
    for column in range(width):
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
    return row


def nonempty_menus(vectors: tuple[Vector, ...]) -> tuple[Menu, ...]:
    return tuple(
        tuple(vectors[index] for index in indices)
        for size in range(1, len(vectors) + 1)
        for indices in combinations(range(len(vectors)), size)
    )


def request_subsets(size: int):
    for mask in range(1 << size):
        yield tuple(index for index in range(size) if mask & (1 << index))


def generalized_rado_value(menus: tuple[Menu, ...], prime: int) -> int:
    request_count = len(menus)
    return min(
        rank_mod(
            list(
                {
                    vector
                    for index in subset
                    for vector in menus[index]
                }
            ),
            prime,
        )
        + request_count
        - len(subset)
        for subset in request_subsets(request_count)
    )


def brute_max_transversal_rank(
    menus: tuple[Menu, ...],
    prime: int,
) -> int:
    return max(
        rank_mod(list(selection), prime)
        for selection in product(*menus)
    )


def outer_matrix(vector: Vector, coefficients: Vector, prime: int) -> Matrix:
    return tuple(
        (entry * coefficient) % prime
        for entry in vector
        for coefficient in coefficients
    )


def basis_matrix(basis: tuple[Vector, ...]) -> Matrix:
    if not basis:
        return ()
    return tuple(
        basis[column][row]
        for row in range(len(basis[0]))
        for column in range(len(basis))
    )


def add_matrices(left: Matrix, right: Matrix, prime: int) -> Matrix:
    return tuple((a + b) % prime for a, b in zip(left, right))


def coefficient_vectors(width: int, prime: int) -> tuple[Vector, ...]:
    return tuple(product(range(prime), repeat=width))


def tensor_atom_counts(
    menu: Menu,
    demand_rank: int,
    prime: int,
) -> Counter[Matrix]:
    atoms: Counter[Matrix] = Counter()
    for vector in menu:
        for coefficients in coefficient_vectors(demand_rank, prime):
            atoms[outer_matrix(vector, coefficients, prime)] += 1
    return atoms


def tensor_representation_count(
    menus: tuple[Menu, ...],
    demand_basis: tuple[Vector, ...],
    prime: int,
) -> int:
    dimension = len(demand_basis[0]) if demand_basis else len(menus[0][0])
    target = basis_matrix(demand_basis)
    zero = (0,) * (dimension * len(demand_basis))
    reachable: Counter[Matrix] = Counter({zero: 1})
    for menu in menus:
        atoms = tensor_atom_counts(menu, len(demand_basis), prime)
        next_reachable: Counter[Matrix] = Counter()
        for left, left_count in reachable.items():
            for right, right_count in atoms.items():
                next_reachable[add_matrices(left, right, prime)] += (
                    left_count * right_count
                )
        reachable = next_reachable
    return reachable[target]


def spans_demand(
    selection: tuple[Vector, ...],
    demand_basis: tuple[Vector, ...],
    prime: int,
) -> bool:
    selected_rank = rank_mod(list(selection), prime)
    return rank_mod(list(selection) + list(demand_basis), prime) == selected_rank


def brute_prescribed_span_exists(
    menus: tuple[Menu, ...],
    demand_basis: tuple[Vector, ...],
    prime: int,
) -> bool:
    return any(
        spans_demand(selection, demand_basis, prime)
        for selection in product(*menus)
    )


def dot(left: Vector, right: Vector, prime: int) -> int:
    return sum(a * b for a, b in zip(left, right)) % prime


def dual_hitting_exists(
    menus: tuple[Menu, ...],
    demand_basis: tuple[Vector, ...],
    prime: int,
) -> bool:
    dimension = len(menus[0][0])
    functionals = tuple(
        functional
        for functional in product(range(prime), repeat=dimension)
        if any(functional)
        and any(dot(functional, demand, prime) for demand in demand_basis)
    )
    return any(
        all(
            any(dot(functional, vector, prime) for vector in selection)
            for functional in functionals
        )
        for selection in product(*menus)
    )


def vector_span(vectors: tuple[Vector, ...], prime: int) -> frozenset[Vector]:
    if not vectors:
        return frozenset({()})
    dimension = len(vectors[0])
    return frozenset(
        tuple(
            sum(coefficients[index] * vectors[index][coordinate]
                for index in range(len(vectors))) % prime
            for coordinate in range(dimension)
        )
        for coefficients in product(range(prime), repeat=len(vectors))
    )


def subspaces_f2(dimension: int) -> tuple[frozenset[Vector], ...]:
    vectors = tuple(product(range(2), repeat=dimension))
    spaces = set()
    for mask in range(1 << len(vectors)):
        subset = tuple(
            vectors[index]
            for index in range(len(vectors))
            if mask & (1 << index)
        )
        if (0,) * dimension not in subset:
            continue
        closed = True
        subset_set = set(subset)
        for left in subset:
            for right in subset:
                if tuple(a ^ b for a, b in zip(left, right)) not in subset_set:
                    closed = False
                    break
            if not closed:
                break
        if closed:
            spaces.add(frozenset(subset))
    return tuple(spaces)


def prescribed_subspace_cuts_pass_f2(
    menus: tuple[Menu, ...],
    demand_basis: tuple[Vector, ...],
) -> bool:
    demand = vector_span(demand_basis, 2)
    dimension = len(menus[0][0])
    demand_rank = rank_mod(list(demand_basis), 2)
    for subspace in subspaces_f2(dimension):
        intersection_rank = rank_mod(list(demand & subspace), 2)
        escaping_menus = sum(
            not set(menu).issubset(subspace) for menu in menus
        )
        if demand_rank - intersection_rank > escaping_menus:
            return False
    return True


def evaluation_vector(
    relation: Vector,
    role_basis: tuple[Vector, ...],
    prime: int,
) -> Vector:
    return tuple(dot(role, relation, prime) for role in role_basis)


def fourier_inversion_count_f2(
    menus: tuple[Menu, ...],
    demand_basis: tuple[Vector, ...],
) -> int:
    dimension = len(menus[0][0])
    demand_rank = len(demand_basis)
    target = basis_matrix(demand_basis)
    group = tuple(product(range(2), repeat=dimension * demand_rank))
    transforms = []
    for menu in menus:
        atoms = tensor_atom_counts(menu, demand_rank, 2)
        transforms.append(
            {
                frequency: sum(
                    count * (-1) ** dot(frequency, matrix, 2)
                    for matrix, count in atoms.items()
                )
                for frequency in group
            }
        )
    numerator = sum(
        (-1) ** dot(frequency, target, 2)
        * product_value(
            transform[frequency] for transform in transforms
        )
        for frequency in group
    )
    assert numerator % len(group) == 0
    return numerator // len(group)


def product_value(values) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def verify_exhaustive_f2_square() -> dict[str, int]:
    zero, e1, e2, e12 = (0, 0), (1, 0), (0, 1), (1, 1)
    vectors = (zero, e1, e2, e12)
    menu_options = nonempty_menus(vectors)
    demand_bases = ((), (e1,), (e2,), (e12,), (e1, e2))
    rank_families = 0
    span_cases = 0
    for request_count in range(1, 4):
        for menus in product(menu_options, repeat=request_count):
            expected_rank = brute_max_transversal_rank(menus, 2)
            assert generalized_rado_value(menus, 2) == expected_rank
            rank_families += 1
            for demand_basis in demand_bases:
                brute = brute_prescribed_span_exists(menus, demand_basis, 2)
                tensor = tensor_representation_count(
                    menus, demand_basis, 2
                ) > 0
                dual = dual_hitting_exists(menus, demand_basis, 2)
                assert tensor == brute == dual
                span_cases += 1
    return {
        "rank_families": rank_families,
        "tensor_dual_span_cases": span_cases,
    }


def verify_role_evaluation_controls() -> dict[str, object]:
    zero, e1, e2 = (0, 0), (1, 0), (0, 1)
    role_x, role_y = e1, e2

    raw_false_column = e2
    raw_rank = rank_mod([raw_false_column], 2)
    evaluated = evaluation_vector(raw_false_column, (role_x,), 2)
    assert raw_rank == 1
    assert evaluated == (0,)
    assert generalized_rado_value(((evaluated,),), 2) == 0

    dependent_menus = (
        (evaluation_vector(e1, (role_x, role_y), 2),),
        (evaluation_vector(e1, (role_x, role_y), 2),),
        (evaluation_vector(e2, (role_x, role_y), 2),),
    )
    assert generalized_rado_value(dependent_menus, 2) == 2
    assert brute_max_transversal_rank(dependent_menus, 2) == 2
    assert generalized_rado_value(dependent_menus, 2) < 3

    concentrated_menus = ((e1, e2), (zero,), (zero,))
    assert rank_mod(list({*concentrated_menus[0]}), 2) == 2
    assert generalized_rado_value(concentrated_menus, 2) == 1
    assert brute_max_transversal_rank(concentrated_menus, 2) == 1

    return {
        "raw_source_rank_false_positive": (raw_rank, 0),
        "dependent_physical_requests": 3,
        "role_rank": 2,
        "generalized_rado_value": 2,
        "ordinary_three_request_rado": False,
        "union_rank_only_false_positive": (2, 1),
    }


def verify_prescribed_span_boundary() -> dict[str, object]:
    e1, e2, e12 = (1, 0), (0, 1), (1, 1)
    menus = ((e1, e2),)
    demand_basis = (e12,)
    assert prescribed_subspace_cuts_pass_f2(menus, demand_basis)
    assert generalized_rado_value(menus, 2) == 1
    assert not brute_prescribed_span_exists(menus, demand_basis, 2)
    assert tensor_representation_count(menus, demand_basis, 2) == 0
    assert not dual_hitting_exists(menus, demand_basis, 2)
    assert fourier_inversion_count_f2(menus, demand_basis) == 0

    positive_menus = ((e1,), (e2,))
    positive_basis = (e1, e2)
    direct_count = tensor_representation_count(
        positive_menus, positive_basis, 2
    )
    assert direct_count > 0
    assert fourier_inversion_count_f2(
        positive_menus, positive_basis
    ) == direct_count
    return {
        "field": "F2",
        "ambient_dimension": 2,
        "requests": 1,
        "menu_size": 2,
        "all_subspace_cuts": True,
        "tensor_membership": False,
        "dual_hitting": False,
        "fourier_count": 0,
        "positive_tensor_count": direct_count,
    }


def verify() -> None:
    exhaustive = verify_exhaustive_f2_square()
    evaluation = verify_role_evaluation_controls()
    prescribed = verify_prescribed_span_boundary()
    print("verified: generalized Rado and tensor-dual equivalence", exhaustive)
    print("verified: dependent-role evaluation controls", evaluation)
    print("verified: prescribed-span strict boundary", prescribed)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
