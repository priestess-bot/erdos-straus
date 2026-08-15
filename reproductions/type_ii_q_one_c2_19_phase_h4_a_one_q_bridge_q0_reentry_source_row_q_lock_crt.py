#!/usr/bin/env python3
"""Verify the q0 re-entry source-row/q-lock CRT boundary controls.

This is a static arithmetic verifier.  It does not construct an actual H4
predecessor, a maximal complete-excess payload, or an admitted macro edge.
"""

from __future__ import annotations

import argparse
from math import gcd

import sympy
from sympy.ntheory.modular import crt

from type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_nonminimal_d_lift_finite_phase_exclusion import (
    minimal_d_ray_screen,
)


def source_t_residue(p: int, q: int, gamma: int, q0: int, ell: int) -> int:
    """Return the unique t class forced by the full source row modulo 4(q-1)."""
    modulus = 4 * (q - 1)
    coefficient = p * gamma * q0 * q0
    if gcd(coefficient, modulus) != 1 or gcd(p, modulus) != 1:
        raise AssertionError("source-row coefficient lost its inverse")
    f_residue = ell * pow(coefficient, -1, modulus) % modulus
    return (f_residue - gamma) * pow(p, -1, modulus) % modulus


def q_lock_residue(q: int, d: int, divisor: int, gamma: int, rho: int) -> int:
    """Return the unique q-lock class for one unitary endpoint allocation."""
    if q % rho or gcd(rho, q // rho) != 1:
        raise AssertionError("rho is not unitary in q")
    other = q // rho
    if rho == 1:
        return (gamma - 2 * d * pow(divisor, -1, q)) % q
    if other == 1:
        return gamma % q
    residue, modulus = crt(
        [rho, other],
        [gamma % rho, (gamma - 2 * d * pow(divisor, -1, other)) % other],
    )
    if int(modulus) != q:
        raise AssertionError("unitary q-lock modulus changed")
    return int(residue)


def combined_t(
    p: int,
    q: int,
    d: int,
    divisor: int,
    gamma: int,
    q0: int,
    ell: int,
    rho: int,
    theta: int,
) -> tuple[int, int, int, int]:
    """Combine arbitrary p residue, q-lock, and full source row by CRT."""
    source_modulus = 4 * (q - 1)
    source = source_t_residue(p, q, gamma, q0, ell)
    lock = q_lock_residue(q, d, divisor, gamma, rho)
    if not (
        gcd(p, q) == 1
        and gcd(p, source_modulus) == 1
        and gcd(q, source_modulus) == 1
    ):
        raise AssertionError("three CRT moduli are no longer pairwise coprime")
    residue, modulus = crt([p, q, source_modulus], [theta % p, lock, source])
    expected_modulus = p * q * source_modulus
    if int(modulus) != expected_modulus:
        raise AssertionError("source-row CRT modulus changed")
    value = int(residue)
    if value == 0:
        value = expected_modulus
    return value, source, lock, expected_modulus


def reconstruct_static_row(
    p: int,
    d: int,
    q: int,
    divisor: int,
    ell: int,
    gamma: int,
    rho: int,
    theta: int,
) -> dict[str, int]:
    """Reconstruct the integer source row determined by the three CRT classes."""
    q0 = q // gamma
    t, source, lock, modulus = combined_t(
        p, q, d, divisor, gamma, q0, ell, rho, theta
    )
    factor = gamma + p * t
    xi = factor * divisor
    source_numerator = gamma * q0 * q0 * xi - 2 * d
    if source_numerator % (q - 1):
        raise AssertionError("source row stopped producing an integral R")
    residual = p * gamma * q0 * q0 * factor - ell
    if residual % (4 * (q - 1)):
        raise AssertionError("full source row stopped being divisible by 4(q-1)")
    k4 = divisor * (residual // (4 * (q - 1)))
    r4 = source_numerator // (q - 1)
    zeta = r4 - xi
    if not (
        r4 > xi > 0
        and zeta > 0
        and p * r4 + 1 == 4 * k4
        and k4 % divisor == 0
        and (q - 1) * r4 == gamma * q0 * q0 * xi - 2 * d
        and t % p == theta % p
        and t % q == lock
        and t % (4 * (q - 1)) == source
    ):
        raise AssertionError("static source-row reconstruction changed")
    return {
        "t": t,
        "modulus": modulus,
        "factor": factor,
        "xi": xi,
        "zeta": zeta,
        "r4": r4,
        "k4": k4,
    }


def verify_composite_q_static_family() -> int:
    """Exercise all unitary q allocations and both raw terminal classes."""
    p, d, q, divisor, ell = 12_409, 5, 1_241, 910, 135
    if not (
        sympy.isprime(p)
        and p % 24 == 1
        and q == 17 * 73
        and divisor == 2 * d * (4 * d * d - 2 * d + 1)
        and (2 * d * p - q + 1) == ell * divisor
    ):
        raise AssertionError("composite-q minimal-D fixture changed")

    controls = 0
    for gamma in (1, 17, 73):
        q0 = q // gamma
        b = 2 * gamma - 1
        if not (q0 > 1 and b > 0 and b % 2 == 1 and gcd(q, b + 1) == gamma):
            raise AssertionError("gamma/b static source data changed")
        raw_classes = (gamma * (b + 1), gamma * (b + 2))
        for rho in (1, 17, 73, q):
            for theta in raw_classes:
                row = reconstruct_static_row(
                    p, d, q, divisor, ell, gamma, rho, theta
                )
                if not (
                    gcd(row["xi"], row["zeta"]) == 1
                    and row["xi"] % p != 0
                    and row["zeta"] % p != 0
                    and gcd(q, row["xi"]) == rho
                    and gcd(q, row["zeta"]) == q // rho
                ):
                    raise AssertionError("static composite-q endpoint control changed")
                controls += 1
    if controls != 24:
        raise AssertionError("composite-q static control count changed")
    return controls


def verify_prime_phase_ray_controls() -> int:
    """Check the prime first points already present in three of the 17 rays."""
    expected = {
        (15, 65, 7_606_503_424_129),
        (78, 11, 2_025_421_441),
        (85, 179, 430_576_893_658_129),
    }
    records = {
        (u, d, p0)
        for u, _a, d, _delta, p0, _period in minimal_d_ray_screen()["rays"]
        if sympy.isprime(p0)
    }
    if records != expected:
        raise AssertionError(f"prime first points in the ray map changed: {records}")

    controls = 0
    for u, d, p in sorted(records):
        divisor = 2 * d * (4 * d * d - 2 * d + 1)
        q, remainder = divmod(p + 1, 2 * d)
        if remainder or not (p % 24 == 1 and p > divisor):
            raise AssertionError("phase-ray prime no longer has the minimal-D form")
        ell, remainder = divmod(2 * d * p - q + 1, divisor)
        if remainder:
            raise AssertionError("phase-ray divisor quotient changed")
        for theta in (2, 3):
            row = reconstruct_static_row(
                p, d, q, divisor, ell, 1, q, theta
            )
            if not (
                gcd(row["xi"], row["zeta"]) == 1
                and row["xi"] % p != 0
                and row["zeta"] % p != 0
                and gcd(q, row["xi"]) == q
                and gcd(q, row["zeta"]) == 1
            ):
                raise AssertionError("phase-ray static endpoint control changed")
            controls += 1
    if controls != 6:
        raise AssertionError("phase-ray static control count changed")
    return controls


def verify() -> None:
    composite_controls = verify_composite_q_static_family()
    phase_controls = verify_prime_phase_ray_controls()
    print(
        "verified q0 source-row/q-lock CRT boundary: "
        f"{composite_controls} composite-q static controls and "
        f"{phase_controls} prime phase-ray controls"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
