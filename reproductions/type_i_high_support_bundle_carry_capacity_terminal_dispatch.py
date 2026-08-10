#!/usr/bin/env python3
"""Verify the high-support bundle carry gate and its p=73 dispatches."""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm, prod

import sympy

import type_i_bottom_sink_scc_complete_excess_bundle as bottom


def sharp_rank(prime: int, K: int, support: int) -> tuple[int, int]:
    if K % support:
        raise AssertionError("charged support did not divide K")
    bound = (prime - 1) ** 2 // 4
    return bound // support, K // support


def carry_receipt(prime: int, cofactor: int, multiplier: int) -> dict[str, int]:
    if not (1 <= cofactor < prime and multiplier >= 2 and gcd(prime, multiplier) == 1):
        raise AssertionError("invalid canonical carry input")
    carry = (-cofactor * pow(prime, -1, multiplier)) % multiplier
    numerator = cofactor + prime * carry
    target, remainder = divmod(numerator, multiplier)
    if not (
        remainder == 0
        and 1 <= target < prime
        and target == cofactor * pow(multiplier, -1, prime) % prime
    ):
        raise AssertionError("canonical carry formula failed")
    drift = multiplier * (target - cofactor)
    slack = prime * carry - cofactor * (multiplier - 1)
    if drift != slack:
        raise AssertionError("carry slack identity failed")
    relation = "decrease" if drift < 0 else "stutter" if drift == 0 else "increase"
    if (relation == "stutter") != (multiplier % prime == 1):
        raise AssertionError("canonical carry equality boundary failed")
    return {
        "C": cofactor,
        "L": multiplier,
        "h": carry,
        "c": target,
        "Delta": drift,
        "relation": relation,
    }


def verify_carry_theorem(prime: int, multipliers: tuple[int, ...]) -> dict[str, object]:
    symmetry_rows = []
    for multiplier in multipliers:
        targets = {
            cofactor: carry_receipt(prime, cofactor, multiplier)["c"]
            for cofactor in range(1, prime)
        }
        if set(targets.values()) != set(range(1, prime)):
            raise AssertionError("multiplier did not permute nonzero residues")
        for cofactor, target in targets.items():
            if targets[prime - cofactor] != prime - target:
                raise AssertionError("antipodal carry symmetry failed")
        decreases = sum(targets[C] < C for C in targets)
        stutters = sum(targets[C] == C for C in targets)
        increases = sum(targets[C] > C for C in targets)
        if multiplier % prime == 1:
            if (decreases, stutters, increases) != (0, prime - 1, 0):
                raise AssertionError("identity multiplier profile changed")
        elif (decreases, stutters, increases) != (
            (prime - 1) // 2,
            0,
            (prime - 1) // 2,
        ):
            raise AssertionError("half-descent carry symmetry failed")
        if sum(targets[C] - C for C in targets) != 0:
            raise AssertionError("total carry drift was not zero")
        symmetry_rows.append(
            {
                "L_mod_p": multiplier % prime,
                "decreases": decreases,
                "stutters": stutters,
                "increases": increases,
            }
        )

    # Three exact sufficient criteria, checked on their residue statements.
    C = prime - 3
    distinct_residues = (1, 2, 3, 4)
    distinct_targets = {
        C * pow(residue, -1, prime) % prime for residue in distinct_residues
    }
    if len(distinct_residues) <= prime - C or min(distinct_targets) >= C:
        raise AssertionError("distinct-residue pigeonhole criterion failed")

    C = (prime + 1) // 2 + 8
    residue = 6
    antipodal_targets = (
        C * pow(residue, -1, prime) % prime,
        C * pow(prime - residue, -1, prime) % prime,
    )
    if C <= (prime - 1) // 2 or min(antipodal_targets) >= C:
        raise AssertionError("antipodal sufficient criterion failed")

    C, divisor = 44, 4
    divisor_row = carry_receipt(prime, C, divisor)
    if C % divisor or divisor_row["h"] != 0 or divisor_row["c"] != C // divisor:
        raise AssertionError("divisibility carry criterion failed")

    return {
        "symmetry_profiles": symmetry_rows,
        "sufficient_criteria": {
            "distinct_residue_pigeonhole": {
                "C": prime - 3,
                "residue_count": len(distinct_residues),
                "minimum_target": min(distinct_targets),
            },
            "antipodal_pair": {
                "C": (prime + 1) // 2 + 8,
                "targets": list(antipodal_targets),
            },
            "divisibility_carry": divisor_row,
        },
    }


def replay_path(
    source: bottom.FormalNode,
    labels: tuple[int, ...],
    expected_nodes: tuple[bottom.FormalNode, ...],
    R: int,
    K_factors: dict[int, int],
) -> list[dict[str, object]]:
    if len(labels) != len(expected_nodes):
        raise AssertionError("raw path fixture length changed")
    current = source
    rows = []
    for q, expected in zip(labels, expected_nodes, strict=True):
        destination, shift, common = bottom.formal_transition(current, q, R, K_factors)
        if destination != expected:
            raise AssertionError("raw path destination changed")
        rows.append(
            {
                "source": list(current),
                "q": q,
                "shift": shift,
                "gcd_reduction": common,
                "destination": list(destination),
            }
        )
        current = destination
    return rows


def centered_box(R: int, K: int) -> tuple[dict[int, int], set[int]]:
    factors = bottom.factorization(K)
    residues = {1}
    for q, exponent in factors.items():
        residues = {
            left * pow(q, z, R) % R
            for left in residues
            for z in range(-exponent, exponent + 1)
        }
    return factors, residues


def empty_improvement_profile() -> dict[str, object]:
    prime = 73
    parent_R, parent_K, parent_support = 1351, 24656, 1
    if not (
        4 * parent_K == prime * parent_R + 1
        and bottom.factorization(parent_R) == {7: 1, 193: 1}
        and bottom.factorization(parent_K) == {2: 4, 23: 1, 67: 1}
    ):
        raise AssertionError("G parent arithmetic changed")
    parent_factors = bottom.factorization(parent_K)
    character = {q: bottom.jacobi_symbol(q, parent_R) for q in parent_factors}
    if set(character.values()) != {1} or bottom.jacobi_symbol(-1, parent_R) != -1:
        raise AssertionError("Jacobi G separator changed")

    universal_source = (
        prime,
        parent_R * (prime - 1) - prime,
        prime - 1,
    )
    source_path = replay_path(
        universal_source,
        (73, 3, 53, 29),
        (
            (1, 1350, 1),
            (450, 901, 1),
            (17, 1334, 1),
            (46, 1305, 1),
        ),
        parent_R,
        parent_factors,
    )
    Q, beta, residual = 1305, 1, 46
    if not (
        beta == 1
        and bottom.factorization(Q) == {3: 2, 5: 1, 29: 1}
        and parent_K % residual == 0
        and gcd(Q, residual) == 1
        and parent_K % Q != 0
    ):
        raise AssertionError("G-to-F complete-excess bundle changed")
    support = lcm(parent_support, Q)
    R, K = bottom.canonical_chart(prime, support)
    if (R, K, support, K // support) != (143, 2610, 1305, 2):
        raise AssertionError("C=2 target chart changed")
    if not sharp_rank(prime, K, support) < sharp_rank(prime, parent_K, parent_support):
        raise AssertionError("G-to-F macro lost E5")

    factors, bounded = centered_box(R, K)
    witness = (-3, 0, -3, 0)
    value = prod(pow(q, z, R) for q, z in zip(factors, witness, strict=True)) % R
    if not (
        factors == {2: 1, 3: 2, 5: 1, 29: 1}
        and len(bounded) == 86
        and R - 1 not in bounded
        and value == R - 1
    ):
        raise AssertionError("C=2 F classification changed")
    F_source_path = replay_path(
        (1, 1000, 7),
        (2, 5, 59),
        ((18, 125, 1), (25, 118, 1), (2, 141, 1)),
        R,
        factors,
    )

    adjacency, _labels = bottom.bottom_graph(R, factors)
    sinks = bottom.sink_components(adjacency)
    if len(sinks) != 1 or len(sinks[0]) != 24 or (2, 141) not in sinks[0]:
        raise AssertionError("C=2 bottom sink changed")
    component = sinks[0]
    rows = []
    for node in sorted(component):
        for selected, other in ((node[1], node[0]), (node[0], node[1])):
            bundle = 1
            supported = 1
            for q, exponent in bottom.factorization(selected).items():
                if exponent > factors.get(q, 0):
                    bundle *= q**exponent
                else:
                    supported *= q**exponent
            residual = other * supported
            if (
                bundle <= 1
                or selected != bundle * supported
                or gcd(bundle, residual) != 1
                or K % residual
                or K % bundle == 0
            ):
                continue
            target_support = lcm(support, bundle)
            if target_support <= support or target_support % prime == 0:
                continue
            target_R, target_K = bottom.canonical_chart(prime, target_support)
            multiplier = target_support // support
            carry = carry_receipt(prime, 2, multiplier)
            if target_K // target_support != carry["c"]:
                raise AssertionError("bundle target disagreed with carry formula")
            rows.append(
                (
                    node,
                    bundle,
                    supported,
                    residual,
                    multiplier,
                    target_K // target_support,
                    carry["h"],
                    carry["Delta"],
                )
            )

    expected = [
        ((1, 142), 71, 2, 2, 71, 72, 70, 4970),
        ((2, 141), 47, 3, 6, 47, 28, 18, 1222),
        ((3, 140), 28, 5, 15, 28, 47, 18, 1260),
        ((5, 138), 23, 6, 30, 23, 35, 11, 759),
        ((6, 137), 137, 1, 6, 137, 16, 30, 1918),
        ((9, 134), 67, 2, 18, 67, 24, 22, 1474),
        ((10, 133), 133, 1, 10, 133, 56, 102, 7182),
        ((15, 128), 128, 1, 15, 128, 8, 14, 768),
        ((45, 98), 49, 2, 90, 49, 6, 4, 196),
        ((58, 85), 17, 5, 290, 17, 13, 3, 187),
    ]
    if rows != expected or any(row[5] < 2 for row in rows):
        raise AssertionError("C=2 complete capacity no-go changed")
    product_mod_p = prod(row[4] for row in rows) % prime
    if product_mod_p != 25:
        raise AssertionError("candidate multiplier product changed")

    terminal = (20, 219, 4380)
    x, y, z = terminal
    if 4 * x * y * z != prime * (x * y + x * z + y * z):
        raise AssertionError("p=73 Type II terminal changed")

    return {
        "parent": {
            "state": [parent_R, parent_K, parent_support],
            "classification": "G_by_Jacobi_separator",
            "character": character,
            "rank": list(sharp_rank(prime, parent_K, parent_support)),
            "source_path": source_path,
        },
        "contract_admissible_target": {
            "state": [R, K, support],
            "classification": "F",
            "bounded_residue_count": len(bounded),
            "unbounded_witness": list(witness),
            "rank": list(sharp_rank(prime, K, support)),
            "source_path": F_source_path,
        },
        "sink_capacity": {
            "node_count": len(component),
            "edge_count": sum(len(adjacency[node]) for node in component),
            "candidate_count": len(rows),
            "improving_count": sum(row[5] < 2 for row in rows),
            "rows": [
                {
                    "node": list(node),
                    "Q": bundle,
                    "beta": beta,
                    "residual": residual,
                    "L": multiplier,
                    "c": target,
                    "h": carry,
                    "Delta": drift,
                }
                for node, bundle, beta, residual, multiplier, target, carry, drift in rows
            ],
            "product_L_mod_p": product_mod_p,
        },
        "dispatch": {
            "bundle_branch": "CARRY_NO_GO",
            "terminal_first_Type_II": list(terminal),
            "selected_branch": "TERMINAL_PREEMPTION",
        },
    }


def positive_carry_edge() -> dict[str, object]:
    prime = 73
    R, K, support = 4563815, 83289624, 1892946
    factors, bounded = centered_box(R, K)
    witness = (-1, 6, 4, -7, -1, -8)
    witness_value = (
        prod(pow(q, z, R) for q, z in zip(factors, witness, strict=True)) % R
    )
    if not (
        4 * K == prime * R + 1
        and K // support == 44
        and factors == {2: 3, 3: 1, 11: 2, 23: 1, 29: 1, 43: 1}
        and len(bounded) == 2739
        and R - 1 not in bounded
        and witness_value == R - 1
    ):
        raise AssertionError("established C=44 F parent changed")

    universal_source = (prime, R * (prime - 1) - prime, prime - 1)
    raw_path = replay_path(
        universal_source,
        (73, 73, 31259, 1933, 6353, 7, 488993),
        (
            (1, 4563814, 1),
            (62518, 4501297, 1),
            (2, 4563813, 1),
            (2361, 4561454, 1),
            (718, 4563097, 1),
            (651871, 3911944, 1),
            (8, 4563807, 1),
        ),
        R,
        factors,
    )
    node = (8, 4563807)
    selected_factors = bottom.factorization(node[1])
    Q, beta, residual = 1521269, 3, 24
    if not (
        selected_factors == {3: 1, Q: 1}
        and node[1] == Q * beta
        and K % residual == 0
        and gcd(Q, residual) == 1
        and K % Q != 0
    ):
        raise AssertionError("C=44 positive bundle changed")

    target_support = lcm(support, Q)
    target_R, target_K = bottom.canonical_chart(prime, target_support)
    multiplier = target_support // support
    carry = carry_receipt(prime, 44, multiplier)
    if not (
        (target_R, target_K, target_support)
        == (315581377367, 5759360136948, 2879680068474)
        and carry
        == {
            "C": 44,
            "L": 1521269,
            "h": 41678,
            "c": 2,
            "Delta": -63893298,
            "relation": "decrease",
        }
        and target_K // target_support == 2
        and sharp_rank(prime, target_K, target_support) < sharp_rank(prime, K, support)
    ):
        raise AssertionError("C=44 to C=2 carry descent changed")

    target_factors, target_bounded = centered_box(target_R, target_K)
    euler_exponent = (target_R - 1) // 2
    if not (
        sympy.isprime(target_R)
        and target_factors == {2: 2, 3: 1, 11: 1, 23: 1, 29: 1, 43: 1, Q: 1}
        and len(target_bounded) == 3581
        and target_R - 1 not in target_bounded
        and sympy.legendre_symbol(11, target_R) == -1
        and pow(11, euler_exponent, target_R) == target_R - 1
        and euler_exponent > target_factors[11]
    ):
        raise AssertionError("new C=2 target F classification changed")

    return {
        "source": {
            "state": [R, K, support],
            "classification": "F",
            "rank": list(sharp_rank(prime, K, support)),
        },
        "path_anchored_bundle": {
            "raw_path": raw_path,
            "node": list(node),
            "Q": Q,
            "beta": beta,
            "residual": residual,
        },
        "carry": carry,
        "target": {
            "state": [target_R, target_K, target_support],
            "rank": list(sharp_rank(prime, target_K, target_support)),
            "classification": "F_by_bounded_miss_and_Euler_witness",
            "bounded_term_count": prod(
                2 * exponent + 1 for exponent in target_factors.values()
            ),
            "bounded_residue_count": len(target_bounded),
            "Euler_witness": {"prime": 11, "exponent": euler_exponent},
        },
        "solution_lift": "identity_on_Sol(4,p)",
    }


def run() -> dict[str, object]:
    empty = empty_improvement_profile()
    positive = positive_carry_edge()
    multipliers = tuple(row["L"] for row in empty["sink_capacity"]["rows"]) + (
        1247,
        1521269,
        74,
    )
    theorem = verify_carry_theorem(73, multipliers)
    return {
        "carry_theorem": theorem,
        "strict_empty_improvement_counterexample": empty,
        "new_positive_edge": positive,
        "theorem_status": "verified",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.verify:
        print("verified high-support bundle carry gate and terminal dispatch")
    else:
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
