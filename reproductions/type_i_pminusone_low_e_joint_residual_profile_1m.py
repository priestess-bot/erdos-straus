#!/usr/bin/env python3
"""Exhaust low p-1 bridge factors on the one-million two-selector residuals."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DYADIC = ROOT / "reproductions" / "type-i-dyadic-pminusone-profile-1m-results.json"
MENU = ROOT / "reproductions" / "type-i-pminusone-b12-menu-profile-1m-results.json"
SELECTOR = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_E_CAP = 4_096
DEFAULT_B_CAP = 4
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-pminusone-low-e-joint-residual-profile-1m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


selector = load_module("pminusone_low_e_joint_selector", SELECTOR)
landscape = selector.direct.support_min.landscape


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            base * prime**power
            for base in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def joint_misses(dyadic_path: Path, menu_path: Path) -> list[int]:
    dyadic = json.loads(dyadic_path.read_text(encoding="utf-8"))
    menu = json.loads(menu_path.read_text(encoding="utf-8"))
    if dyadic["prime_limit"] != menu["prime_limit"] or dyadic["core_prime_count"] != menu["core_prime_count"]:
        raise ValueError("the two input profiles do not share a finite prefix")
    menu_misses = {int(prime) for prime in menu["misses"]}
    return [int(prime) for prime in dyadic["misses"] if int(prime) in menu_misses]


def allowed_low_E(prime: int, e_cap: int) -> list[int]:
    """List every four-divisible E<=cap allowed exactly by the p-1 square condition."""
    source_square = (prime - 1) * (prime - 1) // 4
    factors = landscape.factor_by_trial_division(source_square)
    return [
        divisor
        for divisor in divisors_from_factorization(factors)
        if 4 <= divisor <= e_cap and divisor % 4 == 0
    ]


def first_low_E_witness(prime: int, e_cap: int, b_cap: int | None) -> dict[str, int] | None:
    """Exhaust every allowed low bridge factor and each B-bounded divisor pair."""
    for E in allowed_low_E(prime, e_cap):
        R = E - 1
        K = (prime * R + 1) // 4
        factors = landscape.factor_by_trial_division(K)
        divisors = divisors_from_factorization(factors)
        b_values = divisors if b_cap is None else range(1, b_cap + 1)
        for B in b_values:
            for C in divisors:
                if K % (B * C) or (4 * B * B * C + 1) % R:
                    continue
                H = K // (B * C)
                A_numerator = H + B
                if A_numerator % R:
                    raise AssertionError("complementary normal-form residue did not reconstruct")
                A = A_numerator // R
                if math.gcd(A, B) != 1:
                    continue
                witness = selector.p_minus_one_witness(prime, E, B, C)
                if witness is None:
                    raise AssertionError("low-E factor pair did not reconstruct the p-1 edge")
                return {
                    "E": E,
                    "B": B,
                    "C": C,
                    "H": H,
                    "gap": int(witness["gap"]),
                    "source_denominator": int(witness["source_denominator"]),
                }
    return None


def run_profile(
    dyadic_path: Path = DYADIC,
    menu_path: Path = MENU,
    e_cap: int = DEFAULT_E_CAP,
    b_cap: int | None = DEFAULT_B_CAP,
) -> dict[str, object]:
    """Classify the joint residuals by all square-allowed low p-1 bridge factors."""
    if e_cap < 4 or (b_cap is not None and b_cap < 1):
        raise ValueError("e_cap must be at least 4 and b_cap must be positive when bounded")
    residuals = joint_misses(dyadic_path, menu_path)
    records = []
    misses = []
    for prime in residuals:
        witness = first_low_E_witness(prime, e_cap, b_cap)
        records.append({"prime": prime, "witness": witness})
        if witness is None:
            misses.append(prime)
    witnesses = [record["witness"] for record in records if record["witness"] is not None]
    return {
        "arithmetic": (
            "intersect the stored one-million dyadic and fixed-menu p-1 misses; for every resulting prime, "
            "enumerate all E<=e_cap with 4|E|(p-1)^2/4, factor K=((E-1)p+1)/4, enumerate every BC|K "
            "with B<=b_cap or every B|K when requested, and verify each reconstructed p-1 Type I edge exactly"
        ),
        "scope_note": (
            "A complete finite low-E p-1 refinement of one stored joint residual set. A remaining miss may use "
            "a larger bridge factor, a larger B, a non-p-1 source, another Type I coordinate, or Type II."
        ),
        "prime_limit": json.loads(dyadic_path.read_text(encoding="utf-8"))["prime_limit"],
        "joint_residual_count": len(residuals),
        "e_cap": e_cap,
        "b_cap": b_cap,
        "captured_count": len(witnesses),
        "misses": misses,
        "selected_E_histogram": dict(sorted(Counter(str(witness["E"]) for witness in witnesses).items(), key=lambda item: int(item[0]))),
        "selected_B_histogram": dict(sorted(Counter(str(witness["B"]) for witness in witnesses).items(), key=lambda item: int(item[0]))),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dyadic", type=Path, default=DYADIC)
    parser.add_argument("--menu", type=Path, default=MENU)
    parser.add_argument("--e-cap", type=int, default=DEFAULT_E_CAP)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--all-b", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.dyadic, args.menu, args.e_cap, None if args.all_b else args.b_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
