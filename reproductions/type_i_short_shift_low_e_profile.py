#!/usr/bin/env python3
"""Profile a finite short-shift, dynamic-bridge Type I selector on stored residuals."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESIDUAL = ROOT / "reproductions" / "type-i-shifted-source-b1-menu-profile-10m-results.json"
SELECTOR = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_E_CAP = 1_000_000
DEFAULT_B_CAP = 7
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-short-shift-low-e-profile-10m-results.json"
SHIFTS = (3, 7, 9, 25)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


selector = load_module("short_shift_low_e_selector", SELECTOR)
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


def source_square_divisors(source: int, e_cap: int) -> list[int]:
    """Enumerate E<=cap from n^2 by factoring n once, rather than n^2 directly."""
    factors = {prime: 2 * exponent for prime, exponent in landscape.factor_by_trial_division(source).items()}
    return [divisor for divisor in divisors_from_factorization(factors) if 2 <= divisor <= e_cap and divisor % 2 == 0]


def parse_shifts(value: str) -> tuple[int, ...]:
    """Parse a comma-separated increasing short-shift menu for the command line."""
    try:
        shifts = tuple(int(item) for item in value.split(",") if item)
    except ValueError as error:
        raise argparse.ArgumentTypeError("shifts must be comma-separated integers") from error
    if not shifts or tuple(sorted(set(shifts))) != shifts or any(shift <= 0 or shift % 2 == 0 for shift in shifts):
        raise argparse.ArgumentTypeError("shifts must be increasing distinct positive odd integers")
    return shifts


def first_witness(
    prime: int,
    shifts: tuple[int, ...] = SHIFTS,
    e_cap: int = DEFAULT_E_CAP,
    b_cap: int = DEFAULT_B_CAP,
) -> dict[str, int] | None:
    """Try each short shift, every compatible low E, and every B-bounded divisor pair."""
    for shift in shifts:
        source = prime - shift
        if source % 2 or source < 2:
            continue
        for E in source_square_divisors(source, e_cap):
            normalizer = math.gcd(E, 4)
            if (source * source // normalizer) % E or (E - 1) % shift:
                continue
            R = (E - 1) // shift
            if R < 3 or R % 2 == 0 or (prime * R + 1) % 4:
                continue
            K = (prime * R + 1) // 4
            factors = landscape.factor_by_trial_division(K)
            divisors = divisors_from_factorization(factors)
            for B in range(1, b_cap + 1):
                for C in divisors:
                    if K % (B * C) or (4 * B * B * C + 1) % R:
                        continue
                    witness = selector.shifted_source_witness(prime, shift, R, B, C)
                    if witness is None:
                        raise AssertionError("short-shift state did not reconstruct its edge")
                    return {
                        "shift": shift,
                        "R": R,
                        "E": E,
                        "B": B,
                        "C": C,
                        "H": int(witness["H"]),
                        "gap": int(witness["gap"]),
                        "source_denominator": int(witness["source_denominator"]),
                    }
    return None


def run_profile(
    residual_path: Path = RESIDUAL,
    shifts: tuple[int, ...] = SHIFTS,
    e_cap: int = DEFAULT_E_CAP,
    b_cap: int = DEFAULT_B_CAP,
) -> dict[str, object]:
    """Exhaust the stated short-shift dynamic-bridge selector over a finite residual set."""
    if not shifts or any(shift <= 0 or shift % 2 == 0 for shift in shifts):
        raise ValueError("shifts must be non-empty positive odd integers")
    if e_cap < 2 or b_cap < 1:
        raise ValueError("e_cap must be at least 2 and b_cap must be positive")
    residual = json.loads(residual_path.read_text(encoding="utf-8"))
    records = []
    misses = []
    for prime in (int(value) for value in residual["misses"]):
        witness = first_witness(prime, shifts, e_cap, b_cap)
        records.append({"prime": prime, "witness": witness})
        if witness is None:
            misses.append(prime)
    witnesses = [record["witness"] for record in records if record["witness"] is not None]
    return {
        "arithmetic": (
            "for every stated residual and each short shift s, factor n=p-s, enumerate every even E<=e_cap "
            "allowed by E|n^2/gcd(E,4) with R=(E-1)/s integral, factor K=(pR+1)/4, enumerate all "
            "BC|K with B<=b_cap, and exactly reconstruct every selected Type I edge"
        ),
        "scope_note": (
            "A complete finite audit of one stated short-shift and low-E box. A miss excludes only its shifts, "
            "bridge cap, and B cap; it does not exclude larger or different source states."
        ),
        "prime_limit": residual["prime_limit"],
        "input_residual_count": len(records),
        "shifts": list(shifts),
        "e_cap": e_cap,
        "b_cap": b_cap,
        "captured_count": len(witnesses),
        "misses": misses,
        "selected_shift_histogram": dict(sorted(Counter(str(witness["shift"]) for witness in witnesses).items(), key=lambda item: int(item[0]))),
        "selected_B_histogram": dict(sorted(Counter(str(witness["B"]) for witness in witnesses).items(), key=lambda item: int(item[0]))),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--residual", type=Path, default=RESIDUAL)
    parser.add_argument("--shifts", type=parse_shifts, default=SHIFTS)
    parser.add_argument("--e-cap", type=int, default=DEFAULT_E_CAP)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.residual, args.shifts, args.e_cap, args.b_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
