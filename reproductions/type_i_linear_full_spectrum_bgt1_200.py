#!/usr/bin/env python3
"""Audit the complete linear target spectrum on 200 general-B pressure points.

The input is the hash-frozen 1,964-point linear-source completion profile.  Its
200 records whose first selected witness has ``B>1`` are used only to choose a
stratified pressure set.  For every selected prime, this module then
re-enumerates *all* directed linear source states, deduplicates their moduli
``R``, exhausts every divisor of ``K^2`` at each modulus, and classifies a
non-hit as either a subgroup/character obstruction or a finite-exponent
obstruction.  The output is finite evidence and is not a universal selector.
"""

from __future__ import annotations

from collections import Counter
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-source-general-b-completion-profile-600m-results.json"
SPECTRUM_SCRIPT = ROOT / "reproductions" / "type_i_linear_general_b_spectrum_resolution_profile_600m.py"
OBSTRUCTION_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-linear-full-spectrum-bgt1-200-results.json"

EXPECTED_INPUT_SHA256 = "6374f4489196ea210da63b48367d2e59c7ca97220d55792adcab6f54b44a5f68"
EXPECTED_SELECTED_COUNT = 200
CLASSIFICATIONS = ("hit", "finite_exponent", "subgroup_character")


def load_module(name: str, path: Path):
    """Load a repository reproduction module under an isolated name."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


spectrum = load_module("full_bgt1_spectrum_resolution", SPECTRUM_SCRIPT)
sources = spectrum.sources
compensated = spectrum.compensated
obstruction = load_module("full_bgt1_obstruction_classifier", OBSTRUCTION_SCRIPT)


def file_sha256(path: Path) -> str:
    """Hash an input artifact before using it as a selector."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def selected_primes(input_path: Path = INPUT) -> list[int]:
    """Return the 200 frozen points whose first witness has ``B>1``."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the hash-frozen completion profile changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    captured = payload.get("captured_records")
    if not isinstance(captured, list) or len(captured) != 1_964:
        raise AssertionError("the completion profile has an unexpected record set")
    primes = [
        int(record["prime"])
        for record in captured
        if int(record["selected_witness"]["B"]) > 1
    ]
    if len(primes) != EXPECTED_SELECTED_COUNT or len(set(primes)) != len(primes):
        raise AssertionError("the selected B>1 pressure set changed")
    if primes != sorted(primes):
        raise AssertionError("the authoritative pressure records are not sorted")
    return primes


def antipodal_classification(
    prime: int, R: int, source_states: list[tuple[int, int]]
) -> dict[str, object]:
    """Exhaust one target spectrum and classify its exact obstruction."""
    forms, square_divisor_count, target_divisor_hits = compensated.target_forms_for_R(
        prime, R
    )
    if forms:
        classification = "hit"
        target_in_generated_subgroup = True
    else:
        K = (prime * R + 1) // 4
        factors = sources.exact_factorization(K)
        certificate = obstruction.unit_group_subgroup_certificate(factors, R)
        target_in_generated_subgroup = bool(certificate["target_in_generated_subgroup"])
        classification = (
            "finite_exponent" if target_in_generated_subgroup else "subgroup_character"
        )
    two_residue_eligible = any(
        coordinate % 4 == 3
        for state in source_states
        for coordinate in state
    )
    minus_one_in_two_cyclic = False
    if two_residue_eligible:
        # R is odd, so 2 is a unit.  Euler's finite cyclic order is exact here.
        order = int(sympy.n_order(2, R))
        minus_one_in_two_cyclic = order % 2 == 0 and pow(2, order // 2, R) == R - 1
    return {
        "R": R,
        "source_state_count": len(source_states),
        "K_square_divisor_count": square_divisor_count,
        "target_divisor_hit_count": target_divisor_hits,
        "target_normal_form_count": len(forms),
        "target_in_generated_subgroup": target_in_generated_subgroup,
        "classification": classification,
        "two_residue_eligible": two_residue_eligible,
        "minus_one_in_two_cyclic": minus_one_in_two_cyclic,
    }


def audit_prime(prime: int) -> dict[str, object]:
    """Complete the linear spectrum for one selected pressure point."""
    bound, states_by_R = sources.enumerate_linear_source_states(prime)
    records = [
        antipodal_classification(prime, R, states)
        for R, states in sorted(states_by_R.items())
    ]
    counts = Counter(str(record["classification"]) for record in records)
    classification_counts = {name: int(counts[name]) for name in CLASSIFICATIONS}
    if sum(classification_counts.values()) != len(records):
        raise AssertionError("spectrum classifications do not partition the states")
    hit_R = [record["R"] for record in records if record["classification"] == "hit"]
    finite_R = [
        record["R"] for record in records if record["classification"] == "finite_exponent"
    ]
    subgroup_R = [
        record["R"]
        for record in records
        if record["classification"] == "subgroup_character"
    ]
    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "linear_R_count": len(records),
        "directed_linear_source_state_count": sum(
            len(states) for states in states_by_R.values()
        ),
        "classification_counts": classification_counts,
        "hit_R": hit_R,
        "finite_exponent_R": finite_R,
        "subgroup_character_R": subgroup_R,
        "two_residue_eligible_R_count": sum(
            bool(record["two_residue_eligible"]) for record in records
        ),
        "two_residue_subgroup_escape_R_count": sum(
            bool(record["two_residue_eligible"] and record["minus_one_in_two_cyclic"])
            for record in records
        ),
        "records": records,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Run the complete finite audit on the frozen 200-point set."""
    primes = selected_primes(input_path)
    records = [audit_prime(prime) for prime in primes]
    totals = Counter()
    for record in records:
        totals.update(record["classification_counts"])
    if sum(totals.values()) != sum(int(record["linear_R_count"]) for record in records):
        raise AssertionError("global classification counts do not partition all R")
    return {
        "arithmetic": (
            "select the 200 hash-frozen pressure points whose first general-B witness has B>1; "
            "for each point enumerate every directed linear source through the exact min(a,s) bound, "
            "deduplicate R, exhaust all d|K^2 with 4d=-1 (mod R), and classify each non-hit by exact "
            "membership of -1 in the prime-support subgroup"
        ),
        "scope_note": (
            "This is a complete finite full-spectrum audit on the 200-point stratum selected by "
            "first-witness B>1. The stratum is not a random sample, and the result is not a "
            "universal cross-source selector or a statement about all core primes."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "selected_prime_count": len(primes),
        "linear_R_exhaustively_checked": sum(
            int(record["linear_R_count"]) for record in records
        ),
        "directed_linear_source_state_count": sum(
            int(record["directed_linear_source_state_count"]) for record in records
        ),
        "classification_totals": {name: int(totals[name]) for name in CLASSIFICATIONS},
        "two_residue_eligible_R_count": sum(
            int(record["two_residue_eligible_R_count"]) for record in records
        ),
        "two_residue_subgroup_escape_R_count": sum(
            int(record["two_residue_subgroup_escape_R_count"]) for record in records
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
