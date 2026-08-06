#!/usr/bin/env python3
"""Verify fixed factor-pair strict descents and finite quadratic-ratio controls.

All checks are local identities, fixed factorizations, and finite residue boxes.
The script intentionally performs no prime-range scan and makes no coverage
claim beyond the displayed gaps and controls.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    """Use deterministic trial division for the small fixed controls."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def factorization(value: int) -> list[tuple[int, int]]:
    """Return the prime factorization of a positive fixed control integer."""
    if value <= 0:
        raise AssertionError("factorization expects a positive integer")
    factors: list[tuple[int, int]] = []
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def divisors(value: int) -> list[int]:
    """Enumerate divisors of one fixed factorized input."""
    values = [1]
    for prime, exponent in factorization(value):
        values = [
            divisor * prime_power
            for divisor in values
            for prime_power in (prime**power for power in range(exponent + 1))
        ]
    return values


def signed_ratio_box(value: int, modulus: int) -> set[int]:
    """Return all coprime-divisor ratios modulo one fixed prime modulus."""
    if not is_prime(modulus) or value % modulus == 0:
        raise AssertionError("signed ratio box requires a unit factorization")
    return {
        numerator * pow(denominator, -1, modulus) % modulus
        for numerator in divisors(value)
        for denominator in divisors(value)
        if gcd(numerator, denominator) == 1
    }


def quadratic_residues(modulus: int) -> set[int]:
    """Return the nonzero quadratic residues modulo an odd prime."""
    if not is_prime(modulus) or modulus == 2:
        raise AssertionError("quadratic residue control requires an odd prime")
    return {value * value % modulus for value in range(1, modulus)}


def assert_egyptian_identity(denominator: int, terms: tuple[int, int, int]) -> None:
    """Check 4/denominator against three positive displayed unit fractions."""
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def verify_factor_pair_descent(
    *, p: int, m: int, A: int, B: int, C: int
) -> dict[str, object]:
    """Verify one complete Type II factor pair and its two-tail strict lift."""
    if not is_prime(p) or not is_prime(m) or p % 4 != 1 or m % 4 != 3:
        raise AssertionError("input is not a legal prime/gap control")
    if not (3 <= m <= p - 2) or (p - 1) % (m + 1):
        raise AssertionError("gap does not admit the stated strict source")

    x = (p + m) // 4
    n = (p + m) // (m + 1)
    if 4 * x != p + m or (m + 1) * n != p + m:
        raise AssertionError("gap chart is not integral")
    if x != A * B * C or gcd(A, B) != 1 or A > B:
        raise AssertionError("factor-pair normal form failed")
    if (A + B) % m:
        raise AssertionError("factor-pair gap congruence failed")
    K = (A + B) // m
    d = A * A * C
    if x * x % d or d > x or (x + d) % m:
        raise AssertionError("Type II divisor conditions failed")

    g = gcd(d, x)
    recovered_A = d // g
    recovered_B = x // g
    recovered_C = g // recovered_A
    if (recovered_A, recovered_B, recovered_C) != (A, B, C):
        raise AssertionError("factor-pair normal form no longer recovers uniquely")

    descent = (x, A * C * K, B * C * K)
    terminal = (x, p * A * C * K, p * B * C * K)
    assert_egyptian_identity(n, descent)
    assert_egyptian_identity(p, terminal)
    if n >= p:
        raise AssertionError("descent target was not strict")

    return {
        "p": p,
        "m": m,
        "n": n,
        "x": x,
        "A": A,
        "B": B,
        "C": C,
        "K": K,
        "d": d,
        "descent_denominators": list(descent),
        "terminal_denominators": list(terminal),
    }


def verify_gap_eleven_companion(*, p: int, eta: int) -> dict[str, object]:
    """Check the d_II/d_I companion map on one fixed gap-eleven control."""
    if not is_prime(p) or p % 24 != 1:
        raise AssertionError("companion input is not a core prime")
    q = (p + 11) // 12
    x = 3 * q
    if 12 * q - 11 != p or 9 * q % eta or eta % 11 != 8:
        raise AssertionError("gap-eleven companion selector failed")

    d_ii = 9 * q // eta
    d_i = q * d_ii
    if d_ii > x or x * x % d_ii or (x + d_ii) % 11:
        raise AssertionError("companion Type II divisor failed")
    if x * x % d_i or (p * x + d_i) % 11:
        raise AssertionError("companion Type I divisor failed")

    type_i_terms = (
        x,
        (p * x + d_i) // 11,
        p * (x + p * x * x // d_i) // 11,
    )
    assert_egyptian_identity(p, type_i_terms)
    return {
        "p": p,
        "q": q,
        "eta": eta,
        "d_ii": d_ii,
        "d_i": d_i,
        "type_i_denominators": list(type_i_terms),
    }


PAIR_CONTROLS = (
    {
        "name": "gap7_complete_carrier",
        "p": 97,
        "m": 7,
        "A": 1,
        "B": 13,
        "C": 2,
        "descent": (26, 4, 52),
    },
    {
        "name": "gap11_non_r7_factor_pair",
        "p": 457,
        "m": 11,
        "A": 9,
        "B": 13,
        "C": 1,
        "descent": (117, 18, 26),
    },
    {
        "name": "gap11_square_borrowing",
        "p": 24481,
        "m": 11,
        "A": 13,
        "B": 471,
        "C": 1,
        "descent": (6123, 572, 20724),
    },
    {
        "name": "gap23_adjacent_exit",
        "p": 937,
        "m": 23,
        "A": 3,
        "B": 20,
        "C": 4,
        "descent": (240, 12, 80),
    },
)


def verify_ratio_carriers() -> dict[str, object]:
    """Check the finite residue carriers and the fixed miss controls."""
    carriers = {
        "m7_F2": (7, 2),
        "m11_F9": (11, 9),
        "m23_F12": (23, 12),
    }
    for name, (modulus, carrier) in carriers.items():
        if signed_ratio_box(carrier, modulus) != quadratic_residues(modulus):
            raise AssertionError(f"{name}: quadratic carrier table changed")

    negative_controls = {
        "gap11_q27_all_QR": (11, 81),
        "gap11_q79_insufficient_3_carrier": (11, 237),
        "gap23_q9_insufficient_two_adic_carrier": (23, 30),
    }
    misses: dict[str, list[int]] = {}
    for name, (modulus, x) in negative_controls.items():
        box = signed_ratio_box(x, modulus)
        if (-1) % modulus in box:
            raise AssertionError(f"{name}: fixed factor-pair miss changed")
        misses[name] = sorted(box)
    return {
        "quadratic_carriers": {
            name: sorted(signed_ratio_box(carrier, modulus))
            for name, (modulus, carrier) in carriers.items()
        },
        "negative_ratio_boxes": misses,
    }


def build_result() -> dict[str, object]:
    """Replay fixed identity, carrier, and boundary controls only."""
    receipts: list[dict[str, object]] = []
    for control in PAIR_CONTROLS:
        receipt = verify_factor_pair_descent(
            p=int(control["p"]),
            m=int(control["m"]),
            A=int(control["A"]),
            B=int(control["B"]),
            C=int(control["C"]),
        )
        if tuple(receipt["descent_denominators"]) != control["descent"]:
            raise AssertionError(f"{control['name']}: descent formula changed")
        receipts.append({"name": control["name"], "receipt": receipt})

    companion = verify_gap_eleven_companion(p=73, eta=63)
    return {
        "certificate_type": "factor_pair_carrier_strict_descent_v1",
        "scope": (
            "Four fixed Type II factor-pair controls, one gap-eleven Type I "
            "companion, and finite ratio boxes only; no coverage scan is run."
        ),
        "pair_controls": receipts,
        "gap_eleven_companion": companion,
        "ratio_controls": verify_ratio_carriers(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified factor-pair carrier strict-descent controls: m=7,11,23")


if __name__ == "__main__":
    main()
