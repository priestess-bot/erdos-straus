#!/usr/bin/env python3
"""Verify the fixed Type-I empty-fiber G/F/source-demand dispatch."""

from __future__ import annotations

import argparse
import cmath
import math
from itertools import product


def mod_pow(base: int, exponent: int, modulus: int) -> int:
    if exponent >= 0:
        return pow(base, exponent, modulus)
    return pow(pow(base, -1, modulus), -exponent, modulus)


def box_points(budgets: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(product(*(range(-budget, budget + 1) for budget in budgets)))


def image(generators: tuple[int, ...], point: tuple[int, ...], modulus: int) -> int:
    value = 1
    for generator, exponent in zip(generators, point):
        value = value * mod_pow(generator, exponent, modulus) % modulus
    return value


def closure(generators: set[int], modulus: int) -> set[int]:
    subgroup = {1}
    changed = True
    while changed:
        changed = False
        for left in tuple(subgroup):
            for generator in tuple(generators):
                for right in (generator, pow(generator, -1, modulus)):
                    value = left * right % modulus
                    if value not in subgroup:
                        subgroup.add(value)
                        changed = True
    return subgroup


def unit_group(modulus: int) -> set[int]:
    return {value for value in range(1, modulus) if math.gcd(value, modulus) == 1}


def empty_chart(
    modulus: int,
    generators: tuple[int, ...],
    budgets: tuple[int, ...],
) -> tuple[set[int], set[int], set[int], int]:
    points = box_points(budgets)
    support = {image(generators, point, modulus) for point in points}
    source = closure(set(generators), modulus)
    differences = closure(
        {
            left * pow(right, -1, modulus) % modulus
            for left in support
            for right in support
        },
        modulus,
    )
    target = (-1) % modulus
    return support, source, differences, target


def cyclic_logs(generator: int, order: int, modulus: int) -> dict[int, int]:
    logs: dict[int, int] = {}
    value = 1
    for exponent in range(order):
        if value in logs:
            raise AssertionError("generator is not of the expected order")
        logs[value] = exponent
        value = value * generator % modulus
    if len(logs) != order:
        raise AssertionError("cyclic log table is incomplete")
    return logs


def canonical_cyclic_deficit(
    logs: dict[int, int],
    support_points: tuple[int, ...],
    target: int,
    order: int,
) -> tuple[int, float]:
    scores: list[tuple[float, int]] = []
    target_log = logs[target]
    for character_index in range(1, order):
        total = sum(
            cmath.exp(2j * math.pi * character_index * logs[value] / order)
            for value in support_points
        )
        target_phase = cmath.exp(2j * math.pi * character_index * target_log / order)
        score = -((target_phase.conjugate() * total).real)
        scores.append((score, character_index))
    maximum = max(score for score, _ in scores)
    tied = [
        character_index
        for score, character_index in scores
        if abs(score - maximum) <= 1e-10
    ]
    score = maximum
    character_index = min(tied)
    return character_index, score


def verify_g_controls() -> list[dict[str, object]]:
    controls = (
        (3, (181,), (1,), {1}),
        (7, (2, 211), (1, 1), {1, 2, 4}),
    )
    receipts = []
    for modulus, generators, budgets, expected_source in controls:
        support, source, differences, target = empty_chart(modulus, generators, budgets)
        assert source == expected_source
        assert target not in support
        assert target not in source
        assert differences == expected_source
        receipts.append(
            {
                "R": modulus,
                "support": sorted(support),
                "source": sorted(source),
                "branch": "G_SUPPORT_SEPARATION",
            }
        )
    return receipts


def verify_f_control() -> dict[str, object]:
    modulus = 27
    generators = (17, 29)
    budgets = (1, 1)
    support, source, differences, target = empty_chart(modulus, generators, budgets)
    assert source == unit_group(modulus)
    assert target in source
    assert target not in support
    assert differences == source

    points = box_points(budgets)
    support_points = tuple(image(generators, point, modulus) for point in points)
    logs = cyclic_logs(2, 18, modulus)
    character_index, score = canonical_cyclic_deficit(
        logs, support_points, target, 18
    )
    assert character_index == 1
    assert character_index % 2 == 1
    assert (character_index * logs[target]) % 18 == 9
    assert score > len(points) / (len(source) - 1)
    assert math.gcd(character_index, 18) == 1
    target_odd_sum = 0.0
    for odd_index in range(1, 18, 2):
        total = sum(
            cmath.exp(2j * math.pi * odd_index * logs[value] / 18)
            for value in support_points
        )
        target_odd_sum += total.real
    assert abs(target_odd_sum - len(source) / 2) <= 1e-10
    return {
        "p": 73,
        "R": modulus,
        "K": 493,
        "support": sorted(support),
        "target": target,
        "branch": "F_SOURCE_DIFFERENCE_Q_DEMAND",
        "q": 2,
        "source_rank": 1,
        "character_index": character_index,
        "target_odd_sum": round(target_odd_sum, 12),
        "score": round(score, 12),
    }


def verify_type_ii_rescue() -> dict[str, int]:
    prime = 241
    a, c, k, b, h = 1, 1, 2, 69, 7
    assert h == 4 * a * c * k - 1
    assert (prime + 4 * a * a * c) % h == 0
    assert (k * prime + a) % h == 0
    assert b == (k * prime + a) // h
    assert b > a
    return {"p": prime, "A": a, "C": c, "K": k, "B": b, "h": h}


def verify() -> None:
    g_receipts = verify_g_controls()
    f_receipt = verify_f_control()
    rescue = verify_type_ii_rescue()
    print("verified fixed Type-I empty-fiber G/F/source-demand dispatch")
    print({"G": g_receipts, "F": f_receipt, "TypeII_rescue": rescue})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
