#!/usr/bin/env python3
"""Verify canonical H4 atomic ownership and target-block absorption.

The controls replay the two fixed clean-q H4 fixtures.  They check only the
branch-local facts used by the owner argument: one canonical q word, two
nontrivial blocks, their lcm charge, and the fact that an equal block is no
longer fresh after the target is formed.  No state-graph or range scan runs.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

from type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge import (
    FIXTURES,
    complete_excess,
    factorization,
    raw_q_word,
)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def owner_tuple(
    prime: int,
    residue: int,
    source_carrier: int,
    height: int,
    q: int,
    raw_word: tuple[int, ...],
    endpoint_x: int,
    endpoint_y: int,
) -> tuple[object, ...]:
    return (
        "h4_atomic_q_bridge_v1",
        prime,
        residue,
        source_carrier,
        height,
        q,
        raw_word,
        endpoint_x,
        endpoint_y,
    )


def audit(fixture: object) -> dict[str, int | str]:
    prime = int(getattr(fixture, "prime"))
    peeled_part = int(getattr(fixture, "peeled_part"))
    residue = 1 + prime * peeled_part
    source_carrier = (prime * residue + 1) // 4
    height = gcd(residue - 1, source_carrier)
    d4 = gcd((prime + 1) // 2, source_carrier)
    q = (prime + 1) // (2 * d4)
    selected = residue - height
    endpoint_y, raw_word = raw_q_word(residue, source_carrier, selected, q)
    endpoint_x = residue - endpoint_y
    replayed_y, replayed_word = raw_q_word(residue, source_carrier, selected, q)
    replayed_x = residue - replayed_y
    q_x = complete_excess(endpoint_x, source_carrier)
    q_y = complete_excess(endpoint_y, source_carrier)
    target_support = lcm(source_carrier, q_x, q_y)
    capacity = pow((4 * target_support) % prime, -1, prime)
    target_carrier = target_support * capacity
    canonical_owner = owner_tuple(
        prime,
        residue,
        source_carrier,
        height,
        q,
        raw_word,
        endpoint_x,
        endpoint_y,
    )
    replayed_owner = owner_tuple(
        prime,
        residue,
        source_carrier,
        height,
        q,
        replayed_word,
        replayed_x,
        replayed_y,
    )

    if not (
        prime % 24 == 1
        and residue == q * endpoint_y + height
        and endpoint_x == (q - 1) * endpoint_y + height
        and raw_word == tuple(getattr(fixture, "expected_raw_selected"))
        and q_x > 1
        and q_y > 1
        and canonical_owner == replayed_owner
        and target_support % source_carrier == 0
        and target_support % q_x == 0
        and target_support % q_y == 0
        and target_carrier == target_support * capacity
        and complete_excess(q_x, target_carrier) == 1
        and complete_excess(q_y, target_carrier) == 1
        and canonical_owner == canonical_owner
    ):
        raise AssertionError(f"{getattr(fixture, 'name')}: atomic owner control changed")

    for block in (q_x, q_y):
        for ell in factorization(block):
            old_height = valuation(target_carrier, ell)
            higher_block = ell ** (old_height + 1)
            if not (
                complete_excess(higher_block, target_carrier) == higher_block
                and lcm(target_support, higher_block) > target_support
            ):
                raise AssertionError("higher complete-excess block did not grow lcm support")

    return {
        "name": str(getattr(fixture, "name")),
        "q": q,
        "raw_steps": len(raw_word),
        "q_x": q_x,
        "q_y": q_y,
        "capacity": capacity,
        "target_multiplier": target_support // source_carrier,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    if receipts != [
        {
            "name": "prime_q37_atomic_split_strict",
            "q": 37,
            "raw_steps": 1,
            "q_x": 119_539,
            "q_y": 6_641,
            "capacity": 24,
            "target_multiplier": 793_858_499,
        },
        {
            "name": "composite_q121_atomic_split_strict",
            "q": 121,
            "raw_steps": 2,
            "q_x": 3_571_501,
            "q_y": 59_525,
            "capacity": 80,
            "target_multiplier": 212_593_597_025,
        },
    ]:
        raise AssertionError("H4 atomic owner receipts changed")
    print("verified H4 atomic owner locality and no equal-block recharge")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
