#!/usr/bin/env python3
"""Audit a dense core-prime interval for the two target terminal branches.

Every core prime in ``(lower_exclusive, upper]`` is first subjected to the
complete ordinary Type II ``p-1`` two-tail test.  Only its misses are searched
through every Type I normal form with ``m <= gap_cap`` and every strict
maximum-tail reverse lift, retaining the first even source.  An even source is
terminal by scaling the standard solution for 2.

The gap cap is explicit: this is a boundary test for the proposed finite
target-side box, not a proof of a uniform selector.
"""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
EVEN_SOURCE = ROOT / "reproductions" / "type_i_tail_reverse_even_source_closure.py"
DEFAULT_LOWER_EXCLUSIVE = 500_000_000
DEFAULT_UPPER = 600_000_000
DEFAULT_GAP_CAP = 215
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_module("dense_terminal_short_certificate", SHORT_CERTIFICATE)
even_source = load_module("dense_terminal_even_source", EVEN_SOURCE)


def run_audit(
    lower_exclusive: int = DEFAULT_LOWER_EXCLUSIVE,
    upper: int = DEFAULT_UPPER,
    gap_cap: int = DEFAULT_GAP_CAP,
) -> dict[str, object]:
    """Exhaust both stated branches on the requested dense interval."""
    if lower_exclusive < 1 or upper <= lower_exclusive:
        raise ValueError("require 1 <= lower_exclusive < upper")
    if gap_cap < 3 or gap_cap % 4 != 3:
        raise ValueError("gap_cap must be at least three and 3 modulo four")

    spf = short_certificate.smallest_prime_factors(upper)
    core_primes = [
        prime
        for prime in short_certificate.primes_up_to(upper)
        if prime > lower_exclusive and prime % 24 == 1
    ]
    ordinary_tail_hits = 0
    ordinary_gap_histogram: Counter[int] = Counter()
    fallback_records: list[dict[str, object]] = []
    even_source_misses: list[int] = []

    for prime in core_primes:
        tail = short_certificate.first_type_ii_tail_deflation_witness(prime, spf)
        if tail is not None:
            ordinary_tail_hits += 1
            ordinary_gap_histogram[tail.gap] += 1
            continue
        witness, forms, lifts = even_source.first_even_source_edge(prime, gap_cap)
        if witness is None:
            even_source_misses.append(prime)
            continue
        fallback_records.append(
            {
                "prime": prime,
                "type_i_even_witness": witness,
                "normal_forms_checked_until_first_even_source": forms,
                "strict_reverse_lifts_checked_until_first_even_source": lifts,
            }
        )

    fallback_gap_histogram = Counter(
        int(record["type_i_even_witness"]["gap"]) for record in fallback_records
    )
    return {
        "arithmetic": (
            "exact SPF factorization and complete ordinary Type II p-1-tail divisor "
            "residue tests on every core prime in the interval; for every ordinary-tail "
            "miss, exhaustive Type I normal forms through the stated gap cap and exact "
            "maximum-tail reverse-lift identity checks until the first even source"
        ),
        "scope_note": (
            "A dense finite target-side audit. The Type I fallback is explicitly bounded "
            "by gap_cap, so a closure is evidence for this box rather than a proof of the "
            "global mixed terminal lemma; a miss refutes only this bounded fallback box."
        ),
        "prime_interval": [lower_exclusive + 1, upper],
        "core_prime_count": len(core_primes),
        "ordinary_type_ii_tail_hit_count": ordinary_tail_hits,
        "ordinary_type_ii_tail_miss_count": len(fallback_records) + len(even_source_misses),
        "ordinary_minimum_gap_histogram": {
            str(gap): count for gap, count in sorted(ordinary_gap_histogram.items())
        },
        "type_i_gap_cap": gap_cap,
        "type_i_even_terminal_bridge_count": len(fallback_records),
        "type_i_first_even_source_gap_histogram": {
            str(gap): count for gap, count in sorted(fallback_gap_histogram.items())
        },
        "maximum_selected_type_i_gap": max(fallback_gap_histogram, default=None),
        "even_source_misses": even_source_misses,
        "type_i_even_terminal_bridge_records": fallback_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lower-exclusive", type=int, default=DEFAULT_LOWER_EXCLUSIVE)
    parser.add_argument("--upper", type=int, default=DEFAULT_UPPER)
    parser.add_argument("--gap-cap", type=int, default=DEFAULT_GAP_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.lower_exclusive, args.upper, args.gap_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "type_i_even_terminal_bridge_records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
