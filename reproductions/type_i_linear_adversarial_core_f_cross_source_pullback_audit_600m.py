#!/usr/bin/env python3
"""Audit cross-source shared-layer pullbacks at all adversarial F states."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import itertools
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
CLASSIFICATION_INPUT = (
    ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
)
BLOCK_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-adversarial-core-f-block-alignment-profile-600m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-adversarial-core-f-cross-source-pullback-audit-600m-results.json"
)

EXPECTED_CLASSIFICATION_SHA256 = (
    "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
)
EXPECTED_BLOCK_SHA256 = (
    "608b859ea13700fea5e5096d0268588873500ef2a362ad10169d0f9d8eb1a586"
)
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


block = load_module(
    "adversarial_core_f_block_alignment_for_cross_source_audit",
    ROOT
    / "reproductions"
    / "type_i_linear_adversarial_core_f_block_alignment_profile_600m.py",
)
sources = block.sources


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


def centered_difference(value: int, modulus: int) -> set[int]:
    """Compute D_R(value) from the exact prime-exponent box."""
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


def minimum_exponent_overflow(
    residue: int,
    modulus: int,
    factors: list[tuple[int, int]],
    max_overflow: int = 32,
) -> tuple[int, tuple[int, ...]]:
    """Find the least extra coordinate budget representing one subgroup class."""
    for overflow in range(max_overflow + 1):
        ranges = [
            range(-exponent - overflow, exponent + overflow + 1)
            for _, exponent in factors
        ]
        for vector in itertools.product(*ranges):
            if overflow == 0 and any(
                abs(coordinate) > exponent
                for coordinate, (_, exponent) in zip(vector, factors)
            ):
                continue
            value = 1
            for (prime, _), coordinate in zip(factors, vector):
                value = value * pow(prime, coordinate, modulus) % modulus
            if value == residue:
                if overflow == 0:
                    raise AssertionError(
                        "subgroup pullback unexpectedly lies in finite box"
                    )
                return overflow, tuple(int(coordinate) for coordinate in vector)
    raise AssertionError("minimum exponent overflow exceeds audit cap")


def checked_classification_records(
    payload: dict[str, object], prime: int
) -> list[dict[str, int | str]]:
    profiles = {
        int(profile["prime"]): profile for profile in payload["profiles"]
    }
    if prime not in profiles:
        raise AssertionError(f"missing adversarial prime {prime}")
    profile = profiles[prime]
    records = []
    for record in profile["records"]:
        R = int(record["R"])
        K = int(record["K"])
        if 4 * K != prime * R + 1 or math.gcd(K, R) != 1:
            raise AssertionError("malformed source record")
        records.append(
            {
                "R": R,
                "K": K,
                "classification": str(record["classification"]),
            }
        )
    records.sort(key=lambda record: int(record["R"]))
    if len({int(record["R"]) for record in records}) != len(records):
        raise AssertionError("duplicate source modulus")
    return records


def verify_pairwise_identity(
    records: list[dict[str, int | str]],
) -> int:
    count = 0
    for index, left in enumerate(records):
        for right in records[index + 1 :]:
            R_left = int(left["R"])
            R_right = int(right["R"])
            difference = abs(R_left - R_right)
            if difference == 0 or difference % 4:
                raise AssertionError("source moduli do not differ by four")
            K_left = int(left["K"])
            K_right = int(right["K"])
            if math.gcd(K_left, K_right) != math.gcd(
                K_left, difference // 4
            ):
                raise AssertionError("cross-modulus gcd identity failed")
            count += 1
    return count


def shared_layer(K: int, R: int, moduli: list[int]) -> tuple[int, int]:
    """Return S_R and J_R from all other source moduli."""
    difference_lcm = 1
    for other in moduli:
        if other == R:
            continue
        difference_lcm = math.lcm(difference_lcm, abs(R - other) // 4)
    return math.gcd(K, difference_lcm), difference_lcm


def orientation_record(
    prime: int,
    R: int,
    K: int,
    shared: int,
    orientation: dict[str, object],
) -> dict[str, object]:
    gamma = int(orientation["gamma"])
    affine = int(orientation["affine_block"])
    gamma_difference = centered_difference(gamma, R)
    affine_difference = centered_difference(affine, R)
    shared_difference = centered_difference(shared, R)
    target_pullback = {
        (-pow(residue, -1, R)) % R for residue in gamma_difference
    }
    raw_intersection = sorted(shared_difference & target_pullback)

    affine_certificate = block.subgroup_certificate(affine, R)
    membership_cache: dict[tuple[int, int], list[int]] = {}
    subgroup_intersection = sorted(
        residue
        for residue in raw_intersection
        if block.residue_in_subgroup(
            residue, affine_certificate, membership_cache
        )
    )
    finite_intersection = sorted(set(subgroup_intersection) & affine_difference)
    actual_alignment = sorted(set(target_pullback) & affine_difference)
    stored_alignment = sorted(int(value) for value in orientation["alignment_residues"])
    if actual_alignment != stored_alignment:
        raise AssertionError("block alignment artifact is inconsistent")
    if finite_intersection:
        raise AssertionError(
            "a shared-layer pullback reached the finite affine box: "
            f"p={prime}, R={R}, a={orientation['a']}, s={orientation['s']}"
        )

    result: dict[str, object] = {
        "a": int(orientation["a"]),
        "s": int(orientation["s"]),
        "gamma": gamma,
        "affine_block": affine,
        "shared_layer": shared,
        "shared_layer_factorization": factorization_payload(shared),
        "shared_difference_residue_count": len(shared_difference),
        "target_pullback_count": len(target_pullback),
        "raw_shared_pullback_count": len(raw_intersection),
        "subgroup_shared_pullback_count": len(subgroup_intersection),
        "finite_shared_alignment_count": len(finite_intersection),
        "block_alignment_count": len(actual_alignment),
        "alignment_pigeonhole_margin": int(
            orientation["alignment_pigeonhole_margin"]
        ),
    }
    affine_factors = [
        (int(item["prime"]), int(item["exponent"]))
        for item in orientation["affine_factorization"]
    ]
    if subgroup_intersection:
        overflow_witnesses = {}
        for residue in subgroup_intersection:
            overflow, vector = minimum_exponent_overflow(
                residue, R, affine_factors
            )
            overflow_witnesses[str(residue)] = {
                "minimum_extra_exponent": overflow,
                "vector": list(vector),
            }
        result["affine_factorization"] = [
            {"prime": prime, "exponent": exponent}
            for prime, exponent in affine_factors
        ]
        result["subgroup_pullback_exponent_overflow"] = overflow_witnesses
    if raw_intersection:
        result["raw_shared_pullback_residues"] = raw_intersection
    if subgroup_intersection:
        result["subgroup_shared_pullback_residues"] = subgroup_intersection
    return result


def run_audit(
    classification_path: Path = CLASSIFICATION_INPUT,
    block_path: Path = BLOCK_INPUT,
) -> dict[str, object]:
    if file_sha256(classification_path) != EXPECTED_CLASSIFICATION_SHA256:
        raise AssertionError("classification input changed")
    if file_sha256(block_path) != EXPECTED_BLOCK_SHA256:
        raise AssertionError("block-alignment artifact changed")

    classification = json.loads(classification_path.read_text(encoding="utf-8"))
    block_payload = json.loads(block_path.read_text(encoding="utf-8"))
    if block_payload["input_sha256"] != EXPECTED_CLASSIFICATION_SHA256:
        raise AssertionError("block artifact points to a different input")
    if block_payload["finite_exponent_R_count"] != 45:
        raise AssertionError("F-state count changed")
    if block_payload["directed_orientation_count"] != 69:
        raise AssertionError("orientation count changed")

    block_profiles = {
        int(profile["prime"]): profile for profile in block_payload["profiles"]
    }
    all_records: list[dict[str, object]] = []
    profiles: list[dict[str, object]] = []
    pair_count = 0
    raw_orientation_count = 0
    subgroup_orientation_count = 0
    finite_orientation_count = 0
    raw_residue_count = 0
    subgroup_residue_count = 0
    overflow_distribution: dict[str, int] = {}
    digest_rows: list[tuple[int, ...]] = []

    for prime in ADVERSARIAL_PRIMES:
        records = checked_classification_records(classification, prime)
        pair_count += verify_pairwise_identity(records)
        moduli = [int(record["R"]) for record in records]
        block_profile = block_profiles.get(prime)
        if block_profile is None:
            raise AssertionError(f"missing block profile for {prime}")
        f_records = {
            int(record["R"]): record for record in block_profile["records"]
        }
        F_records = [
            record
            for record in records
            if record["classification"] == "finite_exponent"
        ]
        if len(F_records) != EXPECTED_F_COUNTS[prime]:
            raise AssertionError("per-prime F-state count changed")
        prime_rows = []
        for record in F_records:
            R = int(record["R"])
            K = int(record["K"])
            shared, difference_lcm = shared_layer(K, R, moduli)
            block_record = f_records.get(R)
            if block_record is None:
                raise AssertionError("F state missing from block artifact")
            orientations = []
            for orientation in block_record["orientations"]:
                row = orientation_record(prime, R, K, shared, orientation)
                row["prime"] = prime
                row["R"] = R
                row["K"] = K
                row["shared_difference_lcm"] = difference_lcm
                orientations.append(row)
                raw_count = int(row["raw_shared_pullback_count"])
                subgroup_count = int(row["subgroup_shared_pullback_count"])
                finite_count = int(row["finite_shared_alignment_count"])
                raw_orientation_count += bool(raw_count)
                subgroup_orientation_count += bool(subgroup_count)
                finite_orientation_count += bool(finite_count)
                raw_residue_count += raw_count
                subgroup_residue_count += subgroup_count
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
                        raw_count,
                        subgroup_count,
                        finite_count,
                        int(row["block_alignment_count"]),
                    )
                )
                all_records.append(row)
            prime_rows.append(
                {
                    "R": R,
                    "K": K,
                    "shared_difference_lcm": difference_lcm,
                    "shared_layer": shared,
                    "shared_layer_factorization": factorization_payload(shared),
                    "orientations": orientations,
                }
            )
        profiles.append(
            {
                "prime": prime,
                "finite_exponent_R_count": len(prime_rows),
                "directed_orientation_count": sum(
                    len(row["orientations"]) for row in prime_rows
                ),
                "raw_shared_pullback_orientation_count": sum(
                    int(row["raw_shared_pullback_count"] > 0)
                    for row in all_records
                    if int(row["R"]) in {int(x["R"]) for x in prime_rows}
                    and int(row["K"]) == (prime * int(row["R"]) + 1) // 4
                ),
                "subgroup_shared_pullback_orientation_count": sum(
                    int(row["subgroup_shared_pullback_count"] > 0)
                    for row in all_records
                    if int(row["R"]) in {int(x["R"]) for x in prime_rows}
                    and int(row["K"]) == (prime * int(row["R"]) + 1) // 4
                ),
                "records": prime_rows,
            }
        )

    if len(all_records) != 69:
        raise AssertionError("orientation total changed")
    if finite_orientation_count != 0:
        raise AssertionError("finite shared alignment unexpectedly appeared")
    if raw_orientation_count != 6:
        raise AssertionError("raw shared pullback count changed")
    if subgroup_orientation_count != 4:
        raise AssertionError("subgroup shared pullback count changed")
    if raw_residue_count != 32 or subgroup_residue_count != 14:
        raise AssertionError(
            "shared pullback residue totals changed: "
            f"raw={raw_residue_count}, subgroup={subgroup_residue_count}"
        )

    latent_rows = [
        {
            "prime": int(row["prime"]),
            "R": int(row["R"]),
            "a": int(row["a"]),
            "s": int(row["s"]),
            "shared_layer": int(row["shared_layer"]),
            "raw_shared_pullback_residues": row.get(
                "raw_shared_pullback_residues", []
            ),
            "subgroup_shared_pullback_residues": row.get(
                "subgroup_shared_pullback_residues", []
            ),
        }
        for row in all_records
        if int(row["subgroup_shared_pullback_count"]) > 0
    ]

    return {
        "arithmetic": (
            "for each F state define the exact cross-source shared layer "
            "S_R=gcd(K_R,lcm_{R'!=R}|R-R'|/4); compare its centered "
            "difference spectrum with the block target pullback"
        ),
        "scope_note": (
            "This is a complete finite cross-source pullback audit of all 45 F "
            "states and 69 directed sources in the four adversarial cores. "
            "It rules out direct shared-layer alignment in this finite set, "
            "but does not prove a universal selector."
        ),
        "classification_input": classification_path.name,
        "classification_input_sha256": file_sha256(classification_path),
        "block_input": block_path.name,
        "block_input_sha256": file_sha256(block_path),
        "prime_count": len(ADVERSARIAL_PRIMES),
        "finite_exponent_R_count": sum(EXPECTED_F_COUNTS.values()),
        "directed_orientation_count": len(all_records),
        "pairwise_gcd_identity_count": pair_count,
        "raw_shared_pullback_orientation_count": raw_orientation_count,
        "subgroup_shared_pullback_orientation_count": subgroup_orientation_count,
        "finite_shared_alignment_orientation_count": finite_orientation_count,
        "raw_shared_pullback_residue_count": raw_residue_count,
        "subgroup_shared_pullback_residue_count": subgroup_residue_count,
        "subgroup_pullback_exponent_overflow_distribution": dict(
            sorted(overflow_distribution.items(), key=lambda item: int(item[0]))
        ),
        "minimum_subgroup_pullback_exponent_overflow": min(
            int(key) for key in overflow_distribution
        ),
        "maximum_subgroup_pullback_exponent_overflow": max(
            int(key) for key in overflow_distribution
        ),
        "latent_subgroup_rows": latent_rows,
        "record_sha256": stable_sha256(digest_rows),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--classification-input", type=Path, default=CLASSIFICATION_INPUT)
    parser.add_argument("--block-input", type=Path, default=BLOCK_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.classification_input, args.block_input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in result.items()
                if key not in {"profiles"}
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
