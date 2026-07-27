#!/usr/bin/env python3
"""Extend a Type I one-private-prime escape until the next gap closes it.

Starting from an eight-gap conditional escape, add one moving-window gap at
a time. Every retained state has exact Type I target avoidance in the
one-private-prime model and is locally admissible for simultaneous primality.
The terminal step checks every residue class at the new gap.
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
BASE = ROOT / "reproductions" / "type_i_moving_window_conditional_escape.py"
RESULTS = (
    ROOT / "reproductions" / "type-i-moving-window-adaptive-escape-p709921-j24-results.json"
)


def load_base():
    spec = importlib.util.spec_from_file_location(
        "type_i_moving_window_adaptive_escape_base", BASE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_i_moving_window_conditional_escape.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_base()
model = base.model


@dataclass(frozen=True)
class AffineState:
    prime_coefficient: int
    prime_constant: int
    window: int
    forms: tuple[object, ...]
    rows: tuple[dict[str, object], ...]


def build_state(
    prime_coefficient: int, prime_constant: int, window: int
) -> AffineState | None:
    """Build a locally testable Type I target-avoidance state."""
    if (
        window < 1
        or prime_coefficient % 4
        or prime_constant % 24 != 1
        or math.gcd(prime_coefficient, prime_constant) != 1
    ):
        return None
    x_coefficient = prime_coefficient // 4
    forms = [model.AffineForm(prime_coefficient, prime_constant, "p")]
    rows: list[dict[str, object]] = []
    for j in range(1, window + 1):
        gap = 4 * j - 1
        if x_coefficient % gap or (prime_constant + gap) % 4:
            return None
        x_constant = (prime_constant + gap) // 4
        fixed_factor = math.gcd(x_coefficient, x_constant)
        if math.gcd(fixed_factor, gap) != 1:
            return None
        cofactor = model.AffineForm(
            x_coefficient // fixed_factor,
            x_constant // fixed_factor,
            f"L_{j}",
        )
        if math.gcd(cofactor.coefficient, cofactor.constant) != 1:
            raise AssertionError("gcd extraction did not make the quotient primitive")
        fixed_residues = model.square_divisor_residues(
            model.prime_factorization(fixed_factor), gap
        )
        cofactor_residue = cofactor.constant % gap
        target = (-pow(4, -1, gap)) % gap
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
                "cofactor_residue": cofactor_residue,
                "target": target,
                "model_divisor_residue_count": len(model_residues),
                "cofactor_form": cofactor.as_json(),
            }
        )
    if len({(form.coefficient, form.constant) for form in forms}) != len(forms):
        return None
    return AffineState(
        prime_coefficient=prime_coefficient,
        prime_constant=prime_constant,
        window=window,
        forms=tuple(forms),
        rows=tuple(rows),
    )


def resolve_branch(
    prime_coefficient: int,
    prime_constant: int,
    window: int,
    max_depth: int,
    path: tuple[dict[str, int], ...] = (),
) -> tuple[AffineState, tuple[dict[str, int], ...]] | None:
    """Split every local prime-tuple obstruction until an admissible state."""
    state = build_state(prime_coefficient, prime_constant, window)
    if state is None:
        return None
    obstructions = model.covering_primes(state.forms)
    if not obstructions:
        return state, path
    if max_depth == 0:
        return None
    prime = obstructions[0]
    for residue in range(prime):
        result = resolve_branch(
            prime_coefficient * prime,
            prime_coefficient * residue + prime_constant,
            window,
            max_depth - 1,
            path + ({"prime": prime, "residue": residue},),
        )
        if result is not None:
            return result
    return None


def next_gap_closure(state: AffineState) -> dict[str, object]:
    """Classify every next-gap residue in the stated one-private-prime model."""
    next_j = state.window + 1
    gap = 4 * next_j - 1
    rows: list[dict[str, object]] = []
    for residue in range(gap):
        prime_coefficient = state.prime_coefficient * gap
        prime_constant = state.prime_coefficient * residue + state.prime_constant
        x_coefficient = prime_coefficient // 4
        x_constant = (prime_constant + gap) // 4
        fixed_factor = math.gcd(x_coefficient, x_constant)
        if math.gcd(fixed_factor, gap) != 1:
            rows.append(
                {
                    "gap_residue": residue,
                    "outcome": "nonunit-fixed-factor",
                    "fixed_factor": fixed_factor,
                    "target": None,
                }
            )
            continue
        fixed_residues = model.square_divisor_residues(
            model.prime_factorization(fixed_factor), gap
        )
        cofactor_residue = (x_constant // fixed_factor) % gap
        target = (-pow(4, -1, gap)) % gap
        model_residues = frozenset(
            left * pow(cofactor_residue, exponent, gap) % gap
            for left in fixed_residues
            for exponent in range(3)
        )
        rows.append(
            {
                "gap_residue": residue,
                "outcome": "type-i-target"
                if target in model_residues
                else "no-model-target",
                "fixed_factor": fixed_factor,
                "cofactor_residue": cofactor_residue,
                "target": target,
            }
        )
    return {
        "next_window_j": next_j,
        "gap": gap,
        "all_residue_classes_closed": all(
            row["outcome"] != "no-model-target" for row in rows
        ),
        "rows": rows,
    }


def run_audit(
    seed_prime: int, target_window: int, max_depth: int
) -> dict[str, object]:
    """Build an adaptive escape chain, stopping on the first terminal gap."""
    if target_window < 8:
        raise ValueError("target_window must be at least 8")
    start = base.run_audit(seed_prime, 8, max_depth)["conditional_escape"]
    if start is None:
        raise ValueError("seed does not produce the required eight-gap state")
    state_result = resolve_branch(
        start["forms"][0]["coefficient"],
        start["forms"][0]["constant"],
        8,
        max_depth,
    )
    if state_result is None:
        raise AssertionError("documented initial state must remain admissible")
    state, _ = state_result
    extensions: list[dict[str, object]] = []

    for window in range(9, target_window + 1):
        gap = 4 * window - 1
        chosen = None
        for residue in range(gap):
            result = resolve_branch(
                state.prime_coefficient * gap,
                state.prime_coefficient * residue + state.prime_constant,
                window,
                max_depth,
                ({"gap": gap, "residue": residue},),
            )
            if result is not None:
                chosen = result
                break
        if chosen is None:
            closure = next_gap_closure(state)
            return {
                "arithmetic": (
                    "exact forced-factor extraction, complete Type I "
                    "one-private-prime square-divisor residue checks, and "
                    "finite local admissibility tests"
                ),
                "scope_note": (
                    "The escape is conditional on Dickson/Schinzel. The terminal "
                    "closure is exact only in the stated one-private-prime model."
                ),
                "seed_prime": seed_prime,
                "target_window": target_window,
                "max_split_depth": max_depth,
                "completed_window": state.window,
                "extensions": extensions,
                "one_private_prime_closure": closure,
                "conditional_escape": {
                    "forms": [form.as_json() for form in state.forms],
                    "rows": list(state.rows),
                    "covering_primes": (),
                },
            }
        state, path = chosen
        extensions.append(
            {
                "window_j": window,
                "gap": gap,
                "path": path,
                "prime_coefficient": state.prime_coefficient,
                "prime_constant": state.prime_constant,
                "new_fixed_factor": state.rows[-1]["fixed_factor"],
            }
        )

    return {
        "arithmetic": (
            "exact forced-factor extraction, complete Type I one-private-prime "
            "square-divisor residue checks, and finite local admissibility tests"
        ),
        "scope_note": (
            "Conditional escape only. No terminal closure was reached inside the "
            "requested window."
        ),
        "seed_prime": seed_prime,
        "target_window": target_window,
        "max_split_depth": max_depth,
        "completed_window": state.window,
        "extensions": extensions,
        "one_private_prime_closure": None,
        "conditional_escape": {
            "forms": [form.as_json() for form in state.forms],
            "rows": list(state.rows),
            "covering_primes": (),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-prime", type=int, default=709_921)
    parser.add_argument("--target-window", type=int, default=24)
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
