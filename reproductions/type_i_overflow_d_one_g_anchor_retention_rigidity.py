#!/usr/bin/env python3
"""Verify focused d=1 full-product support-retention rigidity receipts.

The proof is the divisibility argument in the paired claim. These fixed
receipts distinguish the unique n=1 boundary, low numerical support with
non-divisible ledger, and partial (rather than coprime) support loss.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    denominator: int
    expected_overflow: bool
    expected_support_divides_g_capacity: bool
    expected_shared_support: int
    expected_loss_factor: int


FIXTURES = (
    Fixture("unique_n_one_non_overflow_boundary", 73, 1, False, True, 18, 1),
    Fixture("p73_low_support_coprime_loss", 73, 5, True, False, 1, 91),
    Fixture("p73_low_support_partial_loss", 73, 9, True, False, 4, 41),
    Fixture("p97_low_support_coprime_loss", 97, 5, True, False, 1, 121),
    Fixture("p97_high_support_loss", 97, 101, True, False, 1, 2449),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def audit(fixture: Fixture) -> dict[str, int | str | bool]:
    p = fixture.prime
    n = fixture.denominator
    support = (p * n - 1) // 4
    g_capacity = (p - 1) ** 2 // 4
    source_R = 4 * support - n
    source_K = support * (p - 1)
    g_R = p - 2
    shared_support = gcd(support, g_capacity)
    loss_factor = support // shared_support
    support_divides_g_capacity = g_capacity % support == 0

    if not (
        is_prime(p)
        and p % 24 == 1
        and n > 0
        and n % 4 == 1
        and p * n == 4 * support + 1
        and source_R == (p - 1) * n - 1
        and source_K == support * (p - 1)
        and 4 * source_K == p * source_R + 1
        and 4 * g_capacity == p * g_R + 1
        and (support_divides_g_capacity == (n == 1))
        and (source_R > p) == (n > 1)
        and fixture.expected_overflow == (source_R > p)
        and fixture.expected_support_divides_g_capacity
        == support_divides_g_capacity
        and fixture.expected_shared_support == shared_support
        and fixture.expected_loss_factor == loss_factor
    ):
        raise AssertionError(f"{fixture.name}: retention rigidity receipt changed")

    if n > 1:
        if not (n >= 5 and not support_divides_g_capacity and loss_factor > 1):
            raise AssertionError(f"{fixture.name}: overflow support-loss gate changed")
    else:
        if not (source_R == p - 2 and loss_factor == 1):
            raise AssertionError(f"{fixture.name}: n=1 boundary changed")

    return {
        "name": fixture.name,
        "overflow": source_R > p,
        "support": support,
        "g_capacity": g_capacity,
        "support_divides_g_capacity": support_divides_g_capacity,
        "shared_support": shared_support,
        "loss_factor": loss_factor,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    boundary_count = sum(not receipt["overflow"] for receipt in receipts)
    overflow_count = sum(bool(receipt["overflow"]) for receipt in receipts)
    partial_loss_count = sum(receipt["shared_support"] > 1 for receipt in receipts)
    if (boundary_count, overflow_count, partial_loss_count) != (1, 4, 2):
        raise AssertionError("focused rigidity receipt classification changed")
    print(
        "verified 1 unique n=1 retention boundary, 4 d=1 overflow "
        "support-loss receipts, and 2 partial-retention controls"
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
