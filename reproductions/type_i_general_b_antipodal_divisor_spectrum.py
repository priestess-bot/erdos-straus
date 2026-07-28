#!/usr/bin/env python3
"""Audit the antipodal divisor-spectrum identity on complete linear source spectra."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-general-b-antipodal-divisor-spectrum-results.json"
PRESSURE_PRIMES = (
    214_729,
    878_089,
    2_210_569,
    13_782_409,
    64_214_329,
    105_295_129,
    536_944_489,
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sources = load_module("antipodal_divisor_spectrum_sources", SOURCE_SCRIPT)


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    return hashlib.sha256(
        "\n".join(",".join(str(value) for value in row) for row in rows).encode("ascii")
    ).hexdigest()


def divisor_residues(value: int, modulus: int) -> set[int]:
    return {int(divisor) % modulus for divisor in sympy.divisors(value)}


def audit_modulus(prime: int, R: int, source_state_count: int) -> dict[str, int | bool]:
    """Directly compare divisor ratios with centered square-divisor residues."""
    K = (prime * R + 1) // 4
    A = divisor_residues(K, R)
    inverse_A = {pow(residue, -1, R) for residue in A}
    quotient_spectrum = {
        left * right % R for left in A for right in inverse_A
    }
    direct_centered_spectrum = {
        int(divisor) * pow(K, -1, R) % R for divisor in sympy.divisors(K * K)
    }
    antipodal_intersection = A & {(-residue) % R for residue in A}
    target_hit = R - 1 in direct_centered_spectrum
    if (
        quotient_spectrum != direct_centered_spectrum
        or target_hit != bool(antipodal_intersection)
    ):
        raise AssertionError("antipodal divisor-spectrum identity failed")
    return {
        "R": R,
        "K": K,
        "source_state_count": source_state_count,
        "K_divisor_residue_count": len(A),
        "centered_square_residue_count": len(direct_centered_spectrum),
        "antipodal_intersection_count": len(antipodal_intersection),
        "target_hit": target_hit,
    }


def audit_prime(prime: int) -> dict[str, object]:
    bound, states_by_R = sources.enumerate_linear_source_states(prime)
    records = [
        audit_modulus(prime, R, len(states)) for R, states in states_by_R.items()
    ]
    digest_rows = [
        (
            int(record["R"]),
            int(record["K"]),
            int(record["K_divisor_residue_count"]),
            int(record["centered_square_residue_count"]),
            int(record["antipodal_intersection_count"]),
            int(bool(record["target_hit"])),
        )
        for record in records
    ]
    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "complete_linear_R_count": len(records),
        "directed_linear_source_state_count": sum(len(states) for states in states_by_R.values()),
        "target_hit_R_count": sum(bool(record["target_hit"]) for record in records),
        "record_sha256": stable_sha256(digest_rows),
        "records": records,
    }


def run_audit(primes: tuple[int, ...] = PRESSURE_PRIMES) -> dict[str, object]:
    """Reproduce the exact antipodal identity on seven complete spectra."""
    if tuple(sorted(set(primes))) != primes:
        raise ValueError("primes must be a strictly ascending tuple")
    profiles = [audit_prime(prime) for prime in primes]
    return {
        "arithmetic": (
            "for A_R(K)={d mod R:d|K}, enumerate C_R(K) directly from K^2 and independently "
            "as A_R(K)A_R(K)^(-1); target -1 occurs exactly when A_R(K) meets -A_R(K)"
        ),
        "scope_note": (
            "This is an exact fixed-state identity. It does not imply that some state in every complete "
            "linear source spectrum has an antipodal collision."
        ),
        "primes": list(primes),
        "profile_count": len(profiles),
        "complete_linear_R_count": sum(int(profile["complete_linear_R_count"]) for profile in profiles),
        "directed_linear_source_state_count": sum(
            int(profile["directed_linear_source_state_count"]) for profile in profiles
        ),
        "target_hit_R_count": sum(int(profile["target_hit_R_count"]) for profile in profiles),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "profiles"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
