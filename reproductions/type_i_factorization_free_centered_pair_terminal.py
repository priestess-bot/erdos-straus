#!/usr/bin/env python3
"""Verify factorization-free centered-pair Type I terminal serializers.

A centered Type I hit is usually represented by a signed vector over the
complete prime support of K.  This verifier accepts the equivalent primitive
pair (u, v) directly: gcd(u, v) = 1, uv divides K, and u + v is a multiple of
R.  It deliberately uses only integer arithmetic, gcd, and exact rational
checks; it never factors K.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import gcd


@dataclass(frozen=True)
class Control:
    name: str
    prime: int
    modulus: int
    K: int
    u: int
    v: int
    expected_multiplier: int
    expected_gap: int
    expected_center_divisor: int
    expected_certificate_divisor: int
    expected_denominators: tuple[int, int, int]


CONTROLS = (
    Control(
        name="p73_r3_nontrivial_multiplier",
        prime=73,
        modulus=3,
        K=55,
        u=1,
        v=5,
        expected_multiplier=2,
        expected_gap=15,
        expected_center_divisor=11,
        expected_certificate_divisor=44,
        expected_denominators=(22, 110, 4_015),
    ),
    Control(
        name="p73_r23_full_excess_sink_pair",
        prime=73,
        modulus=23,
        K=420,
        u=2,
        v=21,
        expected_multiplier=1,
        expected_gap=7,
        expected_center_divisor=40,
        expected_certificate_divisor=10,
        expected_denominators=(20, 210, 30_660),
    ),
)


def serialize_centered_pair_terminal(
    *,
    prime: int,
    modulus: int,
    K: int,
    u: int,
    v: int,
) -> dict[str, int | bool | tuple[int, int, int]]:
    """Build a direct Type I terminal from a factorization-free pair receipt."""
    if prime <= 0 or prime % 24 != 1:
        raise ValueError("prime must be a positive core-prime candidate")
    if modulus < 3 or modulus % 4 != 3 or K <= 0:
        raise ValueError("chart must have R >= 3, R = 3 (mod 4), and K > 0")
    if prime * modulus + 1 != 4 * K or gcd(K, modulus) != 1:
        raise ValueError("chart identity or chart coprimality failed")
    if u <= 0 or v <= 0:
        raise ValueError("centered-pair coordinates must be positive")

    a, b = sorted((u, v))
    if a == b or gcd(a, b) != 1:
        raise ValueError("centered pair must have distinct coprime coordinates")
    if K % (a * b):
        raise ValueError("centered pair product must divide K")
    if (a + b) % modulus:
        raise ValueError("centered pair must be antipodal modulo R")
    if gcd(a, modulus) != 1 or gcd(b, modulus) != 1:
        raise AssertionError("a divisor of K cannot share a chart prime with R")

    multiplier = (a + b) // modulus
    c = K // (a * b)
    center_divisor = a * a * c
    gap_numerator = 4 * center_divisor + 1
    if gap_numerator % modulus:
        raise AssertionError("centered divisor did not produce an integral gap")
    gap = gap_numerator // modulus
    x_numerator = prime + gap
    if x_numerator % 4:
        raise AssertionError("Type I gap did not recover an integral x")
    x = x_numerator // 4
    certificate_divisor = multiplier * multiplier * c
    quotient = (a * prime + multiplier) // gap
    denominators = (
        multiplier * a * c,
        multiplier * b * c,
        prime * a * b * c,
    )

    checks = {
        "center_divisor_target": center_divisor % modulus == (-K) % modulus,
        "normal_form": prime == 4 * multiplier * a * c - gap,
        "normal_form_coprime": gcd(multiplier, a) == 1,
        "normal_form_quotient": (a * prime + multiplier) % gap == 0
        and quotient == b,
        "natural_gap": 3 <= gap <= prime - 2 and gap % 4 == 3,
        "certificate_divides_x_squared": x * x % certificate_divisor == 0,
        "certificate_congruence": (prime * x + certificate_divisor) % gap == 0,
        "unit_fraction_identity": sum(
            (Fraction(1, denominator) for denominator in denominators),
            Fraction(),
        )
        == Fraction(4, prime),
    }
    if not all(checks.values()):
        raise AssertionError(f"centered-pair terminal checks failed: {checks}")

    return {
        "factorization_free_verifier": True,
        "terminal_kind": "type_i_centered_pair",
        "recursive_edge_eligible": False,
        "a": a,
        "b": b,
        "multiplier": multiplier,
        "c": c,
        "gap": gap,
        "x": x,
        "center_divisor": center_divisor,
        "certificate_divisor": certificate_divisor,
        "denominators": denominators,
    }


def verify() -> None:
    receipts = []
    for control in CONTROLS:
        receipt = serialize_centered_pair_terminal(
            prime=control.prime,
            modulus=control.modulus,
            K=control.K,
            u=control.u,
            v=control.v,
        )
        expected = {
            "multiplier": control.expected_multiplier,
            "gap": control.expected_gap,
            "center_divisor": control.expected_center_divisor,
            "certificate_divisor": control.expected_certificate_divisor,
            "denominators": control.expected_denominators,
        }
        actual = {key: receipt[key] for key in expected}
        if actual != expected:
            raise AssertionError(f"{control.name}: terminal receipt changed")
        receipts.append(receipt)

    try:
        serialize_centered_pair_terminal(
            prime=73,
            modulus=3,
            K=55,
            u=5,
            v=11,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("a non-antipodal divisor pair was incorrectly accepted")

    if not all(bool(receipt["factorization_free_verifier"]) for receipt in receipts):
        raise AssertionError("factorization-free receipt label changed")
    print("verified 2 factorization-free centered-pair Type I terminals")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
