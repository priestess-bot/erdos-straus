#!/usr/bin/env python3
"""Verify the exact p-minus-one lift normalization on stored witnesses."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-p-minus-one-scaled-source-descent-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-p-minus-one-scaled-source-normalization-1b-results.json"


def normalize_witness(prime: int, witness: dict[str, object]) -> dict[str, int]:
    """Recover the unique shift t from a p-divisible target first denominator."""
    source = prime - 1
    shift = int(witness["shift"])
    source_solution = [int(value) for value in witness["source_solution"]]
    target_solution = [int(value) for value in witness["target_solution"]]
    source_first = source_solution[0]
    target_first = target_solution[0]
    if source_first != source * (prime - shift) // 4:
        raise AssertionError("source first denominator violates p-minus-one normalization")
    if target_first % prime or target_first != prime * source_first // shift:
        raise AssertionError("target first denominator is not the required p-divisible lift")
    quotient = target_first // prime
    denominator = 4 * quotient + source
    numerator = source * prime
    if numerator % denominator or numerator // denominator != shift:
        raise AssertionError("p-divisible target first denominator did not recover shift")
    if (
        Fraction(4, source)
        != sum((Fraction(1, value) for value in source_solution), Fraction())
        or Fraction(4, prime)
        != sum((Fraction(1, value) for value in target_solution), Fraction())
    ):
        raise AssertionError("stored normalized lift identity failed")
    return {
        "prime": prime,
        "source_denominator": source,
        "shift": shift,
        "source_first_denominator": source_first,
        "target_first_denominator": target_first,
        "recovered_shift": numerator // denominator,
    }


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Normalize one retained witness for every p-minus-one-covered residual."""
    records = []
    for row in payload["records"]:
        witness = row["first_witness"]
        if witness is None:
            continue
        records.append(normalize_witness(int(row["prime"]), witness))
    return {
        "arithmetic": (
            "exact normalization A=(p-1)(p-t)/4 and inverse recovery "
            "t=(p-1)p/(4(z/p)+p-1) for each p-divisible target first term"
        ),
        "scope_note": (
            "The algebraic normalization is general; the listed witness "
            "collection remains the finite p-minus-one scaled-source audit."
        ),
        "prime_limit": payload["prime_limit"],
        "witness_count": len(records),
        "all_target_first_denominators_divisible_by_prime": all(
            record["target_first_denominator"] % record["prime"] == 0
            for record in records
        ),
        "all_shifts_recovered": all(
            record["shift"] == record["recovered_shift"] for record in records
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
