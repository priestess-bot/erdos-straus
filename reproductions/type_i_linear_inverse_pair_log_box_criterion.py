#!/usr/bin/env python3
"""Verify the inverse-pair cyclic-log box criterion on two F-state rows."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-f-cross-source-pullback-profile-600m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-inverse-pair-log-box-criterion-results.json"
EXPECTED_INPUT_SHA256 = (
    "60a95000d81cdfee41f6b07b54b0f9e088bc56f71772ef296dec49b7c3020d05"
)

CASES = (
    {
        "prime": 64_214_329,
        "R": 359,
        "q": 19,
        "inverse_factor": 135_173,
        "expected_order": 358,
        "expected_target_count": 60,
        "expected_minimum_overflow": 12,
        "expected_maximum_overflow": 77,
    },
    {
        "prime": 105_295_129,
        "R": 839,
        "q": 23,
        "inverse_factor": 73,
        "expected_order": 419,
        "expected_target_count": 2,
        "expected_minimum_overflow": 99,
        "expected_maximum_overflow": 99,
    },
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_profile_rows() -> dict[tuple[int, int], dict[str, object]]:
    """Index the two selected orientations from the frozen seven-spectrum artifact."""
    if file_sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("seven-spectrum profile changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    rows: dict[tuple[int, int], dict[str, object]] = {}
    for profile in payload["profiles"]:
        prime = int(profile["prime"])
        for record in profile["records"]:
            R = int(record["R"])
            for orientation in record["orientations"]:
                if orientation.get("subgroup_shared_pullback_residues"):
                    rows[(prime, R)] = {
                        "K": int(record["K"]),
                        **orientation,
                    }
    return rows


def inverse_pair_profile(case: dict[str, int], row: dict[str, object]) -> dict[str, object]:
    """Apply the exact one-dimensional exponent-difference formula."""
    R = int(case["R"])
    q = int(case["q"])
    inverse_factor = int(case["inverse_factor"])
    if q * inverse_factor % R != 1:
        raise AssertionError("the two affine factors are not inverse modulo R")
    factors = {
        int(record["prime"]): int(record["exponent"])
        for record in row["affine_factorization"]
    }
    if factors != {q: 1, inverse_factor: 1}:
        raise AssertionError("selected row does not have the expected inverse pair")

    order = int(sympy.n_order(q, R))
    if order != int(case["expected_order"]) or order <= 4:
        raise AssertionError("unexpected inverse-pair order")
    finite_box = {
        pow(q, left - right, R)
        for left in range(-1, 2)
        for right in range(-1, 2)
    }
    target = sorted(int(value) for value in row["subgroup_shared_pullback_residues"])
    if any(pow(q, int(sympy.discrete_log(R, value, q)), R) != value for value in target):
        raise AssertionError("a target class is outside the generated cyclic subgroup")

    rows = []
    for residue in target:
        logarithm = int(sympy.discrete_log(R, residue, q))
        least_absolute_log = min(logarithm, order - logarithm)
        overflow = max(0, (least_absolute_log + 1) // 2 - 1)
        rows.append(
            {
                "residue": residue,
                "q_log": logarithm,
                "least_absolute_log": least_absolute_log,
                "minimum_extra_exponent": overflow,
            }
        )
    distribution = Counter(str(int(record["minimum_extra_exponent"])) for record in rows)
    if set(finite_box) & set(target):
        raise AssertionError("the finite inverse-pair box unexpectedly aligns")
    if len(target) != int(case["expected_target_count"]):
        raise AssertionError("target count changed")
    if min(map(int, distribution)) != int(case["expected_minimum_overflow"]):
        raise AssertionError("minimum overflow changed")
    if max(map(int, distribution)) != int(case["expected_maximum_overflow"]):
        raise AssertionError("maximum overflow changed")
    return {
        "prime": int(case["prime"]),
        "R": R,
        "q": q,
        "inverse_factor": inverse_factor,
        "q_order": order,
        "q_inverse_relation": (q * inverse_factor) % R,
        "finite_box_residues": sorted(finite_box),
        "target_count": len(target),
        "finite_target_intersection_count": len(set(finite_box) & set(target)),
        "overflow_distribution": dict(
            sorted(distribution.items(), key=lambda item: int(item[0]))
        ),
        "minimum_overflow": min(distribution, key=int),
        "maximum_overflow": max(distribution, key=int),
        "target_rows": rows,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    if input_path != INPUT:
        raise ValueError("this profile is tied to the frozen seven-spectrum artifact")
    rows = load_profile_rows()
    profiles = []
    for case in CASES:
        key = (int(case["prime"]), int(case["R"]))
        if key not in rows:
            raise AssertionError(f"missing inverse-pair row {key}")
        profiles.append(inverse_pair_profile(case, rows[key]))
    return {
        "arithmetic": (
            "if L=q*r with r=q^-1 (mod R), the centered exponent box reduces to "
            "q^(z_q-z_r); discrete logs give the exact least uniform overflow"
        ),
        "scope_note": (
            "This verifies an inverse-pair lemma and two F-state instances. It does not "
            "claim that every F-state has an inverse-pair affine block or prove the "
            "mixed terminal selector."
        ),
        "input_artifact": INPUT.name,
        "input_sha256": file_sha256(INPUT),
        "case_count": len(profiles),
        "profiles": profiles,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit()
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
