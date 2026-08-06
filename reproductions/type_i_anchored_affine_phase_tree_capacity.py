#!/usr/bin/env python3
"""Verify the anchored affine phase-graph and capacity counterexample.

The C6 model checks two separate facts: the full anchor graph has no vertical
element, while a marked-SNF saturated one-row menu does not preserve the full
phase-cell count needed for capacity.
"""

from __future__ import annotations

import argparse
from collections import deque


def generated_subgroup(
    generators: set[tuple[int, int]], moduli: tuple[int, int]
) -> set[tuple[int, int]]:
    """Return the subgroup generated in C_moduli[0] x C_moduli[1]."""
    subgroup = {(0, 0)}
    queue = deque([(0, 0)])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = (
                (current[0] + generator[0]) % moduli[0],
                (current[1] + generator[1]) % moduli[1],
            )
            if candidate not in subgroup:
                subgroup.add(candidate)
                queue.append(candidate)
    return subgroup


def capacity_bound(
    *, width: int, q: int, phase_counts: dict[int, int], multiplicity: int
) -> int:
    """Evaluate the layered bound for already supplied phase-cell counts."""
    return sum(
        multiplicity * count * (width // (q**level) + 1)
        for level, count in phase_counts.items()
    )


def verify_c6_anchor_counterexample() -> dict[str, object]:
    """Replay the C6 example where saturation cannot replace full D."""
    group_order = 6
    q = 3
    target = 3
    anchor = 0
    anchors = (0, 4, 5)

    stabilizer = {
        shift
        for shift in range(group_order)
        if {(entry + shift) % group_order for entry in anchors} == set(anchors)
    }
    if stabilizer != {0} or target in anchors:
        raise AssertionError("C6 example no longer has the intended F-shape")

    # psi(g)=zeta_3, so gamma_j=-j mod 3 and x_j=t-j in additive notation.
    graph = {
        ((anchor - entry) % group_order, (-entry) % q) for entry in anchors
    }
    expected_graph = {(0, 0), (1, 1), (2, 2)}
    if graph != expected_graph:
        raise AssertionError("anchored C6 phase graph changed")

    full_subgroup = generated_subgroup(graph, (group_order, q))
    menu = {(1, 1)}
    menu_subgroup = generated_subgroup(menu, (group_order, q))
    expected_subgroup = {(value, value % q) for value in range(group_order)}
    if full_subgroup != expected_subgroup or menu_subgroup != expected_subgroup:
        raise AssertionError("marked saturation control changed")
    if any(group_value == 0 and label != 0 for group_value, label in full_subgroup):
        raise AssertionError("anchored graph acquired a nonzero vertical element")

    gamma_by_anchor = {entry: (-entry) % q for entry in anchors}
    rows = ((0, 0, 1), (5, 1, 1), (4, 2, 1))
    width = 2
    multiplicity = 1
    for entry, label, height in rows:
        if height != 1 or label % q != gamma_by_anchor[entry]:
            raise AssertionError("physical affine label control changed")
    if len({label for _, label, _ in rows}) != 3:
        raise AssertionError("physical label multiplicity control changed")

    full_phase_count = len(set(gamma_by_anchor.values()))
    menu_phase_count = len({label for _, label in menu})
    total_height = sum(height for _, _, height in rows)
    full_bound = capacity_bound(
        width=width,
        q=q,
        phase_counts={1: full_phase_count},
        multiplicity=multiplicity,
    )
    compressed_bound = capacity_bound(
        width=width,
        q=q,
        phase_counts={1: menu_phase_count},
        multiplicity=multiplicity,
    )
    if not (
        full_phase_count == 3
        and menu_phase_count == 1
        and total_height == full_bound == 3
        and total_height > compressed_bound == 1
    ):
        raise AssertionError("phase-cell compression counterexample changed")

    return {
        "group": "C6",
        "target": target,
        "anchor_set": list(anchors),
        "anchor_graph": [list(value) for value in sorted(graph)],
        "vertical_elements": [
            list(value)
            for value in sorted(full_subgroup)
            if value[0] == 0
        ],
        "full_phase_count": full_phase_count,
        "saturated_menu_phase_count": menu_phase_count,
        "total_height": total_height,
        "full_capacity_bound": full_bound,
        "invalid_compressed_bound": compressed_bound,
    }


def build_result() -> dict[str, object]:
    """Build only the finite graph and capacity controls."""
    return {
        "certificate_type": "anchored_affine_phase_tree_capacity_control_v1",
        "scope": (
            "Finite anchor graph and conditional capacity control only; no "
            "physical E2, E4, E5, or recursive edge is asserted."
        ),
        "c6_counterexample": verify_c6_anchor_counterexample(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified anchored affine phase-tree capacity controls")


if __name__ == "__main__":
    main()
