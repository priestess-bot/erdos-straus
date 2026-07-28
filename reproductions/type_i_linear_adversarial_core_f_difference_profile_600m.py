#!/usr/bin/env python3
"""Profile divisor-difference coverage at the four adversarial cores' F states."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy
from sympy import Matrix


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-adversarial-core-f-difference-profile-600m-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
ADVERSARIAL_PRIMES = (878_089, 26_034_649, 57_399_241, 283_319_689)
EXPECTED_PER_PRIME_F_COUNTS = {
    878_089: 2,
    26_034_649: 6,
    57_399_241: 24,
    283_319_689: 13,
}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("adversarial_core_f_difference_sources", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    return hashlib.sha256(
        "\n".join(",".join(str(value) for value in row) for row in rows).encode("ascii")
    ).hexdigest()


def generated_subgroup_order(certificate: dict[str, object]) -> tuple[int, int]:
    """Recover |H| and its index from the exact logarithmic lattice certificate."""
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


def load_finite_records(
    input_path: Path = INPUT,
) -> dict[int, list[dict[str, object]]]:
    """Load exactly the F states from the four unique-hit adversarial cores."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full B>1-spectrum input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list):
        raise AssertionError("full B>1-spectrum input lacks profiles")
    selected: dict[int, list[dict[str, object]]] = {}
    for profile in profiles:
        prime = int(profile["prime"])
        if prime not in ADVERSARIAL_PRIMES:
            continue
        records = [
            dict(record)
            for record in profile["records"]
            if record["classification"] == "finite_exponent"
        ]
        records.sort(key=lambda record: int(record["R"]))
        if len(records) != EXPECTED_PER_PRIME_F_COUNTS[prime]:
            raise AssertionError("adversarial F-state count changed")
        selected[prime] = records
    if tuple(sorted(selected)) != ADVERSARIAL_PRIMES:
        raise AssertionError("the four adversarial profiles are not all present")
    return selected


def audit_record(prime: int, stored: dict[str, object]) -> dict[str, object]:
    """Compute A, A A^{-1}, and the exact generated subgroup for one F state."""
    R = int(stored["R"])
    K = int(stored["K"])
    A = {int(divisor) % R for divisor in sympy.divisors(K)}
    difference = {
        (left * pow(right, -1, R)) % R
        for left in A
        for right in A
    }
    factors = sources.exact_factorization(K)
    certificate = sources.unit_group_subgroup_certificate(factors, R)
    H_order, H_index = generated_subgroup_order(certificate)
    negative_A = {(-residue) % R for residue in A}
    if (
        stored["classification"] != "finite_exponent"
        or not bool(stored["target_in_generated_subgroup"])
        or not bool(certificate["target_in_generated_subgroup"])
        or A & negative_A
        or (R - 1) in difference
        or len(difference) > H_order
    ):
        raise AssertionError("F-state difference spectrum violates the exact obstruction boundary")
    density = Fraction(len(difference), H_order)
    missing_residues = []
    if H_index == 1 and H_order - len(difference) <= 100:
        missing_residues = [
            residue
            for residue in range(R)
            if math.gcd(residue, R) == 1 and residue not in difference
        ]
        if len(missing_residues) != H_order - len(difference):
            raise AssertionError("full-unit difference complement has the wrong size")
    return {
        "R": R,
        "K": K,
        "source_state_count": int(stored["source_state_count"]),
        "K_divisor_residue_count": len(A),
        "generated_subgroup_order": H_order,
        "generated_subgroup_index": H_index,
        "difference_residue_count": len(difference),
        "difference_density_numerator": density.numerator,
        "difference_density_denominator": density.denominator,
        "difference_density": float(density),
        "difference_density_deficit": H_order - len(difference),
        "difference_target_in_spectrum": (R - 1) in difference,
        "difference_missing_residues": missing_residues,
        "half_density_deficit": H_order - 2 * len(A),
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Audit difference-set coverage at all F states in the four adversarial cores."""
    stored_by_prime = load_finite_records(input_path)
    profiles = []
    all_records: list[dict[str, object]] = []
    for prime in ADVERSARIAL_PRIMES:
        records = [audit_record(prime, stored) for stored in stored_by_prime[prime]]
        records.sort(key=lambda record: int(record["R"]))
        digest_rows = [
            (
                int(record["R"]),
                int(record["K"]),
                int(record["K_divisor_residue_count"]),
                int(record["generated_subgroup_order"]),
                int(record["difference_residue_count"]),
                int(record["difference_density_deficit"]),
                int(record["half_density_deficit"]),
            )
            for record in records
        ]
        profiles.append(
            {
                "prime": prime,
                "finite_exponent_R_count": len(records),
                "minimum_difference_density_deficit": min(
                    int(record["difference_density_deficit"]) for record in records
                ),
                "maximum_difference_density_deficit": max(
                    int(record["difference_density_deficit"]) for record in records
                ),
                "maximum_difference_density": max(
                    float(record["difference_density"]) for record in records
                ),
                "record_sha256": stable_sha256(digest_rows),
                "records": records,
            }
        )
        all_records.extend({"prime": prime, **record} for record in records)

    maximum_density_record = max(
        all_records,
        key=lambda record: (
            Fraction(
                int(record["difference_density_numerator"]),
                int(record["difference_density_denominator"]),
            ),
            -int(record["prime"]),
            -int(record["R"]),
        ),
    )
    near_saturation = [
        record
        for record in all_records
        if int(record["difference_density_deficit"]) <= 100
    ]
    near_saturation.sort(key=lambda record: (int(record["difference_density_deficit"]), int(record["prime"]), int(record["R"])))
    summary = {
        "arithmetic": (
            "for every F-type state in the four unique-general-B-hit adversarial cores, construct "
            "A_R(K), compute its exact quotient difference spectrum A_R(K)A_R(K)^(-1), and compare "
            "its coverage and missing target against the generated support subgroup"
        ),
        "scope_note": (
            "This is a complete finite profile of 45 F states in four adversarial cores. It tests "
            "difference-set coverage, not a cross-source selector theorem."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "prime_count": len(ADVERSARIAL_PRIMES),
        "finite_exponent_R_count": len(all_records),
        "difference_target_hit_count": sum(
            bool(record["difference_target_in_spectrum"]) for record in all_records
        ),
        "maximum_difference_density_numerator": int(
            maximum_density_record["difference_density_numerator"]
        ),
        "maximum_difference_density_denominator": int(
            maximum_density_record["difference_density_denominator"]
        ),
        "maximum_difference_density": float(maximum_density_record["difference_density"]),
        "maximum_difference_density_witness": {
            key: maximum_density_record[key]
            for key in (
                "prime",
                "R",
                "K",
                "K_divisor_residue_count",
                "generated_subgroup_order",
                "difference_residue_count",
                "difference_density_deficit",
                "half_density_deficit",
            )
        },
        "minimum_difference_density_deficit": min(
            int(record["difference_density_deficit"]) for record in all_records
        ),
        "near_saturation_count_deficit_le_100": len(near_saturation),
        "near_saturation_records": [
            {
                key: record[key]
                for key in (
                    "prime",
                    "R",
                    "K",
                    "difference_residue_count",
                    "generated_subgroup_order",
                "difference_density_deficit",
                "difference_density",
                "difference_missing_residues",
                "half_density_deficit",
                )
            }
            for record in near_saturation
        ],
        "profiles": profiles,
    }
    return summary


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
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
