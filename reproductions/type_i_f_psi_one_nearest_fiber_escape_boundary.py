#!/usr/bin/env python3
"""Reproduce the complete nearest-fibre boundary for the 55 Psi_0=1 states."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path
import time

import sympy


ROOT = Path(__file__).resolve().parents[1]
INTRINSIC_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-private-carrier-selection-invariant-defect-results.json"
)
FOURIER_INPUT = (
    ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
)
SQUARE_INPUT = (
    ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"
)
SPECTRUM_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-psi-one-nearest-fiber-escape-boundary-results.json"
)

EXPECTED_INPUT_HASHES = {
    INTRINSIC_INPUT: "c3be0594411122823453d76f7065ce70eb83631f996b97d3a696f5119a0d5558",
    FOURIER_INPUT: "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d",
    SQUARE_INPUT: "ca3d74768cf90586834dfa7f8a127c760871cf5b5d27cc98be8ec96ec58dc9a1",
    SPECTRUM_INPUT: "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f",
}

EXPECTED_STATE_COUNT = 55
EXPECTED_POSITIVE_WITNESS_COUNT = 140
EXPECTED_DEFECT_COORDINATE_COUNT = 120
EXPECTED_RAW_GCD_ENDPOINT_COUNT = 1_214_833
EXPECTED_EXACT_GCD_ENDPOINT_COUNT = 881_472


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def histogram(values: list[int]) -> dict[str, int]:
    return {str(key): value for key, value in sorted(Counter(values).items())}


def factorization_dict(value: int) -> dict[str, int]:
    return {
        str(prime): int(exponent)
        for prime, exponent in sorted(sympy.factorint(value).items())
    }


def signed_product(
    primes: list[int], exponents: tuple[int, ...], modulus: int
) -> int:
    result = 1
    for prime, exponent in zip(primes, exponents):
        result = result * pow(prime, exponent, modulus) % modulus
    return result


def ratio_from_exponents(
    primes: list[int], exponents: tuple[int, ...]
) -> tuple[int, int]:
    numerator = math.prod(
        prime ** max(exponent, 0)
        for prime, exponent in zip(primes, exponents)
    )
    denominator = math.prod(
        prime ** max(-exponent, 0)
        for prime, exponent in zip(primes, exponents)
    )
    if math.gcd(numerator, denominator) != 1:
        raise AssertionError("signed exponent ratio was not reduced")
    return numerator, denominator


def minus_one_dyadic_exponent(modulus: int) -> int | None:
    residue = 1
    for exponent in range(1, 2 * modulus + 1):
        residue = 2 * residue % modulus
        if residue == modulus - 1:
            return exponent
        if residue == 1:
            return None
    raise AssertionError("dyadic order search exceeded the unit-group bound")


def direct_dyadic_terminals(
    prime: int,
    modulus: int,
    K: int,
    primes: list[int],
    bounds: list[int],
    witness: tuple[int, ...],
    defect_index: int,
) -> list[dict[str, int]]:
    sign = 1 if witness[defect_index] > 0 else -1
    clipped = list(witness)
    clipped[defect_index] -= sign
    if any(abs(value) > bound for value, bound in zip(clipped, bounds)):
        raise AssertionError("clipped unit witness did not enter the original box")
    numerator, denominator = ratio_from_exponents(primes, tuple(clipped))
    L = 2 * K
    terminals = []
    for left_scale, right_scale in ((1, 1), (2, 1), (1, 2)):
        a = left_scale * numerator
        b = right_scale * denominator
        if math.gcd(a, b) != 1 or L % a or L % b:
            continue
        alpha = valuation(a, 2)
        beta = valuation(b, 2)
        maximum_j = 1 + alpha - beta
        for dyadic_exponent in range(1, maximum_j + 1):
            if (a - pow(2, dyadic_exponent, modulus) * b) % modulus:
                continue
            if a >= (2**dyadic_exponent) * b:
                continue
            denominator_power = 2 ** (dyadic_exponent - 1)
            E_numerator = L * a
            E_denominator = denominator_power * b
            if E_numerator % E_denominator:
                raise AssertionError("dyadic terminal failed its integrality criterion")
            E = E_numerator // E_denominator
            source = (4 * K - E) // modulus
            if (
                E % 2
                or L * L % E
                or E % modulus != 1
                or not (0 < source < prime)
                or source % 2
            ):
                raise AssertionError("dyadic terminal reconstruction failed")
            terminals.append(
                {
                    "a": a,
                    "b": b,
                    "j": dyadic_exponent,
                    "E": E,
                    "source": source,
                }
            )
    return terminals


def positive_unit_witnesses(
    modulus: int, primes: list[int], bounds: list[int]
) -> list[dict[str, object]]:
    witnesses = []
    for defect_index, bound in enumerate(bounds):
        ranges: list[object] = [range(-value, value + 1) for value in bounds]
        ranges[defect_index] = (bound + 1,)
        for exponents in itertools.product(*ranges):
            vector = tuple(int(value) for value in exponents)
            if signed_product(primes, vector, modulus) != modulus - 1:
                continue
            if (
                sum(
                    max(0, abs(value) - box_bound)
                    for value, box_bound in zip(vector, bounds)
                )
                != 1
            ):
                raise AssertionError("one-layer shell produced a nonunit defect")
            witnesses.append(
                {
                    "defect_index": defect_index,
                    "defect_prime": primes[defect_index],
                    "exponents": vector,
                }
            )
    return witnesses


def migration_record(
    modulus: int,
    K: int,
    primes: list[int],
    witness: dict[str, object],
) -> dict[str, object]:
    defect_index = int(witness["defect_index"])
    defect_prime = int(witness["defect_prime"])
    exponents = tuple(int(value) for value in witness["exponents"])
    A, B = ratio_from_exponents(primes, exponents)
    m0, remainder = divmod(A + B, modulus)
    if remainder or A % defect_prime:
        raise AssertionError("positive unit witness did not have the expected orientation")
    shift = (-m0) % defect_prime
    if not (1 <= shift < defect_prime):
        raise AssertionError("migration shift ceased to be a q-adic unit")
    migrated_A = A // defect_prime
    migrated_B = (B + modulus * shift) // defect_prime
    migrated_m = (m0 + shift) // defect_prime
    if migrated_A + migrated_B != modulus * migrated_m:
        raise AssertionError("migration identity failed")
    divisor = math.gcd(migrated_A, migrated_B)
    reduced_A = migrated_A // divisor
    reduced_B = migrated_B // divisor
    reduced_m = migrated_m // divisor
    if (
        reduced_A + reduced_B != modulus * reduced_m
        or math.gcd(reduced_A, reduced_B) != 1
        or K % reduced_A
    ):
        raise AssertionError("reduced migration endpoint failed")
    external_factor = reduced_B // math.gcd(reduced_B, K)
    if external_factor <= 1:
        raise AssertionError("a Psi_0=1 migration unexpectedly returned to the K box")
    external_factorization = factorization_dict(external_factor)
    K_support = set(primes)
    old_support = {int(q) for q in external_factorization} & K_support
    new_support = {int(q) for q in external_factorization} - K_support
    if old_support and new_support:
        support_class = "mixed_old_support_excess_and_new_primes"
    elif new_support:
        support_class = "new_primes_only"
    else:
        support_class = "old_support_excess_only"
    return {
        "defect_index": defect_index,
        "defect_prime": defect_prime,
        "positive_exponents": list(exponents),
        "m0": m0,
        "shift": shift,
        "reduced_A": reduced_A,
        "reduced_B": reduced_B,
        "reduced_m": reduced_m,
        "m_strictly_decreased": reduced_m < m0,
        "external_factor": external_factor,
        "external_factorization": external_factorization,
        "external_distinct_prime_count": len(external_factorization),
        "external_support_class": support_class,
    }


def exact_gcd_type_ii_profile(
    prime: int,
    modulus: int,
    K: int,
    primes: list[int],
    witness: dict[str, object],
) -> dict[str, object]:
    defect_prime = int(witness["defect_prime"])
    positive_exponents = tuple(int(value) for value in witness["exponents"])
    negative_exponents = tuple(-value for value in positive_exponents)
    A, B = ratio_from_exponents(primes, negative_exponents)
    m0, remainder = divmod(A + B, modulus)
    if (
        remainder
        or B % defect_prime
        or math.gcd(A, B) != 1
        or B // math.gcd(B, K) != defect_prime
    ):
        raise AssertionError("negative unit witness did not have defect denominator q")
    b = B // defect_prime
    if K % b:
        raise AssertionError("one-layer reduction did not leave b inside K")
    s0 = (-A * pow(modulus, -1, defect_prime)) % defect_prime
    if not (1 <= s0 < defect_prime):
        raise AssertionError("fixed-B lift class was not a q-adic unit")
    a0 = (A + modulus * s0) // defect_prime
    r0 = (m0 + s0) // defect_prime
    if a0 + b != modulus * r0:
        raise AssertionError("fixed-B endpoint parametrization failed")
    maximum_a = (prime - 1) // (2 * b)
    minimum_t = (1 - a0 + modulus - 1) // modulus
    maximum_t = (maximum_a - a0) // modulus
    raw_count = max(0, maximum_t - minimum_t + 1)
    exact_count = 0
    type_ii_hits = []
    first_exact_endpoint = None
    for parameter in range(minimum_t, maximum_t + 1):
        a = a0 + modulus * parameter
        if not (1 <= a <= maximum_a):
            raise AssertionError("endpoint parameter escaped its size interval")
        if math.gcd(a, b) != 1:
            continue
        exact_count += 1
        M = 4 * a * b
        S = a + b
        if M <= S or M > 2 * prime - 2:
            raise AssertionError("Type II endpoint size reduction failed")
        h0 = (-prime) % M
        if not (1 <= h0 < M) or h0 % 4 != 3:
            raise AssertionError("unique Type II gap residue failed")
        endpoint = {
            "parameter": parameter,
            "a": a,
            "b": b,
            "sum": S,
            "modulus_4ab": M,
            "unique_h": h0,
        }
        if first_exact_endpoint is None:
            first_exact_endpoint = endpoint
        if S % h0:
            continue
        if not (3 <= h0 <= prime - 2) or (prime + h0) % M:
            raise AssertionError("Type II unique-gap criterion was inconsistent")
        C = (prime + h0) // M
        x = a * b * C
        smaller, larger = sorted((a, b))
        divisor = smaller * smaller * C
        if divisor > x or x * x % divisor or (x + divisor) % h0:
            raise AssertionError("Type II endpoint reconstruction failed")
        type_ii_hits.append({**endpoint, "C": C, "x": x, "divisor": divisor})
    return {
        "defect_prime": defect_prime,
        "negative_exponents": list(negative_exponents),
        "a0": a0,
        "b": b,
        "r0": r0,
        "minimum_t": minimum_t,
        "maximum_t": maximum_t,
        "maximum_a": maximum_a,
        "raw_size_endpoint_count": raw_count,
        "exact_gcd_endpoint_count": exact_count,
        "first_exact_endpoint": first_exact_endpoint,
        "type_ii_hits": type_ii_hits,
    }


def run() -> dict[str, object]:
    for path, expected_hash in EXPECTED_INPUT_HASHES.items():
        actual_hash = sha256(path)
        if actual_hash != expected_hash:
            raise AssertionError(
                f"frozen input changed: {path.name}: {actual_hash} != {expected_hash}"
            )
    intrinsic = json.loads(INTRINSIC_INPUT.read_text(encoding="utf-8"))
    fourier = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    square = json.loads(SQUARE_INPUT.read_text(encoding="utf-8"))
    spectrum = json.loads(SPECTRUM_INPUT.read_text(encoding="utf-8"))
    fourier_by_state = {
        (int(row["prime"]), int(row["R"])): row for row in fourier["records"]
    }
    square_by_state = {
        (int(row["prime"]), int(row["R"])): row
        for row in square["candidates"]
    }
    spectrum_by_prime = {
        int(profile["prime"]): profile for profile in spectrum["profiles"]
    }
    selected = [
        record
        for record in intrinsic["records"]
        if int(record["intrinsic_original_exponent_box"]["minimum_unit_residual"])
        == 1
    ]
    if len(selected) != EXPECTED_STATE_COUNT:
        raise AssertionError("Psi_0=1 state count changed")

    records = []
    all_positive_witnesses = []
    all_migrations = []
    all_gcd_profiles = []
    all_k2_candidates = []
    defect_coordinate_active = []
    defect_coordinate_owner_counts = []
    split_block_defects = []
    for record in selected:
        prime = int(record["prime"])
        modulus = int(record["R"])
        K = int(record["K"])
        key = (prime, modulus)
        factors = [
            (int(q), int(exponent)) for q, exponent in record["factorization"]
        ]
        primes = [q for q, _exponent in factors]
        bounds = [exponent for _q, exponent in factors]
        if (
            prime % 24 != 1
            or prime * modulus + 1 != 4 * K
            or math.gcd(K, modulus) != 1
            or K % 2 == 0
            or math.prod(q**e for q, e in factors) != K
        ):
            raise AssertionError("square-terminal K input changed")
        witnesses = positive_unit_witnesses(modulus, primes, bounds)
        if not witnesses:
            raise AssertionError("Psi_0=1 state had no positive shell witness")
        all_positive_witnesses.extend((key, witness) for witness in witnesses)
        defect_primes = sorted({int(row["defect_prime"]) for row in witnesses})
        witness_multiplicity = Counter(
            int(row["defect_prime"]) for row in witnesses
        )
        obstruction = record["intrinsic_original_exponent_box"][
            "minimum_projected_obstruction"
        ]
        obstruction_sets = [
            {int(q) for q in support}
            for support in obstruction["support_prime_sets"]
        ]
        if len(obstruction_sets) != 1:
            raise AssertionError("a Psi_0=1 minimum obstruction ceased to be unique")
        if any(
            not set(defect_primes) <= obstruction_set
            for obstruction_set in obstruction_sets
        ):
            raise AssertionError("D was not contained in a projected obstruction")
        J = sorted(obstruction_sets[0])

        active_fourier = {
            int(q) for q in fourier_by_state[key]["active_primes"]
        }
        square_row = square_by_state[key]
        active_square = {int(square_row["q_a"]), int(square_row["q_s"])}
        if active_fourier != active_square or len(active_fourier) != 2:
            raise AssertionError("the canonical two-active support changed")
        q_a = int(square_row["q_a"])
        q_s = int(square_row["q_s"])
        active_presence = {
            "q_a": q_a in defect_primes,
            "q_s": q_s in defect_primes,
        }
        for q in defect_primes:
            defect_coordinate_active.append(q in active_fourier)

        block_heights = [
            [int(value) for value in row]
            for row in record["source_block_q_heights"]
        ]
        owners = {}
        for index, q in enumerate(primes):
            if q not in defect_primes:
                continue
            owner_indices = [
                block_index
                for block_index in range(2)
                if block_heights[block_index][index] > 0
            ]
            owners[str(q)] = owner_indices
            defect_coordinate_owner_counts.append(len(owner_indices))
            if len(owner_indices) == 2:
                if [block_heights[row][index] for row in owner_indices] != [1, 1]:
                    raise AssertionError("a split defect coordinate ceased to have height [1,1]")
                split_block_defects.append(
                    {"prime": prime, "R": modulus, "q": q}
                )
        occupied_blocks = {
            owner for owner_indices in owners.values() for owner in owner_indices
        }

        dyadic_minus_one = minus_one_dyadic_exponent(modulus)
        direct_dyadic_hits = []
        migrations = []
        gcd_profiles = []
        for witness in witnesses:
            positive_vector = tuple(int(value) for value in witness["exponents"])
            reflected_vector = tuple(-value for value in positive_vector)
            for signed_vector in (positive_vector, reflected_vector):
                direct_dyadic_hits.extend(
                    direct_dyadic_terminals(
                        prime,
                        modulus,
                        K,
                        primes,
                        bounds,
                        signed_vector,
                        int(witness["defect_index"]),
                    )
                )
            migration = migration_record(modulus, K, primes, witness)
            migrations.append(migration)
            all_migrations.append((key, migration))
            gcd_profile = exact_gcd_type_ii_profile(
                prime, modulus, K, primes, witness
            )
            gcd_profiles.append(gcd_profile)
            all_gcd_profiles.append((key, gcd_profile))
        if direct_dyadic_hits:
            raise AssertionError("the direct clipped dyadic zero boundary changed")

        k2_candidates = []
        for q in defect_primes:
            if q % 32 != 23:
                continue
            h = (q + 1) // 8
            L = 2 * h - 1
            x = (prime + h) // 4
            if not (h % 4 == 3 and 3 <= h <= prime - 2):
                raise AssertionError("adjacent K=2 candidate left the natural gap range")
            candidate = {
                "prime": prime,
                "R": modulus,
                "q": q,
                "h": h,
                "L": L,
                "x_mod_L": x % L,
                "hit": x % L == 0,
            }
            k2_candidates.append(candidate)
            all_k2_candidates.append(candidate)

        exponent_by_q = dict(factors)
        q_lifts = {}
        for q in defect_primes:
            exponent = exponent_by_q[q]
            right = (
                -(4 * K // (q**exponent)) * pow(prime, -1, q)
            ) % q
            for row in spectrum_by_prime[prime]["records"]:
                delta = int(row["R"]) - modulus
                rhs_holds = (
                    delta % (q**exponent) == 0
                    and delta // (q**exponent) % q == right
                )
                lhs_holds = valuation(int(row["K"]), q) >= exponent + 1
                if lhs_holds != rhs_holds:
                    raise AssertionError("q-adic modulus lift equivalence failed")
            lifted_states = [
                row
                for row in spectrum_by_prime[prime]["records"]
                if int(row["R"]) != modulus
                and valuation(int(row["K"]), q) >= exponent + 1
            ]
            for lifted in lifted_states:
                delta = int(lifted["R"]) - modulus
                if delta % (q**exponent):
                    raise AssertionError("q-adic modulus lift missed its base layer")
                left = delta // (q**exponent) % q
                if left != right:
                    raise AssertionError("q-adic modulus lift residue changed")
            q_lifts[str(q)] = [
                {
                    "R": int(row["R"]),
                    "K": int(row["K"]),
                    "height": valuation(int(row["K"]), q),
                    "classification": str(row["classification"]),
                }
                for row in lifted_states
            ]

        records.append(
            {
                "prime": prime,
                "R": modulus,
                "K": K,
                "factorization": [[q, exponent] for q, exponent in factors],
                "positive_witness_count": len(witnesses),
                "signed_witness_count": 2 * len(witnesses),
                "positive_witness_multiplicity_by_q": {
                    str(q): int(value)
                    for q, value in sorted(witness_multiplicity.items())
                },
                "D": defect_primes,
                "J": J,
                "D_equals_J": defect_primes == J,
                "obstruction_dimension": len(J),
                "active_primes": sorted(active_fourier),
                "active_presence_in_D": active_presence,
                "D_intersects_active": bool(set(defect_primes) & active_fourier),
                "D_subset_active": set(defect_primes) <= active_fourier,
                "defect_prime_block_owners": owners,
                "D_occupied_block_count": len(occupied_blocks),
                "minus_one_dyadic_exponent": dyadic_minus_one,
                "direct_clipped_dyadic_hit_count": 0,
                "k2_candidates": k2_candidates,
                "migrations": migrations,
                "fixed_B_exact_gcd_profiles": gcd_profiles,
                "q_height_lifts": q_lifts,
            }
        )

    if len(all_positive_witnesses) != EXPECTED_POSITIVE_WITNESS_COUNT:
        raise AssertionError("positive shell witness count changed")
    defect_coordinate_count = sum(len(record["D"]) for record in records)
    if defect_coordinate_count != EXPECTED_DEFECT_COORDINATE_COUNT:
        raise AssertionError("defect-coordinate count changed")
    raw_endpoint_count = sum(
        int(profile["raw_size_endpoint_count"])
        for _key, profile in all_gcd_profiles
    )
    exact_endpoint_count = sum(
        int(profile["exact_gcd_endpoint_count"])
        for _key, profile in all_gcd_profiles
    )
    type_ii_hits = [
        hit
        for _key, profile in all_gcd_profiles
        for hit in profile["type_ii_hits"]
    ]
    if raw_endpoint_count != EXPECTED_RAW_GCD_ENDPOINT_COUNT:
        raise AssertionError("raw gcd endpoint count changed")
    if exact_endpoint_count != EXPECTED_EXACT_GCD_ENDPOINT_COUNT:
        raise AssertionError("exact gcd endpoint count changed")
    if type_ii_hits:
        raise AssertionError("fixed-B exact-gcd Type II zero boundary changed")

    multiplicities = [
        int(value)
        for record in records
        for value in record["positive_witness_multiplicity_by_q"].values()
    ]
    active_patterns = Counter(
        (
            bool(record["active_presence_in_D"]["q_a"]),
            bool(record["active_presence_in_D"]["q_s"]),
        )
        for record in records
    )
    migration_support_classes = Counter(
        str(migration["external_support_class"])
        for _key, migration in all_migrations
    )
    coordinate_has_q_lift = [
        bool(lifted)
        for record in records
        for lifted in record["q_height_lifts"].values()
    ]
    state_has_any_q_lift = [
        any(bool(lifted) for lifted in record["q_height_lifts"].values())
        for record in records
    ]
    state_has_all_q_lifts = [
        all(bool(lifted) for lifted in record["q_height_lifts"].values())
        for record in records
    ]
    state_has_exact_endpoint = [
        any(
            int(profile["exact_gcd_endpoint_count"]) > 0
            for profile in record["fixed_B_exact_gcd_profiles"]
        )
        for record in records
    ]
    summary = {
        "state_count": len(records),
        "positive_witness_count": len(all_positive_witnesses),
        "signed_witness_count": 2 * len(all_positive_witnesses),
        "signed_witness_count_per_state_histogram": histogram(
            [int(record["signed_witness_count"]) for record in records]
        ),
        "defect_coordinate_count": defect_coordinate_count,
        "positive_face_witness_multiplicity_histogram": histogram(multiplicities),
        "D_size_histogram": histogram([len(record["D"]) for record in records]),
        "obstruction_dimension_histogram": histogram(
            [int(record["obstruction_dimension"]) for record in records]
        ),
        "D_equals_J_count": sum(bool(record["D_equals_J"]) for record in records),
        "D_proper_subset_J_count": sum(
            not bool(record["D_equals_J"]) for record in records
        ),
        "J_minus_D_size_histogram": histogram(
            [len(record["J"]) - len(record["D"]) for record in records]
        ),
        "D_intersects_active_count": sum(
            bool(record["D_intersects_active"]) for record in records
        ),
        "D_disjoint_active_count": sum(
            not bool(record["D_intersects_active"]) for record in records
        ),
        "D_subset_active_count": sum(
            bool(record["D_subset_active"]) for record in records
        ),
        "active_defect_coordinate_count": sum(defect_coordinate_active),
        "nonactive_defect_coordinate_count": sum(
            not value for value in defect_coordinate_active
        ),
        "active_presence_pattern": {
            "both": active_patterns[(True, True)],
            "q_a_only": active_patterns[(True, False)],
            "q_s_only": active_patterns[(False, True)],
            "neither": active_patterns[(False, False)],
        },
        "single_block_defect_coordinate_count": sum(
            value == 1 for value in defect_coordinate_owner_counts
        ),
        "split_block_defect_coordinate_count": sum(
            value == 2 for value in defect_coordinate_owner_counts
        ),
        "split_block_defects": split_block_defects,
        "D_single_block_state_count": sum(
            int(record["D_occupied_block_count"]) == 1 for record in records
        ),
        "D_spans_blocks_state_count": sum(
            int(record["D_occupied_block_count"]) == 2 for record in records
        ),
        "minus_one_in_dyadic_subgroup_state_count": sum(
            record["minus_one_dyadic_exponent"] is not None for record in records
        ),
        "minus_one_outside_dyadic_subgroup_state_count": sum(
            record["minus_one_dyadic_exponent"] is None for record in records
        ),
        "direct_clipped_dyadic_hit_count": 0,
        "k2_candidate_count": len(all_k2_candidates),
        "k2_hit_count": sum(bool(row["hit"]) for row in all_k2_candidates),
        "k2_candidates": all_k2_candidates,
        "migration_strict_m_count": sum(
            bool(migration["m_strictly_decreased"])
            for _key, migration in all_migrations
        ),
        "migration_external_factor_gt_one_count": sum(
            int(migration["external_factor"]) > 1
            for _key, migration in all_migrations
        ),
        "migration_external_distinct_prime_count_histogram": histogram(
            [
                int(migration["external_distinct_prime_count"])
                for _key, migration in all_migrations
            ]
        ),
        "migration_state_with_single_external_prime_count": sum(
            any(
                int(migration["external_distinct_prime_count"]) == 1
                for migration in record["migrations"]
            )
            for record in records
        ),
        "migration_state_without_single_external_prime_count": sum(
            all(
                int(migration["external_distinct_prime_count"]) > 1
                for migration in record["migrations"]
            )
            for record in records
        ),
        "migration_external_support_class_histogram": dict(
            sorted(migration_support_classes.items())
        ),
        "q_height_lift_coordinate_count": sum(coordinate_has_q_lift),
        "q_height_no_lift_coordinate_count": sum(
            not value for value in coordinate_has_q_lift
        ),
        "q_height_any_lift_state_count": sum(state_has_any_q_lift),
        "q_height_all_lifts_state_count": sum(state_has_all_q_lifts),
        "q_height_no_lift_state_count": sum(
            not value for value in state_has_any_q_lift
        ),
        "fixed_B_raw_size_endpoint_count": raw_endpoint_count,
        "fixed_B_exact_gcd_endpoint_count": exact_endpoint_count,
        "fixed_B_raw_endpoint_witness_count": sum(
            int(profile["raw_size_endpoint_count"]) > 0
            for _key, profile in all_gcd_profiles
        ),
        "fixed_B_exact_endpoint_witness_count": sum(
            int(profile["exact_gcd_endpoint_count"]) > 0
            for _key, profile in all_gcd_profiles
        ),
        "fixed_B_exact_endpoint_state_count": sum(state_has_exact_endpoint),
        "fixed_B_no_exact_endpoint_state_count": sum(
            not value for value in state_has_exact_endpoint
        ),
        "fixed_B_type_ii_hit_count": 0,
    }
    expected_summary = {
        "signed_witness_count_per_state_histogram": {
            "2": 18,
            "4": 17,
            "6": 7,
            "8": 5,
            "10": 5,
            "12": 1,
            "14": 1,
            "18": 1,
        },
        "positive_face_witness_multiplicity_histogram": {
            "1": 103,
            "2": 14,
            "3": 3,
        },
        "D_size_histogram": {"1": 20, "2": 17, "3": 8, "4": 8, "5": 2},
        "obstruction_dimension_histogram": {
            "2": 9,
            "3": 4,
            "4": 16,
            "5": 12,
            "6": 12,
            "7": 2,
        },
        "J_minus_D_size_histogram": {
            "0": 11,
            "1": 9,
            "2": 13,
            "3": 10,
            "4": 7,
            "5": 3,
            "6": 2,
        },
        "migration_external_distinct_prime_count_histogram": {
            "1": 69,
            "2": 58,
            "3": 12,
            "4": 1,
        },
    }
    for field, expected in expected_summary.items():
        if summary[field] != expected:
            raise AssertionError(f"summary field changed: {field}")
    expected_scalars = {
        "D_equals_J_count": 11,
        "D_proper_subset_J_count": 44,
        "D_intersects_active_count": 49,
        "D_disjoint_active_count": 6,
        "D_subset_active_count": 28,
        "active_defect_coordinate_count": 73,
        "nonactive_defect_coordinate_count": 47,
        "single_block_defect_coordinate_count": 118,
        "split_block_defect_coordinate_count": 2,
        "D_single_block_state_count": 22,
        "D_spans_blocks_state_count": 33,
        "minus_one_in_dyadic_subgroup_state_count": 31,
        "minus_one_outside_dyadic_subgroup_state_count": 24,
        "k2_candidate_count": 6,
        "k2_hit_count": 0,
        "migration_strict_m_count": 140,
        "migration_external_factor_gt_one_count": 140,
        "migration_state_with_single_external_prime_count": 37,
        "migration_state_without_single_external_prime_count": 18,
        "q_height_lift_coordinate_count": 23,
        "q_height_no_lift_coordinate_count": 97,
        "q_height_any_lift_state_count": 19,
        "q_height_all_lifts_state_count": 4,
        "q_height_no_lift_state_count": 36,
        "fixed_B_raw_endpoint_witness_count": 85,
        "fixed_B_exact_endpoint_witness_count": 81,
        "fixed_B_exact_endpoint_state_count": 35,
        "fixed_B_no_exact_endpoint_state_count": 20,
        "fixed_B_type_ii_hit_count": 0,
    }
    for field, expected in expected_scalars.items():
        if summary[field] != expected:
            raise AssertionError(f"summary scalar changed: {field}")
    if summary["active_presence_pattern"] != {
        "both": 24,
        "q_a_only": 16,
        "q_s_only": 9,
        "neither": 6,
    }:
        raise AssertionError("active-presence pattern changed")
    if summary["migration_external_support_class_histogram"] != {
        "mixed_old_support_excess_and_new_primes": 7,
        "new_primes_only": 133,
    }:
        raise AssertionError("external-support class histogram changed")

    return {
        "arithmetic": (
            "Exhaust every one-layer target-fibre face for the 55 frozen Psi_0=1 "
            "states; compare all defect coordinates with minimum projected obstructions, "
            "canonical Fourier support and physical half-blocks; test direct clipped dyadic "
            "and q=8h-1 adjacent K=2 maps; reproduce the one-layer external-factor "
            "migration; enumerate every fixed-B exact-q gcd endpoint in the necessary "
            "Type II size range and test its unique possible gap; and inspect the complete "
            "same-prime linear spectrum for one additional q-adic K layer."
        ),
        "scope_note": (
            "Exact only for the frozen 55 states and the named maps. Zero hits do not rule "
            "out other dyadic embeddings, Type I/II certificates, nonminimum witnesses, "
            "changed denominators, or legal changes of R/K. No prime range is expanded."
        ),
        "inputs": {
            path.name: digest for path, digest in EXPECTED_INPUT_HASHES.items()
        },
        "summary": summary,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    started = time.perf_counter()
    result = run()
    elapsed = time.perf_counter() - started
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "state_count": result["summary"]["state_count"],
                "signed_witness_count": result["summary"]["signed_witness_count"],
                "exact_gcd_endpoint_count": result["summary"][
                    "fixed_B_exact_gcd_endpoint_count"
                ],
                "fixed_B_type_ii_hit_count": result["summary"][
                    "fixed_B_type_ii_hit_count"
                ],
                "elapsed_seconds": f"{elapsed:.6f}",
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
