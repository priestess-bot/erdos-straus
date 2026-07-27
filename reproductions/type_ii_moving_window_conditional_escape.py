#!/usr/bin/env python3
"""Find a Dickson-admissible one-private-prime escape for a Type II window.

Write p=Q*n+r, where Q is the lcm of 24 and the moving-window gaps.  After
restricting n to an arithmetic progression, every x_j=(p+4j-1)/4 has a
fixed factor E_j and one primitive affine quotient L_j(k).  This script
checks whether the model x_j=E_j L_j(k), with every L_j(k) prime, misses the
exact Type II divisor target at every window position.

An admissible result is conditional evidence only: Dickson's conjecture (or
Schinzel's Hypothesis H for the displayed linear forms) is additionally
needed to obtain infinitely many prime values.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT
    / "reproductions"
    / "type-ii-moving-window-conditional-escape-p153633769-j37-results.json"
)


def prime_factorization(value: int) -> tuple[tuple[int, int], ...]:
    """Factor a small forced divisor by trial division."""
    if value < 1:
        raise ValueError("value must be positive")
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            exponent = 0
            while value % divisor == 0:
                value //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return tuple(factors)


def primes_through(limit: int) -> tuple[int, ...]:
    return tuple(
        candidate
        for candidate in range(2, limit + 1)
        if all(
            candidate % divisor
            for divisor in range(2, math.isqrt(candidate) + 1)
        )
    )


def window_modulus(window: int) -> int:
    """Return lcm(24, 3, 7, ..., 4*window-1)."""
    if window < 1:
        raise ValueError("window must be positive")
    modulus = 24
    for j in range(1, window + 1):
        modulus = math.lcm(modulus, 4 * j - 1)
    return modulus


def square_divisor_residues(
    factorization: tuple[tuple[int, int], ...], modulus: int
) -> frozenset[int]:
    residues = {1}
    for prime, exponent in factorization:
        if math.gcd(prime, modulus) != 1:
            raise ValueError("forced factor is not a unit modulo the gap")
        residues = {
            residue * pow(prime, power, modulus) % modulus
            for residue in residues
            for power in range(2 * exponent + 1)
        }
    return frozenset(residues)


@dataclass(frozen=True)
class AffineForm:
    coefficient: int
    constant: int
    label: str

    def as_json(self) -> dict[str, int | str]:
        return {
            "coefficient": self.coefficient,
            "constant": self.constant,
            "label": self.label,
        }


@dataclass(frozen=True)
class WindowState:
    modulus: int
    seed_residue: int
    multiplier: int
    offset: int
    forms: tuple[AffineForm, ...]
    rows: tuple[dict[str, object], ...]


def build_state(
    seed_prime: int, window: int, multiplier: int, offset: int
) -> WindowState | None:
    """Build the exact one-private-prime state for n=multiplier*k+offset."""
    modulus = window_modulus(window)
    residue = seed_prime % modulus
    if residue % 24 != 1 or math.gcd(residue, modulus) != 1:
        raise ValueError("seed must give a primitive core residue")
    if multiplier < 1 or not 0 <= offset < multiplier:
        raise ValueError("branch offset must lie in [0, multiplier)")

    prime_form = AffineForm(
        modulus * multiplier,
        modulus * offset + residue,
        "p",
    )
    if math.gcd(prime_form.coefficient, prime_form.constant) != 1:
        return None

    base_coefficient = modulus // 4
    rows: list[dict[str, object]] = []
    forms = [prime_form]
    for j in range(1, window + 1):
        gap = 4 * j - 1
        base_constant = (residue + gap) // 4
        coefficient = base_coefficient * multiplier
        constant = base_coefficient * offset + base_constant
        fixed_factor = math.gcd(coefficient, constant)
        quotient = AffineForm(
            coefficient // fixed_factor,
            constant // fixed_factor,
            f"L_{j}",
        )
        if math.gcd(quotient.coefficient, quotient.constant) != 1:
            raise AssertionError("gcd extraction did not make the quotient primitive")
        if math.gcd(fixed_factor, gap) != 1:
            # Then the prime form would be imprimitive at this gap as well.
            return None

        fixed_residues = square_divisor_residues(
            prime_factorization(fixed_factor), gap
        )
        quotient_residue = quotient.constant % gap
        full_residues = frozenset(
            left * pow(quotient_residue, exponent, gap) % gap
            for left in fixed_residues
            for exponent in range(3)
        )
        target = (-base_constant) % gap
        if target in full_residues:
            return None
        forms.append(quotient)
        rows.append(
            {
                "j": j,
                "gap": gap,
                "fixed_factor": fixed_factor,
                "fixed_factorization": prime_factorization(fixed_factor),
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


def covering_primes(forms: tuple[AffineForm, ...]) -> tuple[int, ...]:
    """Return the complete set of local prime-tuple obstructions.

    Each form is primitive.  A prime larger than the number of forms cannot
    be covered by their at most one root each, so this finite test is exact.
    """
    result: list[int] = []
    for prime in primes_through(len(forms)):
        roots: set[int] = set()
        for form in forms:
            if form.coefficient % prime == 0:
                if form.constant % prime == 0:
                    raise AssertionError("imprimitive affine form")
                continue
            roots.add(
                (-form.constant * pow(form.coefficient, -1, prime)) % prime
            )
        if len(roots) == prime:
            result.append(prime)
    return tuple(result)


def find_admissible_branch(
    seed_prime: int, window: int, max_depth: int
) -> tuple[WindowState, tuple[dict[str, int], ...]] | None:
    """Split successive covering primes until an admissible model is found."""

    def search(
        multiplier: int,
        offset: int,
        depth: int,
        path: tuple[dict[str, int], ...],
    ) -> tuple[WindowState, tuple[dict[str, int], ...]] | None:
        state = build_state(seed_prime, window, multiplier, offset)
        if state is None:
            return None
        obstructions = covering_primes(state.forms)
        if not obstructions:
            return state, path
        if depth == max_depth:
            return None

        prime = obstructions[0]
        for residue in range(prime):
            child_multiplier = multiplier * prime
            child_offset = offset + multiplier * residue
            candidate = search(
                child_multiplier,
                child_offset,
                depth + 1,
                path + ({"prime": prime, "residue": residue},),
            )
            if candidate is not None:
                return candidate
        return None

    return search(1, 0, 0, ())


def run_audit(seed_prime: int, window: int, max_depth: int) -> dict[str, object]:
    result = find_admissible_branch(seed_prime, window, max_depth)
    if result is None:
        return {
            "arithmetic": (
                "exact forced-factor extraction, complete square-divisor residue "
                "sets, and exact local admissibility checks for affine forms"
            ),
            "scope_note": (
                "No branch was found within the stated split depth. This is not a "
                "Type II coverage theorem."
            ),
            "seed_prime": seed_prime,
            "window_j": window,
            "max_split_depth": max_depth,
            "conditional_escape": None,
        }

    state, path = result
    if covering_primes(state.forms):
        raise AssertionError("reported branch must be admissible")
    return {
        "arithmetic": (
            "exact forced-factor extraction, complete square-divisor residue "
            "sets, and exact local admissibility checks for affine forms"
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
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-prime", type=int, default=153_633_769)
    parser.add_argument("--window", type=int, default=37)
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
