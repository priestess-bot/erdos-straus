#!/usr/bin/env python3
"""Classify square-tail obstructions on the bounded-r H19 selector residual."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
SELECTOR_INPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json"
SMALL_R_SCRIPT = ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py"
SUBGROUP_SCRIPT = ROOT / "reproductions" / "type_ii_h19_fourth_even_source_subgroup_profile.py"
QUADRATIC_SCRIPT = ROOT / "reproductions" / "type_ii_h19_fourth_even_source_quadratic_character_profile.py"
DEFAULT_R_CAP = 9_999
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-bounded-r-tail-obstruction-1b-results.json"


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


small_r = load_script("bounded_r_tail_small_r", SMALL_R_SCRIPT)
subgroup = load_script("bounded_r_tail_subgroup", SUBGROUP_SCRIPT)
quadratic = load_script("bounded_r_tail_quadratic", QUADRATIC_SCRIPT)


def residual_primes(payload: dict[str, object], r_cap: int) -> list[int]:
    for stage in payload["stages"]:
        if int(stage["r_cap"]) == r_cap:
            return [int(prime) for prime in stage["uncovered_primes"]]
    raise ValueError("selector input has no stage for the requested r cap")


def classify_state(prime: int, r: int) -> dict[str, object] | None:
    """Classify one compatible state by subgroup membership and a quadratic separator."""
    rays = small_r.compatible_rays(prime, r)
    if not rays:
        return None
    m = (r * prime + 1) // 4
    tail_hits = small_r.tail_hit_count(prime, r)
    target = (-m) % r
    generators = sorted(sympy.factorint(m))
    inside, index, subgroup_order = subgroup.target_in_generated_subgroup(
        r, generators, target
    )
    if tail_hits and not inside:
        raise AssertionError("a tail hit cannot lie outside its generated subgroup")
    classification = (
        "hit"
        if tail_hits
        else "finite-product-set"
        if inside
        else "subgroup-character"
    )
    support = None
    if classification == "subgroup-character":
        support = quadratic.separating_quadratic_support(r, generators, target)
        if support is None:
            raise AssertionError("subgroup-character state lacks a quadratic separator")
        if quadratic.quadratic_character(support, -1) != -1:
            raise AssertionError("separator does not distinguish the negative tail target")
    return {
        "r": r,
        "compatible_ray_count": len(rays),
        "tail_residue_factor_count": tail_hits,
        "target_residue": target,
        "generator_primes": generators,
        "generated_subgroup_index": index,
        "generated_subgroup_order": subgroup_order,
        "classification": classification,
        "quadratic_character_support": list(support) if support is not None else None,
    }


def run_audit(payload: dict[str, object], r_cap: int = DEFAULT_R_CAP) -> dict[str, object]:
    """Classify every compatible bounded-r state for the selected fixed-cap residual."""
    if r_cap < 7 or r_cap % 4 != 3:
        raise ValueError("r cap must be at least seven and 3 modulo 4")
    records = []
    for prime in residual_primes(payload, r_cap):
        states = [
            state
            for r in range(7, r_cap + 1, 8)
            if (state := classify_state(prime, r)) is not None
        ]
        if not states:
            raise AssertionError("selected residual unexpectedly has no compatible state")
        if any(int(state["tail_residue_factor_count"]) for state in states):
            raise AssertionError("selected residual unexpectedly has a bounded-r tail hit")
        counts = Counter(str(state["classification"]) for state in states)
        records.append(
            {
                "prime": prime,
                "compatible_state_count": len(states),
                "classification_counts": dict(sorted(counts.items())),
                "states": states,
            }
        )
    all_states = [state for record in records for state in record["states"]]
    histogram = Counter(str(state["classification"]) for state in all_states)
    subgroup_states = [
        state for state in all_states if state["classification"] == "subgroup-character"
    ]
    return {
        "arithmetic": (
            "exact factor-pair and M1-squared tail tests, followed by prime-power "
            "CRT discrete logarithms, HNF subgroup membership, and exhaustive "
            "quadratic-character separation"
        ),
        "scope_note": (
            "A finite obstruction profile for the r-capped residual. It does not "
            "prove a tail obstruction beyond the cap or a global selector failure."
        ),
        "prime_limit": payload["prime_limit"],
        "r_cap": r_cap,
        "residual_prime_count": len(records),
        "compatible_state_count": len(all_states),
        "classification_counts": dict(sorted(histogram.items())),
        "all_subgroup_character_states_quadratically_separated": all(
            state["quadratic_character_support"] is not None for state in subgroup_states
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selector-input", type=Path, default=SELECTOR_INPUT)
    parser.add_argument("--r-cap", type=int, default=DEFAULT_R_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.selector_input.read_text(encoding="utf-8"))
    result = run_audit(payload, args.r_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
