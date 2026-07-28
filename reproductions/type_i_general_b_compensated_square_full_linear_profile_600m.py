#!/usr/bin/env python3
"""Exhaust compensated squares over every linear-source-induced R on 13 residuals."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-general-b-compensated-square-residual-profile-600m-results.json"
LINEAR_SCRIPT = ROOT / "reproductions" / "type_i_linear_source_general_b_completion_profile_600m.py"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
COMPENSATED_SCRIPT = ROOT / "reproductions" / "type_i_general_b_compensated_square_residual_profile_600m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-general-b-compensated-square-full-linear-profile-600m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


linear = load_module("full_linear_compensated_linear", LINEAR_SCRIPT)
sources = load_module("full_linear_compensated_sources", SOURCE_SCRIPT)
compensated = load_module("full_linear_compensated_bridge", COMPENSATED_SCRIPT)


def normal_form_from_target_divisor(prime: int, R: int, K: int, divisor: int) -> dict[str, int]:
    """Normalize one d|K^2, 4d=-1 (mod R), retaining the canonical H>B orientation."""
    common = math.gcd(divisor, K)
    initial_B = divisor // common
    if common * common % divisor:
        raise AssertionError("target divisor did not normalize to integral C")
    C = common * common // divisor
    initial_H = K // common
    if (
        initial_B * C * initial_H != K
        or initial_B * initial_B * C != divisor
        or math.gcd(initial_B, initial_H) != 1
        or initial_B == initial_H
    ):
        raise AssertionError("target divisor normalization failed")
    B, H = (initial_H, initial_B) if initial_H < initial_B else (initial_B, initial_H)
    A, A_remainder = divmod(B + H, R)
    gap, gap_remainder = divmod(4 * B * B * C + 1, R)
    if (
        A_remainder
        or gap_remainder
        or A <= 0
        or H <= B
        or math.gcd(A, B) != 1
        or not (3 <= gap <= prime - 2 and gap % 4 == 3)
        or prime != 4 * A * B * C - gap
        or 4 * B * C * H != prime * R + 1
    ):
        raise AssertionError("normalized target divisor did not yield a natural Type I form")
    return {"A": A, "B": B, "C": C, "H": H, "m": gap, "R": R, "K": K}


def target_forms_for_R(prime: int, R: int) -> tuple[list[dict[str, int]], int, int]:
    """Exhaust all target-normal forms at one linear-source-induced R."""
    K, remainder = divmod(prime * R + 1, 4)
    if remainder or R < 3 or R % 4 != 3:
        raise AssertionError("invalid linear-source R")
    factors = linear.exact_factorization(K)
    square_divisors = linear.divisors_from_factorization(factors, 2)
    forms: dict[tuple[int, int, int, int], dict[str, int]] = {}
    target_hits = 0
    for divisor in square_divisors:
        if (4 * divisor + 1) % R:
            continue
        target_hits += 1
        form = normal_form_from_target_divisor(prime, R, K, divisor)
        forms[(form["A"], form["B"], form["C"], form["m"])] = form
    return [forms[key] for key in sorted(forms)], len(square_divisors), target_hits


def candidates_for_form(prime: int, form: dict[str, int]) -> tuple[list[dict[str, int | bool]], int]:
    """Exhaust the H-square divisor menu of one normalized target form."""
    factors = linear.exact_factorization(int(form["H"]))
    values: list[dict[str, int | bool]] = []
    divisors_checked = 0
    for T in linear.divisors_from_factorization(factors, 2):
        divisors_checked += 1
        witness = compensated.compensated_witness(
            prime,
            int(form["A"]),
            int(form["B"]),
            int(form["C"]),
            int(form["m"]),
            int(form["R"]),
            int(T),
        )
        if witness is not None:
            values.append(witness)
    return values, divisors_checked


def choose_candidate(values: list[dict[str, int | bool]]) -> dict[str, int | bool]:
    """Use a stable order only after the stated finite menu is complete."""
    if not values:
        raise ValueError("cannot choose an empty candidate set")
    return min(
        values,
        key=lambda witness: (
            int(witness["m"]),
            int(witness["source_denominator"]),
            int(witness["T"]),
            int(witness["B"]),
            int(witness["C"]),
            int(witness["R"]),
        ),
    )


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Decide the compensated-square branch on every R induced by a linear source."""
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    residual = [int(prime) for prime in payload["misses"]]
    if len(residual) != 13 or len(set(residual)) != len(residual):
        raise AssertionError("input is not the exact 13-point general-B residual")
    records: list[dict[str, object]] = []
    misses: list[int] = []
    totals: Counter[str] = Counter()
    coordinate_bounds: list[int] = []
    for prime in residual:
        bound, states_by_R = sources.enumerate_linear_source_states(prime)
        coordinate_bounds.append(bound)
        values: list[dict[str, int | bool]] = []
        local = Counter()
        for R, states in states_by_R.items():
            local["R_count"] += 1
            local["directed_source_state_count"] += len(states)
            forms, square_divisor_count, target_hit_count = target_forms_for_R(prime, R)
            local["K_square_divisors_checked"] += square_divisor_count
            local["target_divisor_hits"] += target_hit_count
            local["target_normal_forms_checked"] += len(forms)
            for form in forms:
                local_values, H_divisor_count = candidates_for_form(prime, form)
                local["H_square_divisors_checked"] += H_divisor_count
                values.extend(local_values)
        local["compensated_square_candidate_count"] = len(values)
        totals.update(local)
        if not values:
            misses.append(prime)
            continue
        selected = choose_candidate(values)
        records.append(
            {
                "prime": prime,
                "linear_source_coordinate_bound": bound,
                "linear_R_count": local["R_count"],
                "target_normal_form_count": local["target_normal_forms_checked"],
                "compensated_square_candidate_count": len(values),
                "selected_witness": selected,
            }
        )
    if len(records) + len(misses) != len(residual):
        raise AssertionError("full linear-R compensated-square audit did not partition its input")
    return {
        "arithmetic": (
            "for every directed linear source state p=a+s+asR through the exact min(a,s) bound, deduplicate "
            "the induced R; at each R enumerate all d|K^2 with 4d=-1 (mod R), normalize every Type I form, "
            "and enumerate every H^2 divisor T for E=4B^2C^2T"
        ),
        "scope_note": (
            "This is complete for the compensated-square mechanism over all R induced by the enumerated linear "
            "E|n source states of the stated 13 primes. It does not exclude non-linear sources, other Type I "
            "factor mechanisms, or Type II certificates."
        ),
        "input": input_path.name,
        "input_residual_count": len(residual),
        "full_linear_R_compensated_square_covered_count": len(records),
        "full_linear_R_compensated_square_miss_count": len(misses),
        "linear_source_coordinate_bound_max": max(coordinate_bounds),
        "linear_R_exhaustively_checked": totals["R_count"],
        "directed_linear_source_state_count": totals["directed_source_state_count"],
        "K_square_divisors_exhaustively_checked": totals["K_square_divisors_checked"],
        "target_divisor_hits": totals["target_divisor_hits"],
        "target_normal_forms_exhaustively_checked": totals["target_normal_forms_checked"],
        "H_square_divisors_exhaustively_checked": totals["H_square_divisors_checked"],
        "compensated_square_candidate_count": totals["compensated_square_candidate_count"],
        "upper_half_covered_count": sum(bool(row["selected_witness"]["upper_half"]) for row in records),
        "misses": misses,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key not in {"misses", "records"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
