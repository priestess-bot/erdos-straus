#!/usr/bin/env python3
"""Verify the ordinary-divisor ratio-two form of the 500M even bridges."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-divisor-audit-500m-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-ratio-pair-audit-500m-results.json"


def run_audit(divisor_audit: dict[str, object]) -> dict[str, object]:
    records: list[dict[str, int]] = []
    for record in divisor_audit["records"]:
        R = int(record["R"])
        K = int(record["K"])
        E = int(record["E"])
        L = 2 * K
        g = math.gcd(E, L)
        a = E // g
        b = L // g
        if L % a or L % b or math.gcd(a, b) != 1:
            raise AssertionError("E/L did not reduce to coprime ordinary divisors of L")
        if (a - 2 * b) % R:
            raise AssertionError("ratio-two ordinary divisor congruence failed")
        if E != L * a // b or E % 2 or E > 2 * L - 2 * R:
            raise AssertionError("ordinary divisor pair did not reconstruct an admissible E")
        records.append(
            {
                "prime": int(record["prime"]),
                "R": R,
                "L": L,
                "E": E,
                "a": a,
                "b": b,
            }
        )
    return {
        "arithmetic": (
            "for every stored even bridge, put L=2K, reduce E/L=a/b, and verify that "
            "coprime a,b divide L, a=2b (mod R), and E=L*a/b satisfies the parity and size bounds"
        ),
        "scope_note": (
            "Finite verification of the symbolic ratio-two divisor-pair equivalence on the "
            "500M even-source records; it is not a global pair-selection theorem."
        ),
        "prime_limit": divisor_audit["prime_limit"],
        "record_count": len(records),
        "all_pairs_coprime": True,
        "all_pairs_hit_ratio_two_mod_R": True,
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
