#!/usr/bin/env python3
"""Profile Type II tail deflation and close its core misses by p-minus-one lifts."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import sys
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
SHORT_CERTIFICATE = ROOT / "reproductions" / "short_certificate.py"
P_MINUS_ONE_SCRIPT = ROOT / "reproductions" / "type_ii_h19_p_minus_one_scaled_source_descent.py"
DEFAULT_LIMIT = 100_000
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-tail-deflation-p-minus-one-core-hybrid-100k-results.json"


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


short_certificate = load_script("tail_deflation_core_hybrid_short", SHORT_CERTIFICATE)
p_minus_one = load_script("tail_deflation_core_hybrid_p_minus_one", P_MINUS_ONE_SCRIPT)


def run_audit(limit: int = DEFAULT_LIMIT) -> dict[str, object]:
    """Audit all core primes with the exact divisor-indexed Type II selector."""
    if limit < 73:
        raise ValueError("limit must be at least 73")
    spf = short_certificate.smallest_prime_factors(limit)
    core_primes = [int(prime) for prime in sympy.primerange(2, limit + 1) if prime % 24 == 1]
    deflations = {}
    for prime in core_primes:
        witness = short_certificate.first_type_ii_tail_deflation_witness(prime, spf)
        if witness is not None:
            deflations[prime] = witness
    misses = [prime for prime in core_primes if prime not in deflations]

    p_minus_one_records = []
    candidate_count = 0
    tail_divisor_test_count = 0
    hit_candidate_count = 0
    for prime in misses:
        result = p_minus_one.audit_primes([prime])
        record = result["records"][0]
        p_minus_one_records.append(record)
        candidate_count += int(result["unique_scaled_source_candidate_count"])
        tail_divisor_test_count += int(result["tail_divisor_test_count"])
        hit_candidate_count += int(result["hit_candidate_count"])
    unclosed = [
        int(record["prime"])
        for record in p_minus_one_records
        if record["first_witness"] is None
    ]
    histogram = Counter(witness.gap for witness in deflations.values())
    return {
        "arithmetic": (
            "complete divisor-indexed Type II tail-deflation scan over p-1, "
            "then complete b=2,4 p-minus-one scaled-source tail enumeration "
            "on exactly the deflation misses"
        ),
        "scope_note": (
            "A finite core-range profile and hybrid closure. It does not prove "
            "a universal tail-deflation or p-minus-one selector."
        ),
        "prime_limit": limit,
        "core_prime_count": len(core_primes),
        "tail_deflation_strict_lift_count": len(deflations),
        "tail_deflation_gap_histogram": {
            str(gap): count for gap, count in sorted(histogram.items())
        },
        "tail_deflation_misses": misses,
        "p_minus_one_residual_count": len(misses),
        "p_minus_one_scaled_source_candidate_count": candidate_count,
        "p_minus_one_tail_divisor_test_count": tail_divisor_test_count,
        "p_minus_one_hit_candidate_count": hit_candidate_count,
        "p_minus_one_strict_lift_count": len(misses) - len(unclosed),
        "unclosed_primes": unclosed,
        "tail_deflation_miss_records": p_minus_one_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
