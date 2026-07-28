#!/usr/bin/env python3
"""Classify whether general-B target hits use one or both linear-source blocks.

For a linear source p=a+s+asR, the source-square normal factorization has
beta=1 and K=gamma*L.  This audit asks only whether -1 already occurs in the
centered square-divisor spectrum of gamma or L separately.  A mixed result is
still a valid target hit of K; it rules out a proof that demands an automatic
single-block hit.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-global-linear-b1-failure-general-b-profile-500m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-general-b-two-block-hit-profile-500m-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "9767df17ff2005153fcf559cb379bab03d7830809f57cdafe327c7f759ba3822"
)
EXPECTED_PER_PRIME_COUNTS = {
    3_942_409: {"mixed_blocks": 4},
    62_588_089: {"mixed_blocks": 5},
    297_640_249: {"mixed_blocks": 7},
    477_015_289: {"affine_block_only": 2, "source_block_only": 2},
}
EXPECTED_AGGREGATE_COUNTS = {
    "affine_block_only": 2,
    "mixed_blocks": 16,
    "source_block_only": 2,
}


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_factorization(value: int) -> list[tuple[int, int]]:
    """Factor a positive integer and certify the reconstruction."""
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
    """Encode a prime factorization for the checked artifact."""
    return [
        {"prime": int(prime), "exponent": int(exponent)} for prime, exponent in factors
    ]


def centered_square_spectrum(factors: list[tuple[int, int]], modulus: int) -> set[int]:
    """Return all centered K-squared divisor residues for one factor block."""
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


def classify_source_orientation(
    prime: int, modulus: int, K: int, a: int, s: int
) -> dict[str, object]:
    """Classify a directed linear source by its gamma and affine factor blocks."""
    if (
        prime != a + s + a * s * modulus
        or s % 2 != 1
        or modulus < 3
        or modulus % 4 != 3
        or K != (prime * modulus + 1) // 4
    ):
        raise AssertionError("invalid directed linear source")
    lambda_value = 4 if s % 4 == 1 else 2
    eta = 4 // lambda_value
    gamma, gamma_remainder = divmod(s * modulus + 1, lambda_value)
    affine_block, affine_remainder = divmod(a * modulus + 1, eta)
    if gamma_remainder or affine_remainder or gamma * affine_block != K:
        raise AssertionError("linear source blocks did not reconstruct K")
    gamma_factors = exact_factorization(gamma)
    affine_factors = exact_factorization(affine_block)
    gamma_spectrum = centered_square_spectrum(gamma_factors, modulus)
    affine_spectrum = centered_square_spectrum(affine_factors, modulus)
    gamma_hit = modulus - 1 in gamma_spectrum
    affine_hit = modulus - 1 in affine_spectrum
    if gamma_hit and affine_hit:
        category = "both_blocks"
    elif gamma_hit:
        category = "source_block_only"
    elif affine_hit:
        category = "affine_block_only"
    else:
        category = "mixed_blocks"
    return {
        "a": a,
        "s": s,
        "lambda": lambda_value,
        "eta": eta,
        "gamma": gamma,
        "gamma_factorization": factorization_payload(gamma_factors),
        "gamma_centered_spectrum_residue_count": len(gamma_spectrum),
        "minus_one_in_gamma_centered_spectrum": gamma_hit,
        "L": affine_block,
        "L_factorization": factorization_payload(affine_factors),
        "L_centered_spectrum_residue_count": len(affine_spectrum),
        "minus_one_in_L_centered_spectrum": affine_hit,
        "target_hit_block_classification": category,
    }


def run_audit(path: Path = INPUT) -> dict[str, object]:
    """Profile every directed source orientation of the 12 frozen target hits."""
    if file_sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("upstream global obstruction profile hash changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    profiles = []
    aggregate = Counter()
    for source_profile in payload["general_B_failure_profiles"]:
        prime = int(source_profile["prime"])
        records = []
        for record in source_profile["records"]:
            if record["classification"] != "hit":
                continue
            modulus, K = int(record["R"]), int(record["K"])
            orientations = [
                classify_source_orientation(
                    prime,
                    modulus,
                    K,
                    int(a),
                    int(s),
                )
                for a, s in record["source_states"]
            ]
            for orientation in orientations:
                aggregate[orientation["target_hit_block_classification"]] += 1
            records.append(
                {
                    "R": modulus,
                    "K": K,
                    "source_orientations": orientations,
                }
            )
        local_counts = Counter(
            orientation["target_hit_block_classification"]
            for record in records
            for orientation in record["source_orientations"]
        )
        local_counts = dict(sorted(local_counts.items()))
        if local_counts != EXPECTED_PER_PRIME_COUNTS[prime]:
            raise AssertionError("per-prime two-block profile changed")
        profiles.append(
            {
                "prime": prime,
                "target_hit_R_count": len(records),
                "directed_target_hit_source_count": sum(
                    len(record["source_orientations"]) for record in records
                ),
                "block_classification_counts": local_counts,
                "records": records,
            }
        )
    aggregate_counts = dict(sorted(aggregate.items()))
    if aggregate_counts != EXPECTED_AGGREGATE_COUNTS:
        raise AssertionError("aggregate two-block profile changed")
    return {
        "arithmetic": (
            "for every directed linear source behind each of the 12 stored "
            "general-B target hits, factor K=gamma*L and exactly enumerate the "
            "centered square-divisor spectra of gamma and L separately modulo R"
        ),
        "scope_note": (
            "This is a finite block-attribution profile of already successful "
            "states. A mixed-block hit remains a valid K-squared target hit; "
            "the result neither rules out adaptive source selection nor proves "
            "a universal source-spectrum intersection."
        ),
        "input_artifact": path.name,
        "input_sha256": file_sha256(path),
        "target_hit_R_count": sum(
            int(profile["target_hit_R_count"]) for profile in profiles
        ),
        "directed_target_hit_source_count": sum(
            int(profile["directed_target_hit_source_count"]) for profile in profiles
        ),
        "aggregate_block_classification_counts": aggregate_counts,
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
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "profiles"},
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
