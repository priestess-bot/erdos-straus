#!/usr/bin/env python3
"""Select Type I bridges with a dyadic normal-form B from K's odd part."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-dyadic-b-source-selector-results.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_module("dyadic_b_source_selector_base", BASE)


def positive_divisors(value: int) -> list[int]:
    """Return every positive divisor using trial division."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    divisors = [1]
    for prime, exponent in factors:
        divisors = [
            previous * prime**power
            for previous in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def two_adic_order(value: int) -> int:
    """Return v_2(value) for a positive integer."""
    if value < 1:
        raise ValueError("value must be positive")
    return (value & -value).bit_length() - 1


def dyadic_b_source_witness(
    prime: int, shift: int, E: int, exponent: int
) -> dict[str, object] | None:
    """Construct a natural B=2^exponent bridge from one source state.

    If K=2^v*K_odd, the selector exhausts d|K_odd satisfying
    2^(v+exponent+2)*d=-1 (mod R) and K_odd/d>2^exponent.
    """
    if (
        prime % 4 != 1
        or shift <= 0
        or shift % 2 == 0
        or E <= 2
        or E % 2
        or exponent < 1
    ):
        return None
    source = prime - shift
    if source % 2 or not 2 <= source < prime or (E - 1) % shift:
        return None
    R = (E - 1) // shift
    if R < 3 or R % 2 == 0 or (source * source // math.gcd(E, 4)) % E:
        return None
    if (prime * R + 1) % 4:
        return None
    K = (prime * R + 1) // 4
    v = two_adic_order(K)
    if exponent > v:
        return None
    B = 1 << exponent
    K_odd = K >> v
    for d in positive_divisors(K_odd):
        H = K_odd // d
        if H <= B or ((1 << (v + exponent + 2)) * d + 1) % R:
            continue
        C = (1 << (v - exponent)) * d
        witness = base.shifted_source_witness(prime, shift, R, B, C)
        if witness is None:
            raise AssertionError("dyadic B residue did not reconstruct a bridge")
        if int(witness["H"]) != H or int(witness["K"]) != K:
            raise AssertionError("dyadic B reconstruction changed the factor pair")
        return {
            "exponent": exponent,
            "two_adic_order_K": v,
            "K_odd_divisor": d,
            **witness,
        }
    return None


def run_audit() -> dict[str, object]:
    """Reconstruct the finite B=2 and B=8 boundary witnesses."""
    b2 = dyadic_b_source_witness(63_332_329, 1, 48, 1)
    b8 = dyadic_b_source_witness(172_657_489, 1, 144, 3)
    rejected = dyadic_b_source_witness(172_657_489, 1, 144, 2)
    if b2 is None or b8 is None or rejected is not None:
        raise AssertionError("dyadic B selector boundary did not reproduce")
    return {
        "arithmetic": (
            "for a source state E=1+sR and K=(pR+1)/4, factor K=2^v*K_odd; "
            "for B=2^t enumerate d|K_odd with 2^(v+t+2)d=-1 (mod R), require "
            "K_odd/d>B, reconstruct C=2^(v-t)d, and verify both bridge identities"
        ),
        "scope_note": (
            "An exact fixed-source-state selector for dyadic B. It does not "
            "supply a source state or a dyadic B exponent for every core prime."
        ),
        "B2_witness": b2,
        "B8_witness": b8,
        "B4_rejected_on_B8_state": rejected,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
