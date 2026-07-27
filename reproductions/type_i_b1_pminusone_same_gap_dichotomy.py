#!/usr/bin/env python3
"""Verify the exact same-gap Type I/II dichotomy in the B=1 p-1 chart."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
TAIL = ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
B1 = ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-b1-pminusone-same-gap-dichotomy-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_module("b1_pminusone_same_gap_base", BASE)


def is_prime(value: int) -> bool:
    """Return primality by trial division; this is only for displayed small terms."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def parameters(q: int, r: int, A: int) -> dict[str, int]:
    """Return the B=1 p-1 chart coordinates from q, r, and A."""
    if q < 1 or r < 1 or A < 1:
        raise ValueError("q, r, and A must be positive")
    m = 4 * q - 1
    R = 4 * r - 1
    C = m * r - q
    p = 4 * A * C - m
    K = C * (A * R - 1)
    return {"q": q, "r": r, "A": A, "m": m, "R": R, "C": C, "p": p, "K": K}


def has_pminusone_terminal_bridge(q: int, r: int, A: int) -> bool:
    """Check the exact bridge condition r | q^2(A+1)^2."""
    return (q * q * (A + 1) * (A + 1)) % r == 0


def same_gap_type_ii_tail(q: int, r: int, A: int) -> dict[str, object] | None:
    """Reconstruct the ordinary Type II double tail, exactly when q divides Ar."""
    state = parameters(q, r, A)
    m, C, p = state["m"], state["C"], state["p"]
    x = A * C
    if (A * r) % q:
        if (p - 1) % (m + 1) == 0:
            raise AssertionError("same-gap scaling unexpectedly remained integral")
        return None
    if x % q:
        raise AssertionError("q|Ar did not imply q|AC")
    divisor = q * A
    if divisor > x or (x * x) % divisor or (divisor + x) % m:
        raise AssertionError("canonical same-gap Type II divisor failed")
    numerator_y = p * (x + divisor)
    numerator_z = p * (x + x * x // divisor)
    if numerator_y % m or numerator_z % m:
        raise AssertionError("same-gap Type II denominators are not integral")
    target = (x, numerator_y // m, numerator_z // m)
    if target[1] % p or target[2] % p:
        raise AssertionError("the two Type II tails are not p-divisible")
    source_denominator = x // q
    source = (target[0], target[1] // p, target[2] // p)
    if Fraction(4, p) != sum((Fraction(1, term) for term in target), Fraction()):
        raise AssertionError("the Type II target identity failed")
    if Fraction(4, source_denominator) != sum(
        (Fraction(1, term) for term in source), Fraction()
    ):
        raise AssertionError("the Type II source identity failed")
    return {
        "divisor": divisor,
        "source_denominator": source_denominator,
        "target_solution": list(target),
        "source_solution": list(source),
    }


def b1_pminusone_witness(q: int, r: int, A: int) -> dict[str, object]:
    """Reconstruct one core B=1 p-1 bridge and its same-gap Type II status."""
    state = parameters(q, r, A)
    p, C, R, K = state["p"], state["C"], state["R"], state["K"]
    if p % 24 != 1:
        raise ValueError("this displayed witness is not a core p == 1 mod 24 instance")
    bridge_condition = has_pminusone_terminal_bridge(q, r, A)
    witness = base.p_minus_one_witness(p, 4 * r, 1, C)
    if (witness is not None) != bridge_condition:
        raise AssertionError("the p-1 bridge disagreed with r|q^2(A+1)^2")
    if witness is None:
        raise AssertionError("a displayed witness must satisfy the bridge condition")
    if (
        list(witness["normal_form"]) != [A, 1, C]
        or int(witness["gap"]) != state["m"]
        or int(witness["R"]) != R
        or int(witness["K"]) != K
        or int(witness["source_denominator"]) != p - 1
    ):
        raise AssertionError("the B=1 p-1 coordinates did not reconstruct")
    tail = same_gap_type_ii_tail(q, r, A)
    tail_condition = (A * r) % q == 0
    if (tail is not None) != tail_condition:
        raise AssertionError("same-gap tail did not agree with q|Ar")
    return {
        **state,
        "E": 4 * r,
        "bridge_condition": bridge_condition,
        "same_gap_type_ii_condition": tail_condition,
        "same_gap_type_ii_tail": tail,
        "type_i_source_denominator": p - 1,
        "prime_check": is_prime(p),
    }


def profile_stored_residual() -> dict[str, object]:
    """Check the same-gap law on every stored B=1 tail-miss bridge."""
    tail = json.loads(TAIL.read_text(encoding="utf-8"))
    b1 = json.loads(B1.read_text(encoding="utf-8"))
    ordinary_misses = {int(entry["prime"]) for entry in tail["misses"]}
    records: list[dict[str, int]] = []
    all_b1_count = 0
    for record in b1["records"]:
        prime = int(record["prime"])
        witness = record["minimum_b1_source_witness"]
        lift = witness["reverse_two_tail_lift"]
        A, B, C = (int(value) for value in witness["normal_form"])
        m, R, E = int(witness["gap"]), int(witness["R"]), int(witness["E"])
        q, r = (m + 1) // 4, (R + 1) // 4
        state = parameters(q, r, A)
        if (
            prime not in ordinary_misses
            or B != 1
            or state["C"] != C
            or state["p"] != prime
        ):
            raise AssertionError("stored B=1 bridge failed the chart reconstruction")
        if same_gap_type_ii_tail(q, r, A) is not None:
            raise AssertionError("an ordinary-tail miss had a same-gap Type II double tail")
        all_b1_count += 1
        if int(lift["source_denominator"]) != prime - 1:
            continue
        if E != R + 1 or not has_pminusone_terminal_bridge(q, r, A):
            raise AssertionError("stored p-1 B=1 bridge failed the terminal chart")
        records.append({"prime": prime, "q": q, "r": r, "A": A})
    if all_b1_count != 1_713 or len(records) != 1_400:
        raise AssertionError("the stored B=1 residual changed")
    return {
        "all_b1_count": all_b1_count,
        "pminusone_count": len(records),
        "all_bridge_conditions_hold": True,
        "all_same_gap_conditions_fail": True,
        "first_example": records[0],
    }


def nonoverlap_ray_samples(count: int = 3) -> list[dict[str, object]]:
    """Return prime terms of p=7896t+913, all outside their same-gap Type II branch."""
    samples: list[dict[str, object]] = []
    t = 0
    while len(samples) < count:
        A = 42 * t + 5
        state = parameters(7, 2, A)
        if is_prime(state["p"]):
            witness = b1_pminusone_witness(7, 2, A)
            if witness["same_gap_type_ii_tail"] is not None:
                raise AssertionError("the nonoverlap ray unexpectedly had a same-gap tail")
            samples.append({"ray_index": t, **witness})
        t += 1
    return samples


def run_audit() -> dict[str, object]:
    """Verify both branches, an infinite nonoverlap ray, and the 500M residual law."""
    overlap = b1_pminusone_witness(1, 6, 5)
    nonoverlap = b1_pminusone_witness(7, 2, 173)
    if overlap["same_gap_type_ii_tail"] is None:
        raise AssertionError("the q|Ar branch did not reconstruct its Type II tail")
    if nonoverlap["same_gap_type_ii_tail"] is not None:
        raise AssertionError("the q-not-dividing-Ar branch did not exclude its same-gap tail")
    step, initial = 7_896, 913
    if math.gcd(step, initial) != 1:
        raise AssertionError("the nonoverlap ray is not primitive")
    return {
        "arithmetic": (
            "for every B=1 normal form write m=4q-1, R=4r-1, and C=mr-q; the "
            "same-gap ordinary Type II double tail exists exactly when q divides Ar. "
            "For a p-1 source, its terminal bridge exists exactly when r divides q^2(A+1)^2."
        ),
        "scope_note": (
            "The nonoverlap statement rules out only the ordinary Type II double tail at the "
            "same gap. It neither excludes Type II certificates at other gaps nor proves a "
            "global mixed selector."
        ),
        "overlap_example": overlap,
        "nonoverlap_example": nonoverlap,
        "nonoverlap_ray": {
            "parameters": {"q": 7, "r": 2, "m": 27, "C": 47, "R": 7, "E": 8},
            "formula": "A=42t+5, p=7896t+913",
            "gcd_step_initial": math.gcd(step, initial),
            "prime_samples": nonoverlap_ray_samples(),
        },
        "stored_500m_b1_residual": profile_stored_residual(),
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
