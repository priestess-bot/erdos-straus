#!/usr/bin/env python3
"""Measure the exact F-state antipodal-density gap on seven single-hit points."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy
from sympy import Matrix


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-full-spectrum-bgt1-200-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-single-hit-f-density-7-results.json"
)
EXPECTED_INPUT_SHA256 = "5f60c11b255aac289b45d2a4721b233534b7bc29476b76bb5f41efc0917a0196"
SINGLE_HIT_PRIMES = (
    67_369,
    878_089,
    13_782_409,
    26_034_649,
    57_399_241,
    152_498_329,
    283_319_689,
)


def load_module(name: str, path: Path):
    """Load the exact unit-group certificate implementation."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("single_hit_f_density_sources", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    """Hash the complete-spectrum input artifact."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_profiles(input_path: Path = INPUT) -> list[dict[str, object]]:
    """Load exactly the seven profiles having one target hit."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the complete-spectrum input artifact changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("records")
    if not isinstance(profiles, list):
        raise AssertionError("complete-spectrum input lacks records")
    selected = [
        dict(profile)
        for profile in profiles
        if int(profile["classification_counts"]["hit"]) == 1
    ]
    if tuple(int(profile["prime"]) for profile in selected) != SINGLE_HIT_PRIMES:
        raise AssertionError("the seven single-hit profiles changed")
    return selected


def generated_subgroup_order(certificate: dict[str, object]) -> tuple[int, int]:
    """Recover the exact support subgroup order and its index."""
    component_orders = [
        int(component["order"])
        for component in certificate["components"]
        if isinstance(component, dict)
    ]
    hnf = Matrix(certificate["column_lattice_hermite_normal_form"])
    index = abs(int(hnf.det()))
    full_order = math.prod(component_orders)
    if index < 1 or full_order % index:
        raise AssertionError("support lattice index is invalid")
    return full_order // index, index


def divisor_residues(value: int, modulus: int) -> set[int]:
    """Return the one-sided divisor residue set exactly."""
    return {int(divisor) % modulus for divisor in sympy.divisors(value)}


def audit_record(prime: int, stored: dict[str, object]) -> dict[str, int]:
    """Compute one F state's divisor density and exact support order."""
    if stored["classification"] != "finite_exponent":
        raise AssertionError("input record is not an F state")
    R = int(stored["R"])
    K = (prime * R + 1) // 4
    residues = divisor_residues(K, R)
    antipodal = residues & {(-residue) % R for residue in residues}
    factors = sources.exact_factorization(K)
    certificate = sources.unit_group_subgroup_certificate(factors, R)
    H_order, H_index = generated_subgroup_order(certificate)
    if (
        not bool(stored["target_in_generated_subgroup"])
        or not bool(certificate["target_in_generated_subgroup"])
        or antipodal
        or 2 * len(residues) > H_order
    ):
        raise AssertionError("F-state antipodal density invariant failed")
    return {
        "R": R,
        "K": K,
        "source_state_count": int(stored["source_state_count"]),
        "K_divisor_residue_count": len(residues),
        "generated_subgroup_order": H_order,
        "generated_subgroup_index": H_index,
        "twice_divisor_residue_count": 2 * len(residues),
        "half_density_deficit": H_order - 2 * len(residues),
    }


def audit_prime(profile: dict[str, object]) -> dict[str, object]:
    """Measure every F state in one single-hit profile."""
    prime = int(profile["prime"])
    records = [
        audit_record(prime, stored)
        for stored in profile["records"]
        if stored["classification"] == "finite_exponent"
    ]
    records.sort(key=lambda record: record["R"])
    if not records:
        raise AssertionError("single-hit profile unexpectedly has no F state")
    return {
        "prime": prime,
        "finite_exponent_R_count": len(records),
        "minimum_half_density_deficit": min(
            record["half_density_deficit"] for record in records
        ),
        "maximum_half_density_deficit": max(
            record["half_density_deficit"] for record in records
        ),
        "half_density_equality_count": sum(
            record["half_density_deficit"] == 0 for record in records
        ),
        "records": records,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Run the exact finite F-density audit."""
    profiles = [audit_prime(profile) for profile in load_profiles(input_path)]
    records = [record for profile in profiles for record in profile["records"]]
    return {
        "arithmetic": (
            "select the seven complete linear spectra with exactly one target hit; for every F state "
            "construct A_R(K) from all divisors of K, recover |H_R(K)| from the exact unit-group "
            "lattice certificate, and measure |H_R(K)|-2|A_R(K)|"
        ),
        "scope_note": (
            "This quantifies the fixed-state F obstruction on seven single-hit pressure points. "
            "It does not provide a cross-source escape theorem or cover the other 193 selected points."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "primes": list(SINGLE_HIT_PRIMES),
        "finite_exponent_R_count": len(records),
        "half_density_equality_count": sum(
            record["half_density_deficit"] == 0 for record in records
        ),
        "minimum_half_density_deficit": min(
            record["half_density_deficit"] for record in records
        ),
        "maximum_half_density_deficit": max(
            record["half_density_deficit"] for record in records
        ),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key != "profiles"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
