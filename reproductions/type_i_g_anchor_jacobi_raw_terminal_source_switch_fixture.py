#!/usr/bin/env python3
"""Fixed G-anchor terminal and raw-factor source-switch-degeneracy fixtures.

This checks three named core primes only.  It does not search primes, prove a
uniform raw-ray bound, or promote a raw path to an E1--E5 recursion edge.  The
only raw hit in this domain has canonical D=1, so this fixture contains no
nontrivial source-switch.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import isqrt


def divisors(value: int) -> tuple[int, ...]:
    """Return positive divisors in increasing order."""
    lower: list[int] = []
    upper: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        lower.append(divisor)
        if divisor * divisor != value:
            upper.append(value // divisor)
    return tuple(lower + list(reversed(upper)))


def jacobi_symbol(value: int, modulus: int) -> int:
    """Return the Jacobi symbol for an odd positive modulus."""
    if modulus <= 0 or modulus % 2 == 0:
        raise ValueError("the Jacobi modulus must be positive and odd")
    value %= modulus
    result = 1
    while value:
        while value % 2 == 0:
            value //= 2
            if modulus % 8 in (3, 5):
                result = -result
        value, modulus = modulus, value
        if value % 4 == 3 and modulus % 4 == 3:
            result = -result
        value %= modulus
    return result if modulus == 1 else 0


def negative_divisors(prime: int) -> tuple[int, ...]:
    """Return the G-anchor divisors in the negative Jacobi coset."""
    modulus = prime - 2
    q_value = (prime - 3) // 2
    return tuple(
        divisor
        for divisor in divisors(q_value)
        if jacobi_symbol(divisor, modulus) == -1
    )


def raw_pairs(prime: int, factor: int) -> tuple[tuple[int, int, int, int], ...]:
    """Enumerate the finite raw-factor menu with h=factor."""
    if factor % 4 != 3:
        return ()
    budget = (factor + 1) // 4
    rows: list[tuple[int, int, int, int]] = []
    for a_value in divisors(budget):
        for c_value in divisors(budget // a_value):
            product = a_value * c_value
            if budget % product:
                continue
            k_value = budget // product
            numerator = k_value * prime + a_value
            if numerator % factor:
                continue
            b_value = numerator // factor
            if a_value <= b_value:
                rows.append((a_value, c_value, k_value, b_value))
    return tuple(rows)


def assert_no_fixed_chart_sink(prime: int) -> list[dict[str, int]]:
    """Check every d|Q endpoint has negative character product outside K."""
    modulus = prime - 2
    q_value = (prime - 3) // 2
    k_value = (prime - 1) ** 2 // 4
    rows: list[dict[str, int]] = []
    for divisor in divisors(q_value):
        x_value = 2 * q_value // divisor
        y_value = modulus - x_value
        product = x_value * y_value
        assert product % k_value != 0
        assert jacobi_symbol(product, modulus) == -1
        rows.append({"delta": divisor, "x": x_value, "y": y_value})
    return rows


def gap_three_certificate(prime: int, factor: int) -> dict[str, int]:
    """Build the gap-three Type II certificate from q|x and q=2 mod 3."""
    x_value = (prime + 3) // 4
    assert x_value % factor == 0 and factor % 3 == 2
    y_value = prime * (x_value + factor) // 3
    z_value = prime * x_value * (x_value + factor) // (3 * factor)
    assert Fraction(4, prime) == (
        Fraction(1, x_value) + Fraction(1, y_value) + Fraction(1, z_value)
    )
    return {"x": x_value, "q": factor, "y": y_value, "z": z_value}


def gap_seven_certificate(prime: int) -> dict[str, int]:
    """Build the p+4 gap-seven leaf forced by 7|Q."""
    x_value = (prime + 7) // 4
    assert (prime - 3) // 2 % 7 == 0
    assert (prime + 4) % 7 == 0
    assert (x_value + 1) % 7 == 0
    y_value = prime * (x_value + 1) // 7
    z_value = prime * x_value * (x_value + 1) // 7
    assert Fraction(4, prime) == (
        Fraction(1, x_value) + Fraction(1, y_value) + Fraction(1, z_value)
    )
    return {"x": x_value, "y": y_value, "z": z_value}


def raw_seven_certificate(prime: int) -> dict[str, int]:
    """Build the unique h=7 raw-normal-form Type II leaf."""
    h_value = 7
    a_value = c_value = 1
    k_value = 2
    b_value = (k_value * prime + a_value) // h_value
    x_value = a_value * b_value
    divisor = a_value * a_value * c_value
    gap = (a_value + b_value) // k_value
    y_value = prime * (x_value + divisor) // gap
    z_value = prime * (x_value + x_value * x_value // divisor) // gap

    assert (prime - 3) // 2 % h_value == 0
    assert a_value * c_value * k_value == (h_value + 1) // 4
    assert (k_value * prime + a_value) % h_value == 0
    assert b_value >= a_value
    assert gap == (prime + 4) // h_value
    assert Fraction(4, prime) == (
        Fraction(1, x_value) + Fraction(1, y_value) + Fraction(1, z_value)
    )
    return {
        "h": h_value,
        "A": a_value,
        "C": c_value,
        "K": k_value,
        "B": b_value,
        "x": x_value,
        "d": divisor,
        "m": gap,
        "y": y_value,
        "z": z_value,
    }


def p73_fixture() -> dict[str, object]:
    """Check the 7-label leaves and raw source-switch degeneracy."""
    prime = 73
    negatives = negative_divisors(prime)
    pairs_7 = raw_pairs(prime, 7)
    pairs_35 = raw_pairs(prime, 35)
    assert negatives == (7, 35)
    assert jacobi_symbol(7, prime - 2) == -1
    assert pairs_7 == ((1, 1, 2, 21),)
    assert pairs_35 == ()
    assert 19 % 3 == 1

    canonical_d = 1
    canonical_targets = tuple(
        (target_d, a_value)
        for target_d in divisors(canonical_d)
        for a_value in divisors(target_d)
        if 4 * a_value * target_d < prime
    )
    assert canonical_targets == ((1, 1),)
    assert not tuple(target for target, _ in canonical_targets if target < canonical_d)

    return {
        "negative_divisors": list(negatives),
        "all_Q_endpoint_non_sinks": assert_no_fixed_chart_sink(prime),
        "gap_seven_certificate": gap_seven_certificate(prime),
        "raw_seven_certificate": raw_seven_certificate(prime),
        "gap_three_factor_absent": 19,
        "raw_pairs": {"7": [list(row) for row in pairs_7], "35": []},
        "source_switch_degeneracy": {
            "canonical_D": canonical_d,
            "target_lattice": [list(row) for row in canonical_targets],
            "strict_lower_target_exists": False,
        },
    }


def p97_fixture() -> dict[str, object]:
    """Check an independent gap-three leaf while its Jacobi label has no ray."""
    prime = 97
    negatives = negative_divisors(prime)
    assert negatives == (47,)
    assert raw_pairs(prime, 47) == ()
    return {
        "negative_divisors": list(negatives),
        "all_Q_endpoint_non_sinks": assert_no_fixed_chart_sink(prime),
        "gap_three_certificate": gap_three_certificate(prime, 5),
        "raw_pairs_47": [],
    }


def p193_fixture() -> dict[str, object]:
    """Check the three simple terminal gates can all be absent."""
    prime = 193
    negatives = negative_divisors(prime)
    assert negatives == (19, 95)
    assert (prime - 3) // 2 % 7 != 0
    assert raw_pairs(prime, 19) == ()
    assert raw_pairs(prime, 95) == ()
    assert (prime + 3) // 4 == 49
    return {
        "negative_divisors": list(negatives),
        "all_Q_endpoint_non_sinks": assert_no_fixed_chart_sink(prime),
        "gap_three_factor_absent": 49,
        "seven_label_absent": True,
        "raw_pairs": {"19": [], "95": []},
    }


def run_fixture() -> dict[str, object]:
    """Run the three named arithmetic examples only."""
    return {
        "scope_note": (
            "Three fixed G-anchor examples only; no prime search, global raw-ray "
            "bound, or E1--E5 recursion claim is tested.  The unique raw hit is "
            "checked as a D=1 terminal, not as a source-switch."
        ),
        "p_73": p73_fixture(),
        "p_97": p97_fixture(),
        "p_193": p193_fixture(),
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
