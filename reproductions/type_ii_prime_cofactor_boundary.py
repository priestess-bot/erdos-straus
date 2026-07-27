#!/usr/bin/env python3
"""Test the one-prime-private-cofactor model for a canonical Type II fan.

Fix p = Q*n+r, where Q is the lcm of 24 and the ray moduli.  For every
shift s, the fixed divisor D_s=gcd(Q,r+4s) divides p+4s, leaving one affine
cofactor L_s(n).  This script asks whether all rays can fail while p and all
L_s are prime.  It checks the latter by the exact admissibility criterion for
a finite family of linear forms.

Failure of this simplified model is not a Type II coverage theorem: actual
common misses can have several private prime factors.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from dataclasses import dataclass
from functools import cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "type-ii-prime-cofactor-boundary-results.json"
CANONICAL_SCRIPT = ROOT / "reproductions" / "type_ii_canonical_ray.py"


def load_canonical_script():
    spec = importlib.util.spec_from_file_location(
        "type_ii_canonical_ray", CANONICAL_SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_canonical_ray.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


canonical = load_canonical_script()
residue = canonical.residue_structure


@cache
def prime_factors(value: int) -> tuple[tuple[int, int], ...]:
    """Factor a small positive integer by trial division."""
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


@cache
def divisor_residues(fixed_factor: int, modulus: int) -> frozenset[int]:
    """Return all divisor residues of a cached fixed factor."""
    return frozenset(
        residue.divisor_residues_from_factorization(
            prime_factors(fixed_factor), modulus
        )
    )


def primes_through(limit: int) -> tuple[int, ...]:
    return tuple(
        value
        for value in range(2, limit + 1)
        if all(value % divisor for divisor in range(2, math.isqrt(value) + 1))
    )


def canonical_fan(base_shift_bound: int) -> tuple[tuple[int, int, int], ...]:
    """Return (shift, a, c) in increasing shift order."""
    if base_shift_bound < 2:
        raise ValueError("base_shift_bound must be at least two")
    return tuple(
        (shift, *canonical.canonical_pair(shift))
        for shift in range(1, base_shift_bound + 1)
    )


def ac_box_fan(ac_bound: int) -> tuple[tuple[int, int, int], ...]:
    """Return every original AC ray in a bounded box, without canonicalizing it.

    Rays with the same shift A^2*C can have distinct moduli 4*A*C.  They must
    remain distinct when testing simultaneous failure of the original box.
    """
    if ac_bound < 1:
        raise ValueError("ac_bound must be positive")
    return tuple(
        (a * a * c, a, c)
        for a in range(1, ac_bound + 1)
        for c in range(1, ac_bound + 1)
    )


def fan_modulus(fan: tuple[tuple[int, int, int], ...]) -> int:
    modulus = 24
    for _, a, c in fan:
        modulus = math.lcm(modulus, 4 * a * c)
    return modulus


def forced_divisor(modulus: int, residue_class: int, shift: int) -> int:
    """The divisor forced in p+4s for p congruent to residue_class mod Q."""
    return math.gcd(modulus, residue_class + 4 * shift)


def ray_safe_with_one_prime_cofactor(
    residue_class: int, modulus: int, shift: int, a: int, c: int
) -> bool:
    """Check whether D_s times one prime cofactor could avoid the ray target."""
    ray_modulus = 4 * a * c
    divisor = forced_divisor(modulus, residue_class, shift)
    if math.gcd(divisor, ray_modulus) != 1:
        raise AssertionError("the forced divisor must be a unit in the ray group")
    forced_residues = divisor_residues(divisor, ray_modulus)
    cofactor_residue = residue_class * pow(divisor, -1, ray_modulus) % ray_modulus
    all_divisor_residues = {
        left * right % ray_modulus
        for left in forced_residues
        for right in (1, cofactor_residue)
    }
    return ray_modulus - 1 not in all_divisor_residues


def affine_forms(
    residue_class: int, modulus: int, fan: tuple[tuple[int, int, int], ...]
) -> tuple[tuple[int, int, str], ...]:
    """Return p and every forced-divisor quotient as affine forms in n."""
    forms = [(modulus, residue_class, "p")]
    for shift, _, _ in fan:
        divisor = forced_divisor(modulus, residue_class, shift)
        forms.append(
            (
                modulus // divisor,
                (residue_class + 4 * shift) // divisor,
                f"s={shift}",
            )
        )
    return tuple(forms)


@dataclass(frozen=True)
class RecursiveRayState:
    """Affine prime forms and fixed factors after recursive local stripping."""

    p_coefficient: int
    p_constant: int
    fixed_factors: tuple[int, ...]
    quotient_coefficients: tuple[int, ...]
    quotient_constants: tuple[int, ...]


def initial_recursive_state(
    residue_class: int, modulus: int, fan: tuple[tuple[int, int, int], ...]
) -> RecursiveRayState:
    """Encode the one-private-cofactor model as a recursive factor state."""
    divisors = tuple(
        forced_divisor(modulus, residue_class, shift) for shift, _, _ in fan
    )
    return RecursiveRayState(
        p_coefficient=modulus,
        p_constant=residue_class,
        fixed_factors=divisors,
        quotient_coefficients=tuple(modulus // divisor for divisor in divisors),
        quotient_constants=tuple(
            (residue_class + 4 * shift) // divisor
            for (shift, _, _), divisor in zip(fan, divisors)
        ),
    )


def recursive_state_forms(
    state: RecursiveRayState, fan: tuple[tuple[int, int, int], ...]
) -> tuple[tuple[int, int, str], ...]:
    """Return the target-prime form and all remaining quotient forms."""
    return (
        (state.p_coefficient, state.p_constant, "p"),
        *(
            (coefficient, constant, f"s={shift}")
            for (shift, _, _), coefficient, constant in zip(
                fan, state.quotient_coefficients, state.quotient_constants
            )
        ),
    )


def recursive_state_is_ray_safe(
    state: RecursiveRayState, fan: tuple[tuple[int, int, int], ...]
) -> bool:
    """Check every ray after treating each residual quotient as one prime."""
    for (_, a, c), fixed_factor in zip(fan, state.fixed_factors):
        ray_modulus = 4 * a * c
        if state.p_coefficient % ray_modulus != 0:
            raise AssertionError("target prime coefficient must retain every ray modulus")
        if math.gcd(fixed_factor, ray_modulus) != 1:
            return False
        fixed_residues = divisor_residues(fixed_factor, ray_modulus)
        quotient_residue = (
            state.p_constant * pow(fixed_factor, -1, ray_modulus) % ray_modulus
        )
        all_divisor_residues = {
            left * right % ray_modulus
            for left in fixed_residues
            for right in (1, quotient_residue)
        }
        if ray_modulus - 1 in all_divisor_residues:
            return False
    return True


def recursive_state_transition(
    state: RecursiveRayState,
    branch_prime: int,
    branch: int,
    fan: tuple[tuple[int, int, int], ...],
) -> RecursiveRayState | None:
    """Substitute the current parameter by q*t+b and strip all forced q powers."""
    if branch_prime not in primes_through(branch_prime):
        raise ValueError("branch_prime must be prime")
    if not 0 <= branch < branch_prime:
        raise ValueError("branch must be a residue modulo branch_prime")
    p_constant = state.p_coefficient * branch + state.p_constant
    # A large target prime cannot remain in a branch identically divisible by q.
    if p_constant % branch_prime == 0:
        return None
    fixed_factors: list[int] = []
    quotient_coefficients: list[int] = []
    quotient_constants: list[int] = []
    for fixed_factor, coefficient, constant in zip(
        state.fixed_factors,
        state.quotient_coefficients,
        state.quotient_constants,
    ):
        coefficient = branch_prime * coefficient
        constant = coefficient // branch_prime * branch + constant
        extra_prime_power = 0
        while coefficient % branch_prime == 0 and constant % branch_prime == 0:
            coefficient //= branch_prime
            constant //= branch_prime
            extra_prime_power += 1
        fixed_factors.append(fixed_factor * branch_prime**extra_prime_power)
        quotient_coefficients.append(coefficient)
        quotient_constants.append(constant)
    result = RecursiveRayState(
        p_coefficient=branch_prime * state.p_coefficient,
        p_constant=p_constant,
        fixed_factors=tuple(fixed_factors),
        quotient_coefficients=tuple(quotient_coefficients),
        quotient_constants=tuple(quotient_constants),
    )
    return result if recursive_state_is_ray_safe(result, fan) else None


def run_recursive_covering_state_audit(
    fan: tuple[tuple[int, int, int], ...],
    initial_prime: int,
    recursive_steps: int,
    root_start: int = 0,
    root_stop: int | None = None,
) -> dict[str, object]:
    """Explore a deterministic local-cover recursion from one universal root prime.

    The first step uses initial_prime, which must cover every retained root
    state. Later steps use the smallest covering prime of each state. Selecting
    one covering prime is exhaustive because every parameter value is covered
    by that prime; branches in which the target form is divisible by it are
    discarded as incapable of yielding arbitrarily large target primes.
    """
    if recursive_steps < 1:
        raise ValueError("recursive_steps must be positive")
    if root_start < 0:
        raise ValueError("root_start must be nonnegative")
    modulus = fan_modulus(fan)
    roots = [
        initial_recursive_state(residue_class, modulus, fan)
        for residue_class in range(1, modulus)
        if residue_class % 24 == 1
        and math.gcd(residue_class, modulus) == 1
        and all(
            ray_safe_with_one_prime_cofactor(
                residue_class, modulus, shift, a, c
            )
            for shift, a, c in fan
        )
    ]
    if any(
        initial_prime not in covering_primes(recursive_state_forms(state, fan))
        for state in roots
    ):
        raise ValueError("initial_prime must cover every one-prime-safe root state")
    total_root_count = len(roots)
    roots = roots[root_start:root_stop]
    active = roots
    levels: list[dict[str, object]] = []
    escaped_state_count = 0
    for step in range(1, recursive_steps + 1):
        next_active: list[RecursiveRayState] = []
        selected_prime_histogram: dict[int, int] = {}
        expanded_branch_count = 0
        target_prime_rejection_count = 0
        ray_safe_branch_count = 0
        for state in active:
            covers = covering_primes(recursive_state_forms(state, fan))
            if not covers:
                escaped_state_count += 1
                continue
            branch_prime = initial_prime if step == 1 else min(covers)
            if branch_prime not in covers:
                raise AssertionError("selected prime must cover the current state")
            selected_prime_histogram[branch_prime] = (
                selected_prime_histogram.get(branch_prime, 0) + 1
            )
            for branch in range(branch_prime):
                expanded_branch_count += 1
                p_constant = state.p_coefficient * branch + state.p_constant
                if p_constant % branch_prime == 0:
                    target_prime_rejection_count += 1
                    continue
                successor = recursive_state_transition(
                    state, branch_prime, branch, fan
                )
                if successor is not None:
                    ray_safe_branch_count += 1
                    next_active.append(successor)
        levels.append(
            {
                "step": step,
                "input_state_count": len(active),
                "selected_prime_histogram": dict(sorted(selected_prime_histogram.items())),
                "expanded_branch_count": expanded_branch_count,
                "target_prime_rejection_count": target_prime_rejection_count,
                "ray_safe_branch_count": ray_safe_branch_count,
            }
        )
        active = next_active
    terminal_admissible_state_count = sum(
        not covering_primes(recursive_state_forms(state, fan)) for state in active
    ) + escaped_state_count
    return {
        "initial_prime": initial_prime,
        "recursive_steps": recursive_steps,
        "one_prime_safe_root_count": total_root_count,
        "root_slice_start": root_start,
        "root_slice_stop": root_start + len(roots),
        "selected_root_count": len(roots),
        "levels": levels,
        "terminal_ray_safe_state_count": len(active),
        "terminal_admissible_state_count": terminal_admissible_state_count,
    }


def first_recursive_admissible_witness(
    fan: tuple[tuple[int, int, int], ...],
    initial_prime: int,
    recursive_steps: int,
    root_start: int = 0,
    root_stop: int | None = None,
) -> dict[str, object] | None:
    """Return one ray-safe, locally admissible terminal state with its history."""
    if recursive_steps < 1:
        raise ValueError("recursive_steps must be positive")
    modulus = fan_modulus(fan)
    roots = [
        initial_recursive_state(residue_class, modulus, fan)
        for residue_class in range(1, modulus)
        if residue_class % 24 == 1
        and math.gcd(residue_class, modulus) == 1
        and all(
            ray_safe_with_one_prime_cofactor(
                residue_class, modulus, shift, a, c
            )
            for shift, a, c in fan
        )
    ]
    if any(
        initial_prime not in covering_primes(recursive_state_forms(state, fan))
        for state in roots
    ):
        raise ValueError("initial_prime must cover every one-prime-safe root state")
    active = [
        (state, state.p_constant, tuple())
        for state in roots[root_start:root_stop]
    ]
    for step in range(1, recursive_steps + 1):
        next_active: list[
            tuple[RecursiveRayState, int, tuple[tuple[int, int], ...]]
        ] = []
        for state, root_residue, history in active:
            covers = covering_primes(recursive_state_forms(state, fan))
            if not covers:
                continue
            branch_prime = initial_prime if step == 1 else min(covers)
            for branch in range(branch_prime):
                p_constant = state.p_coefficient * branch + state.p_constant
                if p_constant % branch_prime == 0:
                    continue
                successor = recursive_state_transition(
                    state, branch_prime, branch, fan
                )
                if successor is None:
                    continue
                successor_history = history + ((branch_prime, branch),)
                if step == recursive_steps:
                    if not covering_primes(recursive_state_forms(successor, fan)):
                        return {
                            "initial_residue_class": root_residue,
                            "branch_history": [
                                {"prime": prime, "residue": residue_class}
                                for prime, residue_class in successor_history
                            ],
                            "target_prime_form": {
                                "coefficient": successor.p_coefficient,
                                "constant": successor.p_constant,
                            },
                            "ray_states": [
                                {
                                    "shift": shift,
                                    "a": a,
                                    "c": c,
                                    "fixed_factor": fixed_factor,
                                    "quotient_coefficient": coefficient,
                                    "quotient_constant": constant,
                                }
                                for (shift, a, c), fixed_factor, coefficient, constant in zip(
                                    fan,
                                    successor.fixed_factors,
                                    successor.quotient_coefficients,
                                    successor.quotient_constants,
                                )
                            ],
                            "covering_primes": [],
                        }
                else:
                    next_active.append(
                        (successor, root_residue, successor_history)
                    )
        active = next_active
    return None


def prime_stripped_branch(
    residue_class: int,
    branch: int,
    prime: int,
    modulus: int,
    fan: tuple[tuple[int, int, int], ...],
) -> tuple[tuple[tuple[int, int, str], ...], tuple[dict[str, int], ...]] | None:
    """Strip every power of a chosen prime after a residue-class substitution.

    A nonempty return means that replacing every remaining quotient by one
    prime still avoids every ray.  The returned affine forms are those prime
    quotients together with the target-prime form.
    """
    if prime not in primes_through(prime):
        raise ValueError("prime must be prime")
    if not 0 <= branch < prime:
        raise ValueError("branch must be a residue modulo prime")
    forms = [(prime * modulus, modulus * branch + residue_class, "p")]
    factors: list[dict[str, int]] = []
    for shift, a, c in fan:
        ray_modulus = 4 * a * c
        divisor = forced_divisor(modulus, residue_class, shift)
        coefficient = prime * (modulus // divisor)
        constant = (modulus // divisor) * branch + (
            residue_class + 4 * shift
        ) // divisor
        extra_prime_power = 0
        while coefficient % prime == 0 and constant % prime == 0:
            coefficient //= prime
            constant //= prime
            extra_prime_power += 1
        fixed_factor = divisor * prime**extra_prime_power
        fixed_residues = divisor_residues(fixed_factor, ray_modulus)
        quotient_residue = (
            residue_class * pow(fixed_factor, -1, ray_modulus) % ray_modulus
        )
        all_divisor_residues = {
            left * right % ray_modulus
            for left in fixed_residues
            for right in (1, quotient_residue)
        }
        if ray_modulus - 1 in all_divisor_residues:
            return None
        forms.append((coefficient, constant, f"s={shift}"))
        factors.append(
            {
                "shift": shift,
                "forced_divisor": divisor,
                "extra_prime_power": extra_prime_power,
                "fixed_factor": fixed_factor,
            }
        )
    return tuple(forms), tuple(factors)


def second_level_branch(
    residue_class: int,
    branch: int,
    modulus: int,
    fan: tuple[tuple[int, int, int], ...],
) -> tuple[tuple[tuple[int, int, str], ...], tuple[dict[str, int], ...]] | None:
    """Compatibility wrapper for the historical mod-three second-level audit."""
    return prime_stripped_branch(residue_class, branch, 3, modulus, fan)


def covering_primes(
    forms: tuple[tuple[int, int, str], ...]
) -> tuple[int, ...]:
    """Return primes that divide at least one form for every n modulo q."""
    result: set[int] = {
        prime
        for coefficient, constant, _ in forms
        for prime, _ in prime_factors(math.gcd(coefficient, constant))
    }
    if result:
        return tuple(sorted(result))
    # A union of len(forms) nonzero roots cannot cover a larger prime field.
    for prime in primes_through(len(forms)):
        roots: set[int] = set()
        identically_zero = False
        for coefficient, constant, _ in forms:
            if coefficient % prime == 0:
                if constant % prime == 0:
                    identically_zero = True
                    break
                continue
            roots.add((-constant * pow(coefficient, -1, prime)) % prime)
        if identically_zero or len(roots) == prime:
            result.add(prime)
    return tuple(sorted(result))


def run_covering_prime_branch_audit(
    fan: tuple[tuple[int, int, int], ...],
    prime: int,
) -> dict[str, int]:
    """Audit one recursive step at a specified first-level covering prime.

    Only residue classes for which the selected prime covers the first-level
    form family are expanded. Each branch strips its forced prime power and
    then requires every residual quotient to be prime, so this is an exact
    bounded-complexity model rather than a Type II coverage test.
    """
    if prime not in primes_through(prime):
        raise ValueError("prime must be prime")
    modulus = fan_modulus(fan)
    core_residues = [
        residue_class
        for residue_class in range(1, modulus)
        if residue_class % 24 == 1 and math.gcd(residue_class, modulus) == 1
    ]
    safe_residues = [
        residue_class
        for residue_class in core_residues
        if all(
            ray_safe_with_one_prime_cofactor(
                residue_class, modulus, shift, a, c
            )
            for shift, a, c in fan
        )
    ]
    covered_residues = [
        residue_class
        for residue_class in safe_residues
        if prime in covering_primes(affine_forms(residue_class, modulus, fan))
    ]
    ray_safe_branch_count = 0
    admissible_branch_count = 0
    for residue_class in covered_residues:
        for branch in range(prime):
            result = prime_stripped_branch(
                residue_class, branch, prime, modulus, fan
            )
            if result is None:
                continue
            ray_safe_branch_count += 1
            forms, _ = result
            if not covering_primes(forms):
                admissible_branch_count += 1
    return {
        "prime": prime,
        "covered_residue_count": len(covered_residues),
        "expanded_branch_count": len(covered_residues) * prime,
        "ray_safe_branch_count": ray_safe_branch_count,
        "admissible_branch_count": admissible_branch_count,
    }


def run_fan_audit(
    fan: tuple[tuple[int, int, int], ...], fan_description: str
) -> dict[str, object]:
    """Run the exact one-private-cofactor audit for an explicitly supplied fan."""
    if not fan:
        raise ValueError("fan must be nonempty")
    modulus = fan_modulus(fan)
    core_residues = [
        residue_class
        for residue_class in range(1, modulus)
        if residue_class % 24 == 1 and math.gcd(residue_class, modulus) == 1
    ]
    safe_residues = [
        residue_class
        for residue_class in core_residues
        if all(
            ray_safe_with_one_prime_cofactor(
                residue_class, modulus, shift, a, c
            )
            for shift, a, c in fan
        )
    ]
    obstruction_histogram: dict[int, int] = {}
    admissible_one_prime_safe_residue_count = 0
    samples: list[dict[str, object]] = []
    second_level_branches: list[dict[str, object]] = []
    second_level_admissible_count = 0
    second_level_branch_by_residue: dict[int, int] = {}
    for residue_class in safe_residues:
        forms = affine_forms(residue_class, modulus, fan)
        obstructions = covering_primes(forms)
        if not obstructions:
            admissible_one_prime_safe_residue_count += 1
        for prime in obstructions:
            obstruction_histogram[prime] = obstruction_histogram.get(prime, 0) + 1
        if len(samples) < 10:
            samples.append(
                {
                    "residue_class": residue_class,
                    "covering_primes": obstructions,
                    "forms": [
                        {"coefficient": coefficient, "constant": constant, "label": label}
                        for coefficient, constant, label in forms
                    ],
                }
            )
        for branch in range(3):
            second_level = second_level_branch(
                residue_class, branch, modulus, fan
            )
            if second_level is None:
                continue
            forms, factors = second_level
            obstructions = covering_primes(forms)
            if not obstructions:
                second_level_admissible_count += 1
                second_level_branch_by_residue[residue_class] = branch
                if len(second_level_branches) < 10:
                    second_level_branches.append(
                        {
                            "residue_class": residue_class,
                            "n_mod_3": branch,
                            "fixed_factors": factors,
                            "forms": [
                                {
                                    "coefficient": coefficient,
                                    "constant": constant,
                                    "label": label,
                                }
                                for coefficient, constant, label in forms
                            ],
                        }
                    )
    return {
        "arithmetic": (
            "exact residue enumeration and finite-field admissibility checks for "
            "the p and forced-divisor quotient linear forms"
        ),
        "scope_note": (
            "This excludes only the model in which every shifted integer has its "
            "forced divisor times one prime cofactor. It is not a coverage proof."
        ),
        "fan_description": fan_description,
        "canonical_fan": [
            {"shift": shift, "a": a, "c": c, "modulus": 4 * a * c}
            for shift, a, c in fan
        ],
        "combined_modulus": modulus,
        "core_residue_count": len(core_residues),
        "one_prime_safe_residue_count": len(safe_residues),
        "admissible_one_prime_safe_residue_count": (
            admissible_one_prime_safe_residue_count
        ),
        "covering_prime_histogram": dict(sorted(obstruction_histogram.items())),
        "second_level_safe_branch_count": second_level_admissible_count,
        "second_level_safe_residue_count": len(second_level_branch_by_residue),
        "second_level_samples": second_level_branches,
        "samples": samples,
    }


def run_audit(base_shift_bound: int) -> dict[str, object]:
    """Run the historical canonical consecutive-shift audit."""
    result = run_fan_audit(
        canonical_fan(base_shift_bound),
        f"canonical shifts 1 through {base_shift_bound}",
    )
    result["base_shift_bound"] = base_shift_bound
    return result


def run_ac_box_audit(ac_bound: int) -> dict[str, object]:
    """Run the same exact model for every original ray A,C<=ac_bound."""
    result = run_fan_audit(ac_box_fan(ac_bound), f"original AC box A,C<={ac_bound}")
    result["ac_bound"] = ac_bound
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-shift-bound", type=int, default=14)
    parser.add_argument(
        "--ac-bound",
        type=int,
        help="audit every original ray A,C in the stated box instead of canonical shifts",
    )
    parser.add_argument(
        "--recursive-covering-prime",
        action="append",
        type=int,
        help="also audit one forced-factor recursive layer for this covering prime",
    )
    parser.add_argument(
        "--recursive-depth",
        type=int,
        help="run deterministic recursive cover transitions to this depth",
    )
    parser.add_argument(
        "--root-start",
        type=int,
        default=0,
        help="start index in the one-prime-safe root-state list",
    )
    parser.add_argument(
        "--root-stop",
        type=int,
        help="exclusive stop index in the one-prime-safe root-state list",
    )
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    fan = (
        ac_box_fan(args.ac_bound)
        if args.ac_bound is not None
        else canonical_fan(args.base_shift_bound)
    )
    payload = (
        run_ac_box_audit(args.ac_bound)
        if args.ac_bound is not None
        else run_audit(args.base_shift_bound)
    )
    if args.recursive_covering_prime:
        payload["recursive_covering_prime_audits"] = [
            run_covering_prime_branch_audit(fan, prime)
            for prime in args.recursive_covering_prime
        ]
    if args.recursive_depth is not None:
        if not args.recursive_covering_prime or len(args.recursive_covering_prime) != 1:
            parser.error(
                "--recursive-depth requires exactly one --recursive-covering-prime"
            )
        initial_prime = args.recursive_covering_prime[0]
        payload["recursive_covering_state_audit"] = (
            run_recursive_covering_state_audit(
                fan,
                initial_prime,
                args.recursive_depth,
                args.root_start,
                args.root_stop,
            )
        )
        payload["recursive_admissible_witness"] = first_recursive_admissible_witness(
            fan,
            initial_prime,
            args.recursive_depth,
            args.root_start,
            args.root_stop,
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
