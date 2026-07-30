#!/usr/bin/env python3
"""Audit shared-gap Type II lifts from every exact minimum-overflow relation.

For each of the 36 lower-modulus F-box misses whose unit-weight minimum is
known through the frozen finite search, this script re-enumerates the complete
minimum shell.  It distinguishes the lexicographic representative stored by
the weighted-cost profile from the union of all tied minimizers.

Every sum a+b is completely factored.  Primality of factors above a small
trial-division base is certified recursively with Lucas's n-1 criterion, so
the legal-divisor enumeration does not rest only on probable-prime tests.
Each candidate gap is then checked independently against the full Type II
normal form.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import cache
import hashlib
import json
import math
from pathlib import Path

from sympy import factorint

from type_i_f_overflow_lower_modulus_shared_gap_type_ii import (
    divisors_from_factorization,
    factorization as trial_factorization,
    type_ii_certificates,
)
from type_i_f_overflow_lower_modulus_weighted_cost import (
    exact_overflow_vectors,
    relation_residue,
)


ROOT = Path(__file__).resolve().parents[1]
WEIGHTED_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-overflow-lower-modulus-weighted-cost-results.json"
)
WEIGHTED_HELPER = (
    ROOT / "reproductions" / "type_i_f_overflow_lower_modulus_weighted_cost.py"
)
SHARED_GAP_HELPER = (
    ROOT
    / "reproductions"
    / "type_i_f_overflow_lower_modulus_shared_gap_type_ii.py"
)
OUTPUT = (
    ROOT
    / "reproductions"
    / "type_i_f_overflow_lower_modulus_min_overflow_shared_gap_results.json"
)

EXPECTED_WEIGHTED_INPUT_SHA256 = (
    "e4bffc9727821fcfd83a5ae0bb02b8d5326ac58a024563e0a9acdfa355fded82"
)
EXPECTED_WEIGHTED_HELPER_SHA256 = (
    "c06adb7b35929f801d3e5b91d3cf4bac15cd10b9446d1df8967d669ca67b7396"
)
EXPECTED_SHARED_GAP_HELPER_SHA256 = (
    "eb9905b8fb7428d0d8ce04fdf78f31e9ef937abb26b4fdc43bf93a39f7dc8802"
)

TRIAL_PRIME_LIMIT = 1_000_000
LUCAS_WITNESS_LIMIT = 10_000

EXPECTED_CANONICAL_HIT_GAPS = {
    (106050289, "forward", 97): (31,),
    (152498329, "reverse", 9377): (151,),
    (155533849, "forward", 89): (51,),
    (171292489, "forward", 1149): (383,),
    (171292489, "reverse", 2681): (383,),
    (236164009, "reverse", 2793): (171,),
    (331117609, "forward", 15413): (31,),
    (356491249, "reverse", 43865): (31,),
    (373561609, "reverse", 737): (51, 67),
    (408626089, "forward", 177): (59,),
    (473173969, "reverse", 32581): (31,),
    (507599689, "reverse", 813): (51,),
    (542688169, "reverse", 5617): (39,),
    (559650361, "reverse", 329): (47,),
}

EXPECTED_ALL_MINIMUM_HIT_GAPS = {
    (106050289, "forward", 97): (31,),
    (152498329, "reverse", 9377): (151,),
    (155533849, "forward", 89): (51,),
    (171292489, "forward", 1149): (115, 383),
    (171292489, "reverse", 2681): (383,),
    (223474729, "reverse", 233): (19, 63),
    (236164009, "reverse", 2793): (171,),
    (306963409, "forward", 125): (367,),
    (331117609, "forward", 15413): (31,),
    (356491249, "reverse", 43865): (31,),
    (373561609, "reverse", 737): (51, 67),
    (408626089, "forward", 177): (59,),
    (473173969, "reverse", 32581): (31,),
    (507599689, "reverse", 813): (51,),
    (542688169, "reverse", 5617): (39,),
    (549401449, "reverse", 617): (19, 27),
    (559650361, "reverse", 329): (47,),
    (570621769, "reverse", 113): (83, 87, 119, 1559),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trial_is_prime(value: int) -> bool:
    """Prove primality by trial division for a deliberately small leaf."""
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


@cache
def raw_factorization(value: int) -> tuple[tuple[int, int], ...]:
    """Factor an integer and verify exact reconstruction before certification."""
    if value <= 0:
        raise ValueError("factorization requires a positive integer")
    factors = tuple(
        sorted((int(prime), int(exponent)) for prime, exponent in factorint(value).items())
    )
    if math.prod(prime**exponent for prime, exponent in factors) != value:
        raise AssertionError("integer factorization did not reconstruct")
    return factors


prime_certificates: dict[int, dict[str, object]] = {}


def prove_prime(value: int) -> None:
    """Prove a factor prime using trial leaves and recursive Lucas certificates."""
    if value in prime_certificates:
        return
    if value <= TRIAL_PRIME_LIMIT:
        if not trial_is_prime(value):
            raise AssertionError(f"a reported factor is composite: {value}")
        prime_certificates[value] = {"prime": value, "method": "trial_division"}
        return

    factors = raw_factorization(value - 1)
    for prime, _exponent in factors:
        prove_prime(prime)

    witnesses: list[list[int]] = []
    for prime, _exponent in factors:
        witness = None
        for candidate in range(2, LUCAS_WITNESS_LIMIT + 1):
            if pow(candidate, value - 1, value) != 1:
                continue
            if math.gcd(pow(candidate, (value - 1) // prime, value) - 1, value) == 1:
                witness = candidate
                break
        if witness is None:
            raise AssertionError(
                f"no Lucas witness through {LUCAS_WITNESS_LIMIT} for {value}, q={prime}"
            )
        witnesses.append([prime, witness])

    # Complete factorization of value-1 plus one witness for every prime
    # divisor is Lucas's primality criterion.  All its prime divisors were
    # proved recursively above.
    prime_certificates[value] = {
        "prime": value,
        "method": "recursive_Lucas_n_minus_one",
        "n_minus_one_factorization": [list(item) for item in factors],
        "witnesses": witnesses,
    }


def certified_factorization(value: int) -> tuple[tuple[int, int], ...]:
    factors = raw_factorization(value)
    for prime, _exponent in factors:
        prove_prime(prime)
    return factors


def rational_representation(
    factors: list[int], vector: tuple[int, ...]
) -> tuple[int, int]:
    numerator = 1
    denominator = 1
    for prime, exponent in zip(factors, vector):
        if exponent >= 0:
            numerator *= prime**exponent
        else:
            denominator *= prime ** (-exponent)
    if math.gcd(numerator, denominator) != 1:
        raise AssertionError("signed prime exponents did not give a reduced fraction")
    return numerator, denominator


def verify_complete_type_ii_check(
    prime: int, gap: int, certificates: list[dict[str, int]]
) -> None:
    """Compare the helper result with the full admissible divisor set."""
    if prime % 4 != 1 or gap % 4 != 3 or not 3 <= gap <= prime - 2:
        raise AssertionError("illegal Type II gap reached the verifier")
    x = (prime + gap) // 4
    expected_divisors = [
        divisor
        for divisor in divisors_from_factorization(
            trial_factorization(x), square=True
        )
        if divisor <= x and (x * x) % divisor == 0 and (x + divisor) % gap == 0
    ]
    reported_divisors = sorted(int(row["divisor"]) for row in certificates)
    if reported_divisors != expected_divisors:
        raise AssertionError("Type II helper did not enumerate the full divisor set")

    for row in certificates:
        a = int(row["A"])
        b = int(row["B"])
        c = int(row["C"])
        divisor = int(row["divisor"])
        if math.gcd(a, b) != 1 or a > b:
            raise AssertionError("Type II normal form lost coprimality or order")
        if x != a * b * c or divisor != a * a * c or (a + b) % gap:
            raise AssertionError("Type II normal form did not reconstruct")
        y = prime * (x + divisor) // gap
        z = prime * (x + x * x // divisor) // gap
        if Fraction(4, prime) != Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
            raise AssertionError("Type II unit-fraction identity failed")


def histogram(rows: list[dict[str, object]], field: str) -> dict[str, int]:
    return {
        str(value): count
        for value, count in sorted(Counter(int(row[field]) for row in rows).items())
    }


def run() -> dict[str, object]:
    weighted_sha = sha256(WEIGHTED_INPUT)
    weighted_helper_sha = sha256(WEIGHTED_HELPER)
    shared_gap_helper_sha = sha256(SHARED_GAP_HELPER)
    if weighted_sha != EXPECTED_WEIGHTED_INPUT_SHA256:
        raise AssertionError("the frozen weighted-cost input changed")
    if weighted_helper_sha != EXPECTED_WEIGHTED_HELPER_SHA256:
        raise AssertionError("the weighted-shell helper changed")
    if shared_gap_helper_sha != EXPECTED_SHARED_GAP_HELPER_SHA256:
        raise AssertionError("the Type II shared-gap helper changed")

    payload = json.loads(WEIGHTED_INPUT.read_text(encoding="utf-8"))
    type_ii_cache: dict[tuple[int, int], list[dict[str, int]]] = {}
    sum_factorization_cache: dict[int, tuple[tuple[int, int], ...]] = {}
    records: list[dict[str, object]] = []
    unresolved: list[dict[str, object]] = []
    global_sums: set[int] = set()

    for profile in payload["profiles"]:
        omega = profile["omega_secondary"]
        if omega is None:
            unresolved.append(
                {
                    "prime": int(profile["prime"]),
                    "orientation": profile["orientation"],
                    "original_R": int(profile["original_R"]),
                    "gap": int(profile["gap"]),
                    "lower_modulus": int(profile["lower_modulus"]),
                    "omega_lower_bound": int(profile["secondary_lower_bound"]),
                }
            )
            continue

        prime = int(profile["prime"])
        orientation = str(profile["orientation"])
        lower_modulus = int(profile["lower_modulus"])
        factorization_data = [
            (int(q), int(exponent)) for q, exponent in profile["factorization"]
        ]
        factors = [q for q, _exponent in factorization_data]
        bounds = [exponent for _q, exponent in factorization_data]

        representations: list[dict[str, object]] = []
        for vector in exact_overflow_vectors(bounds, int(omega)):
            if relation_residue(factors, lower_modulus, vector) != lower_modulus - 1:
                continue
            numerator, denominator = rational_representation(factors, vector)
            total = numerator + denominator
            if total % lower_modulus:
                raise AssertionError("minimum relation did not descend to a divisible sum")
            if total not in sum_factorization_cache:
                sum_factorization_cache[total] = certified_factorization(total)
            total_factors = sum_factorization_cache[total]
            candidate_gaps = [
                divisor
                for divisor in divisors_from_factorization(list(total_factors))
                if divisor % 4 == 3 and 3 <= divisor <= prime - 2
            ]
            hit_gaps: list[int] = []
            for candidate_gap in candidate_gaps:
                key = (prime, candidate_gap)
                if key not in type_ii_cache:
                    certificates = type_ii_certificates(prime, candidate_gap)
                    verify_complete_type_ii_check(prime, candidate_gap, certificates)
                    type_ii_cache[key] = certificates
                if type_ii_cache[key]:
                    hit_gaps.append(candidate_gap)
            global_sums.add(total)
            representations.append(
                {
                    "exponents": list(vector),
                    "a": numerator,
                    "b": denominator,
                    "sum": total,
                    "sum_factorization": [list(item) for item in total_factors],
                    "candidate_gap_count": len(candidate_gaps),
                    "candidate_gaps": candidate_gaps,
                    "type_ii_hit_gaps": hit_gaps,
                }
            )

        representations.sort(key=lambda row: tuple(int(x) for x in row["exponents"]))
        canonical_vector = tuple(int(x) for x in profile["omega_secondary_vector"])
        if not representations or tuple(representations[0]["exponents"]) != canonical_vector:
            raise AssertionError("the frozen lexicographic representative was not reproduced")

        vectors = {tuple(int(x) for x in row["exponents"]) for row in representations}
        sums_by_vector = {
            tuple(int(x) for x in row["exponents"]): int(row["sum"])
            for row in representations
        }
        for vector in vectors:
            inverse = tuple(-entry for entry in vector)
            if inverse not in vectors or sums_by_vector[inverse] != sums_by_vector[vector]:
                raise AssertionError("minimum fiber was not closed under inversion")

        canonical = representations[0]
        all_candidate_gaps = sorted(
            {
                int(gap)
                for representation in representations
                for gap in representation["candidate_gaps"]
            }
        )
        all_hit_gaps = [
            gap for gap in all_candidate_gaps if type_ii_cache[(prime, gap)]
        ]
        canonical_hit_gaps = [int(gap) for gap in canonical["type_ii_hit_gaps"]]

        hit_profiles: list[dict[str, object]] = []
        for hit_gap in all_hit_gaps:
            matching_vectors = [
                row["exponents"]
                for row in representations
                if hit_gap in row["candidate_gaps"]
            ]
            hit_profiles.append(
                {
                    "gap": hit_gap,
                    "canonical_vector_matches": hit_gap in canonical["candidate_gaps"],
                    "matching_minimum_vector_count": len(matching_vectors),
                    "matching_minimum_vectors": matching_vectors,
                    "type_ii_certificate_count": len(type_ii_cache[(prime, hit_gap)]),
                    "type_ii_certificates": type_ii_cache[(prime, hit_gap)],
                }
            )

        unique_sums = {int(row["sum"]) for row in representations}
        if len(representations) != 2 * len(unique_sums):
            raise AssertionError("the frozen minimum representations did not pair by inversion")
        records.append(
            {
                "prime": prime,
                "orientation": orientation,
                "original_R": int(profile["original_R"]),
                "gap": int(profile["gap"]),
                "lower_modulus": lower_modulus,
                "factorization": [list(item) for item in factorization_data],
                "omega": int(omega),
                "canonical_vector": list(canonical_vector),
                "minimum_vector_count": len(representations),
                "minimum_inverse_pair_count": len(representations) // 2,
                "unique_sum_count": len(unique_sums),
                "canonical_candidate_gap_count": int(canonical["candidate_gap_count"]),
                "canonical_type_ii_hit": bool(canonical_hit_gaps),
                "canonical_type_ii_hit_gaps": canonical_hit_gaps,
                "all_minimum_candidate_gap_count": len(all_candidate_gaps),
                "all_minimum_type_ii_hit": bool(all_hit_gaps),
                "all_minimum_type_ii_hit_gaps": all_hit_gaps,
                "tied_minimum_only_hit": bool(all_hit_gaps) and not bool(canonical_hit_gaps),
                "all_minimum_type_ii_certificate_count": sum(
                    len(type_ii_cache[(prime, gap)]) for gap in all_hit_gaps
                ),
                "hit_profiles": hit_profiles,
                "minimum_representations": representations,
            }
        )

    records.sort(
        key=lambda row: (
            int(row["prime"]),
            str(row["orientation"]),
            int(row["lower_modulus"]),
        )
    )
    unresolved.sort(
        key=lambda row: (
            int(row["prime"]),
            str(row["orientation"]),
            int(row["lower_modulus"]),
        )
    )

    canonical_hit_map = {
        (
            int(row["prime"]),
            str(row["orientation"]),
            int(row["lower_modulus"]),
        ): tuple(
            int(gap) for gap in row["canonical_type_ii_hit_gaps"]
        )
        for row in records
        if row["canonical_type_ii_hit"]
    }
    all_hit_map = {
        (
            int(row["prime"]),
            str(row["orientation"]),
            int(row["lower_modulus"]),
        ): tuple(
            int(gap) for gap in row["all_minimum_type_ii_hit_gaps"]
        )
        for row in records
        if row["all_minimum_type_ii_hit"]
    }
    if canonical_hit_map != EXPECTED_CANONICAL_HIT_GAPS:
        raise AssertionError("canonical minimum shared-gap hit map changed")
    if all_hit_map != EXPECTED_ALL_MINIMUM_HIT_GAPS:
        raise AssertionError("all-minimum shared-gap hit map changed")

    if len(records) != 36 or len(unresolved) != 6:
        raise AssertionError("weighted-cost resolution split changed")
    if sum(int(row["minimum_vector_count"]) for row in records) != 204:
        raise AssertionError("minimum-vector count changed")
    if sum(int(row["unique_sum_count"]) for row in records) != 102:
        raise AssertionError("per-state minimum-sum count changed")
    if len(global_sums) != 101:
        raise AssertionError("global minimum-sum count changed")

    canonical_state_hits = [row for row in records if row["canonical_type_ii_hit"]]
    all_state_hits = [row for row in records if row["all_minimum_type_ii_hit"]]
    tied_only_hits = [row for row in records if row["tied_minimum_only_hit"]]
    distinct_certificate_count = sum(
        len(certificates) for certificates in type_ii_cache.values() if certificates
    )
    state_scoped_certificate_count = sum(
        int(row["all_minimum_type_ii_certificate_count"]) for row in records
    )
    lucas_certificates = sorted(
        (
            certificate
            for certificate in prime_certificates.values()
            if certificate["method"] == "recursive_Lucas_n_minus_one"
        ),
        key=lambda row: int(row["prime"]),
    )

    return {
        "arithmetic": (
            "For every resolved Omega_1 state, enumerate the full exact minimum shell. "
            "Write each relation as a reduced a/b with a+b divisible by the lower modulus; "
            "enumerate every legal h dividing a+b, then independently enumerate all Type II "
            "normal-form divisors for x_h=(p+h)/4."
        ),
        "scope_note": (
            "The complete minimum fiber is known only for 36 of 42 frozen F-box misses. "
            "The six states with Omega_1>=10 remain unresolved and are excluded from the "
            "coverage denominator. A miss here excludes only the exact minimum-overflow "
            "fiber, not higher-overflow relations, factor redistribution, or other descents."
        ),
        "weighted_input": WEIGHTED_INPUT.name,
        "weighted_input_sha256": weighted_sha,
        "weighted_helper": WEIGHTED_HELPER.name,
        "weighted_helper_sha256": weighted_helper_sha,
        "shared_gap_helper": SHARED_GAP_HELPER.name,
        "shared_gap_helper_sha256": shared_gap_helper_sha,
        "frozen_state_count": len(records) + len(unresolved),
        "resolved_minimum_state_count": len(records),
        "resolved_minimum_prime_count": len({int(row["prime"]) for row in records}),
        "unresolved_minimum_state_count": len(unresolved),
        "minimum_vector_count": sum(int(row["minimum_vector_count"]) for row in records),
        "minimum_inverse_pair_count": sum(
            int(row["minimum_inverse_pair_count"]) for row in records
        ),
        "per_state_unique_sum_count": sum(int(row["unique_sum_count"]) for row in records),
        "globally_unique_sum_count": len(global_sums),
        "canonical_candidate_gap_count": sum(
            int(row["canonical_candidate_gap_count"]) for row in records
        ),
        "all_minimum_candidate_gap_count": sum(
            int(row["all_minimum_candidate_gap_count"]) for row in records
        ),
        "minimum_representation_gap_incidence_count": sum(
            int(representation["candidate_gap_count"])
            for row in records
            for representation in row["minimum_representations"]
        ),
        "distinct_prime_gap_check_count": len(type_ii_cache),
        "canonical_state_hit_count": len(canonical_state_hits),
        "canonical_prime_hit_count": len(
            {int(row["prime"]) for row in canonical_state_hits}
        ),
        "canonical_state_gap_hit_count": sum(
            len(row["canonical_type_ii_hit_gaps"]) for row in records
        ),
        "canonical_state_scoped_certificate_count": sum(
            sum(
                len(type_ii_cache[(int(row["prime"]), int(gap))])
                for gap in row["canonical_type_ii_hit_gaps"]
            )
            for row in records
        ),
        "all_minimum_state_hit_count": len(all_state_hits),
        "all_minimum_prime_hit_count": len({int(row["prime"]) for row in all_state_hits}),
        "all_minimum_state_gap_hit_count": sum(
            len(row["all_minimum_type_ii_hit_gaps"]) for row in records
        ),
        "all_minimum_distinct_prime_gap_hit_count": sum(
            bool(certificates) for certificates in type_ii_cache.values()
        ),
        "all_minimum_state_scoped_certificate_count": state_scoped_certificate_count,
        "all_minimum_distinct_certificate_count": distinct_certificate_count,
        "tied_minimum_only_state_hit_count": len(tied_only_hits),
        "resolved_minimum_layer_miss_count": len(records) - len(all_state_hits),
        "resolved_omega_histogram": histogram(records, "omega"),
        "canonical_hit_omega_histogram": histogram(canonical_state_hits, "omega"),
        "all_minimum_hit_omega_histogram": histogram(all_state_hits, "omega"),
        "profiles_by_orientation": {
            orientation: {
                "resolved_state_count": sum(
                    row["orientation"] == orientation for row in records
                ),
                "canonical_state_hit_count": sum(
                    row["orientation"] == orientation and row["canonical_type_ii_hit"]
                    for row in records
                ),
                "all_minimum_state_hit_count": sum(
                    row["orientation"] == orientation and row["all_minimum_type_ii_hit"]
                    for row in records
                ),
            }
            for orientation in ("forward", "reverse")
        },
        "factorization_proof": {
            "method": (
                "Exact factorint reconstruction; trial-division primality leaves through "
                f"{TRIAL_PRIME_LIMIT}; recursive Lucas n-1 certificates above the leaf bound."
            ),
            "prime_certificate_count": len(prime_certificates),
            "trial_division_leaf_count": sum(
                row["method"] == "trial_division" for row in prime_certificates.values()
            ),
            "recursive_Lucas_certificate_count": len(lucas_certificates),
            "recursive_Lucas_certificates": lucas_certificates,
        },
        "tied_minimum_only_hits": [
            {
                "prime": row["prime"],
                "orientation": row["orientation"],
                "lower_modulus": row["lower_modulus"],
                "omega": row["omega"],
                "all_minimum_type_ii_hit_gaps": row["all_minimum_type_ii_hit_gaps"],
            }
            for row in tied_only_hits
        ],
        "unresolved_minimum_states": unresolved,
        "records": records,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "frozen_state_count",
                    "resolved_minimum_state_count",
                    "unresolved_minimum_state_count",
                    "minimum_vector_count",
                    "minimum_inverse_pair_count",
                    "all_minimum_candidate_gap_count",
                    "distinct_prime_gap_check_count",
                    "canonical_state_hit_count",
                    "all_minimum_state_hit_count",
                    "tied_minimum_only_state_hit_count",
                    "resolved_minimum_layer_miss_count",
                    "all_minimum_state_gap_hit_count",
                    "all_minimum_state_scoped_certificate_count",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
