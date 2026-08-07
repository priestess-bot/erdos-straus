#!/usr/bin/env python3
"""Verify a q=19 phase-compatible Type-II candidate fiber at core-19 v=5."""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import gcd, isqrt


P = 1_202_376_916_441
R = 5_210_299_971_231
MU0 = 13
MU1 = 4_387_621_028_405
D = 6_303
D_STAR = 6_303
A = 573
MODULUS = 4 * D_STAR
Q = 19
ZETA = 150
SOURCE_A0 = 3
SOURCE_A1 = 573
N_FACTORS = ((17, 1), (19, 3), (53, 2), (3_671, 1))


def is_prime(value: int) -> bool:
    """Use trial division only for the fixed factorization witnesses."""
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


def valuation(value: int, prime: int) -> int:
    """Return the finite valuation of a nonzero integer."""
    if value == 0:
        raise AssertionError("the zero difference has no finite valuation")
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def divisors_from_factorization(
    factors: tuple[tuple[int, int], ...],
) -> list[tuple[tuple[int, ...], int]]:
    """Enumerate the 48 divisors of the declared candidate N."""
    values: list[tuple[tuple[int, ...], int]] = []
    for exponents in product(*(range(power + 1) for _, power in factors)):
        value = 1
        for (prime, _), exponent in zip(factors, exponents):
            value *= prime**exponent
        values.append((exponents, value))
    return values


def multiplicative_order(value: int, modulus: int) -> int:
    """Return a small exact multiplicative order for the fixed q=19 block."""
    if gcd(value, modulus) != 1:
        raise AssertionError("order requested for a nonunit")
    residue = 1
    for exponent in range(1, modulus + 1):
        residue = residue * value % modulus
        if residue == 1:
            return exponent
    raise AssertionError("unit order did not close")


def chi(value: int) -> int:
    """Project a unit modulo 25212 to the order-19 component modulo 191."""
    if gcd(value, MODULUS) != 1:
        raise AssertionError("character requested for a nonunit")
    return pow(value, 10, 191)


def zeta_exponent(value: int) -> int:
    """Decode a value in the declared order-19 character image."""
    table = {pow(ZETA, exponent, 191): exponent for exponent in range(19)}
    return table[value]


def verify_candidate_fiber() -> dict[str, object]:
    """Check the divisor lattice, source labels, range, and shared-q ledger."""
    s = A * D_STAR
    b0 = D * SOURCE_A0
    b1 = D * SOURCE_A1
    N0 = P + 4 * b0
    N = P + 4 * s
    if not (
        D == D_STAR == 3 * 11 * 191
        and A == 3 * 191
        and D_STAR % A == 0
        and D_STAR // A == 11
        and 4 * s == 14_446_476 < P
        and b0 == 18_909
        and b1 == s == 3_611_619
        and D % SOURCE_A0 == D % SOURCE_A1 == 0
        and D // SOURCE_A0 == 11 * 191
        and D // SOURCE_A1 == 11
        and 4 * b0 < P
        and 4 * b1 < P
        and N0 == 19 * 45_667 * 1_385_749
        and N == 17 * 19**3 * 53**2 * 3_671
        and N % MODULUS == P % MODULUS
        and Q % MODULUS != 0
        and gcd(Q, MODULUS) == 1
    ):
        raise AssertionError("v=5 candidate fiber arithmetic changed")
    e0 = valuation(N0, Q)
    e1 = valuation(N, Q)
    delta = s - b0
    ell0 = min(e0, valuation(delta, Q))
    ell1 = e1
    V = valuation(N, Q)
    if not (
        e0 == 1
        and e1 == 3
        and delta == 3_592_710 == 2 * 3**2 * 5 * 11 * 19 * 191
        and ell0 == 1
        and ell1 == 3
        and V == 3
        and min(ell0 + ell1, V) == 3
    ):
        raise AssertionError("v=5 shared q=19 ledger changed")
    return {
        "D": D,
        "D_star": D_STAR,
        "A": A,
        "s": s,
        "modulus": MODULUS,
        "source_labels": {"a0": SOURCE_A0, "b0": b0, "a1": SOURCE_A1, "b1": b1},
        "source_heights": {"e0": e0, "e1": e1},
        "shared_q19_ledger": {
            "ell0": ell0,
            "ell1": ell1,
            "L": ell0 + ell1,
            "V": V,
            "d": 3,
            "scope": "replayable integer depth only; not a count of raw requests or physical slots",
        },
        "N": N,
    }


def verify_phase_compatible_cofactors() -> dict[str, object]:
    """Match the two signed raw phases to one candidate-fiber q=19 chain."""
    candidate = verify_candidate_fiber()
    N = int(candidate["N"])
    H0 = 53 * 3_671
    H1 = Q * H0
    relative = MU1 * pow(MU0, -1, R) % R
    if not (
        H0 == 194_563
        and H1 == 3_696_697
        and N % H0 == 0
        and N % H1 == 0
        and all(N % (H0 * Q**exponent) == 0 for exponent in range(4))
        and all(gcd(H0 * Q**exponent, MODULUS) == 1 for exponent in range(4))
        and pow(ZETA, 19, 191) == 1
        and chi(H0) == pow(ZETA, 16, 191) == 121
        and chi(Q) == pow(ZETA, 11, 191) == 52
        and chi(H1) == pow(ZETA, 8, 191) == 180
        and pow(MU0, 10, 191) == pow(ZETA, 16, 191)
        and pow(MU1, 10, 191) == pow(ZETA, 8, 191)
        and pow(relative, 10, 191) == pow(ZETA, 11, 191)
        and chi(H0) == pow(MU0, 10, 191)
        and chi(H1) == pow(MU1, 10, 191)
        and chi(Q) == pow(relative, 10, 191)
        and multiplicative_order(Q, MODULUS) == 190
    ):
        raise AssertionError("v=5 signed phase-compatible cofactor chain changed")
    block = {pow(Q, exponent, MODULUS) for exponent in range(4)}
    stabilizers = [
        residue
        for residue in block
        if {residue * value % MODULUS for value in block} == block
    ]
    if stabilizers != [1]:
        raise AssertionError("the isolated q=19 block unexpectedly gained a stabilizer")
    return {
        "H0": H0,
        "H1": H1,
        "raw_marks": {"mu0": MU0, "mu1": MU1, "relative": relative},
        "character_exponents": {"H0_and_mu0": 16, "q19_and_relative": 11, "H1_and_mu1": 8},
        "q19_block": [pow(Q, exponent, MODULUS) for exponent in range(4)],
        "isolated_block_stabilizer": stabilizers,
    }


def verify_terminal_boundary() -> dict[str, object]:
    """Exhaust this one candidate N, not all Type-II parameters for p."""
    candidate = verify_candidate_fiber()
    N = int(candidate["N"])
    N0 = P + 4 * D * SOURCE_A0
    H0 = 53 * 3_671
    factors = divisors_from_factorization(N_FACTORS)
    if not (
        all(is_prime(prime) for prime, _ in N_FACTORS)
        and len(factors) == 48
        and all(gcd(value, MODULUS) == 1 for _, value in factors)
        and N0 % H0 == 26_822
        and pow(-1, 10, 191) == 1
    ):
        raise AssertionError("v=5 candidate-fiber boundary setup changed")
    phase_zero = [
        {"exponents": list(exponents), "factor": value}
        for exponents, value in factors
        if chi(value) == 1
    ]
    target_hits = [value for _, value in factors if value % MODULUS == MODULUS - 1]
    expected_phase_zero = [
        {"exponents": [0, 0, 0, 0], "factor": 1},
        {"exponents": [0, 1, 2, 0], "factor": 53_371},
        {"exponents": [0, 2, 1, 1], "factor": 70_237_243},
    ]
    if not (
        phase_zero == expected_phase_zero
        and all(item["factor"] % 3 == 1 for item in phase_zero)
        and not target_hits
    ):
        raise AssertionError("v=5 candidate fiber unexpectedly reached the Type-II target")
    return {
        "phase_zero_factors": phase_zero,
        "target_residue": MODULUS - 1,
        "target_hits": target_hits,
        "reason": "a target factor has chi=1, but every chi=1 divisor is 1 modulo 3",
        "source_gap": "H0 does not divide p+4*b0, so the two matched cofactors are not two raw source blocks",
    }


def build_result() -> dict[str, object]:
    """Build a phase-compatible candidate fiber, deliberately not an adapter."""
    return {
        "certificate_type": "v5_q19_phase_compatible_candidate_fiber_v1",
        "status": "analysis_evidence_only",
        "candidate_fiber": verify_candidate_fiber(),
        "phase_compatible_cofactors": verify_phase_compatible_cofactors(),
        "terminal_boundary": verify_terminal_boundary(),
        "missing_for_adapter_or_capacity": [
            "raw-to-(a,b) functor on a complete source universe",
            "independent physical source slots for the two raw leaves",
            "a third request and layer allocation before d=3 can be priced",
            "demand_to_slot and target-odd carrier",
            "E4/E5 and terminal-first clearance",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified v=5 q=19 phase-compatible candidate fiber")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
