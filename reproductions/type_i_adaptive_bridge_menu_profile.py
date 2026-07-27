#!/usr/bin/env python3
"""Profile a bridge-menu selector whose source shift is chosen from E-1."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESIDUAL = ROOT / "reproductions" / "type-i-shifted-source-b1-menu-profile-50m-results.json"
SELECTOR = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
SOURCE_MODULUS = ROOT / "reproductions" / "type_i_source_square_modulus.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-adaptive-bridge-menu-profile-50m-results.json"
DEFAULT_B_CAP = 7

# A finite bridge menu extracted from the fifty-million final residual.  The shift is not fixed:
# every odd s | E-1 is considered through the source-congruence condition.
E_MENU = (58, 352, 414, 676, 722, 928, 1442, 1540, 2080, 2576, 2704, 2800, 3276, 5540, 5776, 7776)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


selector = load_module("adaptive_bridge_menu_selector", SELECTOR)
source_modulus = load_module("adaptive_bridge_menu_modulus", SOURCE_MODULUS)
landscape = selector.direct.support_min.landscape


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [base * prime**power for base in divisors for power in range(exponent + 1)]
    return sorted(divisors)


@lru_cache(maxsize=None)
def odd_shift_states(E: int, minimum_R: int = 3) -> tuple[tuple[int, int, int], ...]:
    """Return all (s, R, Lambda(E)) with E=sR+1 and the requested odd R floor."""
    if E < 2 or E % 2:
        raise ValueError("bridge factors must be positive even integers")
    modulus = source_modulus.source_square_modulus(E)
    shifts = []
    for shift in divisors_from_factorization(source_modulus.factor_by_trial_division(E - 1)):
        if shift % 2:
            R = (E - 1) // shift
            if R >= minimum_R:
                shifts.append((shift, R, modulus))
    return tuple(shifts)


def first_witness(
    prime: int,
    E_menu: tuple[int, ...] = E_MENU,
    b_cap: int = DEFAULT_B_CAP,
) -> dict[str, int] | None:
    """Select E first, then derive every possible odd source shift from E-1 exactly."""
    if prime % 4 != 1 or b_cap < 1:
        return None
    for E in E_menu:
        for shift, R, modulus in odd_shift_states(E):
            source = prime - shift
            if source < 2 or source % modulus or (prime * R + 1) % 4:
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
                        raise AssertionError("bridge-menu state did not reconstruct its Type I edge")
                    return {
                        "E": E,
                        "shift": shift,
                        "R": R,
                        "B": B,
                        "C": C,
                        "H": int(witness["H"]),
                        "gap": int(witness["gap"]),
                        "source_denominator": int(witness["source_denominator"]),
                    }
    return None


def run_profile(
    residual_path: Path = RESIDUAL,
    E_menu: tuple[int, ...] = E_MENU,
    b_cap: int = DEFAULT_B_CAP,
) -> dict[str, object]:
    """Audit the complete adaptive-shift selector defined by one finite bridge menu."""
    if not E_menu or tuple(sorted(set(E_menu))) != E_menu:
        raise ValueError("E_menu must be a non-empty increasing tuple of distinct bridge factors")
    residual = json.loads(residual_path.read_text(encoding="utf-8"))
    records = []
    misses = []
    for prime in (int(value) for value in residual["misses"]):
        witness = first_witness(prime, E_menu, b_cap)
        records.append({"prime": prime, "witness": witness})
        if witness is None:
            misses.append(prime)
    witnesses = [record["witness"] for record in records if record["witness"] is not None]
    return {
        "arithmetic": (
            "for every stated residual and every bridge E in the finite menu, enumerate every odd s|E-1 "
            "with R=(E-1)/s>=3; enforce p=s mod Lambda(E), factor K=(pR+1)/4, enumerate BC|K with "
            "B<=b_cap, and reconstruct every selected Type I edge exactly"
        ),
        "scope_note": (
            "A complete finite audit of one bridge menu. The adaptive shift is derived from E-1, but a fixed "
            "finite E menu is not a universal selector."
        ),
        "prime_limit": residual["prime_limit"],
        "input_residual_count": len(records),
        "E_menu": list(E_menu),
        "b_cap": b_cap,
        "captured_count": len(witnesses),
        "misses": misses,
        "selected_E_histogram": dict(
            sorted(Counter(str(witness["E"]) for witness in witnesses).items(), key=lambda item: int(item[0]))
        ),
        "selected_shift_histogram": dict(
            sorted(Counter(str(witness["shift"]) for witness in witnesses).items(), key=lambda item: int(item[0]))
        ),
        "selected_B_histogram": dict(
            sorted(Counter(str(witness["B"]) for witness in witnesses).items(), key=lambda item: int(item[0]))
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--residual", type=Path, default=RESIDUAL)
    parser.add_argument("--b-cap", type=int, default=DEFAULT_B_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.residual, E_MENU, args.b_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
