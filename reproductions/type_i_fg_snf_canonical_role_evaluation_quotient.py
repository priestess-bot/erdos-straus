#!/usr/bin/env python3
"""Focused checks for the canonical SNF role-evaluation quotient."""

from __future__ import annotations

import argparse
from itertools import combinations, product

Element = tuple[int, ...]
Vector = tuple[int, ...]


def add_group(left: Element, right: Element, invariants: tuple[int, ...]) -> Element:
    return tuple((a + b) % modulus for a, b, modulus in zip(left, right, invariants))


def multiply_group(multiplier: int, value: Element, invariants: tuple[int, ...]) -> Element:
    return tuple((multiplier * entry) % modulus for entry, modulus in zip(value, invariants))


def all_group_elements(invariants: tuple[int, ...]) -> tuple[Element, ...]:
    return tuple(product(*(range(modulus) for modulus in invariants)))


def generated_subgroup(
    generators: tuple[Element, ...], invariants: tuple[int, ...]
) -> frozenset[Element]:
    zero = (0,) * len(invariants)
    seen = {zero}
    frontier = [zero]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = add_group(current, generator, invariants)
            if candidate not in seen:
                seen.add(candidate)
                frontier.append(candidate)
    return frozenset(seen)


def q_multiple_subgroup(invariants: tuple[int, ...], prime: int) -> frozenset[Element]:
    return frozenset(
        multiply_group(prime, value, invariants)
        for value in all_group_elements(invariants)
    )


def q_visible(value: Element, invariants: tuple[int, ...], prime: int) -> Vector:
    return tuple(
        coordinate % prime
        for coordinate, modulus in zip(value, invariants)
        if modulus % prime == 0
    )


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


def vector_span(
    vectors: tuple[Vector, ...], dimension: int, prime: int
) -> frozenset[Vector]:
    zero = (0,) * dimension
    if not vectors:
        return frozenset({zero})
    return frozenset(
        tuple(
            sum(coefficients[index] * vectors[index][coordinate]
                for index in range(len(vectors))) % prime
            for coordinate in range(dimension)
        )
        for coefficients in product(range(prime), repeat=len(vectors))
    )


def label_hom_from_generators(
    generators: tuple[Element, ...],
    labels: tuple[int, ...],
    invariants: tuple[int, ...],
    prime: int,
) -> dict[Element, int] | None:
    zero = (0,) * len(invariants)
    values = {zero: 0}
    frontier = [zero]
    while frontier:
        current = frontier.pop()
        for generator, label in zip(generators, labels):
            candidate = add_group(current, generator, invariants)
            candidate_label = (values[current] + label) % prime
            if candidate in values:
                if values[candidate] != candidate_label:
                    return None
            else:
                values[candidate] = candidate_label
                frontier.append(candidate)
    return values


def elementary_characters(invariants: tuple[int, ...], prime: int) -> tuple[Vector, ...]:
    dimension = sum(modulus % prime == 0 for modulus in invariants)
    return tuple(product(range(prime), repeat=dimension))


def character_value(
    coefficients: Vector,
    value: Element,
    invariants: tuple[int, ...],
    prime: int,
) -> int:
    return dot(coefficients, q_visible(value, invariants, prime), prime)


def ambient_extensions(
    source_labels: dict[Element, int],
    invariants: tuple[int, ...],
    prime: int,
) -> tuple[Vector, ...]:
    return tuple(
        coefficients
        for coefficients in elementary_characters(invariants, prime)
        if all(
            character_value(coefficients, source, invariants, prime) == label
            for source, label in source_labels.items()
        )
    )


def ambient_extension_cut_passes(
    source_labels: dict[Element, int],
    invariants: tuple[int, ...],
    prime: int,
) -> bool:
    source_subgroup = frozenset(source_labels)
    intersection = source_subgroup & q_multiple_subgroup(invariants, prime)
    return all(source_labels[value] == 0 for value in intersection)


def all_subgroups(invariants: tuple[int, ...]) -> tuple[frozenset[Element], ...]:
    elements = all_group_elements(invariants)
    subgroups = {
        generated_subgroup(tuple(generators), invariants)
        for size in range(0, 3)
        for generators in combinations(elements, size)
    }
    return tuple(subgroups)


def all_local_homomorphisms(
    subgroup: frozenset[Element],
    invariants: tuple[int, ...],
    prime: int,
) -> tuple[dict[Element, int], ...]:
    ordered = tuple(sorted(subgroup))
    zero = (0,) * len(invariants)
    result = []
    for values in product(range(prime), repeat=len(ordered)):
        candidate = dict(zip(ordered, values))
        if candidate[zero] != 0:
            continue
        if all(
            candidate[add_group(left, right, invariants)]
            == (candidate[left] + candidate[right]) % prime
            for left in ordered
            for right in ordered
        ):
            result.append(candidate)
    return tuple(result)


def verify_extension_theorem() -> dict[str, int]:
    checked = 0
    for invariants in ((4,), (2, 2)):
        for subgroup in all_subgroups(invariants):
            for local_hom in all_local_homomorphisms(subgroup, invariants, 2):
                cut = ambient_extension_cut_passes(local_hom, invariants, 2)
                brute = bool(ambient_extensions(local_hom, invariants, 2))
                assert cut == brute
                checked += 1

    # A locally valid character on <2g> in C4 need not extend to an F2-role.
    c4_labels = label_hom_from_generators(((2,),), (1,), (4,), 2)
    assert c4_labels is not None
    assert not ambient_extension_cut_passes(c4_labels, (4,), 2)
    assert not ambient_extensions(c4_labels, (4,), 2)

    # Two ambient lifts agree on a closed source span but differ on a new row.
    closed_labels = label_hom_from_generators(((1, 0),), (1,), (2, 2), 2)
    assert closed_labels is not None
    lifts = ambient_extensions(closed_labels, (2, 2), 2)
    assert set(lifts) == {(1, 0), (1, 1)}
    assert {
        character_value(lift, (1, 0), (2, 2), 2) for lift in lifts
    } == {1}
    assert {
        character_value(lift, (0, 1), (2, 2), 2) for lift in lifts
    } == {0, 1}

    return {
        "small_group_local_homs": checked,
        "c4_local_but_not_ambient": 1,
        "closed_span_extensions": len(lifts),
    }


def evaluation_columns(
    source_vectors: tuple[Vector, ...],
    role_rows: tuple[Vector, ...],
    prime: int,
) -> tuple[Vector, ...]:
    return tuple(
        tuple(dot(role, source, prime) for role in role_rows)
        for source in source_vectors
    )


def verify_perfect_quotient(
    source_vectors: tuple[Vector, ...],
    role_rows: tuple[Vector, ...],
    prime: int,
) -> dict[str, int]:
    dimension = len(source_vectors[0])
    source_space = vector_span(source_vectors, dimension, prime)
    radical = frozenset(
        value
        for value in source_space
        if all(dot(role, value, prime) == 0 for role in role_rows)
    )
    source_rank = rank_mod(list(source_space), prime)
    radical_rank = rank_mod(list(radical), prime)
    columns = evaluation_columns(source_vectors, role_rows, prime)
    role_rank = rank_mod(list(columns), prime)
    assert source_rank - radical_rank == role_rank

    subset_checks = 0
    for size in range(len(source_vectors) + 1):
        for indices in combinations(range(len(source_vectors)), size):
            selected_sources = [source_vectors[index] for index in indices]
            selected_columns = [columns[index] for index in indices]
            quotient_rank = (
                rank_mod(selected_sources + list(radical), prime) - radical_rank
            )
            assert quotient_rank == rank_mod(selected_columns, prime)
            subset_checks += 1
    return {
        "source_rank": source_rank,
        "radical_rank": radical_rank,
        "role_rank": role_rank,
        "subset_rank_checks": subset_checks,
    }


def request_subsets(size: int):
    for mask in range(1 << size):
        yield tuple(index for index in range(size) if mask & (1 << index))


def generalized_rado_value(menus: tuple[tuple[Vector, ...], ...], prime: int) -> int:
    request_count = len(menus)
    return min(
        rank_mod(
            list({vector for index in subset for vector in menus[index]}),
            prime,
        )
        + request_count
        - len(subset)
        for subset in request_subsets(request_count)
    )


def brute_transversal_rank(menus: tuple[tuple[Vector, ...], ...], prime: int) -> int:
    return max(rank_mod(list(selection), prime) for selection in product(*menus))


def verify_evaluation_capacity() -> dict[str, object]:
    # H=C4+C2 and q=2 have a two-dimensional ambient elementary quotient.
    invariants = (4, 2)
    source_elements = ((1, 0), (0, 1), (3, 1))
    source_vectors = tuple(q_visible(value, invariants, 2) for value in source_elements)
    roles = ((1, 0), (0, 1))
    quotient = verify_perfect_quotient(source_vectors, roles, 2)
    columns = evaluation_columns(source_vectors, roles, 2)
    assert rank_mod(list(columns), 2) == 2

    dependent_menus = ((columns[0],), (columns[0],), (columns[1],))
    assert generalized_rado_value(dependent_menus, 2) == 2
    assert brute_transversal_rank(dependent_menus, 2) == 2

    # A raw nonzero source direction can lie entirely in the role radical.
    raw_sources = ((1, 0), (0, 1))
    raw_role = ((1, 0),)
    raw_columns = evaluation_columns(raw_sources, raw_role, 2)
    assert rank_mod([raw_sources[1]], 2) == 1
    assert rank_mod([raw_columns[1]], 2) == 0

    # The coordinate formula also works at an odd elementary prime.
    odd_invariants = (9, 3)
    odd_sources = tuple(
        q_visible(value, odd_invariants, 3)
        for value in ((1, 0), (0, 1), (4, 2))
    )
    odd_quotient = verify_perfect_quotient(
        odd_sources, ((1, 0), (0, 1)), 3
    )
    assert odd_quotient["role_rank"] == 2

    return {
        "binary_perfect_quotient": quotient,
        "dependent_requests": 3,
        "dependent_role_rank": 2,
        "raw_rank_false_positive": (1, 0),
        "odd_prime_perfect_quotient": odd_quotient,
    }


def verify() -> None:
    extension = verify_extension_theorem()
    capacity = verify_evaluation_capacity()
    print("verified: ambient elementary extension criterion", extension)
    print("verified: canonical role-evaluation quotient", capacity)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
