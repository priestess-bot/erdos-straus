#!/usr/bin/env python3
"""Verify source-bound H4 a=1 atomic-macro schema controls.

The two fixtures are local clean-q suffixes, not asserted to be actual
19-phase P-to-H4 predecessors.  They verify the receipt shape and strict
endpoint capacity while the root direct screen correctly preempts dispatch.
No range scan, graph traversal, or general F/G factorization is performed.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, lcm

from type_i_atomic_split_total_typed_rechart import (
    direct_certificate_denominators,
    direct_type_i_ii_screen,
)
from type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge import (
    FIXTURES,
    Fixture,
    complete_excess,
    raw_q_word,
)


@dataclass(frozen=True)
class ParentReceipt:
    """The minimum persistent-prefix data a suffix is allowed to consume."""

    source_id: str
    source_scope: str
    prefix_digest: str
    p_to_h4_replayed: bool


@dataclass(frozen=True)
class SuffixReceipt:
    """Recomputed would-be atomic target before terminal-first dispatch."""

    prime: int
    h4_residual: int
    h4_carrier: int
    height: int
    q: int
    raw_word: tuple[int, ...]
    endpoint_x: int
    endpoint_y: int
    q_x: int
    q_y: int
    target_support: int
    target_capacity: int
    target_carrier: int
    target_residual: int
    owner: tuple[object, ...]


def verify_parent_receipt_gate(parent: ParentReceipt) -> None:
    """Reject a bare H4 chart before any atomic suffix construction."""
    if not (
        parent.source_id
        and parent.source_scope
        and parent.prefix_digest
        and parent.p_to_h4_replayed
    ):
        raise ValueError("missing persistent P-to-H4 source receipt")


def macro_owner(
    parent: ParentReceipt,
    *,
    height: int,
    q: int,
    raw_word: tuple[int, ...],
    endpoint_x: int,
    endpoint_y: int,
) -> tuple[object, ...]:
    """Bind occurrence ownership to P and its complete internal prefix."""
    verify_parent_receipt_gate(parent)
    physical_path = (height, q, raw_word, endpoint_x, endpoint_y)
    return (
        "h4_a1_atomic_macro_v1",
        parent.source_id,
        parent.prefix_digest,
        physical_path,
    )


def derive_local_suffix(parent: ParentReceipt, fixture: Fixture) -> SuffixReceipt:
    """Rebuild the local clean-q suffix with a real parent-receipt gate."""
    verify_parent_receipt_gate(parent)

    prime = fixture.prime
    h4_residual = 1 + prime * fixture.peeled_part
    h4_carrier = (prime * h4_residual + 1) // 4
    h4_support = h4_carrier
    height = gcd(h4_residual - 1, h4_carrier)
    z = h4_residual - height
    half = (prime + 1) // 2
    d4 = gcd(half, h4_support)
    q = half // d4
    endpoint_y, raw_word = raw_q_word(h4_residual, h4_carrier, z, q)
    endpoint_x = h4_residual - endpoint_y
    q_x = complete_excess(endpoint_x, h4_carrier)
    q_y = complete_excess(endpoint_y, h4_carrier)
    target_support = lcm(h4_support, q_x, q_y)
    target_capacity = pow((4 * target_support) % prime, -1, prime)
    target_carrier = target_support * target_capacity
    target_residual = (4 * target_carrier - 1) // prime
    owner = macro_owner(
        parent,
        height=height,
        q=q,
        raw_word=raw_word,
        endpoint_x=endpoint_x,
        endpoint_y=endpoint_y,
    )

    if not (
        prime % 24 == 1
        and prime * h4_residual + 1 == 4 * h4_carrier
        and height < prime + 1
        and q == fixture.expected_q > 1
        and gcd(q, h4_carrier) == 1
        and endpoint_x + endpoint_y == h4_residual
        and gcd(endpoint_x, endpoint_y) == 1
        and raw_word == fixture.expected_raw_selected
        and q_x == fixture.expected_q_x > 1
        and q_y == fixture.expected_q_y > 1
        and gcd(prime, q_x * q_y) == 1
        and target_support % h4_support == 0
        and target_support % q_x == 0
        and target_support % q_y == 0
        and prime * target_residual + 1 == 4 * target_carrier
        and target_capacity == fixture.expected_capacity
        and 1 <= target_capacity <= prime - 2
        and (0, target_capacity) < (0, prime - 1)
    ):
        raise AssertionError(f"{fixture.name}: source-bound atomic suffix changed")

    return SuffixReceipt(
        prime=prime,
        h4_residual=h4_residual,
        h4_carrier=h4_carrier,
        height=height,
        q=q,
        raw_word=raw_word,
        endpoint_x=endpoint_x,
        endpoint_y=endpoint_y,
        q_x=q_x,
        q_y=q_y,
        target_support=target_support,
        target_capacity=target_capacity,
        target_carrier=target_carrier,
        target_residual=target_residual,
        owner=owner,
    )


def terminal_first_dispatch(parent: ParentReceipt, fixture: Fixture) -> tuple[str, str]:
    """Apply the macro's root direct terminal policy before any pending target."""
    verify_parent_receipt_gate(parent)
    direct = direct_type_i_ii_screen(fixture.prime)
    if direct is None:
        return ("pending_suffix", fixture.name)
    kind, gap, divisor = direct
    denominators = direct_certificate_denominators(
        fixture.prime, kind, gap, divisor
    )
    if not all(value > 0 for value in denominators):
        raise AssertionError("direct terminal did not reconstruct")
    return ("terminal", f"direct_{kind}")


def verify() -> None:
    parent = ParentReceipt(
        source_id="persistent-P-control",
        source_scope="charged_history_only",
        prefix_digest="P-to-H4-control",
        p_to_h4_replayed=True,
    )
    receipts = [derive_local_suffix(parent, fixture) for fixture in FIXTURES]

    compact = [
        (
            receipt.prime,
            receipt.q,
            len(receipt.raw_word),
            receipt.q_x,
            receipt.q_y,
            receipt.target_capacity,
        )
        for receipt in receipts
    ]
    if compact != [
        (73, 37, 1, 119_539, 6_641, 24),
        (241, 121, 2, 3_571_501, 59_525, 80),
    ]:
        raise AssertionError("local H4 atomic macro controls changed")

    terminals = [terminal_first_dispatch(parent, fixture) for fixture in FIXTURES]
    if terminals != [("terminal", "direct_I"), ("terminal", "direct_I")]:
        raise AssertionError("terminal-first priority changed")

    try:
        derive_local_suffix(
            ParentReceipt(
                source_id="bare-H4",
                source_scope="",
                prefix_digest="",
                p_to_h4_replayed=False,
            ),
            FIXTURES[0],
        )
    except ValueError:
        pass
    else:
        raise AssertionError("bare H4 receipt bypassed the parent gate")

    print(
        "verified 2 source-bound H4 atomic suffixes, strict capacities, "
        "direct-terminal priority, and bare-H4 provenance refusal"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run exact controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
