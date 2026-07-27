#!/usr/bin/env python3
"""Close H19 Type II residuals with a bounded Type I source selector.

For the residual records of the verified H19 canonical Type II audit, search
the complete Type I normal-form box with a stated B and gap cap, retaining
only certificates whose canonical p-tail deflates to a strict source. This
is a finite hybrid audit; its Type I branch is a restricted slice of the
existing complete quadratic external-source descent family.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JOINT_PROFILE = ROOT / "reproductions" / "type_i_small_b_tail_deflation_profile.py"
H19_INPUT = ROOT / "reproductions" / "type-ii-h19-quadratic-descent-closure-20m-results.json"
RESULTS = ROOT / "reproductions" / "type-i-h19-small-b-tail-hybrid-20m-results.json"
DEFAULT_SMALL_GAP_CAP = 239
DEFAULT_EXTENDED_GAP_CAP = 999
DEFAULT_B_CAP = 4


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


joint = load_module("type_i_h19_small_b_tail_joint", JOINT_PROFILE)


def run_profile(
    input_path: Path = H19_INPUT,
    small_gap_cap: int = DEFAULT_SMALL_GAP_CAP,
    extended_gap_cap: int = DEFAULT_EXTENDED_GAP_CAP,
    b_cap: int = DEFAULT_B_CAP,
) -> dict[str, object]:
    """Run a bounded Type I strict-descent selector on every H19 residual."""
    for cap in (small_gap_cap, extended_gap_cap):
        if cap < 3 or cap % 4 != 3:
            raise ValueError("gap caps must be at least 3 and congruent to 3 modulo 4")
    if extended_gap_cap < small_gap_cap or b_cap < 1:
        raise ValueError("caps must be ordered and b_cap must be positive")
    source = json.loads(input_path.read_text(encoding="utf-8"))
    residuals = [record["prime"] for record in source["records"]]
    if len(residuals) != source["canonical_residual_count"]:
        raise AssertionError("H19 residual record count did not reconstruct")
    spf = joint.short_certificate.smallest_prime_factors(
        (max(residuals) + extended_gap_cap) // 4 + 1
    )
    records: list[dict[str, object]] = []
    for prime in residuals:
        small = joint.first_joint_witness(prime, spf, small_gap_cap, b_cap)
        extended = small or joint.first_joint_witness(
            prime, spf, extended_gap_cap, b_cap
        )
        records.append(
            {
                "prime": prime,
                "small_box_witness": small,
                "extended_box_witness": extended,
            }
        )
    small_recovered = sum(record["small_box_witness"] is not None for record in records)
    extended_misses = [
        record["prime"] for record in records if record["extended_box_witness"] is None
    ]
    extended_only = [
        record for record in records if record["small_box_witness"] is None
    ]
    return {
        "arithmetic": (
            "start with the exact H19 canonical Type II residual records; "
            "for each, exhaustively enumerate A at every B through the cap "
            "and every m=3 (mod 4) through each gap cap, retaining only a "
            "verified Type I certificate with an exact strict source tail"
        ),
        "scope_note": (
            "Finite hybrid closure. The Type I source branch is not a new "
            "descent family; it is a bounded certificate-side slice of the "
            "complete quadratic external-source family."
        ),
        "input_h19_artifact": input_path.name,
        "prime_limit": source["prime_limit"],
        "core_prime_count": source["core_prime_count"],
        "h19_canonical_captured_count": source["canonical_captured_count"],
        "h19_residual_count": len(residuals),
        "small_gap_cap": small_gap_cap,
        "extended_gap_cap": extended_gap_cap,
        "b_cap": b_cap,
        "small_box_recovered_count": small_recovered,
        "extended_box_recovered_count": len(residuals) - len(extended_misses),
        "extended_box_misses": extended_misses,
        "maximum_first_extended_gap": max(
            (
                record["extended_box_witness"]["gap"]
                for record in records
                if record["extended_box_witness"] is not None
            ),
            default=None,
        ),
        "extended_only_records": extended_only,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=H19_INPUT)
    parser.add_argument("--small-gap-cap", type=int, default=DEFAULT_SMALL_GAP_CAP)
    parser.add_argument("--extended-gap-cap", type=int, default=DEFAULT_EXTENDED_GAP_CAP)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_profile(
        args.input, args.small_gap_cap, args.extended_gap_cap, args.b_cap
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
