#!/usr/bin/env python3
"""Audit a scale-extension renewal in the H19 external-source model.

Start with p=6*Q19*t+r, r=8328961.  The H19 one-private-cofactor fan and
the complete external-source models at scales

    1, 2, 3, 4, 5, 6, 8, 9, 12, 15

are jointly admissible.  Adding scale 10 makes the displayed prime forms
locally covered by 5.  This is not a closure: after the exact split
t=5*u+c, every c modulo 5 again has an admissible state, now including
scale 10.  The script recomputes all forced factors and complete
square-divisor residue sets after each split.

As throughout these one-private-cofactor constructions, Dickson's conjecture
or Schinzel's Hypothesis H is needed to turn an admissible form family into
infinitely many actual primes.  This is a conditional boundary, not a
counterexample to Erdos--Straus.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT
    / "reproductions"
    / "type-ii-h19-external-scale-renewal-k10-results.json"
)
BOUNDARY_SCRIPT = ROOT / "reproductions" / "type_ii_prime_cofactor_boundary.py"
EXTERNAL_SCRIPT = (
    ROOT / "reproductions" / "type_ii_h19_external_source_conditional_escape.py"
)

H19_RESIDUE = 8_328_961
BASE_SCALES = (1, 2, 3, 4, 5, 6, 8, 9, 12, 15)
EXTENDED_SCALES = BASE_SCALES + (10,)


def divisors(value: int) -> tuple[int, ...]:
    """Return every positive divisor in increasing order."""
    result: list[int] = []
    for divisor in range(1, math.isqrt(value) + 1):
        if value % divisor:
            continue
        result.append(divisor)
        paired = value // divisor
        if paired != divisor:
            result.append(paired)
    return tuple(sorted(result))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


boundary = load_module("h19_scale_renewal_boundary", BOUNDARY_SCRIPT)
external = load_module("h19_scale_renewal_external", EXTERNAL_SCRIPT)


def state(parameter_scale: int, parameter_offset: int, scales: tuple[int, ...]):
    """Build p=6Q(parameter_scale*u+parameter_offset)+r exactly."""
    fan = boundary.canonical_fan(19)
    modulus = boundary.fan_modulus(fan)
    if modulus != 77_597_520:
        raise AssertionError("unexpected H19 modulus")
    if parameter_scale < 1 or not 0 <= parameter_offset < parameter_scale:
        raise ValueError("invalid affine parameter branch")

    coefficient = 6 * modulus * parameter_scale
    constant = 6 * modulus * parameter_offset + H19_RESIDUE
    if constant % 24 != 1 or math.gcd(coefficient, constant) != 1:
        raise AssertionError("the target prime form must remain primitive and core")

    if not all(
        boundary.ray_safe_with_one_prime_cofactor(
            constant, coefficient, shift, a, c
        )
        for shift, a, c in fan
    ):
        raise AssertionError("a reported H19 ray must stay safe after the split")
    h19_forms = boundary.affine_forms(constant, coefficient, fan)
    if len(h19_forms) != 20:
        raise AssertionError("H19 must contribute p plus nineteen quotients")

    source_rows: list[dict[str, object]] = []
    source_forms: list[tuple[int, int, str]] = []
    for scale in scales:
        if (constant - 1) % (4 * scale) or coefficient % (4 * scale):
            raise AssertionError("selected scale is not available throughout branch")
        row, form = external.source_state(constant, coefficient // 3, 0, scale)
        source_rows.append(row)
        source_forms.append(form)

    forms = h19_forms + tuple(source_forms)
    if any(math.gcd(a, b) != 1 for a, b, _ in forms):
        raise AssertionError("all displayed prime forms must be primitive")
    return {
        "parameter_scale": parameter_scale,
        "parameter_offset": parameter_offset,
        "prime_form": {"coefficient": coefficient, "constant": constant},
        "h19_form_count": len(h19_forms),
        "sources": source_rows,
        "forms": [
            {"coefficient": a, "constant": b, "label": label}
            for a, b, label in forms
        ],
        "combined_form_count": len(forms),
        "covering_primes": list(boundary.covering_primes(forms)),
    }


def covering_root_map(forms: list[dict[str, object]], prime: int) -> dict[str, list[str]]:
    """Record why a local prime covers a form family."""
    roots: dict[str, list[str]] = {}
    for residue_class in range(prime):
        labels = [
            str(form["label"])
            for form in forms
            if (
                int(form["coefficient"]) * residue_class + int(form["constant"])
            )
            % prime
            == 0
        ]
        roots[str(residue_class)] = labels
    if any(not labels for labels in roots.values()):
        raise AssertionError("claimed covering prime leaves an uncovered residue")
    return roots


def run_audit() -> dict[str, object]:
    """Return the pre-cover, covered extension, and all renewal branches."""
    base = state(1, 0, BASE_SCALES)
    if base["covering_primes"]:
        raise AssertionError("the pre-extension state must be admissible")

    covered = state(1, 0, EXTENDED_SCALES)
    if covered["covering_primes"] != [5]:
        raise AssertionError("adding k=10 must create exactly the local 5 cover")
    roots = covering_root_map(covered["forms"], 5)

    renewal_branches = [state(5, residue, EXTENDED_SCALES) for residue in range(5)]
    if any(branch["covering_primes"] for branch in renewal_branches):
        raise AssertionError("every residue branch must renew admissibility")
    if any(branch["combined_form_count"] != 31 for branch in renewal_branches):
        raise AssertionError("each renewed state must contain all H19 and sources")

    # These are exactly the scales k which remain available for every u and
    # every one of the five children, not merely a selected finite subfamily.
    stationary_scale_gcd = math.gcd(
        *[
            math.gcd(
                (int(branch["prime_form"]["constant"]) - 1) // 4,
                int(branch["prime_form"]["coefficient"]) // 4,
            )
            for branch in renewal_branches
        ]
    )
    stationary_scales = divisors(stationary_scale_gcd)
    if stationary_scale_gcd != 360 or len(stationary_scales) != 24:
        raise AssertionError("unexpected common stationary-scale lattice")
    stationary_branches = [
        state(5, residue, stationary_scales) for residue in range(5)
    ]
    if any(branch["covering_primes"] for branch in stationary_branches):
        raise AssertionError("all common stationary scales must still be admissible")
    if any(branch["combined_form_count"] != 44 for branch in stationary_branches):
        raise AssertionError("H19 plus all common stationary scales has 44 forms")

    return {
        "arithmetic": (
            "exact forced-factor extraction, complete square-divisor residue "
            "sets for every external source, and finite-field admissibility "
            "checks before and after the modulus-5 parameter split"
        ),
        "scope_note": (
            "Conditional statement only. Dickson's prime-tuples conjecture or "
            "Schinzel's Hypothesis H is required to obtain infinitely many "
            "actual primes. This is not a counterexample to Erdos--Straus."
        ),
        "h19": {
            "modulus": 77_597_520,
            "residue_class": H19_RESIDUE,
            "base_progression": "p=6*Q19*t+8328961",
        },
        "base_scales": list(BASE_SCALES),
        "extended_scales": list(EXTENDED_SCALES),
        "pre_extension": base,
        "extension_before_split": covered,
        "covering_root_map_mod_5": roots,
        "renewal": {
            "parameter_split": "t=5*u+c",
            "branches": renewal_branches,
        },
        "all_common_stationary_scales": {
            "scale_gcd": stationary_scale_gcd,
            "scales": list(stationary_scales),
            "branches": stationary_branches,
        },
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
