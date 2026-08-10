#!/usr/bin/env python3
"""Verify the p557 common-base capacity no-go and cross-base ladder."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
from math import prod


P = 557281
B_P = (P - 1) // 4
TARGET = 182
OWNER_MODULUS = 3
OWNER_RESIDUE = 2
SOURCE_MODULUS = 199

FACTORS = (2, 5, 11, 2083)
BOUNDS = ((-1, 1), (-1, 1), (-3, 3), (-1, 1))
STEPS = {
    "a": (0, 0, -2, 1),
    "r": (0, 1, -5, 0),
    "s": (0, -1, 1, 2),
    "t": (0, 2, 3, 2),
}

LINE_INTERCEPT = 14924
LINE_COEFFICIENTS = (89544, 14832, 2781, 5652)


def factorization(value: int) -> tuple[tuple[int, int], ...]:
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            exponent = 0
            while value % divisor == 0:
                value //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1 if divisor == 2 else 2
    if value > 1:
        factors.append((value, 1))
    return tuple(factors)


def squarefree_divisors(value: int) -> tuple[int, ...]:
    primes = tuple(prime for prime, _ in factorization(value))
    return tuple(
        prod(choice)
        for choice in product(*((1, prime) for prime in primes))
    )


def canonical_state(value: int) -> tuple[int, int, int]:
    factors = factorization(value)
    base = prod(prime ** ((exponent + 1) // 2) for prime, exponent in factors)
    row = prod(prime ** (exponent // 2) for prime, exponent in factors)
    return base, row, base // row


def owner_labels(base: int) -> tuple[int, ...]:
    return tuple(
        sorted(
            base * base // squarefree
            for squarefree in squarefree_divisors(base)
            if base * base // squarefree <= B_P
            and base * base // squarefree % OWNER_MODULUS == OWNER_RESIDUE
        )
    )


def add(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def inside(record: tuple[int, ...]) -> bool:
    return all(
        lower <= coordinate <= upper
        for coordinate, (lower, upper) in zip(record, BOUNDS)
    )


def source_value(record: tuple[int, ...]) -> int:
    value = 1
    for factor, exponent in zip(FACTORS, record):
        value = value * pow(factor, exponent, SOURCE_MODULUS) % SOURCE_MODULUS
    return value


def line_value(record: tuple[int, ...]) -> int:
    return LINE_INTERCEPT + sum(
        coefficient * coordinate
        for coefficient, coordinate in zip(LINE_COEFFICIENTS, record)
    )


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def verify_common_base_capacity() -> None:
    target_bases = tuple(range(TARGET, B_P + 1, TARGET))
    eligible_bases = tuple(base for base in target_bases if base % 3 != 0)
    nonempty = {
        base: owner_labels(base)
        for base in target_bases
        if owner_labels(base)
    }
    rich = {
        base: labels for base, labels in nonempty.items() if len(labels) >= 3
    }

    assert len(target_bases) == 765
    assert len(eligible_bases) == 510
    assert len(nonempty) == 195
    assert sum(len(labels) for labels in nonempty.values()) == 255

    expected_rich = {
        182: (182, 1274, 2366, 16562),
        364: (728, 5096, 9464, 66248),
        728: (2912, 20384, 37856),
        910: (1820, 4550, 12740, 23660, 31850, 59150),
        1274: (8918, 62426, 115934),
        1820: (7280, 18200, 50960, 94640, 127400),
        2002: (4004, 22022, 28028, 52052),
        3094: (6188, 43316, 52598, 80444),
        3458: (3458, 24206, 44954, 65702),
        4004: (16016, 88088, 112112),
        4186: (8372, 58604, 96278, 108836),
        5278: (10556, 73892, 137228),
        5642: (5642, 39494, 73346),
        6734: (6734, 47138, 87542),
        7826: (7826, 54782, 101738),
        10010: (10010, 70070, 100100, 130130),
    }
    assert rich == expected_rich

    capacities = {
        (base, residue): sum(label % 9 == residue for label in labels)
        for base, labels in nonempty.items()
        for residue in (2, 5, 8)
    }
    assert max(capacities.values()) == 2
    assert all(capacity <= 2 for capacity in capacities.values())

    phase_edges = tuple(
        (base, start, end)
        for base, labels in nonempty.items()
        for start in labels
        for end in labels
        if (end - start) % 27 == 9
    )
    assert phase_edges == (
        (182, 16562, 182),
        (364, 66248, 728),
        (910, 1820, 59150),
        (910, 4550, 12740),
        (910, 23660, 31850),
        (1820, 18200, 50960),
        (1820, 94640, 127400),
        (2002, 4004, 22022),
        (3094, 52598, 80444),
        (3458, 3458, 65702),
        (4004, 16016, 88088),
        (4186, 58604, 96278),
        (10010, 100100, 10010),
    )

    for base, labels in nonempty.items():
        for first in labels:
            seconds = tuple(
                second for second in labels if (second - first) % 27 == 9
            )
            for second in seconds:
                assert not any(
                    (third - second) % 27 == 9 for third in labels
                ), (base, first, second, labels)

    # Removing target compatibility gives a strict positive boundary control.
    positive = (10580, 2300, 230)
    assert all(label in owner_labels(230) for label in positive)
    assert all(canonical_state(label)[0] == 230 for label in positive)
    assert all(
        (right - left) % 27 == 9
        for left, right in zip(positive, positive[1:])
    )
    assert 230 % TARGET != 0


def verify_affine_ladder() -> None:
    records = tuple(
        product(*(range(lower, upper + 1) for lower, upper in BOUNDS))
    )
    assert len(records) == 189

    candidate_steps = tuple(
        product(range(-2, 3), range(-2, 3), range(-6, 7), range(-2, 3))
    )
    valid_steps = tuple(
        step for step in candidate_steps if source_value(step) == 83
    )
    assert set(valid_steps) == set(STEPS.values())

    labelled_chains = []
    for start in records:
        for first_name, first_step in STEPS.items():
            middle = add(start, first_step)
            if not inside(middle):
                continue
            for second_name, second_step in STEPS.items():
                end = add(middle, second_step)
                if inside(end):
                    labelled_chains.append(
                        (start, first_name, second_name, middle, end)
                    )
    assert len(labelled_chains) == 51

    chain_records = {
        record
        for start, _, _, middle, end in labelled_chains
        for record in (start, middle, end)
    }
    assert len(chain_records) == 105

    # This is an extension of the active line 14924 + 89544*z_2.
    origin = (0, 0, 0, 0)
    factor_two = (1, 0, 0, 0)
    assert line_value(origin) == 14924
    assert line_value(factor_two) == 104468
    assert tuple((coefficient // 3) % 9 for coefficient in LINE_COEFFICIENTS) == (
        4,
        3,
        0,
        3,
    )

    expected_increments = {"a": 90, "r": 927, "s": -747, "t": 49311}
    for name, step in STEPS.items():
        increment = sum(
            coefficient * coordinate
            for coefficient, coordinate in zip(LINE_COEFFICIENTS, step)
        )
        assert increment == expected_increments[name]
        assert (increment // 3) % 9 == 3

    # Exhaustive check complements the short modular injectivity proof in the claim.
    assert len({line_value(record) for record in records}) == len(records)
    in_range_chain_records = {
        record for record in chain_records if 1 <= line_value(record) <= B_P
    }
    assert len(in_range_chain_records) == 67
    in_range_chains = tuple(
        chain
        for chain in labelled_chains
        if all(
            1 <= line_value(record) <= B_P
            for record in (chain[0], chain[3], chain[4])
        )
    )
    assert len(in_range_chains) == 33
    assert Counter((chain[1], chain[2]) for chain in in_range_chains) == Counter(
        {("a", "a"): 17, ("r", "s"): 8, ("s", "r"): 8}
    )

    start = (0, -1, 2, -1)
    middle = add(start, STEPS["r"])
    end = add(middle, STEPS["s"])
    assert (middle, end) == ((0, 0, -3, -1), (0, -1, -2, 1))

    selected = (start, middle, end)
    labels = tuple(line_value(record) for record in selected)
    assert labels == (2, 929, 182)
    assert all(1 <= label <= B_P and label % 3 == 2 for label in labels)

    images = tuple(source_value(record) for record in selected)
    assert images == (82, 40, 136)
    assert tuple(
        images[index + 1] * pow(images[index], -1, SOURCE_MODULUS)
        % SOURCE_MODULUS
        for index in range(2)
    ) == (83, 83)

    assert tuple(canonical_state(label) for label in labels) == (
        (2, 1, 2),
        (929, 1, 929),
        (182, 1, 182),
    )
    assert tuple((label - OWNER_RESIDUE) // OWNER_MODULUS for label in labels) == (
        0,
        309,
        60,
    )

    numerators = tuple(P + 4 * label for label in labels)
    assert tuple(factorization(value) for value in numerators) == (
        ((3, 2), (19, 1), (3259, 1)),
        ((3, 2), (83, 1), (751, 1)),
        ((3, 4), (83, 2)),
    )
    assert tuple(valuation(value, 83) for value in numerators) == (0, 1, 2)

    bases = tuple(canonical_state(label)[0] for label in labels)
    assert bases == (2, 929, 182)
    assert len(set(bases)) == 3
    # The prescribed-target contract is D_x | D_b, not the reverse divisibility.
    assert tuple(base % TARGET == 0 for base in bases) == (False, False, True)


def verify() -> None:
    verify_common_base_capacity()
    verify_affine_ladder()
    print("P557_TARGET182_COMMON_BASE_83_THREE_SHEET_CAPACITY_NO_GO")
    print("P557_ACTIVE_LINE_FULL_BOX_SEPARATING_EXTENSION_CERT")
    print("P557_CROSS_BASE_H83_OWNER_WINDOW_VALUATION_LADDER")
    print("P557_CROSS_BASE_PHYSICAL_CARGO_ADAPTER_UNPROVED")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
