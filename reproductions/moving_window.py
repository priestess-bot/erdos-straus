#!/usr/bin/env python3
"""Exact finite audit of the fixed-gap Type II moving window.

For p = 24*t+1 and j >= 1, the moving split is gap A_j=4*j-1 and
X_j=(p+A_j)/4. This script tests the exact Bradford Type II divisor condition
at j=1,...,J. It reports finite evidence only; no output proves a uniform J.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "moving-window-results.json"
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


def run_experiment(limit: int, window: int) -> dict[str, object]:
    if limit < 73 or window < 1:
        raise ValueError("limit must be at least 73 and window must be positive")
    max_x = (limit + 4 * window - 1) // 4 + 1
    spf = short_certificate.smallest_prime_factors(max_x)
    core_primes = [
        prime for prime in short_certificate.primes_up_to(limit) if prime % 24 == 1
    ]
    missing: list[int] = []
    record_holders: list[dict[str, int]] = []
    largest_first_j = 0

    for prime in core_primes:
        for j in range(1, window + 1):
            certificate = short_certificate.type_ii_residue_certificate(
                prime, 4 * j - 1, spf
            )
            if certificate is None:
                continue
            if j > largest_first_j:
                largest_first_j = j
                record_holders.append(
                    {
                        "prime": prime,
                        "j": j,
                        "gap": certificate.gap,
                        "divisor": certificate.divisor,
                        "x": certificate.x,
                    }
                )
            break
        else:
            missing.append(prime)

    return {
        "arithmetic": "exact divisor enumeration plus fractions.Fraction certificate verification",
        "scope_note": (
            "A finite fixed-window Type II audit. Complete coverage here is not a proof "
            "that any fixed window covers all core primes."
        ),
        "prime_limit": limit,
        "window_j": window,
        "gap_bound": 4 * window - 1,
        "core_prime_count": len(core_primes),
        "captured_count": len(core_primes) - len(missing),
        "missing": missing,
        "largest_first_j": largest_first_j if record_holders else None,
        "record_holders": record_holders,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--window", type=int, default=20)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_experiment(args.limit, args.window)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
