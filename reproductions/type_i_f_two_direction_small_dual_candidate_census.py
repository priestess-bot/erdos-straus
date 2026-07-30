#!/usr/bin/env python3
"""Census all small dual two-direction demand keys on the frozen F profile."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-relation-lattice-certificate-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-two-direction-small-dual-candidate-census-results.json"
EXPECTED_INPUT_SHA256 = "5c4f19375e654c4b1ac1d01745125b248f5371048d643633be096a8e332a336c"
EXPECTED_STATE_COUNT = 45


def load_source():
    spec = importlib.util.spec_from_file_location("small_dual_census_source", SOURCE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


source = load_source()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mod_one(value: sympy.Rational) -> sympy.Rational:
    value = sympy.Rational(value)
    return sympy.Rational(value - sympy.floor(value))


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def load_rows(input_path: Path) -> list[dict[str, object]]:
    if sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen F relation-lattice input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    rows = payload.get("profiles")
    if not isinstance(rows, list) or len(rows) != EXPECTED_STATE_COUNT:
        raise AssertionError("the frozen F-state profile is incomplete")
    return [dict(row) for row in rows]


def exact_carrier_capacity(
    prime: int, label: int, q1: int, q2: int
) -> list[int]:
    product = q1 * q2
    if (prime - label) % product:
        return []
    values = []
    for divisor in sympy.divisors((prime - label) // product):
        if (product * divisor - 1) % label:
            continue
        values.append((product * divisor - 1) // label)
    return sorted(int(value) for value in values)


def census(input_path: Path) -> dict[str, object]:
    rows = load_rows(input_path)
    state_cache: dict[int, dict[int, tuple[int, int]]] = {}
    demand_keys: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    support_counts = Counter()
    color_counts = Counter()
    total_candidates = 0

    for row_index, row in enumerate(rows):
        prime = int(row["prime"])
        R = int(row["R"])
        factors = [(int(q), int(e)) for q, e in row["factorization"]]
        dimension = len(factors)
        relation_basis = sympy.Matrix(
            dimension,
            dimension,
            lambda i, j: int(row["relation_basis_columns"][j][i]),
        )
        dual_basis = relation_basis.inv().T
        target_preimage = [int(value) for value in row["target_preimage"]]
        if prime not in state_cache:
            _bound, states_by_R = source.enumerate_linear_source_states(prime)
            state_cache[prime] = {
                int(modulus): max(states) for modulus, states in states_by_R.items()
            }
        if R not in state_cache[prime]:
            raise AssertionError("the F row is absent from the complete linear state map")
        a, s = state_cache[prime][R]
        blocks = [("s", s, s * R + 1), ("a", a, a * R + 1)]
        prime_index = {q: index for index, (q, _e) in enumerate(factors)}

        row_candidates = 0
        for coordinates in itertools.product((-1, 0, 1), repeat=dimension):
            if not any(coordinates):
                continue
            phase_vector = [
                sympy.Rational(value)
                for value in dual_basis * sympy.Matrix(coordinates)
            ]
            target_phase = sum(
                phase_vector[index] * target_preimage[index]
                for index in range(dimension)
            )
            active = tuple(
                index
                for index, value in enumerate(phase_vector)
                if mod_one(value) != 0
            )
            if target_phase.q == 1 or len(active) < 2:
                continue
            pair_indices = (active[0], active[1])
            pair_primes = (factors[pair_indices[0]][0], factors[pair_indices[1]][0])
            colors = []
            heights = []
            for q in pair_primes:
                block_heights = [valuation(block, q) for _label, _t, block in blocks]
                selected = 0 if block_heights[0] >= block_heights[1] else 1
                colors.append(blocks[selected][0])
                heights.append(block_heights[selected])
            target_pair_demand = mod_one(
                target_phase
                - sum(
                    phase_vector[index] * target_preimage[index]
                    for index in range(dimension)
                    if index not in pair_indices
                )
            )
            key = (
                prime,
                pair_primes,
                tuple(colors),
                str(target_pair_demand),
            )
            demand_keys[key].append(
                {
                    "row_index": row_index,
                    "R": R,
                    "dual_coordinates": list(coordinates),
                    "active_support": list(active),
                    "selected_heights": heights,
                    "target_pair_demand_mod_one": [
                        int(target_pair_demand.p),
                        int(target_pair_demand.q),
                    ],
                }
            )
            row_candidates += 1
            total_candidates += 1
            support_counts[len(active)] += 1
            color_counts[tuple(colors)] += 1

        if row_candidates == 0:
            raise AssertionError(f"no small two-direction candidate for row {row_index}")

    repeated = []
    for key, entries in sorted(demand_keys.items(), key=lambda item: str(item[0])):
        distinct_rows = sorted({int(entry["row_index"]) for entry in entries})
        if len(distinct_rows) < 2:
            continue
        representative_by_row = {}
        for entry in entries:
            representative_by_row.setdefault(int(entry["row_index"]), entry)
        state_rows = [representative_by_row[index] for index in distinct_rows]
        prime, pair, colors, demand = key
        label = 0 if colors[0] == "s" else None
        # The selected label is recovered from the state records below; both
        # repeated groups in this frozen census have equal colors.
        state_labels = []
        for entry in entries:
            row = rows[int(entry["row_index"])]
            prime_value = int(row["prime"])
            R = int(row["R"])
            _bound, states_by_R = source.enumerate_linear_source_states(prime_value)
            a, s = max(states_by_R[R])
            state_labels.append(s if colors[0] == "s" else a)
        capacities = [
            exact_carrier_capacity(int(prime), int(label_value), int(pair[0]), int(pair[1]))
            for label_value in sorted(set(state_labels))
        ]
        repeated.append(
            {
                "prime": int(prime),
                "pair_primes": [int(pair[0]), int(pair[1])],
                "colors": list(colors),
                "target_pair_demand": demand,
                "candidate_count": len(entries),
                "state_rows": state_rows,
                "distinct_state_count": len(distinct_rows),
                "carrier_capacity_R_values": capacities,
                "carrier_capacity_count": sum(len(value) for value in capacities),
            }
        )

    if len(repeated) != 2 or max(item["distinct_state_count"] for item in repeated) != 2:
        raise AssertionError("the repeated small-dual demand census changed")
    return {
        "arithmetic": "Enumerate every relation-lattice dual coefficient in {-1,0,1}^d for the frozen F states, project to the first two active directions, and group exact phase/color/carrier demand keys across states.",
        "scope_note": "Finite negative boundary only. The census does not choose a global certificate, prove that a Fourier maximizer is selected, or establish a cross-state contradiction.",
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "state_count": len(rows),
        "dual_coordinate_box": [-1, 1],
        "total_candidates": total_candidates,
        "demand_key_count": len(demand_keys),
        "multi_state_demand_key_count": len(repeated),
        "maximum_multi_state_count": max(item["distinct_state_count"] for item in repeated),
        "candidate_support_counts": {
            str(key): int(value) for key, value in sorted(support_counts.items())
        },
        "candidate_color_counts": {
            "".join(key): int(value) for key, value in sorted(color_counts.items())
        },
        "repeated_demand_groups": repeated,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = census(args.input)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "state_count": payload["state_count"],
                "total_candidates": payload["total_candidates"],
                "demand_key_count": payload["demand_key_count"],
                "multi_state_demand_key_count": payload["multi_state_demand_key_count"],
                "maximum_multi_state_count": payload["maximum_multi_state_count"],
                "repeated_demand_groups": payload["repeated_demand_groups"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
