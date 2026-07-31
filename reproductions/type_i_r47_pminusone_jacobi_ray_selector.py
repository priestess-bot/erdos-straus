#!/usr/bin/env python3
"""Reproduce the Jacobi boundary for the R=47 empty-AP p-1 rays."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-i-r47-pminusone-jacobi-ray-selector-results.json"
)
N = 6_238_440
M = N // 8
EXPECTED_N_FACTORIZATION = {2: 3, 3: 2, 5: 1, 13: 1, 31: 1, 43: 1}
PARITIES = (("even", 1), ("odd", 3))
EXACT_SELECTORS = {8: "even", 24: "odd", 40: "even"}
IFF_SAMPLES = (
    (2, 8),
    (2, 40),
    (6, 8),
    (6, 40),
    (21, 24),
    (35, 24),
)


def factorization(value: int) -> dict[int, int]:
    return {
        int(prime): int(exponent)
        for prime, exponent in sympy.factorint(value).items()
    }


def factorization_payload(value: int) -> list[dict[str, int]]:
    return [
        {"prime": prime, "exponent": exponent}
        for prime, exponent in factorization(value).items()
    ]


def centered_spectrum(value: int, modulus: int) -> set[int]:
    spectrum = {1}
    for prime, exponent in factorization(value).items():
        spectrum = {
            residue * pow(prime, centered_exponent, modulus) % modulus
            for residue in spectrum
            for centered_exponent in range(-exponent, exponent + 1)
        }
    return spectrum


def jacobi(value: int, modulus: int) -> int:
    return int(sympy.jacobi_symbol(value % modulus, modulus))


def admissible_scales(u_mod_4: int) -> list[int]:
    scales = []
    for divisor in sympy.divisors(M):
        scale = 8 * int(divisor)
        complement = N // scale
        if complement * u_mod_4 % 4 == 1:
            scales.append(scale)
    return scales


def fixed_support_row(scale: int) -> dict[str, object]:
    modulus = scale - 1
    if modulus % 8 != 7:
        raise AssertionError("the ray modulus left the 7 mod 8 class")

    factor_rows = []
    for prime, exponent in factorization(scale).items():
        symbol = jacobi(prime, modulus)
        if symbol != 1:
            raise AssertionError("a fixed scale prime left the Jacobi kernel")
        factor_rows.append(
            {"prime": prime, "exponent": exponent, "jacobi_symbol": symbol}
        )

    fixed_spectrum = centered_spectrum(scale, modulus)
    if jacobi(-1, modulus) != -1:
        raise AssertionError("the antipodal target lost its negative character")
    if modulus - 1 in fixed_spectrum:
        raise AssertionError("the fixed centered spectrum hit the target")
    if any(jacobi(residue, modulus) != 1 for residue in fixed_spectrum):
        raise AssertionError("the fixed centered spectrum left the Jacobi kernel")

    return {
        "S": scale,
        "R": modulus,
        "complement_N_over_S": N // scale,
        "S_factorization": factor_rows,
        "jacobi_minus_one": -1,
        "fixed_centered_spectrum_size": len(fixed_spectrum),
        "fixed_centered_target_hit": False,
    }


def exact_selector_row(scale: int, applicable_parity: str) -> dict[str, object]:
    modulus = scale - 1
    fixed_spectrum = centered_spectrum(scale, modulus)
    units = [
        residue
        for residue in range(1, modulus)
        if math.gcd(residue, modulus) == 1
    ]
    positive_classes = [
        residue for residue in units if jacobi(residue, modulus) == 1
    ]
    negative_classes = [
        residue for residue in units if jacobi(residue, modulus) == -1
    ]
    if fixed_spectrum != set(positive_classes):
        raise AssertionError("an exact selector spectrum is not the Jacobi kernel")
    if len(positive_classes) != len(negative_classes):
        raise AssertionError("the Jacobi character is not a two-coset split")

    return {
        "S": scale,
        "R": modulus,
        "applicable_t_parity": applicable_parity,
        "fixed_centered_spectrum": sorted(fixed_spectrum),
        "positive_unit_classes": positive_classes,
        "negative_unit_classes": negative_classes,
        "exact_criterion": (
            "the K_S target hits iff A_S has a prime divisor in a negative "
            "Jacobi class"
        ),
    }


def iff_sample(parameter: int, scale: int) -> dict[str, object]:
    parity = "even" if parameter % 2 == 0 else "odd"
    if EXACT_SELECTORS[scale] != parity:
        raise AssertionError("the sample uses an inapplicable exact selector")

    prime = 1 + N * (2 * parameter + 1)
    modulus = scale - 1
    quotient, remainder = divmod(prime - 1, scale)
    if remainder or quotient % 4 != 1:
        raise AssertionError("the p-1 scale is not admissible")
    cofactor = (modulus * quotient + 1) // 4
    K = (modulus * prime + 1) // 4
    if K != scale * cofactor or 4 * cofactor % modulus != 1:
        raise AssertionError("the K_S=sA_S factorization failed")

    cofactor_factorization = factorization(cofactor)
    negative_prime_factors = [
        factor
        for factor in cofactor_factorization
        if jacobi(factor, modulus) == -1
    ]
    centered_target_hit = modulus - 1 in centered_spectrum(K, modulus)
    if centered_target_hit != bool(negative_prime_factors):
        raise AssertionError("the exact Jacobi iff failed on a sample")

    return {
        "progression_parameter": parameter,
        "p": prime,
        "p_is_prime": bool(sympy.isprime(prime)),
        "S": scale,
        "R": modulus,
        "A_S": cofactor,
        "A_S_factorization": factorization_payload(cofactor),
        "negative_jacobi_prime_factors": negative_prime_factors,
        "centered_target_hit": centered_target_hit,
    }


def run() -> dict[str, object]:
    if factorization(N) != EXPECTED_N_FACTORIZATION:
        raise AssertionError("the canonical progression modulus changed")

    parity_payload: dict[str, object] = {}
    parity_scale_sets: dict[str, set[int]] = {}
    for parity, u_mod_4 in PARITIES:
        scales = admissible_scales(u_mod_4)
        if len(scales) != 24:
            raise AssertionError("an admissible parity does not have 24 scales")
        parity_scale_sets[parity] = set(scales)
        parity_payload[parity] = {
            "two_t_plus_one_mod_4": u_mod_4,
            "admissible_scale_count": len(scales),
            "admissible_scales": scales,
            "fixed_support_rows": [fixed_support_row(scale) for scale in scales],
        }

    all_v2_exact_scales = {8 * int(divisor) for divisor in sympy.divisors(M)}
    if (
        parity_scale_sets["even"] & parity_scale_sets["odd"]
        or parity_scale_sets["even"] | parity_scale_sets["odd"]
        != all_v2_exact_scales
    ):
        raise AssertionError("the parity menus do not partition the 48 scales")
    for scale, parity in EXACT_SELECTORS.items():
        if scale not in parity_scale_sets[parity]:
            raise AssertionError("an exact selector has the wrong parity")

    return {
        "schema_version": "r47-pminusone-jacobi-ray-selector/v1",
        "scope_note": (
            "This artifact verifies finite divisor and residue-class identities. "
            "It does not infer AP-wide coverage from the displayed samples."
        ),
        "canonical_progression": {
            "N": N,
            "N_factorization": factorization_payload(N),
            "formula": "p(t)=1+N(2t+1)",
        },
        "derived_identity": (
            "For admissible S, h=(p-1)/S is 1 mod 4, R=S-1, "
            "A_S=(Rh+1)/4, and K_S=S*A_S."
        ),
        "jacobi_obstruction": (
            "Every prime supported on S has Jacobi symbol +1 modulo R, "
            "whereas -1 has symbol -1; fixed S-supported divisors cannot hit."
        ),
        "parity_menus": parity_payload,
        "exact_selectors": [
            exact_selector_row(scale, parity)
            for scale, parity in EXACT_SELECTORS.items()
        ],
        "directed_iff_samples": [
            iff_sample(parameter, scale) for parameter, scale in IFF_SAMPLES
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    payload = run()
    if args.verify:
        stored = json.loads(args.output.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError("stored result does not match recomputation")
        print(json.dumps(payload["exact_selectors"], ensure_ascii=False, indent=2))
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload["exact_selectors"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
