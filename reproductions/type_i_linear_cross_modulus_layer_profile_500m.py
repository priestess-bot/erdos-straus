#!/usr/bin/env python3
"""Profile cross-modulus shared exponent layers in complete linear R spectra."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-global-linear-b1-failure-general-b-profile-500m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-cross-modulus-layer-profile-500m-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "9767df17ff2005153fcf559cb379bab03d7830809f57cdafe327c7f759ba3822"
)


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization_from_record(record: dict[str, object]) -> list[tuple[int, int]]:
    """Load and verify a stored prime factorization."""
    factors = sorted(
        (int(item["prime"]), int(item["exponent"]))
        for item in record["K_factorization"]
    )
    value = int(record["K"])
    if (
        not factors
        or math.prod(prime**exponent for prime, exponent in factors) != value
        or any(prime < 2 or exponent < 1 for prime, exponent in factors)
    ):
        raise AssertionError("stored K factorization is invalid")
    return factors


def factorization_payload(
    factors: Iterable[tuple[int, int]],
) -> list[dict[str, int]]:
    """Encode a checked factorization in the JSON artifact."""
    return [
        {"prime": int(prime), "exponent": int(exponent)}
        for prime, exponent in factors
    ]


def factorization_of_divisor(
    divisor: int, factors: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """Split a certified divisor using the factorization of its parent."""
    if divisor < 1:
        raise ValueError("divisor must be positive")
    remaining = divisor
    result = []
    for prime, exponent in factors:
        used = 0
        while remaining % prime == 0:
            remaining //= prime
            used += 1
        if used > exponent:
            raise AssertionError("divisor used an exponent outside its parent")
        if used:
            result.append((prime, used))
    if remaining != 1:
        raise AssertionError("divisor has a prime outside its parent")
    return result


def centered_square_spectrum(
    factors: list[tuple[int, int]], modulus: int
) -> set[int]:
    """Enumerate one exact centered square-divisor spectrum."""
    residues = {1}
    for prime, exponent in factors:
        powers = [
            pow(prime, coordinate, modulus)
            for coordinate in range(-exponent, exponent + 1)
        ]
        residues = {
            residue * power % modulus
            for residue in residues
            for power in powers
        }
    return residues


def minimum_support_by_residue(
    factors: list[tuple[int, int]], modulus: int
) -> dict[int, tuple[int, tuple[int, ...]]]:
    """Find the sparsest centered coordinate vector for every residue."""
    result: dict[int, tuple[int, tuple[int, ...]]] = {}
    for vector in itertools.product(
        *(range(-exponent, exponent + 1) for _, exponent in factors)
    ):
        residue = 1
        for (prime, _), coordinate in zip(factors, vector):
            residue = residue * pow(prime, coordinate, modulus) % modulus
        support = sum(coordinate != 0 for coordinate in vector)
        candidate = (support, vector)
        if residue not in result or candidate < result[residue]:
            result[residue] = candidate
    return result


def product_spectrum(
    left: set[int], right: set[int], modulus: int
) -> set[int]:
    """Return the product set of two residue spectra."""
    return {
        left_residue * right_residue % modulus
        for left_residue in left
        for right_residue in right
    }


def checked_records(
    profile: dict[str, object],
) -> list[dict[str, object]]:
    """Return source records ordered by their distinct induced modulus."""
    records = sorted(profile["records"], key=lambda record: int(record["R"]))
    moduli = [int(record["R"]) for record in records]
    if len(moduli) != len(set(moduli)) or any(modulus % 4 != 3 for modulus in moduli):
        raise AssertionError("linear source spectrum has malformed R values")
    for record in records:
        R = int(record["R"])
        K = int(record["K"])
        if 4 * K != int(profile["prime"]) * R + 1 or math.gcd(K, R) != 1:
            raise AssertionError("source record has malformed K")
        factorization_from_record(record)
    return records


def pairwise_gcd_identity(records: list[dict[str, object]]) -> None:
    """Verify gcd(K_R,K_R') = gcd(K_R, abs(R-R')/4) for every pair."""
    for left, right in itertools.combinations(records, 2):
        R_left = int(left["R"])
        R_right = int(right["R"])
        difference = abs(R_left - R_right)
        if difference == 0 or difference % 4:
            raise AssertionError("distinct linear source moduli must differ by four")
        exact = math.gcd(int(left["K"]), int(right["K"]))
        predicted = math.gcd(int(left["K"]), difference // 4)
        if exact != predicted:
            raise AssertionError("cross-modulus gcd identity failed")


def shared_difference_lcm(R: int, moduli: list[int]) -> int:
    """Return lcm_{R' != R} abs(R-R')/4."""
    result = 1
    for other in moduli:
        if other == R:
            continue
        difference = abs(R - other)
        if difference % 4:
            raise AssertionError("linear source differences must be multiples of four")
        result = math.lcm(result, difference // 4)
    return result


def classify_hit(
    record: dict[str, object], records: list[dict[str, object]]
) -> dict[str, object]:
    """Split one target hit into its shared and cross-modulus-excess layers."""
    R = int(record["R"])
    K = int(record["K"])
    factors = factorization_from_record(record)
    moduli = [int(other["R"]) for other in records]
    difference_lcm = shared_difference_lcm(R, moduli)
    shared_layer = math.gcd(K, difference_lcm)
    excess_layer = K // shared_layer

    pairwise_lcm = 1
    for other in records:
        if int(other["R"]) == R:
            continue
        pairwise_lcm = math.lcm(pairwise_lcm, math.gcd(K, int(other["K"])))
    if pairwise_lcm != shared_layer:
        raise AssertionError("shared layer does not match pairwise common factors")

    shared_factors = factorization_of_divisor(shared_layer, factors)
    excess_factors = factorization_of_divisor(excess_layer, factors)
    if (
        math.prod(prime**exponent for prime, exponent in shared_factors)
        != shared_layer
        or math.prod(prime**exponent for prime, exponent in excess_factors)
        != excess_layer
    ):
        raise AssertionError("layer factorization did not reconstruct")

    full_spectrum = centered_square_spectrum(factors, R)
    shared_spectrum = centered_square_spectrum(shared_factors, R)
    excess_spectrum = centered_square_spectrum(excess_factors, R)
    if full_spectrum != product_spectrum(shared_spectrum, excess_spectrum, R):
        raise AssertionError("centered spectrum did not split by exponent layers")

    target = R - 1
    if target not in full_spectrum:
        raise AssertionError("stored target hit disappeared")
    shared_hit = target in shared_spectrum
    excess_hit = target in excess_spectrum
    shared_costs = minimum_support_by_residue(shared_factors, R)
    excess_costs = minimum_support_by_residue(excess_factors, R)
    target_pairs = []
    for shared_residue, (shared_support, shared_vector) in shared_costs.items():
        required_excess = target * pow(shared_residue, -1, R) % R
        if required_excess in excess_costs:
            excess_support, excess_vector = excess_costs[required_excess]
            target_pairs.append(
                (
                    shared_support + excess_support,
                    excess_support,
                    shared_support,
                    shared_vector,
                    excess_vector,
                    shared_residue,
                    required_excess,
                )
            )
    if not target_pairs:
        raise AssertionError("centered spectrum target witness was lost")
    minimum_total = min(target_pairs)
    minimum_excess_support = min(pair[1] for pair in target_pairs)
    minimum_shared_support = min(pair[2] for pair in target_pairs)
    minimum_total_support = minimum_total[0]
    if shared_hit and excess_hit:
        classification = "both_layers_hit"
    elif shared_hit:
        classification = "shared_layer_hit"
    elif excess_hit:
        classification = "excess_layer_hit"
    else:
        classification = "mixed_layers_required"

    return {
        "R": R,
        "K": K,
        "shared_layer": shared_layer,
        "excess_layer": excess_layer,
        "K_factorization": factorization_payload(factors),
        "shared_layer_factorization": factorization_payload(shared_factors),
        "excess_layer_factorization": factorization_payload(excess_factors),
        "shared_layer_centered_spectrum_residue_count": len(shared_spectrum),
        "excess_layer_centered_spectrum_residue_count": len(excess_spectrum),
        "minus_one_in_shared_layer_spectrum": shared_hit,
        "minus_one_in_excess_layer_spectrum": excess_hit,
        "target_hit_cross_modulus_layer_classification": classification,
        "minimum_excess_layer_support": minimum_excess_support,
        "minimum_shared_layer_support": minimum_shared_support,
        "minimum_total_layer_support": minimum_total_support,
        "minimum_total_layer_witness": {
            "shared_coordinates": list(minimum_total[3]),
            "excess_coordinates": list(minimum_total[4]),
            "shared_residue": minimum_total[5],
            "excess_residue": minimum_total[6],
        },
    }


def run_audit(path: Path = INPUT) -> dict[str, object]:
    """Profile every stored general-B hit in the four complete source spectra."""
    if file_sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("upstream global obstruction profile hash changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    profiles = []
    aggregate = Counter()
    mixed_excess_support = Counter()
    for source_profile in payload["general_B_failure_profiles"]:
        records = checked_records(source_profile)
        pairwise_gcd_identity(records)
        hit_records = [
            classify_hit(record, records)
            for record in records
            if record["classification"] == "hit"
        ]
        local_counts = Counter(
            record["target_hit_cross_modulus_layer_classification"]
            for record in hit_records
        )
        aggregate.update(local_counts)
        for record in hit_records:
            if (
                record["target_hit_cross_modulus_layer_classification"]
                == "mixed_layers_required"
            ):
                mixed_excess_support[
                    str(record["minimum_excess_layer_support"])
                ] += 1
        profiles.append(
            {
                "prime": int(source_profile["prime"]),
                "complete_linear_R_count": len(records),
                "general_B_hit_R_count": len(hit_records),
                "cross_modulus_layer_classification_counts": dict(
                    sorted(local_counts.items())
                ),
                "records": hit_records,
            }
        )
    return {
        "arithmetic": (
            "for each fixed prime and every pair of induced linear moduli, verify "
            "gcd(K_R,K_R') = gcd(K_R, abs(R-R')/4); split each hit into the "
            "maximal pairwise-shared exponent layer and its complementary layer, "
            "then enumerate all centered square-divisor spectra exactly"
        ),
        "scope_note": (
            "This is a complete finite profile only for the four frozen global "
            "linear-B=1 failure primes and their complete linear R spectra. "
            "The cross-modulus layer identity is general, but this profile does "
            "not prove the universal selector."
        ),
        "input_artifact": path.name,
        "input_sha256": file_sha256(path),
        "aggregate_cross_modulus_layer_classification_counts": dict(
            sorted(aggregate.items())
        ),
        "mixed_layer_minimum_excess_support_counts": dict(
            sorted(mixed_excess_support.items())
        ),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "aggregate_cross_modulus_layer_classification_counts": result[
                    "aggregate_cross_modulus_layer_classification_counts"
                ]
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
