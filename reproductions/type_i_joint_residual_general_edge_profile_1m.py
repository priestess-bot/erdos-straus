#!/usr/bin/env python3
"""Profile unrestricted-source low-B edges on a stored p-1 residual set."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOW_E = ROOT / "reproductions" / "type-i-pminusone-low-e1m-all-b-joint-residual-profile-1m-results.json"
GENERAL = ROOT / "reproductions" / "type_i_dyadic_residual_general_edge_profile_100k.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-joint-residual-general-edge-profile-1m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


general = load_module("joint_residual_general_edge", GENERAL)


def run_profile(low_e_path: Path = LOW_E) -> dict[str, object]:
    """Exhaust all low-B normal edges on the p-1 residuals left by a stored profile."""
    low_e = json.loads(low_e_path.read_text(encoding="utf-8"))
    residuals = [int(prime) for prime in low_e["misses"]]
    if not residuals:
        raise ValueError("input residual profile is already closed")
    records = []
    form_count = 0
    lift_count = 0
    candidate_count = 0
    for prime in residuals:
        candidates, forms, lifts = general.all_low_b_even_edges(prime)
        if not candidates:
            raise AssertionError(f"joint residual {prime} escaped B<=4")
        minimum_source_distance = min(candidates, key=general.source_distance_key)
        minimum_odd_bridge = min(candidates, key=general.odd_bridge_key)
        general.verify_witness(prime, minimum_source_distance)
        general.verify_witness(prime, minimum_odd_bridge)
        form_count += forms
        lift_count += lifts
        candidate_count += len(candidates)
        records.append(
            {
                "prime": prime,
                "b_bounded_normal_form_count": forms,
                "b_bounded_strict_reverse_lift_count": lifts,
                "strict_even_candidate_count": len(candidates),
                "minimum_source_distance": minimum_source_distance,
                "minimum_odd_bridge": minimum_odd_bridge,
            }
        )
    minimum_source = [record["minimum_source_distance"] for record in records]
    return {
        "arithmetic": (
            "for each p-1 residual of the stored finite profile, enumerate every natural Type I gap, "
            "every B<=4 normal form, and every maximum-tail reverse bridge; retain strict even sources and "
            "independently reconstruct the selected target and source identities"
        ),
        "scope_note": (
            "A complete finite general-source refinement of the stated residual set. It does not establish a "
            "universal bound on source distance, B, or bridge factors."
        ),
        "prime_limit": low_e["prime_limit"],
        "input_residual_count": len(residuals),
        "b_cap": 4,
        "b_bounded_normal_form_count": form_count,
        "b_bounded_strict_reverse_lift_count": lift_count,
        "strict_even_candidate_count": candidate_count,
        "minimum_source_distance_histogram": dict(
            sorted(Counter(str(witness["source_distance"]) for witness in minimum_source).items(), key=lambda item: int(item[0]))
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--low-e", type=Path, default=LOW_E)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.low_e)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
