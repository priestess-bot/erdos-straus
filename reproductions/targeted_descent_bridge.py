#!/usr/bin/env python3
"""Exact reverse-lift audit for a chosen direct certificate.

For a target term t in a decomposition of 4/p, enumerate every n < p for
which replacing t by one source denominator a preserves the other two target
terms. This tests the entire two-tail-preserving bridge for that fixed target
solution, not all possible lifts.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "targeted-bridge-2451289-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location("short_certificate", SHORT_CERTIFICATE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def load_type_ii_ac_ray():
    filename = ROOT / "reproductions" / "type_ii_ac_ray.py"
    spec = importlib.util.spec_from_file_location("targeted_bridge_type_ii_ray", filename)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load type_ii_ac_ray.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def reverse_two_tail_lifts(prime: int, target_term: int) -> list[dict[str, int]]:
    """Enumerate every strict source that preserves the other two target terms."""
    if prime < 2 or target_term < 1:
        raise ValueError("prime and target_term must be positive")
    witnesses: list[dict[str, int]] = []
    for source_denominator in range(2, prime):
        numerator = source_denominator * prime * target_term
        denominator = (
            source_denominator * prime
            + 4 * target_term * (prime - source_denominator)
        )
        if numerator % denominator:
            continue
        source_term = numerator // denominator
        if source_term < 1:
            continue
        if (
            Fraction(4, source_denominator)
            != Fraction(1, source_term)
            + Fraction(4, prime)
            - Fraction(1, target_term)
        ):
            raise AssertionError("reverse lift identity did not verify")
        witnesses.append(
            {
                "source_denominator": source_denominator,
                "source_term": source_term,
            }
        )
    return witnesses


def type_ii_solution(
    prime: int, a: int, c: int, k: int
) -> dict[str, int]:
    """Recover and verify the raw Type II ray target solution."""
    certificate = short_certificate.type_ii_raw_ray_certificate(prime, a, c, k)
    if certificate is None:
        raise ValueError("the supplied AC ray does not yield a certificate")
    h = 4 * a * c * k - 1
    return {
        "a": a,
        "c": c,
        "k": k,
        "h": h,
        "gap": certificate.gap,
        "x": certificate.x,
        "divisor": certificate.divisor,
        "y": certificate.y,
        "z": certificate.z,
    }


def run_audit(prime: int, a: int, c: int, k: int) -> dict[str, object]:
    solution = type_ii_solution(prime, a, c, k)
    target_terms = [solution["x"], solution["y"], solution["z"]]
    reverse = [
        {
            "target_term": target_term,
            "reverse_two_tail_lifts": reverse_two_tail_lifts(prime, target_term),
        }
        for target_term in target_terms
    ]
    return {
        "arithmetic": (
            "exact integer division and fractions.Fraction verification of every "
            "reverse two-tail lift"
        ),
        "scope_note": (
            "The audit fixes one Type II target triple. An empty result excludes "
            "only lifts preserving two terms of that triple; it is not a proof "
            "that no other descent or certificate exists."
        ),
        "prime": prime,
        "type_ii_raw_ray": solution,
        "reverse_two_tail_by_replaced_target_term": reverse,
        "total_reverse_two_tail_lifts": sum(
            len(entry["reverse_two_tail_lifts"]) for entry in reverse
        ),
    }


def ac_first_term_audit(prime: int, ac_bound: int) -> dict[str, object]:
    """Test every distinct bounded-AC target first term for a two-tail bridge."""
    if ac_bound < 1:
        raise ValueError("ac_bound must be positive")
    ray = load_type_ii_ac_ray()
    spf = short_certificate.smallest_prime_factors(prime + 4 * ac_bound**3)
    unique: dict[tuple[int, int, int, int, int], tuple[int, int, int, int]] = {}
    for a in range(1, ac_bound + 1):
        for c in range(1, ac_bound + 1):
            for h in ray.divisors(prime + 4 * a * a * c, spf):
                if h <= 1 or (h + 1) % (4 * a * c):
                    continue
                k = (h + 1) // (4 * a * c)
                certificate = short_certificate.type_ii_raw_ray_certificate(
                    prime, a, c, k
                )
                if certificate is None:
                    continue
                key = (
                    certificate.gap,
                    certificate.x,
                    certificate.divisor,
                    certificate.y,
                    certificate.z,
                )
                unique.setdefault(key, (a, c, k, h))

    records = []
    for (gap, x, divisor, y, z), (a, c, k, h) in unique.items():
        records.append(
            {
                "a": a,
                "c": c,
                "k": k,
                "h": h,
                "gap": gap,
                "x": x,
                "divisor": divisor,
                "reverse_two_tail_lifts_at_x": reverse_two_tail_lifts(prime, x),
            }
        )
    return {
        "ac_bound": ac_bound,
        "distinct_target_solutions": len(records),
        "solutions_with_first_term_bridge": sum(
            bool(record["reverse_two_tail_lifts_at_x"]) for record in records
        ),
        "records": sorted(records, key=lambda record: record["x"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=2_451_289)
    parser.add_argument("--a", type=int, default=1)
    parser.add_argument("--c", type=int, default=2)
    parser.add_argument("--k", type=int, default=13)
    parser.add_argument("--ac-bound", type=int)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.prime, args.a, args.c, args.k)
    if args.ac_bound is not None:
        payload["ac_first_term_audit"] = ac_first_term_audit(
            args.prime, args.ac_bound
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
