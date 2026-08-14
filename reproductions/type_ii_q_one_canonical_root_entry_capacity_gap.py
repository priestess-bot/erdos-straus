#!/usr/bin/env python3
"""Verify fixed controls for the q=1 canonical-root default-entry capacity gap."""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt, prod


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def complete_excess(value: int, capacity: int) -> int:
    capacity_factors = factorization(capacity)
    return prod(
        prime**exponent
        for prime, exponent in factorization(value).items()
        if exponent > capacity_factors.get(prime, 0)
    )


def canonical_root(prime: int) -> dict[str, int]:
    if not is_prime(prime) or prime % 24 != 1:
        raise AssertionError("control is not a core prime")
    t = (prime - 1) // 24
    g = (prime + 1) // 2
    T = prime * prime * t - g
    support = g * T
    K = support * (prime - 1)
    if (4 * K - 1) % prime:
        raise AssertionError("root chart integrality changed")
    R = (4 * K - 1) // prime
    X = (prime + 3) // 4
    B = (prime - 1) ** 2 // 4
    if not (
        t >= 3
        and 4 * K == prime * R + 1
        and support > 4 * prime * prime > B > prime
        and R > prime
        and gcd(X, K) == 1
    ):
        raise AssertionError("canonical root capacity gap changed")
    return {"t": t, "A_root": support, "K_root": K, "R_root": R, "X": X, "B_p": B}


def low_entry_control(prime: int, R0: int, root_support: int) -> dict[str, object]:
    if not (3 <= R0 <= prime - 2 and (prime * R0 + 1) % 4 == 0):
        raise AssertionError("not a legal low default-entry chart")
    K0 = (prime * R0 + 1) // 4
    Q = complete_excess(R0 - 1, K0)
    if not (Q >= 1 and (R0 - 1) % Q == 0 and Q < prime and Q < root_support):
        raise AssertionError("first bundle support bound changed")
    return {"R0": R0, "K0": K0, "Q": Q, "first_support": Q}


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    R = (-pow(prime, -1, modulus)) % modulus
    if not 1 <= R < modulus:
        raise AssertionError("canonical chart representative changed")
    K = (prime * R + 1) // 4
    if K % support:
        raise AssertionError("canonical support no longer divides its chart")
    return R, K


def second_step_envelope(prime: int, first_support: int, root_support: int) -> dict[str, int]:
    R1, K1 = canonical_chart(prime, first_support)
    c1 = K1 // first_support
    d1 = prime - c1
    bundle_upper = first_support * (R1 - 1)
    determinant_upper = first_support * d1
    r_chart_upper = first_support * (prime - 1)
    if not (
        1 <= c1 < prime
        and 1 <= d1 < prime
        and R1 < 4 * first_support < 4 * prime
        and determinant_upper < prime * prime
        and r_chart_upper < prime * prime
        and bundle_upper < 4 * prime * prime
        and max(bundle_upper, determinant_upper, r_chart_upper) < root_support
    ):
        raise AssertionError("two-step support envelope changed")
    return {
        "R1": R1,
        "c1": c1,
        "d1": d1,
        "bundle_upper": bundle_upper,
        "determinant_upper": determinant_upper,
        "r_chart_upper": r_chart_upper,
    }


def verify() -> dict[str, object]:
    controls = (73, 433, 1321)
    rows: list[dict[str, object]] = []
    for prime in controls:
        root = canonical_root(prime)
        low_entries = [
            low_entry_control(prime, 3, root["A_root"]),
            low_entry_control(prime, prime - 2, root["A_root"]),
        ]
        for entry in low_entries:
            entry["second_step_envelope"] = second_step_envelope(
                prime, entry["first_support"], root["A_root"]
            )
        rows.append({"p": prime, "root": root, "low_entries": low_entries})
    return {
        "status": "verified",
        "controls": rows,
        "scope": (
            "Fixed q=1 canonical-root arithmetic and two legal low-entry endpoints per "
            "control; no prime-range, denominator-range, or selector-history scan."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true", help="run the focused verifier")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    print(json.dumps(verify(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
