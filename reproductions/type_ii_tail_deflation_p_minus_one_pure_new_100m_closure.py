#!/usr/bin/env python3
"""Close 100m strict-descent residuals by state-dependent pure-new rays."""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import importlib.util
import json
import sys
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / "reproductions" / "type-ii-tail-deflation-p-minus-one-100m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-ii-tail-deflation-p-minus-one-pure-new-100m-results.json"
)
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"


def load_short_certificate():
    spec = importlib.util.spec_from_file_location(
        "tail_deflation_p_minus_one_pure_new_100m", SHORT_CERTIFICATE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SHORT_CERTIFICATE.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_short_certificate()


def canonical_pair(shift: int) -> tuple[int, int]:
    """Return the unique a,c with shift=a^2*c and c squarefree."""
    if shift < 1:
        raise ValueError("shift must be positive")
    remaining = shift
    square_root = 1
    factor = 2
    while factor * factor <= remaining:
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        square_root *= factor ** (exponent // 2)
        factor = 3 if factor == 2 else factor + 2
    return square_root, shift // (square_root * square_root)


@lru_cache(maxsize=None)
def factorization(value: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (int(prime), int(exponent))
        for prime, exponent in sorted(sympy.factorint(value).items())
    )


def factorization_record(value: int) -> list[dict[str, int]]:
    return [
        {"prime": prime, "exponent": exponent}
        for prime, exponent in factorization(value)
    ]


def witnesses_at_shift(prime: int, shift: int) -> list[dict[str, object]]:
    """Return every valid canonical ray witness at a prescribed shift."""
    a, c = canonical_pair(shift)
    modulus = 4 * a * c
    witnesses = []
    for h in sympy.divisors(prime + 4 * shift):
        if h <= 1 or (h + 1) % modulus:
            continue
        certificate = short_certificate.type_ii_raw_ray_certificate(
            prime, a, c, (h + 1) // modulus
        )
        if certificate is None:
            continue
        witnesses.append(
            {
                "shift": shift,
                "a": a,
                "c": c,
                "h": int(h),
                "h_factorization": factorization_record(int(h)),
                "gap": certificate.gap,
                "divisor": certificate.divisor,
            }
        )
    return witnesses


def pure_new(witness: dict[str, object], old_source_primes: set[int]) -> bool:
    factors = witness["h_factorization"]
    assert isinstance(factors, list)
    return (
        sum(int(row["exponent"]) for row in factors) == 1
        and all(int(row["prime"]) not in old_source_primes for row in factors)
    )


def run_audit(
    input_path: Path = DEFAULT_INPUT,
    base_shift_cap: int = 2,
    release_shift_cap: int = 48,
) -> dict[str, object]:
    """Find base certificates or later pure-new one-prime releases."""
    if base_shift_cap != 2 or release_shift_cap <= base_shift_cap:
        raise ValueError("require the two-shift base and a larger release cap")
    input_payload = json.loads(input_path.read_text(encoding="utf-8"))
    primes = [int(prime) for prime in input_payload["uncovered_primes"]]
    records = []
    for prime in primes:
        old_source_primes = set(prime_factor for prime_factor, _ in factorization(prime + 4))
        old_source_primes.update(
            prime_factor for prime_factor, _ in factorization(prime + 8)
        )
        base_witness = next(
            (
                witness
                for shift in range(1, base_shift_cap + 1)
                for witness in witnesses_at_shift(prime, shift)
            ),
            None,
        )
        first_later_shift = None
        least_h_first_later = None
        first_pure_new = None
        if base_witness is None:
            for shift in range(base_shift_cap + 1, release_shift_cap + 1):
                witnesses = witnesses_at_shift(prime, shift)
                if first_later_shift is None and witnesses:
                    first_later_shift = shift
                    least_h_first_later = witnesses[0]
                pure = next(
                    (
                        witness
                        for witness in witnesses
                        if pure_new(witness, old_source_primes)
                    ),
                    None,
                )
                if pure is not None:
                    first_pure_new = pure
                    break
        records.append(
            {
                "prime": prime,
                "old_source_primes": sorted(old_source_primes),
                "base_witness": base_witness,
                "first_later_shift": first_later_shift,
                "least_h_first_later_witness": least_h_first_later,
                "first_pure_new_witness": first_pure_new,
            }
        )
    base_count = sum(record["base_witness"] is not None for record in records)
    pure_records = [
        record for record in records if record["first_pure_new_witness"] is not None
    ]
    first_any_multi = [
        record
        for record in pure_records
        if record["least_h_first_later_witness"] is not None
        and not pure_new(
            record["least_h_first_later_witness"], set(record["old_source_primes"])
        )
    ]
    pure_histogram = Counter(
        int(record["first_pure_new_witness"]["shift"]) for record in pure_records
    )
    strict_descent_count = int(input_payload["combined_strict_lift_count"])
    return {
        "arithmetic": (
            "complete exact factorization of p+4s, all canonical-ray divisor "
            "checks through the stated cap, and reconstructed Type II "
            "certificate verification"
        ),
        "scope_note": (
            "A finite state-dependent pure-new release closure. It neither "
            "proves a universal release-depth bound nor turns direct "
            "certificates into strict descents."
        ),
        "input_artifact": input_path.name,
        "prime_limit": input_payload["prime_limit"],
        "core_prime_count": input_payload["core_prime_count"],
        "strict_descent_count": strict_descent_count,
        "base_shift_cap": base_shift_cap,
        "release_shift_cap": release_shift_cap,
        "strict_descent_residual_count": len(records),
        "base_short_certificate_count": base_count,
        "later_pure_new_one_prime_count": len(pure_records),
        "least_h_first_later_multi_new_count": len(first_any_multi),
        "later_pure_new_shift_histogram": {
            str(shift): count for shift, count in sorted(pure_histogram.items())
        },
        "unclosed_primes": [
            record["prime"]
            for record in records
            if record["base_witness"] is None
            and record["first_pure_new_witness"] is None
        ],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--base-shift-cap", type=int, default=2)
    parser.add_argument("--release-shift-cap", type=int, default=48)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.input, args.base_shift_cap, args.release_shift_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
