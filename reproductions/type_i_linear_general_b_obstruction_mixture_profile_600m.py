#!/usr/bin/env python3
"""Classify every non-hit linear target spectrum on seven frozen pressure points."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-general-b-spectrum-resolution-profile-600m-results.json"
COMPENSATED_SCRIPT = ROOT / "reproductions" / "type_i_general_b_compensated_square_full_linear_profile_600m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"

EXPECTED_INPUT_SHA256 = "6e2310b8153881f72db838892410e5ef4edcf7c7cdb3121428ca07a3ea4cbca2"
EXPECTED_PER_PRIME = {
    214_729: {"hit": 3, "finite_exponent": 8, "subgroup_character": 19},
    878_089: {"hit": 1, "finite_exponent": 2, "subgroup_character": 21},
    2_210_569: {"hit": 3, "finite_exponent": 4, "subgroup_character": 21},
    13_782_409: {"hit": 1, "finite_exponent": 9, "subgroup_character": 31},
    64_214_329: {"hit": 4, "finite_exponent": 18, "subgroup_character": 25},
    105_295_129: {"hit": 4, "finite_exponent": 10, "subgroup_character": 41},
    536_944_489: {"hit": 4, "finite_exponent": 17, "subgroup_character": 32},
}
EXPECTED_TOTALS = {"hit": 20, "finite_exponent": 68, "subgroup_character": 190}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


compensated = load_module("obstruction_mixture_compensated", COMPENSATED_SCRIPT)
sources = compensated.sources
linear = compensated.linear


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_primes(input_path: Path = INPUT) -> list[int]:
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the seven-point spectrum-resolution artifact changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    records = payload.get("records")
    primes = [int(record["prime"]) for record in records] if isinstance(records, list) else []
    if primes != list(EXPECTED_PER_PRIME):
        raise AssertionError("the frozen obstruction-mixture input changed")
    return primes


def classify_modulus(prime: int, R: int, source_state_count: int) -> dict[str, object]:
    """Classify the exact target spectrum as hit, group, or exponent failure."""
    forms, square_divisor_count, target_divisor_hits = compensated.target_forms_for_R(
        prime, R
    )
    if forms:
        classification = "hit"
        target_in_generated_subgroup = True
    else:
        K = (prime * R + 1) // 4
        factors = linear.exact_factorization(K)
        certificate = sources.unit_group_subgroup_certificate(factors, R)
        target_in_generated_subgroup = bool(
            certificate["target_in_generated_subgroup"]
        )
        classification = (
            "finite_exponent" if target_in_generated_subgroup else "subgroup_character"
        )
    return {
        "R": R,
        "source_state_count": source_state_count,
        "K_square_divisor_count": square_divisor_count,
        "target_divisor_hit_count": target_divisor_hits,
        "target_normal_form_count": len(forms),
        "target_in_generated_subgroup": target_in_generated_subgroup,
        "classification": classification,
    }


def audit_prime(prime: int) -> dict[str, object]:
    bound, states_by_R = sources.enumerate_linear_source_states(prime)
    records = [
        classify_modulus(prime, R, len(states))
        for R, states in states_by_R.items()
    ]
    counts = Counter(str(record["classification"]) for record in records)
    classification_counts = {
        name: int(counts[name])
        for name in ("hit", "finite_exponent", "subgroup_character")
    }
    if classification_counts != EXPECTED_PER_PRIME[prime]:
        raise AssertionError("the frozen per-prime obstruction mixture changed")
    if any(
        bool(record["target_in_generated_subgroup"])
        != (record["classification"] != "subgroup_character")
        for record in records
    ):
        raise AssertionError("subgroup membership and classification disagree")
    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "linear_R_count": len(records),
        "directed_linear_source_state_count": sum(
            len(states) for states in states_by_R.values()
        ),
        "classification_counts": classification_counts,
        "hit_R": [record["R"] for record in records if record["classification"] == "hit"],
        "finite_exponent_R": [
            record["R"]
            for record in records
            if record["classification"] == "finite_exponent"
        ],
        "subgroup_character_R": [
            record["R"]
            for record in records
            if record["classification"] == "subgroup_character"
        ],
        "records": records,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    primes = load_primes(input_path)
    profiles = [audit_prime(prime) for prime in primes]
    totals = Counter()
    for profile in profiles:
        totals.update(profile["classification_counts"])
    classification_totals = {
        name: int(totals[name])
        for name in ("hit", "finite_exponent", "subgroup_character")
    }
    if classification_totals != EXPECTED_TOTALS:
        raise AssertionError("the frozen aggregate obstruction mixture changed")
    return {
        "arithmetic": (
            "for every linear-source-induced R at each stated prime, enumerate all d|K^2 with "
            "4d=-1 (mod R); when there is no hit, decide whether -1 belongs to the exact generated "
            "subgroup of the prime residues of K"
        ),
        "scope_note": (
            "This is a complete finite classification of all target-spectrum states on seven frozen primes. "
            "It does not compare the varying unit groups across R and does not prove a universal selector."
        ),
        "input": input_path.name,
        "input_prime_count": len(primes),
        "linear_R_count": sum(int(profile["linear_R_count"]) for profile in profiles),
        "directed_linear_source_state_count": sum(
            int(profile["directed_linear_source_state_count"]) for profile in profiles
        ),
        "classification_totals": classification_totals,
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key != "profiles"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
