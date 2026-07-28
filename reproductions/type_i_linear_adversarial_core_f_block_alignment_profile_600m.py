#!/usr/bin/env python3
"""Profile the block-level pigeonhole margin at all 45 adversarial F states."""

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
DIFFERENCE_SCRIPT = (
    ROOT / "reproductions" / "type_i_linear_adversarial_core_f_difference_profile_600m.py"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-adversarial-core-f-block-alignment-profile-600m-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
ADVERSARIAL_PRIMES = (878_089, 26_034_649, 57_399_241, 283_319_689)
EXPECTED_F_COUNTS = {
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


near = load_module(
    "adversarial_core_f_near_alignment_sources",
    ROOT / "reproductions" / "type_i_linear_f_near_saturation_block_alignment_600m.py",
)
difference = near.difference
sources = near.sources


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    payload = "\n".join(",".join(str(value) for value in row) for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def centered_difference(value: int, modulus: int) -> set[int]:
    residues = {1}
    for prime, exponent in sources.exact_factorization(value):
        powers = {
            pow(prime, coordinate, modulus)
            for coordinate in range(-exponent, exponent + 1)
        }
        residues = {
            left * right % modulus for left in residues for right in powers
        }
    return residues


def subgroup_certificate(value: int, modulus: int) -> dict[str, object]:
    return sources.unit_group_subgroup_certificate(
        sources.exact_factorization(value), modulus
    )


def residue_log_vector(residue: int, certificate: dict[str, object]) -> list[int]:
    vector = []
    value = residue
    for component in certificate["components"]:
        if not isinstance(component, dict):
            raise AssertionError("subgroup certificate component is malformed")
        modulus = int(component["modulus"])
        root = int(component["primitive_root"])
        local_residue = value % modulus
        if math.gcd(local_residue, modulus) != 1:
            raise AssertionError("target residue is not a unit")
        logarithm = int(sympy.discrete_log(modulus, local_residue, root))
        if pow(root, logarithm, modulus) != local_residue:
            raise AssertionError("residue logarithm did not reconstruct")
        vector.append(logarithm)
    return vector


def residue_in_subgroup(
    residue: int,
    certificate: dict[str, object],
    cache: dict[tuple[int, int], list[int]],
) -> bool:
    components = certificate["components"]
    if not isinstance(components, list) or not components:
        raise AssertionError("subgroup certificate has no components")
    modulus = math.prod(int(component["modulus"]) for component in components)
    key = (modulus, residue % modulus)
    vector = cache.setdefault(key, residue_log_vector(residue, certificate))
    hnf = Matrix(certificate["column_lattice_hermite_normal_form"])
    return sources.solve_upper_hnf_membership(hnf, vector)[0]


def factorization_payload(value: int) -> list[dict[str, int]]:
    return [
        {"prime": int(prime), "exponent": int(exponent)}
        for prime, exponent in sources.exact_factorization(value)
    ]


def orientation_record(
    prime: int,
    modulus: int,
    a: int,
    s: int,
    cache: dict[tuple[int, int], list[int]],
) -> dict[str, object]:
    K = (prime * modulus + 1) // 4
    if (
        prime != a + s + a * s * modulus
        or s % 2 != 1
        or modulus % 4 != 3
        or (prime * modulus + 1) % 4
    ):
        raise AssertionError("invalid directed source")
    lambda_value = 4 if s % 4 == 1 else 2
    eta = 4 // lambda_value
    gamma = (s * modulus + 1) // lambda_value
    affine = (a * modulus + 1) // eta
    if gamma * affine != K:
        raise AssertionError("source blocks did not reconstruct K")

    gamma_difference = centered_difference(gamma, modulus)
    affine_difference = centered_difference(affine, modulus)
    gamma_certificate = subgroup_certificate(gamma, modulus)
    affine_certificate = subgroup_certificate(affine, modulus)
    gamma_order, gamma_index = difference.generated_subgroup_order(gamma_certificate)
    affine_order, affine_index = difference.generated_subgroup_order(affine_certificate)
    target_pullback = {
        (-pow(residue, -1, modulus)) % modulus
        for residue in gamma_difference
    }
    target_pullback_in_affine_subgroup = {
        residue
        for residue in target_pullback
        if residue_in_subgroup(residue, affine_certificate, cache)
    }
    alignment = sorted(target_pullback & affine_difference)
    margin = (
        affine_order
        - len(affine_difference)
        - len(target_pullback_in_affine_subgroup)
    )
    if alignment:
        raise AssertionError(
            f"an F state has a target alignment: p={prime}, R={modulus}, "
            f"a={a}, s={s}, alignment={alignment}"
        )
    if margin < 0:
        raise AssertionError(
            f"the block pigeonhole necessary condition failed: p={prime}, "
            f"R={modulus}, a={a}, s={s}, margin={margin}, "
            f"H_L={affine_order}, D_L={len(affine_difference)}, "
            f"required={len(target_pullback_in_affine_subgroup)}"
        )

    return {
        "a": a,
        "s": s,
        "K": K,
        "lambda": lambda_value,
        "eta": eta,
        "gamma": gamma,
        "gamma_factorization": factorization_payload(gamma),
        "affine_block": affine,
        "affine_factorization": factorization_payload(affine),
        "D_gamma_residue_count": len(gamma_difference),
        "D_affine_residue_count": len(affine_difference),
        "H_gamma_order": gamma_order,
        "H_gamma_index": gamma_index,
        "H_affine_order": affine_order,
        "H_affine_index": affine_index,
        "target_pullback_count": len(target_pullback),
        "target_pullback_in_affine_subgroup_count": len(
            target_pullback_in_affine_subgroup
        ),
        "target_pullback_in_affine_subgroup_residues": sorted(
            target_pullback_in_affine_subgroup
        )
        if margin <= 0
        else [],
        "alignment_residues": alignment,
        "alignment_pigeonhole_margin": margin,
    }


def run_audit() -> dict[str, object]:
    input_path = difference.INPUT
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full B>1-spectrum input changed")
    stored_by_prime = difference.load_finite_records(input_path)
    difference_payload = json.loads(
        difference.DEFAULT_OUTPUT.read_text(encoding="utf-8")
    )
    if difference_payload["input_sha256"] != EXPECTED_INPUT_SHA256:
        raise AssertionError("the difference-spectrum artifact input changed")
    difference_by_state = {
        (int(profile["prime"]), int(record["R"])): record
        for profile in difference_payload["profiles"]
        for record in profile["records"]
    }
    cache: dict[tuple[int, int], list[int]] = {}
    profiles = []
    all_records = []
    for prime in ADVERSARIAL_PRIMES:
        _, states_by_R = sources.enumerate_linear_source_states(prime)
        records = []
        for stored in stored_by_prime[prime]:
            modulus = int(stored["R"])
            states = states_by_R[modulus]
            orientations = [
                orientation_record(prime, modulus, int(a), int(s), cache)
                for a, s in states
            ]
            records.append(
                {
                    "prime": prime,
                    "R": modulus,
                    "K": int(stored["K"]),
                    "source_state_count": len(orientations),
                    "full_difference_residue_count": int(
                        difference_by_state[(prime, modulus)][
                            "difference_residue_count"
                        ]
                    ),
                    "orientations": orientations,
                }
            )
            all_records.extend(orientations)
        if len(records) != EXPECTED_F_COUNTS[prime]:
            raise AssertionError("F-state count changed")
        profiles.append(
            {
                "prime": prime,
                "finite_exponent_R_count": len(records),
                "directed_orientation_count": sum(
                    int(record["source_state_count"]) for record in records
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
                "records": records,
            }
        )

    digest_rows = [
        (
            int(record["prime"]),
            int(record["R"]),
            int(orientation["a"]),
            int(orientation["s"]),
            int(orientation["H_gamma_order"]),
            int(orientation["H_affine_order"]),
            int(orientation["D_gamma_residue_count"]),
            int(orientation["D_affine_residue_count"]),
            int(orientation["target_pullback_in_affine_subgroup_count"]),
            int(orientation["alignment_pigeonhole_margin"]),
        )
        for profile in profiles
        for record in profile["records"]
        for orientation in record["orientations"]
    ]
    return {
        "arithmetic": (
            "for K=gamma*L, the target -1 requires an intersection between "
            "D(L) and the inverse-negative pullbacks of D(gamma); if the "
            "two subsets inside H_L have total size greater than |H_L|, "
            "the target is forced"
        ),
        "scope_note": (
            "This is a complete block-level profile of all 45 F states and 69 "
            "directed sources in the four adversarial cores. It proves a finite "
            "necessary-boundary profile, not a cross-source selector theorem."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "prime_count": len(ADVERSARIAL_PRIMES),
        "finite_exponent_R_count": sum(
            int(profile["finite_exponent_R_count"]) for profile in profiles
        ),
        "directed_orientation_count": sum(
            int(profile["directed_orientation_count"]) for profile in profiles
        ),
        "target_alignment_hit_count": sum(
            len(orientation["alignment_residues"])
            for profile in profiles
            for record in profile["records"]
            for orientation in record["orientations"]
        ),
        "minimum_alignment_pigeonhole_margin": min(
            int(orientation["alignment_pigeonhole_margin"])
            for orientation in all_records
        ),
        "zero_alignment_pigeonhole_margin_count": sum(
            int(orientation["alignment_pigeonhole_margin"] == 0)
            for orientation in all_records
        ),
        "positive_margin_minimum": min(
            int(orientation["alignment_pigeonhole_margin"])
            for orientation in all_records
            if int(orientation["alignment_pigeonhole_margin"]) > 0
        ),
        "nonvacuous_zero_margin_count": sum(
            int(
                orientation["alignment_pigeonhole_margin"] == 0
                and orientation["target_pullback_in_affine_subgroup_count"] > 0
            )
            for orientation in all_records
        ),
        "record_sha256": stable_sha256(digest_rows),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit()
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
