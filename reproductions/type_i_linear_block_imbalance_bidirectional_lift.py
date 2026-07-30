#!/usr/bin/env python3
"""Audit odd-distance lifts from all unique bidirectional dyadic terminals."""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-bidirectional-results.json"
ODD_DISTANCE = ROOT / "reproductions" / "type_i_short_relation_odd_distance_even_source.py"
OUTPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-bidirectional-lift-results.json"
EXPECTED_INPUT_SHA256 = "83af514607e7ab111a3d1905e823bcfe7658f81282de5ab715aad81b2dd09c4f"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


odd_distance = load_module("bidirectional_odd_distance", ODD_DISTANCE)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unique_candidates(payload: dict[str, object]) -> list[dict[str, object]]:
    candidates: dict[tuple[int, int, int, int], dict[str, object]] = {}
    row_count = 0
    for record in payload["records"]:
        for terminal in record["terminal_candidates"]:
            row_count += 1
            key = (
                int(record["prime"]),
                int(record["R"]),
                int(terminal["source"]),
                int(terminal["E"]),
            )
            candidate = {
                "prime": int(record["prime"]),
                "R": int(record["R"]),
                "source": int(terminal["source"]),
                "E": int(terminal["E"]),
                "orientation": str(terminal["orientation"]),
                "J": int(terminal["J"]),
            }
            previous = candidates.get(key)
            if previous is None:
                candidates[key] = candidate
            elif (previous["orientation"], previous["J"]) != (
                candidate["orientation"],
                candidate["J"],
            ):
                previous["orientation"] = "both"
                previous["J"] = min(int(previous["J"]), int(candidate["J"]))
    result = list(candidates.values())
    result.sort(key=lambda item: (int(item["prime"]), int(item["R"]), int(item["E"])))
    for index, candidate in enumerate(result):
        candidate["candidate_index"] = index
    payload["_candidate_row_count"] = row_count
    return result


def run() -> dict[str, object]:
    if EXPECTED_INPUT_SHA256 == "CHANGE_ME":
        raise AssertionError("input hash was not frozen")
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the bidirectional terminal input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    candidates = unique_candidates(payload)
    parameters: list[dict[str, object]] = []
    hits: list[dict[str, object]] = []
    distance_counts: Counter[int] = Counter()
    orientation_parameter_counts: Counter[str] = Counter()
    prime_hit_counts: Counter[int] = Counter()
    for candidate in candidates:
        local_parameters, local_hits = odd_distance.audit_record(
            int(candidate["candidate_index"]),
            {"prime": int(candidate["prime"]), "n": int(candidate["source"])},
        )
        for item in local_parameters:
            enriched = {
                **item,
                "candidate_R": int(candidate["R"]),
                "candidate_E": int(candidate["E"]),
                "orientation": str(candidate["orientation"]),
                "J": int(candidate["J"]),
            }
            parameters.append(enriched)
            distance_counts[int(item["distance"])] += 1
            orientation_parameter_counts[str(candidate["orientation"])] += 1
        for item in local_hits:
            hits.append(
                {
                    **item,
                    "candidate_R": int(candidate["R"]),
                    "candidate_E": int(candidate["E"]),
                    "orientation": str(candidate["orientation"]),
                    "J": int(candidate["J"]),
                }
            )
            prime_hit_counts[int(item["prime"])] += 1
    return {
        "arithmetic": (
            "Deduplicate every forward and reverse dyadic terminal by (p,R,source,E), "
            "then apply the exact odd-distance even-source Type I lift audit."
        ),
        "scope_note": (
            "Finite audit only. It tests the odd-distance lift family from all unique "
            "bidirectional dyadic terminals; a miss does not rule out another source, "
            "distance, or lift family."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "candidate_row_count": int(payload["_candidate_row_count"]),
        "unique_terminal_count": len(candidates),
        "parameter_count": len(parameters),
        "hit_count": len(hits),
        "hit_state_count": len(
            {(int(item["prime"]), int(item["source"])) for item in hits}
        ),
        "hit_prime_count": len(prime_hit_counts),
        "hit_prime_counts": {
            str(prime): int(count)
            for prime, count in sorted(prime_hit_counts.items())
        },
        "parameter_orientation_counts": {
            key: int(value)
            for key, value in sorted(orientation_parameter_counts.items())
        },
        "distance_histogram": {
            str(distance): int(count)
            for distance, count in sorted(distance_counts.items())
        },
        "hit_primes": sorted(prime_hit_counts),
        "parameters": parameters,
        "hits": hits,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "candidate_row_count",
                    "unique_terminal_count",
                    "parameter_count",
                    "hit_count",
                    "hit_state_count",
                    "hit_prime_count",
                    "hit_primes",
                    "parameter_orientation_counts",
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
