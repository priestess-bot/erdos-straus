#!/usr/bin/env python3
"""Audit block-level antipodal alignment at near-saturated F states."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
DIFFERENCE_SCRIPT = (
    ROOT / "reproductions" / "type_i_linear_adversarial_core_f_difference_profile_600m.py"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-f-near-saturation-block-alignment-600m-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
NEAR_SATURATION_DEFICIT_BOUND = 100


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


difference = load_module(
    "near_saturation_difference_profile",
    DIFFERENCE_SCRIPT,
)
sources = difference.sources


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    payload = "\n".join(",".join(str(value) for value in row) for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def factorization_payload(value: int) -> list[dict[str, int]]:
    factors = sources.exact_factorization(value)
    if math.prod(prime**exponent for prime, exponent in factors) != value:
        raise AssertionError("factorization did not reconstruct")
    return [
        {"prime": int(prime), "exponent": int(exponent)}
        for prime, exponent in factors
    ]


def divisor_residues(value: int, modulus: int) -> set[int]:
    return {int(divisor) % modulus for divisor in sympy.divisors(value)}


def difference_set(residues: set[int], modulus: int) -> set[int]:
    return {
        (left * pow(right, -1, modulus)) % modulus
        for left in residues
        for right in residues
    }


def generated_subgroup(residues: set[int], modulus: int) -> set[int]:
    generators = {residue % modulus for residue in residues}
    subgroup = {1}
    frontier = [1]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            product = current * generator % modulus
            if product not in subgroup:
                subgroup.add(product)
                frontier.append(product)
    return subgroup


def orientation_record(
    prime: int,
    modulus: int,
    K: int,
    a: int,
    s: int,
    full_difference: set[int],
) -> dict[str, object]:
    if (
        prime != a + s + a * s * modulus
        or s % 2 != 1
        or modulus % 4 != 3
        or K != (prime * modulus + 1) // 4
    ):
        raise AssertionError("invalid directed linear source")

    lambda_value = 4 if s % 4 == 1 else 2
    eta = 4 // lambda_value
    gamma, gamma_remainder = divmod(s * modulus + 1, lambda_value)
    affine, affine_remainder = divmod(a * modulus + 1, eta)
    if gamma_remainder or affine_remainder or gamma * affine != K:
        raise AssertionError("source blocks did not reconstruct K")

    gamma_residues = divisor_residues(gamma, modulus)
    affine_residues = divisor_residues(affine, modulus)
    K_residues = divisor_residues(K, modulus)
    gamma_difference = difference_set(gamma_residues, modulus)
    affine_difference = difference_set(affine_residues, modulus)
    gamma_subgroup = generated_subgroup(gamma_difference, modulus)
    affine_subgroup = generated_subgroup(affine_difference, modulus)
    product_difference = {
        (left * right) % modulus
        for left in gamma_difference
        for right in affine_difference
    }
    product_divisors = {
        (left * right) % modulus
        for left in gamma_residues
        for right in affine_residues
    }
    target_pullback = {
        (-pow(residue, -1, modulus)) % modulus
        for residue in gamma_difference
    }
    target_pullback_in_affine_subgroup = target_pullback & affine_subgroup
    alignment = sorted(target_pullback & affine_difference)
    alignment_pigeonhole_margin = (
        len(affine_subgroup)
        - len(affine_difference)
        - len(target_pullback_in_affine_subgroup)
    )
    if product_divisors != K_residues:
        raise AssertionError("A(K) did not factor through the two blocks")
    if product_difference != full_difference:
        raise AssertionError("D(K) did not factor through the two block differences")
    if modulus - 1 in gamma_difference or modulus - 1 in affine_difference:
        raise AssertionError("an F-state block already contains the target")
    if alignment:
        raise AssertionError("F-state target unexpectedly aligned across blocks")
    if alignment_pigeonhole_margin < 0:
        raise AssertionError("F-state violates the block pigeonhole bound")

    return {
        "a": a,
        "s": s,
        "lambda": lambda_value,
        "eta": eta,
        "gamma": gamma,
        "gamma_factorization": factorization_payload(gamma),
        "affine_block": affine,
        "affine_factorization": factorization_payload(affine),
        "gcd_gamma_affine": math.gcd(gamma, affine),
        "A_gamma_residue_count": len(gamma_residues),
        "A_affine_residue_count": len(affine_residues),
        "D_gamma_residue_count": len(gamma_difference),
        "D_affine_residue_count": len(affine_difference),
        "H_gamma_residue_count": len(gamma_subgroup),
        "H_affine_residue_count": len(affine_subgroup),
        "D_product_residue_count": len(product_difference),
        "D_full_residue_count": len(full_difference),
        "gamma_target_in_difference": False,
        "affine_target_in_difference": False,
        "target_pullback_residues": sorted(target_pullback),
        "target_pullback_in_affine_subgroup_residues": sorted(
            target_pullback_in_affine_subgroup
        ),
        "target_pullback_in_affine_subgroup_count": len(
            target_pullback_in_affine_subgroup
        ),
        "alignment_pigeonhole_margin": alignment_pigeonhole_margin,
        "target_alignment_residues": alignment,
        "target_alignment_count": len(alignment),
        "D_gamma_residues": sorted(gamma_difference),
        "D_affine_residues": sorted(affine_difference),
    }


def audit_record(
    prime: int,
    stored: dict[str, object],
    near: dict[str, object],
) -> dict[str, object]:
    modulus = int(stored["R"])
    K = int(stored["K"])
    if int(near["prime"]) != prime or int(near["R"]) != modulus:
        raise AssertionError("near-saturation record is mismatched")
    if int(near["difference_density_deficit"]) > NEAR_SATURATION_DEFICIT_BOUND:
        raise AssertionError("record is outside the near-saturation boundary")

    K_residues = divisor_residues(K, modulus)
    full_difference = difference_set(K_residues, modulus)
    if len(full_difference) != int(near["difference_residue_count"]):
        raise AssertionError("stored full difference count changed")
    if (modulus - 1) in full_difference:
        raise AssertionError("near-saturated record is not F-type")
    certificate = sources.unit_group_subgroup_certificate(
        sources.exact_factorization(K), modulus
    )
    subgroup_order, subgroup_index = difference.generated_subgroup_order(certificate)
    if subgroup_order != int(near["generated_subgroup_order"]):
        raise AssertionError("stored generated subgroup order changed")
    if subgroup_index == 1 and len(near["difference_missing_residues"]) != (
        subgroup_order - len(full_difference)
    ):
        raise AssertionError("stored full-unit missing classes changed")

    _, states_by_R = sources.enumerate_linear_source_states(prime)
    states = states_by_R.get(modulus)
    if not states:
        raise AssertionError("source state for near-saturated R is missing")
    orientations = [
        orientation_record(prime, modulus, K, int(a), int(s), full_difference)
        for a, s in states
    ]
    product_counts = {int(row["D_product_residue_count"]) for row in orientations}
    if product_counts != {len(full_difference)}:
        raise AssertionError("block product count is orientation-dependent")
    return {
        "prime": prime,
        "R": modulus,
        "K": K,
        "generated_subgroup_order": subgroup_order,
        "generated_subgroup_index": subgroup_index,
        "D_full_residue_count": len(full_difference),
        "D_full_density_deficit": int(near["difference_density_deficit"]),
        "D_full_missing_residues": list(near["difference_missing_residues"]),
        "source_state_count": len(states),
        "orientation_count": len(orientations),
        "target_alignment_count": sum(
            int(row["target_alignment_count"]) for row in orientations
        ),
        "orientations": orientations,
    }


def run_audit() -> dict[str, object]:
    input_path = difference.INPUT
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full B>1-spectrum input changed")
    base = difference.run_audit(input_path)
    near_records = base["near_saturation_records"]
    selected = [
        row
        for row in near_records
        if int(row["difference_density_deficit"]) <= NEAR_SATURATION_DEFICIT_BOUND
    ]
    selected.sort(key=lambda row: (int(row["prime"]), int(row["R"])))
    stored_by_prime = difference.load_finite_records(input_path)
    records = []
    for row in selected:
        prime = int(row["prime"])
        stored = next(
            record
            for record in stored_by_prime[prime]
            if int(record["R"]) == int(row["R"])
        )
        records.append(audit_record(prime, stored, row))

    digest_rows = [
        (
            int(record["prime"]),
            int(record["R"]),
            int(record["K"]),
            int(record["D_full_residue_count"]),
            int(record["orientation_count"]),
            int(record["target_alignment_count"]),
        )
        for record in records
    ]
    return {
        "arithmetic": (
            "for K=gamma*L, A(K)=A(gamma)A(L) and D(K)=D(gamma)D(L); "
            "the target -1 is present exactly when D(L) intersects "
            "{-x^(-1): x in D(gamma)}. In particular, if the required "
            "pullbacks inside H_L plus D(L) exceed |H_L|, the target is forced."
        ),
        "scope_note": (
            "This is a complete block-level audit of the six F states whose full "
            "difference-set deficit is at most 100 among the four adversarial cores. "
            "The empty alignment intersections are a finite negative boundary, not a "
            "cross-source selector theorem."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "near_saturation_deficit_bound": NEAR_SATURATION_DEFICIT_BOUND,
        "near_saturation_state_count": len(records),
        "directed_orientation_count": sum(
            int(record["orientation_count"]) for record in records
        ),
        "target_alignment_hit_count": sum(
            int(record["target_alignment_count"]) for record in records
        ),
        "minimum_alignment_pigeonhole_margin": min(
            int(orientation["alignment_pigeonhole_margin"])
            for record in records
            for orientation in record["orientations"]
        ),
        "zero_alignment_pigeonhole_margin_count": sum(
            int(orientation["alignment_pigeonhole_margin"] == 0)
            for record in records
            for orientation in record["orientations"]
        ),
        "block_identity_verified_count": len(records),
        "record_sha256": stable_sha256(digest_rows),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key != "records"},
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
