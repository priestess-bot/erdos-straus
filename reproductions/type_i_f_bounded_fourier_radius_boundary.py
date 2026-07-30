#!/usr/bin/env python3
"""Locate the coefficient-box radius needed by the frozen Fourier failures."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy

from type_i_f_bounded_fourier_full_spectrum import (
    INPUT as FULL_INPUT,
    lattice,
    load_states,
    mod_one,
    source,
    dirichlet_mass,
)


ROOT = Path(__file__).resolve().parents[1]
FULL_RESULT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-radius-boundary-results.json"
EXPECTED_FULL_RESULT_SHA256 = "b636ca5714ff784d0a1dd0ec89e42a377de56255a3fefe940e025a3cbe56154d"
EXPECTED_FAILURE_COUNT = 4


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_full_records(path: Path) -> list[dict[str, object]]:
    if sha256(path) != EXPECTED_FULL_RESULT_SHA256:
        raise AssertionError("the bounded Fourier full-spectrum result changed")
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list):
        raise AssertionError("the full-spectrum result lacks records")
    failures = [
        record for record in records if float(record["threshold_ratio"]) < 1.0
    ]
    if len(failures) != EXPECTED_FAILURE_COUNT:
        raise AssertionError("the bounded-radius failure count changed")
    return [dict(record) for record in failures]


def state_lookup() -> dict[tuple[int, int], dict[str, int]]:
    return {(state["prime"], state["R"]): state for state in load_states(FULL_INPUT)}


def best_for_radius(state: dict[str, int], radius: int) -> dict[str, object]:
    factors = source.exact_factorization(state["K"])
    certificate = source.unit_group_subgroup_certificate(factors, state["R"])
    relation_basis, target_preimage, _orders = lattice.solve_relation_lattice(
        factors, certificate
    )
    dimension = len(factors)
    dual_basis = relation_basis.inv().T
    best = None
    candidate_count = 0
    for coordinates in itertools.product(range(-radius, radius + 1), repeat=dimension):
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
        if target_phase.q == 1:
            continue
        active = tuple(
            index
            for index, value in enumerate(phase_vector)
            if mod_one(value) != 0
        )
        if not active:
            continue
        mass = 1.0
        for (_prime, exponent), phase in zip(factors, phase_vector):
            mass *= dirichlet_mass(exponent, phase)
        order = math.lcm(*(int(sympy.Rational(value).q) for value in phase_vector))
        key = (
            -mass,
            order,
            len(active),
            sum(abs(value) for value in coordinates),
            tuple(coordinates),
        )
        candidate_count += 1
        if best is None or key < best[0]:
            best = (
                key,
                mass,
                coordinates,
                phase_vector,
                target_phase,
                active,
            )
    if best is None:
        raise AssertionError("no target-phase candidate in requested radius")
    _key, mass, coordinates, phase_vector, target_phase, active = best
    group_order = abs(int(relation_basis.det()))
    threshold = 1.0 / (group_order - 1)
    target_phase_mod_one = mod_one(target_phase)
    return {
        "radius": radius,
        "candidate_count": candidate_count,
        "dual_coordinates": list(coordinates),
        "phase_vector": [[int(value.p), int(value.q)] for value in phase_vector],
        "active_support": list(active),
        "active_primes": [int(factors[index][0]) for index in active],
        "character_order": math.lcm(
            *(int(sympy.Rational(value).q) for value in phase_vector)
        ),
        "target_phase_mod_one": [
            int(target_phase_mod_one.p),
            int(target_phase_mod_one.q),
        ],
        "normalized_fourier_mass": format(mass, ".17g"),
        "threshold": format(threshold, ".17g"),
        "threshold_ratio": format(mass / threshold, ".17g"),
    }


def run(full_result: Path, max_radius: int) -> dict[str, object]:
    failures = load_full_records(full_result)
    lookup = state_lookup()
    profiles = []
    for failure in failures:
        key = (int(failure["prime"]), int(failure["R"]))
        state = lookup[key]
        scans = [best_for_radius(state, radius) for radius in range(1, max_radius + 1)]
        sufficient = [
            scan["radius"] for scan in scans if float(scan["threshold_ratio"]) >= 1.0
        ]
        if not sufficient:
            raise AssertionError(f"radius {max_radius} did not close {key}")
        profiles.append(
            {
                "prime": key[0],
                "R": key[1],
                "K": key[2] if len(key) > 2 else int(state["K"]),
                "radius_scans": scans,
                "minimal_sufficient_radius": min(sufficient),
            }
        )
    return {
        "arithmetic": "For the four finite-exponent states whose {-1,0,1} bounded Fourier candidate misses the necessary threshold, scan increasing symmetric dual coefficient boxes and record the first sufficient radius.",
        "scope_note": "Finite boundary audit only. It does not prove a universal bounded radius or a cross-state selector theorem.",
        "input": full_result.name,
        "input_sha256": sha256(full_result),
        "failure_count": len(profiles),
        "maximum_scanned_radius": max_radius,
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=FULL_RESULT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-radius", type=int, default=3)
    args = parser.parse_args()
    payload = run(args.input, args.max_radius)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "failure_count": payload["failure_count"],
                "maximum_scanned_radius": payload["maximum_scanned_radius"],
                "minimal_sufficient_radii": [
                    {
                        "prime": profile["prime"],
                        "R": profile["R"],
                        "minimal_sufficient_radius": profile["minimal_sufficient_radius"],
                    }
                    for profile in payload["profiles"]
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
