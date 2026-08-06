#!/usr/bin/env python3
"""Verify the raw-factor affine preflight and its p=5281 obstruction.

An affine source label is useful for a raw transition table only when its
phase differences are a single factor action.  This focused verifier checks
that graph-theoretic gate on the p=5281 Jacobi-odd diamond.  It proves that
the physical tail alone has nonzero curvature, while the derived factor-phase
value M * t^(-1) * K^(-1) is integrable.  It does not assert a
physical E2 lift, an F-state anchor, or a selector edge.
"""

from __future__ import annotations

import argparse
from collections import defaultdict, deque

import type_i_g_anchor_jacobi_p5281_physical_ledger as jacobi_ledger


def discrete_log_table(generator: int, modulus: int) -> dict[int, int]:
    """Return the exponent table for a verified primitive root."""
    values: dict[int, int] = {}
    current = 1
    for exponent in range(modulus - 1):
        if current in values:
            raise AssertionError("candidate generator repeated too early")
        values[current] = exponent
        current = current * generator % modulus
    if current != 1 or len(values) != modulus - 1:
        raise AssertionError("candidate is not a primitive root")
    return values


def integrate_factor_action(
    *,
    vertices: set[int],
    edges: list[tuple[int, int, int]],
    action: dict[int, int],
    modulus: int,
    root: int,
    root_value: int,
) -> dict[int, int]:
    """Integrate an additive factor action along an undirected raw graph.

    A conflict is precisely a nonzero image of a signed closed-walk word.
    Thus this finite routine is the constructive half of the cycle-lattice
    integration criterion used by the accompanying claim card.
    """
    if root not in vertices or set(action) != {factor for _, factor, _ in edges}:
        raise AssertionError("factor action inputs are incomplete")
    adjacency: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for source, factor, destination in edges:
        if source not in vertices or destination not in vertices:
            raise AssertionError("raw edge leaves the declared vertex set")
        increment = action[factor] % modulus
        adjacency[source].append((destination, increment))
        adjacency[destination].append((source, -increment))

    potential = {root: root_value % modulus}
    queue: deque[int] = deque([root])
    while queue:
        source = queue.popleft()
        for destination, increment in adjacency[source]:
            candidate = (potential[source] + increment) % modulus
            previous = potential.get(destination)
            if previous is None:
                potential[destination] = candidate
                queue.append(destination)
            elif previous != candidate:
                raise AssertionError("the factor action has nonzero cycle curvature")
    if set(potential) != vertices:
        raise AssertionError("declared raw graph is disconnected")
    return potential


def factor_differences(
    *,
    values: dict[int, int],
    edges: list[tuple[int, int, int]],
    modulus: int,
) -> dict[int, tuple[int, ...]]:
    """Collect every directed phase increment for each raw factor."""
    differences: dict[int, list[int]] = defaultdict(list)
    for source, factor, destination in edges:
        differences[factor].append((values[destination] - values[source]) % modulus)
    return {factor: tuple(entries) for factor, entries in sorted(differences.items())}


def verify_p5281_raw_factor_action() -> dict[str, object]:
    """Check the tail-only obstruction and the factor-phase correction."""
    parameters = jacobi_ledger.ledger_parameters()
    R = parameters["R"]
    K = parameters["K"]
    Q = parameters["Q"]
    menu = (7, 91, 203, 2639)
    if not jacobi_ledger.is_prime(R) or jacobi_ledger.factorization(R - 1) != {
        2: 1,
        7: 1,
        13: 1,
        29: 1,
    }:
        raise AssertionError("p=5281 primary control changed")

    rows = {
        delta: jacobi_ledger.row_from_delta(delta=delta, parameters=parameters)
        for delta in menu
    }
    raw_edges = jacobi_ledger.inter_menu_raw_edges(parameters=parameters, menu=menu)
    edges = [
        (int(edge["raw_from_delta"]), int(edge["q"]), int(edge["raw_to_delta"]))
        for edge in raw_edges
    ]
    expected_edges = [(7, 13, 91), (7, 29, 203), (91, 29, 2639), (203, 13, 2639)]
    if edges != expected_edges:
        raise AssertionError("p=5281 raw diamond changed")

    logs = discrete_log_table(7, R)
    if logs[7] != 1:
        raise AssertionError("p=5281 primitive-root normalization changed")
    tails = {delta: int(row["t"]) for delta, row in rows.items()}
    carriers = {delta: int(row["M"]) for delta, row in rows.items()}
    tail_cross_ratio = (
        tails[2639]
        * tails[7]
        * pow(tails[91] * tails[203] % R, -1, R)
    ) % R
    carrier_cross_ratio = (
        carriers[2639]
        * carriers[7]
        * pow(carriers[91] * carriers[203] % R, -1, R)
    ) % R
    if tail_cross_ratio != 1267 or carrier_cross_ratio != tail_cross_ratio:
        raise AssertionError("p=5281 diamond cross-ratio changed")
    if logs[tail_cross_ratio] != 492:
        raise AssertionError("p=5281 diamond discrete log changed")

    factor_phase_mark = {
        delta: carriers[delta] * pow(tails[delta], -1, R) * pow(K, -1, R) % R
        for delta in menu
    }
    if factor_phase_mark != {delta: delta for delta in menu}:
        raise AssertionError("the factor-phase mark no longer recovers delta")

    primary_controls: dict[str, object] = {}
    for ell in (7, 13, 29):
        tail_phase = {delta: logs[tails[delta]] % ell for delta in menu}
        full_phase = {delta: logs[factor_phase_mark[delta]] % ell for delta in menu}
        action = {factor: logs[factor] % ell for factor in (13, 29)}
        tail_increments = factor_differences(
            values=tail_phase, edges=edges, modulus=ell
        )
        full_increments = factor_differences(
            values=full_phase, edges=edges, modulus=ell
        )
        tail_curvature = (
            tail_phase[2639] - tail_phase[91] - tail_phase[203] + tail_phase[7]
        ) % ell
        expected_curvature = 492 % ell
        if tail_curvature != expected_curvature or tail_curvature == 0:
            raise AssertionError("tail-only diamond curvature changed")
        if any(len(set(increments)) == 1 for increments in tail_increments.values()):
            raise AssertionError("tail-only marking unexpectedly became factor-local")
        if full_increments != {factor: (action[factor], action[factor]) for factor in (13, 29)}:
            raise AssertionError("factor-phase mark lost its factor action")
        integrated = integrate_factor_action(
            vertices=set(menu),
            edges=edges,
            action=action,
            modulus=ell,
            root=7,
            root_value=full_phase[7],
        )
        if integrated != full_phase:
            raise AssertionError("factor-phase mark did not integrate on the raw graph")

        # With anchor t=1 and j_delta=delta^(-1), gamma(j_delta)=log_7(delta).
        anchors = {delta: pow(delta, -1, R) for delta in menu}
        if any((-logs[anchors[delta]]) % ell != full_phase[delta] for delta in menu):
            raise AssertionError("abstract anchor graph no longer realizes the full phase")
        if any((unit * tail_curvature) % ell == 0 for unit in range(1, ell)):
            raise AssertionError("an affine unit unexpectedly erased tail curvature")
        primary_controls[str(ell)] = {
            "tail_curvature": tail_curvature,
            "tail_factor_increments": {
                str(factor): list(increments)
                for factor, increments in tail_increments.items()
            },
            "full_factor_action": {str(factor): action[factor] for factor in sorted(action)},
            "full_phase": {str(delta): full_phase[delta] for delta in menu},
            "abstract_anchor_rows": {
                str(delta): {"j": anchors[delta], "gamma": full_phase[delta]}
                for delta in menu
            },
        }

    if Q != 7 * 13 * 29:
        raise AssertionError("p=5281 source factorization changed")
    return {
        "parameters": parameters,
        "raw_diamond": {"vertices": list(menu), "edges": [list(edge) for edge in edges]},
        "tail_cross_ratio": tail_cross_ratio,
        "tail_cross_ratio_log_base_7": logs[tail_cross_ratio],
        "factor_phase_mark": {str(delta): factor_phase_mark[delta] for delta in menu},
        "q_primary_controls": primary_controls,
        "raw_factor_action_compatibility": "FULL_MARKED_PHASE_FACTOR_ACTION_VERIFIED",
        "tail_only_status": "TAIL_ONLY_AFFINE_FACTOR_ACTION_OBSTRUCTED",
        "aal_status": "ANCHORED_PHASE_MAP_UNCLOSED",
    }


def build_result() -> dict[str, object]:
    """Build only the raw-factor integration certificate."""
    return {
        "certificate_type": "raw_factor_action_affine_preflight_v1",
        "scope": (
            "Graph-level raw-factor compatibility only. The p=5281 control is a "
            "terminal-preempted G/Jacobi ledger and has no physical F anchor, E2 "
            "carry lift, E4 solution lift, E5 descent, or selector edge."
        ),
        "p5281": verify_p5281_raw_factor_action(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified raw-factor affine preflight controls")


if __name__ == "__main__":
    main()
