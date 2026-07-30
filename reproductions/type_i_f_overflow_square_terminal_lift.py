#!/usr/bin/env python3
"""Audit odd-distance Type I lifts from multi-support square terminals."""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
CROSS_INPUT = ROOT / "reproductions" / "type-i-f-full-cross-color-pair-capacity-results.json"
SUPPORT_INPUT = ROOT / "reproductions" / "type-i-f-overflow-support-boundary-results.json"
CAPACITY_SCRIPT = ROOT / "reproductions" / "type_i_f_same_color_subset_capacity.py"
CROSS_SCRIPT = ROOT / "reproductions" / "type_i_f_full_cross_color_pair_capacity.py"
ODD_DISTANCE_SCRIPT = ROOT / "reproductions" / "type_i_short_relation_odd_distance_even_source.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-overflow-square-terminal-lift-results.json"

EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_CROSS_SHA256 = "c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5"
EXPECTED_SUPPORT_SHA256 = "93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


capacity = load_module("overflow_square_capacity", CAPACITY_SCRIPT)
cross = load_module("overflow_square_cross", CROSS_SCRIPT)
odd_distance = load_module("overflow_square_odd_distance", ODD_DISTANCE_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> dict[str, object]:
    for path, expected, label in (
        (FOURIER_INPUT, EXPECTED_FOURIER_SHA256, "Fourier"),
        (CROSS_INPUT, EXPECTED_CROSS_SHA256, "cross-color"),
        (SUPPORT_INPUT, EXPECTED_SUPPORT_SHA256, "support-boundary"),
    ):
        if sha256(path) != expected:
            raise AssertionError(f"the {label} input changed")

    fourier = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    cross_payload = json.loads(CROSS_INPUT.read_text(encoding="utf-8"))
    support_payload = json.loads(SUPPORT_INPUT.read_text(encoding="utf-8"))
    Fourier_by_key = {
        (int(record["prime"]), int(record["R"])): dict(record)
        for record in fourier["records"]
    }
    support_by_key = {
        (int(record["prime"]), int(record["R"])): dict(record)
        for record in support_payload["records"]
        if record.get("within_radius_cap")
    }
    source_cache: dict[int, dict[int, list[tuple[int, int]]]] = {}
    candidates: dict[tuple[int, int, int, int], dict[str, object]] = {}
    unresolved = [dict(record) for record in cross_payload["unresolved_records"]]
    support_record_count = 0
    assignment_count = 0

    for index, record in enumerate(unresolved, start=1):
        key = (int(record["prime"]), int(record["R"]))
        if key not in support_by_key:
            continue
        Fourier = Fourier_by_key[key]
        if Fourier["status"] != "bounded_fourier_certificate":
            raise AssertionError("support record is not threshold-met")
        prime = key[0]
        if prime not in source_cache:
            _bound, source_cache[prime] = capacity.source.enumerate_linear_source_states(prime)
        support_record_count += 1
        for assignment in cross.cross_color_assignments(Fourier, source_cache[prime]):
            assignment_count += 1
            modulus = key[1]
            a, s = int(assignment["a"]), int(assignment["s"])
            U = s * modulus + 1
            V = a * modulus + 1
            X = min(U, V)
            E = X * X
            if U < V and V % 2 == 1:
                raise AssertionError("square terminal assignment is an exact mixed-parity obstruction")
            K = int(Fourier["K"])
            if (4 * K * K) % E:
                raise AssertionError("smaller-block square is not a divisor")
            source, remainder = divmod(U * V - E, modulus)
            if remainder or not (0 < source < prime):
                raise AssertionError("invalid smaller-block square source")
            if E % modulus != 1 or E <= 1 or E >= 4 * K:
                raise AssertionError("invalid smaller-block square terminal")
            if (source * K) % E or source % 2 or E % 2:
                raise AssertionError("square terminal is not an even source certificate")
            candidate_key = (prime, modulus, source, E)
            candidates.setdefault(
                candidate_key,
                {
                    "prime": prime,
                    "R": modulus,
                    "source": source,
                    "E": E,
                    "a": a,
                    "s": s,
                    "q_a": int(assignment["q_a"]),
                    "q_s": int(assignment["q_s"]),
                    "witness_radius": int(support_by_key[key]["witness_radius"]),
                },
            )
        if index % 50 == 0:
            print(f"processed {index}/{len(unresolved)}", file=sys.stderr)

    parameters: list[dict[str, object]] = []
    hits: list[dict[str, object]] = []
    distance_counts: Counter[int] = Counter()
    hit_prime_counts: Counter[int] = Counter()
    ordered_candidates = sorted(
        candidates.values(),
        key=lambda item: (
            int(item["prime"]),
            int(item["R"]),
            int(item["source"]),
            int(item["E"]),
        ),
    )
    for index, candidate in enumerate(ordered_candidates):
        local_parameters, local_hits = odd_distance.audit_record(
            index,
            {"prime": int(candidate["prime"]), "n": int(candidate["source"])},
        )
        for item in local_parameters:
            parameters.append(
                {
                    **item,
                    "candidate_R": int(candidate["R"]),
                    "candidate_E": int(candidate["E"]),
                    "candidate_a": int(candidate["a"]),
                    "candidate_s": int(candidate["s"]),
                    "candidate_q_a": int(candidate["q_a"]),
                    "candidate_q_s": int(candidate["q_s"]),
                    "witness_radius": int(candidate["witness_radius"]),
                }
            )
            distance_counts[int(item["distance"])] += 1
        for item in local_hits:
            hits.append(
                {
                    **item,
                    "candidate_R": int(candidate["R"]),
                    "candidate_E": int(candidate["E"]),
                    "candidate_a": int(candidate["a"]),
                    "candidate_s": int(candidate["s"]),
                    "candidate_q_a": int(candidate["q_a"]),
                    "candidate_q_s": int(candidate["q_s"]),
                    "witness_radius": int(candidate["witness_radius"]),
                }
            )
            hit_prime_counts[int(item["prime"])] += 1

    return {
        "arithmetic": (
            "For every split-color overflow witness with a valid smaller-block square terminal, "
            "deduplicate (p,R,source,E) and enumerate the complete odd-distance even-source "
            "Type I lift family from the strictly smaller even source."
        ),
        "scope_note": (
            "Finite targeted lift audit only. It covers 253 witness states and their 506 "
            "deterministic cross-color assignments. A miss does not rule out another source, "
            "distance, target divisor, or lift family; the F state that generated a square "
            "terminal may still lack its target divisor."
        ),
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "cross_input": CROSS_INPUT.name,
        "cross_input_sha256": sha256(CROSS_INPUT),
        "support_input": SUPPORT_INPUT.name,
        "support_input_sha256": sha256(SUPPORT_INPUT),
        "unresolved_record_count": len(unresolved),
        "support_record_count": support_record_count,
        "assignment_count": assignment_count,
        "unique_terminal_count": len(ordered_candidates),
        "parameter_count": len(parameters),
        "tail_candidate_count": len(hits),
        "hit_state_count": len({(int(item["prime"]), int(item["source"])) for item in hits}),
        "hit_prime_count": len(hit_prime_counts),
        "hit_primes": sorted(hit_prime_counts),
        "hit_prime_counts": {
            str(prime): int(count) for prime, count in sorted(hit_prime_counts.items())
        },
        "candidates": ordered_candidates,
        "distance_histogram": {
            str(distance): int(count) for distance, count in sorted(distance_counts.items())
        },
        "parameters": parameters,
        "hits": hits,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "unresolved_record_count",
                    "support_record_count",
                    "assignment_count",
                    "unique_terminal_count",
                    "parameter_count",
                    "tail_candidate_count",
                    "hit_state_count",
                    "hit_prime_count",
                    "hit_primes",
                    "distance_histogram",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
