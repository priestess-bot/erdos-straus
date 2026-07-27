#!/usr/bin/env python3
"""Profile pure-new canonical releases after the 50m two-shift boundary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOUNDARY = (
    ROOT
    / "reproductions"
    / "type-ii-tail-deflation-p-minus-one-canonical-50m-s2-boundary.json"
)
DEFAULT_CLOSURE = (
    ROOT / "reproductions" / "type-ii-tail-deflation-p-minus-one-canonical-50m-results.json"
)
DEFAULT_OUTPUT = (
    ROOT
    / "reproductions"
    / "type-ii-tail-deflation-p-minus-one-pure-new-release-50m-results.json"
)


def factorization(value: int) -> list[dict[str, int]]:
    return [
        {"prime": int(prime), "exponent": int(exponent)}
        for prime, exponent in sorted(sympy.factorint(value).items())
    ]


def run_audit(
    boundary_path: Path = DEFAULT_BOUNDARY, closure_path: Path = DEFAULT_CLOSURE
) -> dict[str, object]:
    """Verify source-free one-prime releases for every two-shift residual."""
    boundary = json.loads(boundary_path.read_text(encoding="utf-8"))
    closure = json.loads(closure_path.read_text(encoding="utf-8"))
    if boundary["prime_limit"] != closure["prime_limit"]:
        raise ValueError("boundary and closure prime limits differ")
    if int(boundary["canonical_shift_cap"]) != 2:
        raise ValueError("boundary must be the two-shift audit")
    closure_records = {int(row["prime"]): row for row in closure["records"]}
    records = []
    for prime in [int(value) for value in boundary["unclosed_primes"]]:
        row = closure_records.get(prime)
        if row is None or row["witness"] is None:
            raise AssertionError("closure lacks a witness for a two-shift residual")
        witness = row["witness"]
        first_shift = int(witness["first_shift"])
        if first_shift <= 2:
            raise AssertionError("closure witness did not release after the base fan")
        h = int(witness["h"])
        h_factors = factorization(h)
        old_source_primes = set(sympy.factorint(prime + 4)) | set(
            sympy.factorint(prime + 8)
        )
        overlap = sorted(
            factor["prime"] for factor in h_factors if factor["prime"] in old_source_primes
        )
        new_multiplicity = sum(
            factor["exponent"]
            for factor in h_factors
            if factor["prime"] not in old_source_primes
        )
        records.append(
            {
                "prime": prime,
                "first_release_shift": first_shift,
                "h": h,
                "h_factorization": h_factors,
                "h_is_prime": bool(sympy.isprime(h)),
                "old_source_primes": sorted(int(value) for value in old_source_primes),
                "old_source_overlap": overlap,
                "new_multiplicity": new_multiplicity,
            }
        )
    pure_new = [
        record
        for record in records
        if record["h_is_prime"]
        and not record["old_source_overlap"]
        and record["new_multiplicity"] == 1
    ]
    return {
        "arithmetic": (
            "exact integer factorization of p+4, p+8, and the first later "
            "canonical-ray factor h; the stored Type II witnesses are reused "
            "only after matching their residual primes"
        ),
        "scope_note": (
            "A finite provenance profile for the two-shift strict-descent "
            "residual. It does not establish a universal one-new-factor selector."
        ),
        "prime_limit": boundary["prime_limit"],
        "base_shift_cap": boundary["canonical_shift_cap"],
        "release_shift_cap": closure["canonical_shift_cap"],
        "residual_count": len(records),
        "pure_new_one_prime_release_count": len(pure_new),
        "non_pure_new_primes": [
            record["prime"] for record in records if record not in pure_new
        ],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boundary", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--closure", type=Path, default=DEFAULT_CLOSURE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.boundary, args.closure)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
