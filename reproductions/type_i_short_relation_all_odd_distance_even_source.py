#!/usr/bin/env python3
"""Audit the odd-distance branch on every short relation, not only the selected one."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-short-relation-even-terminal-results.json"
ODD_DISTANCE_SCRIPT = ROOT / "reproductions" / "type_i_short_relation_odd_distance_even_source.py"
LATTICE_SCRIPT = ROOT / "reproductions" / "type_i_f_relation_lattice_certificate.py"
OUTPUT = ROOT / "reproductions" / "type-i-short-relation-all-odd-distance-even-source-results.json"
EXPECTED_INPUT_SHA256 = "41bdb1c1c9c724731db27b81cbd1a8e6d9a7cc298028b16370338a75df01d368"
EXPECTED_RECORD_COUNT = 291


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


odd_distance = load_module("all_relation_odd_distance", ODD_DISTANCE_SCRIPT)
lattice = load_module("all_relation_lattice", LATTICE_SCRIPT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relation_holds(
    relation: tuple[int, ...], generator_logs: list[list[int]], orders: list[int]
) -> bool:
    return all(
        sum(relation[index] * int(generator_logs[index][component]) for index in range(len(relation)))
        % order
        == 0
        for component, order in enumerate(orders)
    )


def rational_ratio(factors: list[tuple[int, int]], relation: tuple[int, ...]):
    ratio = Fraction(1, 1)
    for (prime, _exponent), value in zip(factors, relation):
        ratio *= prime**value if value >= 0 else Fraction(1, prime ** (-value))
    return ratio


def terminal_from_relation(
    record: dict[str, object], relation: tuple[int, ...]
) -> tuple[int, int, tuple[int, ...]]:
    prime = int(record["prime"])
    modulus = int(record["R"])
    K = int(record["K"])
    factors = [(int(q), int(exponent)) for q, exponent in record["factorization"]]
    ratio = rational_ratio(factors, relation)
    if ratio == 1:
        raise AssertionError("a nonzero relation had rational ratio one")
    if ratio > 1:
        relation = tuple(-value for value in relation)
        ratio = 1 / ratio
    exponents = [exponent + value for (_prime, exponent), value in zip(factors, relation)]
    if any(value < 0 or value > 2 * exponent for value, (_prime, exponent) in zip(exponents, factors)):
        raise AssertionError("oriented relation left K^2")
    U = math.prod(q**exponent for (q, _old), exponent in zip(factors, exponents))
    if U >= K or U <= 0 or ratio != Fraction(U, K):
        raise AssertionError("invalid oriented relation quotient")
    if U % modulus != K % modulus or K * K % U:
        raise AssertionError("relation quotient did not preserve the modulus class")
    E = 4 * U
    if E % 4 or 4 * K * K % E or E % modulus != 1 or E > 4 * K - 4 * modulus:
        raise AssertionError("invalid even terminal")
    numerator = 4 * K - E
    source, remainder = divmod(numerator, modulus)
    if remainder or source <= 0 or source >= prime or source % 4:
        raise AssertionError("invalid even terminal source")
    return source, U, relation


def all_relations(record: dict[str, object]) -> list[tuple[int, ...]]:
    modulus = int(record["R"])
    factors = [(int(q), int(exponent)) for q, exponent in record["factorization"]]
    subgroup = lattice.pair.source.unit_group_subgroup_certificate(factors, modulus)
    if not subgroup["target_in_generated_subgroup"]:
        raise AssertionError("short-relation record left the generated subgroup")
    logs = [[int(value) for value in row] for row in subgroup["generator_log_vectors"]]
    orders = [int(component["order"]) for component in subgroup["components"]]
    candidates = []
    for vector in itertools.product(*[range(-exponent, exponent + 1) for _q, exponent in factors]):
        if vector and any(vector) and relation_holds(vector, logs, orders):
            candidates.append(tuple(vector))
    return candidates


def run() -> dict[str, object]:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the short-relation input changed")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED_RECORD_COUNT:
        raise AssertionError("unexpected short-relation record count")

    relation_count = 0
    terminals: dict[tuple[int, int, int], dict[str, object]] = {}
    relation_histogram = Counter()
    for index, record in enumerate(records):
        candidates = all_relations(record)
        relation_count += len(candidates)
        relation_histogram[len(candidates)] += 1
        for candidate in candidates:
            source, U, oriented = terminal_from_relation(record, candidate)
            key = (int(record["prime"]), int(record["R"]), source)
            terminals.setdefault(
                key,
                {
                    "record_index": index,
                    "prime": int(record["prime"]),
                    "R": int(record["R"]),
                    "K": int(record["K"]),
                    "source": source,
                    "U": U,
                    "relation": list(oriented),
                    "relation_count": 0,
                },
            )
            terminals[key]["relation_count"] = int(terminals[key]["relation_count"]) + 1

    parameters: list[dict[str, int]] = []
    hits: list[dict[str, int]] = []
    for terminal in terminals.values():
        local_parameters, local_hits = odd_distance.audit_record(
            int(terminal["record_index"]),
            {"prime": terminal["prime"], "n": terminal["source"]},
        )
        for parameter in local_parameters:
            parameters.append({**terminal, **parameter})
        for hit in local_hits:
            hits.append({**terminal, **hit})

    hit_primes = sorted({int(item["prime"]) for item in hits})
    return {
        "arithmetic": (
            "For every frozen F state, enumerate every nonzero kernel relation in the original "
            "exponent box, orient each relation to a smaller even terminal, deduplicate terminals, "
            "and apply the complete odd-distance even-source Type I lift audit."
        ),
        "scope_note": (
            "Finite audit only. It strengthens the selected-shortest-relation audit by using all "
            "relations in the same exponent boxes; a miss does not rule out another state or lift family."
        ),
        "input": INPUT.name,
        "input_sha256": sha256(INPUT),
        "record_count": len(records),
        "raw_relation_vector_count": relation_count,
        "relation_count_histogram": {str(key): int(value) for key, value in sorted(relation_histogram.items())},
        "oriented_terminal_count": len(terminals),
        "parameter_count": len(parameters),
        "parameter_terminal_count": len({(int(item["prime"]), int(item["R"]), int(item["source"])) for item in parameters}),
        "tail_candidate_count": len(hits),
        "hit_terminal_count": len({(int(item["prime"]), int(item["R"]), int(item["source"])) for item in hits}),
        "hit_prime_count": len(hit_primes),
        "hit_primes": hit_primes,
        "parameters": parameters,
        "hits": hits,
    }


def main() -> int:
    result = run()
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "record_count", "raw_relation_vector_count", "oriented_terminal_count",
        "parameter_count", "parameter_terminal_count", "tail_candidate_count",
        "hit_terminal_count", "hit_prime_count", "hit_primes",
    )}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
