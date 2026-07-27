#!/usr/bin/env python3
"""Verify a Dirichlet-compatible source-side escape class for the finite bridge menu."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIDGE_MENU = ROOT / "reproductions" / "type_i_adaptive_bridge_menu_profile.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-fixed-bridge-menu-crt-escape-results.json"
ESCAPE_RESIDUE = 73
EXPECTED_MODULUS = 781_779_462_544_080


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


bridge_menu = load_module("fixed_bridge_menu_escape_menu", BRIDGE_MENU)


def all_positive_odd_bridge_states(E: int) -> tuple[tuple[int, int, int], ...]:
    """Include R=1 as well: the CRT obstruction is source-side, not selector-specific."""
    return bridge_menu.odd_shift_states(E, minimum_R=1)


def run_audit(
    E_menu: tuple[int, ...] = bridge_menu.E_MENU,
    residue: int = ESCAPE_RESIDUE,
) -> dict[str, object]:
    """Check that one reduced core residue class avoids every source-compatible menu state."""
    states = [
        {"E": E, "shift": shift, "R": R, "source_modulus": modulus}
        for E in E_menu
        for shift, R, modulus in all_positive_odd_bridge_states(E)
    ]
    modulus = math.lcm(24, *(state["source_modulus"] for state in states))
    if modulus != EXPECTED_MODULUS:
        raise AssertionError("the finite bridge menu or its exact source moduli changed")
    if residue % 24 != 1 or math.gcd(residue, modulus) != 1:
        raise AssertionError("escape residue is not a reduced core-prime progression")
    compatible = [
        state for state in states if residue % state["source_modulus"] == state["shift"] % state["source_modulus"]
    ]
    if compatible:
        raise AssertionError(f"escape residue retained {len(compatible)} source-compatible bridge states")
    representative = residue + modulus
    direct_compatible = [
        state
        for state in states
        if bridge_menu.source_modulus.direct_source_square_allowed(
            representative - state["shift"], state["E"]
        )
    ]
    if direct_compatible:
        raise AssertionError("direct source-square definition disagreed with the CRT escape")
    return {
        "arithmetic": (
            "for every E in the fixed bridge menu and every positive odd factorization E=sR+1, compute "
            "Lambda(E), take the lcm with 24, and verify that the reduced core residue p=73 avoids every "
            "necessary source congruence p=s (mod Lambda(E))"
        ),
        "scope_note": (
            "By Dirichlet's theorem the verified reduced progression contains infinitely many primes, so this "
            "fixed bridge menu has infinitely many source-side escapes. This does not exclude bridges outside "
            "the menu, alternative Type I coordinates, or Type II descent."
        ),
        "E_menu": list(E_menu),
        "positive_odd_state_count": len(states),
        "combined_modulus": modulus,
        "escape_residue": residue,
        "representative_positive_source_target": representative,
        "core_residue_mod_24": residue % 24,
        "coprime_to_combined_modulus": math.gcd(residue, modulus) == 1,
        "source_compatible_state_count": len(compatible),
        "direct_source_compatible_state_count": len(direct_compatible),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
