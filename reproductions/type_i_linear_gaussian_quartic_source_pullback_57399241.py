#!/usr/bin/env python3
"""Recover the Gaussian quartic source-label pullback at the high-order G state."""

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
    ROOT / "reproductions" / "type-i-linear-gaussian-quartic-source-pullback-57399241-results.json"
)
EXPECTED_INPUT_SHA256 = "71b24dc30fce218f02d7c81cd8c716b6d60e874e7701161e0887575f2d5f3d2f"
PRIME = 57_399_241
R = 444_955
R_QUARTIC_PRIME = 12_713
R_COFACTOR = 35
EXPECTED_ROWS = [
    (13, 3, [3, 2], 2, 0, 2),
    (51_341, 3, [-221, 50], 2, 3, 0),
    (9_566_533, 43, [1_647, 2_618], 0, 2, 0),
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("gaussian_quartic_pullback_sources", SOURCE_SCRIPT)
order_four = load_module("gaussian_quartic_pullback_order_four", ORDER_FOUR_SCRIPT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(value: tuple[int, int]) -> int:
    """Return the Gaussian norm."""
    real, imaginary = value
    return real * real + imaginary * imaginary


def conjugate(value: tuple[int, int]) -> tuple[int, int]:
    """Return the Gaussian conjugate."""
    real, imaginary = value
    return real, -imaginary


def primary_gaussian_factor(prime: int) -> tuple[int, int]:
    """Choose the primary factor a+bi with b>0 of a rational prime 1 mod 4."""
    if prime % 4 != 1 or not sympy.isprime(prime):
        raise ValueError("a split odd rational prime is required")
    for first in range(1, math.isqrt(prime) + 1):
        second_squared = prime - first * first
        second = math.isqrt(second_squared)
        if second * second != second_squared:
            continue
        for real, imaginary in ((first, second), (second, first)):
            if real % 2 == 0 or imaginary % 2:
                continue
            for signed_real in (real, -real):
                candidate = signed_real, imaginary
                if (signed_real + imaginary) % 4 == 1:
                    return candidate
    raise AssertionError("failed to recover a primary Gaussian factor")


def quartic_exponent(
    numerator: tuple[int, int], denominator: tuple[int, int]
) -> int:
    """Return e in {0,1,2,3} for the Gaussian quartic symbol i^e."""
    prime = norm(denominator)
    if not sympy.isprime(prime) or prime % 4 != 1:
        raise ValueError("the denominator must be a split Gaussian prime")
    real, imaginary = denominator
    if imaginary % prime == 0:
        raise AssertionError("a non-real Gaussian denominator is required")
    imaginary_unit = (-real * pow(imaginary, -1, prime)) % prime
    numerator_real, numerator_imaginary = numerator
    residue = (numerator_real + numerator_imaginary * imaginary_unit) % prime
    if residue == 0:
        raise ValueError("the quartic symbol numerator is not a unit")
    value = pow(residue, (prime - 1) // 4, prime)
    roots = {
        1: 0,
        imaginary_unit: 1,
        prime - 1: 2,
        (-imaginary_unit) % prime: 3,
    }
    if value not in roots:
        raise AssertionError("quartic power did not produce a fourth root of unity")
    return roots[value]


def exponent_label(exponent: int) -> str:
    """Render a fourth-root exponent as a stable label."""
    return ("1", "i", "-1", "-i")[exponent % 4]


def load_state(input_path: Path) -> tuple[dict[str, object], list[tuple[int, int]]]:
    """Recover the one high-order G state and its directed source labels."""
    if file_sha256(input_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("the full B>1-spectrum input changed")
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    profiles = payload.get("profiles")
    if not isinstance(profiles, list):
        raise AssertionError("full B>1-spectrum input lacks profiles")
    profile = next(
        (entry for entry in profiles if int(entry["prime"]) == PRIME), None
    )
    if not isinstance(profile, dict):
        raise AssertionError("the adversarial profile is absent")
    record = next((entry for entry in profile["records"] if int(entry["R"]) == R), None)
    if (
        not isinstance(record, dict)
        or record["classification"] != "subgroup_character"
        or bool(record["target_in_generated_subgroup"])
    ):
        raise AssertionError("the high-order G state changed")
    _, states_by_R = sources.enumerate_linear_source_states(PRIME)
    return record, states_by_R[R]


def source_label_for_prime(q: int, labels: list[tuple[int, int]]) -> int:
    """Find the unique endpoint t for which q divides tR+1."""
    endpoint_values = {endpoint for state in labels for endpoint in state}
    matches = [endpoint for endpoint in sorted(endpoint_values) if (endpoint * R + 1) % q == 0]
    if len(matches) != 1:
        raise AssertionError("a K prime did not have one source-label block")
    return matches[0]


def run_audit(input_path: Path = INPUT) -> dict[str, object]:
    """Verify the phase-preserving Gaussian pullback for every high-state K prime."""
    boundary = order_four.run_audit(input_path)
    record, source_states = load_state(input_path)
    K = int(record["K"])
    factors = sources.exact_factorization(K)
    pi = primary_gaussian_factor(R_QUARTIC_PRIME)
    if (
        R != R_COFACTOR * R_QUARTIC_PRIME
        or pi != (13, 112)
        or source_states != [(3, 43), (43, 3)]
        or int(boundary["order_four_separator_count"]) != 2
        or factors != [(13, 1), (51_341, 1), (9_566_533, 1)]
    ):
        raise AssertionError("the fixed fourth-order source data changed")

    rows: list[dict[str, object]] = []
    for q, _ in factors:
        if q % 4 != 1:
            raise AssertionError("the Gaussian lift needs a split K prime")
        t = source_label_for_prime(q, source_states)
        rho = primary_gaussian_factor(q)
        left = quartic_exponent((q, 0), pi)
        pi_over_rho = quartic_exponent(pi, rho)
        conjugate_pi_over_rho = quartic_exponent(conjugate(pi), rho)
        pi_over_conjugate_rho = quartic_exponent(pi, conjugate(rho))
        source_term = quartic_exponent((-R_COFACTOR * t, 0), rho)
        if (
            (R_COFACTOR * t * R_QUARTIC_PRIME + 1) % q
            or (left - pi_over_rho - pi_over_conjugate_rho) % 4
            or (source_term + pi_over_rho + conjugate_pi_over_rho) % 4
            or (pi_over_conjugate_rho + conjugate_pi_over_rho) % 4
            or left != (2 * pi_over_rho + source_term) % 4
        ):
            raise AssertionError("Gaussian quartic source pullback failed")
        legendre_at_seven = int(sympy.legendre_symbol(q, 7))
        if (
            left not in (0, 2)
            or (1 if left == 0 else -1) != legendre_at_seven
        ):
            raise AssertionError("the order-four separator ceased to be trivial on K")
        rows.append(
            {
                "K_prime": q,
                "source_endpoint_t": t,
                "primary_gaussian_factor_rho": list(rho),
                "quartic_character_exponent_at_12713": left,
                "quartic_character_value_at_12713": exponent_label(left),
                "pi_over_rho_exponent": pi_over_rho,
                "pi_over_rho_value": exponent_label(pi_over_rho),
                "source_symbol_exponent": source_term,
                "source_symbol_value": exponent_label(source_term),
                "pullback_rhs_exponent": (2 * pi_over_rho + source_term) % 4,
                "legendre_q_over_7": legendre_at_seven,
            }
        )
    signature = [
        (
            int(row["K_prime"]),
            int(row["source_endpoint_t"]),
            list(row["primary_gaussian_factor_rho"]),
            int(row["quartic_character_exponent_at_12713"]),
            int(row["pi_over_rho_exponent"]),
            int(row["source_symbol_exponent"]),
        )
        for row in rows
    ]
    if signature != EXPECTED_ROWS:
        raise AssertionError("Gaussian quartic pullback profile changed")

    return {
        "arithmetic": (
            "for r=12713=N(pi), q=N(rho), and q dividing t*35*r+1, verify the "
            "Gaussian quartic pullback (q/pi)_4=(pi/rho)_4^2*(-35t/rho)_4"
        ),
        "scope_note": (
            "This preserves the quartic phase that the quadratic shadow loses, but it is a fixed-state "
            "identity and does not itself compare the varying source moduli of another G or F state."
        ),
        "input": input_path.name,
        "input_sha256": file_sha256(input_path),
        "prime": PRIME,
        "R": R,
        "R_factorization": sources.factorization_payload(sources.exact_factorization(R)),
        "gaussian_factor_pi": list(pi),
        "K": K,
        "K_factorization": sources.factorization_payload(factors),
        "source_states": [list(state) for state in source_states],
        "pullback_relation_count": len(rows),
        "relations": rows,
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
