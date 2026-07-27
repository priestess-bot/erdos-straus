#!/usr/bin/env python3
"""Reconstruct normal Type I bridges from source-state divisor pairs on the 28-point boundary."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PROFILE = ROOT / "reproductions" / "type-i-h19-p25-residue-boundary-source-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-normal-source-state-realization-1b-results.json"


def divisors(factors: dict[int, int]) -> list[int]:
    result = [1]
    for factor, exponent in factors.items():
        result = [value * factor**power for value in result for power in range(exponent + 1)]
    return sorted(result)


def source_state_forms(prime: int, source: int, bridge: int) -> list[dict[str, int]]:
    """Enumerate exactly the (A,B,C,m) normal forms compatible with (p,n,E)."""
    offset = prime - source
    if source <= 0 or offset <= 0 or (bridge - 1) % offset:
        raise AssertionError("invalid source-state parameters")
    R = (bridge - 1) // offset
    if (prime * R + 1) % 4 or (source * source // math.gcd(bridge, 4)) % bridge:
        raise AssertionError("source state failed the bridge integrality conditions")
    K = (prime * R + 1) // 4
    factors = {int(factor): int(exponent) for factor, exponent in sympy.factorint(K).items()}
    all_divisors = divisors(factors)
    forms = []
    for B in all_divisors:
        for C in all_divisors:
            BC = B * C
            if K % BC:
                continue
            H = K // BC
            if (4 * B * B * C + 1) % R:
                continue
            # 4K=1 (mod R) makes the complementary-factor residue automatic.
            if (H + B) % R:
                raise AssertionError("complementary-factor residue did not follow from the first condition")
            A = (H + B) // R
            m = (4 * B * B * C + 1) // R
            if A <= 0 or m <= 0 or math.gcd(A, B) != 1:
                continue
            x, y, z = A * B * C, A * C * H, prime * K
            a = source * K // bridge
            if bridge * a != source * K:
                raise AssertionError("normalized source-square condition did not recover the source term")
            if prime != 4 * x - m or 4 * K != prime * R + 1:
                raise AssertionError("normal form reconstruction failed")
            if Fraction(4, source) != Fraction(1, a) + Fraction(1, x) + Fraction(1, y):
                raise AssertionError("source identity did not verify")
            if Fraction(4, prime) != Fraction(1, x) + Fraction(1, y) + Fraction(1, z):
                raise AssertionError("target identity did not verify")
            forms.append({"A": A, "B": B, "C": C, "H": H, "m": m})
    return sorted(forms, key=lambda form: (form["B"], form["C"], form["A"], form["m"]))


def run_audit(profile: dict[str, object]) -> dict[str, object]:
    records = []
    for entry in profile["records"]:
        prime = int(entry["prime"])
        source = int(entry["source_denominator"])
        bridge = int(entry["bridge_factor"])
        forms = source_state_forms(prime, source, bridge)
        B_one_forms = [form for form in forms if form["B"] == 1]
        if not B_one_forms:
            raise AssertionError("source state had no B=1 normal realization")
        stored = dict(zip(("A", "B", "C"), (int(value) for value in entry["normal_form"])))
        if not any(all(form[key] == value for key, value in stored.items()) for form in forms):
            raise AssertionError("stored normal form was not recovered from source-state divisor pairs")
        records.append(
            {
                "prime": prime,
                "source_denominator": source,
                "bridge_factor": bridge,
                "compatible_normal_form_count": len(forms),
                "B_eq_1_form_count": len(B_one_forms),
                "B_eq_1_realization_exists": True,
                "stored_normal_form_recovered": True,
                "least_divisor_pair_form": forms[0],
            }
        )
    return {
        "arithmetic": (
            "for every stored source state (p,n,E), set R=(E-1)/(p-n), K=(pR+1)/4, then enumerate "
            "all BC|K with R|(4B^2C+1), derive K/(BC)=-B (mod R), then recover A,m and verify both identities"
        ),
        "scope_note": (
            "An exact finite reconstruction of normal-form realizability from source-state divisor pairs. "
            "It identifies the remaining selector problem but does not bound the required factors uniformly."
        ),
        "input_source_state_count": len(records),
        "all_stored_normal_forms_recovered": all(record["stored_normal_form_recovered"] for record in records),
        "all_source_states_have_B_eq_1_realization": all(
            record["B_eq_1_realization_exists"] for record in records
        ),
        "compatible_normal_form_count_histogram": {
            str(count): sum(record["compatible_normal_form_count"] == count for record in records)
            for count in sorted({record["compatible_normal_form_count"] for record in records})
        },
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=SOURCE_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.profile.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
