#!/usr/bin/env python3
"""Compute the truncated Pareto overflow frontier of lower-modulus F misses.

For every overflow vector e with |e|_1 <= CAP, the script decides exactly
whether some target-fiber exponent vector has overflow e.  Pareto points found
in this range are therefore globally Pareto minimal: any possible dominator
would have no larger unit cost and is included in the same exhaustive search.
The script separately checks whether the next shell is covered by the upward
closure of the discovered frontier; only that check can certify that no Pareto
point remains beyond the cap.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-overflow-r-modulus-repair-results.json"
SOURCE_INPUT = (
    ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
)
OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-lower-modulus-pareto-overflow-results.json"
)

EXPECTED_INPUT_SHA256 = "c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f"
EXPECTED_SOURCE_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"
MAX_UNIT_OVERFLOW = 9


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def weak_compositions(total: int, length: int):
    """Yield all length-tuples of nonnegative integers summing to total."""
    vector = [0] * length

    def visit(index: int, remaining: int):
        if index == length - 1:
            vector[index] = remaining
            yield tuple(vector)
            return
        for value in range(remaining + 1):
            vector[index] = value
            yield from visit(index + 1, remaining - value)

    if length <= 0:
        if total == 0:
            yield ()
        return
    yield from visit(0, total)


def dominates(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    """Return whether left is coordinatewise no larger than right."""
    return all(a <= b for a, b in zip(left, right))


def exponent_options(
    prime: int, box_exponent: int, overflow: int, modulus: int
) -> list[tuple[int, int]]:
    """List exponent/residue choices having the prescribed coordinate overflow."""
    if math.gcd(prime, modulus) != 1:
        raise AssertionError("a support prime is not a unit modulo the lower modulus")
    inverse = pow(prime, -1, modulus)
    if overflow == 0:
        exponents = range(-box_exponent, box_exponent + 1)
    else:
        magnitude = box_exponent + overflow
        exponents = (-magnitude, magnitude)
    return [
        (
            exponent,
            pow(prime, exponent, modulus)
            if exponent >= 0
            else pow(inverse, -exponent, modulus),
        )
        for exponent in exponents
    ]


def target_fiber_profile(
    options: list[list[tuple[int, int]]], modulus: int
) -> tuple[int, tuple[int, ...] | None]:
    """Count target representations and retain the lexicographically first witness."""
    # residue -> (number of exponent prefixes, lexicographically first prefix)
    states: dict[int, tuple[int, tuple[int, ...]]] = {1 % modulus: (1, ())}
    for coordinate_options in options:
        next_states: dict[int, tuple[int, tuple[int, ...]]] = {}
        for residue, (count, prefix) in states.items():
            for exponent, coordinate_residue in coordinate_options:
                target_residue = residue * coordinate_residue % modulus
                witness = prefix + (exponent,)
                if target_residue not in next_states:
                    next_states[target_residue] = (count, witness)
                    continue
                old_count, old_witness = next_states[target_residue]
                next_states[target_residue] = (
                    old_count + count,
                    min(old_witness, witness),
                )
        states = next_states
    count, witness = states.get(modulus - 1, (0, None))
    return count, witness


def residue(
    factors: list[tuple[int, int]], modulus: int, vector: tuple[int, ...]
) -> int:
    value = 1 % modulus
    for (prime, _box_exponent), exponent in zip(factors, vector):
        base = prime if exponent >= 0 else pow(prime, -1, modulus)
        value = value * pow(base, abs(exponent), modulus) % modulus
    return value


def overflow_of(
    factors: list[tuple[int, int]], vector: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(
        max(abs(exponent) - box_exponent, 0)
        for (_prime, box_exponent), exponent in zip(factors, vector)
    )


def histogram(values) -> dict[str, int]:
    return {
        str(value): count for value, count in sorted(Counter(values).items())
    }


def state_profile(
    prime: int,
    orientation: str,
    original_R: int,
    gap: int,
    modulus: int,
    factors: list[tuple[int, int]],
) -> dict[str, object]:
    rank = len(factors)
    option_cache = [
        [
            exponent_options(q, box_exponent, overflow, modulus)
            for overflow in range(MAX_UNIT_OVERFLOW + 1)
        ]
        for q, box_exponent in factors
    ]

    target_vectors: list[dict[str, object]] = []
    overflow_vectors_examined = 0
    exponent_vectors_encoded = 0
    for total in range(MAX_UNIT_OVERFLOW + 1):
        for overflow_vector in weak_compositions(total, rank):
            overflow_vectors_examined += 1
            options = [
                option_cache[index][coordinate_overflow]
                for index, coordinate_overflow in enumerate(overflow_vector)
            ]
            exponent_vectors_encoded += math.prod(len(values) for values in options)
            representation_count, witness = target_fiber_profile(options, modulus)
            if representation_count == 0:
                continue
            if witness is None:
                raise AssertionError("a positive target count has no witness")
            if overflow_of(factors, witness) != overflow_vector:
                raise AssertionError("a target witness has the wrong overflow vector")
            if residue(factors, modulus, witness) != modulus - 1:
                raise AssertionError("a target witness has the wrong residue")
            target_vectors.append(
                {
                    "overflow_vector": list(overflow_vector),
                    "unit_cost": total,
                    "support_indices": [
                        index
                        for index, value in enumerate(overflow_vector)
                        if value > 0
                    ],
                    "support_primes": [
                        factors[index][0]
                        for index, value in enumerate(overflow_vector)
                        if value > 0
                    ],
                    "support_size": sum(value > 0 for value in overflow_vector),
                    "target_representation_count": representation_count,
                    "lexicographic_witness": list(witness),
                }
            )

    pareto: list[dict[str, object]] = []
    for record in target_vectors:
        candidate = tuple(int(value) for value in record["overflow_vector"])
        if any(
            dominates(
                tuple(int(value) for value in prior["overflow_vector"]), candidate
            )
            for prior in pareto
        ):
            continue
        pareto.append(record)

    if any(int(record["unit_cost"]) == 0 for record in target_vectors):
        raise AssertionError("an F-box miss unexpectedly contains the target in its box")
    for left_index, left in enumerate(pareto):
        left_vector = tuple(int(value) for value in left["overflow_vector"])
        for right_index, right in enumerate(pareto):
            if left_index == right_index:
                continue
            right_vector = tuple(int(value) for value in right["overflow_vector"])
            if dominates(left_vector, right_vector):
                raise AssertionError("the reported Pareto frontier contains domination")
    for record in target_vectors:
        vector = tuple(int(value) for value in record["overflow_vector"])
        if not any(
            dominates(tuple(int(value) for value in point["overflow_vector"]), vector)
            for point in pareto
        ):
            raise AssertionError("the Pareto frontier does not dominate an observed target")

    next_shell = MAX_UNIT_OVERFLOW + 1
    uncovered_next_shell = [
        vector
        for vector in weak_compositions(next_shell, rank)
        if not any(
            dominates(tuple(int(value) for value in point["overflow_vector"]), vector)
            for point in pareto
        )
    ]
    globally_complete = not uncovered_next_shell

    coordinate_usage = [0] * rank
    support_sets: set[tuple[int, ...]] = set()
    for point in pareto:
        support = tuple(int(index) for index in point["support_indices"])
        support_sets.add(support)
        for index in support:
            coordinate_usage[index] += 1

    unit_omega = min(
        (int(point["unit_cost"]) for point in pareto),
        default=None,
    )
    pareto_vectors = [
        tuple(int(value) for value in point["overflow_vector"]) for point in pareto
    ]
    status = (
        "globally_complete"
        if globally_complete
        else "truncated_nonempty"
        if pareto
        else "no_target_through_cap"
    )
    return {
        "prime": prime,
        "orientation": orientation,
        "original_R": original_R,
        "gap": gap,
        "lower_modulus": modulus,
        "factorization": [[q, exponent] for q, exponent in factors],
        "rank": rank,
        "unit_overflow_cap": MAX_UNIT_OVERFLOW,
        "frontier_status": status,
        "globally_complete": globally_complete,
        "next_shell_coverage_certificate": globally_complete,
        "next_shell_unit_cost": next_shell,
        "next_shell_vector_count": math.comb(next_shell + rank - 1, rank - 1),
        "uncovered_next_shell_vector_count": len(uncovered_next_shell),
        "uncovered_next_shell_examples": [
            list(vector) for vector in uncovered_next_shell[:12]
        ],
        "overflow_vectors_examined": overflow_vectors_examined,
        "exponent_vectors_encoded": exponent_vectors_encoded,
        "target_overflow_vector_count_through_cap": len(target_vectors),
        "dominated_target_overflow_vector_count_through_cap": (
            len(target_vectors) - len(pareto)
        ),
        "pareto_vector_count_through_cap": len(pareto),
        "unit_omega": unit_omega,
        "unit_omega_lower_bound": (
            None if unit_omega is not None else MAX_UNIT_OVERFLOW + 1
        ),
        "support_size_histogram": histogram(
            int(point["support_size"]) for point in pareto
        ),
        "single_coordinate_pareto_count": sum(
            int(point["support_size"]) == 1 for point in pareto
        ),
        "multi_coordinate_pareto_count": sum(
            int(point["support_size"]) >= 2 for point in pareto
        ),
        "distinct_support_count": len(support_sets),
        "coordinate_usage_counts": coordinate_usage,
        "used_coordinate_count": sum(count > 0 for count in coordinate_usage),
        "reused_coordinate_count": sum(count >= 2 for count in coordinate_usage),
        "unused_coordinate_indices": [
            index for index, count in enumerate(coordinate_usage) if count == 0
        ],
        "all_discovered_pareto_single_coordinate": bool(pareto)
        and all(int(point["support_size"]) == 1 for point in pareto),
        "positive_weight_interface": {
            "generators": [list(vector) for vector in pareto_vectors],
            "truncated_price": "min_e sum_i w_i*e_i over the listed generators",
            "exact_for_all_positive_weights": globally_complete,
            "exactness_condition_if_truncated": (
                "listed minimum <= 10*min_i(w_i)"
                if pareto and not globally_complete
                else None
            ),
            "no_target_lower_bound_if_empty": (
                "Omega_w >= 10*min_i(w_i)" if not pareto else None
            ),
        },
        "pareto_vectors_through_cap": pareto,
    }


def run() -> dict[str, object]:
    input_hash = sha256(INPUT)
    source_hash = sha256(SOURCE_INPUT)
    if input_hash != EXPECTED_INPUT_SHA256:
        raise AssertionError("the lower-modulus split input changed")
    if source_hash != EXPECTED_SOURCE_SHA256:
        raise AssertionError("the frozen factorization input changed")

    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    source_payload = json.loads(SOURCE_INPUT.read_text(encoding="utf-8"))
    source_rows = {
        (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"])): dict(row)
        for row in source_payload["records"]
        if row.get("within_radius_cap")
    }

    profiles: list[dict[str, object]] = []
    for row in payload["records"]:
        key = (int(row["prime"]), int(row["R"]), tuple(row["witness_exponents"]))
        if key not in source_rows:
            raise AssertionError("a split row is missing its frozen factorization")
        factors = [
            (int(q), int(exponent))
            for q, exponent in source_rows[key]["factorization"]
        ]
        for candidate in row.get("candidates", []):
            if candidate.get("lower_modulus_classification") != "F_box_miss":
                continue
            profiles.append(
                state_profile(
                    prime=int(row["prime"]),
                    orientation=str(row["orientation"]),
                    original_R=int(row["R"]),
                    gap=int(candidate["gap"]),
                    modulus=int(candidate["balanced_t"]),
                    factors=factors,
                )
            )

    if len(profiles) != 42:
        raise AssertionError(f"unexpected lower-modulus F-box miss count: {len(profiles)}")

    unit_histogram = histogram(
        int(profile["unit_omega"])
        for profile in profiles
        if profile["unit_omega"] is not None
    )
    expected_unit_histogram = {
        "1": 12,
        "2": 8,
        "3": 2,
        "4": 4,
        "5": 2,
        "6": 2,
        "7": 2,
        "8": 3,
        "9": 1,
    }
    if unit_histogram != expected_unit_histogram:
        raise AssertionError("the independent unit-cost minima changed")

    pareto_points = [
        point
        for profile in profiles
        for point in profile["pareto_vectors_through_cap"]
    ]
    coordinate_usages = [
        int(count)
        for profile in profiles
        for count in profile["coordinate_usage_counts"]
    ]
    coordinate_records = sorted(
        (
            {
                "prime": int(profile["prime"]),
                "lower_modulus": int(profile["lower_modulus"]),
                "orientation": str(profile["orientation"]),
                "coordinate_index": index,
                "support_prime": int(profile["factorization"][index][0]),
                "pareto_usage_count": int(count),
                "state_pareto_vector_count": int(
                    profile["pareto_vector_count_through_cap"]
                ),
            }
            for profile in profiles
            for index, count in enumerate(profile["coordinate_usage_counts"])
            if int(count) > 0
        ),
        key=lambda record: (
            -int(record["pareto_usage_count"]),
            int(record["prime"]),
            int(record["lower_modulus"]),
            int(record["coordinate_index"]),
        ),
    )
    statuses = Counter(str(profile["frontier_status"]) for profile in profiles)
    by_orientation = {
        orientation: [
            profile for profile in profiles if profile["orientation"] == orientation
        ]
        for orientation in ("forward", "reverse")
    }
    return {
        "arithmetic": (
            "For each frozen lower-modulus F-box miss, exhaust every overflow vector "
            "e with |e|_1<=9 and decide exactly whether its exponent box meets the "
            "target fiber. Coordinatewise minimal hits form the exact portion of the "
            "global Pareto frontier within the cap."
        ),
        "scope_note": (
            "A point reported through unit cost 9 is globally Pareto minimal, because "
            "every possible dominator lies in the same exhaustive cap. Unless the "
            "cost-10 shell is covered by the discovered upward closure, additional "
            "incomparable Pareto points may exist beyond the cap. Empty truncated "
            "frontiers mean only Omega_1>=10, not an empty target fiber."
        ),
        "input": INPUT.name,
        "input_sha256": input_hash,
        "factorization_input": SOURCE_INPUT.name,
        "factorization_input_sha256": source_hash,
        "unit_overflow_cap": MAX_UNIT_OVERFLOW,
        "state_count": len(profiles),
        "frontier_status_counts": dict(sorted(statuses.items())),
        "globally_complete_state_count": sum(
            bool(profile["globally_complete"]) for profile in profiles
        ),
        "truncated_nonempty_state_count": statuses["truncated_nonempty"],
        "no_target_through_cap_state_count": statuses["no_target_through_cap"],
        "unit_omega_histogram": unit_histogram,
        "pareto_vector_count_through_cap": len(pareto_points),
        "distinct_support_count_through_cap": sum(
            int(profile["distinct_support_count"]) for profile in profiles
        ),
        "same_support_extra_pareto_vector_count": (
            len(pareto_points)
            - sum(int(profile["distinct_support_count"]) for profile in profiles)
        ),
        "states_with_repeated_support_count": sum(
            int(profile["pareto_vector_count_through_cap"])
            > int(profile["distinct_support_count"])
            for profile in profiles
        ),
        "pareto_count_per_state_histogram": histogram(
            int(profile["pareto_vector_count_through_cap"]) for profile in profiles
        ),
        "pareto_support_size_histogram": histogram(
            int(point["support_size"]) for point in pareto_points
        ),
        "single_coordinate_pareto_count": sum(
            int(point["support_size"]) == 1 for point in pareto_points
        ),
        "multi_coordinate_pareto_count": sum(
            int(point["support_size"]) >= 2 for point in pareto_points
        ),
        "states_with_single_coordinate_pareto_count": sum(
            int(profile["single_coordinate_pareto_count"]) > 0 for profile in profiles
        ),
        "states_with_only_single_coordinate_discovered_pareto_count": sum(
            bool(profile["all_discovered_pareto_single_coordinate"])
            for profile in profiles
        ),
        "states_with_multi_coordinate_pareto_count": sum(
            int(profile["multi_coordinate_pareto_count"]) > 0 for profile in profiles
        ),
        "state_coordinate_usage_histogram": histogram(coordinate_usages),
        "used_state_coordinate_count": sum(count > 0 for count in coordinate_usages),
        "reused_state_coordinate_count": sum(count >= 2 for count in coordinate_usages),
        "states_with_reused_coordinate_count": sum(
            int(profile["reused_coordinate_count"]) > 0 for profile in profiles
        ),
        "maximum_state_coordinate_usage_count": max(coordinate_usages, default=0),
        "most_reused_state_coordinates": coordinate_records[:12],
        "rank_histogram": histogram(int(profile["rank"]) for profile in profiles),
        "overflow_vectors_examined": sum(
            int(profile["overflow_vectors_examined"]) for profile in profiles
        ),
        "exponent_vectors_encoded": sum(
            int(profile["exponent_vectors_encoded"]) for profile in profiles
        ),
        "target_overflow_vector_count_through_cap": sum(
            int(profile["target_overflow_vector_count_through_cap"])
            for profile in profiles
        ),
        "globally_complete_states": [
            {
                "prime": profile["prime"],
                "lower_modulus": profile["lower_modulus"],
                "orientation": profile["orientation"],
            }
            for profile in profiles
            if profile["globally_complete"]
        ],
        "no_target_through_cap_states": [
            {
                "prime": profile["prime"],
                "lower_modulus": profile["lower_modulus"],
                "orientation": profile["orientation"],
                "unit_omega_lower_bound": profile["unit_omega_lower_bound"],
            }
            for profile in profiles
            if profile["frontier_status"] == "no_target_through_cap"
        ],
        "profiles_by_orientation": {
            orientation: {
                "state_count": len(rows),
                "globally_complete_state_count": sum(
                    bool(profile["globally_complete"]) for profile in rows
                ),
                "no_target_through_cap_state_count": sum(
                    profile["frontier_status"] == "no_target_through_cap"
                    for profile in rows
                ),
                "pareto_vector_count_through_cap": sum(
                    int(profile["pareto_vector_count_through_cap"])
                    for profile in rows
                ),
            }
            for orientation, rows in by_orientation.items()
        },
        "profiles": profiles,
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
                    "state_count",
                    "frontier_status_counts",
                    "unit_omega_histogram",
                    "pareto_vector_count_through_cap",
                    "pareto_count_per_state_histogram",
                    "pareto_support_size_histogram",
                    "single_coordinate_pareto_count",
                    "multi_coordinate_pareto_count",
                    "states_with_single_coordinate_pareto_count",
                    "states_with_reused_coordinate_count",
                    "globally_complete_state_count",
                    "no_target_through_cap_states",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
