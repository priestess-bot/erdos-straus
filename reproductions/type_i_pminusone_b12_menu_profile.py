#!/usr/bin/env python3
"""Profile a fixed non-dyadic p-1 B=1,2 bridge menu on core primes."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SELECTOR = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_LIMIT = 100_009
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-pminusone-b12-menu-profile-100k-results.json"
E_MENU = (12, 20, 24, 28, 40, 48, 56, 72, 100, 112, 120, 136)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


selector = load_module("pminusone_b12_menu_selector", SELECTOR)
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


def first_menu_witness(prime: int) -> dict[str, int] | None:
    """Search the fixed E menu using only the exact B=1,2 residue conditions."""
    source_square = (prime - 1) * (prime - 1) // 4
    for E in E_MENU:
        if source_square % E:
            continue
        R = E - 1
        K = (prime * R + 1) // 4
        factors = landscape.factor_by_trial_division(K)
        for B in (1, 2):
            for C in divisors_from_factorization(factors):
                if K % (B * C) or (4 * B * B * C + 1) % R:
                    continue
                H = K // (B * C)
                if B == 2 and H % 2 == 0:
                    continue
                witness = selector.p_minus_one_witness(prime, E, B, C)
                if witness is None:
                    raise AssertionError("residue candidate did not reconstruct its p-1 edge")
                return {
                    "E": E,
                    "B": B,
                    "C": C,
                    "H": H,
                    "gap": int(witness["gap"]),
                    "source_denominator": int(witness["source_denominator"]),
                }
    return None


def run_profile(limit: int = DEFAULT_LIMIT) -> dict[str, object]:
    """Exhaust the fixed E menu for every core prime in a finite prefix."""
    if limit < 73:
        raise ValueError("limit must be at least 73")
    records = []
    misses = []
    for prime in landscape.short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        witness = first_menu_witness(prime)
        records.append({"prime": prime, "witness": witness})
        if witness is None:
            misses.append(prime)
    witnesses = [record["witness"] for record in records if record["witness"] is not None]
    return {
        "arithmetic": (
            "for every core prime in the stated prefix, take each E in the fixed menu, enforce "
            "E|(p-1)^2/4, factor K=((E-1)p+1)/4, enumerate all C|K, and test the exact B=1,2 "
            "divisor-residue conditions before reconstructing the p-1 Type I edge"
        ),
        "scope_note": (
            "A complete finite audit of one fixed non-dyadic bridge menu. A miss excludes only these "
            "twelve E values with B in {1,2} and source p-1."
        ),
        "prime_limit": limit,
        "E_menu": list(E_MENU),
        "core_prime_count": len(records),
        "captured_count": len(witnesses),
        "misses": misses,
        "selected_E_histogram": dict(sorted(Counter(str(witness["E"]) for witness in witnesses).items(), key=lambda item: int(item[0]))),
        "selected_B_histogram": dict(sorted(Counter(str(witness["B"]) for witness in witnesses).items(), key=lambda item: int(item[0]))),
        "maximum_selected_gap": max((witness["gap"] for witness in witnesses), default=None),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_profile(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
