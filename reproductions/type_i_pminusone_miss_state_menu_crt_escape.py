#!/usr/bin/env python3
"""Construct a Dirichlet escape for the fixed 500M p-minus-one residual states."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-pminusone-miss-upper-half-profile-500m-results.json"
SOURCE_MODULUS = ROOT / "reproductions" / "type_i_source_square_modulus.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-pminusone-miss-state-menu-crt-escape-500m-results.json"
ESCAPE_RESIDUE = 1


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


source_modulus = load_module("pminusone_miss_state_menu_modulus", SOURCE_MODULUS)


def state_rows(profile: dict[str, object]) -> list[dict[str, int]]:
    """Deduplicate the observed source-square states by their necessary data (s,E)."""
    rows: set[tuple[int, int]] = set()
    for record in profile["records"]:
        shift = int(record["source_distance"])
        E = int(record["E"])
        R = int(record["R"])
        if shift <= 0 or E % 2 or (E - 1) % shift or R != (E - 1) // shift or R % 2 != 1:
            raise AssertionError("stored upper-half record did not reconstruct its source state")
        rows.add((shift, E))
    return [
        {"shift": shift, "E": E, "source_modulus": source_modulus.source_square_modulus(E)}
        for shift, E in sorted(rows)
    ]


def run_audit(profile: dict[str, object], residue: int = ESCAPE_RESIDUE) -> dict[str, object]:
    """Verify that one reduced core progression avoids every fixed source state."""
    rows = state_rows(profile)
    combined_modulus = math.lcm(24, *(row["source_modulus"] for row in rows))
    if residue % 24 != 1 or math.gcd(residue, combined_modulus) != 1:
        raise AssertionError("escape residue is not a reduced core-prime progression")
    compatible = [
        row
        for row in rows
        if residue % row["source_modulus"] == row["shift"] % row["source_modulus"]
    ]
    if compatible:
        raise AssertionError("escape residue retained a source-square-compatible menu state")
    representative = residue + combined_modulus
    direct_compatible = [
        row
        for row in rows
        if source_modulus.direct_source_square_allowed(representative - row["shift"], row["E"])
    ]
    if direct_compatible:
        raise AssertionError("direct source-square check disagreed with the congruence escape")
    return {
        "arithmetic": (
            "deduplicate the 500M p-minus-one residual's minimized upper-half bridges by (s=p-n,E); "
            "for each state compute the exact source-square modulus Lambda(E), take their lcm with 24, "
            "and verify the reduced core residue p=1 avoids every necessary p=s mod Lambda(E) condition"
        ),
        "scope_note": (
            "Dirichlet's theorem gives infinitely many core primes in the verified progression, so the "
            "fixed observed (s,E) menu cannot be a global Type I selector. This does not exclude source "
            "states outside the menu, a p-dependent selection rule, or Type II certificates."
        ),
        "input_artifact": INPUT.name,
        "p_minus_one_miss_count": int(profile["p_minus_one_miss_count"]),
        "fixed_source_state_count": len(rows),
        "source_states": rows,
        "combined_modulus": combined_modulus,
        "escape_residue": residue,
        "core_residue_mod_24": residue % 24,
        "coprime_to_combined_modulus": math.gcd(residue, combined_modulus) == 1,
        "representative_positive_source_target": representative,
        "source_compatible_state_count": len(compatible),
        "direct_source_compatible_state_count": len(direct_compatible),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
