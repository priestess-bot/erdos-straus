#!/usr/bin/env python3
"""Verify the finite secondary q-lock exclusion after the H4 s=0 q swap.

The enumerated q menu is forced by the q-lock divisibility lemma.  It is not
a denominator, Reach-graph, or historical-prime scan.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt

import sympy

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    FINAL_RESIDUAL,
    selector_a,
)


MAX_DELTA = 1_535
PHASE_MODULUS = 912
PHASE_RESIDUE = 769
PHASE_RIGHT_HAND_SIDE = PHASE_RESIDUE + 1
PHASE_PERIOD = 119
EXPECTED_RESIDUAL_ARITHMETIC_RECORDS = (
    (14_449, 1_445, 17, 5, 15, 1_105, 198, 3_994, 123),
    (14_449, 1_445, 17, 5, 15, 1_105, 8_186, 163_754, 3),
    (14_449, 1_445, 289, 5, 15, 1_105, 417_547, 8_351_518, 1),
)


@dataclass(frozen=True)
class LockControl:
    prime: int
    d: int
    e: int
    q: int
    t: int
    expected_xi: int
    expected_quotient: int
    expected_phase_u: int | None
    expected_provenance: bool


LOCK_CONTROLS = (
    # The q-lock equations are not a formal contradiction outside the phase.
    LockControl(409, 41, 1, 5, 1, 22, 37, None, False),
    # The base 19-phase alone is insufficient: u=0 is terminal-first removed.
    LockControl(769, 35, 5, 11, 1, 120, 64, 0, True),
    # Even a residual phase hit is excluded unless H4 provenance d | Delta holds.
    LockControl(14_449, 1_445, 17, 5, 198, 3_994, 123, 15, False),
)


def positive_divisors(value: int) -> tuple[int, ...]:
    result: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        result.append(divisor)
        paired = value // divisor
        if paired != divisor:
            result.append(paired)
    return tuple(sorted(result))


def phase_u(prime: int) -> int:
    if prime % PHASE_MODULUS != PHASE_RESIDUE:
        raise AssertionError("prime is outside the q=1 C=2 19 phase")
    return ((prime - PHASE_RESIDUE) // PHASE_MODULUS) % PHASE_PERIOD


def phase_q_candidates(d: int) -> range:
    """Return q with p=2*d*q-1 in the base 19 phase and q<4*d^2."""
    common = gcd(2 * d, PHASE_MODULUS)
    if PHASE_RIGHT_HAND_SIDE % common:
        return range(0)

    modulus = PHASE_MODULUS // common
    coefficient = (2 * d // common) % modulus
    right_hand_side = (PHASE_RIGHT_HAND_SIDE // common) % modulus
    residue = pow(coefficient, -1, modulus) * right_hand_side % modulus
    first = residue or modulus
    if first < 3:
        first += ((3 - first + modulus - 1) // modulus) * modulus
    return range(first, 4 * d * d, modulus)


def audit_control(control: LockControl) -> dict[str, int | bool | None]:
    p = control.prime
    d = control.d
    e = control.e
    q = control.q
    t = control.t
    h = 2 * e
    xi = h + q * (q - 1) * t
    dividend = p * h - q + 1
    quotient, remainder = divmod(dividend, xi)
    in_phase = p % PHASE_MODULUS == PHASE_RESIDUE
    u = phase_u(p) if in_phase else None
    delta = abs(1_536 - selector_a(p)) if in_phase else None
    provenance = bool(delta and delta % d == 0)

    if not (
        sympy.isprime(p)
        and p % 24 == 1
        and (p + 1) // 2 == d * q
        and q > 1
        and e in positive_divisors(d)
        and t >= 1
        and q <= 4 * d * e - 1
        and xi == control.expected_xi
        and remainder == 0
        and quotient == control.expected_quotient
        and u == control.expected_phase_u
        and provenance == control.expected_provenance
    ):
        raise AssertionError("secondary q-lock algebraic control changed")

    return {
        "p": p,
        "d": d,
        "e": e,
        "q": q,
        "t": t,
        "xi": xi,
        "u": u,
        "provenance": provenance,
    }


def finite_phase_screen() -> dict[str, object]:
    q_parameters = 0
    phase_primes = 0
    residual_phase_parameters = 0
    provenance_parameters = 0
    residual_t_trials = 0
    provenance_t_trials = 0
    residual_arithmetic_records: list[tuple[int, ...]] = []
    actual_arithmetic_records: list[tuple[int, ...]] = []

    for d in range(1, MAX_DELTA + 1):
        for q in phase_q_candidates(d):
            q_parameters += 1
            p = 2 * d * q - 1
            if not sympy.isprime(p):
                continue
            phase_primes += 1
            u = phase_u(p)
            if u not in FINAL_RESIDUAL:
                continue
            residual_phase_parameters += 1

            delta = abs(1_536 - selector_a(p))
            provenance = delta > 0 and delta % d == 0
            if provenance:
                provenance_parameters += 1

            for e in positive_divisors(d):
                if q > 4 * d * e - 1:
                    continue
                h = 2 * e
                dividend = p * h - q + 1
                max_t = (dividend - h) // (q * (q - 1))
                residual_t_trials += max_t
                if provenance:
                    provenance_t_trials += max_t

                for t in range(1, max_t + 1):
                    xi = h + q * (q - 1) * t
                    quotient, remainder = divmod(dividend, xi)
                    if remainder:
                        continue
                    record = (p, d, e, q, u, delta, t, xi, quotient)
                    residual_arithmetic_records.append(record)
                    if provenance:
                        actual_arithmetic_records.append(record)

    result = {
        "q_parameters": q_parameters,
        "phase_primes": phase_primes,
        "residual_phase_parameters": residual_phase_parameters,
        "provenance_parameters": provenance_parameters,
        "residual_t_trials": residual_t_trials,
        "provenance_t_trials": provenance_t_trials,
        "residual_arithmetic_records": tuple(residual_arithmetic_records),
        "actual_arithmetic_records": tuple(actual_arithmetic_records),
    }
    expected = {
        "q_parameters": 3_345_232,
        "phase_primes": 534_967,
        "residual_phase_parameters": 149_977,
        "provenance_parameters": 524,
        "residual_t_trials": 5_273_881,
        "provenance_t_trials": 5_576,
        "residual_arithmetic_records": EXPECTED_RESIDUAL_ARITHMETIC_RECORDS,
        "actual_arithmetic_records": (),
    }
    if result != expected:
        raise AssertionError(f"secondary q-lock finite screen changed: {result}")
    return result


def verify() -> None:
    controls = tuple(audit_control(control) for control in LOCK_CONTROLS)
    screen = finite_phase_screen()
    if controls != (
        {"p": 409, "d": 41, "e": 1, "q": 5, "t": 1, "xi": 22, "u": None, "provenance": False},
        {"p": 769, "d": 35, "e": 5, "q": 11, "t": 1, "xi": 120, "u": 0, "provenance": True},
        {"p": 14_449, "d": 1_445, "e": 17, "q": 5, "t": 198, "xi": 3_994, "u": 15, "provenance": False},
    ):
        raise AssertionError("secondary q-lock controls changed")
    if screen["actual_arithmetic_records"]:
        raise AssertionError("an actual secondary q-lock arithmetic candidate appeared")
    print("verified finite secondary q-lock screen with zero actual H4 candidates")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact finite q-lock screen")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
