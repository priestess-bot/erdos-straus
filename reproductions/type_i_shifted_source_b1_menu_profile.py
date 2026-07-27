#!/usr/bin/env python3
"""Profile a fixed shifted-source B=1 divisor-residue menu on p-1 residuals."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESIDUAL = ROOT / "reproductions" / "type-i-pminusone-low-e1m-all-b-joint-residual-profile-1m-results.json"
SELECTOR = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-shifted-source-b1-menu-profile-1m-results.json"
SOURCE_MENU = ((9, 31), (25, 19))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


selector = load_module("shifted_source_b1_menu_selector", SELECTOR)
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


def first_witness(prime: int, source_menu: tuple[tuple[int, int], ...] = SOURCE_MENU) -> dict[str, int] | None:
    """Try every stated (shift, R) pair and every divisor C|K in menu order."""
    for shift, R in source_menu:
        source = prime - shift
        E = shift * R + 1
        if source % 2 or source < 2 or (prime * R + 1) % 4:
            continue
        if (source * source // math.gcd(E, 4)) % E:
            continue
        K = (prime * R + 1) // 4
        factors = landscape.factor_by_trial_division(K)
        for C in divisors_from_factorization(factors):
            if (4 * C + 1) % R:
                continue
            witness = selector.shifted_source_b1_witness(prime, shift, R, C)
            if witness is None:
                raise AssertionError("shifted-source divisor residue did not reconstruct its edge")
            return {
                "shift": shift,
                "R": R,
                "E": E,
                "C": C,
                "H": int(witness["H"]),
                "gap": int(witness["gap"]),
                "source_denominator": int(witness["source_denominator"]),
            }
    return None


def run_profile(
    residual_path: Path = RESIDUAL,
    source_menu: tuple[tuple[int, int], ...] = SOURCE_MENU,
) -> dict[str, object]:
    """Exhaust the fixed shifted B=1 menu on a stored p-1 residual profile."""
    residual = json.loads(residual_path.read_text(encoding="utf-8"))
    records = []
    misses = []
    for prime in (int(value) for value in residual["misses"]):
        witness = first_witness(prime, source_menu)
        records.append({"prime": prime, "witness": witness})
        if witness is None:
            misses.append(prime)
    witnesses = [record["witness"] for record in records if record["witness"] is not None]
    return {
        "arithmetic": (
            "for every listed p-1 residual and every fixed (s,R) state, test E=sR+1 against the normalized "
            "source-square condition, factor K=(pR+1)/4, enumerate all C|K with 4C=-1 (mod R), and "
            "reconstruct the natural B=1 shifted-source Type I edge exactly"
        ),
        "scope_note": (
            "A complete finite audit of the stated shifted-source menu. A miss excludes only these two fixed "
            "(s,R) states with B=1, not other shifts, bridge factors, B values, or Type II coordinates."
        ),
        "prime_limit": residual["prime_limit"],
        "input_residual_count": len(records),
        "source_menu": [{"shift": shift, "R": R, "E": shift * R + 1} for shift, R in source_menu],
        "captured_count": len(witnesses),
        "misses": misses,
        "selected_shift_histogram": dict(sorted(Counter(str(witness["shift"]) for witness in witnesses).items(), key=lambda item: int(item[0]))),
        "selected_R_histogram": dict(sorted(Counter(str(witness["R"]) for witness in witnesses).items(), key=lambda item: int(item[0]))),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--residual", type=Path, default=RESIDUAL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.residual)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
