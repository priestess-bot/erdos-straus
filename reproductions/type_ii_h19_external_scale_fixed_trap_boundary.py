#!/usr/bin/env python3
"""Exhaust fixed-factor Type II traps on every k=23 residual progression.

For each of the eighteen admissible children in the H19 external-scale
k=23 modulo-29 split, write p=P*n+C and x=(p+m)/4=S*n+x0, S=P/4.
The fixed-factor progression-trap lemma can only use a future gap m dividing
S.  This script exhausts every such m in the Type II natural range and every
divisor of E=gcd(S,x0), checking d=a*x/E exactly.  No child has a trap.

This is a complete boundary for this single fixed-factor mechanism on the
displayed progressions, not for arbitrary future Type II certificates.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-h19-external-scale-fixed-trap-boundary.json"
BRANCHING_SCRIPT = (
    ROOT / "reproductions" / "type_ii_h19_external_scale_k23_branching.py"
)
H19_MAX_GAP = 4 * 19 - 1


def load_branching():
    spec = importlib.util.spec_from_file_location(
        "h19_external_scale_k23_branching", BRANCHING_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load k=23 branching script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


branching = load_branching()
divisors = branching.renewal.divisors


def traps_for_progression(coefficient: int, constant: int) -> dict[str, object]:
    """Exhaust the fixed-factor trap lemma for p=coefficient*n+constant."""
    if coefficient % 4 or constant % 24 != 1:
        raise AssertionError("progression must preserve core integrality")
    step = coefficient // 4
    gaps = [
        gap
        for gap in divisors(step)
        if gap % 4 == 3 and H19_MAX_GAP < gap <= constant - 2
    ]
    traps: list[dict[str, int]] = []
    for gap in gaps:
        x0 = (constant + gap) // 4
        fixed_factor = math.gcd(step, x0)
        if (step // fixed_factor) % gap:
            continue
        cofactor = x0 // fixed_factor
        target = (-x0) % gap
        for scale in divisors(fixed_factor):
            if scale * cofactor % gap == target:
                traps.append(
                    {
                        "gap": gap,
                        "future_shift": (gap + 1) // 4,
                        "fixed_factor": fixed_factor,
                        "cofactor": cofactor,
                        "target_factor": scale,
                    }
                )
                break
    return {
        "prime_step": coefficient,
        "prime_residue": constant,
        "first_gap_exclusive": H19_MAX_GAP,
        "candidate_gap_count": len(gaps),
        "traps": traps,
    }


def run_audit() -> dict[str, object]:
    """Audit all residual progressions from the exact k=23 split."""
    source = branching.run_audit()
    residuals = [
        branch for branch in source["branches"] if branch["admissible_escape"]
    ]
    rows = []
    for branch in residuals:
        prime_form = branch["prime_form"]
        audit = traps_for_progression(
            int(prime_form["coefficient"]), int(prime_form["constant"])
        )
        rows.append({"v_mod_29": branch["v_mod_29"], **audit})
    if len(rows) != 18 or any(row["traps"] for row in rows):
        raise AssertionError("unexpected fixed-factor trap in a residual branch")
    if {int(row["candidate_gap_count"]) for row in rows} != {564}:
        raise AssertionError("unexpected complete candidate-gap count")

    return {
        "arithmetic": (
            "complete divisor enumeration of every permitted future gap m|S, "
            "exact gcd extraction E=gcd(S,x0), and exhaustive divisor checks "
            "for the fixed-factor Type II trap d=a*x/E"
        ),
        "scope_note": (
            "Empty output excludes only the fixed-factor progression-trap "
            "mechanism on these eighteen progressions. It does not exclude "
            "multi-factor certificates, adaptive shifts, or strict descents."
        ),
        "source_state": {
            "claim_id": "type-II-h19-external-scale-k23-branching",
            "residual_branch_count": len(rows),
        },
        "residual_progressions": rows,
        "total_candidate_gap_count": sum(
            int(row["candidate_gap_count"]) for row in rows
        ),
    }


def main() -> int:
    payload = run_audit()
    RESULTS.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
