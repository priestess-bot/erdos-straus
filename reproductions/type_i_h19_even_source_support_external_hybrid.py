#!/usr/bin/env python3
"""Replace the H19 support-four bridge boundary by zero-offset external descent."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUPPORT = ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json"
OFFSET_PROFILE = ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_offset_profile.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-even-source-support-external-hybrid-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


offset_profile = load_module("h19_even_support_external_offset", OFFSET_PROFILE)


def run_audit(support: dict[str, object]) -> dict[str, object]:
    """Rebuild a zero-offset external even source for every support-four boundary point."""
    boundary = [
        int(record["prime"])
        for record in support["records"]
        if int(record["selected_edge"]["E_prime_support_count"]) >= 4
    ]
    if boundary != [48_605_881]:
        raise AssertionError("H19 support-four boundary did not reconstruct")
    spf = offset_profile.targeted_descent.TrialSmallestFactors(max(boundary))
    records: list[dict[str, object]] = []
    for prime in boundary:
        candidates = 0
        witness = None
        # The first zero-offset certificate may have an odd source.  Enumerate
        # every compatible k at shift 1, retaining the first terminal even one.
        for k in offset_profile.short_certificate.positive_divisors_from_spf((prime - 1) // 4, spf):
            candidates += 1
            candidate = offset_profile.short_certificate.shifted_quadratic_factor_external_source_descent_witness(
                prime, k, 1, spf
            )
            if candidate is not None and candidate.source_denominator % 2 == 0:
                witness = candidate
                break
        if witness is None:
            raise AssertionError("support-four boundary had no zero-offset external witness")
        rebuilt = offset_profile.serialize_witness(witness, 1, candidates)
        records.append({"prime": prime, "zero_offset_external_descent": rebuilt})
    return {
        "arithmetic": (
            "take the exact H19 support-four even-bridge boundary; enumerate every compatible "
            "zero-offset quadratic divisor state and verify the first strict external source and "
            "both Egyptian-fraction identities exactly"
        ),
        "scope_note": (
            "A finite hybrid replacement for one support-four bridge factor. It does not prove "
            "a global support-three bridge rule or a universal external-source rule."
        ),
        "prime_limit": support["prime_limit"],
        "h19_source_free_count": support["h19_source_free_count"],
        "support_at_most_three_even_bridge_count": int(support["captured_count"]) - len(boundary),
        "zero_offset_external_boundary_count": len(records),
        "unclosed_primes": [],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--support", type=Path, default=SUPPORT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.support.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
