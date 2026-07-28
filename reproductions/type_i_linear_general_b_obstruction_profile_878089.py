#!/usr/bin/env python3
"""Classify every general-B target spectrum from the linear p=878089 audit.

The frozen counterexample artifact completely enumerates the 54 directed
linear source states E|n at p=878089 and their 24 distinct moduli R.  This
script refactors every K=(pR+1)/4, directly enumerates all d|K^2, and uses
the centered spectrum d*K^{-1} (mod R) to classify each target state as a
hit, a subgroup/character obstruction, or a finite-exponent obstruction.
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

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT / "reproductions" / "type-I-linear-shifted-source-counterexample-878089.json"
)
STRUCTURE = ROOT / "reproductions" / "divisor_residue_structure.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-general-b-obstruction-profile-878089.json"
)

PRIME = 878_089
EXPECTED_INPUT_SHA256 = (
    "9e491bf3816f7880aa3468c61dd7dce0385068ab6fd2388cc0da9f15ca65928c"
)
EXPECTED_R_COUNT = 24
EXPECTED_SOURCE_STATE_COUNT = 54
EXPECTED_CLASSIFICATION_COUNTS = {
    "hit": 1,
    "finite_exponent": 2,
    "subgroup_character": 21,
}
EXPECTED_HIT_R = 59
EXPECTED_FINITE_EXPONENT_R = [279, 503]


def load_module(name: str, path: Path):
    """Load a repository-local helper without treating reproductions as a package."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


structure = load_module("centered_square_spectrum_structure", STRUCTURE)


def file_sha256(path: Path) -> str:
    """Return an exact SHA-256 digest of a frozen input artifact."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_factorization(value: int) -> tuple[tuple[int, int], ...]:
    """Factor and independently verify a positive integer."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors = tuple(
        sorted(
            (int(prime), int(exponent))
            for prime, exponent in sympy.factorint(value).items()
        )
    )
    if math.prod(prime**exponent for prime, exponent in factors) != value or any(
        not sympy.isprime(prime) or exponent < 1 for prime, exponent in factors
    ):
        raise AssertionError("factorization did not reconstruct into positive primes")
    return factors


def divisors_from_factorization(
    factorization: tuple[tuple[int, int], ...],
) -> list[int]:
    """Return every positive divisor in increasing order."""
    values = [1]
    for prime, exponent in factorization:
        values = [
            value * prime**power for value in values for power in range(exponent + 1)
        ]
    return sorted(values)


def parse_input(path: Path) -> tuple[dict[str, object], list[dict[str, object]]]:
    """Hash-freeze and validate the complete p=878089 linear-source audit."""
    if file_sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen p=878089 counterexample artifact changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or int(payload.get("prime", -1)) != PRIME:
        raise AssertionError("counterexample artifact has the wrong prime")
    totals = payload.get("candidate_totals")
    states = payload.get("oriented_linear_source_states")
    audits = payload.get("target_modulus_audits")
    if (
        not isinstance(totals, dict)
        or not isinstance(states, list)
        or not isinstance(audits, list)
    ):
        raise AssertionError("counterexample artifact is malformed")
    if (
        int(totals.get("oriented_linear_source_state_count", -1))
        != EXPECTED_SOURCE_STATE_COUNT
        or int(totals.get("distinct_R_count", -1)) != EXPECTED_R_COUNT
        or len(states) != EXPECTED_SOURCE_STATE_COUNT
        or len(audits) != EXPECTED_R_COUNT
    ):
        raise AssertionError("counterexample source-state totals changed")
    if any(
        bool(audit.get("target_reachable"))
        for audit in audits
        if isinstance(audit, dict)
    ):
        raise AssertionError("the frozen artifact no longer excludes linear B=1")
    return payload, [audit for audit in audits if isinstance(audit, dict)]


def audit_modulus(entry: dict[str, object]) -> dict[str, object]:
    """Classify one complete general-B target divisor spectrum exactly."""
    R = int(entry["R"])
    K = (PRIME * R + 1) // 4
    if R < 3 or R % 4 != 3 or 4 * K != PRIME * R + 1:
        raise AssertionError("stored modulus does not reconstruct K")
    source_state_ids = [int(value) for value in entry["source_state_ids"]]
    if len(source_state_ids) != int(entry["source_state_count"]):
        raise AssertionError("stored source-state identifiers are inconsistent")
    factors = exact_factorization(K)
    if math.gcd(K, R) != 1:
        raise AssertionError("K must be a unit modulo R")

    square_factors = tuple((prime, 2 * exponent) for prime, exponent in factors)
    square_divisors = divisors_from_factorization(square_factors)
    target_divisor_residue = (-K) % R
    matches = [
        divisor for divisor in square_divisors if divisor % R == target_divisor_residue
    ]
    centered_direct = frozenset(
        divisor * pow(K, -1, R) % R for divisor in square_divisors
    )
    spectrum = structure.centered_square_spectrum_classification(factors, R)
    if centered_direct != spectrum["centered_residues"]:
        raise AssertionError(
            "centered spectrum disagreed with direct square-divisor enumeration"
        )
    if bool(matches) != bool(spectrum["target_in_centered_spectrum"]):
        raise AssertionError(
            "centered target test disagreed with direct target divisors"
        )

    minimum_match = min(matches) if matches else None
    if minimum_match is not None:
        complement = K * K // minimum_match
        if (
            minimum_match > K
            or complement % R != target_divisor_residue
            or K * K % minimum_match
        ):
            raise AssertionError(
                "target divisor did not satisfy complement normalization"
            )

    return {
        "R": R,
        "K": K,
        "K_factorization": [
            {"prime": prime, "exponent": exponent} for prime, exponent in factors
        ],
        "source_state_count": len(source_state_ids),
        "source_state_ids": source_state_ids,
        "B_eq_1_target_reachable": bool(entry["target_reachable"]),
        "square_divisor_count": len(square_divisors),
        "centered_spectrum_residue_count": len(spectrum["centered_residues"]),
        "generated_subgroup_order": len(spectrum["generated_subgroup"]),
        "target_divisor_residue": target_divisor_residue,
        "minus_one_in_centered_spectrum": bool(spectrum["target_in_centered_spectrum"]),
        "minus_one_in_generated_subgroup": bool(
            spectrum["target_in_generated_subgroup"]
        ),
        "classification": str(spectrum["classification"]),
        "least_matching_square_divisor": minimum_match,
    }


def run_audit(path: Path = INPUT) -> dict[str, object]:
    """Run the complete 24-modulus centered-spectrum audit."""
    payload, entries = parse_input(path)
    records = [audit_modulus(entry) for entry in entries]
    if [record["R"] for record in records] != sorted(record["R"] for record in records):
        raise AssertionError("stored target moduli are not in canonical order")
    classifications = Counter(str(record["classification"]) for record in records)
    classification_counts = {
        key: int(classifications[key]) for key in sorted(EXPECTED_CLASSIFICATION_COUNTS)
    }
    hits = [record for record in records if record["classification"] == "hit"]
    finite_exponent = [
        record for record in records if record["classification"] == "finite_exponent"
    ]
    if (
        classification_counts != EXPECTED_CLASSIFICATION_COUNTS
        or [record["R"] for record in hits] != [EXPECTED_HIT_R]
        or [record["R"] for record in finite_exponent] != EXPECTED_FINITE_EXPONENT_R
    ):
        raise AssertionError("p=878089 centered-spectrum classification changed")
    if any(record["B_eq_1_target_reachable"] for record in records):
        raise AssertionError("a B=1 target unexpectedly appeared")
    if hits[0]["least_matching_square_divisor"] != 816_781:
        raise AssertionError("the known general-B linear witness changed")

    return {
        "arithmetic": (
            "load the hash-frozen complete p=878089 linear-source audit; for each "
            "of its 24 induced R, factor K=(pR+1)/4, enumerate every d|K^2, "
            "translate the divisor residues by K^{-1}, and classify -1 by exact "
            "membership in the centered finite spectrum and its generated subgroup"
        ),
        "scope_note": (
            "This is a complete 24-modulus general-B target classification only "
            "for the already complete linear-source audit at p=878089. It does "
            "not classify every source state at other primes and does not prove "
            "the universal mixed terminal selector."
        ),
        "input_artifact": path.name,
        "input_sha256": file_sha256(path),
        "prime": int(payload["prime"]),
        "linear_source_state_count": EXPECTED_SOURCE_STATE_COUNT,
        "distinct_R_count": len(records),
        "B_eq_1_hit_count": sum(
            record["B_eq_1_target_reachable"] for record in records
        ),
        "general_B_classification_counts": classification_counts,
        "general_B_hit_R": [record["R"] for record in hits],
        "finite_exponent_failure_R": [record["R"] for record in finite_exponent],
        "subgroup_character_failure_R": [
            record["R"]
            for record in records
            if record["classification"] == "subgroup_character"
        ],
        "records": records,
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
            {key: value for key, value in result.items() if key != "records"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
