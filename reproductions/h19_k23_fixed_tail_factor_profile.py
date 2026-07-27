#!/usr/bin/env python3
"""Separate fixed p-1 factor tail descents from the H19-k23 residuals."""

from __future__ import annotations

import argparse
from collections import Counter
from functools import reduce
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SHARED = ROOT / "reproductions" / "h19-k23-shared-selector-audit-262144.json"
DEFAULT_CLOSURE = ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-262144.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "h19-k23-fixed-tail-factor-profile-262144.json"
BRANCHES = ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py"


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("h19_k23_fixed_tail_branches", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mixed_boundary = load_module(BRANCHES)


def common_p_minus_one_factor() -> tuple[int, dict[int, int]]:
    """Return gcd(A, C-1) across every p=A*t+C residual progression."""
    factors = {}
    values = []
    for branch in mixed_boundary.remaining_branches():
        form = branch["prime_form"]
        value = math.gcd(int(form["coefficient"]), int(form["constant"]) - 1)
        factors[int(branch["v_mod_29"])] = value
        values.append(value)
    return reduce(math.gcd, values), factors


def run_profile(shared: dict[str, object], closure: dict[str, object]) -> dict[str, object]:
    """Classify direct gaps by the fixed divisor common to all 14 branches."""
    fixed_factor, branch_factors = common_p_minus_one_factor()
    if shared["parameter_limit_exclusive"] != closure["input_parameter_limit_exclusive"]:
        raise ValueError("shared and closure artifacts have different parameter limits")
    closure_by_prime = {int(record["prime"]): record for record in closure["records"]}
    fixed_records = []
    residual_records = []
    for record in shared["records"]:
        prime = int(record["prime"])
        gap = int(record["first_witness"]["gap"])
        if prime not in closure_by_prime:
            raise AssertionError("closure artifact omitted a shared record")
        if fixed_factor % (gap + 1) == 0:
            if closure_by_prime[prime]["route"] != "shared-gap":
                raise AssertionError("fixed factor failed to give the direct tail route")
            fixed_records.append(record)
        else:
            residual_records.append(record)
    accidental = [
        record
        for record in residual_records
        if (int(record["prime"]) - 1) % (int(record["first_witness"]["gap"]) + 1) == 0
    ]
    alternative = [
        record
        for record in residual_records
        if closure_by_prime[int(record["prime"])]["route"] == "alternative-p-minus-one-gap"
    ]
    if len(accidental) + len(alternative) != len(residual_records):
        raise AssertionError("residual route classification is incomplete")
    m31_factor_square = [
        record
        for record in alternative
        if int(record["first_witness"]["gap"]) == 27
        and int(closure_by_prime[int(record["prime"])]["tail_witness"]["gap"]) == 31
        and 64 % int(closure_by_prime[int(record["prime"])]["tail_witness"]["divisor"]) == 0
    ]
    return {
        "arithmetic": (
            "exact affine gcd(A,C-1) calculation, divisibility checks for every "
            "stored shared Type II gap, and cross-check against the independently "
            "verified ordinary two-tail closure artifact"
        ),
        "scope_note": (
            "The fixed factor proves direct tail compatibility only for records with "
            "m+1 dividing it. The remaining finite residual still needs its separate "
            "p-1 factor scan and is not a global selector theorem."
        ),
        "parameter_limit_exclusive": shared["parameter_limit_exclusive"],
        "common_p_minus_one_factor": fixed_factor,
        "branch_p_minus_one_factors": {str(key): value for key, value in branch_factors.items()},
        "record_count": len(shared["records"]),
        "fixed_factor_direct_tail_count": len(fixed_records),
        "fixed_factor_gaps": sorted({int(record["first_witness"]["gap"]) for record in fixed_records}),
        "residual_count": len(residual_records),
        "residual_gap_histogram": {
            str(gap): count
            for gap, count in sorted(
                Counter(int(record["first_witness"]["gap"]) for record in residual_records).items()
            )
        },
        "residual_accidental_direct_count": len(accidental),
        "residual_accidental_direct_records": [
            {
                "prime": int(record["prime"]),
                "gap": int(record["first_witness"]["gap"]),
                "v_mod_29": int(record["v_mod_29"]),
                "parameter": int(record["parameter"]),
            }
            for record in accidental
        ],
        "residual_alternative_tail_count": len(alternative),
        "m27_to_m31_q8_factor_square_count": len(m31_factor_square),
        "m27_to_m31_q8_divisor_histogram": {
            str(divisor): count
            for divisor, count in sorted(
                Counter(
                    int(closure_by_prime[int(record["prime"])]["tail_witness"]["divisor"])
                    for record in m31_factor_square
                ).items()
            )
        },
        "remaining_new_factor_alternative_count": len(alternative) - len(m31_factor_square),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shared", type=Path, default=DEFAULT_SHARED)
    parser.add_argument("--closure", type=Path, default=DEFAULT_CLOSURE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    shared = json.loads(args.shared.read_text(encoding="utf-8"))
    closure = json.loads(args.closure.read_text(encoding="utf-8"))
    result = run_profile(shared, closure)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
