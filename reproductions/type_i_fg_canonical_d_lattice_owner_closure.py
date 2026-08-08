#!/usr/bin/env python3
"""Verify the fixed-D canonical source residual control."""

from __future__ import annotations

import argparse


def legendre_symbol(value: int, prime: int) -> int:
    residue = value % prime
    if residue == 0:
        return 0
    return -1 if pow(residue, (prime - 1) // 2, prime) == prime - 1 else 1


def verify() -> None:
    p = 57_399_241
    modulus = 59
    d_value = 41
    source_rows = {
        1: (3, 5, 7, 546_661),
        41: (5, 2_861, 4_013),
    }
    expected_values = {
        1: 57_399_405,
        41: 57_405_965,
    }

    if (p + 4 * d_value * 1, p + 4 * d_value * 41) != (
        expected_values[1],
        expected_values[41],
    ):
        raise AssertionError("fixed-D source numerators changed")

    canonical_rows = []
    for source_a, factors in source_rows.items():
        product = 1
        for factor in factors:
            product *= factor
            if expected_values[source_a] % factor:
                raise AssertionError("canonical factor no longer divides source numerator")
            if legendre_symbol(factor, modulus) != 1:
                raise AssertionError("fixed-D source factor left the square subgroup")
            canonical_rows.append((source_a, factor))
        if product != expected_values[source_a]:
            raise AssertionError("source factorization changed")

    if len(canonical_rows) != 7:
        raise AssertionError("canonical source row count changed")
    if legendre_symbol(2_693, modulus) != -1:
        raise AssertionError("escape representative changed")
    if all(legendre_symbol(factor, modulus) == 1 for _, factor in canonical_rows):
        residual_status = "CANONICAL_D_LATTICE_ESCAPE_OBSTRUCTED"
    else:
        raise AssertionError("canonical source image is no longer trivial in C2")

    lower_factor = 11_479_849
    if p + 4 != 5 * lower_factor:
        raise AssertionError("lower-layer factorization changed")
    if legendre_symbol(lower_factor, modulus) != -1:
        raise AssertionError("lower-layer nonresidue changed")
    scope_status = "LOWER_LAYER_SOURCE_OUTSIDE_CURRENT_UNIVERSE"

    print(
        "verified fixed-D F/G canonical closure: "
        f"{residual_status}; {scope_status}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
