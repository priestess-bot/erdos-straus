#!/usr/bin/env python3
"""Verify core realizability of universal m=1 cycles and its finite corollary."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import sympy
from sympy.ntheory.modular import crt


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-core-formal-cycle-multiplier-scan-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-core-cycle-realizability-results.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factor_support(value: int) -> set[int]:
    factors = {int(prime) for prime in sympy.factorint(value)}
    if math.prod(
        int(prime) ** int(exponent)
        for prime, exponent in sympy.factorint(value).items()
    ) != value:
        raise AssertionError("factorization failed to reconstruct its input")
    return factors


def cycle_support(modulus: int, cycle: list[int]) -> list[int]:
    return sorted(
        set().union(
            *(
                factor_support(node) | factor_support(modulus - node)
                for node in cycle
            )
        )
    )


def exact_support_progression(
    modulus: int,
    support: list[int],
) -> tuple[int, int] | None:
    """Return p=a mod M forcing p=1 mod 24 and v_q(K)=1 on support."""
    if modulus % 8 != 7:
        raise ValueError("the core-supported universal cycle layer requires R=7 mod 8")
    if any(math.gcd(prime, modulus) != 1 for prime in support):
        raise ValueError("cycle support must be coprime to R")
    if 3 in support and modulus % 3 != 2:
        return None

    # Force v_2((pR+1)/4)=1 while retaining p=1 mod 3.
    residue_16 = 7 * pow(modulus, -1, 16) % 16
    if residue_16 % 8 != 1:
        raise AssertionError("the dyadic lift did not retain p=1 mod 8")
    base_residue, base_modulus = crt([16, 3], [residue_16, 1])
    moduli = [int(base_modulus)]
    residues = [int(base_residue)]

    if 3 in support:
        residue_9 = next(
            candidate
            for candidate in range(1, 9)
            if (
                candidate % 3 == 1
                and (candidate * modulus + 1) % 3 == 0
                and (candidate * modulus + 1) % 9 != 0
            )
        )
        moduli.append(9)
        residues.append(residue_9)

    for prime in support:
        if prime <= 3:
            continue
        residue_q = -pow(modulus, -1, prime) % prime
        residue_q2 = next(
            residue_q + lift * prime
            for lift in range(prime)
            if (modulus * (residue_q + lift * prime) + 1) % (prime * prime)
        )
        moduli.append(prime * prime)
        residues.append(residue_q2)

    combined = crt(moduli, residues, check=True)
    if combined is None:
        raise AssertionError("compatible local support conditions failed CRT")
    residue, progression_modulus = map(int, combined)
    residue %= progression_modulus
    if residue % 24 != 1 or math.gcd(residue, progression_modulus) != 1:
        raise AssertionError("the progression was not a core Dirichlet class")

    numerator = residue * modulus + 1
    if valuation(numerator, 2) != 3:
        raise AssertionError("the progression missed exact dyadic valuation")
    for prime in support:
        if prime == 2:
            continue
        if valuation(numerator, prime) != 1:
            raise AssertionError("the progression missed an exact support valuation")
    return residue, progression_modulus


def first_prime_in_progression(
    residue: int,
    modulus: int,
    lower_bound: int,
) -> tuple[int, int]:
    start = max(0, (lower_bound + 1 - residue + modulus - 1) // modulus)
    for step in range(start, start + 10_000):
        candidate = residue + step * modulus
        if sympy.isprime(candidate):
            return candidate, step
    raise AssertionError("no prime found in the bounded witness search")


def verify_cycle_edges(
    modulus: int,
    cycle: list[int],
    selected: list[int],
    labels: list[int],
    k_value: int | None = None,
) -> None:
    destinations = cycle[1:] + cycle[:1]
    for node, coordinate, prime, destination in zip(
        cycle,
        selected,
        labels,
        destinations,
    ):
        if node != min(coordinate, modulus - coordinate):
            raise AssertionError("selected coordinate was not in its source node")
        if coordinate % (prime * prime):
            raise AssertionError("universal edge lacked q^2 divisibility")
        reduced = coordinate // prime
        if min(reduced, modulus - reduced) != destination:
            raise AssertionError("universal edge had the wrong destination")
        if k_value is not None and valuation(coordinate, prime) <= valuation(
            k_value, prime
        ):
            raise AssertionError("realized edge was not K-excess")


def compatible_witness() -> dict[str, object]:
    modulus = 47
    cycle = [2, 15, 16, 8, 4]
    selected = [45, 32, 16, 8, 4]
    labels = [3, 2, 2, 2, 2]
    support = cycle_support(modulus, cycle)
    expected_support = [2, 3, 5, 13, 31, 43]
    if support != expected_support:
        raise AssertionError("the compatible cycle support changed")

    progression = exact_support_progression(modulus, support)
    if progression is None:
        raise AssertionError("the compatible cycle was rejected")
    residue, progression_modulus = progression
    prime, step = first_prime_in_progression(
        residue,
        progression_modulus,
        modulus,
    )
    k_value = (prime * modulus + 1) // 4
    if prime % 24 != 1 or 4 * k_value != prime * modulus + 1:
        raise AssertionError("the explicit prime did not define a core state")
    if any(valuation(k_value, q) != 1 for q in support):
        raise AssertionError("the explicit K did not realize exact support")
    if any(
        not (factor_support(node) | factor_support(modulus - node))
        <= factor_support(k_value)
        for node in cycle
    ):
        raise AssertionError("a realized cycle coordinate left K support")
    verify_cycle_edges(modulus, cycle, selected, labels, k_value)

    radical_numerator = 93
    radical_denominator = 1
    if (
        radical_numerator
        * pow(radical_denominator, -1, modulus)
        % modulus
        != modulus - 1
    ):
        raise AssertionError("the squarefree witness missed -1")
    if not (
        factor_support(radical_numerator) | factor_support(radical_denominator)
    ) <= set(support):
        raise AssertionError("the squarefree witness left cycle support")

    tail_small = radical_denominator
    tail_large = radical_numerator
    normal_a = (tail_small + tail_large) // modulus
    normal_c = k_value // (tail_small * tail_large)
    gap = (4 * tail_small * tail_small * normal_c + 1) // modulus
    if tail_small * tail_large * normal_c != k_value:
        raise AssertionError("the Type I normal form did not reconstruct K")
    if (tail_small * prime + normal_a) % gap:
        raise AssertionError("the Type I normal form divisibility failed")
    solution = (
        normal_a * tail_small * normal_c,
        normal_a * normal_c * tail_large,
        prime * k_value,
    )
    if sum((Fraction(1, value) for value in solution), Fraction()) != Fraction(
        4, prime
    ):
        raise AssertionError("the realized Type I solution failed")

    return {
        "R": modulus,
        "cycle": cycle,
        "cycle_pairs": [[node, modulus - node] for node in cycle],
        "selected_coordinates": selected,
        "edge_labels": labels,
        "support": support,
        "progression": {
            "residue": residue,
            "modulus": progression_modulus,
            "prime_step": step,
        },
        "p": prime,
        "K": k_value,
        "support_valuations_in_K": {
            str(q): valuation(k_value, q) for q in support
        },
        "radical_witness": {
            "numerator": radical_numerator,
            "denominator": radical_denominator,
        },
        "type_I_normal_form": {
            "A": normal_a,
            "B": tail_small,
            "C": normal_c,
            "H": tail_large,
            "gap": gap,
            "solution": list(solution),
        },
    }


def incompatible_witness() -> dict[str, object]:
    modulus = 30_031
    cycle = [31, 6_000, 1_200, 240, 961]
    selected = [30_000, 6_000, 1_200, 29_791, 961]
    labels = [5, 5, 5, 31, 31]
    support = cycle_support(modulus, cycle)
    expected_support = [2, 3, 5, 7, 11, 17, 19, 31, 2_621, 3_433]
    if support != expected_support:
        raise AssertionError("the incompatible cycle support changed")
    verify_cycle_edges(modulus, cycle, selected, labels)
    if exact_support_progression(modulus, support) is not None:
        raise AssertionError("the mod-3 obstruction unexpectedly disappeared")
    if modulus % 3 != 1 or 3 not in support:
        raise AssertionError("the mod-3 obstruction data changed")
    return {
        "R": modulus,
        "cycle": cycle,
        "support": support,
        "compatible": False,
        "obstruction": "3 is in S but R is not 2 mod 3",
    }


def finite_prefix(input_path: Path, incompatible: dict[str, object]) -> dict[str, object]:
    source = json.loads(input_path.read_text(encoding="utf-8"))
    summary = source["summary"]
    first_miss = source["first_direct_radical_miss"]
    if source["limit"] != 100_000 or source["residue_class"] != "R=7 mod 8":
        raise AssertionError("the source scan no longer has the locked scope")
    if summary["moduli"] != 12_500 or summary["direct_radical_miss_cycles"] != 1:
        raise AssertionError("the locked direct-miss count changed")
    if (
        first_miss["R"] != incompatible["R"]
        or first_miss["cycle"] != incompatible["cycle"]
        or first_miss["support"] != incompatible["support"]
    ):
        raise AssertionError("the unique direct miss was not the mod-3 obstruction")
    return {
        "source_result": str(input_path.relative_to(ROOT)),
        "source_result_sha256": sha256(input_path),
        "limit": source["limit"],
        "moduli": summary["moduli"],
        "all_direct_radical_misses": summary["direct_radical_miss_cycles"],
        "core_realizable_direct_radical_misses": 0,
        "inference": (
            "The complete scan has one direct miss, and the exact core-support "
            "criterion excludes that cycle."
        ),
    }


def run(input_path: Path) -> dict[str, object]:
    compatible = compatible_witness()
    incompatible = incompatible_witness()
    return {
        "arithmetic": (
            "Verify the exact local criterion for realizing every coordinate "
            "prime of a universal R=7 mod 8 cycle with valuation one in "
            "K=(pR+1)/4, exhibit a compatible core prime and Type I terminal, "
            "and combine the criterion with the locked R<100000 cycle scan."
        ),
        "criterion": {
            "necessary_and_sufficient_local_condition": (
                "3 not in S or R=2 mod 3"
            ),
            "prime_existence_input": "Dirichlet's theorem on primes in progressions",
        },
        "compatible_witness": compatible,
        "incompatible_first_direct_miss": incompatible,
        "finite_prefix": finite_prefix(input_path, incompatible),
        "script_sha256": sha256(Path(__file__)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(args.input)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["finite_prefix"], sort_keys=True))


if __name__ == "__main__":
    main()
