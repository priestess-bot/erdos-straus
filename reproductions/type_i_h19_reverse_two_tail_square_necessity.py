#!/usr/bin/env python3
"""Test whether H19 B=1 reverse lifts can restrict E to a linear K divisor."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
H19 = ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_GAP_CAP = 127
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-reverse-two-tail-square-necessity-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("h19_reverse_square_landscape", LANDSCAPE)
bridge = load_module("h19_reverse_square_bridge", BRIDGE)


def run_audit(h19: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    residuals = [int(profile["prime"]) for profile in h19["profiles"]]
    if len(residuals) != int(h19["source_free_count"]):
        raise AssertionError("H19 residual count did not reconstruct")
    records: list[dict[str, object]] = []
    form_count = 0
    lift_count = 0
    for prime in residuals:
        local_forms = 0
        local_lifts = 0
        linear_witness: dict[str, object] | None = None
        square_candidates: list[dict[str, object]] = []
        for gap in range(3, gap_cap + 1, 4):
            for entry in landscape.gap_landscape(prime, gap)["type_i"]:
                A, B, C = (int(value) for value in entry["normal_form"])
                if B != 1:
                    continue
                local_forms += 1
                _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
                local_lifts += len(lifts)
                R = (4 * C + 1) // gap
                K = C * (A * R - 1)
                for lift in lifts:
                    E = int(lift["bridge_divisor"]) // (prime * prime)
                    if int(lift["bridge_divisor"]) != prime * prime * E:
                        raise AssertionError("bridge divisor did not normalize to p^2 E")
                    if (4 * K) % E:
                        surplus = E // math.gcd(E, 4 * K)
                        if surplus == 1:
                            raise AssertionError("nonlinear E did not have square surplus")
                        factors = landscape.factor_by_trial_division(surplus)
                        square_candidates.append(
                            {
                                "gap": gap,
                                "normal_form": [A, B, C],
                                "K": K,
                                "E": E,
                                "square_surplus": surplus,
                                "square_surplus_factorization": {
                                    str(q): exponent for q, exponent in factors.items()
                                },
                                "extra_exponent_count": sum(factors.values()),
                                "extra_prime_support_count": len(factors),
                                "reverse_two_tail_lift": lift,
                            }
                        )
                        continue
                    candidate = {
                        "gap": gap,
                        "normal_form": [A, B, C],
                        "K": K,
                        "E": E,
                        "reverse_two_tail_lift": lift,
                    }
                    if linear_witness is None or (
                        candidate["gap"], candidate["E"], candidate["reverse_two_tail_lift"]["source_denominator"]
                    ) < (
                        linear_witness["gap"], linear_witness["E"], linear_witness["reverse_two_tail_lift"]["source_denominator"]
                    ):
                        linear_witness = candidate
        form_count += local_forms
        lift_count += local_lifts
        least_square_surplus = None
        if linear_witness is None:
            if not square_candidates:
                raise AssertionError("a non-linear miss had no strict reverse lift")
            least_square_surplus = min(
                square_candidates,
                key=lambda item: (
                    item["extra_exponent_count"],
                    item["extra_prime_support_count"],
                    item["square_surplus"],
                    item["gap"],
                    item["reverse_two_tail_lift"]["source_denominator"],
                ),
            )
        records.append(
            {
                "prime": prime,
                "b_one_normal_form_count": local_forms,
                "strict_reverse_lift_count": local_lifts,
                "linear_e_witness": linear_witness,
                "least_square_surplus": least_square_surplus,
            }
        )
    misses = [record["prime"] for record in records if record["linear_e_witness"] is None]
    if any(record["strict_reverse_lift_count"] == 0 for record in records):
        raise AssertionError("the stated B=1 reverse closure was not reconstructed")
    surplus_records = [record["least_square_surplus"] for record in records if record["least_square_surplus"]]
    exponent_histogram: dict[str, int] = {}
    support_histogram: dict[str, int] = {}
    for record in surplus_records:
        exponent = str(record["extra_exponent_count"])
        support = str(record["extra_prime_support_count"])
        exponent_histogram[exponent] = exponent_histogram.get(exponent, 0) + 1
        support_histogram[support] = support_histogram.get(support, 0) + 1
    return {
        "arithmetic": (
            "for every stored H19 source-free residual, enumerate every B=1 Type I "
            "normal certificate with m=3 (mod 4) through gap_cap and every strict "
            "maximum-tail reverse lift; test whether its normalized bridge factor E divides 4K"
        ),
        "scope_note": (
            "Finite necessity audit for the stated H19 B=1 box. A miss excludes only "
            "strict reverse lifts in this box with E|4K, not other gaps, overflow, or descent families."
        ),
        "input_h19_artifact": "type-ii-source-free-transition-h19-1b-results.json",
        "prime_limit": h19["prime_limit"],
        "base_shift_bound": h19["base_shift_bound"],
        "h19_residual_count": len(residuals),
        "gap_cap": gap_cap,
        "b_cap": 1,
        "b_one_normal_form_count": form_count,
        "strict_reverse_lift_count": lift_count,
        "linear_e_captured_count": len(records) - len(misses),
        "linear_e_misses": misses,
        "least_square_surplus_exponent_histogram": dict(
            sorted(exponent_histogram.items(), key=lambda item: int(item[0]))
        ),
        "least_square_surplus_support_histogram": dict(
            sorted(support_histogram.items(), key=lambda item: int(item[0]))
        ),
        "maximum_least_square_surplus_exponent_count": max(
            (record["extra_exponent_count"] for record in surplus_records), default=None
        ),
        "maximum_least_square_surplus_support_count": max(
            (record["extra_prime_support_count"] for record in surplus_records), default=None
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h19", type=Path, default=H19)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.h19.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
