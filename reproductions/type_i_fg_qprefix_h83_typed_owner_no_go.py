#!/usr/bin/env python3
"""Verify the p=557281 q=83 no-go and eta-relative neutral sheets."""

from __future__ import annotations

import argparse
import math
from itertools import product


P = 557_281
TARGET = 182
Q = 83
MODULUS = 4 * TARGET
BOUND = (P - 1) // 4


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= value:
        while value % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            value //= prime
        prime += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def valuation(value: int, prime: int) -> int | float:
    if value == 0:
        return math.inf
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def canonical_vertex(value: int) -> tuple[int, int, int]:
    d_value = 1
    a_value = 1
    for prime, exponent in factorization(value).items():
        d_value *= prime ** ((exponent + 1) // 2)
        a_value *= prime ** (exponent // 2)
    return d_value, a_value, d_value // a_value


def divisors(value: int) -> tuple[int, ...]:
    result = [1]
    for prime, exponent in factorization(value).items():
        result = [entry * prime**power for entry in result for power in range(exponent + 1)]
    return tuple(sorted(result))


def multiplicative_order(value: int, modulus: int) -> int:
    assert math.gcd(value, modulus) == 1
    current = 1
    for order in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("multiplicative order not found")


def unit_group(modulus: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, modulus) if math.gcd(value, modulus) == 1)


def multiplicative_stabilizer(block: set[int], modulus: int) -> set[int]:
    residues = {value % modulus for value in block}
    return {
        unit
        for unit in unit_group(modulus)
        if {unit * value % modulus for value in residues} == residues
    }


def chi_two(value: int) -> int:
    """Return the quadratic character (2/value) for an odd integer."""
    assert value % 2 == 1
    return 1 if value % 8 in (1, 7) else -1


def verify_typed_owner_no_go() -> dict[str, object]:
    numerator = P + 4 * TARGET
    assert MODULUS == 728
    assert BOUND == 139_320
    assert numerator == 3**4 * Q**2
    assert valuation(numerator, Q) == 2
    assert canonical_vertex(TARGET) == (182, 1, 182)

    possible_layer_depth = tuple(
        (base_layer, depth)
        for base_layer in range(1, 3)
        for depth in range(1, 3)
        if base_layer + depth <= valuation(numerator, Q)
    )
    assert possible_layer_depth == ((1, 1),)

    # D*=182 divides D(s0), hence divides s0. The target congruence then
    # leaves only t=1 in s0=182*t because t is far below 1+83^2.
    t_bound = BOUND // TARGET
    deep_multipliers = tuple(
        multiplier
        for multiplier in range(1, t_bound + 1)
        if (TARGET * multiplier - TARGET) % Q**2 == 0
    )
    assert t_bound == 765
    assert deep_multipliers == (1,)
    deep = TARGET * deep_multipliers[0]
    assert canonical_vertex(deep)[0] == TARGET
    assert valuation(P + 4 * deep, Q) == 2

    # The canonical fixed-D slots are s1=182*A with A|182.
    source_as = divisors(TARGET)
    shallow_rows = tuple(TARGET * a_value for a_value in source_as)
    assert source_as == (1, 2, 7, 13, 14, 26, 91, 182)
    assert all(row <= BOUND for row in shallow_rows)
    assert all(canonical_vertex(row)[0] == TARGET for row in shallow_rows)

    divisible_by_83 = tuple(
        (a_value, row, valuation(P + 4 * row, Q))
        for a_value, row in zip(source_as, shallow_rows)
        if (P + 4 * row) % Q == 0
    )
    assert divisible_by_83 == ((1, TARGET, 2),)
    shallow_height_one = tuple(
        row for row in shallow_rows if valuation(P + 4 * row, Q) == 1
    )
    assert shallow_height_one == ()

    source_group_order = len(unit_group(199))
    target_group_order = len(unit_group(MODULUS))
    assert source_group_order == 198
    assert target_group_order == 288
    assert source_group_order % Q != 0
    assert target_group_order % Q != 0
    assert multiplicative_order(Q, MODULUS) == 4
    assert math.gcd(4, Q) == 1

    return {
        "status": "P557_H83_TYPED_OWNER_GRAMMAR_NO_GO",
        "only_layer_depth_pair": possible_layer_depth[0],
        "forced_deep_source": deep,
        "canonical_shallow_rows": shallow_rows,
        "height_one_shallow_menu": shallow_height_one,
        "source_c83_role_rank": 0,
        "target_c83_role_rank": 0,
        "order_83_mod_728": 4,
        "arithmetic_factor_83_square_exact": numerator % Q**2 == 0,
    }


def verify_neutral_sheets(no_go: dict[str, object]) -> dict[str, object]:
    def eta(value):
        return pow(value % 13, 4, 13)
    active_three_block = tuple(3**exponent for exponent in range(4))
    assert active_three_block == (1, 3, 9, 27)
    assert tuple(eta(value) for value in active_three_block) == (1, 3, 9, 1)

    sheets = {
        exponent_83: tuple(3**exponent_3 * Q**exponent_83 for exponent_3 in range(4))
        for exponent_83 in (1, 2)
    }
    residues = {
        exponent_83: tuple(value % MODULUS for value in sheet)
        for exponent_83, sheet in sheets.items()
    }
    eta_images = {
        exponent_83: tuple(eta(value) for value in sheet)
        for exponent_83, sheet in sheets.items()
    }
    assert sheets == {
        1: (83, 249, 747, 2_241),
        2: (6_889, 20_667, 62_001, 186_003),
    }
    assert residues == {
        1: (83, 249, 19, 57),
        2: (337, 283, 121, 363),
    }
    assert eta_images == {
        1: (1, 3, 9, 1),
        2: (1, 3, 9, 1),
    }

    completed_box = {
        3**exponent_3 * Q**exponent_83
        for exponent_3, exponent_83 in product(range(4), range(3))
    }
    completed_residues = {value % MODULUS for value in completed_box}
    assert len(completed_box) == 12
    assert len(completed_residues) == 12
    assert completed_box == set(active_three_block) | set(sheets[1]) | set(sheets[2])

    completed_stabilizer = multiplicative_stabilizer(completed_box, MODULUS)
    assert completed_stabilizer == {1}
    assert chi_two(Q) == -1
    conditional_full_group_price = min(
        2,
        multiplicative_order(Q, MODULUS) - 1,
    )
    assert conditional_full_group_price == 2
    q83_request_increment = int(
        no_go["status"] != "P557_H83_TYPED_OWNER_GRAMMAR_NO_GO"
    )
    c83_role_rank_increment = max(
        int(no_go["source_c83_role_rank"]),
        int(no_go["target_c83_role_rank"]),
    )
    eta_c3_capacity_increment = 0 if eta(Q) == 1 else 1
    assert q83_request_increment == 0
    assert c83_role_rank_increment == 0
    assert eta_c3_capacity_increment == 0
    physical_adapter_proved = False
    fiber_realized = False
    required_ledger_price_status = (
        "UNPRICED"
        if not physical_adapter_proved or not fiber_realized
        else "REPRICE_AT_FINAL_STABILIZER"
    )
    assert required_ledger_price_status == "UNPRICED"

    return {
        "status": "P557_H83_ETA_C3_NEUTRAL_SHEETS_EXACT",
        "sheet_residues": residues,
        "sheet_eta_images": eta_images,
        "completed_box_residue_count": len(completed_residues),
        "q83_request_increment_current_grammar": q83_request_increment,
        "c83_role_rank_increment": c83_role_rank_increment,
        "eta_c3_capacity_increment": eta_c3_capacity_increment,
        "chi_two_of_83": -1,
        "completed_box_stabilizer": tuple(sorted(completed_stabilizer)),
        "required_ledger_price_status": required_ledger_price_status,
        "price_status_is_arithmetic_theorem": False,
        "conditional_price_if_final_stabilizer_trivial": (
            conditional_full_group_price
        ),
        "physical_neutral_product_adapter_proved": physical_adapter_proved,
        "fiber_realized": fiber_realized,
    }


def verify() -> None:
    no_go = verify_typed_owner_no_go()
    sheets = verify_neutral_sheets(no_go)
    print("PASS: FG_QPREFIX_H83_TYPED_OWNER_NO_GO")
    print(no_go)
    print(sheets)


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
