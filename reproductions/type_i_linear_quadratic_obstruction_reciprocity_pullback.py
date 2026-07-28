#!/usr/bin/env python3
"""Audit the quadratic-character reciprocity pullback on complete linear spectra."""

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
SOURCE_SCRIPT = ROOT / "reproductions" / "type_i_global_linear_b1_failure_general_b_profile_500m.py"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-linear-quadratic-obstruction-reciprocity-pullback-results.json"
)
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


sources = load_module("quadratic_pullback_sources", SOURCE_SCRIPT)


def stable_sha256(rows: list[tuple[int, ...]]) -> str:
    payload = "\n".join(",".join(str(value) for value in row) for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def odd_squarefree_negative_conductors(R: int) -> list[int]:
    """Return squarefree m|R with (./m) odd, excluding the trivial character."""
    prime_support = [prime for prime, _ in sources.exact_factorization(R)]
    conductors = []
    for size in range(1, len(prime_support) + 1):
        for subset in itertools.combinations(prime_support, size):
            m = math.prod(subset)
            if m % 4 == 3:
                conductors.append(m)
    return conductors


def audit_prime(prime: int) -> dict[str, object]:
    """Check every valid q,t,m instance of the exact reciprocity identity."""
    bound, states_by_R = sources.enumerate_linear_source_states(prime)
    relation_rows: list[tuple[int, ...]] = []
    state_count = 0
    state_with_negative_conductor_count = 0
    prime_R_state_count = 0
    for R, states in states_by_R.items():
        conductors = odd_squarefree_negative_conductors(R)
        if sympy.isprime(R):
            prime_R_state_count += len(states)
        for a, s in states:
            state_count += 1
            if conductors:
                state_with_negative_conductor_count += 1
            K = (prime * R + 1) // 4
            odd_K_primes = [
                q for q, _ in sources.exact_factorization(K) if q % 2 == 1
            ]
            for q in odd_K_primes:
                endpoint_labels = [t for t in (a, s) if (t * R + 1) % q == 0]
                if not endpoint_labels:
                    raise AssertionError("odd K-prime divided neither linear block")
                if math.gcd(q, prime * R) != 1:
                    raise AssertionError("pullback prime is not a unit at pR")
                for t in endpoint_labels:
                    if prime % q != t % q:
                        raise AssertionError("block divisibility did not pull the label back to p")
                    for m in conductors:
                        c = R // m
                        left = int(sympy.jacobi_symbol(q, m))
                        right = int(sympy.jacobi_symbol(prime * c, q))
                        if left != right:
                            raise AssertionError("quadratic reciprocity pullback failed")
                        relation_rows.append((R, a, s, q, t, m, c, left, right))
    return {
        "prime": prime,
        "linear_source_coordinate_bound": bound,
        "complete_linear_R_count": len(states_by_R),
        "complete_directed_linear_source_count": state_count,
        "prime_R_directed_state_count": prime_R_state_count,
        "states_with_odd_negative_quadratic_conductor": state_with_negative_conductor_count,
        "verified_relation_count": len(relation_rows),
        "relation_sha256": stable_sha256(relation_rows),
    }


def run_audit(primes: tuple[int, ...] = PRESSURE_PRIMES) -> dict[str, object]:
    """Audit all complete pressure spectra without assuming a separator exists."""
    if tuple(sorted(set(primes))) != primes:
        raise ValueError("primes must be a strictly ascending tuple")
    profiles = [audit_prime(prime) for prime in primes]
    return {
        "arithmetic": (
            "for q|K odd, q|tR+1, and every odd squarefree m|R with m=3 (mod 4), "
            "quadratic reciprocity gives (q/m)=(p(R/m)/q)"
        ),
        "scope_note": (
            "The audit verifies a local identity for every eligible quadratic conductor. It does not assert "
            "that the character separates a given state, and it leaves the q=2 local condition explicit."
        ),
        "primes": list(primes),
        "profile_count": len(profiles),
        "complete_directed_linear_source_count": sum(
            int(profile["complete_directed_linear_source_count"]) for profile in profiles
        ),
        "prime_R_directed_state_count": sum(
            int(profile["prime_R_directed_state_count"]) for profile in profiles
        ),
        "states_with_odd_negative_quadratic_conductor": sum(
            int(profile["states_with_odd_negative_quadratic_conductor"])
            for profile in profiles
        ),
        "verified_relation_count": sum(int(profile["verified_relation_count"]) for profile in profiles),
        "profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
