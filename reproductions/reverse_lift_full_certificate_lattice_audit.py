#!/usr/bin/env python3
"""Find the first genuine reverse lift in the full Bradford certificate lattice.

For each core prime, enumerate every Type I/II divisor certificate in the
natural gap range. At each target triple, test every one-coordinate
two-tail-preserving reverse lift. The first verified edge is recorded; a
miss means that the entire finite certificate lattice was exhausted.

This is deliberately a target-side audit. It can identify a promising
marked-state relation, but selecting the target certificate first is not an
inductive construction of the source marker.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = (
    ROOT / "reproductions" / "reverse-lift-full-certificate-lattice-10k-results.json"
)
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
    "reverse_lift_full_lattice_short_certificate", SHORT_CERTIFICATE
)
targeted_bridge = load_module(
    "reverse_lift_full_lattice_targeted_bridge", TARGETED_BRIDGE
)


def all_certificates(
    prime: int, spf: list[int]
) -> list[short_certificate.GapCertificate]:
    """Enumerate all valid Bradford certificates in a deterministic order."""
    certificates: list[short_certificate.GapCertificate] = []
    for gap in range(3, prime - 1, 4):
        x = (prime + gap) // 4
        for divisor in short_certificate.divisors_of_square(x, spf):
            if (prime * x + divisor) % gap == 0:
                y = (prime * x + divisor) // gap
                numerator = prime * (x + prime * x * x // divisor)
                if numerator % gap == 0:
                    certificate = short_certificate.GapCertificate(
                        prime, "I", gap, x, divisor, y, numerator // gap
                    )
                    if short_certificate.verify_certificate(certificate):
                        certificates.append(certificate)
            if divisor <= x and (x + divisor) % gap == 0:
                y = prime * (x + divisor) // gap
                numerator = prime * (x + x * x // divisor)
                if numerator % gap == 0:
                    certificate = short_certificate.GapCertificate(
                        prime, "II", gap, x, divisor, y, numerator // gap
                    )
                    if short_certificate.verify_certificate(certificate):
                        certificates.append(certificate)
    return certificates


def first_reverse_lift(
    prime: int, spf: list[int]
) -> tuple[int, short_certificate.GapCertificate | None, dict[str, int] | None]:
    """Return first lattice edge, or None after an exhaustive miss."""
    checked = 0
    for certificate in all_certificates(prime, spf):
        checked += 1
        target = (certificate.x, certificate.y, certificate.z)
        for position, target_term in enumerate(target):
            for lift in targeted_bridge.reverse_two_tail_lifts(prime, target_term):
                source = (
                    lift["source_term"],
                    *(term for index, term in enumerate(target) if index != position),
                )
                if Fraction(4, lift["source_denominator"]) != sum(
                    (Fraction(1, term) for term in source), Fraction()
                ):
                    raise AssertionError("reverse lift source identity did not verify")
                return (
                    checked,
                    certificate,
                    {
                        "replaced_target_position": position,
                        "replaced_target_term": target_term,
                        "source_denominator": lift["source_denominator"],
                        "source_term": lift["source_term"],
                    },
                )
    return checked, None, None


def run_audit(limit: int = DEFAULT_LIMIT) -> dict[str, object]:
    """Run the complete-lattice first-hit audit with exact rational checks."""
    if limit < 73:
        raise ValueError("limit must be at least 73")
    spf = short_certificate.smallest_prime_factors(2 * limit + 1)
    records: list[dict[str, object]] = []
    misses: list[int] = []
    core_count = 0
    certificate_candidates_checked = 0

    for prime in short_certificate.primes_up_to(limit):
        if prime % 24 != 1:
            continue
        core_count += 1
        checked, certificate, lift = first_reverse_lift(prime, spf)
        certificate_candidates_checked += checked
        if certificate is None or lift is None:
            misses.append(prime)
            continue
        records.append(
            {
                "prime": prime,
                "certificate_type": certificate.certificate_type,
                "gap": certificate.gap,
                "divisor": certificate.divisor,
                "target_solution": [certificate.x, certificate.y, certificate.z],
                "certificate_candidates_checked_before_first_hit": checked,
                "reverse_two_tail_lift": lift,
            }
        )

    source_denominators = [
        record["reverse_two_tail_lift"]["source_denominator"] for record in records
    ]
    return {
        "arithmetic": (
            "complete Bradford Type I/II divisor-certificate enumeration until "
            "the first edge (or through the whole lattice on a miss), exhaustive "
            "n=2,...,p-1 reverse two-tail enumeration at each checked target, "
            "and exact rational source/target identity checks"
        ),
        "scope_note": (
            "The selected source marker is recovered after choosing a target "
            "certificate. Thus a hit is evidence for a candidate marked-state "
            "relation, not an inductive selector or a proof for all primes."
        ),
        "prime_limit": limit,
        "core_prime_count": core_count,
        "captured_count": len(records),
        "misses": misses,
        "certificate_candidates_checked_until_first_hit_or_exhaustion": (
            certificate_candidates_checked
        ),
        "first_hit_certificate_type_counts": {
            kind: sum(record["certificate_type"] == kind for record in records)
            for kind in ("I", "II")
        },
        "replaced_target_position_counts": {
            str(position): sum(
                record["reverse_two_tail_lift"]["replaced_target_position"]
                == position
                for record in records
            )
            for position in range(3)
        },
        "even_source_denominator_count": sum(
            source_denominator % 2 == 0
            for source_denominator in source_denominators
        ),
        "unresolved_core_prime_source_count": sum(
            source_denominator % 24 == 1 and spf[source_denominator] == source_denominator
            for source_denominator in source_denominators
        ),
        "maximum_first_hit_gap": max(
            (record["gap"] for record in records), default=None
        ),
        "records": records,
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
