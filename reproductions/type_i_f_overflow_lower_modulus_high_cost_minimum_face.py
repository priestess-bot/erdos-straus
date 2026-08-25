#!/usr/bin/env python3
"""Close and audit the six high-cost lower-modulus unit-minimum faces.

The target exponent coordinates are split in two.  Each half is enumerated only
through a frozen valid upper bound, and for every residue we retain every
exponent vector at its least half-cost.  Matching complementary residues then
recovers the complete global unit-minimum exponent face, not merely one witness
per overflow pattern.  A truncated generating function independently counts
every finite half-shell visited by the meet-in-the-middle table.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
sys.path.insert(0, str(REPRODUCTIONS))

import type_i_f_overflow_lower_modulus_min_overflow_shared_gap as shared_gap  # noqa: E402


PARETO_INPUT = (
    REPRODUCTIONS / "type-i-f-overflow-lower-modulus-pareto-overflow-results.json"
)
UPPER_INPUT = (
    REPRODUCTIONS / "type-i-f-overflow-lower-modulus-shortest-relation-results.json"
)
CAPACITY_INPUT = (
    REPRODUCTIONS / "type-i-f-overflow-lower-modulus-pareto-capacity-flow-results.json"
)
BASELINE_INPUT = (
    REPRODUCTIONS
    / "type_i_f_overflow_lower_modulus_min_overflow_shared_gap_results.json"
)
MINIMUM_SHARED_GAP_HELPER = (
    REPRODUCTIONS / "type_i_f_overflow_lower_modulus_min_overflow_shared_gap.py"
)
SHARED_GAP_HELPER = (
    REPRODUCTIONS / "type_i_f_overflow_lower_modulus_shared_gap_type_ii.py"
)
OUTPUT = (
    REPRODUCTIONS
    / "type-i-f-overflow-lower-modulus-high-cost-minimum-face-results.json"
)

EXPECTED_PARETO_SHA256 = "8fd82842893674641cf15928cf436d872e450b5fd175d47f8a825fad5603c6fe"
EXPECTED_UPPER_SHA256 = "077f565596f9f06e30aca5c7c6c6de487b455581f9e28801b84950531032ad42"
EXPECTED_CAPACITY_SHA256 = "993b3280dd8551e7c26bfbf9164f68172c87ac1412b6827c3bda8b44647b6cb4"
EXPECTED_BASELINE_SHA256 = "085a65615fcd2cc1e30330e4039483f36491871c41cad11d54123514a3f2852f"
EXPECTED_MINIMUM_SHARED_GAP_HELPER_SHA256 = (
    "5557ec9d3cc989a92e22d0e624f306c92d66184a854feb6ff45b4495ace10352"
)
EXPECTED_SHARED_GAP_HELPER_SHA256 = (
    "eb9905b8fb7428d0d8ce04fdf78f31e9ef937abb26b4fdc43bf93a39f7dc8802"
)

EXPECTED_OMEGA = {
    (62704849, "forward", 649): 12,
    (75056809, "reverse", 21113): 11,
    (310002289, "reverse", 107977): 18,
    (312918169, "forward", 16649): 10,
    (366108649, "forward", 11057): 12,
    (373561609, "forward", 208577): 15,
}

EXPECTED_HIT_GAPS = {
    (75056809, "reverse", 21113): (27, 59, 107, 215, 311, 1247),
    (310002289, "reverse", 107977): (19, 171),
    (312918169, "forward", 16649): (31, 47),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def state_key(profile: dict[str, object]) -> tuple[int, str, int, int, int]:
    return (
        int(profile["prime"]),
        str(profile["orientation"]),
        int(profile["original_R"]),
        int(profile["gap"]),
        int(profile["lower_modulus"]),
    )


def short_key(profile: dict[str, object]) -> tuple[int, str, int]:
    return (
        int(profile["prime"]),
        str(profile["orientation"]),
        int(profile["lower_modulus"]),
    )


def exact_overflow_vectors(bounds: tuple[int, ...], cost: int):
    """Yield every exponent vector of one exact unit-overflow cost."""
    vector = [0] * len(bounds)

    def visit(index: int, remaining: int):
        if index == len(bounds):
            if remaining == 0:
                yield tuple(vector)
            return
        bound = bounds[index]
        for exponent in range(-bound, bound + 1):
            vector[index] = exponent
            yield from visit(index + 1, remaining)
        for excess in range(1, remaining + 1):
            for exponent in (bound + excess, -bound - excess):
                vector[index] = exponent
                yield from visit(index + 1, remaining - excess)
        vector[index] = 0

    yield from visit(0, cost)


def shell_counts_from_generating_function(
    bounds: tuple[int, ...], maximum_cost: int
) -> list[int]:
    """Coefficients of prod_i((2*nu_i+1)+2*x/(1-x)) through the cap."""
    coefficients = [1] + [0] * maximum_cost
    for bound in bounds:
        coordinate = [2 * bound + 1] + [2] * maximum_cost
        updated = [0] * (maximum_cost + 1)
        for left_cost, left_count in enumerate(coefficients):
            for right_cost in range(maximum_cost - left_cost + 1):
                updated[left_cost + right_cost] += (
                    left_count * coordinate[right_cost]
                )
        coefficients = updated
    return coefficients


def relation_residue(
    factors: tuple[int, ...], modulus: int, exponents: tuple[int, ...]
) -> int:
    value = 1 % modulus
    for prime, exponent in zip(factors, exponents):
        base = prime if exponent >= 0 else pow(prime, -1, modulus)
        value = value * pow(base, abs(exponent), modulus) % modulus
    return value


def overflow_vector(
    exponents: tuple[int, ...], bounds: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(
        max(abs(exponent) - bound, 0)
        for exponent, bound in zip(exponents, bounds)
    )


def side_minimum_faces(
    factors: tuple[int, ...],
    bounds: tuple[int, ...],
    modulus: int,
    upper_bound: int,
) -> tuple[dict[int, tuple[int, list[tuple[int, ...]]]], dict[str, object]]:
    """Retain every least-cost exponent vector for every reached side residue."""
    minima: dict[int, tuple[int, list[tuple[int, ...]]]] = {}
    enumerated_shell_counts: list[int] = []
    for cost in range(upper_bound + 1):
        shell_count = 0
        for exponents in exact_overflow_vectors(bounds, cost):
            shell_count += 1
            residue = relation_residue(factors, modulus, exponents)
            prior = minima.get(residue)
            if prior is None:
                minima[residue] = (cost, [exponents])
            elif prior[0] == cost:
                prior[1].append(exponents)
        enumerated_shell_counts.append(shell_count)

    generating_counts = shell_counts_from_generating_function(bounds, upper_bound)
    if enumerated_shell_counts != generating_counts:
        raise AssertionError("side shell enumeration disagrees with its generating function")
    for cost, vectors in minima.values():
        if any(
            sum(overflow_vector(vector, bounds)) != cost for vector in vectors
        ):
            raise AssertionError("a side minimum face has the wrong unit cost")
    return minima, {
        "rank": len(factors),
        "residue_count": len(minima),
        "minimum_face_vector_count": sum(len(vectors) for _cost, vectors in minima.values()),
        "shell_counts": generating_counts,
        "generated_vector_count": sum(generating_counts),
    }


def complete_minimum_face(
    factors: tuple[int, ...],
    bounds: tuple[int, ...],
    modulus: int,
    upper_bound: int,
) -> tuple[int, list[tuple[int, ...]], dict[str, object]]:
    """Recover every global unit-minimum exponent vector by exact MITM."""
    split = len(factors) // 2
    left, left_audit = side_minimum_faces(
        factors[:split], bounds[:split], modulus, upper_bound
    )
    right, right_audit = side_minimum_faces(
        factors[split:], bounds[split:], modulus, upper_bound
    )

    target = modulus - 1
    best_cost = upper_bound + 1
    minimum_vectors: set[tuple[int, ...]] = set()
    matching_residue_pairs = 0
    for residue, (left_cost, left_vectors) in left.items():
        needed = target * pow(residue, -1, modulus) % modulus
        if needed not in right:
            continue
        right_cost, right_vectors = right[needed]
        cost = left_cost + right_cost
        if cost > best_cost:
            continue
        if cost < best_cost:
            best_cost = cost
            minimum_vectors.clear()
            matching_residue_pairs = 0
        matching_residue_pairs += 1
        for left_vector in left_vectors:
            for right_vector in right_vectors:
                minimum_vectors.add(left_vector + right_vector)

    if best_cost > upper_bound or not minimum_vectors:
        raise AssertionError("the valid upper bound did not close a minimum face")
    ordered = sorted(minimum_vectors)
    for vector in ordered:
        if relation_residue(factors, modulus, vector) != target:
            raise AssertionError("a reconstructed minimum vector lost the target residue")
        if sum(overflow_vector(vector, bounds)) != best_cost:
            raise AssertionError("a reconstructed minimum vector has the wrong cost")
    return best_cost, ordered, {
        "method": "all_side_minimizers_meet_in_the_middle",
        "valid_upper_bound": upper_bound,
        "split_index": split,
        "matching_residue_pair_count_at_minimum": matching_residue_pairs,
        "left": left_audit,
        "right": right_audit,
    }


def support_size_histogram(
    vectors: list[tuple[int, ...]], bounds: tuple[int, ...]
) -> dict[str, int]:
    return {
        str(size): count
        for size, count in sorted(
            Counter(
                sum(value > 0 for value in overflow_vector(vector, bounds))
                for vector in vectors
            ).items()
        )
    }


def certificate_identity(
    prime: int, gap: int, certificate: dict[str, int]
) -> tuple[int, ...]:
    return (
        prime,
        gap,
        int(certificate["divisor"]),
        int(certificate["A"]),
        int(certificate["B"]),
        int(certificate["C"]),
    )


def run() -> dict[str, object]:
    frozen_hashes = {
        "pareto_input_sha256": sha256(PARETO_INPUT),
        "upper_bound_input_sha256": sha256(UPPER_INPUT),
        "capacity_crosscheck_input_sha256": sha256(CAPACITY_INPUT),
        "baseline_input_sha256": sha256(BASELINE_INPUT),
        "minimum_shared_gap_helper_sha256": sha256(MINIMUM_SHARED_GAP_HELPER),
        "shared_gap_helper_sha256": sha256(SHARED_GAP_HELPER),
    }
    expected_hashes = {
        "pareto_input_sha256": EXPECTED_PARETO_SHA256,
        "upper_bound_input_sha256": EXPECTED_UPPER_SHA256,
        "capacity_crosscheck_input_sha256": EXPECTED_CAPACITY_SHA256,
        "baseline_input_sha256": EXPECTED_BASELINE_SHA256,
        "minimum_shared_gap_helper_sha256": EXPECTED_MINIMUM_SHARED_GAP_HELPER_SHA256,
        "shared_gap_helper_sha256": EXPECTED_SHARED_GAP_HELPER_SHA256,
    }
    if frozen_hashes != expected_hashes:
        raise AssertionError("a frozen high-cost minimum-face input changed")

    pareto_payload = json.loads(PARETO_INPUT.read_text(encoding="utf-8"))
    upper_payload = json.loads(UPPER_INPUT.read_text(encoding="utf-8"))
    capacity_payload = json.loads(CAPACITY_INPUT.read_text(encoding="utf-8"))
    baseline_payload = json.loads(BASELINE_INPUT.read_text(encoding="utf-8"))
    upper_by_key = {state_key(profile): profile for profile in upper_payload["profiles"]}
    capacity_by_key = {
        state_key(profile): profile for profile in capacity_payload["demand_profiles"]
    }

    high_profiles = [
        profile
        for profile in pareto_payload["profiles"]
        if profile["frontier_status"] == "no_target_through_cap"
    ]
    if len(high_profiles) != 6:
        raise AssertionError("the high-cost state count changed")
    high_keys = {state_key(profile) for profile in high_profiles}
    baseline_unresolved_keys = {
        state_key(profile) for profile in baseline_payload["unresolved_minimum_states"]
    }
    if high_keys != baseline_unresolved_keys:
        raise AssertionError("the high-cost states differ from the baseline unresolved set")
    baseline_record_keys = {state_key(record) for record in baseline_payload["records"]}
    if high_keys & baseline_record_keys:
        raise AssertionError("a high-cost state is already present in the resolved baseline")

    shared_gap.prime_certificates.clear()
    type_ii_cache: dict[tuple[int, int], list[dict[str, int]]] = {}
    records: list[dict[str, object]] = []
    new_global_sums: set[int] = set()
    new_certificate_identities: set[tuple[int, ...]] = set()

    for profile in high_profiles:
        key = state_key(profile)
        if key not in upper_by_key or key not in capacity_by_key:
            raise AssertionError("a high-cost state lacks an upper bound or cross-check")
        upper = upper_by_key[key]
        capacity = capacity_by_key[key]
        factors_with_bounds = tuple(
            (int(q), int(bound)) for q, bound in profile["factorization"]
        )
        factors = tuple(q for q, _bound in factors_with_bounds)
        bounds = tuple(bound for _q, bound in factors_with_bounds)
        modulus = int(profile["lower_modulus"])
        upper_vector = tuple(int(value) for value in upper["shortest_relation"])
        upper_bound = int(upper["overflow_layers"])
        if relation_residue(factors, modulus, upper_vector) != modulus - 1:
            raise AssertionError("the frozen upper-bound vector lost the target")
        if sum(overflow_vector(upper_vector, bounds)) != upper_bound:
            raise AssertionError("the frozen upper-bound cost changed")

        omega, minimum_vectors, mitm_audit = complete_minimum_face(
            factors, bounds, modulus, upper_bound
        )
        short = short_key(profile)
        if EXPECTED_OMEGA.get(short) != omega:
            raise AssertionError("a high-cost exact Omega_1 changed")
        if int(capacity["unit_omega"]) != omega:
            raise AssertionError("the capacity cross-check has a different Omega_1")

        minimum_set = set(minimum_vectors)
        for vector in minimum_vectors:
            if tuple(-value for value in vector) not in minimum_set:
                raise AssertionError("the minimum exponent face is not inversion closed")
        if len(minimum_vectors) % 2:
            raise AssertionError("an odd minimum-face size cannot pair by inversion")

        patterns: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
        for vector in minimum_vectors:
            patterns.setdefault(overflow_vector(vector, bounds), []).append(vector)
        if any(len(vectors) != 2 for vectors in patterns.values()):
            raise AssertionError("a high-cost overflow pattern is not one inversion pair")
        capacity_patterns = {
            tuple(int(value) for value in option["overflow_vector"]): tuple(
                int(value) for value in option["lexicographic_witness"]
            )
            for option in capacity["unit_optimal_pareto_options"]
        }
        if set(patterns) != set(capacity_patterns):
            raise AssertionError("the full face and capacity overflow patterns differ")
        for pattern, vectors in patterns.items():
            if min(vectors) != capacity_patterns[pattern]:
                raise AssertionError("the capacity pattern did not retain its lexicographic witness")

        sum_vectors: dict[int, list[tuple[int, ...]]] = {}
        for vector in minimum_vectors:
            numerator, denominator = shared_gap.rational_representation(
                list(factors), vector
            )
            total = numerator + denominator
            if total % modulus:
                raise AssertionError("a minimum-face sum lost lower-modulus divisibility")
            sum_vectors.setdefault(total, []).append(vector)
            new_global_sums.add(total)

        sum_profiles: list[dict[str, object]] = []
        all_candidate_gaps: set[int] = set()
        all_hit_gaps: set[int] = set()
        hit_vectors: set[tuple[int, ...]] = set()
        representation_gap_incidence_count = 0
        for total, vectors in sorted(sum_vectors.items()):
            factorization = shared_gap.certified_factorization(total)
            candidate_gaps = [
                divisor
                for divisor in shared_gap.divisors_from_factorization(list(factorization))
                if divisor % 4 == 3 and 3 <= divisor <= int(profile["prime"]) - 2
            ]
            representation_gap_incidence_count += len(vectors) * len(candidate_gaps)
            hit_gaps: list[int] = []
            hit_profiles: list[dict[str, object]] = []
            for candidate_gap in candidate_gaps:
                cache_key = (int(profile["prime"]), candidate_gap)
                if cache_key not in type_ii_cache:
                    certificates = shared_gap.type_ii_certificates(*cache_key)
                    shared_gap.verify_complete_type_ii_check(
                        cache_key[0], cache_key[1], certificates
                    )
                    type_ii_cache[cache_key] = certificates
                certificates = type_ii_cache[cache_key]
                if not certificates:
                    continue
                hit_gaps.append(candidate_gap)
                hit_profiles.append(
                    {
                        "gap": candidate_gap,
                        "type_ii_certificate_count": len(certificates),
                        "type_ii_certificates": certificates,
                    }
                )
                for certificate in certificates:
                    new_certificate_identities.add(
                        certificate_identity(
                            int(profile["prime"]), candidate_gap, certificate
                        )
                    )
            all_candidate_gaps.update(candidate_gaps)
            all_hit_gaps.update(hit_gaps)
            if hit_gaps:
                hit_vectors.update(vectors)
            sum_profiles.append(
                {
                    "sum": total,
                    "sum_factorization": [list(item) for item in factorization],
                    "minimum_vectors": [list(vector) for vector in sorted(vectors)],
                    "overflow_patterns": [
                        list(pattern)
                        for pattern in sorted(
                            {overflow_vector(vector, bounds) for vector in vectors}
                        )
                    ],
                    "candidate_gap_count": len(candidate_gaps),
                    "candidate_gaps": candidate_gaps,
                    "type_ii_hit_gaps": hit_gaps,
                    "hit_profiles": hit_profiles,
                }
            )
        if any(len(vectors) != 2 for vectors in sum_vectors.values()):
            raise AssertionError("a high-cost minimum sum is not one inversion pair")

        canonical_vector = minimum_vectors[0]
        canonical_total = sum(
            shared_gap.rational_representation(list(factors), canonical_vector)
        )
        canonical_profile = next(
            row for row in sum_profiles if int(row["sum"]) == canonical_total
        )
        hit_tuple = tuple(sorted(all_hit_gaps))
        state_scoped_certificate_count = sum(
            len(type_ii_cache[(int(profile["prime"]), gap)])
            for gap in all_hit_gaps
        )
        sum_scoped_certificate_incidence_count = sum(
            len(hit["type_ii_certificates"])
            for sum_profile in sum_profiles
            for hit in sum_profile["hit_profiles"]
        )
        if hit_tuple != EXPECTED_HIT_GAPS.get(short, ()):
            raise AssertionError("a high-cost shared-gap hit map changed")

        support_histogram = support_size_histogram(minimum_vectors, bounds)
        hit_support_histogram = support_size_histogram(sorted(hit_vectors), bounds)
        miss_support_histogram = support_size_histogram(
            sorted(minimum_set - hit_vectors), bounds
        )
        records.append(
            {
                "prime": int(profile["prime"]),
                "orientation": str(profile["orientation"]),
                "original_R": int(profile["original_R"]),
                "gap": int(profile["gap"]),
                "lower_modulus": modulus,
                "factorization": [list(item) for item in factors_with_bounds],
                "omega": omega,
                "valid_upper_bound": upper_bound,
                "upper_bound_vector": list(upper_vector),
                "mitm_audit": mitm_audit,
                "minimum_face_vector_count": len(minimum_vectors),
                "minimum_inverse_pair_count": len(minimum_vectors) // 2,
                "minimum_overflow_pattern_count": len(patterns),
                "unique_sum_count": len(sum_vectors),
                "minimum_face_vectors": [list(vector) for vector in minimum_vectors],
                "minimum_overflow_patterns": [
                    {
                        "overflow_vector": list(pattern),
                        "support_indices": [
                            index for index, value in enumerate(pattern) if value > 0
                        ],
                        "support_primes": [
                            factors[index]
                            for index, value in enumerate(pattern)
                            if value > 0
                        ],
                        "support_size": sum(value > 0 for value in pattern),
                        "exponent_vector_count": len(vectors),
                        "exponent_vectors": [list(vector) for vector in sorted(vectors)],
                    }
                    for pattern, vectors in sorted(patterns.items())
                ],
                "support_size_histogram": support_histogram,
                "single_support_vector_count": int(support_histogram.get("1", 0)),
                "double_support_vector_count": int(support_histogram.get("2", 0)),
                "three_or_more_support_vector_count": sum(
                    count
                    for size, count in ((int(k), int(v)) for k, v in support_histogram.items())
                    if size >= 3
                ),
                "canonical_vector": list(canonical_vector),
                "canonical_type_ii_hit": bool(canonical_profile["type_ii_hit_gaps"]),
                "canonical_type_ii_hit_gaps": canonical_profile["type_ii_hit_gaps"],
                "all_minimum_candidate_gap_count": len(all_candidate_gaps),
                "minimum_representation_gap_incidence_count": representation_gap_incidence_count,
                "all_minimum_type_ii_hit": bool(all_hit_gaps),
                "all_minimum_type_ii_hit_gaps": list(hit_tuple),
                "all_minimum_type_ii_certificate_count": state_scoped_certificate_count,
                "minimum_sum_scoped_type_ii_certificate_incidence_count": (
                    sum_scoped_certificate_incidence_count
                ),
                "minimum_face_hit_vector_count": len(hit_vectors),
                "type_ii_hit_support_size_histogram": hit_support_histogram,
                "type_ii_miss_support_size_histogram": miss_support_histogram,
                "entire_minimum_face_hits_type_ii": len(hit_vectors) == len(minimum_vectors),
                "sum_profiles": sum_profiles,
            }
        )

    records.sort(key=lambda row: short_key(row))
    if sum(int(row["minimum_face_vector_count"]) for row in records) != 36:
        raise AssertionError("the six-state minimum-face vector count changed")
    if sum(int(row["minimum_overflow_pattern_count"]) for row in records) != 18:
        raise AssertionError("the six-state minimum overflow-pattern count changed")

    new_support_histogram = Counter()
    new_hit_support_histogram = Counter()
    new_miss_support_histogram = Counter()
    for record in records:
        new_support_histogram.update(
            {
                int(size): int(count)
                for size, count in record["support_size_histogram"].items()
            }
        )
        new_hit_support_histogram.update(
            {
                int(size): int(count)
                for size, count in record["type_ii_hit_support_size_histogram"].items()
            }
        )
        new_miss_support_histogram.update(
            {
                int(size): int(count)
                for size, count in record["type_ii_miss_support_size_histogram"].items()
            }
        )
    if dict(sorted(new_support_histogram.items())) != {2: 12, 3: 12, 4: 12}:
        raise AssertionError("the high-cost support-size distribution changed")
    if dict(sorted(new_hit_support_histogram.items())) != {2: 2, 3: 8, 4: 10}:
        raise AssertionError("the high-cost hit-support distribution changed")
    if dict(sorted(new_miss_support_histogram.items())) != {2: 10, 3: 4, 4: 2}:
        raise AssertionError("the high-cost miss-support distribution changed")

    baseline_sums = {
        int(representation["sum"])
        for record in baseline_payload["records"]
        for representation in record["minimum_representations"]
    }
    baseline_candidate_pairs = {
        (int(record["prime"]), int(gap))
        for record in baseline_payload["records"]
        for representation in record["minimum_representations"]
        for gap in representation["candidate_gaps"]
    }
    new_candidate_pairs = {
        (int(record["prime"]), int(gap))
        for record in records
        for sum_profile in record["sum_profiles"]
        for gap in sum_profile["candidate_gaps"]
    }
    baseline_hit_pairs = {
        (int(record["prime"]), int(gap))
        for record in baseline_payload["records"]
        for gap in record["all_minimum_type_ii_hit_gaps"]
    }
    new_hit_pairs = {
        (int(record["prime"]), int(gap))
        for record in records
        for gap in record["all_minimum_type_ii_hit_gaps"]
    }
    baseline_certificate_identities = {
        certificate_identity(int(record["prime"]), int(hit["gap"]), certificate)
        for record in baseline_payload["records"]
        for hit in record["hit_profiles"]
        for certificate in hit["type_ii_certificates"]
    }

    combined_support = Counter()
    combined_hit_support = Counter()
    combined_miss_support = Counter()
    states_with_single_support = 0
    states_with_double_support = 0
    for record in baseline_payload["records"]:
        bounds = tuple(int(bound) for _q, bound in record["factorization"])
        sizes = [
            sum(
                value > 0
                for value in overflow_vector(
                    tuple(int(x) for x in representation["exponents"]), bounds
                )
            )
        for representation in record["minimum_representations"]
        ]
        combined_support.update(sizes)
        for representation, size in zip(record["minimum_representations"], sizes):
            target = (
                combined_hit_support
                if representation["type_ii_hit_gaps"]
                else combined_miss_support
            )
            target.update([size])
        states_with_single_support += int(1 in sizes)
        states_with_double_support += int(2 in sizes)
    for record in records:
        state_histogram = {
            int(size): int(count)
            for size, count in record["support_size_histogram"].items()
        }
        combined_support.update(state_histogram)
        combined_hit_support.update(
            {
                int(size): int(count)
                for size, count in record["type_ii_hit_support_size_histogram"].items()
            }
        )
        combined_miss_support.update(
            {
                int(size): int(count)
                for size, count in record["type_ii_miss_support_size_histogram"].items()
            }
        )
        states_with_single_support += int(state_histogram.get(1, 0) > 0)
        states_with_double_support += int(state_histogram.get(2, 0) > 0)

    high_hit_records = [record for record in records if record["all_minimum_type_ii_hit"]]
    high_canonical_hits = [record for record in records if record["canonical_type_ii_hit"]]
    high_tied_only = [
        record
        for record in records
        if record["all_minimum_type_ii_hit"] and not record["canonical_type_ii_hit"]
    ]
    combined_omega_histogram = {
        str(value): count
        for value, count in sorted(
            Counter(
                int(profile["unit_omega"])
                for profile in capacity_payload["demand_profiles"]
            ).items()
        )
    }
    lucas_certificates = sorted(
        (
            certificate
            for certificate in shared_gap.prime_certificates.values()
            if certificate["method"] == "recursive_Lucas_n_minus_one"
        ),
        key=lambda row: int(row["prime"]),
    )

    new_vector_count = sum(int(record["minimum_face_vector_count"]) for record in records)
    new_inverse_pair_count = sum(
        int(record["minimum_inverse_pair_count"]) for record in records
    )
    combined_state_count = int(baseline_payload["resolved_minimum_state_count"]) + len(records)
    combined = {
        "resolved_minimum_state_count": combined_state_count,
        "unresolved_minimum_state_count": 0,
        "minimum_vector_count": int(baseline_payload["minimum_vector_count"]) + new_vector_count,
        "minimum_inverse_pair_count": int(baseline_payload["minimum_inverse_pair_count"]) + new_inverse_pair_count,
        "per_state_unique_sum_count": int(baseline_payload["per_state_unique_sum_count"]) + sum(
            int(record["unique_sum_count"]) for record in records
        ),
        "globally_unique_sum_count": len(baseline_sums | new_global_sums),
        "canonical_state_hit_count": int(baseline_payload["canonical_state_hit_count"]) + len(high_canonical_hits),
        "all_minimum_state_hit_count": int(baseline_payload["all_minimum_state_hit_count"]) + len(high_hit_records),
        "tied_minimum_only_state_hit_count": int(baseline_payload["tied_minimum_only_state_hit_count"]) + len(high_tied_only),
        "minimum_layer_miss_count": combined_state_count - (
            int(baseline_payload["all_minimum_state_hit_count"]) + len(high_hit_records)
        ),
        "all_minimum_candidate_gap_count": int(baseline_payload["all_minimum_candidate_gap_count"]) + sum(
            int(record["all_minimum_candidate_gap_count"]) for record in records
        ),
        "minimum_representation_gap_incidence_count": int(
            baseline_payload["minimum_representation_gap_incidence_count"]
        ) + sum(
            int(record["minimum_representation_gap_incidence_count"])
            for record in records
        ),
        "distinct_prime_gap_check_count": len(baseline_candidate_pairs | new_candidate_pairs),
        "all_minimum_state_gap_hit_count": int(baseline_payload["all_minimum_state_gap_hit_count"]) + sum(
            len(record["all_minimum_type_ii_hit_gaps"]) for record in records
        ),
        "all_minimum_distinct_prime_gap_hit_count": len(baseline_hit_pairs | new_hit_pairs),
        "all_minimum_state_scoped_certificate_count": int(
            baseline_payload["all_minimum_state_scoped_certificate_count"]
        ) + sum(
            int(record["all_minimum_type_ii_certificate_count"])
            for record in records
        ),
        "all_minimum_distinct_certificate_count": len(
            baseline_certificate_identities | new_certificate_identities
        ),
        "minimum_face_support_size_histogram": {
            str(size): count for size, count in sorted(combined_support.items())
        },
        "type_ii_hit_support_size_histogram": {
            str(size): count for size, count in sorted(combined_hit_support.items())
        },
        "type_ii_miss_support_size_histogram": {
            str(size): count for size, count in sorted(combined_miss_support.items())
        },
        "states_with_single_support_minimum_count": states_with_single_support,
        "states_with_double_support_minimum_count": states_with_double_support,
        "omega_histogram": combined_omega_histogram,
    }

    return {
        "arithmetic": (
            "For each of the six former Omega_1>=10 states, use a frozen valid "
            "target relation as a finite upper bound. Split the exponent coordinates, "
            "retain every least-cost half-vector for every residue, and match "
            "complementary residues to recover the complete unit-minimum exponent face. "
            "Then factor every inversion-invariant a+b and exhaust all legal shared-gap "
            "Type II checks."
        ),
        "scope_note": (
            "This closes only the complete unit-weight minimum exponent face of six "
            "frozen lower-modulus F-box misses. It is not the full Pareto frontier and "
            "does not exclude higher-cost relations, other positive weights, factor "
            "redistribution, or non-shared-gap descents."
        ),
        "pareto_input": PARETO_INPUT.name,
        "upper_bound_input": UPPER_INPUT.name,
        "capacity_crosscheck_input": CAPACITY_INPUT.name,
        "baseline_input": BASELINE_INPUT.name,
        "minimum_shared_gap_helper": MINIMUM_SHARED_GAP_HELPER.name,
        "shared_gap_helper": SHARED_GAP_HELPER.name,
        **frozen_hashes,
        "high_cost_state_count": len(records),
        "minimum_vector_count": sum(int(record["minimum_face_vector_count"]) for record in records),
        "minimum_inverse_pair_count": sum(int(record["minimum_inverse_pair_count"]) for record in records),
        "minimum_overflow_pattern_count": sum(int(record["minimum_overflow_pattern_count"]) for record in records),
        "unique_sum_count": sum(int(record["unique_sum_count"]) for record in records),
        "omega_histogram": {
            str(value): count
            for value, count in sorted(Counter(int(record["omega"]) for record in records).items())
        },
        "support_size_histogram": {
            str(size): count for size, count in sorted(new_support_histogram.items())
        },
        "type_ii_hit_support_size_histogram": {
            str(size): count for size, count in sorted(new_hit_support_histogram.items())
        },
        "type_ii_miss_support_size_histogram": {
            str(size): count for size, count in sorted(new_miss_support_histogram.items())
        },
        "single_support_vector_count": new_support_histogram[1],
        "double_support_vector_count": new_support_histogram[2],
        "three_support_vector_count": new_support_histogram[3],
        "four_support_vector_count": new_support_histogram[4],
        "minimum_face_type_ii_hit_state_count": len(high_hit_records),
        "minimum_face_type_ii_miss_state_count": len(records) - len(high_hit_records),
        "canonical_type_ii_hit_state_count": len(high_canonical_hits),
        "tied_minimum_only_hit_state_count": len(high_tied_only),
        "entire_minimum_face_hit_state_count": sum(
            bool(record["entire_minimum_face_hits_type_ii"]) for record in records
        ),
        "minimum_face_hit_vector_count": sum(
            int(record["minimum_face_hit_vector_count"]) for record in records
        ),
        "all_minimum_state_gap_hit_count": sum(
            len(record["all_minimum_type_ii_hit_gaps"]) for record in records
        ),
        "state_scoped_type_ii_certificate_count": sum(
            int(record["all_minimum_type_ii_certificate_count"])
            for record in records
        ),
        "minimum_sum_scoped_type_ii_certificate_incidence_count": sum(
            int(record["minimum_sum_scoped_type_ii_certificate_incidence_count"])
            for record in records
        ),
        "distinct_type_ii_certificate_count": len(new_certificate_identities),
        "factorization_proof": {
            "method": (
                "Exact factorint reconstruction; trial-division primality leaves "
                f"through {shared_gap.TRIAL_PRIME_LIMIT}; recursive Lucas n-1 "
                "certificates above the leaf bound."
            ),
            "prime_certificate_count": len(shared_gap.prime_certificates),
            "trial_division_leaf_count": sum(
                certificate["method"] == "trial_division"
                for certificate in shared_gap.prime_certificates.values()
            ),
            "recursive_Lucas_certificate_count": len(lucas_certificates),
            "recursive_Lucas_certificates": lucas_certificates,
        },
        "combined_42_state_summary": combined,
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
                    "high_cost_state_count",
                    "minimum_vector_count",
                    "minimum_inverse_pair_count",
                    "minimum_overflow_pattern_count",
                    "support_size_histogram",
                    "minimum_face_type_ii_hit_state_count",
                    "minimum_face_type_ii_miss_state_count",
                    "canonical_type_ii_hit_state_count",
                    "entire_minimum_face_hit_state_count",
                    "minimum_face_hit_vector_count",
                    "all_minimum_state_gap_hit_count",
                    "state_scoped_type_ii_certificate_count",
                    "combined_42_state_summary",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
