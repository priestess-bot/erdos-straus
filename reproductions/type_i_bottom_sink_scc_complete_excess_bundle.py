#!/usr/bin/env python3
"""Verify focused complete-excess bundle receipts in bottom sink SCCs."""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import gcd, isqrt, lcm
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-bottom-sink-scc-complete-excess-bundle-results.json"
)

CASES = (
    {
        "name": "F_reach_composite_bundle_without_single_prime_power_clean_slab",
        "prime": 21_169,
        "R": 19,
        "absorbed_support": 1,
        "expected_minimum_node": (1, 18),
        "expected_sink_size": 9,
        "expected_Q": 18,
        "expected_beta": 1,
        "expected_R_M": 71,
        "expected_classification": "verified_marked_bundle_edge",
        "require_no_single_prime_power_clean_slab": True,
        "F_source": {
            "numerator": 521**3,
            "denominator": 1,
            "path": (
                ((1, 141_420_761, 7_443_198), 521, 329, (12, 271_441, 14_287)),
                ((12, 271_441, 14_287), 521, 301, (11, 521, 28)),
                ((11, 521, 28), 11, 5, (1, 56, 3)),
                ((1, 56, 3), 7, 4, (8, 11, 1)),
            ),
        },
    },
    {
        "name": "overlapping_supported_prime_bundle_marked_edge",
        "prime": 409,
        "R": 51,
        "absorbed_support": 5,
        "expected_minimum_node": (1, 50),
        "expected_sink_size": 16,
        "expected_Q": 50,
        "expected_beta": 1,
        "expected_R_M": 111,
        "expected_classification": "verified_marked_bundle_edge",
        "require_no_single_prime_power_clean_slab": False,
    },
    {
        "name": "overlapping_supported_prime_bundle_overflow",
        "prime": 409,
        "R": 251,
        "absorbed_support": 5,
        "expected_minimum_node": (1, 250),
        "expected_sink_size": 125,
        "expected_Q": 250,
        "expected_beta": 1,
        "expected_R_M": 511,
        "expected_classification": "complete_excess_bundle_overflow",
        "require_no_single_prime_power_clean_slab": False,
    },
    {
        "name": "binary_self_loop_bundle_marked_edge",
        "prime": 1_009,
        "R": 3,
        "absorbed_support": 1,
        "expected_minimum_node": (1, 2),
        "expected_sink_size": 1,
        "expected_Q": 2,
        "expected_beta": 1,
        "expected_R_M": 7,
        "expected_classification": "verified_marked_bundle_edge",
        "require_no_single_prime_power_clean_slab": False,
    },
)

LINEAR_F_OVERFLOW_CASE = {
    "prime": 241,
    "R": 79,
    "a": 3,
    "s": 1,
    "alpha": 1,
    "Q": 71,
    "beta": 8,
    "expected_R_Q": 251,
    "F_exponents": (-3, 1, -1, 2),
    "anchor": {
        "node": (1, 78),
        "Q": 39,
        "beta": 2,
        "expected_R_Q": 11,
    },
    "source": {
        "numerator": 1_445,
        "denominator": 56,
        "path": (
            ((56, 1_445, 19), 17, 15, (73, 85, 2)),
            ((73, 85, 2), 73, 71, (1, 78, 1)),
            ((1, 78, 1), 3, 2, (26, 53, 1)),
            ((26, 53, 1), 13, 12, (2, 77, 1)),
            ((2, 77, 1), 11, 10, (7, 72, 1)),
            ((7, 72, 1), 3, 2, (24, 55, 1)),
            ((24, 55, 1), 3, 2, (8, 71, 1)),
        ),
    },
    "alternate": {
        "Q": 37,
        "alpha": 2,
        "beta": 5,
        "expected_R_Q": 35,
        "path": (
            ((8, 71, 1), 71, 70, (1, 78, 1)),
            ((1, 78, 1), 3, 2, (26, 53, 1)),
            ((26, 53, 1), 13, 12, (2, 77, 1)),
            ((2, 77, 1), 11, 10, (7, 72, 1)),
            ((7, 72, 1), 3, 2, (24, 55, 1)),
            ((24, 55, 1), 11, 10, (5, 74, 1)),
        ),
    },
}

AS_ONE_G_CASE = {"prime": 73, "R": 71, "a": 1, "s": 1}

Node = tuple[int, int]
FormalNode = tuple[int, int, int]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        factors[divisor] = exponent
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def canonical_node(selected: int, R: int) -> Node:
    other = R - selected
    if min(selected, other) <= 0 or gcd(selected, other) != 1:
        raise AssertionError("invalid primitive bottom node")
    return min(selected, other), max(selected, other)


def canonical_formal_node(left: int, right: int, m: int, R: int) -> FormalNode:
    if min(left, right, m) <= 0 or gcd(left, right) != 1 or left + right != R * m:
        raise AssertionError("invalid primitive formal node")
    return min(left, right), max(left, right), m


def formal_transition(
    source: FormalNode,
    q: int,
    R: int,
    K_factors: dict[int, int],
) -> tuple[FormalNode, int, int]:
    smaller, larger, m = source
    selected_sides = [value for value in (smaller, larger) if value % q == 0]
    if len(selected_sides) != 1:
        raise AssertionError("formal edge label did not select one primitive side")
    selected = selected_sides[0]
    other = larger if selected == smaller else smaller
    if factorization(selected).get(q, 0) <= K_factors.get(q, 0):
        raise AssertionError("formal edge label did not exceed K capacity")
    shift = (-m) % q
    if not 1 <= shift < q or gcd(q, R * m * other) != 1:
        raise AssertionError("formal shift was not a unit")
    selected_0 = selected // q
    other_0 = (other + R * shift) // q
    m_0 = (m + shift) // q
    common = gcd(selected_0, other_0)
    if m_0 % common:
        raise AssertionError("formal gcd reduction did not divide the layer")
    destination = canonical_formal_node(
        selected_0 // common,
        other_0 // common,
        m_0 // common,
        R,
    )
    return destination, shift, common


def verify_F_source(
    source: dict[str, object], R: int, K_factors: dict[int, int]
) -> dict[str, object]:
    numerator = int(source["numerator"])
    denominator = int(source["denominator"])
    if gcd(numerator, denominator) != 1 or (numerator + denominator) % R:
        raise AssertionError("F source did not represent the target residue")

    support = sorted(K_factors)
    bounded_residues: set[int] = set()
    for exponents in product(
        *(range(-K_factors[q], K_factors[q] + 1) for q in support)
    ):
        residue = 1
        for q, exponent in zip(support, exponents, strict=True):
            residue = residue * pow(q, exponent, R) % R
        bounded_residues.add(residue)
    target = R - 1
    if target in bounded_residues or numerator * pow(denominator, -1, R) % R != target:
        raise AssertionError("focused source was not an F witness")

    m = (numerator + denominator) // R
    initial = canonical_formal_node(numerator, denominator, m, R)
    current = initial
    path_rows = []
    for raw_source, q, expected_shift, expected_destination in source["path"]:
        raw_source = tuple(raw_source)
        expected_destination = tuple(expected_destination)
        if current != raw_source:
            raise AssertionError("focused F path lost continuity")
        destination, shift, common = formal_transition(
            current, int(q), R, K_factors
        )
        if destination != expected_destination or shift != int(expected_shift) or common != 1:
            raise AssertionError("focused F path changed")
        path_rows.append(
            {
                "source": list(current),
                "q": int(q),
                "shift": shift,
                "gcd_reduction": common,
                "destination": list(destination),
            }
        )
        current = destination
    if current[2] != 1:
        raise AssertionError("focused F path did not reach the bottom layer")
    return {
        "classification": "F",
        "target_residue": target,
        "bounded_residue_count": len(bounded_residues),
        "source": list(initial),
        "path": path_rows,
        "bottom_entry": list(current[:2]),
    }


def jacobi_symbol(numerator: int, denominator: int) -> int:
    if denominator <= 0 or denominator % 2 == 0:
        raise ValueError("Jacobi denominator must be positive and odd")
    numerator %= denominator
    result = 1
    while numerator:
        while numerator % 2 == 0:
            numerator //= 2
            if denominator % 8 in (3, 5):
                result = -result
        numerator, denominator = denominator, numerator
        if numerator % 4 == denominator % 4 == 3:
            result = -result
        numerator %= denominator
    return result if denominator == 1 else 0


def linear_F_overflow_profile() -> dict[str, object]:
    case = LINEAR_F_OVERFLOW_CASE
    prime = int(case["prime"])
    R = int(case["R"])
    a = int(case["a"])
    s = int(case["s"])
    alpha = int(case["alpha"])
    Q = int(case["Q"])
    beta = int(case["beta"])
    K = (prime * R + 1) // 4
    K_factors = factorization(K)
    if not (
        prime == a + s + a * s * R
        and R == alpha * Q + beta
        and K % (alpha * beta) == 0
        and gcd(alpha * Q, beta) == 1
        and K % Q != 0
    ):
        raise AssertionError("focused linear-source slab changed")
    R_Q, K_Q = canonical_chart(prime, Q)
    if R_Q != int(case["expected_R_Q"]) or R_Q <= prime:
        raise AssertionError("focused linear-source overflow changed")
    if not a * s < 4 / alpha:
        raise AssertionError("linear-source overflow size inequality failed")

    support = sorted(K_factors)
    exponents = tuple(int(value) for value in case["F_exponents"])
    if len(support) != len(exponents):
        raise AssertionError("focused F exponent dimension changed")
    residue = 1
    overflow_height = 0
    for q, exponent in zip(support, exponents, strict=True):
        residue = residue * pow(q, exponent, R) % R
        overflow_height += max(abs(exponent) - K_factors[q], 0)
    if residue != R - 1 or overflow_height != 1:
        raise AssertionError("focused Psi-one witness changed")
    source_receipt = verify_F_source(case["source"], R, K_factors)
    if source_receipt["bottom_entry"] != [8, 71]:
        raise AssertionError("focused overflow slab lost its source path")

    anchor = case["anchor"]
    anchor_node = tuple(anchor["node"])
    anchor_destination, anchor_shift, anchor_common = formal_transition(
        (8, 71, 1), Q, R, K_factors
    )
    if (
        anchor_destination[:2] != anchor_node
        or anchor_shift != Q - 1
        or anchor_common != 1
    ):
        raise AssertionError("clean alpha-one peeling did not reach its anchor")
    anchor_bundle = complete_excess_bundle(anchor_node, K, K_factors)
    anchor_Q = int(anchor["Q"])
    anchor_beta = int(anchor["beta"])
    anchor_R_Q, anchor_K_Q = canonical_chart(prime, anchor_Q)
    if not (
        int(anchor_bundle["Q"]) == anchor_Q
        and int(anchor_bundle["beta"]) == anchor_beta
        and anchor_R_Q == int(anchor["expected_R_Q"])
        and anchor_R_Q < prime
    ):
        raise AssertionError("clean alpha-one anchor bundle changed")

    alternate = case["alternate"]
    alternate_Q = int(alternate["Q"])
    alternate_alpha = int(alternate["alpha"])
    alternate_beta = int(alternate["beta"])
    if not (
        R == alternate_alpha * alternate_Q + alternate_beta
        and K % (alternate_alpha * alternate_beta) == 0
    ):
        raise AssertionError("focused alternate slab changed")
    current: FormalNode = (8, 71, 1)
    alternate_path = []
    for raw_source, q, expected_shift, expected_destination in alternate["path"]:
        raw_source = tuple(raw_source)
        expected_destination = tuple(expected_destination)
        if current != raw_source:
            raise AssertionError("alternate path lost continuity")
        destination, shift, common = formal_transition(
            current, int(q), R, K_factors
        )
        if destination != expected_destination or shift != int(expected_shift) or common != 1:
            raise AssertionError("focused alternate path changed")
        alternate_path.append(
            {
                "source": list(current),
                "q": int(q),
                "shift": shift,
                "gcd_reduction": common,
                "destination": list(destination),
            }
        )
        current = destination
    expected_alternate_node = canonical_node(alternate_Q * alternate_alpha, R)
    alternate_R_Q, alternate_K_Q = canonical_chart(prime, alternate_Q)
    if (
        current[:2] != expected_alternate_node
        or alternate_R_Q != int(alternate["expected_R_Q"])
        or alternate_R_Q >= prime
    ):
        raise AssertionError("focused alternate marked carrier changed")
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "linear_source": {"a": a, "s": s, "a_times_s": a * s},
        "F_source_receipt": source_receipt,
        "Psi_0": overflow_height,
        "overflow_slab": {
            "alpha": alpha,
            "Q": Q,
            "beta": beta,
            "R_Q": R_Q,
            "K_Q": K_Q,
            "classification": "linear_F_bundle_overflow",
        },
        "clean_alpha_one_anchor_bundle": {
            "node": list(anchor_node),
            "peeling_q": Q,
            "shift": anchor_shift,
            "Q": anchor_Q,
            "beta": anchor_beta,
            "R_Q": anchor_R_Q,
            "K_Q": anchor_K_Q,
            "classification": "path_anchored_marked_bundle_edge",
        },
        "alternate_slab": {
            "alpha": alternate_alpha,
            "Q": alternate_Q,
            "beta": alternate_beta,
            "R_Q": alternate_R_Q,
            "K_Q": alternate_K_Q,
            "classification": "verified_marked_bundle_edge",
            "path": alternate_path,
        },
    }


def as_one_G_profile() -> dict[str, object]:
    case = AS_ONE_G_CASE
    prime = int(case["prime"])
    R = int(case["R"])
    a = int(case["a"])
    s = int(case["s"])
    K = (prime * R + 1) // 4
    if not (
        prime == a + s + a * s * R
        and prime % 24 == 1
        and R % 24 == 23
        and K == ((R + 1) // 2) ** 2
    ):
        raise AssertionError("as=1 linear source normal form changed")
    character_values = {
        str(q): jacobi_symbol(q, R) for q in factorization(K)
    }
    target_value = jacobi_symbol(-1, R)
    if any(value != 1 for value in character_values.values()) or target_value != -1:
        raise AssertionError("Jacobi G separator changed")
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "linear_source": {"a": a, "s": s, "a_times_s": 1},
        "K_support_character_values": character_values,
        "target_minus_one_character_value": target_value,
        "classification": "G_by_Jacobi_separator",
    }


def bottom_graph(
    R: int, K_factors: dict[int, int]
) -> tuple[dict[Node, set[Node]], dict[tuple[Node, Node], set[int]]]:
    adjacency: dict[Node, set[Node]] = {}
    labels: dict[tuple[Node, Node], set[int]] = {}
    for smaller in range(1, (R + 1) // 2):
        larger = R - smaller
        if gcd(smaller, larger) != 1:
            continue
        source = (smaller, larger)
        adjacency[source] = set()
        for selected in source:
            for q, exponent in factorization(selected).items():
                if exponent <= K_factors.get(q, 0):
                    continue
                destination = canonical_node(selected // q, R)
                adjacency[source].add(destination)
                labels.setdefault((source, destination), set()).add(q)
    return adjacency, labels


def strongly_connected_components(
    adjacency: dict[Node, set[Node]],
) -> list[set[Node]]:
    next_index = 0
    indices: dict[Node, int] = {}
    lowlinks: dict[Node, int] = {}
    stack: list[Node] = []
    on_stack: set[Node] = set()
    components: list[set[Node]] = []

    def visit(node: Node) -> None:
        nonlocal next_index
        indices[node] = next_index
        lowlinks[node] = next_index
        next_index += 1
        stack.append(node)
        on_stack.add(node)

        for destination in adjacency[node]:
            if destination not in indices:
                visit(destination)
                lowlinks[node] = min(lowlinks[node], lowlinks[destination])
            elif destination in on_stack:
                lowlinks[node] = min(lowlinks[node], indices[destination])

        if lowlinks[node] != indices[node]:
            return
        component: set[Node] = set()
        while True:
            member = stack.pop()
            on_stack.remove(member)
            component.add(member)
            if member == node:
                break
        components.append(component)

    for node in adjacency:
        if node not in indices:
            visit(node)
    return components


def sink_components(adjacency: dict[Node, set[Node]]) -> list[set[Node]]:
    return [
        component
        for component in strongly_connected_components(adjacency)
        if all(
            destination in component
            for source in component
            for destination in adjacency[source]
        )
    ]


def complete_excess_bundle(
    node: Node, K: int, K_factors: dict[int, int]
) -> dict[str, object]:
    smaller, larger = node
    Q = 1
    beta = 1
    offending_blocks: list[dict[str, int]] = []
    for q, exponent in factorization(larger).items():
        capacity = K_factors.get(q, 0)
        if exponent > capacity:
            Q *= q**exponent
            offending_blocks.append(
                {
                    "prime": q,
                    "node_exponent": exponent,
                    "K_capacity": capacity,
                }
            )
        else:
            beta *= q**exponent

    if Q <= 1 or larger != Q * beta:
        raise AssertionError("terminal-free minimum node lost its excess bundle")
    if gcd(Q, smaller * beta) != 1 or K % (smaller * beta):
        raise AssertionError("complete-excess residual did not fit in K")
    if K % Q == 0:
        raise AssertionError("complete-excess bundle unexpectedly divided K")
    return {
        "Q": Q,
        "beta": beta,
        "offending_blocks": offending_blocks,
        "residual_product": smaller * beta,
        "Q_gcd_K": gcd(Q, K),
    }


def has_single_prime_power_clean_slab(
    component: set[Node], K: int, K_factors: dict[int, int]
) -> bool:
    for node in component:
        for selected, other in (node, reversed(node)):
            for q, exponent in factorization(selected).items():
                if K_factors.get(q, 0) != 0:
                    continue
                Q = q**exponent
                if K % ((selected // Q) * other) == 0:
                    return True
    return False


def canonical_chart(prime: int, support: int) -> tuple[int, int]:
    modulus = 4 * support
    R_M = (-pow(prime, -1, modulus)) % modulus
    K_M = (prime * R_M + 1) // 4
    if not (1 <= R_M < modulus and R_M % 4 == 3 and K_M % support == 0):
        raise AssertionError("canonical support chart failed")
    return R_M, K_M


def case_profile(case: dict[str, object]) -> dict[str, object]:
    prime = int(case["prime"])
    R = int(case["R"])
    absorbed_support = int(case["absorbed_support"])
    K = (prime * R + 1) // 4
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and R % 4 == 3
        and 3 <= R <= prime - 2
        and 4 * K == prime * R + 1
        and K % absorbed_support == 0
    ):
        raise AssertionError("invalid focused core state")

    K_factors = factorization(K)
    F_source_receipt = (
        verify_F_source(case["F_source"], R, K_factors)
        if "F_source" in case
        else None
    )
    adjacency, labels = bottom_graph(R, K_factors)
    expected_node = tuple(case["expected_minimum_node"])
    matching = [
        component
        for component in sink_components(adjacency)
        if min(component, key=lambda node: (node[0], node)) == expected_node
    ]
    if len(matching) != 1:
        raise AssertionError("expected sink SCC was not unique")
    component = matching[0]
    if len(component) != int(case["expected_sink_size"]):
        raise AssertionError("focused sink SCC size changed")
    if any(not adjacency[node] for node in component):
        raise AssertionError("focused SCC unexpectedly contained a Type I sink")

    minimum_node = min(component, key=lambda node: (node[0], node))
    smaller, _larger = minimum_node
    if any(
        exponent > K_factors.get(q, 0)
        for q, exponent in factorization(smaller).items()
    ):
        raise AssertionError("minimum coordinate still had a raw outgoing edge")
    if K % smaller:
        raise AssertionError("minimum coordinate did not divide K")

    bundle = complete_excess_bundle(minimum_node, K, K_factors)
    if (
        int(bundle["Q"]) != int(case["expected_Q"])
        or int(bundle["beta"]) != int(case["expected_beta"])
    ):
        raise AssertionError("focused bundle changed")

    single_clean = has_single_prime_power_clean_slab(component, K, K_factors)
    if bool(case["require_no_single_prime_power_clean_slab"]) and single_clean:
        raise AssertionError("composite-carrier boundary gained a prime-power clean slab")

    Q = int(bundle["Q"])
    combined_support = lcm(absorbed_support, Q)
    if not (
        combined_support % absorbed_support == 0
        and combined_support % Q == 0
        and combined_support > absorbed_support
        and K % combined_support != 0
    ):
        raise AssertionError("lcm capacity join failed")
    R_M, K_M = canonical_chart(prime, combined_support)
    if R_M == R or R_M != int(case["expected_R_M"]):
        raise AssertionError("focused bundle chart changed")

    bound = (prime - 1) ** 2 // 4
    transition: dict[str, object]
    if R_M < prime:
        if not (
            combined_support <= K_M <= bound
            and bound // combined_support < bound // absorbed_support
        ):
            raise AssertionError("marked bundle potential failed")
        transition = {
            "classification": "verified_marked_bundle_edge",
            "R_M": R_M,
            "K_M": K_M,
            "combined_support": combined_support,
            "source_potential": bound // absorbed_support,
            "target_potential": bound // combined_support,
            "solution_lift": "identity_on_Sol(4,p)",
        }
    else:
        C, remainder = divmod(K_M, combined_support)
        n = 4 * combined_support - R_M
        d = prime - C
        if not (
            remainder == 0
            and combined_support > prime / 4
            and n > 0
            and d > 0
            and prime * n == 4 * combined_support * d + 1
            and gcd(combined_support, prime * n) == 1
        ):
            raise AssertionError("bundle overflow determinant failed")
        transition = {
            "classification": "complete_excess_bundle_overflow",
            "R_M": R_M,
            "K_M": K_M,
            "combined_support": combined_support,
            "C": C,
            "n": n,
            "d": d,
            "determinant": prime * n,
        }

    if transition["classification"] != case["expected_classification"]:
        raise AssertionError("focused bundle classification changed")

    edge_count = sum(len(adjacency[node]) for node in component)
    label_set = sorted(
        {
            q
            for source in component
            for destination in adjacency[source]
            for q in labels[(source, destination)]
        }
    )
    return {
        "name": case["name"],
        "prime": prime,
        "R": R,
        "K": K,
        "K_factorization": {str(q): e for q, e in K_factors.items()},
        "absorbed_support": absorbed_support,
        "F_source_receipt": F_source_receipt,
        "sink_scc": {
            "node_count": len(component),
            "edge_count": edge_count,
            "minimum_node": list(minimum_node),
            "raw_labels": label_set,
            "all_outgoing_edges_internal": True,
            "contains_Type_I_sink": False,
            "has_single_prime_power_clean_slab": single_clean,
        },
        "complete_excess_bundle": bundle,
        "capacity_join_rule": "lcm(absorbed_support,Q)",
        "product_would_overcount": (
            gcd(absorbed_support, Q) > 1
            and absorbed_support * Q != combined_support
        ),
        "transition": transition,
    }


def run() -> dict[str, object]:
    profiles = [case_profile(case) for case in CASES]
    linear_overflow = linear_F_overflow_profile()
    as_one_G = as_one_G_profile()
    summary = {
        "focused_case_count": len(profiles),
        "verified_marked_bundle_edge_count": sum(
            profile["transition"]["classification"]
            == "verified_marked_bundle_edge"
            for profile in profiles
        ),
        "bundle_overflow_count": sum(
            profile["transition"]["classification"]
            == "complete_excess_bundle_overflow"
            for profile in profiles
        ),
        "multi_prime_bundle_count": sum(
            len(profile["complete_excess_bundle"]["offending_blocks"]) > 1
            for profile in profiles
        ),
        "K_overlap_bundle_count": sum(
            int(profile["complete_excess_bundle"]["Q_gcd_K"]) > 1
            for profile in profiles
        ),
        "lcm_prevents_overcount_count": sum(
            bool(profile["product_would_overcount"]) for profile in profiles
        ),
        "single_prime_power_clean_slab_counterexample_count": sum(
            not profile["sink_scc"]["has_single_prime_power_clean_slab"]
            for profile in profiles
            if profile["name"]
            == "F_reach_composite_bundle_without_single_prime_power_clean_slab"
        ),
        "binary_self_loop_closed_count": sum(
            profile["name"] == "binary_self_loop_bundle_marked_edge"
            and profile["transition"]["classification"]
            == "verified_marked_bundle_edge"
            for profile in profiles
        ),
        "linear_F_overflow_ray_count": 1,
        "same_reach_alternate_marked_carrier_count": int(
            linear_overflow["alternate_slab"]["classification"]
            == "verified_marked_bundle_edge"
        ),
        "clean_alpha_one_anchor_closed_count": int(
            linear_overflow["clean_alpha_one_anchor_bundle"]["classification"]
            == "path_anchored_marked_bundle_edge"
        ),
        "as_one_Jacobi_G_exclusion_count": int(
            as_one_G["classification"] == "G_by_Jacobi_separator"
        ),
    }
    expected = {
        "focused_case_count": 4,
        "verified_marked_bundle_edge_count": 3,
        "bundle_overflow_count": 1,
        "multi_prime_bundle_count": 3,
        "K_overlap_bundle_count": 2,
        "lcm_prevents_overcount_count": 2,
        "single_prime_power_clean_slab_counterexample_count": 1,
        "binary_self_loop_closed_count": 1,
        "linear_F_overflow_ray_count": 1,
        "same_reach_alternate_marked_carrier_count": 1,
        "clean_alpha_one_anchor_closed_count": 1,
        "as_one_Jacobi_G_exclusion_count": 1,
    }
    if summary != expected:
        raise AssertionError(f"focused bundle summary changed: {summary}")
    return {
        "schema_version": "type-i-bottom-sink-scc-complete-excess-bundle/v1",
        "scope_note": (
            "Focused exact verification of four complete-excess bundle receipts. "
            "It does not rerun historical state censuses or prove the universal "
            "sink-SCC theorem, whose proof is algebraic."
        ),
        "summary": summary,
        "cases": profiles,
        "linear_F_overflow_boundary": linear_overflow,
        "as_one_linear_source_G_boundary": as_one_G,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
    else:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
