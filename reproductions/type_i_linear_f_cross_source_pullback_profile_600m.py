#!/usr/bin/env python3
"""Profile shared-layer pullbacks across seven complete linear spectra."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-f-cross-source-pullback-profile-600m-results.json"
)
EXPECTED_INPUT_SHA256 = (
    "dce587d6e6703e5cdcb81b6cd05c16989394a7321d2d14515ea2eda6c2aec44d"
)
EXPECTED_F_COUNTS = {
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


shared_audit = load_module(
    "four_core_cross_source_pullback_helpers",
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


def checked_records(
    profile: dict[str, object],
) -> list[dict[str, int | str]]:
    prime = int(profile["prime"])
    records = []
    for stored in profile["records"]:
        R = int(stored["R"])
        K = (prime * R + 1) // 4
        if 4 * K != prime * R + 1 or math.gcd(K, R) != 1:
            raise AssertionError("malformed linear source state")
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
        "finite_shared_alignment_count": 0,
    }
    if raw:
        result["raw_shared_pullback_residues"] = raw
    if subgroup:
        result["subgroup_shared_pullback_residues"] = subgroup
    return result


def run_audit(path: Path = INPUT) -> dict[str, object]:
    if file_sha256(path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("seven-spectrum input changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    profiles = []
    all_orientations: list[dict[str, object]] = []
    digest_rows: list[tuple[int, ...]] = []
    pair_count = 0
    raw_orientation_count = 0
    subgroup_orientation_count = 0
    finite_alignment_count = 0
    raw_residue_count = 0
    subgroup_residue_count = 0

    for source_profile in payload["profiles"]:
        prime = int(source_profile["prime"])
        records = checked_records(source_profile)
        pair_count += verify_pairwise_identity(records)
        _, states_by_R = sources.enumerate_linear_source_states(prime)
        F_records = [
            record
            for record in records
            if record["classification"] == "finite_exponent"
        ]
        if len(F_records) != EXPECTED_F_COUNTS[prime]:
            raise AssertionError("F-state count changed")
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
                int(row["raw_shared_pullback_count"] > 0)
                for row in orientations
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
                int(row["subgroup_shared_pullback_count"])
                for row in orientations
            )
            for row in orientations:
                raw_count = int(row["raw_shared_pullback_count"])
                subgroup_count = int(row["subgroup_shared_pullback_count"])
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
                        int(row["finite_shared_alignment_count"]),
                    )
                )
                all_orientations.append(
                    {
                        "prime": prime,
                        "R": R,
                        "K": K,
                        **row,
                    }
                )
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

    if len(all_orientations) != 105:
        raise AssertionError("orientation total changed")
    if finite_alignment_count != 0:
        raise AssertionError("finite shared alignment unexpectedly appeared")

    return {
        "arithmetic": (
            "for each finite-exponent F state in seven complete linear spectra, "
            "compute the exact cross-source shared layer S_R and compare its "
            "centered difference spectrum with the block target pullback"
        ),
        "scope_note": (
            "This is a finite profile of all 68 F states and 105 directed "
            "sources in seven frozen complete spectra. It rules out direct "
            "shared-layer block alignment in this scope, but does not prove a "
            "universal selector."
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
            {
                key: value
                for key, value in result.items()
                if key != "profiles"
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
