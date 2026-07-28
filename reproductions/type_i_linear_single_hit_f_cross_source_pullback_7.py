#!/usr/bin/env python3
"""Audit shared-layer pullbacks on the seven single-hit linear spectra."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-full-spectrum-bgt1-200-results.json"
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-single-hit-f-cross-source-pullback-7-results.json"
)
EXPECTED_INPUT_SHA256 = (
    "5f60c11b255aac289b45d2a4721b233534b7bc29476b76bb5f41efc0917a0196"
)
SINGLE_HIT_PRIMES = (
    67_369,
    878_089,
    13_782_409,
    26_034_649,
    57_399_241,
    152_498_329,
    283_319_689,
)
EXPECTED_F_COUNTS = {
    67_369: 5,
    878_089: 2,
    13_782_409: 9,
    26_034_649: 6,
    57_399_241: 24,
    152_498_329: 12,
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


shared_audit = load_module(
    "single_hit_cross_source_helpers",
    ROOT
    / "reproductions"
    / "type_i_linear_adversarial_core_f_cross_source_pullback_audit_600m.py",
)
block = shared_audit.block
sources = shared_audit.sources


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    payload = "\n".join(",".join(str(value) for value in row) for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def factorization_payload(value: int) -> list[dict[str, int]]:
    return [
        {"prime": int(prime), "exponent": int(exponent)}
        for prime, exponent in sources.exact_factorization(value)
    ]


def checked_records(profile: dict[str, object]) -> list[dict[str, int | str]]:
    prime = int(profile["prime"])
    records = []
    for stored in profile["records"]:
        R = int(stored["R"])
        K = (prime * R + 1) // 4
        if 4 * K != prime * R + 1 or math.gcd(K, R) != 1:
            raise AssertionError("malformed full-spectrum state")
        records.append(
            {"R": R, "K": K, "classification": str(stored["classification"])}
        )
    records.sort(key=lambda record: int(record["R"]))
    if len({int(record["R"]) for record in records}) != len(records):
        raise AssertionError("duplicate source modulus")
    return records


def verify_pairwise_identity(records: list[dict[str, int | str]]) -> int:
    count = 0
    for index, left in enumerate(records):
        for right in records[index + 1 :]:
            R_left = int(left["R"])
            R_right = int(right["R"])
            difference = abs(R_left - R_right)
            if difference == 0 or difference % 4:
                raise AssertionError("source moduli do not differ by four")
            if math.gcd(int(left["K"]), int(right["K"])) != math.gcd(
                int(left["K"]), difference // 4
            ):
                raise AssertionError("cross-modulus gcd identity failed")
            count += 1
    return count


def orientation_record(
    prime: int,
    R: int,
    K: int,
    shared: int,
    a: int,
    s: int,
) -> dict[str, object]:
    if prime != a + s + a * s * R or s % 2 != 1:
        raise AssertionError("invalid directed source")
    lambda_value = 4 if s % 4 == 1 else 2
    eta = 4 // lambda_value
    gamma = (s * R + 1) // lambda_value
    affine = (a * R + 1) // eta
    if gamma * affine != K:
        raise AssertionError("source blocks do not reconstruct K")

    gamma_difference = shared_audit.centered_difference(gamma, R)
    affine_difference = shared_audit.centered_difference(affine, R)
    shared_difference = shared_audit.centered_difference(shared, R)
    target_pullback = {
        (-pow(residue, -1, R)) % R for residue in gamma_difference
    }
    raw = sorted(shared_difference & target_pullback)
    alignment = sorted(affine_difference & target_pullback)
    if alignment:
        raise AssertionError(
            f"F state has direct block alignment: p={prime}, R={R}, "
            f"a={a}, s={s}, residues={alignment}"
        )

    certificate = block.subgroup_certificate(affine, R)
    membership_cache: dict[tuple[int, int], list[int]] = {}
    subgroup = sorted(
        residue
        for residue in raw
        if block.residue_in_subgroup(residue, certificate, membership_cache)
    )
    finite = sorted(set(subgroup) & affine_difference)
    if finite:
        raise AssertionError(
            f"shared pullback reached finite affine box: p={prime}, R={R}, "
            f"a={a}, s={s}, residues={finite}"
        )

    result: dict[str, object] = {
        "a": a,
        "s": s,
        "gamma": gamma,
        "affine_block": affine,
        "gamma_factorization": factorization_payload(gamma),
        "affine_factorization": factorization_payload(affine),
        "shared_layer": shared,
        "shared_difference_residue_count": len(shared_difference),
        "target_pullback_count": len(target_pullback),
        "raw_shared_pullback_count": len(raw),
        "subgroup_shared_pullback_count": len(subgroup),
        "finite_shared_alignment_count": len(finite),
    }
    if raw:
        result["raw_shared_pullback_residues"] = raw
    if subgroup:
        factors = [
            (int(item["prime"]), int(item["exponent"]))
            for item in result["affine_factorization"]
        ]
        overflow_witnesses = {}
        for residue in subgroup:
            overflow, vector = shared_audit.minimum_exponent_overflow(
                residue, R, factors
            )
            overflow_witnesses[str(residue)] = {
                "minimum_extra_exponent": overflow,
                "vector": list(vector),
            }
        result["subgroup_shared_pullback_residues"] = subgroup
        result["subgroup_pullback_exponent_overflow"] = overflow_witnesses
    return result


def run_audit(path: Path = INPUT) -> dict[str, object]:
    if file_sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("single-hit full-spectrum input changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    profiles_by_prime = {int(profile["prime"]): profile for profile in payload["records"]}
    if set(profiles_by_prime) & set(SINGLE_HIT_PRIMES) != set(SINGLE_HIT_PRIMES):
        raise AssertionError("single-hit pressure profile is incomplete")

    profiles = []
    all_orientations: list[dict[str, object]] = []
    digest_rows: list[tuple[int, ...]] = []
    pair_count = 0
    raw_orientation_count = 0
    subgroup_orientation_count = 0
    finite_alignment_count = 0
    raw_residue_count = 0
    subgroup_residue_count = 0
    overflow_distribution: dict[str, int] = {}

    for prime in SINGLE_HIT_PRIMES:
        source_profile = profiles_by_prime[prime]
        records = checked_records(source_profile)
        pair_count += verify_pairwise_identity(records)
        _, states_by_R = sources.enumerate_linear_source_states(prime)
        F_records = [
            record
            for record in records
            if record["classification"] == "finite_exponent"
        ]
        if len(F_records) != EXPECTED_F_COUNTS[prime]:
            raise AssertionError(f"F-state count changed for p={prime}")
        moduli = [int(record["R"]) for record in records]
        F_rows = []
        for record in F_records:
            R = int(record["R"])
            K = int(record["K"])
            shared, difference_lcm = shared_audit.shared_layer(K, R, moduli)
            orientations = [
                orientation_record(prime, R, K, shared, int(a), int(s))
                for a, s in states_by_R[R]
            ]
            raw_orientation_count += sum(
                int(row["raw_shared_pullback_count"] > 0) for row in orientations
            )
            subgroup_orientation_count += sum(
                int(row["subgroup_shared_pullback_count"] > 0)
                for row in orientations
            )
            finite_alignment_count += sum(
                int(row["finite_shared_alignment_count"] > 0)
                for row in orientations
            )
            raw_residue_count += sum(
                int(row["raw_shared_pullback_count"]) for row in orientations
            )
            subgroup_residue_count += sum(
                int(row["subgroup_shared_pullback_count"]) for row in orientations
            )
            for row in orientations:
                for witness in row.get(
                    "subgroup_pullback_exponent_overflow", {}
                ).values():
                    key = str(int(witness["minimum_extra_exponent"]))
                    overflow_distribution[key] = (
                        overflow_distribution.get(key, 0) + 1
                    )
                digest_rows.append(
                    (
                        prime,
                        R,
                        int(row["a"]),
                        int(row["s"]),
                        shared,
                        int(row["shared_difference_residue_count"]),
                        int(row["raw_shared_pullback_count"]),
                        int(row["subgroup_shared_pullback_count"]),
                        int(row["finite_shared_alignment_count"]),
                    )
                )
                all_orientations.append({"prime": prime, "R": R, "K": K, **row})
            F_rows.append(
                {
                    "R": R,
                    "K": K,
                    "shared_difference_lcm": difference_lcm,
                    "shared_layer": shared,
                    "shared_layer_factorization": factorization_payload(shared),
                    "directed_orientation_count": len(orientations),
                    "raw_shared_pullback_orientation_count": sum(
                        int(row["raw_shared_pullback_count"] > 0)
                        for row in orientations
                    ),
                    "subgroup_shared_pullback_orientation_count": sum(
                        int(row["subgroup_shared_pullback_count"] > 0)
                        for row in orientations
                    ),
                    "orientations": orientations,
                }
            )
        profiles.append(
            {
                "prime": prime,
                "finite_exponent_R_count": len(F_rows),
                "directed_orientation_count": sum(
                    int(row["directed_orientation_count"]) for row in F_rows
                ),
                "raw_shared_pullback_orientation_count": sum(
                    int(row["raw_shared_pullback_orientation_count"])
                    for row in F_rows
                ),
                "subgroup_shared_pullback_orientation_count": sum(
                    int(row["subgroup_shared_pullback_orientation_count"])
                    for row in F_rows
                ),
                "records": F_rows,
            }
        )

    if len(all_orientations) != 110:
        raise AssertionError("directed orientation total changed")
    if finite_alignment_count != 0:
        raise AssertionError("finite shared alignment unexpectedly appeared")

    overflow_keys = sorted(overflow_distribution, key=int)
    return {
        "arithmetic": (
            "for each finite-exponent F state in the seven single-hit complete "
            "linear spectra, compute the exact cross-source shared layer S_R "
            "and compare its centered difference spectrum with the block target "
            "pullback; measure the least affine exponent overflow for subgroup "
            "visible classes"
        ),
        "scope_note": (
            "This is a finite profile of all 71 F states and 110 directed sources "
            "in the seven single-hit spectra. It rules out direct shared-layer "
            "block alignment in this scope, but does not prove a universal selector "
            "or an exponent-transfer/descent lemma."
        ),
        "input_artifact": path.name,
        "input_sha256": file_sha256(path),
        "prime_count": len(profiles),
        "finite_exponent_R_count": sum(
            int(profile["finite_exponent_R_count"]) for profile in profiles
        ),
        "directed_orientation_count": len(all_orientations),
        "pairwise_gcd_identity_count": pair_count,
        "raw_shared_pullback_orientation_count": raw_orientation_count,
        "subgroup_shared_pullback_orientation_count": subgroup_orientation_count,
        "finite_shared_alignment_orientation_count": finite_alignment_count,
        "raw_shared_pullback_residue_count": raw_residue_count,
        "subgroup_shared_pullback_residue_count": subgroup_residue_count,
        "subgroup_pullback_exponent_overflow_distribution": {
            key: overflow_distribution[key] for key in overflow_keys
        },
        "minimum_subgroup_pullback_exponent_overflow": int(overflow_keys[0]),
        "maximum_subgroup_pullback_exponent_overflow": int(overflow_keys[-1]),
        "record_sha256": stable_sha256(digest_rows),
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
            {key: value for key, value in result.items() if key != "profiles"},
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
