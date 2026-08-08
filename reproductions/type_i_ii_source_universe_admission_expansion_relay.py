#!/usr/bin/env python3
"""Verify finite source-universe admission expansion and collision dispatch."""

from __future__ import annotations

import argparse


def canonical_admission(
    source_records: tuple[str, ...],
    requests: tuple[tuple[str, str], ...],
    legal: set[tuple[str, tuple[str, str]]],
) -> tuple[tuple[str, tuple[str, str]], ...]:
    return tuple(
        (record, request)
        for record in source_records
        for request in requests
        if (record, request) in legal
    )


def step(
    universe: tuple[int, ...],
    menu: tuple[int, ...],
    admissions: dict[int, tuple[tuple[str, str], ...]],
    physical_slots: set[str],
    *,
    independent: bool,
    release: bool,
    canonicalized: bool = True,
) -> dict[str, object]:
    if not canonicalized:
        return {"status": "OWNER_TOKEN_SOURCE_CANONICALIZATION_OBSTRUCTED"}
    missing = sorted(set(universe) - set(menu))
    if not missing:
        return {"status": "SOURCE_UNIVERSE_COMPLETE", "remaining": 0}
    record = missing[0]
    edges = admissions.get(record, ())
    menu_next = tuple(sorted(set(menu) | {record}))
    remaining = len(set(universe) - set(menu_next))
    if not edges:
        return {
            "status": "SOURCE_RECORD_UNREALIZED",
            "record": record,
            "remaining": remaining,
        }
    new_slots = {slot for _, slot in edges} - physical_slots
    if new_slots and independent:
        status = (
            "SOURCE_UNIVERSE_EXPANSION_RELEASE"
            if release
            else "SOURCE_UNIVERSE_SOURCE_EXPANSION"
        )
        return {
            "status": status,
            "record": record,
            "new_slots": tuple(sorted(new_slots)),
            "remaining": remaining,
        }
    old_slot = next(iter(sorted({slot for _, slot in edges} & physical_slots)), None)
    if not independent:
        return {
            "status": "SOURCE_UNIVERSE_RELATION_CIRCUIT",
            "record": record,
            "slot": old_slot,
            "remaining": remaining,
        }
    return {
        "status": "SOURCE_UNIVERSE_OWNER_COLLISION",
        "record": record,
        "slot": old_slot,
        "remaining": remaining,
    }


def run_verification() -> dict[str, object]:
    universe = (1, 2, 3)

    release = step(
        universe,
        (1,),
        {2: (("r2", "q7"),)},
        {"q5"},
        independent=True,
        release=True,
    )
    assert release["status"] == "SOURCE_UNIVERSE_EXPANSION_RELEASE"
    assert release["remaining"] == 1

    collision = step(
        universe,
        (1,),
        {2: (("r2", "q5"),)},
        {"q5"},
        independent=True,
        release=False,
    )
    assert collision["status"] == "SOURCE_UNIVERSE_OWNER_COLLISION"

    circuit = step(
        universe,
        (1,),
        {2: (("r2", "q5"),)},
        {"q5"},
        independent=False,
        release=False,
    )
    assert circuit["status"] == "SOURCE_UNIVERSE_RELATION_CIRCUIT"

    unrealized = step(
        universe,
        (1,),
        {},
        {"q5"},
        independent=True,
        release=False,
    )
    assert unrealized["status"] == "SOURCE_RECORD_UNREALIZED"

    complete = step(
        universe,
        universe,
        {},
        {"q5"},
        independent=True,
        release=False,
    )
    assert complete["status"] == "SOURCE_UNIVERSE_COMPLETE"

    source_records = ("u1", "u2")
    requests = (("z0", "z1"), ("z1", "z2"))
    legal = {("u1", requests[0]), ("u2", requests[1])}
    admissions = canonical_admission(source_records, requests, legal)
    assert admissions == (("u1", requests[0]), ("u2", requests[1]))

    blocked = step(
        universe,
        (1,),
        {2: (("r2", "q7"),)},
        {"q5"},
        independent=True,
        release=True,
        canonicalized=False,
    )
    assert blocked["status"] == "OWNER_TOKEN_SOURCE_CANONICALIZATION_OBSTRUCTED"

    return {
        "release": release,
        "collision": collision,
        "circuit": circuit,
        "unrealized": unrealized,
        "complete": complete,
        "canonical_admission": admissions,
        "blocked": blocked,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified source-universe admission expansion relay")
    for key, value in result.items():
        if isinstance(value, dict):
            print(key, value["status"])
        else:
            print(key, value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
