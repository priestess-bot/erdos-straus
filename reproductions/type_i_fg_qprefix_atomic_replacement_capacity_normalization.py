#!/usr/bin/env python3
"""Verify prefix-monotone q-prefix replacement and p=557281 normalization."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter


Resource = tuple[object, ...]


def unit_group(modulus: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, modulus) if math.gcd(value, modulus) == 1)


def multiplicative_stabilizer(block: tuple[int, ...], modulus: int) -> set[int]:
    residues = {value % modulus for value in block}
    return {
        unit
        for unit in unit_group(modulus)
        if {unit * value % modulus for value in residues} == residues
    }


def replace_load(
    current: Counter[Resource],
    old_use: Counter[Resource],
    new_use: Counter[Resource],
    capacity: dict[Resource, int],
) -> Counter[Resource]:
    support = set(current) | set(old_use) | set(new_use)
    assert support <= set(capacity)
    assert all(0 <= current[key] <= capacity[key] for key in capacity)
    assert all(old_use[key] <= current[key] for key in old_use)
    result: Counter[Resource] = Counter()
    for key in capacity:
        value = current[key] - old_use[key] + new_use[key]
        assert 0 <= value <= capacity[key]
        if value:
            result[key] = value
    return result


def descendants(
    root: tuple[object, ...],
    edges: set[tuple[tuple[object, ...], tuple[object, ...]]],
) -> set[tuple[object, ...]]:
    closure = {root}
    frontier = [root]
    while frontier:
        parent = frontier.pop()
        for left, right in edges:
            if left == parent and right not in closure:
                closure.add(right)
                frontier.append(right)
    return closure


def is_acyclic(
    nodes: set[tuple[object, ...]],
    edges: set[tuple[tuple[object, ...], tuple[object, ...]]],
) -> bool:
    indegree = {node: 0 for node in nodes}
    children = {node: set() for node in nodes}
    for parent, child in edges:
        assert parent in nodes and child in nodes
        children[parent].add(child)
        indegree[child] += 1
    frontier = [node for node, degree in indegree.items() if degree == 0]
    visited = 0
    while frontier:
        parent = frontier.pop()
        visited += 1
        for child in children[parent]:
            indegree[child] -= 1
            if indegree[child] == 0:
                frontier.append(child)
    return visited == len(nodes)


def contains_nested(value: object, needle: object) -> bool:
    if value == needle:
        return True
    if isinstance(value, (tuple, list, set, frozenset)):
        return any(contains_nested(entry, needle) for entry in value)
    if isinstance(value, dict):
        return any(
            contains_nested(key, needle) or contains_nested(entry, needle)
            for key, entry in value.items()
        )
    return False


def additive_stabilizer(block: set[int], modulus: int) -> set[int]:
    return {
        shift
        for shift in range(modulus)
        if {(value + shift) % modulus for value in block} == block
    }


def verify_generic_boundaries() -> None:
    # Partial overlap is harmless after the old load is subtracted atomically.
    old = Counter({("shared",): 1, ("old",): 1})
    new = Counter({("shared",): 1, ("new",): 1})
    capacity = {key: 1 for key in old.keys() | new.keys()}
    assert replace_load(old, old, new, capacity) == new

    # External load on a new-only key is the real capacity obstruction.
    external = Counter({("new",): 1})
    current = old + external
    try:
        replace_load(current, old, new, capacity)
    except AssertionError:
        pass
    else:
        raise AssertionError("external residual-capacity conflict was accepted")

    # A stabilizer snapshot is assignment-dependent and must be recomputed.
    old_block = {0, 2}
    new_block = {0, 2, 4}
    assert additive_stabilizer(old_block, 6) == {0}
    assert additive_stabilizer(new_block, 6) == {0, 2, 4}


def verify_p557_transaction() -> dict[str, object]:
    p = 557_281
    target = 182
    q = 3
    base_layer = 1
    modulus = 728
    digest = "EXPLICIT_TARGET_ODD_INDEX_43"

    old_assignment = (digest, target, 19_838, 138_866, 19_838)
    new_assignment = (digest, target, 14_924, 104_468, 7_462)
    old_lineage = (old_assignment, q, base_layer, 2)
    new_lineage = (new_assignment, q, base_layer, 3)

    old_block = (1, 3, 9)
    new_block = (1, 3, 9, 27)
    old_stabilizer = multiplicative_stabilizer(old_block, modulus)
    new_stabilizer = multiplicative_stabilizer(new_block, modulus)
    assert old_stabilizer == new_stabilizer == {1}

    fiber_digest = (target, 1, target)
    old_charge = ((fiber_digest, q % modulus, old_lineage), (modulus, (1,)))
    new_charge = ((fiber_digest, q % modulus, new_lineage), (modulus, (1,)))
    assert old_charge != new_charge

    old_atoms = tuple((old_assignment, level) for level in range(1, 3))
    new_atoms = tuple((new_assignment, level) for level in range(1, 4))
    old_owner = {atom: (old_charge, level) for level, atom in enumerate(old_atoms, 1)}
    new_owner = {atom: (new_charge, level) for level, atom in enumerate(new_atoms, 1)}
    injection = {old_atoms[level - 1]: new_atoms[level - 1] for level in range(1, 3)}
    charge_rekey = {
        old_owner[old_atoms[level - 1]]: new_owner[new_atoms[level - 1]]
        for level in range(1, 3)
    }
    assert all(
        charge_rekey[old_owner[atom]] == new_owner[injection[atom]]
        for atom in old_atoms
    )

    old_source = {
        ("S-old", 19_838, q, absolute_layer) for absolute_layer in (2, 3)
    }
    new_source = {
        ("S-new", 14_924, q, absolute_layer) for absolute_layer in (2, 3, 4)
    }
    old_target = {("T", target, q, absolute_layer) for absolute_layer in (2, 3)}
    new_target = {
        ("T", target, q, absolute_layer) for absolute_layer in (2, 3, 4)
    }
    old_shallow = {("S-old", "edge-2", 138_866, 19_838)}
    new_shallow = {("S-new", "edge-2", 104_468, 7_462)}
    old_keys = old_source | old_target | old_shallow
    new_keys = new_source | new_target | new_shallow

    assert old_keys & new_keys == old_target
    assert old_keys - new_keys == old_source | old_shallow
    assert new_keys - old_keys == new_source | {("T", target, q, 4)} | new_shallow
    assert len(old_keys ^ new_keys) == 8

    old_use = Counter({key: 1 for key in old_keys})
    new_use = Counter({key: 1 for key in new_keys})
    capacity = {key: 1 for key in old_keys | new_keys}
    new_load = replace_load(old_use, old_use, new_use, capacity)
    assert new_load == new_use
    assert all(new_load[key] == 1 for key in old_target)
    assert all(new_load[key] == 0 for key in old_source | old_shallow)

    old_occurrence_owner = {
        key: (old_assignment, old_charge, "q-layer")
        for key in old_source | old_target
    }
    old_occurrence_owner.update(
        {key: (old_assignment, old_charge, "shallow") for key in old_shallow}
    )
    new_occurrence_owner = {
        key: (new_assignment, new_charge, "q-layer")
        for key in new_source | new_target
    }
    new_occurrence_owner.update(
        {key: (new_assignment, new_charge, "shallow") for key in new_shallow}
    )
    old_token_occurrences = {
        old_owner[old_atoms[level - 1]]: {
            ("S-old", 19_838, q, base_layer + level),
            ("T", target, q, base_layer + level),
        }
        for level in range(1, 3)
    }
    new_token_occurrences = {
        new_owner[new_atoms[level - 1]]: {
            ("S-new", 14_924, q, base_layer + level),
            ("T", target, q, base_layer + level),
        }
        for level in range(1, 4)
    }
    for old_token, new_token in charge_rekey.items():
        old_target_backpointer = {
            key for key in old_token_occurrences[old_token] if key[0] == "T"
        }
        new_target_backpointer = {
            key for key in new_token_occurrences[new_token] if key[0] == "T"
        }
        assert old_target_backpointer == new_target_backpointer
    assert all(
        new_occurrence_owner[key][0] == new_assignment for key in old_target
    )
    assert not any(
        contains_nested(owner, old_assignment)
        for owner in new_occurrence_owner.values()
    )

    def eta(value):
        return pow(value % 13, 4, 13)
    kernel = {
        value for value in unit_group(modulus) if eta(value) == 1
    }
    old_section = {
        value
        for value in kernel
        if (-value) % modulus in {entry % modulus for entry in old_block}
    }
    new_section = {
        value
        for value in kernel
        if (-value) % modulus in {entry % modulus for entry in new_block}
    }
    assert len(kernel) == 96
    assert old_section == {727}
    assert new_section == {701, 727}
    assert len(old_section) * (len(kernel) - len(old_section)) == 95
    assert len(new_section) * (len(kernel) - len(new_section)) == 188

    target_height = 4
    maximum_depth = target_height - base_layer
    factor_box = {
        3**exponent_3 * 83**exponent_83 % modulus
        for exponent_3 in range(5)
        for exponent_83 in range(3)
    }
    factor_target_miss = (-1) % modulus not in factor_box
    assert factor_target_miss
    upstream_receipt_payloads = (
        (
            "P557_Q3_DEPTH2_TYPED_ASSIGNMENT",
            old_assignment,
            old_block,
            tuple(sorted(old_stabilizer)),
        ),
        (
            "P557_Q3_DEPTH3_STANDALONE_TYPED_ASSIGNMENT",
            new_assignment,
            new_block,
            tuple(sorted(new_stabilizer)),
        ),
        (
            "TYPEII_SAME_FIBER_FACTOR_BOX_TARGET_MISS",
            tuple(sorted(factor_box)),
            (-1) % modulus,
        ),
        (
            "ETA_MOD13_FOURTH_POWER_C3_ROLE",
            modulus,
            tuple(eta(value) for value in new_block),
        ),
    )
    candidate_universe_payload = {
        "schema": "QPREFIX_PREFIX_MONOTONE_NORMALIZATION_V1",
        "context": {
            "p": p,
            "x": target,
            "q": q,
            "base_layer": base_layer,
            "modulus": modulus,
        },
        "upstream_receipts": upstream_receipt_payloads,
        "candidates": (
            (old_assignment, 2),
            (new_assignment, 3),
        ),
    }
    candidate_universe_digest = hashlib.sha256(
        json.dumps(
            candidate_universe_payload,
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("ascii")
    ).hexdigest()
    old_normalization_context = (old_assignment, candidate_universe_digest)
    new_normalization_context = (new_assignment, candidate_universe_digest)
    assert old_normalization_context[1] == new_normalization_context[1]

    # Declare and validate the exact isolated active-ledger snapshot. This is
    # the scope of the concrete certificate; no larger ledger is inferred.
    outer_node = ("outer-state", p, 199)
    request_node = ("request", digest, target, q, base_layer)
    fiber_node = ("target-fiber", target, 1, target)
    factor_box_node = ("exact-factor-box", 3**4 * 83**2)
    eta_role_node = ("eta-role", modulus, "mod13-fourth-power", "C3")
    factor_target_miss_node = (
        "factor-target-miss",
        factor_box_node,
        factor_target_miss,
    )
    fiber_realized = False
    fiber_realization_gate_node = (
        "fiber-realization-gate",
        fiber_node,
        fiber_realized,
    )
    old_assignment_node = (
        "assignment",
        old_assignment,
        "normalization-context",
        candidate_universe_digest,
    )
    old_lineage_node = ("lineage", old_lineage)
    old_owner_node = ("owner-prefix", tuple(sorted(old_owner.values(), key=repr)))
    old_occurrence_node = (
        "occurrence-incidence",
        tuple(sorted(old_occurrence_owner.items(), key=repr)),
    )
    old_kernel_node = ("kernel-section", tuple(sorted(old_section)))
    old_depth_node = ("labelled-depth", (2, 0), "conditional-defect", (1, 2))
    old_price_node = ("price-status", old_charge, "UNPRICED")
    old_edges = {
        (outer_node, request_node),
        (outer_node, fiber_node),
        (fiber_node, factor_box_node),
        (fiber_node, eta_role_node),
        (factor_box_node, factor_target_miss_node),
        (fiber_node, fiber_realization_gate_node),
        (request_node, old_assignment_node),
        (old_assignment_node, old_lineage_node),
        (old_lineage_node, old_owner_node),
        (old_lineage_node, old_occurrence_node),
        (old_lineage_node, old_kernel_node),
        (fiber_node, old_kernel_node),
        (eta_role_node, old_kernel_node),
        (old_lineage_node, old_depth_node),
        (factor_box_node, old_depth_node),
        (eta_role_node, old_depth_node),
        (old_lineage_node, old_price_node),
        (factor_target_miss_node, old_price_node),
        (fiber_realization_gate_node, old_price_node),
    }
    old_active_nodes = {
        outer_node,
        request_node,
        fiber_node,
        factor_box_node,
        eta_role_node,
        factor_target_miss_node,
        fiber_realization_gate_node,
        old_assignment_node,
        old_lineage_node,
        old_owner_node,
        old_occurrence_node,
        old_kernel_node,
        old_depth_node,
        old_price_node,
    }
    assert {left for edge in old_edges for left in edge} <= old_active_nodes
    assert is_acyclic(old_active_nodes, old_edges)
    rollback_closure = descendants(old_assignment_node, old_edges)
    assert rollback_closure == {
        old_assignment_node,
        old_lineage_node,
        old_owner_node,
        old_occurrence_node,
        old_kernel_node,
        old_depth_node,
        old_price_node,
    }
    declared_snapshot = {
        "scope": "P557_ISOLATED_SINGLE_REQUEST_LEDGER_V1",
        "active_assignments": {old_assignment},
        "active_nodes": old_active_nodes,
        "dependency_edges": old_edges,
        "successor_nodes": set(),
        "e4_nodes": set(),
        "e5_nodes": set(),
        "spent_price_nodes": set(),
        "derived_resource_loads": {},
        "irreversible_carry_set": set(),
        "upstream_receipt_payloads": upstream_receipt_payloads,
    }
    assert declared_snapshot["active_assignments"] == {old_assignment}
    assert not declared_snapshot["successor_nodes"]
    assert not declared_snapshot["e4_nodes"]
    assert not declared_snapshot["e5_nodes"]
    assert not declared_snapshot["spent_price_nodes"]
    assert not declared_snapshot["derived_resource_loads"]
    assert not declared_snapshot["irreversible_carry_set"]

    new_assignment_node = (
        "assignment",
        new_assignment,
        "normalization-context",
        candidate_universe_digest,
    )
    new_lineage_node = ("lineage", new_lineage)
    new_owner_node = ("owner-prefix", tuple(sorted(new_owner.values(), key=repr)))
    new_occurrence_node = (
        "occurrence-incidence",
        tuple(sorted(new_occurrence_owner.items(), key=repr)),
    )
    new_kernel_node = ("kernel-section", tuple(sorted(new_section)))
    new_depth_node = ("labelled-depth", (3, 0), "conditional-defect", (0, 2))
    new_price_node = ("price-status", new_charge, "UNPRICED")
    recompute_closure = {
        new_assignment_node,
        new_lineage_node,
        new_owner_node,
        new_occurrence_node,
        new_kernel_node,
        new_depth_node,
        new_price_node,
    }
    new_edges = {
        (outer_node, request_node),
        (outer_node, fiber_node),
        (fiber_node, factor_box_node),
        (fiber_node, eta_role_node),
        (factor_box_node, factor_target_miss_node),
        (fiber_node, fiber_realization_gate_node),
        (request_node, new_assignment_node),
        (new_assignment_node, new_lineage_node),
        (new_lineage_node, new_owner_node),
        (new_lineage_node, new_occurrence_node),
        (new_lineage_node, new_kernel_node),
        (fiber_node, new_kernel_node),
        (eta_role_node, new_kernel_node),
        (new_lineage_node, new_depth_node),
        (factor_box_node, new_depth_node),
        (eta_role_node, new_depth_node),
        (new_lineage_node, new_price_node),
        (factor_target_miss_node, new_price_node),
        (fiber_realization_gate_node, new_price_node),
    }
    new_active_nodes = (
        old_active_nodes - rollback_closure
    ) | recompute_closure
    assert {left for edge in new_edges for left in edge} <= new_active_nodes
    assert is_acyclic(new_active_nodes, new_edges)
    assert descendants(new_assignment_node, new_edges) == recompute_closure
    assert not any(contains_nested(node, old_assignment) for node in new_active_nodes)
    assert not any(contains_nested(edge, old_assignment) for edge in new_edges)

    old_depth = len(old_atoms)
    new_depth = len(new_atoms)
    old_potential = maximum_depth - old_depth
    new_potential = maximum_depth - new_depth
    assert (old_depth, new_depth, maximum_depth) == (2, 3, 3)
    assert (old_potential, new_potential) == (1, 0)
    assert p + 4 * target == 3**4 * 83**2
    derived_validators = {
        "assignment_binding": new_normalization_context[1]
        == candidate_universe_digest,
        "lineage_depth": len(new_atoms) == 3,
        "owner_prefix": len(new_owner) == 3,
        "occurrence_incidence": not any(
            contains_nested(owner, old_assignment)
            for owner in new_occurrence_owner.values()
        ),
        "kernel_section": new_section == {701, 727},
        "labelled_depth": (new_depth, 0) == (3, 0),
        "price_status": factor_target_miss
        and not fiber_realized
        and not declared_snapshot["spent_price_nodes"],
    }
    assert all(derived_validators.values())

    return {
        "status": (
            "P557_ISOLATED_SINGLE_REQUEST_Q3_DEPTH2_TO_DEPTH3_"
            "ATOMIC_REPLACEMENT"
        ),
        "snapshot_scope": declared_snapshot["scope"],
        "shared_keys": tuple(sorted(old_keys & new_keys)),
        "old_only_count": len(old_keys - new_keys),
        "new_only_count": len(new_keys - old_keys),
        "symmetric_difference": len(old_keys ^ new_keys),
        "owner_prefix_injection": True,
        "occurrence_backpointer_transfer": True,
        "dependency_rollback_nodes": len(rollback_closure),
        "dependency_recompute_nodes": len(recompute_closure),
        "dependency_dag_acyclic": True,
        "derived_validators": derived_validators,
        "derived_resource_loads": declared_snapshot["derived_resource_loads"],
        "irreversible_carry_set": tuple(declared_snapshot["irreversible_carry_set"]),
        "old_stabilizer": tuple(sorted(old_stabilizer)),
        "new_stabilizer": tuple(sorted(new_stabilizer)),
        "price_transition": ("UNPRICED", "UNPRICED"),
        "kernel_section_transition": (
            tuple(sorted(old_section)),
            tuple(sorted(new_section)),
        ),
        "active_labelled_prefix_depth_transition": ((2, 0), (3, 0)),
        "conditional_ambient_defect_transition": ((1, 2), (0, 2)),
        "normalization_candidate_universe_digest": candidate_universe_digest,
        "prefix_normalization_potential": (old_potential, new_potential),
        "global_e5_registered": False,
    }


def verify() -> None:
    verify_generic_boundaries()
    receipt = verify_p557_transaction()
    print("PASS: FG_QPREFIX_ATOMIC_REPLACEMENT_CAPACITY_NORMALIZATION")
    print(receipt)


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
