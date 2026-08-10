#!/usr/bin/env python3
"""Verify the partial-prefix relation-SNF and physical-capacity boundary."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product
from math import gcd


def cyclic_character_solutions(
    source_order: int,
    coordinates: tuple[int, ...],
    phases: tuple[int, ...],
    target_order: int,
) -> tuple[int, ...]:
    """Return generator images for homomorphisms C_n -> C_d fitting the rows."""
    assert len(coordinates) == len(phases)
    return tuple(
        image
        for image in range(target_order)
        if source_order * image % target_order == 0
        and all(
            coordinate * image % target_order == phase % target_order
            for coordinate, phase in zip(coordinates, phases)
        )
    )


def relation_witness(
    source_order: int,
    coordinates: tuple[int, ...],
    phases: tuple[int, ...],
    target_order: int,
    relation: tuple[int, ...],
) -> tuple[int, int]:
    assert len(coordinates) == len(phases) == len(relation)
    source_value = sum(
        coefficient * coordinate
        for coefficient, coordinate in zip(relation, coordinates)
    ) % source_order
    target_value = sum(
        coefficient * phase
        for coefficient, phase in zip(relation, phases)
    ) % target_order
    return source_value, target_value


def maximum_matching(
    requests: tuple[str, ...], candidates: dict[str, tuple[str, ...]]
) -> dict[str, str]:
    """Small exact bipartite matching for already-expanded physical tokens."""
    token_to_request: dict[str, str] = {}

    def augment(request: str, seen: set[str]) -> bool:
        for token in candidates[request]:
            if token in seen:
                continue
            seen.add(token)
            previous = token_to_request.get(token)
            if previous is None or augment(previous, seen):
                token_to_request[token] = request
                return True
        return False

    for request in requests:
        augment(request, set())
    return {request: token for token, request in token_to_request.items()}


def multiplicative_order(value: int, modulus: int) -> int:
    current = 1
    for order in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("multiplicative order not found")


def verify() -> None:
    # Positive control: rho(g)=3 on C_12 realizes phases 0,1,2 at 0,3g,6g.
    positive_solutions = cyclic_character_solutions(
        12, (0, 3, 6), (0, 1, 2), 4
    )
    assert positive_solutions == (3,)
    positive_matching = maximum_matching(
        ("sheet0", "sheet1", "sheet2"),
        {
            "sheet0": ("token0",),
            "sheet1": ("token1",),
            "sheet2": ("token2",),
        },
    )
    assert len(positive_matching) == 3

    # Hall can pass while the selected source relation fails in C_4.
    hall_only_matching = maximum_matching(
        ("primitive_sheet",), {"primitive_sheet": ("only_token",)}
    )
    assert len(hall_only_matching) == 1
    assert cyclic_character_solutions(6, (1,), (1,), 4) == ()
    assert relation_witness(6, (1,), (1,), 4, (6,)) == (0, 2)

    # Relation compatibility cannot manufacture a second physical occurrence.
    hall_deficit = maximum_matching(
        ("request0", "request1"),
        {"request0": ("shared_token",), "request1": ("shared_token",)},
    )
    assert len(hall_deficit) == 1

    # Local bundle edges can pass Hall while reusing one hidden occurrence.
    local_bundle_matching = maximum_matching(
        ("request0", "request1"),
        {"request0": ("bundle0",), "request1": ("bundle1",)},
    )
    underlying_occurrence = {"bundle0": "occurrence0", "bundle1": "occurrence0"}
    assert len(local_bundle_matching) == 2
    assert len(
        {
            underlying_occurrence[token]
            for token in local_bundle_matching.values()
        }
    ) == 1

    # p=557281: every old-state coordinate x in C_198 obeys 198*x=0,
    # while a primitive C_4 sheet sends that relation to 2.
    source_order = 198
    target_order = 4
    target_modulus = 728
    order_three = multiplicative_order(3, target_modulus)
    order_83 = multiplicative_order(83, target_modulus)
    subgroup_three = {
        pow(3, exponent, target_modulus) for exponent in range(order_three)
    }
    subgroup_83 = {
        pow(83, exponent, target_modulus) for exponent in range(order_83)
    }
    assert order_three == 6
    assert order_83 == target_order
    assert subgroup_three & subgroup_83 == {1}
    assert pow(3 % 13, 3, 13) == 1
    assert pow(83 % 13, 3, 13) == 8
    assert multiplicative_order(8, 13) == target_order

    assert relation_witness(
        source_order, (137,), (1,), target_order, (source_order,)
    ) == (0, 2)
    assert relation_witness(
        source_order, (137,), (2,), target_order, (source_order,)
    ) == (0, 0)

    all_hom_generator_images = tuple(
        image
        for image in range(target_order)
        if source_order * image % target_order == 0
    )
    assert all_hom_generator_images == (0, 2)
    assert all(image % 2 == 0 for image in all_hom_generator_images)

    for coordinate in range(source_order):
        assert cyclic_character_solutions(
            source_order, (coordinate,), (1,), target_order
        ) == ()

    # Complete classification of actual-F raw three-record 83-chains.
    modulus = 199
    bounds = ((-1, 1), (-1, 1), (-3, 3), (-1, 1))
    records = tuple(
        product(*(range(lower, upper + 1) for lower, upper in bounds))
    )

    def inside(record: tuple[int, ...]) -> bool:
        return all(
            lower <= coordinate <= upper
            for coordinate, (lower, upper) in zip(record, bounds)
        )

    def add(
        record: tuple[int, ...], increment: tuple[int, ...]
    ) -> tuple[int, ...]:
        return tuple(
            coordinate + delta
            for coordinate, delta in zip(record, increment)
        )

    factors = (2, 5, 11, 2083)

    def source_value(record: tuple[int, ...]) -> int:
        value = 1
        for factor, exponent in zip(factors, record):
            value = value * pow(factor, exponent, modulus) % modulus
        return value

    step_a = (0, 0, -2, 1)
    step_r = (0, 1, -5, 0)
    step_s = (0, -1, 1, 2)
    step_t = (0, 2, 3, 2)
    expected_steps = {step_a, step_r, step_s, step_t}
    candidate_steps = tuple(
        product(range(-2, 3), range(-2, 3), range(-6, 7), range(-2, 3))
    )
    valid_steps = tuple(
        candidate for candidate in candidate_steps if source_value(candidate) == 83
    )
    assert set(valid_steps) == expected_steps
    assert all(
        any(inside(add(record, step)) for record in records)
        for step in valid_steps
    )

    labelled_chains = []
    for start in records:
        for first_step in valid_steps:
            middle = add(start, first_step)
            if not inside(middle):
                continue
            for second_step in valid_steps:
                end = add(middle, second_step)
                if inside(end):
                    labelled_chains.append(
                        (start, first_step, second_step, middle, end)
                    )

    pair_counts = Counter(
        (first_step, second_step)
        for _, first_step, second_step, _, _ in labelled_chains
    )
    assert pair_counts == Counter(
        {(step_a, step_a): 27, (step_r, step_s): 12, (step_s, step_r): 12}
    )
    assert len(labelled_chains) == 51

    starts_by_pair = {
        pair: {
            start
            for start, first_step, second_step, _, _ in labelled_chains
            if (first_step, second_step) == pair
        }
        for pair in pair_counts
    }
    expected_a_starts = {
        (u, v, c, -1)
        for u in range(-1, 2)
        for v in range(-1, 2)
        for c in range(1, 4)
    }
    expected_rs_starts = {
        (u, v, c, -1)
        for u in range(-1, 2)
        for v in (-1, 0)
        for c in (2, 3)
    }
    expected_sr_starts = {
        (u, v, c, -1)
        for u in range(-1, 2)
        for v in (0, 1)
        for c in (1, 2)
    }
    assert starts_by_pair[(step_a, step_a)] == expected_a_starts
    assert starts_by_pair[(step_r, step_s)] == expected_rs_starts
    assert starts_by_pair[(step_s, step_r)] == expected_sr_starts
    assert all(step_t not in pair for pair in pair_counts)

    total_step = (0, 0, -4, 2)
    assert all(
        add(first_step, second_step) == total_step
        for _, first_step, second_step, _, _ in labelled_chains
    )

    raw_chains = tuple(
        (start, middle, end)
        for start, _, _, middle, end in labelled_chains
    )
    all_raw_records = {
        record for chain in raw_chains for record in chain
    }
    assert len(all_raw_records) == 105
    assert len(tuple(record for chain in raw_chains for record in chain)) == 153

    for pair in pair_counts:
        class_records = tuple(
            record
            for chain, labelled in zip(raw_chains, labelled_chains)
            if (labelled[1], labelled[2]) == pair
            for record in chain
        )
        assert len(class_records) == len(set(class_records))

    records_by_start: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for start, _, _, middle, end in labelled_chains:
        records_by_start.setdefault(start, set()).update((start, middle, end))
    assert all(
        records_by_start[left].isdisjoint(records_by_start[right])
        for left, right in combinations(records_by_start, 2)
    )
    lift_multiplicities = Counter(
        Counter(start for start, _, _, _, _ in labelled_chains).values()
    )
    assert lift_multiplicities == Counter({1: 6, 2: 18, 3: 3})

    absolute_image_triples = {
        tuple(source_value(record) for record in chain)
        for chain in raw_chains
    }
    assert len(absolute_image_triples) == 27
    normalized_image_triples = {
        tuple(
            image * pow(images[0], -1, modulus) % modulus
            for image in images
        )
        for images in absolute_image_triples
    }
    assert normalized_image_triples == {(1, 83, pow(83, 2, modulus))}

    representative_images = tuple(
        source_value(record)
        for record in ((0, 0, 2, -1), (0, 0, 0, 0), (0, 0, -2, 1))
    )
    assert representative_images == (12, 1, 83)
    inverse_first = pow(representative_images[0], -1, modulus)
    assert tuple(
        image * inverse_first % modulus for image in representative_images
    ) == (1, 83, pow(83, 2, modulus))
    assert pow(3, 183, modulus) == 83
    assert gcd(198, 183) == 3
    assert multiplicative_order(83, modulus) == 66
    assert 66 % target_order == 2
    assert relation_witness(
        source_order, (183,), (1,), target_order, (66,)
    ) == (0, 2)
    assert multiplicative_order(pow(83, 2, modulus), modulus) == 33
    assert relation_witness(
        source_order, (2 * 183,), (2,), target_order, (33,)
    ) == (0, 2)

    c9_factor_phases = (4, 3, 0, 3)
    assert all(step[0] == 0 for step in valid_steps)
    assert {
        sum(
            phase * increment
            for phase, increment in zip(c9_factor_phases, step)
        )
        % 9
        for step in valid_steps
    } == {3}
    assert 183 % 2 == 1

    def active_source_line(record: tuple[int, ...]) -> int:
        return 14_924 + 89_544 * record[0]

    assert all(
        len({active_source_line(record) for record in chain}) == 1
        for chain in raw_chains
    )

    print("PASS: FG_PARTIAL_PREFIX_RELATION_SNF_PHYSICAL_CAPACITY_GATE")
    print(
        {
            "status": "PARTIAL_PREFIX_RELATION_PRESERVING_ADAPTER_CERT",
            "source": "C12",
            "target": "C4",
            "generator_image": positive_solutions[0],
            "physical_matching_size": len(positive_matching),
        }
    )
    print(
        {
            "status": "HALL_PASS_RELATION_SNF_OBSTRUCTED",
            "source": "C6",
            "target": "C4",
            "failing_relation_target_value": 2,
        }
    )
    print(
        {
            "status": (
                "P557_ORIGINAL_STATE_RELATION_PRESERVING_C4_"
                "ADAPTER_INCLUDING_B1_NO_GO"
            ),
            "source_exponent": source_order,
            "target_order": target_order,
            "hom_generator_images": all_hom_generator_images,
            "primitive_sheet_relation_target_value": 2,
            "raw_edge_lift_count": len(valid_steps),
            "raw_labelled_chain_count": len(raw_chains),
            "raw_chain_type_counts": {
                "a,a": pair_counts[(step_a, step_a)],
                "r,s": pair_counts[(step_r, step_s)],
                "s,r": pair_counts[(step_s, step_r)],
            },
            "raw_image_triple_count": len(absolute_image_triples),
            "raw_distinct_record_count": len(all_raw_records),
            "raw_lift_multiplicity_distribution": dict(lift_multiplicities),
            "raw_edge_order": 66,
            "raw_endpoint_ratio_order": 33,
            "raw_edge_c9_phase": 3,
            "active_source_line_collapses_all_chains": True,
            "physical_occurrence_adapter_proved": False,
        }
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
