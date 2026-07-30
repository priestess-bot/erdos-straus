#!/usr/bin/env python3
"""Map frozen F-state relation-lattice phases to two carrier directions."""

from __future__ import annotations

import argparse
from collections import Counter
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
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-two-direction-phase-demand-results.json"
EXPECTED_INPUT_SHA256 = "5c4f19375e654c4b1ac1d01745125b248f5371048d643633be096a8e332a336c"
EXPECTED_STATE_COUNT = 45


def load_source():
    spec = importlib.util.spec_from_file_location("two_direction_phase_source", SOURCE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


source = load_source()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_pair(value: sympy.Rational) -> list[int]:
    value = sympy.Rational(value)
    return [int(value.p), int(value.q)]


def mod_one(value: sympy.Rational) -> sympy.Rational:
    value = sympy.Rational(value)
    return sympy.Rational(value - sympy.floor(value))


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def recover_linear_state(prime: int, R: int) -> tuple[int, int]:
    _bound, states_by_R = source.enumerate_linear_source_states(prime)
    states = states_by_R.get(R)
    if not states:
        raise AssertionError(f"could not recover a linear state for ({prime}, {R})")
    return max(states)


def choose_dual_pair(
    row: dict[str, object], factors: list[tuple[int, int]]
) -> tuple[list[sympy.Rational], list[int], list[int], sympy.Rational, tuple[int, ...]]:
    """Choose a small dual vector whose target phase is nonintegral and has two active coordinates."""
    dimension = len(factors)
    relation_basis = sympy.Matrix(
        dimension,
        dimension,
        lambda row_index, column: int(row["relation_basis_columns"][column][row_index]),
    )
    if relation_basis.det() == 0:
        raise AssertionError("the relation basis is singular")
    dual_basis = relation_basis.inv().T
    target_preimage = [int(value) for value in row["target_preimage"]]
    candidates = []
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
        candidates.append(
            (
                len(active),
                sum(abs(value) for value in coordinates),
                tuple(coordinates),
                phase_vector,
                target_phase,
                active,
            )
        )
    if not candidates:
        raise AssertionError("no two-direction dual certificate in the {-1,0,1} box")
    candidates.sort(key=lambda item: (item[0], item[1], item[2]))
    _support_size, _l1, coordinates, phase_vector, target_phase, active = candidates[0]
    return phase_vector, list(coordinates), target_preimage, target_phase, active


def block_phase(
    block: int, factors: list[tuple[int, int]], phase_vector: list[sympy.Rational]
) -> sympy.Rational:
    factor_index = {prime: index for index, (prime, _exponent) in enumerate(factors)}
    phase = sympy.Rational(0)
    for prime, exponent in source.exact_factorization(block):
        # When 2 is absent from K, the character is only evaluated on the odd part
        # of the block; all other block primes belong to K's support.
        if prime in factor_index:
            phase += exponent * phase_vector[factor_index[prime]]
    return sympy.Rational(phase)


def phase_projection(
    pair_indices: tuple[int, int],
    factors: list[tuple[int, int]],
    phase_vector: list[sympy.Rational],
    target_phase: sympy.Rational,
) -> tuple[int, int, list[list[int]]]:
    """Project one exact character congruence to a pair of box coordinates."""
    complement_indices = [
        index for index in range(len(factors)) if index not in pair_indices
    ]
    complement_residues = set()
    complement_ranges = [
        range(-int(factors[index][1]), int(factors[index][1]) + 1)
        for index in complement_indices
    ]
    for values in itertools.product(*complement_ranges) if complement_ranges else [()]:
        complement_phase = sum(
            phase_vector[index] * value
            for index, value in zip(complement_indices, values)
        )
        complement_residues.add(mod_one(complement_phase))

    allowed_pairs = []
    first_exponent = int(factors[pair_indices[0]][1])
    second_exponent = int(factors[pair_indices[1]][1])
    first_phase = phase_vector[pair_indices[0]]
    second_phase = phase_vector[pair_indices[1]]
    for first in range(-first_exponent, first_exponent + 1):
        for second in range(-second_exponent, second_exponent + 1):
            pair_phase = first_phase * first + second_phase * second
            if any(
                mod_one(pair_phase + complement_phase) == mod_one(target_phase)
                for complement_phase in complement_residues
            ):
                allowed_pairs.append([first, second])
    return len(complement_residues), len(allowed_pairs), allowed_pairs


def load_rows(input_path: Path) -> list[dict[str, object]]:
    if sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen F relation-lattice input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    rows = payload.get("profiles")
    if not isinstance(rows, list) or len(rows) != EXPECTED_STATE_COUNT:
        raise AssertionError("the frozen F-state profile is incomplete")
    return [dict(row) for row in rows]


def map_state(row: dict[str, object]) -> dict[str, object]:
    prime = int(row["prime"])
    R = int(row["R"])
    K = int(row["K"])
    factors = [(int(prime_factor), int(exponent)) for prime_factor, exponent in row["factorization"]]
    certificate = source.unit_group_subgroup_certificate(
        source.exact_factorization(K), R
    )
    if not bool(certificate["target_in_generated_subgroup"]):
        raise AssertionError("the selected row is not F type")
    phase_vector, coordinates, target_preimage, target_phase, active = choose_dual_pair(
        row, factors
    )
    pair_indices = (active[0], active[1])
    pair_primes = [factors[index][0] for index in pair_indices]
    target_demand = mod_one(
        target_phase
        - sum(
            phase_vector[index] * target_preimage[index]
            for index in range(len(factors))
            if index not in pair_indices
        )
    )
    a, s = recover_linear_state(prime, R)
    blocks = [("s", s, s * R + 1), ("a", a, a * R + 1)]
    selected_carriers = []
    for index, q in zip(pair_indices, pair_primes):
        heights = [valuation(block, q) for _label, _t, block in blocks]
        chosen_block = 0 if heights[0] >= heights[1] else 1
        selected_carriers.append(
            {
                "prime": q,
                "phase": fraction_pair(phase_vector[index]),
                "label": blocks[chosen_block][0],
                "height": heights[chosen_block],
                "heights_by_label": {
                    blocks[0][0]: heights[0],
                    blocks[1][0]: heights[1],
                },
            }
        )

    carrier_records = []
    for label, t, block in blocks:
        pair_heights = [valuation(block, q) for q in pair_primes]
        full = block_phase(block, factors, phase_vector)
        pair_only = sum(
            phase_vector[index] * height
            for index, height in zip(pair_indices, pair_heights)
        )
        carrier_records.append(
            {
                "label": label,
                "t": t,
                "block": block,
                "pair_heights": pair_heights,
                "full_phase_mod_one": fraction_pair(mod_one(full)),
                "pair_phase_mod_one": fraction_pair(mod_one(pair_only)),
                "other_phase_residual_mod_one": fraction_pair(mod_one(full - pair_only)),
            }
        )
    complement_phase_count, projection_pair_count, projection_pairs = phase_projection(
        pair_indices, factors, phase_vector, target_phase
    )
    joint_height_product = 1
    for carrier in selected_carriers:
        joint_height_product *= int(carrier["height"])
    return {
        "prime": prime,
        "R": R,
        "K": K,
        "factorization": [[q, exponent] for q, exponent in factors],
        "linear_state": {"a": a, "s": s},
        "dual_coordinates": coordinates,
        "phase_vector": [fraction_pair(value) for value in phase_vector],
        "target_preimage": target_preimage,
        "target_phase_mod_one": fraction_pair(mod_one(target_phase)),
        "active_support": list(active),
        "pair_indices": list(pair_indices),
        "pair_primes": pair_primes,
        "target_pair_demand_mod_one": fraction_pair(target_demand),
        "phase_projection_pair_count": projection_pair_count,
        "complement_phase_residue_count": complement_phase_count,
        "phase_projection_pairs": projection_pairs,
        "selected_carriers": selected_carriers,
        "joint_height_product": joint_height_product,
        "carrier_records": carrier_records,
    }


def run(input_path: Path) -> dict[str, object]:
    records = [map_state(row) for row in load_rows(input_path)]
    demand_keys = Counter(
        (
            record["prime"],
            tuple(record["pair_primes"]),
            tuple(item["label"] for item in record["selected_carriers"]),
            tuple(record["target_pair_demand_mod_one"]),
        )
        for record in records
    )
    support_counts = Counter(len(record["active_support"]) for record in records)
    color_counts = Counter(
        tuple(item["label"] for item in record["selected_carriers"])
        for record in records
    )
    demand_counts = Counter(
        tuple(record["target_pair_demand_mod_one"]) for record in records
    )
    projection_counts = Counter(
        int(record["phase_projection_pair_count"]) for record in records
    )
    carrier_phase_counts = Counter(
        tuple(
            tuple(carrier[f"{field}_mod_one"])
            for carrier in record["carrier_records"]
            for field in ("full_phase", "pair_phase")
        )
        for record in records
    )
    return {
        "arithmetic": "For each frozen F state, select a small relation-lattice dual phase with nonintegral target value, project the target affine congruence to two active coordinates, and record exact source-block carrier phases and q-adic heights.",
        "scope_note": "This is a finite necessary-phase mapping, not a Fourier amplitude theorem, a capacity contradiction, or an arithmetic descent. The selected dual vector need not be the maximum Fourier coefficient. The pair projection is computed with all complementary coordinates ranging over the full exponent box; an empty projection is a valid state-internal phase obstruction, while a nonempty projection is only a capacity input.",
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "state_count": len(records),
        "dual_coordinate_box": [-1, 1],
        "selected_support_counts": {
            str(key): int(value) for key, value in sorted(support_counts.items())
        },
        "selected_color_counts": {
            "".join(key): int(value) for key, value in sorted(color_counts.items())
        },
        "target_pair_demand_counts": {
            "/".join(str(value) for value in key): int(count)
            for key, count in sorted(demand_counts.items())
        },
        "phase_projection_pair_counts": {
            str(key): int(value) for key, value in sorted(projection_counts.items())
        },
        "empty_phase_projection_count": sum(
            record["phase_projection_pair_count"] == 0 for record in records
        ),
        "carrier_phase_profile_counts": {
            str(key): int(value) for key, value in sorted(carrier_phase_counts.items(), key=str)
        },
        "demand_group_count": len(demand_keys),
        "repeated_demand_group_count": sum(value > 1 for value in demand_keys.values()),
        "maximum_demand_group_size": max(demand_keys.values()),
        "joint_height_product_total": sum(
            record["joint_height_product"] for record in records
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run(args.input)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "state_count": payload["state_count"],
                "selected_support_counts": payload["selected_support_counts"],
                "selected_color_counts": payload["selected_color_counts"],
                "target_pair_demand_counts": payload["target_pair_demand_counts"],
                "phase_projection_pair_counts": payload["phase_projection_pair_counts"],
                "empty_phase_projection_count": payload["empty_phase_projection_count"],
                "demand_group_count": payload["demand_group_count"],
                "repeated_demand_group_count": payload["repeated_demand_group_count"],
                "maximum_demand_group_size": payload["maximum_demand_group_size"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
