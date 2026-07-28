#!/usr/bin/env python3
"""Classify every full linear spectrum behind the 200 selected B>1 pressure points."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-source-general-b-completion-profile-600m-results.json"
MIXTURE_SCRIPT = ROOT / "reproductions" / "type_i_linear_general_b_obstruction_mixture_profile_600m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
EXPECTED_INPUT_SHA256 = "6374f4489196ea210da63b48367d2e59c7ca97220d55792adcab6f54b44a5f68"
EXPECTED_PRIME_COUNT = 200
EXPECTED_PRIME_LIST_SHA256 = "c1f144ac5830d3dbd3e32729711ce69e40e4962ac18c20e87454811d347ba896"
EXPECTED_COMPLETE_LINEAR_R_COUNT = 10_292
EXPECTED_COMPLETE_DIRECTED_LINEAR_SOURCE_COUNT = 18_074
EXPECTED_CLASSIFICATION_TOTALS = {
    "hit": 1_018,
    "finite_exponent": 2_752,
    "subgroup_character": 6_522,
}
EXPECTED_UNIQUE_GENERAL_B_HIT_PRIMES = [
    67_369,
    878_089,
    13_782_409,
    26_034_649,
    57_399_241,
    152_498_329,
    283_319_689,
]
EXPECTED_B_ONE_RESELECTED_PRIME_COUNT = 182


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


mixture = load_module("b_gt_one_full_spectrum_mixture", MIXTURE_SCRIPT)
sources = mixture.sources


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integer_list_sha256(values: list[int]) -> str:
    return hashlib.sha256(
        "".join(f"{value}\n" for value in values).encode("ascii")
    ).hexdigest()


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    return hashlib.sha256(
        "\n".join(",".join(str(value) for value in row) for row in rows).encode("ascii")
    ).hexdigest()


def load_pressure_records(input_path: Path = INPUT) -> list[dict[str, object]]:
    """Select exactly the hash-frozen first witnesses whose normalized B exceeds one."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the finite general-B completion input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    records = payload.get("captured_records")
    if not isinstance(records, list):
        raise AssertionError("general-B completion input lacks captured records")
    selected = [
        dict(record)
        for record in records
        if int(record["selected_witness"]["B"]) > 1
    ]
    primes = [int(record["prime"]) for record in selected]
    if (
        len(selected) != EXPECTED_PRIME_COUNT
        or primes != sorted(primes)
        or integer_list_sha256(primes) != EXPECTED_PRIME_LIST_SHA256
    ):
        raise AssertionError("the selected B>1 pressure set changed")
    return selected


def classify_modulus(prime: int, R: int, source_state_count: int) -> dict[str, int | bool | str]:
    """Classify the exact K-square target and the stricter B=1 divisor target."""
    K = (prime * R + 1) // 4
    factors = sources.exact_factorization(K)
    B_one_matches = [
        divisor
        for divisor in sources.divisors_from_factorization(factors)
        if (4 * divisor + 1) % R == 0
    ]
    square_matches = [
        divisor
        for divisor in sources.divisors_from_factorization(factors, 2)
        if (4 * divisor + 1) % R == 0
    ]
    if B_one_matches and not square_matches:
        raise AssertionError("a B=1 divisor did not remain a K-square target divisor")
    if square_matches:
        classification = "hit"
        target_in_generated_subgroup = True
    else:
        certificate = sources.unit_group_subgroup_certificate(factors, R)
        target_in_generated_subgroup = bool(certificate["target_in_generated_subgroup"])
        classification = (
            "finite_exponent" if target_in_generated_subgroup else "subgroup_character"
        )
    return {
        "R": R,
        "K": K,
        "source_state_count": source_state_count,
        "B_eq_1_target_divisor_count": len(B_one_matches),
        "general_B_target_divisor_count": len(square_matches),
        "target_in_generated_subgroup": target_in_generated_subgroup,
        "classification": classification,
    }


def audit_prime(stored: dict[str, object]) -> dict[str, object]:
    """Exhaust every induced R for a selected B>1 first-certificate prime."""
    prime = int(stored["prime"])
    witness = stored["selected_witness"]
    selected_R = int(witness["R"])
    selected_B = int(witness["B"])
    bound, states_by_R = sources.enumerate_linear_source_states(prime)
    records = [
        classify_modulus(prime, R, len(states)) for R, states in states_by_R.items()
    ]
    records.sort(key=lambda record: int(record["R"]))
    selected_record = next(
        (record for record in records if int(record["R"]) == selected_R), None
    )
    if (
        selected_B <= 1
        or selected_record is None
        or selected_record["classification"] != "hit"
        or not int(selected_record["general_B_target_divisor_count"])
    ):
        raise AssertionError("stored B>1 first witness disappeared from the full target spectrum")
    classification_counts = Counter(str(record["classification"]) for record in records)
    counts = {
        name: int(classification_counts[name])
        for name in ("hit", "finite_exponent", "subgroup_character")
    }
    b_one_hit_R = [
        int(record["R"])
        for record in records
        if int(record["B_eq_1_target_divisor_count"]) > 0
    ]
    hit_R = [int(record["R"]) for record in records if record["classification"] == "hit"]
    digest_rows = [
        (
            int(record["R"]),
            int(record["K"]),
            int(record["source_state_count"]),
            int(record["B_eq_1_target_divisor_count"]),
            int(record["general_B_target_divisor_count"]),
            ("hit", "finite_exponent", "subgroup_character").index(
                str(record["classification"])
            ),
        )
        for record in records
    ]
    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "selected_first_witness": {
            "B": selected_B,
            "R": selected_R,
            "a": int(witness["a"]),
            "s": int(witness["s"]),
            "least_coordinate_u": int(witness["least_coordinate_u"]),
        },
        "complete_linear_R_count": len(records),
        "complete_directed_linear_source_count": sum(
            len(states) for states in states_by_R.values()
        ),
        "classification_counts": counts,
        "general_B_hit_R": hit_R,
        "B_eq_1_hit_R": b_one_hit_R,
        "record_sha256": stable_sha256(digest_rows),
        "records": records,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Exhaust all 200 full spectra behind first-selected B>1 witnesses."""
    stored_records = load_pressure_records(input_path)
    profiles = [audit_prime(record) for record in stored_records]
    totals = Counter()
    for profile in profiles:
        totals.update(profile["classification_counts"])
    classification_totals = {
        name: int(totals[name])
        for name in ("hit", "finite_exponent", "subgroup_character")
    }
    if any(
        int(profile["classification_counts"]["hit"]) < 1 for profile in profiles
    ):
        raise AssertionError("a selected general-B pressure prime lost every full-spectrum hit")
    unique_hit_profiles = [
        profile
        for profile in profiles
        if int(profile["classification_counts"]["hit"]) == 1
    ]
    B_one_reselected_profiles = [profile for profile in profiles if profile["B_eq_1_hit_R"]]
    summary = {
        "complete_linear_R_count": sum(
            int(profile["complete_linear_R_count"]) for profile in profiles
        ),
        "complete_directed_linear_source_count": sum(
            int(profile["complete_directed_linear_source_count"]) for profile in profiles
        ),
        "classification_totals": classification_totals,
        "unique_general_B_hit_primes": [
            int(profile["prime"]) for profile in unique_hit_profiles
        ],
        "B_eq_1_reselected_prime_count": len(B_one_reselected_profiles),
    }
    if (
        summary["complete_linear_R_count"] != EXPECTED_COMPLETE_LINEAR_R_COUNT
        or summary["complete_directed_linear_source_count"]
        != EXPECTED_COMPLETE_DIRECTED_LINEAR_SOURCE_COUNT
        or summary["classification_totals"] != EXPECTED_CLASSIFICATION_TOTALS
        or summary["unique_general_B_hit_primes"]
        != EXPECTED_UNIQUE_GENERAL_B_HIT_PRIMES
        or summary["B_eq_1_reselected_prime_count"]
        != EXPECTED_B_ONE_RESELECTED_PRIME_COUNT
    ):
        raise AssertionError("full B>1 pressure-spectrum profile changed")
    return {
        "arithmetic": (
            "for every prime whose deterministic first certificate in the 1,964-point general-B completion "
            "uses B>1, completely enumerate all linear-source-induced R; decide every d|K^2 with "
            "4d=-1 (mod R), classify its miss as a subgroup or finite-exponent obstruction, and separately "
            "decide all stricter B=1 divisors d|K"
        ),
        "scope_note": (
            "This is a complete finite source-spectrum audit of 200 selected B>1 pressure points. It does "
            "not establish a universal selector beyond the hash-frozen 600-million pressure set."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "prime_count": len(profiles),
        "prime_list_sha256": integer_list_sha256([int(profile["prime"]) for profile in profiles]),
        "complete_linear_R_count": summary["complete_linear_R_count"],
        "complete_directed_linear_source_count": summary[
            "complete_directed_linear_source_count"
        ],
        "classification_totals": summary["classification_totals"],
        "unique_general_B_hit_prime_count": len(unique_hit_profiles),
        "unique_general_B_hit_primes": summary["unique_general_B_hit_primes"],
        "B_eq_1_reselected_prime_count": summary["B_eq_1_reselected_prime_count"],
        "no_B_eq_1_hit_prime_count": len(profiles) - len(B_one_reselected_profiles),
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
