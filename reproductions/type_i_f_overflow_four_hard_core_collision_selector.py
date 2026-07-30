#!/usr/bin/env python3
"""Audit the four residual low-modulus Omega carrier hard cores.

The audit is deliberately finite.  It checks three prime-power subfactor
menus on the exact minimum face, then factors only q-divisible label and
modulus differences in the complete linear-source spectrum.  Every resulting
legal divisor gap is subjected to the complete Type II normal-form test.

For any states still left, a finite multi-source Cayley-graph search computes
the exact minimum overflow price after forbidding overflow on the isolated
heavy coordinate.  No wider prime or state census is performed.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
import hashlib
from itertools import combinations, product
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
sys.path.insert(0, str(REPRODUCTIONS))

import type_i_f_overflow_lower_modulus_min_overflow_shared_gap as shared_gap
import type_i_global_linear_b1_failure_general_b_profile_500m as source


WEIGHTED_INPUT = (
    REPRODUCTIONS / "type-i-f-overflow-lower-modulus-weighted-cost-results.json"
)
CARRIER_INPUT = (
    REPRODUCTIONS
    / "type-i-f-overflow-lower-modulus-omega-carrier-boundary-results.json"
)
MINIMUM_GAP_INPUT = (
    REPRODUCTIONS
    / "type_i_f_overflow_lower_modulus_min_overflow_shared_gap_results.json"
)
MINIMUM_GAP_HELPER = (
    REPRODUCTIONS / "type_i_f_overflow_lower_modulus_min_overflow_shared_gap.py"
)
SOURCE_HELPER = (
    REPRODUCTIONS / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
)
TYPE_II_HELPER = (
    REPRODUCTIONS / "type_i_f_overflow_lower_modulus_shared_gap_type_ii.py"
)
OUTPUT = (
    REPRODUCTIONS
    / "type-i-f-overflow-four-hard-core-collision-selector-results.json"
)

EXPECTED_HASHES = {
    WEIGHTED_INPUT: "e4bffc9727821fcfd83a5ae0bb02b8d5326ac58a024563e0a9acdfa355fded82",
    CARRIER_INPUT: "695b20832c683222b3021d444f5bdcb04f706ab10aeeec9801a3ad85fe85c0fb",
    MINIMUM_GAP_INPUT: "085a65615fcd2cc1e30330e4039483f36491871c41cad11d54123514a3f2852f",
    MINIMUM_GAP_HELPER: "5557ec9d3cc989a92e22d0e624f306c92d66184a854feb6ff45b4495ace10352",
    SOURCE_HELPER: "96ee0c6711a4995fe387686a4915b41f1fcefa70cd4fe808c05a4092bf05e07d",
    TYPE_II_HELPER: "eb9905b8fb7428d0d8ce04fdf78f31e9ef937abb26b4fdc43bf93a39f7dc8802",
}

HARD_KEYS = (
    (99_151_369, "reverse", 82_011, 3, 27_337),
    (310_002_289, "reverse", 137_595, 15, 9_173),
    (487_572_409, "forward", 318_051, 3, 106_017),
    (507_599_689, "forward", 5_691, 3, 1_897),
)

EXPECTED = {
    (99_151_369, 27_337): {
        "omega": 9,
        "minimum_vector_count": 2,
        "minimum_pattern_count": 1,
        "separators": (115_561,),
        "menu_counts": (144, 536, 47),
        "collision_edge_count": 0,
        "collision_gap_count": 0,
        "hit_gaps": (),
    },
    (310_002_289, 9_173): {
        "omega": 7,
        "minimum_vector_count": 2,
        "minimum_pattern_count": 1,
        "separators": (647, 95_857),
        "menu_counts": (720, 5_513, 77),
        "collision_edge_count": 3,
        "collision_gap_count": 19,
        "hit_gaps": (55,),
    },
    (487_572_409, 106_017): {
        "omega": 8,
        "minimum_vector_count": 4,
        "minimum_pattern_count": 2,
        "separators": (6_965_317,),
        "menu_counts": (432, 2_564, 76),
        "collision_edge_count": 0,
        "collision_gap_count": 0,
        "hit_gaps": (),
    },
    (507_599_689, 1_897): {
        "omega": 6,
        "minimum_vector_count": 2,
        "minimum_pattern_count": 1,
        "separators": (23,),
        "menu_counts": (224, 1_229, 48),
        "collision_edge_count": 12,
        "collision_gap_count": 32,
        "hit_gaps": (455, 951),
    },
}

EXPECTED_AVOIDANCE = {
    (99_151_369, 27_337): {
        "q": 115_561,
        "component_size": 27_336,
        "price": 12,
    },
    (487_572_409, 106_017): {
        "q": 6_965_317,
        "component_size": 70_676,
        "price": 15,
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("a collision difference must be nonzero")
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factorization_payload(
    factors: tuple[tuple[int, int], ...] | list[tuple[int, int]],
) -> list[list[int]]:
    return [[int(prime), int(exponent)] for prime, exponent in factors]


def canonical_pair(left: int, right: int) -> tuple[int, int]:
    return (left, right) if left <= right else (right, left)


def prime_power_divisors(
    prime_powers: list[tuple[int, int]],
) -> list[int]:
    divisors = [1]
    for prime, exponent in prime_powers:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def minimum_vectors(
    factors: tuple[int, ...],
    bounds: tuple[int, ...],
    modulus: int,
    omega: int,
) -> list[tuple[int, ...]]:
    vectors = [
        tuple(vector)
        for vector in shared_gap.exact_overflow_vectors(list(bounds), omega)
        if shared_gap.relation_residue(list(factors), modulus, vector) == modulus - 1
    ]
    return sorted(vectors)


def overflow_pattern(
    vector: tuple[int, ...], bounds: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(
        max(abs(exponent) - bound, 0)
        for exponent, bound in zip(vector, bounds)
    )


def subfactor_menus(
    factors: tuple[int, ...], vectors: list[tuple[int, ...]]
) -> tuple[set[tuple[int, int]], set[tuple[int, int]], set[tuple[int, int]]]:
    """Return oriented, arbitrary repartition, and pure two-coordinate pairs."""
    oriented: set[tuple[int, int]] = set()
    repartition: set[tuple[int, int]] = set()
    two_coordinate: set[tuple[int, int]] = set()

    for vector in vectors:
        positive = [
            (prime, exponent)
            for prime, exponent in zip(factors, vector)
            if exponent > 0
        ]
        negative = [
            (prime, -exponent)
            for prime, exponent in zip(factors, vector)
            if exponent < 0
        ]
        for left in prime_power_divisors(positive):
            for right in prime_power_divisors(negative):
                oriented.add(canonical_pair(left, right))

        coordinate_options: list[list[tuple[int, int]]] = []
        for prime, exponent in zip(factors, vector):
            budget = abs(exponent)
            coordinate_options.append(
                [(1, 1)]
                + [(prime**power, 1) for power in range(1, budget + 1)]
                + [(1, prime**power) for power in range(1, budget + 1)]
            )
        for choices in product(*coordinate_options):
            left = math.prod(choice[0] for choice in choices)
            right = math.prod(choice[1] for choice in choices)
            repartition.add(canonical_pair(left, right))

        active = [
            (index, prime, abs(exponent))
            for index, (prime, exponent) in enumerate(zip(factors, vector))
            if exponent
        ]
        for (_i, left_prime, left_bound), (
            _j,
            right_prime,
            right_bound,
        ) in combinations(active, 2):
            for left_power in range(1, left_bound + 1):
                for right_power in range(1, right_bound + 1):
                    two_coordinate.add(
                        canonical_pair(
                            left_prime**left_power,
                            right_prime**right_power,
                        )
                    )

    if not oriented <= repartition or not two_coordinate <= repartition:
        raise AssertionError("a restricted subfactor menu left the full repartition menu")
    return oriented, repartition, two_coordinate


def direct_normal_form_candidates(
    prime: int, pairs: set[tuple[int, int]]
) -> list[dict[str, int]]:
    """Exhaust h | A+B with 4AB | p+h for each coprime factor pair."""
    candidates: list[dict[str, int]] = []
    for left, right in sorted(pairs):
        if math.gcd(left, right) != 1:
            raise AssertionError("coordinate repartition lost coprimality")
        step = 4 * left * right
        gap = (-prime) % step
        limit = min(prime - 2, left + right)
        while gap <= limit:
            if gap >= 3 and gap % 4 == 3 and (left + right) % gap == 0:
                common = (prime + gap) // step
                if common < 1 or prime + gap != 4 * left * right * common:
                    raise AssertionError("direct Type II normal form did not reconstruct")
                candidates.append(
                    {
                        "gap": gap,
                        "A": left,
                        "B": right,
                        "C": common,
                    }
                )
            gap += step
    return candidates


def source_label_occurrences(
    states_by_R: dict[int, list[tuple[int, int]]]
) -> dict[int, list[dict[str, int]]]:
    occurrences: dict[int, list[dict[str, int]]] = defaultdict(list)
    for modulus, states in states_by_R.items():
        for a, s in states:
            for label in set((a, s)):
                occurrences[label].append({"R": modulus, "a": a, "s": s})
    return {label: rows for label, rows in sorted(occurrences.items())}


def legal_divisor_gaps(
    difference: int,
    prime: int,
    factor_cache: dict[int, tuple[tuple[int, int], ...]],
) -> tuple[tuple[tuple[int, int], ...], list[int]]:
    if difference not in factor_cache:
        factor_cache[difference] = shared_gap.certified_factorization(difference)
    factors = factor_cache[difference]
    gaps = [
        divisor
        for divisor in shared_gap.divisors_from_factorization(list(factors))
        if divisor % 4 == 3 and 3 <= divisor <= prime - 2
    ]
    return factors, gaps


def collision_edges(
    prime: int,
    original_R: int,
    separators: tuple[int, ...],
    states_by_R: dict[int, list[tuple[int, int]]],
    factor_cache: dict[int, tuple[tuple[int, int], ...]],
) -> tuple[list[dict[str, object]], dict[int, list[dict[str, object]]]]:
    current_states = states_by_R[original_R]
    current_labels = sorted({label for pair in current_states for label in pair})
    occurrences = source_label_occurrences(states_by_R)
    edges: list[dict[str, object]] = []
    by_q: dict[int, list[dict[str, object]]] = {q: [] for q in separators}

    for q in separators:
        for current_label in current_labels:
            for other_label, other_occurrences in occurrences.items():
                if other_label == current_label:
                    continue
                difference = abs(current_label - other_label)
                q_height = valuation(difference, q)
                if not q_height:
                    continue
                factors, gaps = legal_divisor_gaps(difference, prime, factor_cache)
                edge: dict[str, object] = {
                    "edge_id": f"label:q={q}:{current_label}:{other_label}",
                    "kind": "label",
                    "q": q,
                    "current_label": current_label,
                    "other_label": other_label,
                    "other_label_occurrences": other_occurrences,
                    "difference": difference,
                    "q_valuation": q_height,
                    "difference_factorization": factorization_payload(factors),
                    "candidate_gaps": gaps,
                }
                edges.append(edge)
                by_q[q].append(edge)

        for other_R, other_states in states_by_R.items():
            if other_R == original_R:
                continue
            difference = abs(original_R - other_R)
            q_height = valuation(difference, q)
            if not q_height:
                continue
            factors, gaps = legal_divisor_gaps(difference, prime, factor_cache)
            edge = {
                "edge_id": f"modulus:q={q}:{original_R}:{other_R}",
                "kind": "modulus",
                "q": q,
                "current_R": original_R,
                "other_R": other_R,
                "other_states": [[a, s] for a, s in other_states],
                "difference": difference,
                "q_valuation": q_height,
                "difference_factorization": factorization_payload(factors),
                "candidate_gaps": gaps,
            }
            edges.append(edge)
            by_q[q].append(edge)

    edges.sort(key=lambda row: str(row["edge_id"]))
    for q in by_q:
        by_q[q].sort(key=lambda row: str(row["edge_id"]))
    return edges, by_q


def local_pool_profile(
    q: int,
    q_index: int,
    demand_patterns: list[tuple[int, ...]],
    carrier_row: dict[str, object],
    current_states: list[tuple[int, int]],
    original_R: int,
    q_edges: list[dict[str, object]],
) -> dict[str, object]:
    block_values = sorted(
        {
            value
            for a, s in current_states
            for value in (a * original_R + 1, s * original_R + 1)
        }
    )
    positive_blocks = [
        {"value": value, "q_valuation": valuation(value, q)}
        for value in block_values
        if valuation(value, q)
    ]
    label_edges = [edge for edge in q_edges if edge["kind"] == "label"]
    modulus_edges = [edge for edge in q_edges if edge["kind"] == "modulus"]
    height_row = next(
        row for row in carrier_row["coordinate_heights"] if int(row["q"]) == q
    )

    def edge_summary(rows: list[dict[str, object]]) -> dict[str, int]:
        heights = [int(row["q_valuation"]) for row in rows]
        return {
            "positive_edge_count": len(rows),
            "height_sum": sum(heights),
            "height_max": max(heights, default=0),
        }

    block_heights = [int(row["q_valuation"]) for row in positive_blocks]
    return {
        "q": q,
        "minimum_face_demand": min(pattern[q_index] for pattern in demand_patterns),
        "minimum_face_demand_values": sorted(
            {pattern[q_index] for pattern in demand_patterns}
        ),
        "optimistic_three_channel_capacity": int(height_row["three_channel_sum"]),
        "reduced_endpoint_height": int(height_row["reduced_endpoint_max"]),
        "block": {
            "positive_edge_count": len(positive_blocks),
            "height_sum": sum(block_heights),
            "height_max": max(block_heights, default=0),
            "positive_blocks": positive_blocks,
        },
        "label_difference": edge_summary(label_edges),
        "modulus_difference": edge_summary(modulus_edges),
        "all_distinct_local_edge_height_sum": (
            sum(block_heights)
            + sum(int(row["q_valuation"]) for row in label_edges)
            + sum(int(row["q_valuation"]) for row in modulus_edges)
        ),
    }


def constrained_avoidance_price(
    factors: tuple[int, ...],
    bounds: tuple[int, ...],
    modulus: int,
    forbidden_index: int,
) -> dict[str, object]:
    """Compute exact overflow price with no overflow on one coordinate."""
    starts: dict[int, tuple[int, ...]] = {}
    for vector in product(*(range(-bound, bound + 1) for bound in bounds)):
        residue = shared_gap.relation_residue(list(factors), modulus, vector)
        starts.setdefault(residue, tuple(vector))

    distance = {residue: 0 for residue in starts}
    predecessor: dict[int, tuple[int, int, int] | None] = {
        residue: None for residue in starts
    }
    queue = deque(starts)
    generators = [
        (index, sign, prime if sign > 0 else pow(prime, -1, modulus))
        for index, prime in enumerate(factors)
        if index != forbidden_index
        for sign in (1, -1)
    ]
    while queue:
        residue = queue.popleft()
        for index, sign, generator in generators:
            next_residue = residue * generator % modulus
            if next_residue in distance:
                continue
            distance[next_residue] = distance[residue] + 1
            predecessor[next_residue] = (residue, index, sign)
            queue.append(next_residue)

    target = modulus - 1
    if target not in distance:
        raise AssertionError("the constrained target was not reachable")
    steps: list[tuple[int, int]] = []
    root = target
    while predecessor[root] is not None:
        previous, index, sign = predecessor[root]
        steps.append((index, sign))
        root = previous
    steps.reverse()

    start_vector = starts[root]
    witness = list(start_vector)
    for index, sign in steps:
        witness[index] += sign
    witness_tuple = tuple(witness)
    pattern = overflow_pattern(witness_tuple, bounds)
    price = distance[target]
    if (
        pattern[forbidden_index] != 0
        or sum(pattern) != price
        or shared_gap.relation_residue(list(factors), modulus, witness_tuple)
        != target
    ):
        raise AssertionError("the constrained shortest-path witness did not reconstruct")

    step_counts = Counter(steps)
    return {
        "forbidden_overflow_q": factors[forbidden_index],
        "finite_graph_method": (
            "multi_source_BFS_from_all_exponent_box_residues_using_only_the_"
            "other_signed_prime_generators"
        ),
        "box_vector_count": math.prod(2 * bound + 1 for bound in bounds),
        "distinct_start_residue_count": len(starts),
        "reachable_component_size": len(distance),
        "distance_layer_histogram": {
            str(layer): count
            for layer, count in sorted(Counter(distance.values()).items())
        },
        "exact_constrained_overflow_price": price,
        "start_vector": list(start_vector),
        "shortest_path_step_counts": [
            {
                "coordinate_index": index,
                "q": factors[index],
                "sign": sign,
                "count": count,
            }
            for (index, sign), count in sorted(step_counts.items())
        ],
        "witness_vector": list(witness_tuple),
        "witness_overflow_pattern": list(pattern),
    }


def run() -> dict[str, object]:
    for path, expected in EXPECTED_HASHES.items():
        if sha256(path) != expected:
            raise AssertionError(f"frozen input changed: {path.name}")

    weighted_payload = json.loads(WEIGHTED_INPUT.read_text(encoding="utf-8"))
    carrier_payload = json.loads(CARRIER_INPUT.read_text(encoding="utf-8"))
    minimum_gap_payload = json.loads(MINIMUM_GAP_INPUT.read_text(encoding="utf-8"))

    weighted_by_key = {
        (
            int(row["prime"]),
            str(row["orientation"]),
            int(row["original_R"]),
            int(row["gap"]),
            int(row["lower_modulus"]),
        ): row
        for row in weighted_payload["profiles"]
    }
    carrier_by_key = {
        (
            int(row["prime"]),
            str(row["orientation"]),
            int(row["original_R"]),
            int(row["gap"]),
            int(row["lower_modulus"]),
        ): row
        for row in carrier_payload["records"]
    }
    minimum_gap_by_key = {
        (
            int(row["prime"]),
            str(row["orientation"]),
            int(row["original_R"]),
            int(row["gap"]),
            int(row["lower_modulus"]),
        ): row
        for row in minimum_gap_payload["records"]
    }
    if any(
        key not in weighted_by_key
        or key not in carrier_by_key
        or key not in minimum_gap_by_key
        for key in HARD_KEYS
    ):
        raise AssertionError("a frozen hard-core state disappeared")

    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    collision_factor_cache: dict[int, tuple[tuple[int, int], ...]] = {}
    type_ii_cache: dict[tuple[int, int], list[dict[str, int]]] = {}
    records: list[dict[str, object]] = []

    for key in HARD_KEYS:
        prime, orientation, original_R, gap, modulus = key
        expected = EXPECTED[(prime, modulus)]
        weighted = weighted_by_key[key]
        carrier = carrier_by_key[key]
        prior_gap = minimum_gap_by_key[key]
        if prior_gap["all_minimum_type_ii_hit_gaps"]:
            raise AssertionError("a purported hard core already had a shared-gap hit")

        factorization = tuple(
            (int(q), int(exponent)) for q, exponent in weighted["factorization"]
        )
        factors = tuple(q for q, _exponent in factorization)
        bounds = tuple(exponent for _q, exponent in factorization)
        K = math.prod(q**exponent for q, exponent in factorization)
        if source.exact_factorization(K) != list(factorization):
            raise AssertionError("the target factorization did not verify")
        if 4 * K != prime * original_R + 1 or original_R != gap * modulus:
            raise AssertionError("the lower-modulus state did not reconstruct")

        omega = int(weighted["omega_secondary"])
        vectors = minimum_vectors(factors, bounds, modulus, omega)
        patterns = sorted({overflow_pattern(vector, bounds) for vector in vectors})
        prior_vectors = sorted(
            tuple(int(value) for value in row["exponents"])
            for row in prior_gap["minimum_representations"]
        )
        if vectors != prior_vectors:
            raise AssertionError("minimum-face enumeration disagreed with the frozen audit")
        if (
            omega != expected["omega"]
            or len(vectors) != expected["minimum_vector_count"]
            or len(patterns) != expected["minimum_pattern_count"]
        ):
            raise AssertionError("minimum-face counts changed")

        separators = tuple(
            factors[index]
            for index in range(len(factors))
            if min(pattern[index] for pattern in patterns)
            > int(carrier["coordinate_heights"][index]["three_channel_sum"])
        )
        if separators != expected["separators"]:
            raise AssertionError("mandatory separator set changed")

        oriented, repartition, two_coordinate = subfactor_menus(factors, vectors)
        menu_rows: list[dict[str, object]] = []
        for name, pairs in (
            ("oriented_subfactors", oriented),
            ("all_coordinate_repartitions", repartition),
            ("pure_two_coordinate_pairs", two_coordinate),
        ):
            candidates = direct_normal_form_candidates(prime, pairs)
            menu_rows.append(
                {
                    "menu": name,
                    "coprime_pair_count": len(pairs),
                    "direct_normal_form_candidate_count": len(candidates),
                    "direct_normal_form_candidates": candidates,
                }
            )
        if tuple(int(row["coprime_pair_count"]) for row in menu_rows) != expected[
            "menu_counts"
        ]:
            raise AssertionError("subfactor menu size changed")
        if any(row["direct_normal_form_candidate_count"] for row in menu_rows):
            raise AssertionError("a direct subfactor Type II candidate unexpectedly appeared")

        if prime not in source_cache:
            _bound, source_cache[prime] = source.enumerate_linear_source_states(prime)
        states_by_R = source_cache[prime]
        if original_R not in states_by_R:
            raise AssertionError("the current source state disappeared")
        edges, edges_by_q = collision_edges(
            prime,
            original_R,
            separators,
            states_by_R,
            collision_factor_cache,
        )
        collision_gaps = sorted(
            {
                int(candidate_gap)
                for edge in edges
                for candidate_gap in edge["candidate_gaps"]
            }
        )
        hit_gaps: list[int] = []
        for candidate_gap in collision_gaps:
            cache_key = (prime, candidate_gap)
            if cache_key not in type_ii_cache:
                certificates = shared_gap.type_ii_certificates(prime, candidate_gap)
                shared_gap.verify_complete_type_ii_check(
                    prime, candidate_gap, certificates
                )
                type_ii_cache[cache_key] = certificates
            if type_ii_cache[cache_key]:
                hit_gaps.append(candidate_gap)
        if (
            len(edges) != expected["collision_edge_count"]
            or len(collision_gaps) != expected["collision_gap_count"]
            or tuple(hit_gaps) != expected["hit_gaps"]
        ):
            raise AssertionError("collision selector profile changed")

        shared_minimum_gaps = sorted(
            {
                int(candidate_gap)
                for representation in prior_gap["minimum_representations"]
                for candidate_gap in representation["candidate_gaps"]
            }
        )
        hit_profiles = []
        for hit_gap in hit_gaps:
            generating_edges = [
                str(edge["edge_id"])
                for edge in edges
                if hit_gap in edge["candidate_gaps"]
            ]
            if hit_gap in shared_minimum_gaps:
                raise AssertionError("a collision hit was not genuinely non-shared")
            hit_profiles.append(
                {
                    "gap": hit_gap,
                    "non_shared_with_minimum_face": True,
                    "generating_edge_ids": generating_edges,
                    "type_ii_certificate_count": len(type_ii_cache[(prime, hit_gap)]),
                    "type_ii_certificates": type_ii_cache[(prime, hit_gap)],
                }
            )

        local_pools = []
        for q in separators:
            q_index = factors.index(q)
            local_pools.append(
                local_pool_profile(
                    q,
                    q_index,
                    patterns,
                    carrier,
                    states_by_R[original_R],
                    original_R,
                    edges_by_q[q],
                )
            )

        records.append(
            {
                "prime": prime,
                "orientation": orientation,
                "original_R": original_R,
                "gap": gap,
                "lower_modulus": modulus,
                "factorization": factorization_payload(factorization),
                "omega": omega,
                "minimum_vectors": [list(vector) for vector in vectors],
                "minimum_overflow_patterns": [list(pattern) for pattern in patterns],
                "mandatory_separators": list(separators),
                "local_pool_profiles": local_pools,
                "subfactor_menus": menu_rows,
                "minimum_face_shared_candidate_gaps": shared_minimum_gaps,
                "collision_edge_count": len(edges),
                "collision_edges": edges,
                "collision_candidate_gap_count": len(collision_gaps),
                "collision_candidate_gaps": collision_gaps,
                "collision_type_ii_hit_gaps": hit_gaps,
                "collision_type_ii_hit_profiles": hit_profiles,
                "resolved_by_collision_selector": bool(hit_gaps),
            }
        )

    remaining_records = [
        row for row in records if not row["resolved_by_collision_selector"]
    ]
    remaining_keys = {
        (int(row["prime"]), int(row["lower_modulus"])) for row in remaining_records
    }
    if remaining_keys != set(EXPECTED_AVOIDANCE):
        raise AssertionError("the collision selector did not leave the expected two states")

    avoidance_profiles: list[dict[str, object]] = []
    for row in remaining_records:
        prime = int(row["prime"])
        modulus = int(row["lower_modulus"])
        expected = EXPECTED_AVOIDANCE[(prime, modulus)]
        factorization = tuple(
            (int(q), int(exponent)) for q, exponent in row["factorization"]
        )
        factors = tuple(q for q, _exponent in factorization)
        bounds = tuple(exponent for _q, exponent in factorization)
        forbidden_q = int(expected["q"])
        forbidden_index = factors.index(forbidden_q)
        pool = next(
            item for item in row["local_pool_profiles"] if int(item["q"]) == forbidden_q
        )
        if (
            int(pool["block"]["height_sum"]) != 1
            or int(pool["label_difference"]["height_sum"]) != 0
            or int(pool["modulus_difference"]["height_sum"]) != 0
            or int(pool["reduced_endpoint_height"]) != 0
        ):
            raise AssertionError("a residual heavy coordinate was not locally isolated")

        profile = constrained_avoidance_price(
            factors, bounds, modulus, forbidden_index
        )
        if (
            int(profile["reachable_component_size"]) != expected["component_size"]
            or int(profile["exact_constrained_overflow_price"]) != expected["price"]
        ):
            raise AssertionError("the exact constrained avoidance price changed")
        profile.update(
            {
                "prime": prime,
                "orientation": row["orientation"],
                "original_R": row["original_R"],
                "lower_modulus": modulus,
                "unconstrained_omega": row["omega"],
                "price_increase_over_unconstrained_omega": (
                    int(profile["exact_constrained_overflow_price"])
                    - int(row["omega"])
                ),
            }
        )
        avoidance_profiles.append(profile)

    total_pairs = {
        str(row["menu"]): sum(
            int(menu["coprime_pair_count"])
            for record in records
            for menu in record["subfactor_menus"]
            if menu["menu"] == row["menu"]
        )
        for row in records[0]["subfactor_menus"]
    }
    return {
        "arithmetic": (
            "On exactly four frozen Omega minimum-face carrier hard cores: exhaust three "
            "prime-power subfactor pair menus; factor only mandatory-q-divisible label and "
            "modulus differences in the complete linear-source spectrum; independently "
            "check every legal divisor gap by the complete Type II normal form; and compute "
            "the exact no-heavy-coordinate-overflow price only for the two residual states."
        ),
        "scope_note": (
            "A collision difference is only a finite candidate-gap generator. Divisibility "
            "by q does not force one of its cofactor divisors to be a Type II gap. The two "
            "hits are state-scoped certificates, while the two misses and avoidance prices "
            "are finite boundary data, not a universal selector theorem."
        ),
        "inputs": [
            {"file": path.name, "sha256": sha256(path)}
            for path in EXPECTED_HASHES
        ],
        "hard_core_state_count": len(records),
        "minimum_vector_count": sum(len(row["minimum_vectors"]) for row in records),
        "direct_subfactor_pair_counts": total_pairs,
        "direct_subfactor_normal_form_candidate_count": 0,
        "collision_edge_count": sum(int(row["collision_edge_count"]) for row in records),
        "distinct_state_scoped_collision_gap_check_count": sum(
            int(row["collision_candidate_gap_count"]) for row in records
        ),
        "collision_resolved_state_count": sum(
            int(bool(row["resolved_by_collision_selector"])) for row in records
        ),
        "collision_resolved_primes": [
            int(row["prime"]) for row in records if row["resolved_by_collision_selector"]
        ],
        "collision_type_ii_hit_gaps": {
            str(row["prime"]): row["collision_type_ii_hit_gaps"]
            for row in records
            if row["resolved_by_collision_selector"]
        },
        "remaining_state_count": len(remaining_records),
        "remaining_states": [
            {
                "prime": int(row["prime"]),
                "orientation": row["orientation"],
                "original_R": int(row["original_R"]),
                "lower_modulus": int(row["lower_modulus"]),
            }
            for row in remaining_records
        ],
        "exact_constrained_avoidance_profiles": avoidance_profiles,
        "certified_collision_difference_factorization_count": len(
            collision_factor_cache
        ),
        "recursive_prime_certificate_count": len(shared_gap.prime_certificates),
        "records": records,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "hard_core_state_count",
                    "minimum_vector_count",
                    "direct_subfactor_pair_counts",
                    "direct_subfactor_normal_form_candidate_count",
                    "collision_edge_count",
                    "distinct_state_scoped_collision_gap_check_count",
                    "collision_resolved_state_count",
                    "collision_resolved_primes",
                    "collision_type_ii_hit_gaps",
                    "remaining_state_count",
                    "remaining_states",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
