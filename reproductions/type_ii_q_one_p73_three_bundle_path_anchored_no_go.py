#!/usr/bin/env python3
"""Verify the p=73 three-bundle path-anchored capacity no-go."""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm, prod


PRIME = 73


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


def canonical_root_support() -> int:
    t = (PRIME - 1) // 24
    g = (PRIME + 1) // 2
    return g * (PRIME * PRIME * t - g)


def canonical_chart(support: int) -> tuple[int, int]:
    modulus = 4 * support
    R = (-pow(PRIME, -1, modulus)) % modulus
    K = (PRIME * R + 1) // 4
    if not (1 <= R < modulus and K % support == 0):
        raise AssertionError("canonical chart changed")
    return R, K


def complete_excess(value: int, capacity: int) -> int:
    capacity_factors = factorization(capacity)
    return prod(
        prime**exponent
        for prime, exponent in factorization(value).items()
        if exponent > capacity_factors.get(prime, 0)
    )


def path_anchored_bundle(support: int, selected: int) -> dict[str, int] | None:
    R, K = canonical_chart(support)
    if not (1 <= selected < R and gcd(selected, R) == 1):
        return None
    Q = complete_excess(selected, K)
    if Q <= 1:
        return None
    beta = selected // Q
    opposite_payload = (R - selected) * beta
    if not (
        K % opposite_payload == 0
        and gcd(Q, opposite_payload) == 1
        and K % Q != 0
    ):
        return None
    return {"R": R, "K": K, "selected": selected, "Q": Q, "beta": beta, "A_next": lcm(support, Q)}


def successors(support: int, root_support: int) -> list[dict[str, int]]:
    R, _ = canonical_chart(support)
    rows = []
    for selected in range(1, R):
        receipt = path_anchored_bundle(support, selected)
        if receipt is None:
            continue
        if receipt["A_next"] > support and root_support % receipt["A_next"] == 0:
            rows.append(receipt)
    return rows


def verify() -> dict[str, object]:
    root_support = canonical_root_support()
    if factorization(root_support) != {2: 1, 5: 2, 11: 1, 29: 1, 37: 1}:
        raise AssertionError("p=73 canonical root factorization changed")

    first_rows: list[dict[str, int]] = []
    for R0 in range(3, PRIME - 1):
        if (PRIME * R0 + 1) % 4:
            continue
        K0 = (PRIME * R0 + 1) // 4
        Q0 = complete_excess(R0 - 1, K0)
        beta0 = (R0 - 1) // Q0
        if (
            Q0 > 1
            and K0 % beta0 == 0
            and gcd(Q0, beta0) == 1
            and K0 % Q0 != 0
            and root_support % Q0 == 0
        ):
            first_rows.append({"R0": R0, "K0": K0, "Q0": Q0, "beta0": beta0, "A1": Q0})

    expected_first = [
        {"R0": 3, "K0": 55, "Q0": 2, "beta0": 1, "A1": 2},
        {"R0": 11, "K0": 201, "Q0": 10, "beta0": 1, "A1": 10},
        {"R0": 23, "K0": 420, "Q0": 11, "beta0": 2, "A1": 11},
        {"R0": 51, "K0": 931, "Q0": 50, "beta0": 1, "A1": 50},
        {"R0": 59, "K0": 1077, "Q0": 58, "beta0": 1, "A1": 58},
    ]
    if first_rows != expected_first:
        raise AssertionError("first path-anchored bundle map changed")

    second_rows: list[dict[str, int]] = []
    for first in first_rows:
        for receipt in successors(first["A1"], root_support):
            second_rows.append(
                {
                    "R0": first["R0"],
                    "A1": first["A1"],
                    "R1": receipt["R"],
                    "K1": receipt["K"],
                    "selected": receipt["selected"],
                    "Q1": receipt["Q"],
                    "beta1": receipt["beta"],
                    "A2": receipt["A_next"],
                }
            )
    expected_second = [
        {"R0": 3, "A1": 2, "R1": 7, "K1": 128, "selected": 5, "Q1": 5, "beta1": 1, "A2": 10},
        {"R0": 11, "A1": 10, "R1": 23, "K1": 420, "selected": 11, "Q1": 11, "beta1": 1, "A2": 110},
        {"R0": 11, "A1": 10, "R1": 23, "K1": 420, "selected": 22, "Q1": 11, "beta1": 2, "A2": 110},
        {"R0": 23, "A1": 11, "R1": 3, "K1": 55, "selected": 2, "Q1": 2, "beta1": 1, "A2": 22},
        {"R0": 51, "A1": 50, "R1": 63, "K1": 1150, "selected": 58, "Q1": 29, "beta1": 2, "A2": 1450},
    ]
    if second_rows != expected_second:
        raise AssertionError("second path-anchored bundle map changed")

    third_hits = []
    for second in second_rows:
        for receipt in successors(second["A2"], root_support):
            if receipt["A_next"] == root_support:
                third_hits.append({"second": second, "third": receipt})
    if third_hits:
        raise AssertionError("p=73 unexpectedly acquired a third path-anchored root bundle")

    return {
        "status": "verified",
        "p": PRIME,
        "A_root": root_support,
        "first_path_anchored_bundles": first_rows,
        "second_path_anchored_bundles": second_rows,
        "third_root_hits": third_hits,
        "scope": (
            "One p=73 control, exact low-anchor and canonical bottom-side enumeration for "
            "single-side path-anchored complete-excess bundles; no prime-range, denominator-range, "
            "or selector-history scan."
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
