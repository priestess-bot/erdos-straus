#!/usr/bin/env python3
"""Find a conditional one-private-prime escape for a Type I moving window.

Each x_j=(p+4j-1)/4 is represented as a fixed factor times one primitive
affine prime form. The exact Type I square-divisor target is -1/4 modulo the
gap. A returned state is conditional on Dickson's conjecture or Schinzel's
Hypothesis H for the displayed affine forms.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TYPE_II_MODEL = ROOT / "reproductions" / "type_ii_moving_window_conditional_escape.py"
RESULTS = (
    ROOT
    / "reproductions"
    / "type-i-moving-window-conditional-escape-p21169-j8-results.json"
)


def load_type_ii_model():
    spec = importlib.util.spec_from_file_location(
        "type_i_moving_window_conditional_escape_type_ii_model", TYPE_II_MODEL
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_moving_window_conditional_escape.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


model = load_type_ii_model()


@dataclass(frozen=True)
class WindowState:
    modulus: int
    seed_residue: int
    multiplier: int
    offset: int
    forms: tuple[object, ...]
    rows: tuple[dict[str, object], ...]


def build_state(
    seed_prime: int, window: int, multiplier: int, offset: int
) -> WindowState | None:
    """Build an exact Type I target-avoidance state."""
    modulus = model.window_modulus(window)
    residue = seed_prime % modulus
    if residue % 24 != 1 or math.gcd(residue, modulus) != 1:
        raise ValueError("seed must give a primitive core residue")
    if multiplier < 1 or not 0 <= offset < multiplier:
        raise ValueError("branch offset must lie in the multiplier range")

    prime_form = model.AffineForm(
        modulus * multiplier,
        modulus * offset + residue,
        "p",
    )
    if math.gcd(prime_form.coefficient, prime_form.constant) != 1:
        return None

    base_coefficient = modulus // 4
    forms = [prime_form]
    rows: list[dict[str, object]] = []
    for j in range(1, window + 1):
        gap = 4 * j - 1
        base_constant = (residue + gap) // 4
        coefficient = base_coefficient * multiplier
        constant = base_coefficient * offset + base_constant
        fixed_factor = math.gcd(coefficient, constant)
        if math.gcd(fixed_factor, gap) != 1:
            return None
        quotient = model.AffineForm(
            coefficient // fixed_factor,
            constant // fixed_factor,
            f"L_{j}",
        )
        if math.gcd(quotient.coefficient, quotient.constant) != 1:
            raise AssertionError("gcd extraction did not make the quotient primitive")

        fixed_residues = model.square_divisor_residues(
            model.prime_factorization(fixed_factor), gap
        )
        quotient_residue = quotient.constant % gap
        full_residues = frozenset(
            left * pow(quotient_residue, exponent, gap) % gap
            for left in fixed_residues
            for exponent in range(3)
        )
        target = (-pow(4, -1, gap)) % gap
        if target in full_residues:
            return None
        forms.append(quotient)
        rows.append(
            {
                "j": j,
                "gap": gap,
                "fixed_factor": fixed_factor,
                "fixed_factorization": model.prime_factorization(fixed_factor),
                "cofactor_residue": quotient_residue,
                "target": target,
                "model_divisor_residue_count": len(full_residues),
                "cofactor_form": quotient.as_json(),
            }
        )

    if len({(form.coefficient, form.constant) for form in forms}) != len(forms):
        raise AssertionError("the affine prime forms must be distinct")
    return WindowState(
        modulus=modulus,
        seed_residue=residue,
        multiplier=multiplier,
        offset=offset,
        forms=tuple(forms),
        rows=tuple(rows),
    )


def find_admissible_branch(
    seed_prime: int, window: int, max_depth: int
) -> tuple[WindowState, tuple[dict[str, int], ...]] | None:
    """Split local covering primes until an admissible escape state is found."""

    def search(
        multiplier: int,
        offset: int,
        depth: int,
        path: tuple[dict[str, int], ...],
    ) -> tuple[WindowState, tuple[dict[str, int], ...]] | None:
        state = build_state(seed_prime, window, multiplier, offset)
        if state is None:
            return None
        obstructions = model.covering_primes(state.forms)
        if not obstructions:
            return state, path
        if depth == max_depth:
            return None
        prime = obstructions[0]
        for residue in range(prime):
            candidate = search(
                multiplier * prime,
                offset + multiplier * residue,
                depth + 1,
                path + ({"prime": prime, "residue": residue},),
            )
            if candidate is not None:
                return candidate
        return None

    return search(1, 0, 0, ())


def fixed_square_divisor_witness(
    factorization: tuple[tuple[int, int], ...], modulus: int, target: int
) -> int | None:
    """Return a fixed square-divisor with the required residue, when present."""
    divisors = [1]
    for prime, exponent in factorization:
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(2 * exponent + 1)
        ]
    return next(
        (divisor for divisor in sorted(divisors) if divisor % modulus == target),
        None,
    )


def next_gap_closure(state: WindowState) -> dict[str, object]:
    """Check every next-gap residue branch in the one-private-prime model."""
    next_j = len(state.rows) + 1
    gap = 4 * next_j - 1
    prime_form = state.forms[0]
    rows: list[dict[str, int | bool | None]] = []
    for residue in range(gap):
        coefficient = prime_form.coefficient * gap
        constant = prime_form.coefficient * residue + prime_form.constant
        x_coefficient = coefficient // 4
        x_constant = (constant + gap) // 4
        fixed_factor = math.gcd(x_coefficient, x_constant)
        if math.gcd(fixed_factor, gap) != 1:
            rows.append(
                {
                    "gap_residue": residue,
                    "closed": True,
                    "reason": "nonunit-fixed-factor",
                    "fixed_factor": fixed_factor,
                    "target": None,
                    "fixed_factor_witness": None,
                }
            )
            continue
        factorization = model.prime_factorization(fixed_factor)
        fixed_residues = model.square_divisor_residues(factorization, gap)
        quotient_residue = (x_constant // fixed_factor) % gap
        target = (-pow(4, -1, gap)) % gap
        model_residues = frozenset(
            left * pow(quotient_residue, exponent, gap) % gap
            for left in fixed_residues
            for exponent in range(3)
        )
        closed = target in model_residues
        rows.append(
            {
                "gap_residue": residue,
                "closed": closed,
                "reason": "type-i-target" if closed else "no-model-target",
                "fixed_factor": fixed_factor,
                "target": target,
                "fixed_factor_witness": fixed_square_divisor_witness(
                    factorization, gap, target
                ),
            }
        )
    return {
        "next_window_j": next_j,
        "gap": gap,
        "all_residue_classes_closed": all(row["closed"] for row in rows),
        "rows": rows,
    }


def run_audit(seed_prime: int, window: int, max_depth: int) -> dict[str, object]:
    """Return one admissible conditional Type I escape, when found."""
    result = find_admissible_branch(seed_prime, window, max_depth)
    if result is None:
        return {
            "arithmetic": (
                "exact forced-factor extraction, complete Type I square-divisor "
                "residue sets, and exact local admissibility checks"
            ),
            "scope_note": (
                "No branch was found within the stated split depth. This is not "
                "a Type I coverage theorem."
            ),
            "seed_prime": seed_prime,
            "window_j": window,
            "max_split_depth": max_depth,
            "conditional_escape": None,
        }

    state, path = result
    if model.covering_primes(state.forms):
        raise AssertionError("reported branch must be admissible")
    return {
        "arithmetic": (
            "exact forced-factor extraction, complete Type I square-divisor "
            "residue sets, and exact local admissibility checks"
        ),
        "scope_note": (
            "Conditional statement only. Dickson's prime-tuples conjecture or "
            "Schinzel's Hypothesis H for the displayed affine forms is required "
            "to obtain infinitely many actual primes."
        ),
        "seed_prime": seed_prime,
        "window_j": window,
        "max_split_depth": max_depth,
        "conditional_escape": {
            "window_gap_modulus": state.modulus,
            "seed_residue": state.seed_residue,
            "parameterization": (
                "p=(Q*multiplier)k+(Q*offset+seed_residue), "
                "x_j=fixed_factor_j*L_j(k)"
            ),
            "multiplier": state.multiplier,
            "offset": state.offset,
            "branch_path": path,
            "covering_primes": (),
            "forms": [form.as_json() for form in state.forms],
            "rows": list(state.rows),
        },
        "one_private_prime_closure": next_gap_closure(state),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-prime", type=int, default=21_169)
    parser.add_argument("--window", type=int, default=8)
    parser.add_argument("--max-depth", type=int, default=8)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.seed_prime, args.window, args.max_depth)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
