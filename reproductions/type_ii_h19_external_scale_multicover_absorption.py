#!/usr/bin/env python3
"""Exhibit a zero-exit local-cover split in the enriched H19 scale state.

The d=10 residual child of the k=23 modulo-29 split has all 144 scales
dividing 1200600 available throughout its parameter progression.  H19 plus
these sources has five covering primes: 7, 37, 53, 61, 73.  Splitting by the
smallest one, 7, absorbs precisely that cover in every child.  All seven
children retain the other four covers and have neither an H19 ray certificate
nor a complete external-source descent among the 144 scales.

This is an exact counterexample to the proposed one-step contraction rule
"every local cover has a positive fraction of immediate certificate/descent
children" in this one-private-cofactor plus complete-source model.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT / "reproductions" / "type-ii-h19-external-scale-multicover-absorption.json"
)
BRANCHING_SCRIPT = (
    ROOT / "reproductions" / "type_ii_h19_external_scale_k23_branching.py"
)

PARENT_PARAMETER_SCALE = 3335
PARENT_PARAMETER_OFFSET = 1197
SPLIT_PRIME = 7
SCALES_GCD = 1_200_600
EXPECTED_PARENT_COVERS = [7, 37, 53, 61, 73]
EXPECTED_CHILD_COVERS = [37, 53, 61, 73]


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
renewal = branching.renewal
boundary = branching.boundary
SCALES = renewal.divisors(SCALES_GCD)


def affine_data(parameter_scale: int, parameter_offset: int) -> tuple[int, int]:
    coefficient = 6 * 77_597_520 * parameter_scale
    constant = 6 * 77_597_520 * parameter_offset + renewal.H19_RESIDUE
    return coefficient, constant


def inspect(parameter_scale: int, parameter_offset: int) -> dict[str, object]:
    """Return every relevant source and ray outcome without early exit."""
    coefficient, constant = affine_data(parameter_scale, parameter_offset)
    primitive = constant % 24 == 1 and math.gcd(coefficient, constant) == 1
    if not primitive:
        raise AssertionError("this absorption witness must keep a primitive prime form")

    source_rows: list[dict[str, object]] = []
    source_forms: list[tuple[int, int, str]] = []
    for scale in SCALES:
        row, form = branching.source_profile(coefficient, constant, scale)
        source_rows.append(row)
        source_forms.append(form)
    h19_forms = boundary.affine_forms(
        constant, coefficient, boundary.canonical_fan(19)
    )
    return {
        "parameter_scale": parameter_scale,
        "parameter_offset": parameter_offset,
        "prime_form": {"coefficient": coefficient, "constant": constant},
        "h19_ray_hits": branching.ray_hits(coefficient, constant),
        "source_hits": [row for row in source_rows if row["target_hits"]],
        "combined_form_count": len(h19_forms) + len(source_forms),
        "covering_primes": list(
            boundary.covering_primes(h19_forms + tuple(source_forms))
        ),
    }


def run_audit() -> dict[str, object]:
    """Return the five-cover parent and all seven zero-exit children."""
    parent = inspect(PARENT_PARAMETER_SCALE, PARENT_PARAMETER_OFFSET)
    if (
        parent["h19_ray_hits"]
        or parent["source_hits"]
        or parent["covering_primes"] != EXPECTED_PARENT_COVERS
    ):
        raise AssertionError("unexpected enriched parent state")

    children = [
        inspect(
            PARENT_PARAMETER_SCALE * SPLIT_PRIME,
            PARENT_PARAMETER_OFFSET + PARENT_PARAMETER_SCALE * residue_class,
        )
        for residue_class in range(SPLIT_PRIME)
    ]
    if any(
        child["h19_ray_hits"]
        or child["source_hits"]
        or child["covering_primes"] != EXPECTED_CHILD_COVERS
        for child in children
    ):
        raise AssertionError("modulo-7 split must absorb only the first cover")

    return {
        "arithmetic": (
            "exact forced-factor extraction, complete square-divisor source "
            "residue sets, explicit H19 ray-divisor checks, and a complete "
            "modulo-7 split of the five-cover state"
        ),
        "scope_note": (
            "This refutes only a one-step positive-exit-fraction rule in the "
            "stated model. It does not rule out a multi-cover or deeper "
            "state-transition theorem."
        ),
        "path": {
            "from_k23_branch_residue": 10,
            "stationary_scale_gcd": SCALES_GCD,
            "stationary_scale_count": len(SCALES),
            "parent_progression": "p=6*Q19*(3335*w+1197)+8328961",
        },
        "parent": parent,
        "parameter_split": "w=7*z+c",
        "children": [
            {"w_mod_7": residue_class, **child}
            for residue_class, child in enumerate(children)
        ],
        "immediate_exit_count": 0,
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
