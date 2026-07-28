#!/usr/bin/env python3
"""Extend cross-modulus exponent-layer profiling to seven full linear spectra."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"
)
LAYER_SCRIPT = ROOT / "reproductions" / "type_i_linear_cross_modulus_layer_profile_500m.py"
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-cross-modulus-layer-profile-600m-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "dce587d6e6703e5cdcb81b6cd05c16989394a7321d2d14515ea2eda6c2aec44d"
)
EXPECTED_PER_PRIME_COUNTS = {
    214_729: {"mixed_layers_required": 3},
    878_089: {"shared_layer_hit": 1},
    2_210_569: {"both_layers_hit": 1, "mixed_layers_required": 2},
    13_782_409: {"mixed_layers_required": 1},
    64_214_329: {
        "both_layers_hit": 1,
        "excess_layer_hit": 1,
        "shared_layer_hit": 2,
    },
    105_295_129: {
        "both_layers_hit": 1,
        "mixed_layers_required": 2,
        "shared_layer_hit": 1,
    },
    536_944_489: {"mixed_layers_required": 3, "shared_layer_hit": 1},
}
EXPECTED_AGGREGATE_COUNTS = {
    "both_layers_hit": 3,
    "excess_layer_hit": 1,
    "mixed_layers_required": 11,
    "shared_layer_hit": 5,
}
EXPECTED_MIXED_EXCESS_SUPPORT_COUNTS = {"1": 10, "2": 1}


def load_layer_module():
    spec = importlib.util.spec_from_file_location(
        "cross_modulus_layer_profile_500m", LAYER_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load cross-modulus layer helpers")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


layers = load_layer_module()


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_factorization(value: int) -> list[tuple[int, int]]:
    """Factor one hit K and certify reconstruction."""
    factors = sorted(
        (int(prime), int(exponent))
        for prime, exponent in sympy.factorint(value).items()
    )
    if (
        not factors
        or math.prod(prime**exponent for prime, exponent in factors) != value
        or any(not sympy.isprime(prime) or exponent < 1 for prime, exponent in factors)
    ):
        raise AssertionError("K factorization is invalid")
    return factors


def checked_source_records(profile: dict[str, object]) -> list[dict[str, int | str]]:
    """Recover all source moduli and their K values from the frozen profile."""
    prime = int(profile["prime"])
    records = [
        {
            "R": int(record["R"]),
            "K": (prime * int(record["R"]) + 1) // 4,
            "classification": str(record["classification"]),
        }
        for record in profile["records"]
    ]
    records.sort(key=lambda record: int(record["R"]))
    if len(records) != int(profile["linear_R_count"]):
        raise AssertionError("linear R count changed")
    if len({int(record["R"]) for record in records}) != len(records):
        raise AssertionError("induced source moduli are not distinct")
    for record in records:
        R = int(record["R"])
        K = int(record["K"])
        if R % 4 != 3 or 4 * K != prime * R + 1 or math.gcd(K, R) != 1:
            raise AssertionError("malformed source modulus record")
    return records


def verify_pairwise_identity(records: list[dict[str, int | str]]) -> None:
    """Independently check the exact gcd identity for every source-modulus pair."""
    for index, left in enumerate(records):
        for right in records[index + 1 :]:
            difference = abs(int(left["R"]) - int(right["R"]))
            if difference == 0 or difference % 4:
                raise AssertionError("source-modulus difference is invalid")
            if math.gcd(int(left["K"]), int(right["K"])) != math.gcd(
                int(left["K"]), difference // 4
            ):
                raise AssertionError("cross-modulus gcd identity failed")


def shared_difference_lcm(R: int, all_R: list[int]) -> int:
    """Return lcm of abs(R-R')/4 over the other induced source moduli."""
    result = 1
    for other in all_R:
        if other != R:
            result = math.lcm(result, abs(R - other) // 4)
    return result


def classify_hit(
    record: dict[str, int | str], all_R: list[int]
) -> dict[str, object]:
    """Split one stored hit by its exact cross-modulus exponent layers."""
    R = int(record["R"])
    K = int(record["K"])
    factors = exact_factorization(K)
    shared_layer = math.gcd(K, shared_difference_lcm(R, all_R))
    excess_layer = K // shared_layer
    shared_factors = layers.factorization_of_divisor(shared_layer, factors)
    excess_factors = layers.factorization_of_divisor(excess_layer, factors)
    full_spectrum = layers.centered_square_spectrum(factors, R)
    shared_spectrum = layers.centered_square_spectrum(shared_factors, R)
    excess_spectrum = layers.centered_square_spectrum(excess_factors, R)
    if full_spectrum != layers.product_spectrum(shared_spectrum, excess_spectrum, R):
        raise AssertionError("layer spectra did not reconstruct K")
    target = R - 1
    if target not in full_spectrum:
        raise AssertionError("frozen target hit disappeared")

    shared_costs = layers.minimum_support_by_residue(shared_factors, R)
    excess_costs = layers.minimum_support_by_residue(excess_factors, R)
    target_pairs = []
    for shared_residue, (shared_support, shared_vector) in shared_costs.items():
        needed_excess = target * pow(shared_residue, -1, R) % R
        if needed_excess in excess_costs:
            excess_support, excess_vector = excess_costs[needed_excess]
            target_pairs.append(
                (
                    shared_support + excess_support,
                    excess_support,
                    shared_support,
                    shared_vector,
                    excess_vector,
                    shared_residue,
                    needed_excess,
                )
            )
    if not target_pairs:
        raise AssertionError("target witness disappeared from layer spectra")
    minimum_total = min(target_pairs)

    shared_hit = target in shared_spectrum
    excess_hit = target in excess_spectrum
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
        "K_factorization": layers.factorization_payload(factors),
        "shared_layer_factorization": layers.factorization_payload(shared_factors),
        "excess_layer_factorization": layers.factorization_payload(excess_factors),
        "minus_one_in_shared_layer_spectrum": shared_hit,
        "minus_one_in_excess_layer_spectrum": excess_hit,
        "target_hit_cross_modulus_layer_classification": classification,
        "minimum_excess_layer_support": min(pair[1] for pair in target_pairs),
        "minimum_shared_layer_support": min(pair[2] for pair in target_pairs),
        "minimum_total_layer_support": minimum_total[0],
        "minimum_total_layer_witness": {
            "shared_coordinates": list(minimum_total[3]),
            "excess_coordinates": list(minimum_total[4]),
            "shared_residue": minimum_total[5],
            "excess_residue": minimum_total[6],
        },
    }


def run_audit(path: Path = INPUT) -> dict[str, object]:
    """Profile all 20 target hits across the seven frozen complete spectra."""
    if file_sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("upstream obstruction-mixture profile changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    profiles = []
    aggregate = Counter()
    mixed_supports = Counter()
    for source_profile in payload["profiles"]:
        prime = int(source_profile["prime"])
        records = checked_source_records(source_profile)
        verify_pairwise_identity(records)
        all_R = [int(record["R"]) for record in records]
        hit_records = [
            classify_hit(record, all_R)
            for record in records
            if record["classification"] == "hit"
        ]
        local_counts = Counter(
            record["target_hit_cross_modulus_layer_classification"]
            for record in hit_records
        )
        local_counts = dict(sorted(local_counts.items()))
        if local_counts != EXPECTED_PER_PRIME_COUNTS[prime]:
            raise AssertionError("per-prime layer profile changed")
        aggregate.update(local_counts)
        for record in hit_records:
            if (
                record["target_hit_cross_modulus_layer_classification"]
                == "mixed_layers_required"
            ):
                mixed_supports[str(record["minimum_excess_layer_support"])] += 1
        profiles.append(
            {
                "prime": prime,
                "complete_linear_R_count": len(records),
                "general_B_hit_R_count": len(hit_records),
                "cross_modulus_layer_classification_counts": local_counts,
                "records": hit_records,
            }
        )
    aggregate_counts = dict(sorted(aggregate.items()))
    mixed_support_counts = dict(sorted(mixed_supports.items()))
    if aggregate_counts != EXPECTED_AGGREGATE_COUNTS:
        raise AssertionError("aggregate layer profile changed")
    if mixed_support_counts != EXPECTED_MIXED_EXCESS_SUPPORT_COUNTS:
        raise AssertionError("mixed excess support profile changed")
    return {
        "arithmetic": (
            "use the seven-point complete linear R spectra to verify every "
            "pairwise gcd(K_R,K_R') identity, then factor each target-hit K and "
            "enumerate its shared and excess centered exponent-layer spectra"
        ),
        "scope_note": (
            "This is a finite profile of the 20 target hits in seven frozen "
            "complete spectra. It does not give a universal source selector."
        ),
        "input_artifact": path.name,
        "input_sha256": file_sha256(path),
        "aggregate_cross_modulus_layer_classification_counts": aggregate_counts,
        "mixed_layer_minimum_excess_support_counts": mixed_support_counts,
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
                ],
                "mixed_layer_minimum_excess_support_counts": result[
                    "mixed_layer_minimum_excess_support_counts"
                ],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
