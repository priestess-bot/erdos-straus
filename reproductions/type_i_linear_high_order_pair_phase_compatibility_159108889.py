#!/usr/bin/env python3
"""Verify quartic phase compatibility at the first split high-order G-state pair."""

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
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
GAUSSIAN_SCRIPT = ROOT / "reproductions" / "type_i_linear_gaussian_quartic_source_pullback_57399241.py"
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-high-order-pair-phase-compatibility-159108889-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
PRIME = 159_108_889
LEFT_R = 47_227
RIGHT_R = 53_036_295
SHARED_Q = 70_841


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("high_order_pair_phase_sources", SOURCE_SCRIPT)
gaussian = load_module("high_order_pair_phase_gaussian", GAUSSIAN_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_records(input_path: Path) -> dict[int, dict[str, object]]:
    """Load the two full-spectrum G states that share the split prime SHARED_Q."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full B>1-spectrum input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list):
        raise AssertionError("full B>1-spectrum input lacks profiles")
    profile = next((entry for entry in profiles if int(entry["prime"]) == PRIME), None)
    if not isinstance(profile, dict):
        raise AssertionError("the selected complete spectrum is absent")
    result = {}
    for R in (LEFT_R, RIGHT_R):
        record = next((entry for entry in profile["records"] if int(entry["R"]) == R), None)
        if (
            not isinstance(record, dict)
            or record["classification"] != "subgroup_character"
            or bool(record["target_in_generated_subgroup"])
        ):
            raise AssertionError("the selected high-order G state changed")
        result[R] = record
    return result


def order_four_separators(certificate: dict[str, object]) -> list[dict[str, object]]:
    """Enumerate every order-four character trivial on K support and nontrivial at -1."""
    component_orders = [
        int(component["order"])
        for component in certificate["components"]
        if isinstance(component, dict)
    ]
    allowed_coefficients = [
        [coefficient for coefficient in range(4) if coefficient * order % 4 == 0]
        for order in component_orders
    ]
    generators = [
        [int(value) for value in row]
        for row in certificate["generator_log_vectors"]
    ]
    target = [int(value) for value in certificate["target_log_vector_for_minus_one"]]
    separators = []
    for coefficients in itertools.product(*allowed_coefficients):
        generator_values = [
            sum(coefficient * logarithm for coefficient, logarithm in zip(coefficients, row))
            % 4
            for row in generators
        ]
        target_value = sum(
            coefficient * logarithm for coefficient, logarithm in zip(coefficients, target)
        ) % 4
        if any(generator_values) or target_value == 0:
            continue
        character_order = math.lcm(
            *[
                4 // math.gcd(4, coefficient)
                for coefficient in coefficients
                if coefficient
            ]
        )
        if character_order != 4:
            continue
        separators.append(
            {
                "coefficients": list(coefficients),
                "minus_one_quarter_exponent": target_value,
            }
        )
    return separators


def source_label_for_prime(
    R: int, q: int, states: list[tuple[int, int]]
) -> int:
    """Recover the unique endpoint block tR+1 containing q."""
    endpoints = sorted({endpoint for state in states for endpoint in state})
    matches = [endpoint for endpoint in endpoints if (endpoint * R + 1) % q == 0]
    if len(matches) != 1:
        raise AssertionError("shared K prime does not have one source-label block")
    return matches[0]


def phase_row(
    R: int, q: int, t: int, quartic_prime: int
) -> dict[str, object]:
    """Compute one componentwise quartic pullback row for a split local prime."""
    cofactor, remainder = divmod(R, quartic_prime)
    if remainder:
        raise AssertionError("quartic local prime does not divide R")
    pi = gaussian.primary_gaussian_factor(quartic_prime)
    rho = gaussian.primary_gaussian_factor(q)
    left = gaussian.quartic_exponent((q, 0), pi)
    pi_over_rho = gaussian.quartic_exponent(pi, rho)
    source_symbol = gaussian.quartic_exponent((-cofactor * t, 0), rho)
    if (
        q % 4 != 1
        or (t * R + 1) % q
        or left != (2 * pi_over_rho + source_symbol) % 4
    ):
        raise AssertionError("componentwise Gaussian quartic pullback failed")
    return {
        "quartic_local_prime": quartic_prime,
        "cofactor": cofactor,
        "primary_gaussian_factor_pi": list(pi),
        "quartic_character_exponent": left,
        "quartic_character_value": gaussian.exponent_label(left),
        "pi_over_rho_exponent": pi_over_rho,
        "pi_over_rho_value": gaussian.exponent_label(pi_over_rho),
        "source_symbol_exponent": source_symbol,
        "source_symbol_value": gaussian.exponent_label(source_symbol),
        "pullback_rhs_exponent": (2 * pi_over_rho + source_symbol) % 4,
    }


def audit_state(
    R: int,
    record: dict[str, object],
    states: list[tuple[int, int]],
    quartic_primes: tuple[int, ...],
    quadratic_primes: tuple[int, ...],
) -> dict[str, object]:
    """Recover one high-order separator and its exact phase balance at SHARED_Q."""
    K = int(record["K"])
    factors = sources.exact_factorization(K)
    certificate = sources.unit_group_subgroup_certificate(factors, R)
    depth = sources.two_power_character_depth(certificate)
    separators = order_four_separators(certificate)
    source_label = source_label_for_prime(R, SHARED_Q, states)
    if (
        int(depth["minimal_separating_two_power_character_order"]) != 4
        or SHARED_Q not in {prime for prime, _ in factors}
        or len(separators) != 2
        or any(row["minus_one_quarter_exponent"] != 2 for row in separators)
    ):
        raise AssertionError("selected state ceased to have its expected fourth-order boundary")
    rows = [phase_row(R, SHARED_Q, source_label, prime) for prime in quartic_primes]
    quadratic_exponents = [
        0 if int(sympy.legendre_symbol(SHARED_Q, prime)) == 1 else 2
        for prime in quadratic_primes
    ]
    phase_sum = (
        sum(quadratic_exponents)
        + sum(int(row["quartic_character_exponent"]) for row in rows)
    ) % 4
    if phase_sum:
        raise AssertionError("the fourth-order separator is not trivial on the shared K prime")
    return {
        "R": R,
        "K": K,
        "R_factorization": sources.factorization_payload(sources.exact_factorization(R)),
        "K_factorization": sources.factorization_payload(factors),
        "source_states": [list(state) for state in states],
        "shared_prime_source_label_t": source_label,
        "order_four_separators": separators,
        "quadratic_local_primes": list(quadratic_primes),
        "quadratic_character_exponents_at_shared_prime": quadratic_exponents,
        "quartic_phase_rows": rows,
        "total_separator_exponent_at_shared_prime": phase_sum,
    }


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Verify two compatible fourth-order phase balances at the same split K prime."""
    records = load_records(input_path)
    _, states_by_R = sources.enumerate_linear_source_states(PRIME)
    left = audit_state(
        LEFT_R,
        records[LEFT_R],
        states_by_R[LEFT_R],
        quartic_primes=(569,),
        quadratic_primes=(83,),
    )
    right = audit_state(
        RIGHT_R,
        records[RIGHT_R],
        states_by_R[RIGHT_R],
        quartic_primes=(13, 271_981),
        quadratic_primes=(3,),
    )
    signature = [
        (
            entry["R"],
            entry["shared_prime_source_label_t"],
            [row["quartic_local_prime"] for row in entry["quartic_phase_rows"]],
            [row["quartic_character_exponent"] for row in entry["quartic_phase_rows"]],
            entry["quadratic_character_exponents_at_shared_prime"],
        )
        for entry in (left, right)
    ]
    expected_signature = [
        (47_227, 3, [569], [2], [2]),
        (53_036_295, 3, [13, 271_981], [2, 0], [2]),
    ]
    if signature != expected_signature:
        raise AssertionError("shared-prime fourth-order phase profile changed")
    return {
        "arithmetic": (
            "at the two fourth-order G states for p=159108889 sharing q=70841, recover the "
            "separating fourth-order characters and verify every split local component satisfies the "
            "source-label quartic phase pullback"
        ),
        "scope_note": (
            "Both high-order phase balances are simultaneously trivial at q=70841. This is a boundary "
            "against automatic high-order collision incompatibility, not a terminal-certificate construction."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "prime": PRIME,
        "shared_split_K_prime": SHARED_Q,
        "shared_primary_gaussian_factor_rho": list(
            gaussian.primary_gaussian_factor(SHARED_Q)
        ),
        "states": [left, right],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
