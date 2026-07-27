#!/usr/bin/env python3
"""Remove the B cap on the residual linear-E H19 states through m=127."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "reproductions" / "type-i-h19-reverse-two-tail-linear-e-overflow-b20-1b-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_GAP_CAP = 127
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-reverse-two-tail-linear-e-full-b-boundary-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("h19_linear_e_full_b_landscape", LANDSCAPE)
bridge = load_module("h19_linear_e_full_b_bridge", BRIDGE)


def run_audit(profile: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    if int(profile["gap_cap"]) != gap_cap or int(profile["b_cap"]) < 20:
        raise ValueError("input must be the verified m<=127, B<=20 linear-E profile")
    residuals = [int(value) for value in profile["misses_by_b_cap"]["20"]]
    if len(residuals) != 42:
        raise AssertionError("B<=20 residual set did not reconstruct")
    records: list[dict[str, object]] = []
    total_forms = 0
    total_lifts = 0
    for prime in residuals:
        local_forms = 0
        local_lifts = 0
        linear_witness: dict[str, object] | None = None
        square_candidates: list[dict[str, object]] = []
        for gap in range(3, gap_cap + 1, 4):
            for entry in landscape.gap_landscape(prime, gap)["type_i"]:
                A, B, C = (int(value) for value in entry["normal_form"])
                local_forms += 1
                _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
                local_lifts += len(lifts)
                R = (4 * B * B * C + 1) // gap
                K = B * C * (A * R - B)
                for lift in lifts:
                    E = int(lift["bridge_divisor"]) // (prime * prime)
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
                        candidate["normal_form"][1],
                        candidate["gap"],
                        candidate["E"],
                        candidate["reverse_two_tail_lift"]["source_denominator"],
                    ) < (
                        linear_witness["normal_form"][1],
                        linear_witness["gap"],
                        linear_witness["E"],
                        linear_witness["reverse_two_tail_lift"]["source_denominator"],
                    ):
                        linear_witness = candidate
        total_forms += local_forms
        total_lifts += local_lifts
        if not square_candidates:
            raise AssertionError("unbounded-B residual had no strict reverse lift")
        least_square_surplus = min(
            square_candidates,
            key=lambda item: (
                item["extra_exponent_count"],
                item["extra_prime_support_count"],
                item["square_surplus"],
                item["normal_form"][1],
                item["gap"],
                item["reverse_two_tail_lift"]["source_denominator"],
            ),
        )
        records.append(
            {
                "prime": prime,
                "unbounded_b_normal_form_count": local_forms,
                "strict_reverse_lift_count": local_lifts,
                "linear_e_witness": linear_witness,
                "least_square_surplus": least_square_surplus,
            }
        )
    misses = [record["prime"] for record in records if record["linear_e_witness"] is None]
    exponent_histogram: dict[str, int] = {}
    support_histogram: dict[str, int] = {}
    for record in records:
        surplus = record["least_square_surplus"]
        exponent = str(surplus["extra_exponent_count"])
        support = str(surplus["extra_prime_support_count"])
        exponent_histogram[exponent] = exponent_histogram.get(exponent, 0) + 1
        support_histogram[support] = support_histogram.get(support, 0) + 1
    return {
        "arithmetic": (
            "take the exact B<=20 linear-E residuals; for each, enumerate every "
            "Type I normal certificate with m=3 (mod 4) through gap_cap without a B cap, "
            "then enumerate every strict maximum-tail reverse lift and test E|4K"
        ),
        "scope_note": (
            "Composition of the verified B<=20 capture profile with an unbounded-B audit "
            "of its residuals. It is exhaustive only through the stated gap cap."
        ),
        "input_linear_e_profile": "type-i-h19-reverse-two-tail-linear-e-overflow-b20-1b-results.json",
        "prime_limit": profile["prime_limit"],
        "base_shift_bound": profile["base_shift_bound"],
        "h19_residual_count": profile["h19_residual_count"],
        "gap_cap": gap_cap,
        "b_capped_linear_e_captured_count": profile["cumulative_linear_e_captured_by_b_cap"]["20"],
        "unbounded_b_audited_count": len(records),
        "unbounded_b_normal_form_count": total_forms,
        "strict_reverse_lift_count": total_lifts,
        "unbounded_b_linear_e_captured_count": len(records) - len(misses),
        "unbounded_b_linear_e_misses": misses,
        "full_box_linear_e_captured_count": int(profile["h19_residual_count"]) - len(misses),
        "least_square_surplus_exponent_histogram": dict(
            sorted(exponent_histogram.items(), key=lambda item: int(item[0]))
        ),
        "least_square_surplus_support_histogram": dict(
            sorted(support_histogram.items(), key=lambda item: int(item[0]))
        ),
        "multi_prime_square_surplus_primes": [
            record["prime"]
            for record in records
            if record["least_square_surplus"]["extra_prime_support_count"] > 1
        ],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=PROFILE)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.profile.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
