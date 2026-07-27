#!/usr/bin/env python3
"""Verify an infinite Type I p-1 terminal ray with B=5 and E=32."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-b5-dyadic-terminal-ray-results.json"

STEP = 757_200
INITIAL = 21_169
R = 31
E = 32
B = 5
C = 1_262
GAP = 4_071


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_module("b5_dyadic_terminal_ray_base", BASE)


def is_prime(value: int) -> bool:
    """Return primality by trial division; used only for small displayed samples."""
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


def ray_witness(index: int) -> dict[str, object]:
    """Reconstruct the fixed terminal bridge at one nonnegative ray index."""
    if index < 0:
        raise ValueError("index must be nonnegative")
    A = 30 * index + 1
    prime = STEP * index + INITIAL
    H = A * R - B
    K = B * C * H
    witness = base.p_minus_one_witness(prime, E, B, C)
    if witness is None:
        raise AssertionError("the fixed p-1 bridge did not reconstruct")
    if (
        int(witness["R"]) != R
        or int(witness["K"]) != K
        or list(witness["normal_form"]) != [A, B, C]
        or int(witness["H"]) != H
        or int(witness["gap"]) != GAP
        or int(witness["source_denominator"]) != prime - 1
    ):
        raise AssertionError("the fixed ray parameters did not reconstruct")
    if prime % 24 != 1 or (prime - 1) % 16:
        raise AssertionError("the displayed ray lost its core or dyadic condition")
    if E % R != 1 or (prime - 1) * (prime - 1) // 4 % E:
        raise AssertionError("the bridge factor is not source-square compatible")
    if (4 * K * K) % E or E > 4 * K - 2 * R:
        raise AssertionError("the bridge factor is not a legal terminal divisor")
    return {
        "index": index,
        "prime": prime,
        "A": A,
        "B": B,
        "C": C,
        "H": H,
        "gap": GAP,
        "E": E,
        "R": R,
        "K": K,
        "source_denominator": prime - 1,
        "prime_check": is_prime(prime),
    }


def prime_samples(count: int = 4) -> list[dict[str, object]]:
    """Return the first few prime terms, solely as concrete audit examples."""
    samples: list[dict[str, object]] = []
    index = 0
    while len(samples) < count:
        record = ray_witness(index)
        if record["prime_check"]:
            samples.append(record)
        index += 1
    return samples


def run_audit() -> dict[str, object]:
    """Check the symbolic parameter ray at representative indices and prime terms."""
    algebra_samples = [ray_witness(index) for index in (0, 1, 6, 15)]
    if math.gcd(INITIAL, STEP) != 1:
        raise AssertionError("the progression is not primitive for Dirichlet's theorem")
    return {
        "arithmetic": (
            "for t>=0 set A=30t+1, p=757200t+21169, H=31A-5, and K=5*1262*H; "
            "then 4K=31p+1, E=32 is an even target divisor congruent to 1 modulo 31, "
            "and it gives the p-1 source bridge in normal form (A,5,1262) with gap 4071"
        ),
        "scope_note": (
            "Dirichlet's theorem makes the primitive progression contain infinitely many primes, and every "
            "such prime has this fixed Type I terminal bridge. This is one infinite covered family, not a "
            "selector for all core primes and not a lower bound excluding B<=4 on the same progression."
        ),
        "progression": {"initial": INITIAL, "step": STEP, "gcd": math.gcd(INITIAL, STEP)},
        "algebra_samples": algebra_samples,
        "prime_samples": prime_samples(),
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
