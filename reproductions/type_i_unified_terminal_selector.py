#!/usr/bin/env python3
"""Verify the unified terminal-first receipts for near pairs and dyadic transfers.

The selector deliberately stops at arithmetic even predecessors.  Without a
nonempty marked solution set and a global lift, neither receipt is promoted to
a recursive edge.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NEAR_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-target-fiber-neighbor-profile-600m-results.json"
)
DYADIC_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-linear-target-fiber-dyadic-non-near-profile-600m-results.json"
)
FOURIER_INPUT = (
    ROOT
    / "reproductions"
    / "type-i-fixed-layer-stabilizer-fourier-results.json"
)
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-unified-terminal-selector-results.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation_two(value: int) -> int:
    if value <= 0:
        raise ValueError("2-adic valuation requires a positive integer")
    return (value & -value).bit_length() - 1


def residue_power(base: int, exponent: int, modulus: int) -> int:
    if exponent >= 0:
        return pow(base, exponent, modulus)
    return pow(pow(base, -1, modulus), -exponent, modulus)


def target_residue(primes: list[int], exponents: list[int], modulus: int) -> int:
    residue = 1
    for prime, exponent in zip(primes, exponents):
        residue = residue * residue_power(prime, exponent, modulus) % modulus
    return residue


def verify_type_i_identity(prime: int, modulus: int, K: int) -> None:
    if modulus <= 3 or modulus % 4 != 3:
        raise AssertionError("invalid Type I modulus")
    if prime <= modulus or 4 * K != prime * modulus + 1:
        raise AssertionError("Type I identity changed")
    if math.gcd(prime, modulus) != 1 or math.gcd(K, modulus) != 1:
        raise AssertionError("Type I coprimality failed")


def near_pair_certificate(
    prime: int,
    modulus: int,
    K: int,
    support_primes: list[int],
    support_budgets: list[int],
    left: list[int],
    right: list[int],
) -> dict[str, object]:
    verify_type_i_identity(prime, modulus, K)
    if len(support_primes) != len(support_budgets):
        raise AssertionError("support shape mismatch")
    if len(left) != len(support_primes) or len(right) != len(support_primes):
        raise AssertionError("near-pair vector shape mismatch")
    if left == right:
        raise AssertionError("near pair must be distinct")
    for vector in (left, right):
        if any(abs(exponent) > budget for exponent, budget in zip(vector, support_budgets)):
            raise AssertionError("target vector leaves its exponent box")
        if target_residue(support_primes, vector, modulus) != (-1) % modulus:
            raise AssertionError("target vector is not in the -1 fiber")
    if any(
        abs(left_i - right_i) > budget
        for left_i, right_i, budget in zip(left, right, support_budgets)
    ):
        raise AssertionError("vectors are not a coordinate-budget near pair")

    def ratio_for(first: list[int], second: list[int]) -> Fraction:
        numerator = 1
        denominator = 1
        for q, exponent in zip(support_primes, (a - b for a, b in zip(first, second))):
            if exponent > 0:
                numerator *= q**exponent
            elif exponent < 0:
                denominator *= q**(-exponent)
        return Fraction(numerator, denominator)

    ratio = ratio_for(left, right)
    if ratio >= 1:
        left, right = right, left
        ratio = ratio_for(left, right)
    if not 0 < ratio < 1:
        raise AssertionError("near-pair ratio is not nontrivial")
    if K % ratio.denominator:
        raise AssertionError("near-pair ratio does not produce an integer U")

    U = K * ratio.numerator // ratio.denominator
    E = 4 * U
    difference = 4 * K - E
    if difference % modulus:
        raise AssertionError("near-pair terminal has no integral n")
    n = difference // modulus
    if not (
        0 < U < K
        and (4 * K * K) % E == 0
        and E % modulus == 1 % modulus
        and E <= 4 * K - 4 * modulus
        and 0 < n < prime
        and n % 4 == 0
    ):
        raise AssertionError("near-pair terminal arithmetic failed")

    return {
        "certificate_type": "target_fiber_neighbor_terminal",
        "selector_status": "analysis_evidence",
        "phase": "TERMINAL_FIRST",
        "state_class": "hit",
        "terminal_kind": "even_predecessor",
        "recursive_edge_eligible": False,
        "lift_status": "unproved",
        "proof_boundary": "arithmetic_terminal_only",
        "prime": prime,
        "R": modulus,
        "K": K,
        "support_primes": support_primes,
        "support_budgets": support_budgets,
        "near_pair": {"z": left, "w": right},
        "ratio_fraction": [ratio.numerator, ratio.denominator],
        "terminal": {
            "U": U,
            "E": E,
            "n": n,
            "base_solution": [n // 2, n, n],
        },
    }


def dyadic_certificate(
    prime: int,
    modulus: int,
    K: int,
    a: int,
    b: int,
    j: int,
) -> dict[str, object]:
    verify_type_i_identity(prime, modulus, K)
    L = 2 * K
    if j < 1 or a <= 0 or b <= 0 or math.gcd(a, b) != 1:
        raise AssertionError("invalid dyadic witness")
    if L % a or L % b:
        raise AssertionError("dyadic witness is not supported by L")
    if (a - pow(2, j, modulus) * b) % modulus:
        raise AssertionError("dyadic congruence failed")

    lambda_two = valuation_two(L)
    alpha = valuation_two(a)
    beta = valuation_two(b)
    if not 1 <= j <= lambda_two + alpha - beta:
        raise AssertionError("dyadic exponent leaves the 2-adic budget")
    if not a < (2**j) * b:
        raise AssertionError("dyadic orientation is not descending")

    E_fraction = Fraction(2 * L * a, b * (2**j))
    if E_fraction.denominator != 1:
        raise AssertionError("dyadic E is not integral")
    E = E_fraction.numerator
    difference = 2 * L - E
    if difference % modulus:
        raise AssertionError("dyadic terminal has no integral n")
    n = difference // modulus
    if not (
        E > 0
        and E % 2 == 0
        and (L * L) % E == 0
        and E % modulus == 1 % modulus
        and 0 < n < prime
        and n % 2 == 0
    ):
        raise AssertionError("dyadic terminal arithmetic failed")

    return {
        "certificate_type": "generalized_dyadic_terminal",
        "selector_status": "analysis_evidence",
        "phase": "TERMINAL_FIRST",
        "state_class": "hit",
        "terminal_kind": "even_predecessor",
        "recursive_edge_eligible": False,
        "lift_status": "unproved",
        "proof_boundary": "arithmetic_terminal_only",
        "prime": prime,
        "R": modulus,
        "K": K,
        "L": L,
        "a": a,
        "b": b,
        "j": j,
        "two_adic_budget": {
            "lambda": lambda_two,
            "alpha": alpha,
            "beta": beta,
            "upper_bound": lambda_two + alpha - beta,
        },
        "terminal": {
            "E": E,
            "n": n,
            "base_solution": [n // 2, n, n],
        },
    }


def fixed_fourier_certificate(payload: dict[str, object]) -> dict[str, object]:
    receipt = payload["receipt"]
    if not isinstance(receipt, dict):
        raise AssertionError("Fourier receipt shape changed")
    typed = receipt.get("typed_certificate")
    if not isinstance(typed, dict):
        raise AssertionError("typed Fourier certificate missing")
    expected = {
        "certificate_type": "fixed_layer_quotient_fourier",
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "carrier_mapping_status": "unproved",
        "finite_order_debt_fraction": [1, 36],
    }
    for key, value in expected.items():
        if typed.get(key) != value:
            raise AssertionError(f"Fourier typed field changed: {key}")
    return {
        **typed,
        "phase": "DUAL_CERTIFICATE",
        "proof_boundary": "state_internal_dual_only",
    }


def build_results() -> dict[str, object]:
    near_payload = json.loads(NEAR_INPUT.read_text(encoding="utf-8"))
    near_record = next(record for record in near_payload["records"] if record["near_pair"])
    near_certificate = near_pair_certificate(
        int(near_record["prime"]),
        int(near_record["R"]),
        int(near_record["K"]),
        [int(value) for value in near_record["support_primes"]],
        [int(value) for value in near_record["support_budgets"]],
        [int(value) for value in near_record["minimum_pair"]["z"]],
        [int(value) for value in near_record["minimum_pair"]["w"]],
    )

    dyadic_payload = json.loads(DYADIC_INPUT.read_text(encoding="utf-8"))
    dyadic_record = dyadic_payload["records"][0]
    dyadic_terminal = dyadic_record["terminal"]
    dyadic_certificate_value = dyadic_certificate(
        int(dyadic_record["prime"]),
        int(dyadic_record["R"]),
        int(dyadic_record["K"]),
        int(dyadic_terminal["a"]),
        int(dyadic_terminal["b"]),
        int(dyadic_terminal["j"]),
    )

    fourier_payload = json.loads(FOURIER_INPUT.read_text(encoding="utf-8"))
    fourier_certificate = fixed_fourier_certificate(fourier_payload)

    return {
        "schema_version": 1,
        "arithmetic": (
            "Unified terminal-first receipt for target-fiber near pairs, generalized dyadic "
            "even predecessors, and fixed-layer quotient Fourier analysis."
        ),
        "selector_order": [
            "direct_type_i_or_type_ii",
            "target_fiber_neighbor_terminal",
            "generalized_dyadic_terminal",
            "fixed_layer_quotient_fourier",
        ],
        "scope_note": (
            "The first two receipts verify arithmetic even predecessors only. They remain "
            "analysis_evidence until a nonempty marked lift and E1-E5 are supplied; the "
            "Fourier receipt is state-internal dual evidence."
        ),
        "source_sha256": {
            NEAR_INPUT.name: sha256(NEAR_INPUT),
            DYADIC_INPUT.name: sha256(DYADIC_INPUT),
            FOURIER_INPUT.name: sha256(FOURIER_INPUT),
        },
        "receipts": [near_certificate, dyadic_certificate_value, fourier_certificate],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build_results(), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.verify:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("stored unified result does not match regenerated output")
        print("verified", args.output)
        return
    args.output.write_text(rendered, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
