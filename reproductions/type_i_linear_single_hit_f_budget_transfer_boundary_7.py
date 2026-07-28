#!/usr/bin/env python3
"""Audit known local source transfers from single-hit F budget boundaries."""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PULLBACK_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-single-hit-f-cross-source-pullback-7-results.json"
)
SPECTRUM_INPUT = ROOT / "reproductions" / "type-i-linear-full-spectrum-bgt1-200-results.json"
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-single-hit-f-budget-transfer-boundary-7-results.json"
)
EXPECTED_PULLBACK_SHA256 = (
    "f4b91e222ccfda1e428d7f646b1066c978101ba0398cd45b002e08e48f36d1d5"
)
EXPECTED_SPECTRUM_SHA256 = (
    "5f60c11b255aac289b45d2a4721b233534b7bc29476b76bb5f41efc0917a0196"
)
SINGLE_HIT_PRIMES = (
    67_369,
    878_089,
    13_782_409,
    26_034_649,
    57_399_241,
    152_498_329,
    283_319_689,
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


fixed = load_module(
    "single_hit_budget_fixed_transfer",
    ROOT / "reproductions" / "type_i_linear_source_factor_transfer_profile_600m.py",
)
shift = load_module(
    "single_hit_budget_shift_transfer",
    ROOT / "reproductions" / "type_i_linear_source_shift_transfer_closure_profile_600m.py",
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def boundary_rows(payload: dict[str, object]) -> list[dict[str, int]]:
    rows = []
    for profile in payload["profiles"]:
        prime = int(profile["prime"])
        for record in profile["records"]:
            R = int(record["R"])
            for orientation in record["orientations"]:
                for residue, witness in orientation.get(
                    "subgroup_pullback_exponent_overflow", {}
                ).items():
                    rows.append(
                        {
                            "prime": prime,
                            "R": R,
                            "a": int(orientation["a"]),
                            "s": int(orientation["s"]),
                            "residue": int(residue),
                            "overflow": int(witness["minimum_extra_exponent"]),
                        }
                    )
    return rows


def full_spectrum_by_prime(
    payload: dict[str, object],
) -> dict[int, dict[str, object]]:
    profiles = {int(profile["prime"]): profile for profile in payload["records"]}
    if set(SINGLE_HIT_PRIMES) - set(profiles):
        raise AssertionError("single-hit spectrum input is incomplete")
    return profiles


def state_edges(
    prime: int, states: set[tuple[int, int, int]]
) -> tuple[list[tuple[int, int, int]], dict[str, int]]:
    fixed_edges = [
        (tuple(row["from"]), tuple(row["to"]))
        for row in fixed.factor_transfers(prime, states)
    ]
    _, shift_edges = shift.shift_transfers(prime, states)
    swaps = shift.orientation_swaps(states)
    edges = [
        *fixed_edges,
        *shift_edges,
        *swaps,
        *[(target, source) for source, target in swaps],
    ]
    counts = {
        "fixed_factor_transfer_count": len(fixed_edges),
        "shift_factor_transfer_count": len(shift_edges),
        "orientation_swap_edge_count": len(swaps),
        "known_directed_edge_count": len(edges),
    }
    if len(set(edges)) != len(edges):
        raise AssertionError("local source transfer edges were duplicated")
    return edges, counts


def reverse_reachable(
    states: set[tuple[int, int, int]],
    hit_states: set[tuple[int, int, int]],
    edges: list[tuple[tuple[int, int, int], tuple[int, int, int]]],
) -> set[tuple[int, int, int]]:
    reverse: dict[tuple[int, int, int], set[tuple[int, int, int]]] = defaultdict(set)
    for source, target in edges:
        reverse[target].add(source)
    reachable = set(hit_states)
    pending = list(hit_states)
    while pending:
        target = pending.pop()
        for source in reverse[target]:
            if source not in reachable:
                reachable.add(source)
                pending.append(source)
    if not reachable <= states:
        raise AssertionError("reverse reachability left the source state set")
    return reachable


def profile_prime(
    prime: int,
    source_profile: dict[str, object],
    rows: list[dict[str, int]],
) -> dict[str, object]:
    states = fixed.checked_states(prime)
    hit_R = {
        int(record["R"])
        for record in source_profile["records"]
        if record["classification"] == "hit"
    }
    hit_states = {state for state in states if state[2] in hit_R}
    edges, edge_counts = state_edges(prime, states)
    reachable = reverse_reachable(states, hit_states, edges)

    adjacency: dict[tuple[int, int, int], set[tuple[int, int, int]]] = defaultdict(set)
    undirected: dict[tuple[int, int, int], set[tuple[int, int, int]]] = defaultdict(set)
    for source, target in edges:
        adjacency[source].add(target)
        undirected[source].add(target)
        undirected[target].add(source)

    components: list[set[tuple[int, int, int]]] = []
    unseen = set(states)
    while unseen:
        seed = min(unseen)
        component = {seed}
        unseen.remove(seed)
        pending = [seed]
        while pending:
            state = pending.pop()
            for neighbor in undirected[state]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.add(neighbor)
                    pending.append(neighbor)
        components.append(component)
    component_by_state = {
        state: component for component in components for state in component
    }

    prime_rows = []
    for row in rows:
        state = (row["a"], row["s"], row["R"])
        if state not in states:
            raise AssertionError("budget boundary state is not a complete source state")
        component = component_by_state[state]
        outgoing = adjacency[state]
        prime_rows.append(
            {
                **row,
                "outgoing_edge_count": len(outgoing),
                "directed_reaches_hit": state in reachable,
                "direct_hit_edge_count": sum(
                    int(target in hit_states) for target in outgoing
                ),
                "undirected_component_size": len(component),
                "undirected_component_contains_hit": bool(
                    component & hit_states
                ),
            }
        )

    return {
        "prime": prime,
        "source_state_count": len(states),
        **edge_counts,
        "hit_R": sorted(hit_R),
        "hit_state_count": len(hit_states),
        "reverse_reachable_state_count": len(reachable),
        "boundary_rows": prime_rows,
    }


def run_audit(
    pullback_path: Path = PULLBACK_INPUT,
    spectrum_path: Path = SPECTRUM_INPUT,
) -> dict[str, object]:
    if file_sha256(pullback_path) != EXPECTED_PULLBACK_SHA256:
        raise AssertionError("pullback input changed")
    if file_sha256(spectrum_path) != EXPECTED_SPECTRUM_SHA256:
        raise AssertionError("full-spectrum input changed")
    pullback = json.loads(pullback_path.read_text(encoding="utf-8"))
    spectrum = json.loads(spectrum_path.read_text(encoding="utf-8"))
    profiles = full_spectrum_by_prime(spectrum)
    rows = boundary_rows(pullback)
    grouped: dict[int, list[dict[str, int]]] = defaultdict(list)
    for row in rows:
        grouped[row["prime"]].append(row)

    prime_profiles = [
        profile_prime(prime, profiles[prime], grouped.get(prime, []))
        for prime in SINGLE_HIT_PRIMES
    ]
    all_rows = [row for profile in prime_profiles for row in profile["boundary_rows"]]
    boundary_states = {
        (int(row["prime"]), int(row["a"]), int(row["s"]), int(row["R"]))
        for row in all_rows
    }
    return {
        "arithmetic": (
            "from each subgroup-visible shared-layer F boundary, enumerate the "
            "established fixed-s factor transfers, admissible changing-s transfers, "
            "and both directions of coordinate swaps; test directed reachability "
            "to the exact full-spectrum hit states and record undirected components"
        ),
        "scope_note": (
            "This is a finite audit of three already verified local source operations "
            "on the five boundary states carrying 16 subgroup-visible pullback classes. "
            "Failure of directed reachability only rules out these local transfers; it "
            "does not refute a different source construction or prove the mixed selector."
        ),
        "pullback_input": pullback_path.name,
        "pullback_input_sha256": file_sha256(pullback_path),
        "spectrum_input": spectrum_path.name,
        "spectrum_input_sha256": file_sha256(spectrum_path),
        "prime_count": len(prime_profiles),
        "source_state_count": sum(
            int(profile["source_state_count"]) for profile in prime_profiles
        ),
        "known_directed_edge_count": sum(
            int(profile["known_directed_edge_count"]) for profile in prime_profiles
        ),
        "boundary_row_count": len(all_rows),
        "boundary_state_count": len(boundary_states),
        "boundary_rows_reaching_hit_count": sum(
            int(row["directed_reaches_hit"]) for row in all_rows
        ),
        "boundary_states_reaching_hit_count": len(
            {
                (int(row["prime"]), int(row["a"]), int(row["s"]), int(row["R"]))
                for row in all_rows
                if row["directed_reaches_hit"]
            }
        ),
        "boundary_direct_hit_edge_count": sum(
            int(row["direct_hit_edge_count"]) for row in all_rows
        ),
        "boundary_states_in_hit_undirected_component_count": len(
            {
                (int(row["prime"]), int(row["a"]), int(row["s"]), int(row["R"]))
                for row in all_rows
                if row["undirected_component_contains_hit"]
            }
        ),
        "profiles": prime_profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pullback-input", type=Path, default=PULLBACK_INPUT)
    parser.add_argument("--spectrum-input", type=Path, default=SPECTRUM_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.pullback_input, args.spectrum_input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in result.items() if key != "profiles"},
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
