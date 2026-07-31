#!/usr/bin/env python3
"""Reproduce the R=47 empty-mask dyadic terminal and escape boundary."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy

from type_ii_ac_adversarial_crt_search import (
    divisors_from_factorization,
    factorization,
    ordinary_type_ii_tail_witness,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-r47-empty-support-dyadic-boundary-results.json"
)
MODULUS = 47
OPTIONAL_PRIMES = (5, 13, 31, 43)
PROGRESSION_RESIDUE = 6_238_441
PROGRESSION_MODULUS = 12_476_880
PREFIX_PRIME_COUNT = 100
SMALL_RAYS = ((1, 1), (1, 2), (2, 1), (2, 2))
FOURIER_EXAMPLE = 31_192_201
SUBGROUP_EXAMPLE = 81_099_721
SMALL_RAY_COUNTEREXAMPLE = 193_391_641


def integer_list_sha256(values: list[int]) -> str:
    data = "".join(f"{value}\n" for value in values).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def factorization_payload(value: int) -> list[dict[str, int]]:
    return [
        {"prime": prime, "exponent": exponent}
        for prime, exponent in factorization(value)
    ]


def validate_empty_mask(prime: int) -> tuple[int, int]:
    if prime % 24 != 1 or not sympy.isprime(prime):
        raise ValueError("expected a core prime")
    numerator = MODULUS * prime + 1
    if numerator % 4:
        raise AssertionError("K is not integral")
    K = numerator // 4
    if K % 2 != 0 or K % 4 == 0 or K % 3 != 0 or K % 9 == 0:
        raise AssertionError("the exact 2- and 3-adic valuations changed")
    if any(K % optional_prime == 0 for optional_prime in OPTIONAL_PRIMES):
        raise AssertionError("the optional R=47 support is not empty")
    Q = K // 6
    if math.gcd(Q, 6) != 1 or Q % MODULUS != 2:
        raise AssertionError("the empty-mask quotient lost its forced residue")
    return K, Q


def dyadic_terminal(prime: int) -> dict[str, object]:
    K, Q = validate_empty_mask(prime)
    L = 2 * K
    a = 4
    b = Q
    exponent = 1
    E = L * a // b
    source, remainder = divmod(4 * K - E, MODULUS)
    if (
        remainder
        or math.gcd(a, b) != 1
        or L % a
        or L % b
        or (a - 2 * b) % MODULUS
        or not a < 2 * b
        or E != 48
        or source != prime - 1
        or L * L % E
        or E % MODULUS != 1
    ):
        raise AssertionError("the universal dyadic terminal failed")
    return {
        "p": prime,
        "K": K,
        "Q": Q,
        "L": L,
        "a": a,
        "b": b,
        "j": exponent,
        "E": E,
        "source_denominator": source,
    }


def generated_subgroup(generators: list[int]) -> set[int]:
    subgroup = {1}
    while True:
        expanded = subgroup | {
            value * generator % MODULUS
            for value in subgroup
            for generator in generators
        }
        if expanded == subgroup:
            return subgroup
        subgroup = expanded


def centered_profile(prime: int) -> dict[str, object]:
    K, _ = validate_empty_mask(prime)
    factors = factorization(K)
    residues: set[int] = set()
    exponent_ranges = [range(-exponent, exponent + 1) for _, exponent in factors]
    for exponent_vector in itertools.product(*exponent_ranges):
        residue = 1
        for (factor, _), exponent in zip(factors, exponent_vector, strict=True):
            residue = residue * pow(factor, exponent, MODULUS) % MODULUS
        residues.add(residue)
    subgroup = generated_subgroup([factor % MODULUS for factor, _ in factors])
    target = MODULUS - 1
    if target in residues:
        state = "HIT"
    elif target in subgroup:
        state = "F"
    else:
        state = "G"
    return {
        "p": prime,
        "K": K,
        "K_factorization": factorization_payload(K),
        "centered_spectrum_size": len(residues),
        "centered_target_hit": target in residues,
        "support_subgroup_size": len(subgroup),
        "support_subgroup_target_hit": target in subgroup,
        "state": state,
    }


def small_ray_profile(prime: int, A: int, C: int) -> dict[str, object]:
    shifted = prime + 4 * A * A * C
    ray_modulus = 4 * A * C
    factors = factorization(shifted)
    divisor_residues = sorted(
        {
            divisor % ray_modulus
            for divisor in divisors_from_factorization(factors)
        }
    )
    target = ray_modulus - 1
    witness_divisors = [
        divisor
        for divisor in divisors_from_factorization(factors)
        if divisor % ray_modulus == target
    ]
    witness = None
    if witness_divisors:
        ray_factor = min(witness_divisors)
        kappa = (ray_factor + 1) // ray_modulus
        B, remainder = divmod(kappa * prime + A, ray_factor)
        if remainder or A > B:
            raise AssertionError("raw Type II divisor did not reconstruct")
        gap, gap_remainder = divmod(A + B, kappa)
        if gap_remainder or prime != 4 * A * B * C - gap:
            raise AssertionError("raw Type II normal form failed")
        witness = {
            "ray_factor": ray_factor,
            "kappa": kappa,
            "B": B,
            "gap": gap,
        }
    return {
        "A": A,
        "C": C,
        "shifted_integer": shifted,
        "shifted_factorization": [
            {"prime": factor, "exponent": exponent}
            for factor, exponent in factors
        ],
        "ray_modulus": ray_modulus,
        "target_residue": target,
        "divisor_residues": divisor_residues,
        "hit": witness is not None,
        "witness": witness,
    }


def first_progression_primes(count: int) -> list[tuple[int, int]]:
    rows: list[tuple[int, int]] = []
    for parameter in itertools.count():
        prime = PROGRESSION_RESIDUE + PROGRESSION_MODULUS * parameter
        if sympy.isprime(prime):
            rows.append((parameter, prime))
            if len(rows) == count:
                return rows
    raise AssertionError("unreachable")


def compact_tail_witness(witness: dict[str, object]) -> dict[str, int]:
    return {
        "gap": int(witness["gap"]),
        "x": int(witness["x"]),
        "divisor": int(witness["divisor"]),
        "source_denominator": int(witness["source_denominator"]),
    }


def required_tail_witness(prime: int) -> dict[str, object]:
    witness = ordinary_type_ii_tail_witness(prime)
    if witness is None:
        raise AssertionError(f"p={prime} lost its required p-1 tail witness")
    return witness


def run() -> dict[str, object]:
    progression_primes = first_progression_primes(PREFIX_PRIME_COUNT)
    gap_counts: Counter[int] = Counter()
    small_ray_misses: list[dict[str, object]] = []
    ordinary_tail_misses: list[int] = []

    for parameter, prime in progression_primes:
        dyadic_terminal(prime)
        ray_rows = [small_ray_profile(prime, A, C) for A, C in SMALL_RAYS]
        tail = ordinary_type_ii_tail_witness(prime)
        if tail is None:
            ordinary_tail_misses.append(prime)
        else:
            gap_counts[int(tail["gap"])] += 1
        if not any(bool(row["hit"]) for row in ray_rows):
            small_ray_misses.append(
                {
                    "progression_parameter": parameter,
                    "p": prime,
                    "ordinary_p_minus_one_tail": (
                        None if tail is None else compact_tail_witness(tail)
                    ),
                }
            )

    primes = [prime for _, prime in progression_primes]
    if (
        len(small_ray_misses) != 3
        or ordinary_tail_misses
        or [int(row["p"]) for row in small_ray_misses]
        != [193_391_641, 1_091_727_001, 3_686_918_041]
        or dict(sorted(gap_counts.items())) != {3: 44, 7: 41, 11: 7, 19: 3, 23: 5}
    ):
        raise AssertionError("the directed 100-prime profile changed")

    F_profile = centered_profile(FOURIER_EXAMPLE)
    G_profile = centered_profile(SUBGROUP_EXAMPLE)
    if F_profile["state"] != "F" or G_profile["state"] != "G":
        raise AssertionError("the explicit F/G boundary changed")

    counterexample_terminal = dyadic_terminal(SMALL_RAY_COUNTEREXAMPLE)
    counterexample_rays = [
        small_ray_profile(SMALL_RAY_COUNTEREXAMPLE, A, C)
        for A, C in SMALL_RAYS
    ]
    if any(bool(row["hit"]) for row in counterexample_rays):
        raise AssertionError("the four-ray counterexample acquired a hit")
    counterexample_tail = ordinary_type_ii_tail_witness(SMALL_RAY_COUNTEREXAMPLE)
    if counterexample_tail is None:
        raise AssertionError("the counterexample lost its p-1 tail exit")

    return {
        "schema_version": "r47-empty-support-dyadic-boundary/v1",
        "arithmetic": (
            "derive the universal E=48, n=p-1 dyadic terminal from K=6Q; "
            "classify two exact centered spectra; factor all four AC<=2 "
            "shifted integers; and run a directed 100-prime profile on the "
            "stored canonical empty-mask progression"
        ),
        "scope_note": (
            "The universal terminal and explicit F/G and four-ray boundary "
            "are exact claims. The 100-prime p-1 tail closure is finite "
            "hypothesis-supporting evidence, not an AP-wide theorem."
        ),
        "canonical_progression": {
            "residue": PROGRESSION_RESIDUE,
            "modulus": PROGRESSION_MODULUS,
        },
        "universal_terminal_sample": dyadic_terminal(FOURIER_EXAMPLE),
        "same_R_boundaries": {
            "F_example": F_profile,
            "G_example": G_profile,
            "ordinary_p_minus_one_tail_exits": {
                str(prime): compact_tail_witness(required_tail_witness(prime))
                for prime in (FOURIER_EXAMPLE, SUBGROUP_EXAMPLE)
            },
        },
        "four_small_ray_counterexample": {
            "terminal": counterexample_terminal,
            "centered_profile": centered_profile(SMALL_RAY_COUNTEREXAMPLE),
            "ray_profiles": counterexample_rays,
            "ordinary_p_minus_one_tail_exit": compact_tail_witness(
                counterexample_tail
            ),
        },
        "directed_prefix_profile": {
            "prime_count": len(primes),
            "parameter_min": progression_primes[0][0],
            "parameter_max": progression_primes[-1][0],
            "prime_min": primes[0],
            "prime_max": primes[-1],
            "prime_list_sha256": integer_list_sha256(primes),
            "small_ray_hit_count": len(primes) - len(small_ray_misses),
            "small_ray_miss_count": len(small_ray_misses),
            "small_ray_misses": small_ray_misses,
            "ordinary_p_minus_one_tail_hit_count": len(primes),
            "ordinary_p_minus_one_tail_miss_count": 0,
            "ordinary_tail_first_gap_counts": {
                str(gap): count for gap, count in sorted(gap_counts.items())
            },
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
        print(json.dumps(payload["directed_prefix_profile"], ensure_ascii=False, indent=2))
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload["directed_prefix_profile"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
