#!/usr/bin/env python3
"""Verify raw-certified q-layer ownership and charge-key nonreuse at v=5.

The fixture has an actual raw endpoint H=7.  It verifies only the arithmetic
source half of a proposed owner map; no typed demand, FIBER_REALIZED receipt,
slot injection, capacity price in a larger product, or selector edge is made.
"""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_c3_adaptive_core19_v5_dual_leaf_f19_control as v5
import type_i_raw_factor_block_local_cofactor_provenance as local_receipt


D_STAR = 6_303
A = 11
Q = 7
M = 4 * D_STAR
S = A * D_STAR
N = 1_202_377_193_773


def valuation(value: int, prime: int) -> int:
    """Return a focused positive q-adic valuation."""
    if value <= 0:
        raise AssertionError("valuation requires a positive focused integer")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def multiplicative_order(value: int, modulus: int) -> int:
    """Compute the small exact order needed by this fixed q-block fixture."""
    if gcd(value, modulus) != 1:
        raise AssertionError("order requires a unit")
    residue = 1
    for exponent in range(1, modulus + 1):
        residue = residue * value % modulus
        if residue == 1:
            return exponent
    raise AssertionError("unit order did not close")


def stabilizer(block: set[int], modulus: int) -> set[int]:
    """Compute the multiplicative set stabilizer for a small exact block."""
    return {
        unit
        for unit in range(1, modulus)
        if gcd(unit, modulus) == 1
        and {unit * residue % modulus for residue in block} == block
    }


def verify_raw_self_binding() -> dict[str, object]:
    """Bind the actual H=7 raw receipt to its same-modulus candidate source."""
    receipt = local_receipt.verify_v5_positive_control()
    candidate = dict(receipt["candidate"])
    H = int(candidate["H"])
    candidate_N = int(candidate["N"])
    raw_height = valuation(H, Q)
    candidate_height = valuation(candidate_N, Q)
    if not (
        H == Q == 7
        and D_STAR == int(candidate["D"])
        and A == int(candidate["A"])
        and S == D_STAR * A == 69_333
        and M == 25_212
        and candidate_N == N == v5.P + 4 * S
        and N == Q**2 * 347 * 70_715_591
        and gcd(Q, M) == gcd(H, M) == 1
        and D_STAR % A == 0
        and D_STAR // A == 3 * 191
        and raw_height == 1
        and candidate_height == 2
    ):
        raise AssertionError("raw H=7 self-binding arithmetic changed")

    # The raw receipt deliberately caps its source label at its own q-height.
    source_height = raw_height
    relay_height = min(source_height, candidate_height)
    if not (S - S == 0 and relay_height == source_height == 1):
        raise AssertionError("same-modulus raw q relay changed")
    return {
        "raw_receipt": "v5_A11_H7",
        "source_label": {"a": A, "b": S},
        "candidate_fiber": {"D_star": D_STAR, "A": A, "s": S, "N": N},
        "charge_prime": Q,
        "raw_q_height": raw_height,
        "candidate_q_height": candidate_height,
        "self_bound_relay_height": relay_height,
        "scope": "one raw-certified q atom; no typed demand or token injection",
    }


def verify_one_charge_key() -> dict[str, object]:
    """Show that a candidate-only q extension replaces, rather than adds to, one block."""
    binding = verify_raw_self_binding()
    raw_height = int(binding["raw_q_height"])
    candidate_height = int(binding["candidate_q_height"])
    raw_block = {pow(Q, exponent, M) for exponent in range(raw_height + 1)}
    candidate_block = {pow(Q, exponent, M) for exponent in range(candidate_height + 1)}
    order = multiplicative_order(Q, M)
    raw_stabilizer = stabilizer(raw_block, M)
    candidate_stabilizer = stabilizer(candidate_block, M)
    raw_price = len(raw_block) - 1
    candidate_price = len(candidate_block) - 1
    charge_key = {
        "fiber": {"D_star": D_STAR, "A": A},
        "q_residue_mod_M": Q % M,
        "block_lineage_id": "v5_A11_q7",
        "stabilizer_snapshot": "block_only_T=1",
    }
    if not (
        order == 10
        and raw_block == {1, 7}
        and candidate_block == {1, 7, 49}
        and raw_stabilizer == candidate_stabilizer == {1}
        and raw_price == 1
        and candidate_price == 2
        and raw_block < candidate_block
        and (M - 1) not in raw_block | candidate_block
        and len({charge_key["q_residue_mod_M"]}) == 1
    ):
        raise AssertionError("one-charge-key q-block accounting changed")
    return {
        "charge_key": charge_key,
        "price_mode_requirement": "choose exactly one of final or tower-insertion per block lineage",
        "raw_block": sorted(raw_block),
        "candidate_extension_block": sorted(candidate_block),
        "q_order": order,
        "raw_block_price_at_T1": raw_price,
        "candidate_extension_price_at_T1": candidate_price,
        "source_column_count_upper_bound": 1,
        "forbidden_accounting": [
            "raw depth + q-column rank + q-block price",
            "price(raw block) + price(candidate extension)",
        ],
    }


def build_result() -> dict[str, object]:
    """Build an accounting fixture, deliberately not a capacity or selector edge."""
    return {
        "certificate_type": "raw_certified_q_layer_charge_key_nonreuse_v1",
        "status": "analysis_evidence_only",
        "raw_self_binding": verify_raw_self_binding(),
        "canonical_charge_key": verify_one_charge_key(),
        "not_established": [
            "a Fourier/source rank demand",
            "FIBER_REALIZED or a full source-map/SNF contract",
            "request-to-token or demand-to-slot injection",
            "a Type-II hit, strict descent, or selector edge",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified raw-certified q-layer charge-key nonreuse")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
