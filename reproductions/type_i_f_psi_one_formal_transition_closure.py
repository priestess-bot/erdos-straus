#!/usr/bin/env python3
"""Reproduce the ranked formal selector on the frozen Psi_0=1 family.

The q-adic pair transitions in this file are analysis evidence, not legal
Erdos-Straus descent edges.  Every reported terminal is independently rebuilt
and checked as an exact unit-fraction identity for the original prime.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable, Literal

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-psi-one-nearest-fiber-escape-boundary-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-f-psi-one-formal-transition-closure-results.json"
)
EXPECTED_INPUT_SHA256 = (
    "a7babc394423104647090a6bdae4255ff8cc73d2bb06dae6a0e3e1aefce4b2d2"
)
EXPECTED_STATE_COUNT = 55
EXPECTED_PHYSICAL_START_COUNT = 140

Node = tuple[int, int, int]
RankMode = Literal["min", "max"]
_FACTORIZATION_CACHE: dict[int, dict[int, int]] = {}
_DIVISOR_CACHE: dict[int, tuple[int, ...]] = {}
_GAP_CERTIFICATE_CACHE: dict[tuple[int, int], dict[str, object] | None] = {}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def histogram(values: Iterable[int]) -> dict[str, int]:
    return {
        str(value): count
        for value, count in sorted(Counter(values).items())
    }


def factorization(value: int) -> dict[int, int]:
    if value <= 0:
        raise ValueError("factorization requires a positive integer")
    if value not in _FACTORIZATION_CACHE:
        factors = {int(q): int(e) for q, e in sympy.factorint(value).items()}
        if math.prod(q**e for q, e in factors.items()) != value:
            raise AssertionError("factorization did not reconstruct its input")
        _FACTORIZATION_CACHE[value] = dict(sorted(factors.items()))
    return _FACTORIZATION_CACHE[value]


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    values = [1]
    for q, exponent in sorted(factors.items()):
        values = [
            value * q**power
            for value in values
            for power in range(exponent + 1)
        ]
    return sorted(values)


def divisors(value: int) -> list[int]:
    if value not in _DIVISOR_CACHE:
        _DIVISOR_CACHE[value] = tuple(
            divisors_from_factorization(factorization(value))
        )
    return list(_DIVISOR_CACHE[value])


def square_divisors(value: int) -> list[int]:
    return divisors_from_factorization(
        {q: 2 * exponent for q, exponent in factorization(value).items()}
    )


def canonical_node(left: int, right: int, m: int, modulus: int) -> Node:
    if min(left, right, m) <= 0:
        raise AssertionError("formal coordinates must be positive")
    if math.gcd(left, right) != 1 or left + right != modulus * m:
        raise AssertionError("formal target-pair invariant failed")
    return min(left, right), max(left, right), m


def node_id(node: Node) -> str:
    return f"{node[0]}:{node[1]}:{node[2]}"


def ratio_from_exponents(
    primes: list[int], exponents: tuple[int, ...]
) -> tuple[int, int]:
    numerator = math.prod(
        q ** max(exponent, 0) for q, exponent in zip(primes, exponents)
    )
    denominator = math.prod(
        q ** max(-exponent, 0) for q, exponent in zip(primes, exponents)
    )
    if math.gcd(numerator, denominator) != 1:
        raise AssertionError("signed exponent ratio was not reduced")
    return numerator, denominator


def raw_transitions(
    node: Node, modulus: int, K_bounds: dict[int, int]
) -> list[dict[str, object]]:
    """Enumerate every prime whose height in either coordinate exceeds v_q(K)."""
    smaller, larger, m = node
    rows: list[dict[str, object]] = []
    for side, (selected, other) in (
        ("smaller", (smaller, larger)),
        ("larger", (larger, smaller)),
    ):
        for q, height in factorization(selected).items():
            K_height = K_bounds.get(q, 0)
            if height <= K_height:
                continue
            shift = (-m) % q
            if not 1 <= shift < q or math.gcd(q, modulus * m * other) != 1:
                raise AssertionError("excess prime did not give a unit shift")
            selected_0 = selected // q
            other_0 = (other + modulus * shift) // q
            m_0 = (m + shift) // q
            common = math.gcd(selected_0, other_0)
            if m_0 % common:
                raise AssertionError("post-transition gcd did not divide m")
            destination = canonical_node(
                selected_0 // common,
                other_0 // common,
                m_0 // common,
                modulus,
            )
            if m > 1 and not destination[2] < m:
                raise AssertionError("an m>1 transition failed to lower m")
            if m == 1 and destination[2] != 1:
                raise AssertionError("an m=1 transition changed m")
            rows.append(
                {
                    "q": q,
                    "q_in_K_support": q in K_bounds,
                    "source_side": side,
                    "destination": destination,
                    "gcd_reduction": common,
                    "edge_semantics": "analysis_evidence_not_verified_edge",
                }
            )
    return sorted(
        rows,
        key=lambda row: (
            int(row["q"]),
            str(row["source_side"]),
            row["destination"],
        ),
    )


def rank(node: Node, mode: RankMode) -> tuple[int, int]:
    if mode == "min":
        return node[2], node[0]
    if mode == "max":
        return node[2], node[1]
    raise ValueError(f"unknown rank mode: {mode}")


def verify_solution(prime: int, solution: tuple[int, int, int]) -> None:
    x, y, z = solution
    if min(solution) <= 0 or Fraction(1, x) + Fraction(1, y) + Fraction(1, z) != Fraction(4, prime):
        raise AssertionError("terminal did not verify the Erdos-Straus identity")


def type_i_certificate(
    prime: int, gap: int, x: int, divisor: int
) -> dict[str, object] | None:
    if x * x % divisor or (prime * x + divisor) % gap:
        return None
    y = (prime * x + divisor) // gap
    numerator = prime * x * y
    if numerator % divisor:
        raise AssertionError("Type I third denominator was not integral")
    solution = (x, y, numerator // divisor)
    verify_solution(prime, solution)
    return {
        "type": "Type_I",
        "gap": gap,
        "first_denominator": x,
        "divisor": divisor,
        "solution": list(solution),
        "certificate_semantics": "verified_direct_terminal",
    }


def type_ii_certificate(
    prime: int, gap: int, x: int, divisor: int
) -> dict[str, object] | None:
    if divisor > x or x * x % divisor or (x + divisor) % gap:
        return None
    y = prime * (x + divisor) // gap
    numerator = x * y
    if numerator % divisor:
        raise AssertionError("Type II third denominator was not integral")
    solution = (x, y, numerator // divisor)
    verify_solution(prime, solution)
    return {
        "type": "Type_II",
        "gap": gap,
        "first_denominator": x,
        "divisor": divisor,
        "solution": list(solution),
        "certificate_semantics": "verified_direct_terminal",
    }


def exact_gap_certificate(prime: int, gap: int) -> dict[str, object] | None:
    key = (prime, gap)
    if key in _GAP_CERTIFICATE_CACHE:
        return _GAP_CERTIFICATE_CACHE[key]
    if not (3 <= gap <= prime - 2 and gap % 4 == 3):
        _GAP_CERTIFICATE_CACHE[key] = None
        return None
    x = (prime + gap) // 4
    if 4 * x != prime + gap:
        raise AssertionError("gap did not give an integral first denominator")
    candidates = square_divisors(x)
    for divisor in candidates:
        certificate = type_i_certificate(prime, gap, x, divisor)
        if certificate is not None:
            certificate["complete_divisor_space_size"] = len(candidates)
            _GAP_CERTIFICATE_CACHE[key] = certificate
            return certificate
    for divisor in candidates:
        certificate = type_ii_certificate(prime, gap, x, divisor)
        if certificate is not None:
            certificate["complete_divisor_space_size"] = len(candidates)
            _GAP_CERTIFICATE_CACHE[key] = certificate
            return certificate
    _GAP_CERTIFICATE_CACHE[key] = None
    return None


def centered_type_i_hits(
    prime: int, modulus: int, K: int
) -> tuple[int, list[dict[str, object]]]:
    candidates = square_divisors(K)
    hits: list[dict[str, object]] = []
    for divisor in candidates:
        if divisor >= K or (divisor + K) % modulus:
            continue
        gap_numerator = 4 * divisor + 1
        if gap_numerator % modulus:
            raise AssertionError("centered hit did not produce an integral gap")
        gap = gap_numerator // modulus
        if not (3 <= gap <= prime - 2 and gap % 4 == 3):
            continue
        x = (prime + gap) // 4
        common = math.gcd(divisor, K)
        B = divisor // common
        if common % B:
            raise AssertionError("centered divisor did not have B^2 C form")
        C = common // B
        H = K // common
        if (B + H) % modulus:
            raise AssertionError("centered divisor did not reconstruct A")
        A = (B + H) // modulus
        direct_divisor = A * A * C
        certificate = type_i_certificate(prime, gap, x, direct_divisor)
        if certificate is None:
            raise AssertionError("centered divisor did not reconstruct Type I")
        hits.append(
            {
                "state_modulus": modulus,
                "state_K": K,
                "centered_divisor": divisor,
                "normal_form": {"A": A, "B": B, "C": C, "H": H},
                **certificate,
            }
        )
    return len(candidates), hits


def external_gap_candidates(
    nodes: set[Node], prime: int, K: int
) -> tuple[list[int], dict[int, dict[str, object]]]:
    origins: dict[int, dict[str, object]] = {}
    for node in sorted(nodes):
        for side, value in (("smaller", node[0]), ("larger", node[1])):
            for gap in divisors(value):
                if (
                    gap % 4 != 3
                    or not 3 <= gap <= prime - 2
                    or gap // math.gcd(gap, K) <= 1
                ):
                    continue
                origins.setdefault(
                    gap,
                    {
                        "node": node_id(node),
                        "side": side,
                        "side_value": value,
                        "external_part": gap // math.gcd(gap, K),
                    },
                )
    return sorted(origins), origins


def ranked_state_profile(
    prime: int,
    modulus: int,
    K: int,
    K_bounds: dict[int, int],
    starts: list[Node],
    mode: RankMode,
) -> dict[str, object]:
    visited: set[Node] = set()
    accepted_edges: list[tuple[Node, dict[str, object]]] = []
    rejected_edges: list[tuple[Node, dict[str, object]]] = []
    frontier = list(starts)
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        for edge in raw_transitions(node, modulus, K_bounds):
            destination = edge["destination"]
            if rank(destination, mode) < rank(node, mode):
                accepted_edges.append((node, edge))
                if destination not in visited:
                    frontier.append(destination)
            else:
                rejected_edges.append((node, edge))
        if len(visited) > 100_000:
            raise AssertionError("ranked closure exceeded its safety bound")

    rejected_successors = {
        edge["destination"] for _source, edge in rejected_edges
    } - visited
    terminal_scope = visited | rejected_successors
    gaps, origins = external_gap_candidates(terminal_scope, prime, K)
    certificates: list[dict[str, object]] = []
    for gap in gaps:
        certificate = exact_gap_certificate(prime, gap)
        if certificate is not None:
            certificates.append(
                {"external_gap": gap, "origin": origins[gap], **certificate}
            )

    for source, edge in accepted_edges:
        if not rank(edge["destination"], mode) < rank(source, mode):
            raise AssertionError("accepted edge did not lower its declared rank")
    return {
        "mode": f"lexicographic_m_{mode}_coordinate",
        "rank_definition": f"(m,{mode}(A,B))",
        "visited_node_count": len(visited),
        "accepted_edge_count": len(accepted_edges),
        "rejected_edge_count": len(rejected_edges),
        "one_step_rejected_successor_count": len(rejected_successors),
        "terminal_scope_node_count": len(terminal_scope),
        "external_gap_candidate_count": len(gaps),
        "external_gap_candidates": gaps,
        "first_verified_certificate": certificates[0] if certificates else None,
        "verified_certificate_count": len(certificates),
        "hit": bool(certificates),
        "edge_semantics": "analysis_evidence_not_verified_edge",
        "lookahead_semantics": (
            "rejected successors are checked only for a direct terminal and are never recursed"
        ),
    }


def K_support_closure(
    state_inputs: list[dict[str, object]]
) -> dict[str, object]:
    node_count = 0
    edge_count = 0
    sink_count = 0
    non_strict_m_edges = 0
    maximum_depth = 0
    for state in state_inputs:
        modulus = int(state["R"])
        bounds = state["K_bounds"]
        visited: set[Node] = set()
        adjacency: dict[Node, list[Node]] = {}
        frontier = list(state["starts"])
        while frontier:
            node = frontier.pop()
            if node in visited:
                continue
            visited.add(node)
            destinations = []
            for edge in raw_transitions(node, modulus, bounds):
                if not edge["q_in_K_support"]:
                    continue
                destination = edge["destination"]
                destinations.append(destination)
                non_strict_m_edges += int(destination[2] >= node[2])
                if destination not in visited:
                    frontier.append(destination)
            adjacency[node] = destinations
        memo: dict[Node, int] = {}

        def depth(node: Node) -> int:
            if node not in memo:
                memo[node] = 0 if not adjacency[node] else 1 + max(
                    depth(destination) for destination in adjacency[node]
                )
            return memo[node]

        maximum_depth = max(
            maximum_depth,
            max((depth(start) for start in state["starts"]), default=0),
        )
        node_count += len(visited)
        edge_count += sum(len(values) for values in adjacency.values())
        sink_count += sum(not values for values in adjacency.values())
    result = {
        "node_count": node_count,
        "edge_count": edge_count,
        "sink_count": sink_count,
        "non_strict_m_edge_count": non_strict_m_edges,
        "maximum_track_length": maximum_depth,
    }
    expected = {
        "node_count": 282,
        "edge_count": 153,
        "sink_count": 129,
        "non_strict_m_edge_count": 0,
        "maximum_track_length": 5,
    }
    if result != expected:
        raise AssertionError(f"K-support baseline changed: {result}")
    return result


def reconstruct_inputs(source: dict[str, object]) -> list[dict[str, object]]:
    state_inputs: list[dict[str, object]] = []
    physical_start_count = 0
    for record in source["records"]:
        prime = int(record["prime"])
        modulus = int(record["R"])
        K = int(record["K"])
        K_bounds = {int(q): int(e) for q, e in record["factorization"]}
        primes = list(K_bounds)
        if (
            prime % 24 != 1
            or not sympy.isprime(prime)
            or prime * modulus + 1 != 4 * K
            or math.prod(q**e for q, e in K_bounds.items()) != K
        ):
            raise AssertionError("frozen state arithmetic changed")
        starts: list[Node] = []
        for migration in record["migrations"]:
            exponents = tuple(int(value) for value in migration["positive_exponents"])
            left, right = ratio_from_exponents(primes, exponents)
            if (left + right) % modulus:
                raise AssertionError("frozen witness left the target fiber")
            start = canonical_node(
                left, right, (left + right) // modulus, modulus
            )
            starts.append(start)
        if len(starts) != int(record["positive_witness_count"]):
            raise AssertionError("per-state physical start count changed")
        physical_start_count += len(starts)
        state_inputs.append(
            {
                "prime": prime,
                "R": modulus,
                "K": K,
                "K_bounds": K_bounds,
                "starts": starts,
            }
        )
    if len(state_inputs) != EXPECTED_STATE_COUNT or physical_start_count != EXPECTED_PHYSICAL_START_COUNT:
        raise AssertionError("frozen family cardinality changed")
    return state_inputs


def run() -> dict[str, object]:
    input_hash = sha256(INPUT)
    if input_hash != EXPECTED_INPUT_SHA256:
        raise AssertionError(f"frozen input hash changed: {input_hash}")
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    state_inputs = reconstruct_inputs(source)
    K_support = K_support_closure(state_inputs)

    original_centered_hit_count = 0
    records: list[dict[str, object]] = []
    totals: dict[str, Counter[str]] = {"min": Counter(), "max": Counter()}
    for state in state_inputs:
        prime = int(state["prime"])
        modulus = int(state["R"])
        K = int(state["K"])
        centered_space, centered_hits = centered_type_i_hits(prime, modulus, K)
        original_centered_hit_count += bool(centered_hits)
        modes: dict[str, dict[str, object]] = {}
        for mode in ("min", "max"):
            profile = ranked_state_profile(
                prime,
                modulus,
                K,
                state["K_bounds"],
                state["starts"],
                mode,
            )
            modes[mode] = profile
            for field in (
                "visited_node_count",
                "accepted_edge_count",
                "rejected_edge_count",
                "one_step_rejected_successor_count",
                "terminal_scope_node_count",
                "external_gap_candidate_count",
            ):
                totals[mode][field] += int(profile[field])
            totals[mode]["hit_state_count"] += int(profile["hit"])
        records.append(
            {
                "prime": prime,
                "R": modulus,
                "K": K,
                "physical_start_count": len(state["starts"]),
                "original_centered_scan_space": centered_space,
                "original_centered_hit_count": len(centered_hits),
                "ranked_modes": modes,
                "dual_rank_hit": bool(modes["min"]["hit"] or modes["max"]["hit"]),
            }
        )

    residuals = [
        record for record in records if not bool(record["dual_rank_hit"])
    ]
    cross_chart_profiles: list[dict[str, object]] = []
    for record in residuals:
        prime = int(record["prime"])
        candidate_moduli = sorted(
            set(record["ranked_modes"]["min"]["external_gap_candidates"])
            | set(record["ranked_modes"]["max"]["external_gap_candidates"])
        )
        scans: list[dict[str, object]] = []
        for modulus in candidate_moduli:
            K = (prime * modulus + 1) // 4
            if 4 * K != prime * modulus + 1:
                raise AssertionError("external gap was not a legal new modulus")
            search_space, hits = centered_type_i_hits(prime, modulus, K)
            scans.append(
                {
                    "new_modulus": modulus,
                    "new_K": K,
                    "factorization": [[q, e] for q, e in factorization(K).items()],
                    "centered_search_space": search_space,
                    "hits": hits,
                }
            )
        cross_chart_profiles.append(
            {
                "prime": prime,
                "original_R": int(record["R"]),
                "candidate_moduli": candidate_moduli,
                "scans": scans,
                "hit": any(scan["hits"] for scan in scans),
            }
        )

    summary = {
        "state_count": len(records),
        "physical_start_count": sum(record["physical_start_count"] for record in records),
        "original_state_level_centered_hit_count": original_centered_hit_count,
        "K_support_baseline": K_support,
        "min_rank": dict(totals["min"]),
        "max_rank": dict(totals["max"]),
        "dual_rank_hit_state_count": sum(record["dual_rank_hit"] for record in records),
        "dual_rank_residuals": [
            [int(record["prime"]), int(record["R"])] for record in residuals
        ],
        "cross_chart_hit_state_count": sum(profile["hit"] for profile in cross_chart_profiles),
        "final_verified_state_count": sum(record["dual_rank_hit"] for record in records)
        + sum(profile["hit"] for profile in cross_chart_profiles),
    }
    expected = {
        "original_state_level_centered_hit_count": 0,
        "min_hit": 53,
        "max_hit": 52,
        "dual_hit": 54,
        "residuals": [[16_002_529, 27]],
        "cross_hit": 1,
        "final": 55,
    }
    actual = {
        "original_state_level_centered_hit_count": summary[
            "original_state_level_centered_hit_count"
        ],
        "min_hit": summary["min_rank"]["hit_state_count"],
        "max_hit": summary["max_rank"]["hit_state_count"],
        "dual_hit": summary["dual_rank_hit_state_count"],
        "residuals": summary["dual_rank_residuals"],
        "cross_hit": summary["cross_chart_hit_state_count"],
        "final": summary["final_verified_state_count"],
    }
    if actual != expected:
        raise AssertionError(f"ranked-selector result changed: {actual}")

    residual_hits = [
        (scan["new_modulus"], scan["hits"][0]["centered_divisor"])
        for profile in cross_chart_profiles
        for scan in profile["scans"]
        if scan["hits"]
    ]
    if residual_hits != [(11, 657), (47, 5299)]:
        raise AssertionError(f"cross-chart hit set changed: {residual_hits}")

    return {
        "arithmetic": (
            "Freeze all 55 Psi_0=1 states; enumerate all excess-prime formal transitions; "
            "run the two finite DAGs defined by lexicographic (m,min(A,B)) and "
            "(m,max(A,B)); inspect rejected one-step successors without recursing; "
            "exhaust all external divisors Q congruent to 3 mod 4 as exact Type I/II "
            "gaps; then test the sole residual by using the same Q values as new "
            "centered Type I moduli."
        ),
        "scope_note": (
            "This is exact finite evidence for the frozen 55-state Psi_0=1 family. "
            "Formal transitions remain analysis evidence and do not satisfy the legal "
            "state/lift contract. Direct terminal certificates are independently "
            "verified, but the experiment is not a universal selector theorem."
        ),
        "input": {"path": INPUT.name, "sha256": input_hash},
        "script_sha256": sha256(Path(__file__)),
        "summary": summary,
        "cross_chart_residual_profiles": cross_chart_profiles,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(
        json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
