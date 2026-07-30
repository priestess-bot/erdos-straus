#!/usr/bin/env python3
"""Verify that a short nonzero kernel relation gives an even terminal."""

from __future__ import annotations

import argparse
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
FOURIER_INPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
CROSS_INPUT = ROOT / "reproductions" / "type-i-f-full-cross-color-pair-capacity-results.json"
LATTICE_SCRIPT = ROOT / "reproductions" / "type_i_f_relation_lattice_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-short-relation-even-terminal-results.json"
EXPECTED_FOURIER_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_CROSS_SHA256 = "c99ee379e61aef20b1dbbcdffb1a2b2f532fa8b8697308cdf32ac45b31608cb5"


def load_lattice_module():
    spec = importlib.util.spec_from_file_location("short_relation_lattice", LATTICE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {LATTICE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


lattice = load_lattice_module()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_records() -> list[dict[str, object]]:
    if sha256(FOURIER_INPUT) != EXPECTED_FOURIER_SHA256:
        raise AssertionError("the frozen Fourier input changed")
    if sha256(CROSS_INPUT) != EXPECTED_CROSS_SHA256:
        raise AssertionError("the frozen cross-color input changed")
    fourier = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    cross = json.loads(CROSS_INPUT.read_text(encoding="utf-8"))
    unresolved = {
        (int(record["prime"]), int(record["R"]))
        for record in cross["unresolved_records"]
    }
    records = [
        dict(record)
        for record in fourier["records"]
        if (int(record["prime"]), int(record["R"])) in unresolved
    ]
    if len(records) != len(unresolved):
        raise AssertionError("cross-color unresolved records did not match Fourier records")
    return records


def relation_holds(
    relation: tuple[int, ...], generator_logs: list[list[int]], orders: list[int]
) -> bool:
    for component, order in enumerate(orders):
        residue = sum(
            relation[index] * int(generator_logs[index][component])
            for index in range(len(relation))
        )
        if residue % order:
            return False
    return True


def rational_ratio(factors: list[tuple[int, int]], relation: tuple[int, ...]) -> Fraction:
    ratio = Fraction(1, 1)
    for (prime, _exponent), value in zip(factors, relation):
        if value >= 0:
            ratio *= prime**value
        else:
            ratio /= prime ** (-value)
    return ratio


def audit_record(record: dict[str, object]) -> dict[str, object]:
    p = int(record["prime"])
    R = int(record["R"])
    K = int(record["K"])
    if record.get("status") != "bounded_fourier_certificate":
        raise AssertionError(f"short-relation input is not an F certificate ({p}, {R})")
    factors = [(int(q), int(exponent)) for q, exponent in record["factorization"]]
    if R % 4 != 3 or 4 * K != p * R + 1:
        raise AssertionError(f"invalid Type-I state ({p}, {R})")
    if math.prod(q**exponent for q, exponent in factors) != K:
        raise AssertionError(f"factorization mismatch for ({p}, {R})")

    subgroup = lattice.pair.source.unit_group_subgroup_certificate(factors, R)
    if not subgroup["target_in_generated_subgroup"]:
        raise AssertionError(f"target is not in the subgroup for ({p}, {R})")
    relation_basis, _target_preimage, orders = lattice.solve_relation_lattice(
        factors, subgroup
    )
    generator_logs = [
        [int(value) for value in row]
        for row in subgroup["generator_log_vectors"]
    ]
    candidates = [
        vector
        for vector in itertools.product(
            *[range(-exponent, exponent + 1) for _q, exponent in factors]
        )
        if any(vector) and relation_holds(vector, generator_logs, orders)
    ]
    if not candidates:
        raise AssertionError(f"no nonzero short relation for ({p}, {R})")
    relation = min(
        candidates,
        key=lambda vector: (max(abs(value) for value in vector), sum(abs(value) for value in vector), vector),
    )
    ratio = rational_ratio(factors, relation)
    if ratio == 1:
        raise AssertionError(f"nonzero relation has rational ratio one for ({p}, {R})")
    if ratio > 1:
        relation = tuple(-value for value in relation)
        ratio = 1 / ratio
    if not ratio < 1:
        raise AssertionError(f"relation orientation failed for ({p}, {R})")

    exponents = [exponent + value for (_q, exponent), value in zip(factors, relation)]
    if any(value < 0 or value > 2 * exponent for value, (_q, exponent) in zip(exponents, factors)):
        raise AssertionError(f"oriented relation left the K^2 box for ({p}, {R})")
    U = math.prod(q**exponent for (q, _old), exponent in zip(factors, exponents))
    if Fraction(U, K) != ratio or U >= K or U <= 0:
        raise AssertionError(f"invalid short-relation quotient for ({p}, {R})")
    if U % R != K % R:
        raise AssertionError(f"relation congruence failed for ({p}, {R})")
    if K * K % U:
        raise AssertionError(f"U does not divide K^2 for ({p}, {R})")

    E = 4 * U
    if 4 * K * K % E or E % 4 or E % R != 1 or not (0 < E < 4 * K):
        raise AssertionError(f"invalid even terminal divisor for ({p}, {R})")
    if E > 4 * K - 4 * R:
        raise AssertionError(f"terminal height bound failed for ({p}, {R})")
    numerator = 4 * K - E
    n, remainder = divmod(numerator, R)
    if remainder or n <= 0 or n % 4 or n >= p:
        raise AssertionError(f"invalid even terminal n for ({p}, {R})")

    return {
        "prime": p,
        "R": R,
        "K": K,
        "factorization": [[q, exponent] for q, exponent in factors],
        "relation_basis_index": abs(int(relation_basis.det())),
        "relation": list(relation),
        "relation_linf": max(abs(value) for value in relation),
        "relation_l1": sum(abs(value) for value in relation),
        "relation_count_in_box": len(candidates),
        "rho": [ratio.numerator, ratio.denominator],
        "U": U,
        "E": E,
        "n": n,
    }


def run() -> dict[str, object]:
    records = [audit_record(record) for record in load_records()]
    linf = Counter(int(record["relation_linf"]) for record in records)
    l1 = Counter(int(record["relation_l1"]) for record in records)
    return {
        "arithmetic": "If a nonzero relation lambda in the multiplicative kernel satisfies |lambda_i| <= nu_i, orient it so prod(q_i^lambda_i) < 1; then E=4K prod(q_i^lambda_i) is a legal even terminal divisor.",
        "scope_note": "The algebraic lemma is general for a legal (R,K) state. The finite audit below covers only the 291 frozen split-color unresolved F states; it is a terminal certificate, not a target-divisor selector or a cross-state descent theorem.",
        "fourier_input": FOURIER_INPUT.name,
        "fourier_input_sha256": sha256(FOURIER_INPUT),
        "cross_color_input": CROSS_INPUT.name,
        "cross_color_input_sha256": sha256(CROSS_INPUT),
        "record_count": len(records),
        "terminal_count": len(records),
        "relation_linf_distribution": {str(key): int(value) for key, value in sorted(linf.items())},
        "relation_l1_distribution": {str(key): int(value) for key, value in sorted(l1.items())},
        "maximum_relation_linf": max(int(record["relation_linf"]) for record in records),
        "maximum_relation_l1": max(int(record["relation_l1"]) for record in records),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run()
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: payload[key]
                for key in (
                    "record_count",
                    "terminal_count",
                    "relation_linf_distribution",
                    "relation_l1_distribution",
                    "maximum_relation_linf",
                    "maximum_relation_l1",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
