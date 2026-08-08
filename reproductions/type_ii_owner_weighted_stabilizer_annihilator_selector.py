#!/usr/bin/env python3
"""Verify the owner-weighted finite selector and its strict relay potential."""

from __future__ import annotations

import argparse

from type_ii_target_fiber_owner_weighted_fourier_capacity_bridge import (
    owner_weighted_spectrum,
    subgroup,
    weighted_stabilizer,
)


def profile_spectrum(
    heights: dict[int, int], owner_counts: dict[int, dict[int, int]], modulus: int
) -> tuple[tuple[int, ...], dict[int, int]]:
    """Build a weighted spectrum from an explicit finite owner profile."""
    group = subgroup(tuple(q % modulus for q in heights), modulus)
    weights = {1 % modulus: 1}
    for prime, exponent in sorted(heights.items()):
        choices = {1 % modulus: 1}
        for height in range(1, exponent + 1):
            residue = pow(prime, height, modulus)
            choices[residue] = choices.get(residue, 0) + owner_counts[prime][height]
        updated: dict[int, int] = {}
        for left, left_weight in weights.items():
            for right, right_weight in choices.items():
                product = left * right % modulus
                updated[product] = updated.get(product, 0) + left_weight * right_weight
        weights = updated
    return group, weights


def support_stabilizer(
    weights: dict[int, int], group: tuple[int, ...], modulus: int
) -> tuple[int, ...]:
    """Return the stabilizer of the unweighted support indicator."""
    support = {point for point, weight in weights.items() if weight}
    return tuple(
        element
        for element in group
        if all(
            ((element * point) % modulus in support) == (point in support)
            for point in group
        )
    )


def weighted_selector(
    weights: dict[int, int], group: tuple[int, ...], target: int, modulus: int
) -> dict[str, object]:
    """Apply the finite part of the ordered selector."""
    if target not in group:
        return {"status": "G_SOURCE_SUPPORT_SEPARATION"}
    if weights.get(target, 0) > 0:
        return {"status": "OWNER_WEIGHTED_TARGET_HIT"}
    stabilizer = weighted_stabilizer(weights, group, modulus)
    if len(stabilizer) == 1:
        return {"status": "OWNER_FOURIER_ROLE_REQUIRED", "stabilizer": stabilizer}
    target_coset = {(target * point) % modulus for point in stabilizer}
    assert all(weights.get(point, 0) == 0 for point in target_coset)
    quotient_order = len(group) // len(stabilizer)
    assert 1 < quotient_order < len(group)
    return {
        "status": "OWNER_SPECTRUM_STABILIZER_DESCENT",
        "stabilizer": stabilizer,
        "old_order": len(group),
        "new_order": quotient_order,
    }


def annihilator_relay_order(
    group_order: int,
    kernel_order: int,
    target_in_kernel: bool,
    target_order: int = 2,
) -> int | None:
    """Return the strict finite order after a typed annihilator relay."""
    assert 1 <= kernel_order < group_order
    if target_in_kernel:
        assert kernel_order > 1
        return kernel_order
    if kernel_order == 1:
        assert target_order == group_order
        return None
    quotient_order = group_order // kernel_order
    assert target_order == quotient_order
    assert quotient_order < group_order
    return quotient_order


def run_verification() -> dict[str, object]:
    # Real F-gap control: weighted stabilizer descent happens before Fourier dispatch.
    p_f = 409
    f_sources = {
        4: p_f + 4 * 8 * 4,
        8: p_f + 4 * 8 * 8,
    }
    f_target = p_f + 4 * 2 * 4
    f_profile = owner_weighted_spectrum(f_sources, f_target, 16)
    f_result = weighted_selector(f_profile["weights"], f_profile["group"], 15, 16)
    assert f_result == {
        "status": "OWNER_SPECTRUM_STABILIZER_DESCENT",
        "stabilizer": (1, 7),
        "old_order": 8,
        "new_order": 4,
    }
    assert f_profile["weights"].get(15, 0) == 0

    # Owner imbalance: support periodicity is not weighted periodicity.
    synthetic_group, synthetic_weights = profile_spectrum(
        {3: 1, 7: 1}, {3: {1: 1}, 7: {1: 2}}, 16
    )
    assert synthetic_group == (1, 3, 5, 7, 9, 11, 13, 15)
    assert synthetic_weights == {1: 1, 3: 1, 5: 2, 7: 2}
    assert support_stabilizer(synthetic_weights, synthetic_group, 16) == (1, 7)
    assert weighted_stabilizer(synthetic_weights, synthetic_group, 16) == (1,)
    synthetic_result = weighted_selector(synthetic_weights, synthetic_group, 15, 16)
    assert synthetic_result == {
        "status": "OWNER_FOURIER_ROLE_REQUIRED",
        "stabilizer": (1,),
    }

    # Real direct-hit control: no descent is fabricated when a target owner exists.
    p_hit = 5_113
    hit_sources = {3: p_hit + 24 * 3, 6: p_hit + 24 * 6}
    hit_target = p_hit + 4
    hit_profile = owner_weighted_spectrum(hit_sources, hit_target, 4)
    hit_result = weighted_selector(hit_profile["weights"], hit_profile["group"], 3, 4)
    assert hit_result == {"status": "OWNER_WEIGHTED_TARGET_HIT"}

    # Finite annihilator controls: quotient, subgroup, and top-primary terminal.
    assert annihilator_relay_order(4, 2, False) == 2
    assert annihilator_relay_order(4, 2, True) == 2
    assert annihilator_relay_order(2, 1, False) is None

    return {
        "weighted_stabilizer_descent": f_result,
        "weighted_vs_support": {
            "support_stabilizer": support_stabilizer(synthetic_weights, synthetic_group, 16),
            "weighted_stabilizer": weighted_stabilizer(
                synthetic_weights, synthetic_group, 16
            ),
            "status": synthetic_result["status"],
        },
        "target_hit": hit_result,
        "annihilator_orders": {"quotient": 2, "subgroup": 2, "top_primary": None},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner-weighted stabilizer-annihilator selector")
    print("stabilizer", result["weighted_stabilizer_descent"]["status"])
    print("weight_boundary", result["weighted_vs_support"]["status"])
    print("hit", result["target_hit"]["status"])
    print("annihilator quotient/subgroup/top", result["annihilator_orders"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
