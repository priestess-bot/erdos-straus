#!/usr/bin/env python3
"""Verify the v=5 carrier-subset q=19 prefix allocation obstruction.

This verifier checks a conditional rejection rule for a proposed carrier-only
request-to-token allocation.  It neither creates typed Fourier demands nor
promotes a carrier incidence to a Type-II source label, request, token,
physical slot, capacity price, or selector edge.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, permutations
from math import gcd

import type_i_c3_adaptive_core19_v5_c38_q19_phase_leaf as c38
import type_i_c3_adaptive_core19_v5_dual_leaf_f19_control as v5
import type_i_c3_adaptive_core19_v5_q19_phase_compatible_fiber as candidate
import type_i_raw_factor_block_local_cofactor_provenance as local_receipt


D_STAR = 6_303
A = 573
Q = 19
N_F = 1_202_391_362_917


def valuation(value: int, prime: int) -> int:
    """Return the exact q-adic height of a positive focused integer."""
    if value <= 0:
        raise AssertionError("carrier valuation requires a positive integer")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def prefix_matching_exists(heights: tuple[int, ...]) -> bool:
    """Check matching into distinct layers for prefix neighborhoods [1, h]."""
    if not heights or min(heights) < 1:
        raise AssertionError("focused requests must have positive prefix heights")
    layers = range(1, max(heights) + 1)
    return any(
        all(layer <= height for layer, height in zip(allocation, heights))
        for allocation in permutations(layers, len(heights))
    )


def verify_carrier_subset_caps() -> dict[str, object]:
    """Compute the new physical-carrier cap map and its minimum Hall witnesses."""
    candidate_data = candidate.verify_candidate_fiber()
    N = int(candidate_data["N"])
    shared_depth = int(candidate_data["shared_q19_ledger"]["d"])
    carriers = (
        ("C0", v5.C0, "dual-leaf raw endpoint and cofactor carrier"),
        ("C1", v5.C1, "dual-leaf raw endpoint and cofactor carrier"),
        ("C38", c38.C2, "physical-tail cofactor in z=38*t2; not the raw endpoint"),
    )
    if not (
        D_STAR == candidate.D_STAR == 3 * 11 * 191
        and A == candidate.A == 3 * 191
        and N == N_F == v5.P + 4 * D_STAR * A
        and N == 17 * Q**3 * 53**2 * 3_671
        and gcd(Q, 4 * D_STAR) == 1
        and valuation(N, Q) == shared_depth == 3
        and v5.C0 == v5.P - 3
        and v5.K % v5.C0 == v5.K % v5.C1 == v5.K % c38.C2 == 0
        and c38.Z2 == c38.C2 * c38.T2
    ):
        raise AssertionError("v=5 carrier-subset setup changed")

    rows: list[dict[str, object]] = []
    for name, carrier, kind in carriers:
        common = gcd(carrier, N)
        height = valuation(common, Q)
        if not (
            common == Q
            and height == 1
            and carrier % Q == 0
            and carrier % (Q**2) != 0
        ):
            raise AssertionError(f"{name}: carrier cap changed")
        rows.append(
            {
                "occurrence": name,
                "carrier": carrier,
                "carrier_kind": kind,
                "gcd_with_candidate": common,
                "q19_cap": height,
                "prefix_neighbors": list(range(1, height + 1)),
            }
        )

    witnesses: list[dict[str, object]] = []
    for size in range(1, len(rows) + 1):
        for subset in combinations(rows, size):
            heights = tuple(int(row["q19_cap"]) for row in subset)
            neighbors = set().union(
                *(set(range(1, height + 1)) for height in heights)
            )
            deficit = len(subset) - len(neighbors)
            matching = prefix_matching_exists(heights)
            if deficit > 0 and matching:
                raise AssertionError("a positive Hall witness unexpectedly matched")
            witnesses.append(
                {
                    "occurrences": [str(row["occurrence"]) for row in subset],
                    "heights": list(heights),
                    "neighbors": sorted(neighbors),
                    "hall_deficit": deficit,
                    "matching_for_this_subset": matching,
                }
            )

    pair_witnesses = [row for row in witnesses if len(row["occurrences"]) == 2]
    triple_witness = next(row for row in witnesses if len(row["occurrences"]) == 3)
    if not (
        all(int(row["q19_cap"]) == 1 for row in rows)
        and all(item["hall_deficit"] == 1 for item in pair_witnesses)
        and all(not item["matching_for_this_subset"] for item in pair_witnesses)
        and triple_witness["neighbors"] == [1]
        and triple_witness["hall_deficit"] == 2
        and not triple_witness["matching_for_this_subset"]
    ):
        raise AssertionError("carrier-subset q-prefix obstruction changed")
    return {
        "candidate_fiber": {"D_star": D_STAR, "A": A, "N": N, "q": Q},
        "candidate_q19_height": shared_depth,
        "carrier_cap_rows": rows,
        "hall_witnesses": witnesses,
        "scope": (
            "conditional carrier-subset rejection rule only; candidate depth is not "
            "a count of typed requests, tokens, or physical slots"
        ),
    }


def verify_actual_raw_endpoint_calibration() -> dict[str, object]:
    """Contrast candidate q-height with the q-height of one actual raw endpoint."""
    receipt = local_receipt.verify_v5_positive_control()
    candidate_data = dict(receipt["candidate"])
    H = int(candidate_data["H"])
    N = int(candidate_data["N"])
    if not (
        H == 7
        and N == v5.P + 4 * D_STAR * 11
        and N == 7**2 * 347 * 70_715_591
        and valuation(H, 7) == 1
        and valuation(N, 7) == 2
    ):
        raise AssertionError("actual raw endpoint calibration changed")
    return {
        "raw_endpoint": H,
        "candidate_A": 11,
        "candidate_N": N,
        "endpoint_q7_height": 1,
        "candidate_q7_height": 2,
        "conclusion": "the raw receipt alone does not certify the candidate record's extra q layer",
    }


def build_result() -> dict[str, object]:
    """Build a conditional local obstruction, deliberately not a capacity edge."""
    return {
        "certificate_type": "v5_carrier_subset_q19_prefix_obstruction_v1",
        "status": "analysis_evidence_only",
        "carrier_subset_obstruction": verify_carrier_subset_caps(),
        "actual_raw_endpoint_calibration": verify_actual_raw_endpoint_calibration(),
        "not_established": [
            "three independent typed Fourier/source demands",
            "a complete occurrence-to-(a,b,H,slot) adapter",
            "source-switch, SNF, or request-to-token/physical-slot injection",
            "a Type-II capacity price, target hit, descent, or selector edge",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified v=5 carrier-subset q=19 prefix obstruction")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
