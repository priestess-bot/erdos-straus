#!/usr/bin/env python3
"""Audit odd-distance lifts from canonical block-imbalance terminals."""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-trichotomy-results.json"
ODD_DISTANCE = ROOT / "reproductions" / "type_i_short_relation_odd_distance_even_source.py"
OUTPUT = ROOT / "reproductions" / "type-i-linear-block-imbalance-lift-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


odd_distance = load_module("block_imbalance_odd_distance", ODD_DISTANCE)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> dict[str, object]:
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records = [
        record
        for record in payload["records"]
        if record["classification"] in {"kernel_relation", "dyadic_terminal"}
    ]
    parameters: list[dict[str, int]] = []
    hits: list[dict[str, int]] = []
    prime_hit_counts: Counter[int] = Counter()
    distance_counts: Counter[int] = Counter()
    for index, record in enumerate(records):
        local_parameters, local_hits = odd_distance.audit_record(
            index,
            {"prime": int(record["prime"]), "n": int(record["terminal"]["source"])},
        )
        parameters.extend(local_parameters)
        hits.extend(local_hits)
        distance_counts.update(int(item["distance"]) for item in local_parameters)
        prime_hit_counts.update(int(item["prime"]) for item in local_hits)
    return {
        "arithmetic": (
            "For every canonical kernel or generalized-dyadic terminal from the complete "
            "linear spectrum, apply the exact odd-distance even-source Type I lift audit."
        ),
        "scope_note": (
            "Finite audit only. It tests one canonical terminal per qualifying linear state; "
            "a miss does not rule out another terminal, distance, or lift family."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "terminal_state_count": len(records),
        "parameter_count": len(parameters),
        "hit_count": len(hits),
        "hit_state_count": len({(int(item["prime"]), int(item["source"])) for item in hits}),
        "hit_prime_count": len(prime_hit_counts),
        "hit_prime_counts": {str(prime): int(count) for prime, count in sorted(prime_hit_counts.items())},
        "distance_histogram": {str(distance): int(count) for distance, count in sorted(distance_counts.items())},
        "parameters": parameters,
        "hits": hits,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "terminal_state_count", "parameter_count", "hit_count", "hit_state_count",
        "hit_prime_count", "hit_prime_counts", "distance_histogram",
    )}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
