#!/usr/bin/env python3
"""Audit the quadratic shadow of the one fourth-order adversarial G state."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
ORDER_FOUR_SCRIPT = ROOT / "reproductions" / "type_i_linear_order_four_separator_boundary_57399241.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-order-four-shadow-compatibility-57399241-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
PRIME = 57_399_241
HIGHER_ORDER_R = 444_955
EXPECTED_RELATIONS = [
    (13, 95, 95),
    (13, 5_451, 5_451),
    (13, 5_607, 623),
    (13, 7_687, 7_687),
    (13, 8_519, 8_519),
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("order_four_shadow_sources", SOURCE_SCRIPT)
order_four = load_module("order_four_shadow_boundary", ORDER_FOUR_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def quadratic_shadow_conductor(coefficients: list[int]) -> int:
    """Return the conductor of the square of a quarter-turn character.

    The coordinate convention is the one in the order-four boundary:
    (mod 5 quartic, mod 7 quadratic, mod 12713 quartic). Squaring removes
    the mod-7 factor and retains a local quadratic factor exactly at an odd
    quartic coordinate.
    """
    at_five, _, at_12713 = coefficients
    conductor = 1
    if at_five % 2:
        conductor *= 5
    if at_12713 % 2:
        conductor *= 12_713
    return conductor


def load_prime_profile(input_path: Path) -> dict[str, object]:
    """Load the complete adversarial spectrum containing the high-order state."""
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
        raise AssertionError("the adversarial source spectrum changed")
    return profile


def quadratic_conductor(record: dict[str, object]) -> int | None:
    """Recover the odd quadratic separator conductor of a G state, if it exists."""
    certificate = sources.unit_group_subgroup_certificate(
        sources.exact_factorization(int(record["K"])), int(record["R"])
    )
    depth = sources.two_power_character_depth(certificate)
    if int(depth["minimal_separating_two_power_character_order"]) != 2:
        return None
    support = sources.quadratic_character_local_support(certificate)
    conductor = int(support["minimal_quadratic_conductor"])
    if conductor % 4 != 3:
        raise AssertionError("quadratic separator is not odd at minus one")
    return conductor


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Check the mixed quadratic-shadow law on every actual shared odd prime."""
    boundary = order_four.run_audit(input_path)
    profile = load_prime_profile(input_path)
    records = [dict(record) for record in profile["records"]]
    high = next(record for record in records if int(record["R"]) == HIGHER_ORDER_R)
    if (
        high["classification"] != "subgroup_character"
        or bool(high["target_in_generated_subgroup"])
        or int(boundary["order_four_separator_count"]) != 2
    ):
        raise AssertionError("the distinguished order-four state changed")

    shadow_conductors = {
        quadratic_shadow_conductor(
            [int(value) for value in separator["coefficients"]]
        )
        for separator in boundary["order_four_separators"]
    }
    if shadow_conductors != {12_713}:
        raise AssertionError("conjugate order-four separators lost their common shadow")
    shadow = shadow_conductors.pop()
    high_factors = sources.exact_factorization(int(high["K"]))
    relations: list[dict[str, int]] = []
    for record in records:
        R = int(record["R"])
        if R == HIGHER_ORDER_R or record["classification"] != "subgroup_character":
            continue
        conductor = quadratic_conductor(record)
        if conductor is None:
            continue
        shared = math.gcd(int(high["K"]), int(record["K"]))
        for q, _ in sources.exact_factorization(shared):
            if q == 2:
                continue
            modulus_difference, remainder = divmod(abs(HIGHER_ORDER_R - R), 4)
            if (
                remainder
                or modulus_difference % q
                or math.gcd(q, shadow * conductor) != 1
                or int(sympy.jacobi_symbol(q, shadow)) != 1
                or int(sympy.jacobi_symbol(q, conductor)) != 1
                or int(sympy.jacobi_symbol(shadow * conductor, q))
                != int(sympy.legendre_symbol(-1, q))
            ):
                raise AssertionError("mixed quadratic-shadow compatibility failed")
            relations.append(
                {
                    "shared_odd_prime": q,
                    "quadratic_G_R": R,
                    "quadratic_G_conductor": conductor,
                    "modulus_difference_over_four": modulus_difference,
                    "shadow_conductor": shadow,
                    "shadow_times_quadratic_over_prime": int(
                        sympy.jacobi_symbol(shadow * conductor, q)
                    ),
                    "minus_one_over_prime": int(sympy.legendre_symbol(-1, q)),
                }
            )
    relations.sort(
        key=lambda row: (
            row["quadratic_G_R"],
            row["shared_odd_prime"],
            row["quadratic_G_conductor"],
        )
    )
    relation_signature = [
        (
            row["shared_odd_prime"],
            row["quadratic_G_R"],
            row["quadratic_G_conductor"],
        )
        for row in relations
    ]
    if relation_signature != EXPECTED_RELATIONS:
        raise AssertionError("mixed quadratic-shadow relation set changed")
    if any(
        q not in [prime for prime, _ in high_factors]
        for q, _, _ in relation_signature
    ):
        raise AssertionError("a relation used a prime outside the high-order K support")

    return {
        "arithmetic": (
            "for a fourth-order G separator, square its character to obtain an even quadratic shadow; "
            "when an odd K-prime is shared with a quadratic G state, verify the source-modulus difference "
            "and the reciprocal identity (mD/q)=(-1/q)"
        ),
        "scope_note": (
            "This is a necessary compatibility law. The five actual relations satisfy it, so it does not "
            "force a target hit or provide a fourth-reciprocity pullback."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "prime": PRIME,
        "higher_order_R": HIGHER_ORDER_R,
        "higher_order_K_factorization": sources.factorization_payload(high_factors),
        "higher_order_separator_count": int(boundary["order_four_separator_count"]),
        "quadratic_shadow_conductor": shadow,
        "shared_odd_prime_relation_count": len(relations),
        "relations": relations,
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
