#!/usr/bin/env python3
"""Verify the source-word joint-capacity dichotomy and focused boundaries."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-psi-one-full-spectrum-terminal-descent-audit-results.json"
)
CLOSURE_SCRIPT = (
    ROOT / "reproductions" / "type_i_f_psi_one_formal_transition_closure.py"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-source-word-joint-capacity-dichotomy-results.json"
)

EXPECTED_INPUT_SHA256 = (
    "eb0ef6c4fe5103d907916ebb4d2fc0bc97913344d3cb143e1f17cb582fa0adc2"
)
EXPECTED_CLOSURE_SHA256 = (
    "cd76a4f2c0e602324f87d91ab4be86754feb2c256ab9553a6a05615f91286846"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


closure = load_module("source_word_joint_capacity_closure", CLOSURE_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factorization(n: int) -> dict[str, int]:
    return {str(q): exponent for q, exponent in closure.factorization(n).items()}


def require_edge(
    source: tuple[int, int, int],
    destination: tuple[int, int, int],
    q: int,
    gcd_reduction: int,
    R: int,
    K: int,
) -> None:
    bounds = closure.factorization(K)
    matches = [
        edge
        for edge in closure.raw_transitions(source, R, bounds)
        if tuple(int(value) for value in edge["destination"]) == destination
        and int(edge["q"]) == q
        and int(edge["gcd_reduction"]) == gcd_reduction
    ]
    if len(matches) != 1:
        raise AssertionError(
            f"expected one edge {source} --{q},{gcd_reduction}--> {destination}"
        )


def capacity_profile(prime: int, R: int, product: int) -> dict[str, object]:
    K = (prime * R + 1) // 4
    x_R = (prime + R) // 4
    assert 4 * K == prime * R + 1 and 4 * x_R == prime + R
    delta_raw = (R * R - 1) // 4
    assert R * x_R - K == delta_raw
    assert prime * x_R - K == (prime * prime - 1) // 4

    common_capacity = math.gcd(K, x_R)
    assert common_capacity == math.gcd(x_R, delta_raw)
    assert 4 * common_capacity == math.gcd(prime + R, R * R - 1)
    assert 4 * common_capacity == math.gcd(prime + R, prime * prime - 1)
    K_exclusive = K // common_capacity
    x_exclusive = x_R // common_capacity
    assert math.gcd(K_exclusive, x_exclusive) == 1
    joint_capacity = math.lcm(K, x_R)
    assert joint_capacity == common_capacity * K_exclusive * x_exclusive

    K_defect = product // math.gcd(product, K)
    x_defect = product // math.gcd(product, x_R)
    common_overload = product // math.gcd(product, joint_capacity)
    defect_union = product // math.gcd(product, common_capacity)
    assert math.gcd(K_defect, x_defect) == common_overload
    assert math.lcm(K_defect, x_defect) == defect_union

    double_miss = K_defect > 1 and x_defect > 1
    branch = "not_double_miss"
    exchange: dict[str, object] | None = None
    if double_miss and common_overload > 1:
        branch = "common_overload"
    elif double_miss:
        branch = "split_exchange"
        reduced_delta = delta_raw // common_capacity
        assert joint_capacity % product == 0
        assert K_defect > 1 and x_defect > 1
        assert math.gcd(K_defect, x_defect) == 1
        assert x_exclusive % K_defect == 0
        assert K_exclusive % x_defect == 0
        assert K_defect * x_defect == product // math.gcd(product, common_capacity)
        assert math.gcd(K_defect * x_defect, reduced_delta) == 1
        assert (prime + R) % (4 * common_capacity * K_defect) == 0
        assert (prime * R + 1) % (4 * common_capacity * x_defect) == 0
        a = x_R // (common_capacity * K_defect)
        b = K // (common_capacity * x_defect)
        assert R * K_defect * a - x_defect * b == reduced_delta
        exchange = {
            "reduced_delta": reduced_delta,
            "a": a,
            "b": b,
            "identity": "R*E_K*a-E_x*b=delta",
        }

    return {
        "product": product,
        "product_factorization": factorization(product),
        "K_defect": K_defect,
        "x_R_defect": x_defect,
        "common_overload_factor": common_overload,
        "defect_union": defect_union,
        "branch": branch,
        "exchange": exchange,
    }


def normalized_pair(left: int, right: int, R: int) -> dict[str, int]:
    common = math.gcd(left, right)
    P = left // common
    Q = right // common
    assert math.gcd(P, Q) == 1 and (P + Q) % R == 0
    return {
        "common": common,
        "P": P,
        "Q": Q,
        "layer": (P + Q) // R,
        "product": P * Q,
    }


PATH_CASES = (
    {
        "name": "smallest_core_ambient_empty_suffix_split",
        "prime": 73,
        "R": 23,
        "source": (1, 45, 2),
        "edges": (((1, 45, 2), 3, 1, (8, 15, 1)),),
        "U": 15,
        "V": 8,
        "theta": 1,
        "X": 15,
        "Y": 8,
        "expected_products": (120, 120),
        "expected_branches": ("split_exchange", "split_exchange"),
        "boundary": "ambient_formal_state_not_F",
    },
    {
        "name": "nonempty_both_split",
        "prime": 1_297,
        "R": 47,
        "source": (12, 35, 1),
        "edges": (((12, 35, 1), 7, 1, (5, 42, 1)),),
        "U": 12,
        "V": 35,
        "theta": 7,
        "X": 42,
        "Y": 5,
        "expected_products": (420, 210),
        "expected_branches": ("split_exchange", "split_exchange"),
        "boundary": "formal_path_not_source_anchored",
    },
    {
        "name": "frozen_F_empty_suffix_split_with_internal_terminal",
        "prime": 68_822_329,
        "R": 14_231,
        "source": (207, 3_870_625, 272),
        "edges": (((207, 3_870_625, 272), 5, 55, (156, 14_075, 1)),),
        "U": 14_075,
        "V": 156,
        "theta": 1,
        "X": 14_075,
        "Y": 156,
        "expected_products": (2_195_700, 2_195_700),
        "expected_branches": ("split_exchange", "split_exchange"),
        "boundary": "frozen_F_but_internal_gap_191_is_Type_I",
    },
    {
        "name": "source_anchored_internal_free_mixed_branch",
        "prime": 122_014_489,
        "R": 471,
        "source": (16, 80_525, 171),
        "edges": (
            ((16, 80_525, 171), 5, 5, (76, 3_221, 7)),
            ((76, 3_221, 7), 19, 1, (4, 467, 1)),
        ),
        "U": 3_221,
        "V": 76,
        "theta": 19,
        "X": 467,
        "Y": 4,
        "expected_products": (244_796, 1_868),
        "expected_branches": ("split_exchange", "common_overload"),
        "boundary": "internal_free_but_external_gap_35_is_Type_I",
    },
    {
        "name": "minimum_formal_descendant_residual_common_overload",
        "prime": 5_596_369,
        "R": 35,
        "source": (107, 18_723, 538),
        "edges": (
            ((107, 18_723, 538), 79, 1, (8, 237, 7)),
            ((8, 237, 7), 2, 4, (1, 34, 1)),
            ((1, 34, 1), 17, 1, (2, 33, 1)),
            ((2, 33, 1), 11, 1, (3, 32, 1)),
        ),
        "U": 237,
        "V": 8,
        "theta": 1_496,
        "X": 32,
        "Y": 3,
        "expected_products": (118_184, 5_984),
        "expected_branches": ("common_overload", "common_overload"),
        "expected_common_factors": (136, 544),
        "boundary": "formal_descendant_residual_analysis_evidence",
    },
    {
        "name": "alpha_three_cycle_entry_common_overload",
        "prime": 212_973_049,
        "R": 215,
        "source": (1_585_081, 2_273_094, 17_945),
        "edges": (
            ((1_585_081, 2_273_094, 17_945), 1_259, 1, (1_259, 1_966, 15)),
            ((1_259, 1_966, 15), 983, 1, (2, 213, 1)),
        ),
        "U": 1_259,
        "V": 1_966,
        "theta": 983,
        "X": 213,
        "Y": 2,
        "expected_products": (2_475_194, 426),
        "expected_branches": ("common_overload", "common_overload"),
        "expected_common_factors": (983, 71),
        "boundary": "formal_cycle_entry_analysis_evidence",
    },
    {
        "name": "two_cross_products_have_disjoint_common_carriers",
        "prime": 37_793_809,
        "R": 12_423,
        "source": (3_493, 149_532_158, 12_037),
        "edges": (
            ((3_493, 149_532_158, 12_037), 1_553, 2, (1_549, 48_143, 4)),
            ((1_549, 48_143, 4), 1_549, 1, (1, 12_422, 1)),
        ),
        "U": 48_143,
        "V": 1_549,
        "theta": 1_549,
        "X": 12_422,
        "Y": 1,
        "expected_products": (74_573_507, 12_422),
        "expected_branches": ("common_overload", "common_overload"),
        "expected_common_factors": (1_549, 6_211),
        "boundary": "same_common_overload_prime_is_not_forced_across_pairs",
    },
)


def frozen_record(records: list[dict[str, object]], prime: int, R: int):
    matches = [
        record
        for record in records
        if int(record["prime"]) == prime and int(record["R"]) == R
    ]
    if len(matches) != 1:
        raise AssertionError(f"expected one frozen record for {(prime, R)}")
    return matches[0]


def analyze_path_case(
    case: dict[str, object], records: list[dict[str, object]]
) -> dict[str, object]:
    prime = int(case["prime"])
    R = int(case["R"])
    K = (prime * R + 1) // 4
    for source, q, common, destination in case["edges"]:
        require_edge(source, destination, q, common, R, K)

    U = int(case["U"])
    V = int(case["V"])
    theta = int(case["theta"])
    X = int(case["X"])
    Y = int(case["Y"])
    assert (U + V) % R == 0 and X + Y == R
    assert (theta * X - U) % R == 0
    assert (theta * Y - V) % R == 0
    u = (theta * X - U) // R
    v = (theta * Y - V) // R
    assert u >= 0 and v >= 0
    assert u + v == theta - (U + V) // R

    pairs = (
        normalized_pair(U, theta * Y, R),
        normalized_pair(V, theta * X, R),
    )
    products = tuple(pair["product"] for pair in pairs)
    assert products == tuple(case["expected_products"])
    profiles = [capacity_profile(prime, R, product) for product in products]
    branches = tuple(str(profile["branch"]) for profile in profiles)
    assert branches == tuple(case["expected_branches"])
    common_factors = tuple(
        int(profile["common_overload_factor"]) for profile in profiles
    )
    if "expected_common_factors" in case:
        assert common_factors == tuple(case["expected_common_factors"])

    frozen_boundary: dict[str, object] | None = None
    record: dict[str, object] | None = None
    if prime in {5_596_369, 37_793_809, 68_822_329, 122_014_489, 212_973_049}:
        record = frozen_record(records, prime, R)
        starts = {
            tuple(int(value) for value in witness["start"])
            for witness in record["positive_witnesses"]
        }
        assert tuple(case["source"]) in starts

    if prime == 68_822_329:
        assert record is not None
        certificate = record["internal"]["first_verified_certificate"]
        assert certificate["gap"] == 191 and certificate["type"] == "Type_I"
        frozen_boundary = {
            "internal_hit": True,
            "gap": 191,
            "type": "Type_I",
        }
    elif prime == 122_014_489:
        assert record is not None
        assert int(record["internal"]["legal_gap_count"]) == 7
        assert not bool(record["internal"]["hit"])
        certificate = record["min_rank"]["visited_terminals"][
            "first_verified_certificate"
        ]
        assert certificate["gap"] == 35 and certificate["type"] == "Type_I"
        frozen_boundary = {
            "internal_hit": False,
            "reachable_external_gap": 35,
            "type": "Type_I",
        }
    elif prime == 37_793_809:
        assert record is not None and not bool(record["internal"]["hit"])
        frozen_boundary = {
            "internal_hit": False,
            "common_carrier_intersection": None,
        }

    return {
        "name": str(case["name"]),
        "prime": prime,
        "R": R,
        "K": K,
        "x_R": (prime + R) // 4,
        "source": list(case["source"]),
        "edge_count": len(case["edges"]),
        "post_first_oriented": [U, V, (U + V) // R],
        "endpoint_oriented": [X, Y, 1],
        "theta": theta,
        "u": u,
        "v": v,
        "cross_pairs": [
            {**pair, "capacity": profile}
            for pair, profile in zip(pairs, profiles)
        ],
        "common_carrier_intersection": factorization(
            math.gcd(common_factors[0], common_factors[1])
        ),
        "boundary": str(case["boundary"]),
        "frozen_boundary": frozen_boundary,
    }


def analyze_ambient_difference_case() -> dict[str, object]:
    prime = 97
    R = 47
    product = 2 * 45
    profile = capacity_profile(prime, R, product)
    assert profile["branch"] == "split_exchange"
    gap = 45 - 2
    assert gap == 43 and closure.exact_gap_certificate(prime, gap) is None
    return {
        "prime": prime,
        "R": R,
        "bottom_node": [2, 45, 1],
        "capacity": profile,
        "coordinate_difference_gap": gap,
        "complete_gap_hit": False,
        "boundary": (
            "A split-exchange product does not make its coordinate difference "
            "a Type I/II terminal."
        ),
    }


def complete_reach(
    starts: tuple[tuple[int, int, int], ...], R: int, K: int
) -> tuple[set[tuple[int, int, int]], list[dict[str, object]]]:
    bounds = closure.factorization(K)
    visited: set[tuple[int, int, int]] = set()
    edges: list[dict[str, object]] = []
    frontier = list(starts)
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        for edge in closure.raw_transitions(node, R, bounds):
            destination = tuple(int(value) for value in edge["destination"])
            edges.append(
                {
                    "source": list(node),
                    "q": int(edge["q"]),
                    "destination": list(destination),
                }
            )
            if destination not in visited:
                frontier.append(destination)
    return visited, edges


def analyze_complete_reach_split_counterexample() -> dict[str, object]:
    prime = 2_017
    R = 207
    K = (prime * R + 1) // 4
    x_R = (prime + R) // 4
    assert K == 104_380 and x_R == 556 and prime % 24 == 1

    source = (1_156, 1_535, 13)
    endpoint = (68, 139, 1)
    require_edge(source, endpoint, 17, 1, R, K)
    assert 1_535 * 68 == K and 1_156 == 17 * 68
    assert math.gcd(source[0], source[1]) == 1 and sum(source[:2]) == R * source[2]

    profile = capacity_profile(prime, R, 68 * 139)
    assert profile["branch"] == "split_exchange"
    assert (
        profile["K_defect"],
        profile["x_R_defect"],
        profile["common_overload_factor"],
    ) == (139, 17, 1)
    assert profile["exchange"] == {
        "reduced_delta": 2_678,
        "a": 1,
        "b": 1_535,
        "identity": "R*E_K*a-E_x*b=delta",
    }

    _, centered_hits = closure.centered_type_i_hits(prime, R, K)
    assert not centered_hits
    internal_gaps = [
        gap
        for gap in closure.divisors(K)
        if gap % 4 == 3 and 3 <= gap <= prime - 2
    ]
    assert internal_gaps == [307, 1_535]
    assert all(closure.exact_gap_certificate(prime, gap) is None for gap in internal_gaps)

    endpoint_nodes, endpoint_edges = complete_reach((endpoint,), R, K)
    expected_endpoint_nodes = {
        (68, 139, 1),
        (1, 206, 1),
        (2, 205, 1),
        (5, 202, 1),
    }
    assert endpoint_nodes == expected_endpoint_nodes and len(endpoint_edges) == 4
    gaps, origins = closure.external_gap_candidates(endpoint_nodes, prime, K)
    assert gaps == [103, 139]
    assert all(closure.exact_gap_certificate(prime, gap) is None for gap in gaps)

    second_source = (4, 1_445, 7)
    second_endpoint = (85, 122, 1)
    require_edge(second_source, second_endpoint, 17, 1, R, K)
    state_nodes, state_edges = complete_reach((endpoint, second_endpoint), R, K)
    assert state_nodes == expected_endpoint_nodes | {second_endpoint}
    assert len(state_edges) == 5
    state_gaps, _ = closure.external_gap_candidates(state_nodes, prime, K)
    assert state_gaps == gaps

    first_edge = next(
        edge
        for edge in endpoint_edges
        if edge["source"] == list(endpoint) and edge["q"] == 139
    )
    assert first_edge["destination"] == [1, 206, 1]
    old_pairs = (
        normalized_pair(68, 139, R),
        normalized_pair(139, 68, R),
    )
    new_pairs = (
        normalized_pair(68, 139, R),
        normalized_pair(139, 139 * 206, R),
    )
    assert old_pairs[0] == new_pairs[0]
    assert old_pairs[1]["product"] == 9_452 and new_pairs[1]["product"] == 206

    return {
        "prime": prime,
        "R": R,
        "K": K,
        "x_R": x_R,
        "source": list(source),
        "post_first": list(endpoint),
        "capacity": profile,
        "centered_type_i_hit": False,
        "internal_gaps": internal_gaps,
        "internal_gap_hits": [],
        "endpoint_reach": {
            "nodes": [list(node) for node in sorted(endpoint_nodes)],
            "edges": endpoint_edges,
            "external_gaps": gaps,
            "external_gap_origins": {str(gap): origin for gap, origin in origins.items()},
            "external_gap_hits": [],
        },
        "state_post_first_reach": {
            "starts": [list(endpoint), list(second_endpoint)],
            "node_count": len(state_nodes),
            "edge_count": len(state_edges),
            "external_gaps": state_gaps,
            "external_gap_hits": [],
        },
        "first_bottom_transition": {
            "selected_q": 139,
            "scaled_pair_before": [68, 139],
            "scaled_pair_after": [68, 139 * 206],
            "invariant_cross_product": old_pairs[0]["product"],
            "updated_cross_product": new_pairs[1]["product"],
        },
        "boundary": (
            "Strict split does not force an external terminal at any bounded "
            "depth or anywhere in the complete formal Reach."
        ),
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("frozen Psi-one input hash changed")
    if sha256(CLOSURE_SCRIPT) != EXPECTED_CLOSURE_SHA256:
        raise AssertionError("formal closure script hash changed")
    frozen = json.loads(INPUT.read_text(encoding="utf-8"))
    path_records = [
        analyze_path_case(case, frozen["records"]) for case in PATH_CASES
    ]
    branch_histogram: dict[str, int] = {}
    for record in path_records:
        for pair in record["cross_pairs"]:
            branch = str(pair["capacity"]["branch"])
            branch_histogram[branch] = branch_histogram.get(branch, 0) + 1
    summary = {
        "path_case_count": len(path_records),
        "cross_pair_count": sum(len(record["cross_pairs"]) for record in path_records),
        "branch_histogram": dict(sorted(branch_histogram.items())),
        "split_exchange_path_count": sum(
            any(
                pair["capacity"]["branch"] == "split_exchange"
                for pair in record["cross_pairs"]
            )
            for record in path_records
        ),
        "disjoint_common_carrier_path_count": sum(
            all(
                pair["capacity"]["branch"] == "common_overload"
                for pair in record["cross_pairs"]
            )
            and not record["common_carrier_intersection"]
            for record in path_records
        ),
    }
    expected_summary = {
        "path_case_count": 7,
        "cross_pair_count": 14,
        "branch_histogram": {"common_overload": 7, "split_exchange": 7},
        "split_exchange_path_count": 4,
        "disjoint_common_carrier_path_count": 2,
    }
    if summary != expected_summary:
        raise AssertionError(f"focused joint-capacity boundary changed: {summary}")
    return {
        "schema_version": "type-i-source-word-joint-capacity-dichotomy/v2",
        "scope_note": (
            "Focused exact verification of the algebraic capacity dichotomy and "
            "seven boundary paths, plus the five-node p=2017 complete-Reach "
            "split counterexample. It does not reproduce the full 1412-slab "
            "census and does not upgrade a formal edge to an E4 transition."
        ),
        "inputs": {
            "frozen_psi_one_sha256": EXPECTED_INPUT_SHA256,
            "formal_closure_sha256": EXPECTED_CLOSURE_SHA256,
        },
        "summary": summary,
        "path_records": path_records,
        "ambient_difference_counterexample": analyze_ambient_difference_case(),
        "complete_reach_split_counterexample": analyze_complete_reach_split_counterexample(),
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
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
