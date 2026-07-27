#!/usr/bin/env python3
"""Release same-state large-side residuals through alternative Type I normal forms.

The companion small-side profile isolates records whose selected normal form has
no small-side pair at its own (L,R).  This script exhausts every Type I normal
form and strict even-source reverse lift through the already verified m<=215
box for precisely those records, then selects the least small-side bridge.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-small-side-profile-500m-results.json"
LANDSCAPE = ROOT / "reproductions" / "boundary_gap_certificate_landscape.py"
BRIDGE = ROOT / "reproductions" / "boundary_gap_27_reverse_two_tail_bridge.py"
DEFAULT_GAP_CAP = 215
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-tail-reverse-even-source-small-side-alternative-profile-500m-results.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


landscape = load_module("small_side_alternative_landscape", LANDSCAPE)
bridge = load_module("small_side_alternative_bridge", BRIDGE)


def least_small_side_edge(prime: int, gap_cap: int) -> tuple[dict[str, object] | None, int, int]:
    """Exhaust the stated normal-form box and retain its least small-side bridge."""
    best: dict[str, object] | None = None
    forms = 0
    lifts_checked = 0
    for gap in range(3, gap_cap + 1, 4):
        for entry in landscape.gap_landscape(prime, gap)["type_i"]:
            A, B, C = (int(value) for value in entry["normal_form"])
            forms += 1
            R = (4 * B * B * C + 1) // gap
            H = A * R - B
            K = B * C * H
            L = 2 * K
            certificate = bridge.short_certificate.type_i_normal_form_certificate(prime, gap, A, B)
            if certificate is None:
                raise AssertionError("stored Type I normal form did not reconstruct")
            _, lifts = bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
            for lift in lifts:
                lifts_checked += 1
                source = int(lift["source_denominator"])
                if source % 2:
                    continue
                bridge_divisor = int(lift["bridge_divisor"])
                if bridge_divisor % (prime * prime):
                    raise AssertionError("bridge divisor did not reconstruct E")
                E = bridge_divisor // (prime * prime)
                divisor_gcd = math.gcd(E, L)
                a, b = E // divisor_gcd, L // divisor_gcd
                if a >= b:
                    continue
                if (
                    math.gcd(a, b) != 1
                    or L % a
                    or L % b
                    or (a - 2 * b) % R
                    or E != L * a // b
                    or E % 2
                    or E > 2 * L - 2 * R
                ):
                    raise AssertionError("small-side pair failed the exact bridge conditions")
                target_solution = (certificate.x, certificate.y, certificate.z)
                source_solution = (int(lift["source_term"]), certificate.x, certificate.y)
                if Fraction(4, prime) != sum(
                    (Fraction(1, denominator) for denominator in target_solution), Fraction()
                ):
                    raise AssertionError("small-side target identity failed")
                if Fraction(4, source) != sum(
                    (Fraction(1, denominator) for denominator in source_solution), Fraction()
                ):
                    raise AssertionError("small-side source identity failed")
                candidate = {
                    "gap": gap,
                    "normal_form": [A, B, C],
                    "R": R,
                    "K": K,
                    "E": E,
                    "a": a,
                    "b": b,
                    "source_denominator": source,
                }
                key = (
                    E,
                    gap,
                    B,
                    source,
                    a,
                    b,
                    A,
                    C,
                )
                if best is None or key < (
                    int(best["E"]),
                    int(best["gap"]),
                    int(best["normal_form"][1]),
                    int(best["source_denominator"]),
                    int(best["a"]),
                    int(best["b"]),
                    int(best["normal_form"][0]),
                    int(best["normal_form"][2]),
                ):
                    best = candidate
    return best, forms, lifts_checked


def run_profile(same_state_profile: dict[str, object], gap_cap: int = DEFAULT_GAP_CAP) -> dict[str, object]:
    """Release every same-state large-side residual in the stated finite normal-form box."""
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least 3 and congruent to 3 modulo 4")
    residual_records = [
        record
        for record in same_state_profile["large_side_records"]
        if record["canonical_small_side_pair"] is None
    ]
    records: list[dict[str, object]] = []
    misses: list[int] = []
    forms = 0
    lifts = 0
    for residual in residual_records:
        prime = int(residual["prime"])
        witness, local_forms, local_lifts = least_small_side_edge(prime, gap_cap)
        forms += local_forms
        lifts += local_lifts
        if witness is None:
            misses.append(prime)
        else:
            records.append(
                {
                    "prime": prime,
                    "same_state_large_side": {
                        "R": int(residual["R"]),
                        "L": int(residual["L"]),
                        "selected_pair": residual["selected_pair"],
                    },
                    "alternative_small_side": witness,
                }
            )
    if int(same_state_profile["small_side_available_count"]) + len(records) != int(
        same_state_profile["record_count"]
    ):
        raise AssertionError("alternative profile did not partition the stored terminal closure")
    return {
        "arithmetic": (
            "for every same-(L,R) large-side residual, enumerate all Type I normal forms and strict "
            "even-source reverse lifts through m<=gap_cap, retain a<b ordinary divisor pairs, and "
            "verify both target and source Egyptian-fraction identities exactly"
        ),
        "scope_note": (
            "A finite re-selection result on the stored 500M ordinary-tail residual. It does not "
            "select a normal form beyond the stated gap box or prove a global mixed selector."
        ),
        "input_artifact": INPUT.name,
        "prime_limit": int(same_state_profile["prime_limit"]),
        "gap_cap": gap_cap,
        "same_state_large_side_residual_count": len(residual_records),
        "alternative_small_side_captured_count": len(records),
        "misses": misses,
        "normal_forms_exhaustively_checked": forms,
        "strict_reverse_lifts_exhaustively_checked": lifts,
        "combined_small_side_closure_count": int(same_state_profile["small_side_available_count"]) + len(records),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(json.loads(args.input.read_text(encoding="utf-8")), args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
