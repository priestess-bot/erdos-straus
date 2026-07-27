#!/usr/bin/env python3
"""Audit reverse two-tail lifts of shortest Bradford certificates.

For each core prime in a finite range, recover its least-gap Type I/II
certificate. For every term in that target triple, enumerate every smaller
source denominator that preserves the other two terms under a one-coordinate
replacement. This audits genuine source-reading lifts, rather than the
marked scaled-first representations equivalent to target certificates.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "reverse-lift-shortest-certificate-10k-results.json"
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
TARGETED_BRIDGE = ROOT / "reproductions" / "targeted_descent_bridge.py"
DEFAULT_LIMIT = 10_000


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module(
    "reverse_lift_shortest_certificate_short_certificate", SHORT_CERTIFICATE
)
targeted_bridge = load_module(
    "reverse_lift_shortest_certificate_targeted_bridge", TARGETED_BRIDGE
)


def certificate_lifts(prime: int, certificate) -> list[dict[str, int]]:
    """Return every verified reverse lift for the three target coordinates."""
    if not short_certificate.verify_certificate(certificate):
        raise AssertionError("input certificate did not verify")
    target = (certificate.x, certificate.y, certificate.z)
    records: list[dict[str, int]] = []
    for position, target_term in enumerate(target):
        for lift in targeted_bridge.reverse_two_tail_lifts(prime, target_term):
            source = (
                lift["source_term"],
                *(
                    term
                    for index, term in enumerate(target)
                    if index != position
                ),
            )
            if Fraction(4, lift["source_denominator"]) != sum(
                (Fraction(1, term) for term in source), Fraction()
            ):
                raise AssertionError("reverse lift source identity did not verify")
            records.append(
                {
                    "replaced_target_position": position,
                    "replaced_target_term": target_term,
                    "source_denominator": lift["source_denominator"],
                    "source_term": lift["source_term"],
                }
            )
    return records


def run_audit(limit: int = DEFAULT_LIMIT) -> dict[str, object]:
    """Audit every core prime through the stated limit using exact arithmetic."""
    if limit < 73:
        raise ValueError("limit must be at least 73")
    spf = short_certificate.smallest_prime_factors(2 * limit + 1)
    rows: list[dict[str, object]] = []
    core_count = 0
    target_with_lift_count = 0
    total_lift_count = 0

    for prime in short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        core_count += 1
        certificate = short_certificate.shortest_gap_certificate(
            prime, prime - 2, spf
        )
        if certificate is None:
            raise AssertionError("finite core-prime certificate search failed")
        lifts = certificate_lifts(prime, certificate)
        if lifts:
            target_with_lift_count += 1
            total_lift_count += len(lifts)
            rows.append(
                {
                    "prime": prime,
                    "certificate_type": certificate.certificate_type,
                    "gap": certificate.gap,
                    "divisor": certificate.divisor,
                    "target_solution": [
                        certificate.x,
                        certificate.y,
                        certificate.z,
                    ],
                    "reverse_two_tail_lifts": lifts,
                }
            )

    return {
        "arithmetic": (
            "complete least-gap Bradford certificate search, exhaustive "
            "n=2,...,p-1 reverse two-tail enumeration for every target "
            "coordinate, and exact rational source/target identity checks"
        ),
        "scope_note": (
            "A finite audit of lifts preserving two terms of a least-gap "
            "certificate. It does not exclude other target certificates, "
            "one-denominator lifts, or any broader marked descent."
        ),
        "prime_limit": limit,
        "core_prime_count": core_count,
        "targets_with_reverse_two_tail_lift": target_with_lift_count,
        "total_reverse_two_tail_lifts": total_lift_count,
        "records": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
