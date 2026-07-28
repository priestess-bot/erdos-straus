#!/usr/bin/env python3
"""Recover the genuine order-four separator at one adversarial linear G state."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-order-four-separator-boundary-57399241-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
PRIME = 57_399_241
MODULUS = 444_955
EXPECTED_K = 6_385_019_819_789
EXPECTED_K_FACTORS = [(13, 1), (51_341, 1), (9_566_533, 1)]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("order_four_separator_sources", SOURCE_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_state(input_path: Path = INPUT) -> dict[str, object]:
    """Recover the frozen G state from the complete 200-prime spectrum."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full B>1-spectrum input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list):
        raise AssertionError("full B>1-spectrum input lacks profiles")
    profile = next(
        (entry for entry in profiles if int(entry["prime"]) == PRIME), None
    )
    if (
        not isinstance(profile, dict)
        or profile["B_eq_1_hit_R"]
        or int(profile["classification_counts"]["hit"]) != 1
    ):
        raise AssertionError("the adversarial prime profile changed")
    state = next(
        (entry for entry in profile["records"] if int(entry["R"]) == MODULUS), None
    )
    if (
        not isinstance(state, dict)
        or state["classification"] != "subgroup_character"
        or bool(state["target_in_generated_subgroup"])
        or int(state["general_B_target_divisor_count"]) != 0
    ):
        raise AssertionError("the distinguished order-four boundary changed")
    return state


def order_dividing_four_coefficients() -> list[tuple[int, int, int]]:
    """Parameterize all order-at-most-four characters in quarter-turn coordinates.

    The local component orders are 4, 6, and 12712.  The entries respectively
    encode the coefficients of a 4th root at 5, a quadratic character at 7,
    and a 4th root at 12713.
    """
    return [
        (at_five, at_seven, at_12713)
        for at_five in range(4)
        for at_seven in range(2)
        for at_12713 in range(4)
    ]


def quarter_exponent(
    coefficient: tuple[int, int, int], logarithm: list[int]
) -> int:
    """Return the exponent in i^e for a CRT-local character."""
    at_five, at_seven, at_12713 = coefficient
    log_five, log_seven, log_12713 = logarithm
    return (at_five * log_five + 2 * at_seven * log_seven + at_12713 * log_12713) % 4


def character_order(coefficient: tuple[int, int, int]) -> int:
    """Return the exact order of the character represented by the coefficient."""
    at_five, at_seven, at_12713 = coefficient
    local_orders = (
        1 if at_five == 0 else 4 // math.gcd(4, at_five),
        1 if at_seven == 0 else 2,
        1 if at_12713 == 0 else 4 // math.gcd(4, at_12713),
    )
    return math.lcm(*local_orders)


def character_conductor(coefficient: tuple[int, int, int]) -> int:
    """Return the conductor of the CRT-local character."""
    at_five, at_seven, at_12713 = coefficient
    conductor = 1
    if at_five:
        conductor *= 5
    if at_seven:
        conductor *= 7
    if at_12713:
        conductor *= 12_713
    return conductor


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Enumerate all low-order characters trivial on this state’s K support."""
    state = load_state(input_path)
    bound, states_by_R = sources.enumerate_linear_source_states(PRIME)
    source_states = states_by_R[MODULUS]
    K = (PRIME * MODULUS + 1) // 4
    factors = sources.exact_factorization(K)
    certificate = sources.unit_group_subgroup_certificate(factors, MODULUS)
    depth = sources.two_power_character_depth(certificate)
    generator_logs = [
        [int(value) for value in logarithm]
        for logarithm in certificate["generator_log_vectors"]
    ]
    target_log = [int(value) for value in certificate["target_log_vector_for_minus_one"]]
    if (
        K != EXPECTED_K
        or factors != EXPECTED_K_FACTORS
        or source_states != [(3, 43), (43, 3)]
        or int(bound) != 4_374
        or certificate["target_in_generated_subgroup"]
        or depth["minimal_separating_two_power_character_order"] != 4
    ):
        raise AssertionError("the order-four state arithmetic changed")

    rows = []
    for coefficient in order_dividing_four_coefficients():
        generator_exponents = [quarter_exponent(coefficient, logarithm) for logarithm in generator_logs]
        target_exponent = quarter_exponent(coefficient, target_log)
        if any(generator_exponents):
            continue
        rows.append(
            {
                "coefficients": list(coefficient),
                "character_order": character_order(coefficient),
                "conductor": character_conductor(coefficient),
                "generator_quarter_exponents": generator_exponents,
                "minus_one_quarter_exponent": target_exponent,
            }
        )

    quadratic_rows = [row for row in rows if int(row["character_order"]) <= 2]
    separating_rows = [
        row
        for row in rows
        if int(row["minus_one_quarter_exponent"]) == 2
    ]
    if (
        len(rows) != 4
        or len(quadratic_rows) != 2
        or any(int(row["minus_one_quarter_exponent"]) for row in quadratic_rows)
        or [row["coefficients"] for row in separating_rows] != [[0, 1, 1], [0, 1, 3]]
        or any(int(row["character_order"]) != 4 for row in separating_rows)
        or any(int(row["conductor"]) != 88_991 for row in separating_rows)
    ):
        raise AssertionError("low-order character enumeration changed")

    return {
        "arithmetic": (
            "enumerate every order-dividing-four CRT character modulo 5*7*12713 that is trivial "
            "on the prime support of K; exactly two conjugate order-four characters separate -1, "
            "while no quadratic character does"
        ),
        "scope_note": (
            "This is one local G-state boundary. It identifies the exact fourth-order character but "
            "does not supply a fourth-reciprocity pullback or force a target hit at another source modulus."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "prime": PRIME,
        "R": MODULUS,
        "linear_source_coordinate_bound": bound,
        "source_states": [list(state) for state in source_states],
        "K": K,
        "K_factorization": sources.factorization_payload(factors),
        "classification": state["classification"],
        "target_in_generated_subgroup": certificate["target_in_generated_subgroup"],
        "minimal_separating_two_power_character_order": depth[
            "minimal_separating_two_power_character_order"
        ],
        "components": certificate["components"],
        "generator_primes": certificate["generator_primes"],
        "generator_log_vectors": generator_logs,
        "target_log_vector_for_minus_one": target_log,
        "order_dividing_four_character_count": 32,
        "K_trivial_order_dividing_four_characters": rows,
        "K_trivial_quadratic_character_count": len(quadratic_rows),
        "quadratic_separator_count": sum(
            int(row["minus_one_quarter_exponent"]) == 2 for row in quadratic_rows
        ),
        "order_four_separator_count": len(separating_rows),
        "order_four_separators": separating_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
