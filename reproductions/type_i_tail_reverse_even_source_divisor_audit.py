#!/usr/bin/env python3
"""Verify the parity-normalized divisor form of stored even-source reverse edges."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-closure-500m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-divisor-audit-500m-results.json"


def run_audit(closure: dict[str, object]) -> dict[str, object]:
    records: list[dict[str, int]] = []
    for record in closure["records"]:
        prime = int(record["prime"])
        gap = int(record["gap"])
        A, B, C = (int(value) for value in record["normal_form"])
        R = (4 * B * B * C + 1) // gap
        H = A * R - B
        K = B * C * H
        lift = record["reverse_two_tail_lift"]
        bridge_divisor = int(lift["bridge_divisor"])
        if bridge_divisor % (prime * prime):
            raise AssertionError("bridge divisor did not have the p^2 factor")
        E = bridge_divisor // (prime * prime)
        source = int(lift["source_denominator"])
        source_term = int(lift["source_term"])
        if 4 * K != prime * R + 1 or R % 2 != 1:
            raise AssertionError("normal form did not reconstruct odd R")
        if E % 2 != 0 or source % 2 != 0:
            raise AssertionError("stored even source did not correspond to an even E")
        if (4 * K - E) % R or source != (4 * K - E) // R:
            raise AssertionError("E did not reconstruct the source")
        if (4 * K * K) % E:
            raise AssertionError("E did not divide 4K^2")
        if (source * K) % E or source_term != source * K // E:
            raise AssertionError("E did not reconstruct the source term")
        if E > 4 * K - 2 * R:
            raise AssertionError("source did not satisfy n>=2")
        # E>=2 also makes n<p because pR=4K-1.
        if not 2 <= source < prime:
            raise AssertionError("even-selector strict range did not reconstruct")
        records.append(
            {
                "prime": prime,
                "gap": gap,
                "R": R,
                "K": K,
                "E": E,
                "source_denominator": source,
            }
        )
    return {
        "arithmetic": (
            "for every stored even-source reverse edge, reconstruct R,K,E from its Type I "
            "normal form and verify R odd, E even, E|4K^2, E=4K-nR, and a=nK/E"
        ),
        "scope_note": (
            "A finite verification of an algebraic equivalence on the 500M closure records; "
            "the parity-selector lemma itself is symbolic and does not assert a global selector."
        ),
        "prime_limit": closure["prime_limit"],
        "even_source_record_count": len(records),
        "all_reconstructed_R_odd": True,
        "all_reconstructed_E_even": True,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
