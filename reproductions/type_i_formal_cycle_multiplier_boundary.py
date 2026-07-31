#!/usr/bin/env python3
"""Verify the multiplier bridge and two exact formal-cycle boundaries."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-formal-cycle-multiplier-boundary-results.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization(value: int) -> dict[int, int]:
    factors = {int(q): int(e) for q, e in sympy.factorint(value).items()}
    if math.prod(q**e for q, e in factors.items()) != value:
        raise AssertionError("factorization failed to reconstruct its input")
    return dict(sorted(factors.items()))


def support(value: int) -> set[int]:
    return set(factorization(value))


def signed_cube(modulus: int, primes: list[int]) -> dict[int, tuple[int, int]]:
    residues: dict[int, tuple[int, int]] = {1: (1, 1)}
    for q in primes:
        inverse = pow(q, -1, modulus)
        previous = list(residues.items())
        for residue, (numerator, denominator) in previous:
            residues.setdefault(
                residue * q % modulus,
                (numerator * q, denominator),
            )
            residues.setdefault(
                residue * inverse % modulus,
                (numerator, denominator * q),
            )
    return residues


def verify_signed_witness(
    modulus: int,
    primes: list[int],
    numerator: int,
    denominator: int,
    target: int,
) -> None:
    if math.gcd(numerator, denominator) != 1:
        raise AssertionError("signed witness was not reduced")
    if not (support(numerator) | support(denominator)) <= set(primes):
        raise AssertionError("signed witness left the declared support")
    if any(e != 1 for e in factorization(numerator).values()):
        raise AssertionError("signed numerator was not squarefree")
    if any(e != 1 for e in factorization(denominator).values()):
        raise AssertionError("signed denominator was not squarefree")
    residue = numerator * pow(denominator, -1, modulus) % modulus
    if residue != target:
        raise AssertionError("signed witness missed its target")


def centered_spectrum(value: int, modulus: int) -> set[int]:
    return {
        int(divisor * pow(value, -1, modulus) % modulus)
        for divisor in sympy.divisors(value * value)
    }


def verify_solution(prime: int, solution: tuple[int, int, int]) -> None:
    if min(solution) <= 0:
        raise AssertionError("unit-fraction denominator was not positive")
    if sum((Fraction(1, value) for value in solution), Fraction()) != Fraction(4, prime):
        raise AssertionError("unit-fraction identity failed")


def exact_gap_hits(prime: int, gap: int) -> tuple[list[int], list[int]]:
    x = (prime + gap) // 4
    if 4 * x != prime + gap:
        raise AssertionError("gap did not give an integral first denominator")
    type_i: list[int] = []
    type_ii: list[int] = []
    for divisor in sympy.divisors(x * x):
        divisor = int(divisor)
        if (prime * x + divisor) % gap == 0:
            type_i.append(divisor)
        if divisor <= x and (x + divisor) % gap == 0:
            type_ii.append(divisor)
    return type_i, type_ii


def multiplier_boundary() -> dict[str, object]:
    modulus = 30_031
    cycle = [31, 6_000, 1_200, 240, 961]
    selected = [30_000, 6_000, 1_200, 29_791, 961]
    labels = [5, 5, 5, 31, 31]
    expected_destinations = cycle[1:] + cycle[:1]
    for source, coordinate, q, destination in zip(
        cycle, selected, labels, expected_destinations
    ):
        if source != min(coordinate, modulus - coordinate):
            raise AssertionError("selected coordinate did not belong to its source")
        if coordinate % (q * q):
            raise AssertionError("universal edge lacked q^2 divisibility")
        reduced = coordinate // q
        if min(reduced, modulus - reduced) != destination:
            raise AssertionError("declared universal edge had the wrong destination")

    primes = sorted(
        set().union(
            *(
                support(x) | support(modulus - x)
                for x in cycle
            )
        )
    )
    expected_primes = [2, 3, 5, 7, 11, 17, 19, 31, 2_621, 3_433]
    if primes != expected_primes:
        raise AssertionError("cycle support changed")
    cube = signed_cube(modulus, primes)
    if len(cube) != 25_357:
        raise AssertionError("signed-cube size changed")
    radical = math.prod(primes)
    four_radical = 4 * radical % modulus
    multiplier = pow(four_radical, -1, modulus)
    targets = {
        "minus_one": modulus - 1,
        "minus_four_radical": (-four_radical) % modulus,
        "minus_multiplier": (-multiplier) % modulus,
    }
    if targets["minus_one"] in cube:
        raise AssertionError("declared radical-cube counterexample disappeared")
    witness_left = (155, 4_493_797)
    witness_right = (witness_left[1], witness_left[0])
    verify_signed_witness(
        modulus,
        primes,
        *witness_left,
        targets["minus_four_radical"],
    )
    verify_signed_witness(
        modulus,
        primes,
        *witness_right,
        targets["minus_multiplier"],
    )
    if targets["minus_four_radical"] not in cube or targets["minus_multiplier"] not in cube:
        raise AssertionError("multiplier targets were absent from the signed cube")
    centered_divisor = radical * witness_left[1] // witness_left[0]
    if radical * witness_left[1] % witness_left[0]:
        raise AssertionError("multiplier witness did not produce an integer divisor")
    if (radical * radical) % centered_divisor:
        raise AssertionError("multiplier divisor did not divide the radical square")
    if 4 * centered_divisor % modulus != modulus - 1:
        raise AssertionError("multiplier divisor missed -1/4")
    if modulus % 3 != 1 or 3 not in primes:
        raise AssertionError("core incompatibility check changed")

    return {
        "R": modulus,
        "factorization_R": factorization(modulus),
        "cycle": cycle,
        "cycle_pairs": [[x, modulus - x] for x in cycle],
        "edge_labels": [
            {"selected_coordinate": coordinate, "q": q}
            for coordinate, q in zip(selected, labels)
        ],
        "support": primes,
        "radical": radical,
        "radical_mod_R": radical % modulus,
        "four_radical_mod_R": four_radical,
        "multiplier_mod_R": multiplier,
        "signed_cube_size": len(cube),
        "targets": targets,
        "direct_radical_hit": False,
        "multiplier_bridge_hits": {
            "minus_four_radical": {
                "numerator": witness_left[0],
                "denominator": witness_left[1],
            },
            "minus_multiplier": {
                "numerator": witness_right[0],
                "denominator": witness_right[1],
            },
        },
        "multiplier_centered_divisor": centered_divisor,
        "multiplier_centered_divisor_mod_R": centered_divisor % modulus,
        "core_support_compatibility": {
            "compatible": False,
            "reason": "R=1 mod 3 and core p=1 mod 3 imply K=2 mod 3, but the cycle support contains 3",
        },
    }


def external_cycle_boundary() -> dict[str, object]:
    prime = 241
    modulus = 19
    K = 1_145
    cycle = [(1, 18), (9, 10), (3, 16)]
    selected = [18, 9, 3]
    labels = [2, 3, 3]
    signs: list[int] = []
    for index, (coordinate, q) in enumerate(zip(selected, labels)):
        reduced = coordinate // q
        next_selected = selected[(index + 1) % len(selected)]
        if next_selected == reduced:
            signs.append(1)
        elif next_selected == modulus - reduced:
            signs.append(-1)
        else:
            raise AssertionError("external cycle did not compose")
        if factorization(coordinate)[q] <= factorization(K).get(q, 0):
            raise AssertionError("external edge was not excess")
    product = math.prod(labels)
    sign = math.prod(signs)
    if product % modulus != sign % modulus:
        raise AssertionError("signed cycle-product law failed")
    if centered_spectrum(K, modulus) != {1, 4, 5}:
        raise AssertionError("original centered spectrum changed")

    candidate_gaps = sorted(
        {
            divisor
            for pair in cycle
            for coordinate in pair
            for divisor in map(int, sympy.divisors(coordinate))
            if (
                divisor % 4 == 3
                and 3 <= divisor <= prime - 2
                and divisor // math.gcd(divisor, K) > 1
            )
        }
    )
    if candidate_gaps != [3]:
        raise AssertionError("external gap menu changed")
    type_i, type_ii = exact_gap_hits(prime, 3)
    if type_i or type_ii:
        raise AssertionError("external gap unexpectedly hit")
    K_3 = (3 * prime + 1) // 4
    if (modulus * prime + 1) // 4 != K:
        raise AssertionError("state K identity failed")
    if centered_spectrum(K_3, 3) != {1}:
        raise AssertionError("cross-modulus centered spectrum changed")

    x = (prime + 7) // 4
    solution = (x, prime * (x + 1) // 7, x * prime * (x + 1) // 7)
    verify_solution(prime, solution)
    return {
        "p": prime,
        "R": modulus,
        "K": K,
        "factorization_K": factorization(K),
        "cycle_pairs": [list(pair) for pair in cycle],
        "selected_coordinates": selected,
        "edge_labels": labels,
        "orientation_signs": signs,
        "edge_product": product,
        "edge_product_mod_R": product % modulus,
        "original_centered_spectrum": sorted(centered_spectrum(K, modulus)),
        "external_gap_candidates": candidate_gaps,
        "gap_3": {
            "x": (prime + 3) // 4,
            "type_I_hits": type_i,
            "type_II_hits": type_ii,
        },
        "cross_modulus_3": {
            "K_Q": K_3,
            "centered_spectrum": sorted(centered_spectrum(K_3, 3)),
            "hit": False,
        },
        "independent_type_II": {
            "gap": 7,
            "x": x,
            "divisor": 1,
            "solution": list(solution),
        },
    }


def self_loop_boundary() -> dict[str, object]:
    prime = 1_009
    modulus = 3
    K = 757
    if not sympy.isprime(prime) or not sympy.isprime(K):
        raise AssertionError("self-loop primality control failed")
    if (prime * modulus + 1) // 4 != K:
        raise AssertionError("self-loop K identity failed")
    spectrum = centered_spectrum(K, modulus)
    if spectrum != {1}:
        raise AssertionError("self-loop centered miss changed")
    selected = 2
    q = 2
    destination = (selected // q, modulus - selected // q)
    if set(destination) != {1, 2} or factorization(K).get(q, 0):
        raise AssertionError("declared external self-loop failed")
    return {
        "p": prime,
        "R": modulus,
        "K": K,
        "centered_spectrum": sorted(spectrum),
        "node": [1, 2],
        "selected_coordinate": selected,
        "q": q,
        "destination": list(destination),
    }


def run() -> dict[str, object]:
    return {
        "arithmetic": (
            "Verify the first direct radical-cube cycle boundary, its two multiplier-bridge targets, "
            "the all-external p=241 cycle with three failed cycle-derived terminals, and the R=3 "
            "external self-loop."
        ),
        "multiplier_boundary": multiplier_boundary(),
        "external_cycle_boundary": external_cycle_boundary(),
        "self_loop_boundary": self_loop_boundary(),
        "script_sha256": sha256(Path(__file__)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["multiplier_boundary"], sort_keys=True))


if __name__ == "__main__":
    main()
