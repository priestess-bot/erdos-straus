#!/usr/bin/env python3
"""Verify the H3 terminal-or-fourth-anchor gate on the q=1 C=2 residual.

This works with the 31 residue classes left after the affine terminal
refinement.  It proves exact H3 polynomial residues, a bounded obstruction
mask, and the terminal / clean-fourth-anchor / q=1-mask dispatch without a
prime-range scan.
"""

from __future__ import annotations

import argparse
from math import gcd

import sympy

from short_certificate import type_ii_raw_ray_certificate, verify_certificate
from type_ii_q_one_c2_19_phase_refined_affine_terminal_boundary import FINAL_RESIDUAL


STEP = 108_528
MODULUS = 2_261
RESIDUE_DENOMINATOR = 197_955_072
EASY_U = (1, 8, 36, 41, 43, 68, 85, 90, 99, 103, 111)
HARD_U = (5, 6, 15, 19, 22, 26, 27, 34, 40, 54, 57, 62, 69, 75, 78, 83, 92, 96, 104, 117)


def base_prime(u: int) -> int:
    return 912 * u + 769


def phase_u(prime: int) -> int:
    if prime % 912 != 769:
        raise AssertionError("input is not in the q=1 C=2 19 phase")
    return ((prime - 769) // 912) % 119


def selector_a(prime: int) -> int:
    value = (-1536 * pow(prime, -1, MODULUS)) % MODULUS
    if not 1 <= value < MODULUS:
        raise AssertionError("third-anchor selector was not canonical")
    return value


def h3_data(prime: int) -> dict[str, int]:
    """Rebuild H3 from the three pre-existing complete-excess anchors."""
    if prime % 24 != 1 or prime % 912 != 769:
        raise AssertionError("input is not a core phase parameter")
    a = selector_a(prime)
    f = 2 * prime * prime - 3 * prime - 1
    m0 = (prime - 1) * (2 * prime + 1) * f // 8
    k0 = 2 * m0
    r0 = (4 * k0 - 1) // prime
    q0 = (r0 - 1) // 2
    c1 = (2 * prime + 4) // 3
    m1 = m0 * q0
    k1 = m1 * c1
    r1 = (4 * k1 - 1) // prime
    q1 = (r1 - 1) // 2
    c2 = (13 * prime + 16) // 19
    m2 = m1 * q1
    k2 = m2 * c2
    r2 = (4 * k2 - 1) // prime
    q2 = (r2 - 1) // 2
    c3 = (1536 + a * prime) // MODULUS
    m3 = m2 * q2
    k3 = m3 * c3
    r3 = (4 * k3 - 1) // prime
    if not (
        prime * r0 + 1 == 4 * k0
        and prime * r1 + 1 == 4 * k1
        and prime * r2 + 1 == 4 * k2
        and prime * r3 + 1 == 4 * k3
        and m3 > (prime - 1) ** 2 // 4
        and 1 <= c3 <= prime - 2
        and prime % m3
        and prime % k3
    ):
        raise AssertionError("H3 reconstruction failed")
    return {
        "a": a,
        "M_2": m2,
        "Q_2": q2,
        "c_3": c3,
        "M_3": m3,
        "K_3": k3,
        "R_3": r3,
    }


def factor_primes(value: int) -> frozenset[int]:
    if value == 0:
        raise AssertionError("bounded factor mask unexpectedly vanished")
    return frozenset(sympy.factorint(abs(value)))


def bounded_mask(u: int) -> frozenset[int]:
    """Return every possible odd H3 obstruction prime for this u class."""
    base = base_prime(u)
    a = selector_a(base)
    mask = {prime for prime in factor_primes(1536 - a) if prime not in {2, 3, 7, 19}}
    # The denominator 2261 can only add 17 on a residual p=-1 (mod 17) ray.
    if base % 17 == 16:
        mask.add(17)
    if not (
        base % 7 in {1, 2, 4}
        and base % 3 == 1
        and base % 19 == 9
        and all(prime <= 1523 for prime in mask)
    ):
        raise AssertionError("bounded H3 obstruction mask changed")
    return frozenset(mask)


def phase_prime_factor_candidates(value: int, u: int) -> tuple[int, ...]:
    """Return phase primes in u's progression that divide one fixed constant."""
    base = base_prime(u)
    return tuple(
        prime
        for prime in sorted(factor_primes(value))
        if prime >= base and (prime - base) % STEP == 0 and prime % 24 == 1
    )


def symbolic_h3_residue_remainders() -> None:
    """Use exact polynomial arithmetic to derive the two H3 p-residues."""
    prime, a = sympy.symbols("prime a")
    f = 2 * prime**2 - 3 * prime - 1
    m0 = (prime - 1) * (2 * prime + 1) * f / 8
    k0 = 2 * m0
    r0 = sympy.cancel((4 * k0 - 1) / prime)
    q0 = sympy.cancel((r0 - 1) / 2)
    c1 = (2 * prime + 4) / 3
    m1 = sympy.cancel(m0 * q0)
    k1 = sympy.cancel(m1 * c1)
    r1 = sympy.cancel((4 * k1 - 1) / prime)
    q1 = sympy.cancel((r1 - 1) / 2)
    c2 = (13 * prime + 16) / 19
    m2 = sympy.cancel(m1 * q1)
    k2 = sympy.cancel(m2 * c2)
    r2 = sympy.cancel((4 * k2 - 1) / prime)
    q2 = sympy.cancel((r2 - 1) / 2)
    c3 = (1536 + a * prime) / MODULUS
    m3 = sympy.cancel(m2 * q2)
    k3 = sympy.cancel(m3 * c3)
    r3 = sympy.cancel((4 * k3 - 1) / prime)
    remainders = (
        RESIDUE_DENOMINATOR * r3 - 57 * (MODULUS * a - 8_470_528),
        RESIDUE_DENOMINATOR * (r3 - 1) - 57 * (MODULUS * a - 11_943_424),
    )
    modulus = sympy.Poly(prime, prime)
    for expression in remainders:
        polynomial = sympy.Poly(sympy.expand(expression), prime)
        if polynomial.rem(modulus).as_expr() != 0:
            raise AssertionError("H3 residue polynomial did not have zero p remainder")


def verify_finite_phase_exclusions() -> None:
    """Exclude the only finite phase-prime candidates for H3 source/E5 gates."""
    failures: list[tuple[str, int, tuple[int, ...]]] = []
    for u in sorted(FINAL_RESIDUAL):
        a = selector_a(base_prime(u))
        constants = {
            "raw_p_source": 57 * (MODULUS * a - 8_470_528),
            "p_free_bundle": 57 * (MODULUS * a - 11_943_424),
            "fourth_capacity_top": 3072 * RESIDUE_DENOMINATOR
            + MODULUS * 57 * (MODULUS * a - 11_943_424),
        }
        for name, value in constants.items():
            candidates = phase_prime_factor_candidates(value, u)
            if candidates:
                failures.append((name, u, candidates))
    if failures:
        raise AssertionError(f"an H3 finite phase exclusion failed: {failures}")


def dispatch_h3(prime: int) -> dict[str, object]:
    """Dispatch one actual residual phase prime at H3."""
    u = phase_u(prime)
    if u not in FINAL_RESIDUAL or not sympy.isprime(prime):
        raise AssertionError("input is not an actual 31-class residual phase prime")
    data = h3_data(prime)
    a = int(data["a"])
    c3 = int(data["c_3"])
    m3 = int(data["M_3"])
    k3 = int(data["K_3"])
    r3 = int(data["R_3"])
    w = (prime + 1) // 2
    g = gcd(w, c3)
    source_residue = 57 * (MODULUS * a - 8_470_528) * pow(
        RESIDUE_DENOMINATOR, -1, prime
    ) % prime
    bundle_residue = 57 * (MODULUS * a - 11_943_424) * pow(
        RESIDUE_DENOMINATOR, -1, prime
    ) % prime
    if not (
        r3 % prime == source_residue != 0
        and (r3 - 1) % prime == bundle_residue != 0
        and gcd(r3 - 1, k3) == 2 * g
        and set(factor_primes(g)) <= bounded_mask(u)
    ):
        raise AssertionError("H3 source, bundle, or bounded-mask identity failed")

    factorization = factor_primes(g)
    type_ii_factor = next((factor for factor in sorted(factorization) if factor % 4 == 3), None)
    if type_ii_factor is not None:
        certificate = type_ii_raw_ray_certificate(
            prime, 1, (type_ii_factor + 1) // 4, 1
        )
        if certificate is None or not verify_certificate(certificate):
            raise AssertionError("bounded H3 factor did not give its Type II terminal")
        return {
            "branch": "bounded_factor_type_ii_terminal",
            "u": u,
            "a": a,
            "g": g,
            "factor": type_ii_factor,
            "certificate": certificate,
        }

    if g > 1:
        if not all(factor % 4 == 1 for factor in factorization):
            raise AssertionError("nonterminal H3 mask was not q=1 shaped")
        return {
            "branch": "bounded_q_one_mask",
            "u": u,
            "a": a,
            "g": g,
            "mask": tuple(sorted(factorization)),
        }

    q3 = (r3 - 1) // 2
    if not (
        q3 > 1
        and q3 % 2 == 1
        and gcd(q3, k3) == 1
        and q3 % prime
        and r3 % prime
    ):
        raise AssertionError("clean H3 fourth-anchor bundle was not complete and p-free")
    m4 = m3 * q3
    c4 = c3 * pow(q3, -1, prime) % prime
    k4 = m4 * c4
    r4 = (4 * k4 - 1) // prime
    if not (
        1 <= c4 <= prime - 2
        and prime * r4 + 1 == 4 * k4
        and k4 // m4 == c4
        and m4 > m3
    ):
        raise AssertionError("clean H3 fourth-anchor target was not a strict macro endpoint")
    return {
        "branch": "clean_fourth_p_anchor",
        "u": u,
        "a": a,
        "g": g,
        "Q_3": q3,
        "c_4": c4,
        "R_4": r4,
    }


def verify() -> None:
    symbolic_h3_residue_remainders()
    verify_finite_phase_exclusions()
    if not (
        tuple(sorted(FINAL_RESIDUAL)) == tuple(sorted((*EASY_U, *HARD_U)))
        and len(EASY_U) == 11
        and len(HARD_U) == 20
        and all(not any(factor % 4 == 1 for factor in bounded_mask(u)) for u in EASY_U)
        and all(any(factor % 4 == 1 for factor in bounded_mask(u)) for u in HARD_U)
    ):
        raise AssertionError("H3 bounded-mask residue partition changed")

    clean = dispatch_h3(18_097)
    hard = dispatch_h3(14_449)
    terminal = dispatch_h3(402_049)
    if not (
        clean["branch"] == "clean_fourth_p_anchor"
        and clean["u"] == 19
        and clean["c_4"] == 13_680
        and hard == {"branch": "bounded_q_one_mask", "u": 15, "a": 431, "g": 5, "mask": (5,)}
        and terminal["branch"] == "bounded_factor_type_ii_terminal"
        and terminal["u"] == 83
        and terminal["factor"] == 11
        and terminal["certificate"].gap == 36_551
    ):
        raise AssertionError("H3 terminal-or-fourth-anchor controls changed")
    print(
        "verified q=1 C=2 H3 dispatch: bounded Type II terminal, "
        "clean fourth anchor, or bounded q=1 mask"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact H3 gate receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
