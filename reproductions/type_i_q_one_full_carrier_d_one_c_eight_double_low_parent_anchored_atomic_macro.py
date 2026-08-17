#!/usr/bin/env python3
"""Verify the c=8 double-low parent-anchored atomic-macro interface.

The positive branch is conditional on an actual q=1 receiver parent and an
actual V-side raw label meeting both low-capacity gates.  No such endpoint is
invented here.  The fixed c=8 control is deliberately terminal-preempted and
only checks the checkpoint/source arithmetic plus refusal guards.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, lcm

import type_i_q_one_full_carrier_d_one_c_eight_full_excess_carry_obstruction as c8
import type_i_q_one_full_carrier_d_one_c_eight_universal_source_non_p_separation as source
import type_ii_q_one_full_carrier_d_one_capacity_two_rigidity as capacity_two
import type_ii_q_one_full_carrier_second_anchor_fixed_n_macro as q_one_macro
import type_ii_q_one_full_carrier_second_anchor_overflow as second_anchor
from type_i_q_one_full_carrier_d_one_c_eight_v_side_direct_m_one_capacity_map import (
    complete_excess,
)


@dataclass(frozen=True)
class ParentReceipt:
    """Minimum provenance which a c=8 checkpoint may inherit."""

    state_id: str
    source_tree_scope: str
    replayed_to_checkpoint: bool
    terminal_first_miss: bool


def require_parent(receipt: ParentReceipt) -> None:
    """Reject a bare c=8 chart before it can consume a raw source."""
    if not (
        receipt.state_id
        and receipt.source_tree_scope
        and receipt.replayed_to_checkpoint
        and receipt.terminal_first_miss
    ):
        raise ValueError("missing persistent receiver-to-c=8 parent receipt")


def rank_decreases(
    prime: int,
    parent_support: int,
    checkpoint_support: int,
    target_support: int,
    target_capacity: int,
) -> bool:
    """Check the parent-to-atomic-target E5 comparison."""
    boundary = (prime - 1) ** 2 // 4
    if not (
        prime > 7
        and parent_support > 0
        and target_support > checkpoint_support > prime * prime > boundary
        and 1 <= target_capacity <= 7
    ):
        raise ValueError("double-low rank premises failed")
    parent_rank = (boundary // parent_support, prime - 1)
    target_rank = (boundary // target_support, target_capacity)
    return target_rank < parent_rank


def c_eight_checkpoint(s: int) -> dict[str, int | str]:
    """Replay an actual q=1 parent receipt through its c=8 checkpoint."""
    macro = q_one_macro.even_macro(2 * s)
    postmacro = q_one_macro.postmacro_full_product(macro)
    if postmacro["status"] != "strict_full_product_fold":
        raise AssertionError("c=8 row lost its persistent d=1 receiver")

    receiver = postmacro["successor"]
    prime = int(macro["prime"])
    parent_support, parent_R, parent_K = (
        int(receiver[field]) for field in ("support", "R", "K")
    )
    excess = second_anchor.complete_excess(parent_R - 1, parent_K)
    checkpoint_support = lcm(parent_support, int(excess["Q"]))
    chart = second_anchor.canonical_chart(prime, checkpoint_support)
    row = capacity_two.receiver_data("even", 2 * s)
    target = c8.c_eight_target(s)
    boundary = (prime - 1) ** 2 // 4

    if not (
        macro["selected_carrier"]["q_star"] == 103
        and row["j"] == 11
        and row["g"] == 1
        and row["c"] == 8
        and parent_K == parent_support * (prime - 1)
        and checkpoint_support == int(row["M"]) == target.M
        and int(chart["R"]) == int(row["target_R"]) == target.R
        and int(chart["K"]) == int(row["target_K"]) == target.K
        and target.K == 8 * checkpoint_support
        and checkpoint_support > prime * prime > boundary
        and str(receiver["source_tree_scope"]) == q_one_macro.SOURCE_SCOPE
    ):
        raise AssertionError("c=8 parent checkpoint receipt changed")
    return {
        "prime": prime,
        "parent_support": parent_support,
        "checkpoint_support": checkpoint_support,
        "parent_state_id": str(receiver["state_id"]),
        "scope": str(receiver["source_tree_scope"]),
    }


def suffix_capacity_data(s: int, raw_prime: int) -> dict[str, int]:
    """Recompute an actual V-side endpoint and both canonical capacities."""
    data = source.source_data(s)
    edge = source.v_side_raw_edge(data, raw_prime)
    prime, K, support = data.prime, data.K, data.K // 8
    a, b, layer = edge["destination"]
    q_a = complete_excess(a, K)
    q_b = complete_excess(b, K)
    multiplier_a = lcm(support, q_a) // support
    multiplier_b = lcm(support, q_b) // support
    target_support = lcm(support, q_a, q_b)
    direct_capacity = (8 * pow(multiplier_a, -1, prime)) % prime
    split_capacity = (8 * pow(multiplier_a * multiplier_b, -1, prime)) % prime

    if not (
        raw_prime > 2 * (prime - 1)
        and edge["gcd_reduction"] == 1
        and layer == 1
        and a + b == data.R
        and gcd(a, b) == 1
        and q_a > 1
        and q_b > 1
        and gcd(prime, q_a * q_b) == 1
        and target_support == lcm(support, q_a, q_b) > support
        and split_capacity
        == (8 * pow((target_support // support) % prime, -1, prime)) % prime
    ):
        raise AssertionError("c=8 V-side atomic suffix arithmetic changed")
    return {
        "prime": prime,
        "checkpoint_support": support,
        "target_support": target_support,
        "direct_capacity": direct_capacity,
        "split_capacity": split_capacity,
    }


def verify() -> None:
    checkpoint = c_eight_checkpoint(3279)
    data = source.source_data(3279)
    if source.canonical_p_edge(data) != (1, data.R - 1, 1):
        raise AssertionError("c=8 checkpoint lost its chart-local raw source")

    suffix = suffix_capacity_data(3279, 5_963_047)
    if not (
        checkpoint["prime"] == 157_393
        and checkpoint["checkpoint_support"] == data.K // 8
        and suffix
        == {
            "prime": 157_393,
            "checkpoint_support": data.K // 8,
            "target_support": 59_579_500_651_491_202_538_305_440_357_913
            * (data.K // 8),
            "direct_capacity": 11_230,
            "split_capacity": 38_261,
        }
    ):
        raise AssertionError("terminal-preempted c=8 source control changed")

    # The generic rank proof has two cases: support rank drops, or capacity does.
    for parent_support in (1, 7_750_656, 7_750_657):
        if not rank_decreases(5_569, parent_support, 31_013_762, 31_013_763, 7):
            raise AssertionError("double-low parent rank comparison changed")

    try:
        require_parent(
            ParentReceipt(
                state_id="bare-c8",
                source_tree_scope="",
                replayed_to_checkpoint=False,
                terminal_first_miss=False,
            )
        )
    except ValueError:
        pass
    else:
        raise AssertionError("bare c=8 checkpoint bypassed parent provenance")

    if suffix["direct_capacity"] < 8 or suffix["split_capacity"] < 8:
        raise AssertionError("terminal-preempted control accidentally entered double-low")
    print(
        "verified c=8 double-low parent-macro interface: persistent checkpoint "
        "replay, chart-local raw-source binding, strict rank rule, and bare/"
        "non-low refusal controls"
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
