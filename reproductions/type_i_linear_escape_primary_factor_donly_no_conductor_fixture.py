#!/usr/bin/env python3
"""Constant-size checks for the primary-factor D-only no-conductor split.

The fixture enumerates D-only parameters only for p=97 and two fixed factors.
It is not a search over fibers or primes and does not test any global descent.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt
import json


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


def d_only_parameters(prime: int, source: int) -> tuple[int, ...]:
    """Enumerate the exact finite D-only parameter set for one (p,n)."""
    residual = prime - source
    product = prime * source
    modulus = 4 * residual
    return tuple(
        d_value
        for d_value in divisors(product * product)
        if d_value < source * source
        and d_value % modulus == product % modulus
        and (product * product // d_value) % modulus == product % modulus
    )


def has_marked_tail(prime: int, source: int, d_value: int) -> bool:
    """Use the exact divisor criterion for one D-only marked fiber."""
    residual = prime - source
    product = prime * source
    a_value = (product - d_value) // (4 * residual)
    m_value = 4 * a_value - source
    s_value = source * a_value
    common = gcd(m_value, s_value)
    mu = m_value // common
    sigma = s_value // common
    return any(
        divisor % mu == (-sigma) % mu for divisor in divisors(sigma * sigma)
    )


def raw_factor_rows(prime: int, factor: int) -> tuple[tuple[int, int, int, int], ...]:
    """Enumerate the finite raw-factor Type II menu for one h."""
    if factor % 4 != 3:
        raise ValueError("raw Type II factor requires factor == 3 (mod 4)")
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


def h_three_fixture() -> dict[str, object]:
    """Check the scale contradiction for h=3 on one admissible fiber."""
    prime = 97
    shift = 2
    factor = 3
    source = (prime + 4 * shift) // factor
    parameters = d_only_parameters(prime, source)
    non_source = tuple(
        d_value for d_value in parameters if source * source % d_value
    )
    x_value = (prime + factor) // 4

    assert prime + 4 * shift == 105
    assert source == 35
    assert source < 2 * prime // 3
    assert source <= 4 * prime // 5
    assert non_source == ()
    assert x_value == 25 and x_value * x_value % shift != 0
    assert raw_factor_rows(prime, factor) == ()

    return {
        "p": prime,
        "s": shift,
        "h": factor,
        "n": source,
        "n_over_2p_over_3": True,
        "non_source_D_only_parameters": list(non_source),
        "gap_h_divisibility": False,
        "raw_factor_rows": [],
    }


def h_one_fixture() -> dict[str, object]:
    """Check the h=1 mod 4 branch is routed to the existing no-go."""
    prime = 97
    shift = 2
    factor = 5
    source = (prime + 4 * shift) // factor
    parameters = d_only_parameters(prime, source)
    non_source = tuple(
        d_value for d_value in parameters if source * source % d_value
    )

    assert source == 21 and source % 4 == 1
    assert all(not has_marked_tail(prime, source, d_value) for d_value in non_source)

    return {
        "p": prime,
        "s": shift,
        "h": factor,
        "n": source,
        "non_source_D_only_parameters": list(non_source),
        "non_source_parameter_count": len(non_source),
        "all_non_source_marked_fibers_empty": True,
        "raw_factor_menu": "not_applicable",
    }


def run_fixture() -> dict[str, object]:
    """Run the two fixed h modulo four branches."""
    return {
        "scope_note": (
            "Two fixed factors of p+4s only; this is not a source-menu scan or "
            "a global D-only audit."
        ),
        "h_mod_3": h_three_fixture(),
        "h_mod_1": h_one_fixture(),
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
