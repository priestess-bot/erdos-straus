#!/usr/bin/env python3
"""Resolve the 25-point fixed-ray residual through existing adaptive certificates."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXED_RAY = ROOT / "reproductions" / "type-i-fixed-pminusone-ray-pressure-profile-600m-results.json"
BOX = ROOT / "reproductions" / "type-i-tail-reverse-pminusone-profile-500m-results.json"
GLOBAL = ROOT / "reproductions" / "type-i-pminusone-box-miss-global-audit-500m-results.json"
LINEAR = ROOT / "reproductions" / "type-i-global-linear-b1-failure-general-b-profile-500m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-fixed-ray-residual-resolution-600m-results.json"


def verify_normal_witness(prime: int, witness: dict[str, object]) -> dict[str, int]:
    """Validate a normal-form bridge stored in one of the source audits."""
    normal = witness["normal_form"]
    if not isinstance(normal, list) or len(normal) != 3:
        raise TypeError("witness has no Type I normal form")
    A, B, C = (int(value) for value in normal)
    R = int(witness["R"])
    K = int(witness["K"])
    E = int(witness["E"])
    source = int(witness["source_denominator"])
    H = int(witness.get("H", K // (B * C)))
    if (
        K != B * C * H
        or (H + B) % R
        or prime != 4 * A * B * C - (4 * B * B * C + 1) // R
        or (4 * B * B * C + 1) % R
        or (4 * K - E) % R
        or (4 * K - E) // R != source
        or (4 * K * K) % E
        or E % R != 1
        or E % 2
        or E > 4 * K - 2 * R
        or source % 2
        or not ((prime + 1) // 2 <= source < prime)
    ):
        raise AssertionError("stored normal witness did not reconstruct its terminal bridge")
    source_term, remainder = divmod(source * K, E)
    if remainder:
        raise AssertionError("stored bridge has a nonintegral source tail")
    if Fraction(4, prime) != Fraction(1, A * B * C) + Fraction(1, A * C * H) + Fraction(1, prime * K):
        raise AssertionError("stored target identity did not reconstruct")
    if Fraction(4, source) != Fraction(1, source_term) + Fraction(1, A * B * C) + Fraction(1, A * C * H):
        raise AssertionError("stored source identity did not reconstruct")
    return {
        "A": A,
        "B": B,
        "C": C,
        "H": H,
        "m": (4 * B * B * C + 1) // R,
        "R": R,
        "K": K,
        "E": E,
        "source_denominator": source,
        "source_term": source_term,
    }


def all_conditions_true(witness: dict[str, object]) -> None:
    """Guard the full condition table released by an exhaustive source audit."""
    conditions = witness.get("conditions")
    if not isinstance(conditions, dict) or not conditions or not all(bool(value) for value in conditions.values()):
        raise AssertionError("source audit released an unchecked condition table")


def run_audit(
    fixed_ray_path: Path = FIXED_RAY,
    box_path: Path = BOX,
    global_path: Path = GLOBAL,
    linear_path: Path = LINEAR,
) -> dict[str, object]:
    """Partition all 25 fixed-ray residuals by their already-audited adaptive exit."""
    fixed = json.loads(fixed_ray_path.read_text(encoding="utf-8"))
    box = json.loads(box_path.read_text(encoding="utf-8"))
    global_audit = json.loads(global_path.read_text(encoding="utf-8"))
    linear = json.loads(linear_path.read_text(encoding="utf-8"))

    residual = [int(prime) for prime in fixed["unresolved_primes"]]
    if int(fixed["unresolved_count"]) != len(residual) or len(residual) != 25 or len(set(residual)) != len(residual):
        raise AssertionError("fixed-ray artifact no longer exposes the frozen 25-point residual")

    box_misses = {int(prime) for prime in box["p_minus_one_misses"]}
    box_witnesses = {int(row["prime"]): row["p_minus_one_witness"] for row in box["records"]}
    global_witnesses = {
        int(row["prime"]): row["selected_p_minus_one_witness"] for row in global_audit["captured_records"]
    }
    global_misses = {int(prime) for prime in global_audit["global_p_minus_one_miss_primes"]}
    b_one_hits = {int(row["prime"]): row["B_eq_1_hits"] for row in linear["B_eq_1_records"]}
    general_b = {int(row["prime"]): row["selected_general_B_witness"] for row in linear["general_B_failure_profiles"]}

    if box_misses != set(global_witnesses) | global_misses:
        raise AssertionError("global p-1 audit does not partition its 185 box misses")

    records: list[dict[str, object]] = []
    counts: Counter[str] = Counter()
    for prime in residual:
        if prime in box_witnesses:
            classification = "pminusone_short_box"
            witness = verify_normal_witness(prime, box_witnesses[prime])
        elif prime in global_witnesses:
            classification = "pminusone_global_extension"
            stored = global_witnesses[prime]
            all_conditions_true(stored)
            witness = verify_normal_witness(prime, stored)
        elif prime in global_misses:
            hits = b_one_hits.get(prime)
            if hits:
                selected = min(
                    hits,
                    key=lambda row: (
                        int(row["R"]),
                        int(row["least_B_eq_1_divisor"]),
                        tuple(int(value) for value in row["selected_source_state"]),
                    ),
                )
                stored = selected["witness"]
                if not isinstance(stored, dict):
                    raise TypeError("linear B=1 record has no witness")
                all_conditions_true(stored)
                witness = verify_normal_witness(prime, stored)
                normalization = stored["source_normalization"]
                if not isinstance(normalization, dict) or int(normalization["beta"]) != 1 or witness["B"] != 1:
                    raise AssertionError("selected linear B=1 witness lost the beta=1 invariant")
                classification = "linear_B1_after_global_pminusone_failure"
                witness.update({"a": int(stored["a"]), "s": int(stored["s"]), "beta": 1})
            else:
                stored = general_b.get(prime)
                if not isinstance(stored, dict):
                    raise AssertionError("global p-1 and linear B=1 failure has no general-B exit")
                all_conditions_true(stored)
                witness = verify_normal_witness(prime, stored)
                normalization = stored["source_normalization"]
                if not isinstance(normalization, dict) or int(normalization["beta"]) != 1:
                    raise AssertionError("selected general-B witness lost the beta=1 invariant")
                classification = "linear_general_B_after_B1_failure"
                witness.update({"a": int(stored["a"]), "s": int(stored["s"]), "beta": 1})
        else:
            raise AssertionError("residual prime is absent from all p-1 audit partitions")
        counts[classification] += 1
        records.append({"prime": prime, "classification": classification, "witness": witness})

    if len(records) != len(residual):
        raise AssertionError("residual resolver did not cover every input prime")
    return {
        "arithmetic": (
            "partition the frozen 25-point fixed-ray residual by the stored short-box p-1 witnesses, "
            "the unbounded p-1 extension audit, and finally the beta=1 linear-source B=1 or general-B audits; "
            "reconstruct both target and source identities for every selected witness"
        ),
        "scope_note": (
            "This joins existing finite audits. It does not turn the p-1 or linear-source finite profiles "
            "into universal selectors."
        ),
        "fixed_ray_input": fixed_ray_path.name,
        "short_box_input": box_path.name,
        "global_pminusone_input": global_path.name,
        "linear_input": linear_path.name,
        "fixed_ray_residual_count": len(residual),
        "global_pminusone_failure_count_within_residual": sum(prime in global_misses for prime in residual),
        "resolution_counts": {
            classification: counts[classification]
            for classification in (
                "pminusone_short_box",
                "pminusone_global_extension",
                "linear_B1_after_global_pminusone_failure",
                "linear_general_B_after_B1_failure",
            )
        },
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixed-ray", type=Path, default=FIXED_RAY)
    parser.add_argument("--box", type=Path, default=BOX)
    parser.add_argument("--global-pminusone", type=Path, default=GLOBAL)
    parser.add_argument("--linear", type=Path, default=LINEAR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.fixed_ray, args.box, args.global_pminusone, args.linear)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
