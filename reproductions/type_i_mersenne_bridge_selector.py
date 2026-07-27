#!/usr/bin/env python3
"""Verify the dyadic (R=2^t-1) p-1 source specialization of the Type I selector."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECT = ROOT / "reproductions" / "type_i_direct_small_b_even_source_audit.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-mersenne-bridge-selector-21169-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


direct = load_module("mersenne_bridge_direct", DIRECT)


def shifted_source_witness(
    prime: int, shift: int, R: int, B: int, C: int
) -> dict[str, object] | None:
    """Construct a natural Type I edge from a fixed shifted source state, if valid."""
    if (
        prime % 4 != 1
        or shift <= 0
        or shift % 2 == 0
        or R < 3
        or R % 2 == 0
        or B < 1
        or C < 1
    ):
        return None
    source = prime - shift
    if source % 2 or not 2 <= source < prime:
        return None
    E = shift * R + 1
    if E % 2:
        return None
    normalizer = math.gcd(E, 4)
    if (source * source // normalizer) % E:
        return None
    if (prime * R + 1) % 4:
        return None
    K = (prime * R + 1) // 4
    if K % (B * C) or (4 * B * B * C + 1) % R:
        return None
    H = K // (B * C)
    if (H + B) % R:
        raise AssertionError("the shifted-source complementary residue failed")
    A = (H + B) // R
    if math.gcd(A, B) != 1:
        return None
    gap = (4 * B * B * C + 1) // R
    if gap % 4 != 3 or not 3 <= gap <= prime - 2:
        return None
    if prime != 4 * A * B * C - gap:
        raise AssertionError("shifted-source factor pair did not reconstruct the target")
    source_term_numerator = source * K
    if source_term_numerator % E:
        raise AssertionError("shifted-source square condition did not reconstruct the source term")
    source_term = source_term_numerator // E
    target = (A * B * C, A * C * H, prime * K)
    if Fraction(4, prime) != sum((Fraction(1, term) for term in target), Fraction()):
        raise AssertionError("shifted-source target identity did not verify")
    if Fraction(4, source) != sum(
        (Fraction(1, term) for term in (source_term, target[0], target[1])), Fraction()
    ):
        raise AssertionError("shifted-source identity did not verify")
    _, lifts = direct.support_min.bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
    matching_lift = next(
        (lift for lift in lifts if int(lift["source_denominator"]) == source), None
    )
    if matching_lift is None:
        raise AssertionError("generic maximum-tail bridge did not recover the shifted source")
    if int(matching_lift["bridge_divisor"]) != prime * prime * E:
        raise AssertionError("generic bridge did not have the requested shifted factor")
    return {
        "prime": prime,
        "shift": shift,
        "E": E,
        "R": R,
        "K": K,
        "normal_form": [A, B, C],
        "H": H,
        "gap": gap,
        "source_denominator": source,
        "source_term": source_term,
        "bridge_factor": E,
    }


def shifted_source_b1_witness(prime: int, shift: int, R: int, C: int) -> dict[str, object] | None:
    """Construct a natural B=1 edge from a fixed shifted source state, if valid."""
    witness = shifted_source_witness(prime, shift, R, 1, C)
    if witness is None:
        return None
    return {key: value for key, value in witness.items() if key != "B"}


def p_minus_one_witness(prime: int, E: int, B: int, C: int) -> dict[str, object] | None:
    """Construct a p-1 source edge from an arbitrary four-divisible bridge factor."""
    if prime % 4 != 1 or E < 4 or E % 4 or B < 1 or C < 1:
        return None
    R = E - 1
    if ((prime - 1) * (prime - 1) // 4) % E:
        return None
    if (prime * R + 1) % 4:
        return None
    K = (prime * R + 1) // 4
    if K % (B * C):
        return None
    H = K // (B * C)
    if (4 * B * B * C + 1) % R:
        return None
    if (H + B) % R:
        raise AssertionError("the automatic complementary residue failed")
    A = (H + B) // R
    if math.gcd(A, B) != 1:
        return None
    gap = (4 * B * B * C + 1) // R
    if prime != 4 * A * B * C - gap:
        raise AssertionError("factor pair did not reconstruct the target")
    source = prime - 1
    source_term_numerator = source * K
    if source_term_numerator % E:
        raise AssertionError("source-square condition did not reconstruct the source term")
    source_term = source_term_numerator // E
    target = (A * B * C, A * C * H, prime * K)
    if Fraction(4, prime) != sum((Fraction(1, term) for term in target), Fraction()):
        raise AssertionError("target identity did not verify")
    if Fraction(4, source) != sum(
        (Fraction(1, term) for term in (source_term, target[0], target[1])), Fraction()
    ):
        raise AssertionError("p-1 source identity did not verify")
    _, lifts = direct.support_min.bridge.type_i_normal_reverse_two_tail_lifts(prime, gap, A, B, C)
    matching_lift = next(
        (lift for lift in lifts if int(lift["source_denominator"]) == source), None
    )
    if matching_lift is None:
        raise AssertionError("generic maximum-tail bridge did not recover the dyadic edge")
    if int(matching_lift["bridge_divisor"]) != prime * prime * E:
        raise AssertionError("generic bridge did not have the requested E")
    return {
        "prime": prime,
        "E": E,
        "R": R,
        "K": K,
        "normal_form": [A, B, C],
        "H": H,
        "gap": gap,
        "source_denominator": source,
        "source_term": source_term,
        "bridge_factor": E,
    }


def dyadic_p_minus_one_witness(prime: int, exponent: int, B: int, C: int) -> dict[str, object] | None:
    """Construct a p-1 source edge from the dyadic factor-pair selector, if valid."""
    if exponent < 2:
        return None
    witness = p_minus_one_witness(prime, 1 << exponent, B, C)
    return None if witness is None else {"exponent": exponent, **witness}


def run_audit() -> dict[str, object]:
    witness = dyadic_p_minus_one_witness(21_169, 5, 5, 1_262)
    if witness is None:
        raise AssertionError("the stated 21169 dyadic selector did not reconstruct")
    return {
        "arithmetic": (
            "set E=2^t and R=E-1 for source n=p-1; check E|(p-1)^2/4, then select "
            "BC|K=(pR+1)/4 with R|(4B^2C+1) and gcd((K/(BC)+B)/R,B)=1; reconstruct and "
            "verify both exact unit-fraction identities and the generic maximum-tail bridge"
        ),
        "scope_note": (
            "A verified instance of the exact dyadic p-1 source specialization. It does not show that "
            "a dyadic exponent or factor pair exists for every core prime."
        ),
        "witness": witness,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
