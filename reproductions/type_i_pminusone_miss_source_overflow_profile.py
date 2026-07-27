#!/usr/bin/env python3
"""Profile B=1 exponent overflow on shortest p-minus-one-residual sources.

The 185 points missed by the Type I p-minus-one bridge selector have stored
shortest upper-half source states.  For each such state, this audit tests the
exact B=1 divisor-residue realization.  On a B=1 miss it exhausts the square
divisors F|K^2 in the normalized source-state realization and measures the
least exponent excess of F over K.

This deliberately differs from the earlier support-minimized 500M profile:
it asks whether the dynamically necessary non-p-minus-one source states retain
the observed one-or-two-repeat behavior.
"""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-pminusone-miss-upper-half-profile-500m-results.json"
REALIZATION = ROOT / "reproductions" / "type_i_normal_source_state_realization.py"
OVERFLOW = ROOT / "reproductions" / "type_i_source_state_b1_overflow_profile.py"
PRODUCT = ROOT / "reproductions" / "type_i_source_state_b1_product_boundary.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-pminusone-miss-source-overflow-profile-500m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


realization = load_module("pminusone_source_overflow_realization", REALIZATION)
overflow = load_module("pminusone_source_overflow_square", OVERFLOW)
product = load_module("pminusone_source_overflow_product", PRODUCT)


def classify_record(record: dict[str, object]) -> dict[str, object]:
    """Rebuild one source state and minimize its B=1 exponent overflow."""
    prime = int(record["prime"])
    source = int(record["source_denominator"])
    bridge = int(record["E"])
    distance = prime - source
    if distance <= 1 or bridge % 2 or (bridge - 1) % distance:
        raise AssertionError("stored non-p-minus-one source state is invalid")
    R = (bridge - 1) // distance
    K = (prime * R + 1) // 4
    if R < 3 or R % 2 == 0 or 4 * K != prime * R + 1:
        raise AssertionError("source state did not reconstruct R and K")
    if (source * source // math.gcd(bridge, 4)) % bridge:
        raise AssertionError("stored source state failed the source-square condition")

    forms = realization.source_state_forms(prime, source, bridge)
    if not forms:
        raise AssertionError("stored source state has no Type I normal realization")
    stored_A, stored_B, stored_C = (int(value) for value in record["normal_form"])
    if not any(
        form["A"] == stored_A and form["B"] == stored_B and form["C"] == stored_C
        for form in forms
    ):
        raise AssertionError("stored shortest-source normal form was not recovered")

    factors = {int(q): int(exponent) for q, exponent in overflow.sympy.factorint(K).items()}
    target = -pow(4, -1, R) % R
    B_one_forms = [form for form in forms if form["B"] == 1]
    divisor_hit = any(divisor % R == target for divisor in overflow.divisors(factors))
    if bool(B_one_forms) != divisor_hit:
        raise AssertionError("B=1 realization and divisor-residue test disagreed")

    result: dict[str, object] = {
        "prime": prime,
        "source_denominator": source,
        "source_distance": distance,
        "E": bridge,
        "R": R,
        "K": K,
        "compatible_normal_form_count": len(forms),
        "least_realization_B": int(forms[0]["B"]),
        "B_eq_1_realization_exists": bool(B_one_forms),
    }
    if B_one_forms:
        result["B_eq_1_form_count"] = len(B_one_forms)
        return result

    subgroup = product.generated_subgroup(R, {factor % R for factor in factors})
    if target not in subgroup:
        raise AssertionError("B=1 miss unexpectedly has a subgroup obstruction")

    square_factors = {factor: 2 * exponent for factor, exponent in factors.items()}
    candidates: list[tuple[int, dict[str, int]]] = []
    for factor in overflow.divisors(square_factors):
        witness = overflow.square_divisor_witness(prime, source, bridge, K, factor)
        if witness is not None:
            candidates.append((overflow.overflow(factor, factors), witness))
    if not candidates:
        raise AssertionError("B=1 miss had no square-divisor normal realization")
    excess, witness = min(candidates, key=lambda item: (item[0], item[1]["B"], item[1]["F"]))
    result.update(
        {
            "B_eq_1_failure": "finite_product",
            "least_extra_exponent_count": excess,
            "least_overflow_witness": witness,
        }
    )
    return result


def run_profile(profile: dict[str, object]) -> dict[str, object]:
    """Classify every shortest source state on the 500M p-minus-one residual."""
    records = profile["records"]
    if not isinstance(records, list) or len(records) != 185:
        raise AssertionError("input must be the exact 185-point p-minus-one residual profile")
    rows = [classify_record(record) for record in records if isinstance(record, dict)]
    if len(rows) != len(records) or len({int(row["prime"]) for row in rows}) != len(rows):
        raise AssertionError("source-overflow profile did not preserve the residual prime set")

    B_one_hits = [row for row in rows if bool(row["B_eq_1_realization_exists"])]
    B_one_misses = [row for row in rows if not bool(row["B_eq_1_realization_exists"])]
    if any(row.get("B_eq_1_failure") != "finite_product" for row in B_one_misses):
        raise AssertionError("B=1 misses did not have the claimed finite-product classification")
    excess_histogram = Counter(int(row["least_extra_exponent_count"]) for row in B_one_misses)
    least_B_histogram = Counter(int(row["least_realization_B"]) for row in rows)
    maximum_excess_row = max(
        B_one_misses,
        key=lambda row: (
            int(row["least_extra_exponent_count"]),
            int(row["least_realization_B"]),
            int(row["prime"]),
        ),
    )
    maximum_B_row = max(rows, key=lambda row: (int(row["least_realization_B"]), int(row["prime"])))
    return {
        "arithmetic": (
            "for every shortest non-p-minus-one upper-half source state, rebuild R=(E-1)/(p-n) and "
            "K=(pR+1)/4; exhaust all source-state normal realizations; test the exact B=1 divisor "
            "residue; then on each miss enumerate F|K^2, reconstruct its normal form, and minimize "
            "the exponent excess of F over K"
        ),
        "scope_note": (
            "A complete finite profile only for the 185 p-minus-one misses within the stored p<=500M, "
            "m<=215 box and their shortest upper-half source states. It does not bound exponent overflow "
            "for arbitrary source states or prove the mixed terminal selector."
        ),
        "input_artifact": INPUT.name,
        "p_minus_one_residual_count": len(rows),
        "B_eq_1_realization_count": len(B_one_hits),
        "B_eq_1_miss_count": len(B_one_misses),
        "B_eq_1_subgroup_obstruction_count": 0,
        "B_eq_1_finite_product_obstruction_count": len(B_one_misses),
        "least_extra_exponent_histogram": {
            str(excess): count for excess, count in sorted(excess_histogram.items())
        },
        "maximum_extra_exponent_count": max(excess_histogram),
        "maximum_extra_exponent_record": maximum_excess_row,
        "least_realization_B_histogram": {
            str(B): count for B, count in sorted(least_B_histogram.items())
        },
        "maximum_least_B_record": maximum_B_row,
        "records": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
