#!/usr/bin/env python3
"""Verify the owner-saturation priority and quotient/kernel controls."""

from __future__ import annotations

import argparse

from type_ii_target_fiber_owner_weighted_fourier_capacity_bridge import (
    owner_weighted_spectrum,
)


def owner_saturation_dispatch(
    exponent: int,
    order: int,
    *,
    direct_hit: bool,
    quotient_hit: bool,
) -> str:
    """Return the first legal branch for one owner q-block."""
    if direct_hit:
        return "OWNER_WEIGHTED_TARGET_HIT"
    if order <= 1:
        return "OWNER_Q_BLOCK_TRIVIAL_QUOTIENT"
    if exponent < order - 1:
        return "OWNER_Q_BLOCK_UNSATURATED"
    if not quotient_hit:
        return "SATURATED_OWNER_QUOTIENT_MISS"
    return "SATURATED_OWNER_KERNEL_SPLIT"


def saturated_physical_capacity(owner_count: int, budget: int) -> int:
    """Owner labels do not multiply a single saturated physical slot."""
    if owner_count < 1 or budget < 0:
        raise ValueError("owner count and budget must be valid")
    return budget


def run_verification() -> dict[str, object]:
    # F-type gap: q=7 has order two modulo 16 and its height-one block saturates.
    p_f = 409
    f_sources = {
        4: p_f + 4 * 8 * 4,
        8: p_f + 4 * 8 * 8,
    }
    f_target = p_f + 4 * 2 * 4
    f_profile = owner_weighted_spectrum(f_sources, f_target, 16)
    assert f_profile["heights"] == {3: 1, 7: 1}
    assert f_profile["weights"] == {1: 1, 3: 1, 5: 1, 7: 1}
    H = {1, 7}
    source_cosets = {
        frozenset(point * h % 16 for h in H)
        for point in f_profile["weights"]
    }
    target_coset = frozenset(15 * h % 16 for h in H)
    assert source_cosets == {
        frozenset({1, 7}),
        frozenset({3, 5}),
    }
    assert target_coset not in source_cosets
    f_status = owner_saturation_dispatch(
        1, 2, direct_hit=False, quotient_hit=False
    )
    assert f_status == "SATURATED_OWNER_QUOTIENT_MISS"

    # Direct Type II hit wins over the saturation relay.
    p_hit = 5_113
    hit_sources = {3: p_hit + 24 * 3, 6: p_hit + 24 * 6}
    hit_target = p_hit + 4
    hit_profile = owner_weighted_spectrum(hit_sources, hit_target, 4)
    assert hit_profile["weights"] == {1: 2, 3: 2}
    hit_status = owner_saturation_dispatch(
        1, 2, direct_hit=hit_profile["weights"].get(3, 0) > 0, quotient_hit=True
    )
    assert hit_status == "OWNER_WEIGHTED_TARGET_HIT"

    # Additive C8 -> C4 control: the quotient hits but the target is outside P.
    P = {0, 2}
    target = 4
    kernel = {0, 2, 4, 6}
    section = {k for k in kernel if (target + k) % 8 in P}
    assert section == {4, 6}
    energy = len(section) * (len(kernel) - len(section))
    assert energy == 4
    kernel_status = owner_saturation_dispatch(
        1, 2, direct_hit=False, quotient_hit=True
    )
    assert kernel_status == "SATURATED_OWNER_KERNEL_SPLIT"

    # Unsaturated and owner-collision controls.
    unsaturated = owner_saturation_dispatch(
        1, 4, direct_hit=False, quotient_hit=False
    )
    assert unsaturated == "OWNER_Q_BLOCK_UNSATURATED"
    assert saturated_physical_capacity(owner_count=2, budget=1) == 1

    return {
        "f_gap": f_status,
        "direct_hit": hit_status,
        "kernel_split": {
            "status": kernel_status,
            "section": sorted(section),
            "energy": energy,
        },
        "unsaturated": unsaturated,
        "owner_collision_capacity": 1,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner-saturation quotient/kernel dispatch")
    for key in ("f_gap", "direct_hit", "kernel_split", "unsaturated"):
        value = result[key]
        status = value["status"] if isinstance(value, dict) else value
        print(key, status)
    print("owner_collision_capacity", result["owner_collision_capacity"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
