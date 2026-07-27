#!/usr/bin/env python3
"""Classify failures of the adaptive external-source descent family.

This audit starts only after the four direct families used by external_source.py
have failed. It distinguishes failure of the marked descent selector from
failure of direct certificates: an escape can still have an ordinary
external-source certificate or a bounded Type II AC-ray certificate.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "adaptive-external-escape-results.json"


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


external_source = load_module("adaptive_escape_external_source", "external_source.py")
type_ii_ac_ray = load_module("adaptive_escape_type_ii_ac_ray", "type_ii_ac_ray.py")
short_certificate = external_source.short_certificate


def factorization(value: int, spf: list[int]) -> list[dict[str, int]]:
    """Return a JSON-friendly prime factorization."""
    if value < 1 or value >= len(spf):
        raise ValueError("SPF table does not cover the requested value")
    result: list[dict[str, int]] = []
    while value > 1:
        prime = spf[value]
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        result.append({"prime": prime, "exponent": exponent})
    return result


def adaptive_k_profile(prime: int, k: int, spf: list[int]) -> dict[str, object]:
    """Record the exact factor-residue obstruction for one allowed k."""
    q = 4 * k - 1
    n = (q * prime + 1) // (q + 1)
    factors = factorization(n, spf)
    return {
        "k": k,
        "q": q,
        "source_denominator": n,
        "factorization": factors,
        "prime_residues_mod_q": sorted({entry["prime"] % q for entry in factors}),
    }


def type_ii_entry(
    prime: int, ac_bound: int, spf: list[int]
) -> dict[str, int] | None:
    witness = type_ii_ac_ray.ray_witness(prime, ac_bound, spf)
    if witness is None:
        return None
    a, c, k, h, certificate = witness
    return {
        "a": a,
        "c": c,
        "k": k,
        "h": h,
        "gap": certificate.gap,
        "divisor": certificate.divisor,
    }


def even_source_distance_entry(
    prime: int, distance_limit: int, spf: list[int]
) -> dict[str, int] | None:
    """Return the first marked even-source descent in the odd-distance fan."""
    for distance in range(1, min(distance_limit, prime - 1) + 1, 2):
        witness = short_certificate.even_source_distance_descent_witness(
            prime, distance, spf
        )
        if witness is None:
            continue
        return {
            "distance": distance,
            "source_denominator": witness.source_denominator,
            "k": witness.k,
            "q": witness.q,
            "factor": witness.factor,
            "gap": witness.certificate.gap,
            "divisor": witness.certificate.divisor,
        }
    return None


def quadratic_external_source_entry(
    prime: int, spf: list[int]
) -> dict[str, int] | None:
    """Return the complete quadratic-tail external-source descent witness."""
    witness = short_certificate.quadratic_factor_external_source_descent_witness(
        prime, spf
    )
    if witness is None:
        return None
    return {
        "source_denominator": witness.source_denominator,
        "k": witness.k,
        "q": witness.q,
        "factor": witness.factor,
        "gap": witness.certificate.gap,
        "divisor": witness.certificate.divisor,
    }


def shifted_quadratic_external_source_entry(
    prime: int, spf: list[int]
) -> dict[str, int] | None:
    """Exhaust the allowed nonzero shifts of the quadratic external-source fan."""
    for k in range(1, (prime - 1) // 4 + 1):
        shift = prime % (4 * k)
        if shift == 0 or (4 * k - 1) % shift:
            continue
        witness = short_certificate.shifted_quadratic_factor_external_source_descent_witness(
            prime, k, shift, spf
        )
        if witness is None:
            continue
        return {
            "source_denominator": witness.source_denominator,
            "k": witness.k,
            "shift": shift,
            "q": witness.q,
            "factor": witness.factor,
            "gap": witness.certificate.gap,
            "divisor": witness.certificate.divisor,
        }
    return None


def even_standard_two_tail_entry(
    prime: int, spf: list[int]
) -> dict[str, int] | None:
    """Exhaust the complete even standard large-tail descent family."""
    source = prime // 2 + 1
    if source % 2:
        source += 1
    for source in range(source, prime, 2):
        witness = short_certificate.even_standard_two_tail_descent_witness(
            prime, source, spf
        )
        if witness is None:
            continue
        return {
            "source_denominator": witness.source_denominator,
            "factor": witness.factor,
            "gap": witness.certificate.gap,
            "divisor": witness.certificate.divisor,
        }
    return None


def three_divisible_standard_two_tail_entry(
    prime: int, spf: list[int]
) -> dict[str, int] | None:
    """Exhaust the complete three-divisible standard large-tail family."""
    source = prime // 2 + 1
    source += (-source) % 3
    for source in range(source, prime, 3):
        witness = short_certificate.three_divisible_standard_two_tail_descent_witness(
            prime, source, spf
        )
        if witness is None:
            continue
        return {
            "source_denominator": witness.source_denominator,
            "factor": witness.factor,
            "gap": witness.certificate.gap,
            "divisor": witness.certificate.divisor,
        }
    return None


def run_experiment(
    limit: int, source_limit: int, ac_bound: int, distance_limit: int = 99
) -> dict[str, object]:
    """Return an exact finite classification of adaptive-descent escapes."""
    if limit < 73 or source_limit < 1 or ac_bound < 1 or distance_limit < 1:
        raise ValueError("limit must be at least 73 and bounds must be positive")

    source_trial_primes = short_certificate.primes_up_to(
        math.isqrt(4 * limit + source_limit) + 1
    )
    descent_spf = short_certificate.smallest_prime_factors(limit)
    ray_spf = short_certificate.smallest_prime_factors(limit + 4 * ac_bound**3)
    residual = [
        prime
        for prime in short_certificate.primes_up_to(limit)
        if prime % 24 == 1
        and not external_source.covered_by_direct_families(
            prime, source_trial_primes
        )
    ]

    escapes: list[dict[str, object]] = []
    descent_hits = 0
    for prime in residual:
        if short_certificate.external_source_descent_witness(prime, descent_spf):
            descent_hits += 1
            continue

        base = (prime - 1) // 4
        profiles = [
            adaptive_k_profile(prime, k, descent_spf)
            for k in short_certificate.positive_divisors_from_spf(base, descent_spf)
        ]
        source_witness = external_source.smallest_external_source_witness(
            prime, source_limit, source_trial_primes
        )
        normal_form = (
            None
            if source_witness is None
            else external_source.external_source_factor_ray_normal_form(
                prime, *source_witness
            )
        )
        even_source_witness = even_source_distance_entry(
            prime, distance_limit, descent_spf
        )
        quadratic_witness = quadratic_external_source_entry(prime, descent_spf)
        shifted_quadratic_witness = (
            None
            if quadratic_witness is not None or even_source_witness is not None
            else shifted_quadratic_external_source_entry(prime, descent_spf)
        )
        complete_even_source_witness = (
            None
            if (
                quadratic_witness is not None
                or even_source_witness is not None
                or shifted_quadratic_witness is not None
            )
            else even_source_distance_entry(prime, prime - 2, descent_spf)
        )
        even_standard_witness = (
            None
            if (
                quadratic_witness is not None
                or even_source_witness is not None
                or shifted_quadratic_witness is not None
                or complete_even_source_witness is not None
            )
            else even_standard_two_tail_entry(prime, descent_spf)
        )
        three_standard_witness = (
            None
            if (
                quadratic_witness is not None
                or even_source_witness is not None
                or shifted_quadratic_witness is not None
                or complete_even_source_witness is not None
                or even_standard_witness is not None
            )
            else three_divisible_standard_two_tail_entry(prime, descent_spf)
        )
        ac_witness = type_ii_entry(prime, ac_bound, ray_spf)
        escape_kinds = []
        if three_standard_witness is not None:
            escape_kinds.append("three-divisible-standard-two-tail-descent")
        if even_standard_witness is not None:
            escape_kinds.append("even-standard-two-tail-descent")
        if complete_even_source_witness is not None:
            escape_kinds.append("complete-even-source-distance-descent")
        if shifted_quadratic_witness is not None:
            escape_kinds.append("shifted-quadratic-external-source-descent")
        if quadratic_witness is not None:
            escape_kinds.append("quadratic-external-source-descent")
        if even_source_witness is not None:
            escape_kinds.append("even-source-distance-descent")
        if normal_form is not None:
            escape_kinds.append("external-source-direct")
        if ac_witness is not None:
            escape_kinds.append("type-II-AC-ray")
        if not escape_kinds:
            escape_kinds.append("unclassified-within-bounds")

        escapes.append(
            {
                "prime": prime,
                "p_minus_one_over_four_factorization": factorization(
                    base, descent_spf
                ),
                "adaptive_k_profiles": profiles,
                "quadratic_external_source_descent": quadratic_witness,
                "even_source_distance_descent": even_source_witness,
                "shifted_quadratic_external_source_descent": shifted_quadratic_witness,
                "complete_even_source_distance_descent": complete_even_source_witness,
                "even_standard_two_tail_descent": even_standard_witness,
                "three_divisible_standard_two_tail_descent": three_standard_witness,
                "external_source_factor_ray": normal_form,
                "type_ii_ac_ray": ac_witness,
                "classification": escape_kinds,
            }
        )

    return {
        "arithmetic": (
            "exact SPF factorizations, exact divisor-residue checks, and "
            "fractions.Fraction certificate verification in the imported constructors"
        ),
        "scope_note": (
            "This classifies failures of one marked descent selector after four "
            "direct families. It does not classify all Erdos--Straus certificates "
            "or prove that either finite search bound is uniform."
        ),
        "prime_limit": limit,
        "source_limit": source_limit,
        "ac_bound": ac_bound,
        "even_source_distance_limit": distance_limit,
        "direct_families": ["m=3", "(p+1)/2", "p+4", "4p+1"],
        "residual_after_direct_families": len(residual),
        "adaptive_descent_hits": descent_hits,
        "adaptive_descent_escapes": len(escapes),
        "escapes_with_quadratic_external_source_descent": sum(
            record["quadratic_external_source_descent"] is not None
            for record in escapes
        ),
        "escapes_with_even_source_distance_descent": sum(
            record["even_source_distance_descent"] is not None
            for record in escapes
        ),
        "escapes_with_shifted_quadratic_external_source_descent": sum(
            record["shifted_quadratic_external_source_descent"] is not None
            for record in escapes
        ),
        "joint_escapes_with_complete_even_source_distance_descent": sum(
            record["complete_even_source_distance_descent"] is not None
            for record in escapes
        ),
        "joint_escapes_with_even_standard_two_tail_descent": sum(
            record["even_standard_two_tail_descent"] is not None
            for record in escapes
        ),
        "joint_escapes_with_three_divisible_standard_two_tail_descent": sum(
            record["three_divisible_standard_two_tail_descent"] is not None
            for record in escapes
        ),
        "escapes_with_recorded_descent": sum(
            record["quadratic_external_source_descent"] is not None
            or record["even_source_distance_descent"] is not None
            or record["shifted_quadratic_external_source_descent"] is not None
            or record["complete_even_source_distance_descent"] is not None
            or record["even_standard_two_tail_descent"] is not None
            or record["three_divisible_standard_two_tail_descent"] is not None
            for record in escapes
        ),
        "escapes_with_external_source_window": sum(
            record["external_source_factor_ray"] is not None for record in escapes
        ),
        "escapes_with_type_ii_ac_ray": sum(
            record["type_ii_ac_ray"] is not None for record in escapes
        ),
        "escape_records": escapes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--source-limit", type=int, default=128)
    parser.add_argument("--ac-bound", type=int, default=14)
    parser.add_argument("--distance-limit", type=int, default=99)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_experiment(
        args.limit, args.source_limit, args.ac_bound, args.distance_limit
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
