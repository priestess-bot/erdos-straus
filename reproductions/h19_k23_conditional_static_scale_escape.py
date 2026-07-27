#!/usr/bin/env python3
"""Compile conditional simultaneous escapes for all 14 H19-k23 states.

Each residual branch has 20 H19 private-cofactor affine forms and 37
stationary-source private forms.  If those forms are simultaneously prime,
then every displayed Type II ray and every complete square-tail source
descent has only its fixed factor and one new prime cofactor available.
The precomputed residue profiles show that all 56 exits miss in this model.

The script proves only finite admissibility and the exact residue implication.
Dickson's conjecture or Schinzel's Hypothesis H is additionally needed for the
infinite-prime conclusion.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "h19-k23-conditional-static-scale-escape.json"
MIXED_BOUNDARY_SCRIPT = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"


def load_mixed_boundary():
    spec = importlib.util.spec_from_file_location(
        "h19_k23_conditional_escape_mixed_boundary", MIXED_BOUNDARY_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load mixed-factor boundary")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


mixed_boundary = load_mixed_boundary()
branching = mixed_boundary.branching


def source_private_form(
    coefficient: int, constant: int, scale: int
) -> tuple[dict[str, object], tuple[int, int, str]]:
    """Recover the prime private cofactor form and its complete tail miss."""
    profile, form = branching.source_profile(coefficient, constant, scale)
    if profile["target_hits"]:
        raise AssertionError("post-affine residual source unexpectedly closes")
    return (
        {
            "k": scale,
            "q": profile["q"],
            "fixed_factor": profile["fixed_factor"],
            "target_residue": profile["target_residue"],
            "divisor_residue_count": profile["divisor_residue_count"],
            "private_form": {
                "coefficient": form[0],
                "constant": form[1],
            },
        },
        form,
    )


def conditional_state(branch: dict[str, object]) -> dict[str, object]:
    """Verify one admissible branch and list all prime-cofactor obligations."""
    form = branch["prime_form"]
    coefficient = int(form["coefficient"])
    constant = int(form["constant"])
    scales = tuple(branching.SCALES)
    sources_and_forms = [
        source_private_form(coefficient, constant, scale) for scale in scales
    ]
    source_rows = [row for row, _ in sources_and_forms]
    source_forms = tuple(private_form for _, private_form in sources_and_forms)
    h19_forms = branching.boundary.affine_forms(
        constant, coefficient, branching.boundary.canonical_fan(19)
    )
    all_forms = h19_forms + source_forms
    if len(all_forms) != 57:
        raise AssertionError("expected p plus 19 rays and 37 sources")
    if any(coefficient_form <= 0 or math.gcd(coefficient_form, constant_form) != 1
           for coefficient_form, constant_form, _ in all_forms):
        raise AssertionError("all Dickson forms must be primitive and positive")
    covering = tuple(branching.boundary.covering_primes(all_forms))
    if covering or not branch["admissible_escape"]:
        raise AssertionError("residual branch must remain admissible")
    if branching.ray_hits(coefficient, constant):
        raise AssertionError("post-affine residual unexpectedly has an H19 exit")
    return {
        "v_mod_29": branch["v_mod_29"],
        "prime_form": form,
        "h19_private_form_count": len(h19_forms),
        "stationary_source_count": len(source_rows),
        "combined_form_count": len(all_forms),
        "covering_primes": list(covering),
        "h19_ray_certificate": False,
        "complete_square_tail_source_hits": 0,
        "sources": source_rows,
    }


def run_audit() -> dict[str, object]:
    """Compile the exact finite premises for the conditional escape theorem."""
    states = [conditional_state(branch) for branch in mixed_boundary.remaining_branches()]
    if len(states) != 14:
        raise AssertionError("expected fourteen post-affine residual branches")
    if any(
        state["combined_form_count"] != 57
        or state["covering_primes"]
        or state["h19_ray_certificate"]
        or state["complete_square_tail_source_hits"] != 0
        for state in states
    ):
        raise AssertionError("conditional escape prerequisites are incomplete")
    return {
        "arithmetic": (
            "exact affine private-cofactor forms, complete source-square-tail "
            "residue misses, complete H19 ray misses, and finite-field "
            "admissibility checks"
        ),
        "scope_note": (
            "The displayed finite facts are unconditional. Infinitely many "
            "simultaneous prime values require Dickson's prime-tuples "
            "conjecture or Schinzel's Hypothesis H; this is not a "
            "counterexample to Erdos--Straus."
        ),
        "conditional_consequence": (
            "For each state, if its 57 primitive affine forms are "
            "simultaneously prime at arbitrarily large parameters, then H19 "
            "and all 37 stationary complete-square-tail source descents fail "
            "there."
        ),
        "state_count": len(states),
        "h19_private_form_count_per_state": 20,
        "stationary_source_count_per_state": 37,
        "combined_form_count_per_state": 57,
        "states": states,
    }


def main() -> int:
    payload = run_audit()
    RESULTS.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    summary = {
        key: payload[key]
        for key in (
            "state_count",
            "h19_private_form_count_per_state",
            "stationary_source_count_per_state",
            "combined_form_count_per_state",
            "conditional_consequence",
        )
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
