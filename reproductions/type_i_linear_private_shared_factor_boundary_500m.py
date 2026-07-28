#!/usr/bin/env python3
"""Profile private and shared prime supports across complete linear R spectra.

For each frozen global linear-B=1 failure prime, a prime divisor of K_R is
private when it divides no K_R' at another induced linear modulus R'.  This
script asks whether a general-B target hit can come from the private or shared
prime support alone.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
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
    / "type-i-linear-private-shared-factor-boundary-500m-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "9767df17ff2005153fcf559cb379bab03d7830809f57cdafe327c7f759ba3822"
)
EXPECTED_PER_PRIME_COUNTS = {
    3_942_409: {"mixed_private_shared": 2, "shared_block_hit": 2},
    62_588_089: {"mixed_private_shared": 2},
    297_640_249: {"mixed_private_shared": 3, "shared_block_hit": 1},
    477_015_289: {"mixed_private_shared": 1, "shared_block_hit": 1},
}
EXPECTED_AGGREGATE_COUNTS = {
    "mixed_private_shared": 8,
    "shared_block_hit": 4,
}


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization_from_record(record: dict[str, object]) -> list[tuple[int, int]]:
    """Load and independently validate the stored factorization of K."""
    K = int(record["K"])
    factors = sorted(
        (int(item["prime"]), int(item["exponent"]))
        for item in record["K_factorization"]
    )
    if (
        not factors
        or math.prod(prime**exponent for prime, exponent in factors) != K
        or any(not sympy.isprime(prime) or exponent < 1 for prime, exponent in factors)
    ):
        raise AssertionError("stored K factorization is invalid")
    return factors


def factorization_payload(
    factors: Iterable[tuple[int, int]],
) -> list[dict[str, int]]:
    """Encode a factorization for the checked JSON artifact."""
    return [
        {"prime": int(prime), "exponent": int(exponent)} for prime, exponent in factors
    ]


def centered_square_spectrum(factors: list[tuple[int, int]], modulus: int) -> set[int]:
    """Enumerate the centered K-squared divisor spectrum of one support block."""
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


def classify_hit(
    record: dict[str, object], occurrence_count: dict[int, int]
) -> dict[str, object]:
    """Split one complete-spectrum hit into globally private and shared primes."""
    modulus = int(record["R"])
    factors = factorization_from_record(record)
    private_factors = [factor for factor in factors if occurrence_count[factor[0]] == 1]
    shared_factors = [factor for factor in factors if occurrence_count[factor[0]] > 1]
    if not private_factors or not shared_factors:
        raise AssertionError("frozen hit lost one side of the support partition")
    full_spectrum = centered_square_spectrum(factors, modulus)
    private_spectrum = centered_square_spectrum(private_factors, modulus)
    shared_spectrum = centered_square_spectrum(shared_factors, modulus)
    target = modulus - 1
    if target not in full_spectrum:
        raise AssertionError("stored general-B hit disappeared")
    private_hit = target in private_spectrum
    shared_hit = target in shared_spectrum
    if private_hit and shared_hit:
        classification = "both_blocks_hit"
    elif private_hit:
        classification = "private_block_hit"
    elif shared_hit:
        classification = "shared_block_hit"
    else:
        classification = "mixed_private_shared"
    return {
        "R": modulus,
        "K": int(record["K"]),
        "K_factorization": factorization_payload(factors),
        "private_factorization": factorization_payload(private_factors),
        "shared_factorization": factorization_payload(shared_factors),
        "private_centered_spectrum_residue_count": len(private_spectrum),
        "shared_centered_spectrum_residue_count": len(shared_spectrum),
        "minus_one_in_private_centered_spectrum": private_hit,
        "minus_one_in_shared_centered_spectrum": shared_hit,
        "target_hit_private_shared_classification": classification,
    }


def run_audit(path: Path = INPUT) -> dict[str, object]:
    """Audit all 12 stored general-B hits against complete per-prime spectra."""
    if file_sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("upstream global obstruction profile hash changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    profiles = []
    aggregate = Counter()
    for source_profile in payload["general_B_failure_profiles"]:
        prime = int(source_profile["prime"])
        source_records = source_profile["records"]
        occurrence_count: dict[int, int] = defaultdict(int)
        for record in source_records:
            for factor, _ in factorization_from_record(record):
                occurrence_count[factor] += 1
        records = [
            classify_hit(record, occurrence_count)
            for record in source_records
            if record["classification"] == "hit"
        ]
        local_counts = Counter(
            record["target_hit_private_shared_classification"] for record in records
        )
        local_counts = dict(sorted(local_counts.items()))
        if local_counts != EXPECTED_PER_PRIME_COUNTS[prime]:
            raise AssertionError("per-prime private/shared hit profile changed")
        aggregate.update(local_counts)
        profiles.append(
            {
                "prime": prime,
                "complete_linear_R_count": len(source_records),
                "general_B_hit_R_count": len(records),
                "private_shared_hit_classification_counts": local_counts,
                "records": records,
            }
        )
    aggregate_counts = dict(sorted(aggregate.items()))
    if aggregate_counts != EXPECTED_AGGREGATE_COUNTS:
        raise AssertionError("aggregate private/shared hit profile changed")
    return {
        "arithmetic": (
            "for each fixed prime, define a K_R prime as private when it occurs "
            "at no other R in that prime's complete induced linear spectrum; "
            "split every stored general-B hit into private and shared supports, "
            "then enumerate each centered square-divisor spectrum exactly"
        ),
        "scope_note": (
            "This is a complete finite profile only for the four frozen global "
            "linear-B=1 failure primes and their complete linear R spectra. "
            "Private means private relative to that finite per-prime spectrum; "
            "the result neither proves nor refutes the universal selector."
        ),
        "input_artifact": path.name,
        "input_sha256": file_sha256(path),
        "aggregate_private_shared_hit_classification_counts": aggregate_counts,
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
                "aggregate_private_shared_hit_classification_counts": result[
                    "aggregate_private_shared_hit_classification_counts"
                ]
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
