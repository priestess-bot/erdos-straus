#!/usr/bin/env python3
"""Measure exact antipodal-density deficits at every frozen F-type linear state."""

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
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
INPUT = ROOT / "reproductions" / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-finite-exponent-antipodal-density-profile-600m-results.json"
)
EXPECTED_INPUT_SHA256 = "dce587d6e6703e5cdcb81b6cd05c16989394a7321d2d14515ea2eda6c2aec44d"
EXPECTED_PER_PRIME_F_COUNTS = {
    214_729: 8,
    878_089: 2,
    2_210_569: 4,
    13_782_409: 9,
    64_214_329: 18,
    105_295_129: 10,
    536_944_489: 17,
}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("finite_exponent_density_sources", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    return hashlib.sha256(
        "\n".join(",".join(str(value) for value in row) for row in rows).encode("ascii")
    ).hexdigest()


def divisor_residues(value: int, modulus: int) -> set[int]:
    return {int(divisor) % modulus for divisor in sympy.divisors(value)}


def generated_subgroup_order(certificate: dict[str, object]) -> tuple[int, int]:
    """Recover |H| from the exact logarithmic lattice certificate."""
    component_orders = [
        int(component["order"])
        for component in certificate["components"]
        if isinstance(component, dict)
    ]
    hnf = Matrix(certificate["column_lattice_hermite_normal_form"])
    index = abs(int(hnf.det()))
    full_order = math.prod(component_orders)
    if index < 1 or full_order % index:
        raise AssertionError("support lattice index does not divide the full unit-group order")
    return full_order // index, index


def load_finite_records(input_path: Path = INPUT) -> list[tuple[int, dict[str, object]]]:
    """Read exactly the 68 F-type records from the frozen full-spectrum audit."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen obstruction-mixture input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list):
        raise AssertionError("obstruction-mixture input lacks profiles")
    result = []
    for profile in profiles:
        prime = int(profile["prime"])
        finite_records = [
            dict(record)
            for record in profile["records"]
            if record["classification"] == "finite_exponent"
        ]
        if len(finite_records) != EXPECTED_PER_PRIME_F_COUNTS[prime]:
            raise AssertionError("frozen finite-exponent count changed")
        result.extend((prime, record) for record in finite_records)
    if len(result) != sum(EXPECTED_PER_PRIME_F_COUNTS.values()):
        raise AssertionError("frozen finite-exponent total changed")
    return result


def audit_record(prime: int, stored: dict[str, object]) -> dict[str, int]:
    """Compute the exact divisor density and support-subgroup order for one F state."""
    R = int(stored["R"])
    K = (prime * R + 1) // 4
    A = divisor_residues(K, R)
    antipodal_intersection = A & {(-residue) % R for residue in A}
    factors = sources.exact_factorization(K)
    certificate = sources.unit_group_subgroup_certificate(factors, R)
    H_order, H_index = generated_subgroup_order(certificate)
    if (
        stored["classification"] != "finite_exponent"
        or not bool(stored["target_in_generated_subgroup"])
        or antipodal_intersection
        or not bool(certificate["target_in_generated_subgroup"])
        or 2 * len(A) > H_order
    ):
        raise AssertionError("stored finite-exponent state violated the antipodal density boundary")
    return {
        "R": R,
        "K": K,
        "source_state_count": int(stored["source_state_count"]),
        "K_divisor_residue_count": len(A),
        "generated_subgroup_order": H_order,
        "generated_subgroup_index": H_index,
        "twice_divisor_residue_count": 2 * len(A),
        "half_density_deficit": H_order - 2 * len(A),
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Audit every F-type state of the seven complete pressure spectra."""
    source_records = load_finite_records(input_path)
    records_by_prime: dict[int, list[dict[str, int]]] = {
        prime: [] for prime in EXPECTED_PER_PRIME_F_COUNTS
    }
    for prime, stored in source_records:
        records_by_prime[prime].append(audit_record(prime, stored))
    profiles = []
    for prime, records in records_by_prime.items():
        records.sort(key=lambda record: record["R"])
        if len(records) != EXPECTED_PER_PRIME_F_COUNTS[prime]:
            raise AssertionError("finite density profile lost a frozen record")
        digest_rows = [
            (
                record["R"],
                record["K"],
                record["K_divisor_residue_count"],
                record["generated_subgroup_order"],
                record["generated_subgroup_index"],
                record["half_density_deficit"],
            )
            for record in records
        ]
        profiles.append(
            {
                "prime": prime,
                "finite_exponent_R_count": len(records),
                "minimum_twice_divisor_density_numerator": min(
                    record["twice_divisor_residue_count"] for record in records
                ),
                "maximum_half_density_deficit": max(
                    record["half_density_deficit"] for record in records
                ),
                "record_sha256": stable_sha256(digest_rows),
                "records": records,
            }
        )
    all_records = [record for profile in profiles for record in profile["records"]]
    equality_count = sum(
        record["half_density_deficit"] == 0 for record in all_records
    )
    return {
        "arithmetic": (
            "for every frozen finite-exponent state, construct A_R(K) from all divisors of K, "
            "recover the exact support subgroup order from the unit-group logarithmic lattice, "
            "and measure |H_R(K)|-2|A_R(K)|"
        ),
        "scope_note": (
            "This profile quantifies the half-density sufficient-condition gap only on already known F states. "
            "It does not produce a cross-source escape theorem."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "finite_exponent_R_count": len(all_records),
        "half_density_equality_count": equality_count,
        "minimum_half_density_deficit": min(
            record["half_density_deficit"] for record in all_records
        ),
        "maximum_half_density_deficit": max(
            record["half_density_deficit"] for record in all_records
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
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "profiles"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
