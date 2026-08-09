#!/usr/bin/env python3
"""Focused checks for prescribed-target rectangular Hall--Rado contraction."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product
from typing import NamedTuple

from type_i_owner_profile_canonical_base_target_slot_capacity import (
    canonical_slots,
    canonical_vertex,
    eligible_deep_targets,
    owner_prefix,
)


class Candidate(NamedTuple):
    request: str
    deep_key: tuple[object, ...]
    shallow_key: tuple[object, ...]
    column_key: tuple[object, ...]
    target_key: tuple[object, ...]
    profile: tuple[int, int] | None = None


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def rank_one_profile_passes(
    records: tuple[int, int],
    slots: tuple[int, int],
    gamma: int,
    prime: int,
) -> bool:
    return (
        slots[1]
        - slots[0]
        - gamma * (records[1] - records[0])
    ) % prime == 0


def rank_mod(vectors: list[tuple[int, ...]], prime: int) -> int:
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


def nonempty_subsets(values: tuple[str, ...]):
    for size in range(1, len(values) + 1):
        yield from combinations(values, size)


def fixed_targets(
    requests: tuple[str, ...], candidates: tuple[Candidate, ...]
) -> dict[str, tuple[object, ...]] | None:
    targets: dict[str, tuple[object, ...]] = {}
    for request in requests:
        keys = {
            candidate.target_key
            for candidate in candidates
            if candidate.request == request
        }
        if len(keys) != 1:
            return None
        targets[request] = next(iter(keys))
    return targets


def target_capacity_passes(
    targets: dict[str, tuple[object, ...]],
    capacity: dict[tuple[object, ...], int],
) -> bool:
    return all(
        load <= capacity.get(key, 0)
        for key, load in Counter(targets.values()).items()
    )


def incremental_deep_key(candidate: Candidate) -> tuple[object, ...]:
    if candidate.deep_key == candidate.target_key:
        return ("private-target-claim", candidate.request)
    return candidate.deep_key


def fixed_target_source_system(
    requests: tuple[str, ...],
    candidates: tuple[Candidate, ...],
    occurrence_capacity: dict[tuple[object, ...], int],
) -> tuple[
    tuple[Candidate, ...],
    dict[tuple[object, ...], int],
] | None:
    targets = fixed_targets(requests, candidates)
    if targets is None or not target_capacity_passes(targets, occurrence_capacity):
        return None
    target_load = Counter(targets.values())
    deep_capacity = {
        key: value - target_load.get(key, 0)
        for key, value in occurrence_capacity.items()
    }
    for request in requests:
        deep_capacity[("private-target-claim", request)] = 1
    charged = tuple(
        candidate._replace(deep_key=incremental_deep_key(candidate))
        for candidate in candidates
    )
    return charged, deep_capacity


def hall_deficit(
    requests: tuple[str, ...],
    candidates: tuple[Candidate, ...],
    attribute: str,
    capacity: dict[tuple[object, ...], int] | None = None,
) -> tuple[tuple[str, ...], int] | None:
    for subset in nonempty_subsets(requests):
        neighbors = {
            getattr(candidate, attribute)
            for candidate in candidates
            if candidate.request in subset
        }
        available = (
            len(neighbors)
            if capacity is None
            else sum(capacity.get(key, 0) for key in neighbors)
        )
        if available < len(subset):
            return subset, available
    return None


def rado_deficit(
    requests: tuple[str, ...],
    candidates: tuple[Candidate, ...],
    column_vectors: dict[tuple[object, ...], tuple[int, ...]],
    prime: int,
) -> tuple[tuple[str, ...], int] | None:
    for subset in nonempty_subsets(requests):
        columns = {
            candidate.column_key
            for candidate in candidates
            if candidate.request in subset
        }
        rank = rank_mod([column_vectors[column] for column in columns], prime)
        if rank < len(subset):
            return subset, rank
    return None


def is_rectangular(
    requests: tuple[str, ...], candidates: tuple[Candidate, ...]
) -> bool:
    for request in requests:
        menu = tuple(candidate for candidate in candidates if candidate.request == request)
        if not menu:
            return False
        deep = {candidate.deep_key for candidate in menu}
        shallow = {candidate.shallow_key for candidate in menu}
        columns = {candidate.column_key for candidate in menu}
        actual = {
            (candidate.deep_key, candidate.shallow_key, candidate.column_key)
            for candidate in menu
        }
        if actual != set(product(deep, shallow, columns)):
            return False
    return True


def rectangular_conditions_pass(
    requests: tuple[str, ...],
    candidates: tuple[Candidate, ...],
    column_vectors: dict[tuple[object, ...], tuple[int, ...]],
    shallow_capacity: dict[tuple[object, ...], int],
    occurrence_capacity: dict[tuple[object, ...], int],
    prime: int,
) -> bool:
    source_system = fixed_target_source_system(
        requests, candidates, occurrence_capacity
    )
    if source_system is None:
        return False
    charged, deep_capacity = source_system
    return bool(
        is_rectangular(requests, charged)
        and hall_deficit(requests, charged, "deep_key", deep_capacity) is None
        and hall_deficit(
            requests, charged, "shallow_key", shallow_capacity
        ) is None
        and rado_deficit(requests, charged, column_vectors, prime) is None
    )


def brute_assignment_exists(
    requests: tuple[str, ...],
    candidates: tuple[Candidate, ...],
    column_vectors: dict[tuple[object, ...], tuple[int, ...]],
    shallow_capacity: dict[tuple[object, ...], int],
    occurrence_capacity: dict[tuple[object, ...], int],
    prime: int,
) -> bool:
    menus = [
        tuple(candidate for candidate in candidates if candidate.request == request)
        for request in requests
    ]
    if any(not menu for menu in menus):
        return False
    for selection in product(*menus):
        shallow_load = Counter(candidate.shallow_key for candidate in selection)
        occurrence_load: Counter[tuple[object, ...]] = Counter()
        for candidate in selection:
            for key in {candidate.deep_key, candidate.target_key}:
                occurrence_load[key] += 1
        if any(
            load > shallow_capacity.get(key, 0)
            for key, load in shallow_load.items()
        ):
            continue
        if any(
            load > occurrence_capacity.get(key, 0)
            for key, load in occurrence_load.items()
        ):
            continue
        vectors = [column_vectors[candidate.column_key] for candidate in selection]
        if rank_mod(vectors, prime) == len(requests):
            return True
    return False


def verify_rectangular_product_fixtures() -> dict[str, object]:
    requests = ("r1", "r2")
    deep_1, deep_2 = ("deep", 1), ("deep", 2)
    shallow_1, shallow_2 = ("shallow", 1), ("shallow", 2)
    column_1, column_2 = ("column", 1), ("column", 2)
    target_1, target_2 = ("target", 1), ("target", 2)
    candidates = tuple(
        Candidate("r1", deep, shallow_1, column_1, target_1)
        for deep in (deep_1, deep_2)
    ) + tuple(
        Candidate("r2", deep, shallow_2, column_2, target_2)
        for deep in (deep_1, deep_2)
    )
    vectors = {column_1: (1, 0), column_2: (0, 1)}
    shallow_capacity = {shallow_1: 1, shallow_2: 1}
    occurrence_capacity = {
        deep_1: 1,
        deep_2: 1,
        target_1: 1,
        target_2: 1,
    }
    assert is_rectangular(requests, candidates)
    assert rectangular_conditions_pass(
        requests,
        candidates,
        vectors,
        shallow_capacity,
        occurrence_capacity,
        3,
    )
    assert brute_assignment_exists(
        requests,
        candidates,
        vectors,
        shallow_capacity,
        occurrence_capacity,
        3,
    )

    shared_deep = ("deep", "capacity-two")
    capacity_candidates = (
        Candidate("r1", shared_deep, shallow_1, column_1, target_1),
        Candidate("r2", shared_deep, shallow_2, column_2, target_2),
    )
    shared_occurrence_capacity = {
        shared_deep: 2,
        target_1: 1,
        target_2: 1,
    }
    assert hall_deficit(requests, capacity_candidates, "deep_key") == (
        requests,
        1,
    )
    assert (
        hall_deficit(
            requests,
            capacity_candidates,
            "deep_key",
            {shared_deep: 2},
        )
        is None
    )
    assert rectangular_conditions_pass(
        requests,
        capacity_candidates,
        vectors,
        shallow_capacity,
        shared_occurrence_capacity,
        3,
    )
    assert brute_assignment_exists(
        requests,
        capacity_candidates,
        vectors,
        shallow_capacity,
        shared_occurrence_capacity,
        3,
    )

    self_request = ("self",)
    self_occurrence = ("occurrence", "self")
    self_shallow = ("shallow", "self")
    self_column = ("column", "self")
    self_candidate = (
        Candidate(
            "self",
            self_occurrence,
            self_shallow,
            self_column,
            self_occurrence,
        ),
    )
    assert rectangular_conditions_pass(
        self_request,
        self_candidate,
        {self_column: (1,)},
        {self_shallow: 1},
        {self_occurrence: 1},
        3,
    )
    assert brute_assignment_exists(
        self_request,
        self_candidate,
        {self_column: (1,)},
        {self_shallow: 1},
        {self_occurrence: 1},
        3,
    )

    cross_role = (
        Candidate("r1", target_2, shallow_1, column_1, target_1),
        Candidate("r2", target_1, shallow_2, column_2, target_2),
    )
    assert not rectangular_conditions_pass(
        requests,
        cross_role,
        vectors,
        shallow_capacity,
        {target_1: 1, target_2: 1},
        3,
    )
    assert not brute_assignment_exists(
        requests,
        cross_role,
        vectors,
        shallow_capacity,
        {target_1: 1, target_2: 1},
        3,
    )
    return {
        "requests": 2,
        "candidate_edges": len(candidates),
        "capacitated_deep_key": (2, 2),
        "self_source_target_key": "one-charge-pass",
        "cross_request_role_swap": "residual-deficit",
        "deep_hall": True,
        "shallow_hall": True,
        "column_rado": True,
        "assignment": True,
    }


def verify_profile_phase_coupling_empty() -> dict[str, object]:
    p, q, layer, d_value, target = 4441, 5, 1, 66, 396
    assert is_prime(p) and p % 24 == 1
    bound = (p - 1) // 4
    prefix = owner_prefix(p, q**layer)
    deeper_prefix = owner_prefix(p, q ** (layer + 1))
    delta = (deeper_prefix - prefix) // (q**layer)
    assert (bound, prefix, deeper_prefix, delta) == (1110, 1, 21, 4)

    slots = canonical_slots(p, q, layer, d_value)
    assert slots == (
        (13, 66, 1, 66, 3),
        (79, 396, 6, 11, 4),
        (145, 726, 11, 6, 0),
    )
    targets = eligible_deep_targets(p, q, layer, d_value)
    assert targets == ((121, 11, 5), (396, 66, 10))
    anonymous = tuple(
        (deep[0], shallow[0], target_value)
        for deep in slots
        if deep[4] == delta
        for shallow in slots
        if shallow[4] != delta
        for target_value, _, _ in targets
    )
    assert anonymous == (
        (79, 13, 121),
        (79, 13, 396),
        (79, 145, 121),
        (79, 145, 396),
    )
    anonymous_capacity = min(
        len({deep for deep, _, _ in anonymous}),
        len({shallow for _, shallow, _ in anonymous}),
        len({target_value for _, _, target_value in anonymous}),
    )
    assert anonymous_capacity == 1

    target_base = canonical_vertex(target)[0]
    assert target_base == 66
    nonempty = {
        candidate_base: canonical_slots(p, q, layer, candidate_base)
        for candidate_base in range(target_base, bound + 1, target_base)
        if canonical_slots(p, q, layer, candidate_base)
    }
    assert nonempty == {
        66: slots,
        264: ((211, 1056, 4, 66, 1),),
    }

    survivors = []
    for candidate_base, candidate_slots in nonempty.items():
        for left, right in product(candidate_slots, repeat=2):
            if (right[0] - left[0]) % q != 2:
                continue
            survivors.append(
                (
                    candidate_base,
                    (left[0], right[0]),
                    (left[1], right[1]),
                    (left[4], right[4]),
                )
            )
    assert survivors == [(66, (13, 145), (66, 726), (3, 0))]
    assert rank_one_profile_passes((0, 1), survivors[0][1], 2, q)
    next_layer_edges = tuple(
        survivor
        for survivor in survivors
        if (survivor[3][0] == delta) != (survivor[3][1] == delta)
    )
    assert next_layer_edges == ()
    return {
        "prime": p,
        "fixed_base": d_value,
        "anonymous_triples": len(anonymous),
        "anonymous_capacity": anonymous_capacity,
        "joint_survivor": survivors[0],
        "named_next_layer_edges": 0,
    }


def verify_occurrence_deficit_separation() -> dict[str, object]:
    p, q, layer, d_value = 10273, 3, 1, 70
    assert is_prime(p) and p % 24 == 1
    prefix = owner_prefix(p, q**layer)
    deep_prefix = owner_prefix(p, q ** (layer + 1))
    delta = (deep_prefix - prefix) // (q**layer)
    assert (prefix, deep_prefix, delta) == (2, 8, 2)
    slots = canonical_slots(p, q, layer, d_value)
    assert slots == (
        (46, 140, 2, 35, 1),
        (116, 350, 5, 14, 2),
        (326, 980, 14, 5, 2),
        (816, 2450, 35, 2, 0),
    )
    targets = eligible_deep_targets(p, q, layer, d_value)
    assert targets == (
        (35, 35, 12),
        (98, 14, 6),
        (350, 70, 12),
        (980, 70, 12),
    )
    assert rank_one_profile_passes((0, 70), (46, 116), 1, q)
    assert rank_one_profile_passes((0, 490), (326, 816), 1, q)
    assert rank_one_profile_passes((0, 700), (116, 816), 1, q)
    anonymous_capacity = min(
        sum(slot[4] == delta for slot in slots),
        sum(slot[4] != delta for slot in slots),
        len(targets),
    )
    assert anonymous_capacity == 2

    requests = ("r1", "r2")
    deep_350, deep_980 = ("S", 350, 3, 2), ("S", 980, 3, 2)
    shallow_140 = ("S", 140, 3, 1, 70)
    shallow_2450 = ("S", 2450, 3, 1, 70)
    column_1, column_2 = ("column", 1), ("column", 2)
    target_35, target_350 = ("T", 35, 3, 2), ("T", 350, 3, 2)
    vectors = {column_1: (1, 0), column_2: (0, 1)}
    shallow_capacity = {shallow_140: 1, shallow_2450: 1}
    occurrence_capacity = {
        deep_350: 1,
        deep_980: 1,
        target_35: 1,
        target_350: 1,
    }

    target_collision = (
        Candidate("r1", deep_350, shallow_140, column_1, target_35, (46, 116)),
        Candidate(
            "r2", deep_980, shallow_2450, column_2, target_35, (326, 816)
        ),
    )
    collision_targets = fixed_targets(requests, target_collision)
    assert collision_targets is not None
    assert not target_capacity_passes(collision_targets, occurrence_capacity)
    assert hall_deficit(requests, target_collision, "deep_key") is None
    assert hall_deficit(requests, target_collision, "shallow_key") is None
    assert rado_deficit(requests, target_collision, vectors, q) is None
    assert not brute_assignment_exists(
        requests,
        target_collision,
        vectors,
        shallow_capacity,
        occurrence_capacity,
        q,
    )

    full = (
        Candidate("r1", deep_350, shallow_140, column_1, target_35, (46, 116)),
        Candidate(
            "r2", deep_980, shallow_2450, column_2, target_350, (326, 816)
        ),
    )
    assert rectangular_conditions_pass(
        requests,
        full,
        vectors,
        shallow_capacity,
        occurrence_capacity,
        q,
    )
    assert brute_assignment_exists(
        requests,
        full,
        vectors,
        shallow_capacity,
        occurrence_capacity,
        q,
    )

    deep_collision = (
        Candidate("r1", deep_350, shallow_140, column_1, target_35, (46, 116)),
        Candidate(
            "r2", deep_350, shallow_2450, column_2, target_350, (116, 816)
        ),
    )
    deep_collision_targets = fixed_targets(requests, deep_collision)
    assert deep_collision_targets is not None
    assert target_capacity_passes(deep_collision_targets, occurrence_capacity)
    assert hall_deficit(requests, deep_collision, "deep_key") == (requests, 1)
    assert not brute_assignment_exists(
        requests,
        deep_collision,
        vectors,
        shallow_capacity,
        occurrence_capacity,
        q,
    )
    return {
        "slots": slots,
        "targets": tuple(target for target, _, _ in targets),
        "anonymous_capacity": anonymous_capacity,
        "target_collision": (2, 1),
        "interface_assignment": True,
        "deep_source_deficit": (1, 2),
    }


def projection_hall_passes(
    requests: tuple[str, ...], candidates: tuple[Candidate, ...], attribute: str
) -> bool:
    return hall_deficit(requests, candidates, attribute) is None


def verify_nonrectangular_source_false_positive() -> dict[str, object]:
    requests = ("r1", "r2")
    deep_1, deep_2 = ("deep", 1), ("deep", 2)
    shallow_1, shallow_2 = ("shallow", 1), ("shallow", 2)
    column_1, column_2 = ("column", 1), ("column", 2)
    target_1, target_2 = ("target", 1), ("target", 2)
    candidates = (
        Candidate("r1", deep_1, shallow_1, column_1, target_1),
        Candidate("r2", deep_1, shallow_2, column_2, target_2),
        Candidate("r2", deep_2, shallow_1, column_2, target_2),
    )
    vectors = {column_1: (1, 0), column_2: (0, 1)}
    shallow_capacity = {shallow_1: 1, shallow_2: 1}
    occurrence_capacity = {
        deep_1: 1,
        deep_2: 1,
        target_1: 1,
        target_2: 1,
    }
    source_system = fixed_target_source_system(
        requests, candidates, occurrence_capacity
    )
    assert source_system is not None
    charged, deep_capacity = source_system
    assert not is_rectangular(requests, charged)
    assert hall_deficit(
        requests, charged, "deep_key", deep_capacity
    ) is None
    assert hall_deficit(
        requests, charged, "shallow_key", shallow_capacity
    ) is None
    assert rado_deficit(requests, charged, vectors, 3) is None
    assert not rectangular_conditions_pass(
        requests,
        candidates,
        vectors,
        shallow_capacity,
        occurrence_capacity,
        3,
    )
    assert not brute_assignment_exists(
        requests,
        candidates,
        vectors,
        shallow_capacity,
        occurrence_capacity,
        3,
    )
    return {
        "requests": 2,
        "candidates": 3,
        "deep_projection_hall": True,
        "shallow_projection_hall": True,
        "column_rado": True,
        "joint_assignment": False,
    }


def verify_fixed_d_two_coordinate_rectangle_false_positive() -> dict[str, object]:
    requests = ("r1", "r2")
    deep_1, deep_2 = ("deep", 1), ("deep", 2)
    shallow_1, shallow_2 = ("shallow", 1), ("shallow", 2)
    column_1, column_2 = ("column", 1), ("column", 2)
    target_1, target_2 = ("target", 1), ("target", 2)
    candidates = (
        Candidate("r1", deep_1, shallow_1, column_1, target_1),
        Candidate("r1", deep_2, shallow_1, column_2, target_1),
        Candidate("r2", deep_1, shallow_2, column_2, target_2),
        Candidate("r2", deep_2, shallow_2, column_1, target_2),
    )
    vectors = {column_1: (1, 0), column_2: (0, 1)}
    shallow_capacity = {shallow_1: 1, shallow_2: 1}
    occurrence_capacity = {
        deep_1: 1,
        deep_2: 1,
        target_1: 1,
        target_2: 1,
    }
    for request in requests:
        menu = tuple(
            candidate for candidate in candidates if candidate.request == request
        )
        deep_shallow = {
            (candidate.deep_key, candidate.shallow_key) for candidate in menu
        }
        assert deep_shallow == {
            (deep, shallow)
            for deep in (deep_1, deep_2)
            for shallow in {candidate.shallow_key for candidate in menu}
        }
    assert not is_rectangular(requests, candidates)
    assert hall_deficit(requests, candidates, "deep_key") is None
    assert hall_deficit(requests, candidates, "shallow_key") is None
    assert rado_deficit(requests, candidates, vectors, 3) is None
    assert not brute_assignment_exists(
        requests,
        candidates,
        vectors,
        shallow_capacity,
        occurrence_capacity,
        3,
    )
    return {
        "requests": 2,
        "candidates": 4,
        "deep_shallow_rectangular": True,
        "column_rado": True,
        "joint_assignment": False,
    }


def verify_variable_target_false_positive() -> dict[str, object]:
    requests = ("r1", "r2")
    source_a, source_b = ("source", "a"), ("source", "b")
    shallow_1, shallow_2 = ("shallow", 1), ("shallow", 2)
    column_1, column_2 = ("column", 1), ("column", 2)
    target_alpha, target_beta = ("target", "alpha"), ("target", "beta")
    candidates = (
        Candidate("r1", source_a, shallow_1, column_1, target_alpha),
        Candidate("r2", source_a, shallow_2, column_2, target_beta),
        Candidate("r2", source_b, shallow_2, column_2, target_alpha),
    )
    assert fixed_targets(requests, candidates) is None
    assert projection_hall_passes(requests, candidates, "deep_key")
    assert projection_hall_passes(requests, candidates, "target_key")
    vectors = {column_1: (1, 0), column_2: (0, 1)}
    assert not brute_assignment_exists(
        requests,
        candidates,
        vectors,
        {shallow_1: 1, shallow_2: 1},
        {
            source_a: 1,
            source_b: 1,
            target_alpha: 1,
            target_beta: 1,
        },
        3,
    )
    return {
        "requests": 2,
        "candidates": 3,
        "source_projection_hall": True,
        "target_projection_hall": True,
        "joint_assignment": False,
    }


def verify() -> None:
    rectangular = verify_rectangular_product_fixtures()
    nonrectangular = verify_nonrectangular_source_false_positive()
    fixed_d_twist = verify_fixed_d_two_coordinate_rectangle_false_positive()
    profile_empty = verify_profile_phase_coupling_empty()
    occurrences = verify_occurrence_deficit_separation()
    twisted = verify_variable_target_false_positive()
    print("verified: focused rectangular Hall--Rado contraction fixtures", rectangular)
    print(
        "verified: nonrectangular source projection false positive",
        nonrectangular,
    )
    print(
        "verified: fixed-D two-coordinate rectangle false positive",
        fixed_d_twist,
    )
    print("verified: p=4441 profile-phase coupling empty", profile_empty)
    print("verified: p=10273 occurrence deficit separation", occurrences)
    print("verified: variable-target projection Hall false positive", twisted)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
