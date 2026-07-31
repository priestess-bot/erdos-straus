#!/usr/bin/env python3
"""Certify the short Type I/II selector for nonempty R=47 support masks."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path

import sympy
from sympy.ntheory.modular import crt


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-r47-nonempty-support-short-selector-results.json"
)
MODULUS = 47
OPTIONAL_PRIMES = (5, 13, 31, 43)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def support_progression(support_prime: int) -> tuple[int, int]:
    root = (-pow(MODULUS, -1, support_prime)) % support_prime
    result = crt([24, support_prime], [1, root], check=True)
    if result is None:
        raise AssertionError("support trigger unexpectedly failed CRT")
    residue, modulus = map(int, result)
    return residue or modulus, modulus


def type_i_31_certificate(prime: int) -> dict[str, object]:
    K = (MODULUS * prime + 1) // 4
    if prime % 24 != 1 or K % 93:
        raise AssertionError("31-triggered Type I precondition failed")
    C = K // 93
    gap = (prime + 2) // 93
    if 93 * gap != prime + 2:
        raise AssertionError("Type I gap was not integral")
    denominators = [2 * C, 186 * C, prime * K]
    if sum((Fraction(1, value) for value in denominators), Fraction()) != Fraction(
        4, prime
    ):
        raise AssertionError("Type I unit-fraction identity failed")
    return {
        "type": "I",
        "A": 2,
        "B": 1,
        "C": C,
        "H": 93,
        "gap": gap,
        "denominators": denominators,
    }


def type_ii_certificate(
    prime: int, A: int, C: int, kappa: int
) -> dict[str, object]:
    ray_factor = 4 * A * C * kappa - 1
    numerator = kappa * prime + A
    if numerator % ray_factor:
        raise AssertionError("Type II ray divisibility failed")
    B = numerator // ray_factor
    if A > B or (A + B) % kappa:
        raise AssertionError("Type II ray order or gap integrality failed")
    gap = (A + B) // kappa
    x = A * B * C
    divisor = A * A * C
    if not (
        prime == 4 * A * B * C - gap
        and x * x % divisor == 0
        and divisor <= x
        and (x + divisor) % gap == 0
    ):
        raise AssertionError("Type II divisor conditions failed")
    denominators = [x, prime * A * C * kappa, prime * B * C * kappa]
    if sum((Fraction(1, value) for value in denominators), Fraction()) != Fraction(
        4, prime
    ):
        raise AssertionError("Type II unit-fraction identity failed")
    return {
        "type": "II",
        "A": A,
        "B": B,
        "C": C,
        "kappa": kappa,
        "ray_factor": ray_factor,
        "gap": gap,
        "x": x,
        "divisor": divisor,
        "denominators": denominators,
    }


def choose_certificate(prime: int) -> dict[str, object] | None:
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise ValueError("expected a core prime")
    K = (MODULUS * prime + 1) // 4
    if K % 31 == 0:
        certificate = type_i_31_certificate(prime)
        trigger = 31
    elif K % 5 == 0:
        certificate = type_ii_certificate(prime, 1, 2, 2)
        trigger = 5
    elif K % 13 == 0:
        certificate = (
            type_ii_certificate(prime, 2, 2, 1)
            if prime == 73
            else type_ii_certificate(prime, 5, 2, 1)
        )
        trigger = 13
    elif K % 43 == 0:
        certificate = type_ii_certificate(prime, 11, 1, 1)
        trigger = 43
    else:
        return None
    if Fraction(int(certificate["gap"])) > Fraction(prime + 32, 15):
        raise AssertionError("selected certificate exceeded the common short bound")
    return {
        "p": prime,
        "K": K,
        "trigger_prime": trigger,
        "certificate": certificate,
        "short_bound": f"(p+32)/15 = {Fraction(prime + 32, 15)}",
    }


def first_prime_in_progression(
    residue: int, modulus: int, *, n_min: int = 0
) -> tuple[int, int]:
    for n_value in itertools.count(n_min):
        candidate = residue + modulus * n_value
        if sympy.isprime(candidate):
            return candidate, n_value
    raise AssertionError("unreachable")


def symbolic_ray_cases() -> list[dict[str, object]]:
    n = sympy.symbols("n", integer=True, nonnegative=True)
    rows: list[dict[str, object]] = []
    definitions = [
        (31, "I", None, 0),
        (5, "II", (1, 2, 2), 0),
        (13, "II", (5, 2, 1), 1),
        (43, "II", (11, 1, 1), 0),
    ]
    for support_prime, certificate_type, parameters, n_min in definitions:
        residue, progression_modulus = support_progression(support_prime)
        prime_expr = residue + progression_modulus * n
        K_expr = sympy.cancel((MODULUS * prime_expr + 1) / 4)
        if sympy.denom(K_expr) != 1:
            raise AssertionError("symbolic K was not integral on its progression")

        if certificate_type == "I":
            C_expr = sympy.cancel(K_expr / 93)
            gap_expr = sympy.cancel((prime_expr + 2) / 93)
            identities = [
                sympy.expand(K_expr - 93 * C_expr),
                sympy.expand(4 * C_expr + 1 - 47 * gap_expr),
                sympy.expand(prime_expr + 2 - 93 * gap_expr),
            ]
            formula = {
                "A": "2",
                "B": "1",
                "C": str(C_expr),
                "H": "93",
                "gap": str(gap_expr),
            }
        else:
            if parameters is None:
                raise AssertionError("missing Type II parameters")
            A, C, kappa = parameters
            ray_factor = 4 * A * C * kappa - 1
            B_expr = sympy.cancel((kappa * prime_expr + A) / ray_factor)
            gap_expr = sympy.cancel((A + B_expr) / kappa)
            identities = [
                sympy.expand(ray_factor * B_expr - (kappa * prime_expr + A)),
                sympy.expand(kappa * gap_expr - (A + B_expr)),
                sympy.expand(prime_expr - (4 * A * B_expr * C - gap_expr)),
            ]
            formula = {
                "A": str(A),
                "B": str(B_expr),
                "C": str(C),
                "kappa": str(kappa),
                "ray_factor": str(ray_factor),
                "gap": str(gap_expr),
            }
        if any(identity != 0 for identity in identities):
            raise AssertionError("a symbolic normal-form identity failed")

        bound_difference = sympy.factor((prime_expr + 32) / 15 - gap_expr)
        sample_prime, sample_n = first_prime_in_progression(
            residue, progression_modulus, n_min=n_min
        )
        sample = choose_certificate(sample_prime)
        if sample is None or sample["trigger_prime"] != support_prime:
            # Priority may select an earlier divisor on a multi-trigger sample.
            sample = {
                "p": sample_prime,
                "n": sample_n,
                "direct_case_certificate": (
                    type_i_31_certificate(sample_prime)
                    if certificate_type == "I"
                    else type_ii_certificate(sample_prime, *parameters)
                ),
            }
        rows.append(
            {
                "support_prime": support_prime,
                "certificate_type": certificate_type,
                "progression": {
                    "p": f"{residue} + {progression_modulus}*n",
                    "residue": residue,
                    "modulus": progression_modulus,
                    "n_min_for_formula": n_min,
                },
                "formula": formula,
                "symbolic_identities_verified": True,
                "common_bound_minus_gap": str(bound_difference),
                "sample": sample,
            }
        )

    special = choose_certificate(73)
    if special is None or special["trigger_prime"] != 13:
        raise AssertionError("p=73 lost its exceptional Type II certificate")
    rows.append(
        {
            "support_prime": 13,
            "certificate_type": "II-special",
            "progression": {"p": "73", "n": 0},
            "formula": {"A": 2, "B": 5, "C": 2, "kappa": 1},
            "symbolic_identities_verified": True,
            "common_bound_minus_gap": "0",
            "sample": special,
        }
    )
    return rows


def mask_selector() -> dict[str, object]:
    rows = []
    counts = {"EMPTY_RESIDUAL": 0, "TYPE_I": 0, "TYPE_II": 0}
    for mask in range(1 << len(OPTIONAL_PRIMES)):
        support = [
            prime
            for index, prime in enumerate(OPTIONAL_PRIMES)
            if mask & (1 << index)
        ]
        if not support:
            branch = "EMPTY_RESIDUAL"
            trigger = None
        elif 31 in support:
            branch = "TYPE_I"
            trigger = 31
        else:
            branch = "TYPE_II"
            trigger = next(prime for prime in (5, 13, 43) if prime in support)
        counts[branch] += 1
        rows.append(
            {
                "mask": mask,
                "optional_support": support,
                "selector_branch": branch,
                "trigger_prime": trigger,
            }
        )
    if counts != {"EMPTY_RESIDUAL": 1, "TYPE_I": 8, "TYPE_II": 7}:
        raise AssertionError(f"mask selector counts changed: {counts}")
    return {"counts": counts, "rows": rows}


def run() -> dict[str, object]:
    return {
        "schema_version": "r47-nonempty-support-short-selector/v1",
        "arithmetic": (
            "For every core prime with at least one of 5,13,31,43 in "
            "K=(47p+1)/4, choose a fixed Type I tail or a fixed-parameter "
            "Type II affine ray and certify gap <= (p+32)/15."
        ),
        "scope_note": (
            "This closes the 15 nonempty R=47 support masks. It does not cover "
            "the empty MISS_EXTERNAL mask or general moduli."
        ),
        "priority": [31, 5, 13, 43],
        "common_gap_bound": "m <= (p+32)/15 < p-2",
        "symbolic_ray_cases": symbolic_ray_cases(),
        "mask_selector": mask_selector(),
        "script_sha256": sha256(Path(__file__)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--verify",
        nargs="?",
        const=DEFAULT_OUTPUT,
        type=Path,
        help="recompute and compare with PATH",
    )
    args = parser.parse_args()
    payload = run()
    if args.verify is not None:
        stored = json.loads(args.verify.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError(f"stored certificate differs from replay: {args.verify}")
        action = "verified"
        path = args.verify
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        action = "wrote"
        path = args.output
    print(
        json.dumps(
            {
                "action": action,
                "path": str(path),
                "mask_selector_counts": payload["mask_selector"]["counts"],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
