#!/usr/bin/env python3
"""Validate the B=1,2 divisor-residue forms on the stored 100K complement."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "reproductions" / "type-i-dyadic-residual-general-edge-profile-100k-results.json"
SELECTOR = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-pminusone-b12-residue-selector-100k-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


selector = load_module("pminusone_b12_residue_selector", SELECTOR)


def residue_condition(E: int, B: int, C: int) -> bool:
    """The single divisor-residue condition for a fixed B."""
    R = E - 1
    return (4 * B * B * C + 1) % R == 0


def run_audit(profile_path: Path = PROFILE) -> dict[str, object]:
    """Check each p-1 minimum-source record through the B=1,2 residue selectors."""
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    records = [
        record
        for record in profile["records"]
        if int(record["minimum_source_distance"]["source_distance"]) == 1
    ]
    selected = []
    for record in records:
        prime = int(record["prime"])
        edge = record["minimum_source_distance"]
        E = int(edge["E"])
        B = int(edge["normal_form"][1])
        C = int(edge["normal_form"][2])
        K = int(edge["K"])
        if B not in {1, 2} or not residue_condition(E, B, C) or K % (B * C):
            raise AssertionError("stored p-1 edge does not satisfy the stated divisor-residue selector")
        H = K // (B * C)
        if B == 2 and H % 2 == 0:
            raise AssertionError("B=2 selector lost its odd complementary factor condition")
        witness = selector.p_minus_one_witness(prime, E, B, C)
        if witness is None:
            raise AssertionError("generic p-1 selector did not reconstruct the residue witness")
        if (
            int(witness["gap"]) != int(edge["gap"])
            or int(witness["source_denominator"]) != int(edge["source_denominator"])
            or int(witness["source_term"]) != int(edge["source_term"])
        ):
            raise AssertionError("reconstructed residue witness changed")
        selected.append({"prime": prime, "E": E, "B": B, "C": C, "H": H})

    b_histogram: dict[str, int] = {}
    e_values: set[int] = set()
    for entry in selected:
        key = str(entry["B"])
        b_histogram[key] = b_histogram.get(key, 0) + 1
        e_values.add(entry["E"])
    return {
        "arithmetic": (
            "for each p-1 minimum-source record in the 100K dyadic complement, check the exact B=1 or B=2 "
            "divisor-residue condition in K=((E-1)p+1)/4, the B=2 parity condition when applicable, "
            "and reconstruct both unit-fraction identities through the generic p-1 selector"
        ),
        "scope_note": (
            "A finite validation of the B=1,2 residue forms on the stored complement. It does not show that "
            "a fixed bridge menu or either residue condition succeeds for all core primes."
        ),
        "input_profile": profile_path.name,
        "p_minus_one_record_count": len(selected),
        "b_histogram": dict(sorted(b_histogram.items(), key=lambda item: int(item[0]))),
        "maximum_E": max(e_values),
        "E_values": sorted(e_values),
        "records": selected,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.profile)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
