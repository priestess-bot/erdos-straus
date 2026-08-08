#!/usr/bin/env python3
"""Verify projected source-column expansion and collision accounting."""

from __future__ import annotations

import argparse

from type_ii_target_fiber_owner_weighted_fourier_capacity_bridge import (
    owner_weighted_spectrum,
)


def expansion_step(
    request_count: int,
    physical_capacity: int,
    *,
    independent: bool,
    physical_new: bool,
    new_capacities: tuple[int, ...] = (1,),
) -> dict[str, int | str]:
    """Apply one owner-projected expansion classification."""
    old_delta = request_count - physical_capacity
    if not independent:
        return {
            "status": "DEPENDENT_OWNER_ESCAPE_RELATION",
            "old_delta": old_delta,
            "new_delta": old_delta,
        }
    if not physical_new:
        new_delta = request_count + 1 - physical_capacity
        return {
            "status": "OWNER_COLLISION_EXPANSION",
            "old_delta": old_delta,
            "new_delta": new_delta,
        }
    new_capacity = physical_capacity + sum(new_capacities)
    new_delta = request_count + 1 - new_capacity
    status = (
        "OWNER_PROJECTION_EXPANSION_RELEASE"
        if new_delta <= 0
        else "OWNER_SOURCE_COLUMN_EXPANSION"
    )
    return {
        "status": status,
        "old_delta": old_delta,
        "new_delta": new_delta,
    }


def run_verification() -> dict[str, object]:
    tight = expansion_step(2, 1, independent=True, physical_new=True)
    assert tight == {
        "status": "OWNER_SOURCE_COLUMN_EXPANSION",
        "old_delta": 1,
        "new_delta": 1,
    }

    release = expansion_step(
        2, 1, independent=True, physical_new=True, new_capacities=(2,)
    )
    assert release == {
        "status": "OWNER_PROJECTION_EXPANSION_RELEASE",
        "old_delta": 1,
        "new_delta": 0,
    }

    collision = expansion_step(2, 1, independent=True, physical_new=False)
    assert collision == {
        "status": "OWNER_COLLISION_EXPANSION",
        "old_delta": 1,
        "new_delta": 2,
    }

    dependent = expansion_step(2, 1, independent=False, physical_new=True)
    assert dependent == {
        "status": "DEPENDENT_OWNER_ESCAPE_RELATION",
        "old_delta": 1,
        "new_delta": 1,
    }

    # Real arithmetic control: p=57399241 has two owners for one q=5 occurrence.
    prime = 57_399_241
    sources = {
        1: prime + 4 * 41,
        41: prime + 4 * 41 * 41,
    }
    target = prime + 4
    profile = owner_weighted_spectrum(sources, target, 4)
    assert profile["owner_counts"] == {5: {1: (1, 41)}}
    real_collision = expansion_step(2, 1, independent=True, physical_new=False)
    assert real_collision["status"] == "OWNER_COLLISION_EXPANSION"

    return {
        "tight": tight,
        "release": release,
        "collision": collision,
        "dependent": dependent,
        "real_collision": real_collision,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner-projected source-column expansion")
    for branch in ("tight", "release", "collision", "dependent", "real_collision"):
        print(branch, result[branch]["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
