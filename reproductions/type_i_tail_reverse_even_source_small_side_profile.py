#!/usr/bin/env python3
"""Classify stored even bridges by the small-side ordinary-divisor condition.

For each stored Type I normal bridge put L=2K and reduce E/L=a/b.  A pair
with a<b is a small-side bridge: its size condition is automatic for a core
prime, so only the divisor residue and parity conditions remain.  For every
record whose selected pair is large-side, this script exhausts all coprime
ordinary divisor pairs of the same L to determine whether an alternative
small-side bridge exists in that same normal-form state.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-ratio-pair-audit-500m-results.json"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-tail-reverse-even-source-small-side-profile-500m-results.json"
)


def factorization_record(value: int) -> list[list[int]]:
    """Return a deterministic prime-exponent record for a positive integer."""
    return [
        [int(prime), int(exponent)]
        for prime, exponent in sorted(sympy.factorint(value).items())
    ]


def small_side_pairs(L: int, R: int) -> list[dict[str, int]]:
    """Enumerate every admissible small-side bridge pair for one (L,R) state."""
    if L <= 0 or R < 3 or R % 2 != 1 or math.gcd(L, R) != 1:
        raise ValueError("invalid ordinary-divisor bridge state")
    divisors = [int(value) for value in sympy.divisors(L)]
    pairs: list[dict[str, int]] = []
    for b in divisors:
        for a in divisors:
            if a >= b or math.gcd(a, b) != 1 or (a - 2 * b) % R:
                continue
            E = L * a // b
            if E % 2:
                continue
            if E > 2 * L - 2 * R:
                raise AssertionError("small-side pair failed its automatic bridge bounds")
            if (E - 2 * L) % R:
                raise AssertionError("ordinary divisor pair did not reconstruct E=2L mod R")
            source = (2 * L - E) // R
            if (2 * L - E) % R or source < 2 or source % 2:
                raise AssertionError("small-side pair did not reconstruct a strict even source")
            pairs.append({"E": E, "a": a, "b": b, "source_denominator": source})
    return sorted(pairs, key=lambda pair: (pair["E"], pair["a"], pair["b"]))


def classify_large_side(record: dict[str, int]) -> dict[str, object]:
    """Exhaust the unselected small-side pairs in one large-side bridge state."""
    L, R = int(record["L"]), int(record["R"])
    pairs = small_side_pairs(L, R)
    return {
        "prime": int(record["prime"]),
        "R": R,
        "L": L,
        "selected_pair": {key: int(record[key]) for key in ("E", "a", "b")},
        "factorization": factorization_record(L),
        "small_side_pair_count": len(pairs),
        "canonical_small_side_pair": pairs[0] if pairs else None,
    }


def run_profile(ratio_audit: dict[str, object]) -> dict[str, object]:
    """Rebuild the complete small-side split of the stored 500M bridge data."""
    records = [{key: int(value) for key, value in record.items()} for record in ratio_audit["records"]]
    selected_small = []
    selected_large = []
    for record in records:
        L, R, E, a, b = (record[key] for key in ("L", "R", "E", "a", "b"))
        if math.gcd(L, R) != 1 or math.gcd(a, b) != 1 or L % a or L % b:
            raise AssertionError("stored ordinary-divisor state failed reconstruction")
        if (a - 2 * b) % R or E != L * a // b or E % 2:
            raise AssertionError("stored ratio-two bridge failed reconstruction")
        if a < b:
            if not E < L or E > 2 * L - 2 * R:
                raise AssertionError("small-side bridge did not have automatic size")
            selected_small.append(record)
        elif a > b:
            if not L < E <= 2 * L - 2 * R:
                raise AssertionError("large-side bridge did not have the expected size")
            selected_large.append(classify_large_side(record))
        else:
            raise AssertionError("a coprime ratio-two bridge cannot have a=b")

    large_with_small = [record for record in selected_large if record["canonical_small_side_pair"]]
    large_only = [record for record in selected_large if not record["canonical_small_side_pair"]]
    examples = {
        "selected_small_side": selected_small[0],
        "large_side_with_small_alternative": large_with_small[0],
        "large_side_only": large_only[0],
    }
    return {
        "arithmetic": (
            "reduce every stored bridge E/L=a/b with L=2K; a<b makes the bridge size "
            "automatic. For each selected a>b state, fully enumerate all coprime divisor pairs "
            "of the same L satisfying a=2b mod R and retain its even small-side bridges."
        ),
        "scope_note": (
            "This is a complete finite profile of the stored 500M terminal bridges. It neither "
            "selects a Type I normal form for an arbitrary core prime nor proves a global selector."
        ),
        "input_artifact": INPUT.name,
        "prime_limit": int(ratio_audit["prime_limit"]),
        "record_count": len(records),
        "selected_small_side_count": len(selected_small),
        "selected_large_side_count": len(selected_large),
        "large_side_with_small_alternative_count": len(large_with_small),
        "large_side_only_count": len(large_only),
        "small_side_available_count": len(selected_small) + len(large_with_small),
        "all_selected_small_side_sizes_automatic": True,
        "examples": examples,
        "large_side_records": selected_large,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_profile(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "large_side_records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
