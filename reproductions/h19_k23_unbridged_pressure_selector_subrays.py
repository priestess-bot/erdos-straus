#!/usr/bin/env python3
"""Verify low-defect selector subrays inside the two unbridged pressure rays."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy  # noqa: E402

from reproductions import type_ii_square_root_completion_family as family  # noqa: E402


DEFAULT_INPUT = (
    ROOT
    / "reproductions"
    / "h19-k23-global-one-factor-prime-families-2097152.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "h19-k23-unbridged-pressure-selector-subrays.json"
)
SELECTORS = {
    2_220_549_727_681_245_601: {"q": 15, "divisor": 37_845},
    748_375_048_866_405_601: {"q": 8, "divisor": 1_508_258},
}


def prime_support(value: int) -> set[int]:
    """Return the distinct prime support of one positive integer."""
    if value < 1:
        raise ValueError("value must be positive")
    return {int(prime) for prime in sympy.factorint(value)}


def verify_subray(row: dict[str, object], q: int, divisor: int) -> dict[str, object]:
    """Prove that one fixed tail divisor works on an entire affine subray."""
    prime_seed = int(row["prime_seed"])
    prime_step = int(row["prime_progression_step"])
    if prime_seed % 24 != 1 or prime_step % 24:
        raise AssertionError("subray does not stay in the core residue class")
    if math.gcd(prime_seed, prime_step) != 1:
        raise AssertionError("subray is not primitive")
    if (prime_seed - 1) % 4 or prime_step % 4:
        raise AssertionError("p-1 tail parameters are not integral")

    b_seed = (prime_seed - 1) // 4
    b_step = prime_step // 4
    if b_seed % q or b_step % q:
        raise AssertionError("q does not divide every (p-1)/4 on the subray")
    gap = 4 * q - 1
    x_seed = b_seed + q
    x_step = b_step
    if x_seed * x_seed % divisor or x_step % divisor:
        raise AssertionError("fixed divisor does not divide every x(n)^2")
    if (x_seed + divisor) % gap or x_step % gap:
        raise AssertionError("fixed divisor loses the target residue")
    if divisor > x_seed or math.gcd(divisor, gap) != 1:
        raise AssertionError("fixed divisor violates the Type II size or unit guard")

    support = sorted(prime_support(divisor) - prime_support(q))
    if len(support) > 2:
        raise AssertionError("selector subray exceeds support defect two")
    seed_witness = family.verify_normal_form(prime_seed, gap, divisor)
    next_witness = family.verify_normal_form(prime_seed + prime_step, gap, divisor)
    return {
        "prime_seed": prime_seed,
        "prime_step": prime_step,
        "primitive_progression_gcd": math.gcd(prime_seed, prime_step),
        "q": q,
        "gap": gap,
        "divisor": divisor,
        "divisor_factorization": {
            str(prime): int(exponent)
            for prime, exponent in sympy.factorint(divisor).items()
        },
        "new_support": support,
        "support_defect": len(support),
        "b_step_divisible_by_q": True,
        "x_step_divisible_by_divisor": True,
        "x_step_divisible_by_gap": True,
        "seed_witness": seed_witness,
        "next_parameter_witness": next_witness,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Extract and verify both selector subrays from the one-factor artifact."""
    rows = {int(row["prime_seed"]): row for row in payload["families"]}
    missing = sorted(set(SELECTORS) - set(rows))
    if missing:
        raise AssertionError(f"missing pressure seeds: {missing}")
    verified = [
        verify_subray(rows[seed], selector["q"], selector["divisor"])
        for seed, selector in SELECTORS.items()
    ]
    return {
        "arithmetic": (
            "exact affine divisibility and residue invariants, exact support counts, "
            "primitive progression gcds, and Type II witnesses at n=0 and n=1"
        ),
        "scope_note": (
            "Each refined subray has infinitely many prime values by Dirichlet and "
            "every such value has the fixed low-defect tail witness. This does not "
            "cover every prime value on either original pressure ray."
        ),
        "selector_subray_count": len(verified),
        "support_defect_histogram": {
            str(defect): sum(row["support_defect"] == defect for row in verified)
            for defect in sorted({int(row["support_defect"]) for row in verified})
        },
        "all_subrays_primitive": all(
            row["primitive_progression_gcd"] == 1 for row in verified
        ),
        "all_support_defects_at_most_two": all(
            row["support_defect"] <= 2 for row in verified
        ),
        "subrays": verified,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
