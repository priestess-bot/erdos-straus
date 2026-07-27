#!/usr/bin/env python3
"""Cross-check high even-source overflow against quadratic external descents."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OVERFLOW = ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json"
DEFAULT_QUADRATIC = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-overflow-hybrid-split-1b-results.json"


def run_audit(overflow_payload: dict[str, object], quadratic_payload: dict[str, object]) -> dict[str, object]:
    """Partition stored H19 residuals by first-hit overflow and standard descent."""
    quadratic = {
        int(record["prime"]): record["quadratic_factor_external_source_descent"]
        for record in quadratic_payload["records"]
    }
    first_hit = {int(record["prime"]): int(record["minimum_overflow"]) for record in overflow_payload["records"]}
    if set(quadratic) != set(first_hit) | set(int(prime) for prime in overflow_payload["uncovered_primes"]):
        raise AssertionError("overflow and quadratic profiles cover different residual sets")
    high_overflow = sorted(prime for prime, value in first_hit.items() if value > 1)
    zero_overflow = sorted(prime for prime, value in first_hit.items() if value == 1)
    uncovered = sorted(int(prime) for prime in overflow_payload["uncovered_primes"])
    quadratic_misses = sorted(prime for prime, witness in quadratic.items() if witness is None)
    if any(quadratic[prime] is None for prime in high_overflow + uncovered):
        raise AssertionError("high-overflow or r-uncovered state lacks quadratic closure")
    if any(prime not in zero_overflow for prime in quadratic_misses):
        raise AssertionError("quadratic pressure miss lacks a zero-overflow first r hit")
    high_overflow_k = Counter(
        int(quadratic[prime]["k"])
        for prime in high_overflow
    )
    uncovered_k = Counter(
        int(quadratic[prime]["k"])
        for prime in uncovered
    )
    return {
        "arithmetic": (
            "exact join on the stored residual prime keys between the first-r-hit overflow "
            "profile and the complete quadratic external-source descent profile"
        ),
        "scope_note": (
            "A finite hybrid classification of the stored H19 residual profile. It does "
            "not prove an overflow/standard-source dichotomy beyond this range."
        ),
        "prime_limit": overflow_payload["prime_limit"],
        "h19_residual_count": overflow_payload["h19_residual_count"],
        "zero_overflow_first_hit_count": len(zero_overflow),
        "high_overflow_first_hit_count": len(high_overflow),
        "r_uncovered_count": len(uncovered),
        "quadratic_external_descent_miss_count": len(quadratic_misses),
        "all_high_overflow_have_quadratic_descent": True,
        "all_r_uncovered_have_quadratic_descent": True,
        "all_quadratic_misses_have_zero_overflow_first_hit": True,
        "high_overflow_quadratic_k_histogram": {
            str(k): count for k, count in sorted(high_overflow_k.items())
        },
        "maximum_high_overflow_quadratic_k": max(high_overflow_k, default=None),
        "r_uncovered_quadratic_k_histogram": {
            str(k): count for k, count in sorted(uncovered_k.items())
        },
        "maximum_r_uncovered_quadratic_k": max(uncovered_k, default=None),
        "quadratic_external_descent_misses": quadratic_misses,
        "high_overflow_primes": high_overflow,
        "r_uncovered_primes": uncovered,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--overflow", type=Path, default=DEFAULT_OVERFLOW)
    parser.add_argument("--quadratic", type=Path, default=DEFAULT_QUADRATIC)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.overflow.read_text(encoding="utf-8")),
        json.loads(args.quadratic.read_text(encoding="utf-8")),
    )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
