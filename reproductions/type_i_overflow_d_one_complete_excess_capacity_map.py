#!/usr/bin/env python3
"""Verify fixed full-product d=1 complete-excess capacity receipts.

This is a focused algebraic verifier, not a prime or denominator search.  It
checks the exact support multiplier, the forced high-overflow rechart, and
keeps the primitive raw-p source gate separate from the p-free bundle gate.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt, lcm


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    denominator: int
    expected_Q: int
    expected_beta: int
    expected_multiplier: int
    expected_raw_source: bool
    expected_p_free_bundle: bool


FIXTURES = (
    Fixture("p73_n5_low_two_gate_pass", 73, 5, 179, 2, 179, True, True),
    Fixture("p97_n5_low_two_gate_pass", 97, 5, 239, 2, 239, True, True),
    Fixture("p73_n73_shared_valuation_block", 73, 73, 71, 74, 71, True, True),
    Fixture("p73_n145_raw_source_gate_fail", 73, 145, 5219, 2, 5219, False, True),
    Fixture("p73_n217_p_free_bundle_gate_fail", 73, 217, 7811, 2, 7811, True, False),
)


def factorization(value: int) -> list[tuple[int, int]]:
    if value <= 0:
        raise AssertionError("factorization requires a positive integer")
    result: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            result.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result.append((value, 1))
    return result


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    Q = 1
    for prime, exponent in factorization(value):
        if exponent > valuation(capacity, prime):
            Q *= prime**exponent
    return Q, value // Q


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    K = (prime * R + 1) // 4
    if not (1 <= R < modulus and K % support == 0):
        raise AssertionError("canonical chart normalization failed")
    return R, K


def audit(fixture: Fixture) -> dict[str, int | str | bool]:
    p = fixture.prime
    n = fixture.denominator
    A = (p * n - 1) // 4
    R = (p - 1) * n - 1
    K = A * (p - 1)
    T = (R - 1) // 2
    gcd_formula = gcd((p + 1) // 2, (n + 1) // 2)
    Q, beta = complete_excess(R - 1, K)
    M = lcm(A, Q)
    multiplier = M // A
    capacity_bound = (p - 1) ** 2 // 4
    raw_source_ok = R % p != 0
    p_free_bundle_ok = Q % p != 0

    if not (
        is_prime(p)
        and p % 24 == 1
        and n > 1
        and n % 4 == 1
        and p * n == 4 * A + 1
        and p * R + 1 == 4 * K
        and K % A == 0
        and p < R < 4 * A
        and R % 4 == 3
        and R - 1 == 2 * T
        and gcd(T, A) == gcd_formula
        and Q * beta == R - 1
        and beta > 0
        and K % beta == 0
        and gcd(Q, beta) == 1
        and K % Q != 0
        and Q // gcd(A, Q) == T // gcd_formula == multiplier
        and multiplier > 1
        and M > p * p > capacity_bound
        and raw_source_ok == (n % p != p - 1)
        and p_free_bundle_ok == (n % p != p - 2)
        and fixture.expected_Q == Q
        and fixture.expected_beta == beta
        and fixture.expected_multiplier == multiplier
        and fixture.expected_raw_source == raw_source_ok
        and fixture.expected_p_free_bundle == p_free_bundle_ok
    ):
        raise AssertionError(f"{fixture.name}: capacity formula receipt changed")

    if raw_source_ok:
        U, V, m = p, R * (p - 1) - p, p - 1
        if not (
            U + V == R * m
            and gcd(U, V) == 1
            and (U // p, (V + R) // p, (m + 1) // p) == (1, R - 1, 1)
        ):
            raise AssertionError(f"{fixture.name}: primitive raw-p source changed")
    elif gcd(p, R * (p - 1) - p) == 1:
        raise AssertionError(f"{fixture.name}: raw-source failure gate is not primitive")

    rechart_available = p_free_bundle_ok
    if rechart_available:
        R_M, K_M = canonical_chart(p, M)
        if not (
            M % A == 0
            and M % Q == 0
            and K_M % M == 0
            and R_M > p
            and K_M // M in range(1, p)
        ):
            raise AssertionError(f"{fixture.name}: p-free bundle rechart changed")
    elif gcd(p, 4 * M) == 1:
        raise AssertionError(f"{fixture.name}: p-free failure did not block rechart")

    low_denominator = 1 < n < p
    if low_denominator:
        if not (
            5 <= n <= p - 4
            and A < capacity_bound
            and raw_source_ok
            and p_free_bundle_ok
            and capacity_bound // A > capacity_bound // M == 0
        ):
            raise AssertionError(f"{fixture.name}: low-denominator exit gate changed")

    return {
        "name": fixture.name,
        "A": A,
        "R": R,
        "K": K,
        "T": T,
        "gcd_formula": gcd_formula,
        "Q": Q,
        "beta": beta,
        "multiplier": multiplier,
        "carrier_above_p_square": M > p * p,
        "raw_source_ok": raw_source_ok,
        "p_free_bundle_ok": p_free_bundle_ok,
        "low_denominator": low_denominator,
        "low_outer_rank_strict": low_denominator and capacity_bound // A > capacity_bound // M,
        "canonical_rechart_available": rechart_available,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    ready = sum(
        receipt["raw_source_ok"] and receipt["p_free_bundle_ok"] for receipt in receipts
    )
    low_ready = sum(
        receipt["low_denominator"]
        and receipt["raw_source_ok"]
        and receipt["p_free_bundle_ok"]
        for receipt in receipts
    )
    overlap = sum(receipt["gcd_formula"] > 1 for receipt in receipts)
    raw_failures = sum(not receipt["raw_source_ok"] for receipt in receipts)
    p_free_failures = sum(not receipt["p_free_bundle_ok"] for receipt in receipts)
    forced_high = sum(
        receipt["canonical_rechart_available"] and receipt["carrier_above_p_square"]
        for receipt in receipts
    )
    low_outer_rank = sum(receipt["low_outer_rank_strict"] for receipt in receipts)
    if (ready, low_ready, overlap, raw_failures, p_free_failures, forced_high, low_outer_rank) != (
        3,
        2,
        1,
        1,
        1,
        4,
        2,
    ):
        raise AssertionError("focused complete-excess capacity classification changed")
    print(
        "verified 3 p-source/p-free complete-excess capacity receipts, "
        "4 forced-high rechart receipts, 2 automatic low-denominator outer-rank exits, "
        "1 valuation-overlap control, and 2 independent p-gate boundaries"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
