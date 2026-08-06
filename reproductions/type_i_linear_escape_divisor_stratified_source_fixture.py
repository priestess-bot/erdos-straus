#!/usr/bin/env python3
"""Constant-size checks for divisor-stratified D-lattice source closure.

The fixture checks one small direct source-switch, the D=41 lower-layer
source boundary, and one raw branch which must remain outside the closure.
It is not a recursive census or a proof that every menu row lifts.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import gcd, isqrt


def divisors(value: int) -> tuple[int, ...]:
    """Return the positive divisors of a positive integer in increasing order."""
    lower: list[int] = []
    upper: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        lower.append(divisor)
        if divisor * divisor != value:
            upper.append(value // divisor)
    return tuple(lower + list(reversed(upper)))


def is_squarefree(value: int) -> bool:
    """Return whether value has no repeated prime factor."""
    factor = 2
    remaining = value
    while factor * factor <= remaining:
        if remaining % factor:
            factor += 1
            continue
        remaining //= factor
        if remaining % factor == 0:
            return False
        while remaining % factor == 0:
            remaining //= factor
        factor += 1
    return True


def is_prime(value: int) -> bool:
    """Return whether a positive integer is prime by trial division."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def omega(value: int) -> int:
    """Return the number of prime factors counted with multiplicity."""
    total = 0
    factor = 2
    remaining = value
    while factor * factor <= remaining:
        while remaining % factor == 0:
            remaining //= factor
            total += 1
        factor += 1
    return total + (1 if remaining > 1 else 0)


def standard_sources(prime: int, base: int) -> tuple[int, ...]:
    """Return the standard source parameters for one D layer."""
    return tuple(
        a
        for a in divisors(base)
        if is_squarefree(base // a) and 4 * a * base < prime
    )


def target_lattice(prime: int, base: int) -> tuple[tuple[int, int], ...]:
    """Return the Type II target lattice as (D-prime, A) pairs."""
    return tuple(
        (d_prime, a)
        for d_prime in divisors(base)
        for a in standard_sources(prime, d_prime)
    )


def legendre_symbol(value: int, prime: int) -> int:
    """Return the Legendre symbol for a nonzero residue modulo an odd prime."""
    residue = value % prime
    if residue == 0:
        return 0
    return -1 if pow(residue, (prime - 1) // 2, prime) == prime - 1 else 1


def small_stratified_switch() -> dict[str, object]:
    """Check L_4 as all source layers and one 4-to-1 Type II switch."""
    prime = 73
    base = 4
    strata = tuple(
        (d, a) for d in divisors(base) for a in standard_sources(prime, d)
    )
    lattice = target_lattice(prime, base)
    assert lattice == strata == ((1, 1), (2, 1), (2, 2), (4, 2), (4, 4))

    source_d, source_a = 4, 2
    target_d, target_a = 1, 1
    source_value = prime + 4 * source_d * source_a
    target_value = prime + 4 * target_d * target_a
    h = gcd(source_value, target_value)
    k_value = (h + 1) // (4 * target_d)
    b_value = (k_value * prime + target_a) // h
    x = target_a * b_value
    y = prime * (x + 1) // ((target_a + b_value) // k_value)
    z = prime * (x + x * x) // ((target_a + b_value) // k_value)

    assert source_value == 105
    assert target_value == 77
    assert is_prime(h)
    assert h == 7 and h % (4 * target_d) == -1 % (4 * target_d)
    assert k_value == 2 and b_value == 21
    assert Fraction(4, prime) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
    assert omega(target_d) <= omega(source_d) - 1

    return {
        "prime": prime,
        "base_D": base,
        "strata_equals_target_lattice": [list(pair) for pair in lattice],
        "strict_layer": {"from": source_d, "to": target_d},
        "route": {"source_N": source_value, "target_N": target_value, "h": h},
        "type_ii": {"A": target_a, "C": 1, "K": k_value, "B": b_value},
        "certificate": {"x": x, "y": y, "z": z},
    }


def lower_layer_source_boundary() -> dict[str, object]:
    """Check that the fixed-D residual has a fresh source at d=1."""
    prime = 57_399_241
    base = 41
    modulus = 59
    root_sources = standard_sources(prime, base)
    lower_sources = standard_sources(prime, 1)
    lower_factor = 11_479_849
    lower_value = prime + 4
    root_values = tuple(prime + 4 * base * source for source in root_sources)
    root_to_lower_gcds = tuple(gcd(value, lower_value) for value in root_values)

    assert root_sources == (1, 41)
    assert lower_sources == (1,)
    assert lower_value == 5 * lower_factor
    assert is_prime(lower_factor)
    assert lower_factor % modulus == 42
    assert legendre_symbol(lower_factor, modulus) == -1
    assert root_to_lower_gcds == (5, 5)
    assert all(value % 4 == 1 for value in root_to_lower_gcds)
    assert omega(1) <= omega(base) - 1

    return {
        "prime": prime,
        "base_D": base,
        "root_sources": list(root_sources),
        "not_a_verified_transition": {
            "root_N": list(root_values),
            "gcds_with_lower_N": list(root_to_lower_gcds),
            "all_gcds_are_one_mod_4": True,
        },
        "lower_layer": {
            "D": 1,
            "sources": list(lower_sources),
            "N": lower_value,
            "new_nonresidue_factor": lower_factor,
            "residue_mod_59": lower_factor % modulus,
        },
    }


def raw_reentry_boundary() -> dict[str, object]:
    """Show why a raw Type II terminal is not a descending D-layer source."""
    prime = 73
    initial_d = 1
    external_a0 = 8
    h = 15
    a_value, c_value, k_value = 2, 2, 1
    raw_base = a_value * c_value
    external_source = prime + 4 * external_a0
    b_value = (k_value * prime + a_value) // h

    assert a_value * c_value * k_value == (h + 1) // 4
    assert external_source == 105 and external_source % h == 0
    assert (k_value * prime + a_value) % h == 0
    assert b_value == 5 and a_value <= b_value
    assert raw_base == 4
    assert raw_base not in divisors(initial_d)

    return {
        "prime": prime,
        "initial_D": initial_d,
        "external_provenance": {"a0": external_a0, "N": external_source, "h": h},
        "raw_h": h,
        "raw_parameters": {"A": a_value, "C": c_value, "K": k_value},
        "type_ii": {"B": b_value},
        "raw_base_AC": raw_base,
        "outside_divisor_closure": True,
    }


def run_fixture() -> dict[str, object]:
    """Run three fixed examples and no general scan."""
    return {
        "scope_note": (
            "Three fixed examples only: a strict divisor-layer source-switch, "
            "a fresh d=1 source, and the raw branch excluded from the closure."
        ),
        "small_stratified_switch": small_stratified_switch(),
        "lower_layer_source_boundary": lower_layer_source_boundary(),
        "raw_reentry_boundary": raw_reentry_boundary(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(run_fixture(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
