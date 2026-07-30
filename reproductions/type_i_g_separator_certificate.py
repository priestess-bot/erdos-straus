#!/usr/bin/env python3
"""Reconstruct canonical finite-group separator certificates for frozen G states."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
INPUT = ROOT / "reproductions" / "type-i-linear-general-b-obstruction-mixture-profile-600m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-g-separator-certificate-results.json"
EXPECTED_INPUT_SHA256 = "dce587d6e6703e5cdcb81b6cd05c16989394a7321d2d14515ea2eda6c2aec44d"
EXPECTED_STATE_COUNT = 190


def load_source():
    spec = importlib.util.spec_from_file_location("g_separator_sources", SOURCE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE_SCRIPT.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_source()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_pair(value: sympy.Rational) -> list[int]:
    value = sympy.Rational(value)
    return [int(value.p), int(value.q)]


def load_g_states(input_path: Path) -> list[dict[str, int]]:
    if sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen G/F obstruction input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list):
        raise AssertionError("the obstruction input lacks profiles")
    states = []
    for profile in profiles:
        prime = int(profile["prime"])
        records = profile.get("records")
        if not isinstance(records, list):
            raise AssertionError("a profile lacks records")
        for record in records:
            if record.get("classification") != "subgroup_character":
                continue
            if bool(record.get("target_in_generated_subgroup")):
                raise AssertionError("a selected G state contains -1 in its support subgroup")
            R = int(record["R"])
            K, remainder = divmod(prime * R + 1, 4)
            if remainder:
                raise AssertionError("linear state does not give integral K")
            states.append(
                {
                    "prime": prime,
                    "R": R,
                    "K": K,
                    "source_state_count": int(record["source_state_count"]),
                }
            )
    if len(states) != EXPECTED_STATE_COUNT:
        raise AssertionError(f"unexpected G-state count: {len(states)}")
    return states


def canonical_separator(
    factors: list[tuple[int, int]], certificate: dict[str, object]
) -> dict[str, object]:
    """Find the simplest c in {-1,0,1}^d with y=H^{-T}c separating -1."""
    if bool(certificate["target_in_generated_subgroup"]):
        raise AssertionError("a G separator was requested for an F state")
    orders = [
        int(component["order"])
        for component in certificate["components"]
        if isinstance(component, dict)
    ]
    H = sympy.Matrix(certificate["column_lattice_hermite_normal_form"])
    dimension = len(orders)
    if H.shape != (dimension, dimension) or H.det() == 0:
        raise AssertionError("the support-lattice HNF is not a full-rank square basis")
    logs = [
        [int(value) for value in row]
        for row in certificate["generator_log_vectors"]
    ]
    target = [
        int(value) for value in certificate["target_log_vector_for_minus_one"]
    ]
    if any(len(row) != dimension for row in logs) or len(target) != dimension:
        raise AssertionError("log-vector dimension mismatch")

    dual_basis = H.inv().T
    candidates = sorted(
        [
            (
                tuple(coordinates),
                sum(abs(value) for value in coordinates),
                sum(value != 0 for value in coordinates),
            )
            for coordinates in itertools.product((-1, 0, 1), repeat=dimension)
            if any(coordinates)
        ],
        key=lambda item: (item[1], item[2], item[0]),
    )
    for coordinates, _l1, _support in candidates:
        y_vector = dual_basis * sympy.Matrix(coordinates)
        y = [sympy.Rational(value) for value in y_vector]
        if any((orders[index] * y[index]).q != 1 for index in range(dimension)):
            continue
        generator_phases = [
            sum(y[index] * logs[row][index] for index in range(dimension))
            for row in range(len(logs))
        ]
        if any(phase.q != 1 for phase in generator_phases):
            continue
        target_phase = sum(y[index] * target[index] for index in range(dimension))
        if target_phase.q == 1:
            continue
        character_order = math.lcm(*(int(value.q) for value in y))
        target_phase_mod_one = target_phase - sympy.floor(target_phase)
        return {
            "component_orders": orders,
            "support_lattice_hnf": [
                [int(H[row, column]) for column in range(dimension)]
                for row in range(dimension)
            ],
            "dual_basis_coordinates": list(coordinates),
            "phase_vector": [fraction_pair(value) for value in y],
            "character_order": character_order,
            "active_components": [
                index for index, value in enumerate(y) if value % 1 != 0
            ],
            "generator_phases_integral": True,
            "target_phase": fraction_pair(target_phase),
            "target_phase_mod_one": fraction_pair(target_phase_mod_one),
            "target_separated": True,
        }
    raise AssertionError("no separator found in the {-1,0,1} dual-coordinate box")


def reconstruct(input_path: Path) -> dict[str, object]:
    states = load_g_states(input_path)
    profiles = []
    order_counts: dict[str, int] = {}
    support_counts: dict[str, int] = {}
    for state in states:
        factors = sources.exact_factorization(state["K"])
        certificate = sources.unit_group_subgroup_certificate(factors, state["R"])
        if bool(certificate["target_in_generated_subgroup"]):
            raise AssertionError("recomputed support membership contradicts G classification")
        separator = canonical_separator(factors, certificate)
        order_key = str(separator["character_order"])
        support_key = str(len(separator["active_components"]))
        order_counts[order_key] = order_counts.get(order_key, 0) + 1
        support_counts[support_key] = support_counts.get(support_key, 0) + 1
        profiles.append(
            {
                **state,
                "factorization": [[int(prime), int(exponent)] for prime, exponent in factors],
                "separator": separator,
            }
        )

    return {
        "arithmetic": "For every frozen G state, reconstruct a finite-group character trivial on the K-support and nontrivial at -1 using a canonical small HNF-dual coefficient.",
        "scope_note": "Finite certificate reconstruction only. It verifies the 190 frozen G states and does not prove a cross-state capacity contradiction or a selector for all core primes.",
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "state_count": len(profiles),
        "dual_coordinate_box": [-1, 1],
        "character_order_counts": order_counts,
        "active_component_counts": support_counts,
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = reconstruct(args.input)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "state_count": payload["state_count"],
                "dual_coordinate_box": payload["dual_coordinate_box"],
                "character_order_counts": payload["character_order_counts"],
                "active_component_counts": payload["active_component_counts"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
