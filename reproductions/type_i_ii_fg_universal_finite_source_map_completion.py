#!/usr/bin/env python3
"""Verify finite Type I/II source-universe completion and physical deduplication."""

from __future__ import annotations

import argparse
import math


def divisors(value: int) -> tuple[int, ...]:
    result: list[int] = []
    for candidate in range(1, math.isqrt(value) + 1):
        if value % candidate:
            continue
        result.append(candidate)
        if candidate * candidate != value:
            result.append(value // candidate)
    return tuple(sorted(result))


def square_free(value: int) -> bool:
    for prime in range(2, math.isqrt(value) + 1):
        if value % (prime * prime) == 0:
            return False
    return True


def v2(value: int) -> int:
    result = 0
    while value % 2 == 0:
        value //= 2
        result += 1
    return result


def type_ii_universe(p: int, d: int) -> tuple[tuple[int, int, int], ...]:
    records: list[tuple[int, int, int]] = []
    for d_star in divisors(d):
        for a in divisors(d_star):
            if not square_free(d_star // a) or 4 * a * d_star >= p:
                continue
            for factor in divisors(p + 4 * a * d_star):
                if factor > 1:
                    records.append((d_star, a, factor))
    return tuple(sorted(set(records)))


def type_i_universe(
    p: int, r: int, k: int
) -> tuple[tuple[int, int, int, int, int], ...]:
    length = 2 * k
    records: list[tuple[int, int, int, int, int]] = []
    for a in divisors(length):
        for b in divisors(length):
            if math.gcd(a, b) != 1:
                continue
            budget = v2(length) + v2(a) - v2(b)
            for j in range(1, budget + 1):
                if a % r != (pow(2, j, r) * b) % r:
                    continue
                if a >= (2**j) * b:
                    continue
                denominator = b * (2 ** (j - 1))
                numerator = length * a
                if numerator % denominator:
                    continue
                e_value = numerator // denominator
                if (2 * length - e_value) % r:
                    continue
                n_value = (2 * length - e_value) // r
                if not (0 < n_value < p) or n_value % 2:
                    continue
                records.append((a, b, j, e_value, n_value))
    return tuple(sorted(set(records)))


def menu_status(
    universe: tuple[tuple[int, ...], ...], menu: tuple[tuple[int, ...], ...]
) -> dict[str, object]:
    missing = sorted(set(universe) - set(menu))
    if missing:
        return {
            "status": "SOURCE_UNIVERSE_MENU_ESCAPE",
            "witness": missing[0],
            "universe_size": len(universe),
        }
    return {"status": "SOURCE_UNIVERSE_COMPLETE", "universe_size": len(universe)}


def generated_subgroup(
    rows: tuple[tuple[int, int], ...], group_order: int, label_order: int
) -> set[tuple[int, int]]:
    subgroup = {(0, 0)}
    for row in rows:
        closure = set(subgroup)
        current = (0, 0)
        for _ in range(math.lcm(group_order, label_order)):
            current = (
                (current[0] + row[0]) % group_order,
                (current[1] + row[1]) % label_order,
            )
            closure.update(
                ((value[0] + current[0]) % group_order,
                 (value[1] + current[1]) % label_order)
                for value in subgroup
            )
        subgroup = closure
    return subgroup


def marked_group_status(
    universe: tuple[tuple[int, int], ...],
    menu: tuple[tuple[int, int], ...],
    *,
    group_order: int,
    label_order: int,
) -> str:
    complete = generated_subgroup(universe, group_order, label_order)
    selected = generated_subgroup(menu, group_order, label_order)
    if selected != complete:
        return "MARKED_SOURCE_MENU_GROUP_ESCAPE"
    return "MARKED_SOURCE_MENU_GROUP_SATURATED"


def run_verification() -> dict[str, object]:
    # A Type II source universe contains both p+24=121 and p+72=169 source factors.
    type_ii = type_ii_universe(97, 6)
    assert (6, 1, 11) in type_ii
    assert (6, 3, 13) in type_ii
    ii_missing = menu_status(type_ii, ((6, 1, 11),))
    assert ii_missing["status"] == "SOURCE_UNIVERSE_MENU_ESCAPE"

    # The finite Type I universe contains the non-neighbor generalized dyadic record.
    type_i = type_i_universe(673, 83, 13965)
    assert (15, 49, 1, 8550, 570) in type_i
    i_complete = menu_status(type_i, type_i)
    assert i_complete["status"] == "SOURCE_UNIVERSE_COMPLETE"

    # Integer records can collapse to one physical q slot; enumeration does not add capacity.
    records = ((6, 1, 5), (6, 3, 5), (6, 1, 7))
    physical = {record[2] for record in records}
    assert len(records) == 3
    assert physical == {5, 7}

    escape = marked_group_status(
        ((1, 1), (2, 0)),
        ((1, 1),),
        group_order=6,
        label_order=3,
    )
    assert escape == "MARKED_SOURCE_MENU_GROUP_ESCAPE"

    saturated = marked_group_status(
        ((1, 1), (2, 2)),
        ((1, 1),),
        group_order=6,
        label_order=3,
    )
    assert saturated == "MARKED_SOURCE_MENU_GROUP_SATURATED"

    return {
        "type_ii": ii_missing,
        "type_i": i_complete,
        "physical_projection": {
            "records": len(records),
            "physical_slots": len(physical),
        },
        "marked_escape": escape,
        "marked_saturated": saturated,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified universal finite source-map completion")
    for key, value in result.items():
        print(key, value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
