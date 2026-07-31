#!/usr/bin/env python3
"""Audit affine-boundary gap candidates on the four complete-Reach residuals."""

from __future__ import annotations

from collections import Counter
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
    / "type-i-psi-one-affine-boundary-terminal-profile-results.json"
)

EXPECTED_INPUT_SHA256 = "eb0ef6c4fe5103d907916ebb4d2fc0bc97913344d3cb143e1f17cb582fa0adc2"
EXPECTED_RESIDUALS = [
    (37_793_809, 35),
    (78_268_369, 8_895),
    (174_600_409, 20_631),
    (278_505_049, 231),
]
EXPECTED_PROFILES = [
    (37_793_809, 35, 20, 35, 28, 3, 43, "layer_m", 2_715_622, "Type_I", 8_789_857),
    (78_268_369, 8_895, 6, 6, 9, 2, 19, "abs_A_minus_R", 8_569, "Type_I", 1_361),
    (174_600_409, 20_631, 200, 518, 199, 23, 19, "B", 20_615, "Type_I", 4_200_193),
    (278_505_049, 231, 28, 50, 62, 11, 15, "layer_m", 60, "Type_I", 2_066),
]

Node = tuple[int, int, int]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


closure = load_module("affine_boundary_closure", CLOSURE_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complete_reach(record: dict[str, object]) -> tuple[set[Node], int]:
    R = int(record["R"])
    bounds = {int(q): int(exponent) for q, exponent in record["factorization"]}
    starts = {
        tuple(int(value) for value in witness["start"])
        for witness in record["positive_witnesses"]
    }
    maximum_start_layer = max(node[2] for node in starts)
    coarse_bound = R * maximum_start_layer * (maximum_start_layer + 1) // 4

    visited: set[Node] = set()
    frontier = list(sorted(starts, reverse=True))
    edge_count = 0
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        edges = closure.raw_transitions(node, R, bounds)
        edge_count += len(edges)
        for edge in edges:
            destination = tuple(int(value) for value in edge["destination"])
            if destination not in visited:
                frontier.append(destination)
        if len(visited) > coarse_bound:
            raise AssertionError("complete Reach exceeded its arithmetic bound")
    return visited, edge_count


def boundary_quantities(node: Node, R: int) -> tuple[tuple[str, int], ...]:
    A, B, layer = node
    return (
        ("A", A),
        ("B", B),
        ("layer_m", layer),
        ("abs_A_minus_R", abs(A - R)),
        ("abs_B_minus_R", abs(B - R)),
    )


def affine_boundary_profile(record: dict[str, object]) -> dict[str, object]:
    prime = int(record["prime"])
    R = int(record["R"])
    K = int(record["K"])
    nodes, edge_count = complete_reach(record)

    origins: dict[int, dict[str, object]] = {}
    candidate_quantity_counts: Counter[str] = Counter()
    for node in sorted(nodes):
        for quantity, value in boundary_quantities(node, R):
            if value == 0:
                continue
            for gap in closure.divisors(value):
                if (
                    gap % 4 != 3
                    or not 3 <= gap <= prime - 2
                    or gap // math.gcd(gap, K) <= 1
                ):
                    continue
                candidate_quantity_counts[quantity] += 1
                origins.setdefault(
                    gap,
                    {
                        "node": list(node),
                        "quantity": quantity,
                        "quantity_value": value,
                        "external_part": gap // math.gcd(gap, K),
                    },
                )

    hits = []
    type_counts: Counter[str] = Counter()
    for gap in sorted(origins):
        certificate = closure.exact_gap_certificate(prime, gap)
        if certificate is None:
            continue
        type_counts[str(certificate["type"])] += 1
        hits.append(
            {
                "candidate_gap": gap,
                "origin": origins[gap],
                **certificate,
            }
        )

    return {
        "prime": prime,
        "R": R,
        "reachable_node_count": len(nodes),
        "reachable_edge_count": edge_count,
        "candidate_gap_count": len(origins),
        "candidate_quantity_occurrences": {
            label: candidate_quantity_counts[label]
            for label in ("A", "B", "layer_m", "abs_A_minus_R", "abs_B_minus_R")
        },
        "hit_gap_count": len(hits),
        "type_i_gap_count": int(type_counts["Type_I"]),
        "type_ii_gap_count": int(type_counts["Type_II"]),
        "first_verified_hit": hits[0] if hits else None,
        "all_hit_gaps": [int(hit["candidate_gap"]) for hit in hits],
        "hit": bool(hits),
        "edge_semantics": "analysis_evidence_not_verified_edge",
        "terminal_semantics": "independently_verified_direct_certificate",
    }


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen full-spectrum audit changed")
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    records = {
        (int(record["prime"]), int(record["R"])): record
        for record in source["records"]
    }
    profiles = [affine_boundary_profile(records[state]) for state in EXPECTED_RESIDUALS]

    observed = [
        (
            int(profile["prime"]),
            int(profile["R"]),
            int(profile["reachable_node_count"]),
            int(profile["reachable_edge_count"]),
            int(profile["candidate_gap_count"]),
            int(profile["hit_gap_count"]),
            int(profile["first_verified_hit"]["candidate_gap"]),
            str(profile["first_verified_hit"]["origin"]["quantity"]),
            int(profile["first_verified_hit"]["origin"]["quantity_value"]),
            str(profile["first_verified_hit"]["type"]),
            int(profile["first_verified_hit"]["divisor"]),
        )
        for profile in profiles
    ]
    if observed != EXPECTED_PROFILES:
        raise AssertionError(f"affine-boundary profiles changed: {observed}")

    summary = {
        "input_residual_state_count": len(profiles),
        "reachable_node_count": sum(int(profile["reachable_node_count"]) for profile in profiles),
        "reachable_edge_count": sum(int(profile["reachable_edge_count"]) for profile in profiles),
        "candidate_gap_count": sum(int(profile["candidate_gap_count"]) for profile in profiles),
        "hit_gap_count": sum(int(profile["hit_gap_count"]) for profile in profiles),
        "direct_hit_state_count": sum(bool(profile["hit"]) for profile in profiles),
        "previous_complete_reach_verified_state_count": 2,
        "expanded_complete_reach_verified_state_count": 4,
        "frozen_psi_one_state_count": 483,
        "frozen_final_verified_state_count": 483,
    }
    return {
        "schema_version": "psi-one-affine-boundary-terminal-profile/v1",
        "arithmetic": (
            "For each node (A,B,m) in the complete raw-transition Reach of the four frozen "
            "state-local residuals, enumerate legal external divisors of A, B, m, |A-R|, "
            "and |B-R|; then exhaust the square-divisor Type I/II test for each gap."
        ),
        "scope_note": (
            "This is a finite candidate-generation profile on four frozen states. Formal Reach "
            "edges remain analysis evidence. Every reported terminal independently reconstructs "
            "a solution for the original prime, but the profile does not prove that the affine "
            "boundary menu succeeds for every Psi_0=1 F state."
        ),
        "input": {"path": INPUT.name, "sha256": sha256(INPUT)},
        "closure_script": {
            "path": CLOSURE_SCRIPT.name,
            "sha256": sha256(CLOSURE_SCRIPT),
        },
        "script_sha256": sha256(Path(__file__)),
        "summary": summary,
        "records": profiles,
    }


def main() -> int:
    import argparse

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
