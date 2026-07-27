#!/usr/bin/env python3
"""Extend a conditional one-private-prime moving-window escape state.

Starting from the admissible j<=37 branch in
type_ii_moving_window_conditional_escape.py, this program adds one gap at a
time.  It fixes the new prime-form residue modulo that gap, then recursively
splits every local prime-tuple obstruction.  Every retained state has exact
Type II target avoidance in the one-private-prime model at all positions.

The output remains conditional on Dickson's conjecture or Schinzel's
Hypothesis H.  It is a state-tree audit, not a proof that an escape extends
indefinitely.
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
CONDITIONAL = ROOT / "reproductions" / "type_ii_moving_window_conditional_escape.py"
RESULTS = (
    ROOT
    / "reproductions"
    / "type-ii-moving-window-adaptive-escape-p153633769-j51-results.json"
)


def load_conditional_module():
    spec = importlib.util.spec_from_file_location(
        "type_ii_moving_window_conditional_escape", CONDITIONAL
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_moving_window_conditional_escape.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


conditional = load_conditional_module()


@dataclass(frozen=True)
class State:
    prime_coefficient: int
    prime_constant: int
    window: int
    forms: tuple[object, ...]
    rows: tuple[dict[str, object], ...]


def build_state(prime_coefficient: int, prime_constant: int, window: int) -> State | None:
    """Build a model state for p(k)=prime_coefficient*k+prime_constant."""
    if (
        window < 1
        or prime_coefficient % 4
        or prime_constant % 24 != 1
        or math.gcd(prime_coefficient, prime_constant) != 1
    ):
        return None

    forms = [
        conditional.AffineForm(prime_coefficient, prime_constant, "p")
    ]
    rows: list[dict[str, object]] = []
    x_coefficient = prime_coefficient // 4
    for j in range(1, window + 1):
        gap = 4 * j - 1
        if x_coefficient % gap or (prime_constant + gap) % 4:
            return None
        x_constant = (prime_constant + gap) // 4
        fixed_factor = math.gcd(x_coefficient, x_constant)
        if math.gcd(fixed_factor, gap) != 1:
            return None
        cofactor = conditional.AffineForm(
            x_coefficient // fixed_factor,
            x_constant // fixed_factor,
            f"L_{j}",
        )
        if math.gcd(cofactor.coefficient, cofactor.constant) != 1:
            raise AssertionError("cofactor form must be primitive")

        fixed_residues = conditional.square_divisor_residues(
            conditional.prime_factorization(fixed_factor), gap
        )
        cofactor_residue = cofactor.constant % gap
        target = (-x_constant) % gap
        model_residues = frozenset(
            left * pow(cofactor_residue, exponent, gap) % gap
            for left in fixed_residues
            for exponent in range(3)
        )
        if target in model_residues:
            return None
        forms.append(cofactor)
        rows.append(
            {
                "j": j,
                "gap": gap,
                "fixed_factor": fixed_factor,
                "fixed_factorization": conditional.prime_factorization(
                    fixed_factor
                ),
                "cofactor_residue": cofactor_residue,
                "target": target,
                "model_divisor_residue_count": len(model_residues),
                "cofactor_form": cofactor.as_json(),
            }
        )

    if len({(form.coefficient, form.constant) for form in forms}) != len(forms):
        return None
    return State(
        prime_coefficient=prime_coefficient,
        prime_constant=prime_constant,
        window=window,
        forms=tuple(forms),
        rows=tuple(rows),
    )


def first_model_target(
    prime_coefficient: int, prime_constant: int, window: int
) -> dict[str, int | bool] | None:
    """Locate the first Type II target in the one-private-prime model."""
    if (
        window < 1
        or prime_coefficient % 4
        or prime_constant % 24 != 1
        or math.gcd(prime_coefficient, prime_constant) != 1
    ):
        return None

    x_coefficient = prime_coefficient // 4
    for j in range(1, window + 1):
        gap = 4 * j - 1
        if x_coefficient % gap or (prime_constant + gap) % 4:
            return None
        x_constant = (prime_constant + gap) // 4
        fixed_factor = math.gcd(x_coefficient, x_constant)
        if math.gcd(fixed_factor, gap) != 1:
            return None
        cofactor_coefficient = x_coefficient // fixed_factor
        cofactor_constant = x_constant // fixed_factor
        if math.gcd(cofactor_coefficient, cofactor_constant) != 1:
            raise AssertionError("cofactor form must be primitive")

        fixed_residues = conditional.square_divisor_residues(
            conditional.prime_factorization(fixed_factor), gap
        )
        cofactor_residue = cofactor_constant % gap
        target = (-x_constant) % gap
        triggering_exponent = next(
            (
                exponent
                for exponent in range(3)
                if any(
                    residue * pow(cofactor_residue, exponent, gap) % gap
                    == target
                    for residue in fixed_residues
                )
            ),
            None,
        )
        if triggering_exponent is not None:
            return {
                "j": j,
                "gap": gap,
                "fixed_factor": fixed_factor,
                "target": target,
                "cofactor_residue": cofactor_residue,
                "cofactor_exponent": triggering_exponent,
                "fixed_factor_only": triggering_exponent == 0,
            }
    return None


def resolve_covering(
    prime_coefficient: int,
    prime_constant: int,
    window: int,
    max_depth: int,
    path: tuple[dict[str, int], ...] = (),
) -> tuple[State, tuple[dict[str, int], ...]] | None:
    """Split local covering primes until an admissible state is reached."""
    state = build_state(prime_coefficient, prime_constant, window)
    if state is None:
        return None
    obstructions = conditional.covering_primes(state.forms)
    if not obstructions:
        return state, path
    if len(path) >= max_depth:
        return None

    prime = obstructions[0]
    for residue in range(prime):
        result = resolve_covering(
            prime_coefficient * prime,
            prime_coefficient * residue + prime_constant,
            window,
            max_depth,
            path + ({"prime": prime, "residue": residue},),
        )
        if result is not None:
            return result
    return None


def run_audit(seed_prime: int, target_window: int, max_depth: int) -> dict[str, object]:
    if target_window < 37:
        raise ValueError("target_window must be at least 37")
    base_modulus = conditional.window_modulus(37)
    state_result = resolve_covering(16 * base_modulus, seed_prime, 37, max_depth)
    if state_result is None:
        raise AssertionError("the documented j=37 starting state must be admissible")
    state, _ = state_result
    extensions: list[dict[str, object]] = []

    for window in range(38, target_window + 1):
        gap = 4 * window - 1
        chosen = None
        for gap_residue in range(gap):
            result = resolve_covering(
                state.prime_coefficient * gap,
                state.prime_coefficient * gap_residue + state.prime_constant,
                window,
                max_depth,
            )
            if result is None:
                continue
            chosen = gap_residue, result
            break
        if chosen is None:
            closure_rows: list[dict[str, int | bool | str]] = []
            for gap_residue in range(gap):
                coefficient = state.prime_coefficient * gap
                constant = (
                    state.prime_coefficient * gap_residue
                    + state.prime_constant
                )
                if math.gcd(coefficient, constant) != 1:
                    closure_rows.append(
                        {
                            "gap_residue": gap_residue,
                            "outcome": "imprimitive-prime-form",
                        }
                    )
                    continue
                target = first_model_target(coefficient, constant, window)
                if target is None:
                    closure_rows.append(
                        {
                            "gap_residue": gap_residue,
                            "outcome": "no-model-target",
                        }
                    )
                    continue
                closure_rows.append(
                    {
                        "gap_residue": gap_residue,
                        "outcome": "model-target",
                        **target,
                    }
                )
            all_closed = all(
                row["outcome"] in {"imprimitive-prime-form", "model-target"}
                for row in closure_rows
            )
            return {
                "arithmetic": (
                    "exact forced-factor extraction, complete one-private-prime "
                    "divisor-residue checks, and finite local admissibility tests"
                ),
                "scope_note": (
                    "This deterministic terminal state is closed in the stated "
                    "one-private-prime model."
                    if all_closed
                    else "No extension branch was found with this deterministic "
                    "search and depth bound. It is not a closure theorem."
                ),
                "seed_prime": seed_prime,
                "target_window": target_window,
                "max_split_depth": max_depth,
                "completed_window": state.window,
                "extensions": extensions,
                "one_private_prime_closure": {
                    "next_window_j": window,
                    "gap": gap,
                    "all_residue_classes_closed": all_closed,
                    "rows": closure_rows,
                },
                "conditional_escape": None,
            }

        gap_residue, (state, split_path) = chosen
        extensions.append(
            {
                "window_j": window,
                "gap": gap,
                "gap_residue": gap_residue,
                "covering_split_path": split_path,
            }
        )

    if conditional.covering_primes(state.forms):
        raise AssertionError("reported terminal state must be admissible")
    return {
        "arithmetic": (
            "exact forced-factor extraction, complete one-private-prime "
            "divisor-residue checks, and finite local admissibility tests"
        ),
        "scope_note": (
            "Conditional statement only. Dickson's prime-tuples conjecture or "
            "Schinzel's Hypothesis H for the displayed forms is required to "
            "obtain infinitely many prime values."
        ),
        "seed_prime": seed_prime,
        "target_window": target_window,
        "max_split_depth": max_depth,
        "completed_window": state.window,
        "extensions": extensions,
        "one_private_prime_closure": None,
        "conditional_escape": {
            "parameterization": "p(k)=A*k+B, x_j(k)=E_j*L_j(k)",
            "prime_form": state.forms[0].as_json(),
            "covering_primes": (),
            "forms": [form.as_json() for form in state.forms],
            "rows": list(state.rows),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-prime", type=int, default=153_633_769)
    parser.add_argument("--target-window", type=int, default=51)
    parser.add_argument("--max-depth", type=int, default=8)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.seed_prime, args.target_window, args.max_depth)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
