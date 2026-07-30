#!/usr/bin/env python3
"""Reconstruct bounded Fourier certificates for every frozen finite-exponent F state."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
LATTICE_SCRIPT = ROOT / "reproductions" / "type_i_f_relation_lattice_certificate.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-full-spectrum-results.json"
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
EXPECTED_STATE_COUNT = 2752


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


lattice = load_module("full_spectrum_relation_lattice", LATTICE_SCRIPT)
source = lattice.pair.source


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mod_one(value: sympy.Rational) -> sympy.Rational:
    value = sympy.Rational(value)
    return sympy.Rational(value - sympy.floor(value))


def fraction_pair(value: sympy.Rational) -> list[int]:
    value = sympy.Rational(value)
    return [int(value.p), int(value.q)]


def dirichlet_mass(nu: int, theta: sympy.Rational) -> float:
    theta = mod_one(theta)
    if theta == 0:
        return 1.0
    x = float(theta)
    denominator = (2 * nu + 1) * math.sin(math.pi * x)
    if abs(denominator) < 1e-15:
        return 1.0
    return abs(math.sin((2 * nu + 1) * math.pi * x) / denominator)


def load_states(input_path: Path) -> list[dict[str, int]]:
    if sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen full-spectrum input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    states = []
    for profile in payload.get("profiles", []):
        prime = int(profile["prime"])
        for record in profile.get("records", []):
            if record.get("classification") != "finite_exponent":
                continue
            R = int(record["R"])
            K = int(record["K"])
            if 4 * K != prime * R + 1:
                raise AssertionError(
                    "full-spectrum state failed 4K=pR+1 before Fourier reconstruction"
                )
            states.append(
                {
                    "prime": prime,
                    "R": R,
                    "K": K,
                }
            )
    if len(states) != EXPECTED_STATE_COUNT:
        raise AssertionError(f"unexpected finite-exponent state count: {len(states)}")
    return states


def reconstruct_state(state: dict[str, int]) -> dict[str, object]:
    if 4 * int(state["K"]) != int(state["prime"]) * int(state["R"]) + 1:
        raise AssertionError("Fourier state failed 4K=pR+1")
    factors = source.exact_factorization(state["K"])
    certificate = source.unit_group_subgroup_certificate(factors, state["R"])
    if not bool(certificate["target_in_generated_subgroup"]):
        raise AssertionError("finite-exponent state is not F type")
    relation_basis, target_preimage, _orders = lattice.solve_relation_lattice(
        factors, certificate
    )
    dimension = len(factors)
    dual_basis = relation_basis.inv().T
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
        character_order = math.lcm(
            *(int(sympy.Rational(value).q) for value in phase_vector)
        )
        candidates.append(
            (
                -mass,
                character_order,
                len(active),
                sum(abs(value) for value in coordinates),
                tuple(coordinates),
                phase_vector,
                target_phase,
                active,
            )
        )
    if not candidates:
        return {
            **state,
            "status": "no_bounded_candidate",
            "factorization": [[int(q), int(e)] for q, e in factors],
        }
    candidates.sort(key=lambda item: item[:5])
    (
        negative_mass,
        character_order,
        support_size,
        _l1,
        coordinates,
        phase_vector,
        target_phase,
        active,
    ) = candidates[0]
    group_order = abs(int(relation_basis.det()))
    mass = -negative_mass
    threshold = 1.0 / (group_order - 1)
    return {
        **state,
        "status": (
            "bounded_fourier_certificate"
            if mass >= threshold
            else "bounded_candidate_below_threshold"
        ),
        "factorization": [[int(q), int(e)] for q, e in factors],
        "group_order": group_order,
        "dual_coordinates": list(coordinates),
        "phase_vector": [fraction_pair(value) for value in phase_vector],
        "active_support": list(active),
        "active_primes": [int(factors[index][0]) for index in active],
        "character_order": int(character_order),
        "target_phase_mod_one": fraction_pair(mod_one(target_phase)),
        "normalized_fourier_mass": format(mass, ".17g"),
        "threshold": format(threshold, ".17g"),
        "threshold_ratio": format(mass / threshold, ".17g"),
        "candidate_count": len(candidates),
    }


def run(input_path: Path, limit: int | None = None) -> dict[str, object]:
    states = load_states(input_path)
    selected_states = states if limit is None else states[:limit]
    records = []
    for index, state in enumerate(selected_states, start=1):
        record = reconstruct_state(state)
        if tuple(record[key] for key in ("prime", "R", "K")) != tuple(
            state[key] for key in ("prime", "R", "K")
        ):
            raise AssertionError("Fourier output changed the source state key")
        records.append(record)
        if index % 250 == 0:
            print(f"processed {index}/{len(selected_states)}", file=sys.stderr)
    candidates = [
        record
        for record in records
        if record["status"]
        in {"bounded_fourier_certificate", "bounded_candidate_below_threshold"}
    ]
    threshold_met = [
        record for record in records if record["status"] == "bounded_fourier_certificate"
    ]
    threshold_missed = [
        record
        for record in records
        if record["status"] == "bounded_candidate_below_threshold"
    ]
    missing = [record for record in records if record["status"] == "no_bounded_candidate"]
    ratios = [float(record["threshold_ratio"]) for record in candidates]
    support_counts = Counter(len(record["active_support"]) for record in threshold_met)
    order_counts = Counter(record["character_order"] for record in threshold_met)
    repeated_keys = Counter(
        (
            record["prime"],
            tuple(record["active_primes"]),
            record["character_order"],
            tuple(record["target_phase_mod_one"]),
        )
        for record in threshold_met
    )
    return {
        "arithmetic": "For every finite-exponent F state in the frozen 200-prime complete linear spectrum, reconstruct a relation lattice and select the maximal normalized Fourier product inside c in {-1,0,1}^r subject to a nonintegral target phase.",
        "scope_note": "Finite full-spectrum certificate reconstruction only. The bounded candidate is not asserted to be the global Fourier maximizer; no cross-state capacity contradiction or all-prime selector theorem is claimed.",
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "state_count": len(selected_states),
        "bounded_candidate_count": len(candidates),
        "threshold_met_count": len(threshold_met),
        "threshold_missed_count": len(threshold_missed),
        "no_bounded_candidate_count": len(missing),
        "selected_support_counts": {
            str(key): int(value) for key, value in sorted(support_counts.items())
        },
        "selected_character_order_counts": {
            str(key): int(value) for key, value in sorted(order_counts.items())
        },
        "minimum_threshold_ratio": min(ratios) if ratios else None,
        "median_threshold_ratio": sorted(ratios)[len(ratios) // 2] if ratios else None,
        "repeated_key_count": sum(value > 1 for value in repeated_keys.values()),
        "maximum_repeated_key_size": max(repeated_keys.values()) if repeated_keys else 0,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()
    payload = run(args.input, args.limit)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                key: payload[key]
                for key in (
                    "state_count",
                    "bounded_candidate_count",
                    "threshold_met_count",
                    "threshold_missed_count",
                    "no_bounded_candidate_count",
                    "selected_support_counts",
                    "minimum_threshold_ratio",
                    "median_threshold_ratio",
                    "repeated_key_count",
                    "maximum_repeated_key_size",
                )
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
