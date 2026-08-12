#!/usr/bin/env python3
"""Verify the C=4 canonical G-stutter boundary on p = 25 (mod 48)."""

from __future__ import annotations

import argparse
from math import gcd, lcm

import sympy

import type_i_bottom_sink_scc_complete_excess_bundle as bottom
from type_i_a2_b27_square_only_terminal_ray import nine_route_dispatch


def c4_plus_boundary(prime: int) -> dict[str, int]:
    """Build the least C=4 support for the p = 9 (mod 16) branch."""
    if not sympy.isprime(prime) or prime % 48 != 25:
        raise ValueError("expected a core prime congruent to 25 modulo 48")
    bound = (prime - 1) ** 2 // 4
    R = 4 * prime + 3
    support = (prime * R + 1) // 16
    K = 4 * support
    if not (
        16 * support == prime * R + 1
        and support > bound
        and support - prime < bound
        and 4 * K == prime * R + 1
        and K // support == 4
    ):
        raise AssertionError("C=4 plus boundary formulas failed")
    return {"p": prime, "B": bound, "R": R, "A": support, "K": K}


def centered_hit(*, R: int, K: int) -> bool:
    """Test the finite centered Type-I box only on named controls."""
    residues = {1}
    for q, exponent in bottom.factorization(K).items():
        residues = {
            value * pow(q, coordinate, R) % R
            for value in residues
            for coordinate in range(-exponent, exponent + 1)
        }
    return R - 1 in residues


def canonical_stutter(boundary: dict[str, int]) -> dict[str, int]:
    """Construct the anchor complete-excess macro with unchanged cofactor."""
    prime, R, support, K = (
        boundary["p"],
        boundary["R"],
        boundary["A"],
        boundary["K"],
    )
    Q = 2 * prime + 1
    beta = residual = 2
    M = lcm(support, Q)
    target_R, target_K = bottom.canonical_chart(prime, M)
    if not (
        Q * beta == R - 1
        and gcd(Q, residual) == 1
        and K % residual == 0
        and K % Q != 0
        and gcd(support, Q) == 1
        and M == support * Q
        and target_R == R * Q + 2
        and target_K == 4 * M
        and target_K // M == K // support == 4
    ):
        raise AssertionError("C=4 canonical complete-excess stutter changed")
    return {
        "Q": Q,
        "beta": beta,
        "residual": residual,
        "M": M,
        "target_R": target_R,
        "target_K": target_K,
        "source_cofactor": K // support,
        "target_cofactor": target_K // M,
    }


def two_anchor_compression(boundary: dict[str, int]) -> dict[str, int]:
    """Compose the next canonical anchor and recover a 4-to-2 chart drop."""
    prime, R0, A0 = boundary["p"], boundary["R"], boundary["A"]
    first = canonical_stutter(boundary)
    R1, A1, Q0 = first["target_R"], first["M"], first["Q"]
    K1 = 4 * A1
    Q1 = (R1 - 1) // 2
    A2 = A1 * Q1
    R2, K2 = bottom.canonical_chart(prime, A2)
    if not (
        R1 == R0 * Q0 + 2
        and Q1 == Q0 + 16 * A0
        and R1 - 1 == 2 * Q1
        and gcd(Q1, K1) == gcd(A1, Q1) == 1
        and K1 % 2 == 0
        and K1 % Q1 != 0
        and R2 == (R1 * Q1 + 2 + R0) // 2
        and 2 * R2 == R1 * Q1 + 2 + R0
        and K2 == 2 * A2
        and 4 * K2 == prime * R2 + 1
    ):
        raise AssertionError("C=4 two-anchor compression changed")
    return {
        "Q0": Q0,
        "R1": R1,
        "A1": A1,
        "Q1": Q1,
        "A2": A2,
        "R2": R2,
        "K2": K2,
        "source_cofactor": 4,
        "intermediate_cofactor": K1 // A1,
        "target_cofactor": K2 // A2,
    }


def g_separator(*, R: int, K: int) -> bool:
    """Check the Jacobi G separator on one finite named chart."""
    values = [bottom.jacobi_symbol(q, R) for q in bottom.factorization(K)]
    return all(value == 1 for value in values) and bottom.jacobi_symbol(-1, R) == -1


def verify() -> None:
    # p=73 proves that the chart arithmetic is not tied to a particular
    # terminal dispatch outcome; p=2137 is the residual G control.
    first = c4_plus_boundary(73)
    control = c4_plus_boundary(2137)
    assert first == {"p": 73, "B": 1296, "R": 295, "A": 1346, "K": 5384}
    assert control == {
        "p": 2137,
        "B": 1140624,
        "R": 8551,
        "A": 1142093,
        "K": 4568372,
    }
    assert canonical_stutter(first) == {
        "Q": 147,
        "beta": 2,
        "residual": 2,
        "M": 197862,
        "target_R": 43367,
        "target_K": 791448,
        "source_cofactor": 4,
        "target_cofactor": 4,
    }
    assert two_anchor_compression(first) == {
        "Q0": 147,
        "R1": 43367,
        "A1": 197862,
        "Q1": 21683,
        "A2": 4290241746,
        "R2": 470163479,
        "K2": 8580483492,
        "source_cofactor": 4,
        "intermediate_cofactor": 4,
        "target_cofactor": 2,
    }
    stutter = canonical_stutter(control)
    assert stutter == {
        "Q": 4275,
        "beta": 2,
        "residual": 2,
        "M": 4882447575,
        "target_R": 36555527,
        "target_K": 19529790300,
        "source_cofactor": 4,
        "target_cofactor": 4,
    }
    assert two_anchor_compression(control) == {
        "Q0": 4275,
        "R1": 36555527,
        "A1": 4882447575,
        "Q1": 18277763,
        "A2": 89240219635774725,
        "R2": 334076629427327,
        "K2": 178480439271549450,
        "source_cofactor": 4,
        "intermediate_cofactor": 4,
        "target_cofactor": 2,
    }
    assert g_separator(R=control["R"], K=control["K"])
    assert not centered_hit(R=control["R"], K=control["K"])
    assert not centered_hit(R=stutter["target_R"], K=stutter["target_K"])
    assert nine_route_dispatch(p=2137)["branch"] == "nine_route_residual"
    factors = bottom.factorization(control["K"])
    adjacency, _labels = bottom.bottom_graph(control["R"], factors)
    sinks = bottom.sink_components(adjacency)
    assert len(sinks) == 1 and len(sinks[0]) == 2801
    assert (1, control["R"] - 1) in sinks[0]
    source = (control["p"], control["R"] * (control["p"] - 1) - control["p"], control["p"] - 1)
    destination, shift, common = bottom.formal_transition(source, control["p"], control["R"], factors)
    assert source == (2137, 18262799, 2136)
    assert destination == (1, 8550, 1) and shift == 1 and common == 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()
    print("verified C=4 canonical G-stutter boundary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
