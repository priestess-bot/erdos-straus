#!/usr/bin/env python3
"""Focused checks for exact-successor source overhead and variable role capacity."""

from __future__ import annotations

import argparse
from itertools import combinations, product

Vector = tuple[int, ...]
Basis = tuple[Vector, ...]


def dot(left: Vector, right: Vector, prime: int) -> int:
    return sum(a * b for a, b in zip(left, right)) % prime


def rref_basis(vectors: tuple[Vector, ...] | list[Vector], prime: int) -> Basis:
    if not vectors:
        return ()
    matrix = [[entry % prime for entry in vector] for vector in vectors]
    row = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (
                index
                for index in range(row, len(matrix))
                if matrix[index][column] % prime
            ),
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


def rank_mod(vectors: tuple[Vector, ...] | list[Vector], prime: int) -> int:
    return len(rref_basis(vectors, prime))


def gaussian_binomial(dimension: int, rank: int, prime: int) -> int:
    if dimension < 0 or rank < 0 or rank > dimension:
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
        rref_basis(generators, prime)
        for generators in combinations(nonzero, rank)
        if rank_mod(generators, prime) == rank
    }
    assert len(spaces) == gaussian_binomial(dimension, rank, prime)
    return tuple(sorted(spaces))


def all_subspaces(dimension: int, prime: int) -> tuple[Basis, ...]:
    return tuple(
        space
        for rank in range(dimension + 1)
        for space in subspaces(dimension, rank, prime)
    )


def is_contained(left: Basis, right: Basis, prime: int) -> bool:
    return rank_mod(right + left, prime) == len(right)


def is_annihilated(role_space: Basis, vector_space: Basis, prime: int) -> bool:
    return all(
        dot(role, vector, prime) == 0
        for role in role_space
        for vector in vector_space
    )


def minimal_cover_rank(
    selected: Basis,
    source: Basis,
    dimension: int,
    prime: int,
) -> tuple[int, Basis]:
    for candidate_rank in range(dimension + 1):
        for overhead in subspaces(dimension, candidate_rank, prime):
            if is_contained(source, rref_basis(selected + overhead, prime), prime):
                return candidate_rank, overhead
    raise AssertionError("the ambient space must cover every source span")


def labelled_minimal_overhead(
    selected: Basis,
    labelled_source_columns: tuple[Vector, ...],
    prime: int,
) -> Basis:
    current = rref_basis(selected, prime)
    retained: list[Vector] = []
    for column in labelled_source_columns:
        augmented = rref_basis(current + (column,), prime)
        if len(augmented) > len(current):
            retained.append(column)
            current = augmented
    return tuple(retained)


def verify_minimal_overhead_formula() -> dict[str, int]:
    pair_count = 0
    for prime in (2, 3):
        dimension = 3
        spaces = all_subspaces(dimension, prime)
        for selected in spaces:
            for source in spaces:
                expected = (
                    rank_mod(selected + source, prime) - len(selected)
                )
                actual, overhead = minimal_cover_rank(
                    selected,
                    source,
                    dimension,
                    prime,
                )
                assert actual == expected
                assert is_contained(
                    source,
                    rref_basis(selected + overhead, prime),
                    prime,
                )
                pair_count += 1

    e1 = (1, 0, 0)
    e2 = (0, 1, 0)
    e3 = (0, 0, 1)
    selected = (e1,)
    labelled = (e1, e2, (1, 1, 0), e3)
    retained = labelled_minimal_overhead(selected, labelled, 2)
    source = rref_basis(labelled, 2)
    assert len(retained) == 2
    assert is_contained(source, rref_basis(selected + retained, 2), 2)
    return {
        "checked_subspace_pairs": pair_count,
        "labelled_overhead_rank": len(retained),
    }


def exact_capacity(
    selected: Basis,
    source: Basis,
    dimension: int,
    request_count: int,
    prime: int,
) -> dict[str, int]:
    selected_rank = rank_mod(selected, prime)
    joint_rank = rank_mod(selected + source, prime)
    defect = dimension - request_count
    rank_slack = request_count - selected_rank
    minimal_overhead = joint_rank - selected_rank
    role_capacity = dimension - joint_rank
    assert role_capacity == defect + rank_slack - minimal_overhead
    return {
        "defect": defect,
        "rank_slack": rank_slack,
        "minimal_overhead": minimal_overhead,
        "role_capacity": role_capacity,
    }


def verify_rank_slack_and_saturation() -> dict[str, object]:
    e1 = (1, 0, 0, 0)
    e2 = (0, 1, 0, 0)
    e3 = (0, 0, 1, 0)
    e4 = (0, 0, 0, 1)
    selected = (e1, e1)
    contracted_source = (e1, e2, e3)
    contracted = exact_capacity(selected, contracted_source, 4, 2, 2)
    assert contracted == {
        "defect": 2,
        "rank_slack": 1,
        "minimal_overhead": 2,
        "role_capacity": 1,
    }
    annihilator_lines = [
        line
        for line in subspaces(4, 1, 2)
        if is_annihilated(line, rref_basis(selected + contracted_source, 2), 2)
    ]
    assert annihilator_lines == [(e4,)]
    assert dot(e4, e4, 2) == 1
    assert dot(e4, e2, 2) == 0

    saturated = exact_capacity(selected, (e1, e2, e3, e4), 4, 2, 2)
    assert saturated == {
        "defect": 2,
        "rank_slack": 1,
        "minimal_overhead": 3,
        "role_capacity": 0,
    }
    return {
        "rank_slack_rescues_h_equals_delta": contracted,
        "source_dominating_saturation": saturated,
        "target_outside_joint_span": e4,
        "target_inside_joint_span": e2,
    }


def variable_incidence(
    joint_spaces: tuple[Basis, ...],
    dimension: int,
    slice_rank: int,
    prime: int,
    target: Vector,
) -> dict[str, int]:
    slices = subspaces(dimension, slice_rank, prime)
    branch_sizes = [
        sum(is_annihilated(role_space, joint, prime) for joint in joint_spaces)
        for role_space in slices
    ]
    role_capacities = [
        dimension - rank_mod(joint, prime) for joint in joint_spaces
    ]
    exact_total = sum(
        gaussian_binomial(capacity, slice_rank, prime)
        for capacity in role_capacities
    )
    assert sum(branch_sizes) == exact_total

    target_visible_slices = [
        role_space
        for role_space in slices
        if not is_annihilated(role_space, (target,), prime)
    ]
    assert len(target_visible_slices) == (
        gaussian_binomial(dimension, slice_rank, prime)
        - gaussian_binomial(dimension - 1, slice_rank, prime)
    )
    target_incidence = sum(
        sum(
            is_annihilated(role_space, joint, prime)
            for joint in joint_spaces
        )
        for role_space in target_visible_slices
    )
    target_exact = 0
    for joint, capacity in zip(joint_spaces, role_capacities):
        if not is_contained((target,), joint, prime):
            assert capacity >= 1
            target_exact += (
                gaussian_binomial(capacity, slice_rank, prime)
                - gaussian_binomial(capacity - 1, slice_rank, prime)
            )
    assert target_incidence == target_exact
    return {
        "prime": prime,
        "dimension": dimension,
        "slice_rank": slice_rank,
        "successor_count": len(joint_spaces),
        "incidence_total": exact_total,
        "target_visible_slice_count": len(target_visible_slices),
        "target_visible_incidence": target_incidence,
    }


def verify_variable_and_target_visible_incidence() -> tuple[dict[str, int], ...]:
    e1 = (1, 0, 0, 0)
    e2 = (0, 1, 0, 0)
    e3 = (0, 0, 1, 0)
    e4 = (0, 0, 0, 1)
    joint_spaces_2 = (
        (e1, e2, e3),
        (e1, e2),
        (e1, e2, e4),
        (e1, e2, e3, e4),
    )
    rank_one = variable_incidence(joint_spaces_2, 4, 1, 2, e4)
    rank_two = variable_incidence(joint_spaces_2, 4, 2, 2, e4)
    assert rank_one["incidence_total"] == 5
    assert rank_one["target_visible_incidence"] == 3
    assert rank_two["incidence_total"] == 1
    assert rank_two["target_visible_incidence"] == 1

    f1 = (1, 0, 0)
    f2 = (0, 1, 0)
    f3 = (0, 0, 1)
    joint_spaces_3 = (
        (f1,),
        (f1, f2),
        (f1, f3),
        (f1, f2, f3),
    )
    ternary = variable_incidence(joint_spaces_3, 3, 1, 3, f3)
    return (rank_one, rank_two, ternary)


def verify_same_mincut_different_source_rank() -> dict[str, int]:
    e1 = (1, 0, 0)
    e2 = (0, 1, 0)
    e3 = (0, 0, 1)
    selected = (e3,)
    physical_slot_capacity = 2
    request_count = 3
    max_flow = 2
    assert max_flow == physical_slot_capacity < request_count

    model_a_columns = (e1, e1)
    model_b_columns = (e1, e2)
    model_a_rank = rank_mod(model_a_columns, 2)
    model_b_rank = rank_mod(model_b_columns, 2)
    model_a = exact_capacity(
        selected,
        rref_basis(model_a_columns + selected, 2),
        3,
        1,
        2,
    )
    model_b = exact_capacity(
        selected,
        rref_basis(model_b_columns + selected, 2),
        3,
        1,
        2,
    )
    assert model_a_rank == 1
    assert model_b_rank == 2
    assert model_a["role_capacity"] == 1
    assert model_b["role_capacity"] == 0
    return {
        "physical_slot_capacity": physical_slot_capacity,
        "request_count": request_count,
        "max_flow": max_flow,
        "model_a_source_rank": model_a_rank,
        "model_a_role_capacity": model_a["role_capacity"],
        "model_b_source_rank": model_b_rank,
        "model_b_role_capacity": model_b["role_capacity"],
    }


def verify() -> None:
    minimal = verify_minimal_overhead_formula()
    slack = verify_rank_slack_and_saturation()
    incidence = verify_variable_and_target_visible_incidence()
    mincut = verify_same_mincut_different_source_rank()
    print("verified: minimal labelled source overhead", minimal)
    print("verified: rank slack and source saturation", slack)
    print("verified: variable and target-visible incidence", incidence)
    print("verified: same mincut, different source-rank capacity", mincut)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
