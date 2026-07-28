#!/usr/bin/env python3
"""Exhaust the mixed terminal dichotomy without a Type I gap cap up to 10M."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

import sympy


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
TARGET_SELECTOR = ROOT / "reproductions" / "type_i_target_divisor_terminal_selector.py"
DEFAULT_LIMIT = 10_000_000
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-mixed-terminal-full-gap-audit-10m-results.json"
)


def load_module(name: str, path: Path):
    """Load an established exact arithmetic module."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("full_gap_short_certificate", SHORT_CERTIFICATE)
target_selector = load_module("full_gap_target_selector", TARGET_SELECTOR)


def square_divisors(value: int) -> list[int]:
    """Return all positive divisors of value squared exactly."""
    if value <= 0:
        raise ValueError("square divisor input must be positive")
    factors = sympy.factorint(value)
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * int(prime) ** power
            for divisor in divisors
            for power in range(2 * int(exponent) + 1)
        ]
    return sorted(divisors)


def four_k_squared_divisors(K: int) -> list[int]:
    """Return all positive divisors of 4 times K squared exactly."""
    if K <= 0:
        raise ValueError("K must be positive")
    factors = sympy.factorint(4 * K * K)
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * int(prime) ** power
            for divisor in divisors
            for power in range(int(exponent) + 1)
        ]
    return sorted(divisors)


def ordinary_tail_summary(witness: object) -> dict[str, int]:
    """Serialize the exact ordinary two-tail certificate summary."""
    certificate = witness.certificate
    return {
        "gap": int(certificate.gap),
        "source_denominator": int(witness.source_denominator),
    }


def first_even_bridge_without_gap_cap(
    prime: int, spf: object
) -> tuple[dict[str, object] | None, int, int]:
    """Exhaust every Type I gap and target/bridge divisor until the first bridge."""
    target_candidates = 0
    bridge_candidates = 0
    for gap in range(3, prime - 1, 4):
        x = (prime + gap) // 4
        if 4 * x != prime + gap:
            raise AssertionError("gap parameter did not reconstruct x")
        for target_divisor in short_certificate.divisors_of_square(x, spf):
            if (4 * target_divisor + 1) % gap:
                continue
            target_candidates += 1
            R = (4 * target_divisor + 1) // gap
            if R < 3 or R % 4 != 3:
                continue
            K = x * R - target_divisor
            if K <= 0 or 4 * K != prime * R + 1:
                raise AssertionError("target divisor did not reconstruct K")
            for bridge_factor in four_k_squared_divisors(K):
                bridge_candidates += 1
                witness = target_selector.terminal_witness_from_target_divisors(
                    prime,
                    gap,
                    target_divisor,
                    bridge_factor,
                )
                if witness is not None:
                    return witness, target_candidates, bridge_candidates
    return None, target_candidates, bridge_candidates


def run_audit(limit: int = DEFAULT_LIMIT) -> dict[str, object]:
    """Run the exact finite, no-gap-cap mixed-terminal audit."""
    if limit < 73:
        raise ValueError("limit must include the first core prime")
    spf = short_certificate.smallest_prime_factors(limit)
    core_primes = [
        prime
        for prime in short_certificate.primes_up_to(limit)
        if prime % 24 == 1
    ]
    ordinary_records: list[dict[str, object]] = []
    fallback_records: list[dict[str, object]] = []
    ordinary_miss_primes: list[int] = []
    target_candidates_total = 0
    bridge_candidates_total = 0

    for prime in core_primes:
        ordinary = short_certificate.first_type_ii_tail_deflation_witness(prime, spf)
        if ordinary is not None:
            ordinary_records.append(
                {
                    "prime": prime,
                    "ordinary_type_ii": ordinary_tail_summary(ordinary),
                }
            )
            continue

        ordinary_miss_primes.append(prime)
        witness, target_candidates, bridge_candidates = (
            first_even_bridge_without_gap_cap(prime, spf)
        )
        target_candidates_total += target_candidates
        bridge_candidates_total += bridge_candidates
        if witness is None:
            continue
        fallback_records.append(
            {
                "prime": prime,
                "type_i_even_terminal": target_selector.serialize_witness(witness),
                "target_divisor_candidates_checked": target_candidates,
                "bridge_divisor_candidates_checked": bridge_candidates,
            }
        )

    fallback_by_prime = {int(record["prime"]): record for record in fallback_records}
    misses = [
        prime for prime in ordinary_miss_primes if prime not in fallback_by_prime
    ]
    selected_gaps = [
        int(record["type_i_even_terminal"]["gap"])
        for record in fallback_records
    ]
    if set(ordinary_miss_primes) != set(fallback_by_prime) | set(misses):
        raise AssertionError("ordinary-tail misses did not partition")
    if len(ordinary_records) + len(ordinary_miss_primes) != len(core_primes):
        raise AssertionError("core-prime branch counts did not partition")

    return {
        "arithmetic": (
            "for every core prime p<=limit, exhaust all ordinary Type II p-1 two-tail "
            "divisors; for each miss, exhaust every m=3 (mod 4) with 3<=m<=p-2, "
            "every target divisor e|x^2 with 4e= -1 (mod m), and every E|4K^2 "
            "until an exact even terminal bridge is reconstructed"
        ),
        "scope_note": (
            "This is a finite no-gap-cap audit. It proves the stated dichotomy only "
            "for the selected limit; it does not give a uniform gap bound or a global "
            "mixed terminal selector."
        ),
        "prime_limit": limit,
        "core_prime_count": len(core_primes),
        "ordinary_type_ii_tail_certificate_count": len(ordinary_records),
        "ordinary_type_ii_tail_miss_count": len(ordinary_miss_primes),
        "type_i_even_terminal_bridge_count": len(fallback_records),
        "unclosed_primes": misses,
        "maximum_selected_type_i_gap": max(selected_gaps, default=None),
        "target_divisor_candidates_checked": target_candidates_total,
        "bridge_divisor_candidates_checked": bridge_candidates_total,
        "ordinary_tail_gap_histogram": {
            str(gap): count
            for gap, count in sorted(
                Counter(
                    int(record["ordinary_type_ii"]["gap"])
                    for record in ordinary_records
                ).items()
            )
        },
        "ordinary_tail_miss_primes": ordinary_miss_primes,
        "type_i_even_terminal_records": fallback_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in payload.items()
                if key
                not in {
                    "ordinary_tail_gap_histogram",
                    "ordinary_tail_miss_primes",
                    "type_i_even_terminal_records",
                }
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
