#!/usr/bin/env python3
"""Focused checks for the generalized-Rado fixed quotient defect."""

from __future__ import annotations

import argparse
from itertools import product

Vector = tuple[int, ...]
Menus = tuple[tuple[Vector, ...], ...]


def dot(left: Vector, right: Vector, prime: int) -> int:
    return sum(a * b for a, b in zip(left, right)) % prime


def rank_mod(vectors: list[Vector], prime: int) -> int:
    if not vectors:
        return 0
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
    return row


def request_subsets(size: int):
    for mask in range(1 << size):
        yield tuple(index for index in range(size) if mask & (1 << index))


def menu_union(menus: Menus, subset: tuple[int, ...]) -> tuple[Vector, ...]:
    return tuple({vector for index in subset for vector in menus[index]})


def cut_data(
    menus: Menus,
    dimension: int,
    subset: tuple[int, ...],
    prime: int,
) -> dict[str, int]:
    capacity = rank_mod(list(menu_union(menus, subset)), prime)
    complement_budget = len(menus) - len(subset)
    quotient_dimension = dimension - capacity
    return {
        "capacity": capacity,
        "quotient_dimension": quotient_dimension,
        "complement_budget": complement_budget,
        "defect": quotient_dimension - complement_budget,
    }


def max_transversal_rank(menus: Menus, prime: int) -> int:
    return max(rank_mod(list(selection), prime) for selection in product(*menus))


def exact_defect(menus: Menus, dimension: int, prime: int) -> dict[str, int]:
    cuts = [
        cut_data(menus, dimension, subset, prime)
        for subset in request_subsets(len(menus))
    ]
    maximum_defect = max(cut["defect"] for cut in cuts)
    transversal_rank = max_transversal_rank(menus, prime)
    assert dimension - transversal_rank == maximum_defect
    return {
        "ambient_dimension": dimension,
        "transversal_rank": transversal_rank,
        "maximum_defect": maximum_defect,
        "cut_count": len(cuts),
    }


def annihilator(
    vectors: tuple[Vector, ...],
    dimension: int,
    prime: int,
) -> frozenset[Vector]:
    return frozenset(
        role
        for role in product(range(prime), repeat=dimension)
        if all(dot(role, vector, prime) == 0 for vector in vectors)
    )


def quotient_span_rank(
    base_vectors: tuple[Vector, ...],
    added_vectors: tuple[Vector, ...],
    prime: int,
) -> int:
    base_rank = rank_mod(list(base_vectors), prime)
    return rank_mod(list(base_vectors + added_vectors), prime) - base_rank


def verify_strict_fixed_quotient(prime: int) -> dict[str, object]:
    zero = 0
    one = 1
    e1 = (one, zero, zero)
    e2 = (zero, one, zero)
    e3 = (zero, zero, one)
    menus: Menus = ((e1,), (e1,), (e2, e3))
    cut = (0, 1)
    data = cut_data(menus, 3, cut, prime)

    assert data == {
        "capacity": 1,
        "quotient_dimension": 2,
        "complement_budget": 1,
        "defect": 1,
    }
    assert rank_mod(list(menu_union(menus, (0, 1, 2))), prime) == 3

    cut_vectors = menu_union(menus, cut)
    completion_annihilators = []
    quotient_ranks = []
    for selection in product(*menus):
        selected_annihilator = annihilator(tuple(selection), 3, prime)
        assert len(selected_annihilator) == prime
        completion_annihilators.append(selected_annihilator)

        complement_vectors = tuple(selection[index] for index in (2,))
        quotient_rank = quotient_span_rank(
            cut_vectors, complement_vectors, prime
        )
        assert quotient_rank == 1
        assert quotient_rank < data["quotient_dimension"]
        quotient_ranks.append(quotient_rank)

    common_completion_annihilator = set.intersection(
        *(set(space) for space in completion_annihilators)
    )
    all_candidate_annihilator = annihilator(
        menu_union(menus, (0, 1, 2)), 3, prime
    )
    assert common_completion_annihilator == {(zero, zero, zero)}
    assert all_candidate_annihilator == frozenset({(zero, zero, zero)})

    formula = exact_defect(menus, 3, prime)
    assert formula["transversal_rank"] == 2
    assert formula["maximum_defect"] == 1
    return {
        "prime": prime,
        "cut": cut,
        **data,
        "completion_annihilator_dimensions": tuple(
            rank_mod(list(space), prime) for space in completion_annihilators
        ),
        "common_scalar_dimension": 0,
        "quotient_completion_ranks": tuple(quotient_ranks),
        "exact_formula": formula,
    }


def verify_tight_boundary() -> dict[str, object]:
    e1 = (1, 0, 0)
    e2 = (0, 1, 0)
    e3 = (0, 0, 1)
    menus: Menus = ((e1,), (e2,), (e3,))
    cut = (0, 1)
    data = cut_data(menus, 3, cut, 2)
    assert data == {
        "capacity": 2,
        "quotient_dimension": 1,
        "complement_budget": 1,
        "defect": 0,
    }
    assert quotient_span_rank(menu_union(menus, cut), (e3,), 2) == 1
    formula = exact_defect(menus, 3, 2)
    assert formula["transversal_rank"] == 3
    assert formula["maximum_defect"] == 0
    return {**data, "exact_formula": formula}


def verify_dependent_requests() -> dict[str, object]:
    e1 = (1, 0)
    e2 = (0, 1)
    menus: Menus = ((e1,), (e1,), (e2,))
    formula = exact_defect(menus, 2, 2)
    assert formula["transversal_rank"] == 2
    assert formula["maximum_defect"] == 0
    return formula


def verify() -> None:
    binary = verify_strict_fixed_quotient(2)
    odd = verify_strict_fixed_quotient(3)
    tight = verify_tight_boundary()
    dependent = verify_dependent_requests()
    print("verified: fixed quotient defect", binary)
    print("verified: odd-prime fixed quotient defect", odd)
    print("verified: strict boundary", tight)
    print("verified: dependent-request exact formula", dependent)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
