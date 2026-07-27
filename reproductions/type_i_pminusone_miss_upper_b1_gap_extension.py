#!/usr/bin/env python3
"""Extend the sole 500M p-minus-one upper-B=1 miss past the m<=215 box.

The completed source-reselection profile leaves one upper-half B=1 miss inside
the common m<=215 box.  This script exhausts only the next four admissible
gaps through m=231 and rebuilds every resulting source-state B=1 certificate.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-pminusone-miss-upper-b3-reselection-profile-500m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
RESELECTION = ROOT / "reproductions" / "type_i_pminusone_miss_upper_b3_reselection_profile.py"
INITIAL_GAP_CAP = 215
DEFAULT_GAP_CAP = 231
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-pminusone-miss-upper-b1-gap-extension-500m-results.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("pminusone_b1_gap_extension_landscape", LANDSCAPE)
bridge = load_module("pminusone_b1_gap_extension_bridge", BRIDGE)
reselection = load_module("pminusone_b1_gap_extension_reselection", RESELECTION)


def upper_b_one_candidates(
    prime: int, start_gap: int, gap_cap: int
) -> tuple[list[dict[str, object]], int, int]:
    """Exhaust B=1 upper-half strict lifts in the stated extension window."""
    if start_gap % 4 != 3 or gap_cap % 4 != 3 or start_gap >= gap_cap:
        raise ValueError("gap bounds must be distinct and congruent to 3 modulo 4")
    candidates: list[dict[str, object]] = []
    forms_checked = 0
    lifts_checked = 0
    for gap in range(start_gap + 4, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            if B != 1:
                continue
            forms_checked += 1
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            lifts_checked += len(lifts)
            for lift in lifts:
                source = int(lift["source_denominator"])
                if source % 2 or 2 * source < prime + 1:
                    continue
                divisor = int(lift["bridge_divisor"])
                if divisor % (prime * prime):
                    raise AssertionError("reverse lift did not reconstruct a bridge factor")
                bridge_factor = divisor // (prime * prime)
                witness = reselection.B_one_realization(prime, source, bridge_factor)
                if witness is None:
                    raise AssertionError("a stored B=1 normal form failed the source-state criterion")
                candidates.append(
                    {
                        "gap": gap,
                        "normal_form": [A, B, C],
                        "source_denominator": source,
                        "source_distance": prime - source,
                        "E": bridge_factor,
                        "B_one_realization": witness,
                    }
                )
    return candidates, forms_checked, lifts_checked


def run_profile(previous: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    """Close the prior short-box B=1 residual through the given extension cap."""
    residual_count = int(previous["p_minus_one_residual_count"])
    direct = int(previous["stored_upper_B_eq_1_count"])
    reselected = int(previous["reselected_upper_B_eq_1_count"])
    misses = previous["upper_B_eq_1_misses"]
    if residual_count != 185 or direct != 119 or reselected != 65:
        raise AssertionError("input is not the expected completed m<=215 source-reselection profile")
    if not isinstance(misses, list) or len(misses) != 1:
        raise AssertionError("input must contain exactly one short-box B=1 miss")

    extensions: list[dict[str, object]] = []
    unresolved: list[int] = []
    forms_checked = 0
    lifts_checked = 0
    for miss in misses:
        if not isinstance(miss, dict):
            raise AssertionError("input contains a malformed B=1 miss")
        prime = int(miss["prime"])
        candidates, local_forms, local_lifts = upper_b_one_candidates(
            prime, INITIAL_GAP_CAP, gap_cap
        )
        forms_checked += local_forms
        lifts_checked += local_lifts
        if not candidates:
            unresolved.append(prime)
            continue
        first_gap = min(int(candidate["gap"]) for candidate in candidates)
        first_gap_candidates = [
            candidate for candidate in candidates if int(candidate["gap"]) == first_gap
        ]
        selected = min(
            first_gap_candidates,
            key=lambda candidate: (
                int(candidate["source_distance"]),
                int(candidate["E"]),
            ),
        )
        extensions.append(
            {
                "prime": prime,
                "first_upper_B_eq_1_gap_in_extension": first_gap,
                "first_gap_upper_B_eq_1_candidates": first_gap_candidates,
                "selected_first_gap_upper_B_eq_1_candidate": selected,
            }
        )

    previous_closure = direct + reselected
    if previous_closure + len(misses) != residual_count:
        raise AssertionError("short-box profile did not partition the p-minus-one residual")
    if len(extensions) + len(unresolved) != len(misses):
        raise AssertionError("extension did not partition the short-box B=1 residual")
    return {
        "arithmetic": (
            "take the exact upper-half B=1 residual from the completed m<=215 p-minus-one profile; "
            "for every subsequent admissible gap through the stated cap, exhaust B=1 Type I normal forms "
            "and strict maximum-tail lifts, retain even upper-half sources, then rebuild the exact B=1 "
            "source-state divisor-residue certificate"
        ),
        "scope_note": (
            "A four-gap finite extension of one short-box residual. It shows that the m<=215 B=3 fallback "
            "does not establish a global B=1 obstruction, but it supplies no uniform gap bound or global selector."
        ),
        "input_artifact": INPUT.name,
        "p_minus_one_residual_count": residual_count,
        "initial_gap_cap": INITIAL_GAP_CAP,
        "initial_upper_B_eq_1_closure_count": previous_closure,
        "extension_gap_cap": gap_cap,
        "extension_normal_forms_exhaustively_checked": forms_checked,
        "extension_strict_reverse_lifts_exhaustively_checked": lifts_checked,
        "extension_released_count": len(extensions),
        "upper_B_eq_1_closure_count": previous_closure + len(extensions),
        "upper_B_eq_1_unresolved_count": len(unresolved),
        "extension_records": extensions,
        "unresolved_primes": unresolved,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(json.loads(args.input.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {key: value for key, value in result.items() if key not in {"extension_records", "unresolved_primes"}},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
