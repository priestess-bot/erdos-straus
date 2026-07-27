#!/usr/bin/env python3
"""Audit the quadratic external-source residue state along the k-divisor path.

For a core prime p and k | (p-1)/4, write

    n_k = p - (p-1)/(4k),  q_k = 4k-1,  M_k = k*n_k.

The complete quadratic external-source descent at k exists exactly when
-M_k modulo q_k is a residue of a divisor of M_k^2.  Complementary divisors
have the same target residue, so this residue condition also supplies an
eligible factor e <= M_k.

This audit reconstructs that state path for the H19 residuals already
independently classified by type_ii_h19_quadratic_descent_closure.py.  It is a
finite diagnostic for a multi-source selector, not a uniform theorem.
"""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / "reproductions" / "type-ii-h19-quadratic-descent-closure-20m-results.json"
)
RESULTS = ROOT / "reproductions" / "type-ii-multisource-descent-state-h19-20m-results.json"
RESIDUE_SCRIPT = ROOT / "reproductions" / "divisor_residue_structure.py"
SHORT_CERTIFICATE_SCRIPT = ROOT / "reproductions" / "short_certificate.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


residue = load_module("multisource_descent_residue", RESIDUE_SCRIPT)
short_certificate = load_module(
    "multisource_descent_short_certificate", SHORT_CERTIFICATE_SCRIPT
)


def factorization(value: int, spf: list[int]) -> tuple[tuple[int, int], ...]:
    if value < 1 or value >= len(spf):
        raise ValueError("SPF table does not cover the requested value")
    result: list[tuple[int, int]] = []
    while value > 1:
        prime = spf[value]
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        result.append((prime, exponent))
    return tuple(result)


def combined_factorization(
    first: int, second: int, spf: list[int]
) -> tuple[tuple[int, int], ...]:
    counts: dict[int, int] = {}
    for value in (first, second):
        for prime, exponent in factorization(value, spf):
            counts[prime] = counts.get(prime, 0) + exponent
    return tuple(sorted(counts.items()))


def euler_phi(value: int) -> int:
    result = value
    factor = 2
    remaining = value
    while factor * factor <= remaining:
        if remaining % factor == 0:
            while remaining % factor == 0:
                remaining //= factor
            result -= result // factor
        factor = 3 if factor == 2 else factor + 2
    if remaining > 1:
        result -= result // remaining
    return result


def source_state(prime: int, k: int, spf: list[int]) -> dict[str, object]:
    """Return the complete divisor-residue state for one allowed source."""
    base = (prime - 1) // 4
    if prime % 24 != 1 or k < 1 or base % k:
        raise ValueError("require a core prime and k | (p-1)/4")
    q = 4 * k - 1
    source = prime - base // k
    if (q + 1) * source != q * prime + 1:
        raise AssertionError("source relation failed")
    preserved = k * source
    if math.gcd(preserved, q) != 1:
        raise AssertionError("the divisor-residue group must consist of units")
    factors = combined_factorization(k, source, spf)
    divisor_residues = residue.divisor_residues_from_factorization(
        tuple((factor, 2 * exponent) for factor, exponent in factors), q
    )
    target = (-preserved) % q
    if target == 0:
        raise AssertionError("target must be a unit")
    success = target in divisor_residues
    witness = short_certificate.quadratic_factor_external_source_descent_witness(
        prime, spf, k
    )
    if success != (witness is not None):
        raise AssertionError("residue criterion and explicit lift disagree")
    return {
        "k": k,
        "q": q,
        "source_denominator": source,
        "preserved_denominator": preserved,
        "source_factorization": [
            {"prime": factor, "exponent": exponent}
            for factor, exponent in factorization(source, spf)
        ],
        "preserved_factorization": [
            {"prime": factor, "exponent": exponent} for factor, exponent in factors
        ],
        "target_residue": target,
        "divisor_residue_count": len(divisor_residues),
        "unit_group_size": euler_phi(q),
        "target_in_divisor_residues": success,
        "witness_factor": None if witness is None else witness.factor,
        "certificate_gap": None if witness is None else witness.certificate.gap,
    }


def profile_prime(prime: int, spf: list[int]) -> dict[str, object]:
    """Walk allowed k in increasing order through the first strict lift."""
    base = (prime - 1) // 4
    states: list[dict[str, object]] = []
    for k in short_certificate.positive_divisors_from_spf(base, spf):
        state = source_state(prime, k, spf)
        states.append(state)
        if state["target_in_divisor_residues"]:
            break
    if not states or not states[-1]["target_in_divisor_residues"]:
        raise AssertionError("the supplied prime has no quadratic descent witness")
    return {
        "prime": prime,
        "base": base,
        "first_success_k": states[-1]["k"],
        "prior_failure_count": len(states) - 1,
        "states_through_first_success": states,
    }


def run_audit(input_path: Path = DEFAULT_INPUT) -> dict[str, object]:
    """Profile every H19 residual listed by an independent closure artifact."""
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    limit = int(payload["prime_limit"])
    primes = [int(record["prime"]) for record in payload["records"]]
    if not primes:
        raise ValueError("closure artifact has no residual records")
    spf = short_certificate.smallest_prime_factors(limit)
    profiles = [profile_prime(prime, spf) for prime in primes]
    first_success_histogram = Counter(
        int(profile["first_success_k"]) for profile in profiles
    )
    failure_histogram = Counter(
        int(state["k"])
        for profile in profiles
        for state in profile["states_through_first_success"][:-1]
    )
    return {
        "arithmetic": (
            "exact SPF factorizations, complete square-divisor residue sets, "
            "and cross-checks against explicit rational strict-lift constructors"
        ),
        "scope_note": (
            "A finite state-path audit on the H19 residuals supplied by the "
            "input closure artifact. It does not prove a uniform k selector."
        ),
        "input_artifact": input_path.name,
        "prime_limit": limit,
        "residual_count": len(profiles),
        "first_success_k_histogram": {
            str(k): count for k, count in sorted(first_success_histogram.items())
        },
        "prior_failure_k_histogram": {
            str(k): count for k, count in sorted(failure_histogram.items())
        },
        "total_prior_failure_states": sum(
            int(profile["prior_failure_count"]) for profile in profiles
        ),
        "maximum_prior_failure_count": max(
            int(profile["prior_failure_count"]) for profile in profiles
        ),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
