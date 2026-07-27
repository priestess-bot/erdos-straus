#!/usr/bin/env python3
"""Audit the exact source-congruence modulus for an even Type I bridge factor."""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORT_SHIFT = ROOT / "reproductions" / "type-i-short-shift-low-e-b7-profile-50m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-source-square-modulus-audit-results.json"


def factor_by_trial_division(value: int) -> dict[int, int]:
    if value < 1:
        raise ValueError("value must be positive")
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def source_square_modulus(E: int) -> int:
    """Return the least positive L such that E | n^2/gcd(E, 4) iff L | n for even n."""
    if E < 2 or E % 2:
        raise ValueError("E must be a positive even integer")
    modulus = 1
    for prime, exponent in factor_by_trial_division(E).items():
        extra = min(exponent, 2) if prime == 2 else 0
        required = (exponent + extra + 1) // 2
        modulus *= prime**required
    return modulus


def source_square_allowed(source: int, E: int) -> bool:
    """Decide the normalized source-square condition using its exact modulus."""
    return source >= 2 and source % 2 == 0 and source % source_square_modulus(E) == 0


def direct_source_square_allowed(source: int, E: int) -> bool:
    """Direct definition retained only as an audit oracle."""
    return source >= 2 and source % 2 == 0 and (source * source // math.gcd(E, 4)) % E == 0


def run_audit(
    short_shift_path: Path = SHORT_SHIFT,
    E_limit: int = 2_000,
    source_limit: int = 2_000,
) -> dict[str, object]:
    """Cross-check the theorem exhaustively in a box and on the fifty-million witnesses."""
    if E_limit < 2 or source_limit < 2:
        raise ValueError("audit limits must be at least 2")
    checked_pairs = 0
    for E in range(2, E_limit + 1, 2):
        for source in range(2, source_limit + 1, 2):
            direct = direct_source_square_allowed(source, E)
            modular = source_square_allowed(source, E)
            if direct != modular:
                raise AssertionError(f"source-square modulus mismatch for E={E}, n={source}")
            checked_pairs += 1

    short_shift = json.loads(short_shift_path.read_text(encoding="utf-8"))
    witness_records = [record for record in short_shift["records"] if record["witness"] is not None]
    for record in witness_records:
        prime = int(record["prime"])
        witness = record["witness"]
        shift = int(witness["shift"])
        E = int(witness["E"])
        source = prime - shift
        if (E - 1) % shift or source % source_square_modulus(E):
            raise AssertionError(f"short-shift witness failed source-congruence reduction for {prime}")
    return {
        "arithmetic": (
            "for even E=2^a product q^e define Lambda(E) by the least source valuations forced by "
            "E|n^2/gcd(E,4); exhaustively compare Lambda(E)|n with the direct condition, then verify "
            "the reduction on each stored fifty-million dynamic short-shift witness"
        ),
        "scope_note": (
            "This verifies an exact equivalence for the source-square condition only. It does not ensure the "
            "remaining divisor-pair residue condition for a Type I certificate."
        ),
        "E_limit": E_limit,
        "source_limit": source_limit,
        "checked_even_pairs": checked_pairs,
        "short_shift_prime_limit": short_shift["prime_limit"],
        "short_shift_witness_count": len(witness_records),
        "short_shift_modulus_histogram": dict(
            sorted(
                Counter(str(source_square_modulus(int(record["witness"]["E"]))) for record in witness_records).items(),
                key=lambda item: int(item[0]),
            )
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--short-shift", type=Path, default=SHORT_SHIFT)
    parser.add_argument("--E-limit", type=int, default=2_000)
    parser.add_argument("--source-limit", type=int, default=2_000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = run_audit(args.short_shift, args.E_limit, args.source_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
