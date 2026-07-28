#!/usr/bin/env python3
"""Measure one deep finite-exponent obstruction without creating a new bridge.

The input profile classifies the stated (p, R) target as finite-exponent:
-1 belongs to the support subgroup but not to the centered K-squared spectrum.
This program enlarges that centered exponent box only to quantify the defect.
An entrance at dilation c > 1 is not a Type I certificate, since the original
selector permits only divisors of K squared.
"""

from __future__ import annotations

import argparse
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
    / "type-i-finite-exponent-dilation-boundary-297640249-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "9767df17ff2005153fcf559cb379bab03d7830809f57cdafe327c7f759ba3822"
)
PRIME = 297_640_249
MODULUS = 148_820_123
MAX_DILATION = 50
EXPECTED_FACTORIZATION = [
    (3, 1),
    (37, 1),
    (127, 1),
    (97_651, 1),
    (8_044_331, 1),
]


def file_sha256(path: Path) -> str:
    """Return the SHA-256 digest of exact bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization_payload(
    factors: Iterable[tuple[int, int]],
) -> list[dict[str, int]]:
    """Encode an ascending prime factorization."""
    return [
        {"prime": int(prime), "exponent": int(exponent)} for prime, exponent in factors
    ]


def factorization_product(factors: Iterable[tuple[int, int]]) -> int:
    """Reconstruct the positive integer represented by a factorization."""
    return math.prod(prime**exponent for prime, exponent in factors)


def split_factors(
    factors: list[tuple[int, int]], dilation: int
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    """Use the fixed two-versus-three split for the frozen five-factor state."""
    if len(factors) != 5:
        raise AssertionError("the frozen state no longer has five support primes")
    return factors[:2], factors[2:]


def centered_half_residues(
    factors: list[tuple[int, int]], modulus: int, dilation: int
) -> set[int]:
    """Enumerate one half of the centered exponent box as residues."""
    residues = {1}
    for prime, exponent in factors:
        inverse = pow(prime, -1, modulus)
        residue = pow(inverse, dilation * exponent, modulus)
        powers = []
        for _ in range(2 * dilation * exponent + 1):
            powers.append(residue)
            residue = residue * prime % modulus
        residues = {
            previous * power % modulus for previous in residues for power in powers
        }
    return residues


def find_centered_vector(
    factors: list[tuple[int, int]],
    modulus: int,
    dilation: int,
    target: int,
) -> list[int] | None:
    """Find a deterministic exponent vector in the centered dilation box."""
    if dilation < 1:
        raise ValueError("dilation must be positive")
    left_factors, right_factors = split_factors(factors, dilation)
    right_residues = centered_half_residues(right_factors, modulus, dilation)
    for left_first in range(
        -dilation * left_factors[0][1],
        dilation * left_factors[0][1] + 1,
    ):
        left_first_residue = pow(left_factors[0][0], left_first, modulus)
        for left_second in range(
            -dilation * left_factors[1][1],
            dilation * left_factors[1][1] + 1,
        ):
            left_residue = (
                left_first_residue
                * pow(left_factors[1][0], left_second, modulus)
                % modulus
            )
            required_right = target * pow(left_residue, -1, modulus) % modulus
            if required_right not in right_residues:
                continue
            third_exponents = {
                pow(
                    right_factors[2][0],
                    exponent,
                    modulus,
                ): exponent
                for exponent in range(
                    -dilation * right_factors[2][1],
                    dilation * right_factors[2][1] + 1,
                )
            }
            for right_first in range(
                -dilation * right_factors[0][1],
                dilation * right_factors[0][1] + 1,
            ):
                right_first_residue = pow(right_factors[0][0], right_first, modulus)
                for right_second in range(
                    -dilation * right_factors[1][1],
                    dilation * right_factors[1][1] + 1,
                ):
                    right_second_residue = (
                        right_first_residue
                        * pow(right_factors[1][0], right_second, modulus)
                        % modulus
                    )
                    required_third = (
                        required_right * pow(right_second_residue, -1, modulus)
                    ) % modulus
                    right_third = third_exponents.get(required_third)
                    if right_third is not None:
                        return [
                            left_first,
                            left_second,
                            right_first,
                            right_second,
                            int(right_third),
                        ]
    return None


def centered_residue(
    factors: list[tuple[int, int]], vector: list[int], modulus: int
) -> int:
    """Evaluate a centered exponent vector modulo the target modulus."""
    if len(factors) != len(vector):
        raise ValueError("factor and vector lengths disagree")
    residue = 1
    for (prime, _), exponent in zip(factors, vector):
        residue = residue * pow(prime, exponent, modulus) % modulus
    return residue


def load_frozen_state(path: Path = INPUT) -> tuple[int, list[tuple[int, int]]]:
    """Load and validate the stated finite-exponent obstruction."""
    if file_sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("upstream obstruction profile hash changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    profile = next(
        (
            item
            for item in payload["general_B_failure_profiles"]
            if int(item["prime"]) == PRIME
        ),
        None,
    )
    if profile is None:
        raise AssertionError("frozen prime disappeared from the upstream profile")
    record = next(
        (item for item in profile["records"] if int(item["R"]) == MODULUS),
        None,
    )
    if record is None:
        raise AssertionError("frozen finite-exponent modulus disappeared")
    factors = [
        (int(item["prime"]), int(item["exponent"]))
        for item in record["K_factorization"]
    ]
    K = int(record["K"])
    if (
        record["classification"] != "finite_exponent"
        or bool(record["minus_one_in_centered_spectrum"])
        or not bool(
            record["unit_group_subgroup_certificate"]["target_in_generated_subgroup"]
        )
        or factors != EXPECTED_FACTORIZATION
        or factorization_product(factors) != K
        or K != (PRIME * MODULUS + 1) // 4
        or any(not sympy.isprime(prime) or exponent < 1 for prime, exponent in factors)
    ):
        raise AssertionError("frozen finite-exponent state validation failed")
    return K, factors


def run_audit(path: Path = INPUT) -> dict[str, object]:
    """Find the first entrance of -1 in the stated dilated centered spectra."""
    K, factors = load_frozen_state(path)
    target = MODULUS - 1
    profiles = []
    witness = None
    for dilation in range(1, MAX_DILATION + 1):
        vector = find_centered_vector(factors, MODULUS, dilation, target)
        profiles.append(
            {
                "dilation": dilation,
                "target_in_centered_dilated_spectrum": vector is not None,
            }
        )
        if vector is not None:
            witness = vector
            break
    if witness is None:
        raise AssertionError("target did not enter through the stated dilation cap")
    first_dilation = len(profiles)
    if first_dilation != MAX_DILATION:
        raise AssertionError("the frozen first entrance changed")
    if centered_residue(factors, witness, MODULUS) != target or any(
        abs(value) > first_dilation * exponent
        for value, (_, exponent) in zip(witness, factors)
    ):
        raise AssertionError("centered dilation witness failed verification")
    positive_exponents = [
        first_dilation * exponent + value
        for value, (_, exponent) in zip(witness, factors)
    ]
    return {
        "arithmetic": (
            "for the hash-frozen finite-exponent state, exactly enumerate the "
            "centered exponent box -c*nu_q<=z_q<=c*nu_q by a 2-by-3 "
            "meet-in-the-middle residue test for every 1<=c<=50"
        ),
        "scope_note": (
            "An entrance at c>1 is only an exponent-box diagnostic. It is not "
            "a Type I target certificate, because the original selector uses "
            "only d dividing K squared, namely c=1."
        ),
        "input_artifact": path.name,
        "input_sha256": file_sha256(path),
        "prime": PRIME,
        "R": MODULUS,
        "K": K,
        "K_factorization": factorization_payload(factors),
        "original_classification": "finite_exponent",
        "original_centered_dilation": 1,
        "first_target_dilation": first_dilation,
        "target_absent_through_dilation": first_dilation - 1,
        "centered_exponent_witness": witness,
        "positive_exponent_vector_in_K_to_2c": positive_exponents,
        "dilation_profiles": profiles,
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
            {
                key: value
                for key, value in result.items()
                if key not in {"dilation_profiles"}
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
