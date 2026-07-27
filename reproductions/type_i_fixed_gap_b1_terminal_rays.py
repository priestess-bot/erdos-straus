#!/usr/bin/env python3
"""Verify fixed-gap B=1 Type I p-1 terminal rays."""

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
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-fixed-gap-b1-terminal-rays-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_module("fixed_gap_b1_terminal_rays_base", BASE)


def is_prime(value: int) -> bool:
    """Return primality by trial division; used only for displayed examples."""
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


def ordinary_type_ii_tail(
    prime: int, gap: int, gap_index: int, A: int, C: int
) -> dict[str, object]:
    """Reconstruct the ordinary Type II tail sharing this fixed-gap ray."""
    x = A * C
    divisor = gap_index * A
    if x % divisor or divisor > x or divisor % gap != (-x) % gap:
        raise AssertionError("the displayed ordinary Type II divisor did not reconstruct")
    numerator_y = prime * (x + divisor)
    numerator_z = prime * (x + x * x // divisor)
    if numerator_y % gap or numerator_z % gap:
        raise AssertionError("the Type II denominators are not integral")
    target = (x, numerator_y // gap, numerator_z // gap)
    if target[1] % prime or target[2] % prime:
        raise AssertionError("the displayed certificate does not have two p-divisible tails")
    source_denominator = (prime + gap) // (gap + 1)
    if (gap + 1) * source_denominator != prime + gap:
        raise AssertionError("the ordinary tail source is not integral")
    source = (target[0], target[1] // prime, target[2] // prime)
    if Fraction(4, prime) != sum((Fraction(1, value) for value in target), Fraction()):
        raise AssertionError("the Type II target identity did not verify")
    if Fraction(4, source_denominator) != sum(
        (Fraction(1, value) for value in source), Fraction()
    ):
        raise AssertionError("the Type II source identity did not verify")
    return {
        "gap": gap,
        "divisor": divisor,
        "source_denominator": source_denominator,
        "target_solution": list(target),
        "source_solution": list(source),
    }


def ray_witness(gap_index: int, scale: int, index: int) -> dict[str, object]:
    """Reconstruct one fixed-gap p-1 bridge in the two-parameter ray family."""
    if gap_index < 1 or scale < 1 or index < 1:
        raise ValueError("gap_index, scale, and index must be positive")
    gap = 4 * gap_index - 1
    bridge_scale = 6 * gap_index * scale
    R = 4 * bridge_scale - 1
    E = 4 * bridge_scale
    C = gap_index * (6 * gap * scale - 1)
    A = 6 * scale * index - 1
    step = 24 * scale * C
    initial = 1 - 24 * gap_index * gap * scale
    prime = step * index + initial
    K = C * (A * R - 1)
    witness = base.p_minus_one_witness(prime, E, 1, C)
    if witness is None:
        raise AssertionError("the fixed-gap B=1 bridge did not reconstruct")
    if (
        int(witness["R"]) != R
        or int(witness["K"]) != K
        or list(witness["normal_form"]) != [A, 1, C]
        or int(witness["gap"]) != gap
        or int(witness["source_denominator"]) != prime - 1
    ):
        raise AssertionError("the fixed-gap ray parameters did not reconstruct")
    if math.gcd(step, initial) != 1:
        raise AssertionError("the progression is not primitive for Dirichlet's theorem")
    if prime % 24 != 1 or (prime - 1) * (prime - 1) // 4 % E:
        raise AssertionError("the core or p-1 bridge condition failed")
    if (4 * K * K) % E or E > 4 * K - 2 * R:
        raise AssertionError("the bridge factor is not a legal terminal divisor")
    ordinary_tail = ordinary_type_ii_tail(prime, gap, gap_index, A, C)
    return {
        "gap_index": gap_index,
        "scale": scale,
        "index": index,
        "gap": gap,
        "A": A,
        "B": 1,
        "C": C,
        "R": R,
        "E": E,
        "bridge_scale": bridge_scale,
        "overlap_condition": bridge_scale % gap_index == 0,
        "K": K,
        "prime": prime,
        "source_denominator": prime - 1,
        "ordinary_type_ii_tail": ordinary_tail,
        "progression": {"initial": initial, "step": step, "gcd": math.gcd(step, initial)},
        "prime_check": is_prime(prime),
    }


def prime_samples(gap_index: int, scale: int, count: int = 3) -> list[dict[str, object]]:
    """Return the first few prime terms as concrete examples of one fixed ray."""
    samples: list[dict[str, object]] = []
    index = 1
    while len(samples) < count:
        record = ray_witness(gap_index, scale, index)
        if record["prime_check"]:
            samples.append(record)
        index += 1
    return samples


def run_audit() -> dict[str, object]:
    """Check representative gaps and the prime terms on the smallest ray."""
    examples = [
        ray_witness(1, 1, 1),
        ray_witness(2, 1, 3),
        ray_witness(3, 1, 1),
        ray_witness(5, 3, 2),
    ]
    return {
        "arithmetic": (
            "for q,s,v>=1 set m=4q-1, C=q(6ms-1), A=6sv-1, R=24qs-1, "
            "E=24qs, and p=4AC-m=24sCv+1-24qms; then p is 1 modulo 24, "
            "the progression in v is primitive, and the B=1 normal form has "
            "a p-1 terminal bridge with factor E=R+1"
        ),
        "scope_note": (
            "For every fixed q,s, Dirichlet's theorem gives infinitely many prime terms in the "
            "displayed progression, all with both the stated Type I bridge and an explicit ordinary "
            "Type II tail. These are infinite overlap subfamilies, not a selector for every core prime."
        ),
        "examples": examples,
        "gap_three_prime_samples": prime_samples(1, 1),
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
