#!/usr/bin/env python3
"""Profile whether low Type I overflow can linearize H19 reverse-tail factors."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
H19 = ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_GAP_CAP = 127
DEFAULT_B_CAP = 20
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-reverse-two-tail-linear-e-overflow-b20-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("h19_linear_e_overflow_landscape", LANDSCAPE)
bridge = load_module("h19_linear_e_overflow_bridge", BRIDGE)


def run_profile(
    h19: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP, b_cap: int = DEFAULT_B_CAP
) -> dict[str, object]:
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    if b_cap < 1:
        raise ValueError("b_cap must be positive")
    residuals = [int(profile["prime"]) for profile in h19["profiles"]]
    if len(residuals) != int(h19["source_free_count"]):
        raise AssertionError("H19 residual count did not reconstruct")
    records: list[dict[str, object]] = []
    form_count = 0
    lift_count = 0
    for prime in residuals:
        minimum_witness: dict[str, object] | None = None
        for gap in range(3, gap_cap + 1, 4):
            for entry in landscape.gap_landscape(prime, gap)["type_i"]:
                A, B, C = (int(value) for value in entry["normal_form"])
                if B > b_cap:
                    continue
                form_count += 1
                _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
                lift_count += len(lifts)
                R = (4 * B * B * C + 1) // gap
                K = B * C * (A * R - B)
                for lift in lifts:
                    E = int(lift["bridge_divisor"]) // (prime * prime)
                    if (4 * K) % E:
                        continue
                    candidate = {
                        "gap": gap,
                        "normal_form": [A, B, C],
                        "K": K,
                        "E": E,
                        "reverse_two_tail_lift": lift,
                    }
                    if minimum_witness is None or (
                        B,
                        candidate["gap"],
                        candidate["E"],
                        candidate["reverse_two_tail_lift"]["source_denominator"],
                    ) < (
                        minimum_witness["normal_form"][1],
                        minimum_witness["gap"],
                        minimum_witness["E"],
                        minimum_witness["reverse_two_tail_lift"]["source_denominator"],
                    ):
                        minimum_witness = candidate
        records.append(
            {
                "prime": prime,
                "minimum_linear_e_b": None
                if minimum_witness is None
                else minimum_witness["normal_form"][1],
                "linear_e_witness": minimum_witness,
            }
        )
    cumulative_captured: dict[str, int] = {}
    misses_by_b_cap: dict[str, list[int]] = {}
    first_b_counts: dict[str, int] = {}
    for b in range(1, b_cap + 1):
        captured = [record for record in records if record["minimum_linear_e_b"] is not None and record["minimum_linear_e_b"] <= b]
        cumulative_captured[str(b)] = len(captured)
        misses_by_b_cap[str(b)] = [record["prime"] for record in records if record not in captured]
    for record in records:
        if record["minimum_linear_e_b"] is not None:
            b = str(record["minimum_linear_e_b"])
            first_b_counts[b] = first_b_counts.get(b, 0) + 1
    return {
        "arithmetic": (
            "for every stored H19 source-free residual, enumerate each Type I normal "
            "certificate with m=3 (mod 4) through gap_cap and B<=b_cap; enumerate every "
            "strict maximum-tail reverse lift and retain those whose normalized E divides 4K"
        ),
        "scope_note": (
            "Finite overflow-versus-square-tail profile. It does not exclude larger "
            "overflow, larger gaps, or a source-side rule outside the stated H19 box."
        ),
        "input_h19_artifact": "type-ii-source-free-transition-h19-1b-results.json",
        "prime_limit": h19["prime_limit"],
        "base_shift_bound": h19["base_shift_bound"],
        "h19_residual_count": len(residuals),
        "gap_cap": gap_cap,
        "b_cap": b_cap,
        "normal_form_count": form_count,
        "strict_reverse_lift_count": lift_count,
        "cumulative_linear_e_captured_by_b_cap": cumulative_captured,
        "first_linear_e_b_counts": dict(sorted(first_b_counts.items(), key=lambda item: int(item[0]))),
        "misses_by_b_cap": misses_by_b_cap,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h19", type=Path, default=H19)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(
        json.loads(args.h19.read_text(encoding="utf-8")), args.gap_cap, args.b_cap
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
