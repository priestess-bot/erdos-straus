#!/usr/bin/env python3
"""Verify that three-term ceiling-FCT data are exactly external-source Type I rays.

For positive coefficients c0, c1, c2, put

    p0 = c0, p1 = c0*c1 - 1, p = c2*p1 - c0, 4*k = c1*c2 - 1.

When p is a core prime, the three FCT terms after division by k are

    4/p = 1/(k*p0) + 1/(k*p0*p1) + 1/(k*p1*p).

They yield the Type I certificate with gap c2 and divisor c0*k*p0.
Conversely every external-source Type I witness recovers these coefficients.

This is an algebraic equivalence and a finite implementation audit.  It does
not validate FCT's probabilistic independence assumptions or establish a
uniform source bound.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
RESULTS = ROOT / "reproductions" / "fct-type-i-equivalence-results.json"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "fct_type_i_short_certificate", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load short_certificate.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


@dataclass(frozen=True)
class FCTData:
    c0: int
    c1: int
    c2: int
    p0: int
    p1: int
    prime: int
    k: int
    denominators: tuple[int, int, int]


def fct_data(c0: int, c1: int, c2: int) -> FCTData | None:
    """Build the three-term FCT data when its final denominator scale is integral."""
    if c0 <= 0 or c1 <= 0 or c2 <= 0:
        return None
    scale = c1 * c2 - 1
    if scale <= 0 or scale % 4:
        return None
    p0 = c0
    p1 = c0 * c1 - 1
    prime = c2 * p1 - c0
    if p1 <= 0 or prime <= 0:
        return None
    k = scale // 4
    return FCTData(
        c0=c0,
        c1=c1,
        c2=c2,
        p0=p0,
        p1=p1,
        prime=prime,
        k=k,
        denominators=(k * p0, k * p0 * p1, k * p1 * prime),
    )


def certificate_from_fct(data: FCTData):
    """Recover the Type I certificate encoded by a three-term FCT."""
    certificate = short_certificate.GapCertificate(
        prime=data.prime,
        certificate_type="I",
        gap=data.c2,
        x=data.k * data.c0,
        divisor=data.c0 * data.k * data.c0,
        y=data.k * data.c0 * data.p1,
        z=data.k * data.p1 * data.prime,
    )
    return certificate if short_certificate.verify_certificate(certificate) else None


def fct_from_external_source(prime: int, source: int, gap: int) -> FCTData | None:
    """Recover FCT coefficients from one external-source Type I witness."""
    certificate = short_certificate.external_source_type_i_certificate(
        prime, source, gap
    )
    if certificate is None:
        return None
    if certificate.x % source:
        raise AssertionError("external-source witness lost the FCT scale")
    p1, remainder = divmod(prime + source, gap)
    if remainder:
        raise AssertionError("external-source witness lost its source divisor")
    c1, remainder = divmod(p1 + 1, source)
    if remainder:
        raise AssertionError("source quotient did not recover a FCT coefficient")
    data = fct_data(source, c1, gap)
    if data is None:
        raise AssertionError("external-source witness did not recover integral FCT data")
    if data.prime != prime or data.k != certificate.x // source:
        raise AssertionError("recovered FCT data do not match the source witness")
    if data.denominators != (certificate.x, certificate.y, certificate.z):
        raise AssertionError("FCT denominators do not match the Type I reconstruction")
    return data


def positive_divisors(value: int, trial_primes: list[int]) -> list[int]:
    factors: list[tuple[int, int]] = []
    remaining = value
    for prime in trial_primes:
        if prime * prime > remaining:
            break
        if remaining % prime:
            continue
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        factors.append((prime, exponent))
    if remaining > 1:
        factors.append((remaining, 1))
    result = [1]
    for prime, exponent in factors:
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return sorted(result)


def verify_fct_identity(data: FCTData) -> bool:
    first, second, third = data.denominators
    return Fraction(4, data.prime) == (
        Fraction(1, first) + Fraction(1, second) + Fraction(1, third)
    )


def run_audit(limit: int = 5_000, source_limit: int = 32) -> dict[str, object]:
    if limit < 73 or source_limit < 1:
        raise ValueError("limit must be at least 73 and source_limit must be positive")
    primes = [
        prime
        for prime in short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    trial_primes = short_certificate.primes_up_to(
        math.isqrt(limit + source_limit) + 1
    )
    witness_count = 0
    samples: list[dict[str, object]] = []
    for prime in primes:
        for source in range(1, source_limit + 1):
            for gap in positive_divisors(prime + source, trial_primes):
                data = fct_from_external_source(prime, source, gap)
                if data is None:
                    continue
                certificate = certificate_from_fct(data)
                if certificate is None or not verify_fct_identity(data):
                    raise AssertionError("FCT data failed exact certificate verification")
                witness_count += 1
                if len(samples) < 8:
                    samples.append(
                        {
                            "source_witness": {
                                "prime": prime,
                                "source": source,
                                "gap": gap,
                            },
                            "fct": asdict(data),
                            "certificate_divisor": certificate.divisor,
                        }
                    )
    return {
        "arithmetic": (
            "exact integer recurrences, exact external-source reconstruction, "
            "and fractions.Fraction verification"
        ),
        "scope_note": (
            "The audit verifies only the deterministic FCT/Type I equivalence "
            "inside a finite source window. It does not test a uniform source "
            "bound or validate the FCT heuristic probability model."
        ),
        "prime_limit": limit,
        "source_limit": source_limit,
        "core_prime_count": len(primes),
        "external_source_witness_count": witness_count,
        "sample_witnesses": samples,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5_000)
    parser.add_argument("--source-limit", type=int, default=32)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit, args.source_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
