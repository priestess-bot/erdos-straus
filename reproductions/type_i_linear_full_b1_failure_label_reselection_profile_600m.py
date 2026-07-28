#!/usr/bin/env python3
"""Audit label-layer reselection on every full-spectrum B=1 failure in the B>1 pressure set."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
LAYER_SCRIPT = ROOT / "reproductions" / "type_i_linear_label_layer_support_profile.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-full-b1-failure-label-reselection-profile-600m-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
EXPECTED_PRIMES = [
    878_089,
    3_942_409,
    26_034_649,
    34_252_969,
    42_486_889,
    53_712_409,
    57_399_241,
    62_588_089,
    85_457_689,
    137_431_849,
    168_434_809,
    185_772_409,
    212_973_049,
    283_319_689,
    297_640_249,
    477_015_289,
    507_599_689,
    534_672_889,
]
EXPECTED_SELECTED_SUPPORT_COUNTS = {"1": 3, "2": 14, "3": 1}
EXPECTED_SELECTED_THREE_LAYER_PRIMES = [26_034_649]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


layers = load_module("full_b1_failure_label_layers", LAYER_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_pressure_profiles(input_path: Path = INPUT) -> list[dict[str, object]]:
    """Select exactly the full B=1 failures from the 200 complete pressure spectra."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full B>1-spectrum input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list):
        raise AssertionError("full B>1-spectrum input lacks profiles")
    selected = [dict(profile) for profile in profiles if not profile["B_eq_1_hit_R"]]
    primes = [int(profile["prime"]) for profile in selected]
    if (
        int(payload["no_B_eq_1_hit_prime_count"]) != len(EXPECTED_PRIMES)
        or primes != EXPECTED_PRIMES
        or any(int(profile["classification_counts"]["hit"]) < 1 for profile in selected)
    ):
        raise AssertionError("the full B=1-failure pressure set changed")
    return selected


def audit_prime(stored: dict[str, object]) -> dict[str, object]:
    """Complete one strict B=1 failure spectrum and select its shortest label hit."""
    prime = int(stored["prime"])
    bound, states_by_R = layers.sources.enumerate_linear_source_states(prime)
    labels, collision_lcms = layers.coordinate_label_lcms(states_by_R)
    target_hit_R = []
    orientations = []
    for R, states in states_by_R.items():
        K = (prime * R + 1) // 4
        if R - 1 not in layers.centered_square_spectrum(
            layers.exact_factorization(K), R
        ):
            continue
        target_hit_R.append(R)
        orientations.extend(
            layers.audit_orientation(prime, R, a, s, collision_lcms)
            for a, s in states
        )
    stored_hit_R = [int(R) for R in stored["general_B_hit_R"]]
    if target_hit_R != stored_hit_R or not orientations:
        raise AssertionError("full B=1-failure spectrum lost a stored general-B target hit")
    selected = min(
        orientations,
        key=lambda item: (
            int(item["minimum_target_layer_support"]),
            int(item["R"]),
            int(item["a"]),
            int(item["s"]),
        ),
    )
    if int(selected["minimum_target_layer_support"]) > 3:
        raise AssertionError("the B=1-failure reselection profile exceeded three layers")
    support_counts = Counter(
        str(item["minimum_target_layer_support"]) for item in orientations
    )
    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "complete_linear_R_count": len(states_by_R),
        "complete_directed_linear_source_count": sum(
            len(states) for states in states_by_R.values()
        ),
        "coordinate_label_count": len(labels),
        "target_hit_R": target_hit_R,
        "directed_target_hit_source_count": len(orientations),
        "all_target_orientation_support_counts": dict(sorted(support_counts.items())),
        "selected_orientation": selected,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Run the full strict-B=1-failure label-reselection profile through 600M."""
    profiles = [audit_prime(stored) for stored in load_pressure_profiles(input_path)]
    selected_counts = Counter(
        str(profile["selected_orientation"]["minimum_target_layer_support"])
        for profile in profiles
    )
    selected_counts = dict(sorted(selected_counts.items()))
    selected_three_layer_primes = [
        int(profile["prime"])
        for profile in profiles
        if int(profile["selected_orientation"]["minimum_target_layer_support"]) == 3
    ]
    if (
        selected_counts != EXPECTED_SELECTED_SUPPORT_COUNTS
        or selected_three_layer_primes != EXPECTED_SELECTED_THREE_LAYER_PRIMES
    ):
        raise AssertionError("full B=1-failure label-reselection profile changed")
    return {
        "arithmetic": (
            "for every full-spectrum B=1 failure among the 200 selected B>1 pressure points, "
            "completely enumerate linear sources, decide every K-square target spectrum, split each hit "
            "into the four complete-spectrum coordinate-label layers, and select least support"
        ),
        "scope_note": (
            "This is a finite 600-million pressure profile on 18 full B=1 failures. It supports but does "
            "not prove universal three-layer reselection or the mixed terminal selector."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "prime_count": len(profiles),
        "selected_layer_support_counts": selected_counts,
        "selected_three_layer_primes": selected_three_layer_primes,
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
