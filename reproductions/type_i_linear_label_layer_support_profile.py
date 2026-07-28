#!/usr/bin/env python3
"""Measure label-layer support needed by frozen linear Type I target hits.

For a complete linear source profile of one core prime, coordinate labels give
the collision/private splitting of each source and affine block.  This audit
does not select a source.  It asks, only at already successful (p, R) states,
how many of the four exact factor layers are sufficient for their centered
square-divisor spectrum to contain -1 modulo R.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from typing import Iterable

import sympy


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SCRIPT = (
    ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
)
INPUT_B1_FAILURES = (
    ROOT
    / "reproductions"
    / "type-i-global-linear-b1-failure-general-b-profile-500m-results.json"
)
INPUT_PRESSURE_PROFILES = (
    ROOT
    / "reproductions"
    / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-label-layer-support-profile-results.json"
)

EXPECTED_B1_FAILURES_SHA256 = (
    "9767df17ff2005153fcf559cb379bab03d7830809f57cdafe327c7f759ba3822"
)
EXPECTED_PRESSURE_PROFILES_SHA256 = (
    "dce587d6e6703e5cdcb81b6cd05c16989394a7321d2d14515ea2eda6c2aec44d"
)
EXPECTED_PER_PRIME_SUPPORT_COUNTS = {
    214_729: {"2": 4},
    878_089: {"2": 1},
    2_210_569: {"1": 2, "2": 2},
    3_942_409: {"2": 4},
    13_782_409: {"3": 1},
    62_588_089: {"2": 3, "3": 2},
    64_214_329: {"1": 3, "2": 2},
    105_295_129: {"1": 2, "2": 3, "3": 1},
    297_640_249: {"2": 3, "3": 4},
    477_015_289: {"1": 2, "2": 2},
    536_944_489: {"1": 5, "2": 4},
}
EXPECTED_AGGREGATE_SUPPORT_COUNTS = {"1": 14, "2": 28, "3": 8}
EXPECTED_TARGET_HIT_R_COUNT = 32
EXPECTED_DIRECTED_TARGET_HIT_SOURCE_COUNT = 50

LAYER_NAMES = (
    "source_collision",
    "source_private",
    "affine_collision",
    "affine_private",
)


def load_module(name: str, path: Path):
    """Load the complete linear-source enumerator without running its CLI."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("label_layer_source_enumerator", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact input bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integer_list_sha256(values: Iterable[int]) -> str:
    """Hash an ordered integer list in the project's canonical text format."""
    return hashlib.sha256(
        "".join(f"{int(value)}\n" for value in values).encode("ascii")
    ).hexdigest()


def exact_factorization(value: int) -> list[tuple[int, int]]:
    """Factor a nonnegative layer product and certify the reconstruction."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors = sorted(
        (int(prime), int(exponent))
        for prime, exponent in sympy.factorint(value).items()
    )
    if math.prod(prime**exponent for prime, exponent in factors) != value or any(
        not sympy.isprime(prime) or exponent < 1 for prime, exponent in factors
    ):
        raise AssertionError("factorization did not reconstruct")
    return factors


def factorization_payload(
    factors: Iterable[tuple[int, int]],
) -> list[dict[str, int]]:
    """Encode a factorization in a checked JSON form."""
    return [
        {"prime": int(prime), "exponent": int(exponent)}
        for prime, exponent in factors
    ]


def centered_square_spectrum(
    factors: Iterable[tuple[int, int]], modulus: int
) -> set[int]:
    """Enumerate the exact centered exponent box of one divisor block."""
    residues = {1}
    for prime, exponent in factors:
        powers = [
            pow(prime, coordinate, modulus)
            for coordinate in range(-exponent, exponent + 1)
        ]
        residues = {
            residue * power % modulus for residue in residues for power in powers
        }
    return residues


def coordinate_label_lcms(
    states_by_R: dict[int, list[tuple[int, int]]]
) -> tuple[list[int], dict[int, int]]:
    """Return every coordinate label and its exact cross-label collision lcm."""
    labels = sorted(
        {
            coordinate
            for states in states_by_R.values()
            for a, s in states
            for coordinate in (a, s)
        }
    )
    if not labels:
        raise AssertionError("complete source profile has no coordinate labels")
    collision_lcms = {
        label: math.lcm(
            *(abs(label - other) for other in labels if other != label)
        )
        if len(labels) > 1
        else 1
        for label in labels
    }
    return labels, collision_lcms


def layer_values(
    prime: int,
    R: int,
    a: int,
    s: int,
    collision_lcms: dict[int, int],
) -> tuple[int, tuple[int, int, int, int]]:
    """Split K into source/affine collision and private coordinate layers."""
    if prime != a + s + a * s * R or s % 2 != 1 or R % 4 != 3:
        raise AssertionError("invalid directed linear source")
    lambda_value = 4 if s % 4 == 1 else 2
    eta = 4 // lambda_value
    gamma, gamma_remainder = divmod(s * R + 1, lambda_value)
    affine, affine_remainder = divmod(a * R + 1, eta)
    K = (prime * R + 1) // 4
    if gamma_remainder or affine_remainder or gamma * affine != K:
        raise AssertionError("linear two-block factorization did not reconstruct K")
    source_collision = math.gcd(gamma, collision_lcms[s])
    affine_collision = math.gcd(affine, collision_lcms[a])
    layers = (
        source_collision,
        gamma // source_collision,
        affine_collision,
        affine // affine_collision,
    )
    if math.prod(layers) != K:
        raise AssertionError("label layers did not reconstruct K")
    return K, layers


def mask_layer_names(mask: int) -> list[str]:
    """Encode one nonempty four-layer subset in a stable human-readable form."""
    if mask < 1 or mask >= 1 << len(LAYER_NAMES):
        raise ValueError("layer mask is outside the nonempty four-layer range")
    return [name for index, name in enumerate(LAYER_NAMES) if mask & (1 << index)]


def audit_orientation(
    prime: int,
    R: int,
    a: int,
    s: int,
    collision_lcms: dict[int, int],
) -> dict[str, object]:
    """Find every minimum label-layer subset that supplies a target hit."""
    K, layers = layer_values(prime, R, a, s, collision_lcms)
    target = R - 1
    full_spectrum = centered_square_spectrum(exact_factorization(K), R)
    if target not in full_spectrum:
        raise AssertionError("declared target-hit state lost its centered witness")
    hit_masks = []
    for mask in range(1, 1 << len(LAYER_NAMES)):
        layer_product = math.prod(
            layer for index, layer in enumerate(layers) if mask & (1 << index)
        )
        spectrum = centered_square_spectrum(exact_factorization(layer_product), R)
        if target in spectrum:
            hit_masks.append(mask)
    if not hit_masks:
        raise AssertionError("the full layer product failed to recover its target hit")
    minimum_support = min(mask.bit_count() for mask in hit_masks)
    minimum_masks = [
        mask for mask in hit_masks if mask.bit_count() == minimum_support
    ]
    return {
        "R": R,
        "a": a,
        "s": s,
        "K": K,
        "layers": [
            {
                "name": name,
                "label": s if index < 2 else a,
                "value": layer,
                "factorization": factorization_payload(exact_factorization(layer)),
            }
            for index, (name, layer) in enumerate(zip(LAYER_NAMES, layers))
        ],
        "minimum_target_layer_support": minimum_support,
        "minimum_target_layer_masks": [
            mask_layer_names(mask) for mask in minimum_masks
        ],
    }


def checked_profiles(
    path: Path, expected_sha256: str, kind: str
) -> list[tuple[int, list[dict[str, object]]]]:
    """Load one hash-frozen collection of complete linear spectra."""
    if file_sha256(path) != expected_sha256:
        raise AssertionError(f"{kind} input hash changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if kind == "B=1 failure":
        profiles = payload["general_B_failure_profiles"]
    elif kind == "pressure":
        profiles = payload["profiles"]
    else:
        raise ValueError("unknown profile kind")
    result = []
    for profile in profiles:
        prime = int(profile["prime"])
        records = [dict(record) for record in profile["records"]]
        records.sort(key=lambda record: int(record["R"]))
        if prime % 24 != 1 or not sympy.isprime(prime):
            raise AssertionError("profile contains a non-core prime")
        if len({int(record["R"]) for record in records}) != len(records):
            raise AssertionError("profile repeats an induced source modulus")
        result.append((prime, records))
    return result


def audit_profile(prime: int, records: list[dict[str, object]]) -> dict[str, object]:
    """Audit all directed orientations behind every stored target-hit modulus."""
    bound, states_by_R = sources.enumerate_linear_source_states(prime)
    source_R = sorted(states_by_R)
    recorded_R = [int(record["R"]) for record in records]
    if source_R != recorded_R:
        raise AssertionError("frozen complete source profile no longer matches enumerator")
    for record in records:
        R = int(record["R"])
        K = (prime * R + 1) // 4
        if R % 4 != 3 or 4 * K != prime * R + 1:
            raise AssertionError("malformed frozen source modulus")
        if "source_states" in record and [
            [a, s] for a, s in states_by_R[R]
        ] != record["source_states"]:
            raise AssertionError("frozen directed source states no longer match enumerator")
    labels, collision_lcms = coordinate_label_lcms(states_by_R)
    orientations = []
    for record in records:
        if str(record["classification"]) != "hit":
            continue
        R = int(record["R"])
        orientations.extend(
            audit_orientation(prime, R, a, s, collision_lcms)
            for a, s in states_by_R[R]
        )
    support_counts = Counter(
        str(orientation["minimum_target_layer_support"])
        for orientation in orientations
    )
    support_counts = dict(sorted(support_counts.items()))
    if support_counts != EXPECTED_PER_PRIME_SUPPORT_COUNTS[prime]:
        raise AssertionError(
            "per-prime label-layer support profile changed: "
            f"p={prime}, actual={support_counts}, "
            f"expected={EXPECTED_PER_PRIME_SUPPORT_COUNTS[prime]}"
        )
    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "complete_linear_R_count": len(source_R),
        "complete_directed_linear_source_count": sum(
            len(states) for states in states_by_R.values()
        ),
        "coordinate_label_count": len(labels),
        "coordinate_labels_sha256": integer_list_sha256(labels),
        "target_hit_R_count": sum(
            str(record["classification"]) == "hit" for record in records
        ),
        "directed_target_hit_source_count": len(orientations),
        "minimum_target_layer_support_counts": support_counts,
        "orientations": orientations,
    }


def run_audit(
    b1_failures_path: Path = INPUT_B1_FAILURES,
    pressure_profiles_path: Path = INPUT_PRESSURE_PROFILES,
) -> dict[str, object]:
    """Run the exact four-layer audit on all eleven frozen complete spectra."""
    source_profiles = [
        *checked_profiles(
            b1_failures_path, EXPECTED_B1_FAILURES_SHA256, "B=1 failure"
        ),
        *checked_profiles(
            pressure_profiles_path, EXPECTED_PRESSURE_PROFILES_SHA256, "pressure"
        ),
    ]
    if len(source_profiles) != len(EXPECTED_PER_PRIME_SUPPORT_COUNTS):
        raise AssertionError("the frozen profile family changed")
    if len({prime for prime, _ in source_profiles}) != len(source_profiles):
        raise AssertionError("the two frozen profile families overlap")
    profiles = [
        audit_profile(prime, records)
        for prime, records in sorted(source_profiles, key=lambda item: item[0])
    ]
    aggregate_support_counts = Counter(
        str(orientation["minimum_target_layer_support"])
        for profile in profiles
        for orientation in profile["orientations"]
    )
    aggregate_support_counts = dict(sorted(aggregate_support_counts.items()))
    target_hit_R_count = sum(int(profile["target_hit_R_count"]) for profile in profiles)
    directed_target_hit_source_count = sum(
        int(profile["directed_target_hit_source_count"]) for profile in profiles
    )
    if aggregate_support_counts != EXPECTED_AGGREGATE_SUPPORT_COUNTS:
        raise AssertionError("aggregate label-layer support profile changed")
    if target_hit_R_count != EXPECTED_TARGET_HIT_R_COUNT:
        raise AssertionError("target-hit R count changed")
    if directed_target_hit_source_count != EXPECTED_DIRECTED_TARGET_HIT_SOURCE_COUNT:
        raise AssertionError("directed target-hit source count changed")
    return {
        "arithmetic": (
            "for every directed linear source behind every stored target-hit "
            "modulus, split K into source/affine collision/private layers from "
            "the complete coordinate-label profile and exactly enumerate each "
            "nonempty layer-subproduct centered square spectrum modulo R"
        ),
        "scope_note": (
            "This is a finite dependency profile of already successful states. "
            "It neither selects a successful source for an arbitrary core prime "
            "nor proves a universal bound on the required layer support."
        ),
        "inputs": {
            b1_failures_path.name: file_sha256(b1_failures_path),
            pressure_profiles_path.name: file_sha256(pressure_profiles_path),
        },
        "profile_count": len(profiles),
        "target_hit_R_count": target_hit_R_count,
        "directed_target_hit_source_count": directed_target_hit_source_count,
        "aggregate_minimum_target_layer_support_counts": aggregate_support_counts,
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--b1-failures-input", type=Path, default=INPUT_B1_FAILURES)
    parser.add_argument("--pressure-input", type=Path, default=INPUT_PRESSURE_PROFILES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.b1_failures_input, args.pressure_input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "profile_count": result["profile_count"],
                "target_hit_R_count": result["target_hit_R_count"],
                "directed_target_hit_source_count": result[
                    "directed_target_hit_source_count"
                ],
                "aggregate_minimum_target_layer_support_counts": result[
                    "aggregate_minimum_target_layer_support_counts"
                ],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
