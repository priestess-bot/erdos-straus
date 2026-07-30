#!/usr/bin/env python3
"""Construct bounded canonical Fourier certificates for frozen F states."""

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

import mpmath
import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-f-relation-lattice-certificate-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-f-bounded-fourier-certificate-results.json"
EXPECTED_INPUT_SHA256 = "5c4f19375e654c4b1ac1d01745125b248f5371048d643633be096a8e332a336c"
EXPECTED_STATE_COUNT = 45
MP_DIGITS = 80


def load_source():
    spec = importlib.util.spec_from_file_location("bounded_fourier_source", SOURCE_SCRIPT)
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


def fraction_pair(value: sympy.Rational) -> list[int]:
    value = sympy.Rational(value)
    return [int(value.p), int(value.q)]


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def divisor_residue_spectrum(
    factors: list[tuple[int, int]], modulus: int
) -> set[int]:
    residues = {1}
    for prime, exponent in factors:
        residues = {
            residue * pow(prime, power, modulus) % modulus
            for residue in residues
            for power in range(exponent + 1)
        }
    return residues


def stabilizer_data(
    factors: list[tuple[int, int]],
    modulus: int,
    group_order: int,
    active_prime: int | None,
) -> dict[str, object]:
    """Compute the exact fixed-layer stabilizer when a single role is active."""
    if active_prime is None:
        return {}
    spectrum = divisor_residue_spectrum(factors, modulus)
    stabilizer = {
        candidate
        for candidate in spectrum
        if {candidate * residue % modulus for residue in spectrum} == spectrum
    }
    q_order = None
    if active_prime in {prime for prime, _exponent in factors}:
        current = active_prime % modulus
        q_order = 1
        while current not in stabilizer:
            current = current * active_prime % modulus
            q_order += 1
            if q_order > group_order:
                raise AssertionError("qT order exceeded the ambient group order")
    quotient_order = group_order // len(stabilizer)
    return {
        "divisor_spectrum_size": len(spectrum),
        "stabilizer_size": len(stabilizer),
        "quotient_order": quotient_order,
        "active_qT_order": q_order,
        "active_qT_generates_quotient": q_order == quotient_order,
        "target_in_stabilizer": (-1) % modulus in stabilizer,
    }


def rational_mpf(value: sympy.Rational) -> mpmath.mpf:
    value = sympy.Rational(value)
    return mpmath.mpf(int(value.p)) / int(value.q)


def dirichlet_mass(nu: int, theta: sympy.Rational) -> mpmath.mpf:
    """Return |sum_{-nu<=k<=nu} exp(2*pi*i*k*theta)|/(2*nu+1)."""
    theta = mod_one(theta)
    if theta == 0:
        return mpmath.mpf(1)
    x = rational_mpf(theta)
    numerator = mpmath.sin((2 * nu + 1) * mpmath.pi * x)
    denominator = (2 * nu + 1) * mpmath.sin(mpmath.pi * x)
    return abs(numerator / denominator)


def load_rows(input_path: Path) -> list[dict[str, object]]:
    if sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the frozen F relation-lattice input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    rows = payload.get("profiles")
    if not isinstance(rows, list) or len(rows) != EXPECTED_STATE_COUNT:
        raise AssertionError("the frozen F-state profile is incomplete")
    return [dict(row) for row in rows]


def recover_linear_state(prime: int, R: int) -> tuple[int, int]:
    _bound, states_by_R = source.enumerate_linear_source_states(prime)
    states = states_by_R.get(R)
    if not states:
        raise AssertionError(f"could not recover a linear state for ({prime}, {R})")
    return max(states)


def enumerate_candidates(
    row: dict[str, object],
) -> tuple[list[dict[str, object]], list[tuple[int, int]]]:
    factors = [(int(q), int(e)) for q, e in row["factorization"]]
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
    component_orders = [int(value) for value in row["component_orders"]]
    group_order = math.prod(component_orders)
    candidates = []
    for coordinates in itertools.product((-1, 0, 1), repeat=dimension):
        if not any(coordinates):
            continue
        phase_vector = [
            sympy.Rational(value)
            for value in dual_basis * sympy.Matrix(coordinates)
        ]
        active = tuple(
            index
            for index, value in enumerate(phase_vector)
            if mod_one(value) != 0
        )
        if not active:
            continue
        target_phase = sum(
            phase_vector[index] * target_preimage[index]
            for index in range(dimension)
        )
        if target_phase.q == 1:
            continue
        mass = mpmath.mpf(1)
        phase_budget = mpmath.mpf(0)
        for (_prime, exponent), phase in zip(factors, phase_vector):
            mass *= dirichlet_mass(exponent, phase)
            delta = min(rational_mpf(mod_one(phase)), 1 - rational_mpf(mod_one(phase)))
            phase_budget += min(mpmath.mpf(1), exponent * exponent * delta * delta)
        order = math.lcm(*(int(sympy.Rational(value).q) for value in phase_vector))
        candidates.append(
            {
                "coordinates": list(coordinates),
                "phase_vector": phase_vector,
                "active_support": list(active),
                "target_phase": sympy.Rational(target_phase),
                "character_order": order,
                "normalized_mass": mass,
                "phase_budget": phase_budget,
                "group_order": group_order,
            }
        )
    if not candidates:
        raise AssertionError("no nontrivial small dual candidate with nonintegral target phase")
    candidates.sort(
        key=lambda item: (
            -item["normalized_mass"],
            item["character_order"],
            len(item["active_support"]),
            sum(abs(value) for value in item["coordinates"]),
            tuple(item["coordinates"]),
        )
    )
    return candidates, factors


def map_state(row: dict[str, object]) -> dict[str, object]:
    candidates, factors = enumerate_candidates(row)
    selected = candidates[0]
    group_order = int(selected["group_order"])
    threshold = mpmath.mpf(1) / (group_order - 1)
    mass = selected["normalized_mass"]
    if mass + mpmath.mpf("1e-60") < threshold:
        raise AssertionError("bounded Fourier candidate misses the F lower bound")

    prime = int(row["prime"])
    R = int(row["R"])
    a, s = recover_linear_state(prime, R)
    blocks = [("s", s, s * R + 1), ("a", a, a * R + 1)]
    carriers = []
    for index in selected["active_support"]:
        q = factors[index][0]
        heights = [valuation(block, q) for _label, _t, block in blocks]
        chosen = 0 if heights[0] >= heights[1] else 1
        carriers.append(
            {
                "prime": q,
                "phase": fraction_pair(selected["phase_vector"][index]),
                "label": blocks[chosen][0],
                "height": heights[chosen],
                "heights_by_label": {
                    blocks[0][0]: heights[0],
                    blocks[1][0]: heights[1],
                },
            }
        )

    active_prime = None
    if len(selected["active_support"]) == 1:
        active_prime = factors[selected["active_support"][0]][0]
    quotient_test = stabilizer_data(
        factors, R, group_order, active_prime
    )

    return {
        "prime": prime,
        "R": R,
        "K": int(row["K"]),
        "factorization": [[q, exponent] for q, exponent in factors],
        "linear_state": {"a": a, "s": s},
        "dual_coordinates": selected["coordinates"],
        "phase_vector": [fraction_pair(value) for value in selected["phase_vector"]],
        "active_support": selected["active_support"],
        "character_order": int(selected["character_order"]),
        "target_phase_mod_one": fraction_pair(mod_one(selected["target_phase"])),
        "group_order": group_order,
        "normalized_fourier_mass": mpmath.nstr(mass, 60),
        "threshold": mpmath.nstr(threshold, 60),
        "threshold_ratio": mpmath.nstr(mass / threshold, 50),
        "phase_budget": mpmath.nstr(selected["phase_budget"], 50),
        "candidate_count": len(candidates),
        "carrier_vector": carriers,
        "single_active_quotient_test": quotient_test,
    }


def run(input_path: Path) -> dict[str, object]:
    records = [map_state(row) for row in load_rows(input_path)]
    ratios = [mpmath.mpf(record["threshold_ratio"]) for record in records]
    support_counts = Counter(len(record["active_support"]) for record in records)
    order_counts = Counter(record["character_order"] for record in records)
    color_counts = Counter(
        tuple(item["label"] for item in record["carrier_vector"])
        for record in records
    )
    return {
        "arithmetic": "Within the relation-lattice dual coefficient box {-1,0,1}^r, select the candidate with maximal normalized Fourier product subject to a nonintegral target phase, then record its exact rational phase and linear carrier vector.",
        "scope_note": "Finite bounded Fourier certificates only. The selected candidate is canonical within the stated coefficient box and target-phase filter; it is not asserted to be the global Fourier maximizer. The result is not a cross-state capacity contradiction or an all-prime selector theorem.",
        "input": input_path.name,
        "input_sha256": sha256(input_path),
        "state_count": len(records),
        "dual_coordinate_box": [-1, 1],
        "target_phase_filter": "nonintegral",
        "selected_support_counts": {
            str(key): int(value) for key, value in sorted(support_counts.items())
        },
        "selected_character_order_counts": {
            str(key): int(value) for key, value in sorted(order_counts.items())
        },
        "selected_color_counts": {
            "".join(key): int(value) for key, value in sorted(color_counts.items())
        },
        "minimum_threshold_ratio": mpmath.nstr(min(ratios), 50),
        "median_threshold_ratio": mpmath.nstr(sorted(ratios)[len(ratios) // 2], 50),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    mpmath.mp.dps = MP_DIGITS
    payload = run(args.input)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "state_count": payload["state_count"],
                "selected_support_counts": payload["selected_support_counts"],
                "selected_character_order_counts": payload["selected_character_order_counts"],
                "minimum_threshold_ratio": payload["minimum_threshold_ratio"],
                "median_threshold_ratio": payload["median_threshold_ratio"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
