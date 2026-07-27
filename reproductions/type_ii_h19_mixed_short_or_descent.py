#!/usr/bin/env python3
"""Verify the H19 radius-six AC or mixed-factor-descent closure."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AC = ROOT / "reproductions" / "type-ii-h19-residual-ac-profile-1b-results.json"
DEFAULT_DESCENT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-mixed-short-or-descent-1b-results.json"


def verify_direct_ac(prime: int, witness: dict[str, int]) -> None:
    """Check the stored direct Type II AC certificate exactly."""
    a = int(witness["a"])
    c = int(witness["c"])
    k = int(witness["k"])
    h = int(witness["h"])
    gap = int(witness["gap"])
    x = int(witness["x"])
    y = int(witness["y"])
    z = int(witness["z"])
    if h != 4 * a * c * k - 1 or prime + 4 * a * a * c != h * gap:
        raise AssertionError("AC factor pair did not reconstruct")
    if Fraction(4, prime) != sum((Fraction(1, value) for value in (x, y, z)), Fraction()):
        raise AssertionError("direct AC certificate did not verify")


def verify_descent(prime: int, witness: dict[str, object]) -> None:
    """Check the stored mixed-factor source and target identities exactly."""
    source = int(witness["source_denominator"])
    source_solution = tuple(int(value) for value in witness["source_solution"])
    target_solution = tuple(int(value) for value in witness["target_solution"])
    if not 2 <= source < prime:
        raise AssertionError("mixed-factor source is not strictly smaller")
    if Fraction(4, source) != sum((Fraction(1, value) for value in source_solution), Fraction()):
        raise AssertionError("mixed-factor source solution did not verify")
    if Fraction(4, prime) != sum((Fraction(1, value) for value in target_solution), Fraction()):
        raise AssertionError("mixed-factor target lift did not verify")


def summarize_ac(witness: dict[str, int]) -> dict[str, int]:
    return {key: int(witness[key]) for key in ("radius", "a", "c", "k", "h", "gap", "divisor")}


def summarize_descent(witness: dict[str, object]) -> dict[str, int]:
    return {
        "source_denominator": int(witness["source_denominator"]),
        "k": int(witness["k"]),
        "q": int(witness["q"]),
        "factor": int(witness["factor"]),
        "gap": int(witness["certificate"]["gap"]),
    }


def run_audit(ac_payload: dict[str, object], descent_payload: dict[str, object]) -> dict[str, object]:
    """Verify that each residual has a radius-six direct certificate or a mixed descent."""
    ac_records = {int(record["prime"]): record for record in ac_payload["records"]}
    descent_records = {int(record["prime"]): record for record in descent_payload["records"]}
    if set(ac_records) != set(descent_records):
        raise AssertionError("AC and descent profiles do not describe the same residual set")

    both = []
    short_only = []
    descent_only = []
    unclosed = []
    for prime in sorted(ac_records):
        ac_witness = ac_records[prime]["direct_ac_witness"]
        if ac_witness is None:
            raise AssertionError("stored H19 AC profile unexpectedly lacks a certificate")
        verify_direct_ac(prime, ac_witness)
        short = int(ac_witness["radius"]) <= 6

        descent_witness = descent_records[prime]["mixed_factor_external_source_descent"]
        descent = descent_witness is not None
        if descent:
            verify_descent(prime, descent_witness)

        if short and descent:
            both.append(prime)
        elif short:
            short_only.append({"prime": prime, "direct_ac_witness": summarize_ac(ac_witness)})
        elif descent:
            descent_only.append(
                {"prime": prime, "mixed_factor_descent": summarize_descent(descent_witness)}
            )
        else:
            unclosed.append(prime)

    return {
        "arithmetic": (
            "exact rational verification of stored direct Type II certificates and "
            "of every stored mixed-factor strict source-to-target lift"
        ),
        "scope_note": (
            "A finite H19 profile closure. It does not establish a universal "
            "radius-six bound or a universal mixed-factor selector."
        ),
        "prime_limit": ac_payload["prime_limit"],
        "base_shift_bound": ac_payload["base_shift_bound"],
        "h19_residual_count": len(ac_records),
        "ac_radius_bound": 6,
        "direct_ac_short_count": len(both) + len(short_only),
        "mixed_factor_descent_count": len(both) + len(descent_only),
        "both_count": len(both),
        "direct_ac_only_count": len(short_only),
        "mixed_factor_only_count": len(descent_only),
        "unclosed_primes": unclosed,
        "direct_ac_only_records": short_only,
        "mixed_factor_only_records": descent_only,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ac-profile", type=Path, default=DEFAULT_AC)
    parser.add_argument("--descent-profile", type=Path, default=DEFAULT_DESCENT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.ac_profile.read_text(encoding="utf-8")),
        json.loads(args.descent_profile.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
