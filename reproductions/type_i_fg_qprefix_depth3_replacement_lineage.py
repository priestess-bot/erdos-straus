#!/usr/bin/env python3
"""Verify the p=557281 q=3 depth-3 replacement lineage classification."""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from itertools import product


P = 557_281
Q = 3
TARGET = 182
DEPTH = 3
BASE_LAYER = 1
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


def canonical_vertex(value: int) -> tuple[int, int, int]:
    """Return the unique canonical (D, A, C) with value=D*A=A^2*C."""
    d_value = 1
    a_value = 1
    for prime, exponent in factorization(value).items():
        d_value *= prime ** ((exponent + 1) // 2)
        a_value *= prime ** (exponent // 2)
    c_value = d_value // a_value
    assert value == d_value * a_value == a_value * a_value * c_value
    return d_value, a_value, c_value


def valuation(value: int, prime: int) -> int | float:
    if value == 0:
        return math.inf
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def squarefree_divisors_of_rad(value: int) -> tuple[int, ...]:
    primes = tuple(factorization(value))
    return tuple(
        sorted(
            math.prod(prime for prime, use_prime in zip(primes, bits) if use_prime)
            for bits in product((False, True), repeat=len(primes))
        )
    )


def canonical_slots(d_value: int) -> tuple[int, ...]:
    return tuple(
        sorted(
            d_value * d_value // divisor
            for divisor in squarefree_divisors_of_rad(d_value)
            if d_value * d_value // divisor <= BOUND
        )
    )


def analytic_deep_records() -> tuple[tuple[int, int], ...]:
    target_base = canonical_vertex(TARGET)[0]
    records = []
    for index in range(10):
        source = TARGET * (1 + Q ** (BASE_LAYER + DEPTH) * index)
        records.append((source, canonical_vertex(source)[0]))
    assert records[-1][0] <= BOUND
    assert TARGET * (1 + Q ** (BASE_LAYER + DEPTH) * 10) > BOUND
    assert all(source % target_base == 0 for source, _ in records)
    return tuple(records)


def direct_label_enumeration() -> tuple[
    tuple[tuple[int, int], ...], tuple[tuple[int, int, int], ...]
]:
    target_base = canonical_vertex(TARGET)[0]
    slots_by_base: dict[int, list[int]] = defaultdict(list)
    for label in range(1, BOUND + 1):
        slots_by_base[canonical_vertex(label)[0]].append(label)

    deep_records: list[tuple[int, int]] = []
    typed_pairs: list[tuple[int, int, int]] = []
    first = TARGET
    step = Q ** (BASE_LAYER + DEPTH)
    for deep in range(first, BOUND + 1, step):
        d_value = canonical_vertex(deep)[0]
        if d_value % target_base:
            continue
        deep_records.append((deep, d_value))
        for shallow in slots_by_base[d_value]:
            if valuation(P + 4 * shallow, Q) != BASE_LAYER:
                continue
            difference = shallow - deep
            if difference % Q ** BASE_LAYER:
                continue
            if difference // Q ** BASE_LAYER % Q != 1:
                continue
            typed_pairs.append((deep, shallow, d_value))
    return tuple(deep_records), tuple(typed_pairs)


def inverse_slot_enumeration(
    deep_records: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, int, int], ...]:
    typed_pairs = []
    for deep, d_value in deep_records:
        for shallow in canonical_slots(d_value):
            if shallow % 9 == 5:
                typed_pairs.append((deep, shallow, d_value))
    return tuple(typed_pairs)


def verify_classification() -> dict[str, object]:
    assert BOUND == 139_320
    assert factorization(P) == {P: 1}
    assert P % 24 == 1
    target_base, target_a, target_c = canonical_vertex(TARGET)
    assert (target_base, target_a, target_c) == (182, 1, 182)
    assert target_base == 2 * 7 * 13
    assert P + 4 * TARGET == 3**4 * 83**2
    assert valuation(P + 4 * TARGET, Q) == 4
    assert BASE_LAYER + DEPTH == 4

    expected_deep = (
        (182, 182),
        (14_924, 7_462),
        (29_666, 29_666),
        (44_408, 22_204),
        (59_150, 910),
        (73_892, 5_278),
        (88_634, 88_634),
        (103_376, 25_844),
        (118_118, 118_118),
        (132_860, 66_430),
    )
    expected_pairs = (
        (182, 1_274, 182),
        (14_924, 104_468, 7_462),
        (59_150, 4_550, 910),
        (59_150, 12_740, 910),
        (73_892, 137_228, 5_278),
    )

    analytic_deep = analytic_deep_records()
    direct_deep, direct_pairs = direct_label_enumeration()
    inverse_pairs = inverse_slot_enumeration(analytic_deep)
    assert analytic_deep == direct_deep == expected_deep
    assert direct_pairs == inverse_pairs == expected_pairs

    shallow_menu = {
        deep: tuple(shallow for d0, shallow, _ in expected_pairs if d0 == deep)
        for deep, _ in expected_deep
    }
    assert shallow_menu == {
        182: (1_274,),
        14_924: (104_468,),
        29_666: (),
        44_408: (),
        59_150: (4_550, 12_740),
        73_892: (137_228,),
        88_634: (),
        103_376: (),
        118_118: (),
        132_860: (),
    }

    phase_rows = []
    full_c9_pairs = []
    for deep, shallow, d_value in expected_pairs:
        assert 0 < 4 * deep < P and 0 < 4 * shallow < P
        assert canonical_vertex(deep)[0] == canonical_vertex(shallow)[0] == d_value
        assert d_value % target_base == 0
        assert valuation(P + 4 * deep, Q) >= BASE_LAYER + DEPTH
        assert valuation(TARGET - deep, Q) >= BASE_LAYER + DEPTH
        assert valuation(P + 4 * shallow, Q) == BASE_LAYER
        difference = shallow - deep
        assert valuation(difference, Q) == BASE_LAYER
        assert difference // Q % Q == 1
        phase_mod_9 = difference // Q % 9
        phase_rows.append((deep, shallow, difference, phase_mod_9))
        if phase_mod_9 == 4:
            full_c9_pairs.append((deep, shallow, d_value))

    assert tuple(phase_rows) == (
        (182, 1_274, 1_092, 4),
        (14_924, 104_468, 89_544, 4),
        (59_150, 4_550, -54_600, 7),
        (59_150, 12_740, -46_410, 1),
        (73_892, 137_228, 63_336, 7),
    )
    assert tuple(full_c9_pairs) == (
        (182, 1_274, 182),
        (14_924, 104_468, 7_462),
    )

    return {
        "forced_base_layer": BASE_LAYER,
        "maximum_depth_at_fixed_target": DEPTH,
        "candidate_binding_deep_records": expected_deep,
        "arithmetic_typed_admission_candidates": expected_pairs,
        "chosen_edge_c9_candidates": tuple(full_c9_pairs),
        "phase_rows": tuple(phase_rows),
    }


def verify_witness() -> dict[str, object]:
    deep, shallow, source_base = 14_924, 104_468, 7_462
    target_base = canonical_vertex(TARGET)[0]
    assert canonical_vertex(deep) == (7_462, 2, 3_731)
    assert canonical_vertex(shallow) == (7_462, 14, 533)
    assert factorization(3_731) == {7: 1, 13: 1, 41: 1}
    assert factorization(533) == {13: 1, 41: 1}
    assert source_base == target_base * 41
    assert deep - TARGET == 3**4 * TARGET
    assert shallow == 7 * deep

    difference = shallow - deep
    assert factorization(P + 4 * deep) == {3: 5, 2_539: 1}
    assert factorization(P + 4 * shallow) == {3: 1, 325_051: 1}
    assert factorization(deep - TARGET) == {2: 1, 3: 4, 7: 1, 13: 1}
    assert factorization(difference) == {2: 3, 3: 1, 7: 1, 13: 1, 41: 1}
    assert difference == 89_544
    assert difference // 3 == 29_848
    assert difference // 3 % 3 == 1
    assert difference // 3 % 9 == 4

    beta = (-P * pow(4, -1, Q)) % Q
    tail_modulus = Q**DEPTH
    def tail(value):
        return (value - beta) // Q % tail_modulus
    assert beta == 2
    assert (tail(TARGET), tail(deep), tail(shallow)) == (6, 6, 19)
    assert (tail(shallow) - tail(deep)) % 9 == 4

    numerator = P + 4 * TARGET
    modulus = 4 * target_base
    block = tuple(Q**exponent for exponent in range(DEPTH + 1))
    assert block == (1, 3, 9, 27)
    assert all(numerator % entry == 0 for entry in block)

    def eta(value):
        return pow(value % 13, 4, 13)
    eta_image = tuple(eta(entry) for entry in block)
    assert eta_image == (1, 3, 9, 1)
    units = tuple(value for value in range(1, modulus) if math.gcd(value, modulus) == 1)
    kernel = {value for value in units if eta(value) == 1}
    section = {
        value
        for value in kernel
        if (-value) % modulus in {entry % modulus for entry in block}
    }
    assert len(kernel) == 96
    assert section == {701, 727}
    assert len(section) * (len(kernel) - len(section)) == 188

    assignment_new = (
        "EXPLICIT_TARGET_ODD_INDEX_43",
        TARGET,
        deep,
        shallow,
        source_base,
    )
    lineage_new = (assignment_new, Q, BASE_LAYER, DEPTH)
    direction_new = ((TARGET, 1, TARGET), Q % modulus, lineage_new)
    block_residues = {entry % modulus for entry in block}
    block_stabilizer = {
        unit
        for unit in units
        if {unit * entry % modulus for entry in block_residues} == block_residues
    }
    assert block_stabilizer == {1}
    stabilizer_snapshot_new = (modulus, tuple(sorted(block_stabilizer)))
    charge_new = (direction_new, stabilizer_snapshot_new)
    price_status_new = "UNPRICED"
    atoms = tuple((assignment_new, level) for level in range(1, DEPTH + 1))
    alpha_new = {
        atom: (charge_new, level) for level, atom in enumerate(atoms, start=1)
    }
    assert len(alpha_new) == DEPTH
    assert len(set(alpha_new.values())) == DEPTH
    assert {token[-1] for token in alpha_new.values()} == {1, 2, 3}

    source_keys = tuple(
        ("S-new", deep, Q, BASE_LAYER + level)
        for level in range(1, DEPTH + 1)
    )
    target_keys = tuple(
        ("T", TARGET, Q, BASE_LAYER + level) for level in range(1, DEPTH + 1)
    )
    shallow_key = ("S-new", "edge-2", shallow, source_base)
    standalone_ledger: set[tuple[object, ...]] = set()
    new_layer_keys = set(source_keys + target_keys)
    assert len(new_layer_keys) == 2 * DEPTH
    assert new_layer_keys.isdisjoint(standalone_ledger)
    assert shallow_key not in standalone_ledger

    old_assignment = (
        "EXPLICIT_TARGET_ODD_INDEX_43",
        TARGET,
        19_838,
        138_866,
        19_838,
    )
    old_target_keys = {
        ("T", TARGET, Q, BASE_LAYER + level) for level in range(1, 3)
    }
    old_source_keys = {
        ("S-old", 19_838, Q, BASE_LAYER + level) for level in range(1, 3)
    }
    old_active_ledger = old_target_keys | old_source_keys
    assert set(target_keys) & old_active_ledger == old_target_keys
    assert set(source_keys).isdisjoint(old_active_ledger)
    assert not new_layer_keys.isdisjoint(old_active_ledger)
    assert assignment_new != old_assignment
    assert set(target_keys) != old_target_keys

    return {
        "status": "P557_ACTUAL_F_Q3_DEPTH3_STANDALONE_FRESH_LEDGER_LINEAGE",
        "target": TARGET,
        "source_rows": (deep, shallow),
        "source_base": source_base,
        "source_line": (deep, difference),
        "heights": (
            valuation(P + 4 * TARGET, Q),
            valuation(P + 4 * deep, Q),
            valuation(P + 4 * shallow, Q),
        ),
        "tail_mod_27": (tail(TARGET), tail(deep), tail(shallow)),
        "block": block,
        "eta_image": eta_image,
        "kernel_section": tuple(sorted(section)),
        "kernel_energy": 188,
        "assignment_id": assignment_new,
        "block_lineage_id": lineage_new,
        "charge_key": charge_new,
        "stabilizer_snapshot": stabilizer_snapshot_new,
        "price_status": price_status_new,
        "owner_map_size": len(alpha_new),
        "standalone_new_keys_fresh": True,
        "shallow_occurrence_capacity": 1,
        "legacy_target_overlap": tuple(sorted(old_target_keys)),
        "legacy_plain_insert_status": (
            "Q_PREFIX_PARTIAL_OVERLAP_NOT_FRESH_OR_FULL_REPLAY"
        ),
        "atomic_replacement_verified_separately": True,
        "atomic_replacement_scope": "P557_ISOLATED_SINGLE_REQUEST_LEDGER_V1",
        "atomic_replacement_status": (
            "P557_ISOLATED_SINGLE_REQUEST_Q3_DEPTH2_TO_DEPTH3_"
            "ATOMIC_REPLACEMENT"
        ),
        "old_receipt_disposition": "ALTERNATIVE_NOT_COCHARGED",
        "capacity_price_registered": False,
        "active_labelled_prefix_depth_legacy": (2, 0),
        "conditional_ambient_kernel_defect_legacy": (1, 2),
        "active_labelled_prefix_depth_fresh_choice": (3, 0),
        "conditional_ambient_kernel_defect_fresh_choice": (0, 2),
        "neutral_cargo_realized": False,
        "physical_source_exactness_proved": False,
        "e4_e5_proved": False,
    }


def verify() -> None:
    receipt = {
        "status": "PASS",
        "classification": verify_classification(),
        "witness": verify_witness(),
    }
    print(json.dumps(receipt, ensure_ascii=True, sort_keys=True))


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
